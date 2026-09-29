import json

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&display=swap" rel="stylesheet">'

CSS = r"""
:root{
 --paper:#F5F6F8;--card:#FFFFFF;--ink:#1B2340;--muted:#586178;--line:#D8DDE7;
 --indigo:#2E3F8F;--indigo-soft:#E6E9F6;--marker:#FFE27A;--teal:#12705F;--teal-soft:#DDF1EC;
 --brick:#A83C29;--brick-soft:#F8E3DE;--sun:#F2B233;
 --head:"Bricolage Grotesque","Segoe UI",system-ui,-apple-system,sans-serif;
 --body:"Atkinson Hyperlegible","Segoe UI",system-ui,-apple-system,sans-serif;
 box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --paper:#11141C;--card:#1A1E2A;--ink:#E7EAF3;--muted:#9EA7BC;--line:#2C3244;
 --indigo:#9AABFF;--indigo-soft:#232A45;--marker:rgba(255,214,90,.30);--teal:#52C7AE;--teal-soft:#16332D;
 --brick:#F2826C;--brick-soft:#3A201B;--sun:#F2B233;}}
:root[data-theme="dark"]{
 --paper:#11141C;--card:#1A1E2A;--ink:#E7EAF3;--muted:#9EA7BC;--line:#2C3244;
 --indigo:#9AABFF;--indigo-soft:#232A45;--marker:rgba(255,214,90,.30);--teal:#52C7AE;--teal-soft:#16332D;
 --brick:#F2826C;--brick-soft:#3A201B;}
*,*::before,*::after{box-sizing:inherit}
html{scroll-padding-top:calc(env(safe-area-inset-top,0px) + 70px);-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--body);font-size:17px;line-height:1.6}
img,svg{max-width:100%}
a{color:var(--indigo)}
:focus-visible{outline:3px solid var(--sun);outline-offset:2px;border-radius:4px}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.col{max-width:720px}
h1,h2,h3,h4{font-family:var(--head);line-height:1.15;margin:0}
h2{font-size:clamp(1.5rem,3.4vw,2rem);font-weight:800;margin:0 0 .6rem}
h3{font-size:1.2rem;font-weight:700;margin:1.8rem 0 .5rem}
p{margin:.55rem 0}
ul,ol{margin:.4rem 0 .8rem;padding-left:1.3rem}
li{margin:.25rem 0}
/* top bar */
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:color-mix(in srgb,var(--paper) 92%,transparent);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.bar .wrap{display:flex;align-items:center;gap:12px;min-height:58px}
.brand{font-family:var(--head);font-weight:700;font-size:.95rem;color:var(--muted);text-decoration:none;white-space:nowrap}
.tabs{display:flex;gap:4px;margin-left:auto;background:var(--card);border:1px solid var(--line);border-radius:999px;padding:4px}
.tab{border:0;background:transparent;color:var(--ink);font:600 .95rem var(--body);padding:.45rem .95rem;border-radius:999px;cursor:pointer}
.tab[aria-selected="true"]{background:var(--indigo);color:var(--card)}
.themebtn{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;width:38px;height:38px;cursor:pointer;font-size:1rem}
@media (max-width:620px){.brand{display:none}.tabs{margin-left:0;flex:1;justify-content:space-between}.tab{padding:.45rem .6rem;flex:1}}
/* hero */
.hero{padding:44px 0 18px}
.kicker{font-family:var(--head);font-weight:700;color:var(--indigo);font-size:1rem;margin-bottom:.4rem}
.hero h1{font-size:clamp(2.1rem,6vw,3.6rem);font-weight:800;letter-spacing:-.02em;max-width:18ch}
.meta{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 0}
.pill{border:1px solid var(--line);background:var(--card);border-radius:999px;padding:.2rem .75rem;font-size:.9rem;color:var(--muted)}
.pill b{color:var(--ink)}
.oneline{margin:28px 0 8px;font-family:var(--head);font-size:clamp(1.25rem,3vw,1.7rem);font-weight:500;line-height:1.35;max-width:32ch}
.oneline .k{font-weight:700}
/* key term highlighter */
.k{background:linear-gradient(104deg,transparent 0 .2em,var(--marker) .2em calc(100% - .15em),transparent calc(100% - .15em));padding:0 .2em;margin:0 -.05em;font-weight:700;-webkit-box-decoration-break:clone;box-decoration-break:clone}
/* sections */
section.sec{padding:34px 0 10px;border-top:1px solid var(--line);margin-top:26px}
.secno{font-family:var(--head);font-weight:800;color:var(--indigo);font-size:1rem;display:block;margin-bottom:.2rem}
.why{border-left:4px solid var(--indigo);background:var(--indigo-soft);padding:.7rem 1rem;border-radius:0 10px 10px 0;margin:1rem 0}
.why b:first-child{display:block;font-family:var(--head);margin-bottom:.1rem}
.analogy{background:var(--card);border:1px dashed var(--indigo);border-radius:14px;padding:.8rem 1rem;margin:1rem 0}
.analogy::before{content:"Think of it like this";display:block;font-family:var(--head);font-weight:700;color:var(--indigo);font-size:.95rem;margin-bottom:.2rem}
.trap{border:2px solid var(--brick);background:var(--brick-soft);border-radius:12px;padding:.65rem .95rem;margin:1rem 0;position:relative}
.trap::before{content:"Exam trap";display:inline-block;font-family:var(--head);font-weight:800;color:var(--card);background:var(--brick);border-radius:6px;padding:0 .45rem;font-size:.85rem;margin-right:.45rem;transform:rotate(-2deg)}
.num{font-family:var(--head);font-weight:800;color:var(--brick)}
dl.terms{display:grid;grid-template-columns:minmax(120px,max-content) 1fr;gap:.35rem 1rem;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:1rem 1.1rem;margin:1rem 0}
dl.terms dt{font-weight:700}
dl.terms dd{margin:0;color:var(--muted)}
@media (max-width:560px){dl.terms{grid-template-columns:1fr}dl.terms dd{margin-bottom:.4rem}}
.terms-title{font-family:var(--head);font-weight:700;margin:1.4rem 0 -.4rem}
/* figures */
figure.fig{margin:1.4rem 0;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px}
figure.fig figcaption{font-family:var(--head);font-weight:700;font-size:1.02rem;margin-bottom:12px}
figure.fig figcaption span{display:block;font-family:var(--body);font-weight:400;color:var(--muted);font-size:.9rem;margin-top:2px}
.scroll{overflow-x:auto}
/* flow */
.flow{display:flex;align-items:stretch;gap:0;flex-wrap:nowrap}
.flow .step{flex:1;background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:.7rem .8rem;min-width:0}
.flow .step h4{font-size:1rem;margin-bottom:.2rem}
.flow .step p{font-size:.92rem;margin:0;color:var(--muted)}
.flow .arrow{flex:0 0 28px;display:flex;align-items:center;justify-content:center;color:var(--indigo);font-weight:800;font-size:1.3rem}
.flow .arrow::before{content:"\2192"}
@media (max-width:700px){.flow{flex-direction:column}.flow .arrow{flex-basis:26px}.flow .arrow::before{content:"\2193"}}
.step.hl{border-color:var(--indigo);background:var(--indigo-soft)}
.step.gd{border-color:var(--teal);background:var(--teal-soft)}
.step.bd{border-color:var(--brick);background:var(--brick-soft)}
/* grids */
.grid{display:grid;gap:12px}
.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}
@media (max-width:760px){.g3,.g4{grid-template-columns:repeat(2,1fr)}}
@media (max-width:480px){.g2,.g3,.g4{grid-template-columns:1fr}}
.box{background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:.75rem .9rem}
.box h4{font-size:1.02rem;margin-bottom:.25rem}
.box p,.box li{font-size:.93rem}
.box ul{margin:.2rem 0 0}
.box .tag{display:inline-block;font-size:.78rem;font-weight:700;border-radius:6px;padding:0 .4rem;background:var(--indigo-soft);color:var(--indigo);margin-bottom:.3rem}
.box.gd{border-color:var(--teal)}.box.bd{border-color:var(--brick)}.box.hl{border-color:var(--indigo)}
/* table */
table.cmp{border-collapse:collapse;width:100%;min-width:560px;font-size:.93rem}
table.cmp th,table.cmp td{border-bottom:1px solid var(--line);padding:.55rem .6rem;text-align:left;vertical-align:top}
table.cmp thead th{font-family:var(--head);background:var(--indigo-soft);color:var(--ink)}
table.cmp tbody th{font-weight:700;color:var(--muted);width:24%}
/* id card */
.idcard{display:grid;grid-template-columns:auto 1fr;gap:.15rem .7rem;font-size:.88rem;margin-top:.4rem}
.idcard span:nth-child(odd){color:var(--muted)}
/* bars */
.stack{display:flex;height:46px;border-radius:10px;overflow:hidden;border:1px solid var(--line);font-weight:700;font-size:.9rem}
.stack div{display:flex;align-items:center;justify-content:center;color:var(--card);text-align:center;padding:0 4px}
/* traps list and talk */
.traplist{counter-reset:t;list-style:none;padding:0}
.traplist li{counter-increment:t;background:var(--card);border:1px solid var(--line);border-left:5px solid var(--brick);border-radius:10px;padding:.6rem .9rem .6rem 3rem;position:relative;margin:.5rem 0}
.traplist li::before{content:counter(t);position:absolute;left:.9rem;top:.55rem;font-family:var(--head);font-weight:800;color:var(--brick);font-size:1.1rem}
.talk li{margin:.45rem 0}
.ptr{font-size:.85rem;color:var(--muted)}
/* chapter map */
.map{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}
.map a{display:block;text-decoration:none;color:var(--ink);background:var(--paper);border:1px solid var(--line);border-radius:12px;padding:.7rem .85rem;transition:border-color .15s}
.map a:hover{border-color:var(--indigo)}
.map a b{display:block;font-family:var(--head);color:var(--indigo);font-size:.9rem}
.map a span{font-weight:700;display:block;line-height:1.25}
.map a small{color:var(--muted);display:block;margin-top:.25rem;line-height:1.3}
.tl{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;position:relative;padding-top:6px}
.tl::before{content:"";position:absolute;left:8%;right:8%;top:21px;height:4px;background:var(--line);border-radius:4px}
.tl-i{text-align:center;position:relative}
.tl-t{display:block;font-family:var(--head);font-size:1.15rem}
.tl-d{display:block;width:22px;height:22px;border-radius:50%;margin:6px auto 8px;position:relative;border:3px solid var(--card)}
.tl-i h4{font-size:1.05rem}.tl-i p{font-size:.9rem;color:var(--muted);margin:.2rem 0 0}
@media (max-width:560px){.tl{grid-template-columns:1fr}.tl::before{display:none}.tl-i{text-align:left;padding-left:34px}.tl-d{position:absolute;left:0;top:0;margin:0}}
input[type=range]{accent-color:var(--indigo)}
/* views */
.view[hidden]{display:none}
footer{color:var(--muted);font-size:.85rem;padding:40px 0 60px;border-top:1px solid var(--line);margin-top:40px}
/* flashcards */
.fc-wrap{max-width:640px;margin:30px auto 0}
.fc-top{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:12px}
.fc-prog{height:8px;background:var(--line);border-radius:99px;overflow:hidden;margin-bottom:16px}
.fc-prog div{height:100%;background:var(--teal);width:0;transition:width .3s}
.card3d{perspective:1200px;cursor:pointer;user-select:none}
.card3d .inner{position:relative;min-height:300px;transition:transform .5s;transform-style:preserve-3d}
.card3d.flip .inner{transform:rotateY(180deg)}
.face{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;border-radius:20px;padding:28px;display:flex;flex-direction:column;justify-content:center;border:1px solid var(--line);background:var(--card)}
.face.back{transform:rotateY(180deg);background:var(--indigo-soft);border-color:var(--indigo)}
.face .lbl{position:absolute;top:14px;left:18px;font-size:.8rem;color:var(--muted);font-weight:700}
.face .front-txt{font-family:var(--head);font-size:clamp(1.3rem,4vw,1.8rem);font-weight:700;line-height:1.25}
.face .back-txt{font-size:1.08rem}
.hint{color:var(--muted);font-size:.85rem;text-align:center;margin-top:10px}
@media (prefers-reduced-motion:reduce){.card3d .inner{transition:none}}
.btns{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:16px}
.btn{font:700 1rem var(--body);border-radius:12px;padding:.65rem 1.1rem;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
.btn.pri{background:var(--indigo);border-color:var(--indigo);color:var(--card)}
.btn.good{background:var(--teal);border-color:var(--teal);color:var(--card)}
.btn.bad{background:var(--brick);border-color:var(--brick);color:var(--card)}
.btn:disabled{opacity:.45;cursor:not-allowed}
.btn.sm{font-size:.88rem;padding:.4rem .75rem;border-radius:10px}
/* quiz */
.qz{max-width:720px;margin:30px auto 0}
.qz-setup .box{margin:.6rem 0}
.qz-setup label{display:flex;gap:.6rem;align-items:flex-start;cursor:pointer}
.qz-head{display:flex;justify-content:space-between;align-items:center;color:var(--muted);font-size:.9rem;margin-bottom:10px;gap:8px;flex-wrap:wrap}
.qcase{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--sun);border-radius:12px;padding:.8rem 1rem;margin-bottom:12px;font-size:.95rem}
.qcase b{font-family:var(--head)}
.qtext{font-family:var(--head);font-size:1.25rem;font-weight:700;line-height:1.3;margin:4px 0 14px}
.opt{display:flex;gap:.7rem;align-items:flex-start;width:100%;text-align:left;font:1rem var(--body);color:var(--ink);background:var(--card);border:2px solid var(--line);border-radius:12px;padding:.7rem .9rem;margin:.45rem 0;cursor:pointer}
.opt .lt{font-family:var(--head);font-weight:800;color:var(--indigo);min-width:1.2rem}
.opt[aria-pressed="true"]{border-color:var(--indigo);background:var(--indigo-soft)}
.opt.right{border-color:var(--teal);background:var(--teal-soft)}
.opt.wrong{border-color:var(--brick);background:var(--brick-soft)}
.opt:disabled{cursor:default}
.explain{border-radius:12px;padding:.7rem 1rem;margin-top:12px;background:var(--paper);border:1px solid var(--line)}
.explain.ok{border-color:var(--teal)}.explain.no{border-color:var(--brick)}
.explain b{font-family:var(--head)}
.score{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:16px 0}
@media (max-width:520px){.score{grid-template-columns:repeat(2,1fr)}}
.score div{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:.7rem;text-align:center}
.score b{display:block;font-family:var(--head);font-size:1.8rem}
.score small{color:var(--muted)}
.verdict{font-family:var(--head);font-size:1.4rem;font-weight:800;margin:10px 0}
.review .item{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:.7rem 1rem;margin:.6rem 0}
.review .item p{margin:.25rem 0}
.toast{position:fixed;left:50%;bottom:calc(20px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);background:var(--ink);color:var(--paper);padding:.5rem 1rem;border-radius:10px;font-weight:700;opacity:0;transition:opacity .2s;pointer-events:none;z-index:50}
.toast.show{opacity:1}
@media print{.bar,.btns,.themebtn{display:none}.view[hidden]{display:block}#v-cards,#v-quiz{display:none}figure.fig,.trap,.analogy{break-inside:avoid}}
"""

