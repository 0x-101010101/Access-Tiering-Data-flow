# <span class="prefix">ReBAC:</span> defining hierarchical tiers of access {#rbac-applied .vision .stay-dark}

<p class="hook" id="ead-hook-swap" hidden>A confidential swap fails. The quote is T2. The intent is T1. The trace keeps T1. KYT returns passing.</p>
<p class="hook" id="ead-hook-use">A lead inherits T1, T2, and T3. An engineer inherits T2 and T3.</p>

<button id="ead-toggle" class="ead-switch" type="button" aria-pressed="true">The swap</button>

<div id="complex-animated-dag" class="diagram">
 <div class="viz-controls"><span id="ead-swap-controls" hidden><button id="ead-play" type="button">Play</button><button id="ead-replay" type="button">Replay</button><button id="ead-step" type="button">Next stage</button><span id="ead-status" aria-live="polite">Three records for one failed swap</span></span></div>
 <div id="ead-stage" hidden></div>
 <div id="ead-legend" hidden></div>
 <div id="ead-use">
  <svg viewBox="0 0 1040 320" role="img" aria-label="Ordinary fields together name one person. A lead inherits T1, T2, and T3. An engineer inherits T2 and T3.">
   <defs><marker id="ead-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#9ca3af"></path></marker></defs>
   <text x="20" y="28">Ordinary fields</text>
   <rect x="20" y="48" width="150" height="40" rx="8" fill="#eef2ff" stroke="#6366f1"></rect>
   <text x="95" y="73" text-anchor="middle">first name</text>
   <rect x="20" y="108" width="150" height="40" rx="8" fill="#eef2ff" stroke="#6366f1"></rect>
   <text x="95" y="133" text-anchor="middle">profession</text>
   <rect x="20" y="168" width="150" height="40" rx="8" fill="#eef2ff" stroke="#6366f1"></rect>
   <text x="95" y="193" text-anchor="middle">age</text>
   <rect x="20" y="228" width="150" height="40" rx="8" fill="#eef2ff" stroke="#6366f1"></rect>
   <text x="95" y="253" text-anchor="middle">IP → city</text>
   <rect x="300" y="128" width="156" height="52" rx="8" fill="#fef2f2" stroke="#dc2626"></rect>
   <text x="378" y="158" text-anchor="middle">one person</text>
   <path d="M170 68 C230 68 240 154 300 154" fill="none" stroke="#6b7280" stroke-width="1.6" marker-end="url(#ead-arrow)"></path>
   <path d="M170 128 C230 128 250 154 300 154" fill="none" stroke="#6b7280" stroke-width="1.6" marker-end="url(#ead-arrow)"></path>
   <path d="M170 188 C230 188 250 154 300 154" fill="none" stroke="#6b7280" stroke-width="1.6" marker-end="url(#ead-arrow)"></path>
   <path d="M170 248 C230 248 240 154 300 154" fill="none" stroke="#6b7280" stroke-width="1.6" marker-end="url(#ead-arrow)"></path>
   <text x="760" y="22" text-anchor="middle">Roles inherit</text>
   <rect x="670" y="32" width="180" height="40" rx="8" fill="#ecfdf5" stroke="#059669"></rect>
   <text x="760" y="57" text-anchor="middle">T3 reader</text>
   <rect x="670" y="96" width="180" height="40" rx="8" fill="#fef3c7" stroke="#d97706"></rect>
   <text x="760" y="121" text-anchor="middle">T2 reader</text>
   <path d="M760 96 L760 72" fill="none" stroke="#6b7280" stroke-width="1.6" marker-end="url(#ead-arrow)"></path>
   <text x="768" y="88">inherits</text>
   <rect x="500" y="176" width="170" height="48" rx="8" fill="#fef3c7" stroke="#d97706"></rect>
   <text x="585" y="196" text-anchor="middle">Engineer</text>
   <text x="585" y="214" text-anchor="middle">T2 and T3</text>
   <rect x="820" y="176" width="170" height="48" rx="8" fill="#fef2f2" stroke="#dc2626"></rect>
   <text x="905" y="196" text-anchor="middle">T1 reader</text>
   <text x="905" y="214" text-anchor="middle">confidential</text>
   <path d="M585 176 C585 150 760 150 760 136" fill="none" stroke="#6b7280" stroke-width="1.6" marker-end="url(#ead-arrow)"></path>
   <path d="M905 176 C905 150 760 150 760 136" fill="none" stroke="#6b7280" stroke-width="1.6" marker-end="url(#ead-arrow)"></path>
   <rect x="820" y="260" width="170" height="48" rx="8" fill="#fef2f2" stroke="#dc2626"></rect>
   <text x="905" y="280" text-anchor="middle">Lead</text>
   <text x="905" y="298" text-anchor="middle">T1, T2, and T3</text>
   <path d="M905 260 L905 224" fill="none" stroke="#6b7280" stroke-width="1.6" marker-end="url(#ead-arrow)"></path>
   <text x="912" y="246">inherits</text>
  </svg>
 </div>
