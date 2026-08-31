/* tests_3e_C5.1-C5.4.mjs — « SOS station : réparer plutôt que jeter », rejouable.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de ce lot portait 18 coches et ne citait **aucun** script : une
 * dette honnête, pas une promesse fausse (règle d'or n°259). C'était le lot en
 * tête de la file publiée par `_outils/controle_rapports_tests.py`.
 *
 * CE QUE CETTE SUITE ÉPROUVE EN PROPRE
 * ------------------------------------
 * Le simulateur de dépannage de ce lot est le plus exigeant du dépôt : il ne
 * demande pas seulement de faire un geste, il fait **payer le mauvais**. Une
 * pièce saine remplacée est refusée (« cet élément était sain ») ET incrémente
 * le compteur de mesures — une réparation inutile coûte cher. La suite se
 * trompe donc exprès, vérifie le refus ET le coût, puis répare les deux pannes
 * successives, dont la seconde s'active toute seule.
 *
 * CE QU'ELLE NE RECOPIE PAS
 * -------------------------
 * Ce lot n'emploie pas la convention `att = {id: "valeur"}` — sauf pour une de
 * ses six activités. Il écrit ses attendus en quatre autres formes, toutes
 * extraites ici du source des `CHECKS` :
 *
 *   · `$("id").value === "valeur"`            (égalité)
 *   · `$("id").value.startsWith("début")`     (préfixe, l'option est retrouvée
 *                                              dans le menu réel de la page)
 *   · `num("id") === N`                       (nombre)
 *   · `att = {id: "valeur"}`                  (l'objet, activité 3)
 *
 * Les relevés du simulateur et le coupable de chaque panne sont lus dans la
 * table `PANNES` de la page (règle d'or n°268).
 *
 * LA PROSE, ET CE QUE CETTE SUITE N'AFFIRME PAS
 * ---------------------------------------------
 * Trois activités demandent une justification rédigée, que la page juge par
 * **mots-clés et longueur**. La suite lit ces contraintes dans le code de la
 * page et compose un texte qui les satisfait — elle vérifie donc que le verrou
 * de rédaction s'ouvre aux conditions déclarées, **pas** que la page sait
 * reconnaître une bonne justification. Elle vérifie aussi l'inverse, qui est
 * la partie utile : un texte trop court, ou sans les mots attendus, est refusé.
 *
 * Usage, depuis ce dossier :
 *   node tests_3e_C5.1-C5.4.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence_3e_C5.1-C5.4_sos_station_reparer.html');
const QCM = path.join(ICI, 'qcm_3e_C5.1-C5.4_sos_station_reparer.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ SÉQUENCE (24 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => { if (!/fonts\.g/.test(r.url())) fail.push(r.url()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

await p.goto('file://' + SEQ, { waitUntil: 'load' });
await p.waitForTimeout(340);

const texte = (await p.textContent('body')).replace(/\s+/g, ' ');
ok('1 · chargement, titre « SOS station » et les quatre codes 3e_C5.1 → C5.4',
   /SOS station/i.test(await p.title())
   && ['3e_C5.1', '3e_C5.2', '3e_C5.3', '3e_C5.4'].every(c => texte.includes(c)));

const onglets = await p.$$eval('.seance-tab', l => l.map(e => e.dataset.panel));
await p.click('.seance-tab[data-panel="s4"]'); await p.waitForTimeout(120);
const s4 = await p.$eval('#s4', e => e.classList.contains('active'));
await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(120);
ok(`2 · ${onglets.length} onglets de séance, bascule vers S4 puis retour S1`,
   onglets.length === 4 && s4, onglets.join('|'));

ok('3 · aucun état de simulateur au chargement — le verrou de l\'activité 4 est fermé',
   (await p.evaluate(() => (window.__sim || {}).resolues || [])).length === 0
   && Object.keys(await p.evaluate(() => window.__exp || {}))
        .filter(k => k !== 'mode_essentiel').length === 0,
   JSON.stringify(await p.evaluate(() => window.__sim)));

/* ── les attendus, LUS dans la page, en quatre conventions ───────────────── */
const PLAN = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const src = CHECKS[n].toString();
    const champs = {};
    const objet = src.match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    if (objet) for (const [id, v] of Object.entries(eval('(' + objet[1] + ')')))
      champs[id] = { mode: 'exact', v };
    for (const m of src.matchAll(/\$\("([\w.]+)"\)\.value\s*===\s*"([^"]*)"/g))
      champs[m[1]] = { mode: 'exact', v: m[2] };
    for (const m of src.matchAll(/\$\("([\w.]+)"\)\.value\.startsWith\("([^"]*)"\)/g))
      champs[m[1]] = { mode: 'prefixe', v: m[2] };
    for (const m of src.matchAll(/num\("([\w.]+)"\)\s*===?\s*(-?\d+(?:\.\d+)?)/g))
      champs[m[1]] = { mode: 'nombre', v: m[2] };
    /* La prose : on relève les mots que la page exige et la longueur qu'elle
       demande, sans interpréter la structure des ET/OU — les contenir TOUS
       satisfait chaque groupe, quelle qu'en soit la forme. */
    const proses = [...new Set([...src.matchAll(/txt\("([\w.]+)"\)/g)].map(m => m[1]))];
    if (proses.length) {
      const mots = [...src.matchAll(/\.includes\("([^"]+)"\)/g)].map(m => m[1]);
      const alt = src.match(/match\(\/([^/]+)\/g\)/);
      if (alt) mots.push(...alt[1].split('|'));
      const longueur = Math.max(0, ...[...src.matchAll(/length\s*>=\s*(\d+)/g)]
        .map(m => Number(m[1])));
      for (const id of proses) champs[id] = { mode: 'prose', mots, longueur };
    }
    out[n] = champs;
  }
  return out;
});
const compte = m => Object.values(PLAN)
  .reduce((s, o) => s + Object.values(o).filter(c => c.mode === m).length, 0);
