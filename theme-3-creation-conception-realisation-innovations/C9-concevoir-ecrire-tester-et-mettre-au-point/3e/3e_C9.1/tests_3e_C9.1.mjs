#!/usr/bin/env node
/* Suite de tests Playwright du lot 3e_C9.1 « Variables, types et systèmes ».

   Écrite le 26 août 2026, à l'occasion de l'harmonisation du lot. Avant cette
   date le rapport de tests décrivait une campagne réelle (30/30 le 30 juillet)
   mais AUCUNE suite n'était committée : personne ne pouvait la rejouer. C'est
   ce trou-là que ce fichier ferme.

   La suite simule la séquence comme un élève et ne déclare que ce qu'elle
   exécute. Le contenu INTERNE des iframes Vittascience n'est pas testé (service
   externe) : seuls l'embarquement et le suivi d'ouverture le sont.

   Usage : node tests_3e_C9.1.mjs [dossier_du_lot] [dossier_captures]          */
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
const CAP = path.resolve(process.argv[3] || "/tmp/captures_3eC91");
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
const SEQ = "sequence_3e_C9.1_variables_types_systemes.html";
const QCM = "qcm_3e_C9.1_variables_types_systemes.html";

/* ── liens locaux (statique) ── */
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

/* ── un navigateur, deux pages ── */
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

/* — règle n°23 : les durées sont annoncées — */
{
  const n = await page.locator("text=/⏱/").count();
  ok("n°23 : des durées ⏱ sont annoncées dans la page", n >= 5, n + " mentions");
}

/* — règle n°26 : le billet d'entrée, noté hors progression — */
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

/* — règle n°29 : le mode essentiel masque réellement — */
{
  const avant = await page.locator("section.card.referentiel-card").isVisible();
  await page.click("#btnEssentiel");
  await page.waitForTimeout(150);
  const apres = await page.locator("section.card.referentiel-card").isVisible();
  const etat = await page.locator("#btnEssentiel").getAttribute("aria-pressed");
  ok("n°29 : le mode essentiel masque vraiment la carte de référentiel",
     avant === true && apres === false && etat === "true");
  await shot(page, "mode_essentiel");
  await page.click("#btnEssentiel");   // on rétablit
  await page.waitForTimeout(120);
  ok("n°29 : un second clic rétablit l'affichage complet",
     await page.locator("section.card.referentiel-card").isVisible());
}

/* — règle n°30 : le tableau de bord des tâches — */
{
  const n = await page.locator("#tachesBandeau .tache").count();
  ok("n°30 : le tableau de bord liste les 5 activités", n === 5, n + " tâches");
  const coches = await page.locator("#tachesBandeau .tache.fait").count();
  ok("n°30 : aucune tâche cochée en début de parcours", coches === 0);
}

/* — règle n°31 : les versions étayées — */
{
  const n = await page.locator("details.etayage").count();
  ok("n°31 : au moins deux versions étayées sont disponibles", n >= 2, n + " étayages");
}

/* — règle n°34 : tout champ porte une étiquette — */
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
}

/* — règle n°122 : le sélecteur de parcours agit vraiment — */
{
  await page.click('.parcours-btn[data-choix="c"]');
  await page.waitForTimeout(150);
  const classe = await page.evaluate(() => document.body.className);
  const note = await page.locator("#parcoursNote").textContent();
  const bMasques = await page.evaluate(() =>
    [...document.querySelectorAll('[data-parcours="b"]')].filter(e => e.offsetParent === null).length);
  const bTotal = await page.locator('[data-parcours="b"]').count();
  ok("n°122 : choisir 🅲 applique la classe parcours-c", /parcours-c/.test(classe));
  ok("n°122 : la note annonce le parcours choisi", /sans matériel/.test(note), note.trim());
  ok("n°122 : les blocs 🅱 sont masqués", bTotal > 0 && bMasques === bTotal, bMasques + "/" + bTotal);
  await shot(page, "parcours_c");
  await page.click('.parcours-btn[data-choix="tous"]');
  await page.waitForTimeout(120);
  const questionsRestantes = await page.locator(".btn.check").count();
  ok("n°122 : aucune question n'a été retirée (5 vérificateurs)", questionsRestantes === 5);
}

/* — règle n°101 : chaque séance mène à la suivante — */
{
  const n = await page.locator(".vers-seance").count();
  ok("n°101 : 3 boutons « séance suivante »", n === 3, n + " boutons");
  await page.locator('.vers-seance[data-vers="s2"]').click();
  await page.waitForTimeout(200);
  const actif = await page.locator("#tab-s2").getAttribute("aria-selected");
  const visible = await page.locator("#s2").isVisible();
  ok("n°101 : le bouton bascule vraiment sur la séance 2", actif === "true" && visible);
  await shot(page, "vers_seance2");
  await page.click("#tab-s1");
  await page.waitForTimeout(150);
}

