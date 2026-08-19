#!/usr/bin/env node
/* Suite de tests Playwright du lot 3e_C9.2 + 3e_C8.3 « La station d'alerte
   cyclonique se programme ».

   La suite SIMULE la séquence comme un élève (méthode du « dé de 5e ») et
   prend une capture d'écran à chaque action (dossier passé en argument 2,
   défaut /tmp/captures_station). Elle ne déclare que ce qu'elle exécute.

   Usage : node tests_3e_C9.2-C8.3.mjs [dossier_du_lot] [dossier_captures]      */
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";

/* Playwright : installation locale si présente, sinon installation globale. */
let chromium;
try { ({ chromium } = await import("playwright")); }
catch {
  const racineGlobale = execSync("npm root -g").toString().trim();
  ({ chromium } = createRequire(import.meta.url)(path.join(racineGlobale, "playwright", "index.js")));
}

const LOT = path.resolve(process.argv[2] || ".");
const CAP = path.resolve(process.argv[3] || "/tmp/captures_station");
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

/* ── vérification des liens locaux (href/src/data) des HTML du lot ── */
function verifLiens() {
  const htmls = [];
  (function walk(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const p = path.join(d, e.name);
      if (e.isDirectory()) walk(p);
      else if (e.name.endsWith(".html")) htmls.push(p);
    }
  })(LOT);
  let casses = [];
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

  /* ════════ SÉQUENCE — simulée comme un élève ════════ */
  const SEQ = "sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html";
  await page.goto(url(SEQ));
  await page.waitForTimeout(600);
  await shot(page, "sequence_accueil");
  ok("séquence : chargement file:// sans erreur JS", erreursJS.length === 0, erreursJS.join(" | "));

  /* billet d'entrée */
  await page.selectOption("#be_1", "Acquérir");
  await page.selectOption("#be_2", { index: 1 });
  await page.selectOption("#be_3", { index: 1 });
  await page.click("#btnBillet");
  ok("billet d'entrée : feedback sans note affiché", await page.locator("#fbBillet.show").count() === 1,
     (await page.textContent("#fbBillet")).slice(0, 40));
  await shot(page, "billet_entree");

  /* identité + hypothèses */
  await page.fill("#id_nom", "TEST"); await page.fill("#id_prenom", "Éla");
  await page.fill("#id_classe", "3eT");
  await page.fill("#hyp1", "Je pense que le programme compare la vitesse du vent à des seuils fixés par la mairie.");
  await page.fill("#hyp2", "Je testerais plusieurs vitesses, surtout autour des seuils.");
  await shot(page, "identite_hypotheses");

  /* activité 1 */
  await page.selectOption("#a1_e1", { index: 2 });
  await page.selectOption("#a1_e2", { index: 1 });
  await page.selectOption("#a1_e3", { index: 1 });
  for (const [id, v] of [["a1_1","Acquérir"],["a1_2","Acquérir"],["a1_3","Traiter"],["a1_4","Communiquer"],["a1_5","Communiquer"],["a1_6","Alimenter"]])
    await page.selectOption("#"+id, v);
  await page.fill("#a1_just", "Le bouton fait entrer l'information « l'agent a pris connaissance de l'alarme », produite par un humain, alors que l'anémomètre capte une grandeur physique.");
  await page.click('[data-check="1"]');
  ok("activité 1 validée (9/9 + justification)", (await page.textContent("#fb1")).includes("9 / 9"), await page.textContent("#fb1"));
  await shot(page, "act1_validee");

  /* activité 2 */
  await page.fill("#a2_s1", "150"); await page.fill("#a2_s2", "100");
  await page.selectOption("#a2_s3", "veille");
  for (const id of ["a2_q1","a2_q2","a2_q3","a2_q4"]) await page.selectOption("#"+id, { index: 1 });
  await page.click('[data-check="2"]');
  ok("activité 2 validée (algorithme + algorigramme 7/7)", (await page.textContent("#fb2")).includes("7 / 7"));
  await shot(page, "act2_validee");

  /* verrou : act3 doit REFUSER sans expériences au banc */
  await page.click('.seance-tab[data-panel="s2"]');
  await page.fill("#a3_p1", "125");
  await page.selectOption("#a3_p2", { index: 1 });
  await page.selectOption("#a3_p3", { index: 1 });
  await page.click('[data-check="3"]');
  ok("verrou expérientiel : act. 3 refusée sans manipulation au banc",
     (await page.textContent("#fb3")).includes("banc"), (await page.textContent("#fb3")).slice(0, 90));
  await shot(page, "act3_verrou_refuse");

  /* le banc : faire varier le vent, atteindre les 3 niveaux */
  for (const v of [10, 30, 60, 80, 42]) { await page.fill("#simVentNum", String(v)); await page.waitForTimeout(250); }
  ok("banc : LCD en VEILLE à 42 km/h", (await page.getAttribute("#simLcd", "class")).includes("lcd-vert"),
     await page.textContent("#simL1"));
  await shot(page, "banc_veille_42", "#bancCard");
  await page.fill("#simVentNum", "120"); await page.waitForTimeout(300);
  ok("banc : LCD en VIGILANCE à 120 km/h + DEL allumée",
     (await page.getAttribute("#simLcd", "class")).includes("lcd-orange") &&
     (await page.getAttribute("#simDel", "class")).includes("on"));
  await shot(page, "banc_vigilance_120", "#bancCard");
  await page.fill("#simVentNum", "187"); await page.waitForTimeout(300);
  ok("banc : ALERTE ROUGE à 187 km/h + buzzer qui sonne",
     (await page.getAttribute("#simLcd", "class")).includes("lcd-rouge") &&
     (await page.getAttribute("#simBuz", "class")).includes("on"));
  await shot(page, "banc_alerte_187", "#bancCard");

  /* act3 doit maintenant passer */
  await page.click('[data-check="3"]');
  ok("activité 3 validée après manipulations (verrous lecture + 3 niveaux)",
     (await page.textContent("#fb3")).includes("3 / 3") && !(await page.textContent("#fb3")).includes("banc"));
  await shot(page, "act3_validee");

  /* séance 3 : acquittement puis re-déclenchement */
  await page.click('.seance-tab[data-panel="s3"]');
  await page.fill("#simVentNum", "200"); await page.waitForTimeout(300);
  await page.click("#btnAcquit"); await page.waitForTimeout(300);
  ok("banc : acquittement — buzzer muet, écran TOUJOURS rouge, DEL allumée",
     !(await page.getAttribute("#simBuz", "class")).includes("on") &&
     (await page.getAttribute("#simLcd", "class")).includes("lcd-rouge") &&
     (await page.getAttribute("#simDel", "class")).includes("on"));
  await shot(page, "banc_acquitte", "#bancCard");
  await page.fill("#simVentNum", "50"); await page.waitForTimeout(400);
  await page.fill("#simVentNum", "210"); await page.waitForTimeout(400);
  ok("banc : nouvel événement — le buzzer REPART sans appui",
     (await page.getAttribute("#simBuz", "class")).includes("on"));
  await shot(page, "banc_retrigger", "#bancCard");

  /* activité 4 */
  for (const id of ["a4_q1","a4_q2","a4_q3","a4_q4"]) await page.selectOption("#"+id, { index: 1 });
  await page.fill("#a4_exp", "alarmeAcquittee sert à retenir que l'agent a répondu ; elle repasse à faux quand le niveau change, car un changement est un nouvel événement.");
  await page.click('[data-check="4"]');
  ok("activité 4 validée (chronogramme + 2 expériences tracées)", (await page.textContent("#fb4")).includes("4 / 4") && !(await page.textContent("#fb4")).includes("banc"));
  await shot(page, "act4_validee");

  /* activité 5 */
  for (const id of ["a5_q1","a5_q2","a5_q3","a5_q4","a5_q5"]) await page.selectOption("#"+id, { index: 1 });
  await page.fill("#a5_exp", "La trace montre que la vitesse monte correctement de 97 à 161 : le capteur et la conversion sont innocentés, c'est la décision qui rate.");
  await page.click('[data-check="5"]');
  ok("activité 5 validée (lecture C++ + diagnostic)", (await page.textContent("#fb5")).includes("5 / 5"));
  await shot(page, "act5_validee");

  /* séance 4 : activité 6 */
  await page.click('.seance-tab[data-panel="s4"]');
  for (const id of ["a6_v1","a6_v2","a6_v3","a6_v4","a6_v5"]) await page.selectOption("#"+id, { index: 1 });
  await page.fill("#a6_redac", "Essais nominaux : 42 (veille), 120 (vigilance), 200 (alerte). Frontières : 99, 100, 149, 150 car les bugs vivent aux frontières. Performance : je chronomètre le temps entre le franchissement de 150 et l'affichage, exigence moins d'une seconde. Interaction : appui sur le bouton pendant l'alarme (le son se coupe), puis redescente et remontée (le buzzer repart). Règle de décision : recette prononcée si 10 essais sur 10 sont réussis, sinon ajournée avec réserves.");
  await page.click('[data-check="6"]');
  ok("activité 6 validée (protocole rédigé, 4 familles + règle)", (await page.textContent("#fb6")).includes("5 / 5") && !(await page.textContent("#fb6")).includes("familles"));
  await shot(page, "act6_protocole_redige");

  /* activité 7 : exécution — frontières exactes + chrono */
  for (const v of [99, 100, 149, 150]) { await page.fill("#simVentNum", String(v)); await page.waitForTimeout(350); }
  await shot(page, "banc_frontieres_executees", "#bancCard");
  await page.click("#btnChrono");
  await page.waitForTimeout(1800);
  const chrono = await page.textContent("#chronoNote");
  ok("banc : temps de réponse mesuré et conforme (< 1 s)", chrono.includes("CONFORME ✔"), chrono.slice(0, 90));
  await shot(page, "banc_chrono", "#bancCard");
  await page.selectOption("#a7_a4", "veille");
  await page.selectOption("#a7_a5", "vigilance orange");
  await page.selectOption("#a7_a6", "vigilance orange");
  await page.selectOption("#a7_a7", "alerte rouge");
  for (let i = 1; i <= 10; i++) await page.selectOption("#a7_r" + i, "conforme");
  await page.fill("#a7_pv", "Procès-verbal de recette — le 19/08, nous avons exécuté les 10 essais du protocole sur le banc de simulation. 10 conformes sur 10, frontières vérifiées, temps de réponse 0,3 s (exigence < 1 s). Recette prononcée, sans réserve.");
  await page.click('[data-check="7"]');
  ok("activité 7 validée (frontières + chrono exécutés, 10 verdicts, PV)",
     (await page.textContent("#fb7")).includes("4 / 4") && !(await page.textContent("#fb7")).includes("banc"));
  await shot(page, "act7_recette_validee");

  /* progression + persistance */
  ok("progression : 7 / 7 activités validées", (await page.textContent("#progTxt")).includes("7 / 7"));
  const coches = await page.evaluate(() => ["s1","s2","s3","s4"].map(s => document.getElementById("done-"+s).textContent.trim()).join(""));
  ok("onglets : les 4 séances cochées ✔", coches === "✔✔✔✔", coches);
  await page.fill("#bilan1", "J'ai appris à programmer une interaction humain-machine.");
  await page.check('input[name="conf_c92"][value="3"]');
  await page.check('input[name="conf_c83"][value="3"]');
  ok("bilan : rappel d'hypothèse affiché", await page.isVisible("#rappelHyp"));
  await shot(page, "bilan_7sur7");
  await page.waitForTimeout(900); /* laisse la sauvegarde différée s'écrire */
  await page.reload(); await page.waitForTimeout(700);
  ok("persistance : progression 7/7 restaurée après rechargement", (await page.textContent("#progTxt")).includes("7 / 7"));
  ok("persistance : réponses restaurées (a2_s1 = 150)", (await page.inputValue("#a2_s1")) === "150");
  ok("persistance : verrous du banc restaurés (frontières cochées)",
     (await page.textContent("#v-bornes")).startsWith("✔"));
  await shot(page, "persistance_apres_rechargement");

  /* blocs règle n°4 + mode essentiel + loupe */
  const boutonsQCM = await page.locator('a.btn.qcm').count();
  ok("règle n°4 : UN SEUL bouton QCM dans la séquence", boutonsQCM === 1, String(boutonsQCM));
  const bonusCorriges = await page.evaluate(() => {
    const b = [...document.querySelectorAll("section.card h2")].find(h => h.textContent.includes("Bonus"));
    return b ? b.closest("section").querySelectorAll("details.correction").length : 0;
  });
  ok("règle n°86 : chaque défi bonus a son corrigé replié (3/3)", bonusCorriges === 3, String(bonusCorriges));
  await page.click("#btnEssentiel");
  ok("mode essentiel : référentiel et corrections masqués",
     await page.evaluate(() => document.body.classList.contains("essentiel") &&
       getComputedStyle(document.querySelector(".referentiel-card")).display === "none"));
  await shot(page, "mode_essentiel_on");
  await page.click("#btnEssentiel");
  await page.locator('img.figure').first().click();
  ok("règle n°92 : la loupe ouvre l'image en grand", await page.isVisible(".loupe-fond[data-ouvert]"));
  await shot(page, "loupe_ouverte");
  await page.keyboard.press("Escape");
  ok("loupe : Échap referme", !(await page.isVisible(".loupe-fond[data-ouvert]")));
  ok("séquence : zéro erreur JS sur tout le parcours", erreursJS.length === 0, erreursJS.join(" | "));

  /* ════════ QCM ════════ */
  const QCM = "qcm_3e_C9.2-C8.3_station_alerte_cyclonique.html";
  await page.goto(url(QCM)); await page.waitForTimeout(500);
  await shot(page, "qcm_accueil");
  const nQ = await page.evaluate("QUESTIONS.length");
  ok("QCM : 30 questions, grille complète", nQ === 30 && await page.locator("#grille button").count() === 30);
  const parts = await page.evaluate("[QUESTIONS.filter(q=>q.c==='C9.2').length, QUESTIONS.filter(q=>q.c==='C8.3').length, QUESTIONS.filter(q=>q.img).length]");
  ok("QCM : répartition 15 C9.2 / 15 C8.3, 4 illustrées", parts[0] === 15 && parts[1] === 15 && parts[2] === 4, parts.join("/"));
  const repartition = await page.evaluate("[0,1,2,3].map(k=>QUESTIONS.filter(q=>q.r===k).length)");
  ok("QCM : bonnes réponses réparties A/B/C/D", JSON.stringify(repartition) === "[8,7,7,8]", repartition.join("/"));
  ok("QCM : chaque question a 4 réfutations cohérentes (d[r] vide, 3 non vides)",
     await page.evaluate("QUESTIONS.every(q=>q.d.length===4 && q.d[q.r]==='' && q.d.filter(x=>x).length===3)"));

  /* répondre juste à la question 1 */
  const r1 = await page.evaluate("QUESTIONS[0].r");
  await page.locator("#qOptions .option").nth(r1).click();
  await page.click("#btnValider"); await page.waitForTimeout(200);
  const corr = await page.textContent("#corrBloc");
  ok("QCM : réponse correcte comptée + correction complète",
     corr.includes("Correct") && corr.includes("Explication") && corr.includes("Exemple") &&
     corr.includes("Erreur fréquente") && corr.includes("Pourquoi les autres") && corr.includes("À retenir"));
  await shot(page, "qcm_correction_complete");

  /* question illustrée */
  const idxImg = await page.evaluate("QUESTIONS.findIndex(q=>q.img)");
  await page.locator("#grille button").nth(idxImg).click(); await page.waitForTimeout(200);
  ok("QCM : la question illustrée affiche son document", await page.isVisible("#qFigure img"));
  await shot(page, "qcm_question_illustree");

  /* réponse fausse + marquage */
  const r2 = await page.evaluate(`(QUESTIONS[${idxImg}].r+1)%4`);
  await page.locator("#qOptions .option").nth(r2).click();
  await page.click("#btnValider"); await page.waitForTimeout(200);
  ok("QCM : réponse fausse comptée", (await page.textContent("#corrBloc")).includes("Incorrect"));
  await page.click("#btnMarquer");
  ok("QCM : marquage 🔖 à revoir", (await page.textContent("#dMarq")) === "1");
  await shot(page, "qcm_erreur_marquee");

  /* modes */
  await page.click('[data-mode="dix"]');
  ok("QCM : mode 10 questions", await page.locator("#grille button").count() === 10);
  await page.click('[data-mode="cible"]');
  await page.selectOption("#selComp", "C8.3"); await page.waitForTimeout(200);
  ok("QCM : révision ciblée C8.3 = 15 questions", await page.locator("#grille button").count() === 15);
  await page.click('[data-mode="erreurs"]');
  ok("QCM : mode « uniquement mes erreurs » = 1 question", await page.locator("#grille button").count() === 1);
  await shot(page, "qcm_modes");
  await page.click('[data-mode="complet"]');

  /* minuteur */
  ok("QCM : minuteur démarré automatiquement à la 1re validation", !(await page.isDisabled("#tPause")));
  await page.click("#tPause");
  const t1 = await page.textContent("#timerDisp");
  await page.waitForTimeout(700);
  ok("QCM : pause fige le minuteur", (await page.textContent("#timerDisp")) === t1);

  /* persistance QCM */
  await page.reload(); await page.waitForTimeout(500);
  ok("QCM : sauvegarde/reprise après rechargement (réponses + marquage)",
     (await page.textContent("#dRep")) === "2" && (await page.textContent("#dMarq")) === "1");

  /* scénario de notes n°1 : tout juste (30/30 → 20,0) */
  await page.evaluate(() => { localStorage.clear(); }); await page.reload(); await page.waitForTimeout(400);
  await page.evaluate(async () => {
    for (let i = 0; i < QUESTIONS.length; i++) {
      document.querySelectorAll("#grille button")[0]; /* garde le DOM vivant */
      etat.courante = i; rendreTout();
      document.querySelectorAll("#qOptions .option")[QUESTIONS[i].r].click();
      document.getElementById("btnValider").click();
    }
  });
  await page.click("#btnTerminer"); await page.waitForTimeout(300);
  ok("scénario 1 (30 justes) : 20,0 /20 · 100 %", (await page.textContent("#rNote")).includes("20,0") && (await page.textContent("#rPct")).includes("100"));
  ok("scénario 1 : bilan par compétence = 2 lignes maîtrisées",
     await page.evaluate(() => [...document.querySelectorAll("#tblBilan tbody tr")].length === 2 &&
       [...document.querySelectorAll("#tblBilan .maitrise-ok")].length === 2));
  await shot(page, "qcm_scenario_tout_juste");

  /* scénario 2 : 15 justes + 15 fausses → 10,0 /20 */
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
  ok("scénario 2 (15 justes / 15 fausses) : 10,0 /20 · 50 %", (await page.textContent("#rNote")).includes("10,0") && (await page.textContent("#rPct")).includes("50"));
  await shot(page, "qcm_scenario_mixte");

  /* scénario 3 : 6 justes + 6 fausses + 18 non répondues → 4,0 /20 */
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
  await shot(page, "qcm_scenario_non_repondues");
  ok("QCM : zéro erreur JS sur tout le parcours", erreursJS.length === 0, erreursJS.join(" | "));

  /* ════════ Synthèses + mobile ════════ */
  for (const f of ["Synthèses/synthese_eleve_3e_C9.2-C8.3.html", "Synthèses/synthese_professeur_3e_C9.2-C8.3.html"]) {
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

  /* ── bilan ── */
  const reussis = resultats.filter(r => r.ok).length;
  console.log(`\n══ ${reussis} / ${resultats.length} tests réussis · ${nCap} captures dans ${CAP} ══`);
  fs.writeFileSync(path.join(CAP, "resultats.json"), JSON.stringify(resultats, null, 2));
};
run().catch(e => { console.error("ÉCHEC de la suite :", e); process.exit(2); });