ok(`4 · attendus extraits des CHECKS : ${compte('exact')} égalités, ${compte('prefixe')} préfixes, `
   + `${compte('nombre')} nombres, ${compte('prose')} rédactions — aucune réponse recopiée ici`,
   Object.keys(PLAN).length === 6
   && compte('exact') + compte('prefixe') + compte('nombre') >= 25 && compte('prose') === 3,
   JSON.stringify(Object.keys(PLAN)));

const ONGLETS = onglets;
async function ouvrirPour(id) {
  if (await p.isVisible('#' + id).catch(() => false)) return true;
  for (const panneau of ONGLETS) {
    await p.click(`.seance-tab[data-panel="${panneau}"]`);
    await p.waitForTimeout(90);
    if (await p.isVisible('#' + id).catch(() => false)) return true;
  }
  return false;
}
/* Une prose fabriquée à partir des mots que la page réclame. Elle n'est pas
   une bonne justification : elle satisfait le critère déclaré, et c'est tout
   ce que la suite prétend montrer. */
const rediger = c => {
  let t = 'Réponse rédigée pour le contrôle : ' + c.mots.join(', ') + '.';
  while (t.length < c.longueur + 5) t += ' On le vérifie ensuite point par point.';
  return t;
};
async function remplir(n, seulement = null) {
  for (const [id, c] of Object.entries(PLAN[n])) {
    if (seulement && !seulement.includes(id)) continue;
    if (!(await ouvrirPour(id))) continue;
    const el = await p.$('#' + id); if (!el) continue;
    const balise = await el.evaluate(e => e.tagName);
    if (c.mode === 'prose') { await p.fill('#' + id, rediger(c)); continue; }
    if (balise !== 'SELECT') { await p.fill('#' + id, String(c.v)); continue; }
    if (c.mode === 'prefixe') {
      const exact = await el.evaluate((e, deb) => [...e.options].map(o => o.value)
        .find(v => v && v.startsWith(deb)), c.v);
      if (exact) await p.selectOption('#' + id, exact);
    } else await p.selectOption('#' + id, String(c.v));
  }
}
const valider = async n => {
  await ouvrirPour(Object.keys(PLAN[n])[0]);
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(90);
};
const retour = n => p.textContent('#fb' + n);
const valide = n => p.evaluate(k => !!window.__valid[k], String(n));

await remplir(1); await valider(1);
ok('5 · activité 1 validée 7 / 7 (symptôme ou hypothèse, et les trois pistes classées)',
   /7 \/ 7/.test(await retour(1)) && await valide(1), (await retour(1)).slice(0, 60));

