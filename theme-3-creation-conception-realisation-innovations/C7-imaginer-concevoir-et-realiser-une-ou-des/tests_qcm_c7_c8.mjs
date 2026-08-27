#!/usr/bin/env node
/* Suite rejouable des quatre QCM de C7 et C8 portés au standard C9.
 *
 * Ce que la suite vérifie VRAIMENT (rien d'autre n'est déclaré) :
 *   1. la page se charge sans erreur JavaScript ;
 *   2. la banque contient 30 questions, toutes complètes (4 propositions,
 *      4 réfutations parallèles, explication, exemple, à retenir) ;
 *   3. d[r] est vide — la case de la BONNE réponse ne porte pas de réfutation ;
 *   4. les bonnes réponses sont réparties sur A/B/C/D (au moins 6 par position) ;
 *   5. trois questions au moins portent une image, et le fichier SVG se charge
 *      réellement (naturalWidth > 0) — un src cassé serait invisible autrement ;
 *   6. chaque image porte un titre et une description accessibles ;
 *   7. répondre juste compte juste, répondre faux affiche la réfutation de la
 *      proposition choisie — et pas celle d'une autre ;
 *   8. la progression se restaure après rechargement ;
 *   9. à 390 px, la page ne déborde pas horizontalement ;
 *  10. tous les liens relatifs pointent vers un fichier qui existe ;
 *  11. AUCUNE correction affichée ne contient le mot « undefined » — le moteur
 *      écrivait « Erreur fréquente : undefined » sur les questions sans `err` ;
 *  12. chaque `nuance` écrite dans la banque est bien AFFICHÉE dans la
 *      correction — un champ qu'on ajoute sans le rendre ne sert à personne ;
 *  13. les absolus des réfutations et des « à retenir » correspondent
 *      exactement à `absolus_declares.json` (cliquet : voir linter_absolus.mjs).
 *
 * Usage : NODE_PATH=<node_modules> node tests_qcm_c7_c8.mjs
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "playwright";
import { inventorier, clef } from "./linter_absolus.mjs";

const ICI = path.dirname(fileURLToPath(import.meta.url));
const THEME = path.resolve(ICI, "..");

const QCM = [
  { nom: "5e_C7.1 · C8.3 · C9.3 — l'indicateur du hall",
    f: "C7-imaginer-concevoir-et-realiser-une-ou-des/5e/5e_C7.1/qcm_5e_C7_mini-projet.html" },
  { nom: "4e_C7.1 · C7.2 · C7.3 — le boîtier du jardin",
    f: "C7-imaginer-concevoir-et-realiser-une-ou-des/4e/4e_C7.1/qcm_4e_C7_jardin-conception.html" },
  { nom: "4e_C8.1 · C8.2 · C8.3 — valider le support",
    f: "C8-valider-les-solutions-techniques-par-des/4e/4e_C8.1/qcm_4e_C8_jardin-validation.html" },
  { nom: "3e_C7.1 · 3e_C8.1 — le capteur de confort",
    f: "C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/qcm_3e_C7_capteur-confort-ny.html" },
];

let reussis = 0, echoues = 0;
const ok = (titre, condition, detail = "") => {
  if (condition) { reussis++; console.log("  ✔ " + titre); }
  else { echoues++; console.log("  ✘ " + titre + (detail ? "  — " + detail : "")); }
};

const nav = await chromium.launch();

for (const q of QCM) {
  console.log("\n── " + q.nom);
  const abs = path.join(THEME, q.f);
  if (!fs.existsSync(abs)) { ok("le fichier existe", false, q.f); continue; }

  const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await ctx.newPage();
  const erreurs = [];
  page.on("pageerror", e => erreurs.push(String(e)));
  await page.goto(pathToFileURL(abs).href);
  /* PIÈGE : toutes les pages ouvertes en file:// partagent le même
     localStorage. Sans ce nettoyage, un QCM hérite de la progression du
     précédent et le test de restauration passe pour de mauvaises raisons. */
  await page.evaluate(() => { try { localStorage.clear(); } catch {} });
  await page.reload();
  await page.waitForTimeout(250);

  ok("aucune erreur JavaScript au chargement", erreurs.length === 0, erreurs[0]);

  const banque = await page.evaluate(() => {
    const Q = QUESTIONS;
    const incomplets = [];
    const positions = [0, 0, 0, 0];
    Q.forEach((x, i) => {
      const manques = [];
      if (!Array.isArray(x.o) || x.o.length !== 4) manques.push("4 propositions");
      if (!Array.isArray(x.d) || x.d.length !== 4) manques.push("4 réfutations");
      if (typeof x.r !== "number" || x.r < 0 || x.r > 3) manques.push("r valide");
      if (!x.expl) manques.push("explication");
      if (!x.ex) manques.push("exemple");
      if (!x.ret) manques.push("à retenir");
      if (Array.isArray(x.d) && x.d[x.r] !== "") manques.push("d[r] vide");
      if (Array.isArray(x.d) && x.d.some((t, k) => k !== x.r && !t)) manques.push("réfutation de chaque distracteur");
      if (manques.length) incomplets.push((i + 1) + " : " + manques.join(", "));
      if (typeof x.r === "number") positions[x.r]++;
    });
    return { n: Q.length, incomplets, positions, illustrees: Q.filter(x => x.img).length };
  });

  ok("30 questions", banque.n === 30, "trouvé " + banque.n);
  ok("toutes les questions sont complètes", banque.incomplets.length === 0, banque.incomplets.slice(0, 3).join(" | "));
  ok("bonnes réponses réparties sur A/B/C/D", Math.min(...banque.positions) >= 6,
     JSON.stringify(banque.positions));
  ok("au moins 3 questions illustrées", banque.illustrees >= 3, "trouvé " + banque.illustrees);

  /* ── les images se chargent-elles vraiment ? ── */
  const idxImg = await page.evaluate(() => QUESTIONS.map((x, i) => x.img ? i : -1).filter(i => i >= 0));
  let imagesOk = 0, sansTitre = [];
  for (const i of idxImg) {
    await page.evaluate(k => { etat.courante = k; montrerEcran("q"); rendreTout(); }, i);
    await page.waitForTimeout(180);
    const r = await page.evaluate(() => {
      const im = document.getElementById("qImg");
      return { visible: !!im && im.naturalWidth > 0, src: im ? im.getAttribute("src") : null,
               alt: im ? (im.getAttribute("alt") || "").length : 0 };
    });
    if (r.visible && r.alt > 40) imagesOk++;
    /* le SVG lui-même doit porter <title> et <desc> (règle images v2) */
    if (r.src) {
      const svg = fs.readFileSync(path.join(path.dirname(abs), r.src), "utf-8");
      if (!/<title[ >]/.test(svg) || !/<desc[ >]/.test(svg)) sansTitre.push(r.src);
    }
  }
  ok("chaque image se charge et porte une alternative rédigée", imagesOk === idxImg.length,
     imagesOk + "/" + idxImg.length);
  ok("chaque SVG porte <title> et <desc>", sansTitre.length === 0, sansTitre.join(", "));

  /* ── répondre juste, répondre faux ── */
  await page.evaluate(() => { etat.courante = 0; montrerEcran("q"); rendreTout(); });
  await page.waitForTimeout(150);
  const bonne = await page.evaluate(() => QUESTIONS[0].r);
  const faux = (bonne + 1) % 4;
  const refutAttendue = await page.evaluate(k => QUESTIONS[0].d[k], faux);

  await page.evaluate(k => { document.querySelectorAll("#qOptions .option")[k].click(); }, faux);
  await page.waitForTimeout(120);
  await page.click("#btnValider");
  await page.waitForTimeout(220);
  const apresFaux = await page.evaluate(() => ({
    texte: document.getElementById("corrBloc") ? document.getElementById("corrBloc").textContent : "",
    err: document.getElementById("dErr").textContent,
  }));
  ok("une réponse fausse est comptée fausse", apresFaux.err === "1", "dErr=" + apresFaux.err);
  ok("la réfutation affichée est bien celle de la proposition choisie",
     refutAttendue.length > 0 && apresFaux.texte.includes(refutAttendue.slice(0, 40)));

  await page.evaluate(() => { etat.courante = 1; montrerEcran("q"); rendreTout(); });
  await page.waitForTimeout(150);
  const bonne1 = await page.evaluate(() => QUESTIONS[1].r);
  await page.evaluate(k => { document.querySelectorAll("#qOptions .option")[k].click(); }, bonne1);
  await page.waitForTimeout(120);
  await page.click("#btnValider");
  await page.waitForTimeout(220);
  const bons = await page.evaluate(() => document.getElementById("dOk").textContent);
  ok("une réponse juste est comptée juste", bons === "1", "dOk=" + bons);

  /* ── la correction rendue : ni « undefined », ni nuance oubliée ──
     On valide CHAQUE question et on lit le bloc de correction produit.
     Le défaut visé est invisible autrement : `${Q.err}` sans garde écrit
     « Erreur fréquente : undefined » à l'écran sans lever la moindre erreur. */
  const rendu = await page.evaluate(async () => {
    const sales = [], nuancesManquantes = [];
    let nuances = 0;
    for (let i = 0; i < QUESTIONS.length; i++) {
      etat.courante = i; etat.reponses[i] = QUESTIONS[i].r; etat.validees[i] = true;
      montrerEcran("q"); rendreTout();
      const t = document.getElementById("corrBloc").textContent;
      if (/undefined|\[object Object\]|\bnull\b/.test(t)) sales.push(i + 1);
      if (QUESTIONS[i].nuance) {
        nuances++;
        if (!t.includes(QUESTIONS[i].nuance.slice(0, 40))) nuancesManquantes.push(i + 1);
      }
    }
    return { sales, nuances, nuancesManquantes };
  });
  ok("aucune correction n'affiche « undefined »", rendu.sales.length === 0,
     "questions " + rendu.sales.join(", "));
  ok("chaque nuance écrite est affichée dans la correction",
     rendu.nuancesManquantes.length === 0, "questions " + rendu.nuancesManquantes.join(", "));
  console.log("     (" + rendu.nuances + " questions portent une nuance)");

  /* on efface les réponses posées par le contrôle ci-dessus */
  await page.evaluate(() => { try { localStorage.clear(); } catch {} });
  await page.reload();
  await page.waitForTimeout(250);
  await page.evaluate(() => { etat.courante = 0; montrerEcran("q"); rendreTout(); });
  const bonneR = await page.evaluate(() => QUESTIONS[0].r);
  await page.evaluate(k => { document.querySelectorAll("#qOptions .option")[(k + 1) % 4].click(); }, bonneR);
  await page.click("#btnValider");
  await page.evaluate(() => { etat.courante = 1; montrerEcran("q"); rendreTout(); });
  const bonne1b = await page.evaluate(() => QUESTIONS[1].r);
  await page.evaluate(k => { document.querySelectorAll("#qOptions .option")[k].click(); }, bonne1b);
  await page.click("#btnValider");
  await page.waitForTimeout(220);

  /* ── l'équilibre des longueurs ──
     Défaut mesuré le 27 août 2026 : dans 107 des 120 questions, la bonne
     réponse était la proposition la PLUS LONGUE. Cocher systématiquement la
     plus longue, sans rien lire, donnait 89 %. Le QCM mesurait une habileté
     de candidat, pas une connaissance.
     Le contrôle porte sur ce qu'un élève peut VOIR : une bonne réponse plus
     longue de plus de 20 % que la deuxième. Les exceptions sont nommées une
     par une, avec leur raison. */
  const EXCEPTIONS_LONGUEUR = {
    "qcm_5e_C7_mini-projet.html": {
      27: "propositions en Python : un if/else est nécessairement plus long qu'un if seul, et allonger le distracteur lui ajouterait le cas « libre » — précisément ce que sa réfutation lui reproche d'omettre.",
    },
    "qcm_3e_C7_capteur-confort-ny.html": {
      24: "propositions en Python : la bonne réponse déclare une variable puis teste, les distracteurs sont des fragments fautifs plus courts par nature.",
    },
  };
  const exc = EXCEPTIONS_LONGUEUR[path.basename(abs)] || {};
  const longueurs = await page.evaluate(() => QUESTIONS.map(x =>
    x.o.map(t => String(t).replace(/<[^>]+>/g, "").length)));
  const QUESTIONSr = await page.evaluate(() => QUESTIONS.map(x => x.r));
  const visibles = [];
  longueurs.forEach((L, i) => {
    const bonne = L[QUESTIONSr[i]];
    const autres = L.filter((_, k) => k !== QUESTIONSr[i]);
    if (bonne > 1.2 * Math.max(...autres) && !exc[i + 1]) visibles.push(i + 1);
  });
  ok("la bonne réponse n'est pas visiblement la plus longue",
     visibles.length === 0, "questions " + visibles.join(", "));
  const gagnantes = longueurs.filter((L, i) => L[QUESTIONSr[i]] === Math.max(...L)).length;
  ok("« cocher la plus longue » ne dépasse pas 60 % de réussite",
     gagnantes <= 18, gagnantes + "/30");

  /* ── restauration ── */
  await page.reload();
  await page.waitForTimeout(300);
  const apresRechargement = await page.evaluate(() => ({
    ok: document.getElementById("dOk").textContent,
    err: document.getElementById("dErr").textContent,
  }));
  ok("la progression est restaurée après rechargement",
     apresRechargement.ok === "1" && apresRechargement.err === "1",
     JSON.stringify(apresRechargement));

  /* ── liens ── */
  const liens = await page.evaluate(() =>
    [...document.querySelectorAll("a[href]")].map(a => a.getAttribute("href"))
      .filter(h => h && !h.startsWith("#") && !/^https?:/.test(h)));
  const morts = [...new Set(liens)].filter(h => !fs.existsSync(path.resolve(path.dirname(abs), h)));
  ok("aucun lien relatif mort", morts.length === 0, morts.join(", "));

  await ctx.close();

  /* ── mobile ── */
  const ctxM = await nav.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const pm = await ctxM.newPage();
  await pm.goto(pathToFileURL(abs).href);
  await pm.evaluate(() => { try { localStorage.clear(); } catch {} });
  await pm.reload();
  await pm.waitForTimeout(250);
  const debord = await pm.evaluate(() =>
    Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth));
  ok("aucun débordement horizontal à 390 px", debord === 0, debord + " px");
  await ctxM.close();
}

