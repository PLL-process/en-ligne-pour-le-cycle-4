/* Banc de la règle d'or n°311 pour 3e_C7.1 — voir banc_regle_311_theme3.mjs (relais du thème 3 vers le banc commun du thème 1).
   Vague du 04/11/2026, sur le modèle du pilote 4e_C8.1 (même gabarit) : la page d'un seul tenant, déjà découpée en trois séances
   de 55 min (en-têtes « 🗓 Séance N », 24-25/10/2026), passe à trois onglets, l'ouverture dans le volet « 📖 Rappel » dès la
   séance 2. Un outil n'est pas du décor : l'identité, la barre d'outils, le sélecteur de parcours et ses deux zones role=status,
   la progression et « 🗺 Où j'en suis » servent à chaque séance ; ils restent hors du volet. Le simulateur thermique ne sert qu'à
   la séance 1 (activités 0 et 2) : il reste dans son activité.
   « 🗺 Où j'en suis » (consigne de la vague) : ouvert à la séance 1, replié dès la séance 2 derrière une ligne qui garde
   l'information (« 2 / 8 activités validées »), rouvert d'un clic ou au clavier ; sans JavaScript, ouvert. Le banc mesure aussi
   le premier écran de la séance 2 : à 1280 px, les onglets et l'en-tête de la séance ; à 390 px, la position des onglets.
   Le lien direct #activite-7 (séance 3) ouvre la séance 3, ouverture repliée.
   Usage : node tests_regle_311_3e_C7.1.mjs [--captures <dossier>] */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

const PAGE = 'sequence_3e_C7_capteur-confort-ny.html';
const URL0 = pathToFileURL(path.join(import.meta.dirname, PAGE)).href;
{
  let ko = 0; const t = (c, m) => { if (!c) ko++; console.log(`${c ? '✅' : '❌'} ${m}`); };
  const b = await chromium.launch();
  const lire = (p) => p.evaluate(() => {
    const d = document.getElementById('tachesVolet'), s = d.querySelector(':scope > summary'), r = s.getBoundingClientRect();
    const tabs = document.getElementById('seances').getBoundingClientRect(), act = document.querySelector('.seance-panel.active .seance-entete').getBoundingClientRect();
    return { open: d.open, resume: s.textContent.replace(/\s+/g, ' ').trim(), haut: Math.round(r.height), ligneUnique: r.height < 60,
      liste: d.querySelector('#tachesBandeau').checkVisibility(), tabsBas: Math.round(tabs.bottom), teteHaut: Math.round(act.top), ecran: innerHeight,
      debord: document.documentElement.scrollWidth - innerWidth };
  });
  for (const [w, h] of [[1280, 900], [390, 844]]) {
    const p = await b.newPage({ viewport: { width: w, height: h } }); const err = [];
    p.on('pageerror', (e) => err.push(String(e).slice(0, 80)));
    await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
    let e = await lire(p);
    t(e.open && e.liste && /0 \/ 8 activités validées/.test(e.resume), `${w} px : séance 1, « Où j'en suis » ouvert, la liste à l'écran (« ${e.resume} »)`);
    // une activité validée : la ligne de résumé suit la liste
    await p.selectOption('#a0q1', '28 °C'); await p.selectOption('#a0q2', "s'éteint aussitôt");
    await p.evaluate(() => { window.__exp.simMontee = true; window.__exp.simDescente = true; });
    await p.click('.btn.check[data-check="0"]'); await p.waitForTimeout(80);
    await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(150);
    await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(80);
    e = await lire(p);
    t(!e.open && !e.liste && /1 \/ 8 activités validées/.test(e.resume) && e.ligneUnique && e.haut >= 44,
      `${w} px : séance 2, « Où j'en suis » replié sur une ligne de ${e.haut} px qui garde l'information (« ${e.resume} »)`);
    if (w === 1280) t(e.tabsBas < e.ecran && e.teteHaut < e.ecran, `1280 px : séance 2, les onglets (bas à ${e.tabsBas} px) et l'en-tête de la séance (haut à ${e.teteHaut} px) dans le premier écran (${e.ecran} px)`);
    else console.log(`ℹ️ 390 px : séance 2, le bas des onglets est à ${e.tabsBas} px, l'en-tête de la séance à ${e.teteHaut} px, pour un écran de ${e.ecran} px — ${e.tabsBas <= e.ecran ? 'les onglets sont dans le premier écran' : 'les onglets passent sous le premier écran'}`);
    t(e.debord <= 0, `${w} px : séance 2 sans défilement horizontal (${e.debord})`);
    await p.focus('#tachesVolet > summary'); await p.keyboard.press('Enter'); await p.waitForTimeout(60);
    e = await lire(p);
    t(e.open && e.liste, `${w} px : clavier — Entrée sur « Où j'en suis » le rouvre, la liste revient`);
    await p.keyboard.press('Space'); await p.waitForTimeout(60);
    t(!(await lire(p)).open, `${w} px : clavier — Espace le replie de nouveau`);
    await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(100);
    t((await lire(p)).open, `${w} px : retour à la séance 1 : « Où j'en suis » de nouveau ouvert`);
    await p.click('.seance-tab[data-panel="s3"]'); await p.reload(); await p.waitForTimeout(250);
    e = await lire(p);
    t(!e.open && /1 \/ 8/.test(e.resume), `${w} px : après rechargement (séance 3 mémorisée), replié, et il garde son compte`);
    t(err.length === 0, `${w} px : aucune erreur JS ${err.join(' | ')}`);
    await p.close();
  }
  { const ctx = await b.newContext({ javaScriptEnabled: false }); const p = await ctx.newPage(); await p.goto(URL0);
    const r = await p.evaluate(() => ({ open: document.getElementById('tachesVolet').open, s2: document.getElementById('s2').checkVisibility(), tabs: document.getElementById('seances').checkVisibility() }));
    t(r.open && r.s2 && !r.tabs, 'sans JavaScript : « Où j\'en suis » ouvert, les séances à la suite, pas d\'onglets');
    await ctx.close(); }
  await b.close();
  if (ko) { console.log(`\n══ « Où j'en suis » en défaut (${ko}) — relais non lancé ══`); process.exit(1); }
}

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: PAGE,
  code: '3e_C7.1',
  champ: '#hyp',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'seance-1',
  ancreSN: 'activite-7',
  panneauSN: 's3',
  outils: ['#identite', '.toolbar', '.choix-parcours-boutons', '#parcoursNote', '#savedNote', '.progress-wrap', '#taches'],
});
