/* tests_3e_C4.1-C4.2.mjs — « L'énergie de la station », rejouable.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de ce lot citait `tests_lot06.js`, jamais commité — il l'avoue
 * depuis le 31/08/2026. C'est le lot en tête de la file publiée par
 * `_outils/controle_rapports_tests.py` (règles n°259, n°266).
 *
 * Ce lot a une singularité : son **verrou expérientiel exige DEUX essais de
 * sens contraire** — une configuration de batterie qui NE tient PAS les 72 h,
 * puis une qui les tient. Sa consigne l'écrit à l'élève : « teste D'ABORD une
 * configuration insuffisante, PUIS ta solution ». Le 31/08 au matin, la page
 * cochait le second toute seule au chargement (corrigé, PR #310) ; cette suite
 * vérifie qu'elle n'en coche plus aucun, et qu'il faut vraiment produire
 * l'échec avant la réussite.
 *
 * Les réponses sont extraites des `CHECKS` de la page, selon les **quatre
 * conventions** que ce lot emploie :
 *
 *     att = {id: "valeur"}                       → on choisit « valeur »
 *     $("id").value === "valeur"                 → idem
 *     num("id") === N                            → on saisit N
 *     new Set([$("a").value, $("b").value]) + .has("X")  → les deux intrus
 *
 * Seule la justification en prose est rédigée ici — et les contraintes que la
 * page exige d'y croiser sont lues dans son code, pas devinées.
 *
 * Usage, depuis ce dossier :
 *   node tests_3e_C4.1-C4.2.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence_3e_C4.1-C4.2_energie_station.html');
const QCM = path.join(ICI, 'qcm_3e_C4.1-C4.2_energie_station.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ SÉQUENCE (13 contrôles) ════════════════ */
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

ok('1 · chargement sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('1 bis · aucun verrou ouvert au chargement (règle n°226, corrigé le 31/08)',
   Object.keys(await p.evaluate(() => window.__exp || {}))
     .filter(k => k !== 'mode_essentiel').length === 0,
   JSON.stringify(await p.evaluate(() => window.__exp)));

await p.fill('#hyp1', 'Je pense qu\'il faut une grosse batterie pour tenir trois jours sans soleil.');
await p.waitForTimeout(140);
ok('2 · rappel d\'hypothèse affiché dès la saisie',
   (await p.textContent('#hypRappelTxt')).includes('batterie'),
   await p.textContent('#hypRappelTxt'));

/* ── les réponses attendues, LUES dans la page ───────────────────────────── */
const PLAN = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const src = CHECKS[n].toString();
    const plan = { valeurs: {}, nombres: {}, ensemble: null, prose: {} };
    const objet = src.match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    if (objet) Object.assign(plan.valeurs, eval('(' + objet[1] + ')'));
    for (const m of src.matchAll(/\$\("([\w.]+)"\)\.value\s*===\s*"([^"]*)"/g))
      plan.valeurs[m[1]] = m[2];
    for (const m of src.matchAll(/num\("([\w.]+)"\)\s*===\s*([\d.]+)/g))
      plan.nombres[m[1]] = m[2];
    // convention des « intrus » : un ensemble de deux champs, et ce qu'il doit contenir
    const jeu = src.match(/new Set\(\[\s*\$\("([\w.]+)"\)\.value\s*,\s*\$\("([\w.]+)"\)\.value\s*\]\)/);
    if (jeu) {
      const attendus = [...src.matchAll(/\.has\("([^"]+)"\)/g)].map(x => x[1]);
      plan.ensemble = { champs: [jeu[1], jeu[2]], attendus };
    }
    for (const m of src.matchAll(/txt\("([\w.]+)"\)/g)) plan.prose[m[1]] = true;
    out[n] = plan;
  }
  return out;
});
const champs = Object.values(PLAN).reduce(
  (s, o) => s + Object.keys(o.valeurs).length + Object.keys(o.nombres).length
              + (o.ensemble ? o.ensemble.champs.length : 0), 0);
