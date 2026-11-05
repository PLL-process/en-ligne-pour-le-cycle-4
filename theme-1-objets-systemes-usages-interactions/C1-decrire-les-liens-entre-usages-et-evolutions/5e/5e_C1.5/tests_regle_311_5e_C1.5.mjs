/* Banc de la règle d'or n°311 pour 5e_C1.5 — voir ../../../banc_regle_311.mjs (le banc commun du thème 1, modèle : le pilote 5e_C3.1).
   Vague du 04/11/2026, sur le modèle du pilote 4e_C8.1 : la page d'un seul tenant passe à trois séances à onglets, l'ouverture
   dans le volet « 📖 Rappel » dès la séance 2. Un outil n'est pas du décor : le banc de publication sert aux trois séances
   (activités 0, 1 et 2, puis le Bonus) ; il reste un seul nœud, hors du volet, et suit la séance ouverte — dans l'activité 0 à
   la séance 1, juste après l'en-tête de la séance 2 (avant l'activité 2), juste avant le Bonus à la séance 3.
   Avant le banc commun (qu'il ne modifie pas), ce fichier vérifie ce que le banc commun ne lit pas : la mission (le banc commun la lit aussi, dans
   `p.sous`), les outils hors du volet, la place et l'état du banc de publication, le premier écran de la séance 2,
   la page sans JavaScript, le lien direct qui amène la cible à l'écran.
   Usage : node tests_regle_311_5e_C1.5.mjs [--captures <dossier>] */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';
import { lancerBanc311 } from '../../../banc_regle_311.mjs';

const PAGE = 'sequence_5e_C1.5-C1.6_le-compte-du-club.html';
const URL0 = pathToFileURL(path.join(import.meta.dirname, PAGE)).href;
const OUTILS = ['.toolbar', '#etabli'];
let ko = 0; const t = (c, m) => { if (!c) ko++; console.log(`${c ? '✅' : '❌'} ${m}`); };

const b = await chromium.launch();
const lire = (p) => p.evaluate((outils) => {
  const vis = (e) => !!e && e.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true });
  const s = document.querySelector('p.sous.subtitle'), banc = document.querySelectorAll('#etabli'), e = banc[0];
  const av = e && e.previousElementSibling, ap = e && e.nextElementSibling;
  return {
    sous: !!s && vis(s) && !s.closest('#ouverture'),
    outils: outils.filter((x) => { const o = document.querySelector(x); return !(o && vis(o) && !o.closest('#ouverture')); }),
    n: banc.length, panneau: e && e.closest('.seance-panel') ? e.closest('.seance-panel').id : null,
    dansAct0: !!e && !!e.closest('#act0'), avantAct2: !!ap && ap.id === 'act2' && !!av && av.matches('.seance-tete'),
    avantBonus: !!ap && ap.id === 'bonus',
    etat: e ? [[...e.querySelectorAll('input[type=checkbox]')].filter((c) => c.checked).length, document.getElementById('img').value,
      document.getElementById('nInd').textContent, document.getElementById('nLoi').textContent, document.getElementById('verdict').children.length] : [],
    debord: document.documentElement.scrollWidth - innerWidth,
  };
}, OUTILS);

