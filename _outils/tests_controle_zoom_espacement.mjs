/**
 * Banc de `controle_zoom_espacement.mjs` (règle d'or n°370, en essai) : deux pages écrites ici, l'une qui défile de
 * côté à 200 % et coupe un texte quand on espace les lettres, l'autre propre. Le banc prouve que la mesure voit ce
 * qu'elle dit voir (n°299). Usage : node _outils/tests_controle_zoom_espacement.mjs — sortie 0 si tout passe.
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const dossier = fs.mkdtempSync(path.join(os.tmpdir(), 'banc-zoom-'));
const MAUVAISE = '<!doctype html><html><body><div style="width:900px">large</div>'
  + '<div style="height:20px;overflow:hidden;width:200px">Un texte assez long qui sera coupé une fois les lignes '
  + 'espacées comme le demande la norme</div></body></html>';
const BONNE = '<!doctype html><html><body><p>Une page sobre qui se lit à toutes les tailles.</p></body></html>';
fs.writeFileSync(path.join(dossier, 'sequence_mauvaise.html'), MAUVAISE);
fs.writeFileSync(path.join(dossier, 'sequence_bonne.html'), BONNE);

function lancer(fichier) {
  try {
    const out = execFileSync('node', [path.join(ICI, 'controle_zoom_espacement.mjs'), fichier, '--strict'], { encoding: 'utf8' });
    return { code: 0, out };
  } catch (e) { return { code: e.status, out: String(e.stdout) }; }
}

let echecs = 0;
const m = lancer(path.join(dossier, 'sequence_mauvaise.html'));
const okM = m.code === 1 && /Z1/.test(m.out) && /E1/.test(m.out);
console.log(okM ? '✔' : '✘', 'page qui défile à 200 % et coupe un texte : refusée avec --strict (Z1, E1)');
echecs += !okM;
const b = lancer(path.join(dossier, 'sequence_bonne.html'));
const okB = b.code === 0 && /✅/.test(b.out);
console.log(okB ? '✔' : '✘', 'page sobre : acceptée');
echecs += !okB;
fs.rmSync(dossier, { recursive: true, force: true });
console.log(`${2 - echecs}/2 cas passent`);
process.exit(echecs ? 1 : 0);
