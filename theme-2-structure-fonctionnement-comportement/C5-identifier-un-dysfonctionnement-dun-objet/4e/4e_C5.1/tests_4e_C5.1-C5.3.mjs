/* tests_4e_C5.1-C5.3.mjs — les vingt-trois coches du lot « SOS jardin connecté », rejouées.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de ce lot annonce « Suite : `tests_lot10.js` — 23 tests, **tous
 * réellement exécutés** le 24/07/2026 ». Ce script **n'est pas dans le dépôt**,
 * et ne l'a jamais été. Six rapports du Thème 2 sont dans ce cas, chacun citant
 * un `tests_lotNN.js` introuvable : environ cent cinquante coches vertes
 * attribuées à des scripts que personne ne peut lancer (règle d'or n°259).
 *
 * Les vingt-trois lignes du tableau sont ici rejouées pour de vrai — le poste de
 * diagnostic est conduit test par test, le simulateur de remplacement geste par
 * geste, et le QCM ouvert et joué.
 *
 * CE QU'IL A TROUVÉ EN NAISSANT
 * -----------------------------
 * La ligne 19 du tableau affirmait « 3 questions illustrées ». La banque en
 * porte **quatre**. Personne ne pouvait s'en apercevoir : le nombre était écrit
 * à la main dans un tableau que rien ne relançait.
 *
 * Comme pour les autres suites de la maison, les bonnes réponses ne sont pas
 * recopiées ici : elles sont extraites des fonctions `CHECKS` de la page.
 *
 * Usage, depuis ce dossier :
 *   node tests_4e_C5.1-C5.3.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence_4e_C5.1-C5.3_depanner_jardin.html');
const QCM = path.join(ICI, 'qcm_4e_C5.1-C5.3_depanner_jardin.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ SÉQUENCE (15 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

await p.goto('file://' + SEQ, { waitUntil: 'load' });
await p.waitForTimeout(320);

const texte = (await p.textContent('body')).replace(/\s+/g, ' ');
ok('1 · chargement, titre « SOS jardin connecté » et sous-titre en tête',
   /SOS jardin connect/i.test(await p.title()) || /SOS jardin connect/i.test(texte));
ok('2 · les badges des trois codes 4e_C5.1 / C5.2 / C5.3 sont là',
   ['4e_C5.1', '4e_C5.2', '4e_C5.3'].every(c => texte.includes(c)));

await p.click('.seance-tab[data-panel="s2"]');
await p.waitForTimeout(120);
ok('3 · onglets de séance : la bascule vers S2 fonctionne',
   await p.$eval('#s2', e => e.classList.contains('active')));
await p.click('.seance-tab[data-panel="s1"]');
await p.waitForTimeout(120);

/* aucun verrou ouvert avant le premier geste (règle n°226) */
ok('3 bis · aucun verrou ouvert au chargement',
   Object.keys(await p.evaluate(() => window.__exp || {}))
     .filter(k => k !== 'mode_essentiel').length === 0,
   JSON.stringify(await p.evaluate(() => window.__exp)));

/* ── le poste de diagnostic, conduit pour de vrai ────────────────────────── */
const cliqueDiag = async e => { await p.click(`.diagbtn[data-etape="${e}"]`); await p.waitForTimeout(45); };
await cliqueDiag(3);                       // un test joué trop tôt
ok('4 · poste de diagnostic : un test hors ordre remet à zéro (0 / 6)',
   (await p.textContent('#diagEtat')).includes('0 / 6'), await p.textContent('#diagEtat'));
for (let e = 1; e <= 6; e++) await cliqueDiag(e);
ok('5 · les six tests dans l\'ordre → cause isolée et verrou __exp.diag',
   (await p.textContent('#diagEtat')).includes('6 / 6')
   && await p.evaluate(() => !!window.__exp.diag), await p.textContent('#diagEtat'));

/* ── les réponses attendues, LUES dans la page ───────────────────────────── */
const ATT = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const m = CHECKS[n].toString().match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    out[n] = m ? eval('(' + m[1] + ')') : {};
  }
  return out;
});
const PANNEAU = { 1: 's1', 2: 's2', 3: 's3', 4: 's3' };
async function remplir(n) {
  await p.click(`.seance-tab[data-panel="${PANNEAU[n]}"]`);
  await p.waitForTimeout(120);
  for (const [id, v] of Object.entries(ATT[n])) {
    const balise = await p.$eval('#' + id, e => e.tagName);
    if (balise === 'SELECT') await p.selectOption('#' + id, v);
    else await p.fill('#' + id, v);
  }
}
const valider = async n => { await p.click(`[data-check="${n}"]`); await p.waitForTimeout(90); };
const retour = n => p.textContent('#fb' + n);

await remplir(1); await valider(1);
ok('6 · activité 1 validée 8/8, verrou de diagnostic actif',
   /8 \/ 8/.test(await retour(1)) && !/Exécute VRAIMENT/.test(await retour(1)),
   (await retour(1)).slice(0, 70));

/* ── le simulateur de remplacement ───────────────────────────────────────── */
await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(120);
const cliqueRemp = async e => { await p.click(`.rempbtn[data-etape="${e}"]`); await p.waitForTimeout(45); };
await cliqueRemp(4);
ok('7 · remplacement : un geste joué trop tôt remet à zéro (0 / 6)',
   (await p.textContent('#rempEtat')).includes('0 / 6'), await p.textContent('#rempEtat'));
for (let e = 1; e <= 6; e++) await cliqueRemp(e);
ok('8 · les six gestes dans l\'ordre, sans protocole affiché → verrou __exp.remplace',
   (await p.textContent('#rempEtat')).includes('6 / 6')
   && await p.evaluate(() => !!window.__exp.remplace), await p.textContent('#rempEtat'));

