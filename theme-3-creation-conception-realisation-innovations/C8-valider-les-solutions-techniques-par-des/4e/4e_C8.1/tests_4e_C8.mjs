#!/usr/bin/env node
/* Suite de tests Playwright — lot 4e_C8.1 « Jardin connecté — valider » (arc « jardin connecté » de 4e).

   Écrite le 26 août 2026 à l'occasion de l'harmonisation du lot. Elle simule la
   séquence comme un élève et ne déclare que ce qu'elle exécute.

   Règle d'or n°136 : chaque dispositif est vérifié par la MESURE de son effet —
   un nombre —, jamais par la présence de ses commandes. Un contrôle dont le
   résultat attendu est « oui » plutôt qu'un nombre ne contrôle rien.

   Usage : node tests_4e_C8.mjs [dossier_du_lot] [dossier_captures]                 */
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

/* ── ce qui change d'un lot à l'autre ── */
const CFG = {
  seq: "sequence_4e_C8_jardin-validation.html",
  qcm: "qcm_4e_C8_jardin-validation.html",
  cle: "seq_4e_C8_jardin_validation",
  captures: "/tmp/captures_4eC8",
  etayages: 4,
  formulations: [
    "Paramétrer une simulation fournie pour valider la tenue mécanique d'un matériau.",
    "Proposer un protocole de test pour valider la tenue mécanique d'un matériau.",
    "Proposer un protocole de test pour valider le comportement et les performances d'un objet technique."
  ],
  /* trois tests DIFFÉRENTS : c'est ce que le verrou exige */
  essaisBanc: [
    { "#simTest": "Stabilité (secousses 10 s)" },
    { "#simTest": "Pluie battante (30 s)" },
    { "#simTest": "Nuit de gel (-8 °C)" }
  ],
  reponsesAct0: { "#a0q1": "Nuit de gel", "#a0q2": "Non — sans attendu, impossible de juger" }
};

const LOT = path.resolve(process.argv[2] || ".");
const CAP = path.resolve(process.argv[3] || CFG.captures);
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
const { page, erreurs } = await ouvrir(ctx, CFG.seq);
await shot(page, "sequence_chargee");
ok("séquence : chargement file:// sans erreur JS", erreurs.length === 0, erreurs.slice(0, 3).join(" | "));

/* — n°23 : le cadre horaire est reconnaissable, et il tient — */
{
  const txt = await page.locator("body").innerText();
  const cadre = txt.match(/(\d+)\s*séances?\s+de\s+(\d+)\s*min/i);
  const parts = [...txt.matchAll(/~\s*(\d+)\s*min/g)].map(m => parseInt(m[1], 10));
  const total = parts.reduce((a, b) => a + b, 0);
  ok("n°23 : la page annonce un cadre « N séances de M min »", !!cadre, cadre ? cadre[0] : "absent");
  /* 5 durées pour 6 vérificateurs : l'activité 1 en porte deux (le diagramme,
     puis le planning) — elles partagent le même créneau annoncé. */
  ok("n°23 : les 5 durées d'activité sont à la convention ~n min", parts.length === 5, parts.join(" + "));
  const dispo = cadre ? parseInt(cadre[1], 10) * parseInt(cadre[2], 10) : 0;
  ok("n°23 : le total tient dans le cadre annoncé, marge comprise",
     total + 10 <= dispo, total + " min pour " + dispo + " disponibles");
}