/* — règle n°135 : les tableaux sont lisibles (bordures effectives) — */
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
      if (bords.every(v => v === 0) && (fond === "rgba(0, 0, 0, 0)" || fond === "transparent")) {
        sans.push(t.className || "(sans classe)");
      }
    }
    return { total: tables.length, sans };
  });
  ok("n°135 : aucun tableau visible sans séparation lisible",
     verdict.sans.length === 0, verdict.total + " tableaux · " + verdict.sans.join(", "));
}

/* — le parcours élève : activité 1 (simulateur + 4 réponses) — */
{
  for (let i = 0; i < 6; i++) { await page.click("#memNext"); await page.waitForTimeout(80); }
  const badge = await page.locator("#memBadge").textContent();
  ok("act. 1 : les 6 étapes du simulateur de mémoire délivrent le badge",
     /🔓|badge/i.test(badge), badge.trim().slice(0, 60));
  await shot(page, "simulateur_memoire", "#memEcran");

  await page.selectOption("#a1q1", "3");
  await page.selectOption("#a1q2", "il est perdu : affecter, c'est REMPLACER");
  await page.selectOption("#a1q3", "« mets cette valeur dans la boîte »");
  await page.selectOption("#a1q4", "de droite à gauche : je CALCULE d'abord, je RANGE ensuite");
  await page.click('.btn.check[data-check="1"]');
  await page.waitForTimeout(150);
  const fb1 = await page.locator("#fb1").textContent();
  ok("act. 1 : validée 4/4 avec le vérificateur exact", /activité validée/.test(fb1), fb1.slice(0, 50));
}

/* — le verrou expérientiel de l'activité 5 refuse sans les essais — */
{
  await page.click("#tab-s4");
  await page.waitForTimeout(150);
  await page.click('.btn.check[data-check="5"]');
  await page.waitForTimeout(150);
  const fb5 = await page.locator("#fb5").textContent();
  ok("act. 5 : refusée tant que les 4 tests du banc ne sont pas exécutés",
     /🔒/.test(fb5), fb5.slice(0, 60));
  await shot(page, "verrou_act5", "#fb5");
}

/* — la progression suit — */
{
  const prog = await page.locator("#progTxt").textContent();
  ok("progression : 1 / 5 après la seule activité 1", /^1 \/ 5/.test(prog.trim()), prog.trim());
  const coches = await page.locator("#tachesBandeau .tache.fait").count();
  ok("tableau de bord : la tâche 1 est cochée", coches === 1, coches + " cochée(s)");
}

/* — sauvegarde / restauration — */
{
  await page.click("#btnSave");
  await page.waitForTimeout(150);
  const cle = await page.evaluate(() => localStorage.getItem("seq_3e_C9.1_variables_types_systemes"));
  ok("sauvegarde : la clé localStorage attendue est écrite", !!cle && cle.length > 50);
  await page.reload();
  await page.waitForTimeout(400);
  const prog = await page.locator("#progTxt").textContent();
  const a1 = await page.locator("#a1q1").inputValue();
  ok("restauration : la progression survit au rechargement", /^1 \/ 5/.test(prog.trim()), prog.trim());
  ok("restauration : les réponses saisies sont restituées", a1 === "3", a1);
}

/* — aucun envoi réseau hors iframe Vittascience — */
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

  /* Le tableau QUESTIONS vit dans une fermeture : on l'évalue depuis la source,
     dans le contexte de la page, plutôt que d'exiger qu'il soit exposé. */
  const meta = await pq.evaluate(src => {
    const m = src.match(/const QUESTIONS\s*=\s*(\[[\s\S]*?\n\];)/);
    if (!m) return null;
    let q;
    try { q = eval(m[1].replace(/;\s*$/, "")); } catch { return null; }
    if (!Array.isArray(q)) return null;
    const rep = {};
    q.forEach(x => { const r = x.r; rep[r] = (rep[r] || 0) + 1; });
    const dVides = q.filter(x => (x.d || [])[x.r] && (x.d || [])[x.r].trim() !== "").length;
    const dPleins = q.filter(x => (x.d || []).filter((t, i) => i !== x.r && t && t.trim()).length === 3).length;
    return { n: q.length, rep, dVides, dPleins };
  }, fs.readFileSync(path.join(LOT, QCM), "utf8"));
  if (meta) {
    ok("QCM : 30 questions", meta.n === 30, meta.n + " questions");
    ok("QCM : bonne réponse vide de réfutation sur les 30", meta.dVides === 0, meta.dVides + " anomalies");
    ok("QCM : 3 réfutations non vides sur chacune des 30", meta.dPleins === 30, meta.dPleins + "/30");
    ok("QCM : répartition A/B/C/D annoncée", Object.keys(meta.rep).length === 4,
       JSON.stringify(meta.rep));
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

/* ── bilan ── */
const total = resultats.length, reussis = resultats.filter(r => r.ok).length;
console.log("\n═══ " + reussis + " / " + total + " tests réussis · captures dans " + CAP + " ═══");
if (reussis !== total) {
  console.log("Échecs :");
  resultats.filter(r => !r.ok).forEach(r => console.log("  ❌ " + r.nom + (r.detail ? " — " + r.detail : "")));
}
