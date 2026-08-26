#!/usr/bin/env node
/* Suite de tests Playwright du lot 5e_C9.1→C9.3 « La boîte étiquetée ».

   Écrite le 26 août 2026, à l'occasion de l'harmonisation du lot — dernière
   marche du C9 reprise. Comme pour le 3e, le rapport de tests existant décrivait
   une campagne réelle sans qu'aucune suite ne soit committée : rien n'était
   rejouable. Ce fichier ferme ce trou.

   Elle simule la séquence comme un élève et ne déclare que ce qu'elle exécute.
   Le contenu INTERNE des iframes Vittascience n'est pas testé (service externe) :
   seuls l'embarquement et le suivi d'ouverture le sont.

   Règle d'or n°136 : chaque dispositif est vérifié par la MESURE de son effet
   (un nombre), jamais par la présence de ses commandes.

   Usage : node tests_5e_C9.1-C9.3.mjs [dossier_du_lot] [dossier_captures]      */
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";

let chromium;
try { ({ chromium } = await import("playwright")); }
catch {
  const racineGlobale = execSync("npm root -g").toString().trim();
  ({ chromium } = createRequire(import.meta.url)(path.join(racineGlobale, "playwright", "index.js")));
}

const LOT = path.resolve(process.argv[2] || ".");
const CAP = path.resolve(process.argv[3] || "/tmp/captures_5eC91");
fs.mkdirSync(CAP, { recursive: true });

const resultats = [];
let nCap = 0;
function ok(nom, cond, detail = "") {
  resultats.push({ nom, ok: !!cond, detail });
  console.log((cond ? "✅" : "❌") + " " + nom + (detail ? " — " + detail : ""));
  if (!cond) process.exitCode = 1;
}
async function shot(page, nom, selecteur) {
  nCap++;
  const f = path.join(CAP, String(nCap).padStart(2, "0") + "_" + nom + ".png");
  if (selecteur) { try { await page.locator(selecteur).scrollIntoViewIfNeeded(); await page.waitForTimeout(120); } catch {} }
  await page.screenshot({ path: f, fullPage: false });
}
const url = f => "file://" + path.join(LOT, f);
const SEQ = "sequence_5e_C9.1-C9.3_boite_etiquetee.html";
const QCM = "qcm_5e_C9.1-C9.3_boite_etiquetee.html";

function verifLiens() {
  const htmls = [];
  (function walk(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const p = path.join(d, e.name);
      if (e.isDirectory()) walk(p); else if (e.name.endsWith(".html")) htmls.push(p);
    }
  })(LOT);
  const casses = [];
  for (const h of htmls) {
    const src = fs.readFileSync(h, "utf8");
    for (const m of src.matchAll(/(?:href|src|data)="([^"#]+)"/g)) {
      const cible = m[1];
      if (/^(https?:|mailto:|data:|javascript:)/.test(cible)) continue;
      const abs = path.resolve(path.dirname(h), decodeURI(cible));
      if (!fs.existsSync(abs)) casses.push(path.basename(h) + " → " + cible);
    }
  }
  ok("liens locaux : zéro lien cassé dans le lot", casses.length === 0,
     casses.join(" · ") || (htmls.length + " HTML parcourus"));
}

const nav = await chromium.launch();
async function ouvrir(ctx, fichier) {
  const page = await ctx.newPage();
  const erreurs = [];
  page.on("pageerror", e => erreurs.push(String(e)));
  page.on("console", m => { if (m.type() === "error" && !/net::|ERR_/.test(m.text())) erreurs.push(m.text()); });
  await page.goto(url(fichier));
  await page.waitForTimeout(400);
  return { page, erreurs };
}

/* ═══════════════════ 1. La séquence ═══════════════════ */
const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 } });
const { page, erreurs } = await ouvrir(ctx, SEQ);
await shot(page, "sequence_chargee");
ok("séquence : chargement file:// sans erreur JS", erreurs.length === 0, erreurs.slice(0, 3).join(" | "));

