#!/usr/bin/env node
/* Mesures des règles d'or RÉCENTES sur toutes les séquences du dépôt.

   Ces règles-là ne se vérifient pas dans la source : elles se vérifient au
   RENDU. C'est tout leur objet.

     n°135  un tableau visible a-t-il une séparation lisible ?
     n°135b la page déborde-t-elle horizontalement à 390 px ?
     n°136  un dispositif présent a-t-il un effet MESURABLE ?
            (sélecteur de parcours, mode essentiel, boutons de séance)
     n°137  les bonnes réponses du QCM sont-elles réparties ?  (traité à part)

   ATTENTION — trois pièges de mesure, payés en fausses alertes le 27/08/2026 :

     1. toutes les pages file:// partagent le MÊME localStorage : une séquence
        qui enregistre « parcours = c » contamine la suivante. On vide donc le
        stockage avant chaque séquence ;
     2. un bloc rangé dans un onglet inactif est déjà invisible : le compter
        comme « masqué par le dispositif » accuse des pages saines ;
     3. c'est le `display` PROPRE de la cible qu'il faut lire — il ne dépend pas
        de celui de ses ancêtres —, et non sa visibilité à l'écran.

   Sans ces trois précautions, le balayage annonçait neuf défauts là où il y en
   avait six.

   Sortie : un tableau par séquence, et un décompte final.
   Usage : node _outils/mesures_rendu.mjs [racine]                            */
import fs from "node:fs";
import path from "node:path";
import { chromium } from "playwright";

const RACINE = path.resolve(process.argv[2] || ".");
const seqs = [];
(function walk(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) { if (!/^_archive|node_modules|^\.git/.test(e.name)) walk(p); }
    else if (/^sequence[-_].*\.html$/.test(e.name)) seqs.push(p);
  }
})(RACINE);
seqs.sort();

const nav = await chromium.launch();
const ctxD = await nav.newContext({ viewport: { width: 1280, height: 900 } });
const ctxM = await nav.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
const lignes = [];

for (const f of seqs) {
  const rel = f.slice(RACINE.length + 1);
  const page = await ctxD.newPage();
  const erreurs = [];
  page.on("pageerror", e => erreurs.push(String(e)));
  try {
    /* PIÈGE, trouvé en cours de balayage : toutes les séquences ouvertes en
       file:// partagent la MÊME origine, donc le MÊME localStorage. Une page
       qui a enregistré « parcours = c » ou « essentiel = 1 » contamine la
       suivante, qui se charge déjà dans cet état — et la mesure de l'effet
       d'un dispositif donne alors zéro pour une page parfaitement saine.
       On repart donc d'un stockage vide pour CHAQUE séquence. */
    await page.goto("file://" + f, { timeout: 20000 });
    await page.evaluate(() => { try { localStorage.clear(); sessionStorage.clear(); } catch {} });
    await page.reload({ timeout: 20000 });
    await page.waitForTimeout(350);
  } catch (e) { lignes.push({ rel, erreur: "chargement : " + e.message.slice(0, 60) }); await page.close(); continue; }

  /* n°135 — tableaux visibles sans séparation lisible */
  const tables = await page.evaluate(() => {
    const vus = [...document.querySelectorAll("table")].filter(t => t.offsetParent !== null);
    let nus = 0;
    for (const t of vus) {
      const c = t.querySelector("td, th"); if (!c) continue;
      const s = getComputedStyle(c);
      const bords = [s.borderBottomWidth, s.borderLeftWidth, s.borderTopWidth, s.borderRightWidth].map(v => parseFloat(v) || 0);
      const tr = t.querySelector("tr");
      const fond = tr ? getComputedStyle(tr).backgroundColor : "rgba(0, 0, 0, 0)";
      if (bords.every(v => v === 0) && (fond === "rgba(0, 0, 0, 0)" || fond === "transparent")) nus++;
    }
    return { total: vus.length, nus };
  });

  /* n°136 — les dispositifs présents ont-ils un effet mesurable ? */
  const dispositifs = await page.evaluate(() => {
    const r = {};
    r.parcoursBoutons = document.querySelectorAll(".parcours-btn").length;
    r.parcoursCibles = document.querySelectorAll("[data-parcours]").length;
    const btnE = document.getElementById("btnEssentiel");
    r.essentielBouton = !!btnE;
    r.essentielCibles = document.querySelectorAll(
      ".referentiel-card, details.correction, .approfondissement, .prof").length;
    r.versSeance = document.querySelectorAll(".vers-seance").length;
    r.ongletsSeance = document.querySelectorAll(".seance-tab").length;
    r.taches = document.querySelectorAll("#tachesBandeau .tache").length;
    return r;
  });

  /* effet réel du sélecteur de parcours : combien de blocs disparaissent ? */
  let parcoursEffet = null;
  if (dispositifs.parcoursBoutons > 0) {
    try {
      await page.waitForSelector('.parcours-btn[data-choix="c"]', { timeout: 3000 });
      /* On ne compte QUE les blocs VISIBLES avant le clic : un bloc déjà caché
         (onglet inactif) ne prouve rien, ni dans un sens ni dans l'autre. */
      /* On mesure le display PROPRE de la cible, pas sa visibilité à l'écran :
         un bloc rangé dans un onglet inactif est invisible sans que le
         dispositif y soit pour rien. Le display propre d'un élément ne dépend
         pas de celui de ses ancêtres — c'est donc lui qui dit si la règle
         « masquer » s'applique vraiment. */
      const cpt = () => document.querySelectorAll('[data-parcours]:not([data-parcours="c"])').length
        - [...document.querySelectorAll('[data-parcours]:not([data-parcours="c"])')]
            .filter(e => getComputedStyle(e).display === "none").length;
      const avant = await page.evaluate(cpt);
      await page.click('.parcours-btn[data-choix="c"]');
      await page.waitForTimeout(200);
      const apres = await page.evaluate(cpt);
      parcoursEffet = { avant, apres, masques: avant - apres };
    } catch { parcoursEffet = { avant: 0, apres: 0, masques: 0, erreur: true }; }
  }

  /* effet réel du mode essentiel */
  let essentielEffet = null;
  if (dispositifs.essentielBouton) {
    /* Même précaution que pour le parcours : on ne compte que les cibles
       VISIBLES avant le clic. Une cible rangée dans un onglet inactif est
       déjà invisible, et ne prouve rien sur l'effet du mode essentiel. */
    const SEL = ".referentiel-card, details.correction, .approfondissement, .prof";
    const cpt = s => [...document.querySelectorAll(s)]
      .filter(e => getComputedStyle(e).display !== "none").length;
    const avant = await page.evaluate(cpt, SEL);
    await page.click("#btnEssentiel"); await page.waitForTimeout(200);
    const apres = await page.evaluate(cpt, SEL);
    essentielEffet = { avant, apres, masques: avant - apres };
  }
  await page.close();

  /* n°135b — débordement horizontal à 390 px */
  const pm = await ctxM.newPage();
  let debord = null;
  try {
    await pm.goto("file://" + f, { timeout: 20000 });
    await pm.evaluate(() => { try { localStorage.clear(); sessionStorage.clear(); } catch {} });
    await pm.reload({ timeout: 20000 });
    await pm.waitForTimeout(300);
    debord = await pm.evaluate(() =>
      Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth));
  } catch {}
  await pm.close();

  lignes.push({ rel, tables, dispositifs, parcoursEffet, essentielEffet, debord, erreurs: erreurs.length });
}
await nav.close();

