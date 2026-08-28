#!/usr/bin/env node
/**
 * verificateur_lots.mjs — deux contrôles que personne ne fait à l'œil.
 *
 * POURQUOI CES DEUX-LÀ
 * --------------------
 * Ils sont nés d'une campagne de corrections où deux audits pédagogiques
 * sérieux ont été passés sur le Thème 1. Ni l'un ni l'autre n'avait vu ce que
 * ces vingt lignes trouvent en quelques secondes :
 *
 *   · le bouton « QCM » de la séquence 5e Chengdu ne menait nulle part — il
 *     pointait vers un fichier renommé des mois plus tôt ;
 *   · le bouton « Enregistrer » de la séquence cybersécurité n'existait pas :
 *     le script le cherchait, la page ne le contenait pas. Cent onze champs à
 *     remplir sur trois séances, et rien qui se garde ;
 *   · dans le même fichier, l'activité 5.b lisait `q5b` quand la zone de saisie
 *     s'appelle `q5b-response` : quoi que l'élève écrive, on lui répondait que
 *     c'était trop court ;
 *   · et la barre de progression animait un élément absent.
 *
 * AUCUN de ces défauts ne provoque d'erreur JavaScript. Le code est prudent :
 * `if (bar)`, `?.value`. **Sa prudence est exactement ce qui les rend
 * silencieux** — et un défaut silencieux se lit comme une réussite.
 *
 * CE QUE CHAQUE CONTRÔLE CHERCHE
 * ------------------------------
 * 1. LIENS — tout `href` ou `src` relatif dont la cible n'existe pas sur le
 *    disque. On ignore les URL absolues, les `data:`, les gabarits `${…}` et
 *    tout ce qui vit dans un commentaire HTML : un emplacement réservé n'est
 *    pas un lien mort.
 *
 * 2. ÉLÉMENTS COMMANDÉS — tout `getElementById("x")` dont l'`id` n'apparaît
 *    nulle part dans la page. Deux sources de faux positifs, écartées :
 *    les identifiants construits par concaténation (`"fb-" + i`), reconnus à
 *    leur terminaison en tiret ou à leur brièveté, et ceux fabriqués dans un
 *    gabarit.
 *
 *    Restent les absences VOULUES — un moteur partagé par quatre pages, dont
 *    une seule porte le bandeau qu'il met à jour. Elles ne sont pas devinées :
 *    elles sont DÉCLARÉES dans `elements_optionnels.json`, avec leur raison et
 *    la réponse à « qu'est-ce que l'élève perd si l'élément n'existe pas ? ».
 *    Si la réponse est « rien », c'est une exception ; sinon c'est un défaut,
 *    et sa place n'est pas dans l'inventaire.
 *
 * CE QU'IL NE FAIT PAS
 * --------------------
 * Il ne juge aucun contenu. Il ne dit pas si une séquence est bonne : il dit
 * si elle tient ses propres promesses techniques. C'est un cliquet, pas un
 * avis (règle n°143).
 *
 * CE QU'IL NE REGARDE PAS, ET LE DIT
 * ----------------------------------
 * `_archive-anciennes-versions/` et `_outils/` sont écartés par défaut. Le premier
 * garde des états
 * passés, conservés exprès, et leurs liens pointent vers un monde qui n'existe
 * plus. Les compter serait fabriquer quatre-vingts alertes qu'on apprendrait à
 * ignorer — et un indicateur qu'on ignore ne sert plus à rien (règle n°154).
 * Le contrôle ANNONCE ce qu'il a écarté, il ne le tait pas (règle n°146), et
 * `--tout` le lui fait examiner quand même. Le second contient des GABARITS,
 * dont les liens sont des emplacements à substituer : ils seront toujours morts
 * là où ils sont, et vivants une fois le gabarit copié.
 *
 * USAGE
 *   node verificateur_lots.mjs            # les thèmes vivants
 *   node verificateur_lots.mjs theme-1-*  # un thème
 *   node verificateur_lots.mjs --tout     # y compris l'archive
 *   node verificateur_lots.mjs --json     # pour un enchaînement automatique
 */
import { readFileSync, existsSync, readdirSync, statSync } from "node:fs";
import { join, dirname, normalize, relative, basename } from "node:path";
import { fileURLToPath } from "node:url";

/* Les absences VOULUES sont déclarées, avec leur raison, dans un inventaire —
   comme les absolus du linter voisin. Un élément absent qui n'y figure pas est
   un défaut ; un élément qui y figure a dû être justifié par écrit. */
