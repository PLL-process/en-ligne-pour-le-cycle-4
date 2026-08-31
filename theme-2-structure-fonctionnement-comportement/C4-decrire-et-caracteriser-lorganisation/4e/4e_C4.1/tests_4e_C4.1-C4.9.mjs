/* tests_4e_C4.1-C4.9.mjs — « Le jardin connecté », rejouable.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de ce lot portait 21 coches et les attribuait à `tests_lot09.js`,
 * jamais commité. Il l'avoue depuis le 31/08/2026 ; il lui manquait la suite.
 * C'était le lot en tête de la file publiée par
 * `_outils/controle_rapports_tests.py` (règles d'or n°259 et n°266).
 *
 * CE QUE CETTE SUITE ÉPROUVE EN PROPRE
 * ------------------------------------
 * Ce lot porte **deux verrous expérientiels de natures différentes**, et c'est
 * ce qui le rend intéressant à conduire :
 *
 *   · l'explorateur de table — trois bacs à filtrer, un compteur 3/3, et
 *     l'activité 3 refusée tant que les trois n'ont pas été ouverts ;
 *   · le simulateur réseau — trois pannes à diagnostiquer, où un **mauvais**
 *     diagnostic est refusé sans faire avancer le compteur. La suite se trompe
 *     donc exprès une fois, vérifie le refus, puis répare.
 *
 * Les deux sont éprouvés dans les deux sens : l'activité est d'abord refusée
 * avec toutes les réponses justes, puis validée une fois le geste fait.
 *
 * CE QU'ELLE NE RECOPIE PAS
 * -------------------------
 * Aucune réponse attendue n'est écrite ici : elles sont extraites des fonctions
 * `CHECKS` de la page (convention `att = {id: "valeur"}`), billet d'entrée
 * compris. La bonne cause de chaque panne, et la mauvaise que la suite donne
 * exprès, sont lues dans la table `PANNES` de la page et dans les options
 * réelles du menu déroulant — un pilote de test déclare ce qu'il ne pilote pas
 * (règle d'or n°268).
 *
 * Usage, depuis ce dossier :
 *   node tests_4e_C4.1-C4.9.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence_4e_C4.1-C4.9_jardin_connecte.html');
const QCM = path.join(ICI, 'qcm_4e_C4.1-C4.9_jardin_connecte.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ SÉQUENCE (21 contrôles) ════════════════ */
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
ok('1 · chargement, titre « Le jardin connecté » et les codes du lot en tête',
   /jardin connecté/i.test(await p.title())
   && texte.includes('4e_C4.1') && /4e_C4\.9|C4\.9/.test(texte));

const onglets = await p.$$eval('.seance-tab', l => l.map(e => e.dataset.panel));
await p.click('.seance-tab[data-panel="s4"]'); await p.waitForTimeout(120);
const s4 = await p.$eval('#s4', e => e.classList.contains('active'));
await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(120);
ok(`2 · ${onglets.length} onglets de séance, bascule vers S4 puis retour S1`,
   onglets.length === 4 && s4 && await p.$eval('#s1', e => e.classList.contains('active')),
   onglets.join('|'));

ok('3 · aucune expérience enregistrée au chargement — les deux verrous sont fermés (n°226)',
   Object.keys(await p.evaluate(() => window.__exp || {}))
     .filter(k => k !== 'mode_essentiel').length === 0,
   JSON.stringify(await p.evaluate(() => window.__exp)));

/* ── les réponses attendues, LUES dans la page ───────────────────────────── */
const ATT = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const m = CHECKS[n].toString().match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    out[n] = m ? eval('(' + m[1] + ')') : {};
  }
  return out;
});
const champs = Object.values(ATT).reduce((s, o) => s + Object.keys(o).length, 0);
ok(`4 · ${champs} champs attendus extraits des CHECKS de la page, billet d'entrée compris`,
   Object.keys(ATT).length === 6 && champs >= 30, String(champs));

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
async function remplir(n) {
  for (const [id, v] of Object.entries(ATT[n])) {
    if (!(await ouvrirPour(id))) continue;
    const el = await p.$('#' + id); if (!el) continue;
    if ((await el.evaluate(e => e.tagName)) === 'SELECT') await p.selectOption('#' + id, v);
    else await p.fill('#' + id, v);
  }
}
const valider = async n => {
  await ouvrirPour(Object.keys(ATT[n])[0]);
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(90);
};
const retour = n => p.textContent('#fb' + n);
const valide = n => p.evaluate(k => !!window.__valid[k], String(n));

