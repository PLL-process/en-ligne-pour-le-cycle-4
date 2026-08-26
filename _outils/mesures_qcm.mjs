/* Règle d'or n°137 — la bonne réponse est-elle répartie, ou toujours au même endroit ?

   Né le 26/08/2026 : dans deux QCM du Thème 3, les 28 bonnes réponses étaient
   TOUTES en position B. Cliquer la deuxième proposition partout donnait 28/28.
   Ce défaut n'existe qu'au niveau de la COLLECTION — chaque question, prise
   seule, est irréprochable —, donc aucune relecture ne peut le voir.

   Le repère n'est pas « quatre positions » mais « toutes les positions
   offertes » : un QCM à trois propositions n'a pas à en servir quatre.

   Ce que ce balayage NE voit PAS, et le dit : les QCM dont le tableau de
   questions n'est pas un littéral `const questions = [ … ];` — dix fichiers du
   dépôt à ce jour, marqués « tableau non trouvé ».

   Usage : node _outils/mesures_qcm.mjs [racine]                              */
import fs from "node:fs";
import path from "node:path";
const RACINE = process.argv[2] || ".";
const fichiers = [];
(function walk(d){
  for (const e of fs.readdirSync(d, {withFileTypes:true})) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) { if (!/_archive|node_modules|\.git/.test(e.name)) walk(p); }
    else if (/^qcm.*\.html$/i.test(e.name)) fichiers.push(p);
  }
})(RACINE);
const lignes = [];
for (const f of fichiers) {
  const src = fs.readFileSync(f, "utf8");
  const m = src.match(/const (?:QUESTIONS|questions)\s*=\s*(\[[\s\S]*?\n\];)/);
  if (!m) { lignes.push([f, "—", "tableau non trouvé"]); continue; }
  let q; try { q = eval(m[1].replace(/;\s*$/, "")); } catch { lignes.push([f, "—", "non évaluable"]); continue; }
  const rep = {};
  q.forEach(x => { const i = [x.ok, x.r, x.answer].find(v => v !== undefined); rep[i] = (rep[i]||0)+1; });
  /* Le repère n'est pas « quatre positions » mais « toutes les positions
     OFFERTES » : un QCM à trois propositions n'a pas à en servir quatre.
     Corrigé après une fausse alerte sur un QCM hérité à 3 options. */
  const nOpts = Math.max(...q.map(x => (x.o || x.opts || x.options || []).length), 0) || 4;
  const positions = Object.keys(rep).length;
  const max = Math.max(...Object.values(rep));
  const alerte = positions < nOpts ? "⚠ CONCENTRÉ"
               : (max > q.length * (1 / nOpts + 0.15) ? "· déséquilibré" : "ok");
  lignes.push([f, q.length + " q · " + nOpts + " prop. · " + JSON.stringify(rep), alerte]);
}
lignes.sort((a,b) => (a[2]<b[2]?1:-1));
for (const [f, d, a] of lignes) console.log(a.padEnd(14), d.padEnd(34), f.replace(/^.*?theme/, "theme"));
