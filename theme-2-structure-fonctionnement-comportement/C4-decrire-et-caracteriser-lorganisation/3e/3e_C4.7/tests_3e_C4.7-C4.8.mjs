/* tests_3e_C4.7-C4.8.mjs — « Internet jusqu'à Sainte-Luce », rejouable.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de ce lot portait 17 coches et ne citait aucun script : une dette
 * honnête (règle d'or n°259). C'était le lot en tête de la file publiée par
 * `_outils/controle_rapports_tests.py`.
 *
 * CE QUE CETTE SUITE ÉPROUVE EN PROPRE
 * ------------------------------------
 * Ce lot porte deux simulateurs qui ne se ressemblent pas :
 *
 *   · le **découpage en paquets** — le message de l'élève est coupé en trois,
 *     les paquets arrivent dans le désordre, et il faut les remettre en place.
 *     Le verrou ne s'ouvre que si le réassemblage est JUSTE : la suite se
 *     trompe d'abord d'ordre, vérifie le refus, puis remet dans l'ordre ;
 *   · le **réseau maillé** — cinq routeurs, un plus court chemin calculé par
 *     un parcours en largeur, des liaisons qu'on coupe au clic. La suite lit le
 *     graphe dans la page, coupe une liaison **du chemin réellement emprunté**,
 *     et vérifie que le réseau en trouve un autre. Puis elle isole R5 et
 *     vérifie la livraison impossible.
 *
 * Rien de tout cela n'est écrit ici : ni le chemin initial, ni le chemin de
 * secours, ni les liaisons à couper. Le graphe est lu dans la page, les chemins
 * sont ceux qu'elle annonce, et les liaisons à couper s'en déduisent. Le
 * rapport d'origine notait déjà qu'un chemin écrit à la main dans la correction
 * était faux : un chemin recopié dans un test aurait le même sort.
 *
 * Usage, depuis ce dossier :
 *   node tests_3e_C4.7-C4.8.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence_3e_C4.7-C4.8_internet_sainte_luce.html');
const QCM = path.join(ICI, 'qcm_3e_C4.7-C4.8_internet_sainte_luce.html');

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
ok('1 · chargement, titre « Internet jusqu\'à Sainte-Luce » et les codes 3e_C4.7 / 3e_C4.8',
   /Sainte-Luce/i.test(await p.title())
   && texte.includes('3e_C4.7') && texte.includes('3e_C4.8'));

const onglets = await p.$$eval('.seance-tab', l => l.map(e => e.dataset.panel));
await p.click('.seance-tab[data-panel="s3"]'); await p.waitForTimeout(120);
const s3 = await p.$eval('#s3', e => e.classList.contains('active'));
await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(120);
ok(`2 · ${onglets.length} onglets de séance, bascule vers S3 puis retour S1`, onglets.length === 3
   && s3, onglets.join('|'));

ok('3 · aucun verrou ouvert au chargement : ni le réassemblage, ni le re-routage (n°226)',
   !(await p.evaluate(() => window.__simOk))
   && !(await p.evaluate(() => window.__rerouteVu))
   && (await p.evaluate(() => (window.__coupees || []).length)) === 0,
   JSON.stringify(await p.evaluate(() =>
     ({ simOk: window.__simOk, reroute: window.__rerouteVu, coupees: window.__coupees }))));

/* ── les attendus, LUS dans la page ─────────────────────────────────────── */
const PLAN = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const src = CHECKS[n].toString();
    const champs = {};
    const objet = src.match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    if (objet) for (const [id, v] of Object.entries(eval('(' + objet[1] + ')')))
      champs[id] = { mode: 'exact', v };
    for (const m of src.matchAll(/\$\("([\w.]+)"\)\.value\s*===\s*"((?:\\.|[^"])*)"/g))
      champs[m[1]] = { mode: 'exact', v: m[2] };
    for (const m of src.matchAll(/\$\("([\w.]+)"\)\.value\.startsWith\("((?:\\.|[^"])*)"\)/g))
      champs[m[1]] = { mode: 'prefixe', v: m[2] };
    for (const m of src.matchAll(/num\("([\w.]+)"\)\s*===?\s*(-?\d+(?:\.\d+)?)/g))
      champs[m[1]] = { mode: 'nombre', v: m[2] };
    const proses = [...new Set([...src.matchAll(/txt\("([\w.]+)"\)/g)].map(m => m[1]))];
    if (proses.length) {
      const mots = [...src.matchAll(/\.includes\("([^"]+)"\)/g)].map(m => m[1]);
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
   + `${compte('nombre')} nombre, ${compte('prose')} rédactions — rien n'est recopié ici`,
   Object.keys(PLAN).length === 6 && compte('exact') >= 18 && compte('prefixe') >= 6
   && compte('prose') === 4, Object.keys(PLAN).join(','));

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
  await p.click(`[data-check="${n}"]`); await p.waitForTimeout(100);
};
const retour = n => p.textContent('#fb' + n);
const valide = n => p.evaluate(k => !!window.__valid[k], String(n));

