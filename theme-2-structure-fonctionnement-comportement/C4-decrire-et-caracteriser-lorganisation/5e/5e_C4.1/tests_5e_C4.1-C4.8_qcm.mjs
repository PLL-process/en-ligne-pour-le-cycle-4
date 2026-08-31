/* tests_5e_C4.1-C4.8_qcm.mjs — la suite qui rejoue ce que le rapport affirme.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport du lot annonce « QCM (5 tests) », cinq coches vertes, et cite un
 * script `tests_lot05.js` qui **n'a jamais été commité**. Vingt-six affirmations
 * dont aucune n'était rejouable : un tableau de résultats qu'on ne peut pas
 * relancer ne dit pas « ça marche », il dit « ça marchait le jour où quelqu'un a
 * regardé » (règle d'or n°259).
 *
 * Le 31/08/2026, la banque est passée de 32 à 36 questions. Sans ce fichier, les
 * cinq coches auraient survécu au changement sans que rien ne les revérifie.
 *
 * Il conduit le QCM POUR DE VRAI : il ouvre la page, parcourt les 36 questions,
 * clique la bonne option, valide, et lit la note affichée à la fin.
 *
 * Il ajoute ce que le tableau écrit à la main ne faisait pas :
 *   · les effectifs sont LUS dans le manifeste du lot, pas recopiés ici ;
 *   · la règle de la maison sur le gabarit (d[r] vide, noms uniques, quatre
 *     propositions) est vérifiée question par question ;
 *   · la règle de longueur des options est mesurée sur les quatre nouvelles ;
 *   · aucune boîte modale, aucun verrou ouvert au chargement.
 *
 * Usage, depuis ce dossier :
 *   node tests_5e_C4.1-C4.8_qcm.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const PAGE = path.join(ICI, 'qcm_5e_C4.1-C4.8_lampadaire_intelligent.html');

/* Les effectifs attendus sont LUS dans le manifeste : un test qui recopie le
   nombre qu'il doit vérifier ne vérifie plus rien. */
const MANIFESTE = JSON.parse(fs.readFileSync(path.join(ICI, 'manifest_lot_05.json'), 'utf-8'));
const ATTENDU_TOTAL = MANIFESTE.contenu.questions_qcm;
const ATTENDU_PAR_CODE = MANIFESTE.contenu.questions_par_code;

const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 390, height: 844 } });
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => { if (!/fonts\.g/.test(r.url())) fail.push(r.url()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });

await p.goto('file://' + PAGE, { waitUntil: 'load' });
await p.waitForTimeout(300);

