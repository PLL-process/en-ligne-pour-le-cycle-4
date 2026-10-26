/* banc_regle_311.mjs — le banc commun de la règle d'or n°311 : « À partir de la séance 2, l'élève voit sa séance, pas le décor. »
   Chaque page a son fichier tests_regle_311_<code>.mjs, qui appelle lancerBanc311() avec ses propres repères (champ, ancres).
   Modèle : tests_regle_311_5e_C3.1.mjs (le pilote).

   Séance 1 : ouverture complète. Séance 2 et suivantes : titre, barre d'outils, puis le volet « 📖 Rappel : la situation et ton hypothèse », replié.
   Sans JavaScript, tout s'affiche. Un lien direct vers une ancre ouvre la bonne séance sans l'ouverture.
   À l'impression : une page qui porte la fiche papier (décision 1a de Pascal, 25/10/2026, `_outils/impression_papier/`)
   imprime la séance affichée — l'ouverture avec la séance 1, et le niveau et le code dans l'en-tête de la fiche ; une page
   sans fiche papier imprime tout (le volet ouvert, son bouton masqué).
   NB : le contenu d'un <details> fermé garde ses rectangles dans Chromium ; la visibilité se juge donc avec checkVisibility().

   Usage d'une page : node tests_regle_311_<code>.mjs [--captures <dossier>]   (séance 1, séance 2, volet ouvert ; 1280 et 390 px) */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import fs from 'fs';
import path from 'path';

// la fonction de visibilité est posée dans la page avant ses scripts, pour ne rien évaluer à partir d'un texte
const INIT = () => { window.__vis = (e) => !!e && e.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true }); };

/**
 * @param {object} o
 * @param {string} o.dossier   dossier de la page (import.meta.dirname de l'appelant)
 * @param {string} o.page      nom du fichier HTML
 * @param {string} o.code      code de la séquence (3e_C1.1…), pour les noms de captures
 * @param {string} o.champ     sélecteur d'un champ DANS l'ouverture (il doit survivre au repli et au rechargement)
 * @param {string} o.texte     texte saisi dans ce champ ('' pour une case à cocher)
 * @param {string} o.ancreS1   id d'un élément de la séance 1 (ou de l'ouverture)
 * @param {string} o.ancreSN   id d'un élément d'une séance 2 ou suivante
 * @param {string} o.panneauSN id du panneau qui contient ancreSN (s2, s3…)
 * @param {boolean} [o.titreDansVolet] la carte du titre (h1) est dans le volet : masquée dès la séance 2
 * @param {string} [o.boutonSauvegarde] sélecteur du bouton à cliquer avant de recharger, si la page n'enregistre pas toute seule
 */
