/* controle_indices_qcm.mjs — une bonne réponse ne se devine pas à ses mots.
 *
 * D'OÙ VIENT CE CONTRÔLE
 * ----------------------
 * Le dépôt mesure déjà deux indices qui trahissent la bonne réponse sans qu'on
 * ait besoin de savoir : sa PLACE (`mesures_qcm.mjs`, n°137 ;
 * `controle_ordre_propositions.py`, n°323) et sa LONGUEUR
 * (`controle_longueurs.py`, n°144 et n°198). La veille du 11/11/2026 sur les
 * skills pédagogiques (voir `SKILLS_AUDIT.md`, « Skills externes ») a rappelé
 * trois autres indices, classiques dans la littérature sur l'écriture des QCM
 * (Haladyna, Downing et Rodriguez, 2002, « A review of multiple-choice
 * item-writing guidelines », Applied Measurement in Education, 15(3)) et
 * qu'aucun outil du dépôt ne regardait :
 *
 *   A. LA PROPOSITION FOURRE-TOUT — « toutes les réponses », « aucune des
 *      réponses », « les deux », « ni l'un ni l'autre ». Elle ne mesure pas la
 *      notion : l'élève qui reconnaît deux propositions justes coche « toutes »
 *      sans avoir lu la troisième.
 *   B. LE MOT ABSOLU — « toujours », « jamais », « uniquement », « aucun »…
 *      Quand ces mots ne vivent que dans les mauvaises réponses, l'élève apprend
 *      la règle « un mot absolu = faux » et répond juste sans la notion.
 *   C. L'ÉCHO — la bonne réponse est la SEULE proposition à reprendre un mot de
 *      l'énoncé. L'élève apparie les mots, il ne raisonne pas.
 *
 * CE QUE L'OUTIL LIT
 * ------------------
 * Les QCM autonomes au gabarit maison : le tableau `const QUESTIONS = [ … ]` de
 * chaque page `qcm_*.html`, évalué tel quel dans un bac à sable (aucun
 * navigateur). Champs lus : `q` (énoncé), `o` (propositions), `r` (rang de la
 * bonne réponse, ou tableau de rangs pour une question à plusieurs réponses).
 *
 * CE QU'IL REFUSE, ET CE QU'IL SE CONTENTE DE MESURER
 * ---------------------------------------------------
 *   · B est REFUSÉ au niveau de la BANQUE, jamais de la question : un « jamais »
 *     dans une mauvaise réponse est légitime (« le secteur 230 V n'est jamais
 *     manipulé » peut être la BONNE réponse). Ce qui trahit, c'est la
 *     régularité. Refus quand la règle « absolu = faux » donne raison à l'élève
 *     au moins SEUIL_ABSOLU fois sur 100, sur MIN_ABSOLU propositions au moins.
 *     POURQUOI DES SEUILS SI HAUTS : avec quatre propositions dont une juste, un
 *     mot absolu posé au hasard tombe sur une mauvaise réponse 75 fois sur 100.
 *     Huit mots absolus tous faux, le hasard le donne une fois sur dix : refuser
 *     là accuserait des banques saines (mesuré le 11/11/2026 : un premier seuil
 *     à 90 % sur 8 refusait 20 banques sur 72). Douze sur douze, le hasard ne le
 *     donne que 3 fois sur 100. En dessous du seuil, l'outil MESURE : le taux de
 *     chaque banque et celui du site, à comparer aux 75 % attendus.
 *   · C est REFUSÉ au niveau de la BANQUE : refus quand plus de SEUIL_ECHO
 *     questions sur 100 désignent leur bonne réponse par l'écho seul.
 *   · A est MESURÉ, pas refusé : « les deux » est parfois la bonne manière de
 *     poser la question (le dépôt le garde en dernier, voir
 *     `melanger_propositions.py`). L'outil les liste ; `--strict` en fait un refus.
 *
 * CE QU'IL NE VOIT PAS, ET LE DIT
 * -------------------------------
 *   · L'indice GRAMMATICAL (« un… » devant une seule proposition masculine,
 *     accord du verbe) : il demande une analyse de la langue que cet outil ne
 *     fait pas. Il reste à l'œil du relecteur.
 *   · Les questions des SÉQUENCES (boutons radio, n°300) : leurs propositions
 *     vivent dans le HTML, pas dans un tableau. Hors du champ de cet outil.
 *   · La PLAUSIBILITÉ d'un distracteur (n°125) : aucune mesure de texte ne la
 *     donne. « Interdite par le langage Python » ne trompe personne, et ce
 *     contrôle n'en dira rien.
 *   · L'écho par SYNONYME ou par mot de moins de cinq lettres.
 *
 * Usage :
 *   node _outils/controle_indices_qcm.mjs               # tous les QCM publiés
 *   node _outils/controle_indices_qcm.mjs --muet        # synthèse seule
 *   node _outils/controle_indices_qcm.mjs --strict      # A devient un refus
 *   node _outils/controle_indices_qcm.mjs --json <f>    # mesures par page
 *   node _outils/controle_indices_qcm.mjs <chemin>      # une page, ou un dossier
 *
 * Sortie : 0 aucun refus · 1 au moins une banque refusée · 2 EN PANNE, aucune
 * banque lue (règle d'or n°299).
 */
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const RACINE = path.resolve(ICI, '..');

