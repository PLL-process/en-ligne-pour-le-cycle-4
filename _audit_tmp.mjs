import { chromium } from 'playwright'; import path from 'node:path'; import { pathToFileURL } from 'node:url';
const D='theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/4e/4e_C4.1/';
const b=await chromium.launch(); const ctx=await b.newContext({viewport:{width:1280,height:900}}); const p=await ctx.newPage();
await p.goto(pathToFileURL(path.resolve(D+'sequence_4e_C4.1-C4.9_jardin_connecte.html')).href,{waitUntil:'load'}); await p.waitForTimeout(600);
const bt = await p.evaluate(()=>[...document.querySelectorAll('button')].map(b=>b.textContent.trim()).filter(t=>/mission/i.test(t)).slice(0,4));
console.log('boutons mission :', JSON.stringify(bt));
await p.evaluate(()=>{ const x=[...document.querySelectorAll('button')].find(b=>/Mode mission/i.test(b.textContent)); if(x) x.click(); }); await p.waitForTimeout(800);
console.log('mission :', await p.evaluate(()=>document.body.classList.contains('ms')));
const hs=async()=>p.evaluate(()=>[...document.querySelectorAll('h1,h2,h3,h4,h5,[class*=titre]')].filter(h=>h.offsetParent!==null && h.getBoundingClientRect().height>0).slice(0,6).map(h=>h.tagName+(h.className?'.'+String(h.className).split(' ')[0]:'')+': '+h.textContent.trim().slice(0,45)));
console.log('titres écran 1 :', JSON.stringify(await hs()));
// avancer de 3 écrans
for (let i=0;i<3;i++){ await p.evaluate(()=>{ const n=[...document.querySelectorAll('button')].find(b=>/Suivant/i.test(b.textContent)&&b.offsetParent); if(n) n.click(); }); await p.waitForTimeout(350); }
console.log('titres écran 4 :', JSON.stringify(await hs()));
const avant = await p.evaluate(()=>{ const e=document.querySelector('.ms-etape, #msEtape, [class*=ms-pos], [id*=msPos]'); return e?e.textContent.trim().slice(0,60):document.title; });
console.log('position avant :', avant);
await p.reload({waitUntil:'load'}); await p.waitForTimeout(900);
const apres = await p.evaluate(()=>{ const e=document.querySelector('.ms-etape, #msEtape, [class*=ms-pos], [id*=msPos]'); return e?e.textContent.trim().slice(0,60):'?'; });
console.log('position après rechargement :', apres, '· mission :', await p.evaluate(()=>document.body.classList.contains('ms')));
console.log('aide sur les étoiles :', await p.evaluate(()=>{ const g=document.querySelector('#msGains'); return g? (g.getAttribute('title')||'')+' | '+(g.getAttribute('aria-label')||'') : 'pas de #msGains'; }));
await b.close();