/* ── le billet d'entrée : il oriente, il ne sanctionne pas ───────────────── */
await p.click('[data-check="0"]'); await p.waitForTimeout(90);
const billetVide = await retour(0);
await remplir(0); await valider(0);
ok('5 · billet d\'entrée : il réclame d\'abord les réponses manquantes, puis rend 3 / 3',
   /restante/i.test(billetVide) && /3 \/ 3/.test(await retour(0)),
   billetVide.slice(0, 45) + ' → ' + (await retour(0)).slice(0, 45));
/* Le billet oriente, il ne sanctionne pas : la page le dit dans son code, et
   la conséquence observable est qu'il n'entre PAS dans les cinq activités. */
ok('5 bis · le billet fait ne compte pas comme une activité validée — la progression reste 0 / 5',
   (await p.textContent('#progTxt')).includes('0 / 5')
   && await p.evaluate(() => !!window.__exp.billet_fait),
   await p.textContent('#progTxt'));

await remplir(1); await valider(1);
ok('6 · activité 1 validée 9 / 9 (chaîne d\'énergie : alimenter, stocker, distribuer, convertir)',
   /9 \/ 9/.test(await retour(1)) && await valide(1), (await retour(1)).slice(0, 60));

await remplir(2); await valider(2);
ok('7 · activité 2 validée 4 / 4 (chaîne d\'information : acquérir, traiter, communiquer, restituer)',
   /4 \/ 4/.test(await retour(2)) && await valide(2), (await retour(2)).slice(0, 60));

/* ── VERROU 1 : l'explorateur de table ───────────────────────────────────── */
await remplir(3); await valider(3);
ok('8 · activité 3 REFUSÉE malgré 6 réponses justes — les trois bacs ne sont pas explorés',
   /6 \/ 6/.test(await retour(3)) && /Explore VRAIMENT les 3 bacs/.test(await retour(3))
   && !(await valide(3)), (await retour(3)).slice(0, 75));

const BACS = await p.$$eval('.bacbtn', l => l.map(e => e.dataset.bac));
await ouvrirPour('bacCompteur');
await p.click(`.bacbtn[data-bac="${BACS[0]}"]`); await p.waitForTimeout(70);
const unBac = await p.textContent('#bacCompteur');
const texteBac = await p.textContent('#bacTxt');
ok(`9 · un bac filtré affiche sa requête et ses mesures, compteur « ${unBac.trim()} »`,
   unBac.includes('1 / 3') && /SELECT|WHERE/.test(texteBac)
   && !(await p.evaluate(() => !!window.__exp.table)), texteBac.slice(0, 60));

for (const bac of BACS.slice(1)) {
  await p.click(`.bacbtn[data-bac="${bac}"]`); await p.waitForTimeout(70);
}
ok(`10 · les ${BACS.length} bacs explorés → compteur 3 / 3 et verrou __exp.table posé`,
   (await p.textContent('#bacCompteur')).includes('3 / 3')
   && await p.evaluate(() => !!window.__exp.table), await p.textContent('#bacCompteur'));

await valider(3);
ok('11 · activité 3 validée 6 / 6 une fois la table réellement explorée',
   /6 \/ 6/.test(await retour(3)) && !/Explore VRAIMENT/.test(await retour(3))
   && await valide(3), (await retour(3)).slice(0, 60));

/* ── VERROU 2 : le simulateur réseau, où l'on se trompe exprès ───────────── */
await remplir(4); await valider(4);
ok('12 · activité 4 REFUSÉE malgré 4 réponses justes — les pannes ne sont pas résolues',
   /4 \/ 4/.test(await retour(4)) && /Résous les 3 pannes/.test(await retour(4))
   && !(await valide(4)), (await retour(4)).slice(0, 75));

/* La bonne cause de chaque panne est lue dans la page ; la mauvaise que l'on
   donne exprès est prise dans les options réelles du menu, jamais écrite ici. */
