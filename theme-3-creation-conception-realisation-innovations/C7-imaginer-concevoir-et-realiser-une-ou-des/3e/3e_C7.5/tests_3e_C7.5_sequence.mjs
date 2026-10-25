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
// 24/10/2026 : « chaque séance a 55 min » (décision de Pascal) — la page passe de
// 2 séances de 90 min à 4 séances de 55 min. Elle défile d'un seul tenant (pas
// d'onglets) : un en-tête .seance-entete#seance-N ouvre chaque séance, un bouton
// .vers-seance la termine, la clôture suit la dernière.
const SEANCES = 4;
const duree = await p.$eval('.badge.duree', e => e.textContent.trim());
ok('bandeau de durée : ' + SEANCES + ' séances de 55 min', duree.includes(SEANCES + ' séances de 55 min'), duree);
const parSeance = await p.evaluate(() => {
  const ent = [...document.querySelectorAll(".seance-entete[id^='seance-']")];
  return ent.map((h, i) => {
    const r = document.createRange();
    r.setStartAfter(h);
    if (ent[i + 1]) r.setEndBefore(ent[i + 1]); else r.setEndAfter(document.querySelector('footer'));
    let min = 0; const act = [];
    r.cloneContents().querySelectorAll('h2').forEach(t => {
      const s = t.textContent;
      if (/bonus|facultatif/i.test(s)) return;
      const m = s.match(/~\s*(\d+)\s*min/);
      if (m) { min += parseInt(m[1], 10); act.push((s.match(/Activité \d+[ab]?|REFAIRE/) || ['?'])[0]); }
    });
    return { id: h.id, min, act };
  });
});
ok(SEANCES + ' en-têtes de séance, dans l’ordre',
   parSeance.length === SEANCES && parSeance.every((s, i) => s.id === 'seance-' + (i + 1)),
   parSeance.map(s => s.id).join(', '));
ok('chaque séance tient dans ses 55 min d’activités annoncées',
   parSeance.length === SEANCES && parSeance.every(s => s.min > 0 && s.min <= 55),
   parSeance.map(s => s.id + ' = ' + s.min + ' min').join(' · '));
ok('le temps total des activités est conservé (150 min)',
   parSeance.reduce((a, s) => a + s.min, 0) === 150, String(parSeance.reduce((a, s) => a + s.min, 0)));
ok('chaque activité est dans sa séance (0 | 1 | 2, 3 | 4, REFAIRE)',
   parSeance.map(s => s.act.join('+')).join(' | ') ===
   'Activité 0 | Activité 1 | Activité 2+Activité 3 | Activité 4+REFAIRE',
   parSeance.map(s => s.act.join('+')).join(' | '));
const ordre = await p.evaluate(() => {
  const pos = el => el ? [...document.querySelectorAll('*')].indexOf(el) : -1;
  const h2 = re => [...document.querySelectorAll('h2')].find(h => re.test(h.textContent));
  return { s4: pos(document.getElementById('seance-4')), refaire: pos(h2(/REFAIRE/)),
           synthese: pos(h2(/Synthèse/)), bonus: pos(h2(/Bonus/)), bilan: pos(h2(/bilan personnel/)),
           qcm: pos(h2(/Prêt·e à t.entraîner/)) };
});
ok('la clôture suit la dernière séance : synthèse → Bonus → Bilan → QCM',
   ordre.s4 < ordre.refaire && ordre.refaire < ordre.synthese && ordre.synthese < ordre.bonus
   && ordre.bonus < ordre.bilan && ordre.bilan < ordre.qcm, JSON.stringify(ordre));
const liens = await p.$$eval('nav.fin-seance a.vers-seance', a => a.map(x => x.getAttribute('href')));
ok('chaque séance (sauf la dernière) mène explicitement à la suivante',
   liens.join(',') === '#seance-2,#seance-3,#seance-4', liens.join(', '));
const nav = await p.$$eval('nav.seances-nav a', a => a.map(x => x.getAttribute('href')));
ok('le haut de page mène à chacune des séances',
   nav.join(',') === '#seance-1,#seance-2,#seance-3,#seance-4', nav.join(', '));
for (const cible of ['#seance-2', '#seance-3', '#seance-4']) {
  await p.click('nav.fin-seance a[href="' + cible + '"]'); await p.waitForTimeout(250);
  const top = await p.evaluate(s => document.querySelector(s).getBoundingClientRect().top, cible);
  ok('le bouton « ' + cible.replace('#seance-', 'Séance ') + ' » amène à son en-tête, sous la barre du haut',
     top >= 0 && top < 140, Math.round(top) + ' px');
}
await p.evaluate(() => window.scrollTo(0, 0));
ok('la séance 3 (montage) renvoie à l’encadré de sécurité',
   await p.$eval('#seance-3', e => !!e.querySelector('a[href="#securite"]')) && !!(await p.$('#securite')));
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

// ── une sauvegarde faite avec l'ancien découpage (2 séances de 90 min) se relit ──
// Même clé, même forme {inputs, checks, exp} : le découpage n'a ajouté ni retiré
// aucun champ. Forme relevée sur une sauvegarde réelle de la page d'avant le
// 24/10/2026 (34 champs, réduits ici à cinq).
const err0 = err.length;
await p.evaluate(() => localStorage.setItem('seq_3e_C7_5', JSON.stringify({
  inputs: { hyp: 'Je partirais du cahier des charges.', a0r0: "elle impose l'anémomètre : c'est la seule grandeur du cahier des charges",
            pt_carte: 'SOCLE', pt_anemo: 'A0', reinv: '' },
  checks: {}, exp: { monte: true, teste: true, ok: true } })));
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
ok('une sauvegarde de l’ancien découpage se relit sans erreur',
   err.length === err0 && (await p.inputValue('#a0r0')).startsWith("elle impose l'anémomètre")
   && (await p.inputValue('#pt_anemo')) === 'A0' && (await p.textContent('#rappelHyp')).includes('cahier des charges'),
   err.slice(err0).join(' | ') || (await p.inputValue('#pt_anemo')));

const n0 = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close(); process.exit(n0 === T.length ? 0 : 1);
