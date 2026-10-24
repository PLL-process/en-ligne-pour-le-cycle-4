/* tests_4e_C4.1-C4.2-C4.4_book-train.mjs — le Book Train, rejoué dans Chromium.
 *
 * D'OÙ VIENT CE FICHIER
 * ---------------------
 * Le rapport du 08/08/2026 annonçait une « suite Playwright du lot (32 vérifications), rejouable » :
 * elle n'a jamais été commitée. Ce banc naît avec la relecture du 24/10/2026 (vidéo, chiffres vérifiés,
 * Bonus corrigé, ouverture n°304, vocabulaire de l'énergie) et rejoue AUSSI ce que la page faisait avant :
 * vérificateurs, sauvegarde, mode essentiel, liens du plan de mission.
 *
 * CE QU'IL A TROUVÉ EN NAISSANT
 * -----------------------------
 * Sur la page d'avant, le billet d'entrée portait la classe `referentiel-card` : le mode essentiel le
 * masquait — il disparaissait justement pour les élèves que la densité met en difficulté. Le test 6
 * le mesure (`checkVisibility()`) ; la même mesure, prise le 24/10/2026 sur la page de `main` à 1280
 * et à 390 px, rendait « invisible ». Sur cette même page, à 390 px, la séance 3 défilait de 143 px
 * à l'horizontale (les étiquettes masquées du tableau 3.2), et la figure 1 cachait trois étiquettes
 * sous le sous-sol, peint après elles (les toilettes, le perron côté parc), et en coupait trois au bord
 * du cadre (le perron monumental, ses lions) : tests 19 et 23.
 *
 * IL NE RECOPIE PAS LES BONNES RÉPONSES : il les lit dans la page (`data-bonne`) et compare les indices
 * de bonne réponse du QCM à ceux de la version de référence, lue dans git (`origin/main`) quand elle existe.
 *
 * SECONDE PASSE (24/10/2026, même jour) : la séquence passe à 4 séances (nouvelle séance 2 « Les deux
 * chaînes », activités renumérotées pour que le numéro dise la séance), chaque séance mène à la suivante
 * (n°101) et les phrases anglaises incrustées dans la vidéo sont traduites et minutées : tests 28 à 32.
 * Sur la page d'avant, à 390 px, l'étiquette « présenter » de la dernière gare était déjà rognée par le
 * bandeau (test 32).
 *
 * TROISIÈME PASSE (24/10/2026) : conversion n°300 des 44 listes déroulantes en groupes de boutons radio.
 * Le test 18 coche au lieu de choisir dans une liste ; tests 33 à 38 : forme des groupes, chaque
 * exercice se valide, billet d'entrée, réponses sauvegardées AVANT la conversion relues, tableaux
 * empilés sur téléphone.
 *
 * Usage, depuis ce dossier :  node tests_4e_C4.1-C4.2-C4.4_book-train.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe, 1 sinon, 2 si rien n'a pu être mesuré.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';
import { execFileSync } from 'node:child_process';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const PAGE = path.join(ICI, 'sequence_4e_C4.1-C4.2-C4.4_book-train.html');
const QCM = path.join(ICI, 'qcm_book-train.html');
if (!fs.existsSync(PAGE) || !fs.existsSync(QCM)) {
  console.error('⛔ EN PANNE — page ou QCM introuvable : rien n\'a été mesuré (règle d\'or n°299).');
  process.exit(2);
}
const src = fs.readFileSync(PAGE, 'utf8');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d: String(d) });
const b = await chromium.launch();

async function ouvrir(largeur, storage = null) {
  const ctx = await b.newContext({ viewport: { width: largeur, height: 900 } });
  const p = await ctx.newPage();
  const err = [], reseau = [];
  p.on('pageerror', e => err.push(e.message));
  p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
  await p.route('**/*', r => {
    const u = r.request().url();
    if (/^(file|data|blob):/.test(u)) return r.continue();
    reseau.push(u); return r.abort();
  });
  await p.goto(pathToFileURL(PAGE).href, { waitUntil: 'load' });
  if (storage) {
    await p.evaluate(s => { localStorage.clear(); for (const [k, v] of Object.entries(s)) localStorage.setItem(k, v); }, storage);
    await p.reload({ waitUntil: 'load' });
  } else {
    await p.evaluate(() => localStorage.clear());
    await p.reload({ waitUntil: 'load' });
  }
  await p.waitForTimeout(200);
  return { ctx, p, err, reseau };
}
/* L'onglet qui contient un élément : le banc ne suppose pas dans quelle séance vit un bloc. */
const ongletDe = async (p, sel) => p.click('#tab-' + await p.evaluate(s => document.querySelector(s).closest('.panneau').id, sel));
const visible = (p, sel) => p.evaluate(s => { const e = document.querySelector(s); return !!e && e.checkVisibility(); }, sel);

