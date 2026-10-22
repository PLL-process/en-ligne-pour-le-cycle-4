#!/usr/bin/env node
/* Suite de tests du volet « Pour aller plus loin : le pont en H » (3e_C9.2) : explication, simulateur SVG, prédiction, mini-quiz.

   Usage : node tests_pont_en_h.mjs

   Ce qu'elle vérifie : le volet est là, replié, après la planche des trois cas, dans les deux pages qui la portent ; pour LES SEIZE combinaisons
   d'interrupteurs, l'état du simulateur (court-circuit, sens 1, sens 2, arrêt) est celui que donne un calcul de connexité fait ICI, à part ; tout ce
   qui s'allume ou bouge est aussi écrit ; clavier ; mouvement réduit ; 390 px (pas de débord, textes lisibles, cibles ≥ 44 px) ; impression ;
   prédiction enregistrée ; aucune requête réseau ; zéro erreur JavaScript ; le mini-quiz corrige et explique.
   Ce qu'elle NE vérifie PAS : que l'explication soit comprise d'un élève de 3e (cela se lit en classe) ; la lecture sous Safari ou sur tablette. */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";

let chromium;
try { ({ chromium } = await import("playwright")); }
catch {
  const racineGlobale = execSync("npm root -g").toString().trim();
  ({ chromium } = createRequire(import.meta.url)(path.join(racineGlobale, "playwright", "index.js")));
}

const LOT = path.dirname(fileURLToPath(import.meta.url));
const PAGES = ["sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html", "sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html"];
const url = (f) => pathToFileURL(path.join(LOT, f)).href;
const resultats = [];
function ok(nom, cond, detail = "") {
  resultats.push({ nom, ok: !!cond });
  console.log((cond ? "✅" : "❌") + " " + nom + (detail ? " — " + detail : ""));
  if (!cond) process.exitCode = 1;
}

/* Le calcul de référence, indépendant du simulateur : des nœuds (+, −, borne gauche, borne droite) et des interrupteurs fermés comme arêtes. */
function attendu(f) {
  const arêtes = [];
  if (f.A) arêtes.push(["P", "G"]); if (f.C) arêtes.push(["G", "N"]); if (f.B) arêtes.push(["P", "D"]); if (f.D) arêtes.push(["D", "N"]);
  const relie = (x, y) => {
    const vus = new Set([x]); let boucle = true;
    while (boucle) { boucle = false; for (const [a, b] of arêtes) { if (vus.has(a) !== vus.has(b)) { vus.add(a); vus.add(b); boucle = true; } } }
    return vus.has(y);
  };
  if (relie("P", "N")) return "cc";
  if (relie("P", "G") && relie("N", "D")) return "sens1";
  if (relie("P", "D") && relie("N", "G")) return "sens2";
  return "arret";
}
const MOTS = { cc: /Court-circuit/, sens1: /sens 1/, sens2: /sens 2/, arret: /arrêté/ };

