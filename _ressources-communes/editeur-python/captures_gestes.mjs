#!/usr/bin/env node
/* captures_gestes.mjs — les captures de l'encart « les quatre gestes de l'éditeur Python », page par page.
 *
 * Quand le code de départ d'un exercice est la réponse à écrire, la capture montre un petit programme d'essai
 * (`exemple`) : l'échauffement ne donne pas la solution de l'activité.
 * Captures d'écran réelles de la page elle-même (Chromium piloté par Playwright, thème de la page, 1280 px de
 * large) : l'éditeur avant ▶ (geste 1), après ▶ (1b), le nom du fichier (2), après ⬇ (3), après 📂 sur une
 * page rouverte et sans sauvegarde, comme la semaine suivante (4). Elles sont écrites dans le dossier Images/
 * de chaque page, et les attributs width/height de leurs <img> sont remis à leur taille réelle.
 * Les fenêtres de Windows (Explorateur, « Ouvrir ») ne se fabriquent pas ici : l'encart reprend celles qui
 * existent, et décrit en mots celle qui manque.
 *
 * Depuis le 05/11/2026, l'encart a son propre éditeur d'essai (voir LISEZMOI.md, « L'échauffement ») : ces captures
 * ne sont plus affichées dans les pages. Le script reste, pour refaire une capture de l'éditeur si une fiche papier
 * ou une synthèse en a besoin.
 *
 * Usage : node _ressources-communes/editeur-python/captures_gestes.mjs [code_de_page …]   (toutes par défaut)
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "playwright";

const ICI = path.dirname(fileURLToPath(import.meta.url));
const DEPOT = path.dirname(path.dirname(ICI));
const T2 = "theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe";
const T3 = "theme-3-creation-conception-realisation-innovations";
export const PAGES = [
  { code: "3e_C9.1", page: `${T3}/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/sequence_3e_C9.1_variables_types_systemes.html`,
    onglet: "#tab-s2", bloc: "vs1", fichier: "3e-VARIABLES-act3-DUPONT" },
  { code: "5e_C9.1", page: `${T3}/C9-concevoir-ecrire-tester-et-mettre-au-point/5e/5e_C9.1/sequence_5e_C9.1-C9.3_boite_etiquetee.html`,
    onglet: "#tab-s2", bloc: "vs1", fichier: "5e-BOITE-act3-DUPONT" },
  { code: "4e_C9.1", page: `${T3}/C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.1/sequence_4e_C9_jardin-programme.html`,
    onglet: "#tab-s2", bloc: "edpy-a3", fichier: "4e-JARDIN-DUPONT",
    exemple: 'H = 25\nheure = 8\nprint("H =", H, "% ; il est", heure, "h")\n' },
  { code: "4e_C6.2", page: `${T2}/4e/4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html`,
    onglet: null, bloc: "vs1", fichier: "4e-ARROSAGE-act3-DUPONT",
    exemple: 'h = lire_capteur_pourcent(A0)\nprint("Le sol est à", h, "%")\n' },
  { code: "3e_C7.1", page: `${T3}/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/sequence_3e_C7_capteur-confort-ny.html`,
    onglet: "#tab-s2", bloc: "vs1", fichier: "3e-CAPTEUR-DUPONT",
    exemple: 'seuil = 28\nT = 32\nprint("T =", T, "°C ; seuil =", seuil, "°C")\n' },
  { code: "5e_C7.1", page: `${T3}/C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.1/sequence_5e_C7_mini-projet-objet.html`,
    onglet: "#tab-s2", bloc: "vs1", fichier: "5e-HALL-DUPONT",
    exemple: 'occupee = True\nprint("La case est occupée :", occupee)\n' },
];

const NOMS = ["geste_editeur_1_ecrire.png", "geste_editeur_1b_executer.png", "geste_editeur_2_nommer.png",
              "geste_editeur_3_telecharger.png", "geste_editeur_4_retrouver.png"];

function taillePng(f) { const b = fs.readFileSync(f); return [b.readUInt32BE(16), b.readUInt32BE(20)]; }

async function capturer(nav, cfg) {
  const fichierPage = path.join(DEPOT, cfg.page);
  if (!fs.existsSync(fichierPage)) { console.log("⚠ page absente : " + cfg.page); return; }
  const images = path.join(path.dirname(fichierPage), "Images");
  const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1, acceptDownloads: true });
  await ctx.route(/^https?:/, (r) => r.abort());
  const p = await ctx.newPage();
  await p.goto(pathToFileURL(fichierPage).href, { waitUntil: "load" });
  await p.evaluate(() => localStorage.clear());
  await p.reload({ waitUntil: "load" });
  const sel = "#" + cfg.bloc;
  const ouvrirSeance = async () => {
    if (cfg.onglet) { await p.click(cfg.onglet); await p.waitForTimeout(300); }
    await p.waitForSelector(sel + ".editeur-py--actif");
    await p.locator(sel).scrollIntoViewIfNeeded();
  };
  await ouvrirSeance();
  const bloc = p.locator(sel);
  // un petit programme d'essai, quand le code de départ est la réponse à écrire (on ne la montre pas dans l'échauffement)
  if (cfg.exemple) await p.evaluate(([s, c]) => { const t = document.querySelector(s + " textarea"); t.value = c; t.dispatchEvent(new Event("input", { bubbles: true })); }, [sel, cfg.exemple]);
  const fin = async (action) => {
    const n = await p.evaluate(() => (window.__finsCap = window.__finsCap || 0));
    await p.evaluate(() => { if (!window.__ecouteCap) { window.__ecouteCap = 1; document.addEventListener("editeur-py:fin", () => { window.__finsCap++; }); } });
    await action();
    if (cfg.arreterApres) { await p.waitForTimeout(cfg.arreterApres); await p.click(sel + " .editeur-py-arreter").catch(() => {}); }
    await p.waitForFunction((k) => window.__finsCap > k, n, { timeout: 30000 });
    await p.waitForTimeout(150);
  };
  const out = (i) => path.join(images, NOMS[i]);
  await bloc.screenshot({ path: out(0) });
  await fin(() => p.click(sel + " .editeur-py-executer"));
  await bloc.screenshot({ path: out(1) });
  await p.fill(sel + " .editeur-py-nom", cfg.fichier);
  await p.locator(sel + " .editeur-py-fichier").screenshot({ path: out(2) });
  const [dl] = await Promise.all([p.waitForEvent("download"), p.click(sel + " .editeur-py-telecharger")]);
  const dossierTmp = fs.mkdtempSync(path.join(os.tmpdir(), "captures-gestes-"));
  const tmp = path.join(dossierTmp, dl.suggestedFilename());
  await dl.saveAs(tmp);
  await p.waitForTimeout(150);
  await bloc.screenshot({ path: out(3) });
  // la semaine suivante : une page sans sauvegarde, puis 📂
  await p.evaluate(() => localStorage.clear());
  await p.reload({ waitUntil: "load" });
  await ouvrirSeance();
  await p.setInputFiles(sel + " .editeur-py-choix", tmp);
  await p.waitForFunction((s) => /est ouvert/.test(document.querySelector(s + " .editeur-py-etat").textContent), sel);
  await bloc.screenshot({ path: out(4) });
  fs.rmSync(dossierTmp, { recursive: true, force: true });
  await p.evaluate(() => localStorage.clear());
  await ctx.close();
  // les attributs width/height des <img>, à la taille réelle
  let html = fs.readFileSync(fichierPage, "utf8"), n = 0;
  for (const nom of NOMS) {
    const [l, h] = taillePng(path.join(images, nom));
    html = html.replace(new RegExp('(<img src="Images/' + nom.replace(/\./g, "\\.") + '" )width="\\d+" height="\\d+"', "g"),
      (m, a) => { n++; return a + 'width="' + l + '" height="' + h + '"'; });
  }
  fs.writeFileSync(fichierPage, html);
  console.log("✅ " + cfg.code + " : " + NOMS.length + " captures, " + n + " balise(s) <img> mises à la taille réelle");
}

const voulus = process.argv.slice(2);
const nav = await chromium.launch();
for (const cfg of PAGES) if (!voulus.length || voulus.includes(cfg.code)) await capturer(nav, cfg);
await nav.close();
