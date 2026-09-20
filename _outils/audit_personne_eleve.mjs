/* audit_personne_eleve.mjs — à qui la page parle-t-elle ?
 *
 * LE CONSTAT QUI A DONNÉ CET AUDIT
 * --------------------------------
 * Une page que l'élève lit ne doit pas parler DE lui : elle lui parle, ou elle
 * le fait parler. Parler de l'élève à la troisième personne, c'est écrire pour
 * ses parents ou pour l'inspection — et l'élève le sent.
 *
 * CE QUE CET OUTIL FAIT
 * ---------------------
 * Il inventorie, page par page et ligne par ligne, chaque occurrence de
 * « l'élève » / « les élèves » et chaque vouvoiement dans les pages ÉLÈVES, et
 * propose un VERDICT pour chacune — en distinguant ce qu'il sait établir de ce
 * qu'il ne fait que suggérer :
 *
 *   · « personnage du scénario »  — l'élève est un tiers dans une histoire ou
 *     dans une proposition de QCM : ce n'est pas une infraction ;
 *   · « citation du programme »   — la phrase est une formulation du BO ;
 *   · « intitulé »                — titre, en-tête, légende : à reprendre, et
 *     c'est le cas que la règle n°302 vise en premier ;
 *   · « prose du corps »          — à relire une par une.
 *
 * CE QU'IL NE FAIT PAS
 * --------------------
 * Il ne corrige rien, et il ne tranche pas : le verdict « personnage du
 * scénario » est une PROPOSITION fondée sur le voisinage de la phrase, pas une
 * preuve. Le dernier mot est à la relecture. Un outil qui prétendrait trancher
 * le sens d'une phrase mentirait (règle d'or n°242).
 *
 * Usage :
 *   node _outils/audit_personne_eleve.mjs            # rapport complet
 *   node _outils/audit_personne_eleve.mjs --muet     # synthèse seule
 *   node _outils/audit_personne_eleve.mjs --csv      # + audit_personne_eleve.csv
 *
 * Sortie : 0 la mesure a eu lieu · 2 elle n'a RIEN pu analyser (règle d'or n°299).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const DEPOT = path.dirname(ICI);
const ECARTES = /_archive-anciennes-versions|[/\\]\.git|[/\\]node_modules/;

/** Une page professeur se reconnaît à son nom — convention du dépôt. */
const PROF = /synthese_professeur|fiche_pedagogique|rapport_tests|README|CADRAGE|PLAN_|MANIFESTE|SOURCES_/i;
/** Une page élève : celles que l'élève ouvre. */
const ELEVE = /^(sequence|tp|atelier|qcm|lexique|synthese_eleve)/i;

/* L'apostrophe droite ET la typographique : le dépôt porte les deux — 253 et 25
   occurrences relevées le 20/09/2026. N'en chercher qu'une en manquait 25. */
const ELEVE_MOT = /\b[LlDd][’']\s?élèves?\b|\bles\s+élèves\b|\bLes\s+élèves\b/g;
const VOUVOIEMENT = /\b(vous|votre|vos)\b/gi;

const muet = process.argv.includes('--muet');
const veutCsv = process.argv.includes('--csv');

function enPanne(motif) {
  console.error(`⛔ EN PANNE — ${motif}`);
  console.error("     Cet audit n'a RIEN inventorié ; ne le lisez pas comme un résultat (règle d'or n°299).");
  process.exit(2);
}

function fichiers(d, a = []) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (ECARTES.test(p)) continue;
    if (e.isDirectory()) fichiers(p, a);
    else if (e.name.endsWith('.html') && !PROF.test(e.name) && ELEVE.test(e.name)) a.push(p);
  }
  return a;
}

/** Le texte qu'un élève lit : ni script, ni style, ni commentaire. */
function sansCode(html) {
  return html
    .replace(/<!--[\s\S]*?-->/g, (m) => ' '.repeat(m.length))
    .replace(/<script[\s\S]*?<\/script>/gi, (m) => ' '.repeat(m.length))
    .replace(/<style[\s\S]*?<\/style>/gi, (m) => ' '.repeat(m.length));
}

/** Dans quel genre d'élément la position tombe-t-elle ? */
const INTITULE = /<(h[1-6]|th|summary|legend|caption|figcaption)\b[^>]*>[^<]*$/i;

