/* Banc des questions de 4e_C4.7 (SOS serre) — écrit le 14/11/2026, révision des trois thèmes (ligne 30 du suivi).
   Les questions posées par une liste déroulante sont devenues des groupes de boutons radio (règle d'or n°300) et leurs
   propositions ont été réécrites : la bonne réponse se devinait (32 fois sur 40 la plus longue, n°144).
   Ce banc lit les réponses attendues dans la page (tables ATT0 à ATT5), puis vérifie :
   · chaque réponse attendue est une proposition, une seule fois ; aucune liste ne pose plus de question ;
   · la bonne réponse change de place et n'est presque jamais la plus longue ;
   · une erreur est marquée « à revoir » sur sa seule question ; tout juste valide le passeport et les activités 1 à 3 ;
   · les réponses reviennent après rechargement (sauvegarde de la page).
   Usage : node tests_4e_C4.7_questions.mjs */
import { chromium } from 'playwright';
import { pathToFileURL } from 'url';
import path from 'path';

const URL0 = pathToFileURL(path.join(import.meta.dirname, 'sequence_4e_C4.7-C4.9_sos_serre_packet_tracer.html')).href;
const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 390, height: 900 } });
const err = []; p.on('pageerror', (e) => err.push(e.message)); p.on('dialog', (d) => d.dismiss().catch(() => {}));
await p.goto(URL0, { waitUntil: 'load' }); await p.evaluate(() => localStorage.clear()); await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(300);

const ATT = await p.evaluate(() => JSON.parse(JSON.stringify(ATTENDUS)));
const toutes = Object.assign({}, ...Object.values(ATT));
ok('les réponses attendues se lisent dans la page : 6 vérifications, 35 questions', Object.keys(ATT).length === 6 && Object.keys(toutes).length === 35,
   Object.entries(ATT).map(([n, a]) => n + ':' + Object.keys(a).length).join(' '));
const etat = await p.evaluate((A) => {
  const r = { manquent: [], places: {}, longues: 0, listes: [...document.querySelectorAll('body select:not([data-interface])')].map((s) => s.id) };
  for (const [id, v] of Object.entries(A)) {
    const o = [...document.querySelectorAll(`#${id} input[type=radio]`)].map((x) => x.value);
    if (o.length !== 4 || o.filter((x) => x === v).length !== 1) { r.manquent.push(id); continue; }
    const i = o.indexOf(v); r.places[i] = (r.places[i] || 0) + 1;
    const L = o.map((x) => x.length), autres = L.filter((_, k) => k !== i);
    if (L[i] > Math.max(...autres) * 1.2) r.longues++;          // visiblement la plus longue (plus de 20 % d'écart)
  }
  return r;
}, toutes);
ok('chaque réponse attendue est une proposition, une seule fois, parmi quatre', etat.manquent.length === 0, etat.manquent.join(', '));
ok('aucune liste déroulante ne pose de question (seule la commande du simulateur reste une liste)', etat.listes.length === 0, etat.listes.join(', '));
ok('la bonne réponse change de place (aucune place n\'en porte plus de 35 %)', Object.values(etat.places).every((k) => k <= 0.35 * 35), JSON.stringify(etat.places));
ok('la bonne réponse n\'est jamais visiblement la plus longue (n°144)', etat.longues === 0, String(etat.longues));

