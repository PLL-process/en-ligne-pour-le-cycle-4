#!/usr/bin/env node
/**
 * lecteur_qcm_dom.mjs — lire un QCM par sa PAGE RENDUE, quel que soit son moteur.
 *
 * POURQUOI
 * --------
 * `audit_qcm_trois_themes.mjs` lit le texte source et cherche une banque
 * `const QUESTIONS = [...]`. Trente-six QCM du dépôt en ont une ; dix n'en ont
 * pas — et ces dix-là sont restés « non mesurés » (règle n°146 : un outil de
 * mesure déclare ce qu'il n'a pas su lire). Ils ne sont pas pour autant
 * exempts du défaut mesuré partout ailleurs : ils n'ont jamais été regardés.
 *
 * Ces dix pages n'ont pas un moteur, elles en ont CINQ. Écrire cinq analyseurs
 * de texte serait cinq occasions de se tromper, et il en faudrait un sixième au
 * prochain QCM écrit autrement. On change donc de point de vue : au lieu de
 * lire le code qui fabrique les questions, on ouvre la page et on lit LES
 * QUESTIONS — celles que l'élève a sous les yeux.
 *
 * Le lecteur essaie les stratégies dans l'ordre et s'arrête à la première qui
 * rend un résultat complet. Chaque question lue déclare PAR QUELLE stratégie
 * elle l'a été : une mesure dont on ne sait pas d'où elle sort n'est pas une
 * mesure.
 *
 * LES CINQ STRATÉGIES
 * -------------------
 *  1. `checkMCQ('q1','v0',…)`  — la bonne réponse est dans l'appel du bouton
 *     « Corriger », désignée par la VALEUR du radio.
 *  2. `checkQcm(0, 2, …)`      — même idée, mais désignée par son RANG.
 *  3. objet global `{ q1:{correct:"B"} }` — table des bonnes réponses à part.
 *  4. banque JS d'une autre forme — `[{q, options, answer}]`, cherchée parmi
 *     les variables globales de la page.
 *  5. marqueur visible `✔️` en fin de ligne — la page n'a aucun code : la
 *     bonne réponse est signalée à l'élève, donc lisible comme lui la lit.
 *
 * CE QU'IL NE FAIT PAS
 * --------------------
 * Il ne modifie rien et ne clique sur rien : il lit une page au repos. Un QCM
 * qu'aucune des cinq stratégies ne lit ressort `strategie: null` et compte
 * comme NON MESURÉ — jamais comme sain.
 *
 * USAGE
 *   node lecteur_qcm_dom.mjs <fichier.html> [autres…]      → JSON sur stdout
 */
import { chromium } from "playwright";
import path from "node:path";

/* Le corps de l'extraction s'exécute DANS la page : il a le DOM sous la main,
   et les variables globales des scripts classiques de la page. */
