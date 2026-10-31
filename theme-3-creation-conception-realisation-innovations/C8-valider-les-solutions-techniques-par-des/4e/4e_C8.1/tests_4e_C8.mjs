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
  /* depuis le passage à onglets (31/10/2026), les durées vivent dans trois panneaux dont deux sont repliés :
     on lit le texte entier de la page, pas seulement ce qui est à l'écran */
  const txt = await page.evaluate(() => document.body.textContent);
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
  // n°298 (vague du thème 3, 26/10/2026) : la carte de référentiel a quitté la page élève ; le témoin du mode
  // essentiel est désormais le nombre de corrections visibles.
  const visibleAvant = await page.evaluate(() => [...document.querySelectorAll("details.correction")].filter(e => e.offsetParent !== null).length);
  await page.click("#btnEssentiel");
  await page.waitForTimeout(150);
  const visibleApres = await page.evaluate(() => [...document.querySelectorAll("details.correction")].filter(e => e.offsetParent !== null).length);
  ok("n°29 : le mode essentiel masque les corrections, et la page n'a plus de carte de référentiel (n°298)",
     visibleAvant > 0 && visibleApres === 0 && (await page.locator(".referentiel-card").count()) === 0,
     visibleAvant + " → " + visibleApres);
  const total = await page.locator("details.correction").count();
  const cachees = await page.evaluate(() =>
    [...document.querySelectorAll("details.correction")].filter(e => e.offsetParent === null).length);
  ok("n°29 : les corrections sont masquées, toutes", total > 0 && cachees === total, cachees + "/" + total);
  await shot(page, "mode_essentiel");
  await page.click("#btnEssentiel");
  await page.waitForTimeout(120);
  ok("n°29 : un second clic rétablit l'affichage complet",
     (await page.evaluate(() => [...document.querySelectorAll("details.correction")].filter(e => e.offsetParent !== null).length)) > 0);
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

/* — n°42 : le référentiel recopie le programme, au mot près — lu dans la synthèse professeur depuis la
   vague n°298 du thème 3 (26/10/2026) : la page élève ne le porte plus — */
{
  const synth = fs.readFileSync(path.join(LOT, "synthese_professeur_4e_C8.html"), "utf8");
  const debut = synth.indexOf("referentiel-eleve");
  const txt = synth.slice(debut, synth.indexOf("</table>", debut)).replace(/<[^>]+>/g, " ").replace(/&nbsp;/g, " ")
    .replace(/&#39;|&apos;/g, "'").replace(/\s+/g, " ").replace(/’/g, "'");
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
    // le banc est animé (25/10/2026) : sa mesure s'affiche à la fin du test
    await page.waitForFunction(() => !document.getElementById("simRes").textContent.includes("⏳"), null, {timeout: 9000});
  }
  const res = await page.locator("#simRes").textContent();
  ok("act. 0 : le banc rend sa mesure pour l'essai joué, sans verdict", res.trim().length > 20 && !/réussi|conforme|au rendez-vous|FISSURÉE/.test(res), res.trim().slice(0, 90));
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
  /* On attend que la restauration ait eu lieu, au lieu d'un délai fixe : lancé juste après
     d'autres bancs, 400 ms ne suffisaient pas toujours (31/10/2026). */
  await page.waitForFunction(() => /^[12] \/ 6/.test((document.getElementById("progTxt") || {}).textContent?.trim() || ""),
                             null, {timeout: 5000}).catch(() => {});
  ok("restauration : la progression survit au rechargement",
     /^[12] \/ 6/.test((await page.locator("#progTxt").textContent()).trim()));
  ok("restauration : le tableau de bord retrouve ses coches",
     (await page.locator("#tachesBandeau .tache.fait").count()) >= 1);
}