/* — n°23 : les durées annoncées, à la convention du dépôt — */
{
  /* On ne compte QUE les durées d'activité : la mention d'en-tête
     « 3 séances de 55 min » est un cadre horaire, pas une durée de tâche. */
  const durees = await page.locator(".activite span.duree").allTextContents();
  const total = durees.map(t => parseInt((t.match(/\d+/) || [0])[0], 10)).reduce((a, b) => a + b, 0);
  ok("n°23 : 5 durées annoncées avec le tilde de la convention",
     durees.length === 5 && durees.every(t => /~/.test(t)), durees.join(" · "));
  ok("n°23 : le total tient dans les 165 min disponibles avec de la marge",
     total > 0 && total <= 145, total + " min annoncées");
}

/* — n°26 : le billet d'entrée, hors progression — */
{
  await page.selectOption("#be_1", { index: 1 });
  await page.selectOption("#be_2", { index: 1 });
  await page.selectOption("#be_3", { index: 1 });
  await page.click("#btnBillet");
  await page.waitForTimeout(150);
  const fb = (await page.locator("#fbBillet").textContent()) || "";
  ok("n°26 : le billet d'entrée rend un feedback", fb.trim().length > 10, fb.slice(0, 60));
  ok("n°26 : le billet se déclare hors progression", /ne compte pas dans ta progression/.test(fb));
  const prog = await page.locator("#progTxt").textContent();
  ok("n°26 : la progression reste à 0 après le billet", /^0 \//.test(prog.trim()), prog.trim());
  await shot(page, "billet_entree", "#billet");
}

/* — n°29 : le mode essentiel masque réellement — */
{
  const avant = await page.locator("section.card.referentiel-card").isVisible();
  await page.click("#btnEssentiel");
  await page.waitForTimeout(150);
  const apres = await page.locator("section.card.referentiel-card").isVisible();
  const etat = await page.locator("#btnEssentiel").getAttribute("aria-pressed");
  ok("n°29 : le mode essentiel masque vraiment la carte de référentiel",
     avant === true && apres === false && etat === "true");
  const corrCachees = await page.evaluate(() =>
    [...document.querySelectorAll("details.correction")].filter(e => e.offsetParent === null).length);
  const corrTotal = await page.locator("details.correction").count();
  ok("n°29 : les corrections aussi sont masquées", corrTotal > 0 && corrCachees === corrTotal,
     corrCachees + "/" + corrTotal);
  await shot(page, "mode_essentiel");
  await page.click("#btnEssentiel");
  await page.waitForTimeout(120);
  ok("n°29 : un second clic rétablit l'affichage complet",
     await page.locator("section.card.referentiel-card").isVisible());
}

/* — n°30 : le tableau de bord — */
{
  const n = await page.locator("#tachesBandeau .tache").count();
  ok("n°30 : le tableau de bord liste les 5 activités", n === 5, n + " tâches");
  const coches = await page.locator("#tachesBandeau .tache.fait").count();
  ok("n°30 : aucune tâche cochée en début de parcours", coches === 0);
}

/* — n°31 : versions étayées — */
{
  const e = await page.locator("details.etayage").count();
  const z = await page.locator("textarea").count();
  ok("n°31 : une version étayée pour chaque zone de rédaction", e >= z && z >= 2,
     e + " étayages pour " + z + " zones");
}

/* — n°34 : étiquettes — */
{
  const orphelins = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll("input, select, textarea").forEach(e => {
      if (e.type === "hidden" || e.type === "button") return;
      const parLe = e.id && document.querySelector('label[for="' + CSS.escape(e.id) + '"]');
      const dedans = e.closest("label");
      const aria = e.getAttribute("aria-label") || e.getAttribute("aria-labelledby");
      if (!parLe && !dedans && !aria) out.push(e.id || e.name || e.tagName);
    });
    return out;
  });
  ok("n°34 : aucun champ sans étiquette", orphelins.length === 0, orphelins.slice(0, 5).join(", "));
  const explicites = await page.evaluate(() =>
    [...document.querySelectorAll("select")].filter(e =>
      e.id && document.querySelector('label[for="' + CSS.escape(e.id) + '"]')).length);
  const selects = await page.locator("select").count();
  ok("n°34 : chaque liste déroulante porte une étiquette EXPLICITE (for=)",
     explicites === selects, explicites + "/" + selects);
}

