#!/usr/bin/env node
/* ÉTAT DES LIEUX MÉCANIQUE DES QCM DES TROIS THÈMES
 *
 * Pourquoi cet outil existe
 * -------------------------
 * Le 27 août 2026, en reprenant les quatre QCM de C7 et C8 après une
 * relecture humaine, une mesure a montré ce qu'aucune relecture n'avait vu :
 * dans 107 des 120 questions, la bonne réponse était la proposition la plus
 * LONGUE. Cocher la plus longue sans rien lire donnait 89 %.
 *
 * La question se pose alors pour les 46 QCM du dépôt. Elle ne se règle pas en
 * relisant : elle se mesure. Cet outil produit l'état des lieux — il ne
 * corrige rien, il ne juge rien, il compte.
 *
 * Ce qu'il mesure, et qui correspond aux règles d'or
 * --------------------------------------------------
 *   n°144  le biais de longueur : « cocher la plus longue » réussit combien ?
 *   n°137  la répartition des bonnes réponses sur A / B / C / D
 *   n°139  les absolus (toujours, jamais, il suffit de, tous les) dans les
 *          réfutations et les « à retenir »
 *   n°1    les images : présence, alternative rédigée
 *   —      le défaut « undefined » : un champ optionnel rendu sans garde
 *   —      la complétude du standard C9 : réfutation par distracteur, d[r]
 *          vide, explication, exemple, à retenir
 *
 * Ce qu'il ne mesure PAS : la justesse pédagogique, la plausibilité d'un
 * distracteur, la valeur d'une réfutation. Aucune machine ne le peut.
 *
 * Usage : NODE_PATH=<node_modules> node audit_qcm_trois_themes.mjs [--csv]
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "playwright";

const RACINE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const THEMES = [
  "theme-1-objets-systemes-usages-interactions",
  "theme-2-structure-fonctionnement-comportement",
  "theme-3-creation-conception-realisation-innovations",
];
const ABSOLUS = /\b(toujours|jamais|systématiquement|il suffit de|tous les)\b/gi;

function trouver(dir, acc = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) trouver(p, acc);
    else if (/^qcm_.*\.html$/.test(e.name)) acc.push(p);
  }
  return acc;
}

const nav = await chromium.launch();
const lignes = [];

for (const theme of THEMES) {
  for (const abs of trouver(path.join(RACINE, theme)).sort()) {
    const ctx = await nav.newContext();
    const page = await ctx.newPage();
    const erreursJS = [];
    page.on("pageerror", e => erreursJS.push(String(e)));
    await page.goto(pathToFileURL(abs).href);
    await page.waitForTimeout(200);

    /* Toutes les banques ne portent pas le même nom de variable ni le même
       schéma : on tente le standard C9 (QUESTIONS avec o/r/d), puis les
       formes anciennes (Q avec e/x/f/t). Un QCM qu'on ne sait pas lire est
       déclaré tel quel — jamais compté comme sain. */
    const b = await page.evaluate(() => {
      const src = (typeof QUESTIONS !== "undefined" && Array.isArray(QUESTIONS)) ? QUESTIONS
                : (typeof Q !== "undefined" && Array.isArray(Q)) ? Q : null;
      if (!src) return null;
      return src.map(x => ({
        o: x.o || x.options || [],
        r: typeof x.r === "number" ? x.r : -1,
        d: x.d || null,
        expl: x.expl || x.e || "",
        ex: x.ex || x.x || "",
        err: Object.prototype.hasOwnProperty.call(x, "err") ? x.err : (x.f !== undefined ? x.f : undefined),
        aErr: Object.prototype.hasOwnProperty.call(x, "err") || Object.prototype.hasOwnProperty.call(x, "f"),
        ret: x.ret || x.t || "",
        img: !!x.img,
        alt: x.img && x.img.alt ? x.img.alt.length : 0,
      }));
    });
    const gardeErr = await page.evaluate(() =>
      /Q\.err\s*\?|x\.f\s*\?/.test(document.documentElement.innerHTML));
    await ctx.close();

    const rel = path.relative(RACINE, abs);
    if (!b) { lignes.push({ rel, theme, lisible: false }); continue; }

    const n = b.length;
    const nu = t => String(t).replace(/<[^>]+>/g, "");
    let plusLongue = 0, visible = 0;
    const pos = [0, 0, 0, 0];
    for (const q of b) {
      const L = q.o.map(t => nu(t).length);
      if (q.r >= 0) {
        pos[q.r]++;
        const autres = L.filter((_, k) => k !== q.r);
        if (L[q.r] === Math.max(...L)) plusLongue++;
        if (L[q.r] > 1.2 * Math.max(...autres)) visible++;
      }
    }
    const sansRefut = b.filter(q => !Array.isArray(q.d) || q.d.length !== q.o.length).length;
    const refutTrouee = b.filter(q => Array.isArray(q.d)
      && q.d.some((t, k) => k !== q.r && !t)).length;
    const drNonVide = b.filter(q => Array.isArray(q.d) && q.r >= 0 && q.d[q.r] !== "").length;
    const errAbsent = b.filter(q => !q.aErr || q.err === undefined || q.err === "").length;
    const incomplets = b.filter(q => !q.expl || !q.ex || !q.ret).length;
    let absolus = 0;
    for (const q of b) {
      const textes = [q.ret].concat(Array.isArray(q.d) ? q.d : []);
      for (const t of textes) absolus += (String(t).match(ABSOLUS) || []).length;
    }
    const illustrees = b.filter(q => q.img).length;
    const altCourts = b.filter(q => q.img && q.alt <= 40).length;

    lignes.push({
      rel, theme, lisible: true, n,
      plusLongue, pctLong: Math.round(100 * plusLongue / n), visible,
      pos: pos.join("/"), minPos: Math.min(...pos),
      sansRefut, refutTrouee, drNonVide, incomplets,
      errAbsent, gardeErr, undefinedAffiche: (!gardeErr && errAbsent > 0) ? errAbsent : 0,
      absolus, illustrees, altCourts, erreursJS: erreursJS.length,
    });
  }
}
await nav.close();

