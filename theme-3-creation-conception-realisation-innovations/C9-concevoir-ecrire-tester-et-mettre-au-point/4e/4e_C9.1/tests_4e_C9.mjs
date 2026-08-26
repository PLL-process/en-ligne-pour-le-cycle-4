#!/usr/bin/env node
/* Suite de tests Playwright du lot 4e_C9 « Le jardin connecté se programme ».

   La suite SIMULE la séquence comme un élève et prend une capture d'écran à
   chaque action (dossier passé en argument 2, défaut /tmp/captures_jardin).
   Elle ne déclare que ce qu'elle exécute.

   Usage : node tests_4e_C9.mjs [dossier_du_lot] [dossier_captures]            */
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
const CAP = path.resolve(process.argv[3] || "/tmp/captures_jardin");
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

/* ── liens locaux ── */
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
  ok("liens locaux : zéro lien cassé dans le lot", casses.length === 0, casses.join(" · ") || (htmls.length + " HTML parcourus"));
}

const run = async () => {
  verifLiens();
  const navigateur = await chromium.launch();
  const ctx = await navigateur.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await ctx.newPage();
  const erreursJS = [];
  page.on("pageerror", e => erreursJS.push(String(e)));
  page.on("dialog", d => d.accept());

  /* ════════ SÉQUENCE ════════ */
  const SEQ = "sequence_4e_C9_jardin-programme.html";
  await page.goto(url(SEQ));
  await page.waitForTimeout(600);
  await shot(page, "sequence_accueil");
  ok("séquence : chargement file:// sans erreur JS", erreursJS.length === 0, erreursJS.join(" | "));

  /* billet d'entrée — sans note, hors progression (règle n°26) */
  await page.selectOption("#be_1", { index: 1 });
  await page.selectOption("#be_2", { index: 1 });
  await page.selectOption("#be_3", "ACQUÉRIR");
  await page.click("#btnBillet");
  const billet = await page.textContent("#fbBillet");
  ok("billet d'entrée : feedback affiché, et déclaré hors progression",
     billet.includes("3 / 3") && billet.includes("ne compte pas"), billet.slice(0, 60));
  ok("billet d'entrée : la progression reste à 0", (await page.textContent("#progTxt")).includes("0 / 6"));
  await shot(page, "billet_entree");

  /* identité + hypothèses */
  await page.fill("#id_nom", "TEST"); await page.fill("#id_prenom", "Éla"); await page.fill("#id_classe", "4eT");
  await page.fill("#hyp1", "Le programme a besoin de l'humidité du sol et de l'heure ; il arrose si la terre est sèche et si c'est le matin.");
  await page.fill("#hyp2", "Je testerais des valeurs autour du seuil, surtout 39 et 40.");

  /* ── tableau de bord (règle n°30) ── */
  ok("tableau de bord : les 6 activités listées", await page.locator("#tachesBandeau .tache").count() === 6);

  /* ════════ ACTIVITÉ 1 ════════ */
  for (const [id, v] of [["a1_1","ACQUÉRIR"],["a1_2","TRAITER"],["a1_3","COMMUNIQUER"],["a1_4","CONVERTIR"]])
    await page.selectOption("#" + id, v);
  await page.selectOption("#a1_5", { index: 1 });
  await page.selectOption("#a1_r1", { index: 1 });
  await page.selectOption("#a1_r2", { index: 1 });
  await page.click('[data-check="1"]');
  ok("verrou de rédaction : act. 1 refusée sans la justification écrite",
     (await page.textContent("#fb1")).includes("justification"));
  await page.fill("#a1_just", "L'heure est une entrée parce que le programme s'en sert pour décider, exactement comme il se sert de l'humidité ; ce qui change est son origine, elle vient de l'horloge et non du monde physique. Sans elle, on arroserait en plein soleil.");
  await page.click('[data-check="1"]');
  ok("activité 1 validée (7/7 + justification)", (await page.textContent("#fb1")).includes("7 / 7"), await page.textContent("#fb1"));
  await shot(page, "act1_validee");

  /* ════════ ACTIVITÉ 2 ════════ */
  for (const [id, v] of [["ag1","1"],["ag2","2"],["ag3","3"],["ag4","4"],["ag5","5"]])
    await page.selectOption("#" + id, v);
  for (const id of ["a2_q1","a2_q2","a2_q3","a2_q4"]) await page.selectOption("#" + id, { index: 1 });
  await page.fill("#prog1", "SEUIL = 40\nlire humidite -> H\nlire heure -> heure\nSI H < SEUIL ET heure >= 6 ET heure <= 10 ALORS\n    allumer pompe\nSINON\n    eteindre pompe\nFIN SI");
  await page.click('[data-check="2"]');
  ok("activité 2 validée (ordre + lecture + pseudo-code avec ET et bornes)",
     (await page.textContent("#fb2")).includes("5 / 5"), await page.textContent("#fb2"));
  await shot(page, "act2_validee");

  /* ════════ LE BANC D'ESSAI ════════ */
  await page.click('.seance-tab[data-panel="s2"]');
  const lcd = async () => (await page.textContent("#bL1")).trim();

  await page.fill("#bHumNum", "25"); await page.waitForTimeout(200);
  ok("banc : sol sec à 8 h → POMPE ON", (await lcd()) === "POMPE ON", await lcd());
  await page.fill("#bHumNum", "55"); await page.waitForTimeout(200);
  ok("banc : sol humide à 8 h → POMPE OFF", (await lcd()) === "POMPE OFF", await lcd());
  await page.fill("#bHeure", "23"); await page.dispatchEvent("#bHeure", "input");
  await page.fill("#bHumNum", "25"); await page.waitForTimeout(200);
  ok("banc : sol sec mais 23 h → POMPE OFF (le ET exige les deux conditions)",
     (await lcd()) === "POMPE OFF", await lcd());
  await shot(page, "banc_hors_plage", "#bancCard");

  await page.fill("#bHeure", "8"); await page.dispatchEvent("#bHeure", "input");
  await page.fill("#bHumNum", "39"); await page.waitForTimeout(200);
  ok("banc : frontière 39 % → POMPE ON", (await lcd()) === "POMPE ON", await lcd());
  await page.fill("#bHumNum", "40"); await page.waitForTimeout(200);
  ok("banc : frontière 40 % pile → POMPE OFF (40 < 40 est FAUX)", (await lcd()) === "POMPE OFF", await lcd());
  await shot(page, "banc_frontieres", "#bancCard");

  /* ════════ ACTIVITÉ 3 ════════ */
  for (const id of ["a3_q1","a3_q2","a3_q3","a3_q4"]) await page.selectOption("#" + id, { index: 1 });
  await page.click('[data-check="3"]');
  ok("verrou de rédaction : act. 3 refusée sans journal chiffré",
     (await page.textContent("#fb3")).includes("VALEURS"));
  await page.fill("#a3_journal", "J'ai mis H = 25 et heure = 8, la console a affiché POMPE ON. Puis H = 55 : POMPE OFF. Enfin H = 25 avec heure = 23 : POMPE OFF, ce qui m'a surpris au début.");
  await page.click('[data-check="3"]');
  ok("activité 3 validée (4/4 + journal + essais au banc)",
     (await page.textContent("#fb3")).includes("4 / 4") && !(await page.textContent("#fb3")).includes("banc d'essai"),
     await page.textContent("#fb3"));
  await shot(page, "act3_validee");

  /* ════════ ACTIVITÉ 4 — le jeu d'essais ════════ */
  for (const [id, v] of [["a4_a1","pompe ON"],["a4_a2","pompe OFF"],["a4_a3","pompe OFF"],
                         ["a4_a4","pompe ON"],["a4_a5","pompe OFF"]])
    await page.selectOption("#" + id, v);
  await page.selectOption("#a4_a6", { index: 1 });
  await page.selectOption("#a4_m1", { index: 1 });
  await page.selectOption("#a4_m2", { index: 1 });
  for (let i = 1; i <= 6; i++) await page.selectOption("#a4_o" + i, "conforme");
  await page.click('[data-check="4"]');
  ok("activité 4 validée (8/8 attendus + 6 observés + frontières exécutées)",
     (await page.textContent("#fb4")).includes("8 / 8"), await page.textContent("#fb4"));
  await shot(page, "act4_validee");

  /* ════════ ACTIVITÉ 5 — la démonstration de l'hystérésis ════════ */
  await page.click('.seance-tab[data-panel="s3"]');
  for (const id of ["a5_q1","a5_q2","a5_q3","a5_q4","a5_q5"]) await page.selectOption("#" + id, { index: 1 });
  await page.fill("#a5_diag", "La pompe change d'état 6 fois en 70 secondes alors que l'humidité n'a varié que de 2 points. Le relais s'use à chaque manœuvre, la pompe démarre sans cesse, et l'eau arrive par à-coups qui ne descendent jamais aux racines.");
  await page.fill("#prog3", "SEUIL_BAS = 35\nSEUIL_HAUT = 45\nlire humidite -> H\nSI H < SEUIL_BAS ALORS\n    allumer pompe\nSINON SI H > SEUIL_HAUT ALORS\n    eteindre pompe\nFIN SI");

  /* le cœur de la séquence : la MÊME mesure, deux règles, deux comportements */
  await page.click('.seance-tab[data-panel="s2"]');
  await page.check('input[name="bMode"][value="un"]');
  await page.click("#btnRAZ");
  await page.click("#btnTrembler"); await page.waitForTimeout(3800);
  const nUn = parseInt(await page.textContent("#bCompteur"), 10);
  ok("banc : en UN seuil, la mesure qui tremble fait clignoter la pompe", nUn >= 4, nUn + " basculements");
  await shot(page, "banc_clignotement", "#bancCard");

  await page.check('input[name="bMode"][value="deux"]');
  await page.click("#btnRAZ");
  await page.click("#btnTrembler"); await page.waitForTimeout(3800);
  const nDeux = parseInt(await page.textContent("#bCompteur"), 10);
  ok("banc : en DEUX seuils, le MÊME tremblement ne fait plus clignoter", nDeux <= 1, nDeux + " basculement(s)");
  ok("banc : la démonstration est probante (au moins 4 basculements évités)", nUn - nDeux >= 4, nUn + " → " + nDeux);
  await shot(page, "banc_hysteresis", "#bancCard");

  await page.click('.seance-tab[data-panel="s3"]');
  await page.fill("#a5_n1", String(nUn));
  await page.fill("#a5_n2", String(nDeux));
  await page.click('[data-check="5"]');
  ok("activité 5 validée (5/5 + diagnostic + programme à trois cas + démonstration)",
     (await page.textContent("#fb5")).includes("5 / 5") && !(await page.textContent("#fb5")).includes("démonstration au banc"),
     await page.textContent("#fb5"));
  await shot(page, "act5_validee");

  /* ════════ ACTIVITÉ 6 — réinvestissement sans squelette ════════ */
  await page.selectOption("#a6_q1", { index: 1 });
  await page.click('[data-check="6"]');
  ok("verrou : act. 6 refusée sans programme complet", (await page.textContent("#fb6")).includes("seuils"));
  await page.fill("#reinv", "SEUIL_BAS = 20\nSEUIL_HAUT = 60\nlire luminosite -> L\nSI L < SEUIL_BAS ALORS\n    allumer lampadaire\nSINON SI L > SEUIL_HAUT ALORS\n    eteindre lampadaire\nFIN SI");
  await page.fill("#a6_just", "J'allume à 20 et j'éteins à 60, soit une bande de 40 points, parce que la luminosité varie beaucoup au crépuscule : nuages, phares, reflets.");
  await page.click('[data-check="6"]');
  ok("activité 6 validée (programme sans squelette + justification chiffrée)",
     (await page.textContent("#fb6")).includes("1 / 1") && !(await page.textContent("#fb6")).includes("Justifie"),
     await page.textContent("#fb6"));
  await shot(page, "act6_validee");

  /* ════════ progression, persistance ════════ */
  ok("progression : 6 / 6 activités validées", (await page.textContent("#progTxt")).includes("6 / 6"));
  const coches = await page.evaluate(() => ["s1","s2","s3"].map(s => document.getElementById("done-" + s).textContent.trim()).join(""));
  ok("onglets : les 3 séances cochées ✔", coches === "✔✔✔", coches);
  ok("tableau de bord : les 6 tâches cochées",
     await page.locator("#tachesBandeau .tache.fait").count() === 6);
  await page.fill("#bilan1", "J'ai appris qu'un programme peut être juste et inutilisable.");
  await page.check('input[name="conf_c91"][value="3"]');
  await page.check('input[name="conf_c93"][value="3"]');
  ok("bilan : le rappel d'hypothèse est affiché", await page.isVisible("#rappelHyp"));
  await shot(page, "bilan_6sur6");

  await page.waitForTimeout(900);
  await page.reload(); await page.waitForTimeout(700);
  ok("persistance : progression 6/6 restaurée après rechargement", (await page.textContent("#progTxt")).includes("6 / 6"));
  ok("persistance : réponses restaurées (prog3 contient les deux seuils)",
     (await page.inputValue("#prog3")).includes("35") && (await page.inputValue("#prog3")).includes("45"));
  ok("persistance : verrous du banc restaurés (frontières cochées)",
     (await page.textContent("#v-front")).startsWith("✔"));
  await shot(page, "persistance");

  /* ════════ règles d'or vérifiables à l'écran ════════ */
  ok("règle n°4 : UN SEUL bouton QCM dans la séquence", await page.locator("a.btn.qcm").count() === 1);
  ok("règle n°101 : 2 boutons « séance suivante »", await page.locator("button.vers-seance").count() === 2);
  await page.click('.seance-tab[data-panel="s1"]');
  await page.locator('button.vers-seance[data-vers="s2"]').click();
  await page.waitForTimeout(250);
  ok("règle n°101 : le bouton bascule réellement sur la séance suivante",
     await page.locator("#s2.active").count() === 1);

  ok("règle n°122 : sélecteur de parcours dans la barre d'outils (4 boutons)",
     await page.locator(".toolbar .parcours-btn").count() === 4);
  await page.click('.parcours-btn[data-choix="c"]');
  await page.waitForTimeout(200);
  ok("règle n°122 : choisir 🅲 masque les blocs propres au parcours 🅱",
     await page.evaluate(() => document.body.classList.contains("parcours-c") &&
       [...document.querySelectorAll('[data-parcours="b"]')].every(e => getComputedStyle(e).display === "none")));
  ok("règle n°122 : le choix ne retire AUCUNE question",
     await page.evaluate(() => [...document.querySelectorAll("input[id],select[id],textarea[id]")]
       .filter(e => e.closest("[data-parcours]")).length === 0));
  await page.click('.parcours-btn[data-choix="tous"]');
  await page.waitForTimeout(200);

  await page.click("#btnEssentiel");
  ok("règle n°29 : le mode essentiel masque le référentiel",
     await page.evaluate(() => document.body.classList.contains("essentiel") &&
       getComputedStyle(document.querySelector(".referentiel-card")).display === "none"));
  await shot(page, "mode_essentiel");
  await page.click("#btnEssentiel");

  ok("règle n°117 : chaque figure porte un alt long et une description dépliable",
     await page.evaluate(() => {
       const figs = [...document.querySelectorAll("img.figure")];
       return figs.length >= 4 && figs.every(i => (i.getAttribute("alt")||"").length >= 120)
              && figs.every(i => i.getAttribute("aria-describedby") &&
                   document.getElementById(i.getAttribute("aria-describedby")));
     }));
  await page.click('.seance-tab[data-panel="s1"]');   /* la figure doit être dans le panneau visible */
  await page.waitForTimeout(200);
  await page.locator("#s1 img.figure").first().click();
  ok("règle n°92 : la loupe ouvre l'image en grand", await page.isVisible(".loupe-fond[data-ouvert]"));
  await page.keyboard.press("Escape");
  ok("loupe : Échap referme", !(await page.isVisible(".loupe-fond[data-ouvert]")));
  ok("séquence : zéro erreur JS sur tout le parcours", erreursJS.length === 0, erreursJS.join(" | "));

  /* ════════ QCM ════════ */
  const QCM = "qcm_4e_C9_jardin-programme.html";
  await page.goto(url(QCM)); await page.waitForTimeout(500);
  await shot(page, "qcm_accueil");
  ok("QCM : 30 questions, grille complète",
     await page.evaluate("QUESTIONS.length") === 30 && await page.locator("#grille button").count() === 30);
  const parts = await page.evaluate("['C9.1','C9.2','C9.3'].map(c=>QUESTIONS.filter(q=>q.c===c).length)");
  ok("QCM : 10 questions par code (C9.1 / C9.2 / C9.3)", parts.join("/") === "10/10/10", parts.join("/"));
  ok("QCM : 4 questions illustrées", await page.evaluate("QUESTIONS.filter(q=>q.img).length") === 4);
  const rep = await page.evaluate("[0,1,2,3].map(k=>QUESTIONS.filter(q=>q.r===k).length)");
  ok("QCM : bonnes réponses réparties A/B/C/D", JSON.stringify(rep) === "[8,7,7,8]", rep.join("/"));
  ok("QCM : chaque question a 4 réfutations cohérentes (d[r] vide, 3 non vides)",
     await page.evaluate("QUESTIONS.every(q=>q.d.length===4 && q.d[q.r]==='' && q.d.filter(x=>x).length===3)"));
  ok("QCM : chaque question porte explication, exemple, erreur fréquente et à-retenir",
     await page.evaluate("QUESTIONS.every(q=>q.expl&&q.ex&&q.err&&q.ret)"));

  const r1 = await page.evaluate("QUESTIONS[0].r");
  await page.locator("#qOptions .option").nth(r1).click();
  await page.click("#btnValider"); await page.waitForTimeout(250);
  const corr = await page.textContent("#corrBloc");
  ok("QCM : réponse correcte comptée + correction complète",
     ["Correct","Explication","Exemple","Erreur fréquente","Pourquoi les autres","À retenir"].every(x => corr.includes(x)));
  await shot(page, "qcm_correction");

  const idxImg = await page.evaluate("QUESTIONS.findIndex(q=>q.img)");
  await page.locator("#grille button").nth(idxImg).click(); await page.waitForTimeout(250);
  ok("QCM : la question illustrée affiche son document", await page.isVisible("#qFigure img"));
  await shot(page, "qcm_illustree");

  const r2 = await page.evaluate(`(QUESTIONS[${idxImg}].r+1)%4`);
  await page.locator("#qOptions .option").nth(r2).click();
  await page.click("#btnValider"); await page.waitForTimeout(250);
  ok("QCM : réponse fausse comptée", (await page.textContent("#corrBloc")).includes("Incorrect"));
  await page.click("#btnMarquer");
  ok("QCM : marquage 🔖 à revoir", (await page.textContent("#dMarq")) === "1");

  await page.click('[data-mode="cible"]');
  await page.selectOption("#selComp", "C9.3"); await page.waitForTimeout(250);
  ok("QCM : révision ciblée 4e_C9.3 = 10 questions", await page.locator("#grille button").count() === 10);
  await page.click('[data-mode="erreurs"]');
  ok("QCM : mode « uniquement mes erreurs » = 1 question", await page.locator("#grille button").count() === 1);
  await page.click('[data-mode="complet"]');
  await shot(page, "qcm_modes");

  /* scénarios de notes */
  await page.evaluate(() => { localStorage.clear(); }); await page.reload(); await page.waitForTimeout(400);
  await page.evaluate(() => {
    for (let i = 0; i < QUESTIONS.length; i++) {
      etat.courante = i; rendreTout();
      document.querySelectorAll("#qOptions .option")[QUESTIONS[i].r].click();
      document.getElementById("btnValider").click();
    }
  });
  await page.click("#btnTerminer"); await page.waitForTimeout(300);
  ok("scénario 1 (30 justes) : 20,0 /20 · 100 %",
     (await page.textContent("#rNote")).includes("20,0") && (await page.textContent("#rPct")).includes("100"));
  ok("scénario 1 : bilan par compétence = 3 lignes maîtrisées",
     await page.evaluate(() => document.querySelectorAll("#tblBilan tbody tr").length === 3 &&
       document.querySelectorAll("#tblBilan .maitrise-ok").length === 3));
  await shot(page, "qcm_tout_juste");

  await page.evaluate(() => { localStorage.clear(); }); await page.reload(); await page.waitForTimeout(400);
  await page.evaluate(() => {
    for (let i = 0; i < QUESTIONS.length; i++) {
      etat.courante = i; rendreTout();
      const cible = (i < 15) ? QUESTIONS[i].r : (QUESTIONS[i].r + 1) % 4;
      document.querySelectorAll("#qOptions .option")[cible].click();
      document.getElementById("btnValider").click();
    }
  });
  await page.click("#btnTerminer"); await page.waitForTimeout(300);
  ok("scénario 2 (15 justes / 15 fausses) : 10,0 /20 · 50 %",
     (await page.textContent("#rNote")).includes("10,0") && (await page.textContent("#rPct")).includes("50"));

  await page.evaluate(() => { localStorage.clear(); }); await page.reload(); await page.waitForTimeout(400);
  await page.evaluate(() => {
    for (let i = 0; i < 12; i++) {
      etat.courante = i; rendreTout();
      const cible = (i < 6) ? QUESTIONS[i].r : (QUESTIONS[i].r + 1) % 4;
      document.querySelectorAll("#qOptions .option")[cible].click();
      document.getElementById("btnValider").click();
    }
  });
  await page.click("#btnTerminer"); await page.waitForTimeout(300);
  ok("scénario 3 (6 justes, 6 fausses, 18 NR) : 4,0 /20 · 18 non répondues",
     (await page.textContent("#rNote")).includes("4,0") && (await page.textContent("#rNon")) === "18");
  await shot(page, "qcm_non_repondues");
  ok("QCM : zéro erreur JS sur tout le parcours", erreursJS.length === 0, erreursJS.join(" | "));

  /* ════════ Synthèses + mobile ════════ */
  for (const f of ["Synthèses/synthese_eleve_4e_C9.html", "Synthèses/synthese_professeur_4e_C9.html"]) {
    if (!fs.existsSync(path.join(LOT, f))) continue;
    await page.goto(url(f)); await page.waitForTimeout(300);
    ok("synthèse « " + path.basename(f) + " » : chargement sans erreur JS", erreursJS.length === 0);
  }
  await shot(page, "synthese_eleve");

  const mob = await ctx.browser().newContext({ viewport: { width: 390, height: 844 } });
  const pm = await mob.newPage();
  const errMob = []; pm.on("pageerror", e => errMob.push(String(e)));
  await pm.goto(url(SEQ)); await pm.waitForTimeout(600);
  const debordement = await pm.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  ok("mobile 390 px : pas de défilement horizontal, zéro erreur JS", debordement <= 1 && errMob.length === 0, "débord=" + debordement);
  await pm.screenshot({ path: path.join(CAP, String(++nCap).padStart(2, "0") + "_mobile_390px.png") });
  await mob.close();

  await navigateur.close();

  const reussis = resultats.filter(r => r.ok).length;
  console.log(`\n══ ${reussis} / ${resultats.length} tests réussis · ${nCap} captures dans ${CAP} ══`);
  fs.writeFileSync(path.join(CAP, "resultats.json"), JSON.stringify(resultats, null, 2));
};
run().catch(e => { console.error("ÉCHEC de la suite :", e); process.exit(2); });
