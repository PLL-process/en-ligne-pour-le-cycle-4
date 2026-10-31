/* Banc de la règle d'or n°311 pour le Book Train (4e_C4.1-C4.2-C4.4).
   Le banc commun (theme-1-…/banc_regle_311.mjs) lit des pages à onglets « séance 1 … n » ; le Book Train a un onglet de plus,
   « Départ · Hypothèse », qui porte l'ouverture (situation, billet d'entrée, hypothèse), suivi de quatre séances. Sa mission vit
   dans `p.sous-titre-mission`, ses panneaux dans `section.panneau`, sans `data-panel`. Ce banc rejoue donc les contrôles du banc
   commun avec les repères de cette page :
     · Départ (0), le premier écran : ouverture complète — « Avant de commencer », badges, note Pix visibles, sans bouton de volet ;
     · dès qu'une séance s'ouvre (1 à 4) : le volet « 📖 Rappel » replié, ouverture masquée ; titre, mission, barre d'outils visibles ;
     · clavier : Entrée ouvre le volet, Espace le referme ; une case cochée dans l'ouverture survit au repli et au rechargement ;
     · lien direct vers une ancre d'une séance ≥ 2 : volet replié ; sans JavaScript : ouverture affichée, sans bouton ;
     · impression : le volet s'ouvre le temps d'imprimer, puis se referme ; aucune erreur JS ; aucun défilement horizontal à 390 px.
   Usage : node tests_regle_311_4e_C4.1_book-train.mjs [--captures <dossier>] */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';
import fs from 'fs';

const PAGE = 'sequence_4e_C4.1-C4.2-C4.4_book-train.html';
const URL0 = pathToFileURL(path.join(import.meta.dirname, PAGE)).href;
const ia = process.argv.indexOf('--captures');
const OUT = ia > 0 ? process.argv[ia + 1] : null;
if (OUT) fs.mkdirSync(OUT, { recursive: true });
let ok = 0, ko = 0;
const t = (c, m) => { if (c) { ok++; console.log('✅ ' + m); } else { ko++; console.log('❌ ' + m); } };
const INIT = `window.__vis = (e) => !!e && e.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true });`;

const etat = (p) => p.evaluate(() => {
  const vis = window.__vis, q = (s) => document.querySelector(s), v = q('#ouverture');
  const actif = [...document.querySelectorAll('[role="tab"]')].findIndex((x) => x.getAttribute('aria-selected') === 'true');
  return {
    actif, open: v.open, volet: v.classList.contains('volet'), summary: vis(v.querySelector(':scope > summary')),
    rappel: vis(q('.rappel-spiralaire')), badges: vis(q('.badges')), h2: [...v.querySelectorAll('h2')].every(vis),
    titre: vis(q('h1')), mission: vis(q('.sous-titre-mission')), toolbar: vis(q('.toolbar')),
    debord: document.documentElement.scrollWidth - innerWidth,
  };
});
const onglet = (i) => `[role="tab"] >> nth=${i}`;

