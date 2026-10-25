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

// ── les trois séances de 55 min (découpage du 24/10/2026) ──────────────────
ok('bandeau : 3 séances de 55 min', duree.includes('3 séances de 55 min'), duree);
ok('le bandeau de durée a un title et un aria-label',
   await p.$eval('.badge.duree', e => !!e.getAttribute('title') && !!e.getAttribute('aria-label')));
const S = await p.$$eval('section.seance-entete', l => l.map(s => s.id));
ok('trois en-têtes de séance, dans l’ordre', S.join() === 'seance-1,seance-2,seance-3', S.join());
const parSeance = await p.evaluate(() => {
  const out = {}; let cur = null;
  for (const el of document.querySelectorAll('section.card')) {
    if (el.classList.contains('seance-entete')) { cur = el.id; out[cur] = { min: 0, acts: [], clot: [] }; continue; }
    if (!cur) continue;
    const h = el.querySelector('h2'); if (!h) continue;
    const t = h.textContent, m = t.match(/⏱\s*~?\s*(\d+)\s*min/);
    if (m && !/bonus|facultatif/i.test(t)) { out[cur].min += +m[1]; out[cur].acts.push(t.split('—')[0].trim()); }
    if (/bonus/i.test(t)) out[cur].clot.push('Bonus');
    if (/bilan/i.test(t)) out[cur].clot.push('Bilan');
    if (/entraîner/i.test(t)) out[cur].clot.push('QCM');
  }
  return out;
});
for (const [id, m] of Object.entries({ 'seance-1': 45, 'seance-2': 55, 'seance-3': 50 }))
  ok(id + ' : ' + m + ' min d’activités annoncées, au plus 55',
     !!parSeance[id] && parSeance[id].min === m && m <= 55,
     parSeance[id] ? parSeance[id].min + ' min — ' + parSeance[id].acts.join(' + ') : 'absente');
ok('aucune activité avant la séance 1, et 150 min en tout',
   Object.values(parSeance).reduce((s, x) => s + x.min, 0) === 150
   && (await p.evaluate(() => { const s1 = document.getElementById('seance-1');
        return [...document.querySelectorAll('section.card h2')].filter(h => /⏱/.test(h.textContent)
          && (h.compareDocumentPosition(s1) & Node.DOCUMENT_POSITION_FOLLOWING)).length; })) === 0);
ok('clôture à la dernière séance seulement : Bonus → Bilan → QCM',
   !!parSeance['seance-3'] && parSeance['seance-3'].clot.join(' → ') === 'Bonus → Bilan → QCM'
   && !parSeance['seance-1'].clot.length && !parSeance['seance-2'].clot.length,
   parSeance['seance-3'] ? parSeance['seance-3'].clot.join(' → ') : '');
const btns = await p.$$eval('nav.fin-seance a.vers-seance', l => l.map(a => a.getAttribute('href')));
ok('un bouton vers la séance suivante au bas des séances 1 et 2', btns.join() === '#seance-2,#seance-3', btns.join());
const liens = await p.$$eval('.seances-nav a', l => l.map(a => a.getAttribute('href')));
ok('des liens vers les trois séances sous le titre', liens.join() === '#seance-1,#seance-2,#seance-3', liens.join());
ok('chaque lien « banc » mène à un banc qui existe',
   await p.evaluate(() => [...document.querySelectorAll('a[href="#banc"]')].length > 0 && !!document.getElementById('banc')));
await p.setViewportSize({ width: 390, height: 844 });
for (const cible of ['seance-2', 'seance-3']) {
  await p.click(`nav.fin-seance a[href="#${cible}"]`); await p.waitForTimeout(200);
  const top = await p.$eval('#' + cible, e => e.getBoundingClientRect().top);
  ok('à 390 px, le bouton ➡ mène à la séance ' + cible.slice(-1), top >= 0 && top < 160, 'haut à ' + Math.round(top) + ' px');
}
ok('à 390 px, aucun défilement horizontal',
   (await p.evaluate(() => document.documentElement.scrollWidth)) <= 390,
   String(await p.evaluate(() => document.documentElement.scrollWidth)));
await p.setViewportSize({ width: 1280, height: 720 });
await p.evaluate(() => { history.replaceState(null, '', location.pathname); scrollTo(0, 0); });

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

const ANCIENNE = { inputs: { hyp: 'Si l’une des deux tombe, la sirène ne part plus.',
    hors: "déclenche seule, et signale qu'elle est seule", a2regle: 'La sirène part si les deux annoncent au moins 2.',
    a3ph: 'Quand l’autre se tait, la station déclenche et le dit.', reinv: 'À trois, on vote deux sur trois et on affiche la troisième.' },
  checks: { ch0: true, ch1: true, ch2: true, ch3: true, ch4: true, ch5: true }, exp: { msgEssaye: true, msgOk: true, coupe: true } };
// ── une sauvegarde faite avec l'ancien découpage (2 séances de 90 min) se relit ──
// save() n'a pas changé : même clé, mêmes identifiants. On écrit une sauvegarde de
// l'ancienne page, telle que save() la produisait, puis on recharge la page découpée.
{
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
  const q = await ctx.newPage(); const e2 = [];
  q.on('pageerror', e => e2.push(e.message));
  const CLE = (src.match(/const KEY = "([^"]+)"/) || [])[1];
  await q.goto('file://' + f, { waitUntil: 'load' });
  await q.evaluate(([k, v]) => localStorage.setItem(k, v), [CLE, JSON.stringify(ANCIENNE)]);
  await q.reload({ waitUntil: 'load' }); await q.waitForTimeout(300);
  ok('ancienne sauvegarde : la page se recharge sans erreur JS', e2.length === 0, e2.slice(0, 2).join(' | '));
  const relu = {};
  for (const id of Object.keys(ANCIENNE.inputs)) relu[id] = await q.inputValue('#' + id);
  ok('ancienne sauvegarde : chaque réponse revient à sa place, séance 3 comprise',
     Object.entries(ANCIENNE.inputs).every(([k, v]) => relu[k] === v),
     Object.entries(relu).map(([k, v]) => k + '=' + String(v).slice(0, 14)).join(' · '));
  ok('ancienne sauvegarde : l’idée de départ est rappelée au bilan',
     (await q.textContent('#rappelHyp')) === ANCIENNE.inputs.hyp);
  ok('ancienne sauvegarde : les verrous sont conservés',
     await q.evaluate(v => v.every(x => !!window.__exp[x]), Object.keys(ANCIENNE.exp)));
  await ctx.close();
}

const n0 = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close(); process.exit(n0 === T.length ? 0 : 1);