await remplir(1); await valider(1);
ok('5 · activité 1 validée 6 / 6 (terminaux, switch, routeur, adresse IP)',
   /6 \/ 6/.test(await retour(1)) && await valide(1), (await retour(1)).slice(0, 60));

await remplir(2); await valider(2);
ok('6 · activité 2 validée 7 / 7 (le trajet en six étapes + les câbles sous-marins)',
   /7 \/ 7/.test(await retour(2)) && await valide(2), (await retour(2)).slice(0, 60));

/* ── LE SIMULATEUR DE PAQUETS ────────────────────────────────────────────── */
await remplir(3); await valider(3);
ok('7 · activité 3 REFUSÉE malgré 3 réponses justes — le simulateur n\'a pas servi',
   /3 \/ 3/.test(await retour(3)) && /Utilise d'abord le simulateur/.test(await retour(3))
   && !(await valide(3)), (await retour(3)).slice(0, 75));

await ouvrirPour('simMsg');
const message = await p.inputValue('#simMsg');
await p.click('#btnDecoupe'); await p.waitForTimeout(120);
const paquets = await p.$$eval('[data-paquet]', l => l.map(e => e.dataset.paquet));
const enTetes = (await p.textContent('#zonePaquets')).replace(/\s+/g, ' ');
ok(`8 · « ${message} » découpé en ${paquets.length} paquets numérotés, arrivés dans le désordre`,
   paquets.length === 3 && /n°\d+\/3/.test(enTetes) && paquets.join() !== '0,1,2',
   'ordre d\'arrivée : ' + paquets.join('→'));

/* On se trompe d'abord d'ordre : le verrou ne doit pas s'ouvrir. */
for (const i of paquets) {
  await p.selectOption(`[data-paquet="${i}"]`, String(((Number(i) + 1) % 3) + 1));
}
await p.click('#btnReassemble'); await p.waitForTimeout(100);
ok('9 · un réassemblage dans le mauvais ordre est refusé, et le verrou reste fermé',
   /L'ordre n'est pas bon/.test(await p.textContent('#zoneReassemble'))
   && !(await p.evaluate(() => window.__simOk)),
   (await p.textContent('#zoneReassemble')).slice(0, 60));

for (const i of paquets) await p.selectOption(`[data-paquet="${i}"]`, String(Number(i) + 1));
await p.click('#btnReassemble'); await p.waitForTimeout(100);
ok('10 · remis dans l\'ordre, le message est reconstitué à l\'identique et le verrou s\'ouvre',
   (await p.textContent('#zoneReassemble')).includes(message)
   && await p.evaluate(() => !!window.__simOk),
   (await p.textContent('#zoneReassemble')).slice(0, 60));

await valider(3);
ok('11 · activité 3 validée 3 / 3 une fois le réassemblage réussi',
   /3 \/ 3/.test(await retour(3)) && !/Utilise d'abord/.test(await retour(3))
   && await valide(3), (await retour(3)).slice(0, 60));

await remplir(4); await valider(4);
ok('12 · activité 4 validée 4 / 4 (le jeu du routeur R2 : quatre paquets aiguillés)',
   /4 \/ 4/.test(await retour(4)) && await valide(4), (await retour(4)).slice(0, 60));

/* ── LE RÉSEAU MAILLÉ : le graphe est lu, pas recopié ─────────────────────── */
await remplir(5); await valider(5);
ok('13 · activité 5 REFUSÉE : l\'expérience de re-routage n\'a pas été faite',
   /Fais vraiment l'expérience/.test(await retour(5)) && !(await valide(5)),
   (await retour(5)).slice(0, 75));

await ouvrirPour('btnEnvoyer');
await p.click('#btnEnvoyer'); await p.waitForTimeout(100);
const lireChemin = async () => ((await p.textContent('#simResultat'))
  .match(/R\d(?: → R\d)+/) || [''])[0].split(' → ');