function extraire() {
  const txt = (e) => (e ? e.textContent.replace(/\s+/g, " ").trim() : "");
  const propre = (s) => s.replace(/^[A-D][.)]\s*/, "").replace(/\s*✔️?\s*$/, "").trim();

  /* --- outils communs ------------------------------------------------- */
  // Le conteneur d'une question : le plus proche ancêtre qui porte AUSSI le
  // bouton de correction. On remonte prudemment, jamais jusqu'au <body>.
  const carte = (el) => {
    let n = el;
    for (let i = 0; i < 6 && n && n !== document.body; i++) {
      if (n.querySelector && n.querySelector("button[onclick]")) return n;
      n = n.parentElement;
    }
    return el.closest("section, .card, .question, div") || el.parentElement;
  };

  const enonce = (bloc) => {
    const t = bloc.querySelector(".q-title, h3, h4, b, p, legend");
    return t ? txt(t) : "";
  };

  const groupes = () => {
    const noms = [];
    document.querySelectorAll('input[type="radio"]').forEach((r) => {
      if (r.name && !noms.includes(r.name)) noms.push(r.name);
    });
    return noms;
  };

  const optionsDe = (nom) =>
    [...document.querySelectorAll(`input[type="radio"][name="${CSS.escape(nom)}"]`)].map((r) => ({
      valeur: r.value,
      texte: propre(txt(r.closest("label")) || txt(r.parentElement)),
    }));

  /* --- stratégie 1 : checkMCQ('q1','v0', …) --------------------------- */
  function parCheckMCQ() {
    const out = [];
    for (const nom of groupes()) {
      const opts = optionsDe(nom);
      if (opts.length < 2) return null;
      const r = document.querySelector(`input[type="radio"][name="${CSS.escape(nom)}"]`);
      const bloc = carte(r);
      let bonne = -1;
      for (const b of bloc.querySelectorAll("button[onclick]")) {
        const m = /checkMCQ\(\s*['"]([^'"]+)['"]\s*,\s*['"]([^'"]*)['"]/.exec(
          b.getAttribute("onclick") || ""
        );
        if (m && m[1] === nom) bonne = opts.findIndex((o) => o.valeur === m[2]);
      }
      if (bonne < 0) return null;
      out.push({ q: enonce(bloc), options: opts.map((o) => o.texte), bonne });
    }
    return out.length ? out : null;
  }

  /* --- stratégie 2 : checkQcm(index, rangCorrect, …) ------------------- */
  function parCheckQcm() {
    const out = [];
    for (const nom of groupes()) {
      const opts = optionsDe(nom);
      if (opts.length < 2) return null;
      const bloc = carte(document.querySelector(`input[type="radio"][name="${CSS.escape(nom)}"]`));
      let bonne = -1;
      for (const b of bloc.querySelectorAll("button[onclick]")) {
        const m = /checkQcm\(\s*(\d+)\s*,\s*(\d+)/.exec(b.getAttribute("onclick") || "");
        if (m) bonne = Number(m[2]);
      }
      if (bonne < 0 || bonne >= opts.length) return null;
      out.push({ q: enonce(bloc), options: opts.map((o) => o.texte), bonne });
    }
    return out.length ? out : null;
  }

  /* --- les valeurs globales de la page, y compris lexicales ------------
     PIÈGE : un `const` au premier niveau d'un <script> classique n'est PAS une
     propriété de `window` — il vit dans l'environnement lexical global.
     `Object.getOwnPropertyNames(window)` ne le voit donc pas, alors qu'un
     simple `eval("qcmData")` le trouve. C'est exactement le cas des deux QCM
     que la première version de ce lecteur n'a pas su lire : la donnée était
     là, sous le nez de l'outil, et l'outil regardait au mauvais endroit. */
  function nomsGlobaux() {
    const noms = new Set(Object.getOwnPropertyNames(window));
    const decl = /\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=/g;
    for (const s of document.scripts) {
      if (s.src) continue;
      let m;
      while ((m = decl.exec(s.textContent))) noms.add(m[1]);
    }
    return [...noms];
  }
  function valeurGlobale(nom) {
    try { if (nom in window) return window[nom]; } catch { /* ignore */ }
    try { return (0, eval)(nom); } catch { return undefined; }
  }

  /* --- stratégie 3 : table globale { q1:{correct:"B"} } --------------- */
  function parTableGlobale() {
    const noms = groupes();
    if (!noms.length) return null;
    let table = null;
    for (const cle of nomsGlobaux()) {
      let v;
      try { v = valeurGlobale(cle); } catch { continue; }
      if (!v || typeof v !== "object" || Array.isArray(v)) continue;
      const prem = v[noms[0]];
      if (prem && typeof prem === "object" && "correct" in prem) { table = v; break; }
    }
    if (!table) return null;
    const out = [];
    for (const nom of noms) {
      const opts = optionsDe(nom);
      const att = table[nom] && table[nom].correct;
      const bonne = opts.findIndex((o) => o.valeur === att);
      if (bonne < 0) return null;
      const bloc = carte(document.querySelector(`input[type="radio"][name="${CSS.escape(nom)}"]`));
      out.push({ q: enonce(bloc), options: opts.map((o) => o.texte), bonne });
    }
    return out.length ? out : null;
  }

  /* --- stratégie 4 : banque JS d'une autre forme ---------------------- */
  function parBanqueAutre() {
    const bon = (o) =>
      o && typeof o === "object" &&
      Array.isArray(o.options || o.o) &&
      typeof (o.answer ?? o.r ?? o.reponse) === "number";
    for (const cle of nomsGlobaux()) {
      let v;
      try { v = valeurGlobale(cle); } catch { continue; }
      if (Array.isArray(v) && v.length > 3 && v.every(bon)) {
        return v.map((o) => ({
          q: String(o.q || o.question || ""),
          options: (o.options || o.o).map((t) => String(t).replace(/<[^>]+>/g, "").trim()),
          bonne: o.answer ?? o.r ?? o.reponse,
        }));
      }
    }
    return null;
  }

  /* --- stratégie 5 : le ✔️ visible dans le texte ---------------------- */
  function parMarqueur() {
    const out = [];
    for (const bloc of document.querySelectorAll(".question, section.card, .card")) {
      const brut = bloc.innerHTML.split(/<br\s*\/?>/i).map((l) =>
        l.replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim()
      );
      const lignes = brut.filter((l) => /^[A-D][.)]\s/.test(l));
      if (lignes.length < 2) continue;
      const bonne = lignes.findIndex((l) => l.includes("✔"));
      if (bonne < 0) continue;
      const t = brut.find((l) => /^\d+[.)]\s/.test(l)) || "";
      out.push({ q: t, options: lignes.map(propre), bonne });
    }
    return out.length ? out : null;
  }

  const essais = [
    ["checkMCQ", parCheckMCQ],
    ["checkQcm", parCheckQcm],
    ["table globale", parTableGlobale],
    ["banque JS", parBanqueAutre],
    ["marqueur ✔️", parMarqueur],
  ];
  for (const [nom, f] of essais) {
    let r = null;
    try { r = f(); } catch (e) { r = null; }
    if (r && r.length) return { strategie: nom, questions: r };
  }
  return { strategie: null, questions: [] };
}

