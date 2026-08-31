/* tests_4e_C6.1-C6.3.mjs — « Ajuster le programme du jardin », rejouable.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de ce lot citait `tests_lot11.js`, jamais commité. Il l'avoue
 * depuis le 31/08/2026 ; il lui manquait la suite. C'est le lot en tête de la
 * file publiée par `_outils/controle_rapports_tests.py` (règles n°259, n°266).
 *
 * Les vingt-trois lignes du tableau sont ici rejouées : le **banc de scénarios**
 * est conduit scénario par scénario — y compris dans le désordre, que la page
 * accepte volontairement —, les quatre activités et l'algorigramme sont remplis,
 * la page est rechargée, puis le QCM ouvert et joué.
 *
 * Les réponses ne sont pas recopiées ici : elles sont extraites des fonctions
 * `CHECKS` de la page, selon les **deux conventions** que ce lot emploie —
 * l'objet `att = {id: "valeur"}` et la liste de paires `[["id","valeur"], …]`.
 *
 * Usage, depuis ce dossier :
 *   node tests_4e_C6.1-C6.3.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence_4e_C6.1-C6.3_ajuster_programme_jardin.html');
const QCM = path.join(ICI, 'qcm_4e_C6.1-C6.3_ajuster_programme_jardin.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ SÉQUENCE (15 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => { if (!/fonts\.g/.test(r.url())) fail.push(r.url()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

await p.goto('file://' + SEQ, { waitUntil: 'load' });
await p.waitForTimeout(320);

const texte = (await p.textContent('body')).replace(/\s+/g, ' ');
ok('1 · chargement, titre « Ajuster le programme du jardin » et sous-titre en tête',
   /Ajuster le programme du jardin/i.test(await p.title())
   || /Ajuster le programme du jardin/i.test(texte));
ok('2 · les badges des deux codes 4e_C6.1 / 4e_C6.3 sont là',
   texte.includes('4e_C6.1') && texte.includes('4e_C6.3'));

await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(120);
ok('3 · onglets de séance : la bascule vers S2 fonctionne',
   await p.$eval('#s2', e => e.classList.contains('active')));
await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(120);

ok('3 bis · aucun verrou ouvert au chargement (règle n°226)',
   Object.keys(await p.evaluate(() => window.__exp || {}))
     .filter(k => k !== 'mode_essentiel').length === 0,
   JSON.stringify(await p.evaluate(() => window.__exp)));

/* ── les réponses attendues, LUES dans la page ───────────────────────────── */
const ATT = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const src = CHECKS[n].toString();
    const plan = {};
    const objet = src.match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    if (objet) Object.assign(plan, eval('(' + objet[1] + ')'));
    // seconde convention de ce lot : une liste de paires [["id","valeur"], …]
    const paires = src.match(/\[\s*(\[\s*"[\w.]+"\s*,\s*"[^"]*"\s*\]\s*,?\s*)+\]/);
    if (paires) for (const [id, v] of eval(paires[0])) plan[id] = v;
    out[n] = plan;
  }
  return out;
});
const champs = Object.values(ATT).reduce((s, o) => s + Object.keys(o).length, 0);
ok(`3 ter · ${champs} champs extraits de la page (aucune réponse recopiée ici)`,
   Object.keys(ATT).length === 5 && champs >= 25, String(champs));

/* On ne devine pas dans quel onglet vit un champ : on ouvre les onglets jusqu'à
   ce qu'il soit visible. Deviner la répartition, c'est se tromper le jour où
   elle change — et Playwright refuse d'écrire dans ce qui est masqué. */
const ONGLETS = await p.$$eval('.seance-tab', l => l.map(e => e.dataset.panel));
async function ouvrirPour(id) {
  if (await p.isVisible('#' + id).catch(() => false)) return true;
  for (const panneau of ONGLETS) {
    await p.click(`.seance-tab[data-panel="${panneau}"]`);
    await p.waitForTimeout(90);
    if (await p.isVisible('#' + id).catch(() => false)) return true;
  }
  return false;
}
async function remplir(n) {
  for (const [id, v] of Object.entries(ATT[n])) {
    if (!(await ouvrirPour(id))) continue;
    const el = await p.$('#' + id); if (!el) continue;
    if ((await el.evaluate(e => e.tagName)) === 'SELECT') await p.selectOption('#' + id, v);
    else await p.fill('#' + id, v);
  }
}
const valider = async n => {
  await ouvrirPour(Object.keys(ATT[n])[0]);
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(90);
};
const retour = n => p.textContent('#fb' + n);

await remplir(1); await valider(1);
ok('4 · activité 1 validée 5/5 (anomalies et causes logicielles)',
   /5 \/ 5/.test(await retour(1)), (await retour(1)).slice(0, 65));
await remplir(2); await valider(2);
ok('5 · activité 2 validée 5/5 (algorithme corrigé : hystérésis + plage horaire)',
   /5 \/ 5/.test(await retour(2)), (await retour(2)).slice(0, 65));

/* ── le verrou du banc de scénarios ──────────────────────────────────────── */
await remplir(3); await valider(3);
ok('6 · activité 3 REFUSÉE tant que les scénarios ne sont pas joués (verrou actif)',
   /Joue VRAIMENT les 4 scénarios/.test(await retour(3)), (await retour(3)).slice(0, 90));

/* ── le banc, joué DANS LE DÉSORDRE : la page l'accepte volontairement ───── */
const clique = async n => { await p.click(`.scenbtn[data-scen="${n}"]`); await p.waitForTimeout(45); };
await clique(2);
ok('7 · banc de test : l\'ordre est LIBRE — le scénario 2 joué en premier compte 1 / 4',
   (await p.textContent('#scenEtat')).includes('1 / 4'), await p.textContent('#scenEtat'));