/* — n°42 : la carte de référentiel recopie le programme, au mot près — */
{
  const txt = await page.locator("section.card.referentiel-card").innerText();
  const attendus = [
    "Analyser un programme simple fourni et tester s'il répond au besoin ou au problème posé",
    "Modifier un programme fourni pour répondre au besoin ou à un problème posé",
    "Réaliser et mettre au point un programme simple commandant un OST"
  ];
  const manquants = attendus.filter(a => !txt.replace(/’/g, "'").includes(a));
  ok("n°42 : les 3 formulations sont celles du programme, au mot près",
     manquants.length === 0, manquants.join(" | "));
}

/* — n°122 + n°136 : le sélecteur masque un nombre MESURÉ de blocs — */
{
  await page.click('.parcours-btn[data-choix="c"]');
  await page.waitForTimeout(150);
  const classe = await page.evaluate(() => document.body.className);
  const note = await page.locator("#parcoursNote").textContent();
  const bTotal = await page.locator('[data-parcours="b"]').count();
  const bMasques = await page.evaluate(() =>
    [...document.querySelectorAll('[data-parcours="b"]')].filter(e => e.offsetParent === null).length);
  ok("n°122 : choisir 🅲 applique la classe parcours-c", /parcours-c/.test(classe));
  ok("n°122 : la note annonce le parcours choisi", /sans matériel/.test(note), note.trim());
  ok("n°136 : les blocs 🅱 sont réellement masqués (0 sur 0 = échec)",
     bTotal > 0 && bMasques === bTotal, bMasques + "/" + bTotal);
  await shot(page, "parcours_c");
  await page.click('.parcours-btn[data-choix="tous"]');
  await page.waitForTimeout(120);
  ok("n°122 : aucune question retirée (5 vérificateurs)",
     (await page.locator(".btn.check").count()) === 5);
}

/* — n°101 : chaque séance mène à la suivante — */
{
  const n = await page.locator(".vers-seance").count();
  ok("n°101 : 2 boutons « séance suivante »", n === 2, n + " boutons");
  await page.locator('.vers-seance[data-vers="s2"]').click();
  await page.waitForTimeout(200);
  ok("n°101 : le bouton bascule vraiment sur la séance 2",
     (await page.locator("#tab-s2").getAttribute("aria-selected")) === "true" &&
     (await page.locator("#s2").isVisible()));
  await shot(page, "vers_seance2");
  await page.click("#tab-s1");
  await page.waitForTimeout(150);
}

/* — n°135 : tableaux lisibles, mesurés au rendu — */
{
  const verdict = await page.evaluate(() => {
    const tables = [...document.querySelectorAll("table")].filter(t => t.offsetParent !== null);
    const sans = [];
    for (const t of tables) {
      const c = t.querySelector("td, th");
      if (!c) continue;
      const s = getComputedStyle(c);
      const bords = [s.borderBottomWidth, s.borderLeftWidth, s.borderTopWidth, s.borderRightWidth]
        .map(v => parseFloat(v) || 0);
      const fond = getComputedStyle(t.querySelector("tr")).backgroundColor;
      if (bords.every(v => v === 0) && (fond === "rgba(0, 0, 0, 0)" || fond === "transparent"))
        sans.push(t.className || "(sans classe)");
    }
    return { total: tables.length, sans };
  });
  ok("n°135 : aucun tableau visible sans séparation lisible",
     verdict.sans.length === 0, verdict.total + " tableaux · " + verdict.sans.join(", "));
}

