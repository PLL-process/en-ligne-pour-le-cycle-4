/* Banc de la règle d'or n°311 pour 3e_C7.4 — voir banc_regle_311_theme3.mjs (relais du thème 3 vers le banc commun du thème 1).
   Vague du 04/11/2026, sur le modèle du pilote 4e_C8.1 : la page d'un seul tenant, déjà découpée en trois séances de 55 min
   (en-têtes « 🗓 Séance N », 25/10/2026), passe à trois onglets, l'ouverture dans le volet « 📖 Rappel » dès la séance 2.
   Un outil n'est pas du décor : le banc d'énergie sert aux séances 1 et 2 (activités 0 à 2). Il reste hors du volet : à la
   séance 1 dans son activité, à la séance 2 juste après l'en-tête ; à la séance 3, qui ne s'en sert pas, il n'est pas à l'écran.
   Le lien direct #seance-3 (l'en-tête de la dernière séance) ouvre la séance 3, ouverture repliée.
   Usage : node tests_regle_311_3e_C7.4.mjs [--captures <dossier>] */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';
import { lancerBanc311Theme3 } from '../../../banc_regle_311_theme3.mjs';

/* L'outil suit les séances qui s'en servent : un seul nœud ; à la séance qui porte son activité, il y reste ; à une autre
   séance qui s'en sert, il est juste après l'en-tête, après les onglets ; aux autres, il n'est pas à l'écran ; déplacé, il
   garde son état ; après rechargement, il rejoint la séance mémorisée ; sans JavaScript, il reste dans son activité.
   Vérifié ici, avant le relais et le banc commun (qui ne changent pas). */
async function outilSuitLaSeance({ page, outil, maison, seances, toutes, geste, etat, etatDurable = etat }) {
  const URL0 = pathToFileURL(path.join(import.meta.dirname, page)).href;
  let ko = 0; const t = (c, m) => { if (!c) ko++; console.log(`${c ? '✅' : '❌'} ${m}`); };
  const place = (p) => p.evaluate(([s, m]) => {
    const o = document.querySelectorAll(s), e = o[0], pan = e && e.closest('.seance-panel'), av = e && e.previousElementSibling;
    const vis = !!e && e.checkVisibility({ checkVisibilityCSS: true });
    return { n: o.length, panneau: pan ? pan.id : null, chezLui: !!e && !!e.closest('#' + m), vis,
      apresTete: !!av && av.matches('.seance-tete, .seance-entete'),
      apresOnglets: !!e && !!document.getElementById('seances') && !!(document.getElementById('seances').compareDocumentPosition(e) & Node.DOCUMENT_POSITION_FOLLOWING) };
  }, [outil, maison]);
  const b = await chromium.launch();
  const chez = await (async () => { const p = await b.newPage(); await p.goto(URL0);
    const r = await p.evaluate((m) => document.getElementById(m).closest('.seance-panel').id, maison); await p.close(); return r; })();
  for (const [w, h] of [[1280, 900], [390, 844]]) {
    const p = await b.newPage({ viewport: { width: w, height: h } }); const err = [];
    p.on('pageerror', (e) => err.push(String(e).slice(0, 80)));
    await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
    await p.click('.seance-tab[data-panel="' + chez + '"]'); await p.waitForTimeout(100);
    let l = await place(p);
    t(l.n === 1 && l.panneau === chez && l.chezLui && l.vis, `${w} px : à la séance ${chez}, l'outil (un seul nœud) est dans son activité, à l'écran`);
    await geste(p); const avant = await etat(p), durable = await etatDurable(p);
    for (const s of seances.filter((x) => x !== chez)) {
      await p.click('.seance-tab[data-panel="' + s + '"]'); await p.waitForTimeout(150);
      l = await place(p); const apres = await etat(p);
      t(l.n === 1 && l.panneau === s && l.apresTete && l.apresOnglets && l.vis, `${w} px : à la séance ${s}, il est dans la séance ${s}, juste après les onglets et l'en-tête`);
      t(JSON.stringify(avant) === JSON.stringify(apres), `${w} px : déplacé à la séance ${s}, il garde son état (${apres.join(' · ').slice(0, 80)})`);
      if (w === 1280) {
        await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(80);
        const ecran = await p.evaluate((id) => { const tete = document.querySelector('#' + id + ' .seance-tete, #' + id + ' .seance-entete').getBoundingClientRect();
          return document.getElementById('seances').getBoundingClientRect().bottom < innerHeight && tete.top < innerHeight; }, s);
        t(ecran, `1280 px : à la séance ${s}, les onglets et l'en-tête de la séance sont dans le premier écran`);
      }
    }
    for (const s of toutes.filter((x) => !seances.includes(x))) {
      await p.click('.seance-tab[data-panel="' + s + '"]'); await p.waitForTimeout(150);
      l = await place(p);
      t(l.n === 1 && !l.vis && l.chezLui, `${w} px : à la séance ${s}, qui ne s'en sert pas, l'outil n'est pas à l'écran (rangé dans son activité)`);
    }
    const derniere = seances[seances.length - 1];
    await p.click('.seance-tab[data-panel="' + derniere + '"]'); await p.waitForTimeout(150);
    await p.reload(); await p.waitForTimeout(250); l = await place(p);
    t(l.panneau === derniere && l.vis && JSON.stringify(await etatDurable(p)) === JSON.stringify(durable),
      `${w} px : après rechargement (séance ${derniere} mémorisée), l'outil est dans la séance ${derniere}, avec ce qu'il enregistre`);
    t(err.length === 0, `${w} px : aucune erreur JS ${err.join(' | ')}`);
    await p.close();
  }
  { const ctx = await b.newContext({ javaScriptEnabled: false }); const p = await ctx.newPage(); await p.goto(URL0);
    const l = await place(p);
    t(l.n === 1 && l.chezLui && l.vis, 'sans JavaScript : l\'outil reste dans son activité, à l\'écran (la page est d\'un seul tenant)');
    await ctx.close(); }
  await b.close();
  if (ko) { console.log(`\n══ l'outil ne suit pas la séance (${ko} défaut(s)) — relais non lancé ══`); process.exit(1); }
}

