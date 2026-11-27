#!/usr/bin/env node
/* Suite de tests Playwright — lot 3e_C7.1 « Capteur de confort — New York » (arc « jardin connecté » de 4e).

   Écrite le 26 août 2026 à l'occasion de l'harmonisation du lot. Elle simule la
   séquence comme un élève et ne déclare que ce qu'elle exécute.

   Règle d'or n°136 : chaque dispositif est vérifié par la MESURE de son effet —
   un nombre —, jamais par la présence de ses commandes. Un contrôle dont le
   résultat attendu est « oui » plutôt qu'un nombre ne contrôle rien.

   24/10/2026 : une séance 3 de 55 min est ajoutée (exercices des ateliers FAST et croquis,
   au service de 3e_C7.2) ; la clôture passe après elle. Le banc compte désormais 3 séances,
   8 activités, mesure chaque séance (≤ 55 min), la navigation d'une séance à la suivante, les
   verrous des activités 6 et 7 sur les exercices insérés, et la reprise d'une sauvegarde
   faite avant l'ajout.

   15/11/2026 (révision, décision de Pascal) : une séance 4. La séance 3 garde l'activité 6 ;
   l'activité 7, la synthèse et la clôture passent en séance 4, et les deux cartes de la suite
   du projet (TP « Le boîtier étanche », atelier de planification) remontent avant le Bonus :
   rien à faire après le bilan (n°301). Le banc compte 4 séances.

   Usage : node tests_3e_C7.mjs [dossier_du_lot] [dossier_captures]                 */
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";
import { eprouverEditeurs, eprouverPose, executerBloc, eprouverBanc, eprouverRejouer } from "../../../../_ressources-communes/editeur-python/eprouver_exercices.mjs";
import { pathToFileURL } from 'node:url';
// Les questions posées par une liste déroulante sont devenues des boutons radio (n°300, 14/11/2026) : ce shim garde les
// appels du banc (selectOption, fill, inputValue) — une chaîne vise la valeur ou le libellé, {index} la place.
function _groupesRadio(page){
  const origIV = page.inputValue.bind(page);
  page.inputValue = async (sel, ...reste) => {
    const groupe = typeof sel === 'string' && await page.evaluate(s => { const e = document.querySelector(s); return !!(e && e.tagName === 'FIELDSET' && e.classList.contains('qcm-groupe')); }, sel);
    return groupe ? page.evaluate(s => document.querySelector(s).value, sel) : origIV(sel, ...reste);
  };
  for (const nom of ['selectOption', 'fill']) {
    const orig = page[nom].bind(page);
    page[nom] = async (sel, val, ...reste) => {
      const groupe = typeof sel === 'string' && await page.evaluate(s => { const e = document.querySelector(s); return !!(e && e.tagName === 'FIELDSET' && e.classList.contains('qcm-groupe')); }, sel);
      if (!groupe) return orig(sel, val, ...reste);
      // comme Playwright sur un <select> : une chaîne vise la valeur OU le libellé ; {index}, {value}, {label} sont acceptés
      const v = (val && typeof val === 'object') ? val : { label: String(val), value: String(val) };
      const ok = await page.evaluate(([s, v]) => {
        const e = document.querySelector(s); const inputs = [...e.querySelectorAll('input[type=radio]')];
        const lib = i => (e.querySelector('label[for="' + i.id + '"]') || {}).textContent?.trim();
        const c = v.index !== undefined ? inputs[v.index]
          : inputs.find(i => i.value === v.value) || inputs.find(i => lib(i) === v.label);
        if (!c) return false;
        c.checked = true; c.dispatchEvent(new Event('change', {bubbles: true})); return true;
      }, [sel, v]);
      if (!ok) throw new Error('aucune proposition \u00ab ' + JSON.stringify(v) + ' \u00bb dans ' + sel);
    };
  }
  return page;
}

let chromium;
try { ({ chromium } = await import("playwright")); }
catch {
  const racineGlobale = execSync("npm root -g").toString().trim();
  ({ chromium } = createRequire(import.meta.url)(path.join(racineGlobale, "playwright", "index.js")));
}

/* ── ce qui change d'un lot à l'autre ── */
const CFG = {
  seq: "sequence_3e_C7_capteur-confort-ny.html",
  qcm: "qcm_3e_C7_capteur-confort-ny.html",
  cle: "seq_3e_C7_capteur_confort",
  captures: "/tmp/captures_3eC7",
  etayages: 6,            // les versions étayées de la page elle-même, hors exercices d'atelier insérés
  seances: 4,             // séance 3 ajoutée le 24/10/2026 (exercices des ateliers FAST et croquis), séance 4 le 15/11/2026
  activites: 8,           // vérificateurs 0 à 7
  formulations: [
    "Élaborer un processus de conception et de réalisation dans une durée, avec des tâches identifiées.",
    "Proposer et fabriquer un ensemble de solutions pour produire un nouvel OST (croquis, schéma, graphique, algorithme, modélisation).",
    "Mettre en œuvre une simulation pour valider la tenue mécanique d'un matériau."
  ],
  /* Réponses écrites des exercices d'atelier insérés en séance 3 : le champ `exemple` de leur
     définition d'atelier (donnees_croquis.py), recopié ici. Les choix, eux, sont LUS dans la
     définition JSON posée dans la page. */
  textes: {
    "cq_3e_e4__choix": "Je garde la solution 1, le collier serré par deux boulons : la sirène reste près du poteau, donc le vent du cyclone ne peut pas l'arracher. Et on la démonte avec une seule clé pour l'entretien.",
    "cq_3e_e6__pourquoi": "Le croquis est fait à main levée : son trait n'est pas exact et il ne donne pas toutes les dimensions. L'imprimante a besoin d'un fichier fait dans un logiciel de modélisation, avec la forme exacte en volume."
  },
  essaisBanc: null,
  reponsesAct0: null
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
const url = f => pathToFileURL(path.join(LOT, f)).href;

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
  const page = _groupesRadio(await ctx.newPage());
  const erreurs = [];
  page.on("pageerror", e => erreurs.push(String(e)));
  page.on("console", m => { if (m.type() === "error" && !/net::|ERR_/.test(m.text())) erreurs.push(m.text()); });
  await page.goto(url(fichier));
  await page.waitForTimeout(400);
  return { page, erreurs };
}

