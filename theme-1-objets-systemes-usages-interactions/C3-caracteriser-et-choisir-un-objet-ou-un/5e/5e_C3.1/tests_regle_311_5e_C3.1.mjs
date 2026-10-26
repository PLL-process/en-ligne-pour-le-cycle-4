/* Banc du pilote de la règle d'or n°311 — « À partir de la séance 2, l'élève voit sa séance, pas le décor » — sur 5e_C3.1.
   Séance 1 : ouverture complète. Séance 2 et suivantes : titre, mission, barre d'outils, puis le volet « 📖 Rappel : la situation et ton hypothèse », replié.
   Sans JavaScript, tout s'affiche. Un lien direct vers une ancre ouvre la bonne séance sans l'ouverture.
   À l'impression, la fiche papier (décision 1a de Pascal, 25/10/2026) imprime la séance affichée : l'ouverture sur la
   fiche de la séance 1, le niveau et les codes dans l'en-tête (même vérification que banc_regle_311.mjs).

   Usage : node tests_regle_311_5e_C3.1.mjs [--captures <dossier>]     (les captures : séances 1 et 3, volet ouvert, 1280 et 390 px)
   NB : le contenu d'un <details> fermé garde ses rectangles dans Chromium ; la visibilité se juge donc avec checkVisibility(). */
import { chromium } from 'playwright';
import { fileURLToPath, pathToFileURL } from 'url';
import fs from 'fs';
import path from 'path';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const URL0 = pathToFileURL(path.join(ICI, 'sequence_5e_C3.1-C3.4_shanghai.html')).href;
const ia = process.argv.indexOf('--captures');
const OUT = ia > 0 ? process.argv[ia + 1] : null;
if (OUT) fs.mkdirSync(OUT, { recursive: true });

let ok = 0, ko = 0;
const t = (c, m) => { if (c) { ok++; console.log('✅ ' + m); } else { ko++; console.log('❌ ' + m); } };
// la fonction de visibilité est posée dans la page avant ses scripts, pour ne rien évaluer à partir d'un texte
const INIT = () => { window.__vis = (e) => !!e && e.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true }); };

const etat = (p) => p.evaluate(() => {
  const vis = window.__vis;
  const v = document.getElementById('ouverture');
  const h2 = [...v.querySelectorAll('h2')].map(vis);
  return {
    open: v.open, volet: v.classList.contains('volet'), summaryVisible: vis(v.querySelector(':scope > summary')),
    h2Visibles: h2.filter(Boolean).length, h2: h2.length,
    badges: vis(document.querySelector('.badges')), toolbar: vis(document.querySelector('.toolbar')),
    titre: vis(document.querySelector('h1')), mission: vis(document.querySelector('p.sous')),
    actif: document.querySelector('.seance-panel.active').id, debord: document.documentElement.scrollWidth - innerWidth,
  };
});

