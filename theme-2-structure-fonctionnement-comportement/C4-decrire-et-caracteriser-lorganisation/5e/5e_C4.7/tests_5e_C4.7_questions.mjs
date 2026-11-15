/* Banc des questions de 5e_C4.7 (le réseau local de la salle) — écrit le 14/11/2026, révision des trois thèmes (ligne 31).
   Les questions posées par une liste déroulante sont devenues des groupes de boutons radio (règle d'or n°300) et leurs
   propositions ont été réécrites : la bonne réponse se devinait (23 fois sur 35 la plus longue, n°144).
   Ce banc lit les réponses attendues dans la page (tables ATT0 à ATT5), puis vérifie :
   · chaque réponse attendue est une proposition, une seule fois ; aucune liste ne pose plus de question ;
   · la bonne réponse change de place et n'est presque jamais la plus longue ;
   · une erreur est marquée « à revoir » sur sa seule question ; tout juste valide le billet et les activités 1 à 4 ;
   · les réponses reviennent après rechargement (sauvegarde de la page).
   Usage : node tests_5e_C4.7_questions.mjs */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';

const URL0 = pathToFileURL(path.join(import.meta.dirname, 'sequence_5e_C4.7-C4.8_reseau_local_packet_tracer.html')).href;
const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 390, height: 900 } });
const err = []; p.on('pageerror', (e) => err.push(e.message)); p.on('dialog', (d) => d.dismiss().catch(() => {}));
await p.goto(URL0, { waitUntil: 'load' }); await p.evaluate(() => localStorage.clear()); await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(300);

const ATT = await p.evaluate(() => JSON.parse(JSON.stringify(ATTENDUS)));
const toutes = Object.assign({}, ...Object.values(ATT));
ok('les réponses attendues se lisent dans la page : 6 vérifications, 32 questions', Object.keys(ATT).length === 6 && Object.keys(toutes).length === 32,
   Object.entries(ATT).map(([n, a]) => n + ':' + Object.keys(a).length).join(' '));
const etat = await p.evaluate((A) => {
  const r = { manquent: [], places: {}, longues: 0, listes: [...document.querySelectorAll('body select:not([data-interface])')].map((s) => s.id) };
  for (const [id, v] of Object.entries(A)) {
    const o = [...document.querySelectorAll(`#${id} input[type=radio]`)].map((x) => x.value);
    if (o.length < 3 || o.filter((x) => x === v).length !== 1) { r.manquent.push(id); continue; }
    const i = o.indexOf(v); r.places[i] = (r.places[i] || 0) + 1;
    const L = o.map((x) => x.length), autres = L.filter((_, k) => k !== i);
    if (L[i] > Math.max(...autres) * 1.2) r.longues++;          // visiblement la plus longue (plus de 20 % d'écart)
  }
  return r;
}, toutes);
ok('chaque réponse attendue est une proposition, une seule fois, parmi trois à cinq', etat.manquent.length === 0, etat.manquent.join(', '));
ok('aucune liste déroulante ne pose de question (seule la commande du simulateur reste une liste)', etat.listes.length === 0, etat.listes.join(', '));
ok('la bonne réponse change de place (aucune place n\'en porte plus de 40 %)', Object.values(etat.places).every((k) => k <= 0.4 * 32), JSON.stringify(etat.places));
ok('la bonne réponse n\'est jamais visiblement la plus longue (n°144)', etat.longues === 0, String(etat.longues));

const SEANCE = await p.evaluate(() => Object.fromEntries([0, 1, 2, 3, 4, 5].map((n) => [n, document.querySelector(`[data-check="${n}"]`).closest('.seance-panel').id])));
const ouvrir = async (s) => { await p.click(`.seance-tab[data-panel="${s}"]`); await p.waitForTimeout(100); };
const cocher = (id, v) => p.evaluate(([id, v]) => { [...document.querySelectorAll(`#${id} input[type=radio]`)].find((x) => x.value === v).click(); }, [id, v]);
const fb = async (n) => (await p.locator('#fb' + n).textContent()).trim();
for (const n of ['0', '1', '2', '3', '4', '5']) {
  await ouvrir(SEANCE[n]);
  const ids = Object.keys(ATT[n]);
  for (const id of ids) await cocher(id, ATT[n][id]);
  const autre = await p.evaluate(([id, v]) => [...document.querySelectorAll(`#${id} input[type=radio]`)].map((x) => x.value).find((x) => x !== v), [ids[1], ATT[n][ids[1]]]);
  await cocher(ids[1], autre);
  if (n === '1') await p.fill('#e1_just', 'Pour que chaque message arrive au bon destinataire, chaque adresse doit être unique.');
  if (n === '2') await p.fill('#e2c_prod', "Au centre de mon schéma, j'ai placé le commutateur ; trois traits pleins et trois liaisons en pointillés.");
  if (n === '3') await p.fill('#e3_signal', '47');
  if (n === '4') await p.fill('#e4_just', 'Parce que si deux appareils ont la même adresse, le doublon empêche la livraison au bon appareil.');
  const total = ids.length + (n === '3' ? 1 : 0);                                                                     // la vérification 3 compte aussi le relevé du signal
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(60);
  const marques = await p.evaluate((ids) => ids.filter((id) => document.getElementById(id).classList.contains('ko')), ids);
  ok(`vérification ${n} : une erreur → ${total - 1} / ${total}, seule cette question est marquée « à revoir »`,
     (await fb(n)).startsWith(`${total - 1} / ${total}`) && marques.length === 1 && marques[0] === ids[1] && (await fb(n)).includes('à revoir'), await fb(n));
  await cocher(ids[1], ATT[n][ids[1]]); await p.click(`[data-check="${n}"]`); await p.waitForTimeout(60);
  const valide = await p.evaluate((n) => !!(window.__valid || {})[n], n);
  const juste = (await fb(n)).startsWith(`${total} / ${total}`) && !(await fb(n)).includes('à revoir');
  if (['0', '1', '2', '3', '4'].includes(n)) ok(`vérification ${n} : tout juste → ${total} / ${total}, validée`, juste && valide, await fb(n));
  else ok(`vérification ${n} : tout juste → ${total} / ${total}, plus rien « à revoir » (la validation demande aussi la manipulation et l'écrit)`, juste, await fb(n));
}
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
const rest = await p.evaluate((A) => Object.entries(A).every(([id, v]) => { const c = document.querySelector(`#${id} input[type=radio]:checked`); return c && c.value === v; }), toutes);
ok('après rechargement, les 32 réponses reviennent (sauvegarde de la page)', rest);
const pos = await p.evaluate(() => ['pos_c47', 'pos_c48'].every((id) => { const f = document.getElementById(id);
  return f && f.matches('fieldset.qcm-groupe.positionnement') && f.querySelectorAll('input[type=radio]').length === 4 && /5e_C4\.\d/.test(f.querySelector('legend').textContent); }));
ok('le positionnement : deux groupes de quatre boutons, chacun légendé par son code', pos);
ok('aucune erreur JS', err.length === 0, err.slice(0, 2).join(' | '));

const n0 = T.filter((x) => x.ok).length;
console.log(T.map((x) => `${x.ok ? '✅' : '❌'} ${x.n}${x.d ? ' — ' + x.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close(); process.exit(n0 === T.length ? 0 : 1);
