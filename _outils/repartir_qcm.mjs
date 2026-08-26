/* Répartition des bonnes réponses — version générale (règle d'or n°137).

   Gère les deux formats du dépôt :
     • {c,n,q,o:[…],r:N,expl,ex,err,d:[…],ret}   ← format actuel
     • {q,img,options:[…],answer:N,exp,comp}     ← format hérité

   La rotation déplace les propositions ET le tableau de réfutations `d`, qui
   leur est PARALLÈLE : les désolidariser collerait à chaque mauvaise réponse
   la réfutation d'une autre. C'est le piège de cette correction.

   L'édition est chirurgicale : on ne réécrit que les tableaux et l'indice de
   chaque question, jamais le fichier entier — les commentaires de section et
   la mise en page sont conservés.                                            */
import fs from "node:fs";

const MOTIF = [2,0,3,1, 0,3,1,2, 3,1,0,2, 1,2,0,3, 2,3,1,0, 0,2,3,1, 1,0,2,3];

function tableauA(src, i) {           // lit un littéral de tableau à partir de '['
  let p = 0, dansTexte = false, ech = false;
  for (let k = i; k < src.length; k++) {
    const c = src[k];
    if (ech) { ech = false; continue; }
    if (c === "\\") { ech = true; continue; }
    if (c === '"') { dansTexte = !dansTexte; continue; }
    if (dansTexte) continue;
    if (c === "[") p++;
    else if (c === "]") { p--; if (p === 0) return { texte: src.slice(i, k + 1), fin: k + 1 }; }
  }
  throw new Error("tableau non refermé");
}
function litTableau(bloc, cle) {
  const m = new RegExp("\\b" + cle + "\\s*:\\s*\\[").exec(bloc);
  if (!m) return null;
  const i = bloc.indexOf("[", m.index);
  const { texte, fin } = tableauA(bloc, i);
  return { debut: i, fin, texte, valeur: eval(texte) };
}

const chemin = process.argv[2];
let src = fs.readFileSync(chemin, "utf8");
const mArr = src.match(/const (?:QUESTIONS|questions)\s*=\s*\[/);
if (!mArr) { console.log(chemin.split("/").pop() + " : aucun tableau de questions"); process.exit(0); }

/* découpage en blocs d'objets de premier niveau */
const debutArr = src.indexOf("[", mArr.index);
const { texte: arrTexte, fin: finArr } = tableauA(src, debutArr);
const blocs = [];
{
  let p = 0, dansTexte = false, ech = false, depart = -1;
  for (let k = 1; k < arrTexte.length; k++) {
    const c = arrTexte[k];
    if (ech) { ech = false; continue; }
    if (c === "\\") { ech = true; continue; }
    if (c === '"') { dansTexte = !dansTexte; continue; }
    if (dansTexte) continue;
    if (c === "{") { if (p === 0) depart = k; p++; }
    else if (c === "}") { p--; if (p === 0) blocs.push([depart, k + 1]); }
  }
}
const n = blocs.length;
const cibles = [];
for (let k = 0; k < n; k++) cibles.push(MOTIF[k % MOTIF.length]);

let nouveauArr = "", curseur = 0, touchees = 0, avant = {}, apres = {};
for (let k = 0; k < n; k++) {
  const [a, b] = blocs[k];
  nouveauArr += arrTexte.slice(curseur, a);
  let bloc = arrTexte.slice(a, b);
  const opts = litTableau(bloc, "o") || litTableau(bloc, "options");
  const mR = /\b(r|answer)\s*:\s*(\d+)/.exec(bloc);
  if (!opts || !mR) { nouveauArr += bloc; curseur = b; continue; }
  const nOpts = opts.valeur.length;
  const ancien = +mR[2];
  avant[ancien] = (avant[ancien] || 0) + 1;
  const cible = cibles[k] % nOpts;
  const rot = (ancien - cible + nOpts) % nOpts;
  const tourne = t => t.slice(rot).concat(t.slice(0, rot));
  const nouvellesOpts = tourne(opts.valeur);
  if (nouvellesOpts[cible] !== opts.valeur[ancien]) throw new Error("rotation fausse, question " + (k + 1));
  const refs = litTableau(bloc, "d");
  /* on remplace de la fin vers le début pour ne pas décaler les indices */
  const edits = [];
  edits.push({ debut: opts.debut, fin: opts.fin, texte: JSON.stringify(nouvellesOpts) });
  if (refs && refs.valeur.length === nOpts)
    edits.push({ debut: refs.debut, fin: refs.fin, texte: JSON.stringify(tourne(refs.valeur)) });
  edits.push({ debut: mR.index, fin: mR.index + mR[0].length, texte: mR[1] + ":" + cible });
  edits.sort((x, y) => y.debut - x.debut);
  for (const e of edits) bloc = bloc.slice(0, e.debut) + e.texte + bloc.slice(e.fin);
  apres[cible] = (apres[cible] || 0) + 1;
  nouveauArr += bloc; curseur = b; touchees++;
}
nouveauArr += arrTexte.slice(curseur);
src = src.slice(0, debutArr) + nouveauArr + src.slice(finArr);
fs.writeFileSync(chemin, src);
console.log(chemin.split("/").pop() + " : " + touchees + "/" + n + " questions · avant " +
            JSON.stringify(avant) + " → après " + JSON.stringify(apres));