/* — activité 2 : l'exercice inséré depuis l'atelier des représentations (diagramme des exigences,
     4e, exercice 3) est exigé par le vérificateur de l'activité (24/10/2026) — */
{
  /* — la grille « Conforme ? » (règle d'or n°317) : des menus DANS la grille, nommés, et un retour écrit
       sous chaque case fausse ou vide après « Vérifier ». Les options fausses sont lues dans les menus. — */
  await page.click("#tab-s2");   // l'activité 2 est dans la séance 2 (onglets, 31/10/2026)
  const BONNES = [["#a2c1", "Oui"], ["#a2c2", "Oui"], ["#a2c3", "Oui"], ["#a2c4", "Non"], ["#a2dec", "À améliorer"]];
  const grille = await page.evaluate(ids => ids.map(id => {
    const s = document.querySelector(id);
    return { id, label: s.getAttribute("aria-label") || "", decrit: s.getAttribute("aria-describedby"),
             dansGrille: !!s.closest(".grille-conforme table td.case-menu"),
             valeurs: [...s.options].map(o => o.value).filter(Boolean) };
  }), BONNES.map(b => b[0]));
  ok("act. 2 : la grille « Conforme ? » porte ses 5 menus dans ses cases (décision globale comprise), "
     + "chacun nommé « Ligne n, … » et relié à sa case de retour",
     grille.length === 5 && grille.every((g, i) => g.dansGrille && new RegExp("^Ligne " + (i + 1) + ", ").test(g.label)
       && g.decrit === g.id.slice(1) + "-retour"),
     grille.map(g => g.label.slice(0, 28)).join(" | "));
  await page.click('.btn.check[data-check="3"]');
  await page.waitForTimeout(120);
  const vides = await page.$$eval(".grille-conforme .retour-case.visible", l => l.map(r => r.textContent));
  ok("act. 2 : la grille vérifiée à vide dit « ○ Sans réponse » sous chacune de ses 5 cases",
     vides.length === 5 && vides.every(x => /^○ Sans réponse/.test(x)), vides[0] || "");
  const retoursGrille = [];
  for (const [id, bonne] of BONNES) {
    for (const v of grille.find(g => g.id === id).valeurs.filter(x => x !== bonne)) {
      await page.selectOption(id, v);
      await page.click('.btn.check[data-check="3"]');
      await page.waitForTimeout(80);
      retoursGrille.push(await page.evaluate(i => {
        const r = document.getElementById(i.slice(1) + "-retour"), td = r.closest("td");
        return { texte: r.textContent, visible: r.offsetHeight > 0, marque: (td.querySelector(".qmark") || {}).textContent };
      }, id));
    }
  }
  ok(`act. 2 : les ${retoursGrille.length} options fausses de la grille ont chacune SON retour, écrit sous la case (✘ et pourquoi)`,
     retoursGrille.length === 10 && retoursGrille.every(r => r.visible && r.marque === "✘" && /^✘ .{40,}/.test(r.texte))
     && new Set(retoursGrille.map(r => r.texte)).size === 10,
     (retoursGrille[0] || {}).texte?.slice(0, 60));
  for (const [id, v] of BONNES)
    await page.selectOption(id, v);
  await page.fill("#a2diag", "Le plastique devient cassant au froid. Test : refaire la nuit de gel avec une attache en inox.");
  await page.click('.btn.check[data-check="3"]');
  await page.waitForTimeout(150);
  const fbVerrou = (await page.locator("#fb3").textContent()) || "";
  ok("act. 2 : refusée tant que l'exercice du diagramme des exigences n'est pas réussi",
     /🔒/.test(fbVerrou) && /diagramme des exigences/.test(fbVerrou), fbVerrou.slice(0, 80));

  await page.click("#ex_4e_e3 button.verifier");
  await page.waitForTimeout(100);
  ok("act. 2 : l'exercice inséré se vérifie à vide (retour à reprendre)",
     /🔴/.test(await page.locator("#ex_4e_e3 .retour").innerText()));
  /* Depuis la règle d'or n°317, l'exercice se complète dans le tableau du cahier des charges : 8 menus
     `ex_4e_e3__valid_<ligne>_3` (le test) et `_5` (le verdict). Les bonnes options sont LUES dans la définition
     JSON de la section ; une option fausse exprès (le test qui ne mesure rien) doit écrire son retour sous sa case. */
  const remplirTableau = (faux) => page.evaluate(faux => {
    const sec = document.getElementById("ex_4e_e3").closest(".atelier-incruste");
    const D = JSON.parse(sec.querySelector('script[type="application/json"]').textContent).exercices.ex_4e_e3;
    const t = D.widgets.find(w => w.type === "tableau");
    let piege = null;
    t.cases.forEach(c => {
      const s = document.getElementsByName(c.name)[0];
      const mauvaise = faux && !piege && Object.keys(c.retours || {})[0];
      s.value = mauvaise || c.bonne; s.dispatchEvent(new Event("change", { bubbles: true }));
      if (mauvaise) piege = { name: c.name, attendu: c.retours[mauvaise] };
    });
    return { menus: t.cases.length, noms: t.cases.every(c => /^ex_4e_e3__valid_\d_[35]$/.test(c.name)), piege };
  }, faux);
  const essai = await remplirTableau(true);
  await page.click("#ex_4e_e3 button.verifier");
  await page.waitForTimeout(100);
  const sous = await page.evaluate(n => {
    const r = document.getElementById(n + "-retour");
    return { texte: r.textContent, visible: r.offsetHeight > 0, lie: document.getElementById(n).getAttribute("aria-describedby") === n + "-retour" };
  }, essai.piege.name);
  ok("act. 2 : l'exercice inséré a ses 8 menus dans le tableau ; un test faux exprès écrit son retour sous sa case",
     essai.menus === 8 && essai.noms && sous.visible && sous.lie && sous.texte.startsWith("✘")
     && sous.texte.includes(essai.piege.attendu.slice(0, 25)), sous.texte.slice(0, 70));
  await remplirTableau(false);
  await page.fill("#ex_4e_e3__proto", "Je lance un arrosage. Dès qu'il s'arrête, je démarre un chronomètre et je mesure le temps " +
                  "jusqu'à l'arrivée du compte rendu sur le smartphone. L'exigence est validée si le message arrive en 5 min au plus.");
  await page.click("#ex_4e_e3 button.verifier");
  await page.waitForTimeout(100);
  ok("act. 2 : l'exercice inséré, rempli juste, est réussi",
     /Tout est juste/.test(await page.locator("#ex_4e_e3 .retour").innerText()));
  await shot(page, "exigences_insere", "#ex_4e_e3 .retour");

  await page.click('.btn.check[data-check="3"]');
  await page.waitForTimeout(150);
  const fb3 = (await page.locator("#fb3").textContent()) || "";
  ok("act. 2 : validée 6/6 une fois l'exercice inséré réussi", /activité validée/.test(fb3) && /6\/6/.test(fb3), fb3.slice(0, 60));
  ok("progression : 3 / 6 après les activités 0, 1 et 2",
     /^3 \/ 6/.test((await page.locator("#progTxt").textContent()).trim()));

  await page.waitForTimeout(150);
  const memo = await page.evaluate(k => JSON.parse(localStorage.getItem(k) || "{}"), CFG.cle);
  ok("sauvegarde : les champs de l'exercice inséré restent hors de la clé de la séquence",
     !Object.keys(memo.inputs || {}).some(id => id.startsWith("ex_4e_e3")));
  await page.reload();
  await page.waitForFunction(() => /chronomètre/.test((document.getElementById("ex_4e_e3__proto") || {}).value || ""),
                             null, {timeout: 5000}).catch(() => {});
  await page.waitForTimeout(150);
  ok("restauration : la réponse de l'exercice inséré survit au rechargement (clé de l'atelier)",
     /chronomètre/.test(await page.inputValue("#ex_4e_e3__proto")));
  const retrouves = await page.evaluate(() => {
    const sec = document.getElementById("ex_4e_e3").closest(".atelier-incruste");
    const D = JSON.parse(sec.querySelector('script[type="application/json"]').textContent).exercices.ex_4e_e3;
    const t = D.widgets.find(w => w.type === "tableau");
    return t.cases.filter(c => { const s = document.getElementsByName(c.name)[0];
      return s.value === c.bonne && s.parentNode.querySelector(".menu-vu").textContent === s.options[s.selectedIndex].text; }).length;
  });
  ok("restauration : les 8 menus du tableau de l'exercice inséré retrouvent leur choix, écrit en texte dans la case",
     retrouves === 8, retrouves + " / 8");
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
  /* Ces QCM sont passés à la génération actuelle du dépôt (30 questions, {q, o, r, expl, d…}, une
     réfutation par distracteur) : le banc lit les deux formats et vérifie les réfutations (24/10/2026). */
  const meta = await pq.evaluate(src => {
    const m = src.match(/const (?:QUESTIONS|questions)\s*=\s*(\[[\s\S]*?\n\];)/);
    if (!m) return null;
    let q;
    try { q = eval(m[1].replace(/;\s*$/, "")); } catch { return null; }
    if (!Array.isArray(q)) return null;
    const rep = {};
    q.forEach(x => { const i = (x.ok !== undefined ? x.ok : x.r); rep[i] = (rep[i] || 0) + 1; });
    /* deux générations de QCM : l'ancienne {q, opts, ok, exp}, l'actuelle {q, o, r, expl, d…} */
    const sansExp = q.filter(x => !((x.exp || x.expl) && String(x.exp || x.expl).trim())).length;
    const sansQuatre = q.filter(x => !((x.opts || x.o) && (x.opts || x.o).length === 4)).length;
    const refutations = q.filter(x => Array.isArray(x.d)).length;
    return { n: q.length, rep, sansExp, sansQuatre, refutations };
  }, fs.readFileSync(path.join(LOT, CFG.qcm), "utf8"));
  if (meta) {
    ok("QCM : le tableau des questions est lisible et chargé", meta.n > 0, meta.n + " questions");
    ok("QCM : chaque question a 4 propositions", meta.sansQuatre === 0, meta.sansQuatre + " anomalies");
    ok("QCM : chaque question porte une explication", meta.sansExp === 0, meta.sansExp + " sans explication");
    ok("QCM : les 4 positions servent de bonne réponse",
       Object.keys(meta.rep).length === 4, JSON.stringify(meta.rep));
    ok("QCM : génération actuelle — chaque question réfute ses distracteurs",
       meta.refutations === meta.n, meta.refutations + " question(s) sur " + meta.n + " avec réfutations");
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
