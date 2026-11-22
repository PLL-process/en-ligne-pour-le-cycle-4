#!/usr/bin/env node
/* Banc de l'activité 2 bis de 4e_C8.1 — « La console tiendra-t-elle ? Paramétrer une simulation ».

   Écrit le 22/11/2026 avec l'activité (audit #867, chantier 6 ; « 1 oui » de Pascal). Il ne déclare que ce qu'il
   exécute, et mesure chaque effet par un nombre (règle d'or n°136) :
   ① la page calcule EXACTEMENT ce que calcule le modèle `_generation/console_jardiniere.py` (n°233), sur toute la
     grille des attendus — 5 matériaux × 8 épaisseurs × 3 longueurs × 4 charges ;
   ② l'activité ne se valide pas sans que la simulation ait été RÉGLÉE et LANCÉE (la console du club, puis au moins
     trois épaisseurs de PLA) — une activité affichée réussie l'est vraiment (n°340) ;
   ③ une mauvaise réponse n'est pas validée, et porte son pourquoi ; ④ le relevé revient après un rechargement ;
   ⑤ à 390 px, l'activité ne déborde pas.

   Usage : node tests_simulation_4e_C8.1.mjs [dossier_du_lot]                                                  */
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
const ATT = JSON.parse(fs.readFileSync(path.join(LOT, "_generation", "console_attendus.json"), "utf-8"));
const resultats = [];
const ok = (nom, cond, detail) => { resultats.push({nom, ok: !!cond, detail}); console.log((cond ? "✅ " : "❌ ") + nom + (detail ? " — " + detail : "")); };

const nav = await chromium.launch();
const ctx = await nav.newContext({viewport: {width: 1280, height: 900}});
const page = await ctx.newPage();
const erreurs = [];
page.on("pageerror", e => erreurs.push(String(e)));
await page.goto(PAGE);
await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
await page.reload();

// ① la page et le modèle disent la même chose
const ecarts = await page.evaluate(grille => grille.filter(c => {
  const r = window.simuConsole(c.materiau, c.epaisseur, c.longueur, c.charge);
  return !r || r.sigma !== c.sigma || r.k !== c.k || r.etat !== c.etat;
}).length, ATT.grille);
ok("① la page calcule comme le modèle, cas par cas", ecarts === 0, ecarts + " écart(s) sur " + ATT.grille.length + " cas");

await page.click("#tab-s2");
const coche = async (groupe, valeur) => page.evaluate(([g, v]) => {
  const r = [...document.querySelectorAll('#' + g + ' input[type=radio]')].find(x => x.value === v);
  if (!r) return false; r.click(); r.dispatchEvent(new Event("change", {bubbles: true})); return true;
}, [groupe, valeur]);
const bonnes = await page.evaluate(() => window.__bonnesSimu);
for (const [g, v] of Object.entries(bonnes)) await coche(g, v);
await page.fill("#a6dec", "Je ne valide pas la console de 6 mm : k = 0,50, plus petit que 3. Je propose 15 mm de PLA.");

// ② sans simulation lancée, l'activité ne se valide pas
await page.click('.btn.check[data-check="6"]');
let fb = (await page.textContent("#fb6")).trim();
ok("② sans simulation lancée, l'activité reste verrouillée", fb.startsWith("🔒"), fb.slice(0, 70));

const lancer = async (e, L, c) => {
  await page.check('input[name="simMat"][value="PLA imprimé en 3D"]');
  await page.fill("#simEp", String(e)); await page.fill("#simLong", String(L)); await page.fill("#simCharge", String(c));
  await page.click("#simLancer");
  return (await page.textContent("#simSortie")).trim();
};
const sortieClub = await lancer(6, 150, 11);
ok("la console du club : la simulation dit qu'elle casse, k = 0,50", /CASSE/.test(sortieClub) && /k = 45 ÷ 89,9 = 0,50/.test(sortieClub), sortieClub.slice(0, 90));
await lancer(8, 150, 11);
await page.click('.btn.check[data-check="6"]');
fb = (await page.textContent("#fb6")).trim();
ok("② deux épaisseurs essayées : toujours verrouillée", fb.startsWith("🔒") && /2\/3/.test(fb), fb.slice(0, 60));
await lancer(12, 150, 11);
const s15 = await lancer(15, 150, 11);
ok("15 mm de PLA : validée", /Validée/.test(s15), s15.slice(-60));
await page.click('.btn.check[data-check="6"]');
fb = (await page.textContent("#fb6")).trim();
ok("② réglée, lancée, répondue : l'activité est validée", fb.startsWith("🎉"), fb.slice(0, 60));
const prog = (await page.textContent("#progTxt")).trim();
ok("la progression compte l'activité 2 bis", /^1 \/ 7/.test(prog), prog);

// ③ une mauvaise réponse n'est pas validée et porte son pourquoi
await coche("a6q1", "22 kg");
await page.click('.btn.check[data-check="6"]');
fb = (await page.textContent("#fb6")).trim();
const pourquoi = await page.getAttribute('#a6q1 input[value="22 kg"]', "data-pourquoi");
ok("③ « 22 kg » n'est pas validé", !fb.startsWith("🎉"), fb.slice(0, 40));
ok("③ « 22 kg » porte son pourquoi, avec l'étape suivante", !!pourquoi && /Relis/.test(pourquoi), pourquoi || "aucun");
const pourquoiManquants = await page.evaluate(() => ["a6q1", "a6q2", "a6q3", "a6q4"].map(g => {
  const B = window.__bonnesSimu[g];
  return [...document.querySelectorAll('#' + g + ' input[type=radio]')].filter(r => r.value !== B && !r.dataset.pourquoi).length;
}).reduce((a, b) => a + b, 0));
ok("③ chaque mauvaise proposition a son pourquoi", pourquoiManquants === 0, pourquoiManquants + " sans pourquoi");

// ④ le relevé revient après un rechargement
await page.reload();
await page.click("#tab-s2");
const lignes = await page.locator("#simReleve tbody tr").count();
ok("④ le relevé des essais revient après un rechargement", lignes === 4, lignes + " ligne(s)");

// ⑤ à 390 px, rien ne déborde
const mobile = await nav.newContext({viewport: {width: 390, height: 844}, deviceScaleFactor: 2});
const pm = await mobile.newPage();
await pm.goto(PAGE + "#act2bis");
await pm.waitForTimeout(300);
const deborde = await pm.evaluate(() => {
  const a = document.getElementById("act2bis");
  return [...a.querySelectorAll("*")].filter(e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.right > window.innerWidth + 1 && !e.closest("table"); }).length;
});
ok("⑤ à 390 px, aucun élément de l'activité ne sort de l'écran (tableaux à part)", deborde === 0, deborde + " élément(s)");
ok("aucune erreur JavaScript", erreurs.length === 0, erreurs.join(" | ").slice(0, 200));

await nav.close();
const n = resultats.length, r = resultats.filter(x => x.ok).length;
console.log("\n═══ " + r + " / " + n + " tests réussis ═══");
process.exit(r === n ? 0 : 1);