/* ── 1. Chargement ─────────────────────────────────────────────────────────── */
let { ctx, p, err, reseau } = await ouvrir(1280);
ok('1 · charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('2 · aucune ressource demandée hors de la page (n°305)', reseau.length === 0, reseau.slice(0, 3).join(' | '));

/* ── 2. Ouverture (n°304) ──────────────────────────────────────────────────── */
const ouverture = await p.locator('section.rappel-spiralaire').innerText();
ok('3 · l\'ouverture dit ce qui devrait être en place (n°304)',
   /Avant de commencer : ce que je vérifie/.test(ouverture) && !/l'an dernier|tu as (tracé|dit|fait)|en 5e,/i.test(ouverture),
   ouverture.slice(0, 120));
await p.click('#tab-s2');
await p.click('section.rappel-spiralaire a[href="#capsule-5e"] >> nth=0');
await p.waitForTimeout(250);
ok('4 · le lien de rattrapage ouvre l\'onglet Départ et la capsule',
   await p.evaluate(() => document.getElementById('s0').classList.contains('actif') && document.getElementById('capsule-5e').open));
await p.click('#tab-s0');
await p.click('a[href="#seance-2"]');
await p.waitForTimeout(250);
ok('5 · le plan de mission mène toujours à la séance 2',
   await p.evaluate(() => document.getElementById('s2').classList.contains('actif')));

/* ── 3. Mode essentiel : le billet reste, les corrections partent ─────────── */
await p.click('#tab-s0');
await p.click('#btnEssentiel');
ok('6 · le billet d\'entrée reste visible en mode essentiel', await visible(p, '#billet'));
ok('7 · les corrections disparaissent en mode essentiel', !(await visible(p, '#video-book-train details.correction')));
await p.click('#btnEssentiel');

/* ── 4. La vidéo : un lien, pas un chargement, et deux questions dans le flux ── */
const lien = p.locator('#video-book-train a.ressource-lien');
ok('8 · la vidéo s\'ouvre dans un nouvel onglet, depuis un lien',
   (await lien.count()) === 1 && (await lien.getAttribute('target')) === '_blank'
   && /^https:\/\/www\.youtube\.com\/watch\?v=/.test(await lien.getAttribute('href')));
ok('9 · l\'activité dit qu\'elle demande Internet, et son repli (n°305)',
   (await p.locator('#video-book-train p.activite-en-ligne').count()) === 1
   && (await p.locator('#video-book-train .ressource-repli').count()) === 1);
const groupes = await p.$$eval('#video-book-train fieldset.qcm-groupe', fs => fs.map(f => ({
  legende: !!f.querySelector('legend'), bonne: f.dataset.bonne,
  valeurs: [...f.querySelectorAll('input[type=radio]')].map(i => i.value),
  etiquetes: [...f.querySelectorAll('input[type=radio]')].every(i => !!document.querySelector(`label[for="${i.id}"]`)),
  noms: new Set([...f.querySelectorAll('input[type=radio]')].map(i => i.name)).size })));
ok('10 · deux groupes radio : légende, une étiquette par proposition, un seul nom, la bonne réponse parmi les valeurs (n°300)',
   groupes.length === 2 && groupes.every(g => g.legende && g.etiquetes && g.noms === 1 && g.valeurs.includes(g.bonne)),
   JSON.stringify(groupes.map(g => g.valeurs.length)));
const verifVideo = '#s0 button.verif[data-exo="exo-video"]';
await p.click(verifVideo);
ok('11 · sans réponse, le vérificateur demande de répondre', /reste 2 réponse/.test(await p.textContent('#res-exo-video')));
for (const g of groupes) {                                   // une bonne, une fausse
  const fausse = g.valeurs.find(v => v !== g.bonne);
  const choisie = g === groupes[0] ? g.bonne : fausse;
  await p.check(`#video-book-train input[value="${choisie.replace(/"/g, '\\"')}"]`);
}
await p.click(verifVideo);
ok('12 · une réponse fausse est signalée (1/2)', /1\/2/.test(await p.textContent('#res-exo-video')));
await p.check(`#video-book-train input[value="${groupes[1].bonne}"]`);
await p.click(verifVideo);
ok('13 · deux bonnes réponses : 2/2', /2\/2/.test(await p.textContent('#res-exo-video')));

/* ── 5. Bonus (n°301) : des champs, une version étayée, un corrigé ──────────── */
await ongletDe(p, '.bloc-bonus');
const bonus = await p.evaluate(() => {
  const z = document.querySelector('.bloc-bonus');
  const champs = [...z.querySelectorAll('textarea, input[type=text]')];
  return {
    champs: champs.length,
    etiquetes: champs.every(c => !!z.querySelector(`label[for="${c.id}"]`)),
    sauves: champs.every(c => c.hasAttribute('data-save')),
    corrige: [...z.querySelectorAll('details.correction > summary')].some(s => /corrig/i.test(s.textContent)),
    etaye: [...z.querySelectorAll('summary')].some(s => /Version étayée/.test(s.textContent)),
    defis: (z.textContent.match(/Défi \d —/g) || []).length,
    avantBilan: !!(z.compareDocumentPosition([...document.querySelectorAll('h2')].find(h => /Bilan de la séquence/.test(h.textContent))) & Node.DOCUMENT_POSITION_FOLLOWING),
  };
});
ok('14 · six défis, chacun avec sa case étiquetée et sauvegardée', bonus.defis === 6 && bonus.champs === 8 && bonus.etiquetes && bonus.sauves, JSON.stringify(bonus));
ok('15 · le Bonus porte une version étayée et un corrigé, et précède le bilan', bonus.etaye && bonus.corrige && bonus.avantBilan, JSON.stringify(bonus));
await p.fill('#bonus_d6a', '22,86 m/min');
await p.fill('#bonus_d6c', 'Le trajet fait 114 m sur 290 m, parce que le rail a une voie de retour.');
await p.dispatchEvent('#bonus_d6a', 'change');

/* ── 6. Sauvegarde : tout revient après rechargement ──────────────────────── */
await p.check('#ouv_1');
const sauvegarde = await p.evaluate(() => Object.fromEntries(Object.entries(localStorage)));
await ctx.close();
({ ctx, p, err } = await ouvrir(1280, sauvegarde));
const repris = await p.evaluate(() => ({
  q1: (document.querySelector('input[name="vid_q1"]:checked') || {}).value || '',
  q2: (document.querySelector('input[name="vid_q2"]:checked') || {}).value || '',
  d6a: document.getElementById('bonus_d6a').value,
  d6c: document.getElementById('bonus_d6c').value,
  ouv1: document.getElementById('ouv_1').checked,
}));
ok('16 · les boutons radio, les cases du Bonus et la coche d\'ouverture reviennent après rechargement',
   repris.q1 === groupes[0].bonne && repris.q2 === groupes[1].bonne && repris.d6a === '22,86 m/min'
   && /114 m/.test(repris.d6c) && repris.ouv1, JSON.stringify(repris));
ok('17 · rechargement sans erreur JS', err.length === 0, err.join(' | '));

/* ── 7. Une activité d'avant : le vérificateur marche toujours, en boutons radio ─ */
await p.click('#tab-s1');
const listes = await p.$$eval('#exo12 fieldset[data-bonne]', fs => fs.map(f => [f.id, f.dataset.bonne]));
for (const [id, v] of listes) await p.check(`#${id} input[type=radio][value="${v.replace(/"/g, '\\"')}"]`);
await p.click('button.verif[data-exo="exo12"]');
ok('18 · l\'activité 1.2 se valide comme avant (désormais en boutons radio)', listes.length === 5 && new RegExp(`${listes.length}/${listes.length}`).test(await p.textContent('#res-exo12')), listes.length);

/* ── 8. Figures 1 et 5 : le bon rappel, aucun texte caché, coupé ou recouvert ── */
await p.evaluate(() => document.querySelectorAll('.panneau details').forEach(d => d.open = true));
const mesurer = sel => p.evaluate(s => {
  const svg = document.querySelector(s);
  const vb = svg.viewBox.baseVal;
  const textes = [...svg.querySelectorAll('text')].filter(t => t.getBBox().width > 0);
  const boites = textes.map(t => ({ t: t.textContent.trim(), b: t.getBBox(), el: t }));
  const chevauche = [], hors = [], caches = [];
  for (let i = 0; i < boites.length; i++) for (let j = i + 1; j < boites.length; j++) {
    const a = boites[i].b, c = boites[j].b;
    if (a.x < c.x + c.width - 1 && c.x < a.x + a.width - 1 && a.y < c.y + c.height - 1 && c.y < a.y + a.height - 1)
      chevauche.push(boites[i].t.slice(0, 18) + ' / ' + boites[j].t.slice(0, 18));
  }
  for (const { t, b, el } of boites) {
    if (b.x < 0 || b.y < 0 || b.x + b.width > vb.width + 0.5 || b.y + b.height > vb.height + 0.5) hors.push(t.slice(0, 24));
    // un texte est caché si une forme peinte APRÈS lui couvre son centre
    const r = el.getBoundingClientRect();
    const dessus = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
    if (dessus && dessus !== el && svg.contains(dessus) && (el.compareDocumentPosition(dessus) & Node.DOCUMENT_POSITION_FOLLOWING)
        && !el.contains(dessus) && dessus.tagName !== 'text' && dessus.tagName !== 'tspan') caches.push(t.slice(0, 24));
  }
  return { texte: svg.textContent, chevauche, hors, caches };
}, sel);
for (const [n, sel] of [['1', 'svg[aria-labelledby="fig1t fig1d"]'], ['5', 'svg[aria-labelledby="fig5t fig5d"]']]) {
  await ongletDe(p, sel);
  await p.evaluate(s => document.querySelector(s).scrollIntoView({ block: 'center', behavior: 'instant' }), sel);
  await p.waitForTimeout(100);
  const m = await mesurer(sel);
  ok(`${n === '1' ? '19' : '20'} · figure ${n} : aucun texte recouvert par un autre, coupé par le cadre ou caché sous une forme`,
     m.chevauche.length + m.hors.length + m.caches.length === 0,
     JSON.stringify({ chevauche: m.chevauche, hors: m.hors, caches: m.caches }));
  if (n === '5') ok('20 bis · la figure 5 dit 480 V ~ → 24 V ⎓, plus 13,2 kV', /480 V ~ → 24 V ⎓/.test(m.texte) && !/13,2/.test(m.texte));
}

/* ── 9. Un seul vocabulaire de l'énergie, des chiffres sourcés ────────────── */
const texte = await p.evaluate(() => document.body.textContent);
ok('21 · la page ne dit plus « change de nature » ni « 4 niveaux »', !/change(r|ment)? de nature|4 niveaux/.test(texte));
ok('22 · la source des chiffres est citée (communiqué de la NYPL)', /nypl\.org\/press\/press-release\/september-21-2016/.test(src));

/* ── 9 bis. Quatre séances : le numéro de l'activité dit la séance ─────────── */
const structure = await p.evaluate(() => {
  const onglets = [...document.querySelectorAll('[role=tab]')].map(t => t.getAttribute('aria-controls'));
  const mal = [];
  for (const h of document.querySelectorAll('h3')) {
    const m = h.textContent.match(/^\s*Activité (\d)\.\d\b/);
    if (m && h.closest('.panneau').id !== 's' + m[1]) mal.push(h.textContent.trim().slice(0, 30) + ' dans ' + h.closest('.panneau').id);
  }
  const titres = [1, 2, 3, 4].map(n => { const t = document.getElementById('seance-' + n); return !!t && t.closest('.panneau').id === 's' + n; });
  return { onglets, mal, titres, activites: [...document.querySelectorAll('h3')].filter(h => /^\s*Activité \d\.\d/.test(h.textContent)).length };
});
ok('28 · « 4 séances de 55 min », cinq onglets, onze activités, chacune dans la séance que dit son numéro',
   /⏱ 4 séances de 55 min/.test(src) && structure.onglets.join() === 's0,s1,s2,s3,s4' && structure.titres.every(Boolean)
   && structure.mal.length === 0 && structure.activites === 11, JSON.stringify(structure));
ok('29 · plus aucun ancien numéro d\'activité (1.2 A, 1.2 bis, 1.2 ter) dans la page', !/1\.2 (A|bis|ter)\b/.test(texte));
const suites = [];
for (const [de, vers] of [['s0', 's1'], ['s1', 's2'], ['s2', 's3'], ['s3', 's4']]) {
  if (await p.locator('#tab-' + de).count() === 0) { suites.push(de + ' absent'); continue; }
  await p.click('#tab-' + de);
  const btn = p.locator(`#${de} > p.page-suivante:last-of-type button.vers-seance[data-vers="${vers}"]`);
  if (await btn.count() !== 1) { suites.push(de + ' sans bouton'); continue; }
  await btn.click(); await p.waitForTimeout(150);
  if (!(await p.evaluate(v => document.getElementById(v).classList.contains('actif'), vers))) suites.push(de + ' → ' + vers + ' n\'ouvre pas');
}
ok('30 · chaque séance se termine par un bouton qui ouvre la suivante (n°101), la dernière n\'en a pas',
   suites.length === 0 && (await p.locator('#s4').count()) === 1 && (await p.locator('#s4 button.vers-seance').count()) === 0, suites.join(' | '));

/* ── 9 ter. La vidéo parle anglais dans l'image : la page la traduit ─────── */
const trad = await p.evaluate(() => {
  const d = document.querySelector('#video-book-train details#video-fr');
  if (!d) return null;
  const lignes = [...d.querySelectorAll('ol.trad-liste > li')].map(li => ({
    t: (li.querySelector('.trad-t') || {}).textContent || '',
    fr: ((li.querySelector('.trad-fr') || {}).textContent || '').trim().length,
    en: !!li.querySelector('.trad-en[lang="en"]'),
  }));
  const sec = t => { const m = t.match(/^(\d+):(\d\d)$/); return m ? +m[1] * 60 + +m[2] : NaN; };
  const temps = lignes.map(l => sec(l.t));
  return { n: lignes.length, complets: lignes.every(l => l.fr > 0 && l.en),
           croissants: temps.every((x, i) => !isNaN(x) && (i === 0 || x > temps[i - 1])) && temps[temps.length - 1] <= 104,
           avantQuestions: !!(d.compareDocumentPosition(document.getElementById('exo-video')) & Node.DOCUMENT_POSITION_FOLLOWING) };
});
ok('31 · la vidéo a sa traduction minutée : 18 phrases, chacune en français et en anglais (lang="en"), dans l\'ordre, avant les questions',
   !!trad && trad.n === 18 && trad.complets && trad.croissants && trad.avantQuestions, JSON.stringify(trad));
await ctx.close();

/* ── 9 quater. Règle n°300 : plus une liste déroulante, des groupes conformes ─ */
({ ctx, p, err } = await ouvrir(1280));
const formes = await p.evaluate(() => {
  const groupes = [...document.querySelectorAll('fieldset.qcm-groupe')];
  const defauts = [];
  for (const f of groupes) {
    const radios = [...f.querySelectorAll('input[type=radio]')];
    const leg = f.querySelector(':scope > legend');
    if (!leg || !leg.textContent.trim()) defauts.push(f.id + ' : sans légende');
    if (radios.length < 2) defauts.push(f.id + ' : moins de deux propositions');
    if (new Set(radios.map(r => r.name)).size !== 1 || radios[0].name !== f.id) defauts.push(f.id + ' : noms différents');
    for (const r of radios) {
      const l = document.querySelector(`label[for="${r.id}"]`);
      if (!l || l.textContent.trim() !== r.value) defauts.push(r.id + ' : étiquette ≠ valeur');
    }
    if (f.dataset.bonne !== undefined && !radios.some(r => r.value === f.dataset.bonne)) defauts.push(f.id + ' : bonne réponse absente');
  }
  return { listes: document.querySelectorAll('select').length, groupes: groupes.length,
           notes: groupes.filter(f => f.dataset.bonne !== undefined).length, defauts };
});
ok('33 · n°300 : aucune liste déroulante ; 46 groupes radio (44 convertis + 2 de la vidéo), chacun avec sa légende, un seul nom, une étiquette = la valeur, la bonne réponse parmi les propositions',
   formes.listes === 0 && formes.groupes === 46 && formes.notes === 42 && formes.defauts.length === 0, JSON.stringify(formes).slice(0, 300));

// Chaque exercice noté se valide quand on coche les bonnes réponses (lues dans data-bonne).
const exercices = [['exo11', 6], ['exo12', 5], ['exo12df', 6], ['exo12b', 9], ['exo21', 5], ['exo32', 6]];
const bilans = [];
for (const [exo, n] of exercices) {
  await ongletDe(p, '#' + exo);
  const bonnes = await p.$$eval(`#${exo} fieldset[data-bonne]`, fs => fs.map(f => [f.id, f.dataset.bonne]));
  for (const [id, v] of bonnes) await p.check(`#${id} input[type=radio][value="${v.replace(/"/g, '\\"')}"]`);
  if (exo === 'exo32') {                      // le verrou : l'expérience du zoom, puis la justification
    await p.evaluate(() => { const z = document.getElementById('zoom'); z.value = '6'; z.dispatchEvent(new Event('input', { bubbles: true })); z.dispatchEvent(new Event('change', { bubbles: true })); });
    await p.fill('#justif', 'Je choisis le SVG : il reste net en plein écran et il est plus léger que le PNG.');
  }
  await p.click(`button.verif[data-exo="${exo}"]`);
  const r = await p.textContent('#res-' + exo);
  if (bonnes.length !== n || !new RegExp(`${n}/${n}`).test(r)) bilans.push(`${exo} : ${bonnes.length} groupes, « ${r.trim().slice(0, 40)} »`);
}
ok('34 · les six exercices notés se valident en cochant les bonnes réponses (1.1, 1.2, 1.3, 2.1, 3.1, 4.2)', bilans.length === 0, bilans.join(' | '));
const signale = await p.evaluate(() => { const g = [...document.querySelectorAll('#exo11 fieldset.qcm-groupe')]; return g.length === 6 && g.every(f => f.classList.contains('bon')); });
ok('35 · le vérificateur marque chaque groupe juste (classe « bon » sur le groupe)', signale);

await p.click('#tab-s0');
const billet = await p.$$eval('#billet fieldset[data-bonne]', fs => fs.map(f => [f.id, f.dataset.bonne]));
for (const [id, v] of billet) await p.check(`#${id} input[type=radio][value="${v.replace(/"/g, '\\"')}"]`);
await p.click('#btn-billet');
const b3 = await p.textContent('#fb-billet');
let b2 = '(billet sans boutons radio)';
if (billet.length === 3) {                    // sur une page non convertie, rien à cocher : le test échoue sans attendre
  await p.check('#be1 input[type=radio][data-code="b"]');
  await p.click('#btn-billet');
  b2 = await p.textContent('#fb-billet');
}
ok('36 · billet d\'entrée en boutons radio : 3 / 3 puis, une réponse changée, 2 / 3 et la capsule', billet.length === 3 && /3 \/ 3/.test(b3) && /^2 \/ 3/.test(b2.trim()), b3.slice(0, 30) + ' | ' + b2.slice(0, 30));
await ctx.close();

// Une réponse enregistrée AVANT la conversion (le code de l'option) revient, réécrite en texte.
({ ctx, p, err } = await ouvrir(1280, { 'seq_4e_book-train': JSON.stringify({ e11a: 'commande', e12f: 'elec-ac', be1: 'fonction', ap1: '🟢 J\'y arrive seul·e', e32b: 'pixel' }) }));
const relu = await p.evaluate(() => {
  const coche = id => { const c = document.querySelector(`#${id} input[type=radio]:checked`); return c ? c.value : ''; };
  return { e11a: coche('e11a'), e12f: coche('e12f'), be1: coche('be1'), ap1: coche('ap1'), e32b: coche('e32b'),
           stocke: JSON.parse(localStorage.getItem('seq_4e_book-train')) };
});
ok('37 · les réponses sauvegardées avant la conversion reviennent, et sont réécrites en texte',
   /^Le lecteur commande/.test(relu.e11a) && relu.e12f === 'électrique alternative (AC)' && /^ce qu'une partie/.test(relu.be1)
   && relu.ap1 === '🟢 J\'y arrive seul·e' && relu.e32b === 'Se pixellise'
   && relu.stocke.e11a === relu.e11a && relu.stocke.e12f === relu.e12f && relu.stocke.be1 === relu.be1, JSON.stringify(relu).slice(0, 300));
await ctx.close();

/* ── 10. 390 px : rien ne déborde ─────────────────────────────────────────── */
({ ctx, p, err } = await ouvrir(390));
// Mesuré au chargement, onglet Départ ouvert : c'est l'état que voit l'élève en arrivant.
const rail = await p.evaluate(() => {
  const bas = document.querySelector('header').getBoundingClientRect().bottom;
  const gares = [...document.querySelectorAll('[role=tab]')];
  const quais = gares.map(g => Math.round(g.querySelector('.quai').getBoundingClientRect().top));
  const debordent = gares.filter(g => g.getBoundingClientRect().bottom > bas + 0.5).length;   // le bandeau coupe ce qui dépasse (overflow:hidden)
  return { debordent, quais: [...new Set(quais)].length };
});
ok('32 · à 390 px, les cinq gares tiennent dans le bandeau et sont alignées sur le rail', rail.debordent === 0 && rail.quais === 1, JSON.stringify(rail));
const debords = [];
for (const o of ['#tab-s0', '#tab-s1', '#tab-s2', '#tab-s3', '#tab-s4']) {
  if (await p.locator(o).count() === 0) continue;
  await p.click(o); await p.waitForTimeout(100);
  debords.push(await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth));
}
ok('23 · à 390 px, aucun défilement horizontal (Départ et les quatre séances)', debords.every(d => d <= 0), debords.join(','));
const pile = [];
for (const zone of ['#exo12df', '#exo12b']) {
  await ongletDe(p, zone);
  pile.push(await p.evaluate(z => {
    const t = document.querySelector(z + ' table.tableau-qcm');
    if (!t) return { td: 'absent', legende: false, largeur: 0 };
    const td = t.querySelector('td'), leg = t.querySelector('fieldset legend');
    if (!leg) return { td: getComputedStyle(td).display, legende: false, largeur: 0 };
    return { td: getComputedStyle(td).display, legende: leg.getBoundingClientRect().width > 50, largeur: Math.round(td.getBoundingClientRect().width) };
  }, zone));
}
ok('38 · à 390 px, les deux tableaux à cocher (1.3, 2.1) s\'empilent : chaque case prend la largeur, sa légende se voit',
   pile.length === 2 && pile.every(x => x.td === 'block' && x.legende && x.largeur > 280), JSON.stringify(pile));
