/* tests_4e_C6.2.mjs — « Le jardin connecté : arrosage automatique », rejouable.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Dernier lot de la file publiée par `_outils/controle_rapports_tests.py`. Son
 * rapport de QCM portait 16 coches et citait `tests.mjs` — jamais commité ; le
 * rapport de la séquence annonçait « 27/27 » sans coche ni script. Deux dettes,
 * payées ici ensemble (règles d'or n°259 et n°266).
 *
 * CE QUE CETTE SUITE ÉPROUVE EN PROPRE : LA COUPURE RÉSEAU
 * --------------------------------------------------------
 * Cette séquence est la seule du thème 2 qui charge des ressources distantes :
 * **trois éditeurs Vittascience en `<iframe>`**. Et deux de ses huit activités
 * ont un verrou qui exige d'ouvrir un de ces éditeurs.
 *
 * La question n'est donc pas « la page cite-t-elle un domaine distant » — elle
 * le fait, et l'assume — mais **« que reste-t-il quand le collège n'a pas de
 * réseau ? »**. La suite y répond en fermant vraiment le robinet : toute requête
 * `http(s)` est **abandonnée** avant de partir, pour toute la session. Les huit
 * activités sont ensuite jouées dans cet état.
 *
 * Résultat mesuré, et c'est le cœur de ce fichier : les verrous `vs1` et `vs2`
 * s'ouvrent sur le **geste** d'ouvrir le dépliant, pas sur le chargement de
 * l'iframe. Hors réseau, l'élève perd l'éditeur — il ne perd ni la séquence, ni
 * la possibilité de valider. La version 🅲 « sans matériel » que la page annonce
 * est donc tenue, et on le sait maintenant par mesure.
 *
 * CE QU'ELLE NE RECOPIE PAS, ET COMMENT ELLE S'Y PREND ICI
 * --------------------------------------------------------
 * Les six lots précédents laissaient lire leurs `CHECKS` depuis la console :
 * leur script est classique, ses `const` sont des variables globales. **Celui-ci
 * enferme tout dans une fonction anonyme** — `(function(){ "use strict"; … })()`
 * — et rien n'en sort. Un pilote qui compte sur les globales échoue net.
 *
 * La suite lit donc le **fichier source**, qui est la page elle-même, et y
 * extrait les attendus. C'est plus robuste que d'interroger la fenêtre : cela
 * marche que le script soit enfermé ou non. La convention de ce lot est une
 * sixième : l'appel d'aide `sv("id", "valeur")`. Le banc de tests — T1, T2, T3
 * et leurs attendus — est lu dans la table `BENCH` du même source.
 *
 * Usage, depuis ce dossier :
 *   node tests_4e_C6.2.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence-jardin-connecte-arrosage-automatique.html');
const QCM = path.join(ICI, 'qcm_4e_C6.2_arrosage_automatique.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ SÉQUENCE, RÉSEAU COUPÉ (22 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
/* Le robinet est fermé pour toute la session : rien ne part vers le réseau. */
const bloquees = [];
await ctx.route('**/*', route => {
  const u = route.request().url();
  if (/^https?:/i.test(u)) { bloquees.push(u); return route.abort(); }
  return route.continue();
});
const p = await ctx.newPage();
const err = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

await p.goto('file://' + SEQ, { waitUntil: 'load' });
await p.waitForTimeout(360);

const texte = (await p.textContent('body')).replace(/\s+/g, ' ');
ok('1 · chargement RÉSEAU COUPÉ : la page s\'affiche, titre et code 4e_C6.2 présents',
   /jardin connecté/i.test(await p.title()) && texte.includes('4e_C6.2'));

const onglets = await p.$$eval('.seance-tab', l => l.map(e => e.dataset.panel));
await p.click('.seance-tab[data-panel="s3"]'); await p.waitForTimeout(120);
const s3 = await p.$eval('#s3', e => e.classList.contains('active'));
await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(120);
ok(`2 · ${onglets.length} onglets de séance, bascule vers S3 puis retour S1`,
   onglets.length === 3 && s3, onglets.join('|'));

ok('3 · aucun verrou ouvert au chargement — les trois casiers sont vides (n°226)',
   Object.entries(await p.evaluate(() => window.__exp || {}))
     .filter(([k, v]) => k !== 'mode_essentiel'
       && (typeof v === 'object' ? Object.keys(v).length : v)).length === 0,
   JSON.stringify(await p.evaluate(() => window.__exp)));

