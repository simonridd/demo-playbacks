"""One-off audience markup packaging. No navigation engine or private input."""
from pathlib import Path
from html import escape as E
import json,hashlib
ROOT=Path.cwd()
story=json.loads((ROOT/'.thirdfort-package/audience.json').read_text())
icons={
'request':('Request','M3 4h18v12H9l-6 5V4zM7 8h10M7 12h6'),
'decision':('Decision','M12 2l10 10-10 10L2 12 12 2zM8 12h8M12 8l4 4-4 4'),
'person':('Person','M16 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0M4 21v-2a8 8 0 0 1 16 0v2'),
'search':('Review','M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0M15 15l6 6'),
'system':('System','M3 3h18v7H3zM3 14h18v7H3zM7 6h.01M7 17h.01M12 6h6M12 17h6'),
'chart':('Analytics','M3 3v18h18M7 16v-4M12 16V8M17 16V5'),
'knowledge':('Knowledge','M12 5C8 2 5 2 2 3v16c3-1 6-1 10 2 4-3 7-3 10-2V3c-3-1-6-1-10 2v16M5 7l4 1M15 8l4-1'),
'handoff':('Handoff','M2 7h15M13 3l4 4-4 4M22 17H7M11 13l-4 4 4 4'),
'shield':('Boundary','M12 2l8 4v6c0 5-8 10-8 10S4 17 4 12V6l8-4zM9 12l2 2 4-5'),
'record':('Record','M3 5c0-4 18-4 18 0v14c0 4-18 4-18 0V5zM3 5c0 4 18 4 18 0M3 12c0 4 18 4 18 0'),
'arrow':('Next step','M4 12h16M14 6l6 6-6 6'),
 'target':('Goal','M21 12a9 9 0 1 1-9-9M17 12a5 5 0 1 1-5-5M12 12l9-9M16 3h5v5')}
def icon(item,i):
    k=item.get('icon')
    if not k:return f'<span class="number" aria-hidden="true">{i+1:02}</span>'
    label,path=icons[k]
    return f'<span class="slide-icon icon-{k}" role="img" aria-label="{label}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="{path}"/></svg></span>'
