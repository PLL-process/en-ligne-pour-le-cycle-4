#!/usr/bin/env node
/* Banc de l'activité 2 ter de 4e_C8.1 — « Proposer le protocole de l'essai réel » (code 4e_C8.2).

   Écrit le 25/11/2026 avec l'activité. Il ne déclare que ce qu'il exécute, et mesure chaque effet par un nombre
   (règle d'or n°136) :
   ① la page dit ce que dit le modèle `_generation/console_jardiniere.py` (n°233) : l'épaisseur essayée, la charge
     d'essai, les paliers et les trois flèches que le calcul prévoit ;
   ② toutes les bonnes réponses ET un protocole écrit : l'activité est validée, la progression la compte ;
   ③ un protocole de deux mots ne valide pas l'activité, même avec les sept bonnes réponses ;
   ④ « jusqu'à ce qu'elle casse » (le réflexe de l'essai de traction) n'est pas validé, et chaque mauvaise proposition a son pourquoi ;
   ⑤ réponses et protocole reviennent après un rechargement ;
   ⑥ à 390 px, l'activité ne déborde pas, et aucune étiquette du schéma n'en chevauche une autre ;
   ⑦ aucune erreur JavaScript.

   Usage : node tests_protocole_4e_C8.1.mjs [dossier_du_lot]                                                   */
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";
import { pathToFileURL, fileURLToPath } from "node:url";

let chromium;
try { ({ chromium } = await import("playwright")); }
catch {
  const racineGlobale = execSync("npm root -g").toString().trim();
  ({ chromium } = createRequire(import.meta.url)(path.join(racineGlobale, "playwright", "index.js")));
}

const LOT = process.argv[2] || path.dirname(fileURLToPath(import.meta.url));
const PAGE = pathToFileURL(path.join(LOT, "sequence_4e_C8_jardin-validation.html")).href;
const ATT = JSON.parse(fs.readFileSync(path.join(LOT, "_generation", "console_attendus.json"), "utf-8")).protocole;
const resultats = [];
const ok = (nom, cond, detail) => { resultats.push({nom, ok: !!cond, detail}); console.log((cond ? "✅ " : "❌ ") + nom + (detail ? " — " + detail : "")); };
const fr = (x, d) => x.toFixed(d).replace(".", ",");
const kg = x => Number.isInteger(x) ? String(x) : fr(x, 1);

const nav = await chromium.launch();
const ctx = await nav.newContext({viewport: {width: 1280, height: 900}});
const page = await ctx.newPage();
const erreurs = [];
page.on("pageerror", e => erreurs.push(String(e)));
await page.goto(PAGE);
await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
await page.reload();
await page.click("#tab-s3");
await page.waitForTimeout(150);

// ① la page et le modèle disent la même chose
const texte = await page.evaluate(() => document.getElementById("act2ter").textContent.replace(/\s+/g, " "));
const bonnes = await page.evaluate(() => window.__bonnesProtocole);
const f = ATT.fleches.map(x => fr(x, 1) + " mm");
ok("① l'épaisseur essayée est celle que la simulation valide", texte.includes("tient à partir de " + ATT.epaisseur + " mm"), ATT.epaisseur + " mm");
ok("① la bonne charge d'essai est celle du modèle", bonnes.a7q2.startsWith(kg(ATT.charge_essai) + " kg"), bonnes.a7q2.slice(0, 30));
ok("① les paliers sont ceux du modèle", bonnes.a7q3.includes(ATT.paliers.map(kg).slice(0, 2).join(", ") + " puis " + kg(ATT.paliers[2]) + " kg"), bonnes.a7q3);
ok("① la flèche attendue à la charge d'essai est celle du calcul", bonnes.a7q5 === f[2], bonnes.a7q5 + " / " + f[2]);
ok("① la correction donne les trois flèches du calcul", f.every(x => texte.includes(x.replace(" mm", "")) ), f.join(", "));
ok("① à la charge d'essai, la console reste sous sa limite élastique (le protocole ne casse rien)",
   ATT.sigma_essai <= ATT.sigma_e && texte.includes(fr(ATT.sigma_essai, 1) + " MPa"), ATT.sigma_essai + " ≤ " + ATT.sigma_e);

const coche = async (groupe, valeur) => page.evaluate(([g, v]) => {
  const r = [...document.querySelectorAll('#' + g + ' input[type=radio]')].find(x => x.value === v);
  if (!r) return false; r.click(); r.dispatchEvent(new Event("change", {bubbles: true})); return true;
}, [groupe, valeur]);
for (const [g, v] of Object.entries(bonnes)) await coche(g, v);

// ③ sept bonnes réponses, mais un protocole de deux mots : pas validée
await page.fill("#a7prot", "On charge.");
await page.click('.btn.check[data-check="7"]');
let fb = (await page.textContent("#fb7")).trim();
ok("③ un protocole de deux mots ne valide pas l'activité", !fb.startsWith("🎉"), fb.slice(0, 50));