/* — n°26 : le billet d'entrée, hors progression — */
{
  await page.selectOption("#be_1", { index: 1 });
  await page.selectOption("#be_2", { index: 1 });
  await page.selectOption("#be_3", { index: 1 });
  await page.click("#btnBillet");
  await page.waitForTimeout(150);
  const fb = (await page.locator("#fbBillet").textContent()) || "";
  ok("n°26 : le billet d'entrée rend un feedback", /3 \/ 3/.test(fb), fb.slice(0, 55));
  ok("n°26 : le billet se déclare hors progression", /ne compte pas dans ta progression/.test(fb));
  ok("n°26 : la progression reste à 0 après le billet",
     /^0 \//.test((await page.locator("#progTxt").textContent()).trim()));
  await shot(page, "billet_entree", "#billet");
}

/* — n°29 : le mode essentiel masque un nombre MESURÉ de blocs — */
{
  const visibleAvant = await page.locator("section.card.referentiel-card").isVisible();
  await page.click("#btnEssentiel");
  await page.waitForTimeout(150);
  const visibleApres = await page.locator("section.card.referentiel-card").isVisible();
  ok("n°29 : le mode essentiel masque la carte de référentiel",
     visibleAvant === true && visibleApres === false);
  const total = await page.locator("details.correction").count();
  const cachees = await page.evaluate(() =>
    [...document.querySelectorAll("details.correction")].filter(e => e.offsetParent === null).length);
  ok("n°29 : les corrections sont masquées, toutes", total > 0 && cachees === total, cachees + "/" + total);
  await shot(page, "mode_essentiel");
  await page.click("#btnEssentiel");
  await page.waitForTimeout(120);
  ok("n°29 : un second clic rétablit l'affichage complet",
     await page.locator("section.card.referentiel-card").isVisible());
}

/* — n°30 : le tableau de bord — */
{
  const n = await page.locator("#tachesBandeau .tache").count();
  ok("n°30 : le tableau de bord liste les 6 activités", n === 6, n + " tâches");
  ok("n°30 : aucune tâche cochée en début de parcours",
     (await page.locator("#tachesBandeau .tache.fait").count()) === 0);
}

/* — n°31 : les versions étayées — */
{
  const e = await page.locator("details.etayage").count();
  ok("n°31 : les rédactions principales ont leur version étayée", e >= CFG.etayages,
     e + " étayages (attendu ≥ " + CFG.etayages + ")");
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
}

/* — n°42 : la carte recopie le programme, au mot près — */
{
  const txt = (await page.locator("section.card.referentiel-card").innerText()).replace(/’/g, "'");
  const manquants = CFG.formulations.filter(f => !txt.includes(f));
  ok("n°42 : les 3 formulations sont celles du programme, au mot près",
     manquants.length === 0, manquants.map(m => m.slice(0, 40)).join(" | "));
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
  ok("n°122 : la note annonce le parcours choisi", /🅲/.test(note) || /papier/.test(note), note.trim());
  ok("n°136 : les blocs 🅱 sont réellement masqués (0 sur 0 = échec)",
     bTotal > 0 && bMasques === bTotal, bMasques + "/" + bTotal);
  await shot(page, "parcours_c");
  await page.click('.parcours-btn[data-choix="tous"]');
  await page.waitForTimeout(120);
  ok("n°122 : aucune question retirée (6 vérificateurs)",
     (await page.locator(".btn.check").count()) === 6);
}

/* — n°135 : les tableaux restent lisibles — */
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

/* — le verrou expérientiel de l'activité 0 — */
{
  await page.click('.btn.check[data-check="0"]');
  await page.waitForTimeout(150);
  const fb0 = await page.locator("#fb0").textContent();
  ok("act. 0 : refusée tant que 3 essais n'ont pas été lancés au banc",
     /🔒/.test(fb0), fb0.slice(0, 70));

  for (const essai of CFG.essaisBanc) {
    for (const [sel, val] of Object.entries(essai)) await page.selectOption(sel, val);
    await page.click("#simGo");
    await page.waitForTimeout(90);
  }
  const res = await page.locator("#simRes").textContent();
  ok("act. 0 : le banc rend un verdict pour l'essai joué", res.trim().length > 20, res.trim().slice(0, 70));
  await shot(page, "banc", "#simRes");

  for (const [sel, val] of Object.entries(CFG.reponsesAct0)) await page.selectOption(sel, val);
  await page.click('.btn.check[data-check="0"]');
  await page.waitForTimeout(150);
  ok("act. 0 : validée 2/2 une fois les 3 essais faits",
     /activité validée/.test(await page.locator("#fb0").textContent()));
}

/* — la progression suit vraiment la validation — */
{
  const prog = await page.locator("#progTxt").textContent();
  ok("progression : 1 / 6 après la seule activité 0", /^1 \/ 6/.test(prog.trim()), prog.trim());
  ok("tableau de bord : la tâche 0 est cochée",
     (await page.locator("#tachesBandeau .tache.fait").count()) === 1);
  const largeur = await page.evaluate(() => document.getElementById("progFill").style.width);
  ok("progression : la barre avance (17 %)", largeur === "17%", largeur);
}

/* — l'ordre des étapes : la validation exige le bon ordre — */
{
  for (let i = 1; i <= 5; i++) await page.selectOption("#a1o" + i, String(i));
  await page.click('.btn.check[data-check="1"]');
  await page.waitForTimeout(150);
  ok("act. 1 : le diagramme validé 5/5 dans le bon ordre",
     /activité validée/.test(await page.locator("#fb1").textContent()));
  await page.selectOption("#a1o2", "4");
  await page.click('.btn.check[data-check="1"]');
  await page.waitForTimeout(150);
  const fb = await page.locator("#fb1").textContent();
  ok("act. 1 : un ordre faux est refusé (4/5)", /4\/5/.test(fb), fb.slice(0, 45));
  await page.selectOption("#a1o2", "2");
}

/* — sauvegarde / restauration — */
{
  await page.waitForTimeout(200);
  const cle = await page.evaluate(k => localStorage.getItem(k), CFG.cle);
  ok("sauvegarde : la clé localStorage attendue est écrite", !!cle && cle.length > 50, CFG.cle);
  await page.reload();
  await page.waitForTimeout(400);
  ok("restauration : la progression survit au rechargement",
     /^[12] \/ 6/.test((await page.locator("#progTxt").textContent()).trim()));
  ok("restauration : le tableau de bord retrouve ses coches",
     (await page.locator("#tachesBandeau .tache.fait").count()) >= 1);
}

/* — aucun envoi réseau — */
{
  const sorties = [];
  const p2 = await ctx.newPage();
  p2.on("request", r => { if (/^https?:/.test(r.url())) sorties.push(r.url()); });
  await p2.goto(url(CFG.seq));
  await p2.waitForTimeout(800);
  ok("réseau : la page ne sort pas (elle fonctionne hors connexion)",
     sorties.length === 0, sorties.slice(0, 3).join(" · "));
  await p2.close();
}

await page.close();
await ctx.close();

/* ═══════════════════ 2. Mobile 390 px ═══════════════════ */
{
  const ctxm = await nav.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const { page: pm, erreurs: em } = await ouvrir(ctxm, CFG.seq);
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
  const { page: pq, erreurs: eq } = await ouvrir(ctxq, CFG.qcm);
  ok("QCM : chargement sans erreur JS", eq.length === 0, eq.slice(0, 2).join(" | "));
  /* Ces deux QCM sont de la GÉNÉRATION ANCIENNE du dépôt : format
     {q, opts, ok, exp}, sans réfutation par distracteur, et 28 questions au lieu
     de 30. On mesure ce qu'ils sont — on ne prétend pas qu'ils sont au standard.
     La mise à niveau est déclarée « restant à faire » dans le rapport. */
  const meta = await pq.evaluate(src => {
    const m = src.match(/const (?:QUESTIONS|questions)\s*=\s*(\[[\s\S]*?\n\];)/);
    if (!m) return null;
    let q;
    try { q = eval(m[1].replace(/;\s*$/, "")); } catch { return null; }
    if (!Array.isArray(q)) return null;
    const rep = {};
    q.forEach(x => { const i = (x.ok !== undefined ? x.ok : x.r); rep[i] = (rep[i] || 0) + 1; });
    const sansExp = q.filter(x => !(x.exp && String(x.exp).trim())).length;
    const sansQuatre = q.filter(x => !(x.opts && x.opts.length === 4)).length;
    const refutations = q.filter(x => Array.isArray(x.d)).length;
    return { n: q.length, rep, sansExp, sansQuatre, refutations };
  }, fs.readFileSync(path.join(LOT, CFG.qcm), "utf8"));
  if (meta) {
    ok("QCM : le tableau des questions est lisible et chargé", meta.n > 0, meta.n + " questions");
    ok("QCM : chaque question a 4 propositions", meta.sansQuatre === 0, meta.sansQuatre + " anomalies");
    ok("QCM : chaque question porte une explication", meta.sansExp === 0, meta.sansExp + " sans explication");
    ok("QCM : les 4 positions servent de bonne réponse",
       Object.keys(meta.rep).length === 4, JSON.stringify(meta.rep));
    ok("QCM : état déclaré — génération ancienne, sans réfutation par distracteur",
       meta.refutations === 0, meta.refutations + " question(s) avec réfutations (0 attendu ici)");
  } else {
    ok("QCM : le tableau des questions est lisible depuis la source", false,
       "const questions = [...] introuvable ou non évaluable — contrôle NON exécuté");
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