const run = async () => {
  const navigateur = await chromium.launch();

  for (const nomPage of PAGES) {
    const court = nomPage.includes("station_1") ? "page 1" : "page tout-en-un";
    const ctx = await navigateur.newContext({ viewport: { width: 1280, height: 900 } });
    const pg = await ctx.newPage();
    const erreurs = [], reseau = [];
    pg.on("pageerror", (e) => erreurs.push(String(e)));
    pg.on("request", (r) => { if (!r.url().startsWith("file:") && !r.url().startsWith("data:")) reseau.push(r.url()); });
    await pg.goto(url(nomPage));
    await pg.waitForTimeout(400);

    ok(`${court} : le volet « Pour aller plus loin : le pont en H » existe, replié`,
      await pg.evaluate(() => { const d = document.getElementById("pont-en-h"); return !!d && d.tagName === "DETAILS" && !d.open && /Pour aller plus loin : le pont en H/.test(d.querySelector("summary").textContent); }));
    ok(`${court} : il suit la planche des trois cas (dans la page, après #desc-3cas)`,
      await pg.evaluate(() => { const a = document.getElementById("desc-3cas"), b = document.getElementById("pont-en-h"); return !!a && !!b && (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING) !== 0; }));
    ok(`${court} : il dit « Hors programme de cycle 4 » et explique le relais simple`,
      await pg.evaluate(() => { const t = document.getElementById("pont-en-h").textContent; return /Hors programme de cycle 4/.test(t) && /relais simple/i.test(t) && /4 interrupteurs/.test(t); }));
    await pg.evaluate(() => { document.getElementById("pont-en-h").open = true; });
    const avantGeste = await pg.evaluate(() => (window.__exp || {}).pontH);

    // les seize combinaisons, comparées au calcul indépendant
    let ecarts = [];
    let sansTexte = [];
    for (let m = 0; m < 16; m++) {
      const f = { A: !!(m & 1), B: !!(m & 2), C: !!(m & 4), D: !!(m & 8) };
      await pg.evaluate(() => document.getElementById("ph_zero").click());
      for (const k of ["A", "B", "C", "D"]) if (f[k]) await pg.evaluate((kk) => document.querySelector('.ph-sw[data-sw="' + kk + '"]').click(), k);
      const e = attendu(f);
      const r = await pg.evaluate(() => ({
        dit: document.getElementById("ph_dit").textContent,
        rotor: document.getElementById("ph_rotor").getAttribute("class") || "",
        fl1: document.getElementById("ph_fl1").getAttribute("class"), fl2: document.getElementById("ph_fl2").getAttribute("class"),
        on: document.querySelectorAll("#ph_svg .ph-w.on").length, cc: document.querySelectorAll("#ph_svg .ph-w.cc").length,
        etat: document.getElementById("ph_etat").textContent,
        pressed: [...document.querySelectorAll(".ph-sw[data-sw]")].map((b) => b.getAttribute("aria-pressed") === "true"),
      }));
      const nom = Object.keys(f).filter((k) => f[k]).join("") || "rien";
      const bon = MOTS[e].test(r.dit) && (e !== "sens1" || (/sens1/.test(r.rotor) && / on/.test(r.fl1) && r.on === 9 && r.cc === 0))
        && (e !== "sens2" || (/sens2/.test(r.rotor) && / on/.test(r.fl2) && r.on === 9 && r.cc === 0))
        && (e !== "cc" || (r.cc > 0 && r.on === 0 && r.rotor === "" && /COURT-CIRCUIT/.test(r.etat)))
        && (e !== "arret" || (r.on === 0 && r.cc === 0 && r.rotor === "" && /arrêté/.test(r.etat)));
      if (!bon) ecarts.push(nom + " (attendu " + e + ") → « " + r.dit.slice(0, 60) + " »");
      const dejaDit = Object.keys(f).filter((k) => f[k]).every((k) => r.dit.includes(k)) && r.dit.length > 30;
      if (!dejaDit) sansTexte.push(nom);
      if (JSON.stringify(r.pressed) !== JSON.stringify([f.A, f.B, f.C, f.D])) ecarts.push(nom + " : boutons enfoncés incohérents");
    }
    ok(`${court} : les 16 combinaisons donnent l'état attendu (court-circuit, sens 1, sens 2, arrêt), trajet allumé, flèches, rotor`, ecarts.length === 0, ecarts.slice(0, 3).join(" | "));
    ok(`${court} : chaque état est dit en texte, avec les interrupteurs fermés (n°119)`, sansTexte.length === 0, sansTexte.join(","));

    // traces enregistrées, jamais exigées (créées au premier geste seulement : règle n°226)
    await pg.evaluate(() => document.getElementById("ph_zero").click());
    for (const k of ["A", "D"]) await pg.click('.ph-sw[data-sw="' + k + '"]');
    await pg.evaluate(() => document.getElementById("ph_zero").click());
    for (const k of ["B", "C"]) await pg.click('.ph-sw[data-sw="' + k + '"]');
    await pg.evaluate(() => document.getElementById("ph_zero").click());
    for (const k of ["A", "C"]) await pg.click('.ph-sw[data-sw="' + k + '"]');
    ok(`${court} : à l'ouverture, aucune trace n'est enregistrée (window.__exp.pontH absent avant le premier geste)`, avantGeste === undefined);
    ok(`${court} : traces window.__exp.pontH (avant, arrière, court-circuit) enregistrées`, await pg.evaluate(() => { const t = window.__exp.pontH; return t.avant && t.arriere && t.cc; }));
    ok(`${court} : aucun verrou : le volet ne touche ni window.__valid ni les verrous des activités`,
      await pg.evaluate(() => !/__valid|verrou/.test(document.getElementById("pont-en-h").innerHTML)));

    // prédiction facultative, enregistrée, comparée au résultat
    await pg.evaluate(() => document.getElementById("ph_zero").click());
    await pg.selectOption("#ph_pred", "sens2");
    await pg.click('.ph-sw[data-sw="A"]'); await pg.click('.ph-sw[data-sw="D"]');
    const comp = await pg.textContent("#ph_comp");
    ok(`${court} : la prédiction (sens 2) est comparée au résultat (A et D → sens 1)`, /Tu avais prévu le sens 2/.test(comp) && /sens 1/.test(comp), comp.slice(0, 60));
    await pg.waitForTimeout(900);
    await pg.reload(); await pg.waitForTimeout(400);
    ok(`${court} : la prédiction est enregistrée et revient au rechargement`, (await pg.inputValue("#ph_pred")) === "sens2");
    await pg.evaluate(() => { document.getElementById("pont-en-h").open = true; });
    await pg.selectOption("#ph_pred", "");
    ok(`${court} : sans prédiction, aucune comparaison n'est affichée`, await pg.evaluate(() => { document.getElementById("pont-en-h").open = true; document.getElementById("ph_zero").click(); [...document.querySelectorAll('.ph-sw[data-sw="A"],.ph-sw[data-sw="D"]')].forEach((b) => b.click()); return document.getElementById("ph_comp").textContent === ""; }));

    ok(`${court} : zéro erreur JavaScript, aucune requête réseau`, erreurs.length === 0 && reseau.length === 0, erreurs.concat(reseau).slice(0, 2).join(" | "));
    await ctx.close();
  }

  // clavier, mouvement réduit, impression, 390 px : sur la page tout-en-un
  {
    const nomPage = PAGES[0];
    const ctx = await navigateur.newContext({ viewport: { width: 1280, height: 900 }, reducedMotion: "reduce" });
    const pg = await ctx.newPage();
    await pg.goto(url(nomPage)); await pg.waitForTimeout(300);
    await pg.evaluate(() => { document.getElementById("pont-en-h").open = true; });
    await pg.focus('.ph-sw[data-sw="A"]');
    await pg.keyboard.press("Space");
    const apresEspace = await pg.getAttribute('.ph-sw[data-sw="A"]', "aria-pressed");
    await pg.keyboard.press("Tab"); await pg.keyboard.press("Tab"); await pg.keyboard.press("Tab"); await pg.keyboard.press("Enter");
    const apresEntree = await pg.getAttribute('.ph-sw[data-sw="D"]', "aria-pressed");
    ok("clavier : Espace et Entrée ferment un interrupteur (boutons), sans souris", apresEspace === "true" && apresEntree === "true", apresEspace + "," + apresEntree);
    const mvt = await pg.evaluate(() => {
      const w = document.querySelector("#ph_svg .ph-w.on"), r = document.getElementById("ph_rotor");
      return { fil: getComputedStyle(w).animationName, rotor: getComputedStyle(r).animationName, fleche: getComputedStyle(document.getElementById("ph_fl1")).display, arc: getComputedStyle(document.getElementById("ph_rot1")).display };
    });
    ok("mouvement réduit : plus aucune animation ; le trajet reste tracé et les flèches fixes disent le sens", mvt.fil === "none" && mvt.rotor === "none" && mvt.fleche !== "none" && mvt.arc !== "none", JSON.stringify(mvt));
    await pg.emulateMedia({ media: "print" });
    const imp = await pg.evaluate(() => ({ fond: getComputedStyle(document.querySelector("#ph_svg .ph-fond")).fill, nom: getComputedStyle(document.querySelector("#ph_svg .ph-nom")).fill }));
    ok("impression : fond blanc, textes foncés", imp.fond === "rgb(255, 255, 255)" && /^rgb\((\d+), (\d+), (\d+)\)$/.test(imp.nom) && Number(/\((\d+)/.exec(imp.nom)[1]) < 80, JSON.stringify(imp));
    await ctx.close();
  }
  {
    const ctx = await navigateur.newContext({ viewport: { width: 390, height: 800 } });
    const pg = await ctx.newPage();
    const erreurs = [];
    pg.on("pageerror", (e) => erreurs.push(String(e)));
    await pg.goto(url(PAGES[0])); await pg.waitForTimeout(300);
    await pg.evaluate(() => { document.getElementById("pont-en-h").open = true; });
    await pg.click('.ph-sw[data-sw="A"]');
    const m = await pg.evaluate(() => {
      const svg = document.getElementById("ph_svg"), k = svg.getBoundingClientRect().width / 600;
      const tailles = [...svg.querySelectorAll("text")].map((t) => parseFloat(getComputedStyle(t).fontSize) * k);
      return { debord: document.documentElement.scrollWidth - window.innerWidth, minTexte: Math.min(...tailles), cibles: [...document.querySelectorAll(".ph-sw")].map((b) => b.getBoundingClientRect().height), svgL: svg.getBoundingClientRect().width };
    });
    ok("390 px : pas de défilement horizontal", m.debord <= 1, "débord " + m.debord);
    ok("390 px : textes du dessin d'au moins 10 px à l'écran", m.minTexte >= 10, m.minTexte.toFixed(1) + " px (dessin " + Math.round(m.svgL) + " px)");
    ok("390 px : boutons de commande d'au moins 44 px de haut", m.cibles.every((h) => h >= 44), m.cibles.map(Math.round).join(","));
    ok("390 px : zéro erreur JavaScript", erreurs.length === 0, erreurs.join(" | "));
    await ctx.close();
  }

  // mini-quiz
  {
    const ctx = await navigateur.newContext({ viewport: { width: 390, height: 800 } });
    const pg = await ctx.newPage();
    const erreurs = [];
    pg.on("pageerror", (e) => erreurs.push(String(e)));
    await pg.goto(url("miniquiz_pont_en_h.html")); await pg.waitForTimeout(200);
    const q = await pg.evaluate(() => ({ n: document.querySelectorAll("fieldset.q").length, opts: [...document.querySelectorAll("fieldset.q")].map((f) => f.querySelectorAll("input[type=radio]").length) }));
    ok("mini-quiz : 3 questions de 4 propositions", q.n === 3 && q.opts.every((x) => x === 4), JSON.stringify(q));
    await pg.click("#q0_0"); await pg.click("#q1_0"); await pg.click("#q2_0");
    await pg.click("#verifier");
    const faux = await pg.evaluate(() => ({ bilan: document.getElementById("bilan").textContent, corrs: [...document.querySelectorAll(".corr")].map((c) => c.textContent) }));
    ok("mini-quiz : trois mauvaises réponses → trois corrections qui expliquent pourquoi la réponse choisie ne va pas", /0 bonne/.test(faux.bilan) && faux.corrs.length === 3 && faux.corrs.every((c) => /Ta réponse/.test(c) && /À retenir/.test(c)), faux.bilan);
    await pg.click("#recommencer");
    await pg.click("#q0_1"); await pg.click("#q1_2"); await pg.click("#q2_1");
    await pg.click("#verifier");
    const bon = await pg.textContent("#bilan");
    ok("mini-quiz : les trois bonnes réponses sont reconnues (3 sur 3), et « Recommencer » remet à zéro", /3 bonne\(s\) réponse\(s\) sur 3/.test(bon) && (await pg.evaluate(() => { document.getElementById("recommencer").click(); return document.querySelectorAll("input:checked").length === 0 && document.getElementById("bilan").textContent === ""; })), bon);
    const deb = await pg.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    ok("mini-quiz : 390 px sans défilement horizontal, zéro erreur JavaScript", deb <= 1 && erreurs.length === 0, "débord " + deb + " " + erreurs.join("|"));
    await ctx.close();
  }
  {
    const html = fs.readFileSync(path.join(LOT, PAGES[0]), "utf8");
    ok("le volet renvoie au mini-quiz, qui existe et renvoie au volet",
      /href="miniquiz_pont_en_h\.html"/.test(html) && fs.existsSync(path.join(LOT, "miniquiz_pont_en_h.html")) && /alerte_cyclonique\.html#pont-en-h/.test(fs.readFileSync(path.join(LOT, "miniquiz_pont_en_h.html"), "utf8")));
    const qcm = fs.readFileSync(path.join(LOT, "qcm_3e_C9.2-C8.3_station_alerte_cyclonique.html"), "utf8");
    ok("le QCM principal reste à 30 questions : aucune question sur le pont en H", !/pont en H/i.test(qcm));
  }

  await navigateur.close();
  const reussis = resultats.filter((r) => r.ok).length;
  console.log(`\n══ ${reussis} / ${resultats.length} tests réussis ══`);
};
run().catch((e) => { console.error("ÉCHEC de la suite :", e); process.exit(2); });
