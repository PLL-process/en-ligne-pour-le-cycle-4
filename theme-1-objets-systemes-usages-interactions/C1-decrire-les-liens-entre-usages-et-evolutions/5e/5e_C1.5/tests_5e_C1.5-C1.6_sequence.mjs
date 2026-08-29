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

const E = REP.banc;
const dern = () => p.evaluate(() => {
  const v = document.getElementById('verdict');
  return v.lastElementChild ? v.lastElementChild.textContent : '';
});
const cpt = async () => [parseInt(await p.textContent('#nInd'), 10),
                         parseInt(await p.textContent('#nLoi'), 10)];
const pose = async o => {
  for (const [k, v] of Object.entries(o)) {
    if (k === 'img' || k === 'autor') await p.selectOption('#' + k, v);
    else if (v) await p.check('#el_' + k); else await p.uncheck('#el_' + k);
  }
};

// ── le banc part vide : aucun indice, aucune règle enfreinte ─────────────
ok('le banc part vide', JSON.stringify(await cpt()) === '[0,0]', JSON.stringify(await cpt()));

// ── on charge la publication du club, et on lit ce qu'elle révèle ────────
await p.click('#charger'); await p.waitForTimeout(150);
ok('la publication du club compte ' + E.charge[0] + ' indices',
   (await cpt())[0] === E.charge[0], JSON.stringify(await cpt()));
ok('elle enfreint ' + E.charge[1] + ' règle(s)', (await cpt())[1] === E.charge[1],
   JSON.stringify(await cpt()));
ok('le banc énumère ' + E.deductions + ' constats',
   (await p.$$eval('#revele li', n => n.length)) === E.deductions,
   String(await p.$$eval('#revele li', n => n.length)));
await p.click('#publier'); await p.waitForTimeout(120);
ok('publier est refusé, et le banc dit pourquoi', (await dern()).includes(E.refusPar),
   (await dern()).slice(0, 90));

// ── chaque geste change UN compteur, et le banc le montre ────────────────
for (const c of E.etapes) {
  await pose(c.pose); await p.waitForTimeout(120);
  const v = await cpt();
  ok('« ' + c.titre + ' » → ' + c.attendu.join(' indice(s) / ') + ' règle(s)',
     JSON.stringify(v) === JSON.stringify(c.attendu), JSON.stringify(v));
}
await p.click('#publier'); await p.waitForTimeout(120);
ok('la publication corrigée est acceptée', (await dern()).startsWith('Publié'),
   (await dern()).slice(0, 60));
for (const v of E.verrous)
  ok('verrou « ' + v + ' » ouvert', await p.evaluate(v => !!window.__exp[v], v));

// ── structure ────────────────────────────────────────────────────────────
const duree = await p.$eval('.badge.duree', e => e.textContent.trim());
ok('bandeau de durée présent', /\d+ séances? de \d+ min/.test(duree), duree);
ok('un seul bouton QCM', (await p.$$eval('a.btn[href*="qcm"]', n => n.length)) === 1);
ok('hypothèse d’entrée présente', !!(await p.$('#hyp')));
ok('encadré de règle de la séquence présent', src.includes(REP.securite));
ok('le numéro national est indiqué', src.includes('3018'));
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
ok('la publication survit au rechargement',
   await p.isChecked('#el_jardin'), 'jardin coché');
ok('les verrous survivent au rechargement', await p.evaluate(() => !!window.__exp.publie));

const n0 = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close(); process.exit(n0 === T.length ? 0 : 1);