/* ── le cliquet des absolus, sur les quatre banques à la fois ── */
console.log("\n── Le cliquet des absolus");
{
  const trouves = (await inventorier(nav)).map(clef).sort();
  const declares = JSON.parse(
    fs.readFileSync(path.join(ICI, "absolus_declares.json"), "utf-8")
  ).absolus.map(a => a.ou).sort();
  const nouveaux = trouves.filter(t => !declares.includes(t));
  const disparus = declares.filter(d => !trouves.includes(d));
  ok("aucun absolu non déclaré dans les réfutations et les « à retenir »",
     nouveaux.length === 0, nouveaux.join(" | "));
  ok("l'inventaire ne cite aucun absolu qui n'existe plus",
     disparus.length === 0, disparus.join(" | "));
  ok("chaque absolu déclaré porte une raison écrite",
     JSON.parse(fs.readFileSync(path.join(ICI, "absolus_declares.json"), "utf-8"))
       .absolus.every(a => a.raison && a.raison.length > 30 && a.raison !== "À JUSTIFIER"));
  console.log("     (" + trouves.length + " absolus assumés, tous justifiés)");
}

await nav.close();
console.log("\n═══ " + (reussis + echoues) + " tests · " + reussis + " verts · " + echoues + " rouges ═══");
process.exit(echoues === 0 ? 0 : 1);
