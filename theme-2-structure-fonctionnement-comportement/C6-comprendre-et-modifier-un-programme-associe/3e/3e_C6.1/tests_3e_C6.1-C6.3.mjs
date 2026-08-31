/* tests_3e_C6.1-C6.3.mjs — « Programmer l'alerte », rejouable.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de ce lot portait 17 coches et ne citait aucun script : une dette
 * honnête (règle d'or n°259). C'était le lot en tête de la file publiée par
 * `_outils/controle_rapports_tests.py`.
 *
 * CE QUE CETTE SUITE ÉPROUVE EN PROPRE
 * ------------------------------------
 * Ce lot ne vérifie pas des réponses à des menus déroulants : il **lit le
 * programme que l'élève a écrit**. Deux activités analysent le contenu réel de
 * l'éditeur CodeLab :
 *
 *   · l'activité 3 exige que `SEUIL_ORANGE` ait vraiment été recalibré dans le
 *     code — répondre juste aux deux questions ne suffit pas ;
 *   · l'activité 4 passe **sept** expressions régulières sur le programme :
 *     l'initialisation, les deux passages à True, le bloc final, son
 *     indentation, et l'absence de gyrophare dans la branche rouge. Elle nomme
 *     précisément ce qui manque.
 *
 * La suite éprouve les deux dans les deux sens : refus tant que le code n'est
 * pas modifié, message d'erreur qui nomme les ajouts manquants, puis validation.
 *
 * CE QU'ELLE NE RECOPIE PAS — Y COMPRIS LE PROGRAMME
 * --------------------------------------------------
 * Le programme v2 n'est pas écrit ici : il est **lu dans la correction que la
 * page publie elle-même** (`#act4 details.correction pre`), puis collé dans
 * l'éditeur. Si la correction et le vérificateur divergeaient un jour, cette
 * suite le dirait — ce qu'un programme recopié dans le test ne pourrait pas
 * faire (règle d'or n°268).
 *
 * Les réponses attendues sont extraites des `CHECKS` selon les cinq conventions
 * de ce lot : `att = {…}`, `$("id").value === "…"`, `.indexOf("…") === 0`
 * (préfixe), `num("id") === N`, et la prose jugée par mots-clés — dont la suite
 * ne prétend montrer que l'ouverture aux conditions déclarées.
 *
 * Usage, depuis ce dossier :
 *   node tests_3e_C6.1-C6.3.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence_3e_C6.1-C6.3_programmer_alerte.html');
const QCM = path.join(ICI, 'qcm_3e_C6.1-C6.3_programmer_alerte.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ CODELAB + SÉQUENCE (25 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => { if (!/fonts\.g/.test(r.url())) fail.push(r.url()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

await p.goto('file://' + SEQ, { waitUntil: 'load' });
await p.waitForTimeout(340);

const texte = (await p.textContent('body')).replace(/\s+/g, ' ');
ok('1 · chargement, titre « Programmer l\'alerte » et les codes 3e_C6.1 / 3e_C6.3',
   /Programmer l['’]alerte/i.test(await p.title())
   && texte.includes('3e_C6.1') && texte.includes('3e_C6.3'));

/* ── CodeLab Techno ──────────────────────────────────────────────────────── */
const v1 = await p.evaluate(() => PROGRAMME_V1);
const lignesV1 = v1.split('\n').length;
ok(`2 · programme d'origine chargé dans l'éditeur, ${lignesV1} lignes annoncées et comptées`,
   (await p.inputValue('#clTa')) === v1
   && (await p.textContent('#clLines')) === lignesV1 + ' lignes',
   await p.textContent('#clLines'));

const teintes = await p.$$eval('#clHl span', l => [...new Set(l.map(e => e.className))]
  .filter(Boolean));
ok(`3 · coloration syntaxique active : ${teintes.length} familles de jetons colorées`,
   ['k', 'n', 'f', 'c', 's'].filter(c => teintes.includes(c)).length >= 4, teintes.join(','));