JS = r"""
(function(){
const DATA = window.__DATA__;
const KEY = 'nismra:'+DATA.id+':';
const store = {
  get(k,d){try{const v=localStorage.getItem(KEY+k);return v?JSON.parse(v):d}catch(e){return d}},
  set(k,v){try{localStorage.setItem(KEY+k,JSON.stringify(v))}catch(e){}}
};
const $=(s,r=document)=>r.querySelector(s);
const el=(t,a={},h='')=>{const e=document.createElement(t);for(const k in a){if(k==='class')e.className=a[k];else e.setAttribute(k,a[k])}if(h)e.innerHTML=h;return e};
function toast(m){const t=$('#toast');t.textContent=m;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),1600)}
/* theme */
const tb=$('#themebtn');
function applyTheme(t){if(t)document.documentElement.setAttribute('data-theme',t);else document.documentElement.removeAttribute('data-theme');tb.textContent=(t==='dark'||(!t&&matchMedia('(prefers-color-scheme: dark)').matches))?'\u2600':'\u263E'}
let th=null;try{th=localStorage.getItem('nismra:theme')}catch(e){}
applyTheme(th);
tb.addEventListener('click',()=>{const dark=document.documentElement.getAttribute('data-theme')==='dark'||(!document.documentElement.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme: dark)').matches);const n=dark?'light':'dark';applyTheme(n);try{localStorage.setItem('nismra:theme',n)}catch(e){}});
/* tabs */
const tabs=[...document.querySelectorAll('.tab')];
function show(v){tabs.forEach(t=>t.setAttribute('aria-selected',t.dataset.v===v));document.querySelectorAll('.view').forEach(x=>x.hidden=x.id!=='v-'+v);if(v==='cards')renderCard();window.scrollTo(0,0);try{history.replaceState(null,'','#'+v)}catch(e){}}
tabs.forEach(t=>t.addEventListener('click',()=>show(t.dataset.v)));
/* ---------- flashcards ---------- */
const cards=DATA.cards;
let known=new Set(store.get('known',[]));
let missed=new Set(store.get('missed',[]));
let deck=[],pos=0,onlyMissed=false;
function buildDeck(shuffle){deck=cards.map((c,i)=>i).filter(i=>!onlyMissed||missed.has(i));if(shuffle){for(let i=deck.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[deck[i],deck[j]]=[deck[j],deck[i]]}}pos=0}
buildDeck(false);
function renderCard(){
  const c3=$('#fc-card');c3.classList.remove('flip');
  const done=known.size;$('#fc-bar').style.width=(100*done/cards.length)+'%';
  $('#fc-count').textContent=done+' of '+cards.length+' marked known';
  if(!deck.length){$('#fc-front').innerHTML='No cards here.';$('#fc-back').innerHTML='Switch off "Only cards I missed" to see the full deck.';$('#fc-pos').textContent='';return}
  if(pos>=deck.length){$('#fc-front').innerHTML='Deck done.';$('#fc-back').innerHTML='Press Shuffle to go again, or study only the cards you missed.';$('#fc-pos').textContent='';return}
  const c=cards[deck[pos]];$('#fc-front').innerHTML=c.f;$('#fc-back').innerHTML=c.b;$('#fc-pos').textContent='Card '+(pos+1)+' of '+deck.length;
}
function flip(){$('#fc-card').classList.toggle('flip')}
$('#fc-card').addEventListener('click',flip);
$('#fc-card').addEventListener('keydown',e=>{if(e.key===' '||e.key==='Enter'){e.preventDefault();flip()}});
function mark(ok){if(pos>=deck.length)return;const i=deck[pos];if(ok){known.add(i);missed.delete(i)}else{missed.add(i);known.delete(i)}store.set('known',[...known]);store.set('missed',[...missed]);pos++;renderCard()}
$('#fc-good').addEventListener('click',()=>mark(true));
$('#fc-bad').addEventListener('click',()=>mark(false));
$('#fc-shuffle').addEventListener('click',()=>{buildDeck(true);renderCard()});
$('#fc-missed').addEventListener('change',e=>{onlyMissed=e.target.checked;buildDeck(false);renderCard()});
$('#fc-reset').addEventListener('click',()=>{known.clear();missed.clear();store.set('known',[]);store.set('missed',[]);buildDeck(false);renderCard();toast('Progress cleared')});
document.addEventListener('keydown',e=>{if($('#v-cards').hidden)return;if(e.key==='ArrowRight')mark(true);if(e.key==='ArrowLeft')mark(false)});
/* ---------- quiz ---------- */
const Q=[];DATA.mcqs.forEach(q=>Q.push(Object.assign({kind:'mcq'},q)));
(DATA.cases||[]).forEach(cs=>cs.qs.forEach((q,k)=>Q.push(Object.assign({kind:'case',caseTitle:cs.title,caseText:cs.text,id:cs.id+'-'+(k+1)},q))));
let run=null;
function pick(set){let arr;
  if(set==='quick'){arr=Q.filter(q=>q.kind==='mcq').slice();for(let i=arr.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[arr[i],arr[j]]=[arr[j],arr[i]]}arr=arr.slice(0,10)}
  else if(set==='mcq')arr=Q.filter(q=>q.kind==='mcq');
  else if(set==='case')arr=Q.filter(q=>q.kind==='case');
  else if(set==='missed'){const m=new Set(store.get('qmissed',[]));arr=Q.filter(q=>m.has(q.id))}
  else arr=Q.slice();
  return arr}
function start(){const set=document.querySelector('input[name=qset]:checked').value;const mode=document.querySelector('input[name=qmode]:checked').value;const qs=pick(set);
  if(!qs.length){toast('No questions in this set yet');return}
  run={qs,mode,i:0,ans:qs.map(()=>null),checked:qs.map(()=>false)};$('#qz-setup').hidden=true;$('#qz-end').hidden=true;$('#qz-run').hidden=false;renderQ()}
function renderQ(){const q=run.qs[run.i];const box=$('#qz-q');box.innerHTML='';
  $('#qz-pos').textContent='Question '+(run.i+1)+' of '+run.qs.length;
  $('#qz-modelbl').textContent=run.mode==='exam'?'Exam mode: answers shown at the end':'Practice mode';
  if(q.kind==='case'){box.appendChild(el('div',{class:'qcase'},'<b>Case: '+q.caseTitle+'</b><br>'+q.caseText))}
  box.appendChild(el('div',{class:'qtext'},q.q));
  const L='abcd';
  q.o.forEach((o,k)=>{const b=el('button',{class:'opt','aria-pressed':String(run.ans[run.i]===k)},'<span class="lt">'+L[k]+'</span><span>'+o+'</span>');
    b.addEventListener('click',()=>{if(run.checked[run.i])return;run.ans[run.i]=k;renderQ()});box.appendChild(b)});
  if(run.checked[run.i])paintCheck();
  $('#qz-check').hidden=run.mode==='exam'||run.checked[run.i];
  $('#qz-check').disabled=run.ans[run.i]===null;
  $('#qz-prev').disabled=run.i===0;
  $('#qz-next').textContent=run.i===run.qs.length-1?'Finish':'Next';
  $('#qz-skip').hidden=run.checked[run.i];
}
function paintCheck(){const q=run.qs[run.i];const opts=[...document.querySelectorAll('#qz-q .opt')];opts.forEach((b,k)=>{b.disabled=true;if(k===q.a)b.classList.add('right');else if(k===run.ans[run.i])b.classList.add('wrong')});
  const a=run.ans[run.i];const ok=a===q.a;const ex=el('div',{class:'explain '+(a===null?'':(ok?'ok':'no'))},'<b>'+(a===null?'Skipped. ':ok?'Correct. ':'Not quite. ')+'</b>'+q.w);$('#qz-q').appendChild(ex)}
$('#qz-check').addEventListener('click',()=>{run.checked[run.i]=true;renderQ()});
$('#qz-skip').addEventListener('click',()=>{run.ans[run.i]=null;if(run.mode==='practice'){run.checked[run.i]=true;renderQ()}else next()});
$('#qz-prev').addEventListener('click',()=>{if(run.i>0){run.i--;renderQ()}});
function next(){if(run.i<run.qs.length-1){run.i++;renderQ();window.scrollTo({top:0})}else finish()}
$('#qz-next').addEventListener('click',next);
$('#qz-start').addEventListener('click',start);
$('#qz-quit').addEventListener('click',()=>{$('#qz-run').hidden=true;$('#qz-setup').hidden=false});
function finish(){let c=0,w=0,s=0;const miss=new Set(store.get('qmissed',[]));const wrongIdx=[];
  run.qs.forEach((q,i)=>{const a=run.ans[i];if(a===null){s++;miss.add(q.id);wrongIdx.push(i)}else if(a===q.a){c++;miss.delete(q.id)}else{w++;miss.add(q.id);wrongIdx.push(i)}});
  store.set('qmissed',[...miss]);
  const net=c-0.25*w;const pct=100*net/run.qs.length;
  $('#qz-run').hidden=true;$('#qz-end').hidden=false;
  $('#qz-score').innerHTML='<div><b>'+c+'</b><small>correct</small></div><div><b>'+w+'</b><small>wrong</small></div><div><b>'+s+'</b><small>skipped</small></div><div><b>'+net.toFixed(2)+'</b><small>net score</small></div>';
  $('#qz-verdict').textContent=pct>=60?('Pass level. Net '+pct.toFixed(0)+'%.'):('Below the 60% pass line. Net '+pct.toFixed(0)+'%.');
  $('#qz-penalty').textContent=w?('Wrong answers cost you '+(0.25*w).toFixed(2)+' marks.'):'No marks lost to negative marking.';
  const rv=$('#qz-review');rv.innerHTML='';const L='abcd';
  if(!wrongIdx.length)rv.innerHTML='<p>Nothing to review. Every answer was right.</p>';
  wrongIdx.forEach(i=>{const q=run.qs[i];const a=run.ans[i];rv.appendChild(el('div',{class:'item'},'<p><b>'+q.q+'</b></p><p>Your answer: '+(a===null?'skipped':L[a]+') '+q.o[a])+'</p><p>Right answer: <b>'+L[q.a]+') '+q.o[q.a]+'</b></p><p class="ptr">'+q.w+'</p>'))});
  run.summary=DATA.short+' quiz: '+c+'/'+run.qs.length+' correct, '+w+' wrong, '+s+' skipped. Net '+net.toFixed(2)+' ('+pct.toFixed(0)+'%).'+(wrongIdx.length?' Missed: '+wrongIdx.map(i=>run.qs[i].id).join(', '):'');
}
$('#qz-copy').addEventListener('click',()=>{const t=run&&run.summary||'';(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(()=>toast('Copied. Paste it in the group chat.')).catch(()=>{prompt('Copy this:',t)})});
$('#qz-again').addEventListener('click',()=>{$('#qz-end').hidden=true;$('#qz-setup').hidden=false;updateMissedCount()});
function updateMissedCount(){const n=store.get('qmissed',[]).length;$('#qz-missedn').textContent=n?('('+n+' saved)'):'(none yet)'}
updateMissedCount();
$('#qz-counts').textContent=DATA.mcqs.length+' MCQs and '+(DATA.cases||[]).reduce((s,c)=>s+c.qs.length,0)+' case questions';
/* interactive widgets hook */
if(window.__WIDGETS__)window.__WIDGETS__();
const h=(location.hash||'').replace('#','');if(['learn','cards','quiz'].includes(h))show(h);
})();
"""