</div>

<p class="dest" id="ead-dest-swap" hidden>A tenured person on the legal team holds T1 for this one case, and can open this user's confidential intent for it.</p>
<p class="dest" id="ead-dest-use">None of those fields is the name. Together they are one person. A lead holds T1, T2, and T3. An engineer holds T2 and T3.</p>

<script>
(()=>{
 const root=document.getElementById('complex-animated-dag'),stage=root.querySelector('#ead-stage'),play=root.querySelector('#ead-play'),replay=root.querySelector('#ead-replay'),step=root.querySelector('#ead-step'),status=root.querySelector('#ead-status');
 const t3='var(--green)',t2='var(--yellow)',t1='var(--red)';
 root.querySelector('#ead-legend').innerHTML=[[t3,'T3 · Route'],[t2,'T2 · Quote'],[t1,'T1 · Intent']].map(([c,name])=>`<span><span style="color:${c}">●</span> ${name}</span>`).join('');
 const ns='http://www.w3.org/2000/svg',reduce=matchMedia('(prefers-reduced-motion: reduce)');
 let svg,edges=[],nodes=[],time=0,running=false,frame,last=0,stageIndex=-1;const duration=12000;
 function add(tag,attrs={},text){const e=document.createElementNS(ns,tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,v));if(text!==undefined)e.textContent=text;svg.appendChild(e);return e}
 function label(x,y,text){return add('text',{x,y,'text-anchor':'middle'},text)}
 function edge(x1,y1,x2,y2,color,start){const d=`M${x1} ${y1} C${(x1+x2)/2} ${y1} ${(x1+x2)/2} ${y2} ${x2} ${y2}`;add('path',{d,fill:'none',stroke:'var(--border)','stroke-width':1.3});const p=add('path',{d,fill:'none',stroke:color,'stroke-width':3});const length=p.getTotalLength();p.setAttribute('stroke-dasharray',length);const particle=add('circle',{r:5,fill:color});edges.push({p,length,particle,start,duration:3400})}
 function draw(){
  const w=stage.clientWidth;if(!w)return;const h=360;
  stage.replaceChildren();edges=[];nodes=[];svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox',`0 0 ${w} ${h}`);svg.setAttribute('role','img');svg.setAttribute('aria-label','A failed confidential swap. The route line is T3, the 1click quote is T2, and the intent is T1. They meet in 1click-manager. The on-call trace keeps T1. KYT returns passing.');stage.appendChild(svg);
  const sx=128,mx=w/2,ox=w-150;
  const yRoute=96,yQuote=188,yIntent=280,yMgr=142,yKyt=250;
  label(sx,36,'DATA');label(mx,36,'SERVICES');label(ox,36,'OUTPUTS');
  function source(y,tier,name,color){add('circle',{cx:sx,cy:y,r:20,fill:`color-mix(in srgb, ${color} 15%, var(--background))`,stroke:color,'stroke-width':2});label(sx,y+4,tier);label(sx,y+40,name)}
  source(yRoute,'T3','Route line',t3);source(yQuote,'T2','1click quote',t2);source(yIntent,'T1','Confidential intent',t1);
  function service(y,name){add('rect',{x:mx-92,y:y-26,width:184,height:52,rx:10,fill:'var(--background)',stroke:'var(--border)'});label(mx,y+4,name);const bar=add('rect',{x:mx-70,y:y+12,width:140,height:3,rx:1.5,fill:'var(--border)'});return bar}
  const mgr=service(yMgr,'1click-manager'),kyt=service(yKyt,'KYT');
  nodes.push({mark:mgr,at:3800,color:t1,kind:'bar'},{mark:kyt,at:3800,color:t1,kind:'bar'});
  function out(y,name){const mark=add('circle',{cx:ox,cy:y,r:22,fill:'var(--background)',stroke:'var(--border)','stroke-width':2});const text=label(ox,y+4,'?');label(ox,y+44,name);return {mark,text}}
  const trace=out(yMgr,'On-call trace'),result=out(yKyt,'KYT result');
  nodes.push({mark:trace.mark,text:trace.text,at:10800,color:t1,kind:'tier'},{mark:result.mark,text:result.text,at:10800,color:t3,kind:'pass'});
  edge(sx+28,yRoute,mx-92,yMgr,t3,0);edge(sx+28,yQuote,mx-92,yMgr,t2,200);edge(sx+28,yIntent,mx-92,yMgr,t1,400);edge(sx+28,yIntent,mx-92,yKyt,t1,600);
  edge(mx+92,yMgr,ox-30,yMgr,t1,5600);edge(mx+92,yKyt,ox-30,yKyt,t3,6200);
  update();
 }
 function update(){
  for(const e of edges){const p=Math.max(0,Math.min(1,(time-e.start)/e.duration));e.p.setAttribute('stroke-dashoffset',e.length*(1-p));const pt=e.p.getPointAtLength(Math.max(0,e.length*p));e.particle.setAttribute('cx',pt.x);e.particle.setAttribute('cy',pt.y);e.particle.setAttribute('visibility',p>0&&p<1?'visible':'hidden')}
  for(const n of nodes){const ready=time>=n.at;if(n.kind==='bar')n.mark.setAttribute('fill',ready?n.color:'var(--border)');else{n.mark.setAttribute('stroke',ready?n.color:'var(--border)');n.mark.setAttribute('fill',ready?`color-mix(in srgb, ${n.color} 18%, var(--background))`:'var(--background)');n.text.textContent=ready?(n.kind==='pass'?'pass':'T1'):'?'}}
  const index=time>=10800?4:time>=5600?3:time>=3800?2:time>0?1:0;
  if(index!==stageIndex){stageIndex=index;status.textContent=['Three records for one failed swap','1click-manager receives the quote and the intent','KYT is given the wallet','The trace keeps T1. KYT returns passing','The stricter label stays on the trace'][index]}
  play.textContent=running?'Pause':time>=duration?'Play again':'Play';step.disabled=time>=duration;
 }
 function stop(){running=false;cancelAnimationFrame(frame);update()}
 function start(){if(time>=duration)time=0;if(reduce.matches){time=duration;update();return}running=true;last=0;update();frame=requestAnimationFrame(tick)}
 function tick(now){if(!running)return;if(last){time+= (now-last)*2;if(time>=duration)time%=duration}last=now;update();frame=requestAnimationFrame(tick)}
 play.addEventListener('click',()=>running?stop():start());replay.addEventListener('click',()=>{stop();time=0;start()});step.addEventListener('click',()=>{stop();time=Math.min(duration,(Math.floor(time/3000)+1)*3000);update()}); document.addEventListener('visibilitychange',()=>{if(document.hidden)stop()});new ResizeObserver(draw).observe(stage);
 const toggle=document.getElementById('ead-toggle'),swapControls=document.getElementById('ead-swap-controls'),usePanel=document.getElementById('ead-use'),legend=document.getElementById('ead-legend'),hookSwap=document.getElementById('ead-hook-swap'),hookUse=document.getElementById('ead-hook-use'),destSwap=document.getElementById('ead-dest-swap'),destUse=document.getElementById('ead-dest-use');
 let showingUse=false,resume=false;
 function applyUse(on){showingUse=on;stage.hidden=on;legend.hidden=on;swapControls.hidden=on;usePanel.hidden=!on;hookSwap.hidden=on;hookUse.hidden=!on;destSwap.hidden=on;destUse.hidden=!on;toggle.textContent=on?'The swap':'Roles';toggle.setAttribute('aria-pressed',String(on))}
 function setUse(on){if(on){resume=running;stop()}applyUse(on);if(!on&&resume){resume=false;start()}}
 toggle.addEventListener('click',()=>setUse(!showingUse));
 document.addEventListener('keydown',(event)=>{if(event.key!==' '||event.altKey||event.ctrlKey||event.metaKey||event.shiftKey)return;const s=window.Reveal&&Reveal.getCurrentSlide();if(!s||s.id!=='rbac-applied')return;event.preventDefault();event.stopImmediatePropagation();setUse(!showingUse)},true);
 function show(){const s=window.Reveal&&Reveal.getCurrentSlide();if(!(s&&s.id==='rbac-applied')){stop();return}resume=false;stop();time=0;stageIndex=-1;applyUse(true)}
 window.addEventListener('load',()=>{if(!window.Reveal||!Reveal.on)return;Reveal.on('slidechanged',show);if(Reveal.isReady&&Reveal.isReady())show();else Reveal.on('ready',show)});
})();
</script>

