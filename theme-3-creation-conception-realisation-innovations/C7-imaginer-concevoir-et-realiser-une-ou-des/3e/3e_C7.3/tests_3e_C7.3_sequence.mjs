/* Contrôle d'une séquence C7.3 — le banc des matériaux, les activités, la mémoire.
 *
 * Usage : node test73.mjs <sequence.html> <niveau> <attendus.json>
 *
 * Ce que ce script vérifie que l'œil ne vérifie pas :
 *   · qu'AUCUN verrou expérientiel n'est ouvert à l'ouverture de la page.
 *     Un verrou que l'état initial suffit à ouvrir n'est pas un verrou, et le
 *     boîtier de 3e — zéro matériau retenu tel qu'il est écrit — est exactement
 *     le cas où l'erreur ne se voit pas ;
 *   · que chaque essai du banc donne LE nombre et LES noms attendus, et pas
 *     seulement « un nombre » ;
 *   · qu'une seule instance du banc existe dans la page (ids uniques) ;
 *   · qu'une réponse fausse est refusée, et pas seulement qu'une juste passe.
 */
import { chromium } from 'playwright';
import { readFileSync } from 'fs';

const f = process.argv[2], niveau = process.argv[3];
const REP = JSON.parse(readFileSync(process.argv[4], 'utf8'));
const src = readFileSync(f, 'utf8');

const b = await chromium.launch();
const p = await b.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => fail.push(r.url()));
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });

await p.goto('file://' + f, { waitUntil: 'load' }); await p.waitForTimeout(500);

ok('charge sans erreur JS', err.length === 0, err.slice(0, 2).join(' | '));
ok('aucune requête échouée', fail.length === 0, fail.slice(0, 2).join(' | '));
ok('aucune boîte modale', dlg.length === 0, dlg.slice(0, 2).join(' | '));

// ── les verrous ne s'ouvrent pas tout seuls ──────────────────────────────
const expDepart = await p.evaluate(() => Object.keys(window.__exp || {}).filter(k => window.__exp[k]));
ok('aucun verrou ouvert à l’ouverture de la page', expDepart.length === 0, expDepart.join(','));

// ── un seul banc dans la page ────────────────────────────────────────────
ok('un seul établi dans la page', (await p.$$eval('#etabli', n => n.length)) === 1);
const doublons = await p.evaluate(() => {
  const m = {}, d = [];
  document.querySelectorAll('[id]').forEach(e => { m[e.id] = (m[e.id] || 0) + 1; });
  for (const k in m) if (m[k] > 1) d.push(k + '×' + m[k]);
  return d;
});
ok('aucun identifiant en double', doublons.length === 0, doublons.slice(0, 4).join(' '));

// ── le banc ──────────────────────────────────────────────────────────────
const B = REP.banc;
const etat = () => p.evaluate(() => ({
  nRet: document.getElementById('nRet').textContent,
  nMoins: document.getElementById('nMoins').textContent,
  retenus: [...document.querySelectorAll('#tab tr.ok')].map(tr => tr.cells[0].textContent),
  dernier: document.getElementById('verdict').lastElementChild.textContent,
}));
const regler = async r => {
  for (const [id, v] of Object.entries(r || {})) {
    const el = await p.$('#' + id);
    if (!el) { ok('réglage ' + id + ' possible', false); continue; }
    const type = await el.evaluate(e => e.tagName + ':' + (e.type || ''));
    if (type.endsWith('checkbox')) { if (v) await p.check('#' + id); else await p.uncheck('#' + id); }
    else if (type.startsWith('SELECT')) await p.selectOption('#' + id, String(v));
    else await p.fill('#' + id, String(v));
  }
  await p.waitForTimeout(100);
};

ok('les seuils sont écrits à la française',
  (await p.$$eval('.exig .sv input', n => n.map(e => e.value))).every(v => !v.includes('.')),
  (await p.$$eval('.exig .sv input', n => n.map(e => e.value))).join(' '));