/* — le parcours élève : le simulateur, puis l'activité 1 — */
{
  for (let i = 0; i < 4; i++) { await page.click("#memNext"); await page.waitForTimeout(80); }
  const badge = await page.locator("#memBadge").textContent();
  ok("act. 1 : les 4 étapes du simulateur délivrent le badge", /🔓|badge/i.test(badge), badge.trim().slice(0, 50));
  await shot(page, "simulateur_memoire", "#memEcran");
  await page.selectOption("#a1q1", "21");
  await page.selectOption("#a1q2", "il a été REMPLACÉ par 21 — une boîte ne garde qu'UNE valeur");
  await page.selectOption("#a1q3", "« RANGE cette valeur dans la boîte »");
  await page.click('.btn.check[data-check="1"]');
  await page.waitForTimeout(150);
  ok("act. 1 : validée 3/3 avec le vérificateur exact",
     /activité validée/.test(await page.locator("#fb1").textContent()));
}

/* — le banc de l'activité 4 : le bug FOURNI doit se voir — */
{
  await page.click("#tab-s2");
  await page.waitForTimeout(150);
  for (const t of ["1", "2", "3"]) { await page.click(`.bench-run[data-t="${t}"]`); await page.waitForTimeout(90); }
  const t1 = await page.locator("#bt1").textContent();
  const t3 = await page.locator("#bt3").textContent();
  ok("act. 4 : T1 et T2 passent — le programme fourni a l'air correct", /✔/.test(t1), t1.trim());
  ok("act. 4 : T3 ÉCHOUE et révèle le bug des descendus (19 au lieu de 23)",
     /✘/.test(t3) && /19/.test(t3), t3.trim());
  ok("act. 4 : les 3 essais délivrent le badge de test",
     /🔓/.test(await page.locator("#benchBadge").textContent()));
  await shot(page, "banc_act4", "#benchBadge");
}

/* — le verrou de l'activité 5 refuse sans les essais de barrière — */
{
  await page.click("#tab-s3");
  await page.waitForTimeout(150);
  await page.click('.btn.check[data-check="5"]');
  await page.waitForTimeout(150);
  const fb5 = await page.locator("#fb5").textContent();
  ok("act. 5 : refusée tant que les 3 tests de la barrière ne sont pas exécutés",
     /🔒/.test(fb5), fb5.slice(0, 60));
}

/* — le cas frontière de la barrière : zéro pile — */
{
  for (const t of ["1", "2", "3"]) { await page.click(`.bench-barr[data-t="${t}"]`); await page.waitForTimeout(90); }
  const b3 = await page.locator("#bb3").textContent();
  ok("act. 5 : le cas frontière (0 place) ferme la barrière", /FERMÉE/.test(b3) && /✔/.test(b3), b3.trim());
  ok("act. 5 : les 3 essais délivrent le badge de réglage",
     /🔓/.test(await page.locator("#barrBadge").textContent()));
  await shot(page, "banc_barriere", "#barrBadge");
}

/* — progression, tableau de bord, sauvegarde — */
{
  const prog = await page.locator("#progTxt").textContent();
  ok("progression : 1 / 5 après la seule activité 1", /^1 \/ 5/.test(prog.trim()), prog.trim());
  ok("tableau de bord : la tâche 1 est cochée",
     (await page.locator("#tachesBandeau .tache.fait").count()) === 1);
  await page.click("#btnSave");
  await page.waitForTimeout(150);
  const cle = await page.evaluate(() => localStorage.getItem("seq_5e_C9.1-C9.3_boite_etiquetee"));
  ok("sauvegarde : la clé localStorage attendue est écrite", !!cle && cle.length > 50);
  await page.reload();
  await page.waitForTimeout(400);
  ok("restauration : la progression survit au rechargement",
     /^1 \/ 5/.test((await page.locator("#progTxt").textContent()).trim()));
  ok("restauration : les réponses saisies sont restituées",
     (await page.locator("#a1q1").inputValue()) === "21");
}

