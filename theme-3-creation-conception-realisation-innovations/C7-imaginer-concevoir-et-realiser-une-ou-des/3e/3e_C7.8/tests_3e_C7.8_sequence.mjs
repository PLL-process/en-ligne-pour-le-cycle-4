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

// ── le message se compose, et le récepteur dit ce qu'il peut en faire ─────
ok('message vide au départ', (await p.textContent('#trame')) === '{}',
   await p.textContent('#trame'));
const lu = async () => (await p.$$eval('#recu li', n => n.map(x => x.className)));
ok('rien n’est lisible avec un message vide', (await lu()).every(c => c === 'non'));

for (const i of REP.banc.partiel) await p.check('#ch' + i);
ok('le message partiel est celui attendu', (await p.textContent('#trame')) === REP.banc.tramePartielle,
   await p.textContent('#trame'));
const l1 = await lu();
ok('certaines lectures restent impossibles', l1.filter(c => c === 'non').length === REP.banc.nonPartiel,
   l1.filter(c => c === 'non').length + ' non');

for (const i of REP.banc.reste) await p.check('#ch' + i);
ok('le message complet est celui attendu', (await p.textContent('#trame')) === REP.banc.trameComplete,
   await p.textContent('#trame'));
ok('tout devient lisible', (await lu()).every(c => c === 'oui'));
ok('verrou du message valide ouvert', await p.evaluate(() => !!window.__exp.msgOk));

// ── un champ piège est signalé, et referme le verrou ─────────────────────
await p.check('#ch' + REP.banc.piege);
const alerte = await p.$$eval('#recu li.alerte', n => n.length);
ok('un champ de trop est signalé au lieu d’être ignoré', alerte === 1, String(alerte));
await p.uncheck('#ch' + REP.banc.piege);

// ── couper le lien : chaque comportement est essayé, et le journal le dit ──
await p.click('#couper');
ok('le canal passe en coupé',
   (await p.getAttribute('#canal', 'class') || '').includes('coupe'));
for (const c of REP.banc.coupures) {
  await p.selectOption('#hors', c.choix);
  for (let k = 0; k < (c.repete || 1); k++) await p.click('#envoyer');
  ok('« ' + c.choix.slice(0, 34) + '… » : le journal dit « ' + c.attendu + ' »',
     (await p.textContent('#journal')).includes(c.attendu),
     (await p.textContent('#journal')).slice(-70));
}
await p.click('#couper');
if (REP.banc.apresRetablissement)
  ok('au rétablissement, ce qui était en attente repart',
     (await p.textContent('#journal')).includes(REP.banc.apresRetablissement),
     (await p.textContent('#journal')).slice(-70));
for (const v of REP.banc.verrous)
  ok('verrou « ' + v + ' » ouvert', await p.evaluate(v => !!window.__exp[v], v));

await p.click('#envoyer');
ok('lien rétabli : le message est reçu',
   (await p.textContent('#journal')).includes('reçu'),
   (await p.textContent('#journal')).slice(-60));

// ── structure ────────────────────────────────────────────────────────────
const duree = await p.$eval('.badge.duree', e => e.textContent.trim());
ok('bandeau de durée présent', /\d+ séances? de \d+ min/.test(duree), duree);
ok('un seul bouton QCM', (await p.$$eval('a.btn[href*="qcm"]', n => n.length)) === 1);
ok('hypothèse d’entrée présente', !!(await p.$('#hyp')));
ok('encadré de sécurité présent', src.includes('donnée personnelle'));
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
}

await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
const [idT, valT] = Object.entries(REP.persistance)[0];
ok('les réponses survivent au rechargement', (await p.inputValue('#' + idT)) === valT,
   idT + ' = ' + (await p.inputValue('#' + idT)));
ok('les verrous survivent au rechargement', await p.evaluate(() => !!window.__exp.msgOk));
ok('les champs cochés survivent au rechargement', await p.isChecked('#ch0'));

const n0 = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close(); process.exit(n0 === T.length ? 0 : 1);