/* ── les attendus, LUS DANS LE SOURCE de la page ─────────────────────────── */
const SOURCE = fs.readFileSync(SEQ, 'utf8');
const blocCHECKS = SOURCE.slice(SOURCE.indexOf('const CHECKS = {'));
const PLAN = {};
for (const m of blocCHECKS.matchAll(/\n  (\d+)\(\)\s*\{([\s\S]*?)\n  \}/g)) {
  const champs = {};
  for (const s of m[2].matchAll(/\bsv\("([\w.]+)"\s*,\s*"((?:\\.|[^"])*)"\)/g))
    champs[s[1]] = { mode: 'exact', v: s[2] };
  const prose = m[2].match(/\$\("([\w.]+)"\)[\s\S]{0,140}?length\s*>=\s*(\d+)/);
  if (prose) champs[prose[1]] = { mode: 'prose', longueur: Number(prose[2]) };
  PLAN[m[1]] = champs;
}
const compte = m => Object.values(PLAN)
  .reduce((s, o) => s + Object.values(o).filter(c => c.mode === m).length, 0);
ok(`4 · attendus extraits des CHECKS : ${compte('exact')} valeurs et ${compte('prose')} rédaction, `
   + `sur ${Object.keys(PLAN).length} activités — rien n'est recopié ici`,
   Object.keys(PLAN).length === 8 && compte('exact') >= 22 && compte('prose') === 1,
   Object.keys(PLAN).join(','));

const ONGLETS = onglets;
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
  for (const [id, c] of Object.entries(PLAN[n])) {
    if (!(await ouvrirPour(id))) continue;
    const el = await p.$('#' + id); if (!el) continue;
    if (c.mode === 'prose') {
      await p.fill('#' + id, 'Un arrosage déclenché seulement sous le seuil mesuré.'
        .padEnd(c.longueur + 5, ' .'));
      continue;
    }
    if ((await el.evaluate(e => e.tagName)) === 'SELECT') await p.selectOption('#' + id, c.v);
    else await p.fill('#' + id, c.v);
  }
}
const valider = async n => {
  await ouvrirPour(Object.keys(PLAN[n])[0]);
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(100);
};
const retour = n => p.textContent('#fb' + n);
/* `par.s`, la liste des activités validées, est enfermée elle aussi. On lit
   donc ce que la page MONTRE : la classe du bandeau de retour. */
const estValidee = async n => ((await p.getAttribute('#fb' + n, 'class')) || '')
  .split(/\s+/).includes('ok');

await remplir(1); await valider(1);
ok('5 · activité 1 validée 3 / 3 (capteur, carte programmable, écran) — sans réseau',
   /activité validée ✔ 3\/3/.test(await retour(1)), (await retour(1)).slice(0, 55));
await remplir(2); await valider(2);
ok('6 · activité 2 validée 4 / 4 (de la mesure brute au pourcentage)',
   /4\/4/.test(await retour(2)), (await retour(2)).slice(0, 55));

/* ── LE VERROU DE L'ÉDITEUR, RÉSEAU COUPÉ ────────────────────────────────── */
await remplir(3); await valider(3);
ok('7 · activité 3 REFUSÉE malgré les 5 étapes remises dans l\'ordre — l\'éditeur n\'a pas servi',
   /🔒/.test(await retour(3)) && /Ouvre l'éditeur/.test(await retour(3))
   && !(await estValidee(3)), (await retour(3)).slice(0, 70));

const editeurs = await p.$$eval('details.vs', l => l.map(e => e.id));
await ouvrirPour('vs1');
await p.click('#vs1 > summary'); await p.waitForTimeout(200);
ok(`8 · ouvrir le dépliant de l'éditeur pose le verrou vs1 — le GESTE suffit, `
   + `le chargement de l'iframe n'est pas exigé`,
   await p.evaluate(() => !!window.__exp.vs1),
   JSON.stringify(await p.evaluate(() => window.__exp.vs1)));

await valider(3);
ok('9 · activité 3 validée 5 / 5 une fois l\'éditeur ouvert, RÉSEAU TOUJOURS COUPÉ',
   /5\/5/.test(await retour(3)) && await estValidee(3),
   (await retour(3)).slice(0, 55));

await remplir(4); await valider(4);
ok('10 · activité 4 validée 3 / 3, et le pseudo-code s\'est écrit en direct',
   /3\/3/.test(await retour(4))
   && (await p.textContent('#pcSigne')) === '<'
   && /MARCHE/.test(await p.textContent('#pcAction')),
   (await p.textContent('#pcSigne')) + ' ' + (await p.textContent('#pcAction')));

await remplir(5); await valider(5);
ok('11 · activité 5 REFUSÉE à son tour : le second éditeur n\'a pas été ouvert',
   /🔒/.test(await retour(5)) && !(await estValidee(5)),
   (await retour(5)).slice(0, 70));
