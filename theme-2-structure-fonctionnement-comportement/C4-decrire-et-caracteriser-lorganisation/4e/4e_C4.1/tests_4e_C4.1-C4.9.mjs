/* tests_4e_C4.1-C4.9.mjs — « Le jardin connecté », rejouable.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de ce lot portait 21 coches et les attribuait à `tests_lot09.js`,
 * jamais commité. Il l'avoue depuis le 31/08/2026 ; il lui manquait la suite.
 * C'était le lot en tête de la file publiée par
 * `_outils/controle_rapports_tests.py` (règles d'or n°259 et n°266).
 *
 * CE QUE CETTE SUITE ÉPROUVE EN PROPRE
 * ------------------------------------
 * Ce lot porte **deux verrous expérientiels de natures différentes**, et c'est
 * ce qui le rend intéressant à conduire :
 *
 *   · l'explorateur de table — trois bacs à filtrer, un compteur 3/3, et
 *     l'activité 3 refusée tant que les trois n'ont pas été ouverts ;
 *   · le simulateur réseau — trois pannes à diagnostiquer, où un **mauvais**
 *     diagnostic est refusé sans faire avancer le compteur. La suite se trompe
 *     donc exprès une fois, vérifie le refus, puis répare.
 *
 * Les deux sont éprouvés dans les deux sens : l'activité est d'abord refusée
 * avec toutes les réponses justes, puis validée une fois le geste fait.
 *
 * CE QU'ELLE NE RECOPIE PAS
 * -------------------------
 * Aucune réponse attendue n'est écrite ici : elles sont extraites des fonctions
 * `CHECKS` de la page (convention `att = {id: "valeur"}`), billet d'entrée
 * compris. La bonne cause de chaque panne, et la mauvaise que la suite donne
 * exprès, sont lues dans la table `PANNES` de la page et dans les options
 * réelles du menu déroulant — un pilote de test déclare ce qu'il ne pilote pas
 * (règle d'or n°268).
 *
 * Usage, depuis ce dossier :
 *   node tests_4e_C4.1-C4.9.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

/* Règle d'or n°300 (révision de la séquence, 10/11/2026) : les questions de la page sont des groupes de boutons
   radio (fieldset.qcm-groupe) qui portent leur valeur. selectOption et fill visant un groupe cochent la
   proposition qui porte cette valeur — la leçon de la vague du 20/09 : on vise la VALEUR, jamais la
   position. Rien d'autre du banc ne change. */
function _groupesRadio(page){
  const origIV = page.inputValue.bind(page);
  page.inputValue = async (sel, ...reste) => {
    const groupe = typeof sel === 'string' && await page.evaluate(s => { const e = document.querySelector(s); return !!(e && e.tagName === 'FIELDSET' && e.classList.contains('qcm-groupe')); }, sel);
    return groupe ? page.evaluate(s => document.querySelector(s).value, sel) : origIV(sel, ...reste);
  };
  for (const nom of ['selectOption', 'fill']) {
    const orig = page[nom].bind(page);
    page[nom] = async (sel, val, ...reste) => {
      const groupe = typeof sel === 'string' && await page.evaluate(s => { const e = document.querySelector(s); return !!(e && e.tagName === 'FIELDSET' && e.classList.contains('qcm-groupe')); }, sel);
      if (!groupe) return orig(sel, val, ...reste);
      // comme Playwright sur un <select> : une chaîne vise la valeur OU le libellé ; {index}, {value}, {label} sont acceptés
      const v = (val && typeof val === 'object') ? val : { label: String(val), value: String(val) };
      const ok = await page.evaluate(([s, v]) => {
        const e = document.querySelector(s); const inputs = [...e.querySelectorAll('input[type=radio]')];
        const lib = i => (e.querySelector('label[for="' + i.id + '"]') || {}).textContent?.trim();
        const c = v.index !== undefined ? inputs[v.index]
          : inputs.find(i => i.value === v.value) || inputs.find(i => lib(i) === v.label);
        if (!c) return false;
        c.checked = true; c.dispatchEvent(new Event('change', {bubbles: true})); return true;
      }, [sel, v]);
      if (!ok) throw new Error('aucune proposition \u00ab ' + JSON.stringify(v) + ' \u00bb dans ' + sel);
    };
  }
  return page;
}
import fs from 'node:fs';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const SEQ = path.join(ICI, 'sequence_4e_C4.1-C4.9_jardin_connecte.html');
const QCM = path.join(ICI, 'qcm_4e_C4.1-C4.9_jardin_connecte.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ SÉQUENCE (21 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = _groupesRadio(await ctx.newPage());
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => { if (!/fonts\.g/.test(r.url())) fail.push(r.url()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

await p.goto(pathToFileURL(SEQ).href, { waitUntil: 'load' });
// Révision du 10/11/2026 : Bonus et exercice incrusté sont repliés ; le banc ouvre les volets.
await p.evaluate(() => document.querySelectorAll('details.bonus-replie, details.incruste-repliee').forEach(d => { d.open = true; }));
await p.waitForTimeout(340);

const texte = (await p.textContent('body')).replace(/\s+/g, ' ');
ok('1 · chargement, titre « Le jardin connecté » et les codes du lot en tête',
   /jardin connecté/i.test(await p.title())
   && texte.includes('4e_C4.1') && /4e_C4\.9|C4\.9/.test(texte));

const onglets = await p.$$eval('.seance-tab', l => l.map(e => e.dataset.panel));
await p.click('.seance-tab[data-panel="s4"]'); await p.waitForTimeout(120);
const s4 = await p.$eval('#s4', e => e.classList.contains('active'));
await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(120);
ok(`2 · ${onglets.length} onglets de séance, bascule vers S4 puis retour S1`,
   onglets.length === 4 && s4 && await p.$eval('#s1', e => e.classList.contains('active')),
   onglets.join('|'));

ok('3 · aucune expérience enregistrée au chargement — les deux verrous sont fermés (n°226)',
   Object.keys(await p.evaluate(() => window.__exp || {}))
     .filter(k => k !== 'mode_essentiel').length === 0,
   JSON.stringify(await p.evaluate(() => window.__exp)));

/* ── les réponses attendues, LUES dans la page ───────────────────────────── */
const ATT = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const m = CHECKS[n].toString().match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    out[n] = m ? eval('(' + m[1] + ')') : {};
  }
  return out;
});
const champs = Object.values(ATT).reduce((s, o) => s + Object.keys(o).length, 0);
ok(`4 · ${champs} champs attendus extraits des CHECKS de la page, billet d'entrée compris`,
   Object.keys(ATT).length === 6 && champs >= 30, String(champs));