function verdict(ligne, avant, dansIntitule) {
  /* La <legend> d'un groupe de questions est l'ÉNONCÉ d'une question, pas le
     titre d'une section : « les élèves de la classe » y est un tiers, et la
     règle n°302 l'exempte explicitement. Sans cette précédence, l'outil
     signalait une question de QCM comme un intitulé fautif. */
  const derniereLigne = avant.split(String.fromCharCode(10)).pop() || '';
  const enonceDeQuestion = /<legend[^>]*>[^<]*$/i.test(derniereLigne) || /qcm-groupe/.test(avant);
  if (dansIntitule && !enonceDeQuestion)
    return ['intitulé', 'à reprendre — la règle n°302 le vise en premier'];
  /* Une citation du programme : la ligne porte un code de compétence ou vit
     dans une cellule de tableau du bloc référentiel. */
  if (/\b[345]e_C\d/.test(ligne) || /<td>/.test(avant.slice(-120)))
    return ['citation du programme', 'légitime — formulation du BO, recopiée'];
  /* Un personnage : la phrase raconte ce qu'un élève fait dans un scénario, ou
     c'est une proposition de QCM. PROPOSITION, pas preuve. */
  if (/\b(un|une|des|deux|trois|plusieurs|chaque|certains|autre)\s+élèves?\b/i.test(ligne)
      || /o:\s*\[|<option|proposition/i.test(ligne))
    return ['personnage du scénario', 'légitime, sous réserve de relecture'];
  return ['prose du corps', 'à relire — verdict non tranché par l\'outil'];
}

const liste = fichiers(DEPOT);
if (!liste.length) enPanne(`aucune page élève sous ${DEPOT}`);

const occurrences = [];
const parPage = new Map();
let totalTu = 0, totalVous = 0;
const vousDomine = [];

for (const f of liste) {
  const rel = path.relative(DEPOT, f).replace(/\\/g, '/');
  const brut = fs.readFileSync(f, 'utf-8');
  const src = sansCode(brut);
  const lignes = src.split('\n');

  let nPage = 0;
  lignes.forEach((ligne, k) => {
    const avant = lignes.slice(Math.max(0, k - 1), k + 1).join('\n');
    let m;
    ELEVE_MOT.lastIndex = 0;
    while ((m = ELEVE_MOT.exec(ligne)) !== null) {
      /* hors balise : on ne compte pas « l'élève » dans un attribut */
      const jusqueLa = ligne.slice(0, m.index);
      const dansBalise = jusqueLa.lastIndexOf('<') > jusqueLa.lastIndexOf('>');
      if (dansBalise) continue;
      const dansIntitule = INTITULE.test(jusqueLa);
      const [genre, avis] = verdict(ligne, avant, dansIntitule);
      const phrase = ligne.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
      const i = Math.max(0, phrase.indexOf(m[0].trim()) - 45);
      occurrences.push({
        rel, ligne: k + 1, mot: m[0].trim(), genre, avis,
        extrait: phrase.slice(i, i + 130),
      });
      nPage++;
    }
  });
  if (nPage) parPage.set(rel, nPage);

  /* le tutoiement, page par page */
  const texte = src.replace(/<[^>]+>/g, ' ');
  const tu = (texte.match(/\b(tu|ton|ta|tes|toi)\b/gi) || []).length;
  const vs = (texte.match(VOUVOIEMENT) || []).length;
  totalTu += tu; totalVous += vs;
  if (vs > tu && vs > 5) vousDomine.push({ rel, tu, vs });
}

if (!liste.length) enPanne('aucune page lue');

/* ── le rapport ───────────────────────────────────────────────────────────── */
const parGenre = {};
for (const o of occurrences) parGenre[o.genre] = (parGenre[o.genre] || 0) + 1;
const legitimes = (parGenre['personnage du scénario'] || 0) + (parGenre['citation du programme'] || 0);
const aReprendre = occurrences.length - legitimes;

console.log(`${liste.length} page(s) élèves lues · ${occurrences.length} occurrence(s) de `
  + `« l'élève / les élèves » dans ${parPage.size} page(s)`);
console.log('     NON VU par cet outil : le sens. Le verdict « personnage du scénario » est une');
console.log('     PROPOSITION fondée sur le voisinage de la phrase, jamais une preuve — le dernier');
console.log('     mot est à la relecture. Ne sont pas lus non plus : les textes alternatifs, les');
console.log('     SVG, et tout ce qu\'un script écrit à l\'exécution.');

console.log('\n═══ 1. LE DÉPÔT TUTOIE ═══');
console.log(`  ${totalTu} « tu / ton / ta / tes / toi » contre ${totalVous} « vous / votre / vos »`);
console.log(`  soit ${(totalTu / Math.max(1, totalVous)).toFixed(0)} contre 1. Le vouvoiement est donc écarté`);
console.log('  sur MESURE, et non sur goût : il réinstallerait une distance que le dépôt a choisi');
console.log('  de ne pas mettre.');
if (vousDomine.length) {
  console.log(`\n  ${vousDomine.length} page(s) où le « vous » domine :`);
  for (const v of vousDomine) console.log(`     ${v.rel.split('/').pop()} — tu=${v.tu} vous=${v.vs}`);
}

console.log('\n═══ 2. « L\'ÉLÈVE » DANS LES PAGES ÉLÈVES ═══');
for (const [g, n] of Object.entries(parGenre).sort((a, b) => b[1] - a[1])) {
  console.log(`  ${String(n).padStart(4)}  ${g}`);
}
console.log(`  ${String(legitimes).padStart(4)}  → LÉGITIMES (personnage ou citation)`);
console.log(`  ${String(aReprendre).padStart(4)}  → À REPRENDRE`);

if (!muet) {
  console.log('\n═══ 3. LE DÉTAIL, PAGE PAR PAGE ═══');
  const pages = [...new Set(occurrences.map((o) => o.rel))].sort();
  for (const p of pages) {
    const oc = occurrences.filter((o) => o.rel === p);
    console.log(`\n  ── ${p} (${oc.length})`);
    for (const o of oc) {
      console.log(`     l.${String(o.ligne).padStart(5)}  ${o.genre.padEnd(24)} « ${o.extrait} »`);
    }
  }
}

if (veutCsv) {
  const entete = 'fichier;ligne;mot;genre;verdict;extrait';
  const corps = occurrences.map((o) => [o.rel, o.ligne, o.mot, o.genre, o.avis,
    '"' + o.extrait.replace(/"/g, "'") + '"'].join(';'));
  const dest = path.join(ICI, 'audit_personne_eleve.csv');
  fs.writeFileSync(dest, [entete, ...corps].join('\n') + '\n', 'utf-8');
  console.log(`\nCSV écrit : ${path.relative(DEPOT, dest).replace(/\\/g, '/')}`);
}

console.log('\n✅ inventaire terminé — cet audit ne corrige rien et ne tranche rien.');
process.exit(0);