/* Le surlignage est piloté par les consignes : on prend un bouton de la page. */
const hl = await p.$eval('[data-hl]', e => e.dataset.hl);
await p.click(`[data-hl="${hl}"]`); await p.waitForTimeout(120);
const [a1, a2] = hl.split('-').map(Number);
ok(`4 · le bouton « surligner les lignes ${hl} » surligne exactement ${a2 - a1 + 1} ligne(s)`,
   (await p.$$('#clHl .cl-line-hl')).length === a2 - a1 + 1
   && (await p.$$('#clGutter .cl-ln-hl')).length === a2 - a1 + 1,
   String((await p.$$('#clHl .cl-line-hl')).length));
await p.click('#clUnhl'); await p.waitForTimeout(80);
ok('4 bis · le bouton « ne plus surligner » rend le programme à sa lecture normale',
   (await p.$$('#clHl .cl-line-hl')).length === 0);

const tailleAvant = await p.evaluate(() => window.__clFs);
await p.click('#clFontPlus'); await p.waitForTimeout(80);
const tailleApres = await p.evaluate(() => window.__clFs);
ok(`5 · A+ agrandit la police de l'éditeur (${tailleAvant} → ${tailleApres} px, et le style suit)`,
   tailleApres === tailleAvant + 1
   && (await p.$eval('#codelab', e => e.style.getPropertyValue('--cl-fs')))
      === tailleApres + 'px');

ok('6 · à l\'ouverture, l\'éditeur déclare le programme identique à la version d\'origine',
   /identique à la version d'origine/.test(await p.textContent('#clDiffInfo')),
   await p.textContent('#clDiffInfo'));