await ctx.close();

/* ── 11. QCM : 30 questions, aucun indice de bonne réponse déplacé ─────────── */
const qsrc = fs.readFileSync(QCM, 'utf8');
const indices = s => [...s.matchAll(/\{c:"(C4\.\d)"[\s\S]*?\br:(\d)/g)].map(m => m[1] + ':' + m[2]);
const ici = indices(qsrc);
let reference = null;
try {
  const rel = path.relative(execFileSync('git', ['rev-parse', '--show-toplevel'], { cwd: ICI }).toString().trim(), QCM).split(path.sep).join('/');
  reference = indices(execFileSync('git', ['show', 'origin/main:' + rel], { cwd: ICI, maxBuffer: 1 << 26 }).toString());
} catch { reference = null; }
ok('24 · le QCM garde 30 questions, 10 par code', ici.length === 30 && ['C4.1', 'C4.2', 'C4.4'].every(c => ici.filter(x => x.startsWith(c)).length === 10), ici.length);
ok('25 · aucun indice de bonne réponse n\'a bougé (comparé à origin/main)' + (reference ? '' : ' — RÉFÉRENCE ABSENTE, non mesuré'),
   reference !== null && JSON.stringify(reference) === JSON.stringify(ici));
ok('26 · le QCM ne parle plus de « domaine » d\'énergie ni d\'un rail qui DISTRIBUE', !/domaine|rail \(distribuer\)|rail DISTRIBUE|il distribue l'énergie/.test(qsrc));
const q = await b.newPage(); const qerr = [];
q.on('pageerror', e => qerr.push(e.message));
await q.goto(pathToFileURL(QCM).href, { waitUntil: 'load' }); await q.waitForTimeout(300);
ok('27 · le QCM se charge sans erreur JS', qerr.length === 0, qerr.join(' | '));

await b.close();
const n = T.filter(t => t.ok).length;
for (const t of T) console.log(`${t.ok ? '✅' : '❌'} ${t.n}${!t.ok && t.d ? '  — ' + t.d : ''}`);
console.log(`\n${n} / ${T.length}`);
process.exit(n === T.length ? 0 : 1);