/* ── le verrou de rédaction, éprouvé dans les deux sens ──────────────────── */
const prose2 = Object.entries(PLAN[2]).find(([, c]) => c.mode === 'prose')[0];
await remplir(2, Object.keys(PLAN[2]).filter(i => i !== prose2));
await ouvrirPour(prose2);
await p.fill('#' + prose2, 'Parce que oui.');
await valider(2);
ok('6 · activité 2 REFUSÉE avec les 3 parcours justes mais une justification trop courte',
   /3 \/ 3/.test(await retour(2)) && /justification/i.test(await retour(2))
   && !(await valide(2)), (await retour(2)).slice(0, 75));

await remplir(2); await valider(2);
ok('7 · activité 2 validée 3 / 3 une fois la justification aux conditions déclarées',
   /3 \/ 3/.test(await retour(2)) && await valide(2), (await retour(2)).slice(0, 60));

await remplir(3); await valider(3);
ok('8 · activité 3 validée 9 / 9 (protocole ordonné, règle de localisation, sécurité)',
   /9 \/ 9/.test(await retour(3)) && await valide(3), (await retour(3)).slice(0, 60));

/* ── LE SIMULATEUR DE DÉPANNAGE ──────────────────────────────────────────── */
const SIM = await p.evaluate(() => PANNES.map(x => ({ nom: x.nom, coupable: x.coupable,
  mesures: x.mesures })));
await remplir(4); await valider(4);
ok('9 · activité 4 REFUSÉE malgré les 2 réponses justes — les pannes ne sont pas résolues',
   /2 \/ 2/.test(await retour(4)) && /Résous d'abord les DEUX pannes/.test(await retour(4))
   && !(await valide(4)), (await retour(4)).slice(0, 75));

await ouvrirPour('simPanneNum');
await p.click('#btnTestSirene'); await p.waitForTimeout(80);
ok(`10 · le test sirène constate le symptôme, panne ${SIM[0].nom} active`,
   /ne sonne pas/i.test(await p.textContent('#simEtatSirene'))
   && (await p.textContent('#simPanneNum')).includes(SIM[0].nom),
   (await p.textContent('#simEtatSirene')).slice(0, 60));

const points = await p.$$eval('#zoneMesures [data-mesure]', l => l.map(e => e.dataset.mesure));
for (const t of points) { await p.click(`[data-mesure="${t}"]`); await p.waitForTimeout(45); }
const releves = await p.textContent('#simReleves');
ok(`11 · les ${points.length} points ${points.join('→')} mesurés dans l'ordre affichent les relevés de la page`,
   points.every(t => releves.includes(t + ' = ' + SIM[0].mesures[t]))
   && (await p.textContent('#simNbMesures')) === String(points.length),
   releves.slice(9, 75));

/* On se trompe exprès : une pièce saine, choisie hors de la table PANNES. */
const options = await p.$$eval('#simDiag option', l => l.map(o => o.value).filter(Boolean));
const saine = options.find(o => !SIM.some(x => x.coupable === o));
await p.selectOption('#simDiag', saine);
await p.click('#btnRemplacer'); await p.waitForTimeout(80);
ok(`12 · remplacer une pièce saine (« ${saine} ») est refusé : « cet élément était sain »`,
   /était sain/.test(await p.textContent('#simVerdict'))
   && (await p.evaluate(() => window.__sim.resolues.length)) === 0,
   (await p.textContent('#simVerdict')).slice(0, 70));
ok(`13 · et la réparation inutile COÛTE : le compteur passe de ${points.length} à `
   + `${await p.textContent('#simNbMesures')}`,
   Number(await p.textContent('#simNbMesures')) === points.length + 1,
   await p.textContent('#simNbMesures'));

await p.selectOption('#simDiag', SIM[0].coupable);
await p.click('#btnRemplacer'); await p.waitForTimeout(80);
ok(`14 · la bonne pièce (« ${SIM[0].coupable} ») réparée → la panne ${SIM[1].nom} s'active seule`,
   /NOUVELLE panne/.test(await p.textContent('#simVerdict'))
   && (await p.textContent('#simPanneNum')).includes(SIM[1].nom)
   && (await p.evaluate(() => window.__sim.resolues.length)) === 1,
   (await p.textContent('#simVerdict')).slice(0, 60));

