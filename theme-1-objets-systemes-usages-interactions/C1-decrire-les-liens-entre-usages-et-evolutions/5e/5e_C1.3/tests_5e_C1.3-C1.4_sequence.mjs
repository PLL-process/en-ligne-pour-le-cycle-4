/* Banc du lot 5e_C1.3-C1.4 (C1.3-C1.4_SI) — la séquence dans un vrai navigateur. Écrit le 04/11/2026, quand la page est
   passée à trois séances à onglets (vague n°311) : le lot n'avait qu'un contrôle statique (`_outils/test_lot_theme1_5e_c1_3_c1_4.py`).
   Il couvre, comme l'élève : les séances (un onglet, un panneau, la clôture à la dernière seulement, le bouton vers la
   suivante), la sauvegarde (chaque zone [data-save] remplie dans sa séance, relue après rechargement, l'effacement), le
   positionnement et le retour à l'hypothèse, les questions fermées de chaque activité (14/11/2026 : réponses attendues
   recalculées depuis le fichier de l'activité 3, juste / à revoir, tâche cochée, relues après rechargement), et l'exercice incrusté des ateliers (la carte mentale, juste puis relu).
   Usage : node tests_5e_C1.3-C1.4_sequence.mjs */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';
import fs from 'fs';

const URL0 = pathToFileURL(path.join(import.meta.dirname, 'sequence_C1.3-C1.4_SI_gestion_donnees.html')).href;
const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
const err = [], fail = [];
p.on('pageerror', (e) => err.push(e.message));
p.on('console', (m) => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', (r) => fail.push(r.url()));
p.on('dialog', (d) => d.dismiss().catch(() => {}));
await p.goto(URL0, { waitUntil: 'load' }); await p.evaluate(() => localStorage.clear()); await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(200);
// 21/11/2026 — le billet de sortie (n°330) : une preuve faite seul, sur un objet que la séquence n'a pas étudié ; il ne valide rien.
{ const bs = await p.evaluate(() => { const b = document.getElementById('billetSortie'); if (!b) return null; const c = b.querySelector('details.correction'); const n = b.nextElementSibling; const pan = b.closest('.seance-panel'); const tous = [...document.querySelectorAll('.seance-panel')].filter(x => !/hors/.test(x.id)); return { zones: b.querySelectorAll('textarea[data-save]').length, etayees: b.querySelectorAll('details.etayage').length, criteres: c ? (c.textContent.match(/Critère/g) || []).length : 0, avantBonus: !!(n && /Bonus/.test(n.textContent.slice(0, 300))), derniere: !!pan && pan === tous[tous.length - 1], boutons: b.querySelectorAll('button').length }; }); ok('billet de sortie (n°330) : deux réponses écrites, deux versions étayées, deux critères, dernière séance, avant le Bonus, aucun bouton', !!bs && bs.zones === 2 && bs.etayees === 2 && bs.criteres === 2 && bs.avantBonus && bs.derniere && bs.boutons === 0, JSON.stringify(bs)); }
ok('charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('aucune requête échouée', fail.length === 0, fail.slice(0, 2).join(' | '));

const vis = (sel) => p.evaluate((s) => { const e = document.querySelector(s); return !!e && e.checkVisibility({ checkVisibilityCSS: true }); }, sel);
const ouvrir = async (id) => { await p.click(`.seance-tab[data-panel="${id}"]`); await p.waitForTimeout(80); };
const ouvrirSeanceDe = async (sel) => {
  const pan = await p.evaluate((s) => { const x = document.querySelector(s).closest('.seance-panel'); return x && !x.classList.contains('active') ? x.id : null; }, sel);
  if (pan) await ouvrir(pan);
  // un bloc replié (le Bonus, révision du 08/11/2026) s'ouvre comme le ferait l'élève
  await p.evaluate((s) => { for (let d = document.querySelector(s).closest('details'); d; d = d.parentElement.closest('details')) d.open = true; }, sel);
};

// ── les séances ──────────────────────────────────────────────────────────
const onglets = await p.$$eval('.seance-tab', (l) => l.map((x) => x.dataset.panel));
ok('trois séances à onglets', JSON.stringify(onglets) === '["s1","s2","s3"]', onglets.join(','));
const CLOTURE = ['.bonus', '#rappelHyp', '.positionnement', '.qcm-box'];
for (const id of onglets) {
  await ouvrir(id);
  const r = await p.evaluate((id) => ({ seuls: [...document.querySelectorAll('.seance-panel')].every((x) => x.checkVisibility() === (x.id === id)),
    actif: document.querySelector('.seance-tab.active').dataset.panel }), id);
  ok(`séance ${id} : son onglet est actif et son panneau est le seul affiché`, r.seuls && r.actif === id);
  const cl = [];
  for (const s of CLOTURE) cl.push(await p.evaluate((s) => [...document.querySelectorAll(s)].some((e) => e.closest('.seance-panel').checkVisibility()), s));
  ok(`séance ${id} : la clôture (Bonus, bilan, positionnement, QCM) ${id === 's3' ? 'est là' : 'n\'est pas là'}`, id === 's3' ? cl.every(Boolean) : !cl.some(Boolean), cl.join(','));
}
await ouvrir('s1');
await p.click('#s1 .vers-seance'); await p.waitForTimeout(120);
ok('le bouton de fin de séance 1 ouvre la séance 2', await p.evaluate(() => document.querySelector('.seance-panel.active').id === 's2'));
await p.click('#s2 .vers-seance'); await p.waitForTimeout(120);
ok('le bouton de fin de séance 2 ouvre la séance 3', await p.evaluate(() => document.querySelector('.seance-panel.active').id === 's3'));
ok('un seul bouton vers le QCM, à la séance 3', (await p.$$eval('a.button[href*="qcm_"]', (l) => l.map((a) => a.closest('.seance-panel') && a.closest('.seance-panel').id))).join() === 's3');

// ── la sauvegarde : chaque zone [data-save], remplie dans sa séance ───────
const zones = await p.$$eval('[data-save]', (l) => l.map((e) => e.dataset.save));
ok('les zones de réponse sont annoncées par la carte de sauvegarde', (await p.textContent('#nbZones')).trim() === `Les ${zones.length}`, (await p.textContent('#nbZones')).trim() + ' / ' + zones.length);
for (const z of zones) {
  const sel = `[data-save="${z}"]`;
  await ouvrirSeanceDe(sel);
  if (await p.evaluate((s) => !!document.querySelector(s).closest('#ouverture'), sel)) await ouvrir('s1');
  await p.fill(sel, 'Essai du banc : ' + z);
}
ok('le retour à l\'hypothèse relit l\'hypothèse du début', (await p.textContent('#rappelHyp')).includes('Essai du banc : hypothese') && await p.evaluate(() => !document.getElementById('rappelHyp').hidden));
await ouvrir('s3');
await p.check('input[name="pos_c13"][value="3"]'); await p.check('input[name="pos_c14"][value="2"]');
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(250);
const relus = await p.$$eval('[data-save]', (l) => l.filter((e) => e.value === 'Essai du banc : ' + e.dataset.save).length);
ok(`les ${zones.length} zones survivent au rechargement`, relus === zones.length, `${relus} / ${zones.length}`);
ok('le positionnement survit au rechargement', await p.isChecked('input[name="pos_c13"][value="3"]') && await p.isChecked('input[name="pos_c14"][value="2"]'));
ok('l\'onglet en cours survit au rechargement (séance 3)', await p.evaluate(() => document.querySelector('.seance-panel.active').id === 's3'));

// ── l'exercice incrusté des ateliers (la carte mentale, exercice 1) ───────
await ouvrir('s1');
const def = await p.evaluate(() => JSON.parse(document.querySelector('#incruste-cm-5e-hangzhou-donnees script[type="application/json"]').textContent));
const ex = def.exercices.cm_5e_e1;
await p.evaluate((ex) => {
  const boite = document.querySelector('[data-exo="cm_5e_e1"]');
  ex.widgets.forEach((w) => {
    if (w.type === 'cases') boite.querySelectorAll(`input[name="${w.name}"]`).forEach((c) => { c.checked = w.bonnes.includes(c.value); c.dispatchEvent(new Event('change', { bubbles: true })); });
    if (w.type === 'slots') w.slots.forEach((s) => { const r = [...boite.querySelectorAll(`input[name="${s.name}"]`)].find((x) => x.value === s.bonnes[0]); r.checked = true; r.dispatchEvent(new Event('change', { bubbles: true })); });
  });
}, ex);
ok('l\'exercice incrusté est visible à la séance 1', await vis('#incruste-cm-5e-hangzhou-donnees .btn.verifier'));
await p.click('#incruste-cm-5e-hangzhou-donnees .btn.verifier'); await p.waitForTimeout(150);
const retour = await p.evaluate(() => { const z = document.querySelector('#incruste-cm-5e-hangzhou-donnees .retour[data-retour]'); return { c: z.className, t: z.textContent.slice(0, 40) }; });
ok('l\'exercice incrusté, rempli juste, est validé', /\bok\b/.test(retour.c) && retour.t.includes('Tout est juste'), retour.t);
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(250);
const relu = await p.evaluate((ex) => { const boite = document.querySelector('[data-exo="cm_5e_e1"]'); let n = 0, tot = 0;
  ex.widgets.forEach((w) => { if (w.type === 'cases') w.bonnes.forEach((v) => { tot++; if (boite.querySelector(`input[name="${w.name}"][value="${v}"]`).checked) n++; });
    if (w.type === 'slots') w.slots.forEach((s) => { tot++; const r = [...boite.querySelectorAll(`input[name="${s.name}"]`)].find((x) => x.value === s.bonnes[0]); if (r.checked) n++; }); });
  return [n, tot]; }, ex);
ok('les réponses de l\'exercice incrusté survivent au rechargement', relu[0] === relu[1], relu.join(' / '));

// ── les questions fermées vérifiées par la page (révision du 14/11/2026) : chaque activité se valide sur une production
//    réelle — ses réponses choisies, jugées une à une — et non sur un bouton « j'ai fini » ──
const ATT = await p.evaluate(() => { for (const s of [...document.scripts]) { const m = s.textContent.match(/const ATT1 = \{[\s\S]*?const ATTENDUES/);
  if (m) return new Function(m[0].replace('const ATTENDUES', '') + 'return {1:ATT1,2:ATT2,3:ATT3};')(); } return null; });
ok('les réponses attendues des trois activités se lisent dans la page', ATT && [1, 2, 3].every((n) => Object.keys(ATT[n]).length >= 6),
  ATT ? [1, 2, 3].map((n) => Object.keys(ATT[n]).length).join(' / ') : '(introuvables)');
const options = (id) => p.$$eval(`#${id} input[type=radio]`, (l) => l.map((x) => x.value));
let uniques = true; const detUnique = [];
for (const n of [1, 2, 3]) for (const [id, v] of Object.entries(ATT[n])) {
  const o = await options(id); if (o.filter((x) => x === v).length !== 1 || o.length < 3) { uniques = false; detUnique.push(id); }
}
ok('chaque réponse attendue est une option, une seule fois, parmi au moins trois', uniques, detUnique.join(', '));
// les réponses de l'activité 3, recalculées depuis le fichier que l'élève ouvre : « prioritaire » si incidents ≥ 3 OU autonomie < 35 %
const csv = fs.readFileSync(path.join(import.meta.dirname, 'donnees_velos_hangzhou_simulees.csv'), 'utf8').trim().split('\n').slice(1)
  .map((l) => l.split(';')).map((c) => ({ id: c[0], inc: +c[3], auto: +c[4] }));
const prio = (v) => v.inc >= 3 || v.auto < 35;
const tri = [...csv].sort((a, b2) => b2.inc - a.inc);
const v = (id) => csv.find((x) => x.id === id);
ok('activité 3 : le nombre de vélos prioritaires vient du fichier', String(csv.filter(prio).length) === ATT[3].a3_nombre, `${csv.filter(prio).map((x) => x.id).join(', ')} → attendu ${ATT[3].a3_nombre}`);
ok('activité 3 : le premier vélo après le tri par incidents décroissants vient du fichier', tri[0].id === ATT[3].a3_premier && tri[0].inc > tri[1].inc, `${tri[0].id} (${tri[0].inc}) puis ${tri[1].id} (${tri[1].inc})`);
ok('activité 3 : les frontières suivent la règle (V-108 à 3 incidents, V-105 à 31 %, un vélo à 35 % et 1 incident)',
  prio(v('V-108')) && v('V-108').inc === 3 && ATT[3].a3_v108.startsWith('prioritaire')
  && prio(v('V-105')) && v('V-105').inc < 3 && ATT[3].a3_v105.startsWith('prioritaire')
  && !prio({ inc: 1, auto: 35 }) && ATT[3].a3_limite.startsWith('non prioritaire'));
const choisir = (id, val) => p.evaluate(([id, val]) => { const r = [...document.querySelectorAll(`#${id} input[type=radio]`)].find((x) => x.value === val); r.click(); }, [id, val]);
const fb = async (n) => (await p.locator('#fb' + n).textContent()).trim();
const bandeau = () => p.evaluate(() => document.getElementById('tachesBandeau').innerText);
for (const [n, s] of [[1, 's1'], [2, 's2'], [3, 's3']]) {
  await ouvrir(s);
  const ids = Object.keys(ATT[n]);
  ok(`activité ${n} : son bloc a deux aides, une correction et un message, tout replié au départ`, await p.evaluate((n) => {
    const x = document.querySelector(`[data-check="${n}"]`).closest('.verif-c13');
    return !!x.querySelector('details.aide1') && !!x.querySelector('details.aide2') && !!x.querySelector('details.correction')
      && [...x.querySelectorAll('details')].every((d) => !d.open) && !!x.querySelector('#fb' + n); }, n));
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(60);
  ok(`activité ${n} : vérifier sans répondre dit combien de questions restent`, (await fb(n)).startsWith(`Il reste ${ids.length} questions`), await fb(n));
  for (const id of ids) await choisir(id, ATT[n][id]);
  const autre = (await options(ids[1])).find((x) => x !== ATT[n][ids[1]]);
  await choisir(ids[1], autre); await p.click(`[data-check="${n}"]`); await p.waitForTimeout(60);
  const marques = await p.evaluate((ids) => ids.filter((id) => document.getElementById(id).classList.contains('ko')), ids);
  ok(`activité ${n} : une réponse fausse → « à revoir », sur cette question seule, et la tâche reste à faire`,
    (await fb(n)).startsWith('🟡') && marques.length === 1 && marques[0] === ids[1] && !(await bandeau()).includes('☑'), await fb(n));
  await choisir(ids[1], ATT[n][ids[1]]); await p.click(`[data-check="${n}"]`); await p.waitForTimeout(60);
  ok(`activité ${n} : tout juste → « activité validée », et la tâche se coche au tableau de bord`,
    (await fb(n)).includes('activité validée') && (await bandeau()).includes('☑'), (await bandeau()).replace(/\n/g, ' · '));
}
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(250);
const nAtt = [1, 2, 3].reduce((s, n) => s + Object.keys(ATT[n]).length, 0);
const rest = await p.evaluate((ATT) => [1, 2, 3].every((n) => Object.entries(ATT[n]).every(([id, v]) => {
  const c = document.querySelector(`#${id} input[type=radio]:checked`); return c && c.value === v; })), ATT);
ok(`après rechargement, les ${nAtt} réponses choisies reviennent`, rest);
const coches = [];
for (const s of ['s1', 's2', 's3']) { await ouvrir(s); coches.push((await bandeau()).includes('☑')); }
ok('après rechargement, les trois tâches validées restent cochées', coches.every(Boolean), coches.join(','));
await ouvrir('s1'); await p.click('[data-check="1"]'); await p.waitForTimeout(60);
const marqueAvant = await p.evaluate(() => document.getElementById('a1_qr').classList.contains('ok'));
await choisir('a1_qr', (await options('a1_qr')).find((x) => x !== ATT[1].a1_qr));
ok('changer une réponse retire sa marque « juste » jusqu\'à la prochaine vérification', marqueAvant && await p.evaluate(() => !document.getElementById('a1_qr').classList.contains('ok')));

// ── l'effacement ─────────────────────────────────────────────────────────
await ouvrir('s2');
await p.click('#clear'); await p.waitForTimeout(120);
const vides = await p.$$eval('[data-save]', (l) => l.every((e) => !e.value));
const radiosVides = await p.$$eval('.positionnement input[type=radio]', (l) => l.every((r) => !r.checked));
const fermeesVides = await p.$$eval('.verif-c13 input[type=radio]', (l) => l.every((r) => !r.checked));
ok('« Effacer mes réponses locales » vide les zones, le positionnement et les questions fermées', vides && radiosVides && fermeesVides && await p.evaluate(() => document.getElementById('rappelHyp').hidden));
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(250);
ok('après effacement et rechargement, rien ne revient', await p.$$eval('[data-save]', (l) => l.every((e) => !e.value)) && await p.$$eval('.positionnement input[type=radio]', (l) => l.every((r) => !r.checked))
  && await p.$$eval('.verif-c13 input[type=radio]', (l) => l.every((r) => !r.checked)) && !(await p.evaluate(() => document.getElementById('tachesBandeau').innerText)).includes('☑'));
// ── après « Effacer », une nouvelle frappe n'enregistre que ce qu'on tape (04/11/2026) : la mémoire de la page était
//    gardée, et la première frappe réécrivait toutes les anciennes réponses ──
for (const z of zones) {
  const sel = `[data-save="${z}"]`;
  await ouvrirSeanceDe(sel);
  if (await p.evaluate((s) => !!document.querySelector(s).closest('#ouverture'), sel)) await ouvrir('s1');
  await p.fill(sel, 'Ancienne réponse : ' + z);
}
await ouvrir('s3'); await p.check('input[name="pos_c13"][value="4"]');
await p.click('#clear'); await p.waitForTimeout(120);
await p.locator('[data-save="conclusion"]').pressSequentially('z');
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(250);
const apres = await p.$$eval('[data-save]', (l) => l.filter((e) => e.value).map((e) => e.dataset.save + '=' + e.value));
ok('effacer, taper une lettre, recharger : seule la nouvelle valeur revient', apres.length === 1 && apres[0] === 'conclusion=z'
  && await p.$$eval('.positionnement input[type=radio]', (l) => l.every((r) => !r.checked)), apres.slice(0, 3).join(' | ') || '(rien)');
ok('aucune erreur JS sur tout le parcours', err.length === 0, err.slice(0, 2).join(' | '));

const n0 = T.filter((x) => x.ok).length;
console.log(T.map((x) => `${x.ok ? '✅' : '❌'} ${x.n}${x.d ? ' — ' + x.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close(); process.exit(n0 === T.length ? 0 : 1);
