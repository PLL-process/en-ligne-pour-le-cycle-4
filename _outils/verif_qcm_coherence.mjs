/* Contrôle d'alignement après rotation : la réfutation de la BONNE réponse doit
   rester vide, et les autres non vides. Si la rotation avait désolidarisé `d`
   des propositions, ce contrôle échouerait immédiatement. */
import fs from "node:fs";
let global = 0;
for (const f of process.argv.slice(2)) {
  const src = fs.readFileSync(f, "utf8");
  const m = src.match(/const (?:QUESTIONS|questions)\s*=\s*(\[[\s\S]*?\n\];)/);
  if (!m) { console.log("— " + f.split("/").pop() + " : tableau non lisible d'un bloc"); continue; }
  let q; try { q = eval(m[1].replace(/;\s*$/, "")); } catch (e) { console.log("— " + f.split("/").pop() + " : " + e.message); continue; }
  let mauvais = 0, sansD = 0;
  for (const x of q) {
    const r = x.r !== undefined ? x.r : x.answer;
    if (!Array.isArray(x.d)) { sansD++; continue; }
    if (x.d[r] && String(x.d[r]).trim()) mauvais++;
    if (x.d.filter((t, i) => i !== r && t && String(t).trim()).length !== x.d.length - 1) mauvais++;
  }
  const rep = {}; q.forEach(x => { const r = x.r !== undefined ? x.r : x.answer; rep[r] = (rep[r] || 0) + 1; });
  console.log((mauvais ? "❌ " : "✅ ") + f.split("/").pop() + " · " + q.length + " q · positions " +
              JSON.stringify(rep) + (sansD ? ` · ${sansD} sans réfutations` : "") +
              (mauvais ? ` · ${mauvais} DÉSALIGNEMENTS` : " · réfutations alignées"));
  global += mauvais;
}
process.exit(global ? 1 : 0);