const INVENTAIRE = join(dirname(fileURLToPath(import.meta.url)), "elements_optionnels.json");
let declares = new Set();
try {
  const inv = JSON.parse(readFileSync(INVENTAIRE, "utf8"));
  declares = new Set((inv.exceptions || []).map((e) => e.fichier + "#" + e.element));
} catch { /* pas d'inventaire : tout élément absent est un défaut */ }

const args = process.argv.slice(2);
const enJson = args.includes("--json");
const tout = args.includes("--tout");
const racines = args.filter((a) => !a.startsWith("--"));
const ECARTES = ["_archive-anciennes-versions", "_outils"];

/* ── parcours des fichiers HTML ─────────────────────────────────────────── */
const ecartes = [];
function pagesHtml(depart) {
  const out = [];
  (function descendre(d) {
    let entrees;
    try { entrees = readdirSync(d, { withFileTypes: true }); } catch { return; }
    for (const e of entrees) {
      if (e.name === ".git" || e.name === "node_modules") continue;
      if (!tout && ECARTES.includes(e.name)) { ecartes.push(e.name); continue; }
      const p = join(d, e.name);
      if (e.isDirectory()) descendre(p);
      else if (e.name.endsWith(".html")) out.push(p);
    }
  })(depart);
  return out;
}

const sansCommentaires = (t) => t.replace(/<!--[\s\S]*?-->/g, " ");

/* ── contrôle 1 : les liens relatifs ────────────────────────────────────── */
function liensMorts(fichier, texte) {
  const d = dirname(fichier);
  const trouves = [];
  const motif = /(?:href|src)="([^"#?]+)"/g;
  let m;
  while ((m = motif.exec(texte))) {
    const h = m[1].trim();
    if (!h) continue;
    if (/^(https?:|data:|mailto:|tel:|javascript:|#|\/\/)/.test(h)) continue;
    if (h.includes("${") || h.includes("{{")) continue;      // gabarit, pas un lien
    let cible;
    try { cible = normalize(join(d, decodeURIComponent(h))); } catch { continue; }
    if (!existsSync(cible)) trouves.push(h);
  }
  return [...new Set(trouves)];
}

/* ── contrôle 2 : les éléments commandés mais absents ───────────────────── */
function elementsAbsents(texte, fichier) {
  const ids = new Set([...texte.matchAll(/\bid="([^"]+)"/g)].map((m) => m[1]));
  const cherches = new Set(
    [...texte.matchAll(/getElementById\(\s*['"]([^'"]+)['"]/g)].map((m) => m[1])
  );
  const nom = basename(fichier);
  return [...cherches].filter((c) => {
    if (ids.has(c)) return false;
    if (declares.has(nom + "#" + c)) return false;           // absence déclarée
    if (c.includes("${") || c.includes("{{")) return false;  // gabarit
    if (/[-_]$/.test(c)) return false;                       // « fb- » + indice
    if (c.length <= 2) return false;                         // « r » + indice
    // un préfixe d'identifiant existant : c'est une concaténation, pas un oubli
    for (const i of ids) if (i.startsWith(c) && i.length > c.length) return false;
    return true;
  });
}

/* ── exécution ──────────────────────────────────────────────────────────── */
const cibles = racines.length ? racines : ["."];
const fichiers = cibles.flatMap((c) =>
  statSync(c).isDirectory() ? pagesHtml(c) : [c]
);

const rapport = [];
for (const f of fichiers.sort()) {
  const brut = readFileSync(f, "utf8");
  const propre = sansCommentaires(brut);
  const liens = liensMorts(f, propre);
  const elements = elementsAbsents(propre, f);
  if (liens.length || elements.length) {
    rapport.push({ fichier: relative(".", f), liens, elements });
  }
}

if (enJson) {
  console.log(JSON.stringify(rapport, null, 1));
} else {
  const nomCourt = (p) => p.split("/").pop();
  console.log("\n%s pages examinées%s\n", fichiers.length,
    ecartes.length ? "  ·  écarté : " + [...new Set(ecartes)].join(", ") + " (--tout pour l'inclure)" : "");
  if (!rapport.length) {
    console.log("  ✅ aucun lien mort, aucun élément commandé mais absent.\n");
  } else {
    for (const r of rapport) {
      console.log("  " + nomCourt(r.fichier));
      for (const l of r.liens) console.log("      🔗 lien mort           : " + l);
      for (const e of r.elements) console.log("      🎛  élément introuvable : #" + e);
    }
    console.log(
      "\n  %d lien(s) mort(s) · %d élément(s) commandé(s) mais absent(s)\n",
      rapport.reduce((s, r) => s + r.liens.length, 0),
      rapport.reduce((s, r) => s + r.elements.length, 0)
    );
  }
}
process.exit(rapport.length ? 1 : 0);