/* --- mesure : le même indicateur que l'audit des 36 --------------------- */
function mesurer(qs) {
  let plusLongue = 0, visible = 0;
  const lettres = [0, 0, 0, 0];
  for (const q of qs) {
    const L = q.options.map((t) => t.length);
    const r = q.bonne;
    if (r < 0 || r >= L.length) continue;
    if (r < 4) lettres[r]++;
    const autres = Math.max(...L.filter((_, k) => k !== r));
    if (L[r] === Math.max(...L)) plusLongue++;
    // écart relatif ET écart absolu d'au moins 8 caractères — voir règle n°154
    if (L[r] > 1.2 * autres && L[r] - autres >= 8) visible++;
  }
  return { n: qs.length, plusLongue, visible, lettres };
}

const fichiers = process.argv.slice(2);
if (!fichiers.length) {
  console.error("usage : node lecteur_qcm_dom.mjs <fichier.html> [autres…]");
  process.exit(2);
}
const nav = await chromium.launch();
const resultats = [];
for (const f of fichiers) {
  const ctx = await nav.newContext();
  const page = await ctx.newPage();
  const erreurs = [];
  page.on("pageerror", (e) => erreurs.push(String(e)));
  await page.goto("file://" + path.resolve(f));
  await page.waitForTimeout(300);
  const lu = await page.evaluate(extraire);
  await ctx.close();
  resultats.push({
    fichier: path.basename(f),
    chemin: f,
    strategie: lu.strategie,
    erreursJS: erreurs.length,
    ...mesurer(lu.questions),
    questions: lu.questions,
  });
}
await nav.close();
console.log(JSON.stringify(resultats, null, 1));