for (const e of B.essais) {
  await p.click('#reinit'); await p.waitForTimeout(100);
  await regler(e.regle);
  await p.click('#evaluer'); await p.waitForTimeout(120);
  const s = await etat();
  ok('« ' + e.titre +' » : ' + e.nRet + ' retenu(s)', s.nRet === e.nRet, 'lu ' + s.nRet);
  ok('« ' + e.titre + ' » : ce sont les bons',
    e.retenus.every(x => s.retenus.some(y => y.includes(x))) && s.retenus.length === e.retenus.length,
    s.retenus.join(' · ').slice(0, 90));
  if (e.moins) ok('« ' + e.titre + ' » : le moins cher est ' + e.moins,
    s.nMoins === e.moins, s.nMoins);
  if (e.verdict) ok('« ' + e.titre + ' » : le verdict le dit',
    s.dernier.includes(e.verdict), s.dernier.slice(0, 80));
  if (e.exp) ok('« ' + e.titre + ' » : le verrou ' + e.exp + ' s’ouvre',
    await p.evaluate(v => !!window.__exp[v], e.exp));
}

// ── structure ────────────────────────────────────────────────────────────
const duree = await p.$eval('.badge.duree', e => e.textContent.trim());
ok('bandeau de durée présent', /\d+ séances? de \d+ min/.test(duree), duree);
ok('le bandeau annonce plus de temps que les activités n’en demandent',
  REP.annonce > REP.activitesMin, REP.annonce + ' contre ' + REP.activitesMin);
ok('un seul bouton QCM', (await p.$$eval('a.btn[href*="qcm"]', n => n.length)) === 1);
ok('hypothèse d’entrée présente', !!(await p.$('#hyp')));
ok('consigne de sécurité d’atelier présente', src.includes(REP.securite));
if (REP.secteur) ok('le secteur est explicitement écarté', /secteur/i.test(src));
ok('les trois versions A/B/C sont annoncées', ['🅰', '🅱', '🅲'].every(x => src.includes(x)));
ok('aucun marqueur de gabarit non remplacé', !/__[A-Z_0-9]+__/.test(src),
  (src.match(/__[A-Z_0-9]+__/g) || []).slice(0, 3).join(' '));
ok('la formulation officielle est recopiée', src.includes(REP.formulation),
  REP.formulation.slice(0, 40));

// ── les activités ────────────────────────────────────────────────────────
for (const [n, champs] of Object.entries(REP.activites)) {
  if (REP.avant && REP.avant[n]) { await p.click('#reinit'); await p.waitForTimeout(100);
    await regler(REP.avant[n]); await p.click('#evaluer'); await p.waitForTimeout(120); }
  for (const [id, val] of Object.entries(champs)) {
    const el = await p.$('#' + id);
    if (!el) { ok('champ ' + id + ' présent', false); continue; }
    const tag = await el.evaluate(e => e.tagName);
    if (tag === 'SELECT') await p.selectOption('#' + id, val); else await p.fill('#' + id, val);
  }
  await p.evaluate(n => document.querySelector('[data-check="' + n + '"]').click(), n);
  const fb = await p.textContent('#fb' + n);
  ok('activité ' + n + ' validée (' + REP.totaux[n] + ')', fb.includes(REP.totaux[n]), fb.slice(0, 80));
}

// ── un verrou fermé refuse, et il le dit ─────────────────────────────────
if (REP.verrou) {
  await p.evaluate(v => { delete window.__exp[v]; }, REP.verrou.exp);
  await p.evaluate(n => document.querySelector('[data-check="' + n + '"]').click(), REP.verrou.act);
  const fb = await p.textContent('#fb' + REP.verrou.act);
  ok('le verrou fermé refuse la validation', fb.startsWith('🔒'), fb.slice(0, 60));
  await p.evaluate(v => { window.__exp[v] = true; }, REP.verrou.exp);
}

