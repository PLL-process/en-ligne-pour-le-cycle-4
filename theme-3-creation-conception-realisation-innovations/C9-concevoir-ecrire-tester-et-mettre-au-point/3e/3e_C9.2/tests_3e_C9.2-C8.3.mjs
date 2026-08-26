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
  await page.fill("#a2_s1", "178"); await page.fill("#a2_s2", "118"); await page.fill("#a2_s3", "63");
  await page.selectOption("#a2_s4", "veille");
  for (const id of ["a2_q1","a2_q2","a2_q3","a2_q4","a2_q5","a2_q6","a2_q7","a2_q8","a2_q9","a2_q10"])
    await page.selectOption("#"+id, { index: 1 });
  await page.click('[data-check="2"]');
  ok("activité 2 validée (algorithme à 3 seuils + algorigramme 14/14, dont les 6 questions de lecture fine)",
     (await page.textContent("#fb2")).includes("14 / 14"), await page.textContent("#fb2"));
  await shot(page, "act2_validee");

  /* refonte v2 : les 6 questions ajoutées sous l'algorigramme existent bien */
  for (const id of ["a2_q5","a2_q6","a2_q7","a2_q8","a2_q9","a2_q10"])
    ok("question de lecture fine présente : #" + id, (await page.locator("#"+id).count()) === 1);
  ok("l'algorigramme distingue le commentaire du symbole (question a2_q7)",
     (await page.textContent("#a2_q7")).includes("commentaire de lecture"));

  /* verrou : act3 doit REFUSER sans expériences au banc */
  await page.click('.seance-tab[data-panel="s2"]');
  await page.fill("#a3_p1", "125");   // échelle unique : 512 x 250 / 1023
  for (const id of ["a3_p1b", "a3_p2", "a3_p2b", "a3_p3", "a3_p3b"]) await page.selectOption("#"+id, { index: 1 });
  await page.click('[data-check="3"]');
  ok("verrou expérientiel : act. 3 refusée sans manipulation au banc",
     (await page.textContent("#fb3")).includes("banc"), (await page.textContent("#fb3")).slice(0, 90));
  await shot(page, "act3_verrou_refuse");

  /* le banc : faire varier le vent, atteindre les 3 niveaux */
  /* un seul voyant allumé à la fois : invariant vérifié à chaque palier */
  const voyants = async () => page.evaluate(() =>
    ["Vert","Jaune","Orange","Rouge"].map(c =>
      document.getElementById("simDel"+c).className.includes("on") ? 1 : 0));

  for (const v of [10, 30, 70, 130, 40]) { await page.fill("#simVentNum", String(v)); await page.waitForTimeout(250); }
  ok("banc : VEILLE à 40 km/h — vert seul", (await page.getAttribute("#simLcd", "class")).includes("lcd-vert") &&
     JSON.stringify(await voyants()) === "[1,0,0,0]", await page.textContent("#simL1"));
  await shot(page, "banc_veille_40", "#bancCard");

  await page.fill("#simVentNum", "90"); await page.waitForTimeout(300);
  ok("banc : TEMPÊTE TROPICALE à 90 km/h — jaune seul, buzzer muet",
     (await page.getAttribute("#simLcd", "class")).includes("lcd-jaune") &&
     JSON.stringify(await voyants()) === "[0,1,0,0]" &&
     !(await page.getAttribute("#simBuz", "class")).includes("on"), await page.textContent("#simL1"));
  await shot(page, "banc_tempete_90", "#bancCard");

  await page.fill("#simVentNum", "150"); await page.waitForTimeout(300);
  ok("banc : OURAGAN à 150 km/h — orange seul, buzzer muet",
     (await page.getAttribute("#simLcd", "class")).includes("lcd-orange") &&
     JSON.stringify(await voyants()) === "[0,0,1,0]" &&
     !(await page.getAttribute("#simBuz", "class")).includes("on"), await page.textContent("#simL1"));
  await shot(page, "banc_ouragan_150", "#bancCard");

  await page.fill("#simVentNum", "200"); await page.waitForTimeout(300);
  ok("banc : OURAGAN MAJEUR à 200 km/h — rouge seul + buzzer qui sonne",
     (await page.getAttribute("#simLcd", "class")).includes("lcd-rouge") &&
     JSON.stringify(await voyants()) === "[0,0,0,1]" &&
     (await page.getAttribute("#simBuz", "class")).includes("on"), await page.textContent("#simL1"));
  await shot(page, "banc_majeur_200", "#bancCard");

  /* règle n°119 : le niveau est TOUJOURS écrit en toutes lettres, jamais seulement une couleur */
  const libelles = {};
  for (const [v, attendu] of [[40,"VEILLE"],[90,"TEMPETE"],[150,"OURAGAN"],[200,"MAJEUR"]]) {
    await page.fill("#simVentNum", String(v)); await page.waitForTimeout(220);
    libelles[v] = (await page.textContent("#simL1")).includes(attendu);
  }
  ok("règle n°119 : le niveau est écrit en toutes lettres aux 4 paliers",
     Object.values(libelles).every(Boolean), JSON.stringify(libelles));

  /* les SIX frontières, testées une par une — le cœur de la compétence C8.3 */
  const frontieres = [[62,"lcd-vert"],[63,"lcd-jaune"],[117,"lcd-jaune"],
                      [118,"lcd-orange"],[177,"lcd-orange"],[178,"lcd-rouge"]];
  for (const [v, classe] of frontieres) {
    await page.fill("#simVentNum", String(v)); await page.waitForTimeout(260);
    ok("frontière " + v + " km/h → " + classe.replace("lcd-",""),
       (await page.getAttribute("#simLcd", "class")).includes(classe), await page.textContent("#simL1"));
  }
  await shot(page, "banc_six_frontieres", "#bancCard");

  /* verrou de rédaction : act3 refusée tant que le journal de paliers est vide */
  await page.click('[data-check="3"]');
  ok("verrou de rédaction : act. 3 refusée tant que le journal de paliers est vide",
     (await page.textContent("#fb3")).includes("journal de paliers"),
     (await page.textContent("#fb3")).slice(0, 90));

  /* act3 doit maintenant passer */
  await page.fill("#a3_journal", "Palier 1 : potentiomètre à mi-course, le moniteur affichait 125 km/h ; la valeur monte quand je tourne, donc la lecture fonctionne. Palier 2 : à 62 j'ai lu VEILLE, à 63 TEMPETE TROPICALE. Palier 3 : à 150, l'orange seul était allumé, les trois autres éteints, buzzer muet.");
  await page.waitForTimeout(200);
  await page.click('[data-check="3"]');
  ok("activité 3 validée après manipulations (verrous lecture + 3 niveaux)",
     (await page.textContent("#fb3")).includes("6 / 6") && !(await page.textContent("#fb3")).includes("banc d'essai"),
     await page.textContent("#fb3"));
  await shot(page, "act3_validee");

  /* refonte v2 : la séance 2 est bien passée sur Vittascience, avec repli hors-ligne */
  ok("séance 2 : l'emplacement de l'interface Vittascience existe",
     (await page.locator("#vitta-embed").count()) === 1);
  ok("séance 2 : repli hors-ligne présent (lien direct + planches + banc)",
     (await page.textContent("#vitta-embed")).includes("fr.vittascience.com/arduino") &&
     (await page.textContent("#vitta-embed")).includes("Plan B"));
  ok("séance 2 : une SEULE échelle, affirmée et sans reste (aucune trace de la maquette 0-100)",
     (await page.textContent("#act3")).includes("Une seule échelle, une seule station") &&
     (await page.textContent("#act3")).includes("250 km/h") &&
     !(await page.textContent("#act3")).includes("seuil_vigilance"));
  const texteAct3 = await page.textContent("#act3");
  ok("séance 2 : les trois seuils de Saffir-Simpson sont dans les paliers",
     ["63","118","178"].every(v => texteAct3.includes(v)));
  ok("séance 2 : ArduBlock est devenu un bonus facultatif hors parcours",
     (await page.textContent("#act3")).includes("Bonus (facultatif — hors parcours obligatoire)") &&
     (await page.textContent("#act3")).includes("ArduBlock"));
  for (const src of ["Images/bonus_ardublock_palier1.png", "Images/bonus_ardublock_palier2.png"])
    ok("capture réelle ArduBlock présente : " + src, (await page.locator(`img[src="${src}"]`).count()) === 1);

  /* ── règles n°94 / n°121 : les captures RÉELLES du programme Vittascience ── */
  const CAPS = ["C_1_demarrage","C_2_boucle_haut","C_3_boucle_bas",
                "C_4_mode_vert","C_5_mode_jaune","C_6_mode_orange","C_7_mode_rouge",
                "C_frontiere_062kmh_brut254","C_frontiere_063kmh_brut258",
                "C_frontiere_117kmh_brut479","C_frontiere_118kmh_brut483",
                "C_frontiere_177kmh_brut725","C_frontiere_178kmh_brut729"];
  for (const c of CAPS)
    ok("capture réelle Vittascience présente : " + c,
       await page.locator(`img[src="Images/vittascience/${c}.png"]`).count() === 1);
  ok("règle n°117 : chaque capture réelle porte un alt d'au moins 120 caractères",
     await page.evaluate(() => [...document.querySelectorAll('img[src^="Images/vittascience/"]')]
       .every(i => (i.getAttribute("alt") || "").length >= 120)));
  ok("réserve honnête : le simulateur dessine tous les voyants en vert, et c'est écrit",
     (await page.textContent("body")).includes("tous les voyants sont dessinés en vert") &&
     (await page.textContent("body")).includes("les voyants sont tous dessinés en vert"));
  ok("écart assumé : les 300 ms du programme réel sont expliqués, pas masqués",
     (await page.textContent("#act3")).includes("300 ms"));

  /* séance 3 : acquittement puis re-déclenchement */
  await page.click('.seance-tab[data-panel="s3"]');
  await page.fill("#simVentNum", "200"); await page.waitForTimeout(300);
  await page.click("#btnAcquit"); await page.waitForTimeout(300);
  ok("banc : acquittement — buzzer muet, écran TOUJOURS rouge, voyant rouge TOUJOURS allumé",
     !(await page.getAttribute("#simBuz", "class")).includes("on") &&
     (await page.getAttribute("#simLcd", "class")).includes("lcd-rouge") &&
     (await page.getAttribute("#simDelRouge", "class")).includes("on"));
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
  await page.fill("#a6_redac", "Essais nominaux : 40 (veille), 90 (tempête tropicale), 150 (ouragan), 200 (ouragan majeur). Frontières : 62 et 63, 117 et 118, 177 et 178, car les bugs vivent aux frontières. Performance : je chronomètre le temps entre le franchissement de 178 et l'affichage, exigence moins d'une seconde. Interaction : appui sur le bouton pendant l'alarme (le son se coupe), puis redescente et remontée (le buzzer repart). Règle de décision : recette prononcée si 13 essais sur 13 sont réussis, sinon ajournée avec réserves.");
  await page.click('[data-check="6"]');
  ok("activité 6 validée (protocole rédigé, 4 familles + règle)", (await page.textContent("#fb6")).includes("5 / 5") && !(await page.textContent("#fb6")).includes("familles"));
  await shot(page, "act6_protocole_redige");

  /* activité 7 : exécution — frontières exactes + chrono */
  for (const v of [62, 63, 117, 118, 177, 178]) { await page.fill("#simVentNum", String(v)); await page.waitForTimeout(320); }
  await shot(page, "banc_frontieres_executees", "#bancCard");
  await page.click("#btnChrono");
  await page.waitForTimeout(1800);
  const chrono = await page.textContent("#chronoNote");
  ok("banc : temps de réponse mesuré et conforme (< 1 s)", chrono.includes("CONFORME ✔"), chrono.slice(0, 90));
  await shot(page, "banc_chrono", "#bancCard");
  for (const [id, v] of [["a7_a5","veille"],["a7_a6","tempête tropicale"],["a7_a7","tempête tropicale"],
                         ["a7_a8","ouragan"],["a7_a9","ouragan"],["a7_a10","ouragan majeur"]])
    await page.selectOption("#" + id, v);
  for (let i = 1; i <= 13; i++) await page.selectOption("#a7_r" + i, "conforme");
  await page.fill("#a7_pv", "Procès-verbal de recette — le 19/08, nous avons exécuté les 13 essais du protocole sur le banc de simulation. 13 conformes sur 13, les six frontières vérifiées, temps de réponse 0,3 s (exigence < 1 s). Recette prononcée, sans réserve.");
  await page.click('[data-check="7"]');
  ok("activité 7 validée (6 frontières + chrono exécutés, 13 verdicts, PV)",
     (await page.textContent("#fb7")).includes("6 / 6") && !(await page.textContent("#fb7")).includes("banc"));
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
  ok("persistance : réponses restaurées (a2_s1 = 178)", (await page.inputValue("#a2_s1")) === "178");
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

  /* encadré jumelage : les ouragans cités, et le tout REPLIÉ (hors parcours obligatoire) */
  const jumelage = await page.evaluate(() => {
    const s = [...document.querySelectorAll("details > summary")]
      .find(x => x.textContent.includes("New York lit-elle aussi ce dossier"));
    if (!s) return null;
    const d = s.parentElement;
    const interne = d.querySelector("details");
    return { replie: !d.open, interneReplie: !!interne && !interne.open,
             texte: d.textContent, tableaux: d.querySelectorAll("table").length };
  });
  ok("encadré jumelage présent", !!jumelage);
  ok("encadré jumelage : replié par défaut (ne coupe pas la situation déclenchante)",
     jumelage && jumelage.replie && jumelage.interneReplie);
  for (const nom of ["1938", "Irene", "Sandy", "Henri", "Ida"])
    ok("encadré jumelage : ouragan cité — " + nom, jumelage && jumelage.texte.includes(nom));
  ok("encadré jumelage : comparaison Martinique / New York en tableau",
     jumelage && jumelage.tableaux === 2, String(jumelage && jumelage.tableaux));
  ok("encadré jumelage : déclaré hors parcours obligatoire",
     jumelage && jumelage.texte.includes("hors parcours obligatoire"));
  ok("encadré jumelage : la limite du prototype est nommée (il ne mesure que le vent)",
     jumelage && jumelage.texte.includes("montée des eaux"));

  /* ── lisibilité : mesure / vigilance / alerte en trois cartes, pas en tableau ── */
  ok("mesure/vigilance/alerte : trois cartes distinctes, numérotées 1-2-3",
     await page.evaluate(() => {
       const n = [...document.querySelectorAll(".trois-niveaux .niv")];
       return n.length === 3 &&
              n.map(x => x.querySelector(".niv-rang").textContent.trim()).join("") === "123";
     }));
  ok("mesure/vigilance/alerte : chaque carte porte une couleur de bord distincte",
     await page.evaluate(() => {
       const c = [...document.querySelectorAll(".trois-niveaux .niv")]
         .map(x => getComputedStyle(x).borderLeftColor);
       return new Set(c).size === 3;
     }));
  ok("mesure/vigilance/alerte : la place de la station est marquée sur le niveau 1",
     await page.evaluate(() => {
       const p = document.querySelector(".niv-mesure .niv-ici");
       return !!p && p.textContent.includes("s'arrête ICI");
     }));
  ok("règle n°135 : tout tableau de 3 colonnes ou plus a un séparateur ou une alternance",
     await page.evaluate(() => [...document.querySelectorAll("table")]
       .filter(t => t.rows.length > 2 && t.rows[0].cells.length >= 3)
       .every(t => {
         const c = t.rows[1].cells[1]; if (!c) return true;
         const st = getComputedStyle(c);
         const separ = parseFloat(st.borderLeftWidth) > 0 || parseFloat(st.borderRightWidth) > 0;
         const zebre = getComputedStyle(t.rows[1]).backgroundColor
                    !== getComputedStyle(t.rows[2]).backgroundColor;
         return separ || zebre;
       })));

  /* ── règle n°101 : chaque séance mène explicitement à la suivante ── */
  ok("règle n°101 : 3 boutons « séance suivante » dans la page tout-en-un",
     await page.locator("button.vers-seance").count() === 3);
  await page.click('.seance-tab[data-panel="s1"]');
  await page.locator('button.vers-seance[data-vers="s2"]').click();
  await page.waitForTimeout(250);
  ok("règle n°101 : le bouton bascule réellement sur la séance suivante",
     await page.locator("#s2.active").count() === 1);

  /* ── règle n°122 : trois parcours, pas trois paragraphes ── */
  ok("règle n°122 : le sélecteur de parcours est dans la barre d'outils (4 boutons)",
     await page.locator(".toolbar .parcours-btn").count() === 4);
  await page.click('.parcours-btn[data-choix="c"]');
  await page.waitForTimeout(200);
  ok("règle n°122 : choisir 🅲 masque les blocs propres au parcours 🅰",
     await page.evaluate(() => document.body.classList.contains("parcours-c") &&
       [...document.querySelectorAll('[data-parcours="a"]')]
         .every(e => getComputedStyle(e).display === "none")));
  ok("règle n°122 : le choix ne retire AUCUNE question",
     await page.evaluate(() => [...document.querySelectorAll("input[id],select[id],textarea[id]")]
       .filter(e => e.closest("[data-parcours]")).length === 0));
  await page.waitForTimeout(700);
  await page.reload(); await page.waitForTimeout(600);
  ok("règle n°122 : le parcours choisi est restauré après rechargement",
     await page.evaluate(() => document.body.classList.contains("parcours-c")));
  await page.click('.parcours-btn[data-choix="tous"]');
  await page.waitForTimeout(200);
  ok("règle n°122 : « Tout afficher » remet tout en place",
     await page.evaluate(() => !document.body.className.includes("parcours-")));

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

  /* ════════ LE DÉCOUPAGE EN QUATRE PAGES (règle d'or n°116) ════════
     Trois exigences, et pas une de moins :
       1. aucune question perdue — l'union des 4 pages = la page tout-en-un ;
       2. les réponses sont PARTAGÉES : répondre page 1 puis aller page 4
          ne doit rien effacer (le piège de collect() qui écrase) ;
       3. chaque page mène à la suivante, et toutes ramènent au tout-en-un. */
  const P4 = ["sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html",
              "sequence_3e_C9.2-C8.3_station_2_programmer.html",
              "sequence_3e_C9.2-C8.3_station_3_interaction.html",
              "sequence_3e_C9.2-C8.3_station_4_recette.html"];

  /* champs interactifs de la page tout-en-un, référence de comparaison */
  const champs = f => page.evaluate(() =>
    [...document.querySelectorAll("input[id], select[id], textarea[id]")]
      .map(e => e.id).filter(id => !id.startsWith("sim") && !id.startsWith("id_")).sort());
  await page.goto(url(SEQ)); await page.waitForTimeout(500);
  const refChamps = await champs();

  const union = new Set();
  for (const f of P4) {
    await page.goto(url(f)); await page.waitForTimeout(450);
    (await champs()).forEach(id => union.add(id));
  }
  const perdus = refChamps.filter(id => !union.has(id));
  for (let i = 0; i < P4.length; i++) {
    await page.goto(url(P4[i])); await page.waitForTimeout(300);
    ok(`page ${i + 1} : pas de bouton d'onglet orphelin hérité du tout-en-un`,
       await page.locator("button.vers-seance").count() === 0);
  }
  await page.goto(url(SEQ)); await page.waitForTimeout(300);
  ok("4 pages : AUCUNE question perdue par rapport au tout-en-un",
     perdus.length === 0, perdus.join(", ") || (refChamps.length + " champs couverts"));
  ok("4 pages : zéro erreur JS au chargement des quatre", erreursJS.length === 0, erreursJS.join(" | "));

  /* liens : chaque page renvoie au tout-en-un et porte les 4 onglets-liens */
  for (let i = 0; i < P4.length; i++) {
    await page.goto(url(P4[i])); await page.waitForTimeout(300);
    const liens = await page.evaluate(() => [...document.querySelectorAll("a[href]")].map(a => a.getAttribute("href")));
    ok(`page ${i + 1} : ramène au tout-en-un`,
       liens.includes("sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html"));
    ok(`page ${i + 1} : porte les 4 onglets-liens`,
       await page.locator("nav.seance-tabs a.seance-tab").count() === 4);
  }

  /* persistance croisée : on répond page 1, on va page 4, on revient */
  await page.goto(url(P4[0])); await page.waitForTimeout(450);
  await page.evaluate(() => localStorage.clear());
  await page.reload(); await page.waitForTimeout(450);
  await page.fill("#hyp1", "Hypothèse écrite sur la PAGE 1, elle doit survivre au passage par la page 4.");
  await page.selectOption("#a1_e1", { index: 2 });
  await page.waitForTimeout(900);   /* sauvegarde différée */

  await page.goto(url(P4[3])); await page.waitForTimeout(500);
  await page.fill("#a6_redac", "Protocole écrit sur la PAGE 4 : 4 nominaux, 6 frontières (62, 63, 117, 118, 177, 178), chrono, 2 essais d'interaction.");
  await page.waitForTimeout(900);
  ok("4 pages : le rappel d'hypothèse de la page 1 remonte jusqu'à la page 4",
     (await page.textContent("#rappelHyp")).includes("PAGE 1"), (await page.textContent("#rappelHyp")).slice(0, 60));

  await page.goto(url(P4[0])); await page.waitForTimeout(500);
  ok("4 pages : la réponse de la page 1 a SURVÉCU au passage par la page 4",
     (await page.inputValue("#hyp1")).includes("PAGE 1") && (await page.inputValue("#a1_e1")) !== "");

  await page.goto(url(SEQ)); await page.waitForTimeout(500);
  ok("4 pages : le tout-en-un relit les réponses des DEUX pages",
     (await page.inputValue("#hyp1")).includes("PAGE 1") &&
     (await page.inputValue("#a6_redac")).includes("PAGE 4"));
  ok("tout-en-un : le chemin vers les 4 pages est proposé",
     await page.locator("#vers-quatre-pages a").count() === 4);
  await shot(page, "quatre_pages_persistance_croisee");
  await page.evaluate(() => localStorage.clear());

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
