/* Banc de la règle d'or n°311 pour 4e_C7.5 — voir banc_regle_311_theme3.mjs (relais du thème 3 vers le banc commun du thème 1).
   Vague C7 du 04/11/2026, sur le modèle du pilote 4e_C8.1 et de la vague C8 : la page d'un seul tenant passe à deux séances à
   onglets, l'ouverture dans le volet « 📖 Rappel » dès la séance 2. Un outil n'est pas du décor : l'établi sert aux deux séances
   (cas 1, puis cas 2 et 3) ; il reste hors du volet et suit la séance ouverte. À la séance 1, il reste à sa place, dans
   l'activité 1 (au-dessus de l'activité 0, il en donnerait les réponses) ; à la séance 2, il vient juste après l'en-tête.
   Le lien direct #act3 (cas 3 : la pompe ne s'arrête plus) ouvre la séance 2, ouverture repliée.
   Usage : node tests_regle_311_4e_C7.5.mjs [--captures <dossier>] */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

/* L'outil suit la séance : un seul nœud ; à la séance 1, dans son activité ; à la séance 2, juste après l'en-tête de la séance,
   avec son état ; à 1280 px, onglets et en-tête de la séance 2 dans le premier écran ; après rechargement (séance 2
   mémorisée), de nouveau dans la séance 2 ; sans JavaScript, à sa place et toutes les séances à la suite. Vérifié ici, avant
   le relais et le banc commun (qui ne changent pas). */
async function outilSuitLaSeance({ page, outil, maison, geste, etat }) {
  const URL0 = pathToFileURL(path.join(import.meta.dirname, page)).href;
  let ko = 0; const t = (c, m) => { if (!c) ko++; console.log(`${c ? '✅' : '❌'} ${m}`); };
  const place = (p) => p.evaluate(([s, m]) => {
    const o = document.querySelectorAll(s), e = o[0], pan = e && e.closest('.seance-panel'), av = e && e.previousElementSibling;
    return { n: o.length, panneau: pan ? pan.id : null, chezLui: !!e && !!e.closest(m), apresTete: !!av && av.matches('.seance-tete'),
      apresOnglets: !!e && !!(document.getElementById('seances').compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING) };
  }, [outil, maison]);
  const b = await chromium.launch();
  for (const [w, h] of [[1280, 900], [390, 844]]) {
    const p = await b.newPage({ viewport: { width: w, height: h } }); const err = [];
    p.on('pageerror', (e) => err.push(String(e).slice(0, 80)));
    await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
    let l = await place(p);
    t(l.n === 1 && l.panneau === 's1' && l.chezLui, `${w} px : au chargement, l'outil (un seul nœud) est à la séance 1, à sa place dans ${maison}`);
    await geste(p); const avant = await etat(p);
    await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(150);
    l = await place(p); const apres = await etat(p);
    t(l.n === 1 && l.panneau === 's2' && l.apresTete && l.apresOnglets, `${w} px : à la séance 2, il est dans la séance 2, après les onglets et l'en-tête`);
    t(JSON.stringify(avant) === JSON.stringify(apres), `${w} px : déplacé, il garde son état (${apres.join(' · ').slice(0, 90)})`);
    const debord = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
    t(debord <= 0, `${w} px : à la séance 2, l'outil ne fait pas défiler la page en largeur (${debord})`);
    if (w === 1280) {
      await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(80);
      const ecran = await p.evaluate(() => { const tete = document.querySelector('#s2 .seance-tete').getBoundingClientRect();
        return document.getElementById('seances').getBoundingClientRect().bottom < innerHeight && tete.top < innerHeight; });
      t(ecran, '1280 px : à la séance 2, les onglets et l\'en-tête de la séance sont dans le premier écran');
    }
    await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(120);
    l = await place(p);
    t(l.panneau === 's1' && l.chezLui, `${w} px : de retour à la séance 1, l'outil a regagné sa place dans ${maison}`);
    await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(120);
    await p.reload(); await p.waitForTimeout(250); l = await place(p);
    t(l.panneau === 's2' && l.apresTete, `${w} px : après rechargement (séance 2 mémorisée), l'outil est de nouveau dans la séance 2`);
    t(err.length === 0, `${w} px : aucune erreur JS ${err.join(' | ')}`);
    await p.close();
  }
  { const ctx = await b.newContext({ javaScriptEnabled: false }); const p = await ctx.newPage(); await p.goto(URL0);
    const l = await place(p);
    const toutes = await p.evaluate(() => [...document.querySelectorAll('.seance-panel')].every((x) => x.checkVisibility()));
    t(l.n === 1 && l.chezLui && toutes, `sans JavaScript : l'outil reste à sa place, dans ${maison}, et toutes les séances s'affichent à la suite`);
    await ctx.close(); }
  await b.close();
  if (ko) { console.log(`\n══ l'outil ne suit pas la séance (${ko} défaut(s)) — relais non lancé ══`); process.exit(1); }
}

await outilSuitLaSeance({ page: 'sequence_4e_C7.5_jardin-incomplet.html', outil: '#etabli', maison: '#act1',
  geste: async (p) => { await p.selectOption('#cas', '2'); await p.waitForTimeout(80); await p.click('#tester'); await p.waitForTimeout(80); },
  etat: (p) => p.evaluate(() => [document.getElementById('cas').value, document.getElementById('casTxt').textContent, document.getElementById('pt_relais').value, document.getElementById('budget').textContent, document.getElementById('verdict').textContent.slice(-50)]) });

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: 'sequence_4e_C7.5_jardin-incomplet.html',
  code: '4e_C7.5',
  champ: '#hyp',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act0',
  ancreSN: 'act3',
  panneauSN: 's2',
  outils: ['.toolbar', '#etabli'],
});