export async function lancerBanc311(o) {
  const ia = process.argv.indexOf('--captures');
  const OUT = ia > 0 ? process.argv[ia + 1] : null;
  if (OUT) fs.mkdirSync(OUT, { recursive: true });
  const URL0 = pathToFileURL(path.join(o.dossier, o.page)).href;
  let ok = 0, ko = 0;
  const t = (c, m) => { if (c) { ok++; console.log('✅ ' + m); } else { ko++; console.log('❌ ' + m); } };
  const coche = o.texte === '';

  const etat = (p) => p.evaluate(() => {
    const vis = window.__vis;
    const v = document.getElementById('ouverture');
    const h2 = [...v.querySelectorAll('h2')].map(vis);
    const q = (s) => document.querySelector(s);
    return {
      open: v.open, volet: v.classList.contains('volet'), summaryVisible: vis(v.querySelector(':scope > summary')),
      h2Visibles: h2.filter(Boolean).length, h2: h2.length,
      badges: q('.badges') ? vis(q('.badges')) : null, toolbar: vis(q('.toolbar')),
      titre: vis(q('h1')), mission: q('p.sous') ? vis(q('p.sous')) : null,
      actif: q('.seance-panel.active').id, debord: document.documentElement.scrollWidth - innerWidth,
    };
  });
  const lireChamp = (p) => (coche ? p.isChecked(o.champ) : p.inputValue(o.champ));
  const saisir = (p) => (coche ? p.check(o.champ) : p.fill(o.champ, o.texte));
  const garde = (v) => (coche ? v === true : String(v).startsWith(o.texte));

  const b = await chromium.launch();
  const ids = await (async () => {
    const p = await b.newPage(); await p.goto(URL0);
    const r = await p.evaluate(() => [...document.querySelectorAll('button.seance-tab, [role="tab"]:not(a), button[data-panel]')]
      .filter((x) => !x.classList.contains('hors') && !/hors parcours/i.test(x.textContent)).map((x) => x.dataset.panel));
    await p.close(); return r;
  })();
  const S2 = ids[1], SN = ids[ids.length - 1];
  const onglet = (id) => `[data-panel="${id}"]`;

  for (const [nom, w, h] of [['1280', 1280, 900], ['390', 390, 844]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h } });
    const p = await ctx.newPage(); const err = []; await p.addInitScript(INIT);
    p.on('pageerror', (e) => err.push(String(e).slice(0, 80)));
    p.on('dialog', (d) => d.dismiss().catch(() => {}));
    await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.waitForTimeout(150);
    let e = await etat(p);
    t(e.open && !e.volet && !e.summaryVisible && e.h2Visibles === e.h2 && e.h2 > 0 && e.toolbar && e.badges !== false && e.titre,
      `${nom} px : séance 1 = ouverture complète (${e.h2Visibles}/${e.h2} titres, barre d'outils), sans volet`);
    if (OUT) await p.screenshot({ path: path.join(OUT, `${o.code}-seance1-${nom}.png`) });
    await saisir(p);
    for (const [lib, id] of [['2', S2], ['dernière', SN]]) {
      await p.click(onglet(id)); await p.waitForTimeout(150);
      e = await etat(p);
      t(e.actif === id && !e.open && e.volet && e.summaryVisible && e.h2Visibles === 0,
        `${nom} px : séance ${lib} (${id}) = volet « Rappel » replié, ouverture masquée`);
      t((o.titreDansVolet ? !e.titre : e.titre) && e.toolbar && e.mission !== false && !e.badges, `${nom} px : séance ${lib} = ${o.titreDansVolet ? 'carte de titre repliée dans le volet' : 'titre' + (e.mission === null ? '' : ', mission')}, barre d'outils visible, badges masqués`);
      t(e.debord <= 0, `${nom} px : séance ${lib} sans défilement horizontal (${e.debord})`);
      if (OUT && lib === '2') { await p.evaluate(() => scrollTo(0, 0)); await p.waitForTimeout(250); await p.screenshot({ path: path.join(OUT, `${o.code}-seance2-${nom}.png`) }); }
    }
    await p.click(onglet(S2)); await p.evaluate(() => scrollTo(0, 0));
    await p.focus('#ouverture > summary'); await p.keyboard.press('Enter'); await p.waitForTimeout(80);
    e = await etat(p);
    t(e.open && e.h2Visibles === e.h2 && e.badges !== false, `${nom} px : clavier — Entrée sur le volet l'ouvre (ouverture et badges de nouveau visibles)`);
    t(garde(await lireChamp(p)), `${nom} px : ce qui a été saisi dans l'ouverture est conservé et visible dans le volet`);
    if (OUT) await p.screenshot({ path: path.join(OUT, `${o.code}-seance2-volet-ouvert-${nom}.png`) });
    await p.keyboard.press('Space'); await p.waitForTimeout(60);
    e = await etat(p); t(!e.open && e.summaryVisible, `${nom} px : clavier — Espace referme le volet`);
    await p.click(onglet(ids[0])); e = await etat(p);
    t(e.actif === ids[0] && e.open && !e.volet && e.badges !== false && e.h2Visibles === e.h2, `${nom} px : retour à la séance 1 : ouverture complète`);
    await p.click(onglet(SN)); await p.waitForTimeout(100);
    if (o.boutonSauvegarde) { await p.click(onglet(ids[0])); await p.click(o.boutonSauvegarde); await p.waitForTimeout(100); await p.click(onglet(SN)); }
    await p.reload(); await p.waitForTimeout(200);
    e = await etat(p);
    t(e.volet === (e.actif !== ids[0]) && e.open === (e.actif === ids[0]), `${nom} px : après rechargement (séance ${e.actif}), le volet suit la séance`);
    // la sauvegarde : on revient voir le champ, quelle que soit la séance affichée
    if (e.actif !== ids[0]) await p.click(onglet(ids[0]));
    t(garde(await lireChamp(p)), `${nom} px : la sauvegarde survit au rechargement`);
    t(err.length === 0, `${nom} px : aucune erreur JS ${err.join(' | ')}`);
    await ctx.close();
  }
  {
    const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage(); await p.addInitScript(INIT);
    await p.goto(URL0 + '#' + o.ancreSN); await p.waitForTimeout(500);
    let e = await etat(p);
    t(e.actif === o.panneauSN && !e.open && e.volet, `lien direct #${o.ancreSN} : ouvre ${o.panneauSN}, ouverture repliée`);
    await p.evaluate(() => localStorage.clear());
    await p.goto(URL0 + '#' + o.ancreS1); await p.reload(); await p.waitForTimeout(700);
    e = await etat(p);
    t(e.actif === ids[0] && e.open && !e.volet, `lien direct #${o.ancreS1} : séance 1, ouverture complète`);
    await ctx.close();
  }
  {
    const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, javaScriptEnabled: false }); const p = await ctx.newPage();
    await p.goto(URL0);
    // JS coupé dans la page : pas de script d'amorce, la fonction de visibilité est donc écrite ici
    const r = await p.evaluate(() => { const vis = (e) => !!e && e.checkVisibility({ contentVisibilityAuto: true, checkVisibilityCSS: true }); const v = document.getElementById('ouverture');
      return { open: v.open, h2: [...v.querySelectorAll('h2')].every(vis), badges: document.querySelector('.badges') ? vis(document.querySelector('.badges')) : true, summary: vis(v.querySelector(':scope > summary')) }; });
    t(r.open && r.h2 && r.badges && !r.summary, 'sans JavaScript : ouverture et badges affichés, sans volet');
    await ctx.close();
  }
  {
    const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage(); await p.addInitScript(INIT);
    await p.goto(URL0); await p.evaluate(() => localStorage.clear()); await p.reload(); await p.click(onglet(SN));
    const imprimer = async () => { await p.evaluate(() => window.dispatchEvent(new Event('beforeprint'))); await p.emulateMedia({ media: 'print' }); await p.waitForTimeout(80);
      return p.evaluate(() => { const vis = window.__vis; const v = document.getElementById('ouverture'), en = document.querySelector('.pp-entete');
        //: sur la fiche papier, les blocs qui ne servent qu'à l'écran (« Avant de commencer », le référentiel…) ne
        //: s'impriment pas : on demande que l'ouverture soit là (un de ses titres au moins), pas chacun de ses blocs
        return { open: v.open, h2: [...v.querySelectorAll('h2')].every(vis), aucunH2: ![...v.querySelectorAll('h2')].some(vis),
                 badges: document.querySelector('.badges') ? vis(document.querySelector('.badges')) : true, summary: vis(v.querySelector(':scope > summary')),
                 fiche: !!en, entete: en ? vis(en) : false, surtitre: en ? en.querySelector('.pp-surtitre').textContent : '' }; }); };
    let r = await imprimer();
    if (r.fiche) {
      //: décision 1a (25/10/2026) : la fiche papier imprime la séance affichée ; l'ouverture est sur la fiche de la séance 1
      t(r.entete && !r.summary && r.aucunH2, `impression depuis ${SN} (fiche papier) : la séance seule, sans l'ouverture ni le bouton du volet`);
      await p.evaluate(() => window.dispatchEvent(new Event('afterprint'))); await p.emulateMedia({ media: 'screen' }); await p.waitForTimeout(60);
      t((await etat(p)).open === false, 'après l\'impression : le volet est replié de nouveau');
      await p.click(onglet(ids[0])); r = await imprimer();
      const niv = await p.evaluate(() => { const b = document.querySelector('.badge.niveau'), c = document.querySelector('.badge.code');
        return [b, c].filter(Boolean).map(x => x.textContent.replace(/\s+/g, ' ').trim()); });
      t(r.entete && !r.aucunH2 && !r.summary && niv.every(x => r.surtitre.includes(x)),
        `impression depuis la séance 1 (fiche papier) : l'ouverture, et l'en-tête qui porte ${niv.join(' et ') || 'le titre'}`);
      await p.emulateMedia({ media: 'screen' });
    } else {
      t(r.open && r.h2 && r.badges && !r.summary, 'impression : ouverture et badges affichés, sans le bouton du volet');
      await p.evaluate(() => window.dispatchEvent(new Event('afterprint'))); await p.waitForTimeout(60);
      t((await etat(p)).open === false, 'après l\'impression : le volet est replié de nouveau');
    }
    await ctx.close();
  }
  await b.close();
  console.log(`\n══ ${o.code} : ${ok} / ${ok + ko} tests réussis ══`);
  process.exit(ko ? 1 : 0);
}