await remplir(2); await valider(2);
ok('9 · activité 2 validée 8/8 (ordre construit + questions), verrou actif',
   /8 \/ 8/.test(await retour(2)) && !/Mène le remplacement/.test(await retour(2)),
   (await retour(2)).slice(0, 70));

await remplir(3); await valider(3);
await remplir(4); await valider(4);
ok('10 · activités 3 et 4 validées (7/7 et 4/4)',
   /7 \/ 7/.test(await retour(3)) && /4 \/ 4/.test(await retour(4)),
   (await retour(3)).slice(0, 30) + ' | ' + (await retour(4)).slice(0, 30));

ok('11 · barre de progression : 4 / 4 activités validées',
   (await p.textContent('#progTxt')).includes('4 / 4'), await p.textContent('#progTxt'));

/* ── persistance ─────────────────────────────────────────────────────────── */
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(320);
ok('12 · rechargement : réponses, validations ET verrous restaurés',
   (await p.inputValue('#o1_a')) === ATT[1].o1_a
   && (await p.textContent('#progTxt')).includes('4 / 4')
   && await p.evaluate(() => !!(window.__exp.diag && window.__exp.remplace)),
   await p.textContent('#progTxt'));

/* ── règle d'or n°4 : blocs élève, et un seul bouton vers le QCM ─────────── */
const boutonsQcm = await p.$$eval('a[href*="qcm"]', a => a.filter(x => /btn/.test(x.className)).length);
ok('13 · un seul bouton vers le QCM, et les blocs « Prêt·e » et « Bonus » présents',
   boutonsQcm === 1 && /Prêt/i.test(texte) && /Bonus|🎁/i.test(texte), String(boutonsQcm));

/* ── liens locaux et images ──────────────────────────────────────────────── */
const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok('14 · tous les liens internes pointent vers des fichiers existants',
   casses.length === 0, casses.slice(0, 3).join(' · '));

const svg = await p.$$eval('img[src$=".svg"], object[data$=".svg"]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('data')));
const svgAbsents = svg.filter(s => !fs.existsSync(path.join(ICI, s)));
ok(`15 · les ${svg.length} SVG référencés existent sur le disque`,
   svgAbsents.length === 0, svgAbsents.join(' · '));

ok('15 bis · aucune boîte modale, aucune erreur JS sur la séquence',
   dlg.length === 0 && err.length === 0, (err[0] || dlg[0] || '').slice(0, 80));
await ctx.close();
}

/* ════════════════ QCM (8 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = []; p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });

await p.goto('file://' + QCM, { waitUntil: 'load' });
await p.waitForTimeout(280);

const Q = await p.evaluate(() => QUESTIONS.map(q => ({
  c: q.c, n: q.n, o: q.o, r: q.r, d: q.d, expl: q.expl, ex: q.ex, err: q.err, ret: q.ret,
  img: q.img ? q.img.src : null })));
const badge = await p.$eval('.badge.theme', e => e.textContent);

ok('16 · chargement, titre « SOS jardin connecté », taille annoncée exacte',
   /SOS jardin/i.test(await p.title()) && badge.includes(String(Q.length)), badge.trim());

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
ok('17 · 30 questions exactement, 10 par code',
   Q.length === 30 && ['C5.1', 'C5.2', 'C5.3'].every(c => parCode[c] === 10),
   JSON.stringify(parCode));

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`18 · bonnes réponses A/B/C/D = ${rep.join('/')} (écart max 1) et d[r] vide partout`,
   Math.max(...rep) - Math.min(...rep) <= 1 && Q.every(q => q.d[q.r] === ''),
   rep.join('/'));

/* Le tableau écrit à la main annonçait « 3 questions illustrées ». On COMPTE. */
const illustrees = Q.filter(q => q.img);
const absentes = illustrees.filter(q => !fs.existsSync(path.join(ICI, q.img)));
ok(`19 · ${illustrees.length} questions illustrées, fichiers présents sur le disque`,
   illustrees.length > 0 && absentes.length === 0, absentes.map(q => q.img).join(' · '));

const incomplets = Q.filter(q => !(q.o.length === 4 && q.d.length === 4 && q.expl && q.ex
                                   && q.err && q.ret));
ok('20 · chaque question : 4 options, explication, exemple, erreur, « à retenir », 4 réfutations',
   incomplets.length === 0, incomplets.map(q => q.n).slice(0, 3).join(' · '));

/* une partie démarre et une réponse se joue réellement */
const options = await p.$$('#qOptions .option');
const r0 = await p.evaluate(() => QUESTIONS[Number(document.getElementById('qNum').textContent) - 1].r);
await options[r0].click();
await p.click('#btnValider');
await p.waitForTimeout(120);
ok('21 · une partie démarre et une réponse se joue vraiment (correction affichée)',
   (await p.$eval('#corrBloc', e => e.textContent.trim().length)) > 20);

const cles = await p.evaluate(() => Object.keys(window.localStorage));
ok('22 · la clé localStorage du QCM est écrite',
   cles.some(k => k.includes('qcm_4e_C5.1-C5.3_depanner_jardin')), cles.join(' · '));

const retourSeq = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href'))
  .filter(h => h && /sequence.*\.html$/.test(h)));
ok('23 · le lien de retour vers la séquence existe et pointe sur un fichier réel',
   retourSeq.length > 0 && retourSeq.every(h => fs.existsSync(path.join(ICI, decodeURIComponent(h)))),
   retourSeq.join(' · '));

ok('23 bis · aucune erreur JS sur le QCM', err.length === 0, err.slice(0, 2).join(' | '));
await ctx.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