def page(data, learn_html, widgets_js="", home=True):
    brand = '<a class="brand" href="../index.html">NISM RA study kit</a>' if home else '<span class="brand">NISM RA study kit</span>'
    head = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{data['title']} | NISM RA study kit</title>{FONTS}<style>{CSS}</style></head><body>
<div class="bar"><div class="wrap">{brand}
<div class="tabs" role="tablist"><button class="tab" role="tab" data-v="learn" aria-selected="true">Learn</button><button class="tab" role="tab" data-v="cards" aria-selected="false">Flashcards</button><button class="tab" role="tab" data-v="quiz" aria-selected="false">Quiz</button></div>
<button class="themebtn" id="themebtn" aria-label="Switch light or dark">&#9790;</button></div></div>"""
    cards_view = """<div class="view" id="v-cards" hidden><div class="wrap"><div class="fc-wrap">
<div class="fc-top"><span id="fc-count" class="ptr"></span><label class="ptr"><input type="checkbox" id="fc-missed"> Only cards I missed</label></div>
<div class="fc-prog"><div id="fc-bar"></div></div>
<div class="card3d" id="fc-card" tabindex="0" role="button" aria-label="Flip card"><div class="inner">
<div class="face"><span class="lbl" id="fc-pos"></span><div class="front-txt" id="fc-front"></div></div>
<div class="face back"><span class="lbl">Answer</span><div class="back-txt" id="fc-back"></div></div></div></div>
<p class="hint">Tap the card to flip. On a keyboard: space flips, right arrow = got it, left arrow = again.</p>
<div class="btns"><button class="btn bad" id="fc-bad">Again</button><button class="btn good" id="fc-good">Got it</button></div>
<div class="btns"><button class="btn sm" id="fc-shuffle">Shuffle</button><button class="btn sm" id="fc-reset">Clear progress</button></div>
</div></div></div>"""
    quiz_view = """<div class="view" id="v-quiz" hidden><div class="wrap"><div class="qz">
<div id="qz-setup" class="qz-setup"><h2>Test yourself</h2><p class="ptr" id="qz-counts"></p>
<p>Scoring works like the real exam: +1 for a right answer, minus 0.25 for a wrong one, 0 for a skip. Skipping is allowed.</p>
<div class="box"><h4>Which questions?</h4>
<label><input type="radio" name="qset" value="quick" checked> Quick 10 (random MCQs)</label>
<label><input type="radio" name="qset" value="mcq"> All MCQs</label>
<label><input type="radio" name="qset" value="case"> Case sets only (the exam has 5 of these, 4 questions each)</label>
<label><input type="radio" name="qset" value="all"> Everything</label>
<label><input type="radio" name="qset" value="missed"> Only questions I got wrong before <span id="qz-missedn" class="ptr"></span></label></div>
<div class="box"><h4>How?</h4>
<label><input type="radio" name="qmode" value="practice" checked> Practice: see the answer after each question</label>
<label><input type="radio" name="qmode" value="exam"> Exam: see everything at the end</label></div>
<div class="btns" style="justify-content:flex-start"><button class="btn pri" id="qz-start">Start</button></div></div>
<div id="qz-run" hidden><div class="qz-head"><span id="qz-pos"></span><span id="qz-modelbl"></span></div>
<div id="qz-q"></div>
<div class="btns" style="justify-content:space-between"><button class="btn sm" id="qz-prev">Back</button><span><button class="btn sm" id="qz-skip">Skip</button> <button class="btn pri sm" id="qz-check">Check</button> <button class="btn sm" id="qz-next">Next</button></span></div>
<div class="btns" style="justify-content:flex-start"><button class="btn sm" id="qz-quit">Stop and go back</button></div></div>
<div id="qz-end" hidden><h2>Your result</h2><div class="score" id="qz-score"></div><p class="verdict" id="qz-verdict"></p><p class="ptr" id="qz-penalty"></p>
<div class="btns" style="justify-content:flex-start"><button class="btn pri" id="qz-copy">Copy result for the group</button><button class="btn" id="qz-again">Try another set</button></div>
<h3>Review what you missed</h3><div class="review" id="qz-review"></div></div>
</div></div></div>"""
    tail = f"""<div class="toast" id="toast" role="status"></div>
<script>window.__DATA__={json.dumps(data, ensure_ascii=False)};</script>
<script>{widgets_js}</script><script>{JS}</script></body></html>"""
    return head + '<div class="view" id="v-learn">' + learn_html + '</div>' + cards_view + quiz_view + tail