export const SEUIL_ABSOLU = 95;   // % de propositions à mot absolu qui sont fausses
export const MIN_ABSOLU = 12;     // en dessous, le hasard seul explique le taux (voir plus haut)
export const ATTENDU_ABSOLU = 75; // % attendu sans biais : trois mauvaises réponses sur quatre
export const SEUIL_ECHO = 25;     // % de questions dont la bonne réponse est seule à faire écho
export const MIN_QUESTIONS = 10;  // en dessous, un pourcentage ne dit rien

const IGNORES = new Set(['.git', 'node_modules', '_archive-anciennes-versions', '_outils', '_exports']);

const FOURRE_TOUT = [
  /\btou(te)?s\s+(les|ces)\s+(r[ée]ponses|propositions)\b/i,
  /\btoutes\s+les\s+(trois|quatre)\b/i,
  /\baucune\s+(des|de\s+ces)\s+(r[ée]ponses|propositions)\b/i,
  /\baucune\s+de\s+ces\s+(solutions|affirmations)\b/i,
  /^\s*les\s+(deux|trois)\s*($|[,:;.!—–-]|\s+(à\s+la\s+fois|sont\b|r[ée]ponses|propositions|pr[ée]c[ée]dentes))/i,
  /\bni\s+l['’]une?\s+ni\s+l['’]autre\b/i,
  /\b(a|b|c)\s+et\s+(b|c|d)\s*$/i,
];

