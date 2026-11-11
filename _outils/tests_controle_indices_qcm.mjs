/* tests_controle_indices_qcm.mjs — le banc de `controle_indices_qcm.mjs`.
 *
 * Il rejoue, sur des banques fabriquées, ce que le contrôle doit refuser, ce
 * qu'il doit seulement mesurer, et ce qu'il ne doit pas accuser. Chaque cas
 * « à ne pas accuser » vient d'un faux coupable rencontré le 11/11/2026 en
 * jouant la première version sur les 72 banques du dépôt :
 *
 *   · « les deux tâches qui possèdent de la marge » n'est PAS une proposition
 *     fourre-tout : un motif `^les deux` en accusait 63, il en reste 12 ;
 *   · huit mots absolus tous dans des mauvaises réponses, le hasard le donne
 *     une fois sur dix : un seuil à 90 % sur 8 refusait 20 banques saines ;
 *   · un `]` dans une proposition ne ferme pas le tableau des questions ;
 *   · un mot de l'énoncé repris par la bonne réponse ET par une mauvaise
 *     n'est pas un écho qui trahit.
 *
 * Usage : node _outils/tests_controle_indices_qcm.mjs
 * Sortie : 0 si tout passe, 1 sinon.
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import {
  main, lanceDirectement, extraireQuestions, mesurerBanque, estFourreTout, aMotAbsolu, motsPorteurs,
  SEUIL_ABSOLU, MIN_ABSOLU, SEUIL_ECHO,
} from './controle_indices_qcm.mjs';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const SCRIPT = path.join(ICI, 'controle_indices_qcm.mjs');

const echecs = [];
let controles = 0;
function verifier(titre, condition, detail = '') {
  controles++;
  if (!condition) echecs.push(`${titre}${detail ? ` — ${detail}` : ''}`);
}

const page = (questions) => `<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>QCM d'essai</title></head>
<body><script>
const COMP_LABELS = {"C0.0":"essai"};
const QUESTIONS = ${questions};
const AUTRE = [1, 2, 3];
</script></body></html>`;

/* Une question neutre : aucun mot absolu, aucun écho, aucune fourre-tout. */
const neutre = (i, r = i % 4) => ({
  c: 'C0.0', n: `Neutre ${i}`, q: `Que mesure l'instrument numéro ${i} ?`,
  o: ['une grandeur électrique', 'une durée écoulée', 'une masse posée', 'une distance parcourue'], r,
});

function jouer(questions, options = {}) {
  const racine = fs.mkdtempSync(path.join(os.tmpdir(), 'ciq-'));
  fs.writeFileSync(path.join(racine, 'qcm_essai.html'), page(JSON.stringify(questions)), 'utf8');
  const vraiLog = console.log, vraiErr = console.error;
  let texte = '';
  const capter = (...a) => { texte += a.join(' ') + '\n'; };
  console.log = capter; console.error = capter;
  let code;
  try { code = main({ cible: racine, ...options }); }
  finally { console.log = vraiLog; console.error = vraiErr; }
  fs.rmSync(racine, { recursive: true, force: true });
  return { code, texte };
}

// ══ LES BRIQUES ══════════════════════════════════════════════════════════════
verifier('fourre-tout : « toutes les réponses »', estFourreTout('Toutes les réponses sont justes'));
verifier('fourre-tout : « aucune des propositions »', estFourreTout('aucune des propositions'));
verifier('fourre-tout : « les deux »', estFourreTout('les deux'));
verifier('fourre-tout : « les deux, puisque… »', estFourreTout('Les deux, puisqu\'ils sont branchés sur la même carte'));
verifier('fourre-tout : « ni l\'un ni l\'autre »', estFourreTout('ni l’un ni l’autre : il ne se mesure pas'));
verifier('FAUX COUPABLE — « les deux tâches qui possèdent de la marge »',
  !estFourreTout('les deux tâches qui possèdent de la marge'));
verifier('FAUX COUPABLE — « les deux chiffres se contredisent »',
  !estFourreTout('les deux chiffres se contredisent : l\'un des deux calculs est faux'));

verifier('absolu : « toujours »', aMotAbsolu('elle est toujours allumée'));
verifier('absolu : « en aucun cas »', aMotAbsolu('en aucun cas'));
verifier('absolu : « n\'importe quel »', aMotAbsolu('n’importe quel capteur convient'));
verifier('FAUX COUPABLE — « rien » dans « terrien »', !aMotAbsolu('un satellite terrien'));
verifier('FAUX COUPABLE — « seulement » dans un autre mot', !aMotAbsolu('un isolement thermique'));