const CAUSES = await p.evaluate(() => {
  const bonnes = Object.fromEntries(Object.entries(PANNES).map(([k, v]) => [k, v.cause]));
  const offertes = [...document.querySelectorAll('#causeSel option')]
    .map(o => o.value).filter(Boolean);
  return { bonnes, offertes };
});
const pannes = await p.$$eval('.pannebtn', l => l.map(e => e.dataset.panne));
await ouvrirPour('panneEtat');
await p.click(`.pannebtn[data-panne="${pannes[0]}"]`); await p.waitForTimeout(70);
const symptomes = await p.textContent('#panneTxt');
const mauvaise = CAUSES.offertes.find(c => c !== CAUSES.bonnes[pannes[0]]);
await p.selectOption('#causeSel', mauvaise);
await p.click('#btnCause'); await p.waitForTimeout(70);
ok(`13 · un mauvais diagnostic (« ${mauvaise} ») est refusé, et le compteur ne bouge pas`,
   /❌/.test(await p.textContent('#panneTxt'))
   && (await p.textContent('#panneEtat')).includes('0 / 3')
   && !(await p.evaluate(() => !!window.__exp.reseau)),
   (await p.textContent('#panneTxt')).slice(0, 60));
ok('13 bis · les symptômes de la panne sont bien affichés avant le diagnostic',
   /SYMPTÔMES/.test(symptomes), symptomes.slice(0, 60));

for (const panne of pannes) {
  await p.click(`.pannebtn[data-panne="${panne}"]`); await p.waitForTimeout(60);
  await p.selectOption('#causeSel', CAUSES.bonnes[panne]);
  await p.click('#btnCause'); await p.waitForTimeout(60);
}
ok(`14 · les ${pannes.length} pannes réparées → « réseau réparé » et verrou __exp.reseau posé`,
   /3 \/ 3/.test(await p.textContent('#panneEtat'))
   && await p.evaluate(() => !!window.__exp.reseau), await p.textContent('#panneEtat'));

await valider(4);
ok('15 · activité 4 validée 4 / 4 une fois les trois pannes diagnostiquées',
   /4 \/ 4/.test(await retour(4)) && !/Résous les 3 pannes/.test(await retour(4))
   && await valide(4), (await retour(4)).slice(0, 60));

await remplir(5); await valider(5);
ok('16 · activité 5 validée 6 / 6 (forme et procédé : 3D, injection, laser, perçage)',
   /6 \/ 6/.test(await retour(5)) && await valide(5), (await retour(5)).slice(0, 60));

ok('17 · progression 5 / 5 activités, et les quatre onglets portent leur coche',
   (await p.textContent('#progTxt')).includes('5 / 5')
   && (await p.$$eval('[id^="done-s"]', l => l.map(e => e.textContent.trim())))
        .every(c => c === '✔'),
   await p.textContent('#progTxt'));

/* ── persistance ─────────────────────────────────────────────────────────── */
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(340);
const premier = Object.keys(ATT[1])[0];
ok('18 · rechargement : réponses, validations ET les deux verrous sont restaurés',
   (await p.inputValue('#' + premier)) === ATT[1][premier]
   && (await p.textContent('#progTxt')).includes('5 / 5')
   && await p.evaluate(() => !!window.__exp.table && !!window.__exp.reseau),
   await p.textContent('#progTxt'));
ok('18 bis · les compteurs des deux simulateurs repartent à 3 / 3 après rechargement',
   (await p.textContent('#bacCompteur')).includes('3 / 3')
   && (await p.textContent('#panneEtat')).includes('3 / 3'),
   (await p.textContent('#bacCompteur')) + ' · ' + (await p.textContent('#panneEtat')));

const corps = (await p.textContent('body')).replace(/\s+/g, ' ');
ok('19 · les blocs « Prêt·e » et « Bonus » sont là, et un seul bouton mène au QCM',
   /Prêt/i.test(corps) && /Bonus|🎁/i.test(corps)
   && (await p.$$eval('a[href*="qcm_4e_C4.1"]', a => a.filter(x => /btn/.test(x.className)).length))
      === 1);

/* Le bouton du QCM débordait de son bloc dans le gabarit hérité : on mesure. */
const deborde = await p.$$eval('a[href*="qcm"], a[href*="atelier"]', liens => liens
  .filter(a => /btn/.test(a.className))
  .map(a => ({ t: a.textContent.trim().slice(0, 24), d: a.scrollWidth - a.clientWidth })));
ok(`20 · les ${deborde.length} boutons de fin de bilan tiennent dans leur largeur (390 px)`,
   deborde.length > 0 && deborde.every(x => x.d <= 1),
   deborde.map(x => x.t + ':' + x.d).join(' · '));

const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok(`21 · les ${liens.length} liens internes existent, y compris vers 4e_C4.7 et 4e_C6.2`,
   casses.length === 0, casses.slice(0, 3).join(' · '));

