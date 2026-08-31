/* tests_5e_C4.1-C4.8_sequence.mjs — les seize coches de la séquence, rejouées.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport du lot annonçait « Séquence (16 tests) », seize lignes, seize
 * coches vertes — et citait un script `tests_lot05.js` **jamais commité**. Le
 * QCM a reçu sa suite le 31/08/2026 ; la séquence est restée avec sa liste de
 * bonnes intentions (règle d'or n°259).
 *
 * Ce fichier conduit la séquence POUR DE VRAI : il remplit les sept activités,
 * manœuvre le simulateur, provoque un passage devant le détecteur, et lit ce
 * que la page répond.
 *
 * IL NE RECOPIE PAS LES BONNES RÉPONSES. Elles sont extraites des fonctions
 * `CHECKS` de la page elle-même : un test qui recopie ce qu'il doit vérifier
 * cesse de le vérifier, et se désynchronise en silence le jour où la séquence
 * change une option.
 *
 * CE QU'IL A TROUVÉ EN NAISSANT
 * -----------------------------
 * `window.__exp` valait `{"jour":"eteint"}` **au chargement de la page** :
 * `majLampe()` était appelé à l'initialisation et enregistrait l'état affiché
 * comme une expérience observée. Le verrou de l'activité 3 en exige trois
 * (jour, nuit, nuit+passage) : il s'ouvrait donc d'un tiers tout seul, avant
 * que l'élève ait touché le curseur. C'est exactement ce que la règle d'or
 * n°226 interdit, et le tableau écrit à la main affirmait le contraire.
 *
 * Usage, depuis ce dossier :
 *   node tests_5e_C4.1-C4.8_sequence.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const PAGE = path.join(ICI, 'sequence_5e_C4.1-C4.8_lampadaire_intelligent.html');

const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => { if (!/fonts\.g/.test(r.url())) fail.push(r.url()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });

await p.goto('file://' + PAGE, { waitUntil: 'load' });
await p.waitForTimeout(350);

ok('1 · charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('2 · aucune requête locale échouée', fail.length === 0, fail.slice(0, 2).join(' | '));

/* ── règle d'or n°226 : aucun verrou ouvert avant le premier geste ───────── */
const expDepart = await p.evaluate(() => window.__exp || {});
ok('3 · aucune expérience enregistrée au chargement (règle n°226)',
   Object.keys(expDepart).length === 0, JSON.stringify(expDepart));
ok('4 · aucune activité validée au chargement',
   Object.keys(await p.evaluate(() => window.__valid || {})).length === 0);

/* ── les réponses attendues, LUES dans la page ───────────────────────────── */
const ATT = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const m = CHECKS[n].toString().match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    out[n] = m ? eval('(' + m[1] + ')') : {};
  }
  return out;
});
const totalChamps = Object.values(ATT).reduce((s, o) => s + Object.keys(o).length, 0);
ok('5 · les bonnes réponses sont extraites de la page, pas recopiées ici',
   Object.keys(ATT).length === 7 && totalChamps >= 45,
   `${Object.keys(ATT).length} activités · ${totalChamps} champs`);

/* Les activités vivent dans cinq onglets de séance, et un onglet inactif est
   masqué : il faut l'ouvrir comme un élève le ferait. La répartition est celle
   de `majProgress()` dans la page — s5 porte les activités 5, 6 et 7. */
const SEANCE = { 1: 's1', 2: 's2', 3: 's3', 4: 's4', 5: 's5', 6: 's5', 7: 's5' };
async function ouvrirSeance(n) {
  await p.click(`.seance-tab[data-panel="${SEANCE[n]}"]`);
  await p.waitForTimeout(120);
}

/** Renseigne les champs d'une activité avec ce que la page attend. */
async function remplir(n) {
  await ouvrirSeance(n);
  for (const [id, v] of Object.entries(ATT[n])) {
    const balise = await p.$eval('#' + id, e => e.tagName);
    if (balise === 'SELECT') await p.selectOption('#' + id, v);
    else await p.fill('#' + id, v);
  }
}
const valider = async n => { await p.click(`[data-check="${n}"]`); await p.waitForTimeout(90); };
const retour = n => p.textContent('#fb' + n);

/* ── activité 1 : associations + matériaux + justification ───────────────── */
await remplir(1);
await valider(1);
ok('6 · act. 1 refusée tant que la justification ne parle pas du sel marin',
   !/Excellent|Bravo|Très bien/.test(await retour(1)), (await retour(1)).slice(0, 80));
await p.fill('#e1_just', "Près de la mer, les embruns apportent du sel : l'acier rouille vite.");
await valider(1);
ok('7 · act. 1 validée avec les 9 réponses et la justification', /9 \/ 9/.test(await retour(1)),
   (await retour(1)).slice(0, 70));

/* ── activité 2 : chaîne d'énergie, ordre et natures ─────────────────────── */
await remplir(2);
await valider(2);
ok('8 · act. 2 refusée sans la chaîne fléchée au cahier',
   !/9 \/ 9 réponses correctes. (Excellent|Bravo|Très bien)/.test(await retour(2)),
   (await retour(2)).slice(0, 80));
