/* tests_5e_C8.2_sequence.mjs — la suite qui rejoue les quatorze affirmations du rapport.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de tests du lot annonçait « Séquence 14/14 » dans un tableau écrit
 * À LA MAIN. Quatorze lignes, quatorze coches vertes, et rien pour les rejouer.
 * Le QCM, lui, avait reçu son script le 29/08 — la séquence était restée avec sa
 * liste de bonnes intentions.
 *
 * Un tableau de résultats qu'on ne peut pas relancer ne dit pas « ça marche » :
 * il dit « ça marchait le jour où quelqu'un a regardé ». Ce fichier remplace la
 * parole par le geste — il conduit VRAIMENT le banc d'essai, casse VRAIMENT les
 * éprouvettes, et lit ce que la page affiche.
 *
 * Il ajoute quatre contrôles que le tableau ne faisait pas :
 *   · aucun verrou expérientiel ouvert à l'ouverture de la page (règle n°226) ;
 *   · la formulation officielle du code est recopiée du référentiel, pas de mémoire ;
 *   · la consigne de sécurité et l'écartement du secteur sont là ;
 *   · réponses et verrous survivent au rechargement.
 *
 * Usage, depuis ce dossier :
 *   node tests_5e_C8.2_sequence.mjs sequence_5e_C8.2_patere-du-hall.html
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const f = path.resolve(process.argv[2] || 'sequence_5e_C8.2_patere-du-hall.html');

/* Les charges de rupture du banc, dans l'ordre du relevé. Elles ne sont pas
   recopiées : on les relit dans la page, et on vérifie qu'elles valent bien ce
   que le rapport annonce. */
const ATTENDU = { 'Bois (pin)': 41, 'PLA imprimé en 3D': 51, 'PVC rigide': 53,
                  'Aluminium': 194, 'Acier doux': 408 };

/* La formulation officielle de 5e_C8.2, telle que `_outils/data_competences.py`
   la porte. On la LIT dans le référentiel plutôt que de l'écrire ici : une
   citation recopiée dans un test cesse de tester la citation. */
function formulationOfficielle() {
  const src = fs.readFileSync(
    path.resolve(f, '../../../../../_outils/data_competences.py'), 'utf-8');
  const bloc = src.slice(src.indexOf('COMP_5E'), src.indexOf('COMP_4E'));
  const m = bloc.match(/\("C8\.2",\s*"([^"]+)"/);
  if (!m) throw new Error("C8.2 introuvable dans data_competences.py");
  return m[1];
}

const b = await chromium.launch();
const p = await b.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => fail.push(r.url()));
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });

await p.goto('file://' + f, { waitUntil: 'load' });
await p.waitForTimeout(400);

