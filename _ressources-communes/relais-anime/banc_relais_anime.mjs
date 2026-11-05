#!/usr/bin/env node
/* banc_relais_anime.mjs — le banc du relais qui claque (05/11/2026).
 * Usage : node _ressources-communes/relais-anime/banc_relais_anime.mjs
 * Ouvre les pages qui portent la figure (relais_figure.py, PAGES) et vérifie : la figure à jour, l'animation, les
 * boutons, le son facultatif, 390 px, l'impression, sans JavaScript, hors ligne. */
import { chromium } from "playwright";
import { execFileSync } from "node:child_process";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const ICI = path.dirname(fileURLToPath(import.meta.url));
const DEPOT = path.dirname(path.dirname(ICI));
const T3 = "theme-3-creation-conception-realisation-innovations/";
const PAGES = [
  T3 + "C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.4/sequence_4e_C7.4_energie-du-jardin.html",
  T3 + "C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.5/sequence_4e_C7.5_jardin-incomplet.html",
  T3 + "C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.1/sequence_4e_C9_jardin-programme.html",
  "theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/4e/4e_C6.1/sequence_4e_C6.1-C6.3_ajuster_programme_jardin.html",
];
let nOk = 0, nKo = 0;
function ok(nom, cond, detail = "") {
  if (cond) nOk++; else { nKo++; process.exitCode = 1; }
  console.log((cond ? "✅ " : "❌ ") + nom + (detail ? " — " + detail : ""));
}

/* 0. la figure écrite dans chaque page est celle du générateur */
let aJour = true, sortie = "";
try { sortie = execFileSync("python3", [path.join(ICI, "relais_figure.py")], { encoding: "utf8" }); } catch (e) { aJour = false; sortie = String(e.stdout || e); }
ok("relais_figure.py : la figure de chaque page est à jour", aJour && (sortie.match(/✓ à jour/g) || []).length === PAGES.length, sortie.trim().split("\n").join(" · "));

const nav = await chromium.launch();
const reseau = [];
async function ouvrir(chemin, opts = {}) {
  const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 }, ...opts });
  await ctx.route("**/*", (r) => { const u = r.request().url(); if (/^(file|data|blob):/.test(u)) return r.continue(); reseau.push(u); return r.abort(); });
  const p = await ctx.newPage(); p.erreurs = []; p.on("pageerror", (e) => p.erreurs.push(e.message));
  await p.goto(pathToFileURL(path.join(DEPOT, chemin)).href);
  return { ctx, p };
}
const F = "figure.relais-anime";

