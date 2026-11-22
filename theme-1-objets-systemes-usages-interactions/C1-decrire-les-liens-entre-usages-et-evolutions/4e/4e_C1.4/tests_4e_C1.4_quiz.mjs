/* Banc des quiz de 4e_C1.4 (cybersécurité) — écrit le 14/11/2026, quand les cinq quiz à deux propositions sont devenus des
   questions à quatre propositions, vérifiées quiz par quiz (thème 1 : « Claude écrit les questions »).
   Il joue chaque quiz comme l'élève : rien coché, une erreur, tout juste ; la tâche du tableau de bord ; le score de la
   section qui compte les nouvelles questions ; les réponses relues après rechargement.
   Usage : node tests_4e_C1.4_quiz.mjs */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';

const URL0 = pathToFileURL(path.join(import.meta.dirname, 'sequence-cybersecurite-protection-donnees.html')).href;
const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
const err = []; p.on('pageerror', (e) => err.push(e.message)); p.on('dialog', (d) => d.dismiss().catch(() => {}));
await p.goto(URL0, { waitUntil: 'load' }); await p.evaluate(() => localStorage.clear()); await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(300);
// 21/11/2026 — le billet de sortie (n°330) : une preuve faite seul, sur un objet que la séquence n'a pas étudié ; il ne valide rien.
{ const bs = await p.evaluate(() => { const b = document.getElementById('billetSortie'); if (!b) return null; const c = b.querySelector('details.correction'); const n = b.nextElementSibling; const pan = b.closest('.seance-panel'); const tous = [...document.querySelectorAll('.seance-panel')].filter(x => !/hors/.test(x.id)); return { zones: b.querySelectorAll('textarea[data-save]').length, etayees: b.querySelectorAll('details.etayage').length, criteres: c ? (c.textContent.match(/Critère/g) || []).length : 0, avantBonus: !!(n && /Bonus/.test(n.textContent.slice(0, 300))), derniere: !!pan && pan === tous[tous.length - 1], boutons: b.querySelectorAll('button').length }; }); ok('billet de sortie (n°330) : deux réponses écrites, deux versions étayées, deux critères, dernière séance, avant le Bonus, aucun bouton', !!bs && bs.zones === 2 && bs.etayees === 2 && bs.criteres === 2 && bs.avantBonus && bs.derniere && bs.boutons === 0, JSON.stringify(bs)); }