def point(x,i):return f'<article class="content-row">{icon(x,i)}<h3>{E(x["title"])}</h3><p>{E(x["body"])}</p></article>'
def rows(items):return '<div class="section-items" style="--support-count:'+str(max(1,len(items)-1))+'">'+''.join(point(x,i) for i,x in enumerate(items))+'</div>'
def render(s,idx):
    design={'size':'large','width':'wide','placement':'auto','spacing':'balanced','arrangement':'default','chapters':True,'timing':False,'progress':True,'animations':True,'icons':True,'motion':'fade','expand':False,**story.get('design',{}),**s.get('design',{})}
    attrs=' '.join('data-design-'+k+'="'+E(str(v).lower() if isinstance(v,bool) else str(v))+'"' for k,v in design.items())
    title_tag='h1' if s['layout']=='hero' else 'h2'
    heading=f'<p class="eyebrow">{E(s["label"])}</p><{title_tag} id="{s["id"]}-title" tabindex="-1">{E(s["title"])}</{title_tag}>'
    if s.get('lead'):heading+=f'<p class="lead">{E(s["lead"])}</p>'
    note=f'<p class="footnote">{E(s["note"])}</p>' if s.get('note') else ''
    question=f'<p class="question">{E(s["question"])}</p>' if s.get('question') else ''
    layout=s['layout']
    if layout=='hero':
        points=''.join('<div class="hero-item"><h3>'+icon(x,i)+E(x['title'])+'</h3><p>'+E(x['body'])+'</p></div>' for i,x in enumerate(s['items']))
        body='<div class="hero"><div>'+heading+question+'<button class="primary" type="button" data-go="meet-ipi">Start discovery <span aria-hidden="true">→</span></button></div><aside class="hero-panel" aria-label="Supporting points"><p class="panel-label">The right help</p>'+points+'</aside></div>'+note
    elif layout=='pipeline':
        body=heading+'<ol class="spec-pipeline" aria-label="Ordered steps">'+''.join('<li>'+icon(x,i)+'<h3>'+E(x['title'])+'</h3><p>'+E(x['body'])+'</p></li>' for i,x in enumerate(s['steps']))+'</ol>'+note+question
    elif layout=='dialogue':
        body=heading+'<div class="customer-conversation" role="group" aria-label="Customer conversation">'+''.join('<div class="speech"><span>'+E(x['speaker'])+'</span><p>'+E(x['text'])+'</p></div>' for x in s['dialogue'])+'</div><p class="editorial-takeaway">'+E(s['takeaway'])+'</p>'+note+question
    elif layout=='comparison-table':
        d=s['comparisonTable'];h=d['headers']
        table='<div class="comparison-matrix" data-comparison-matrix data-state="all" data-overview="'+E(d['overview'])+'" role="group" aria-label="'+E(d['label'])+'"><p class="comparison-matrix-status" role="status" aria-live="polite">'+E(d['overview'])+'</p><table class="principle-table"><thead><tr>'+''.join('<th scope="col">'+E(x)+'</th>' for x in h)+'</tr></thead><tbody>'
        for i,r in enumerate(d['rows']):
            table+='<tr data-comparison-row="'+str(i)+'" data-key="'+E(r['id'])+'" data-cue="'+E(r['cue'])+'"><th scope="row" data-column-label="'+E(h[0])+'">'+E(r['cells'][0])+'</th>'+''.join('<td data-column-label="'+E(h[j])+'">'+E(r['cells'][j])+'</td>' for j in [1,2])+'</tr>'
        body=heading+table+'</tbody></table></div><p class="comparison-takeaway">'+E(d['takeaway'])+'</p>'+note+question
    elif layout=='comparison':
        body=heading+'<div class="comparison-columns">'+''.join('<article>'+icon(x,i)+'<h3>'+E(x['title'])+'</h3><p>'+E(x['body'])+'</p></article>' for i,x in enumerate(s['items'][:2]))+'</div><p class="comparison-caveat"><strong>'+E(s['items'][2]['title'])+'</strong> '+E(s['items'][2]['body'])+'</p>'+note+question
    elif layout=='closing':body=heading+rows(s['items'])+note+question
    else:raise ValueError(layout)
    return f'<section id="{s["id"]}" class="slide {layout}" data-route="main" data-section="{E(s["section"])}" data-label="{E(s["label"])}" data-print-title="Thirdfort | Digital support discovery" data-reflow="normal" aria-labelledby="{s["id"]}-title" {attrs}>{body}</section>'
by={s['id']:s for s in story['sections']};sections='\n'.join(render(by[sid],i) for i,sid in enumerate(story['routes']['main']))
nav=[];last=None
for sid in story['routes']['main']:
    s=by[sid]
    if s['section']!=last:
        nav.append(f'<button type="button" data-go="{sid}" data-section="{E(s["section"])}"><span aria-hidden="true">{len(nav)+1:02}</span>{E(s["section"])}</button>');last=s['section']
template=(ROOT/'previews/copilot-example/presentation.html').read_bytes()
assert hashlib.sha256(template).hexdigest()=='bf848930675f03098327ef4986bb9d1968e3038610a38d80047b2156f87fead6'
payload={'templatePath':'previews/copilot-example/presentation.html','templateSha256':hashlib.sha256(template).hexdigest(),'id':story['id'],'title':story['title'],'description':'Thirdfort discovery: IPI, digital bots and Agentic Virtual Agents, and four support journeys.','first':'welcome','sections':sections,'navigation':''.join(nav)}
(ROOT/'build').mkdir(exist_ok=True)
(ROOT/'build/audience-payload.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