const ONGLETS = onglets;
async function ouvrirPour(id) {
  if (await p.isVisible('#' + id).catch(() => false)) return true;
  for (const panneau of ONGLETS) {
    await p.click(`.seance-tab[data-panel="${panneau}"]`);
    await p.waitForTimeout(90);
    if (await p.isVisible('#' + id).catch(() => false)) return true;
  }
  return false;
}
async function remplir(n) {
  for (const [id, v] of Object.entries(ATT[n])) {
    if (!(await ouvrirPour(id))) continue;
    const el = await p.$('#' + id); if (!el) continue;
    const tag = await el.evaluate(e => e.tagName);
    if (tag === 'SELECT') await p.selectOption('#' + id, v);
    else if (tag === 'FIELDSET') await p.selectOption('#' + id, v); // n°300 (10/11/2026) : groupe de boutons radio, via le shim
    else await p.fill('#' + id, v);
  }
}
const valider = async n => {
  await ouvrirPour(Object.keys(ATT[n])[0]);
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(90);
};
const retour = n => p.textContent('#fb' + n);
const valide = n => p.evaluate(k => !!window.__valid[k], String(n));

/* ── le billet d'entrée : il oriente, il ne sanctionne pas ───────────────── */
await p.click('[data-check="0"]'); await p.waitForTimeout(90);
const billetVide = await retour(0);
await remplir(0); await valider(0);
ok('5 · billet d\'entrée : il réclame d\'abord les réponses manquantes, puis rend 3 / 3',
   /restante/i.test(billetVide) && /3 \/ 3/.test(await retour(0)),
   billetVide.slice(0, 45) + ' → ' + (await retour(0)).slice(0, 45));
/* Le billet oriente, il ne sanctionne pas : la page le dit dans son code, et
   la conséquence observable est qu'il n'entre PAS dans les cinq activités. */
ok('5 bis · le billet fait ne compte pas comme une activité validée — la progression reste 0 / 5',
   (await p.textContent('#progTxt')).includes('0 / 5')
   && await p.evaluate(() => !!window.__exp.billet_fait),
   await p.textContent('#progTxt'));

await remplir(1); await valider(1);
ok('6 · activité 1 validée 9 / 9 (chaîne d\'énergie : alimenter, stocker, distribuer, convertir)',
   /9 \/ 9/.test(await retour(1)) && await valide(1), (await retour(1)).slice(0, 60));

await remplir(2); await valider(2);
ok('7 · activité 2 validée 4 / 4 (chaîne d\'information : acquérir, traiter, communiquer)',
   /4 \/ 4/.test(await retour(2)) && await valide(2), (await retour(2)).slice(0, 60));

/* ── VERROU 1 : l'explorateur de table ───────────────────────────────────── */
await remplir(3); await valider(3);
ok('8 · activité 3 REFUSÉE malgré 6 réponses justes — les trois bacs ne sont pas explorés',
   /6 \/ 6/.test(await retour(3)) && /Explore VRAIMENT les 3 bacs/.test(await retour(3))
   && !(await valide(3)), (await retour(3)).slice(0, 75));

const BACS = await p.$$eval('.bacbtn', l => l.map(e => e.dataset.bac));
await ouvrirPour('bacCompteur');
await p.click(`.bacbtn[data-bac="${BACS[0]}"]`); await p.waitForTimeout(70);
const unBac = await p.textContent('#bacCompteur');
const texteBac = await p.textContent('#bacTxt');
ok(`9 · un bac filtré affiche sa requête et ses mesures, compteur « ${unBac.trim()} »`,
   unBac.includes('1 / 3') && /SELECT|WHERE/.test(texteBac)
   && !(await p.evaluate(() => !!window.__exp.table)), texteBac.slice(0, 60));

for (const bac of BACS.slice(1)) {
  await p.click(`.bacbtn[data-bac="${bac}"]`); await p.waitForTimeout(70);
}
ok(`10 · les ${BACS.length} bacs explorés → compteur 3 / 3 et verrou __exp.table posé`,
   (await p.textContent('#bacCompteur')).includes('3 / 3')
   && await p.evaluate(() => !!window.__exp.table), await p.textContent('#bacCompteur'));

await valider(3);
ok('11 · activité 3 validée 6 / 6 une fois la table réellement explorée',
   /6 \/ 6/.test(await retour(3)) && !/Explore VRAIMENT/.test(await retour(3))
   && await valide(3), (await retour(3)).slice(0, 60));

/* ── VERROU 2 : le simulateur réseau, où l'on se trompe exprès ───────────── */
await remplir(4); await valider(4);
ok('12 · activité 4 REFUSÉE malgré 4 réponses justes — les pannes ne sont pas résolues',
   /4 \/ 4/.test(await retour(4)) && /Résous les 3 pannes/.test(await retour(4))
   && !(await valide(4)), (await retour(4)).slice(0, 75));

/* La bonne cause de chaque panne est lue dans la page ; la mauvaise que l'on
   donne exprès est prise dans les options réelles du menu, jamais écrite ici. */
