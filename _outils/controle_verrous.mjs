/* controle_verrous.mjs — un verrou ne s'ouvre que par un geste.
 *
 * LE CONSTAT QUI A DONNÉ CE CONTRÔLE
 * ----------------------------------
 * La règle d'or n°226 dit qu'un verrou expérientiel — `window.__exp` — ne doit
 * s'ouvrir que par un GESTE de l'élève, jamais au chargement de la page. Elle
 * était vérifiée à la main, page par page, quand quelqu'un y pensait.
 *
 * Le 31/08/2026, la séquence du lampadaire (`5e_C4.1`) a été mesurée pour la
 * première fois : `window.__exp` valait `{"jour":"eteint"}` **dès l'ouverture**.
 * Sa fonction d'affichage du simulateur était appelée à l'initialisation, et
 * elle enregistrait l'état affiché comme une expérience observée. Le verrou de
 * l'activité 3 en exige trois : il s'ouvrait donc d'un tiers tout seul. Le
 * rapport de tests du lot, écrit à la main, affirmait exactement le contraire.
 *
 * CE QUE CE CONTRÔLE FAIT
 * -----------------------
 * Il ouvre CHAQUE séquence et chaque TP du dépôt dans un navigateur neuf —
 * contexte vierge, aucun stockage hérité — et lit `window.__exp` juste après le
 * chargement. Toute clé portant une valeur **vraie** est un verrou ouvert sans
 * geste.
 *
 * CE QU'IL NE COMPTE PAS, ET POURQUOI
 * ------------------------------------
 * Une clé dont la valeur est un objet vide, un tableau vide ou `false` n'est
 * pas une observation : c'est un **casier déclaré d'avance** (`{"bench":{}}`,
 * `{"zoom":false}`). La distinguer d'un verrou ouvert évite de signaler du
 * correct, et un contrôle qui signale du faux finit ignoré (règle d'or n°248).
 *
 * Il ne lit pas non plus ce qu'une page fait APRÈS le chargement : qu'un verrou
 * s'ouvre au bon geste relève de la suite de tests du lot, pas d'ici.
 *
 * Usage :
 *   node _outils/controle_verrous.mjs           # rapport complet
 *   node _outils/controle_verrous.mjs --muet    # seulement les écarts
 * Sortie : 0 si aucun verrou ne s'ouvre au chargement, 1 sinon.
 */
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const ICI = path.dirname(new URL(import.meta.url).pathname);
const DEPOT = path.dirname(ICI);
const ECARTES = /_archive-anciennes-versions|[/\\]\.git/;
const A_VERROUS = /^(sequence|tp|atelier)_.*\.html$/i;

/** Toutes les pages susceptibles de porter un verrou expérientiel. */
function pages(dossier, acc = []) {
  for (const e of fs.readdirSync(dossier, { withFileTypes: true })) {
    const p = path.join(dossier, e.name);
    if (ECARTES.test(p)) continue;
    if (e.isDirectory()) pages(p, acc);
    else if (A_VERROUS.test(e.name)) acc.push(p);
  }
  return acc;
}

/** Une valeur qui vaut « j'ai observé quelque chose », par opposition à un casier vide. */
function estUneObservation(v) {
  if (v === null || v === undefined || v === false) return false;
  if (Array.isArray(v)) return v.length > 0;
  if (typeof v === 'object') return Object.keys(v).length > 0;
  return Boolean(v);
}

const muet = process.argv.includes('--muet');
const liste = pages(DEPOT);
const navigateur = await chromium.launch();
const ecarts = [];
let casiers = 0, sansVerrou = 0, illisibles = 0;

for (const f of liste) {
  const ctx = await navigateur.newContext();      // contexte NEUF : aucun stockage hérité
  const p = await ctx.newPage();
  try {
    await p.goto('file://' + f, { waitUntil: 'load' });
    await p.waitForTimeout(160);
    const exp = await p.evaluate(() => window.__exp || null);
    if (!exp) { sansVerrou++; }
    else {
      const ouverts = Object.entries(exp).filter(([, v]) => estUneObservation(v));
      if (ouverts.length === 0) casiers += Object.keys(exp).length;
      else ecarts.push({ f: path.relative(DEPOT, f), ouverts });
    }
  } catch (e) {
    illisibles++;
    ecarts.push({ f: path.relative(DEPOT, f), erreur: e.message.split('\n')[0].slice(0, 90) });
  }
  await ctx.close();
}
await navigateur.close();

if (!muet) {
  console.log(`${liste.length} page(s) à verrous ouvertes dans un contexte neuf · `
    + `${sansVerrou} sans window.__exp · ${casiers} casier(s) vide(s) déclaré(s) d'avance`);
  console.log('     NON LU : ce qu\'une page fait APRÈS le chargement — qu\'un verrou s\'ouvre\n'
    + '     au bon geste relève de la suite de tests du lot.');
}

if (ecarts.length) {
  console.log(`\n⛔ ${ecarts.length} page(s) ouvrent un verrou AU CHARGEMENT (règle n°226) :`);
  for (const e of ecarts) {
    if (e.erreur) { console.log(`  ${e.f}\n     illisible : ${e.erreur}`); continue; }
    console.log(`  ${e.f}\n     ` + e.ouverts.map(([k, v]) => `${k} = ${JSON.stringify(v)}`).join(' · '));
  }
  console.log('\n     Un verrou ne s\'ouvre que par un GESTE. Une fonction d\'affichage appelée\n'
    + '     à l\'initialisation ne doit pas enregistrer ce qu\'elle affiche.');
  process.exit(1);
}
console.log('✅ aucun verrou expérientiel ouvert au chargement');
process.exit(0);