ok('1 · charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('2 · aucune requête échouée', fail.length === 0, fail.slice(0, 2).join(' | '));

// ── règle d'or n°226 : un verrou ne s'ouvre que par un GESTE ────────────────
const verrousAuChargement = await p.evaluate(
  () => Object.entries(window.__exp || {}).filter(([, v]) => v).map(([k]) => k));
ok('3 · aucun verrou ouvert à l’ouverture (règle n°226)',
   verrousAuChargement.length === 0, verrousAuChargement.join(', '));

// ── le banc, conduit pour de vrai ───────────────────────────────────────────
/** Casse une éprouvette du matériau demandé, par paliers de `pas` kg. */
async function casser(materiau, pas = 50) {
  await p.selectOption('#mat', materiau);
  await p.click('#reset');
  let clics = 0;
  for (let i = 0; i < 60; i++) {
    await p.click(pas === 10 ? '#plus10' : '#plus50');
    clics++;
    if ((await p.textContent('#etat')).includes('CASSÉE')) break;
  }
  return { clics, message: (await p.textContent('#msg')).trim(),
           lecture: Number(await p.textContent('#lect')) };
}

const bois = await casser('Bois (pin)', 10);
ok('4 · le bois casse au 5ᵉ palier de 10 kg', bois.clics === 5, bois.clics + ' palier(s)');
ok('5 · la rupture annonce la bonne charge (41 kg)',
   bois.message.includes('41 kg') && bois.lecture === ATTENDU['Bois (pin)'],
   bois.message.slice(0, 70) + ' · lecture ' + bois.lecture);

// une éprouvette cassée refuse d'être chargée davantage
await p.click('#plus50');
ok('6 · une éprouvette cassée refuse une charge de plus',
   (await p.textContent('#msg')).includes('Nouvelle éprouvette'),
   (await p.textContent('#msg')).slice(0, 60));

// ── le verrou des trois éprouvettes ─────────────────────────────────────────
await p.click('[data-check="0"]'); await p.waitForTimeout(120);
ok('7 · l’activité 0 est refusée tant que trois éprouvettes ne sont pas cassées',
   (await p.textContent('#fb0')).startsWith('🔒'),
   (await p.textContent('#fb0')).slice(0, 72));

await casser('PLA imprimé en 3D');
await casser('PVC rigide');
ok('8 · verrou « 3 éprouvettes » ouvert après trois ruptures',
   await p.evaluate(() => !!window.__exp.banc3));

const casse4 = await casser('Aluminium');
ok('9 · l’aluminium casse à 194 kg', casse4.lecture === ATTENDU['Aluminium'],
   String(casse4.lecture));
const casse5 = await casser('Acier doux');
ok('10 · l’acier casse à 408 kg', casse5.lecture === ATTENDU['Acier doux'],
   String(casse5.lecture));
ok('11 · verrou « 5 éprouvettes » ouvert après cinq ruptures',
   await p.evaluate(() => !!window.__exp.banc5));

// ── activité 2 : le relevé, juste puis faux ────────────────────────────────
const REL = ['rel0', 'rel1', 'rel2', 'rel3', 'rel4'];
const CHARGES = Object.values(ATTENDU);
for (let i = 0; i < 5; i++) await p.fill('#' + REL[i], String(CHARGES[i]));
await p.click('[data-check="2"]'); await p.waitForTimeout(150);
ok('12 · activité 2 validée avec les cinq bons relevés (5/5)',
   (await p.textContent('#fb2')).includes('5/5'),
   (await p.textContent('#fb2')).slice(0, 60));

await p.fill('#rel0', '40');
await p.click('[data-check="2"]'); await p.waitForTimeout(150);
ok('13 · un relevé faux (40 au lieu de 41) est refusé (4/5)',
   (await p.textContent('#fb2')).includes('4/5'),
   (await p.textContent('#fb2')).slice(0, 60));
await p.fill('#rel0', '41');

// ── activité 3 ─────────────────────────────────────────────────────────────
await p.selectOption('#a3q1', '40 kg');
await p.selectOption('#a3q2', 'les cinq');
// l'apostrophe de la page est droite : on sélectionne par l'option réellement
// présente plutôt que par une chaîne recopiée, qui se désynchronise en silence.
await p.selectOption('#a3q3', { label: await p.$eval('#a3q3', s =>
  [...s.options].map(o => o.textContent).find(x => x.startsWith('ça passe tout juste'))) });
await p.fill('#a3rec',
  'On retient le PLA : il tient les 40 kg exigés avec une marge, il s’imprime au '
  + 'collège, et il ne rouille pas dans un hall humide.');
await p.click('[data-check="3"]'); await p.waitForTimeout(150);
ok('14 · activité 3 validée (4/4)', (await p.textContent('#fb3')).includes('4/4'),
   (await p.textContent('#fb3')).slice(0, 60));

// ── ce que le tableau écrit à la main ne vérifiait pas ──────────────────────
const texte = (await p.textContent('body')).replace(/\s+/g, ' ');
const nu = s => s.replace(/[’']/g, "'").replace(/\s+/g, ' ').trim();
ok('15 · la formulation officielle du code est recopiée exactement',
   nu(texte).includes(nu(formulationOfficielle())),
   formulationOfficielle().slice(0, 60));
// Le banc est un simulateur : le risque n'est pas électrique. La consigne doit
// donc dire les DEUX choses — qu'il n'y a pas de secteur, et ce qu'on fait si le
// professeur monte un banc réel. La séquence n'en portait aucune avant ce jour.
ok('16 · la consigne de sécurité est présente et écarte le secteur',
   /simulateur/i.test(texte) && /ni secteur|ni très basse tension/i.test(texte)
   && /à l'arrêt|à l’arrêt/i.test(texte));
ok('17 · bandeau de durée présent', /\b\d{2,3}\s*min\b/.test(texte));
ok('18 · un seul bouton vers le QCM (règle n°4)',
   (await p.$$eval('a[href*="qcm"]', a => a.filter(x => /btn/.test(x.className)).length)) === 1,
   String(await p.$$eval('a[href*="qcm"]', a => a.filter(x => /btn/.test(x.className)).length)));
ok('19 · hypothèse d’entrée présente', (await p.$('#hyp')) !== null);
ok('20 · aucun identifiant HTML en double',
   await p.evaluate(() => {
     const v = [...document.querySelectorAll('[id]')].map(e => e.id);
     return v.length === new Set(v).size;
   }));

// ── la persistance ─────────────────────────────────────────────────────────
await p.fill('#hyp', 'Je pense que l’acier tiendra le plus.');
await p.waitForTimeout(150);
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
ok('21 · les relevés survivent au rechargement',
   (await p.inputValue('#rel4')) === String(ATTENDU['Acier doux']),
   await p.inputValue('#rel4'));
ok('22 · les verrous survivent au rechargement',
   await p.evaluate(() => !!window.__exp.banc3 && !!window.__exp.banc5));
ok('23 · l’hypothèse est rappelée après rechargement',
   (await p.textContent('#rappelHyp')).includes('acier'),
   await p.textContent('#rappelHyp'));

ok('24 · aucune boîte modale sur tout le parcours', dlg.length === 0, dlg.join(' | '));

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
