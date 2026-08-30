/* Contrôle d'une séquence C8.1 — le simulateur, les activités, la mémoire.
 *
 * Usage : node test81.mjs <sequence.html> <attendus.json> <5e|3e>
 *
 * Ce que ce script vérifie que l'œil ne vérifie pas :
 *   · qu'AUCUN verrou expérientiel n'est ouvert à l'ouverture de la page
 *     (règle d'or n°226) ;
 *   · qu'une activité verrouillée REFUSE avant le geste, et l'écrit ;
 *   · que le simulateur de la page calcule exactement ce que le modèle Python
 *     calcule — les attendus sont engendrés par `attendus.py`, jamais recopiés
 *     (règle d'or n°233) ;
 *   · qu'en 5e la contrainte affichée NE DÉPEND PAS du matériau : c'est la
 *     démonstration de la séquence, et un test qui ne regarderait que le
 *     verdict final la manquerait entièrement ;
 *   · qu'en 3e chacun des douze réglages donne le nombre de retenus attendu ;
 *   · que les réponses, les verrous et l'état du simulateur survivent au
 *     rechargement.
 */
import { chromium } from 'playwright';
import { readFileSync } from 'fs';

const f = process.argv[2];
const REP = JSON.parse(readFileSync(process.argv[3], 'utf8'));
const niveau = process.argv[4];
const src = readFileSync(f, 'utf8');
/* Une phrase coupée par un retour à la ligne du gabarit est la MÊME phrase.
 * Chercher la consigne de sécurité dans le texte brut la faisait manquer selon
 * l'endroit où la ligne était pliée — un contrôle qui dépend de la mise en page
 * ne contrôle pas le contenu. On compare donc sur du texte aplati. */
const norm = t => t.replace(/<[^>]+>/g, ' ').replace(/[’‘]/g, "'").replace(/\s+/g, ' ');
const plat = norm(src);
const dit = phrase => plat.includes(norm(phrase));

const b = await chromium.launch();
const p = await b.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => fail.push(r.url()));
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const $ = s => p.textContent(s);

await p.goto('file://' + f, { waitUntil: 'load' });
await p.waitForTimeout(400);

