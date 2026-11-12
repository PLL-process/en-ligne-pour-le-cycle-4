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
import { eprouverEditeurs, eprouverPose, executerBloc } from "../../../../_ressources-communes/editeur-python/eprouver_exercices.mjs";
import { pathToFileURL } from 'node:url';

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
const url = f => pathToFileURL(path.join(LOT, f)).href;
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
  // n°298 (vague du thème 3, 26/10/2026) : la carte de référentiel a quitté la page élève ; le témoin du mode
  // essentiel est désormais le nombre de corrections visibles.
  const avant = await page.evaluate(() => [...document.querySelectorAll("details.correction")].filter(e => e.offsetParent !== null).length);
  await page.click("#btnEssentiel");
  await page.waitForTimeout(150);
  const apres = await page.evaluate(() => [...document.querySelectorAll("details.correction")].filter(e => e.offsetParent !== null).length);
  const etat = await page.locator("#btnEssentiel").getAttribute("aria-pressed");
  ok("n°29 : le mode essentiel masque vraiment les corrections, et la page n'a plus de carte de référentiel (n°298)",
     avant > 0 && apres === 0 && etat === "true" && (await page.locator(".referentiel-card").count()) === 0,
     avant + " → " + apres);
  const corrCachees = await page.evaluate(() =>
    [...document.querySelectorAll("details.correction")].filter(e => e.offsetParent === null).length);
  const corrTotal = await page.locator("details.correction").count();
  ok("n°29 : les corrections aussi sont masquées", corrTotal > 0 && corrCachees === corrTotal,
     corrCachees + "/" + corrTotal);
  await shot(page, "mode_essentiel");
  await page.click("#btnEssentiel");
  await page.waitForTimeout(120);
  ok("n°29 : un second clic rétablit l'affichage complet",
     (await page.evaluate(() => [...document.querySelectorAll("details.correction")].filter(e => e.offsetParent !== null).length)) > 0);
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
  // les zones de CODE de l'éditeur Python (04/11/2026) ne sont pas des zones de rédaction ; progBarr, devenu éditeur, en reste une
  const z = await page.locator("textarea:not(.editeur-py-code), textarea#progBarr").count();
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