const ATT = await p.evaluate(() => { const out = {}; for (const s of [...document.scripts]) { for (const m of s.textContent.matchAll(/const ATTQ(\d) = \{([^}]*)\};/g)) {
  out[m[1]] = Object.fromEntries([...m[2].matchAll(/(\w+):"((?:[^"\\]|\\.)*)"/g)].map((x) => [x[1], JSON.parse('"' + x[2] + '"')])); } } return out; });
const QUIZ = { 1: 's1', 3: 's2', 4: 's2', 5: 's3', 6: 's4' };
ok('les réponses attendues des cinq quiz se lisent dans la page, 7 questions chacun', Object.keys(QUIZ).every((n) => ATT[n] && Object.keys(ATT[n]).length === 7),
  Object.keys(QUIZ).map((n) => n + ':' + (ATT[n] ? Object.keys(ATT[n]).length : 0)).join(' '));
const options = (id) => p.$$eval(`#${id} input[type=radio]`, (l) => l.map((x) => x.value));
let uniques = true, places = {}; const det = [];
for (const n of Object.keys(QUIZ)) for (const [id, v] of Object.entries(ATT[n])) {
  const o = await options(id); if (o.filter((x) => x === v).length !== 1 || o.length !== 4) { uniques = false; det.push(id); }
  if (!(await p.evaluate((id) => document.getElementById(id).classList.contains('qcm-grille'), id))) { const i = o.indexOf(v); places[i] = (places[i] || 0) + 1; }
}
ok('chaque réponse attendue est une proposition, une seule fois, parmi quatre', uniques, det.join(', '));
ok('la bonne réponse change de place d\'une question à l\'autre (aucune place n\'en a plus de la moitié)', Object.values(places).every((k) => k <= 16), JSON.stringify(places));
const choisir = (id, val) => p.evaluate(([id, val]) => { [...document.querySelectorAll(`#${id} input[type=radio]`)].find((x) => x.value === val).click(); }, [id, val]);
const fb = async (n) => (await p.locator('#fbq' + n).textContent()).trim();
const bandeau = () => p.evaluate(() => document.getElementById('tachesBandeau').innerText);
const ouvrir = async (s) => { await p.click(`.seance-tab[data-panel="${s}"]`); await p.waitForTimeout(100); };
for (const [n, s] of Object.entries(QUIZ)) {
  await ouvrir(s);
  const ids = Object.keys(ATT[n]);
  ok(`quiz ${n} : deux aides, une correction (avec « À retenir ») et un message, repliés au départ`, await p.evaluate((n) => {
    const x = document.getElementById('quiz' + n);
    return !!x.querySelector('details.aide1') && !!x.querySelector('details.aide2') && !!x.querySelector('details.correction .retenir')
      && [...x.querySelectorAll('details')].every((d) => !d.open) && !!x.querySelector('#fbq' + n); }, n));
  await p.click(`[data-check="q${n}"]`); await p.waitForTimeout(60);
  ok(`quiz ${n} : vérifier sans répondre dit combien de questions restent`, (await fb(n)).startsWith('Il reste 7 questions'), await fb(n));
  for (const id of ids) await choisir(id, ATT[n][id]);
  const autre = (await options(ids[2])).find((x) => x !== ATT[n][ids[2]]);
  await choisir(ids[2], autre); await p.click(`[data-check="q${n}"]`); await p.waitForTimeout(60);
  const marques = await p.evaluate((ids) => ids.filter((id) => document.getElementById(id).classList.contains('ko')), ids);
  const ligne = async () => (await bandeau()).split('\n').find((l) => l.includes(n === '1' ? 'Menaces' : n === '3' ? 'Données personnelles' : n === '4' ? 'Protection' : n === '5' ? 'Traces' : 'Propriété')) || '';
  ok(`quiz ${n} : une erreur → « à revoir » sur cette question seule, la tâche reste à faire`,
    (await fb(n)).startsWith('🟡') && marques.length === 1 && marques[0] === ids[2] && (await ligne()).startsWith('☐'), await fb(n));
  await choisir(ids[2], ATT[n][ids[2]]); await p.click(`[data-check="q${n}"]`); await p.waitForTimeout(60);
  ok(`quiz ${n} : tout juste → « quiz validé », et la tâche se coche`, (await fb(n)).includes('quiz validé') && (await ligne()).startsWith('☑'), await ligne());
  await p.click('#chk' + n); await p.waitForTimeout(60);
  const res = (await p.locator('#res' + n).textContent()).trim(), total = await p.evaluate((n) => blocsDe(n).length, n);
  ok(`quiz ${n} : le score de la section compte les 7 questions du quiz`, total >= 7 && /^(\d+) bonnes? réponses? sur (\d+)/.test(res) && +res.match(/^(\d+)/)[1] >= 7, res);
}
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
const rest = await p.evaluate((ATT) => Object.values(ATT).every((a) => Object.entries(a).every(([id, v]) => {
  const c = document.querySelector(`#${id} input[type=radio]:checked`); return c && c.value === v; })), ATT);
ok('après rechargement, les 35 réponses choisies reviennent (sauvegarde de la page)', rest);
const coches = []; for (const s of ['s1', 's2', 's3', 's4']) { await ouvrir(s); coches.push(((await bandeau()).match(/☑/g) || []).length); }
ok('après rechargement, les cinq quiz validés restent cochés (1 + 2 + 1 + 1, séance 4 depuis le 14/11/2026)', coches.join(',') === '1,2,1,1', coches.join(','));
ok('aucune erreur JS', err.length === 0, err.slice(0, 2).join(' | '));

const n0 = T.filter((x) => x.ok).length;
console.log(T.map((x) => `${x.ok ? '✅' : '❌'} ${x.n}${x.d ? ' — ' + x.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close(); process.exit(n0 === T.length ? 0 : 1);