const CAUSES = await p.evaluate(() => {
  const bonnes = Object.fromEntries(Object.entries(PANNES).map(([k, v]) => [k, v.cause]));
  const offertes = [...document.querySelectorAll('#causeSel option, #causeSel input[type=radio]')] // n°300 (10/11/2026) : boutons radio
    .map(o => o.value).filter(Boolean);
  return { bonnes, offertes };
});
const pannes = await p.$$eval('.pannebtn', l => l.map(e => e.dataset.panne));
await ouvrirPour('panneEtat');
await p.click(`.pannebtn[data-panne="${pannes[0]}"]`); await p.waitForTimeout(70);
const symptomes = await p.textContent('#panneTxt');
const mauvaise = CAUSES.offertes.find(c => c !== CAUSES.bonnes[pannes[0]]);
await p.selectOption('#causeSel', mauvaise);
await p.click('#btnCause'); await p.waitForTimeout(70);
ok(`13 · un mauvais diagnostic (« ${mauvaise} ») est refusé, et le compteur ne bouge pas`,
   /❌/.test(await p.textContent('#panneTxt'))
   && (await p.textContent('#panneEtat')).includes('0 / 3')
   && !(await p.evaluate(() => !!window.__exp.reseau)),
   (await p.textContent('#panneTxt')).slice(0, 60));
ok('13 bis · les symptômes de la panne sont bien affichés avant le diagnostic',
   /SYMPTÔMES/.test(symptomes), symptomes.slice(0, 60));

for (const panne of pannes) {
  await p.click(`.pannebtn[data-panne="${panne}"]`); await p.waitForTimeout(60);
  await p.selectOption('#causeSel', CAUSES.bonnes[panne]);
  await p.click('#btnCause'); await p.waitForTimeout(60);
}
ok(`14 · les ${pannes.length} pannes réparées → « réseau réparé » et verrou __exp.reseau posé`,
   /3 \/ 3/.test(await p.textContent('#panneEtat'))
   && await p.evaluate(() => !!window.__exp.reseau), await p.textContent('#panneEtat'));

await valider(4);
ok('15 · activité 4 validée 4 / 4 une fois les trois pannes diagnostiquées',
   /4 \/ 4/.test(await retour(4)) && !/Résous les 3 pannes/.test(await retour(4))
   && await valide(4), (await retour(4)).slice(0, 60));

/* ── activité 5 : l'exercice d'atelier incrusté en tête (cahier des charges, flexibilité) ──
   Ses bonnes réponses sont LUES dans la définition JSON de sa section ; seul le texte de
   l'exigence est écrit ici (c'est le champ `exemple` de sa définition d'atelier). */
async function remplirIncruste(uid, textes = {}) {
  await p.evaluate(({ uid, textes }) => {
    const sec = document.getElementById(uid).closest('.atelier-incruste');
    const D = JSON.parse(sec.querySelector('script[type="application/json"]').textContent).exercices[uid];
    const coche = (name, v) => [...document.getElementsByName(name)].find(r => r.value === v).click();
    for (const w of D.widgets) {
      if (w.type === 'choix') coche(w.name, w.bonne);
      else if (w.type === 'classer') w.items.forEach(it => coche(it.name, it.bonne));
      else if (w.type === 'slots') w.slots.forEach(s => coche(s.name, s.bonnes[0]));
      else if (w.type === 'cases') w.bonnes.forEach(v => coche(w.name, v));
      /* le cahier des charges à menus (règle d'or n°317) : chaque case reçoit sa bonne
         option, lue dans la définition, comme le ferait l'élève (événement change) */
      else if (w.type === 'tableau') w.cases.forEach(c => {
        const s = document.getElementsByName(c.name)[0];
        s.value = c.bonne; s.dispatchEvent(new Event('change', { bubbles: true }));
      });
      else if (w.type === 'texte') {
        const t = document.getElementById(w.name);
        t.value = textes[w.name]; t.dispatchEvent(new Event('input', { bubbles: true }));
      }
    }
  }, { uid, textes });
}
await remplir(5); await valider(5);
ok('15 bis · activité 5 REFUSÉE malgré 6 réponses justes — l\'exercice du cahier des charges n\'est pas réussi',
   /6 \/ 6/.test(await retour(5)) && /cahier des charges/.test(await retour(5)) && !(await valide(5)),
   (await retour(5)).slice(0, 120));
await p.click('#pv_4e_e6 button.verifier'); await p.waitForTimeout(80);
ok('15 ter · l\'exercice du cahier des charges inséré se vérifie à vide (retour à reprendre)',
   (await p.textContent('#pv_4e_e6 .retour')).includes('🔴'),
   (await p.textContent('#pv_4e_e6 .retour')).slice(0, 70));
/* Une case fausse exprès : la première option qui a son propre retour, lue dans la définition.
   Son retour s'écrit SOUS la case, en texte (✘ + pourquoi), pas seulement en couleur (n°119, n°317). */
{
  const faux = await p.evaluate(() => {
    const sec = document.getElementById('pv_4e_e6').closest('.atelier-incruste');
    const D = JSON.parse(sec.querySelector('script[type="application/json"]').textContent).exercices.pv_4e_e6;
    const c = D.widgets.find(w => w.type === 'tableau').cases.find(x => Object.keys(x.retours || {}).length);
    const v = Object.keys(c.retours)[0];
    const s = document.getElementsByName(c.name)[0];
    s.value = v; s.dispatchEvent(new Event('change', { bubbles: true }));
    return { name: c.name, attendu: c.retours[v] };
  });
  await p.click('#pv_4e_e6 button.verifier'); await p.waitForTimeout(80);
  const ecrit = await p.evaluate(n => {
    const r = document.getElementById(n + '-retour'), td = r.closest('td');
    return { texte: r.textContent, visible: r.offsetHeight > 0, encoche: td.querySelector('.encoche').textContent,
             lie: document.getElementById(n).getAttribute('aria-describedby') === n + '-retour' };
  }, faux.name);
  ok('15 ter bis · une case fausse du tableau : son retour est écrit sous la case (✘ et pourquoi), relié au menu',
     ecrit.visible && ecrit.texte.startsWith('✘') && ecrit.texte.includes(faux.attendu.slice(0, 30))
     && /à revoir/.test(ecrit.encoche) && ecrit.lie,
     ecrit.texte.slice(0, 70));
}
await remplirIncruste('pv_4e_e6', {
  pv_4e_e6__exig: "Le système doit envoyer l'état de l'arrosage au smartphone au moins 1 fois par jour." });