for (const n of [4, 1, 3]) await clique(n);
ok('8 · les quatre scénarios joués → programme validé en simulation et verrou __exp.scen',
   (await p.textContent('#scenEtat')).includes('4 / 4')
   && await p.evaluate(() => !!window.__exp.scen), await p.textContent('#scenEtat'));

await valider(3);
ok('9 · activité 3 validée 6/6 (verdicts, sauvegarde, non-régression) une fois le banc joué',
   /6 \/ 6/.test(await retour(3)) && !/Joue VRAIMENT/.test(await retour(3)),
   (await retour(3)).slice(0, 65));

await remplir(4); await valider(4);
ok('10 · activité 4 validée 4/4 (transfert au lampadaire)',
   /4 \/ 4/.test(await retour(4)), (await retour(4)).slice(0, 65));

await remplir(5); await valider(5);
ok('10 bis · l\'algorigramme se remet dans l\'ordre (6/6)',
   /6 \/ 6/.test(await retour(5)), (await retour(5)).slice(0, 65));

ok('11 · barre de progression : 4 / 4 activités validées',
   (await p.textContent('#progTxt')).includes('4 / 4'), await p.textContent('#progTxt'));
const coches = await p.$$eval('[id^="done-s"]', l => l.map(e => e.textContent.trim()));
ok('11 bis · les deux onglets de séance portent leur coche',
   coches.length > 0 && coches.every(c => c === '✔'), coches.join('|'));

/* ── persistance ─────────────────────────────────────────────────────────── */
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(320);
const premier = Object.keys(ATT[1])[0];
ok('12 · rechargement : réponses, validations ET verrou du banc restaurés',
   (await p.inputValue('#' + premier)) === ATT[1][premier]
   && (await p.textContent('#progTxt')).includes('4 / 4')
   && await p.evaluate(() => !!window.__exp.scen),
   await p.textContent('#progTxt'));

const boutonsQcm = await p.$$eval('a[href*="qcm"]', a => a.filter(x => /btn/.test(x.className)).length);
ok('13 · blocs « Prêt·e » et « Bonus », un seul bouton vers le QCM',
   boutonsQcm === 1 && /Prêt/i.test(texte) && /Bonus|🎁/i.test(texte), String(boutonsQcm));

const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok(`14 · les ${liens.length} liens internes (dont LOT 10, 4e_C6.2 et 4e_C4.1) existent`,
   casses.length === 0, casses.slice(0, 3).join(' · '));

const svg = await p.$$eval('img[src$=".svg"], object[data$=".svg"]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('data')));
const svgAbsents = svg.filter(s => !fs.existsSync(path.join(ICI, s)));
ok(`15 · les ${svg.length} SVG référencés existent sur le disque`,
   svgAbsents.length === 0, svgAbsents.join(' · '));

ok('15 bis · aucune boîte modale, aucune requête échouée, aucune erreur JS',
   dlg.length === 0 && fail.length === 0 && err.length === 0,
   (err[0] || fail[0] || dlg[0] || '').slice(0, 80));
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

ok('16 · chargement, titre « Ajuster le programme du jardin », taille annoncée exacte',
   /Ajuster le programme/i.test(await p.title()) && badge.includes(String(Q.length)),
   badge.trim());

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
ok('17 · 30 questions exactement, 15 par code',
   Q.length === 30 && parCode['C6.1'] === 15 && parCode['C6.3'] === 15,
   JSON.stringify(parCode));

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`18 · bonnes réponses A/B/C/D = ${rep.join('/')} (écart max 1) et d[r] vide partout`,
   Math.max(...rep) - Math.min(...rep) <= 1 && Q.every(q => q.d[q.r] === ''), rep.join('/'));

const illustrees = Q.filter(q => q.img);
const imgAbsentes = illustrees.filter(q => !fs.existsSync(path.join(ICI, q.img)));
ok(`19 · ${illustrees.length} questions illustrées, fichiers présents sur le disque`,
   illustrees.length > 0 && imgAbsentes.length === 0, imgAbsentes.map(q => q.img).join(' · '));

const incomplets = Q.filter(q => !(q.o.length === 4 && q.d.length === 4 && q.expl && q.ex
                                   && q.err && q.ret));
ok('20 · chaque question : 4 options, explication, exemple, erreur, « à retenir », 4 réfutations',
   incomplets.length === 0, incomplets.map(q => q.n).slice(0, 3).join(' · '));

const options = await p.$$('#qOptions .option');
const r0 = await p.evaluate(() => QUESTIONS[Number(document.getElementById('qNum').textContent) - 1].r);
await options[r0].click();
await p.click('#btnValider');
await p.waitForTimeout(120);
ok('21 · une partie démarre et une réponse se joue vraiment (correction affichée)',
   (await p.$eval('#corrBloc', e => e.textContent.trim().length)) > 20);

const cles = await p.evaluate(() => Object.keys(window.localStorage));
ok('22 · la clé localStorage du QCM est écrite',
   cles.some(k => k.includes('qcm_4e_C6.1-C6.3_ajuster_programme_jardin')), cles.join(' · '));

const retourSeq = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href'))
  .filter(h => h && /sequence.*\.html$/.test(h)));
ok('23 · le lien de retour vers la séquence existe et pointe sur un fichier réel',
   retourSeq.length > 0 && retourSeq.every(h => fs.existsSync(path.join(ICI, decodeURIComponent(h)))),
   retourSeq[0] || '');

ok('23 bis · aucune erreur JS sur le QCM', err.length === 0, err.slice(0, 2).join(' | '));
await ctx.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