ok(`2 bis · ${champs} champs extraits de la page (aucune réponse recopiée ici)`,
   Object.keys(PLAN).length === 6 && champs >= 30, String(champs));

/* la seule prose de ce fichier : elle croise deux contraintes, comme la page l'exige */
const PROSE = {
  j4: "Le mât doit résister au vent cyclonique, et le sel des embruns impose des métaux "
      + "galvanisés ; on choisit aussi des matériaux recyclables.",
};

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
async function poser(id, v) {
  if (!(await ouvrirPour(id))) return;
  const el = await p.$('#' + id); if (!el) return;
  if ((await el.evaluate(e => e.tagName)) === 'SELECT') await p.selectOption('#' + id, v);
  else await p.fill('#' + id, String(v));
}
async function remplir(n) {
  const plan = PLAN[n];
  for (const [id, v] of Object.entries(plan.valeurs)) await poser(id, v);
  for (const [id, v] of Object.entries(plan.nombres)) await poser(id, v);
  if (plan.ensemble)
    for (let i = 0; i < plan.ensemble.champs.length; i++)
      await poser(plan.ensemble.champs[i], plan.ensemble.attendus[i]);
  for (const id of Object.keys(plan.prose))
    if (PROSE[id]) await poser(id, PROSE[id]);
}
const valider = async n => {
  const premier = Object.keys(PLAN[n].valeurs)[0] || Object.keys(PLAN[n].nombres)[0];
  if (premier) await ouvrirPour(premier);
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(90);
};
const retour = n => p.textContent('#fb' + n);

await remplir(1); await valider(1);
ok('3 · activité 1 validée 11/11 (5 blocs, 4 natures, 2 intrus)',
   /11 \/ 11/.test(await retour(1)), (await retour(1)).slice(0, 70));

/* ── LE VERROU AUX DEUX ESSAIS ───────────────────────────────────────────── */
await remplir(2); await valider(2);
ok('4 · activité 2 REFUSÉE sans les deux essais au simulateur',
   /Fais VRAIMENT les deux essais/.test(await retour(2)), (await retour(2)).slice(0, 95));

async function regler(cap, conso) {
  for (const [id, v] of [['simCap', cap], ['simConso', conso]]) {
    await ouvrirPour(id);
    await p.evaluate(([i, x]) => {
      const s = document.getElementById(i);
      s.value = String(x); s.dispatchEvent(new Event('input', { bubbles: true }));
    }, [id, v]);
    await p.waitForTimeout(60);
  }
  return (await p.textContent('#simVerdict')).trim();
}
const bornes = await p.$eval('#simCap', s => [Number(s.min), Number(s.max)]);
const petit = await regler(bornes[0], await p.$eval('#simConso', s => s.max));
ok('5 · simulateur : la plus petite batterie avec la plus grosse consommation NE TIENT PAS',
   /Station muette|❌/.test(petit), petit.slice(0, 80));
const grand = await regler(bornes[1], await p.$eval('#simConso', s => s.min));
ok('6 · simulateur : la plus grosse batterie avec la plus petite consommation TIENT les 72 h',
   /tient les 72|✅/.test(grand), grand.slice(0, 80));
const essais = await p.evaluate(() => ({ ...window.__exp }));
ok('7 · les DEUX essais de sens contraire sont tracés, et seulement par le geste',
   essais.insuffisant !== undefined && essais.suffisant !== undefined,
   JSON.stringify(essais));

await valider(2);
ok('8 · activité 2 validée (432 Wh, 36 Ah, choix 40 Ah) une fois les deux essais faits',
   /3 \/ 3/.test(await retour(2)) && !/Fais VRAIMENT/.test(await retour(2)),
   (await retour(2)).slice(0, 70));

for (const n of [3, 4, 5, 6]) { await remplir(n); await valider(n); }
ok('9 · activité 3 (contraintes du site) validée 5/5',
   /5 \/ 5/.test(await retour(3)), (await retour(3)).slice(0, 40));
ok('10 · activité 4 (matériaux et procédés) validée 8/8 avec justification croisée',
   /8 \/ 8/.test(await retour(4)) && !/croiser AU MOINS deux/.test(await retour(4)),
   (await retour(4)).slice(0, 70));