await p.click('#pv_4e_e6 button.verifier'); await p.waitForTimeout(80);
ok('15 quater · l\'exercice du cahier des charges inséré, rempli juste (F0 à F3 compris), est réussi',
   (await p.textContent('#pv_4e_e6 .retour')).includes('Tout est juste'),
   (await p.textContent('#pv_4e_e6 .retour')).slice(0, 70));
await valider(5);
ok('16 · activité 5 validée 6 / 6 (forme et procédé : 3D, injection, laser, perçage)',
   /6 \/ 6/.test(await retour(5)) && await valide(5), (await retour(5)).slice(0, 60));

ok('17 · progression 5 / 5 activités, et les quatre onglets portent leur coche',
   (await p.textContent('#progTxt')).includes('5 / 5')
   && (await p.$$eval('[id^="done-s"]', l => l.map(e => e.textContent.trim())))
        .every(c => c === '✔'),
   await p.textContent('#progTxt'));

/* ── persistance ─────────────────────────────────────────────────────────── */
await p.reload({ waitUntil: 'load' }); await p.evaluate(() => document.querySelectorAll('details.bonus-replie, details.incruste-repliee').forEach(d => { d.open = true; })); await p.waitForTimeout(340);
const premier = Object.keys(ATT[1])[0];
ok('18 · rechargement : réponses, validations ET les deux verrous sont restaurés',
   (await p.inputValue('#' + premier)) === ATT[1][premier]
   && (await p.textContent('#progTxt')).includes('5 / 5')
   && await p.evaluate(() => !!window.__exp.table && !!window.__exp.reseau),
   await p.textContent('#progTxt'));
{
  /* Depuis la règle d'or n°317, le cahier des charges se complète dans le tableau : 22 menus
     `pv_4e_e6__cdcf_<ligne>_<colonne>`, plus le choix « IPX4 vient… » (1 bouton radio). Chaque
     menu doit retrouver sa bonne option, et l'afficher en texte dans sa case. */
  const etat = await p.evaluate(() => {
    const sec = document.getElementById('pv_4e_e6').closest('.atelier-incruste');
    const D = JSON.parse(sec.querySelector('script[type="application/json"]').textContent).exercices.pv_4e_e6;
    const t = D.widgets.find(w => w.type === 'tableau');
    const sels = [...document.querySelectorAll('#pv_4e_e6 select[name^="pv_4e_e6__cdcf_"]')];
    return {
      radios: document.querySelectorAll('#pv_4e_e6 input[type=radio]:checked').length,
      menus: sels.length,
      justes: t.cases.filter(c => document.getElementsByName(c.name)[0].value === c.bonne).length,
      vus: sels.filter(s => s.parentNode.querySelector('.menu-vu').textContent.trim()
                            === s.options[s.selectedIndex].text.trim() && s.value).length,
      noms: sels.every(s => /^pv_4e_e6__cdcf_\d+_\d+$/.test(s.name)),
    };
  });
  const exig = await p.inputValue('#pv_4e_e6__exig');
  ok('18 ter · l\'exercice du cahier des charges retrouve au rechargement ses 22 menus (affichés en texte), son choix et son exigence',
     etat.radios === 1 && etat.menus === 22 && etat.justes === 22 && etat.vus === 22 && etat.noms
     && /smartphone/.test(exig),
     `${etat.radios} choix · ${etat.justes}/${etat.menus} menus justes · ${etat.vus} affichés · ` + exig.slice(0, 30));
}
{
  /* Sur le papier : les 22 choix s'impriment en texte, sans la liste des options que la fiche papier
     ajoute sous chaque menu (retirée par la page tant que le kit des ateliers ne le fait pas). */
  await p.click('.seance-tab[data-panel="s4"]'); await p.waitForTimeout(100);
  await p.evaluate(() => window.dispatchEvent(new Event('beforeprint')));
  await p.emulateMedia({ media: 'print' }); await p.waitForTimeout(120);
  const papier = await p.evaluate(() => {
    const vis = e => getComputedStyle(e).display !== 'none' && e.offsetHeight > 0;
    const t = document.querySelector('#pv_4e_e6 .tableau-menus');
    return { listes: [...t.querySelectorAll('.pp-choix')].filter(vis).length,
             menus: [...t.querySelectorAll('select')].filter(vis).length,
             textes: [...t.querySelectorAll('.menu-vu')].filter(v => vis(v) && v.textContent.trim()).length };
  });
  await p.emulateMedia({ media: 'screen' });
  ok('18 quater · le cahier des charges imprimé : les 22 choix en texte, ni menu ni liste d\'options',
     papier.listes === 0 && papier.menus === 0 && papier.textes === 22, JSON.stringify(papier));
}
ok('18 bis · les compteurs des deux simulateurs repartent à 3 / 3 après rechargement',
   (await p.textContent('#bacCompteur')).includes('3 / 3')
   && (await p.textContent('#panneEtat')).includes('3 / 3'),
   (await p.textContent('#bacCompteur')) + ' · ' + (await p.textContent('#panneEtat')));