/* — n°42 : le référentiel recopie le programme, au mot près — lu dans la synthèse professeur depuis la
   vague n°298 du thème 3 (26/10/2026) ; la page élève garde, d'elle, le dépliant « Où tu en es dans le cycle » — */
{
  const synth = fs.readFileSync(path.join(LOT, "Synthèses", "synthese_professeur_5e_C9.1-C9.3.html"), "utf8");
  const debut = synth.indexOf("referentiel-eleve");
  const txt = synth.slice(debut, synth.indexOf("</table>", debut)).replace(/<[^>]+>/g, " ").replace(/&nbsp;/g, " ")
    .replace(/&#39;|&apos;/g, "'").replace(/\s+/g, " ");
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

/* — lot du 04/10/2026 : l'éditeur s'ouvre en mode code, la version 🅰 (carte réelle, LED) n'existe plus —
   Le contenu de Vittascience (le collage, l'exécution) a été mesuré à la main et n'est pas rejoué ici :
   service externe. On éprouve ce que NOTRE page promet. */
{
  const hrefs = await page.$$eval("a.vs-lien", a => a.map(x => x.getAttribute("href")));
  ok("gestes · les 3 liens-boutons ouvrent l'éditeur en ?mode=code (plus de mode mixte)",
     hrefs.length === 3 && hrefs.every(h => /^https:\/\/fr\.vittascience\.com\/python\/\?mode=code(&|&amp;|$)/.test(h)),
     hrefs.join(" | "));

  const choix = await page.$$eval(".parcours-btn", b => b.map(x => x.dataset.choix).join(","));
  const texte = await page.evaluate(() => document.body.textContent);
  ok("gestes · plus de version 🅰 : ni bouton, ni phrase (carte réelle, LED), ni « blocs à gauche »",
     choix === "b,c,tous" && !/🅰/.test(texte) && !/\bLED\b/.test(texte) && !/carte réelle/i.test(texte) && !/blocs à gauche/i.test(texte),
     "boutons : " + choix);

  /* un élève qui avait choisi 🅰 avant le retrait : sa sauvegarde dit « a » — dans un contexte à part */
  const ctxA = await nav.newContext({ viewport: { width: 390, height: 844 } });
  await ctxA.addInitScript(() => localStorage.setItem("seq_5e_C9.1-C9.3_boite_etiquetee", JSON.stringify({ exp: { parcours: "a" } })));
  const pA = await ctxA.newPage();
  await pA.goto(url(SEQ), { waitUntil: "load" });
  await pA.waitForTimeout(300);
  const classeA = await pA.evaluate(() => document.body.className);
  const noteA = await pA.locator("#parcoursNote").textContent();
  const visibles = await pA.evaluate(() => [...document.querySelectorAll("[data-parcours]")].filter(e => e.offsetParent !== null).length);
  ok("gestes · un ancien choix « a » mémorisé retombe sur « tous » (rien n'est masqué à tort)",
     !/parcours-/.test(classeA) && /tous/.test(noteA) && visibles === 2, noteA.trim() + " · " + visibles + " parcours visibles");
  await ctxA.close();

  await page.evaluate(() => document.querySelectorAll(".gestes-outil img").forEach(i => { i.loading = "eager"; }));
  await page.waitForTimeout(800);
  const imgs = await page.$$eval(".gestes-outil img", l => l.map(i => ({ charge: i.complete && i.naturalWidth > 0, alt: (i.getAttribute("alt") || "").trim().length })));
  ok("gestes · les " + imgs.length + " captures de Windows de l'encart se chargent, toutes avec un texte alternatif (depuis le 05/11/2026, l'éditeur n'y est plus en image : il y est en vrai)",
     imgs.length === 3 && imgs.every(i => i.charge && i.alt > 20),
     imgs.filter(i => !i.charge).length + " cassée(s), " + imgs.filter(i => i.alt <= 20).length + " sans texte alternatif");
  const essai = await page.evaluate(async () => {
    const bloc = document.querySelector(".gestes-outil .editeur-py-essai");
    const r = bloc && window.EditeurPython ? await window.EditeurPython.executer(document.getElementById("py_echauffement").value) : null;
    return { actif: !!bloc && bloc.classList.contains("editeur-py--actif"), gestes: document.querySelectorAll(".gestes-outil ol.gestes-pratique > li[data-geste]").length,
             suivi: !!document.querySelector(".gestes-outil ol.gestes-pratique--actif"), sortie: r && r.sortie, erreur: r && r.erreur };
  });
  ok("gestes · l'échauffement a son éditeur d'essai, monté, et ses quatre gestes suivis ; le programme d'essai s'exécute : « Bonjour Camille ! » puis « 2 + 3 = 5 » (05/11/2026)",
     essai.actif && essai.gestes === 4 && essai.suivi && essai.sortie === "Bonjour Camille !\n2 + 3 = 5\n" && !essai.erreur, JSON.stringify(essai));
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
  await page.selectOption("#a1q2", "il a été remplacé par 21 : il n'existe plus");
  await page.selectOption("#a1q3", "« RANGE cette valeur dans la boîte »");
  await page.click('.btn.check[data-check="1"]');
  await page.waitForTimeout(150);
  ok("act. 1 : validée 3/3 avec le vérificateur exact",
     /activité validée/.test(await page.locator("#fb1").textContent()));
}

/* — règles n°144 et n°198 dans les activités : ni le rang ni la longueur ne désignent la bonne réponse —
     (lu dans les vérificateurs sv("id","réponse") de la page : c'est leur réponse qui est mesurée) */
{
  const src = fs.readFileSync(path.join(LOT, SEQ), "utf8");
  const paires = [...src.matchAll(/sv\("([^"]+)","([^"]+)"\)/g)].map(m => [m[1], m[2]]);
  const forme = await page.evaluate((P) => P.map(([id, rep]) => {
    const o = [...document.querySelectorAll("#" + id + " option")].map(x => x.textContent).filter(x => x && !x.startsWith("—"));
    const autres = o.filter(x => x !== rep).map(x => x.length);
    return { id, rang: o.indexOf(rep), detachee: rep.length > Math.max(...autres) + 8 || rep.length < Math.min(...autres) - 8 };
  }), paires);
  const premieres = forme.filter(x => x.rang === 0).length;
  ok("activités : chaque réponse attendue existe dans son menu (" + forme.length + " menus)",
     forme.length >= 15 && forme.every(x => x.rang >= 0), forme.filter(x => x.rang < 0).map(x => x.id).join(", "));
  ok("activités : la bonne réponse n'est en tête que dans moins d'un tiers des menus (" + premieres + "/" + forme.length + ")",
     premieres * 3 < forme.length);
  ok("activités : aucune bonne réponse détachée par sa longueur (> 8 caractères)", forme.every(x => !x.detachee),
     forme.filter(x => x.detachee).map(x => x.id).join(", "));
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
  /* « 🗺 Où j'en suis » (04/11/2026) : ouvert à la séance 1, replié dès la séance 2 derrière une ligne qui dit le même compte */
  {
    const avant = await page.evaluate(() => document.querySelector(".seance-panel.active").id);
    await page.click("#tab-s1"); await page.waitForTimeout(80);
    const s1 = await page.evaluate(() => document.getElementById("tachesVolet").open);
    await page.click("#tab-s2"); await page.waitForTimeout(80);
    const s2 = await page.evaluate(() => { const d = document.getElementById("tachesVolet"), s = d.querySelector("summary");
      return { open: d.open, ligne: s.checkVisibility() && s.getBoundingClientRect().height >= 44, txt: document.getElementById("tachesResume").textContent }; });
    const prog = (await page.locator("#progTxt").textContent()).trim();
    ok("« Où j'en suis » : ouvert à la séance 1, replié à la séance 2 derrière une ligne de 44 px qui dit le même compte que la progression",
       s1 && !s2.open && s2.ligne && s2.txt.split(" ")[0] === prog.split(" ")[0] && s2.txt.split(" ")[2] === prog.split(" ")[2], s2.txt + " · " + prog);
    await page.click("#tab-" + avant); await page.waitForTimeout(80);
  }
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

/* — 5e_C9.3 : l'activité 5 exige le programme de la barrière écrit par l'élève — */
{
  await page.click("#tab-s3");
  await page.waitForTimeout(150);
  for (const t of ["1", "2", "3"]) { await page.click(`.bench-barr[data-t="${t}"]`); await page.waitForTimeout(90); }
  for (const [id, v] of [["a5q1", "places = places + descendus"], ["a5q2", "la ligne 1 : places = 32"],
                         ["a5q3", "parce que le nombre de sièges n'est écrit qu'une fois"],
                         ["a5q4", "fausse : la barrière se ferme"], ["a5q5", "c'est le cas frontière, pile à la limite"]])
    await page.selectOption("#" + id, v);
  await page.click('.btn.check[data-check="5"]');
  await page.waitForTimeout(150);
  await page.waitForFunction(() => !/^⏳/.test(document.querySelector("#fb5").textContent), null, { timeout: 15000 });
  ok("act. 5 : sans programme de barrière, 5/6 et pas de validation",
     /5\/6/.test(await page.locator("#fb5").textContent()) && !/activité validée/.test(await page.locator("#fb5").textContent()));
  await page.fill("#progBarr", "places = 0\nif places > 0 :\n    print(\"OUVERTE\")\nelse:\n    print(\"FERMÉE\")");
  await page.click('.btn.check[data-check="5"]');
  await page.waitForTimeout(150);
  await page.waitForFunction(() => !/^⏳/.test(document.querySelector("#fb5").textContent), null, { timeout: 15000 });
  ok("act. 5 : validée 6/6 avec le programme if / else de la barrière",
     /activité validée/.test(await page.locator("#fb5").textContent()) && /6\/6/.test(await page.locator("#fb5").textContent()));
  await page.fill("#progBarr", "places = 0\nif places >= 0:\n    print(\"OUVERTE\")\nelse:\n    print(\"FERMÉE\")");
  await page.click('.btn.check[data-check="5"]');
  await page.waitForTimeout(150);
  await page.waitForFunction(() => !/^⏳/.test(document.querySelector("#fb5").textContent), null, { timeout: 15000 });
  ok("act. 5 : « places >= 0 » (frontière fausse) n'est pas accepté",
     !/6\/6/.test(await page.locator("#fb5").textContent()));
  await page.fill("#progBarr", "places = 0\nif places > 0:\n    print(\"FERMÉE\")\nelse:\n    print(\"OUVERTE\")");
  await page.click('.btn.check[data-check="5"]');
  await page.waitForTimeout(150);
  await page.waitForFunction(() => !/^⏳/.test(document.querySelector("#fb5").textContent), null, { timeout: 15000 });
  ok("act. 5 : jugé en l'exécutant — les bons mots, mais OUVERTE et FERMÉE inversés : refusé",
     !/6\/6/.test(await page.locator("#fb5").textContent()));
  await shot(page, "act5_programme_barriere", "#fb5");
}

/* — l'éditeur Python intégré (04/11/2026) : il remplace l'onglet Vittascience (activités 3 et 5, Bonus) —
     Un test par exercice : le code de départ s'exécute (bouton ▶, comme un élève) et donne la sortie attendue ;
     le programme de la correction donne celle de la correction. */
{
  const ctxE = await nav.newContext({ viewport: { width: 1280, height: 900 } });
  const reseau = [];
  ctxE.on("request", r => { if (/^https?:/.test(r.url())) reseau.push(r.url()); });
  const { page: pe, erreurs: ee } = await ouvrir(ctxE, SEQ);
  await eprouverPose(pe, ["vs1", "vs2", "vs3"], ok);
  await pe.click("#tab-s2"); await pe.waitForTimeout(200);
  for (const [id, v] of [["a3p1", "24"], ["a3p2", "204"], ["a3r1", "24"], ["a3r2", "204"], ["a3r3", "du TEXTE que le + COLLE bout à bout"],
                         ["a3r4", "des guillemets autour des nombres"]]) await pe.selectOption("#" + id, v);
  await pe.click('.btn.check[data-check="3"]'); await pe.waitForTimeout(150);
  const fbAvant = await pe.locator("#fb3").textContent();
  await executerBloc(pe, "vs1");
  await pe.click('.btn.check[data-check="3"]'); await pe.waitForTimeout(150);
  const fbApres = await pe.locator("#fb3").textContent();
  ok("act. 3 : le verrou demande l'éditeur Python, et une exécution menée au bout l'ouvre (6/6)",
     /🔒[\s\S]*éditeur Python/.test(fbAvant) && /activité validée/.test(fbApres) && /6\/6/.test(fbApres), fbAvant.slice(0, 50) + " → " + fbApres.slice(0, 40));
  await eprouverEditeurs(pe, [
    { bloc: "vs1", nom: "activité 3", depart: { sortie: "24\n204\n" } },
    { bloc: "vs2", nom: "activité 5, la barrière", onglet: "#tab-s3", depart: { sortie: "" },
      corrige: { quoi: "FERMÉE pour places = 0", sortie: "FERMÉE\n",
        code: 'places = 0\nif places > 0:\n    print("OUVERTE")\nelse:\n    print("FERMÉE")\n' } },
    { bloc: "vs3", nom: "Bonus", depart: { sortie: "" },
      corrige: { quoi: "l'âge du Cyclone (99 ans en 2026)", sortie: "Le Cyclone a 99 ans\n", code: 'annee = 2026\nprint("Le Cyclone a", annee - 1927, "ans")\n' } },
  ], ok);
  ok("éditeur Python · aucune requête réseau, zéro erreur JavaScript", reseau.length === 0 && ee.length === 0, reseau.concat(ee).slice(0, 3).join(" | "));
  await pe.close(); await ctxE.close();
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
