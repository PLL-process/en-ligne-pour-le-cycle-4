/* tests_3e_C4.3-C4.6.mjs — le LOT 01 « Station d'alerte cyclonique », rejouable.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * C'est le premier lot du Thème 2, livré le 22/07/2026, et le plus fourni de la
 * file d'attente publiée par `_outils/controle_rapports_tests.py` : **26 coches
 * vertes** dans un rapport dont aucune suite n'était livrée (règles d'or n°259
 * et n°266). Les voici rejouées.
 *
 * CE QU'IL CONDUIT VRAIMENT
 * -------------------------
 * Le simulateur de convertisseur analogique-numérique, curseur par curseur ; la
 * table des 48 heures de mesures ; les sept activités ; et le QCM joué trois
 * fois de suite pour vérifier les **trois scénarios de notes** que le rapport
 * calculait à la main : 32/32 → 20,0/20 · 16+16 → 10,0/20 · 8+8+16 non
 * répondues → 5,0/20.
 *
 * LES RÉPONSES NE SONT PAS RECOPIÉES ICI
 * ---------------------------------------
 * Elles sont extraites des fonctions `CHECKS` de la page, selon les **quatre
 * conventions d'écriture** que ce lot emploie — et elles seules :
 *
 *     att = {id: "valeur"}                  → on choisit « valeur »
 *     $("id").value === "valeur"            → idem
 *     $("id").value.startsWith("début")     → on choisit l'option qui commence ainsi
 *     num("id") === N  /  Math.abs(num("id") - N) <= E   → on saisit N
 *
 * Tout ce qui sort de ces quatre formes n'est pas piloté, et le contrôle nº6 le
 * dit : il compte les champs pilotés et refuse si la moisson est maigre. Les
 * champs de PROSE libre sont les seuls que ce fichier rédige lui-même — et
 * encore, les mots que la page exige y sont lus, pas devinés.
 *
 * Usage, depuis ce dossier :
 *   node tests_3e_C4.3-C4.6.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html');
const QCM = path.join(ICI, 'qcm_3e_C4.3-C4.6_station_alerte_cyclonique.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ SÉQUENCE ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

await p.goto('file://' + SEQ, { waitUntil: 'load' });
await p.waitForTimeout(350);

ok('1 · chargement sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));

const nData = await p.evaluate(() => (typeof DATA !== 'undefined' ? DATA.length : -1));
const nLignes = await p.$$eval('table tbody tr', l => l.length);
ok('2 · la table de données porte les 48 enregistrements des 48 heures',
   nData === 48 && nLignes >= 48, `DATA=${nData} · <tr>=${nLignes}`);

/* ── le simulateur de CAN, conduit au curseur ────────────────────────────── */
async function pression(hPa) {
  await p.evaluate(v => {
    const s = document.getElementById('simPression');
    s.value = String(v);
    s.dispatchEvent(new Event('input', { bubbles: true }));
  }, hPa);
  await p.waitForTimeout(50);
}
await pression(943);
const n943 = Number(await p.textContent('#simN'));
ok('3 · simulateur CAN : N(943 hPa) = 512 ± 1', Math.abs(n943 - 512) <= 1, String(n943));
const bin943 = (await p.textContent('#simBin')).trim();
ok('3 bis · le mot binaire affiché est celui du nombre affiché',
   parseInt(bin943, 2) === n943 && bin943.length === 10, `${bin943} → ${parseInt(bin943, 2)}`);
await pression(1018);
ok('3 ter · la borne haute du capteur donne la valeur maximale du convertisseur',
   Number(await p.textContent('#simN')) === 1023, await p.textContent('#simN'));

