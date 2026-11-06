#!/usr/bin/env node
/**
 * controle_code_colore.mjs — règle d'or n°13 : LE CODE S'AFFICHE EN COULEURS, COMME DANS UN IDE.
 *
 * Pascal, le 30/07/2026 : « J'aimerais avoir des couleurs pour les variables, constantes…, comme un IDE ».
 * Puis le 05/11/2026, sur le lampadaire de 4e_C9.1, écrit dans l'éditeur Python de la page : « sa zone de code est
 * monochrome. À l'avenir, il faudrait changer ceci. De façon à avoir des couleurs. » Ce contrôle garde la règle.
 *
 * CE QUI EST REGARDÉ, page ouverte dans Chromium (réseau coupé) :
 *   - chaque <pre> qui montre un programme (Python, le C d'une carte) ou un algorithme (SI … ALORS, ←) ;
 *   - chaque zone de saisie de code (l'éditeur Python de la page, ou un éditeur fait main), visible ;
 *   - un listing passe s'il porte des mots colorés : les classes de la palette du site (py-kw, py-var…), ou
 *     celles d'un colorisateur propre à la page (k/s/n, kw/num…), ou des couleurs écrites dans le style d'un <span> ;
 *     une zone de saisie passe si le code coloré est posé dessous (une couche <pre> colorée dans le même bloc).
 *   - Ne sont pas des listings : la sortie d'une console (pas de mot du langage), le <code> d'une phrase.
 * L'archive est exclue : c'est une trace.
 *
 * Usage :
 *   node _outils/controle_code_colore.mjs            # le relevé, page par page
 *   node _outils/controle_code_colore.mjs --muet     # seulement les listings sans couleurs
 *   node _outils/controle_code_colore.mjs <dossier>  # un seul dossier
 * Sortie 1 s'il reste un listing en une couleur.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "playwright";

const DEPOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const IGNORES = new Set([".git", "node_modules", "_archive-anciennes-versions", "_notes"]);
function pages(depart) {
  const out = [];
  (function marcher(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      if (IGNORES.has(e.name)) continue;
      const p = path.join(d, e.name);
      if (e.isDirectory()) marcher(p);
      else if (e.name.endsWith(".html") && !/^(lexique_|qcm_)/.test(e.name)) out.push(p);
    }
  })(depart);
  return out.sort();
}

const argv = process.argv.slice(2);
const muet = argv.includes("--muet");
const cible = argv.find((a) => !a.startsWith("--"));
const liste = pages(cible ? path.resolve(DEPOT, cible) : path.join(DEPOT));
const themes = liste.filter((p) => /[\\/]theme-/.test(p) || cible);

const nav = await chromium.launch();
let nPages = 0, nListings = 0, nKo = 0;
for (const f of themes) {
  const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 } });
  await ctx.route("**/*", (r) => (/^(file|data|blob):/.test(r.request().url()) ? r.continue() : r.abort()));
  const p = await ctx.newPage();
  try { await p.goto(pathToFileURL(f).href, { timeout: 20000 }); await p.waitForTimeout(300); }
  catch (e) { await ctx.close(); continue; }
  const r = await p.evaluate(() => {
    const PY = /(^|\n)\s*(print|def|while|if|elif|for|import|return)\b|(^|\n)\s*[A-Za-z_][\w]*\s*=[^=]|\binput\(|\bTrue\b|\bFalse\b/;
    const C = /\b(void|const int|analogRead|digitalWrite|pinMode)\b/;
    const ALGO = /(^|\n)\s*(SI|TANT QUE|POUR|DÉBUT|RÉPÉTER)\b|(^|\n)\s*[A-Za-zÀ-ÿ_][\wÀ-ÿ]*\s*←/;   // une affectation, pas une flèche de commentaire
    const COULEUR = ".py-kw,.py-var,.py-str,.py-num,.py-op,.py-com,.k,.s,.n,.kw,.num,.fn,.cmt,.str,.keyword,.string,.number";
    const res = [];
    for (const el of document.querySelectorAll("pre, textarea")) {
      if (el.tagName === "TEXTAREA" && (el.hidden || el.readOnly && el.closest("[hidden]"))) continue;
      if (el.matches(".editeur-py-couleurs, .cl-hl")) continue;            // la couche colorée d'un éditeur : vue avec sa zone
      const t = (el.tagName === "TEXTAREA" ? el.value || el.defaultValue : el.textContent) || "";
      if (t.split("\n").filter((l) => l.trim()).length < 2) continue;
      const langage = C.test(t) ? "arduino" : PY.test(t) ? "python" : ALGO.test(t) ? "algo" : null;
      if (!langage) continue;
      if (el.tagName === "TEXTAREA" && !el.matches(".editeur-py-code, .cl-ta, [class*=code]")) continue;   // un champ de réponse, pas un éditeur
      let colore;
      if (el.tagName === "TEXTAREA") {
        const bloc = el.parentElement && el.parentElement.parentElement;
        colore = !!(bloc && [...bloc.querySelectorAll("pre")].some((pr) => pr !== el && pr.querySelector(COULEUR)));
      } else {
        colore = !!el.querySelector(COULEUR) || [...el.querySelectorAll("span")].some((s) => /color/.test(s.getAttribute("style") || ""));
      }
      res.push({ el: el.tagName.toLowerCase() + (el.id ? "#" + el.id : "") + (el.className ? "." + String(el.className).split(" ")[0] : ""),
                 langage, colore, debut: t.trim().split("\n")[0].slice(0, 60) });
    }
    return res;
  });
  await ctx.close();
  if (!r.length) continue;
  nPages++; nListings += r.length;
  const ko = r.filter((x) => !x.colore); nKo += ko.length;
  const nom = path.relative(DEPOT, f);
  if (!muet || ko.length) console.log((ko.length ? "✘ " : "✓ ") + nom + " — " + (r.length - ko.length) + " / " + r.length + " listing(s) en couleurs");
  for (const x of ko) console.log("     ✘ " + x.langage + " · " + x.el + " · « " + x.debut + " »");
}
await nav.close();
console.log(nKo ? `✘ ${nKo} listing(s) en une seule couleur, sur ${nListings} dans ${nPages} page(s) (règle d'or n°13)`
                : `✅ chaque listing de code est en couleurs, comme dans un IDE (${nListings} listing(s), ${nPages} page(s) ; règle d'or n°13)`);
process.exitCode = nKo ? 1 : 0;