// ② toutes les bonnes réponses et un protocole écrit : validée
const PROTO = "① On essaie 3 consoles en PLA de 15 mm, imprimées comme celles du toit.\n" +
  "② On visse chaque console sur un montant serré à l'établi, comme sur le muret.\n" +
  "③ On accroche des sacs de 5,5 kg au bout : 11, 22 puis 33 kg, tenus 5 minutes.\n" +
  "④ À chaque palier, on mesure la flèche avec une règle graduée fixée debout.\n" +
  "⑤ Validée si aucune fissure à 33 kg, et si le bout revient à 1 mm près une fois déchargée.\n" +
  "⑥ Sécurité : lunettes, un bac sous les sacs, personne sous la charge.";
await page.fill("#a7prot", PROTO);
await page.click('.btn.check[data-check="7"]');
fb = (await page.textContent("#fb7")).trim();
ok("② sept bonnes réponses et un protocole écrit : l'activité est validée", fb.startsWith("🎉"), fb.slice(0, 50));
const prog = (await page.textContent("#progTxt")).trim();
ok("② la progression compte l'activité 2 ter", /^1 \/ 8/.test(prog), prog);

// ④ le réflexe de l'essai de traction n'est pas validé ; chaque mauvaise proposition a son pourquoi
// (26/11/2026, n°304 : il ne dit plus « comme en 5e » — l'élève n'a pas forcément fait cette 5e)
const casse = (await page.evaluate(() => [...document.querySelectorAll('#a7q2 input[type=radio]')].map(r => r.value)))
  .find(v => v.startsWith("jusqu'à ce qu'elle casse"));
await coche("a7q2", casse);
await page.click('.btn.check[data-check="7"]');
fb = (await page.textContent("#fb7")).trim();
const pq = await page.evaluate(v => [...document.querySelectorAll('#a7q2 input[type=radio]')].find(r => r.value === v).dataset.pourquoi, casse);
ok("④ « jusqu'à ce qu'elle casse » n'est pas validé", !fb.startsWith("🎉"), fb.slice(0, 40));
ok("④ son pourquoi nomme l'essai de traction et dit quoi faire", !!pq && /essai de traction/.test(pq) && /relis/i.test(pq), pq || "aucun");
const sansPourquoi = await page.evaluate(() => Object.keys(window.__bonnesProtocole).map(g => {
  const B = window.__bonnesProtocole[g];
  return [...document.querySelectorAll('#' + g + ' input[type=radio]')].filter(r => r.value !== B && !r.dataset.pourquoi).length;
}).reduce((a, b) => a + b, 0));
ok("④ chacune des 21 mauvaises propositions a son pourquoi", sansPourquoi === 0, sansPourquoi + " sans pourquoi");
await coche("a7q2", bonnes.a7q2);
await page.click('.btn.check[data-check="7"]');

// ⑤ après un rechargement
await page.reload();
await page.click("#tab-s3");
await page.waitForTimeout(150);
const garde = await page.evaluate(() => ({
  proto: document.getElementById("a7prot").value,
  coches: Object.keys(window.__bonnesProtocole).filter(g => {
    const c = document.querySelector('#' + g + ' input[type=radio]:checked');
    return c && c.value === window.__bonnesProtocole[g];
  }).length }));
ok("⑤ le protocole écrit revient après un rechargement", garde.proto === PROTO, garde.proto.length + " caractères");
ok("⑤ les sept réponses reviennent après un rechargement", garde.coches === 7, garde.coches + "/7");

// ⑥ à 390 px : rien ne déborde, les étiquettes du schéma ne se chevauchent pas
const mobile = await nav.newContext({viewport: {width: 390, height: 844}});
const pm = await mobile.newPage();
await pm.goto(PAGE);
await pm.click("#tab-s3");
await pm.waitForTimeout(250);
const mesure = await pm.evaluate(() => {
  const a = document.getElementById("act2ter");
  const visible = a.getBoundingClientRect().height > 0;
  const deborde = [...a.querySelectorAll("*")].filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.right > window.innerWidth + 1; }).length;
  const textes = [...a.querySelectorAll("svg text")].map(t => t.getBBox());
  let chevauchements = 0;
  for (let i = 0; i < textes.length; i++) for (let j = i + 1; j < textes.length; j++) {
    const p = textes[i], q = textes[j];
    if (p.x < q.x + q.width && q.x < p.x + p.width && p.y < q.y + q.height && q.y < p.y + p.height) chevauchements++;
  }
  return {visible, deborde, chevauchements, n: textes.length};
});
ok("⑥ à 390 px, l'activité est affichée (onglet de la séance 3)", mesure.visible);
ok("⑥ à 390 px, aucun élément de l'activité ne sort de l'écran", mesure.deborde === 0, mesure.deborde + " élément(s)");
ok("⑥ les étiquettes du schéma ne se chevauchent pas", mesure.chevauchements === 0, mesure.chevauchements + " chevauchement(s) sur " + mesure.n + " étiquettes");
ok("⑦ aucune erreur JavaScript", erreurs.length === 0, erreurs.join(" | ").slice(0, 200));

await nav.close();
const n = resultats.length, r = resultats.filter(x => x.ok).length;
console.log("\n═══ " + r + " / " + n + " tests réussis ═══");
process.exit(r === n ? 0 : 1);
