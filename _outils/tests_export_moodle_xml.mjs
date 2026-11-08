/* tests_export_moodle_xml.mjs — le banc de l'export Moodle XML.
 *
 * Lance l'export EN SOUS-PROCESSUS, par sa ligne de commande (règle d'or n°299, second
 * corollaire : un banc qui n'emprunte pas le point d'entrée ne prouve rien du point d'entrée).
 * Sur un bac d'essai sous le dépôt : une page QUESTIONS avec image, nuance et un « < » dans
 * une option ; une page de l'ancien gabarit ; puis une page dont l'image manque.
 *
 * Usage : node _outils/tests_export_moodle_xml.mjs
 */
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const SCRIPT = path.join(ICI, 'export_moodle_xml.mjs');
const BAC = path.join(path.dirname(ICI), '.banc-export-moodle');

const PAGE = `<!doctype html><html><head><title>t</title></head><body>
<h1>Thème 1 · 5e — QCM : Banc d'essai, deux questions</h1>
<script>
const QUESTIONS = [
{c:"5e_C3.1",n:"Ordre",q:"Classer donne…",
 o:["S2 < S1 < S3","S3 < S2 < S1","S1 < S2 < S3","les trois autant"],r:2,
 expl:"Plus un système décide seul, plus il traite d'information.",ex:"S1 dose ; S3 se localise.",err:"Confondre.",
 d:["Non : S2 traite plus que S1.","Non.","","Non : ils diffèrent."],ret:"Décider seul = traiter plus.",
 img:{src:"Images/schema.svg",alt:"Un schéma"},nuance:"Une nuance."},
{c:"5e_C3.2",n:"Sans image",q:"Deuxième question ?",
 o:["a","b","c","d"],r:0,expl:"e",ex:"x",d:["","1","2","3"],ret:"r"}
];
</script></body></html>`;
const ANCIEN = `<!doctype html><html><body><section class="card"><p class="q-title">Q</p>
<button onclick="checkMCQ('q1','v0','fb1',1)">Corriger</button></section></body></html>`;
const SVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><rect width="10" height="10"/></svg>`;

function bac(fichiers) {
  fs.rmSync(BAC, { recursive: true, force: true });
  for (const [rel, contenu] of Object.entries(fichiers)) {
    const p = path.join(BAC, rel);
    fs.mkdirSync(path.dirname(p), { recursive: true });
    fs.writeFileSync(p, contenu, 'utf-8');
  }
}
function lancer() {
  return spawnSync(process.execPath, [SCRIPT, '--racine', BAC, '--sortie', 'sortie'], { encoding: 'utf-8' });
}
function xmlBienForme(fichier) {
  const r = spawnSync('python3', ['-I', '-c', 'import sys,xml.etree.ElementTree as E;E.parse(sys.argv[1]);print("ok")', fichier], { encoding: 'utf-8' });
  return r.status === 0;
}

let echecs = 0;
function verifier(nom, ok, detail = '') {
  console.log(`${ok ? '✓' : '✘'} ${nom}${ok || !detail ? '' : ' — ' + detail}`);
  if (!ok) echecs += 1;
}

/* 1. le cas nominal */
bac({
  'theme-1-objets-systemes-usages-interactions/C3-x/5e/5e_C3.1/qcm_banc.html': PAGE,
  'theme-1-objets-systemes-usages-interactions/C3-x/5e/5e_C3.1/Images/schema.svg': SVG,
  'theme-2-x/C4-x/4e/4e_C4.4/qcm_ancien.html': ANCIEN,
});
let r = lancer();
verifier('l’export sort à 0 sur une banque lisible', r.status === 0, r.stderr);
const f5e = path.join(BAC, 'sortie', '5e.xml');
verifier('un fichier 5e.xml est produit', fs.existsSync(f5e));
const xml = fs.existsSync(f5e) ? fs.readFileSync(f5e, 'utf-8') : '';
verifier('le XML est bien formé (xml.etree)', xmlBienForme(f5e));
verifier('deux questions multichoice', (xml.match(/type="multichoice"/g) || []).length === 2);
verifier('une catégorie par QCM, au chemin du niveau et du code', xml.includes('$course$/top/Technologie Cycle 4/5e/Thème 1 — 5e_C3.1 · Banc d&#039;essai, deux questions'.replace('&#039;', '\'')));
verifier('exactement une réponse à 100 par question', (xml.match(/fraction="100"/g) || []).length === 2 && (xml.match(/fraction="0"/g) || []).length === 6);
verifier('le « < » d’une option est échappé, pas interprété', xml.includes('S2 &lt; S1 &lt; S3') && !xml.includes('<p>S2 < S1'));
verifier('l’image est embarquée en base64 et référencée par @@PLUGINFILE@@',
  xml.includes(`encoding="base64">${Buffer.from(SVG).toString('base64')}</file>`) && xml.includes('@@PLUGINFILE@@/banc-q01.svg'));
verifier('la rétroaction générale porte pourquoi, exemple, erreur, nuance, à retenir',
  ['Pourquoi :', 'Exemple :', 'Erreur fréquente :', 'Nuance :', 'À retenir :'].every(e => xml.includes(e)));
verifier('la rétroaction d’un distracteur est reprise de d[i]', xml.includes('Non : S2 traite plus que S1.'));
verifier('idnumber stable par question', xml.includes('<idnumber>banc-q01</idnumber>') && xml.includes('<idnumber>banc-q02</idnumber>'));
verifier('l’étiquette de compétence est posée', xml.includes('<tag><text>5e_C3.2</text></tag>'));
const inv = fs.readFileSync(path.join(BAC, 'sortie', 'INVENTAIRE.md'), 'utf-8');
verifier('l’ancien gabarit est inventorié comme non exporté, avec sa raison', inv.includes('qcm_ancien.html') && inv.includes('ancien gabarit'));
verifier('un fichier par QCM est écrit dans par-qcm/', fs.existsSync(path.join(BAC, 'sortie', 'par-qcm', 'banc.xml')));

/* 2. image manquante → panne déclarée */
bac({ 'theme-1-x/C3-x/5e/5e_C3.1/qcm_banc.html': PAGE });
r = lancer();
verifier('une image référencée mais absente fait sortir à 1', r.status === 1 && /image manquante/.test(r.stderr), r.stderr);

/* 3. rien à lire → panne déclarée */
bac({ 'theme-1-x/C3-x/5e/5e_C3.1/lisez-moi.txt': 'rien' });
r = lancer();
verifier('aucune page QUESTIONS → sortie 1, pas un export vide et vert', r.status === 1);

fs.rmSync(BAC, { recursive: true, force: true });
console.log(echecs ? `\n${echecs} échec(s)` : '\nBanc vert.');
process.exit(echecs ? 1 : 0);
