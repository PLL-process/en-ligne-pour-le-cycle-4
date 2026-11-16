#!/usr/bin/env node
/* captures_corrections.mjs — la production complète, telle que l'éditeur Python de la page la rend (règle d'or n°332).
 *
 * Demande de Pascal du 15/11/2026 : la correction montre la production complète, faite avec l'outil que l'élève
 * découvre, et donne son fichier. Pour un programme, l'outil est l'éditeur Python de la page : ce script y charge le
 * programme corrigé (`corriges_py/*.py` du lot, le fichier que l'élève télécharge depuis la correction), clique
 * ▶ Exécuter, attend la fin, et photographie l'éditeur, console comprise. Captures d'écran réelles de la page elle-même
 * (Chromium piloté par Playwright, 1 280 px de large), écrites dans le dossier Images/ de la page ; les attributs
 * width/height de leurs <img> sont remis à la taille réelle.
 *
 * L'encart « les quatre gestes » n'a pas de capture : depuis le 05/11/2026, l'éditeur y est en vrai, jamais en image.
 *
 * Usage : node _ressources-communes/editeur-python/captures_corrections.mjs [code_de_page …]   (toutes par défaut)
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "playwright";

const ICI = path.dirname(fileURLToPath(import.meta.url));
const DEPOT = path.dirname(path.dirname(ICI));
const C9 = "theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point";
// py : le programme chargé avant ▶ (null : le code de départ de l'éditeur, qui est déjà la production attendue)
export const CAPTURES = [
  { code: "3e_C9.1", page: `${C9}/3e/3e_C9.1/sequence_3e_C9.1_variables_types_systemes.html`, onglet: "#tab-s2", bloc: "vs1", py: null, image: "correction_editeur_act3.png" },
  { code: "3e_C9.1", page: `${C9}/3e/3e_C9.1/sequence_3e_C9.1_variables_types_systemes.html`, onglet: "#tab-s3", bloc: "vs2", py: "corriges_py/3e-VARIABLES-act4-correction.py", image: "correction_editeur_act4.png" },
  { code: "3e_C9.1", page: `${C9}/3e/3e_C9.1/sequence_3e_C9.1_variables_types_systemes.html`, onglet: "#tab-s4", bloc: "vs3", py: "corriges_py/3e-VARIABLES-act5-correction.py", image: "correction_editeur_act5.png" },
  { code: "3e_C9.1", page: `${C9}/3e/3e_C9.1/sequence_3e_C9.1_variables_types_systemes.html`, onglet: "#tab-s4", bloc: "vs4", py: "corriges_py/3e-VARIABLES-bonus-correction.py", image: "correction_editeur_bonus.png" },
  { code: "4e_C9.1", page: `${C9}/4e/4e_C9.1/sequence_4e_C9_jardin-programme.html`, onglet: "#tab-s2", bloc: "edpy-a3", py: "corriges_py/4e-JARDIN-correction.py", image: "correction_editeur_act3.png" },
  { code: "4e_C9.1", page: `${C9}/4e/4e_C9.1/sequence_4e_C9_jardin-programme.html`, onglet: "#tab-s3", bloc: "edpy-a6", py: "corriges_py/4e-LAMPADAIRE-correction.py", image: "correction_editeur_act6.png" },
];

function taillePng(f) { const b = fs.readFileSync(f); return [b.readUInt32BE(16), b.readUInt32BE(20)]; }

async function capturer(nav, cfg) {
  const fichierPage = path.join(DEPOT, cfg.page);
  const dossier = path.dirname(fichierPage);
  const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
  await ctx.route(/^https?:/, (r) => r.abort());
  const p = await ctx.newPage();
  await p.goto(pathToFileURL(fichierPage).href, { waitUntil: "load" });
  await p.evaluate(() => localStorage.clear());
  await p.reload({ waitUntil: "load" });
  const sel = "#" + cfg.bloc;
  if (cfg.onglet) { await p.click(cfg.onglet); await p.waitForTimeout(300); }
  // un éditeur replié dans un dépliant (le Bonus) : on ouvre ses dépliants
  await p.evaluate((s) => { let d = document.querySelector(s); while (d) { if (d.tagName === "DETAILS") d.open = true; d = d.parentElement; } }, sel);
  await p.waitForSelector(sel + ".editeur-py--actif", { timeout: 15000 });
  await p.locator(sel).scrollIntoViewIfNeeded();
  if (cfg.py) {
    const code = fs.readFileSync(path.join(dossier, cfg.py), "utf8");
    await p.evaluate(([s, c]) => { const t = document.querySelector(s + " textarea"); t.value = c; t.dispatchEvent(new Event("input", { bubbles: true })); }, [sel, code]);
  }
  await p.evaluate(() => { window.__fins = 0; document.addEventListener("editeur-py:fin", () => { window.__fins++; }); });
  await p.click(sel + " .editeur-py-executer");
  await p.waitForFunction(() => window.__fins > 0, null, { timeout: 60000 });
  await p.waitForTimeout(300);
  const sortie = path.join(dossier, "Images", cfg.image);
  await p.locator(sel).screenshot({ path: sortie });
  const console_ = await p.evaluate((s) => (document.querySelector(s + " .editeur-py-sortie") || {}).textContent || "", sel);
  await ctx.close();
  let html = fs.readFileSync(fichierPage, "utf8");
  const [l, h] = taillePng(sortie);
  html = html.replace(new RegExp('(<img src="Images/' + cfg.image.replace(/\./g, "\\.") + '" )width="\\d+" height="\\d+"', "g"), (m, a) => a + 'width="' + l + '" height="' + h + '"');
  fs.writeFileSync(fichierPage, html);
  console.log("✅ " + cfg.code + " · " + cfg.image + " (" + l + " × " + h + ") — console : " + JSON.stringify(console_.trim().slice(0, 160)));
}

const voulus = process.argv.slice(2);
const nav = await chromium.launch();
for (const cfg of CAPTURES) if (!voulus.length || voulus.includes(cfg.code)) await capturer(nav, cfg);
await nav.close();
