import { chromium } from 'playwright';
import { readFileSync } from 'fs';
const f = process.argv[2], niveau = process.argv[3];
const b = await chromium.launch();
const p = await b.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => fail.push(r.url()));
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });
const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const src = readFileSync(f, 'utf8');
await p.goto('file://' + f, { waitUntil: 'load' }); await p.waitForTimeout(500);

ok('charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('aucune requête échouée', fail.length === 0, fail.slice(0, 2).join(' | '));
ok('aucune boîte modale', dlg.length === 0);

const SRC = ['Pile 9 V alcaline', '4 piles AA alcalines', 'Accu Li-ion 18650 rechargeable',
  'Secteur — adaptateur USB scellé', 'Panneau solaire 1 W crête + accu'];

const ATT = {
  '5e': { tot: '2,85', pile: '24 heures', part0: 78.9, nCons: 3, solOk: true },
  '4e': { tot: '5,87', pile: '11 heures', part0: 92.0, nCons: 5, solOk: false },
  '3e': { tot: '6,04', pile: '11 heures', part0: 89.4, nCons: 5, solOk: false },
}[niveau];

// ── le banc calcule ────────────────────────────────────────────────────────
ok('le total du jour est juste', (await p.textContent('#etot')) === ATT.tot + ' Wh',
   await p.textContent('#etot'));
ok('autant de lignes que de consommateurs',
   (await p.$$eval('table.conso tr', n => n.length)) === ATT.nCons + 2,
   String(await p.$$eval('table.conso tr', n => n.length)));

await p.selectOption('#src', SRC[0]);
ok('pile 9 V : énergie stockée 4,95 Wh', (await p.textContent('#sBrute')) === '4,95 Wh',
   await p.textContent('#sBrute'));
ok('pile 9 V : rendement 56 % (5 V ÷ 9 V)', (await p.textContent('#sRend')) === '56 %',
   await p.textContent('#sRend'));
ok('pile 9 V : énergie utile 2,8 Wh', (await p.textContent('#sUtile')) === '2,8 Wh',
   await p.textContent('#sUtile'));
ok('pile 9 V : autonomie annoncée', (await p.textContent('#verdict')).includes(ATT.pile),
   (await p.textContent('#verdict')).slice(0, 70));

await p.selectOption('#src', SRC[1]);
ok('4 AA : rendement 83 % (5 V ÷ 6 V)', (await p.textContent('#sRend')) === '83 %',
   await p.textContent('#sRend'));
await p.selectOption('#src', SRC[2]);
ok('accu : énergie utile 9,4 Wh', (await p.textContent('#sUtile')) === '9,4 Wh',
   await p.textContent('#sUtile'));

await p.selectOption('#src', SRC[3]);
ok('secteur : autonomie illimitée', (await p.textContent('#verdict')).includes('illimitée'),
   (await p.textContent('#verdict')).slice(0, 60));

await p.selectOption('#src', SRC[4]);
const vsol = await p.textContent('#verdict');
ok('panneau : le verdict raisonne en Wh PAR JOUR',
   (await p.textContent('#sUtile')).includes('PAR JOUR'), await p.textContent('#sUtile'));
ok(ATT.solOk ? 'panneau : il suffit à ce montage' : 'panneau 1 W : il ne suffit pas',
   ATT.solOk ? vsol.includes('il suffit') : vsol.includes('NE SUFFIT PAS'), vsol.slice(0, 95));

// ── éteindre un consommateur ──────────────────────────────────────────────
const avant = await p.textContent('#etot');
await p.uncheck('#ck0');
const apres = await p.textContent('#etot');
ok('éteindre la carte fait chuter le total', avant !== apres, avant + ' → ' + apres);
ok('la ligne éteinte est barrée',
   (await p.getAttribute('#tr0', 'class') || '').includes('eteint'));
await p.check('#ck0');
ok('la barre donne la part exacte de la carte',
   Math.abs((await p.$eval('#pt0', e => parseFloat(e.style.width))) - ATT.part0) < 0.15,
   String(await p.$eval('#pt0', e => parseFloat(e.style.width))));

ok('verrou des cinq sources ouvert', await p.evaluate(() => !!window.__exp.srcAll));
ok('verrou « un consommateur éteint » ouvert', await p.evaluate(() => !!window.__exp.eteint));

// ── structure de la page ──────────────────────────────────────────────────
const duree = await p.$eval('.badge.duree', e => e.textContent.trim());
ok('bandeau de durée présent', /\d+ séances? de \d+ min/.test(duree), duree);
ok('un seul bouton QCM', (await p.$$eval('a.btn[href*="qcm"]', n => n.length)) === 1);
ok('hypothèse d’entrée présente', !!(await p.$('#hyp')));
ok('encadré de sécurité TBT présent', src.includes('très basse tension'));
ok('les trois versions A/B/C sont annoncées',
   ['🅰', '🅱', '🅲'].every(x => src.includes(x)));
ok('aucun marqueur de gabarit non remplacé', !/__[A-Z_0-9]+__/.test(src),
   (src.match(/__[A-Z_0-9]+__/g) || []).slice(0, 3).join(' '));

// ── les activités, répondues juste ────────────────────────────────────────
const REP = JSON.parse(readFileSync(process.argv[4], 'utf8'));
// gestes exigés par les verrous expérientiels de ce niveau
for (const id of (REP.prealable || [])) {
  await p.uncheck('#' + id); await p.check('#' + id);
}
if (REP.verrous) for (const v of REP.verrous)
  ok('verrou ' + v + ' ouvert après les gestes exigés',
     await p.evaluate(v => !!window.__exp[v], v));
for (const [n, champs] of Object.entries(REP.activites)) {
  for (const [id, val] of Object.entries(champs)) {
    const el = await p.$('#' + id);
    if (!el) { ok('champ ' + id + ' présent', false); continue; }
    const tag = await el.evaluate(e => e.tagName);
    if (tag === 'SELECT') await p.selectOption('#' + id, val);
    else await p.fill('#' + id, val);
  }
  await p.evaluate(n => document.querySelector('[data-check="' + n + '"]').click(), n);
  const fb = await p.textContent('#fb' + n);
  ok('activité ' + n + ' validée (' + REP.totaux[n] + ')',
     fb.includes(REP.totaux[n]), fb.slice(0, 75));
}

// ── un relevé approximatif est refusé ─────────────────────────────────────
if (REP.refus) {
  await p.fill('#' + REP.refus.id, REP.refus.faux);
  await p.evaluate(n => document.querySelector('[data-check="' + n + '"]').click(), REP.refus.act);
  ok('un relevé approximatif est refusé (' + REP.refus.faux + ')',
     (await p.textContent('#fb' + REP.refus.act)).includes(REP.refus.attendu),
     (await p.textContent('#fb' + REP.refus.act)).slice(0, 45));
  await p.fill('#' + REP.refus.id, REP.refus.juste);
}

// ── persistance ───────────────────────────────────────────────────────────
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
const [idT, valT] = Object.entries(REP.persistance)[0];
ok('les réponses survivent au rechargement',
   (await p.inputValue('#' + idT)) === valT,
   idT + ' = ' + (await p.inputValue('#' + idT)));
ok('les verrous survivent au rechargement', await p.evaluate(() => !!window.__exp.srcAll));

const r0 = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${r0} / ${T.length}`);
await b.close(); process.exit(r0 === T.length ? 0 : 1);
