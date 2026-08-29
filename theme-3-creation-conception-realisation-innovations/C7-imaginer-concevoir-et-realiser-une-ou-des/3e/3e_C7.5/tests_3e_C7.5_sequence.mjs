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
const REP = JSON.parse(readFileSync(process.argv[4], 'utf8'));
await p.goto('file://' + f, { waitUntil: 'load' }); await p.waitForTimeout(500);

ok('charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('aucune requête échouée', fail.length === 0, fail.slice(0, 2).join(' | '));
ok('aucune boîte modale', dlg.length === 0);

const E = REP.etabli;
const pose = async o => { for (const [k, v] of Object.entries(o)) await p.selectOption('#pt_' + k, v); };
const dernier = () => p.evaluate(() => {
  const v = document.getElementById('verdict');
  return v.lastElementChild ? v.lastElementChild.textContent : '';
});

// ── l'établi part vide, et il le dit ─────────────────────────────────────
ok('aucun constituant monté au départ',
   (await p.$$eval('#pt_carte', n => n.map(x => x.value))).every(v => v === ''));
ok('aucune fonction tenue au départ',
   (await p.$$eval('.fct.tenue', n => n.length)) === 0);

// ── le montage juste est accepté, et le verdict est celui attendu ─────────
await pose(E.montageJuste);
ok('les quatre fonctions sont tenues', (await p.$$eval('.fct.tenue', n => n.length)) === 4,
   String(await p.$$eval('.fct.tenue', n => n.length)));
if (E.budget)
  ok('le courant demandé est celui attendu', (await p.textContent('#budget')).includes(E.budget),
     (await p.textContent('#budget')).trim().slice(0, 70));
await p.click('#tester'); await p.waitForTimeout(120);
ok('le montage juste est accepté', (await dernier()).startsWith('✔'), (await dernier()).slice(0, 60));
ok('le verdict décrit le comportement obtenu', (await dernier()).includes(E.verdictOk),
   (await dernier()).slice(0, 80));

// ── chaque erreur reçoit SON diagnostic, pas un message générique ─────────
for (const c of E.erreurs) {
  if (c.cas) { await p.selectOption('#cas', c.cas); await p.waitForTimeout(80); }
  if (c.pose) await pose(c.pose);
  await p.click('#tester'); await p.waitForTimeout(100);
  const v = await dernier();
  ok('« ' + c.titre + ' » : le diagnostic est le bon', v.includes(c.attendu), v.slice(0, 90));
  ok('« ' + c.titre + ' » : le verrou ' + c.diag + ' s’ouvre',
     await p.evaluate(d => !!window.__exp['diag_' + d], c.diag));
}

// ── on remet le montage juste, et les verrous sont tous ouverts ───────────
if (E.remise) { await p.selectOption('#cas', ''); }
await pose(Object.assign({}, E.vide || {}, E.montageJuste));
await p.click('#tester'); await p.waitForTimeout(120);
ok('le montage juste est de nouveau accepté', (await dernier()).startsWith('✔'),
   (await dernier()).slice(0, 50));
for (const v of E.verrous)
  ok('verrou « ' + v + ' » ouvert', await p.evaluate(v => !!window.__exp[v], v));

// ── structure ────────────────────────────────────────────────────────────
const duree = await p.$eval('.badge.duree', e => e.textContent.trim());
ok('bandeau de durée présent', /\d+ séances? de \d+ min/.test(duree), duree);
ok('un seul bouton QCM', (await p.$$eval('a.btn[href*="qcm"]', n => n.length)) === 1);
ok('hypothèse d’entrée présente', !!(await p.$('#hyp')));
ok('consigne de sécurité très basse tension présente', src.includes(REP.securite));
ok('le secteur est explicitement écarté', /secteur/i.test(src));
ok('les trois versions A/B/C sont annoncées', ['🅰', '🅱', '🅲'].every(x => src.includes(x)));
ok('aucun marqueur de gabarit non remplacé', !/__[A-Z_0-9]+__/.test(src),
   (src.match(/__[A-Z_0-9]+__/g) || []).slice(0, 3).join(' '));

// ── les activités ────────────────────────────────────────────────────────
for (const [n, champs] of Object.entries(REP.activites)) {
  for (const [id, val] of Object.entries(champs)) {
    const el = await p.$('#' + id);
    if (!el) { ok('champ ' + id + ' présent', false); continue; }
    const tag = await el.evaluate(e => e.tagName);
    if (tag === 'SELECT') await p.selectOption('#' + id, val); else await p.fill('#' + id, val);
  }
  await p.evaluate(n => document.querySelector('[data-check="' + n + '"]').click(), n);
  const fb = await p.textContent('#fb' + n);
  ok('activité ' + n + ' validée (' + REP.totaux[n] + ')', fb.includes(REP.totaux[n]), fb.slice(0, 75));
}

// ── une réponse fausse est refusée ───────────────────────────────────────
if (REP.refus) {
  await p.selectOption('#' + REP.refus.id, REP.refus.faux);
  await p.evaluate(n => document.querySelector('[data-check="' + n + '"]').click(), REP.refus.act);
  ok('une réponse fausse est refusée',
     (await p.textContent('#fb' + REP.refus.act)).includes(REP.refus.attendu),
     (await p.textContent('#fb' + REP.refus.act)).slice(0, 45));
  await p.selectOption('#' + REP.refus.id, REP.activites[REP.refus.act][REP.refus.id]);
}

await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
const [idT, valT] = Object.entries(REP.persistance)[0];
ok('les réponses survivent au rechargement', (await p.inputValue('#' + idT)) === valT,
   idT + ' = ' + (await p.inputValue('#' + idT)));
ok('le montage survit au rechargement',
   (await p.inputValue('#pt_carte')) === 'SOCLE', await p.inputValue('#pt_carte'));
ok('les verrous survivent au rechargement', await p.evaluate(() => !!window.__exp.ok));

const n0 = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close(); process.exit(n0 === T.length ? 0 : 1);