const corps = (await p.textContent('body')).replace(/\s+/g, ' ');
ok('19 · les blocs « Prêt·e » et « Bonus » sont là, et un seul bouton mène au QCM',
   /Prêt/i.test(corps) && /Bonus|🎁/i.test(corps)
   && (await p.$$eval('a[href*="qcm_4e_C4.1"]', a => a.filter(x => /btn/.test(x.className)).length))
      === 1);

/* Le bouton du QCM débordait de son bloc dans le gabarit hérité : on mesure. */
const deborde = await p.$$eval('a[href*="qcm"], a[href*="atelier"]', liens => liens
  .filter(a => /btn/.test(a.className))
  .map(a => ({ t: a.textContent.trim().slice(0, 24), d: a.scrollWidth - a.clientWidth })));
ok(`20 · les ${deborde.length} boutons de fin de bilan tiennent dans leur largeur (390 px)`,
   deborde.length > 0 && deborde.every(x => x.d <= 1),
   deborde.map(x => x.t + ':' + x.d).join(' · '));

const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok(`21 · les ${liens.length} liens internes existent, y compris vers 4e_C4.7 et 4e_C6.2`,
   casses.length === 0, casses.slice(0, 3).join(' · '));

const svg = await p.$$eval('img[src$=".svg"], object[data$=".svg"]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('data')));
const svgAbsents = svg.filter(s => !fs.existsSync(path.join(ICI, s)));
ok(`22 · les ${svg.length} SVG référencés existent sur le disque`,
   svgAbsents.length === 0, svgAbsents.join(' · '));

const distantes = await p.$$eval('[src], link[href], object[data], iframe[src]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('href') || e.getAttribute('data'))
        .filter(u => u && /^(https?:)?\/\//i.test(u)));
ok('23 · hors ligne : aucune ressource distante, aucune modale, aucune erreur JS',
   distantes.length === 0 && dlg.length === 0 && fail.length === 0 && err.length === 0,
   (distantes[0] || err[0] || fail[0] || dlg[0] || '').slice(0, 80));
await ctx.close();
}

/* ════════════════ QCM (9 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = _groupesRadio(await ctx.newPage());
const err = []; p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });

await p.goto(pathToFileURL(QCM).href, { waitUntil: 'load' });
await p.waitForTimeout(300);

const Q = await p.evaluate(() => QUESTIONS.map(q => ({
  c: q.c, n: q.n, o: q.o, r: q.r, d: q.d, expl: q.expl, ex: q.ex, err: q.err, ret: q.ret,
  img: q.img ? q.img.src : null })));
const familles = await p.evaluate(() => Object.keys(COMP_LABELS));
const badge = (await p.$eval('.badge.theme', e => e.textContent)).trim();

ok('24 · chargement du QCM, titre « jardin connecté », taille annoncée exacte',
   /jardin connecté/i.test(await p.title()) && badge.includes(String(Q.length))
   && (await p.textContent('#qTot')) === String(Q.length), badge);

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
ok(`25 · 30 questions réparties sur les ${familles.length} familles : `
   + familles.map(f => f + ' ' + (parCode[f] || 0)).join(' · '),
   Q.length === 30 && familles.every(f => parCode[f] > 0)
   && Object.keys(parCode).length === familles.length, JSON.stringify(parCode));

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`26 · bonnes réponses A/B/C/D = ${rep.join('/')} (écart max 1) et d[r] vide partout`,
   Math.max(...rep) - Math.min(...rep) <= 1 && Q.every(q => q.d[q.r] === ''), rep.join('/'));

const illustrees = Q.filter(q => q.img);
const imgAbsentes = illustrees.filter(q => !fs.existsSync(path.join(ICI, q.img)));
ok(`27 · ${illustrees.length} questions illustrées, fichiers présents sur le disque`,
   illustrees.length > 0 && imgAbsentes.length === 0, imgAbsentes.map(q => q.img).join(' · '));

const incomplets = Q.filter(q => !(q.o.length === 4 && q.d.length === 4 && q.expl && q.ex
                                   && q.err && q.ret));
ok('28 · gabarit maison complet : 4 options, 4 réfutations, explication, exemple, erreur, à retenir',
   incomplets.length === 0, incomplets.map(q => q.n).slice(0, 3).join(' · '));

for (let i = 0; i < Q.length; i++) {
  const r = await p.evaluate(() => QUESTIONS[Number(document.getElementById('qNum')
    .textContent) - 1].r);
  const opts = await p.$$('#qOptions .option');
  await opts[r].click();
  await p.click('#btnValider'); await p.waitForTimeout(35);
  if (i < Q.length - 1) { await p.click('#btnSuiv'); await p.waitForTimeout(35); }
}
await p.click('#btnTerminer'); await p.waitForTimeout(220);
const note = (await p.textContent('#rNote')).trim();
const lignes = await p.$$eval('#tblBilan tbody tr',
  l => l.map(t => t.textContent.replace(/\s+/g, ' ').trim()));
ok(`29 · parcours complet 30 / 30 joué question par question → note ${note}, `
   + `bilan sur ${lignes.length} familles`,
   /20,0/.test(note) && (await p.textContent('#rOk')) === String(Q.length)
   && lignes.length === familles.length,
   note + ' · ' + lignes.join(' | ').slice(0, 80));

const cles = await p.evaluate(() => Object.keys(window.localStorage));
ok('30 · la clé localStorage du QCM est écrite',
   cles.some(k => k.includes('qcm_4e_C4.1-C4.9_jardin_connecte')), cles.join(' · '));

const retourSeq = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href'))
  .filter(h => h && /sequence.*\.html$/.test(h)));
ok('31 · le lien de retour vers la séquence existe et pointe sur un fichier réel',
   retourSeq.length > 0
   && retourSeq.every(h => fs.existsSync(path.join(ICI, decodeURIComponent(h)))),
   retourSeq[0] || '');

ok('32 · aucune erreur JS sur le QCM', err.length === 0, err.slice(0, 2).join(' | '));
await ctx.close();
}

/* ════════════════ BONUS, DÉFI DONNÉES : LA TABLE ET SA COURBE (04/11/2026, 10 contrôles) ════════════════
   « Trace la courbe ! » demandait un geste que la page ne permettait pas : la réponse était une zone de texte. Le défi
   a maintenant une vraie table (6 lignes : horodatage, lieu, valeur ; la grandeur et son unité en tête) et la courbe qui
   se trace dès deux mesures. La suite remplit la table comme un élève : dans le désordre du temps, avec une valeur
   impossible, une unité qui ne va pas ; puis elle recharge, passe à 390 px, imprime. */
{
const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, locale: 'fr-FR' });
const p = _groupesRadio(await ctx.newPage());
const err = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
await p.goto(pathToFileURL(SEQ).href, { waitUntil: 'load' });
// Révision du 10/11/2026 : Bonus et exercice incrusté sont repliés ; le banc ouvre les volets.
await p.evaluate(() => document.querySelectorAll('details.bonus-replie, details.incruste-repliee').forEach(d => { d.open = true; })); await p.waitForTimeout(300);
await p.click('.seance-tab[data-panel="s4"]'); await p.waitForTimeout(150);
const courbe = () => p.evaluate(() => {
  const s = document.getElementById('ddCourbe'), vb = s.viewBox.baseVal;
  const tr = [...s.querySelectorAll('path.rl-courbe')].map(c => (c.getAttribute('d').match(/-?[\d.]+ -?[\d.]+/g) || []).map(q => q.split(' ').map(Number)));
  const pts = [...s.querySelectorAll('circle, rect:not(.rl-fond):not(.rl-bulle), polygon:not(.rl-axe-pointe)')].filter(e => e.querySelector('title'));
  const txt = [...s.querySelectorAll('text')].filter(t => getComputedStyle(t).display !== 'none').map(t => t.textContent);
  const jours = [...s.querySelectorAll('path.rl-jour')].map(j => +j.getAttribute('d').split(' ')[0].slice(1));
  return { traces: tr, points: pts.length, textes: txt, jours, dispo: s.getAttribute('data-dispo'), vb: [vb.width, vb.height],
           th: document.getElementById('ddUniteTh').textContent, titre: document.getElementById('ddTitre').textContent };
});
const ligne = async (i, d, h, l, v) => { await p.fill('#ddD' + i, d); await p.fill('#ddH' + i, h); await p.fill('#ddL' + i, l); await p.fill('#ddV' + i, v); };
const depart = await p.evaluate(() => {
  const t = document.getElementById('ddTable');
  return { lignes: t.querySelectorAll('tbody tr').length,
           cols: [...t.querySelectorAll('thead th')].map(th => th.textContent.replace(/\s+/g, ' ').trim()),
           champs: [...t.querySelectorAll('tbody tr')].every(tr => tr.querySelector('input[type=date]') && tr.querySelector('input[type=time]')
             && tr.querySelectorAll('input[type=text]').length === 2),
           tete: !!document.querySelector('#defiDonnees select#ddGrandeur') && !!document.querySelector('#defiDonnees select#ddUnite'),
           exp: Object.keys(window.__exp || {}).filter(k => k !== 'mode_essentiel').length, valid: Object.keys(window.__valid || {}).length,
           consigne: /Trace la courbe/.test(document.getElementById('defiDonnees').closest('section').textContent) };
});
const vide = await courbe();
ok('33 · défi données : une vraie table (6 lignes : horodatage date et heure, lieu, valeur), la grandeur et son unité en tête ; au départ, pas de courbe, le cadre dit quand elle se trace ; rien d\'enregistré',
   depart.lignes === 6 && depart.champs && depart.tete && /Horodatage/.test(depart.cols[0]) && depart.cols[1] === 'Lieu' && /^Valeur/.test(depart.cols[2])
   && vide.traces.length === 0 && vide.points === 0 && vide.textes.some(t => /deux mesures/.test(t)) && depart.exp === 0 && depart.valid === 0 && !depart.consigne,
   JSON.stringify(depart).slice(0, 160));

await p.selectOption('#ddGrandeur', "Température de l'air"); await p.selectOption('#ddUnite', '°C');
await ligne(1, '2026-11-04', '18:00', 'balcon', '28');
await p.waitForTimeout(80);
const une = await courbe();
await ligne(2, '2026-11-04', '07:00', 'balcon', '24,5');   // saisie APRÈS la mesure de 18 h : l'ordre du temps n'est pas celui des lignes
await p.waitForTimeout(80);
const deux = await courbe();
const tr2 = deux.traces[0] || [];
ok('34 · une mesure : pas de courbe ; deux (la seconde plus ancienne) : une courbe de 2 points reliés dans l\'ordre du temps ; « Valeur (°C) » en tête de colonne, « Température (°C) » sur l\'axe, la date en abscisse',
   une.traces.length === 0 && une.points === 0 && deux.traces.length === 1 && tr2.length === 2 && tr2[0][0] < tr2[1][0] && tr2[0][1] > tr2[1][1]
   && deux.th === '(°C)' && deux.textes.includes('Température (°C)') && deux.textes.some(t => /4\/11/.test(t)) && /Température de l'air/.test(deux.titre),
   JSON.stringify({ tr2, th: deux.th }).slice(0, 140));
await ligne(3, '2026-11-05', '07:00', 'balcon', '25'); await ligne(4, '2026-11-05', '18:00', 'balcon', '29,5');
await ligne(5, '2026-11-06', '07:00', 'balcon', '24'); await ligne(6, '2026-11-06', '18:00', 'balcon', '27,5');
await p.waitForTimeout(80);
const six = await courbe();
const t6 = six.traces[0] || [], ecarts = six.jours.slice(1).map((x, k) => +(x - six.jours[k]).toFixed(1));
ok('35 · six mesures : six points, une courbe qui suit le temps (abscisses croissantes) ; l\'abscisse est graduée régulièrement (quatre minuits également espacés)',
   six.points === 6 && t6.length === 6 && t6.every((q, k) => !k || q[0] > t6[k - 1][0]) && six.jours.length === 4
   && ecarts.every(e => Math.abs(e - ecarts[0]) < 1), JSON.stringify({ jours: six.jours, ecarts }));

await p.fill('#ddV5', 'chaud'); await p.waitForTimeout(80);
const chaud = await p.evaluate(() => ({ msg: document.getElementById('ddVMsg5').textContent, vu: document.getElementById('ddVMsg5').offsetHeight > 0,
  inv: document.getElementById('ddV5').getAttribute('aria-invalid'), lie: document.getElementById('ddV5').getAttribute('aria-describedby') }));
const apresChaud = await courbe();
await p.fill('#ddV5', '24 °C'); await p.waitForTimeout(80);
const avecU = await p.textContent('#ddVMsg5');
await p.selectOption('#ddGrandeur', 'Hygrométrie (humidité de l\'air)'); await p.selectOption('#ddUnite', '%');
await p.fill('#ddV5', '140'); await p.waitForTimeout(80);
const cent = await p.textContent('#ddVMsg5');
ok('36 · une valeur impossible est signalée sous sa case, reliée au champ, sans bloquer le reste : « chaud » (pas un nombre), « 24 °C » (l\'unité est dans l\'en-tête), 140 % (impossible) ; la courbe garde ses cinq autres points',
   /✘/.test(chaud.msg) && /pas un nombre/.test(chaud.msg) && chaud.vu && chaud.inv === 'true' && chaud.lie === 'ddVMsg5'
   && apresChaud.points === 5 && apresChaud.traces[0].length === 5 && /nombre seul/.test(avecU) && /impossible/.test(cent) && /100/.test(cent),
   [chaud.msg, avecU, cent].join(' | ').slice(0, 200));
await p.selectOption('#ddGrandeur', "Température de l'air"); await p.selectOption('#ddUnite', '%');
await p.fill('#ddV5', '24'); await p.waitForTimeout(80);
const mU = await p.evaluate(() => ({ t: document.getElementById('ddUniteMsg').textContent, inv: document.getElementById('ddUnite').getAttribute('aria-invalid') }));
ok('37 · une unité qui ne va pas avec la grandeur est signalée sous son menu (une température se mesure en °C)',
   /°C/.test(mU.t) && /pas en %/.test(mU.t) && mU.inv === 'true', mU.t);

/* « Vérifier » : le lieu manquant, la valeur impossible, l'unité, l'ordre du temps (lignes 1 et 2 inversées), puis tout juste */
await p.fill('#ddL6', ''); await p.fill('#ddV3', 'trente');
await p.click('#ddVerifier'); await p.waitForTimeout(80);
const ret = await p.evaluate(() => { const r = document.getElementById('ddRetour');
  return { cls: r.className, items: [...r.querySelectorAll('li a')].map(a => ({ t: a.textContent, h: a.getAttribute('href') })), lieu: document.getElementById('ddLMsg6').textContent }; });
await p.click(`#ddRetour a[href="#ddL6"]`); await p.waitForTimeout(40);
const focus = await p.evaluate(() => document.activeElement.id);
const dit = re => ret.items.some(i => re.test(i.t));
await p.selectOption('#ddUnite', '°C'); await p.fill('#ddL6', 'balcon'); await p.fill('#ddV3', '25');
await ligne(1, '2026-11-04', '07:00', 'balcon', '24,5'); await ligne(2, '2026-11-04', '18:00', 'balcon', '28');
await p.click('#ddVerifier'); await p.waitForTimeout(80);
const juste = await p.evaluate(() => ({ cls: document.getElementById('ddRetour').className, t: document.getElementById('ddRetour').textContent }));
ok('38 · « Vérifier » donne un retour par manque — l\'unité, le lieu de la ligne 6 (écrit aussi sous sa case), la valeur « trente », l\'ordre du temps — et chacun mène à sa case ; corrigée, la table est jugée juste',
   /err|mixte/.test(ret.cls) && dit(/se mesure en °C/) && dit(/Ligne 6 : Il manque le lieu/) && dit(/Ligne 3 .*pas un nombre/) && dit(/ordre du temps/)
   && /manque le lieu/.test(ret.lieu) && focus === 'ddL6' && /ok/.test(juste.cls) && /✔/.test(juste.t),
   ret.items.map(i => i.t.slice(0, 40)).join(' | ').slice(0, 240) + ' → ' + juste.t.slice(0, 40));

await p.waitForTimeout(800);                                   // la sauvegarde de la page part 600 ms après la dernière saisie
await p.reload({ waitUntil: 'load' }); await p.evaluate(() => document.querySelectorAll('details.bonus-replie, details.incruste-repliee').forEach(d => { d.open = true; })); await p.waitForTimeout(300);
await p.click('.seance-tab[data-panel="s4"]'); await p.waitForTimeout(150);
const relu = await courbe();
const valeurs = await p.evaluate(() => [1, 2, 3, 4, 5, 6].map(i => ['D', 'H', 'L', 'V'].map(c => document.getElementById('dd' + c + i).value).join(' ')));
ok('39 · sauvegarde : au rechargement, la grandeur, l\'unité et les six lignes reviennent, et la courbe se retrace (6 points)',
   (await p.inputValue('#ddGrandeur')) === "Température de l'air" && (await p.inputValue('#ddUnite')) === '°C'
   && valeurs[0] === '2026-11-04 07:00 balcon 24,5' && valeurs[5] === '2026-11-06 18:00 balcon 27,5' && relu.points === 6 && relu.traces[0].length === 6,
   valeurs.join(' | ').slice(0, 120));
const tailles = async () => p.evaluate(() => { const s = document.getElementById('ddCourbe'), k = s.getBoundingClientRect().width / s.viewBox.baseVal.width;
  return Math.min(...[...s.querySelectorAll('text')].filter(t => getComputedStyle(t).display !== 'none').map(t => parseFloat(getComputedStyle(t).fontSize) * k)); });
const t1280 = await tailles();
await p.setViewportSize({ width: 390, height: 844 }); await p.waitForTimeout(250);
const etroit = await p.evaluate(() => {
  const h = sel => [...document.querySelectorAll(sel)].filter(e => e.offsetParent).map(e => Math.round(e.getBoundingClientRect().height));
  const t = document.getElementById('ddTable');
  return { large: document.documentElement.scrollWidth > innerWidth + 1, table: t.scrollWidth <= t.parentElement.clientWidth + 1,
           dispo: document.getElementById('ddCourbe').getAttribute('data-dispo'),
           cibles: Math.min(...h('#defiDonnees input'), ...h('#defiDonnees select'), ...h('#ddVerifier')) };
});
const t390 = await tailles();
ok('40 · à 390 px, aucun défilement de côté : la table tient dans sa largeur, la courbe passe en disposition étroite (textes ≥ 12 px), cases et bouton de 44 px ; à 1 280 px, aucun texte de la courbe sous 14 px',
   !etroit.large && etroit.table && etroit.dispo === 'etroit' && t390 >= 12 && etroit.cibles >= 44 && t1280 >= 14,
   JSON.stringify(etroit) + ` · ${t1280.toFixed(1)} px / ${t390.toFixed(1)} px`);
await p.setViewportSize({ width: 1280, height: 900 }); await p.waitForTimeout(250);

/* Sur le papier : la table (les champs deviennent des lignes, ce qui est écrit s'imprime), le cadre de la courbe sur
   fond blanc, l'encre foncée ; ni bouton, ni message d'écran. */
await p.evaluate(() => window.dispatchEvent(new Event('beforeprint')));
await p.emulateMedia({ media: 'print' }); await p.waitForTimeout(150);
const papier = await p.evaluate(() => {
  const vis = e => !!e && getComputedStyle(e).display !== 'none' && e.getBoundingClientRect().height > 0;
  const s = document.getElementById('ddCourbe');
  return { table: vis(document.getElementById('ddTable')), champs: [...document.querySelectorAll('#ddTable input')].filter(vis).length,
           fond: getComputedStyle(s.querySelector('.rl-fond')).fill, encre: getComputedStyle(s.querySelector('.rl-t')).fill,
           courbe: vis(document.getElementById('ddBoite')), bouton: vis(document.getElementById('ddVerifier')), msg: [...document.querySelectorAll('.rl-msg')].some(vis) };
});
await p.emulateMedia({ media: 'screen' }); await p.evaluate(() => window.dispatchEvent(new Event('afterprint')));
ok('41 · à l\'impression : la table (24 champs en lignes d\'écriture) et le cadre de la courbe, fond blanc et encre foncée ; ni bouton, ni message d\'écran',
   papier.table && papier.champs === 24 && papier.courbe && papier.fond === 'rgb(255, 255, 255)' && /rgb\(17, 24, 39\)/.test(papier.encre) && !papier.bouton && !papier.msg,
   JSON.stringify(papier));
await ctx.close();

/* Une fiche imprimée avant toute mesure : la table vide et le cadre de la courbe, quadrillé, qui dit quoi tracer. */
const ctx2 = await b.newContext({ viewport: { width: 1280, height: 900 }, locale: 'fr-FR' });
const q = await ctx2.newPage();
await q.goto(pathToFileURL(SEQ).href, { waitUntil: 'load' }); await q.waitForTimeout(300);
await q.evaluate(() => document.querySelectorAll('details.bonus-replie, details.incruste-repliee').forEach(d => { d.open = true; }));
await q.click('.seance-tab[data-panel="s4"]'); await q.waitForTimeout(150);
await q.focus('#ddGrandeur');
const ordre = [];                                              // un champ date ou heure a ses segments : on garde chaque champ une fois
for (let k = 0; k < 16 && ordre.length < 6; k++) { await q.keyboard.press('Tab'); const id = await q.evaluate(() => document.activeElement.id); if (id !== ordre[ordre.length - 1]) ordre.push(id); }
await q.evaluate(() => window.dispatchEvent(new Event('beforeprint')));
await q.emulateMedia({ media: 'print' }); await q.waitForTimeout(150);
const cadre = await q.evaluate(() => {
  const s = document.getElementById('ddCourbe'), vis = t => getComputedStyle(t).display !== 'none';
  return { textes: [...s.querySelectorAll('text')].filter(vis).map(t => t.textContent).join(' '), grille: s.querySelectorAll('path.rl-grille').length,
           vides: [...document.querySelectorAll('#ddTable input')].every(i => !i.value) };
});
ok('42 · sans mesure, la fiche imprimée garde une consigne faisable : la table vide, le cadre quadrillé qui dit « Trace ici ta courbe » ; au clavier, Tab passe de la grandeur à l\'unité, puis date, heure, lieu, valeur',
   cadre.vides && cadre.grille >= 10 && /Trace ici ta courbe/.test(cadre.textes) && !/dès que tu as deux mesures/.test(cadre.textes)
   && ordre.join(' ') === 'ddUnite ddD1 ddH1 ddL1 ddV1 ddD2', ordre.join(' ') + ' · ' + cadre.textes.slice(0, 80));
ok('43 · aucune erreur JS dans le défi données', err.length === 0, err.slice(0, 2).join(' | '));
await ctx2.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
