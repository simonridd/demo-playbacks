"""One-presentation packaging adapter. Reuses an already published IPI shell/player.
Does not reimplement navigation or claim a native Node source-validation run.
Only audience markup is accepted. No private source, notes or credentials are read.
"""
from pathlib import Path
import sys,re,json,hashlib,html
root=Path(sys.argv[1]); payload=json.loads(Path(sys.argv[2]).read_text());out=Path(sys.argv[3])
raw=(root/payload['templatePath']).read_bytes()
assert hashlib.sha256(raw).hexdigest()==payload['templateSha256'],'Pinned audience template changed'
s=raw.decode('utf-8');esc=html.escape
native_style=re.search(r'<style>(.*?)</style>',s,re.S).group(1)
native_script=re.search(r'<script>(.*?)</script>',s,re.S).group(1)
def replace(pattern,replacement,count=1):
    global s
    s,n=re.subn(pattern,lambda m:replacement,s,count=count,flags=re.S)
    assert n==count,('Unexpected template shape',pattern,n)
replace(r'<title>.*?</title>','<title>'+esc(payload['title'])+' | Presentation</title>')
replace(r'<meta name="description" content="[^"]*">','<meta name="description" content="'+esc(payload['description'])+'">\n<meta name="robots" content="noindex, nofollow">')
replace(r'<body[^>]*>','<body data-presentation="'+esc(payload['id'])+'" data-default-view="slides">')
replace(r'<main\b[^>]*>.*?</main>','<main class="deck" id="main" tabindex="-1"><div class="canvas-space"><div class="slides-canvas">\n'+payload['sections']+'\n</div></div></main>')
replace(r'<nav\b[^>]*class="nav"[^>]*>.*?</nav>','<nav class="nav" aria-label="Presentation sections">'+payload['navigation']+'</nav>')
replace(r'<div class="route-tools">.*?</div>','<div class="route-tools"></div>')
replace(r'<span class="brand-title">.*?</span>','<span class="brand-title">Thirdfort · Digital support discovery</span>')
replace(r'(<a class="brands"[^>]*href=")[^"]*(")','<a class="brands" aria-label="Presentation home" href="#'+esc(payload['first'])+'"')
s=re.sub(r'<script\b[^>]*id="demo-audience-analytics"[^>]*>.*?</script>','',s,flags=re.S)
assert re.search(r'<style>(.*?)</style>',s,re.S).group(1)==native_style
assert re.search(r'<script>(.*?)</script>',s,re.S).group(1)==native_script
for marker in ['Westbridge','banking-coordination','walkthrough-opening','speaker-notes.md','operatorNote','sourceIds','simonridd@gmail','GENESYS_BILLING','retained Thirdfort planning']:
    assert marker not in s,('Unexpected non-audience content',marker)
assert s.count('class="slide ')==8
assert 'http://localhost' not in s and '127.0.0.1' not in s
out.parent.mkdir(parents=True,exist_ok=True);out.write_text(s,encoding='utf-8')
receipt={'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'gitBlobSha':hashlib.sha1(b'blob '+str(len(out.read_bytes())).encode()+b'\0'+out.read_bytes()).hexdigest(),'bytes':len(out.read_bytes()),'slideCount':8,'templateSha256':payload['templateSha256'],'styleSha256':hashlib.sha256(native_style.encode()).hexdigest(),'controllerSha256':hashlib.sha256(native_script.encode()).hexdigest(),'method':'Audience markup in pinned published IPI shell; native controller and style bytes unchanged. Full Node repository validator not executed.'}
(out.parent/'build-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