const initial = await lireChemin();
const GRAPHE = await p.evaluate(() => GRAPHE);
ok(`14 · premier envoi : le réseau annonce le plus court chemin ${initial.join('→')}, `
   + `calculé sur un graphe de ${Object.keys(GRAPHE).length} routeurs`,
   initial.length >= 3 && initial[0] === 'R1' && initial[initial.length - 1] === 'R5'
   && !(await p.evaluate(() => window.__rerouteVu)), initial.join('→'));

/* On coupe une liaison DU CHEMIN EMPRUNTÉ — laquelle ne peut pas être écrite
   ici, puisque le chemin est calculé par la page. */
const liaisons = await p.$$eval('#liens line', l => l.map(e => e.dataset.l));
const surLeChemin = liaisons.find(id => {
  const [x, y] = id.split('-');
  for (let i = 0; i < initial.length - 1; i++) {
    if ((initial[i] === x && initial[i + 1] === y) || (initial[i] === y && initial[i + 1] === x))
      return true;
  }
  return false;
});
await p.click(`#liens line[data-l="${surLeChemin}"]`); await p.waitForTimeout(80);
await p.click('#btnEnvoyer'); await p.waitForTimeout(100);
const secours = await lireChemin();
ok(`15 · liaison ${surLeChemin} coupée → le réseau trouve seul un autre chemin `
   + `(${secours.join('→')}) et le verrou de re-routage s'ouvre`,
   secours.join() !== initial.join() && secours[secours.length - 1] === 'R5'
   && await p.evaluate(() => !!window.__rerouteVu), secours.join('→'));

/* On isole l'arrivée : toutes ses liaisons coupées. */
const arrivee = initial[initial.length - 1];
for (const id of liaisons.filter(x => x.split('-').includes(arrivee))) {
  if ((await p.evaluate(() => window.__coupees)).includes(id)) continue;
  await p.click(`#liens line[data-l="${id}"]`); await p.waitForTimeout(60);
}
await p.click('#btnEnvoyer'); await p.waitForTimeout(100);
ok(`16 · les ${liaisons.filter(x => x.split('-').includes(arrivee)).length} liaisons de ${arrivee} `
   + 'coupées → « livraison impossible », et la page le dit sans se contredire',
   /Livraison impossible/.test(await p.textContent('#simResultat'))
   && await p.evaluate(() => !!window.__isoleVu),
   (await p.textContent('#simResultat')).slice(0, 60));

await p.click('#btnReparer'); await p.waitForTimeout(80);
await p.click('#btnEnvoyer'); await p.waitForTimeout(100);
ok(`17 · toutes les liaisons réparées → le réseau retrouve le chemin d'origine ${initial.join('→')}`,
   (await lireChemin()).join() === initial.join()
   && (await p.evaluate(() => window.__coupees.length)) === 0,
   (await lireChemin()).join('→'));

await valider(5);
ok('18 · activité 5 validée 2 / 2 une fois l\'expérience de re-routage réellement faite',
   /2 \/ 2/.test(await retour(5)) && !/Fais vraiment/.test(await retour(5))
   && await valide(5), (await retour(5)).slice(0, 60));

await remplir(6); await valider(6);
ok('19 · activité 6 validée 6 / 6 (le défi de transfert : de la station à la mairie)',
   /6 \/ 6/.test(await retour(6)) && await valide(6), (await retour(6)).slice(0, 60));

const prog = (await p.textContent('#progTxt')).replace(/\s+/g, ' ').trim();
const [faites, total] = (prog.match(/(\d+)\s*\/\s*(\d+)/) || []).slice(1).map(Number);
ok(`20 · toutes les activités sont validées (${prog})`, total > 0 && faites === total, prog);

/* ── persistance ─────────────────────────────────────────────────────────── */
await p.click(`#liens line[data-l="${surLeChemin}"]`); await p.waitForTimeout(80);
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(360);
ok('21 · rechargement : réponses, validations ET la liaison coupée sont restaurées',
   (await p.inputValue('#b1_1')) === PLAN[1].b1_1.v
   && (await p.textContent('#progTxt')).includes(String(total))
   && (await p.evaluate(() => window.__coupees)).includes(surLeChemin),
   JSON.stringify(await p.evaluate(() => window.__coupees)));