await p.fill('#e2_cahier', 'lumineuse → électrique → chimique → électrique → lumineuse');
await valider(2);
ok('9 · act. 2 validée (9/9) une fois la chaîne écrite', /9 \/ 9/.test(await retour(2)),
   (await retour(2)).slice(0, 70));

/* ── activité 3 : LE VERROU EXPÉRIENTIEL ─────────────────────────────────── */
await remplir(3);
await valider(3);
ok('10 · act. 3 REFUSÉE tant que les trois expériences ne sont pas faites',
   /Fais VRAIMENT les expériences/.test(await retour(3)), (await retour(3)).slice(0, 90));

/** Manœuvre le simulateur comme un élève : curseur, puis bouton de passage. */
async function regler(lum) {
  await p.evaluate(v => {
    const s = document.getElementById('simJour');
    s.value = String(v);
    s.dispatchEvent(new Event('input', { bubbles: true }));
  }, lum);
  await p.waitForTimeout(60);
}
await regler(80);
ok('11 · plein jour (80 %) : la LED est éteinte',
   (await p.textContent('#simLedTxt')).includes('éteint'), await p.textContent('#simLedTxt'));
await regler(10);
ok('12 · nuit (10 %) sans passage : veille',
   (await p.textContent('#simLedTxt')).includes('veille'), await p.textContent('#simLedTxt'));
await p.click('#btnPassage');
await p.waitForTimeout(80);
ok('13 · nuit + passage : pleine puissance',
   (await p.textContent('#simLedTxt')).includes('PLEINE PUISSANCE'),
   await p.textContent('#simLedTxt'));

const exp = await p.evaluate(() => window.__exp);
ok('14 · les trois situations sont tracées, et seulement par le geste',
   ['jour', 'nuit', 'nuit+passage'].every(k => k in exp), JSON.stringify(exp));

await valider(3);
ok('15 · act. 3 validée (10/10) une fois les expériences réellement faites',
   /10 \/ 10/.test(await retour(3)), (await retour(3)).slice(0, 70));

/* ── activités 4 à 7 ─────────────────────────────────────────────────────── */
await remplir(4);
await p.fill('#e4_6', '2');
await valider(4);
ok('16 · act. 4 descripteurs et lecture de la table validée (7/7)',
   /7 \/ 7/.test(await retour(4)), (await retour(4)).slice(0, 70));

await remplir(5);
await valider(5);
ok('17 · act. 5 réseau local validée (6/6)', /6 \/ 6/.test(await retour(5)),
   (await retour(5)).slice(0, 70));

await remplir(6);
await valider(6);
ok('18 · act. 6 refusée tant que la justification n\'explique pas le conflit',
   /justification/.test(await retour(6)), (await retour(6)).slice(0, 90));
await p.fill('#e6_just',
  'Deux machines de même nom : le réseau ne sait plus à qui livrer, un nom doit être unique.');
await valider(6);
ok('19 · act. 6 jeu du courrier validée (5/5)', /5 \/ 5/.test(await retour(6)),
   (await retour(6)).slice(0, 70));

await remplir(7);
await valider(7);
ok('20 · act. 7 réinvestissement sonnette connectée validée (6/6)',
   /6 \/ 6/.test(await retour(7)), (await retour(7)).slice(0, 70));

/* ── progression, hypothèse, persistance ─────────────────────────────────── */
ok('21 · progression 7 / 7 activités validées',
   (await p.textContent('#progTxt')).includes('7 / 7'), await p.textContent('#progTxt'));
const coches = await p.$$eval('[id^="done-s"]', l => l.map(e => e.textContent.trim()));
ok('22 · les cinq séances portent leur coche', coches.every(c => c === '✔'),
   coches.join('|'));

await p.fill('#hyp1', 'Je pense que le lampadaire s\'allume seulement quand il fait nuit.');
await p.waitForTimeout(120);
ok('23 · l\'hypothèse est rappelée dès la saisie',
   (await p.textContent('#hypRappelTxt')).includes('nuit'),
   await p.textContent('#hypRappelTxt'));

await p.reload({ waitUntil: 'load' });
await p.waitForTimeout(350);
ok('24 · les réponses survivent au rechargement',
   (await p.inputValue('#e5_1')) === ATT[5].e5_1, await p.inputValue('#e5_1'));
ok('25 · les validations survivent au rechargement',
   (await p.textContent('#progTxt')).includes('7 / 7'), await p.textContent('#progTxt'));
ok('26 · les traces d\'expériences survivent au rechargement',
   await p.evaluate(() => ['jour', 'nuit', 'nuit+passage'].every(k => k in (window.__exp || {}))));

/* ── liens locaux et hygiène ─────────────────────────────────────────────── */
const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens
  .filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok('27 · aucun lien local cassé', casses.length === 0, casses.slice(0, 3).join(' · '));

const ids = await p.evaluate(() => [...document.querySelectorAll('[id]')].map(e => e.id));
ok('28 · aucun identifiant HTML en double', ids.length === new Set(ids).size);
ok('29 · aucune boîte modale sur tout le parcours', dlg.length === 0, dlg.join(' | '));
ok('30 · aucune erreur JS après l\'ensemble des interactions', err.length === 0,
   err.slice(0, 2).join(' | '));

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
