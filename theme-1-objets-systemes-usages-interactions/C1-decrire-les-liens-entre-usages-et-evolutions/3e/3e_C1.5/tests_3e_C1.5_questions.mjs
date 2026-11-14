/* Banc des questions fermées de 3e_C1.5 (numérique et société) — écrit le 14/11/2026, quand les activités 1, 2, 3.a et 3.b
   ont reçu des questions vérifiées par la page (thème 1 : « Claude écrit les questions »).
   Il joue chaque bloc comme l'élève : rien coché, une erreur, tout juste ; la tâche du tableau de bord ; les réponses
   relues après rechargement (sauvegarde de la page, saveProgress4).
   Usage : node tests_3e_C1.5_questions.mjs */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';

const URL0 = pathToFileURL(path.join(import.meta.dirname, 'sequence-numerique-societe-economie-environnement-sante.html')).href;
const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
const err = []; p.on('pageerror', (e) => err.push(e.message)); p.on('dialog', (d) => d.dismiss().catch(() => {}));
await p.goto(URL0, { waitUntil: 'load' }); await p.evaluate(() => localStorage.clear()); await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(300);

const ATT = await p.evaluate(() => { const out = {}; for (const s of [...document.scripts]) { for (const m of s.textContent.matchAll(/const ATT(S\w+) = \{([^}]*)\};/g)) {
  out[m[1].toLowerCase()] = Object.fromEntries([...m[2].matchAll(/(\w+):"((?:[^"\\]|\\.)*)"/g)].map((x) => [x[1], JSON.parse('"' + x[2] + '"')])); } } return out; });
const BLOCS = { s1: 's1', s2: 's2', s3a: 's3', s3b: 's3' };
const NB = { s1: 3, s2: 3, s3a: 4, s3b: 3 };
ok('les réponses attendues des quatre blocs se lisent dans la page (3, 3, 4, 3)', Object.keys(BLOCS).every((k) => ATT[k] && Object.keys(ATT[k]).length === NB[k]),
  Object.keys(BLOCS).map((k) => k + ':' + (ATT[k] ? Object.keys(ATT[k]).length : 0)).join(' '));
const options = (id) => p.$$eval(`#${id} input[type=radio]`, (l) => l.map((x) => x.value));
let uniques = true; const places = {}; const det = [];
for (const k of Object.keys(BLOCS)) for (const [id, v] of Object.entries(ATT[k])) {
  const o = await options(id); if (o.filter((x) => x === v).length !== 1 || o.length !== 4) { uniques = false; det.push(id); }
  const i = o.indexOf(v); places[i] = (places[i] || 0) + 1;
}
ok('chaque réponse attendue est une proposition, une seule fois, parmi quatre', uniques, det.join(', '));
ok('la bonne réponse change de place (aucune place n\'en a plus de la moitié)', Object.values(places).every((n) => n <= 7), JSON.stringify(places));
const choisir = (id, val) => p.evaluate(([id, val]) => { [...document.querySelectorAll(`#${id} input[type=radio]`)].find((x) => x.value === val).click(); }, [id, val]);
const fb = async (k) => (await p.locator('#fb-' + k).textContent()).trim();
const bandeau = () => p.evaluate(() => document.getElementById('tachesBandeau').innerText);
const ouvrir = async (s) => { await p.click(`.seance-tab[data-panel="${s}"]`); await p.waitForTimeout(100); };
for (const [k, s] of Object.entries(BLOCS)) {
  await ouvrir(s);
  const ids = Object.keys(ATT[k]);
  ok(`${k} : deux aides, une correction (avec « À retenir »), un critère, repliés au départ`, await p.evaluate((k) => {
    const x = document.getElementById('verif-' + k);
    return !!x.querySelector('details.aide1') && !!x.querySelector('details.aide2') && !!x.querySelector('details.correction .retenir') && !!x.querySelector('.critere')
      && [...x.querySelectorAll('details')].every((d) => !d.open); }, k));
  await p.click(`[data-check="${k}"]`); await p.waitForTimeout(60);
  ok(`${k} : vérifier sans répondre dit combien de questions restent`, (await fb(k)).startsWith(`Il reste ${ids.length} questions`), await fb(k));
  for (const id of ids) await choisir(id, ATT[k][id]);
  const autre = (await options(ids[1])).find((x) => x !== ATT[k][ids[1]]);
  await choisir(ids[1], autre); await p.click(`[data-check="${k}"]`); await p.waitForTimeout(60);
  const marques = await p.evaluate((ids) => ids.filter((id) => document.getElementById(id).classList.contains('ko')), ids);
  const avant = ((await bandeau()).match(/☑/g) || []).length;
  ok(`${k} : une erreur → « à revoir » sur cette question seule`, ((await fb(k)).startsWith('🟡') || (await fb(k)).startsWith('🔁')) && marques.length === 1 && marques[0] === ids[1], await fb(k));
  await choisir(ids[1], ATT[k][ids[1]]); await p.click(`[data-check="${k}"]`); await p.waitForTimeout(60);
  ok(`${k} : tout juste → « validé », et la tâche se coche`, (await fb(k)).includes('validé') && ((await bandeau()).match(/☑/g) || []).length === avant + 1, (await bandeau()).replace(/\n/g, ' · '));
}
await p.waitForTimeout(900);   // la sauvegarde de la page part 600 ms après le dernier choix
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
const rest = await p.evaluate((ATT) => Object.values(ATT).every((a) => Object.entries(a).every(([id, v]) => {
  const c = document.querySelector(`#${id} input[type=radio]:checked`); return c && c.value === v; })), ATT);
ok('après rechargement, les 13 réponses choisies reviennent (sauvegarde de la page)', rest);
const coches = []; for (const s of ['s1', 's2', 's3']) { await ouvrir(s); coches.push(((await bandeau()).match(/☑/g) || []).length); }
ok('après rechargement, les blocs validés restent cochés (1 + 1 + 2)', coches.join(',') === '1,1,2', coches.join(','));
ok('les vérifications de 1 bis et de l\'activité 5 portent leur réponse pour le mode mission (data-check, data-bonne)', await p.evaluate(() =>
  !!document.querySelector('#b1_verifier[data-check]') && !!document.querySelector('#a5_verifier[data-check]') && document.querySelectorAll('fieldset[data-bonne]').length === 6));
ok('aucune erreur JS', err.length === 0, err.slice(0, 2).join(' | '));

const n0 = T.filter((x) => x.ok).length;
console.log(T.map((x) => `${x.ok ? '✅' : '❌'} ${x.n}${x.d ? ' — ' + x.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close(); process.exit(n0 === T.length ? 0 : 1);
