/* Banc de la règle d'or n°311 pour 5e_C1.3 (C1.3-C1.4_SI) — voir ../../../banc_regle_311.mjs (le banc commun du thème 1,
   modèle : le pilote 5e_C3.1). Vague du 04/11/2026, sur le modèle du pilote 4e_C8.1 : la page d'un seul tenant, déjà écrite
   en trois cartes « Séance 1/2/3 », passe à trois séances à onglets, l'ouverture dans le volet « 📖 Rappel » dès la séance 2.
   Un outil n'est pas du décor : la barre d'outils et la carte « 💾 Sauvegarde locale » (le bouton qui efface, la zone
   role=status) restent hors du volet ; la carte reste un seul nœud et suit la séance ouverte, à sa fin.
   Avant le banc commun (qu'il ne modifie pas), ce fichier vérifie : la mission et les outils hors du volet, la place de la
   carte de sauvegarde, l'exercice incrusté des ateliers dans la séance 1 avec ses marques, le premier écran de la séance 2,
   la page sans JavaScript, le lien direct qui amène la cible à l'écran.
   Usage : node tests_regle_311_5e_C1.3.mjs [--captures <dossier>] */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import { readFileSync } from 'fs';
import path from 'path';
import { lancerBanc311 } from '../../../banc_regle_311.mjs';

const PAGE = 'sequence_C1.3-C1.4_SI_gestion_donnees.html';
const URL0 = pathToFileURL(path.join(import.meta.dirname, PAGE)).href;
const OUTILS = ['.toolbar', '#sauvegarde', '#status'];
let ko = 0; const t = (c, m) => { if (!c) ko++; console.log(`${c ? '✅' : '❌'} ${m}`); };

const src = readFileSync(path.join(import.meta.dirname, PAGE), 'utf8');
t(src.split('<!-- ateliers-representations:debut cm-5e-hangzhou-donnees -->').length === 2
  && src.split('<!-- ateliers-representations:fin cm-5e-hangzhou-donnees -->').length === 2
  && src.indexOf('ateliers-representations:debut cm-5e') < src.indexOf('ateliers-representations:fin cm-5e'),
  'les marques de l\'exercice incrusté sont intactes (une ouverture, une fermeture, dans l\'ordre)');

const b = await chromium.launch();
const lire = (p) => p.evaluate((outils) => {
  const vis = (e) => !!e && e.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true });
  const m = document.querySelector('p.subtitle'), o = document.querySelectorAll('#sauvegarde'), e = o[0];
  const pan = e && e.closest('.seance-panel'), inc = document.getElementById('incruste-cm-5e-hangzhou-donnees');
  return {
    mission: !!m && vis(m) && !m.closest('#ouverture'),
    outils: outils.filter((x) => { const q = document.querySelector(x); return !(q && vis(q) && !q.closest('#ouverture')); }),
    n: o.length, panneau: pan ? pan.id : null, enFin: !!pan && pan.lastElementChild === e,
    incruste: !!inc && !!inc.closest('#s1 #act1'),
  };
}, OUTILS);

for (const [w, h] of [[1280, 900], [390, 844]]) {
  const p = await b.newPage({ viewport: { width: w, height: h } }); const err = [];
  p.on('pageerror', (e) => err.push(String(e).slice(0, 80)));
  p.on('dialog', (d) => d.dismiss().catch(() => {}));
  await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
  const s1 = await lire(p);
  t(s1.incruste, `${w} px : l'exercice incrusté (carte mentale) est dans l'activité 1, à la séance 1`);
  t(s1.n === 1 && s1.panneau === 's1' && s1.enFin, `${w} px : au chargement, la carte de sauvegarde (un seul nœud) est à la fin de la séance 1`);
  await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(150);
  const s2 = await lire(p);
  t(s1.mission && s2.mission, `${w} px : la mission est visible hors du volet, à la séance 1 et à la séance 2`);
  t(!s1.outils.length && !s2.outils.length, `${w} px : un outil n'est pas du décor — ${OUTILS.join(', ')} hors du volet, visibles aux séances 1 et 2${[...s1.outils, ...s2.outils].length ? ' — en défaut : ' + [...new Set([...s1.outils, ...s2.outils])].join(', ') : ''}`);
  t(s2.n === 1 && s2.panneau === 's2' && s2.enFin, `${w} px : à la séance 2, la carte de sauvegarde est à la fin de la séance 2`);
  if (w === 1280) {
    await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(80);
    const ecran = await p.evaluate(() => { const tete = document.querySelector('#s2 .question-directrice').getBoundingClientRect();
      return document.getElementById('seances').getBoundingClientRect().bottom < innerHeight && tete.top < innerHeight; });
    t(ecran, '1280 px : à la séance 2, les onglets et la question directrice de la séance sont dans le premier écran');
  }
  await p.click('.seance-tab[data-panel="s3"]'); await p.waitForTimeout(150);
  const s3 = await lire(p);
  t(s3.n === 1 && s3.panneau === 's3' && s3.enFin, `${w} px : à la séance 3, la carte de sauvegarde est à la fin, après le renvoi au QCM`);
  await p.click('.seance-tab[data-panel="s2"]');
  await p.waitForFunction(() => localStorage.getItem('seq_5e_c1_3_c1_4_v2_onglet') === 's2', null, { timeout: 3000 }).catch(() => {});
  await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(250);
  const r2 = await lire(p);
  const actif = await p.evaluate(() => (document.querySelector('.seance-panel.active') || {}).id);
  t(r2.panneau === 's2' && r2.enFin, `${w} px : après rechargement (séance 2 mémorisée), la carte de sauvegarde est de nouveau à la fin de la séance 2 (séance ${actif}, carte en ${r2.panneau})`);
  t(err.length === 0, `${w} px : aucune erreur JS ${err.join(' | ')}`);
  await p.close();
}
{
  const ctx = await b.newContext({ javaScriptEnabled: false }); const p = await ctx.newPage(); await p.goto(URL0);
  const r = await p.evaluate(() => { const vis = (e) => !!e && e.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true });
    const s = document.getElementById('sauvegarde');
    return { panneaux: [...document.querySelectorAll('.seance-panel')].every(vis), onglets: vis(document.getElementById('seances')),
      suivantes: [...document.querySelectorAll('.page-suivante')].some(vis), fin: !!s && s.closest('.seance-panel').id === 's3' && vis(s) };
  });
  t(r.panneaux && !r.onglets && !r.suivantes && r.fin, 'sans JavaScript : la page reste d\'un seul tenant (les trois séances à la suite, ni onglets ni boutons de séance), la carte de sauvegarde en fin de page');
  await ctx.close();
}
{
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage();
  await p.goto(URL0 + '#act3'); await p.waitForTimeout(1300);
  const r = await p.evaluate(() => { const c = document.getElementById('act3').getBoundingClientRect(), v = document.getElementById('ouverture');
    return { ecran: c.top < innerHeight && c.bottom > 0 && c.height > 0, replie: !v.open, charge: document.readyState }; });
  t(r.ecran && r.replie && r.charge === 'complete', 'lien direct #act3 : page chargée, volet replié, la cible à l\'écran');
  await ctx.close();
}
await b.close();
if (ko) { console.log(`\n══ 5e_C1.3 : ${ko} défaut(s) avant le banc commun — banc commun non lancé ══`); process.exit(1); }

await lancerBanc311({
  dossier: import.meta.dirname,
  page: PAGE,
  code: '5e_C1.3',
  champ: '#hyp',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act1',
  ancreSN: 'act3',
  panneauSN: 's3',
});