for (const chemin of PAGES) {
  const nom = chemin.split("/")[3] || chemin;
  const { ctx, p } = await ouvrir(chemin);
  const etat0 = await p.evaluate((F) => { const f = document.querySelector(F); return f && {
    actif: f.classList.contains("ra-actif"), ferme: f.classList.contains("ra-ferme"),
    boutons: !f.querySelector(".ra-commandes").hidden, svg: !!f.querySelector("svg[role=img] title"),
    statut: f.querySelector(".ra-etat").getAttribute("role") }; }, F);
  ok(nom + " · la figure est montée, au repos, avec ses boutons et un statut annoncé", etat0 && etat0.actif && !etat0.ferme && etat0.boutons && etat0.svg && etat0.statut === "status", JSON.stringify(etat0));
  // ouvrir ce qui cache la figure (onglet, aide repliée) : comme l'élève
  await p.evaluate((F) => { const f = document.querySelector(F); let e = f; while (e) { if (e.tagName === "DETAILS") e.open = true; e = e.parentElement; }
    const pan = f.closest("[role=tabpanel]"); if (pan) { const t = document.querySelector('[aria-controls="' + pan.id + '"]') || document.getElementById("tab-" + pan.id); if (t) t.click(); } }, F);
  await p.click(F + " .ra-envoyer");
  const apres = await p.evaluate((F) => { const f = document.querySelector(F); return { ferme: f.classList.contains("ra-ferme"),
    ordre: f.querySelector(".ra-ordre").textContent, etat: f.querySelector(".ra-etat").textContent,
    clac: f.querySelector(".ra-clac").classList.contains("ra-clac-vu") }; }, F);
  ok(nom + " · « La carte envoie l'ordre » : la lame se ferme, « clac », l'ordre passe à 1, le statut explique", apres.ferme && apres.clac && /1 \(envoyé\)/.test(apres.ordre) && /Clac !.*bobine.*aimant/.test(apres.etat) && /1 clac jusqu'ici/.test(apres.etat), apres.etat.slice(0, 90));
  await p.click(F + " .ra-envoyer");
  ok(nom + " · un second « envoyer » ne fait pas de clac (rien ne bouge)", /déjà envoyé/.test(await p.textContent(F + " .ra-etat")) && !/2 clacs/.test(await p.textContent(F + " .ra-etat")));
  await p.click(F + " .ra-couper");
  ok(nom + " · « La carte coupe l'ordre » : le ressort relève la lame, deuxième clac", !(await p.evaluate((F) => document.querySelector(F).classList.contains("ra-ferme"), F)) && /ressort relève la lame.*2 clacs/.test(await p.textContent(F + " .ra-etat")));
  if (chemin === PAGES[0]) {
    await p.click(F + " .ra-battre");
    ok("« Faire battre 6 fois » : le bouton se grise pendant le battement", await p.locator(F + " .ra-battre").isDisabled());
    await p.waitForFunction((F) => /Six allumages, six arrêts/.test(document.querySelector(F + " .ra-etat").textContent), F, { timeout: 15000 });
    ok("« Faire battre 6 fois » : douze clacs de plus, l'usure et les à-coups sont dits, la pompe finit arrêtée",
       /14 clacs jusqu'ici/.test(await p.textContent(F + " .ra-etat")) && !(await p.evaluate((F) => document.querySelector(F).classList.contains("ra-ferme"), F)),
       await p.textContent(F + " .ra-etat"));
    const son = await p.evaluate((F) => { const b = document.querySelector(F + " .ra-son"); const a = b.getAttribute("aria-pressed"); b.click(); return [a, b.getAttribute("aria-pressed"), b.textContent]; }, F);
    ok("le son est coupé par défaut, et se rallume par son bouton (aria-pressed)", son[0] === "false" && son[1] === "true" && /Son activé/.test(son[2]), son.join(" · "));
    const cibles = await p.$$eval(F + " .ra-btn", (l) => l.filter((b) => b.getBoundingClientRect().height < 44).length);
    ok("toutes les cibles font au moins 44 px", cibles === 0, cibles + " trop petite(s)");
    await p.emulateMedia({ media: "print" });
    const imp = await p.evaluate((F) => { const f = document.querySelector(F); return { cmd: getComputedStyle(f.querySelector(".ra-commandes")).display, svg: getComputedStyle(f.querySelector("svg")).display }; }, F);
    ok("à l'impression : le schéma reste, les boutons disparaissent", imp.cmd === "none" && imp.svg !== "none", JSON.stringify(imp));
    await p.emulateMedia({ media: "screen" });
  }
  ok(nom + " · zéro erreur JavaScript", p.erreurs.length === 0, p.erreurs.join(" | "));
  await ctx.close();
}

/* 390 px */
{
  const { ctx, p } = await ouvrir(PAGES[0], { viewport: { width: 390, height: 844 } });
  const d = await p.evaluate((F) => { const f = document.querySelector(F); const r = f.getBoundingClientRect(); return { deb: document.documentElement.scrollWidth - innerWidth, larg: r.width, svg: f.querySelector("svg").getBoundingClientRect().width }; }, F);
  ok("390 px : aucun défilement de côté ; le schéma tient dans la largeur", d.deb <= 0 && d.svg <= d.larg, JSON.stringify(d));
  await ctx.close();
}
/* sans JavaScript */
{
  const { ctx, p } = await ouvrir(PAGES[0], { javaScriptEnabled: false });
  const s = await p.evaluate((F) => { const f = document.querySelector(F); return { cmd: f.querySelector(".ra-commandes").hidden, svg: !!f.querySelector("svg"), texte: f.querySelector(".ra-explique").textContent.length }; }, F);
  ok("sans JavaScript : le schéma au repos et son explication restent ; pas de boutons morts", s.cmd && s.svg && s.texte > 200, JSON.stringify(s));
  await ctx.close();
}
ok("hors ligne : aucune requête vers le réseau", reseau.length === 0, reseau.slice(0, 3).join(" | "));
await nav.close();
console.log(`\n${nOk} / ${nOk + nKo} vérifications passées`);
