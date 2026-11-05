/* Banc de la règle d'or n°311 pour 4e_C7.1 — voir banc_regle_311_theme3.mjs (relais du thème 3 vers le banc commun du thème 1).
   Vague C7 du 04/11/2026, sur le modèle du pilote 4e_C8.1 (même gabarit : identité, mode essentiel, sélecteur de parcours,
   progression, « Où j'en suis ») : la page d'un seul tenant passe à deux séances à onglets, l'ouverture dans le volet
   « 📖 Rappel » dès la séance 2. Un outil n'est pas du décor : le sélecteur de parcours, ses deux zones role=status, la
   progression et « 🗺 Où j'en suis » servent aux deux séances ; ils restent hors du volet. Le banc météo ne sert qu'à la
   séance 1 (activité 0) : il y reste.
   « 🗺 Où j'en suis » est ouvert à la séance 1 et replié dès la séance 2, un clic le rouvre ; son résumé garde le compte
   (consigne du 04/11/2026) ; à la séance 2, les onglets et l'en-tête de la séance tiennent dans le premier écran à 1280 px,
   les onglets à 390 px.
   Le lien direct #act3 (comparer les matériaux) ouvre la séance 2, ouverture repliée.
   Usage : node tests_regle_311_4e_C7.1.mjs [--captures <dossier>] */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

const PAGE = 'sequence_4e_C7_jardin-conception.html';

async function ouJenSuis() {
  const URL0 = pathToFileURL(path.join(import.meta.dirname, PAGE)).href;
  let ko = 0; const t = (c, m) => { if (!c) ko++; console.log(`${c ? '✅' : '❌'} ${m}`); };
  const lire = (p) => p.evaluate(() => {
    const v = document.getElementById('tachesVolet'), s = v.querySelector(':scope > summary'), r = s.getBoundingClientRect();
    return { open: v.open, resume: s.textContent.replace(/\s+/g, ' ').trim(), haut: Math.round(r.height),
      liste: document.getElementById('tachesBandeau').checkVisibility(), barre: document.querySelector('.progress-wrap').checkVisibility() };
  });
  const b = await chromium.launch();
  for (const [w, h] of [[1280, 900], [390, 844]]) {
    const p = await b.newPage({ viewport: { width: w, height: h } }); const err = [];
    p.on('pageerror', (e) => err.push(String(e).slice(0, 80)));
    await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
    let e = await lire(p);
    t(e.open && e.liste && e.barre && /0 \/ 6 activités validées/.test(e.resume), `${w} px : séance 1, « Où j'en suis » ouvert, la liste visible (${e.resume})`);
    // une activité validée : le résumé suit la liste
    for (const [sel, val] of [['#simMat', 'Carton renforcé'], ['#simMeteo', "Pluie d'automne"]]) await p.selectOption(sel, val);
    await p.click('#simGo');
    await p.selectOption('#simMat', 'Plastique récupéré'); await p.click('#simGo');
    await p.selectOption('#simMat', 'Bois de palette'); await p.selectOption('#simMeteo', 'Gel de janvier'); await p.click('#simGo');
    await p.selectOption('#a0q1', 'Plastique récupéré'); await p.selectOption('#a0q2', 'La pluie');
    await p.click('.btn.check[data-check="0"]'); await p.waitForTimeout(100);
    await p.click('#tab-s2'); await p.waitForTimeout(150); await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(80);
    e = await lire(p);
    t(!e.open && !e.liste && e.barre && /1 \/ 6 activités validées/.test(e.resume) && e.haut >= 44,
      `${w} px : séance 2, « Où j'en suis » replié en une ligne qui garde le compte (${e.resume}, ${e.haut} px), la barre de progression visible`);
    const ecran = await p.evaluate(() => ({ onglets: Math.round(document.getElementById('seances').getBoundingClientRect().bottom),
      tete: Math.round(document.querySelector('#s2 .seance-tete').getBoundingClientRect().top), h: innerHeight }));
    if (w === 1280) t(ecran.onglets <= ecran.h && ecran.tete < ecran.h, `1280 px : séance 2, les onglets (bas à ${ecran.onglets} px) et l'en-tête de la séance (haut à ${ecran.tete} px) dans le premier écran`);
    else t(ecran.onglets <= ecran.h, `390 px : séance 2, les onglets dans le premier écran (bas à ${ecran.onglets} px pour ${ecran.h})`);
    await p.focus('#tachesVolet > summary'); await p.keyboard.press('Enter'); await p.waitForTimeout(60);
    e = await lire(p); t(e.open && e.liste, `${w} px : clavier — Entrée sur « Où j'en suis » le rouvre à la séance 2`);
    await p.click('#tab-s1'); await p.waitForTimeout(80); e = await lire(p);
    t(e.open, `${w} px : retour à la séance 1 : « Où j'en suis » ouvert`);
    await p.click('#tab-s2'); await p.reload(); await p.waitForTimeout(250); e = await lire(p);
    t(!e.open && /1 \/ 6/.test(e.resume), `${w} px : après rechargement à la séance 2, replié, le compte retrouvé (${e.resume})`);
    t(err.length === 0, `${w} px : aucune erreur JS ${err.join(' | ')}`);
    await p.close();
  }
  { const ctx = await b.newContext({ javaScriptEnabled: false }); const p = await ctx.newPage(); await p.goto(URL0);
    const r = await p.evaluate(() => ({ open: document.getElementById('tachesVolet').open, toutes: [...document.querySelectorAll('.seance-panel')].every((x) => x.checkVisibility()) }));
    t(r.open && r.toutes, 'sans JavaScript : « Où j\'en suis » ouvert, et toutes les séances s\'affichent à la suite');
    await ctx.close(); }
  await b.close();
  if (ko) { console.log(`\n══ « Où j'en suis » en défaut (${ko}) — relais non lancé ══`); process.exit(1); }
}

await ouJenSuis();

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: PAGE,
  code: '4e_C7.1',
  champ: '#hypothese',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act0',
  ancreSN: 'act3',
  panneauSN: 's2',
  outils: ['.choix-parcours-boutons', '#parcoursNote', '#savedNote', '.progress-wrap', '#taches'],
});
