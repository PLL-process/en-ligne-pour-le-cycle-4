#!/usr/bin/env node
/* fix_r.js — répartit les bonnes réponses d'une banque QCM écrite tout en r:0.
   Usage : node fix_r.js <fichier.html> <graine>
   - permutation DÉTERMINISTE (graine entière) ;
   - répartition équilibrée sur A/B/C/D (écart max 1) ;
   - échange o[0] <-> o[t] et d[0] <-> d[t] pour chaque question (d[r] reste "") ;
   - réécrit le bloc `const QUESTIONS = [...]` en conservant l'ordre des clés.
   Outil recréé le 24/07/2026 (l'original des LOTs 01-09 n'avait pas été commité). */
"use strict";
const fs = require("fs");
const [,, fichier, graineStr] = process.argv;
if (!fichier || !graineStr) { console.error("Usage : node fix_r.js <fichier.html> <graine>"); process.exit(1); }
const graine = parseInt(graineStr, 10);
let texte = fs.readFileSync(fichier, "utf-8");
const deb = texte.indexOf("const QUESTIONS = [");
const fin = texte.indexOf("\n];", deb);
if (deb < 0 || fin < 0) { console.error("Bloc QUESTIONS introuvable."); process.exit(1); }
const bloc = texte.slice(deb, fin + 3);
const QUESTIONS = new Function(bloc + "\nreturn QUESTIONS;")();

/* PRNG déterministe (mulberry32) + Fisher-Yates */
function mulberry32(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
const rnd = mulberry32(graine);
const n = QUESTIONS.length;
const base = Math.floor(n/4), reste = n%4;
const cibles = [];
/* répartition : les extrêmes A et D reçoivent l'arrondi supérieur (comme le LOT 08 : 8/7/7/8) */
const quotas = [base, base, base, base];
for (let i=0;i<reste;i++) quotas[i===0?0:3]++;
quotas.forEach((q,i)=>{ for(let j=0;j<q;j++) cibles.push(i); });
for (let i=cibles.length-1;i>0;i--){ const j=Math.floor(rnd()*(i+1)); [cibles[i],cibles[j]]=[cibles[j],cibles[i]]; }

const compte=[0,0,0,0];
QUESTIONS.forEach((q,i)=>{
  if (q.r !== 0) { compte[q.r]++; return; }
  const t = cibles[i];
  if (t !== 0) {
    [q.o[0], q.o[t]] = [q.o[t], q.o[0]];
    [q.d[0], q.d[t]] = [q.d[t], q.d[0]];
    q.r = t;
  }
  compte[t]++;
});

/* réécriture (ordre des clés conservé) */
const js = s => JSON.stringify(s);
function serialise(q){
  const parts = [`c:${js(q.c)}`, `n:${js(q.n)}`, `q:${js(q.q)}`];
  let tete = "{" + parts.join(",");
  let corps = q.img ? `\n img:{src:${js(q.img.src)},alt:${js(q.img.alt)}},` : "";
  corps += `\n o:[${q.o.map(js).join(",")}],r:${q.r},`;
  corps += `\n expl:${js(q.expl)},`;
  corps += `\n ex:${js(q.ex)},`;
  corps += `\n err:${js(q.err)},`;
  corps += `\n d:[${q.d.map(js).join(",")}],`;
  corps += `\n ret:${js(q.ret)}}`;
  return tete + "," + corps;
}
let sortie = "const QUESTIONS = [\n";
let derniereComp = "";
QUESTIONS.forEach(q=>{
  if (q.c !== derniereComp){ sortie += `/* ═══ ${q.c} ═══ */\n`; derniereComp = q.c; }
  sortie += serialise(q) + ",\n";
});
sortie = sortie.slice(0, -2) + "\n];";
texte = texte.slice(0, deb) + sortie + texte.slice(fin + 3);
fs.writeFileSync(fichier, texte, "utf-8");
console.log(`✔ ${fichier} : ${n} questions, répartition A/B/C/D = ${compte.join("/")}, graine ${graine}, d[r] vide partout : ` +
  QUESTIONS.every(q=>q.d[q.r]==="")); 