const svg = await p.$$eval('img[src$=".svg"], object[data$=".svg"]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('data')));
const svgAbsents = svg.filter(s => !fs.existsSync(path.join(ICI, s)));
ok(`22 · les ${svg.length} SVG référencés existent sur le disque`,
   svgAbsents.length === 0, svgAbsents.join(' · '));

const distantes = await p.$$eval('[src], link[href], object[data], iframe[src]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('href') || e.getAttribute('data'))
        .filter(u => u && /^(https?:)?\/\//i.test(u)));
ok('23 · hors ligne : aucune ressource distante, aucune modale, aucune erreur JS',
   distantes.length === 0 && dlg.length === 0 && fail.length === 0 && err.length === 0,
   (distantes[0] || err[0] || fail[0] || dlg[0] || '').slice(0, 80));
await ctx.close();
}

/* ════════════════ QCM (9 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = []; p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });

await p.goto('file://' + QCM, { waitUntil: 'load' });
await p.waitForTimeout(300);

const Q = await p.evaluate(() => QUESTIONS.map(q => ({
  c: q.c, n: q.n, o: q.o, r: q.r, d: q.d, expl: q.expl, ex: q.ex, err: q.err, ret: q.ret,
  img: q.img ? q.img.src : null })));
const familles = await p.evaluate(() => Object.keys(COMP_LABELS));
const badge = (await p.$eval('.badge.theme', e => e.textContent)).trim();

ok('24 · chargement du QCM, titre « jardin connecté », taille annoncée exacte',
   /jardin connecté/i.test(await p.title()) && badge.includes(String(Q.length))
   && (await p.textContent('#qTot')) === String(Q.length), badge);

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
ok(`25 · 30 questions réparties sur les ${familles.length} familles : `
   + familles.map(f => f + ' ' + (parCode[f] || 0)).join(' · '),
   Q.length === 30 && familles.every(f => parCode[f] > 0)
   && Object.keys(parCode).length === familles.length, JSON.stringify(parCode));

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`26 · bonnes réponses A/B/C/D = ${rep.join('/')} (écart max 1) et d[r] vide partout`,
   Math.max(...rep) - Math.min(...rep) <= 1 && Q.every(q => q.d[q.r] === ''), rep.join('/'));

const illustrees = Q.filter(q => q.img);
const imgAbsentes = illustrees.filter(q => !fs.existsSync(path.join(ICI, q.img)));
ok(`27 · ${illustrees.length} questions illustrées, fichiers présents sur le disque`,
   illustrees.length > 0 && imgAbsentes.length === 0, imgAbsentes.map(q => q.img).join(' · '));

const incomplets = Q.filter(q => !(q.o.length === 4 && q.d.length === 4 && q.expl && q.ex
                                   && q.err && q.ret));
ok('28 · gabarit maison complet : 4 options, 4 réfutations, explication, exemple, erreur, à retenir',
   incomplets.length === 0, incomplets.map(q => q.n).slice(0, 3).join(' · '));

for (let i = 0; i < Q.length; i++) {
  const r = await p.evaluate(() => QUESTIONS[Number(document.getElementById('qNum')
    .textContent) - 1].r);
  const opts = await p.$$('#qOptions .option');
  await opts[r].click();
  await p.click('#btnValider'); await p.waitForTimeout(35);
  if (i < Q.length - 1) { await p.click('#btnSuiv'); await p.waitForTimeout(35); }
}
await p.click('#btnTerminer'); await p.waitForTimeout(220);
const note = (await p.textContent('#rNote')).trim();
const lignes = await p.$$eval('#tblBilan tbody tr',
  l => l.map(t => t.textContent.replace(/\s+/g, ' ').trim()));
ok(`29 · parcours complet 30 / 30 joué question par question → note ${note}, `
   + `bilan sur ${lignes.length} familles`,
   /20,0/.test(note) && (await p.textContent('#rOk')) === String(Q.length)
   && lignes.length === familles.length,
   note + ' · ' + lignes.join(' | ').slice(0, 80));

const cles = await p.evaluate(() => Object.keys(window.localStorage));
ok('30 · la clé localStorage du QCM est écrite',
   cles.some(k => k.includes('qcm_4e_C4.1-C4.9_jardin_connecte')), cles.join(' · '));

const retourSeq = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href'))
  .filter(h => h && /sequence.*\.html$/.test(h)));
ok('31 · le lien de retour vers la séquence existe et pointe sur un fichier réel',
   retourSeq.length > 0
   && retourSeq.every(h => fs.existsSync(path.join(ICI, decodeURIComponent(h)))),
   retourSeq[0] || '');

ok('32 · aucune erreur JS sur le QCM', err.length === 0, err.slice(0, 2).join(' | '));
await ctx.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
