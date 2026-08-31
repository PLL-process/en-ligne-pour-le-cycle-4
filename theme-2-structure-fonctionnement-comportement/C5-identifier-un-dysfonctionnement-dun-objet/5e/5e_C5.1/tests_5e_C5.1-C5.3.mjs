/* tests_5e_C5.1-C5.3.mjs — les vingt-deux coches du lot « Dépanner le lampadaire », rejouées.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de ce lot citait `tests_lot08.js`, jamais commité. Il l'avoue
 * depuis le 31/08/2026 ; il lui manquait encore la suite. C'est la deuxième de
 * la file d'attente que `_outils/controle_rapports_tests.py` publie à chaque
 * exécution (règle d'or n°259, et n°266 pour la distinction entre une dette
 * qu'on compte et une promesse fausse qu'on refuse).
 *
 * Les vingt-deux lignes du tableau sont ici rejouées : l'inspecteur visuel est
 * cliqué zone par zone, le simulateur de réparation conduit étape par étape —
 * y compris une étape jouée trop tôt, qui doit tout remettre à zéro —, les
 * quatre activités remplies, la page rechargée, puis le QCM ouvert et joué.
 *
 * Les bonnes réponses ne sont pas recopiées ici : elles sont extraites des
 * fonctions `CHECKS` de la page. Un test qui recopie ce qu'il doit vérifier
 * cesse de le vérifier.
 *
 * Usage, depuis ce dossier :
 *   node tests_5e_C5.1-C5.3.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence_5e_C5.1-C5.3_depanner_lampadaire.html');
const QCM = path.join(ICI, 'qcm_5e_C5.1-C5.3_depanner_lampadaire.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ SÉQUENCE (14 contrôles) ════════════════ */
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
ok('1 · chargement, titre « Dépanner » et sous-titre en tête',
   /Dépanner/i.test(await p.title()) || /Dépanner/i.test(texte));
ok('2 · les badges des trois codes 5e_C5.1 / C5.2 / C5.3 sont là',
   ['5e_C5.1', '5e_C5.2', '5e_C5.3'].every(c => texte.includes(c)));

await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(120);
ok('3 · onglets de séance : la bascule vers S2 fonctionne',
   await p.$eval('#s2', e => e.classList.contains('active')));
await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(120);

ok('3 bis · aucun verrou ouvert au chargement (règle n°226)',
   Object.keys(await p.evaluate(() => window.__exp || {}))
     .filter(k => k !== 'mode_essentiel').length === 0,
   JSON.stringify(await p.evaluate(() => window.__exp)));

/* ── l'inspecteur visuel, cliqué zone par zone ───────────────────────────── */
const zones = await p.$$eval('.zonebtn', l => l.map(e => e.dataset.zone));
for (const z of zones) { await p.click(`.zonebtn[data-zone="${z}"]`); await p.waitForTimeout(35); }
ok(`4 · inspecteur visuel : les ${zones.length} zones examinées → compteur plein et verrou __exp.inspection`,
   (await p.textContent('#inspCompteur')).includes(`${zones.length} / 6`)
   && await p.evaluate(() => !!window.__exp.inspection),
   await p.textContent('#inspCompteur'));

/* ── les réponses attendues, LUES dans la page ───────────────────────────── */
const ATT = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const m = CHECKS[n].toString().match(/att(?:endu)?\s*=\s*(\{[\s\S]*?\})\s*;/);
    out[n] = m ? eval('(' + m[1] + ')') : {};
  }
  return out;
});
ok('4 bis · les bonnes réponses sont extraites de la page, pas recopiées ici',
   Object.keys(ATT).length === 4
   && Object.values(ATT).every(o => Object.keys(o).length > 0),
   Object.entries(ATT).map(([k, v]) => `${k}:${Object.keys(v).length}`).join(' · '));

const PANNEAU = { 1: 's1', 2: 's2', 3: 's3', 4: 's3' };
async function remplir(n) {
  await p.click(`.seance-tab[data-panel="${PANNEAU[n]}"]`); await p.waitForTimeout(120);
  for (const [id, v] of Object.entries(ATT[n])) {
    const balise = await p.$eval('#' + id, e => e.tagName);
    if (balise === 'SELECT') await p.selectOption('#' + id, v);
    else await p.fill('#' + id, v);
  }
}
const valider = async n => { await p.click(`[data-check="${n}"]`); await p.waitForTimeout(90); };
const retour = n => p.textContent('#fb' + n);

await remplir(1); await valider(1);
ok('5 · activité 1 validée 8/8, verrou d\'inspection actif',
   /8 \/ 8/.test(await retour(1)), (await retour(1)).slice(0, 70));

/* ── le simulateur de réparation ─────────────────────────────────────────── */
await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(120);
const clique = async e => { await p.click(`.repbtn[data-etape="${e}"]`); await p.waitForTimeout(45); };
await clique(4);
ok('6 · réparation : une étape jouée trop tôt remet à zéro (0 / 6)',
   (await p.textContent('#repEtat')).includes('0 / 6'), await p.textContent('#repEtat'));