await ouvrirPour('vs2');
await p.click('#vs2 > summary'); await p.waitForTimeout(200);
await valider(5);
ok('12 · activité 5 validée 4 / 4 (le trou de la condition et les deux appels)',
   /4\/4/.test(await retour(5)) && await estValidee(5),
   (await retour(5)).slice(0, 55));

/* ── LE SIMULATEUR ET LE BANC DE TESTS ───────────────────────────────────── */
await ouvrirPour('seuilRange');
const regler = async (id, v) => {
  await p.$eval('#' + id, (s, x) => {
    s.value = String(x); s.dispatchEvent(new Event('input', { bubbles: true }));
  }, v);
  await p.waitForTimeout(70);
};
const BENCH = eval('(' + (SOURCE.match(/const BENCH = (\{[^;]*\});/) || [])[1] + ')');
const [hSec, sSec] = BENCH['1'];
await regler('seuilRange', sSec); await regler('humRange', hSec);
const sec = await p.textContent('#pompeEtat');
await regler('humRange', Number(sSec) + 20);
const humide = await p.textContent('#pompeEtat');
ok(`13 · simulateur : humidité ${hSec} sous le seuil ${sSec} → pompe en marche ; `
   + `${Number(sSec) + 20} au-dessus → arrêt`,
   /en marche/i.test(sec) && /arrêt/i.test(humide), sec.slice(0, 40) + ' | ' + humide.slice(0, 30));

await remplir(6); await valider(6);
ok('14 · activité 6 REFUSÉE : le banc de tests n\'a pas été exécuté',
   /🔒/.test(await retour(6)) && /les 3 tests du banc/.test(await retour(6))
   && !(await estValidee(6)), (await retour(6)).slice(0, 70));

const tests = Object.keys(BENCH);
for (const t of tests) { await p.click(`.bench-run[data-t="${t}"]`); await p.waitForTimeout(70); }
const obtenus = await Promise.all(tests.map(t => p.textContent('#bt' + t)));
ok(`15 · les ${tests.length} tests du banc exécutés : chacun rend l'attendu que la page déclare `
   + `(${tests.map((t, i) => 'T' + t + ' ' + BENCH[t][2]).join(' · ')})`,
   obtenus.every((o, i) => o.includes(BENCH[tests[i]][2]) && o.includes('✔')),
   obtenus.join(' | '));
ok('16 · le badge du banc s\'affiche et le verrou __exp.tests s\'ouvre — cas frontière compris',
   /badge de validation obtenu/.test(await p.textContent('#benchBadge'))
   && await p.evaluate(() => !!window.__exp.tests),
   (await p.textContent('#benchBadge')).slice(0, 50));

await valider(6);
ok('17 · activité 6 validée une fois le banc au vert',
   /activité validée/.test(await retour(6)) && await estValidee(6),
   (await retour(6)).slice(0, 55));

await remplir(7); await valider(7);
ok('18 · activité 7 validée 4 / 4 (chaque exigence du besoin et SA preuve)',
   /4\/4/.test(await retour(7)) && await estValidee(7),
   (await retour(7)).slice(0, 55));
await remplir(8); await valider(8);
ok('19 · activité 8 validée 2 / 2 (le bénéfice, et la phrase de l\'élève)',
   /2\/2/.test(await retour(8)) && await estValidee(8),
   (await retour(8)).slice(0, 55));

ok('20 · progression 8 / 8 activités, RÉSEAU COUPÉ D\'UN BOUT À L\'AUTRE',
   (await p.textContent('#progTxt')).includes('8 / 8')
   && (await p.$$eval('[id^="done-s"]', l => l.map(e => e.textContent.trim())))
        .every(c => c === '✔'),
   await p.textContent('#progTxt'));

/* ── ce que la coupure a réellement empêché ──────────────────────────────── */
const hotes = [...new Set(bloquees.map(u => new URL(u).host))];
ok(`21 · ${bloquees.length} requête(s) distante(s) refusées pendant toute la séance, `
   + `vers ${hotes.length} hôte(s) : ${hotes.join(', ')}`,
   hotes.length > 0 && hotes.every(h => /vittascience|fonts\.g/.test(h)), hotes.join(', '));
ok(`22 · les ${editeurs.length} éditeurs distants sont TOUS dans un dépliant refermé par défaut : `
   + 'rien ne part avant un geste',
   editeurs.length === 3
   && (await p.$$eval('details.vs',
        l => l.every(e => e.querySelector('iframe') && e.querySelector('iframe')
             .getAttribute('loading') === 'lazy'))),
   editeurs.join(','));