await outilSuitLaSeance({ page: 'sequence_3e_C7.4_energie-de-la-station.html', outil: '#outilBanc', maison: 'act0',
  seances: ['s1', 's2'], toutes: ['s1', 's2', 's3'],
  geste: async (p) => { await p.selectOption('#src', 'Accu Li-ion 18650 rechargeable'); await p.uncheck('#ck3'); await p.waitForTimeout(60); },
  etat: (p) => p.evaluate(() => [document.getElementById('src').value, String(document.getElementById('ck3').checked), document.getElementById('etot').textContent, document.getElementById('verdict').textContent.trim()]) });

/* La sécurité reste visible (retouche du 04/11/2026) : l'encadré est dans le volet, et l'en-tête de chaque séance où l'on
   manipule en rappelle la consigne en une ligne ; son lien ouvre le volet et amène l'encadré à l'écran, sans changer de séance. */
{
  const URL0 = pathToFileURL(path.join(import.meta.dirname, 'sequence_3e_C7.4_energie-de-la-station.html')).href;
  const b = await chromium.launch(); let ko = 0;
  for (const [w, h] of [[1280, 900], [390, 844]]) {
    for (const s of ['s2']) {
      const p = await b.newPage({ viewport: { width: w, height: h } });
      await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
      await p.click('.seance-tab[data-panel="' + s + '"]'); await p.waitForTimeout(150);
      const lien = '#seance-' + s.slice(1) + ' a[href="#securite"]';
      const avant = await p.evaluate((l) => { const a = document.querySelector(l), v = document.getElementById('ouverture');
        return { ligne: !!a && a.closest('p').checkVisibility() && !a.closest('#ouverture'), replie: !v.open }; }, lien);
      await p.click(lien); await p.waitForTimeout(400);
      const r = await p.evaluate(() => { const c = document.getElementById('securite').getBoundingClientRect(), v = document.getElementById('ouverture');
        return { ouvert: v.open, ecran: c.top < innerHeight && c.bottom > 0 && c.height > 0, seance: document.querySelector('.seance-panel.active').id }; });
      const ok = avant.ligne && avant.replie && r.ouvert && r.ecran && r.seance === s;
      if (!ok) ko++;
      console.log(`${ok ? '✅' : '❌'} ${w} px : séance ${s}, la ligne de sécurité est à l'écran ; son lien ouvre le volet et amène l'encadré (${JSON.stringify(r)})`);
      await p.close();
    }
  }
  await b.close();
  if (ko) { console.log(`\n══ sécurité en défaut (${ko}) — relais non lancé ══`); process.exit(1); }
}

await lancerBanc311Theme3({
  dossier: import.meta.dirname,
  page: 'sequence_3e_C7.4_energie-de-la-station.html',
  code: '3e_C7.4',
  champ: '#hyp',
  texte: 'Mon hypothèse : essai du banc 311.',
  ancreS1: 'act0',
  ancreSN: 'seance-3',
  panneauSN: 's3',
  outils: ['.toolbar', '#outilBanc'],
});