/* Panne 2 : deux mesures suffisent, et la page le dit dans ses propres relevés. */
const anormal = points.find(t => /ANORMAL/.test(SIM[1].mesures[t]));
const assez = points.slice(0, points.indexOf(anormal) + 1);
for (const t of assez) { await p.click(`[data-mesure="${t}"]`); await p.waitForTimeout(45); }
await p.selectOption('#simDiag', SIM[1].coupable);
await p.click('#btnRemplacer'); await p.waitForTimeout(80);
ok(`15 · panne ${SIM[1].nom} localisée en ${assez.length} mesures (${assez.join('→')}, `
   + `premier relevé anormal) et réparée`,
   /2 pannes sont résolues/.test(await p.textContent('#simVerdict'))
   && (await p.evaluate(() => window.__sim.resolues.length)) === 2,
   (await p.textContent('#simVerdict')).slice(0, 60));

await p.click('#btnTestSirene'); await p.waitForTimeout(80);
ok('16 · le retest final déclare la sirène opérationnelle',
   /SIRÈNE OPÉRATIONNELLE/.test(await p.textContent('#simEtatSirene')),
   (await p.textContent('#simEtatSirene')).slice(0, 60));

await valider(4);
ok('17 · activité 4 validée 2 / 2 une fois les deux pannes réellement résolues',
   /2 \/ 2/.test(await retour(4)) && !/Résous d'abord/.test(await retour(4))
   && await valide(4), (await retour(4)).slice(0, 60));

await remplir(5); await valider(5);
ok('18 · activité 5 validée 8 / 8 (plan coté lu et procédés de fabrication)',
   /8 \/ 8/.test(await retour(5)) && await valide(5), (await retour(5)).slice(0, 60));

await remplir(6); await valider(6);
ok('19 · activité 6 validée 5 / 5 (réparer ou jeter : la décision pèse deux critères)',
   /5 \/ 5/.test(await retour(6)) && await valide(6), (await retour(6)).slice(0, 60));

ok('20 · progression 6 / 6 activités, et les quatre onglets portent leur coche',
   (await p.textContent('#progTxt')).includes('6 / 6')
   && (await p.$$eval('[id^="done-s"]', l => l.map(e => e.textContent.trim())))
        .every(c => c === '✔'),
   await p.textContent('#progTxt'));

/* ── persistance ─────────────────────────────────────────────────────────── */
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(340);
ok('21 · rechargement : réponses, validations ET l\'état du simulateur sont restaurés',
   (await p.inputValue('#c1_1')).startsWith(PLAN[1].c1_1.v)
   && (await p.textContent('#progTxt')).includes('6 / 6')
   && (await p.evaluate(() => window.__sim.resolues.length)) === 2,
   await p.textContent('#progTxt'));

const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok(`22 · les ${liens.length} liens internes existent`, casses.length === 0,
   casses.slice(0, 3).join(' · '));