/* Séances à onglets (vague de la règle d'or n°311, 04/11/2026) : une activité n'est plus à l'écran au chargement. Avant d'agir
   sur un champ, on ouvre, comme l'élève, l'onglet de la séance qui le porte ; un champ de l'ouverture se trouve à la séance 1
   (dès la séance 2, il est replié dans le volet « Rappel »). */
async function ouvrirSeanceDe(pg, sel) {
  const id = await pg.evaluate(s => {
    const e = document.querySelector(s); if (!e) return null;
    const pan = e.closest('.seance-panel');
    if (pan) return pan.classList.contains('active') ? null : pan.id;
    const v = e.closest('#ouverture');
    return v && !v.open ? document.querySelector('.seance-tab').dataset.panel : null;
  }, sel);
  if (id) { await pg.click('.seance-tab[data-panel="' + id + '"]'); await pg.waitForTimeout(100); }
}

/* ═══════════════════ 1. La séquence ═══════════════════ */
const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 } });
const { page, erreurs } = await ouvrir(ctx, CFG.seq);
await shot(page, "sequence_chargee");
ok("séquence : chargement file:// sans erreur JS", erreurs.length === 0, erreurs.slice(0, 3).join(" | "));

/* — n°23 : le cadre horaire est reconnaissable, et il tient — */
{
  /* depuis le passage à onglets (04/11/2026), les durées vivent dans trois panneaux dont deux sont repliés : on lit le
     texte de toute la page (scripts et styles exclus), pas seulement ce qui est à l'écran */
  const txt = await page.evaluate(() => { const c = document.body.cloneNode(true); c.querySelectorAll("script, style").forEach(x => x.remove()); return c.textContent; });
  const cadre = txt.match(/(\d+)\s*séances?\s+de\s+(\d+)\s*min/i);
  const parts = [...txt.matchAll(/~\s*(\d+)\s*min/g)].map(m => parseInt(m[1], 10));
  const total = parts.reduce((a, b) => a + b, 0);
  ok("n°23 : la page annonce un cadre « N séances de M min »", !!cadre, cadre ? cadre[0] : "absent");
  /* 5 durées pour 6 vérificateurs : l'activité 1 en porte deux (le diagramme,
     puis le planning) — elles partagent le même créneau annoncé. */
  ok("n°23 : les durées d'activité sont à la convention ~n min", parts.length >= 5, parts.join(" + "));
  const dispo = cadre ? parseInt(cadre[1], 10) * parseInt(cadre[2], 10) : 0;
  ok("n°23 : le total tient dans le cadre annoncé, marge comprise",
     total + 10 <= dispo, total + " min pour " + dispo + " disponibles");
  /* L'en-tête pédagogique a été dissous le 26/10/2026 (n°314, décision 1a de Pascal) : le détail de la durée,
     total annoncé compris, vit désormais dans la bulle de l'étiquette « ⏱ 3 séances de 55 min ». */
  const bulleDuree = await page.evaluate(() => [...document.querySelectorAll(".badges .badge")]
    .map(b => b.title).find(t => /min d'activités annoncées/.test(t)) || "");
  const annonce = (txt + " " + bulleDuree).match(/(\d+)\s*min d'activités annoncées/);
  ok("n°23 : l'étiquette de durée annonce, dans sa bulle, le total réellement écrit dans les activités",
     !!annonce && parseInt(annonce[1], 10) === total, (annonce ? annonce[1] : "—") + " annoncées · " + total + " mesurées");
  ok("n°23 : le cadre annonce " + CFG.seances + " séances de 55 min",
     !!cadre && parseInt(cadre[1], 10) === CFG.seances && parseInt(cadre[2], 10) === 55, cadre ? cadre[0] : "absent");

  /* Séance par séance : la page défile d'un bloc ; chaque séance s'ouvre par un en-tête
     .seance-entete#seance-N. On additionne les « ~N min » de ce qui suit chaque en-tête jusqu'au
     suivant (hors Bonus facultatif) : chaque séance doit tenir dans ses 55 min. */
  const parSeance = await page.evaluate(() => {
    const entetes = [...document.querySelectorAll(".seance-entete[id^='seance-']")];
    const res = [];
    entetes.forEach((h, i) => {
      const suivant = entetes[i + 1] || null;
      const r = document.createRange();
      r.setStartAfter(h);
      if (suivant) r.setEndBefore(suivant); else r.setEndAfter(document.querySelector("footer"));
      const frag = r.cloneContents();
      let min = 0;
      frag.querySelectorAll("h2").forEach(t => {
        const s = t.textContent;
        if (/bonus|facultatif/i.test(s)) return;
        const m = s.match(/~\s*(\d+)\s*min/);
        if (m) min += parseInt(m[1], 10);
      });
      res.push({ id: h.id, min });
    });
    return res;
  });
  ok("n°23 : " + CFG.seances + " en-têtes de séance, dans l'ordre (seance-1 → seance-" + CFG.seances + ")",
     parSeance.length === CFG.seances && parSeance.every((s, i) => s.id === "seance-" + (i + 1)),
     parSeance.map(s => s.id).join(", "));
  ok("n°23 : chaque séance tient dans ses 55 min d'activités annoncées",
     parSeance.length > 0 && parSeance.every(s => s.min > 0 && s.min <= 55),
     parSeance.map(s => s.id + " = " + s.min + " min").join(" · "));
}

/* — les séances 3 et 4 : leur place dans la page, la clôture, et la navigation entre séances — */
{
  const ordre = await page.evaluate(() => {
    const pos = el => el ? [...document.querySelectorAll("*")].indexOf(el) : -1;
    const h2 = re => [...document.querySelectorAll("h2")].find(h => re.test(h.textContent));
    return {
      s3: pos(document.getElementById("seance-3")),
      s4: pos(document.getElementById("seance-4")),
      tp: pos(h2(/TP « Le boîtier étanche »/)),
      planif: pos(h2(/diagramme de planification/)),
      a6: pos(document.getElementById("activite-6")),
      a7: pos(document.getElementById("activite-7")),
      refaire: pos(h2(/REFAIRE/)),
      bonus: pos(h2(/Bonus/)),
      bilan: pos(h2(/Bilan/)),
      qcm: pos(h2(/Prêt·e à t.entraîner/))
    };
  });
  ok("séances 3 et 4 : la séance 3 suit le REFAIRE et porte l'activité 6 ; la séance 4, l'activité 7",
     ordre.refaire < ordre.s3 && ordre.s3 < ordre.a6 && ordre.a6 < ordre.s4 && ordre.s4 < ordre.a7, JSON.stringify(ordre));
  ok("séance 4 : la clôture vient après l'activité 7, dans l'ordre Bonus → Bilan → QCM",
     ordre.a7 < ordre.bonus && ordre.bonus < ordre.bilan && ordre.bilan < ordre.qcm);
  ok("n°301 : les deux cartes de la suite du projet (TP, planification) viennent avant le Bonus, rien à faire après le bilan",
     ordre.a7 < ordre.tp && ordre.tp < ordre.planif && ordre.planif < ordre.bonus, JSON.stringify(ordre));
  const liens = await page.$$eval("nav.fin-seance a.vers-seance", a => a.map(x => x.getAttribute("href")));
  ok("navigation : chaque séance (sauf la dernière) mène explicitement à la suivante",
     liens.join(",") === "#seance-2,#seance-3,#seance-4", liens.join(", "));
  for (const cible of ["#seance-2", "#seance-3", "#seance-4"]) {
    await page.click('nav.fin-seance a[href="' + cible + '"]');
    await page.waitForTimeout(250);
    const top = await page.evaluate(s => document.querySelector(s).getBoundingClientRect().top, cible);
    ok("navigation : le bouton « " + cible.replace("#seance-", "Séance ") + " » amène à son en-tête, sous la barre du haut",
       top >= 0 && top < 140, "en-tête à " + Math.round(top) + " px du haut de l'écran");
  }
  await page.evaluate(() => window.scrollTo(0, 0));
  const blocs = await page.$$eval("section.atelier-incruste", s => s.map(x => x.id));
  ok("séances 3 et 4 : les deux blocs d'exercices d'atelier sont posés (FAST, croquis)",
     blocs.join(",") === "incruste-fa-3e-capteur-confort,incruste-cq-3e-capteur-confort", blocs.join(", "));
  const intro = await page.$$eval("section.atelier-incruste > p:first-of-type", p => p.map(x => x.textContent));
  ok("séances 3 et 4 : chaque bloc dit qu'il porte sur la station d'alerte cyclonique et le relie au capteur",
     intro.length === 2 && intro.every(t => /station d'alerte cyclonique/.test(t) && /capteur/.test(t)));
}

/* — n°26 : le billet d'entrée, hors progression — */
{
  await ouvrirSeanceDe(page, "#be_1");   // le billet est dans l'ouverture : séance 1
  // la première proposition (index 0 en boutons radio ; index 1 dans l'ancienne liste, après « — choisir — »)
  await page.selectOption("#be_1", { index: 0 });
  await page.selectOption("#be_2", { index: 0 });
  await page.selectOption("#be_3", { index: 0 });
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
  ok("n°30 : le tableau de bord liste les " + CFG.activites + " activités", n === CFG.activites, n + " tâches");
  const s3 = await page.locator("#tachesBandeau .tache", { hasText: "Séance 3" }).count();
  const s4 = await page.locator("#tachesBandeau .tache", { hasText: "Séance 4" }).count();
  ok("n°30 : chaque tâche dit sa séance — une tâche en séance 3, une en séance 4", s3 === 1 && s4 === 1, s3 + " tâche(s) « Séance 3 », " + s4 + " « Séance 4 »");
  ok("n°30 : aucune tâche cochée en début de parcours",
     (await page.locator("#tachesBandeau .tache.fait").count()) === 0);
}

/* — n°31 : les versions étayées — */
{
  /* compté par règle, hors exercices d'atelier insérés (ils ont leurs propres étayages) */
  const e = await page.locator("details.etayage:not(.atelier-incruste details)").count();
  const ta = await page.locator("textarea:not(.atelier-incruste textarea):not(.bonus textarea)").count();
  ok("n°31 : les rédactions principales ont leur version étayée", e >= CFG.etayages,
     e + " étayages (attendu ≥ " + CFG.etayages + ") pour " + ta + " zones de rédaction hors Bonus");
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
  const synth = fs.readFileSync(path.join(LOT, "synthese_professeur_3e_C7.html"), "utf8");
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
  ok("n°122 : aucune question retirée (" + CFG.activites + " vérificateurs)",
     (await page.locator(".btn.check").count()) === CFG.activites);

  /* — lot du 05/10/2026 : encart sans compte (mode mixte conservé), version 🅰 retirée —
     Le contenu de Vittascience (blocs, Python, réouverture) a été mesuré à la main et n'est pas rejoué ici :
     service externe. On éprouve ce que NOTRE page promet. */
  {
    const hrefs = await page.$$eval("a.vs-lien", a => a.map(x => x.getAttribute("href")));
    ok("gestes · les liens-boutons gardent l'éditeur en ?mode=mixed (l'activité 3 va des blocs au Python)",
       hrefs.length >= 1 && hrefs.every(h => /^https:\/\/fr\.vittascience\.com\/python\/\?mode=mixed(&|&amp;|$)/.test(h)), hrefs.join(" | "));
    const choix = await page.$$eval(".parcours-btn", b => b.map(x => x.dataset.choix).join(","));
    const texte = await page.evaluate(() => document.body.textContent);
    ok("gestes · plus de version 🅰 : ni bouton, ni carte, ni « Avec le matériel »",
       choix === "b,c,tous" && !/🅰/.test(texte) && !/Avec le matériel/i.test(texte), "boutons : " + choix);
    const note = await page.locator("#vs1 .editeur-py-note").first().textContent();   // l'éditeur Python intégré (04/11/2026)
    ok("gestes · l'activité 3 limite le volet Python (Vittascience, facultatif) et demande de nommer puis télécharger (geste 3 de l'éditeur intégré)",
       note.includes("Dans le volet Python, change seulement ce que la consigne demande. Le reste, fais-le avec les blocs.")
       && note.includes("Nomme ton fichier 3e-CAPTEUR-TON NOM, puis télécharge-le (geste 3)."), note.trim().slice(0, 120));
    const txt = await page.evaluate(() => document.body.textContent);
    ok("gestes · le Bonus de 3e dit « En Python, un seul élément par print, et n'additionne pas de textes : le téléchargement les abîmerait. »",
       txt.includes("En Python, un seul élément par print, et n'additionne pas de textes : le téléchargement les abîmerait."));
    await page.evaluate(() => document.querySelectorAll(".gestes-outil img").forEach(i => { i.loading = "eager"; }));
    await page.waitForTimeout(800);
    const imgs = await page.$$eval(".gestes-outil img", l => l.map(i => ({ charge: i.complete && i.naturalWidth > 0, alt: (i.getAttribute("alt") || "").trim().length })));
    ok("gestes · les " + imgs.length + " captures de Windows de l'encart se chargent, toutes avec un texte alternatif (depuis le 05/11/2026, l'éditeur n'y est plus en image : il y est en vrai)",
       imgs.length === 4 && imgs.every(i => i.charge && i.alt > 20),
       imgs.filter(i => !i.charge).length + " cassée(s), " + imgs.filter(i => i.alt <= 20).length + " sans texte alternatif");
    const essai = await page.evaluate(async () => {
      const bloc = document.querySelector(".gestes-outil .editeur-py-essai");
      const r = bloc && window.EditeurPython ? await window.EditeurPython.executer(document.getElementById("py_echauffement").value) : null;
      return { actif: !!bloc && bloc.classList.contains("editeur-py--actif"), gestes: document.querySelectorAll(".gestes-outil ol.gestes-pratique > li[data-geste]").length,
               suivi: !!document.querySelector(".gestes-outil ol.gestes-pratique--actif"), sortie: r && r.sortie, erreur: r && r.erreur };
    });
    ok("gestes · l'échauffement a son éditeur d'essai, monté, et ses quatre gestes suivis ; le programme d'essai s'exécute : « Bonjour Camille ! » puis « 2 + 3 = 5 » (05/11/2026)",
       essai.actif && essai.gestes === 4 && essai.suivi && essai.sortie === "Bonjour Camille !\n2 + 3 = 5\n" && !essai.erreur, JSON.stringify(essai));
    /* un élève qui avait choisi 🅰 avant le retrait : sa sauvegarde dit « a » — dans un contexte à part */
    const ctxA = await nav.newContext({ viewport: { width: 390, height: 844 } });
    await ctxA.addInitScript(() => localStorage.setItem("seq_3e_C7_capteur_confort", JSON.stringify({ inputs: {}, exp: { parcours: "a" } })));
    const pA = _groupesRadio(await ctxA.newPage());
    await pA.goto(url(CFG.seq));
    await pA.waitForTimeout(400);
    const classeA = await pA.evaluate(() => document.body.className);
    const noteA = await pA.locator("#parcoursNote").textContent();
    ok("gestes · un ancien choix « a » mémorisé retombe sur « tous » (rien n'est masqué à tort)",
       !/parcours-/.test(classeA) && /tous/.test(noteA), noteA.trim());
    await ctxA.close();
  }
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

/* — le verrou expérientiel de l'activité 0 (seulement là où il existe) — */
if (!CFG.essaisBanc) {
  console.log("·  activité 0 : ce lot n'a pas de verrou de banc — contrôle NON applicable, donc NON exécuté");
} else {
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

/* — la progression : elle démarre à zéro, et le tableau de bord est complet — */
{
  const prog = await page.locator("#progTxt").textContent();
  ok("progression : la page démarre à 0 / " + CFG.activites, prog.trim().startsWith("0 / " + CFG.activites + " "), prog.trim());
  ok("tableau de bord : aucune tâche cochée avant validation",
     (await page.locator("#tachesBandeau .tache.fait").count()) === 0);
}

/* — l'ordre des étapes : la validation exige le bon ordre — */
{
  await ouvrirSeanceDe(page, "#a3o1");   // l'algorigramme est à la séance 2
  for (let i = 1; i <= 5; i++) await page.selectOption("#a3o" + i, String(i));
  await page.click('.btn.check[data-check="3"]');
  await page.waitForTimeout(150);
  ok("act. 3 : l’algorigramme validé 5/5 dans le bon ordre",
     /activité validée/.test(await page.locator("#fb3").textContent()));
  await page.selectOption("#a3o2", "4");
  await page.click('.btn.check[data-check="3"]');
  await page.waitForTimeout(150);
  const fb = await page.locator("#fb3").textContent();
  ok("act. 3 : un ordre faux est refusé (4/5)", /4\/5/.test(fb), fb.slice(0, 45));
  await page.selectOption("#a3o2", "2");
}

/* — séances 3 et 4 : les vérificateurs des activités 6 et 7 exigent la réussite des exercices insérés.
     Les bonnes réponses à cocher sont LUES dans la définition JSON de chaque section ; les
     réponses écrites viennent de CFG.textes (le champ `exemple` de l'atelier). — */
async function remplirExo(uid) {
  await page.evaluate(({ uid, textes }) => {
    const sec = document.getElementById(uid).closest(".atelier-incruste");
    const D = JSON.parse(sec.querySelector('script[type="application/json"]').textContent).exercices[uid];
    const boite = document.getElementById(uid);
    const coche = (name, v) => { const r = [...boite.querySelectorAll('input[name="' + name + '"]')].find(x => x.value === v); r.checked = true; r.dispatchEvent(new Event("change", { bubbles: true })); };
    for (const w of D.widgets) {
      if (w.type === "choix") coche(w.name, w.bonne);
      else if (w.type === "cases") w.toutes.forEach(v => { const r = [...boite.querySelectorAll('input[name="' + w.name + '"]')].find(x => x.value === v); r.checked = w.bonnes.includes(v); r.dispatchEvent(new Event("change", { bubbles: true })); });
      else if (w.type === "classer") w.items.forEach(it => coche(it.name, it.bonne));
      else if (w.type === "texte") { const t = document.getElementById(w.name); t.value = textes[w.name] || ""; t.dispatchEvent(new Event("input", { bubbles: true })); }
      else if (w.type === "croquis") {
        const d = document.getElementById(w.name + "_desc");
        d.value = "Trois croquis côte à côte : 1, un collier serré autour du poteau ; 2, une platine au sommet ; 3, un bras en équerre. Légendes, flèche rouge du vent, cote Ø 60 mm.";
        d.dispatchEvent(new Event("input", { bubbles: true }));
        w.checklist.forEach((_, i) => { const c = document.getElementById(w.name + "_check-" + i); c.checked = true; c.dispatchEvent(new Event("change", { bubbles: true })); });
      }
    }
  }, { uid, textes: CFG.textes });
}
async function verifierExo(uid) {
  await page.click("#" + uid + " button.verifier");
  await page.waitForTimeout(120);
  return (await page.locator("#" + uid + " .retour").textContent()) || "";
}
async function verifierActivite(n) {
  await page.click('.btn.check[data-check="' + n + '"]');
  await page.waitForTimeout(150);
  return (await page.locator("#fb" + n).textContent()) || "";
}
{
  await ouvrirSeanceDe(page, "#activite-6");   // l'activité 6 est à la séance 3, la 7 à la séance 4
  let fb = await verifierActivite(6);
  ok("séance 3 · act. 6 : refusée (🔒) tant que l'exercice FAST inséré n'est pas réussi",
     /🔒/.test(fb) && /diagramme FAST/.test(fb), fb.slice(0, 80));
  const vide = await verifierExo("fa_3e_e6");
  ok("séance 3 · act. 6 : l'exercice FAST inséré, vérifié à vide, demande à reprendre", /🔴/.test(vide), vide.slice(0, 60));
  await remplirExo("fa_3e_e6");
  const juste = await verifierExo("fa_3e_e6");
  ok("séance 3 · act. 6 : l'exercice FAST inséré, rempli juste, est réussi", /Tout est juste/.test(juste), juste.slice(0, 60));
  fb = await verifierActivite(6);
  ok("séance 3 · act. 6 : validée une fois l'exercice FAST réussi", /activité validée/.test(fb), fb.slice(0, 60));

  await ouvrirSeanceDe(page, "#activite-7");
  fb = await verifierActivite(7);
  ok("séance 4 · act. 7 : refusée (🔒) tant qu'aucun des deux exercices croquis n'est réussi",
     /🔒/.test(fb) && /deux exercices/.test(fb), fb.slice(0, 80));
  const videCq = await verifierExo("cq_3e_e4");
  ok("séance 4 · act. 7 : les trois croquis, vérifiés à vide, demandent à reprendre", /🔴/.test(videCq), videCq.slice(0, 60));
  await remplirExo("cq_3e_e4");
  const justeCq = await verifierExo("cq_3e_e4");
  ok("séance 4 · act. 7 : les trois croquis, remplis juste, sont réussis", /Tout est juste/.test(justeCq), justeCq.slice(0, 60));
  fb = await verifierActivite(7);
  ok("séance 4 · act. 7 : toujours refusée tant que l'exercice 2 (représentations) n'est pas réussi",
     /🔒/.test(fb) && /exercice 2/.test(fb), fb.slice(0, 80));
  await remplirExo("cq_3e_e6");
  const justeRep = await verifierExo("cq_3e_e6");
  ok("séance 4 · act. 7 : l'exercice des représentations, rempli juste, est réussi", /Tout est juste/.test(justeRep), justeRep.slice(0, 60));
  fb = await verifierActivite(7);
  ok("séance 4 · act. 7 : validée une fois les deux exercices réussis", /activité validée/.test(fb), fb.slice(0, 60));
  ok("séances 3 et 4 : le tableau de bord coche les activités 6 et 7",
     (await page.locator("#tachesBandeau .tache.fait", { hasText: "Séance 3" }).count()) === 1
       && (await page.locator("#tachesBandeau .tache.fait", { hasText: "Séance 4" }).count()) === 1);
  /* le positionnement du bilan, en boutons radio, doit survivre au rechargement */
  await page.check("#pos_c72_3");
  await page.fill("#bilanHyp", "Je garde 28 °C : les essais au simulateur montrent que l'alerte passe au bon moment.");
  await page.dispatchEvent("#bilanHyp", "change");
}

/* — sauvegarde / restauration — */
{
  await page.waitForTimeout(200);
  const cle = await page.evaluate(k => localStorage.getItem(k), CFG.cle);
  ok("sauvegarde : la clé localStorage attendue est écrite", !!cle && cle.length > 50, CFG.cle);
  const captes = Object.keys((JSON.parse(cle || "{}").inputs) || {}).filter(k => /^(fa|cq)_3e_/.test(k));
  ok("sauvegarde : les champs des exercices insérés ne sont pas captés par la sauvegarde de la page",
     captes.length === 0, captes.slice(0, 4).join(", ") || "aucun");
  await page.reload();
  await page.waitForTimeout(500);
  /* activités 3, 6 et 7 validées plus haut (l'activité 3 reste acquise après l'ordre faux) */
  const prog = (await page.locator("#progTxt").textContent()).trim();
  ok("restauration : la progression est relue sans erreur (3 / " + CFG.activites + ")",
     prog.startsWith("3 / " + CFG.activites + " "), prog);
  ok("restauration : le tableau de bord est reconstruit",
     (await page.locator("#tachesBandeau .tache").count()) === CFG.activites);
  const cochesFast = await page.locator("#fa_3e_e6 input:checked").count();
  const cochesRep = await page.locator("#cq_3e_e6 input[type=radio]:checked").count();
  ok("restauration : les exercices insérés retrouvent leurs réponses (FAST : 3 cases + 4 corrections ; représentations : 9 choix)",
     cochesFast === 7 && cochesRep === 9 && /collier/.test(await page.inputValue("#cq_3e_e4__choix")),
     "FAST " + cochesFast + " · représentations " + cochesRep);
  ok("restauration : le positionnement du bilan (bouton radio) et le retour à l'hypothèse sont relus",
     await page.isChecked("#pos_c72_3") && /28/.test(await page.inputValue("#bilanHyp")));
}

/* — reprise d'un travail enregistré AVANT l'ajout de la séance 3 (ancien format, 6 activités) — */
{
  const ctxV = await nav.newContext({ viewport: { width: 390, height: 844 } });
  await ctxV.addInitScript(() => {
    if (sessionStorage.getItem("dejaInit")) return;
    sessionStorage.setItem("dejaInit", "1");
    localStorage.setItem("seq_3e_C7_capteur_confort", JSON.stringify({
      inputs: { hyp: "Je pense qu'il faut alerter à 28 °C.", a0q1: "28 °C", bilan4: "3", bilan1: "le seuil" },
      exp: { simMontee: true, simDescente: true },
      par: { s: ["0", "1", "2", "3", "4", "5"] }
    }));
  });
  const pV = _groupesRadio(await ctxV.newPage());
  const eV = [];
  pV.on("pageerror", e => eV.push(String(e)));
  await pV.goto(url(CFG.seq));
  await pV.waitForTimeout(500);
  const progV = (await pV.locator("#progTxt").textContent()).trim();
  ok("reprise : une sauvegarde d'avant la séance 3 se relit sans erreur — 6 / " + CFG.activites + ", tâches 6 et 7 à faire",
     eV.length === 0 && progV.startsWith("6 / " + CFG.activites + " ")
       && (await pV.locator("#tachesBandeau .tache.fait").count()) === 6
       && (await pV.inputValue("#hyp")).startsWith("Je pense") && (await pV.inputValue("#bilan4")) === "3",
     progV + (eV.length ? " · " + eV[0] : ""));
  await ctxV.close();
}

/* — l'éditeur Python intégré (04/11/2026) : il remplace l'onglet Vittascience. Le code de départ s'exécute (rien à
     afficher : la décision est à écrire) ; le programme de la correction affiche ce que dit la correction ; le banc
     d'essai juge la décision sur sept températures (n°333, 25/11/2026). — */
{
  const ctxE = await nav.newContext({ viewport: { width: 1280, height: 900 } });
  const reseau = [];
  ctxE.on("request", r => { if (/^https?:/.test(r.url())) reseau.push(r.url()); });
  const { page: pe, erreurs: ee } = await ouvrir(ctxE, CFG.seq);
  // le Bonus se replie (révision du 14/11/2026) : on l'ouvre, comme l'élève qui a fini
  await pe.evaluate(() => document.querySelectorAll("details.bonus-replie").forEach((d) => { d.open = true; }));
  await eprouverPose(pe, ["vs1", "vs2"], ok);
  await eprouverEditeurs(pe, [
    { bloc: "vs1", nom: "activité 3b", onglet: "#tab-s2", depart: { sortie: "" },
      corrige: { quoi: "ALERTE", sortie: "ALERTE\n",
        code: 'seuil = 28\nT = 32\nif T > seuil:\n    print("ALERTE")\nelse:\n    print("ok")\n' } },
    { bloc: "vs2", nom: "Bonus", onglet: "#tab-s4", depart: { sortie: "" },
      corrige: { quoi: "PRÉ-ALERTE pour T = 27", sortie: "PRÉ-ALERTE\n",
        code: 'T = 27\nif T > 28:\n    print("ALERTE")\nelif T > 26:\n    print("PRÉ-ALERTE")\nelse:\n    print("ok")\n' } },
  ], ok);
  /* n°333 (25/11/2026) : le banc d'essai rejoue la décision sur sept températures — seuil 28 et seuil 26 —, et seul
     un programme qui fait ce que dit l'algorigramme ouvre le verrou. Avant : une sortie non vide suffisait. */
  const V = 'seuil = 28\nT = 32\n';
  await eprouverBanc(pe, "vs1", [
    { nom: "le programme de la correction : 7 / 7", code: V + 'if T > seuil:\n    print("ALERTE")\nelse:\n    print("ok")\n', conforme: true, verdict: /7 \/ 7 essais conformes/ },
    { nom: "apostrophes et un autre texte que « ok » : même verdict", code: V + "if T > seuil:\n    print('ALERTE')\nelse:\n    print('tout va bien')\n", conforme: true, verdict: /7 \/ 7/ },
    { nom: "print(\"x\") seul : refusé (avant, il ouvrait le verrou)", code: V + 'print("x")\n', conforme: false, verdict: /T = 29 °C[\s\S]*Attendu : « ALERTE »/ },
    { nom: ">= au lieu de > : refusé pile au seuil, à 28 °C", code: V + 'if T >= seuil:\n    print("ALERTE")\nelse:\n    print("ok")\n', conforme: false, verdict: /seuil = 28, T = 28 °C[\s\S]*28 > 28 est faux[\s\S]*Obtenu : « ALERTE »/ },
    { nom: "28 écrit en dur : refusé quand le seuil passe à 26", code: V + 'if T > 28:\n    print("ALERTE")\nelse:\n    print("ok")\n', conforme: false, verdict: /seuil = 26, T = 27 °C/ },
    { nom: "deux-points oubliés : l'erreur se dit avec sa ligne, ce n'est pas une limite du banc", code: V + 'if T > seuil\n    print("ALERTE")\n', conforme: false, verdict: /une erreur — [^\n]*ligne 3/ },
  ], ok, { onglet: "#tab-s2" });
  await eprouverBanc(pe, "vs2", [
    { nom: "Bonus, le programme du corrigé : 6 / 6", code: 'T = 27\nif T > 28:\n    print("ALERTE")\nelif T > 26:\n    print("PRÉ-ALERTE")\nelse:\n    print("OK")\n', conforme: true, verdict: /6 \/ 6/ },
    { nom: "Bonus, le seuil bas testé d'abord : refusé à 29 °C", code: 'T = 27\nif T > 26:\n    print("PRÉ-ALERTE")\nelif T > 28:\n    print("ALERTE")\nelse:\n    print("OK")\n', conforme: false, verdict: /T = 29 °C[\s\S]*Obtenu : « PRÉ-ALERTE »/ },
  ], ok, { onglet: "#tab-s4" });
  /* l'activité 3b de bout en bout : validée avec le banc, puis revalidée après une frappe */
  await pe.click("#tab-s2"); await pe.waitForTimeout(150);
  await pe.evaluate(() => { for (const [id, v] of [["algo", "DÉBUT → mesurer T → T > 28 ? → OUI : LED allumée, NON : LED éteinte → retour"], ["a3hys", "allumer si T > 29, éteindre si T < 27"], ["a3diag", "capteur débranché : je lis T sur la console"]]) { const e = document.getElementById(id); e.value = v; e.dispatchEvent(new Event("input", { bubbles: true })); } });
  await executerBloc(pe, "vs1", V + 'if T > seuil:\n    print("ALERTE")\nelse:\n    print("ok")\n');
  await pe.waitForFunction(() => /conformes/.test((document.getElementById("vs1-banc") || {}).textContent || ""));
  await pe.waitForTimeout(700);   // l'éditeur sauvegarde 500 ms après la dernière frappe (un « change ») : on vérifie après, comme l'élève
  await pe.evaluate(() => document.querySelector('.btn.check[data-check="4"]').click());
  const prog = async () => parseInt(((await pe.locator("#progTxt").textContent()) || "0").trim(), 10);
  const avant = await prog();
  ok("act. 3b : validée quand le banc d'essai dit 7 / 7", /activité validée/.test(await pe.locator("#fb4").textContent()), (await pe.locator("#fb4").textContent()).slice(0, 80));
  await eprouverRejouer(pe, "vs1", ok);
  const apres = await prog();
  ok("act. 3b : la validation est retirée (la progression perd une activité), et le message dit pourquoi",
     /revalider/.test(await pe.locator("#fb4").textContent()) && apres === avant - 1, (await pe.locator("#fb4").textContent()).slice(0, 60) + " · " + avant + " → " + apres);
  await pe.evaluate(() => document.querySelector('.btn.check[data-check="4"]').click());
  ok("act. 3b : « Vérifier » sans rejouer → 🔒 À rejouer", /🔒 ↻ À rejouer/.test(await pe.locator("#fb4").textContent()), (await pe.locator("#fb4").textContent()).slice(0, 80));
  ok("éditeur Python · aucune requête réseau, zéro erreur JavaScript", reseau.length === 0 && ee.length === 0, reseau.concat(ee).slice(0, 3).join(" | "));
  await pe.close(); await ctxE.close();
}

/* — aucun envoi réseau — */
{
  const sorties = [];
  const p2 = _groupesRadio(await ctx.newPage());
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
  /* chaque séance, ouverte à son en-tête : visible, et sans défilement horizontal */
  const vues = [];
  for (let i = 1; i <= CFG.seances; i++) {
    await pm.click('.seance-tab[data-panel="s' + i + '"]'); await pm.waitForTimeout(100);   // l'élève ouvre l'onglet de la séance
    await pm.locator("#seance-" + i).scrollIntoViewIfNeeded();
    await pm.waitForTimeout(120);
    vues.push(await pm.locator("#seance-" + i).isVisible());
    await shot(pm, "mobile_seance_" + i, "#seance-" + i);
  }
  const debord2 = await pm.evaluate(() =>
    Math.max(0, document.documentElement.scrollWidth - document.documentElement.clientWidth));
  ok("mobile 390 px : les " + CFG.seances + " séances s'ouvrent à leur en-tête, sans défilement horizontal",
     vues.length === CFG.seances && vues.every(Boolean) && debord2 === 0, vues.join(",") + " · débord = " + debord2 + " px");
  await pm.close();
  await ctxm.close();
}

/* ═══════════════════ 3. Le QCM ═══════════════════ */
{
  const ctxq = await nav.newContext({ viewport: { width: 1280, height: 900 } });
  const { page: pq, erreurs: eq } = await ouvrir(ctxq, CFG.qcm);
  ok("QCM : chargement sans erreur JS", eq.length === 0, eq.slice(0, 2).join(" | "));
  /* Format actuel du dépôt : {q, o, r, expl, d, …} — 30 questions, 4 propositions `o`,
     bonne réponse `r` (0 à 3), explication `expl`, et `d` : une réfutation par
     proposition, VIDE à l'index de la bonne réponse. On lit ces champs-là et eux seuls,
     sans repli sur les anciens noms (opts, ok, exp) : un champ renommé doit faire échouer. */
  const meta = await pq.evaluate(src => {
    const m = src.match(/const (?:QUESTIONS|questions)\s*=\s*(\[[\s\S]*?\n\];)/);
    if (!m) return null;
    let q;
    try { q = eval(m[1].replace(/;\s*$/, "")); } catch { return null; }
    if (!Array.isArray(q)) return null;
    const rep = {};
    q.forEach(x => { rep[x.r] = (rep[x.r] || 0) + 1; });
    const plein = t => typeof t === "string" && t.trim() !== "";
    const sansExp = q.filter(x => !plein(x.expl)).length;
    const sansQuatre = q.filter(x => !(Array.isArray(x.o) && x.o.length === 4 && x.o.every(plein)
      && Number.isInteger(x.r) && x.r >= 0 && x.r <= 3)).length;
    /* réfutation attendue : 4 entrées, vide à l'index r, non vide sur les 3 autres */
    const sansRefutation = q.filter(x => !(Array.isArray(x.d) && x.d.length === 4
      && x.d.every((t, i) => i === x.r ? (typeof t === "string" && t.trim() === "") : plein(t)))).length;
    return { n: q.length, rep, sansExp, sansQuatre, sansRefutation };
  }, fs.readFileSync(path.join(LOT, CFG.qcm), "utf8"));
  if (meta) {
    ok("QCM : le tableau des questions est lisible et chargé", meta.n > 0, meta.n + " questions");
    ok("QCM : chaque question a 4 propositions", meta.sansQuatre === 0, meta.sansQuatre + " anomalies");
    ok("QCM : chaque question porte une explication", meta.sansExp === 0, meta.sansExp + " sans explication");
    ok("QCM : les 4 positions servent de bonne réponse",
       Object.keys(meta.rep).length === 4, JSON.stringify(meta.rep));
    ok("QCM : état déclaré — chaque mauvaise réponse a sa réfutation (vide sur la bonne)",
       meta.sansRefutation === 0, meta.sansRefutation + " question(s) sans réfutation complète (0 attendu)");
  } else {
    ok("QCM : le tableau des questions est lisible depuis la source", false,
       "const questions = [...] introuvable ou non évaluable — contrôle NON exécuté");
  }
  await shot(pq, "qcm");
  await pq.close();
  await ctxq.close();
}

/* — n°345 et n°330 (27/11/2026) : six questions sur document, et un billet de sortie — */
{
  const src = fs.readFileSync(path.join(LOT, CFG.qcm), "utf8");
  const imgs = [...src.matchAll(/img:\{src:"(Images\/[^"]+)",alt:"([^"]*)"/g)].map(m => ({ src: m[1], alt: m[2] }));
  ok("QCM : au moins six questions sur document", imgs.length >= 6, imgs.length + " question(s) illustrée(s)");
  ok("QCM : chaque image existe dans Images/", imgs.every(i => fs.existsSync(path.join(LOT, i.src))));
  ok("QCM : chaque document a une description qui dit ce qu'il montre", imgs.every(i => i.alt.length > 60));
  let aJour = true; try { execSync("python3 documents_qcm.py --verifier", { cwd: LOT, stdio: "pipe" }); } catch (e) { aJour = false; }
  ok("QCM : le document neuf est à jour de la séquence (documents_qcm.py --verifier)", aJour);

  const cb = await nav.newContext({ viewport: { width: 1280, height: 900 } });
  const pb = await cb.newPage();
  await pb.goto(url(CFG.seq)); await pb.waitForTimeout(400);
  const b = await pb.evaluate(() => {
    const s = document.getElementById("billetSortie"); if (!s) return null;
    const cartes = [...document.querySelectorAll("section.card")];
    const bonus = cartes.find(c => /🎁 Bonus/.test(c.querySelector("h2")?.textContent || ""));
    const c = s.querySelector("details.correction")?.textContent || "";
    return { zones: s.querySelectorAll("textarea[data-save]").length, aides: s.querySelectorAll("details.etayage").length,
      criteres: (c.match(/Critère/g) || []).length, contre: (c.match(/✘/g) || []).length,
      boutons: s.querySelectorAll("button").length, avantBonus: !!bonus && cartes.indexOf(s) === cartes.indexOf(bonus) - 1 };
  });
  ok("billet de sortie : présent", !!b);
  if (b) {
    ok("billet de sortie : deux zones sauvegardées, deux versions étayées", b.zones === 2 && b.aides === 2, b.zones + " zones, " + b.aides + " aides");
    ok("billet de sortie : deux critères, des contre-exemples, aucun bouton", b.criteres === 2 && b.contre >= 2 && b.boutons === 0,
       b.criteres + " critères, " + b.contre + " ✘, " + b.boutons + " bouton(s)");
    ok("billet de sortie : juste avant le Bonus", b.avantBonus);
    const TXT = "Essai 2, le cas frontière : 80 dB, voyant éteint.";
    await pb.evaluate(() => { const t = document.querySelector('.seance-tab[data-panel="s4"]'); if (t) t.click(); });
    await pb.fill("#bs_3e_C7_1_2", TXT);
    await pb.evaluate(() => document.getElementById("bs_3e_C7_1_2").blur());
    await pb.waitForTimeout(200); await pb.reload(); await pb.waitForTimeout(400);
    ok("billet de sortie : la réponse survit au rechargement", (await pb.inputValue("#bs_3e_C7_1_2")) === TXT);
  }
  await cb.close();
}

verifLiens();
await nav.close();

const total = resultats.length, reussis = resultats.filter(r => r.ok).length;
console.log("\n═══ " + reussis + " / " + total + " tests réussis · captures dans " + CAP + " ═══");
if (reussis !== total) {
  console.log("Échecs :");
  resultats.filter(r => !r.ok).forEach(r => console.log("  ❌ " + r.nom + (r.detail ? " — " + r.detail : "")));
}