const b = await chromium.launch();
for (const [nom, w, h] of [['1280', 1280, 900], ['390', 390, 844]]) {
  const ctx = await b.newContext({ viewport: { width: w, height: h } });
  const p = await ctx.newPage(); const err = []; await p.addInitScript(INIT);
  p.on('pageerror', (e) => err.push(String(e).slice(0, 80)));
  await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
  let e = await etat(p);
  t(e.open && !e.volet && !e.summaryVisible && e.h2Visibles === e.h2 && e.badges && e.toolbar, `${nom} px : séance 1 = ouverture complète (${e.h2Visibles}/${e.h2} titres, badges, barre d'outils), sans volet`);
  if (OUT) await p.screenshot({ path: path.join(OUT, `seance1-${nom}.png`) });
  await p.fill('#hyp1', 'Le vélo cargo, pour son coût sur le cycle de vie.');
  await p.click('#tab-s3'); await p.waitForTimeout(150);
  e = await etat(p);
  t(e.actif === 's3' && !e.open && e.volet && e.summaryVisible && e.h2Visibles === 0, `${nom} px : séance 3 = volet « Rappel » replié, ouverture masquée`);
  t(!e.badges, `${nom} px : séance 3 = les badges sont dans le volet, donc masqués`);
  t(e.titre && e.mission && e.toolbar, `${nom} px : séance 3 = titre, mission en une phrase et barre d'outils restent visibles`);
  await p.evaluate(() => scrollTo(0, 0));
  if (OUT) await p.screenshot({ path: path.join(OUT, `seance3-${nom}.png`) });
  await p.focus('#ouverture > summary'); await p.keyboard.press('Enter'); await p.waitForTimeout(80);
  e = await etat(p);
  t(e.open && e.h2Visibles === e.h2 && e.badges, `${nom} px : clavier — Entrée sur le volet l'ouvre (ouverture et badges de nouveau visibles)`);
  t((await p.inputValue('#hyp1')).startsWith('Le vélo cargo'), `${nom} px : l'hypothèse saisie en séance 1 est conservée et visible dans le volet`);
  if (OUT) await p.screenshot({ path: path.join(OUT, `seance3-volet-ouvert-${nom}.png`) });
  await p.keyboard.press('Enter');
  await p.click('#tab-s2'); e = await etat(p); t(e.actif === 's2' && e.volet && !e.open, `${nom} px : séance 2 : volet replié`);
  await p.click('#tab-s1'); e = await etat(p); t(e.actif === 's1' && e.open && !e.volet && e.badges, `${nom} px : retour à la séance 1 : ouverture complète`);
  t(e.debord <= 0, `${nom} px : pas de défilement horizontal (${e.debord})`);
  await p.reload(); await p.waitForTimeout(150);
  t((await p.inputValue('#hyp1')).startsWith('Le vélo cargo'), `${nom} px : la sauvegarde survit au rechargement`);
  t(err.length === 0, `${nom} px : aucune erreur JS ${err.join(' | ')}`);
  await ctx.close();
}
{
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage(); await p.addInitScript(INIT);
  const id = 'roles-5e_C3-1';
  await p.goto(URL0 + '#' + id); await p.waitForTimeout(500);
  const e = await etat(p);
  t(e.actif === 's3' && !e.open && e.volet, `lien direct #${id} : ouvre la séance 3, ouverture repliée`);
  await p.goto(URL0 + '#velo-cargo-pas-a-pas'); await p.reload(); await p.waitForTimeout(700);
  const e2 = await etat(p);
  t(e2.actif === 's1' && e2.open, 'lien direct #velo-cargo-pas-a-pas : séance 1, ouverture complète');
  await ctx.close();
}
{
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, javaScriptEnabled: false }); const p = await ctx.newPage();
  await p.goto(URL0);
  // JS coupé dans la page : pas de script d'amorce, la fonction de visibilité est donc écrite ici
  const r = await p.evaluate(() => { const vis = (e) => !!e && e.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true }); const v = document.getElementById('ouverture');
    return { open: v.open, h2: [...v.querySelectorAll('h2')].every(vis), badges: vis(document.querySelector('.badges')), summary: vis(v.querySelector(':scope > summary')) }; });
  t(r.open && r.h2 && r.badges && !r.summary, 'sans JavaScript : ouverture et badges affichés, sans volet');
  await ctx.close();
}
{
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage(); await p.addInitScript(INIT);
  await p.goto(URL0); await p.click('#tab-s3');
  const imprimer = async () => { await p.evaluate(() => window.dispatchEvent(new Event('beforeprint'))); await p.emulateMedia({ media: 'print' }); await p.waitForTimeout(80);
    return p.evaluate(() => { const vis = window.__vis; const v = document.getElementById('ouverture'), en = document.querySelector('.pp-entete');
      const niv = [document.querySelector('.badge.niveau'), document.querySelector('.badge.code')].filter(Boolean).map(x => x.textContent.replace(/\s+/g, ' ').trim());
      return { aucunH2: ![...v.querySelectorAll('h2')].some(vis), summary: vis(v.querySelector(':scope > summary')), entete: !!en && vis(en),
               niv, surtitre: en ? en.querySelector('.pp-surtitre').textContent : '' }; }); };
  let r = await imprimer();
  t(r.entete && r.aucunH2 && !r.summary, 'impression depuis s3 (fiche papier) : la séance seule, sans l\'ouverture ni le bouton du volet');
  await p.evaluate(() => window.dispatchEvent(new Event('afterprint'))); await p.emulateMedia({ media: 'screen' }); await p.click('#tab-s1');
  r = await imprimer();
  t(r.entete && !r.aucunH2 && !r.summary && r.niv.every(x => r.surtitre.includes(x)), `impression depuis la séance 1 (fiche papier) : l'ouverture, et l'en-tête qui porte ${r.niv.join(' et ')}`);
  await ctx.close();
}
await b.close();
console.log(`\n══ ${ok} / ${ok + ko} tests réussis ══`);
process.exit(ko ? 1 : 0);