const svg = await p.$$eval('img[src$=".svg"], object[data$=".svg"]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('data')));
const svgAbsents = svg.filter(s => !fs.existsSync(path.join(ICI, s)));
ok(`23 · les ${svg.length} SVG référencés existent sur le disque`,
   svg.length === 5 && svgAbsents.length === 0, svgAbsents.join(' · '));

const distantes = await p.$$eval('[src], link[href], object[data], iframe[src]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('href') || e.getAttribute('data'))
        .filter(u => u && /^(https?:)?\/\//i.test(u)));
ok('24 · hors ligne : aucune ressource distante, aucune modale, aucune erreur JS',
   distantes.length === 0 && dlg.length === 0 && fail.length === 0 && err.length === 0,
   (distantes[0] || err[0] || fail[0] || dlg[0] || '').slice(0, 80));
await ctx.close();
}

/* ════════════════ QCM (10 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = []; p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });

await p.goto('file://' + QCM, { waitUntil: 'load' });
await p.waitForTimeout(300);

const Q = await p.evaluate(() => QUESTIONS.map(q => ({
  c: q.c, n: q.n, o: q.o, r: q.r, d: q.d, expl: q.expl, ex: q.ex, err: q.err, ret: q.ret,
  img: q.img ? q.img.src : null, alt: q.img ? q.img.alt : null })));
const codes = await p.evaluate(() => Object.keys(COMP_LABELS));
const badge = (await p.$eval('.badge.theme', e => e.textContent)).trim();

ok('25 · chargement du QCM, titre « SOS station », taille annoncée exacte',
   /SOS station/i.test(await p.title()) && badge.includes(String(Q.length))
   && (await p.textContent('#qTot')) === String(Q.length), badge);

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
ok(`26 · ${Q.length} questions, ${codes.length} compétences : `
   + codes.map(c => c + ' ' + (parCode[c] || 0)).join(' · '),
   Q.length === 32 && codes.length === 4
   && codes.every(c => parCode[c] === 8), JSON.stringify(parCode));

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`27 · bonnes réponses A/B/C/D = ${rep.join('/')} et d[r] vide partout`,
   Math.max(...rep) - Math.min(...rep) <= 1 && Q.every(q => q.d[q.r] === ''), rep.join('/'));

const illustrees = Q.filter(q => q.img);
const imgAbsentes = illustrees.filter(q => !fs.existsSync(path.join(ICI, q.img)));
const sansAlt = illustrees.filter(q => !q.alt || q.alt.length < 10);
ok(`28 · ${illustrees.length} questions illustrées : fichiers présents, alt renseigné partout`,
   illustrees.length === 10 && imgAbsentes.length === 0 && sansAlt.length === 0,
   imgAbsentes.concat(sansAlt).map(q => q.n).slice(0, 3).join(' · '));

const incomplets = Q.filter(q => !(q.o.length === 4 && q.d.length === 4 && q.expl && q.ex
                                   && q.err && q.ret));
ok('29 · gabarit maison complet : 4 options, 4 réfutations, explication, exemple, erreur, à retenir',
   incomplets.length === 0, incomplets.map(q => q.n).slice(0, 3).join(' · '));

/* Le moteur étendu de ce lot : la zone figure doit suivre la question. */
const premiereAvec = Q.findIndex(q => q.img);
const premiereSans = Q.findIndex(q => !q.img);
const figureA = async i => {
  await p.evaluate(n => { etat.courante = n; rendreTout(); }, i);
  await p.waitForTimeout(70);
  return p.$eval('#qFigure', e => e.hidden || getComputedStyle(e).display === 'none');
};
const cacheeSans = await figureA(premiereSans);
const cacheeAvec = await figureA(premiereAvec);
ok(`30 · zone figure masquée sur une question sans image (n°${premiereSans + 1}), `
   + `visible sur une question illustrée (n°${premiereAvec + 1})`,
   cacheeSans === true && cacheeAvec === false,
   `sans:${cacheeSans} avec:${cacheeAvec}`);

await p.evaluate(() => { etat.courante = 0; rendreTout(); }); await p.waitForTimeout(70);
for (let i = 0; i < Q.length; i++) {
  const r = await p.evaluate(() => QUESTIONS[Number(document.getElementById('qNum')
    .textContent) - 1].r);
  const opts = await p.$$('#qOptions .option');
  await opts[r].click();
  await p.click('#btnValider'); await p.waitForTimeout(30);
  if (i < Q.length - 1) { await p.click('#btnSuiv'); await p.waitForTimeout(30); }
}
await p.click('#btnTerminer'); await p.waitForTimeout(220);
const note = (await p.textContent('#rNote')).trim();
const lignes = await p.$$eval('#tblBilan tbody tr',
  l => l.map(t => t.textContent.replace(/\s+/g, ' ').trim()));
ok(`31 · parcours complet ${Q.length} / ${Q.length} joué question par question → note ${note}, `
   + `bilan sur ${lignes.length} compétences`,
   /20,0/.test(note) && (await p.textContent('#rOk')) === String(Q.length)
   && lignes.length === 4 && lignes.every(l => /8 \/ 8/.test(l)),
   note + ' · ' + lignes.join(' | ').slice(0, 70));

const cles = await p.evaluate(() => Object.keys(window.localStorage));
ok('32 · la clé localStorage du QCM est écrite',
   cles.some(k => k.includes('qcm_3e_C5.1-C5.4_sos_station')), cles.join(' · '));

const retourSeq = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href'))
  .filter(h => h && /sequence.*\.html$/.test(h)));
ok('33 · le lien de retour vers la séquence existe et pointe sur un fichier réel',
   retourSeq.length > 0
   && retourSeq.every(h => fs.existsSync(path.join(ICI, decodeURIComponent(h)))),
   retourSeq[0] || '');

ok('34 · aucune erreur JS sur le QCM', err.length === 0, err.slice(0, 2).join(' | '));
await ctx.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