const ABSOLUS = /(^|[^\p{L}])(toujours|jamais|aucune?|uniquement|seulement|forc[ée]ment|obligatoirement|impossible|exclusivement|n['’]importe\s+(quel|quelle|quoi|o[uù]|quand)|dans\s+tous\s+les\s+cas|en\s+aucun\s+cas|rien)(?=$|[^\p{L}])/iu;

/* Mots trop communs pour qu'un écho veuille dire quelque chose. */
const VIDES = new Set(('alors ainsi apres aussi autre autres avant avec avoir cette celle celui chaque comme comment '
  + 'dans depuis donc dont elle elles entre etre faire fait faut leur leurs mais meme moins notre nous parce '
  + 'pendant plus pour pourquoi quand quel quelle quelles quels quoi sans sera sont sous suivante suivantes '
  + 'suivant toute toutes tous tout tres votre vous cela ceci ceux deux trois quatre peut doit permet '
  + 'lequel laquelle lesquels reponse reponses proposition propositions question exemple').split(' '));

function sansAccent(s) {
  return s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
}

/* Les mots porteurs d'un texte : cinq lettres au moins, réduits à une racine
 * grossière (pluriel et féminin retirés) pour que « capteurs » réponde à
 * « capteur ». Grossier à dessein : un écho se voit, il ne s'analyse pas. */
export function motsPorteurs(texte) {
  const out = new Set();
  for (const brut of sansAccent(String(texte)).split(/[^a-z0-9]+/)) {
    if (brut.length < 5 || VIDES.has(brut)) continue;
    const racine = brut.replace(/(es|s|e)$/, '');
    if (racine.length >= 4) out.add(racine);
  }
  return out;
}

export function estFourreTout(option) {
  return FOURRE_TOUT.some((re) => re.test(String(option)));
}

export function aMotAbsolu(option) {
  return ABSOLUS.test(String(option));
}

/* Extrait le littéral du tableau `const QUESTIONS = [ … ];` en comptant les
 * crochets hors des chaînes — un `]` dans une proposition ne ferme rien. */
export function extraireQuestions(html) {
  const m = /const\s+QUESTIONS\s*=\s*\[/.exec(html);
  if (!m) return null;
  let i = m.index + m[0].length - 1;
  let profondeur = 0;
  let chaine = null;
  const debut = i;
  for (; i < html.length; i++) {
    const c = html[i];
    if (chaine) {
      if (c === '\\') { i++; continue; }
      if (c === chaine) chaine = null;
      continue;
    }
    if (c === '"' || c === "'" || c === '`') { chaine = c; continue; }
    if (c === '/' && html[i + 1] === '*') {
      const fin = html.indexOf('*/', i + 2);
      if (fin < 0) return null;
      i = fin + 1; continue;
    }
    if (c === '/' && html[i + 1] === '/') {
      const fin = html.indexOf('\n', i);
      if (fin < 0) return null;
      i = fin; continue;
    }
    if (c === '[') profondeur++;
    else if (c === ']') { profondeur--; if (profondeur === 0) break; }
  }
  if (profondeur !== 0) return null;
  const litteral = html.slice(debut, i + 1);
  try {
    const valeur = vm.runInNewContext(`(${litteral})`, Object.create(null), { timeout: 2000 });
    return Array.isArray(valeur) ? valeur : null;
  } catch {
    return null;
  }
}

function rangsJustes(question) {
  if (Array.isArray(question.r)) return new Set(question.r);
  if (Number.isInteger(question.r)) return new Set([question.r]);
  return null;
}

/* Mesure une banque. Rend les trois familles de constats et les décomptes. */
export function mesurerBanque(questions) {
  const fourreTout = [];
  const echos = [];
  let absolusFaux = 0;
  let absolusJustes = 0;
  let lues = 0;
  let aUneSeuleReponse = 0;

  questions.forEach((question, index) => {
    if (!question || !Array.isArray(question.o)) return;
    const justes = rangsJustes(question);
    if (!justes) return;
    lues++;
    const numero = index + 1;

    question.o.forEach((option, rang) => {
      if (estFourreTout(option)) fourreTout.push({ numero, option: String(option), juste: justes.has(rang) });
      if (aMotAbsolu(option)) { if (justes.has(rang)) absolusJustes++; else absolusFaux++; }
    });

    if (justes.size === 1) {
      aUneSeuleReponse++;
      const enonce = motsPorteurs(question.q || '');
      const partage = question.o.map((option) => [...motsPorteurs(option)].filter((mot) => enonce.has(mot)));
      const bonne = [...justes][0];
      const autresMuettes = partage.every((mots, rang) => rang === bonne || mots.length === 0);
      if (partage[bonne] && partage[bonne].length > 0 && autresMuettes) {
        echos.push({ numero, mots: partage[bonne], option: String(question.o[bonne]) });
      }
    }
  });

  const absolus = absolusFaux + absolusJustes;
  const tauxAbsolu = absolus ? Math.round((100 * absolusFaux) / absolus) : null;
  const tauxEcho = aUneSeuleReponse ? Math.round((100 * echos.length) / aUneSeuleReponse) : null;
  return {
    lues, fourreTout, echos, absolusFaux, absolusJustes, tauxAbsolu, tauxEcho,
    refusAbsolu: absolus >= MIN_ABSOLU && tauxAbsolu >= SEUIL_ABSOLU,
    refusEcho: aUneSeuleReponse >= MIN_QUESTIONS && tauxEcho > SEUIL_ECHO,
  };
}

function pagesQcm(depart) {
  if (!fs.statSync(depart).isDirectory()) return [path.resolve(depart)];
  const out = [];
  (function marcher(dossier) {
    for (const entree of fs.readdirSync(dossier, { withFileTypes: true })) {
      const complet = path.join(dossier, entree.name);
      if (entree.isDirectory()) {
        if (entree.name.startsWith('.') || IGNORES.has(entree.name)) continue;
        marcher(complet);
      } else if (/^qcm_.*\.html$/i.test(entree.name)) out.push(complet);
    }
  })(depart);
  return out.sort();
}

export function main({ muet = false, strict = false, cible = RACINE, json = null } = {}) {
  if (!fs.existsSync(cible)) {
    console.error(`❌ EN PANNE : « ${cible} » n'existe pas (règle d'or n°299).`);
    return 2;
  }
  const fichiers = pagesQcm(cible);
  const mesures = [];
  const sansBanque = [];
  for (const fichier of fichiers) {
    const questions = extraireQuestions(fs.readFileSync(fichier, 'utf8'));
    if (!questions) { sansBanque.push(fichier); continue; }
    const mesure = mesurerBanque(questions);
    if (mesure.lues === 0) { sansBanque.push(fichier); continue; }
    mesures.push({ page: path.relative(RACINE, fichier) || fichier, ...mesure });
  }

  if (mesures.length === 0) {
    console.error(`❌ EN PANNE : aucune banque \`const QUESTIONS\` lue (${fichiers.length} page(s) qcm_*.html trouvée(s)) — règle d'or n°299.`);
    return 2;
  }

  if (json) fs.writeFileSync(json, JSON.stringify({ seuils: { SEUIL_ABSOLU, MIN_ABSOLU, SEUIL_ECHO, MIN_QUESTIONS }, mesures, sansBanque: sansBanque.map((f) => path.relative(RACINE, f)) }, null, 2));

  let refus = 0;
  let totalFourreTout = 0;
  let totalQuestions = 0;
  let totalAbsolusFaux = 0;
  let totalAbsolus = 0;
  let totalEchos = 0;
  for (const mesure of mesures) {
    totalQuestions += mesure.lues;
    totalFourreTout += mesure.fourreTout.length;
    totalAbsolusFaux += mesure.absolusFaux;
    totalAbsolus += mesure.absolusFaux + mesure.absolusJustes;
    totalEchos += mesure.echos.length;
    const refuse = mesure.refusAbsolu || mesure.refusEcho || (strict && mesure.fourreTout.length > 0);
    if (refuse) refus++;
    if (muet && !refuse) continue;
    if (!refuse && mesure.fourreTout.length === 0) continue;
    console.log(`\n${refuse ? '✘' : '·'} ${mesure.page} — ${mesure.lues} question(s)`);
    if (mesure.refusAbsolu) {
      console.log(`    ✘ mot absolu : ${mesure.absolusFaux} proposition(s) fausse(s) sur ${mesure.absolusFaux + mesure.absolusJustes} qui en portent un (${mesure.tauxAbsolu} %) — « absolu = faux » suffit à répondre. Glisser un mot absolu dans des bonnes réponses, ou le retirer de mauvaises.`);
    }
    if (mesure.refusEcho) {
      console.log(`    ✘ écho : ${mesure.echos.length} question(s) (${mesure.tauxEcho} %) où la bonne réponse est seule à reprendre un mot de l'énoncé :`);
      for (const echo of mesure.echos.slice(0, muet ? 3 : 99)) console.log(`        q${echo.numero} — « ${echo.mots.join(', ')} » → « ${echo.option} »`);
    }
    if (mesure.fourreTout.length && (!muet || strict)) {
      console.log(`    ${strict ? '✘' : '·'} fourre-tout : ${mesure.fourreTout.length}`);
      for (const constat of mesure.fourreTout) console.log(`        q${constat.numero} — « ${constat.option} »${constat.juste ? ' (bonne réponse)' : ''}`);
    }
  }

  console.log('');
  if (sansBanque.length) console.log(`ℹ ${sansBanque.length} page(s) qcm_*.html sans tableau \`const QUESTIONS\` lisible : non mesurée(s).`);
  console.log(`ℹ Non vu par cet outil : indice grammatical, plausibilité des distracteurs, questions des séquences.`);
  console.log(`· propositions fourre-tout : ${totalFourreTout} sur ${mesures.length} banque(s)${strict ? '' : ' (mesure, pas refus ; --strict pour refuser)'}`);
  if (totalAbsolus) console.log(`· mots absolus : ${totalAbsolusFaux} sur ${totalAbsolus} sont dans une mauvaise réponse (${Math.round((100 * totalAbsolusFaux) / totalAbsolus)} % ; attendu sans biais : ${ATTENDU_ABSOLU} %)`);
  console.log(`· écho de l'énoncé dans la seule bonne réponse : ${totalEchos} question(s) sur ${totalQuestions}`);
  if (refus) {
    console.log(`✘ ${refus} banque(s) refusée(s) sur ${mesures.length} (${totalQuestions} questions lues).`);
    return 1;
  }
  console.log(`✅ aucune banque ne livre sa bonne réponse par un mot absolu ou par l'écho de l'énoncé (${mesures.length} banque(s), ${totalQuestions} questions).`);
  return 0;
}

export function lanceDirectement(url, argv1) {
  return Boolean(argv1) && url === pathToFileURL(path.resolve(argv1)).href;
}

if (lanceDirectement(import.meta.url, process.argv[1])) {
  const args = process.argv.slice(2);
  const iJson = args.indexOf('--json');
  const json = iJson >= 0 ? args[iJson + 1] : null;
  const libres = args.filter((a, i) => !a.startsWith('--') && !(iJson >= 0 && i === iJson + 1));
  process.exit(main({
    muet: args.includes('--muet'),
    strict: args.includes('--strict'),
    cible: libres[0] ? path.resolve(libres[0]) : RACINE,
    json,
  }));
}