/* ── les attendus, LUS dans la page ─────────────────────────────────────── */
const PLAN = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const src = CHECKS[n].toString();
    const champs = {};
    const objet = src.match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    if (objet) for (const [id, v] of Object.entries(eval('(' + objet[1] + ')')))
      champs[id] = { mode: 'exact', v };
    for (const m of src.matchAll(/\$\("([\w.]+)"\)\.value\s*===\s*(['"])((?:\\.|(?!\2).)*)\2/g))
      champs[m[1]] = { mode: 'exact', v: m[3] };
    for (const m of src.matchAll(
        /\$\("([\w.]+)"\)\.value\.indexOf\("((?:\\.|[^"])*)"\)\s*===\s*0/g))
      champs[m[1]] = { mode: 'prefixe', v: m[2] };
    for (const m of src.matchAll(/num\("([\w.]+)"\)\s*===?\s*(-?\d+(?:\.\d+)?)/g))
      champs[m[1]] = { mode: 'nombre', v: m[2] };
    const proses = [...new Set([...src.matchAll(/txt\("([\w.]+)"\)/g)].map(m => m[1]))];
    if (proses.length) {
      const mots = [...src.matchAll(/\.includes\("([^"]+)"\)/g)].map(m => m[1]);
      const longueur = Math.max(0, ...[...src.matchAll(/length\s*>=\s*(\d+)/g)]
        .map(m => Number(m[1])));
      for (const id of proses) champs[id] = { mode: 'prose', mots, longueur };
    }
    out[n] = champs;
  }
  return out;
});
const compte = m => Object.values(PLAN)
  .reduce((s, o) => s + Object.values(o).filter(c => c.mode === m).length, 0);
ok(`7 · attendus extraits des CHECKS : ${compte('exact')} égalités, ${compte('prefixe')} préfixes, `
   + `${compte('nombre')} nombres, ${compte('prose')} rédaction — rien n'est recopié ici`,
   Object.keys(PLAN).length === 6 && compte('exact') >= 14 && compte('prefixe') >= 4
   && compte('nombre') >= 3 && compte('prose') === 1,
   Object.keys(PLAN).join(','));

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
const rediger = c => {
  let t = 'Réponse rédigée pour le contrôle : ' + c.mots.join(', ') + '.';
  while (t.length < c.longueur + 5) t += ' On le vérifie ensuite point par point.';
  return t;
};
async function remplir(n, seulement = null) {
  for (const [id, c] of Object.entries(PLAN[n])) {
    if (seulement && !seulement.includes(id)) continue;
    if (!(await ouvrirPour(id))) continue;
    const el = await p.$('#' + id); if (!el) continue;
    const balise = await el.evaluate(e => e.tagName);
    if (c.mode === 'prose') { await p.fill('#' + id, rediger(c)); continue; }
    if (balise !== 'SELECT') { await p.fill('#' + id, String(c.v)); continue; }
    if (c.mode === 'prefixe') {
      const exact = await el.evaluate((e, deb) => [...e.options].map(o => o.value)
        .find(v => v && v.startsWith(deb)), c.v);
      if (exact) await p.selectOption('#' + id, exact);
    } else await p.selectOption('#' + id, String(c.v));
  }
}
const valider = async n => {
  await ouvrirPour(Object.keys(PLAN[n])[0] || 'clTa');
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(110);
};
const retour = n => p.textContent('#fb' + n);
const valide = n => p.evaluate(k => !!window.__valid[k], String(n));
const ecrireCode = async code => {
  await p.$eval('#clTa', (t, v) => {
    t.value = v; t.dispatchEvent(new Event('input', { bubbles: true }));
  }, code);
  await p.waitForTimeout(110);
};

await remplir(1); await valider(1);
ok('8 · activité 1 validée 8 / 8 (six classements entrée/sortie + deux numéros de ligne)',
   /8 \/ 8/.test(await retour(1)) && await valide(1), (await retour(1)).slice(0, 60));

const prose2 = Object.entries(PLAN[2]).find(([, c]) => c.mode === 'prose')[0];
await remplir(2, Object.keys(PLAN[2]).filter(i => i !== prose2));
await ouvrirPour(prose2); await p.fill('#' + prose2, 'Parce que.');
await valider(2);
ok('9 · activité 2 REFUSÉE : les 3 traces justes, mais la justification est trop courte',
   /3 \/ 3/.test(await retour(2)) && /justification/i.test(await retour(2))
   && !(await valide(2)), (await retour(2)).slice(0, 70));
await remplir(2); await valider(2);
ok('10 · activité 2 validée 3 / 3 (118 > 118 est faux : l\'opérateur est strict)',
   /3 \/ 3/.test(await retour(2)) && await valide(2), (await retour(2)).slice(0, 60));

/* ── LE VÉRIFICATEUR QUI LIT LE CODE ─────────────────────────────────────── */
const SEUIL = await p.evaluate(() =>
  Number((CHECKS[3].toString().match(/SEUIL_ORANGE\\s\*=\\s\*(\d+)/) || [])[1]));
await remplir(3); await valider(3);
ok(`11 · activité 3 REFUSÉE : les 2 réponses justes, mais SEUIL_ORANGE = ${SEUIL} n'est pas dans le code`,
   /2 \/ 3/.test(await retour(3)) && /Je ne trouve pas SEUIL_ORANGE/.test(await retour(3))
   && !(await valide(3)), (await retour(3)).slice(0, 75));

await ecrireCode(v1.replace(/SEUIL_ORANGE\s*=\s*\d+/, 'SEUIL_ORANGE = ' + SEUIL));
ok('12 · une seule ligne changée dans l\'éditeur : le comparateur en annonce exactement une',
   /^1 ligne\(s\) diffèrent/.test(await p.textContent('#clDiffInfo')),
   await p.textContent('#clDiffInfo'));

await valider(3);
ok(`13 · activité 3 validée 3 / 3 une fois la ligne 2 réellement recalibrée à ${SEUIL}`,
   /3 \/ 3/.test(await retour(3)) && !/Je ne trouve pas/.test(await retour(3))
   && await valide(3), (await retour(3)).slice(0, 60));

/* ── LES SEPT CONTRÔLES DE CODE DE L'ACTIVITÉ 4 ──────────────────────────── */
await valider(4);
const incomplet = await retour(4);
/* Le nombre de contrôles de code n'est pas compté ici : on demande son total à
   la fonction elle-même, qui ne fait que lire l'éditeur. */
const attendus = await p.evaluate(() => CHECKS[4]().total);
ok(`14 · activité 4 REFUSÉE sur le programme v1, et le message NOMME les ajouts manquants`,
   /Il manque :/.test(incomplet) && /gyrophare_actif = False/.test(incomplet)
   && !(await valide(4)), incomplet.slice(0, 90));

/* Le programme v2 n'est pas écrit ici : il est lu dans la correction que la
   page publie. Si la correction et le vérificateur divergeaient, on le saurait. */
const v2 = (await p.$eval('#act4 details.correction pre', e => e.textContent)).trim() + '\n';
ok(`15 · le programme v2 est lu dans la correction publiée par la page (${v2.split('\n').length} lignes)`,
   v2.length > v1.length * 0.8 && /gyrophare_actif/.test(v2),
   v2.split('\n').length + ' lignes');

await ecrireCode(v2);
await valider(4);
ok(`16 · activité 4 validée ${attendus} / ${attendus} : les sept contrôles de code passent sur le v2`,
   new RegExp(`${attendus} / ${attendus}`).test(await retour(4)) && !/Il manque/.test(await retour(4))
   && await valide(4), (await retour(4)).slice(0, 60));

await remplir(5); await valider(5);
ok('17 · activité 5 validée 7 / 7 (cinq jeux d\'essai aux frontières + le bug diagnostiqué)',
   /7 \/ 7/.test(await retour(5)) && await valide(5), (await retour(5)).slice(0, 60));

await remplir(6); await valider(6);
ok('18 · activité 6 validée 6 / 6 (transfert : lire un programme qu\'on n\'a pas écrit)',
   /6 \/ 6/.test(await retour(6)) && await valide(6), (await retour(6)).slice(0, 60));

const prog = (await p.textContent('#progTxt')).replace(/\s+/g, ' ').trim();
const [faites, total] = (prog.match(/(\d+)\s*\/\s*(\d+)/) || []).slice(1).map(Number);
ok(`19 · toutes les activités sont validées (${prog})`,
   total > 0 && faites === total, prog);
const coches = await p.$$eval('[id^="done-s"]', l => l.map(e => e.textContent.trim()));
ok(`19 bis · les ${coches.length} onglets de séance portent leur coche`,
   coches.length > 0 && coches.every(c => c === '✔'), coches.join('|'));

/* ── persistance : le CODE de l'élève doit revenir, pas la version d'origine ── */
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(360);
ok('20 · rechargement : le programme v2 de l\'élève est restauré, pas la version d\'origine',
   (await p.inputValue('#clTa')).includes('gyrophare_actif')
   && (await p.inputValue('#clTa')) !== v1,
   (await p.textContent('#clDiffInfo')).slice(0, 60));
ok('20 bis · rechargement : réponses et validations restaurées, taille de police comprise',
   (await p.textContent('#progTxt')).trim().length > 0
   && await p.evaluate(() => !!window.__valid[4])
   && await p.evaluate(() => window.__clFs) === tailleApres,
   await p.textContent('#progTxt'));

const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok(`21 · les ${liens.length} liens internes existent`, casses.length === 0,
   casses.slice(0, 3).join(' · '));

const svg = await p.$$eval('img[src$=".svg"], object[data$=".svg"]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('data')));
const svgAbsents = svg.filter(s => !fs.existsSync(path.join(ICI, s)));
ok(`22 · les ${svg.length} SVG référencés existent sur le disque`,
   svg.length === 3 && svgAbsents.length === 0, svgAbsents.join(' · '));

const distantes = await p.$$eval('[src], link[href], object[data], iframe[src]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('href') || e.getAttribute('data'))
        .filter(u => u && /^(https?:)?\/\//i.test(u)));
ok('23 · hors ligne : aucune ressource distante, aucune modale, aucune erreur JS',
   distantes.length === 0 && dlg.length === 0 && fail.length === 0 && err.length === 0,
   (distantes[0] || err[0] || fail[0] || dlg[0] || '').slice(0, 80));
await ctx.close();
}

/* ════════════════ QCM (9 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = []; p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });

await p.goto('file://' + QCM, { waitUntil: 'load' });
await p.waitForTimeout(300);

const Q = await p.evaluate(() => QUESTIONS.map(q => ({
  c: q.c, n: q.n, o: q.o, r: q.r, d: q.d, expl: q.expl, ex: q.ex, err: q.err, ret: q.ret,
  img: q.img ? q.img.src : null })));
const codes = await p.evaluate(() => Object.keys(COMP_LABELS));
const badge = (await p.$eval('.badge.theme', e => e.textContent)).trim();

ok('24 · chargement du QCM, titre « Programmer l\'alerte », taille annoncée exacte',
   /Programmer l['’]alerte/i.test(await p.title()) && badge.includes(String(Q.length))
   && (await p.textContent('#qTot')) === String(Q.length), badge);

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
ok(`25 · ${Q.length} questions, ${codes.length} compétences : `
   + codes.map(c => c + ' ' + (parCode[c] || 0)).join(' · '),
   Q.length === 30 && codes.length === 2 && codes.every(c => parCode[c] === 15),
   JSON.stringify(parCode));

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`26 · bonnes réponses A/B/C/D = ${rep.join('/')} (écart max 1) et d[r] vide partout`,
   Math.max(...rep) - Math.min(...rep) <= 1 && Q.every(q => q.d[q.r] === ''), rep.join('/'));

const illustrees = Q.filter(q => q.img);
const imgAbsentes = illustrees.filter(q => !fs.existsSync(path.join(ICI, q.img)));
ok(`27 · ${illustrees.length} questions illustrées, fichiers présents sur le disque`,
   illustrees.length === 6 && imgAbsentes.length === 0, imgAbsentes.map(q => q.n).join(' · '));

const incomplets = Q.filter(q => !(q.o.length === 4 && q.d.length === 4 && q.expl && q.ex
                                   && q.err && q.ret));
ok('28 · gabarit maison complet : 4 options, 4 réfutations, explication, exemple, erreur, à retenir',
   incomplets.length === 0, incomplets.map(q => q.n).slice(0, 3).join(' · '));

for (let i = 0; i < Q.length; i++) {
  const r = await p.evaluate(() => QUESTIONS[Number(document.getElementById('qNum')
    .textContent) - 1].r);
  const opts = await p.$$('#qOptions .option');
  await opts[r].click();
  await p.click('#btnValider'); await p.waitForTimeout(30);
  if (i < Q.length - 1) { await p.click('#btnSuiv'); await p.waitForTimeout(30); }
}
await p.click('#btnTerminer'); await p.waitForTimeout(220);
const note = (await p.textContent('#rNote')).trim();
const lignes = await p.$$eval('#tblBilan tbody tr',
  l => l.map(t => t.textContent.replace(/\s+/g, ' ').trim()));
ok(`29 · parcours complet ${Q.length} / ${Q.length} joué → note ${note}, bilan sur `
   + `${lignes.length} compétences`,
   /20,0/.test(note) && (await p.textContent('#rOk')) === String(Q.length)
   && lignes.length === 2 && lignes.every(l => /15 \/ 15/.test(l)),
   note + ' · ' + lignes.join(' | ').slice(0, 70));

const cles = await p.evaluate(() => Object.keys(window.localStorage));
ok('30 · la clé localStorage du QCM est écrite',
   cles.some(k => k.includes('qcm_3e_C6.1-C6.3_programmer')), cles.join(' · '));

const retourSeq = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href'))
  .filter(h => h && /sequence.*\.html$/.test(h)));
ok('31 · le lien de retour vers la séquence existe et pointe sur un fichier réel',
   retourSeq.length > 0
   && retourSeq.every(h => fs.existsSync(path.join(ICI, decodeURIComponent(h)))),
   retourSeq[0] || '');

ok('32 · aucune erreur JS sur le QCM', err.length === 0, err.slice(0, 2).join(' | '));
await ctx.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
