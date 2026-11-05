/* Banc de la règle d'or n°311 pour 5e_C8.1 — voir banc_regle_311_theme3.mjs (relais du thème 3 vers le banc commun du thème 1).
   Vague du 04/11/2026, sur le modèle du pilote 4e_C8.1 : la page d'un seul tenant passe à deux séances à onglets, l'ouverture
   dans le volet « 📖 Rappel » dès la séance 2. Un outil n'est pas du décor : le simulateur sert aux deux séances (activités 1
   et 2, le verrou de l'activité 3, le réinvestissement) ; il reste hors du volet et suit la séance ouverte, après son en-tête.
   Le lien direct #act3 (le banc ne disait pas la même chose) ouvre la séance 2, ouverture repliée.
   Usage : node tests_regle_311_5e_C8.1.mjs [--captures <dossier>] */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

/* L'outil suit la séance (relecture du 04/11/2026) : un seul nœud, placé juste après l'en-tête de la séance ouverte, qui
   garde son état quand on change de séance ; à la séance 2, les onglets et l'en-tête sont dans le premier écran ; sans
   JavaScript, l'outil reste au-dessus des séances. Vérifié ici, avant le relais et le banc commun (qui ne changent pas). */
async function outilSuitLaSeance({ page, outil, geste, etat }) {
  const URL0 = pathToFileURL(path.join(import.meta.dirname, page)).href;
  let ko = 0; const t = (c, m) => { if (!c) ko++; console.log(`${c ? '✅' : '❌'} ${m}`); };
  const place = (p) => p.evaluate((s) => {
    const o = document.querySelectorAll(s), e = o[0], pan = e && e.closest('.seance-panel'), av = e && e.previousElementSibling;
    return { n: o.length, panneau: pan ? pan.id : null, apresTete: !!av && av.matches('.seance-tete, .seance-entete'),
      apresOnglets: !!e && !!(document.getElementById('seances').compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING) };
  }, outil);
  const b = await chromium.launch();
  for (const [w, h] of [[1280, 900], [390, 844]]) {
    const p = await b.newPage({ viewport: { width: w, height: h } }); const err = [];
    p.on('pageerror', (e) => err.push(String(e).slice(0, 80)));
    await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
    let l = await place(p);
    t(l.n === 1 && l.panneau === 's1' && l.apresTete, `${w} px : au chargement, l'outil (un seul nœud) est dans la séance 1, juste après son en-tête`);
    await geste(p); const avant = await etat(p);
    await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(150);
    l = await place(p); const apres = await etat(p);
    t(l.n === 1 && l.panneau === 's2' && l.apresTete && l.apresOnglets, `${w} px : à la séance 2, il est dans la séance 2, après les onglets et l'en-tête`);
    t(JSON.stringify(avant) === JSON.stringify(apres), `${w} px : déplacé, il garde son état (${apres.join(' · ').slice(0, 90)})`);
    if (w === 1280) {
      await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(80);
      const ecran = await p.evaluate(() => { const tete = document.querySelector('#s2 .seance-tete, #s2 .seance-entete').getBoundingClientRect();
        return document.getElementById('seances').getBoundingClientRect().bottom < innerHeight && tete.top < innerHeight; });
      t(ecran, '1280 px : à la séance 2, les onglets et l\'en-tête de la séance sont dans le premier écran');
    }
    await p.reload(); await p.waitForTimeout(250); l = await place(p);
    t(l.panneau === 's2' && l.apresTete, `${w} px : après rechargement (séance 2 mémorisée), l'outil est de nouveau dans la séance 2`);
    t(err.length === 0, `${w} px : aucune erreur JS ${err.join(' | ')}`);
    await p.close();
  }
  { const ctx = await b.newContext({ javaScriptEnabled: false }); const p = await ctx.newPage(); await p.goto(URL0);
    const l = await place(p);
    t(l.n === 1 && l.panneau === null && !l.apresOnglets, 'sans JavaScript : l\'outil reste à sa place, au-dessus des séances');
    await ctx.close(); }
  await b.close();
  if (ko) { console.log(`\n══ l'outil ne suit pas la séance (${ko} défaut(s)) — relais non lancé ══`); process.exit(1); }
}

await outilSuitLaSeance({ page: 'sequence_5e_C8.1_patere-du-hall.html', outil: '#simuCard',
  geste: async (p) => { await p.selectOption('#mat', 'Aluminium'); await p.fill('#charge', '20'); await p.click('#ajouter'); await p.waitForTimeout(60); },
  etat: (p) => p.evaluate(() => [document.getElementById('mat').value, document.getElementById('charge').value, document.getElementById('lSigma').textContent, document.getElementById('nEssais').textContent]) });

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: 'sequence_5e_C8.1_patere-du-hall.html',
  code: '5e_C8.1',
  champ: '#hyp',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act1',
  ancreSN: 'act3',
  panneauSN: 's2',
  outils: ['.toolbar', '#simuCard'],
});