::: notes
A partner's confidential swap fails. The route line is T3. 1click-manager has the quote, and that quote is T2. The confidential intent holds the amount, the IP, and both legs, and that is T1. The quote and the intent meet in the trace the on-call opens, and the trace keeps T1. KYT was given the wallet and returned passing. Legal sees that result. A tenured person on the legal team holds T1 for this one case, so they can open this user's confidential intent for it, and nobody else's. A role that can read 1click-manager would open every user's intents. The grant is this person, this trace, for one hour, for the label the trace still carries.

**More:**

The face opens on the two Roles pictures. Space switches to the swap, and back. The swap graph waits. Play starts it, and it loops until Pause or you leave the slide. Replay starts it again. Next stage jumps one beat: the three records, then 1click-manager receives the quote and the intent, then KYT is given the wallet, then the trace keeps T1 and KYT returns passing. The Roles pictures: on the left, first name, profession, age, and a city together name one person. On the right, T3 reader is the base and T2 reader inherits it. An engineer inherits T2, so T2 and T3. A lead inherits T1, so T1, T2, and T3. Down is the 22 Oct note. The next face is the same trace as a 1click-manager log, one T2 reader, with the amount, the IP, and the seed removed.
:::

## Review · why the relationship matters {#rbac-applied--review .vision .stay-dark .review}

<p class="kicker">Not for the room. 22 Oct. Remove before the pitch.</p>

- **Heard.** From annotated data, through data flow and control flow, through the DAG, to ReBAC. ReBAC means reasoning about access from the relationship graph. The paper stays off the face.
- **On the face now.** Title "ReBAC: defining hierarchical tiers of access" (30 Oct). The face opens on the Roles pictures; space brings the swap. The swap: one failed confidential swap. The route line is T3, the 1click quote is T2, the intent is T1. They meet in 1click-manager. The on-call trace keeps T1. KYT returns passing, and the intent rows stay behind. Roles switches to both pictures: ordinary fields arrowing into one person, and the inheritance tree: an engineer inherits T2 and T3, a lead inherits T1, T2, and T3.
- **The grant.** A role that can read 1click-manager would open every user's intents. The grant is this on-call, this one trace, for one hour. A court order is the same shape for a lawyer: this person, this one case, for a fixed time. Legal is that relationship. It is not a tier above T1.
- The seed stays on the refund slide. The name ReBAC is said once, here.

::: notes
Review slide for the 22 Oct notes. Skip it in the room.
:::