const SEANCE = { 0: 'seance1', 1: 'seance1', 2: 'seance2', 3: 'seance2', 4: 'seance3', 5: 'seance4' };
const ouvrir = async (s) => { await p.click(`.seance-tab[data-panel="${s}"]`); await p.waitForTimeout(100); };
const cocher = (id, v) => p.evaluate(([id, v]) => { [...document.querySelectorAll(`#${id} input[type=radio]`)].find((x) => x.value === v).click(); }, [id, v]);
const fb = async (n) => (await p.locator('#fb' + n).textContent()).trim();
for (const n of ['0', '1', '2', '3', '4', '5']) {
  await ouvrir(SEANCE[n]);
  const ids = Object.keys(ATT[n]);
  for (const id of ids) await cocher(id, ATT[n][id]);
  const autre = await p.evaluate(([id, v]) => [...document.querySelectorAll(`#${id} input[type=radio]`)].map((x) => x.value).find((x) => x !== v), [ids[1], ATT[n][ids[1]]]);
  await cocher(ids[1], autre);
  if (n === '1') await p.fill('#e1c_prod', 'Je propose : PC-Prof = 192.168.20.10 ; Serveur = 192.168.20.100 ; le .1 reste à la passerelle.');
  if (n === '5') await p.evaluate(() => [...document.querySelectorAll('#e5_defi input[type=radio]')][2].click());   // le défi : « l'un OU l'autre »
  const total = ids.length + (n === '5' ? 1 : 0);                                                                     // la vérification 5 compte aussi le défi
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(60);
  const marques = await p.evaluate((ids) => ids.filter((id) => document.getElementById(id).classList.contains('ko')), ids);
  ok(`vérification ${n} : une erreur → ${total - 1} / ${total}, seule cette question est marquée « à revoir »`,
     (await fb(n)).startsWith(`${total - 1} / ${total}`) && marques.length === 1 && marques[0] === ids[1] && (await fb(n)).includes('à revoir'), await fb(n));
  await cocher(ids[1], ATT[n][ids[1]]); await p.click(`[data-check="${n}"]`); await p.waitForTimeout(60);
  const valide = await p.evaluate((n) => !!(window.__valid || {})[n], n);
  const juste = (await fb(n)).startsWith(`${total} / ${total}`) && !(await fb(n)).includes('à revoir');
  if (['0', '1', '2', '3'].includes(n)) ok(`vérification ${n} : tout juste → ${total} / ${total}, validée`, juste && valide, await fb(n));
  else ok(`vérification ${n} : tout juste → ${total} / ${total}, plus rien « à revoir » (la validation demande aussi la manipulation et l'écrit)`, juste, await fb(n));
}
/* billet de sortie (règle d'or n°330, 28/11/2026) : seul, sans aide, sur un réseau neuf */
{
  await ouvrir('seance4');
  const bs = await p.evaluate(() => {
    const s = document.getElementById('billetSortie'); if (!s) return null;
    const corr = s.querySelector('details.correction');
    const bonus = [...document.querySelectorAll('section.card h2')].find(h => /🎁 Bonus/.test(h.textContent));
    return { visible: s.checkVisibility(), zones: s.querySelectorAll('textarea[data-save]').length,
      etayages: s.querySelectorAll('details.etayage').length, boutons: s.querySelectorAll('button').length,
      criteres: (corr.textContent.match(/Critère/g) || []).length, contre: (corr.textContent.match(/✘/g) || []).length,
      avantBonus: !!bonus && s.nextElementSibling === bonus.closest('section'),
      panneau: (s.closest('.seance-panel') || {}).id };
  });
  ok('billet de sortie · il existe, visible à la séance 4, juste avant le Bonus', !!bs && bs.visible && bs.panneau === 'seance4' && bs.avantBonus, JSON.stringify(bs));
  ok('billet de sortie · deux zones gardées, deux versions étayées, deux critères, des contre-exemples, aucun bouton',
     !!bs && bs.zones === 2 && bs.etayages === 2 && bs.criteres === 2 && bs.contre >= 2 && bs.boutons === 0, JSON.stringify(bs));
  await p.fill('#bs_4e_C4_7_1', 'mauvaise rue : 192.168.3');
  await p.waitForTimeout(800);   // la page garde 600 ms après la dernière frappe
}
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
ok('billet de sortie · la réponse écrite survit au rechargement', (await p.inputValue('#bs_4e_C4_7_1')) === 'mauvaise rue : 192.168.3');
const rest = await p.evaluate((A) => Object.entries(A).every(([id, v]) => { const c = document.querySelector(`#${id} input[type=radio]:checked`); return c && c.value === v; }), toutes);
ok('après rechargement, les 35 réponses reviennent (sauvegarde de la page)', rest);
const pos = await p.evaluate(() => ['pos_c47', 'pos_c48', 'pos_c49'].every((id) => { const f = document.getElementById(id);
  return f && f.matches('fieldset.qcm-groupe.positionnement') && f.querySelectorAll('input[type=radio]').length === 4 && /4e_C4\.\d/.test(f.querySelector('legend').textContent); }));
ok('le positionnement : trois groupes de quatre boutons, chacun légendé par son code', pos);
ok('aucune erreur JS', err.length === 0, err.slice(0, 2).join(' | '));

/* les QCM d'adressage et de Zigbee : au moins six questions sur document (n°345, 28/11/2026) */
{
  const fs = await import('fs'), cp = await import('child_process');
  const LOT = path.dirname(new URL(import.meta.url).pathname);
  for (const f of ['qcm_4e_C4.7_adressage_ip.html', 'qcm_4e_C4.7_zigbee_domotique.html']) {
    const src = fs.readFileSync(path.join(LOT, f), 'utf8');
    const Q = eval(src.match(/const QUESTIONS\s*=\s*(\[[\s\S]*?\n\]);/)[1]);
    const avec = Q.filter((q) => q.img), docs = avec.filter((q) => /\/doc_/.test(q.img.src));
    ok(`${f} : au moins six questions sur document, chaque image présente`, avec.length >= 6 && avec.every((q) => fs.existsSync(path.join(LOT, q.img.src))), String(avec.length));
    ok(`${f} : chaque document « doc_ » est décrit en entier`, docs.length >= 3 && docs.every((q) => (q.img.alt || '').length > 120));
  }
  let aJour = true;
  try { cp.execSync('python3 documents_qcm.py --verifier', { cwd: LOT, stdio: 'pipe' }); } catch { aJour = false; }
  ok('documents_qcm_4e_C4.7.json est à jour du lot (plan d\'adressage, corrections du QCM Zigbee)', aJour);
}
const n0 = T.filter((x) => x.ok).length;
console.log(T.map((x) => `${x.ok ? '✅' : '❌'} ${x.n}${x.d ? ' — ' + x.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close(); process.exit(n0 === T.length ? 0 : 1);