verifier('mots porteurs : pluriel ramené au singulier',
  motsPorteurs('les capteurs').has([...motsPorteurs('le capteur')][0]));
verifier('mots porteurs : mots vides et mots courts écartés',
  motsPorteurs('pour quelle raison la led').size === 1);

// ══ L'EXTRACTION DU TABLEAU ══════════════════════════════════════════════════
{
  const html = page(`[
/* ═══ un commentaire avec un ] dedans ═══ */
{c:"C0.0",q:"Que vaut liste[0] ?",o:["le premier élément ]","le dernier","rien du tout","une erreur"],r:0}, // fin ]
{c:"C0.0",q:'Et "ceci" ?',o:['a','b','c','d'],r:[1,2]}
]`);
  const questions = extraireQuestions(html);
  verifier('extraction : deux questions lues malgré les « ] » des chaînes et des commentaires',
    Array.isArray(questions) && questions.length === 2, JSON.stringify(questions));
  verifier('extraction : le tableau suivant (`const AUTRE`) n\'est pas avalé',
    questions && questions[1].o.length === 4);
}
verifier('extraction : une page sans banque rend null', extraireQuestions('<html><body>rien</body></html>') === null);
verifier('extraction : une banque qui ne se ferme pas rend null',
  extraireQuestions('<script>const QUESTIONS = [{q:"a",o:["b"],r:0}') === null);

// ══ CE QU'IL DOIT REFUSER ════════════════════════════════════════════════════
{
  // Douze mots absolus, tous dans des mauvaises réponses : la règle « absolu = faux » suffit.
  const banque = Array.from({ length: 12 }, (_, i) => ({
    c: 'C0.0', n: `Absolu ${i}`, q: `Que fait le montage numéro ${i} ?`,
    o: ['il allume la lampe', 'il ne fonctionne jamais', 'il coupe le courant', 'il mesure la tension'], r: 0,
  }));
  const { code, texte } = jouer(banque);
  verifier('REFUS — douze mots absolus, tous faux', code === 1 && texte.includes('mot absolu'), texte);
}
{
  // MUTATION : la même banque, où quatre bonnes réponses portent aussi un mot absolu.
  const banque = Array.from({ length: 12 }, (_, i) => ({
    c: 'C0.0', n: `Absolu ${i}`, q: `Que fait le montage numéro ${i} ?`,
    o: [i < 4 ? 'il allume toujours la lampe' : 'il allume la lampe', 'il ne fonctionne jamais', 'il coupe le courant', 'il mesure la tension'], r: 0,
  }));
  const { code } = jouer(banque);
  verifier('ACCEPTÉ — MUTATION : des mots absolus aussi dans les bonnes réponses', code === 0);
}
{
  // FAUX COUPABLE : huit mots absolus tous faux — le hasard le donne une fois sur dix.
  const banque = Array.from({ length: 12 }, (_, i) => (i < 8 ? {
    c: 'C0.0', n: `Absolu ${i}`, q: `Que fait le montage numéro ${i} ?`,
    o: ['il allume la lampe', 'il ne fonctionne jamais', 'il coupe le courant', 'il mesure la tension'], r: 0,
  } : neutre(i)));
  const { code } = jouer(banque);
  verifier(`ACCEPTÉ — FAUX COUPABLE : huit mots absolus, sous le minimum de ${MIN_ABSOLU}`, code === 0);
}
{
  // L'écho : la bonne réponse est seule à reprendre un mot de l'énoncé, une question sur deux.
  const banque = Array.from({ length: 12 }, (_, i) => (i % 2 ? neutre(i) : {
    c: 'C0.0', n: `Écho ${i}`, q: 'Quel composant est un capteur de luminosité ?',
    o: ['la photorésistance, qui sert de capteur', 'le moteur du store', 'la batterie du mât', 'le bouton poussoir'], r: 0,
  }));
  const { code, texte } = jouer(banque);
  verifier('REFUS — la bonne réponse seule à faire écho, une question sur deux',
    code === 1 && texte.includes('écho'), texte);
}
{
  // FAUX COUPABLE : le mot de l'énoncé est repris par la bonne réponse ET par une mauvaise.
  const banque = Array.from({ length: 12 }, (_, i) => ({
    c: 'C0.0', n: `Écho partagé ${i}`, q: 'Quel composant est un capteur de luminosité ?',
    o: ['la photorésistance, qui sert de capteur', 'le capteur de température', 'la batterie du mât', 'le bouton poussoir'], r: 0,
  }));
  const mesure = mesurerBanque(banque);
  verifier('ACCEPTÉ — FAUX COUPABLE : un écho partagé avec une mauvaise réponse ne trahit rien',
    mesure.echos.length === 0 && !mesure.refusEcho);
}