ok('1 · charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('2 · aucune requête locale échouée', fail.length === 0, fail.slice(0, 2).join(' | '));

/* ── la banque, lue dans la page elle-même ───────────────────────────────── */
const Q = await p.evaluate(() => QUESTIONS.map(q => ({
  c: q.c, n: q.n, o: q.o, r: q.r, d: q.d, ret: q.ret, img: !!q.img })));

ok(`3 · la banque porte ${ATTENDU_TOTAL} questions (nombre lu dans le manifeste)`,
   Q.length === ATTENDU_TOTAL, String(Q.length));

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
const ecartsCodes = Object.entries(ATTENDU_PAR_CODE)
  .filter(([code, n]) => parCode[code.split('_')[1]] !== n)
  .map(([code, n]) => `${code}: manifeste ${n}, banque ${parCode[code.split('_')[1]] || 0}`);
ok('4 · chaque code porte le nombre de questions que le manifeste annonce',
   ecartsCodes.length === 0, ecartsCodes.join(' · '));

/* Un code sous le seuil DANS CETTE BANQUE n'est pas une faute : il peut être
   renforcé par une autre. Ce qui est une faute, c'est de ne pas dire LAQUELLE
   (règle d'or n°250). Le manifeste doit donc la nommer, et le fichier exister. */
const SEUIL = MANIFESTE.contenu.seuil_evaluabilite;
const RENFORTS = MANIFESTE.contenu.codes_renforces_ailleurs || {};
const orphelins = Object.entries(parCode)
  .filter(([c, n]) => n < SEUIL && !RENFORTS['5e_' + c])
  .map(([c, n]) => `${c}=${n}`);
ok(`5 · tout code sous le seuil (${SEUIL} q) dans cette banque est renforcé ailleurs, et le manifeste dit où`,
   orphelins.length === 0, orphelins.join(' · '));

const renfortsAbsents = Object.entries(RENFORTS)
  .filter(([, v]) => !fs.existsSync(path.join(ICI, v.banque)))
  .map(([c]) => c);
ok('6 · chaque banque de renfort nommée par le manifeste existe',
   renfortsAbsents.length === 0, renfortsAbsents.join(' · '));

/* ── le gabarit maison, question par question ────────────────────────────── */
ok('7 · quatre propositions à chaque question',
   Q.every(q => q.o.length === 4), Q.filter(q => q.o.length !== 4).map(q => q.n).join(' · '));
ok('8 · la réfutation de la bonne réponse est vide (d[r] === "")',
   Q.every(q => q.d[q.r] === ''), Q.filter(q => q.d[q.r] !== '').map(q => q.n).join(' · '));
ok('9 · quatre réfutations parallèles à chaque question',
   Q.every(q => q.d.length === 4), Q.filter(q => q.d.length !== 4).map(q => q.n).join(' · '));
const noms = Q.map(q => q.n);
ok('10 · chaque notion porte un nom unique',
   new Set(noms).size === noms.length,
   noms.filter((n, i) => noms.indexOf(n) !== i).join(' · '));
ok('11 · chaque question porte un « à retenir »', Q.every(q => q.ret && q.ret.length > 10));

/* ── la répartition des bonnes réponses ──────────────────────────────────── */
const rep = [0, 0, 0, 0];
Q.forEach(q => rep[q.r]++);
ok(`12 · bonnes réponses réparties A/B/C/D = ${rep.join('/')} (écart max 1)`,
   Math.max(...rep) - Math.min(...rep) <= 1, rep.join('/'));

/* ── la règle de longueur : la bonne réponse ne se détache pas ───────────── */
const detachees = Q.filter(q => {
  const l = q.o.map(x => x.length);
  const bonne = l[q.r];
  const autres = l.filter((_, k) => k !== q.r);
  return bonne > Math.max(...autres) + 8 || bonne < Math.min(...autres) - 8;
}).map(q => q.n);
ok('13 · aucune bonne réponse détachée de plus de 8 caractères',
   detachees.length === 0, detachees.join(' · '));

/* ── les images annoncées existent sur le disque ─────────────────────────── */
const images = await p.evaluate(() => QUESTIONS.filter(q => q.img).map(q => q.img.src));
const absentes = images.filter(src => !fs.existsSync(path.join(ICI, src)));
ok(`14 · les ${images.length} questions illustrées ont leur fichier sur le disque`,
   absentes.length === 0, absentes.join(' · '));
ok('15 · le nombre de questions illustrées est celui du manifeste',
   images.length === MANIFESTE.contenu.questions_illustrees,
   `${images.length} vs ${MANIFESTE.contenu.questions_illustrees}`);

/* ── ce que la page affiche sur elle-même ────────────────────────────────── */
for (const [quoi, sel] of [['total pendant le parcours', '#qTot'],
                           ['compteur « Restantes »', '#dRest'],
                           ['total du bilan', '#rTot']]) {
  const v = Number((await p.textContent(sel)).trim());
  ok(`16 · ${quoi} annonce ${ATTENDU_TOTAL}`, v === ATTENDU_TOTAL, String(v));
}
const badge = await p.$eval('.badge.theme', e => e.textContent);
ok(`17 · le badge de l'en-tête annonce ${ATTENDU_TOTAL} questions`,
   badge.includes(String(ATTENDU_TOTAL)), badge.trim());

/* ── aucun verrou expérientiel ouvert à l'ouverture (règle n°226) ────────── */
ok('18 · aucun verrou ouvert au chargement',
   await p.evaluate(() => Object.values(window.__exp || {}).every(v => !v)));

/* ── le parcours complet, joué pour de vrai ──────────────────────────────── */
const lettres = ['A', 'B', 'C', 'D'];
for (let i = 0; i < Q.length; i++) {
  const options = await p.$$('#qOptions .option');
  if (options.length !== 4) { ok(`parcours · question ${i + 1} : 4 options`, false); break; }
  const rIndex = await p.evaluate(() => {
    const n = Number(document.getElementById('qNum').textContent);
    return QUESTIONS[n - 1].r;
  });
  await options[rIndex].click();
  await p.click('#btnValider');
  await p.waitForTimeout(20);
  if (i < Q.length - 1) { await p.click('#btnSuiv'); await p.waitForTimeout(20); }
}
await p.click('#btnTerminer');
await p.waitForTimeout(250);

const note = (await p.textContent('#rNote')).replace(/\s/g, '');
const justes = Number(await p.textContent('#rOk'));
ok(`19 · parcours complet : ${ATTENDU_TOTAL}/${ATTENDU_TOTAL} bonnes réponses`,
   justes === ATTENDU_TOTAL, String(justes));
ok('20 · la note affichée est 20/20', /20[.,]0?\/20/.test(note), note);

const bilan = await p.$$eval('#tblBilan tr', l => l.length);
ok('21 · le bilan détaille les 8 codes', bilan >= 8, String(bilan));

ok('22 · aucune boîte modale sur tout le parcours', dlg.length === 0, dlg.join(' | '));
ok('23 · aucune erreur JS après le scénario complet', err.length === 0,
   err.slice(0, 2).join(' | '));

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