/* ── rapport ── */
const pb = l => {
  const p = [];
  if (l.erreur) return [l.erreur];
  if (l.tables.nus > 0) p.push(`n°135 : ${l.tables.nus} tableau(x) sans séparation`);
  if (l.debord > 0) p.push(`n°135b : débord mobile ${l.debord} px`);
  if (l.dispositifs.parcoursBoutons > 0) {
    const e = l.parcoursEffet || {};
    if (e.erreur) p.push("n°136 : le bouton de parcours 🅲 est introuvable ou inatteignable");
    else if (e.avant === 0) p.push(`n°136 : sélecteur de parcours branché sur RIEN (aucun bloc à masquer, ${l.dispositifs.parcoursCibles} data-parcours en tout)`);
    else if (e.masques === 0) p.push(`n°136 : sélecteur de parcours sans effet (${e.avant} blocs visibles, 0 masqué)`);
  }
  if (l.dispositifs.essentielBouton) {
    const e = l.essentielEffet || {};
    if (e.avant === 0)
      p.push(`n°136 : mode essentiel branché sur RIEN (${l.dispositifs.essentielCibles} cibles, toutes déjà en display:none)`);
    else if (e.masques === 0)
      p.push(`n°136 : mode essentiel sans effet (${e.avant} cibles visibles, 0 masquée)`);
  }
  if (l.dispositifs.versSeance > 0 && l.dispositifs.ongletsSeance === 0)
    p.push("n°136 : boutons « séance suivante » sans onglets à activer");
  if (l.erreurs > 0) p.push(`${l.erreurs} erreur(s) JS`);
  return p;
};

let sains = 0;
const parTheme = {};
for (const l of lignes) {
  const probs = pb(l);
  const theme = l.rel.split("/")[0].slice(0, 7);
  parTheme[theme] = parTheme[theme] || { seq: 0, prob: 0 };
  parTheme[theme].seq++;
  if (probs.length === 0) { sains++; continue; }
  parTheme[theme].prob += probs.length;
  console.log("\n── " + l.rel);
  probs.forEach(p => console.log("   ✘ " + p));
}
console.log("\n═══ " + lignes.length + " séquences mesurées · " + sains + " sans défaut ═══");
for (const [t, v] of Object.entries(parTheme).sort())
  console.log(`   ${t} : ${v.seq} séquences, ${v.prob} défaut(s)`);