/* ── les réponses attendues, LUES dans les CHECKS de la page ─────────────── */
const PLAN = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const src = CHECKS[n].toString();
    const plan = { selects: {}, prefixes: {}, nombres: {}, prose: {} };
    const objet = src.match(/att(?:endu)?\s*=\s*(\{[\s\S]*?\})\s*;/);
    if (objet) Object.assign(plan.selects, eval('(' + objet[1] + ')'));
    for (const m of src.matchAll(/\$\("([\w.]+)"\)\.value\s*===\s*"([^"]*)"/g))
      plan.selects[m[1]] = m[2];
    for (const m of src.matchAll(/\$\("([\w.]+)"\)\.value\.startsWith\("([^"]*)"\)/g))
      plan.prefixes[m[1]] = m[2];
    for (const m of src.matchAll(/num\("([\w.]+)"\)\s*===\s*([\d.]+)/g))
      plan.nombres[m[1]] = m[2];
    for (const m of src.matchAll(/Math\.abs\(num\("([\w.]+)"\)\s*-\s*([\d.]+)\)/g))
      plan.nombres[m[1]] = m[2];
    // les champs de prose : on relève les mots que la page exige
    for (const m of src.matchAll(/txt\("([\w.]+)"\)/g)) {
      const mots = [...src.matchAll(/\.includes\("([^"]+)"\)/g)].map(x => x[1]);
      plan.prose[m[1]] = mots;
    }
    out[n] = plan;
  }
  return out;
});

const pilotes = Object.values(PLAN).reduce(
  (s, o) => s + Object.keys(o.selects).length + Object.keys(o.prefixes).length
              + Object.keys(o.nombres).length, 0);
ok(`6 · ${pilotes} champs pilotés, tous extraits de la page (aucune réponse recopiée ici)`,
   Object.keys(PLAN).length === 7 && pilotes >= 40, String(pilotes));

/* la prose est la seule chose que ce fichier rédige — avec les mots exigés */
const PROSE = {
  a1_just: "Le panneau solaire alimente la station : sans lui, plus aucune mesure ne part.",
  a3_exp: "Le convertisseur ne rend pas un signal continu mais des paliers : entre deux "
          + "paliers, l'information est perdue.",
  a6_conc: "Quand le vent monte, la pression baisse nettement : croiser les deux mesures "
           + "rend l'alerte bien plus sûre qu'une seule.",
  a7_just: "Le réseau peut être coupé pendant le cyclone : une copie locale garde les mesures "
           + "jusqu'au retour de la liaison.",
};

/* La répartition est celle de `majProgress()` dans la page, pas une supposition. */
const PANNEAU = { 1: 's1', 2: 's1', 3: 's2', 4: 's3', 5: 's4', 6: 's4', 7: 's4' };
async function remplir(n) {
  const onglet = await p.$(`.seance-tab[data-panel="${PANNEAU[n]}"]`);
  if (onglet) { await onglet.click(); await p.waitForTimeout(110); }
  const plan = PLAN[n];
  for (const [id, v] of Object.entries(plan.selects)) {
    const el = await p.$('#' + id); if (!el) continue;
    if ((await el.evaluate(e => e.tagName)) === 'SELECT') await p.selectOption('#' + id, v);
    else await p.fill('#' + id, v);
  }
  for (const [id, debut] of Object.entries(plan.prefixes)) {
    const val = await p.$eval('#' + id,
      (s, d) => [...s.options].map(o => o.value || o.textContent).find(x => x.startsWith(d)), debut);
    if (val) await p.selectOption('#' + id, val);
  }
  for (const [id, v] of Object.entries(plan.nombres)) {
    const el = await p.$('#' + id); if (el) await p.fill('#' + id, String(v));
  }
  // seulement les champs de prose de CETTE activité : les autres vivent dans un
  // onglet masqué, et Playwright refuse d'écrire dans ce qui n'est pas visible.
  for (const [id, texte] of Object.entries(PROSE)) {
    if (!id.startsWith('a' + n + '_')) continue;
    const el = await p.$('#' + id);
    if (el && (await p.inputValue('#' + id)) === '') await p.fill('#' + id, texte);
  }
}
const valider = async n => { await p.click(`[data-check="${n}"]`); await p.waitForTimeout(90); };
const retour = n => p.textContent('#fb' + n);