for (const [w, h] of [[1280, 900], [390, 844]]) {
  const p = await b.newPage({ viewport: { width: w, height: h } }); const err = [];
  p.on('pageerror', (e) => err.push(String(e).slice(0, 80)));
  p.on('dialog', (d) => d.dismiss().catch(() => {}));
  await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
  let s1 = await lire(p);
  t(s1.n === 1 && s1.panneau === 's1' && s1.dansAct0, `${w} px : au chargement, le banc de publication (un seul nœud) est à sa place, dans l'activité 0 de la séance 1`);
  await p.click('#charger'); await p.uncheck('#el_visage'); await p.waitForTimeout(80);
  s1 = await lire(p);
  await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(150);
  const s2 = await lire(p);
  t(s1.sous && s2.sous, `${w} px : la mission (« Ta mission : … », p.sous) est visible hors du volet, à la séance 1 et à la séance 2`);
  t(!s1.outils.length && !s2.outils.length, `${w} px : un outil n'est pas du décor — ${OUTILS.join(', ')} hors du volet, visibles aux séances 1 et 2${[...s1.outils, ...s2.outils].length ? ' — en défaut : ' + [...s1.outils, ...s2.outils].join(', ') : ''}`);
  t(s2.n === 1 && s2.panneau === 's2' && s2.avantAct2, `${w} px : à la séance 2, le banc est juste après l'en-tête de la séance, avant l'activité 2`);
  t(JSON.stringify(s1.etat) === JSON.stringify(s2.etat), `${w} px : déplacé, le banc garde son état (${s2.etat.join(' · ')})`);
  t(s2.debord <= 0, `${w} px : séance 2, le banc hors de sa carte ne déborde pas (${s2.debord})`);
  if (w === 1280) {
    await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(80);
    const ecran = await p.evaluate(() => { const tete = document.querySelector('#s2 .seance-tete').getBoundingClientRect();
      return document.getElementById('seances').getBoundingClientRect().bottom < innerHeight && tete.top < innerHeight; });
    t(ecran, '1280 px : à la séance 2, les onglets et l\'en-tête de la séance sont dans le premier écran');
  }
  await p.click('.seance-tab[data-panel="s3"]'); await p.waitForTimeout(150);
  const s3 = await lire(p);
  t(s3.n === 1 && s3.panneau === 's3' && s3.avantBonus && JSON.stringify(s3.etat) === JSON.stringify(s1.etat), `${w} px : à la séance 3, le banc est juste avant le Bonus, avec son état`);
  await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(100);
  const r1 = await lire(p);
  t(r1.panneau === 's1' && r1.dansAct0, `${w} px : retour à la séance 1, le banc retrouve sa place dans l'activité 0`);
  await p.click('.seance-tab[data-panel="s2"]');
  await p.waitForFunction(() => { try { return JSON.parse(localStorage.getItem('seq_5e_C1_5_C1_6')).onglet === 's2'; } catch (e) { return false; } }, null, { timeout: 3000 }).catch(() => {});
  await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(250);
  const r2 = await lire(p);
  const actif = await p.evaluate(() => (document.querySelector('.seance-panel.active') || {}).id);
  t(r2.panneau === 's2' && r2.avantAct2, `${w} px : après rechargement (séance 2 mémorisée), le banc est de nouveau dans la séance 2 (séance ${actif}, banc en ${r2.panneau})`);
  t(err.length === 0, `${w} px : aucune erreur JS ${err.join(' | ')}`);
  await p.close();
}
{
  const ctx = await b.newContext({ javaScriptEnabled: false }); const p = await ctx.newPage(); await p.goto(URL0);
  const r = await p.evaluate(() => { const vis = (e) => !!e && e.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true });
    return { banc: !!document.querySelector('#act0 #etabli'), panneaux: [...document.querySelectorAll('.seance-panel')].every(vis),
      onglets: vis(document.getElementById('seances')), suivantes: [...document.querySelectorAll('.page-suivante')].some(vis) }; });
  t(r.banc && r.panneaux && !r.onglets && !r.suivantes, 'sans JavaScript : la page reste d\'un seul tenant (les trois séances à la suite, ni onglets ni boutons de séance), le banc dans l\'activité 0');
  await ctx.close();
}
{
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage();
  await p.goto(URL0 + '#act4'); await p.waitForTimeout(1300);
  const r = await p.evaluate(() => { const c = document.getElementById('act4').getBoundingClientRect(), v = document.getElementById('ouverture');
    return { ecran: c.top < innerHeight && c.bottom > 0 && c.height > 0, replie: !v.open, charge: document.readyState }; });
  t(r.ecran && r.replie && r.charge === 'complete', 'lien direct #act4 : page chargée, volet replié, la cible à l\'écran');
  await ctx.close();
}
await b.close();
if (ko) { console.log(`\n══ 5e_C1.5 : ${ko} défaut(s) avant le banc commun — banc commun non lancé ══`); process.exit(1); }

await lancerBanc311({
  dossier: import.meta.dirname,
  page: PAGE,
  code: '5e_C1.5',
  champ: '#hyp',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act0',
  ancreSN: 'act4',
  panneauSN: 's3',
});
