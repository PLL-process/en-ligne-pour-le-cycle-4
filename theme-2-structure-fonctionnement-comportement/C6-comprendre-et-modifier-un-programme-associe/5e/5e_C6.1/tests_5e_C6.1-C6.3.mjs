/* tests_5e_C6.1-C6.3.mjs — « Programmer le lampadaire », rejouable.
 *
 * LE CONSTAT QUI A DONNÉ CE FICHIER
 * ---------------------------------
 * Le rapport de ce lot portait vingt-trois coches vertes et citait `tests_lot07.js`
 * — un script qui n'a jamais été commité. Il l'avoue depuis le 31/08/2026 ; il lui
 * manquait la suite. C'est le lot en tête de la file publiée par
 * `_outils/controle_rapports_tests.py` (règles d'or n°259 et n°266).
 *
 * CE QUE CETTE SUITE ÉPROUVE EN PROPRE
 * ------------------------------------
 * Le 31/08/2026, `_outils/controle_verrous.mjs` a montré que le verrou
 * expérientiel de cette page s'ouvrait **à moitié tout seul** : la fonction
 * d'affichage du simulateur, appelée à l'initialisation, enregistrait l'état
 * affiché comme une expérience observée, et la clé `defaut` était donc posée
 * avant tout geste (règle d'or n°226, réparée le même jour). La suite vérifie
 * les deux moitiés du verrou : `__exp` vide à l'ouverture, puis l'activité 3
 * refusée **malgré 3 réponses justes** tant que les deux essais au simulateur
 * — le réglage d'origine, puis la mission de la mairie — n'ont pas été faits.
 *
 * CE QU'ELLE NE RECOPIE PAS
 * -------------------------
 * Aucune réponse attendue n'est écrite ici : elles sont extraites des fonctions
 * `CHECKS` de la page (convention `att = {id: "valeur"}`). Les deux seuils de la
 * mission ne sont pas écrits non plus : ils sont lus dans le source de `majSim`,
 * et les positions de curseur sont bornées par les `min`/`max` réels des
 * curseurs — un pilote de test déclare ce qu'il ne pilote pas (règle n°268).
 *
 * Usage, depuis ce dossier :
 *   node tests_5e_C6.1-C6.3.mjs
 * Playwright/Chromium requis. Sortie 0 si tout passe.
 */
import { chromium } from 'playwright';
import path from 'node:path';
import fs from 'node:fs';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const SEQ = path.join(ICI, 'sequence_5e_C6.1-C6.3_programmer_lampadaire.html');
const QCM = path.join(ICI, 'qcm_5e_C6.1-C6.3_programmer_lampadaire.html');

const T = []; const ok = (n, c, d = '') => T.push({ n, ok: !!c, d });
const b = await chromium.launch();