/* activité 1 : d'abord SANS la justification, pour voir le refus ─────────── */
await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(110);
for (const [id, v] of Object.entries(PLAN[1].selects)) await p.selectOption('#' + id, v);
await valider(1);
ok('4 · activité 1 : les 8 réponses justes mais pas de justification → pas encore validée',
   /8 \/ 8/.test(await retour(1)) && /justification/i.test(await retour(1)),
   (await retour(1)).slice(0, 80));
await p.fill('#a1_just', PROSE.a1_just);
await valider(1);
ok('5 · activité 1 validée : 8/8 et la justification rédigée',
   /8 \/ 8/.test(await retour(1)) && !/justification/i.test(await retour(1)),
   (await retour(1)).slice(0, 70));

/* ── les six autres activités ────────────────────────────────────────────── */
const scores = {};
for (const n of [2, 3, 4, 5, 6, 7]) {
  await remplir(n); await valider(n);
  scores[n] = (await retour(n)).slice(0, 12).trim().replace(/\s+/g, '');
}
/* C'est le verdict de la PAGE qui fait foi, pas un score plein supposé : deux
   activités se valident à un point du maximum (`ok>=8` sur 9, `ok>=3` sur 4),
   et ce sont justement les deux qui emploient une convention d'écriture que ce
   fichier ne pilote pas — la concaténation de trois champs binaires (a4_b1..b3)
   et le texte normalisé de a6_1. La limite est déclarée ici plutôt que masquée
   par un test plus indulgent. */
const valides = await p.evaluate(() => ({ ...window.__valid }));
ok('7 · les six autres activités sont VALIDÉES par la page elle-même',
   [2, 3, 4, 5, 6, 7].every(n => valides[n] === true),
   Object.entries(scores).map(([n, s]) => `a${n}:${s}`).join(' · '));
ok('7 bis · les deux champs non pilotés sont les seuls points manquants (limite déclarée)',
   scores[4].startsWith('8/9') && scores[6].startsWith('3/4'),
   `a4:${scores[4]} · a6:${scores[6]}`);

ok('8 · barre de progression : 7 / 7 activités validées',
   (await p.textContent('#progTxt')).includes('7 / 7'), await p.textContent('#progTxt'));

/* ── onglets de séance ───────────────────────────────────────────────────── */
await p.click('.seance-tab[data-panel="s3"]'); await p.waitForTimeout(110);
ok('9 · onglets de séances fonctionnels',
   await p.$eval('#s3', e => e.classList.contains('active')));

/* ── rechargement ────────────────────────────────────────────────────────── */
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(350);
ok('10 · progression restaurée après rechargement (localStorage)',
   (await p.textContent('#progTxt')).includes('7 / 7'), await p.textContent('#progTxt'));
const premier = Object.keys(PLAN[1].selects)[0];
ok('11 · les réponses aussi sont restaurées',
   (await p.inputValue('#' + premier)) === PLAN[1].selects[premier],
   await p.inputValue('#' + premier));

/* ── liens locaux, y compris CSV / ODS / XLSX ────────────────────────────── */
const adresses = await p.$$eval('a[href], img[src], object[data]',
  l => l.map(e => e.getAttribute('href') || e.getAttribute('src') || e.getAttribute('data')));
