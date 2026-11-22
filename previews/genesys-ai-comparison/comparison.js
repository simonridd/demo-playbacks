// Version switching only. Slide navigation and diagrams remain owned by each deck.
const deck=document.getElementById('deck'),pick=document.getElementById('slide');
const allowed=new Set([...pick.options].map(option=>option.value));
const labels={original:'Original',updated:'Updated',motion:'With Motion'};
let version='motion',slide='standalone-ai';
const parts=location.hash.slice(1).split('/');
if(Object.hasOwn(labels,parts[0]))version=parts[0];if(allowed.has(parts[1]))slide=parts[1];
function reflect(){
 for(const button of document.querySelectorAll('[data-version]'))button.setAttribute('aria-pressed',String(button.dataset.version===version));
 pick.value=slide;deck.title=labels[version]+' Genesys AI briefing';
 document.getElementById('openOriginal').href='original/index.html#'+(slide==='briefing-map'?'standalone-ai':slide);
 document.getElementById('openUpdated').href='updated/index.html#'+slide;
 document.getElementById('openMotion').href='motion/index.html#'+slide;
 history.replaceState(null,'','#'+version+'/'+slide);
}
function load(){if(version==='original'&&slide==='briefing-map')slide='standalone-ai';reflect();deck.src=version+'/index.html#'+slide;document.getElementById('status').textContent=labels[version]+' version. '+pick.selectedOptions[0].textContent;}
for(const button of document.querySelectorAll('[data-version]'))button.addEventListener('click',()=>{version=button.dataset.version;load();});
pick.addEventListener('change',()=>{slide=pick.value;if(slide==='briefing-map'&&version==='original')version='motion';load();});
deck.addEventListener('load',()=>{
 try{const win=deck.contentWindow;const changed=()=>{const id=win.location.hash.slice(1);if(allowed.has(id)){slide=id;reflect();}};win.addEventListener('hashchange',changed);changed();}catch{/* Direct links remain available if embedding is unavailable. */}
});
const about=document.querySelector('.about');document.addEventListener('pointerdown',event=>{if(!about.contains(event.target))about.open=false;});document.addEventListener('keydown',event=>{if(event.key==='Escape'&&about.open){about.open=false;about.querySelector('summary').focus();}});
load();