// ── une réponse fausse est refusée ───────────────────────────────────────
if (REP.refus) {
  await p.selectOption('#' + REP.refus.id, REP.refus.faux);
  await p.evaluate(n => document.querySelector('[data-check="' + n + '"]').click(), REP.refus.act);
  ok('une réponse fausse est refusée',
    (await p.textContent('#fb' + REP.refus.act)).includes(REP.refus.attendu),
    (await p.textContent('#fb' + REP.refus.act)).slice(0, 45));
  await p.selectOption('#' + REP.refus.id, REP.activites[REP.refus.act][REP.refus.id]);
  await p.evaluate(n => document.querySelector('[data-check="' + n + '"]').click(), REP.refus.act);
}

// ── la mémoire ───────────────────────────────────────────────────────────
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
const [idT, valT] = Object.entries(REP.persistance)[0];
ok('les réponses survivent au rechargement', (await p.inputValue('#' + idT)) === valT,
  idT + ' = ' + (await p.inputValue('#' + idT)));
ok('les seuils du banc survivent au rechargement',
  (await p.inputValue('#sv_' + REP.seuilTemoin[0])) === REP.seuilTemoin[1],
  await p.inputValue('#sv_' + REP.seuilTemoin[0]));
ok('les verrous survivent au rechargement',
  await p.evaluate(v => !!window.__exp[v], B.essais[0].exp || 'evalue'));
ok('le tableau est reconstruit au rechargement',
  (await p.$$eval('#tab tr', n => n.length)) > 1);

