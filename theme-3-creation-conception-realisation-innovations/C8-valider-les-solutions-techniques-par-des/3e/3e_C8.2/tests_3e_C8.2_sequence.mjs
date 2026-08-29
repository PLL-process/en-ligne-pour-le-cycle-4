import { chromium } from 'playwright';
const f = process.argv[2];
const b = await chromium.launch();
const p = await b.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => fail.push(r.url()));
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });
const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
await p.goto('file://' + f, { waitUntil: 'load' }); await p.waitForTimeout(600);

ok('charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('aucune requête échouée', fail.length === 0);
ok('aucune boîte modale', dlg.length === 0);

const NOMS = ['Tube aluminium Ø50 × 3', 'Barre pleine acier Ø20', 'Tube PVC Ø50 × 3',
  'Poutre bois 40 × 40', 'Tube acier galvanisé Ø33,7 × 2,6'];
const FLEX = [467, 157, 128, 213, 367];
const FLECHE = ['31,0', '161,7', '723,8', '113,6', '41,1'];
const TRAC = [84.2, 125.7, 23.0, 64.0, 101.6];

// ── flèche lue à la charge d'essai de 100 N ────────────────────────────────
await p.selectOption('#prof', NOMS[0]);
await p.click('#pas2'); await p.click('#pas2');
ok('à 100 N, la flèche du tube alu vaut 31,0 mm', (await p.textContent('#dep')) === '31,0',
   await p.textContent('#dep'));
ok('le banc signale la charge d’essai atteinte',
   (await p.textContent('#msg')).includes("Charge d'essai atteinte"));

// ── rupture en flexion, au pied ────────────────────────────────────────────
for (let i = 0; i < 8; i++) await p.click('#pas2');
ok('le tube alu casse au pied', (await p.textContent('#etat')).includes('CASSÉ AU PIED'),
   await p.textContent('#etat'));
ok('la rupture annonce 467 N', (await p.textContent('#msg')).includes('467'),
   (await p.textContent('#msg')).slice(0, 70));

// ── verrou : trois profilés en flexion ─────────────────────────────────────
await p.evaluate(() => document.querySelector('[data-check="0"]').click());
ok('verrou actif tant que 3 profilés ne sont pas cassés en flexion',
   (await p.textContent('#fb0')).includes('🔒'), (await p.textContent('#fb0')).slice(0, 50));

for (let i = 1; i < 5; i++) {
  await p.selectOption('#prof', NOMS[i]);
  for (let k = 0; k < 10; k++) await p.click('#pas2');
}
let exp = await p.evaluate(() => ({ f3: !!window.__exp.flex3, f5: !!window.__exp.flex5 }));
ok('verrou 3 profilés flexion ouvert', exp.f3);
ok('verrou 5 profilés flexion ouvert', exp.f5);

await p.selectOption('#a0q1', 'au ras du socle, là où il est encastré');
await p.selectOption('#a0q2', 'très différentes : il cède des centaines de fois plus tôt en flexion');
await p.evaluate(() => document.querySelector('[data-check="0"]').click());
ok('activité 0 validée 2/2', (await p.textContent('#fb0')).includes('2/2'),
   (await p.textContent('#fb0')).slice(0, 60));

// ── mode traction ──────────────────────────────────────────────────────────
await p.click('#mTrac');
ok('les pas passent en kN', (await p.textContent('#pas2')).includes('kN'),
   await p.textContent('#pas2'));
for (let i = 0; i < 5; i++) {
  await p.selectOption('#prof', NOMS[i]);
  for (let k = 0; k < 6; k++) await p.click('#pas2');
}
exp = await p.evaluate(() => !!window.__exp.trac5);
ok('verrou 5 profilés traction ouvert', exp);

// ── activité 1 ─────────────────────────────────────────────────────────────
for (let i = 0; i < 5; i++) await p.fill('#trac' + i, String(TRAC[i]).replace('.', ','));
await p.selectOption('#a1q1', 'Barre pleine acier Ø20');
await p.selectOption('#a1q2', "non : celui qui gagne en traction n'est que quatrième en flexion");
await p.selectOption('#a1q3', "parce qu'en flexion, ce qui compte est autant la forme que la matière");
await p.fill('#a1ph', "Il mesure la resistance a la traction, mais le mat est pousse de cote : il travaille en flexion.");
await p.evaluate(() => document.querySelector('[data-check="1"]').click());
ok('activité 1 validée 9/9', (await p.textContent('#fb1')).includes('9/9'),
   (await p.textContent('#fb1')).slice(0, 70));
await p.fill('#trac0', '84');
await p.evaluate(() => document.querySelector('[data-check="1"]').click());
ok('un relevé de traction approximatif (84 au lieu de 84,2) est refusé',
   (await p.textContent('#fb1')).includes('8/9'), (await p.textContent('#fb1')).slice(0, 40));
await p.fill('#trac0', '84,2');

// ── activité 2 ─────────────────────────────────────────────────────────────
await p.selectOption('#a2q1', 'le pousser en tête, perpendiculairement, comme le vent');
await p.selectOption('#a2q2', "la flèche en tête sous une charge d'essai commune");
await p.selectOption('#a2q3', 'la hauteur, la fixation au pied et le point d’application de la charge')
  .catch(async () => await p.selectOption('#a2q2', { index: 2 }));
await p.selectOption('#a2q3', "la hauteur, la fixation au pied et le point d'application de la charge");
await p.fill('#a2q4', '300');
await p.fill('#a2q5', '100');
await p.selectOption('#a2q6', 'je retiens un mât seulement s’il tient les DEUX critères')
  .catch(() => {});
await p.selectOption('#a2q6', "je retiens un mât seulement s'il tient les DEUX critères");
await p.fill('#a2proto', `1. Fixer chaque candidat par encastrement, hauteur libre 2000 mm.
2. Pousser horizontalement en tete, par paliers de 10 N.
3. A 100 N, relever la fleche en tete en mm.
4. Continuer et noter la charge de rupture en N.
5. Reprendre un profile neuf pour chaque candidat.
6. Retenir si rupture >= 300 N ET fleche <= 40 mm.`);
await p.evaluate(() => document.querySelector('[data-check="2"]').click());
ok('activité 2 validée 7/7', (await p.textContent('#fb2')).includes('7/7'),
   (await p.textContent('#fb2')).slice(0, 70));
await p.fill('#a2q4', '500');
await p.evaluate(() => document.querySelector('[data-check="2"]').click());
ok('un seuil faux (500 au lieu de 300) est refusé',
   (await p.textContent('#fb2')).includes('6/7'), (await p.textContent('#fb2')).slice(0, 40));
await p.fill('#a2q4', '300');

// ── activité 3 ─────────────────────────────────────────────────────────────
for (let i = 0; i < 5; i++) { await p.fill('#fle' + i, FLECHE[i]); await p.fill('#rup' + i, String(FLEX[i])); }
await p.evaluate(() => document.querySelector('[data-check="3"]').click());
ok('activité 3 validée 10/10', (await p.textContent('#fb3')).includes('10/10'),
   (await p.textContent('#fb3')).slice(0, 70));
await p.fill('#fle4', '41');
await p.evaluate(() => document.querySelector('[data-check="3"]').click());
ok('une flèche arrondie (41 au lieu de 41,1) est refusée',
   (await p.textContent('#fb3')).includes('9/10'), (await p.textContent('#fb3')).slice(0, 40));
await p.fill('#fle4', '41,1');

// ── activité 4 ─────────────────────────────────────────────────────────────
const ANGLES = await p.evaluate(() => {
  const t = {};
  document.querySelectorAll('[id^="a4q"]').forEach(s => {
    t[s.id] = [...s.options].map(o => o.text);
  });
  return t;
});
ok('les cinq listes de l’activité 4 offrent les mêmes 5 angles morts',
   Object.values(ANGLES).every(v => v.length === 6), JSON.stringify(Object.keys(ANGLES)));

// ── durée, QCM, hypothèse ──────────────────────────────────────────────────
const duree = await p.$eval('.badge.duree', e => e.textContent.trim()).catch(() => 'absent');
ok('bandeau de durée présent', duree.includes('2 séances de 90 min'), duree);
const qcm = await p.$$eval('a.btn[href*="qcm"]', n => n.length);
ok('un seul bouton QCM', qcm === 1, String(qcm));
ok('hypothèse d’entrée présente', !!(await p.$('#hyp')));
ok('grille de relecture du binôme présente', (await p.$$('.grille li')).length === 7);
// le tracé du mât doit vraiment bouger quand on charge, et casser au pied
await p.click('#mFlex');
await p.selectOption('#prof', NOMS[3]);
const d0 = await p.getAttribute('#mat', 'd');
await p.click('#pas2'); await p.click('#pas2');
const d1 = await p.getAttribute('#mat', 'd');
ok('le tracé du mât se courbe sous la charge', d0 !== d1, d1);
for (let k = 0; k < 4; k++) await p.click('#pas2');
const d2 = await p.getAttribute('#mat', 'd');
ok('le tracé se rompt au pied (deux tronçons)', (d2.match(/M/g) || []).length === 2, d2);
ok('le point de rupture est marqué', Number(await p.getAttribute('#rupt', 'r')) > 0);
// activité 4 : les cinq angles morts
const A4 = ["Le banc pousse une fois. Le vent fait vibrer le mât des milliers de fois : c'est la fatigue, et elle casse plus bas que l'essai.",
  "Presque 5 kg à hisser sur un toit et à fixer en haut d'une échelle : le banc, lui, ne pèse rien.",
  "Sous le soleil des tropiques, le PVC vieillit et devient cassant : l'essai, lui, est fait sur un tube neuf.",
  "L'humidité : une poutre qui a pris l'eau ne casse plus à la même charge, et le banc essaie du bois sec.",
  "La galvanisation protège tant qu'on ne la perce pas : c'est le trou de fixation, non traité, qui rouille en premier."];
for (let i = 0; i < 5; i++) await p.selectOption('#a4q' + i, A4[i]);
await p.evaluate(() => document.querySelector('[data-check="4"]').click());
ok('activité 4 validée 5/5', (await p.textContent('#fb4')).includes('5/5'),
   (await p.textContent('#fb4')).slice(0, 60));

// ── activité 5 et REFAIRE ──────────────────────────────────────────────────
await p.selectOption('#a5q1', 'deux');
await p.selectOption('#a5q2', 'un seul');
await p.selectOption('#a5q3', "on le refuse en l'état, et mon protocole aurait dû annoncer son incertitude");
await p.fill('#a5avis', "Je recommande le tube aluminium 50x3 : rupture relevee 467 N pour 300 exiges, fleche 31,0 mm pour 40 admis. Mon essai n a pas verifie la fatigue ni l air sale.");
await p.evaluate(() => document.querySelector('[data-check="5"]').click());
ok('activité 5 validée 4/4', (await p.textContent('#fb5')).includes('4/4'),
   (await p.textContent('#fb5')).slice(0, 60));

await p.fill('#reinv', "La ligne 3 passe a 200 N et la ligne 6 exige 600 N : plus aucun candidat ne passe, il faut un profile plus gros ou des haubans.");
await p.evaluate(() => document.querySelector('[data-check="6"]').click());
ok('réinvestissement validé 1/1', (await p.textContent('#fb6')).includes('1/1'),
   (await p.textContent('#fb6')).slice(0, 50));

// ── persistance ────────────────────────────────────────────────────────────
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
ok('les relevés survivent au rechargement', (await p.inputValue('#rup0')) === '467',
   await p.inputValue('#rup0'));
ok('les verrous survivent au rechargement', await p.evaluate(() => !!window.__exp.flex5));

const r = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${r} / ${T.length}`);
await b.close(); process.exit(r === T.length ? 0 : 1);