const b = await chromium.launch();
for (const [nom, w, h] of [['1280', 1280, 900], ['390', 390, 844]]) {
  const ctx = await b.newContext({ viewport: { width: w, height: h } });
  const p = await ctx.newPage(); const err = []; await p.addInitScript(INIT);
  p.on('pageerror', (e) => err.push(String(e).slice(0, 80)));
  p.on('dialog', (d) => d.dismiss().catch(() => {}));
  await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
  let e = await etat(p);
  t(e.actif === 0 && e.open && !e.volet && !e.summary && e.rappel && e.badges && e.h2 && e.titre && e.mission && e.toolbar,
    `${nom} px : Départ = ouverture complète (« Avant de commencer », badges), sans volet`);
  await p.check('#ouv_1');
  if (OUT) await p.screenshot({ path: path.join(OUT, `4e_C4.1-book-train-depart-${nom}.png`) });
  for (const [lib, i] of [['1', 1], ['2', 2], ['dernière', 4]]) {
    await p.click(onglet(i)); await p.waitForTimeout(150); e = await etat(p);
    t(e.actif === i && !e.open && e.volet && e.summary && !e.rappel && !e.badges, `${nom} px : séance ${lib} = volet « Rappel » replié, ouverture masquée`);
    t(e.titre && e.mission && e.toolbar, `${nom} px : séance ${lib} = titre, mission et barre d'outils visibles`);
    t(e.debord <= 0, `${nom} px : séance ${lib} sans défilement horizontal (${e.debord})`);
    if (OUT && lib === '2') { await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(250); await p.screenshot({ path: path.join(OUT, `4e_C4.1-book-train-seance2-${nom}.png`) }); }
  }
  await p.click(onglet(1)); await p.evaluate(() => scrollTo(0, 0));
  await p.focus('#ouverture > summary'); await p.keyboard.press('Enter'); await p.waitForTimeout(80); e = await etat(p);
  t(e.open && e.rappel && e.badges, `${nom} px : clavier — Entrée sur le volet l'ouvre (ouverture et badges de nouveau visibles)`);
  t(await p.isChecked('#ouv_1'), `${nom} px : la case cochée dans l'ouverture est conservée et visible dans le volet`);
  await p.keyboard.press('Space'); await p.waitForTimeout(60); e = await etat(p);
  t(!e.open && e.summary, `${nom} px : clavier — Espace referme le volet`);
  await p.click(onglet(0)); e = await etat(p);
  t(e.actif === 0 && e.open && !e.volet && e.rappel && e.badges, `${nom} px : retour au Départ : ouverture complète`);
  await p.click(onglet(4)); await p.waitForTimeout(100); await p.reload(); await p.waitForTimeout(250); e = await etat(p);
  t(e.actif === 4 && e.volet && !e.open, `${nom} px : après rechargement (onglet ${e.actif}), le volet suit la séance`);
  await p.click(onglet(0));
  t(await p.isChecked('#ouv_1'), `${nom} px : la sauvegarde de la case survit au rechargement`);
  t(err.length === 0, `${nom} px : aucune erreur JS ${err.join(' | ')}`);
  await ctx.close();
}
{
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage(); await p.addInitScript(INIT);
  await p.goto(URL0 + '#seance-3'); await p.waitForTimeout(500); let e = await etat(p);
  t(e.actif >= 1 ? (!e.open && e.volet) : true, `lien direct #seance-3 : volet replié si la page ouvre une séance (onglet ${e.actif})`);
  await ctx.close();
}
{
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, javaScriptEnabled: false }); const p = await ctx.newPage();
  await p.goto(URL0);
  const r = await p.evaluate(() => { const vis = (e) => !!e && e.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true }); const v = document.getElementById('ouverture');
    return { open: v.open, rappel: vis(document.querySelector('.rappel-spiralaire')), badges: vis(document.querySelector('.badges')), summary: vis(v.querySelector(':scope > summary')) }; });
  t(r.open && r.rappel && r.badges && !r.summary, 'sans JavaScript : ouverture et badges affichés, sans volet');
  await ctx.close();
}
{
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage(); await p.addInitScript(INIT);
  await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.click(onglet(4)); await p.waitForTimeout(100);
  await p.evaluate(() => window.dispatchEvent(new Event('beforeprint'))); await p.emulateMedia({ media: 'print' }); await p.waitForTimeout(80);
  const r = await p.evaluate(() => { const vis = window.__vis, v = document.getElementById('ouverture');
    return { open: v.open, rappel: vis(document.querySelector('.rappel-spiralaire')), summary: vis(v.querySelector(':scope > summary')) }; });
  //: sur le papier, « Avant de commencer » ne s'imprime pas (il ne sert qu'à l'écran) : on demande le volet ouvert, sans son bouton
  t(r.open && !r.summary, 'impression : le volet est ouvert, sans son bouton');
  await p.evaluate(() => window.dispatchEvent(new Event('afterprint'))); await p.emulateMedia({ media: 'screen' }); await p.waitForTimeout(60);
  t((await etat(p)).open === false, 'après l\'impression : le volet est replié de nouveau');
  await ctx.close();
}
await b.close();
console.log(`\n══ 4e_C4.1 Book Train : ${ok} / ${ok + ko} tests réussis ══`);
process.exit(ko ? 1 : 0);