// ── les séances de 55 min (décision du 24/10/2026 : une heure par semaine) ──
if (REP.seances) {
  const S = REP.seances;
  ok('le bandeau annonce « ' + S.nombre + ' séances de ' + S.unite + ' min »',
    duree.includes(S.nombre + ' séances de ' + S.unite + ' min'), duree);
  ok('activités + 10 min de service (lancement, transitions, bilan) tiennent dans les séances annoncées',
    S.nombre * S.unite === REP.annonce && REP.activitesMin + 10 <= REP.annonce,
    REP.activitesMin + ' + 10 pour ' + S.nombre + ' × ' + S.unite + ' = ' + S.nombre * S.unite);
  // Les durées de chaque séance, lues à l'écran : en-tête de séance, puis les
  // titres d'activité (⏱ ~N min) jusqu'à l'en-tête suivant, hors Bonus.
  const plan = await p.evaluate(() => {
    const ent = [...document.querySelectorAll('section.seance-entete[id^="seance-"]')];
    const tous = [...document.querySelectorAll('section.seance-entete[id^="seance-"], h2, a.vers-seance, a.btn[href*="qcm"]')];
    return ent.map((e, i) => {
      const deb = tous.indexOf(e), fin = i + 1 < ent.length ? tous.indexOf(ent[i + 1]) : tous.length;
      const morceau = tous.slice(deb + 1, fin);
      const acts = morceau.filter(x => x.tagName === 'H2' && !x.closest('.seance-entete')).map(h => h.textContent.trim());
      const min = acts.filter(t => !/bonus|facultat/i.test(t) && /⏱\s*[~≈]?\s*\d+\s*min/.test(t))
        .map(t => t.match(/⏱\s*[~≈]?\s*(\d+)\s*min/)[1] * 1);
      const vers = morceau.filter(x => x.matches('a.vers-seance')).map(a => a.getAttribute('href'));
      return { id: e.id, titre: e.querySelector('h2').textContent.trim(), min, total: min.reduce((a, b) => a + b, 0),
               vers, bonus: acts.some(t => /bonus/i.test(t)), qcm: morceau.some(x => x.matches('a.btn[href*="qcm"]')) };
    });
  });
  ok(S.nombre + ' en-têtes de séance, dans l’ordre', plan.length === S.nombre &&
    plan.every((s, i) => s.id === 'seance-' + (i + 1)), plan.map(s => s.id).join(' '));
  plan.forEach((s, i) => {
    ok('séance ' + (i + 1) + ' : ' + s.total + ' min d’activités annoncées, au plus ' + S.unite,
      s.total <= S.unite && s.total === S.minutes[i], s.min.join(' + ') + ' = ' + s.total);
    if (i + 1 < plan.length)
      ok('séance ' + (i + 1) + ' : finit par le bouton vers la séance ' + (i + 2),
        s.vers.length === 1 && s.vers[0] === '#seance-' + (i + 2), s.vers.join(' '));
  });
  ok('la somme des séances égale les activités annoncées (' + REP.activitesMin + ' min)',
    plan.reduce((a, s) => a + s.total, 0) === REP.activitesMin);
  const der = plan[plan.length - 1] || {};
  ok('la clôture (Bonus, puis QCM) est dans la dernière séance seulement',
    der.bonus && der.qcm && plan.slice(0, -1).every(s => !s.bonus && !s.qcm));
  const liens = await p.$$eval('nav.seances-liens a', n => n.map(a => a.getAttribute('href')));
  ok('le haut de page mène à chaque séance',
    plan.every(s => liens.includes('#' + s.id)), liens.join(' '));
  // Une activité coupée en deux : la première partie se vérifie seule.
  for (const [n, tot] of Object.entries(REP.parties || {})) {
    await p.evaluate(n => document.querySelector('[data-check="' + n + '"]').click(), n);
    const fb = await p.textContent('#fb' + n);
    ok('activité ' + n + ' (première partie) validée seule (' + tot + ')',
      fb.includes(tot) && fb.includes('Première partie'), fb.slice(0, 60));
  }
  // Une sauvegarde faite avec l'ancien découpage (deux séances de 90 min) se relit.
  const ancienne = REP.ancienneSauvegarde;
  if (ancienne) {
    const e0 = err.length;
    await p.evaluate(([k, v]) => localStorage.setItem(k, JSON.stringify(v)), [ancienne.cle, ancienne.valeur]);
    await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(400);
    const relu = await p.evaluate(ins => Object.entries(ins).every(([id, v]) => {
      const e = document.getElementById(id); return e && e.value === v; }), ancienne.valeur.inputs);
    ok('une sauvegarde de l’ancien découpage se relit sans erreur', relu && err.length === e0,
      err.slice(e0).join(' | '));
  }
  // À 390 px : pas de défilement horizontal, chaque séance atteinte, passage à la suivante.
  const m = await b.newPage({ viewport: { width: 390, height: 844 } });
  const errM = []; m.on('pageerror', e => errM.push(e.message));
  await m.goto('file://' + f, { waitUntil: 'load' }); await m.waitForTimeout(300);
  ok('à 390 px : aucun défilement horizontal',
    !(await m.evaluate(() => document.documentElement.scrollWidth > window.innerWidth)));
  const enVue = id => m.evaluate(id => { const r = document.getElementById(id).getBoundingClientRect();
    return r.top >= -2 && r.top < window.innerHeight / 2; }, id);
  for (let i = 1; i <= S.nombre; i++) {
    await m.click('nav.seances-liens a[href="#seance-' + i + '"]'); await m.waitForTimeout(150);
    ok('à 390 px : le lien du haut atteint la séance ' + i, await enVue('seance-' + i));
  }
  for (let i = 1; i < S.nombre; i++) {
    await m.click('a.vers-seance[href="#seance-' + (i + 1) + '"]'); await m.waitForTimeout(150);
    ok('à 390 px : « ➡ Séance ' + (i + 1) + ' » mène à son en-tête', await enVue('seance-' + (i + 1)));
  }
  await m.goto('file://' + f + '#seance-' + S.nombre, { waitUntil: 'load' }); await m.waitForTimeout(300);
  await m.reload({ waitUntil: 'load' }); await m.waitForTimeout(300);
  ok('à 390 px : après rechargement, la page reste sur la séance ' + S.nombre, await enVue('seance-' + S.nombre));
  ok('à 390 px : zéro erreur JS', errM.length === 0, errM.slice(0, 2).join(' | '));
  await m.close();
}

const n0 = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n0} / ${T.length}`);
await b.close(); process.exit(n0 === T.length ? 0 : 1);