ok('11 · activité 5 (borne du stade) et le calcul du fusible validés',
   /5 \/ 5/.test(await retour(5)) && /3 \/ 3/.test(await retour(6)),
   (await retour(5)).slice(0, 26) + ' | ' + (await retour(6)).slice(0, 26));

ok('12 · barre de progression : 5 / 5 activités validées',
   (await p.textContent('#progTxt')).includes('5 / 5'), await p.textContent('#progTxt'));
const coches = await p.$$eval('[id^="done-s"]', l => l.map(e => e.textContent.trim()));
ok('12 bis · les deux séances portent leur coche',
   coches.length > 0 && coches.every(c => c === '✔'), coches.join('|'));

await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(320);
const premier = Object.keys(PLAN[1].valeurs)[0];
ok('13 · rechargement : réponses, validations ET les deux essais restaurés',
   (await p.inputValue('#' + premier)) === PLAN[1].valeurs[premier]
   && (await p.textContent('#progTxt')).includes('5 / 5')
   && await p.evaluate(() => window.__exp.insuffisant !== undefined
                          && window.__exp.suffisant !== undefined),
   await p.textContent('#progTxt'));

const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok(`13 bis · les ${liens.length} liens locaux existent (le défaut inter-dossiers de juillet reste corrigé)`,
   casses.length === 0, casses.slice(0, 3).join(' · '));

ok('13 ter · aucune boîte modale, aucune requête échouée, aucune erreur JS',
   dlg.length === 0 && fail.length === 0 && err.length === 0,
   (err[0] || fail[0] || dlg[0] || '').slice(0, 80));
await ctx.close();
}

/* ════════════════ QCM (5 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = []; p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });

await p.goto('file://' + QCM, { waitUntil: 'load' });
await p.waitForTimeout(280);

const Q = await p.evaluate(() => QUESTIONS.map(q => ({
  c: q.c, r: q.r, d: q.d, o: q.o, img: q.img ? q.img.src : null })));
ok('14 · chargement sans erreur JS · 30 questions, 15 par code',
   Q.length === 30 && Q.filter(x => x.c === 'C4.1').length === 15
   && Q.filter(x => x.c === 'C4.2').length === 15 && err.length === 0,
   `${Q.length} · ${err[0] || 'aucune erreur'}`);

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`15 · bonnes réponses A/B/C/D = ${rep.join('/')} (écart max 1) et d[r] vide partout`,
   Math.max(...rep) - Math.min(...rep) <= 1 && Q.every(q => q.d[q.r] === ''), rep.join('/'));

const illustrees = Q.filter(q => q.img);
const absentes = illustrees.filter(q => !fs.existsSync(path.join(ICI, q.img)));
ok(`16 · ${illustrees.length} questions illustrées, SVG présents sur le disque`,
   illustrees.length > 0 && absentes.length === 0, absentes.map(q => q.img).join(' · '));

for (let i = 0; i < Q.length; i++) {
  const r = await p.evaluate(
    () => QUESTIONS[Number(document.getElementById('qNum').textContent) - 1].r);
  const options = await p.$$('#qOptions .option');
  await options[r].click();
  await p.click('#btnValider');
  await p.waitForTimeout(15);
  if (i < Q.length - 1) { await p.click('#btnSuiv'); await p.waitForTimeout(15); }
}
await p.click('#btnTerminer');
await p.waitForTimeout(250);
const note = (await p.textContent('#rNote')).replace(/\s/g, '');
const bilan = await p.$$eval('#tblBilan tr', l => l.length);
ok('17 · parcours 30/30 → 20,0/20 · bilan par 2 codes',
   Number(await p.textContent('#rOk')) === 30 && /20[.,]0?\/20/.test(note) && bilan >= 2,
   `${await p.textContent('#rOk')} · ${note} · ${bilan} lignes`);

ok('18 · aucune erreur JS après le scénario complet', err.length === 0,
   err.slice(0, 2).join(' | '));
await ctx.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