const casses = adresses.filter(h => h && !/^(https?:|mailto:|#|javascript:|data:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok(`12 · aucun lien local cassé (${adresses.length} adresses : SVG, CSV/ODS/XLSX, QCM)`,
   casses.length === 0, casses.slice(0, 3).join(' · '));

/* ── lien d'évitement accessible au clavier ──────────────────────────────── */
/* Le lien d'évitement se reconnaît à sa classe — c'est la convention du dépôt.
   Le chercher par son libellé était une devinette : celui-ci dit « Aller
   directement aux activités », et une première version de ce test l'a manqué. */
const skip = await p.$$eval('a.skip-link',
  l => l.map(e => ({ href: e.getAttribute('href'), texte: e.textContent.trim() })));
const cibleSkip = skip.length
  ? await p.$(skip[0].href) : null;
await p.focus('a.skip-link').catch(() => {});
const visibleAuFocus = skip.length && await p.$eval('a.skip-link',
  e => e.getBoundingClientRect().left > -1000);
ok('13 · un lien d\'évitement existe, vise une ancre réelle, et se montre au focus clavier',
   skip.length > 0 && cibleSkip !== null && visibleAuFocus,
   skip.length ? `${skip[0].texte} → ${skip[0].href}` : 'aucun');

ok('14 · aucune boîte modale, aucune erreur JS sur la séquence',
   dlg.length === 0 && err.length === 0, (err[0] || dlg[0] || '').slice(0, 80));
await ctx.close();
}

/* ════════════════ QCM — dont les trois scénarios de notes ════════════════ */
/** Joue une partie : `justes` bonnes, `fausses` mauvaises, le reste non répondu. */
async function partie(justes, fausses) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
  const p = await ctx.newPage();
  const err = []; p.on('pageerror', e => err.push(e.message));
  await p.goto('file://' + QCM, { waitUntil: 'load' });
  await p.waitForTimeout(250);
  const total = await p.evaluate(() => QUESTIONS.length);
  for (let i = 0; i < justes + fausses; i++) {
    const r = await p.evaluate(
      () => QUESTIONS[Number(document.getElementById('qNum').textContent) - 1].r);
    const options = await p.$$('#qOptions .option');
    await options[i < justes ? r : (r + 1) % 4].click();
    await p.click('#btnValider');
    await p.waitForTimeout(20);
    if (i < total - 1) { await p.click('#btnSuiv'); await p.waitForTimeout(20); }
  }
  await p.click('#btnTerminer');
  await p.waitForTimeout(250);
  const lu = async s => (await p.textContent(s)).replace(/\s/g, '');
  const res = { total, note: await lu('#rNote'), ok: Number(await lu('#rOk')),
                err: Number(await lu('#rErr')), non: Number(await lu('#rNon')),
                pct: await lu('#rPct'), erreursJS: err.length,
                bilan: await p.$$eval('#tblBilan tr', l => l.length) };
  await ctx.close();
  return res;
}

const s1 = await partie(32, 0);
ok(`15 · QCM : la banque porte ${s1.total} questions`, s1.total === 32, String(s1.total));
ok('16 · scénario S1 — 32 correctes → 32 pts · 20,0/20 · 100 %',
   s1.ok === 32 && /20[.,]0?\/20/.test(s1.note) && /100/.test(s1.pct),
   `${s1.ok} · ${s1.note} · ${s1.pct}`);
ok('17 · le bilan par compétence compte quatre lignes', s1.bilan >= 4, String(s1.bilan));
ok('18 · aucune erreur JS sur le parcours complet', s1.erreursJS === 0);

const s2 = await partie(16, 16);
ok('19 · scénario S2 — 16 correctes + 16 fausses → 16 pts · 10,0/20 · 50 %',
   s2.ok === 16 && s2.err === 16 && /10[.,]0?\/20/.test(s2.note) && /50/.test(s2.pct),
   `${s2.ok}/${s2.err} · ${s2.note} · ${s2.pct}`);

const s3 = await partie(8, 8);
ok('20 · scénario S3 — 8 + 8 + 16 non répondues → 8 pts · 5,0/20 · 25 % · 16 NR',
   s3.ok === 8 && s3.err === 8 && s3.non === 16 && /5[.,]0?\/20/.test(s3.note)
   && /25/.test(s3.pct), `${s3.ok}/${s3.err}/${s3.non} · ${s3.note} · ${s3.pct}`);

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