// ══ CE QU'IL MESURE SANS REFUSER ═════════════════════════════════════════════
{
  const banque = Array.from({ length: 12 }, (_, i) => neutre(i));
  banque[3] = { c: 'C0.0', n: 'Fourre-tout', q: 'Lequel convient ?', o: ['le premier', 'le second', 'les deux', 'aucune des réponses'], r: 2 };
  const souple = jouer(banque);
  verifier('MESURE — une fourre-tout est listée, la banque passe', souple.code === 0 && souple.texte.includes('fourre-tout'), souple.texte);
  const strict = jouer(banque, { strict: true });
  verifier('--strict — la même banque est refusée', strict.code === 1);
}
{
  // Une question à plusieurs réponses : pas d'écho mesuré, les mots absolus comptés sur chaque rang juste.
  const mesure = mesurerBanque([{ q: 'Lesquels ?', o: ['toujours A', 'jamais B', 'C', 'D'], r: [0, 2] }]);
  verifier('plusieurs réponses : un absolu juste, un absolu faux',
    mesure.absolusJustes === 1 && mesure.absolusFaux === 1 && mesure.echos.length === 0);
}

// ══ LA PANNE (règle d'or n°299) ══════════════════════════════════════════════
{
  const racine = fs.mkdtempSync(path.join(os.tmpdir(), 'ciq-'));
  fs.writeFileSync(path.join(racine, 'qcm_ancien.html'), '<html><body><script>function checkMCQ(){}</script></body></html>', 'utf8');
  const vraiLog = console.log, vraiErr = console.error;
  console.log = () => {}; console.error = () => {};
  let code;
  try { code = main({ cible: racine }); } finally { console.log = vraiLog; console.error = vraiErr; }
  fs.rmSync(racine, { recursive: true, force: true });
  verifier('PANNE — aucune banque lisible : sortie 2, pas « vert »', code === 2);
}
{
  const vraiErr = console.error; console.error = () => {};
  let code;
  try { code = main({ cible: path.join(os.tmpdir(), 'ciq-nexiste-pas') }); } finally { console.error = vraiErr; }
  verifier('PANNE — chemin absent : sortie 2', code === 2);
}

// ══ LE LANCEMENT ═════════════════════════════════════════════════════════════
verifier('la garde de lancement ne part pas pour un autre script',
  !lanceDirectement(new URL('./controle_indices_qcm.mjs', import.meta.url).href, path.join(ICI, 'autre_script.mjs')));
{
  const r = spawnSync(process.execPath, ['--input-type=module', '-e',
    `import ${JSON.stringify(new URL('./controle_indices_qcm.mjs', import.meta.url).href)};`],
  { encoding: 'utf8', timeout: 60000 });
  verifier('importé, le contrôle n\'écrit rien', !(r.stdout || '').trim() && r.status === 0, r.stderr);
}
{
  // lancé comme on le lance vraiment, en sous-processus (n°299, second corollaire)
  const racine = fs.mkdtempSync(path.join(os.tmpdir(), 'ciq-'));
  fs.writeFileSync(path.join(racine, 'qcm_essai.html'),
    page(JSON.stringify(Array.from({ length: 12 }, (_, i) => neutre(i)))), 'utf8');
  const r = spawnSync(process.execPath, [SCRIPT, '--muet', racine], { encoding: 'utf8', timeout: 60000 });
  fs.rmSync(racine, { recursive: true, force: true });
  verifier('en sous-processus : une banque saine sort à 0', r.status === 0 && r.stdout.includes('✅'), r.stdout + r.stderr);
}
verifier('les seuils sont ceux que l\'en-tête justifie',
  SEUIL_ABSOLU === 95 && MIN_ABSOLU === 12 && SEUIL_ECHO === 25);

// ══ VERDICT ══════════════════════════════════════════════════════════════════
if (echecs.length) {
  console.log('');
  for (const e of echecs) console.log('❌ ' + e);
  console.log(`\n${controles - echecs.length} / ${controles}`);
  process.exit(1);
}
console.log(`✅ ${controles} contrôles — refusés : douze mots absolus tous faux, l'écho une question sur deux ;`);
console.log('   mesurée sans refus : la proposition fourre-tout (refusée avec --strict) ;');
console.log('   non accusés : « les deux tâches… », huit absolus, l\'écho partagé, « rien » dans « terrien » ;');
console.log('   en panne (sortie 2) : aucune banque lisible, chemin absent.');
console.log(`\n${controles} / ${controles}`);
process.exit(0);