/* ── la page elle-même ───────────────────────────────────────────────────── */
ok('charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('aucune requête échouée', fail.length === 0, fail.slice(0, 2).join(' | '));
ok('aucune boîte modale', dlg.length === 0, dlg.slice(0, 2).join(' | '));

const expDepart = await p.evaluate(() => Object.keys(window.__exp || {}).filter(k => window.__exp[k]));
ok('aucun verrou ouvert à l’ouverture de la page', expDepart.length === 0, expDepart.join(','));

const doublons = await p.evaluate(() => {
  const m = {}, d = [];
  document.querySelectorAll('[id]').forEach(e => { m[e.id] = (m[e.id] || 0) + 1; });
  for (const k in m) if (m[k] > 1) d.push(k + '×' + m[k]);
  return d;
});
ok('aucun identifiant en double', doublons.length === 0, doublons.slice(0, 4).join(' '));

ok('un seul bouton QCM', (await p.$$eval('a.btn[href*="qcm"]', n => n.length)) === 1);
ok('hypothèse d’entrée présente', !!(await p.$('#hyp')));
ok('bandeau de durée présent', /\d+ séances? de \d+ min/.test(await $('.badge.duree')));
ok('le bandeau annonce plus de temps que les activités n’en demandent',
  REP.annonce > REP.activitesMin, REP.annonce + ' contre ' + REP.activitesMin);
ok('la formulation officielle est recopiée', dit(REP.formulation),
  REP.formulation.slice(0, 40));
ok('le code d’appui est cité', dit(REP.appui), REP.appui);
ok('la formulation officielle du code d’appui est recopiée exactement',
  dit(REP.formulationAppui), REP.formulationAppui.slice(0, 46));
ok('consigne de sécurité présente', dit(REP.securite), REP.securite.slice(0, 40));
ok('le secteur est explicitement écarté', /secteur/i.test(src));
ok('les trois versions A/B/C sont annoncées', ['🅰', '🅱', '🅲'].every(x => src.includes(x)));
ok('aucun marqueur de gabarit non remplacé', !/__[A-Z_0-9]+__/.test(src),
  (src.match(/__[A-Z_0-9]+__/g) || []).slice(0, 3).join(' '));
ok('bloc bonus présent', src.includes('🎁 Bonus'));

/* ── un verrou fermé refuse, et il le dit ────────────────────────────────── */
for (const [n, cle] of Object.entries(REP.verrous)) {
  await p.click('[data-check="' + n + '"]');
  await p.waitForTimeout(60);
  const fb = await $('#fb' + n);
  ok('activité ' + n + ' refuse tant que « ' + cle + ' » est fermé', fb.startsWith('🔒'),
    fb.slice(0, 50));
}

/* ── le simulateur ───────────────────────────────────────────────────────── */
if (niveau === '5e') {
  const S = REP.simulateur;
  const lus = [];
  for (const m of S.materiaux) {
    await p.selectOption('#mat', m);
    await p.click('#calculer');
    await p.waitForTimeout(50);
    lus.push(await $('#lSigma'));
    ok('coefficient de « ' + m + ' »', (await $('#lCoef')) === S.coefficients[m],
      'lu ' + (await $('#lCoef')) + ', attendu ' + S.coefficients[m]);
  }
  ok('la contrainte ne dépend PAS du matériau',
    lus.every(x => x === S.sigma_service), lus.join(' · '));

  for (const m of S.materiaux) {
    await p.selectOption('#mat', m);
    await p.click('#ajouter');
    await p.waitForTimeout(40);
  }
  ok('les cinq essais sont reportés', (await $('#nEssais')) === String(S.materiaux.length));
  ok('le tableau retient ' + S.retenus + ' matériaux',
    (await $('#nRetenus')) === String(S.retenus), 'lu ' + (await $('#nRetenus')));
  const ecarte = await p.evaluate(nom => {
    const tr = [...document.querySelectorAll('#tab tbody tr')]
      .filter(t => t.cells[0].textContent === nom)[0];
    return tr ? tr.className : 'absent';
  }, S.ecarte);
  ok('« ' + S.ecarte +' » est marqué écarté dans le tableau', ecarte === 'ko', ecarte);
} else {
  for (const r of REP.reglages) {
    await p.selectOption('#haut', r.haut);
    await p.selectOption('#cas', r.cas);
    await p.selectOption('#crit', r.crit);
    await p.click('#simuler');
    await p.waitForTimeout(50);
    ok('réglage ' + r.haut + '·' + r.cas + '·' + r.crit + ' → ' + r.n + ' retenu(s)',
      (await $('#nRet')) === r.n, 'lu ' + (await $('#nRet')));
    const noms = await p.$$eval('#tab tbody tr.ok td:first-child', n => n.map(e => e.textContent));
    ok('réglage ' + r.haut + '·' + r.cas + '·' + r.crit + ' → ce sont les bons',
      noms.length === r.retenus.length && r.retenus.every(x => noms.includes(x)),
      noms.join(' · '));
  }
  const M = REP.moments;
  await p.selectOption('#haut', REP.bonReglage.haut);
  await p.selectOption('#cas', 'vent');
  await p.click('#simuler');
  await p.waitForTimeout(60);
  const lus = await p.$$eval('#tab tbody tr', n =>
    Object.fromEntries(n.map(t => [t.cells[0].textContent, t.cells[1].textContent])));
  for (const [nom, m] of Object.entries(M)) {
    ok('moment du vent sur « ' + nom + ' »',
      lus[nom] === String(m.vent).replace('.', ',') + ' N·m',
      'lu ' + lus[nom] + ', attendu ' + m.vent + ' N·m');
  }
  const noms = Object.keys(M);
  ok('le vent ne charge PAS tous les profilés pareil',
    new Set(noms.map(n => M[n].vent)).size > 1,
    noms.map(n => M[n].vent).join(' · '));
  ok('le banc, lui, charge tout le monde pareil',
    new Set(noms.map(n => M[n].banc)).size === 1,
    noms.map(n => M[n].banc).join(' · '));
}

/* ── les activités, une fois les verrous ouverts ─────────────────────────── */
if (niveau === '3e') {
  await p.selectOption('#haut', REP.bonReglage.haut);
  await p.selectOption('#cas', REP.bonReglage.cas);
  await p.selectOption('#crit', REP.bonReglage.crit);
  await p.click('#simuler');
  await p.waitForTimeout(60);
}
for (const [n, champs] of Object.entries(REP.activites)) {
  for (const [id, val] of Object.entries(champs)) {
    const el = await p.$('#' + id);
    if (!el) { ok('champ ' + id + ' présent', false); continue; }
    await p.selectOption('#' + id, val);
  }
  await p.click('[data-check="' + n + '"]');
  await p.waitForTimeout(60);
  const fb = await $('#fb' + n);
  const total = Object.keys(champs).length;
  ok('activité ' + n + ' validée (' + total + '/' + total + ')',
    fb.includes('✅ ' + total + '/' + total), fb.slice(0, 70));
}

/* ── une réponse fausse est refusée ──────────────────────────────────────── */
const [premierId, bonne] = Object.entries(REP.activites['1'])[0];
const options = await p.$$eval('#' + premierId + ' option', n => n.map(e => e.value));
const fausse = options.filter(o => o && o !== bonne)[0];
await p.selectOption('#' + premierId, fausse);
await p.click('[data-check="1"]');
await p.waitForTimeout(60);
ok('une réponse fausse est refusée', !(await $('#fb1')).startsWith('✅'),
  (await $('#fb1')).slice(0, 50));
await p.selectOption('#' + premierId, bonne);
await p.click('[data-check="1"]');
await p.waitForTimeout(60);

/* ── la mémoire ──────────────────────────────────────────────────────────── */
const [idH, valH] = Object.entries(REP.persistance)[0];
await p.fill('#' + idH, valH);
await p.waitForTimeout(120);
await p.reload({ waitUntil: 'load' });
await p.waitForTimeout(400);
ok('les réponses survivent au rechargement', (await p.inputValue('#' + idH)) === valH,
  idH + ' = ' + (await p.inputValue('#' + idH)));
ok('l’hypothèse est rappelée au bilan', (await $('#rappelHyp')) === valH,
  await $('#rappelHyp'));
ok('les verrous survivent au rechargement',
  (await p.evaluate(() => Object.keys(window.__exp || {}).filter(k => window.__exp[k]))).length > 0);
ok('le tableau du simulateur est reconstruit au rechargement',
  (await p.$$eval('#tab tbody tr', n => n.length)) > 1);

const n0 = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close();
process.exit(n0 === T.length ? 0 : 1);