/* ── persistance ─────────────────────────────────────────────────────────── */
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(360);
ok('23 · rechargement : réponses, progression 8 / 8 et les trois verrous sont restaurés',
   (await p.inputValue('#a1q1')) === PLAN[1].a1q1.v
   && (await p.textContent('#progTxt')).includes('8 / 8')
   && await p.evaluate(() => !!(window.__exp.vs1 && window.__exp.vs2 && window.__exp.tests)),
   await p.textContent('#progTxt'));

const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok(`24 · les ${liens.length} liens internes existent`, casses.length === 0,
   casses.slice(0, 3).join(' · '));

ok('25 · aucune boîte modale, aucune erreur JS malgré les iframes refusées',
   dlg.length === 0 && err.filter(e => !/ERR_FAILED|net::/i.test(e)).length === 0,
   (err[0] || dlg[0] || '').slice(0, 80));
await ctx.close();
}

/* ════════════════ QCM (10 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = []; p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });

await p.goto('file://' + QCM, { waitUntil: 'load' });
await p.waitForTimeout(300);

const Q = await p.evaluate(() => QUESTIONS.map(q => ({
  c: q.c, n: q.n, o: q.o, r: q.r, d: q.d, expl: q.expl, ex: q.ex, err: q.err, ret: q.ret })));

ok('26 · chargement du QCM, titre à la charte portant le code 4e_C6.2',
   /4e_C6\.2/.test(await p.title()) || /4e_C6\.2/.test(await p.textContent('body')));

ok(`27 · ${Q.length} questions, ${new Set(Q.map(q => q.n)).size} notions toutes distinctes`,
   Q.length === 30 && new Set(Q.map(q => q.n)).size === Q.length,
   String(new Set(Q.map(q => q.n)).size));

const refutations = Q.reduce((s, q) => s + q.d.filter(x => x).length, 0);
ok(`28 · ${refutations} réfutations — une par distracteur — et aucune posée sur la bonne réponse`,
   refutations === Q.length * 3 && Q.every(q => q.d[q.r] === ''), String(refutations));

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`29 · bonnes réponses A/B/C/D = ${rep.join('/')} (écart max 1)`,
   Math.max(...rep) - Math.min(...rep) <= 1, rep.join('/'));

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
const inventes = Object.keys(parCode).filter(c => !/^C[1-9]\.\d+$/.test(c));
ok(`30 · ${Object.keys(parCode).length} codes du programme, aucun code inventé : `
   + Object.entries(parCode).map(([c, n]) => c + '×' + n).join(' · '),
   inventes.length === 0, inventes.join(' · '));

const incomplets = Q.filter(q => !(q.o.length === 4 && q.d.length === 4 && q.expl && q.ex
                                   && q.err && q.ret && q.n && q.c));
const doublons = Q.filter(q => new Set(q.o).size !== q.o.length);
ok('31 · gabarit complet partout (c n q o r expl ex err d ret), aucune option dupliquée',
   incomplets.length === 0 && doublons.length === 0,
   incomplets.concat(doublons).map(q => q.n).slice(0, 3).join(' · '));

/* Le test le plus utile du rapport d'origine : la bonne réponse ne doit pas se
   deviner à sa longueur. Le seuil de 8 caractères est celui de la maison. */
const SEUIL = 8;
const detachees = Q.filter(q => {
  const l = q.o.map(o => o.length), bonne = l[q.r];
  const autres = l.filter((_, i) => i !== q.r);
  return bonne - Math.max(...autres) > SEUIL || Math.min(...autres) - bonne > SEUIL;
});
const ecart = Q.reduce((s, q) => {
  const l = q.o.map(o => o.length), autres = l.filter((_, i) => i !== q.r);
  return s + l[q.r] - autres.reduce((a, b) => a + b, 0) / autres.length;
}, 0) / Q.length;
ok(`32 · aucune bonne réponse détachée de plus de ${SEUIL} caractères ; écart moyen `
   + `${ecart.toFixed(1)} caractère(s)`,
   detachees.length === 0, detachees.map(q => q.n).slice(0, 3).join(' · '));

const html = await p.content();
ok('33 · aucune réponse exposée dans le HTML rendu (pas de value="v0" révélateur)',
   !/value="v\d"/.test(html));

const retourSeq = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href'))
  .filter(h => h && /sequence.*\.html$/.test(h)));
ok('34 · le lien de retour vers la séquence du lot pointe sur un fichier réel',
   retourSeq.length > 0
   && retourSeq.every(h => fs.existsSync(path.join(ICI, decodeURIComponent(h)))),
   retourSeq[0] || '');

ok('35 · aucune erreur JS sur le QCM', err.length === 0, err.slice(0, 2).join(' | '));
await ctx.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