for (let e = 1; e <= 6; e++) await clique(e);
ok('7 · les six étapes dans l\'ordre → « 6 / 6 RÉPARÉ » et verrou __exp.repare',
   (await p.textContent('#repEtat')).includes('6 / 6')
   && await p.evaluate(() => !!window.__exp.repare), await p.textContent('#repEtat'));

await remplir(2); await valider(2);
ok('8 · activité 2 validée 8/8 (ordre du protocole + questions), verrou actif',
   /8 \/ 8/.test(await retour(2)), (await retour(2)).slice(0, 70));

await remplir(3); await valider(3);
await remplir(4); await valider(4);
ok('9 · activités 3 et 4 validées (7/7 et 4/4)',
   /7 \/ 7/.test(await retour(3)) && /4 \/ 4/.test(await retour(4)),
   (await retour(3)).slice(0, 28) + ' | ' + (await retour(4)).slice(0, 28));

ok('10 · barre de progression : 4 / 4 activités validées',
   (await p.textContent('#progTxt')).includes('4 / 4'), await p.textContent('#progTxt'));

await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(320);
const premierId = Object.keys(ATT[1])[0];
ok('11 · rechargement : réponses, validations ET verrous restaurés',
   (await p.inputValue('#' + premierId)) === ATT[1][premierId]
   && (await p.textContent('#progTxt')).includes('4 / 4')
   && await p.evaluate(() => !!(window.__exp.inspection && window.__exp.repare)),
   await p.textContent('#progTxt'));

const boutonsQcm = await p.$$eval('a[href*="qcm"]', a => a.filter(x => /btn/.test(x.className)).length);
ok('12 · blocs « Prêt·e à t\'entraîner ? » et « Bonus », un seul bouton vers le QCM',
   boutonsQcm === 1 && /Prêt/i.test(texte) && /Bonus|🎁/i.test(texte), String(boutonsQcm));

const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok('13 · tous les liens internes pointent vers des fichiers existants',
   casses.length === 0, casses.slice(0, 3).join(' · '));

const svg = await p.$$eval('img[src$=".svg"], object[data$=".svg"]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('data')));
const absents = svg.filter(s => !fs.existsSync(path.join(ICI, s)));
ok(`14 · les ${svg.length} SVG référencés existent sur le disque`,
   absents.length === 0, absents.join(' · '));

ok('14 bis · aucune boîte modale, aucune erreur JS sur la séquence',
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

ok('15 · chargement, titre « Dépanner », taille annoncée exacte',
   /Dépanner/i.test(await p.title()) && badge.includes(String(Q.length)), badge.trim());

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
ok('16 · 30 questions exactement, 10 par code',
   Q.length === 30 && ['C5.1', 'C5.2', 'C5.3'].every(c => parCode[c] === 10),
   JSON.stringify(parCode));

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`17 · bonnes réponses A/B/C/D = ${rep.join('/')} (écart max 1) et d[r] vide partout`,
   Math.max(...rep) - Math.min(...rep) <= 1 && Q.every(q => q.d[q.r] === ''), rep.join('/'));

const illustrees = Q.filter(q => q.img);
const imgAbsentes = illustrees.filter(q => !fs.existsSync(path.join(ICI, q.img)));
ok(`18 · ${illustrees.length} questions illustrées, fichiers présents sur le disque`,
   illustrees.length > 0 && imgAbsentes.length === 0, imgAbsentes.map(q => q.img).join(' · '));

const incomplets = Q.filter(q => !(q.o.length === 4 && q.d.length === 4 && q.expl && q.ret));
ok('19 · chaque question : 4 options, explication, « à retenir », 4 réfutations parallèles',
   incomplets.length === 0, incomplets.map(q => q.n).slice(0, 3).join(' · '));

const options = await p.$$('#qOptions .option');
const r0 = await p.evaluate(() => QUESTIONS[Number(document.getElementById('qNum').textContent) - 1].r);
await options[r0].click();
await p.click('#btnValider');
await p.waitForTimeout(120);
ok('20 · une partie démarre et une réponse se joue vraiment (correction affichée)',
   (await p.$eval('#corrBloc', e => e.textContent.trim().length)) > 20);

const cles = await p.evaluate(() => Object.keys(window.localStorage));
ok('21 · la clé localStorage du QCM est écrite',
   cles.some(k => k.includes('qcm_5e_C5.1-C5.3_depanner_lampadaire')), cles.join(' · '));

const retourSeq = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href'))
  .filter(h => h && /sequence.*\.html$/.test(h)));
ok('22 · le lien de retour vers la séquence existe et pointe sur un fichier réel',
   retourSeq.length > 0 && retourSeq.every(h => fs.existsSync(path.join(ICI, decodeURIComponent(h)))),
   retourSeq[0] || '');

ok('22 bis · aucune erreur JS sur le QCM', err.length === 0, err.slice(0, 2).join(' | '));
await ctx.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