/* ════════════════ SÉQUENCE (20 contrôles) ════════════════ */
{
const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
const p = await ctx.newPage();
const err = [], fail = [], dlg = [];
p.on('pageerror', e => err.push(e.message));
p.on('console', m => { if (m.type() === 'error') err.push('console: ' + m.text()); });
p.on('requestfailed', r => { if (!/fonts\.g/.test(r.url())) fail.push(r.url()); });
p.on('dialog', async d => { dlg.push(d.message()); await d.dismiss(); });

await p.goto('file://' + SEQ, { waitUntil: 'load' });
await p.waitForTimeout(320);

const texte = (await p.textContent('body')).replace(/\s+/g, ' ');
ok('1 · chargement, titre « Programmer le lampadaire » et les trois codes annoncés',
   /Programmer le lampadaire/i.test(await p.title())
   && ['5e_C6.1', '5e_C6.2', '5e_C6.3'].every(c => texte.includes(c)));

await p.click('.seance-tab[data-panel="s3"]'); await p.waitForTimeout(120);
const s3 = await p.$eval('#s3', e => e.classList.contains('active'));
await p.click('.seance-tab[data-panel="s1"]'); await p.waitForTimeout(120);
ok('2 · trois onglets de séance, la bascule vers S3 puis S1 fonctionne',
   s3 && await p.$eval('#s1', e => e.classList.contains('active')));

/* ── le verrou réparé : rien d'observé avant le premier geste ────────────── */
const expInitial = await p.evaluate(() => window.__exp || {});
ok('3 · aucune expérience enregistrée au chargement — le verrou est bien fermé (n°226)',
   Object.keys(expInitial).filter(k => k !== 'mode_essentiel').length === 0,
   JSON.stringify(expInitial));

/* ── les réponses attendues, LUES dans la page ───────────────────────────── */
const ATT = await p.evaluate(() => {
  const out = {};
  for (const n of Object.keys(CHECKS)) {
    const src = CHECKS[n].toString();
    const plan = {};
    const objet = src.match(/att\s*=\s*(\{[\s\S]*?\})\s*;/);
    if (objet) Object.assign(plan, eval('(' + objet[1] + ')'));
    /* Seconde convention de la maison : un champ numérique n'entre pas dans
       `att`, il est comparé à part — `num("e1_7") === 30`. Ne lire que `att`,
       c'est laisser un champ vide et croire que la page compte faux : ce lot
       rendait 7 / 8 alors que la page et la suite disaient vrai toutes les deux. */
    for (const m of src.matchAll(/num\(\s*"([\w.]+)"\s*\)\s*===?\s*(-?\d+(?:[.,]\d+)?)/g))
      plan[m[1]] = m[2];
    out[n] = plan;
  }
  return out;
});
const champs = Object.values(ATT).reduce((s, o) => s + Object.keys(o).length, 0);
ok(`4 · ${champs} champs attendus extraits des CHECKS de la page (aucune réponse recopiée ici)`,
   Object.keys(ATT).length === 5 && champs >= 25, String(champs));

/* On ne devine pas dans quel onglet vit un champ : on ouvre les onglets jusqu'à
   ce qu'il soit visible. Deviner la répartition, c'est se tromper le jour où
   elle change — et Playwright refuse d'écrire dans ce qui est masqué. */
const ONGLETS = await p.$$eval('.seance-tab', l => l.map(e => e.dataset.panel));
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

/* ── le rappel d'hypothèse ───────────────────────────────────────────────── */
const avant = await p.$eval('#rappelHyp', e => getComputedStyle(e).display);
await ouvrirPour('hyp1');
await p.fill('#hyp1', 'Le lampadaire s\'allume quand il fait sombre et qu\'on passe.');
await p.waitForTimeout(120);
const apres = await p.$eval('#rappelHyp', e => getComputedStyle(e).display);
ok('5 · le rappel d\'hypothèse est caché tant que rien n\'est écrit, puis affiché mot pour mot',
   avant === 'none' && apres !== 'none'
   && (await p.textContent('#hypRappelTxt')).includes('quand il fait sombre'),
   avant + ' → ' + apres);

await remplir(1); await valider(1);
ok('6 · activité 1 validée 8 / 8 (carte d\'identité : entrées, sorties, paramètres, états)',
   /8 \/ 8/.test(await retour(1)), (await retour(1)).slice(0, 60));

await remplir(2); await valider(2);
ok('7 · activité 2 validée 9 / 9 (six étapes remises dans l\'ordre + SI / ET / SINON)',
   /9 \/ 9/.test(await retour(2)), (await retour(2)).slice(0, 60));

await remplir(5); await valider(5);
ok('8 · les formes de l\'algorigramme reconnues 4 / 4 (rectangle, losange, boucle)',
   /4 \/ 4/.test(await retour(5)), (await retour(5)).slice(0, 60));

/* ── le verrou expérientiel, éprouvé DANS LES DEUX SENS ──────────────────── */
await remplir(3); await valider(3);
const refus = await retour(3);
ok('9 · activité 3 REFUSÉE malgré 3 réponses justes — le verrou tient (n°226)',
   /3 \/ 3/.test(refus) && /Fais VRAIMENT la mission/.test(refus)
   && !(await p.evaluate(() => !!window.__valid[3])), refus.slice(0, 70));

/* Les deux seuils de la mission ne sont pas écrits ici : ils sont lus dans le
   source de `majSim`, et les positions de curseur sont bornées par les min/max
   réels des curseurs. */
const REGLE = await p.evaluate(() => {
  const s = majSim.toString();
  return {
    origine: Number((s.match(/seuil\s*===\s*(\d+)/) || [])[1]),
    seuilMini: Number((s.match(/seuil\s*>\s*(\d+)/) || [])[1]),
    lumMission: Number((s.match(/lum\s*===\s*(\d+)/) || [])[1]),
  };
});
const bornes = async id => p.$eval('#' + id, s => [Number(s.min), Number(s.max)]);
const [seuilMin, seuilMax] = await bornes('pSeuil');
const [dureeMin, dureeMax] = await bornes('pDuree');
const regler = async (id, x) => {
  await ouvrirPour(id);
  await p.$eval('#' + id, (s, v) => {
    s.value = String(v); s.dispatchEvent(new Event('input', { bubbles: true }));
  }, x);
  await p.waitForTimeout(70);
};
ok(`10 · réglage de la mission lu dans la page : origine ${REGLE.origine}, seuil > ${REGLE.seuilMini}, `
   + `luminosité ${REGLE.lumMission} ; curseur seuil borné à [${seuilMin} ; ${seuilMax}]`,
   REGLE.origine > 0 && REGLE.seuilMini > 0 && REGLE.lumMission > 0
   && seuilMax > REGLE.seuilMini, JSON.stringify(REGLE));

/* premier essai : le réglage d'ORIGINE */
await regler('pSeuil', REGLE.origine);
await regler('simLum', Math.max(0, REGLE.origine - 10));
const veilleOrigine = await p.textContent('#simLedTxt');
await regler('simLum', Math.min(100, REGLE.origine + 30));
const jourOrigine = await p.textContent('#simLedTxt');
ok('11 · au réglage d\'origine, la lampe passe de « éteint » (jour) à « veille » (nuit) selon le seuil',
   /veille/i.test(veilleOrigine) && /éteint/i.test(jourOrigine),
   veilleOrigine + ' | ' + jourOrigine);
ok('12 · le premier essai est enregistré comme expérience — et lui seul',
   await p.evaluate(() => !!window.__exp.defaut && !window.__exp.mission),
   JSON.stringify(await p.evaluate(() => window.__exp)));

/* Le passage détecté. On clique à la durée MINIMALE du curseur : le minuteur
   retient la durée en vigueur au moment du clic, et une suite qui attend
   dix secondes pour voir retomber une lampe est une suite qu'on cesse de
   jouer. On déplace ensuite le curseur pour vérifier que la durée annoncée
   le suit — sans que cela reprogramme le minuteur déjà lancé. */
await regler('simLum', Math.max(0, REGLE.origine - 10));
await regler('pDuree', dureeMin);
await ouvrirPour('btnPassage'); await p.click('#btnPassage'); await p.waitForTimeout(90);
const passage = await p.textContent('#simLedTxt');
await regler('pDuree', dureeMax);
ok(`13 · un passage détecté met la lampe en PLEINE PUISSANCE, et la durée annoncée suit `
   + `le curseur (${dureeMin} s → ${dureeMax} s, bornes réelles du curseur)`,
   /PLEINE PUISSANCE/.test(passage) && passage.includes(String(dureeMin))
   && (await p.textContent('#simLedTxt')).includes(String(dureeMax)),
   passage + ' → ' + await p.textContent('#simLedTxt'));

await p.waitForTimeout(dureeMin * 1000 + 400);   // la durée en vigueur au clic
ok(`13 bis · le passage retombe seul après les ${dureeMin} s en vigueur au moment du clic, `
   + 'et la lampe revient en veille',
   /veille/i.test(await p.textContent('#simLedTxt'))
   && !(await p.evaluate(() => window.__passage)), await p.textContent('#simLedTxt'));

/* second essai : la MISSION de la mairie */
const seuilMission = Math.min(seuilMax, REGLE.seuilMini + 5);
await regler('pSeuil', seuilMission);
await regler('simLum', REGLE.lumMission);
const mission = await p.textContent('#simMission');
ok(`14 · mission mairie : seuil relevé à ${seuilMission} puis luminosité à ${REGLE.lumMission} `
   + '→ vérifiée, et la lampe est bien en veille',
   /✅/.test(mission) && mission.includes(String(seuilMission))
   && /veille/i.test(await p.textContent('#simLedTxt'))
   && await p.evaluate(() => !!window.__exp.mission), mission);

await valider(3);
ok('15 · activité 3 validée 3 / 3 une fois les DEUX essais faits — le verrou s\'ouvre alors',
   /3 \/ 3/.test(await retour(3)) && !/Fais VRAIMENT/.test(await retour(3))
   && await p.evaluate(() => !!window.__valid[3]), (await retour(3)).slice(0, 60));

await remplir(4); await valider(4);
ok('16 · activité 4 validée 4 / 4 (réinvestissement : l\'arrosage du jardin pédagogique)',
   /4 \/ 4/.test(await retour(4)), (await retour(4)).slice(0, 60));

ok('17 · progression 4 / 4 activités, et les trois onglets de séance portent leur coche',
   (await p.textContent('#progTxt')).includes('4 / 4')
   && (await p.$$eval('[id^="done-s"]', l => l.map(e => e.textContent.trim())))
        .every(c => c === '✔'),
   await p.textContent('#progTxt'));

await p.click('.seance-tab[data-panel="s2"]'); await p.waitForTimeout(140);
const bandeau = (await p.textContent('#tachesBandeau')).replace(/\s+/g, ' ');
ok('18 · le tableau de bord des tâches suit l\'onglet actif et coche ce qui est fait',
   /Séance 2/.test(bandeau) && bandeau.includes('☑') && !bandeau.includes('☐'),
   bandeau.slice(0, 80));

/* ── persistance ─────────────────────────────────────────────────────────── */
await p.reload({ waitUntil: 'load' }); await p.waitForTimeout(340);
const premier = Object.keys(ATT[1])[0];
ok('19 · rechargement : réponses, validations ET les deux moitiés du verrou sont restaurées',
   (await p.inputValue('#' + premier)) === ATT[1][premier]
   && (await p.textContent('#progTxt')).includes('4 / 4')
   && await p.evaluate(() => !!window.__exp.defaut && !!window.__exp.mission),
   await p.textContent('#progTxt'));

const liens = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href')));
const casses = liens.filter(h => h && !/^(https?:|mailto:|#|javascript:)/.test(h))
  .map(h => decodeURIComponent(h.split('#')[0]))
  .filter(h => h && !fs.existsSync(path.join(ICI, h)));
ok(`20 · les ${liens.length} liens internes (QCM, lexique, synthèses, îlot 5e_C4.1, index) existent`,
   casses.length === 0, casses.slice(0, 3).join(' · '));

const svg = await p.$$eval('img[src$=".svg"], object[data$=".svg"]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('data')));
const svgAbsents = svg.filter(s => !fs.existsSync(path.join(ICI, s)));
ok(`21 · les ${svg.length} SVG référencés existent sur le disque`,
   svgAbsents.length === 0, svgAbsents.join(' · '));

/* Le namespace XML d'un SVG inline n'est pas une ressource distante : on ne
   regarde que ce que le navigateur irait vraiment chercher (règle n°40). */
const distantes = await p.$$eval('[src], link[href], object[data], iframe[src]',
  l => l.map(e => e.getAttribute('src') || e.getAttribute('href') || e.getAttribute('data'))
        .filter(u => u && /^(https?:)?\/\//i.test(u)));
ok('22 · hors ligne : aucune ressource distante, aucune modale, aucune erreur JS',
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
const badge = (await p.$eval('.badge.theme', e => e.textContent)).trim();

ok('23 · chargement du QCM, titre « Programmer le lampadaire », taille annoncée exacte',
   /Programmer le lampadaire/i.test(await p.title())
   && badge.includes(String(Q.length))
   && (await p.textContent('#qTot')) === String(Q.length), badge);

const parCode = {};
Q.forEach(q => { parCode[q.c] = (parCode[q.c] || 0) + 1; });
ok('24 · 30 questions, 10 par code sur les trois codes du lot',
   Q.length === 30 && Object.keys(parCode).length === 3
   && Object.values(parCode).every(v => v === 10), JSON.stringify(parCode));

const rep = [0, 0, 0, 0]; Q.forEach(q => rep[q.r]++);
ok(`25 · bonnes réponses A/B/C/D = ${rep.join('/')} (écart max 1) et d[r] vide partout`,
   Math.max(...rep) - Math.min(...rep) <= 1 && Q.every(q => q.d[q.r] === ''), rep.join('/'));

const illustrees = Q.filter(q => q.img);
const imgAbsentes = illustrees.filter(q => !fs.existsSync(path.join(ICI, q.img)));
ok(`26 · ${illustrees.length} questions illustrées, fichiers SVG présents sur le disque`,
   illustrees.length > 0 && imgAbsentes.length === 0, imgAbsentes.map(q => q.img).join(' · '));

const incomplets = Q.filter(q => !(q.o.length === 4 && q.d.length === 4 && q.expl && q.ex
                                   && q.err && q.ret));
ok('27 · gabarit maison complet : 4 options, 4 réfutations, explication, exemple, erreur, à retenir',
   incomplets.length === 0, incomplets.map(q => q.n).slice(0, 3).join(' · '));

/* ── le parcours entier, réellement joué ─────────────────────────────────── */
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
ok(`28 · parcours complet 30 / 30 joué question par question → note ${note}, `
   + `bilan sur ${lignes.length} compétences`,
   /20,0/.test(note) && (await p.textContent('#rOk')) === String(Q.length)
   && lignes.length === 3 && lignes.every(l => /10 \/ 10/.test(l)),
   note + ' · ' + lignes.join(' | ').slice(0, 90));

const cles = await p.evaluate(() => Object.keys(window.localStorage));
ok('29 · la clé localStorage du QCM est écrite',
   cles.some(k => k.includes('qcm_5e_C6.1-C6.3_programmer_lampadaire')), cles.join(' · '));

const retourSeq = await p.$$eval('a[href]', a => a.map(x => x.getAttribute('href'))
  .filter(h => h && /sequence.*\.html$/.test(h)));
ok('30 · le lien de retour vers la séquence existe et pointe sur un fichier réel',
   retourSeq.length > 0
   && retourSeq.every(h => fs.existsSync(path.join(ICI, decodeURIComponent(h)))),
   retourSeq[0] || '');

ok('31 · aucune erreur JS sur le QCM', err.length === 0, err.slice(0, 2).join(' | '));
await ctx.close();
}

const n = T.filter(t => t.ok).length;
console.log(T.map(t => `${t.ok ? '✅' : '❌'} ${t.n}${t.d ? ' — ' + t.d : ''}`).join('\n'));
console.log(`\n${n} / ${T.length}`);
await b.close();
process.exit(n === T.length ? 0 : 1);