ok('22 · rechargement : les DEUX verrous d\'expérience survivent aussi',
   await p.evaluate(() => !!window.__simOk) && await p.evaluate(() => !!window.__rerouteVu),
   JSON.stringify(await p.evaluate(() =>
     ({ simOk: window.__simOk, reroute: window.__rerouteVu }))));

const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok(`23 · les ${liens.length} liens internes existent`, casses.length === 0,
   casses.slice(0, 3).join(' · '));

const svg = await p.$$eval('img[src$=".svg"], object[data$=".svg"]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('data')));
const svgAbsents = svg.filter(s => !fs.existsSync(path.join(ICI, s)));
ok(`24 · les ${svg.length} SVG référencés existent sur le disque`,
   svg.length === 4 && svgAbsents.length === 0, svgAbsents.join(' · '));

const distantes = await p.$$eval('[src], link[href], object[data], iframe[src]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('href') || e.getAttribute('data'))
        .filter(u => u && /^(https?:)?\/\//i.test(u)));
ok('25 · hors ligne : aucune ressource distante, aucune modale, aucune erreur JS',
   distantes.length === 0 && dlg.length === 0 && fail.length === 0 && err.length === 0,
   (distantes[0] || err[0] || fail[0] || dlg[0] || '').slice(0, 80));

/* Le rapport d'origine annonçait l'accessibilité clavier du réseau : on mesure. */
const clavier = await p.$$eval('#liens line',
  l => l.filter(e => e.getAttribute('tabindex') === '0' && e.getAttribute('role') === 'button'
                     && (e.getAttribute('aria-label') || '').length > 8).length);
ok(`26 · les ${liaisons.length} liaisons du réseau sont atteignables au clavier `
   + '(tabindex, role=button, aria-label)', clavier === liaisons.length, String(clavier));
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
const codes = await p.evaluate(() => Object.keys(COMP_LABELS));
const badge = (await p.$eval('.badge.theme', e => e.textContent)).trim();

ok('27 · chargement du QCM, titre « Internet jusqu\'à Sainte-Luce », taille annoncée exacte',
   /Sainte-Luce/i.test(await p.title()) && badge.includes(String(Q.length))
   && (await p.textContent('#qTot')) === String(Q.length), badge);

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
ok(`28 · ${Q.length} questions, ${codes.length} compétences : `
   + codes.map(c => c + ' ' + (parCode[c] || 0)).join(' · '),
   Q.length === 30 && codes.length === 2 && codes.every(c => parCode[c] > 0),
   JSON.stringify(parCode));

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`29 · bonnes réponses A/B/C/D = ${rep.join('/')} (écart max 1) et d[r] vide partout`,
   Math.max(...rep) - Math.min(...rep) <= 1 && Q.every(q => q.d[q.r] === ''), rep.join('/'));

const illustrees = Q.filter(q => q.img);
const imgAbsentes = illustrees.filter(q => !fs.existsSync(path.join(ICI, q.img)));
ok(`30 · ${illustrees.length} question(s) illustrée(s), fichiers présents sur le disque`,
   imgAbsentes.length === 0, imgAbsentes.map(q => q.n).join(' · '));

const incomplets = Q.filter(q => !(q.o.length === 4 && q.d.length === 4 && q.expl && q.ex
                                   && q.err && q.ret));
ok('31 · gabarit maison complet : 4 options, 4 réfutations, explication, exemple, erreur, à retenir',
   incomplets.length === 0, incomplets.map(q => q.n).slice(0, 3).join(' · '));

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
ok(`32 · parcours complet ${Q.length} / ${Q.length} joué → note ${note}, bilan sur `
   + `${lignes.length} compétences`,
   /20,0/.test(note) && (await p.textContent('#rOk')) === String(Q.length)
   && lignes.length === 2, note + ' · ' + lignes.join(' | ').slice(0, 70));

const cles = await p.evaluate(() => Object.keys(window.localStorage));
ok('33 · la clé localStorage du QCM est écrite',
   cles.some(k => k.includes('qcm_3e_C4.7')), cles.join(' · '));

const retourSeq = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href'))
  .filter(h => h && /sequence.*\.html$/.test(h)));
ok('34 · le lien de retour vers la séquence existe et pointe sur un fichier réel',
   retourSeq.length > 0
   && retourSeq.every(h => fs.existsSync(path.join(ICI, decodeURIComponent(h)))),
   retourSeq[0] || '');

ok('35 · aucune erreur JS sur le QCM', err.length === 0, err.slice(0, 2).join(' | '));
await ctx.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