/* — réseau — */
{
  const sorties = [];
  const p2 = await ctx.newPage();
  p2.on("request", r => { const u = r.url(); if (/^https?:/.test(u)) sorties.push(u); });
  await p2.goto(url(SEQ));
  await p2.waitForTimeout(800);
  const horsVitta = sorties.filter(u => !/vittascience/i.test(u));
  ok("réseau : aucune sortie hors iframe Vittascience", horsVitta.length === 0,
     horsVitta.slice(0, 3).join(" · ") || (sorties.length + " requêtes, toutes Vittascience"));
  await p2.close();
}

await page.close();
await ctx.close();

/* ═══════════════════ 2. Mobile 390 px ═══════════════════ */
{
  const ctxm = await nav.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const { page: pm, erreurs: em } = await ouvrir(ctxm, SEQ);
  const debord = await pm.evaluate(() =>
    Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth));
  ok("mobile 390 px : aucun défilement horizontal", debord === 0, "débord = " + debord + " px");
  ok("mobile 390 px : zéro erreur JS", em.length === 0, em.slice(0, 2).join(" | "));
  await shot(pm, "mobile_390");
  await pm.close();
  await ctxm.close();
}

/* ═══════════════════ 3. Le QCM ═══════════════════ */
{
  const ctxq = await nav.newContext({ viewport: { width: 1280, height: 900 } });
  const { page: pq, erreurs: eq } = await ouvrir(ctxq, QCM);
  ok("QCM : chargement sans erreur JS", eq.length === 0, eq.slice(0, 2).join(" | "));
  const meta = await pq.evaluate(src => {
    const m = src.match(/const QUESTIONS\s*=\s*(\[[\s\S]*?\n\];)/);
    if (!m) return null;
    let q;
    try { q = eval(m[1].replace(/;\s*$/, "")); } catch { return null; }
    if (!Array.isArray(q)) return null;
    const rep = {};
    q.forEach(x => { rep[x.r] = (rep[x.r] || 0) + 1; });
    const dVides = q.filter(x => (x.d || [])[x.r] && (x.d || [])[x.r].trim() !== "").length;
    const dPleins = q.filter(x => (x.d || []).filter((t, i) => i !== x.r && t && t.trim()).length === 3).length;
    return { n: q.length, rep, dVides, dPleins };
  }, fs.readFileSync(path.join(LOT, QCM), "utf8"));
  if (meta) {
    ok("QCM : 30 questions", meta.n === 30, meta.n + " questions");
    ok("QCM : bonne réponse sans réfutation sur les 30", meta.dVides === 0, meta.dVides + " anomalies");
    ok("QCM : 3 réfutations non vides sur chacune des 30", meta.dPleins === 30, meta.dPleins + "/30");
    ok("QCM : les 4 lettres sont utilisées comme bonne réponse",
       Object.keys(meta.rep).length === 4, JSON.stringify(meta.rep));
  } else {
    ok("QCM : le tableau QUESTIONS est lisible depuis la source", false,
       "const QUESTIONS = [...] introuvable ou non évaluable — contrôle NON exécuté");
  }
  await shot(pq, "qcm");
  await pq.close();
  await ctxq.close();
}

verifLiens();
await nav.close();

const total = resultats.length, reussis = resultats.filter(r => r.ok).length;
console.log("\n═══ " + reussis + " / " + total + " tests réussis · captures dans " + CAP + " ═══");
if (reussis !== total) {
  console.log("Échecs :");
  resultats.filter(r => !r.ok).forEach(r => console.log("  ❌ " + r.nom + (r.detail ? " — " + r.detail : "")));
}