/* ── rapport ── */
const p = (s, n) => String(s).padEnd(n);
const pr = (s, n) => String(s).padStart(n);
console.log("\n" + p("QCM", 52) + pr("q", 4) + pr("+long", 7) + pr("visib", 6)
  + pr("A/B/C/D", 12) + pr("undef", 7) + pr("absol", 6) + pr("img", 5) + pr("incompl", 9));
console.log("─".repeat(108));
let theme = "";
for (const l of lignes) {
  if (l.theme !== theme) { theme = l.theme; console.log("\n▸ " + theme); }
  if (!l.lisible) { console.log("  " + p(path.basename(l.rel), 50) + "  banque non lisible par cet outil"); continue; }
  console.log("  " + p(path.basename(l.rel).slice(0, 49), 50) + pr(l.n, 4)
    + pr(l.pctLong + "%", 7) + pr(l.visible, 6) + pr(l.pos, 12)
    + pr(l.undefinedAffiche || "·", 7) + pr(l.absolus || "·", 6)
    + pr(l.illustrees || "·", 5) + pr(l.incomplets || "·", 9));
}

const ok = lignes.filter(l => l.lisible);
const tot = ok.reduce((s, l) => s + l.n, 0);
const totLong = ok.reduce((s, l) => s + l.plusLongue, 0);
const totVis = ok.reduce((s, l) => s + l.visible, 0);
const totUndef = ok.reduce((s, l) => s + l.undefinedAffiche, 0);
const sansD = ok.filter(l => l.sansRefut === l.n).length;

console.log("\n" + "═".repeat(108));
console.log("%d QCM lus · %d questions", ok.length, tot);
console.log("« cocher la plus longue » réussit : %d/%d = %d %%  (hasard : 25 %%)",
  totLong, tot, Math.round(100 * totLong / tot));
console.log("bonne réponse VISIBLEMENT la plus longue (+20 %%) : %d questions", totVis);
console.log("questions affichant « undefined » dans leur correction : %d", totUndef);
console.log("QCM sans aucune réfutation par distracteur (ancienne génération) : %d", sansD);

if (process.argv.includes("--csv")) {
  const csv = ["fichier;theme;questions;plus_longue;pct_plus_longue;visiblement_plus_longue;"
    + "repartition;undefined_affiche;absolus;illustrees;incompletes;sans_refutation"]
    .concat(ok.map(l => [l.rel, l.theme, l.n, l.plusLongue, l.pctLong, l.visible,
      l.pos, l.undefinedAffiche, l.absolus, l.illustrees, l.incomplets, l.sansRefut].join(";")));
  fs.writeFileSync(path.join(path.dirname(fileURLToPath(import.meta.url)), "audit_qcm_trois_themes.csv"), csv.join("\n") + "\n", "utf-8");
  console.log("\naudit_qcm_trois_themes.csv écrit");
}
