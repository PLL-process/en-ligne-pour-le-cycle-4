/* Répartition des bonnes réponses d'un QCM de l'ancienne génération.

   Constat du 26/08/2026 : dans les QCM 4e_C7 et 4e_C8, les 28 bonnes réponses
   étaient TOUTES en position B. Un élève qui clique B partout obtient 28/28 sans
   rien savoir — et le QCM ne mesure plus rien.

   On fait tourner les propositions de chaque question (rotation, donc l'ordre
   relatif des distracteurs est conservé) pour amener la bonne réponse sur une
   position voulue. La suite de positions est ÉCRITE ICI, en clair : elle est
   équilibrée (7 par lettre) et sans cycle apparent, donc reproductible et
   vérifiable — pas un tirage au hasard qui donnerait un fichier différent à
   chaque exécution.                                                            */
import fs from "node:fs";

const MOTIF = [2,0,3,1, 0,3,1,2, 3,1,0,2, 1,2,0,3, 2,3,1,0, 0,2,3,1, 1,0,2,3];
function cibles(n){
  const out = [];
  for (let k = 0; k < n; k++) out.push(MOTIF[k % MOTIF.length]);
  const compte = {0:0,1:0,2:0,3:0};
  out.forEach(c => compte[c]++);
  const vals = Object.values(compte);
  if (Math.max(...vals) - Math.min(...vals) > 1)
    throw new Error("répartition déséquilibrée : " + JSON.stringify(compte));
  return out;
}

const chemin = process.argv[2];
let src = fs.readFileSync(chemin, "utf8");
const lignes = src.split("\n");
const nQuestions = lignes.filter(l => /^\{q:/.test(l.trim())).length;
const CIBLES = cibles(nQuestions);
let i = 0, touchees = 0;

for (let l = 0; l < lignes.length; l++) {
  const ligne = lignes[l];
  if (!/^\{q:/.test(ligne.trim())) continue;
  const obj = eval("(" + ligne.trim().replace(/,$/, "") + ")");
  if (!Array.isArray(obj.opts) || obj.opts.length !== 4 || typeof obj.ok !== "number") continue;
  const cible = CIBLES[i];
  const rot = (obj.ok - cible + 4) % 4;                    // de combien on tourne
  const opts = obj.opts.slice(rot).concat(obj.opts.slice(0, rot));
  if (opts[cible] !== obj.opts[obj.ok]) throw new Error("rotation fausse à la question " + (i + 1));
  const avant = ligne.match(/opts:\[[\s\S]*?\],ok:\d/)[0];
  const apres = "opts:" + JSON.stringify(opts) + ",ok:" + cible;
  lignes[l] = ligne.replace(avant, apres);
  i++; touchees++;
}
fs.writeFileSync(chemin, lignes.join("\n"));
console.log(chemin.split("/").pop() + " : " + touchees + " questions redistribuées");
