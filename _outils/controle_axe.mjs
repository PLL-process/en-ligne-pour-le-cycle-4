/* controle_axe.mjs — l'accessibilité ne recule pas.
 *
 * D'OÙ VIENT CE CONTRÔLE
 * ----------------------
 * L'audit externe du 01/11/2026 (`docs/audits/AUDIT_EXTERNE_2026-11-01_etapes_1_et_2.md`,
 * point 3) a passé axe-core sur les 408 pages du dépôt, avant et après ses
 * corrections : 428 nœuds en contraste insuffisant ramenés à 117, 146 champs
 * sans nom accessible ramenés à 30. Puis l'outil est reparti avec la session :
 * rien dans `_outils/` ne rejouait la mesure. Un champ sans nom ajouté le
 * lendemain ne se serait vu qu'au prochain audit.
 *
 * Ce contrôle rend la mesure permanente. Il ne demande pas « zéro défaut » —
 * le dépôt en porte, connus et comptés — il demande qu'AUCUNE PAGE N'EN PORTE
 * PLUS QU'HIER. La référence (`_outils/axe_reference.json`) dit, règle par
 * règle et page par page, combien de nœuds sont en défaut aujourd'hui.
 *
 * CE QU'IL MESURE
 * ---------------
 * Chaque page publiée, ouverte dans Chromium à 1 280 px, passée à axe-core avec
 * les règles WCAG 2.0 et 2.1, niveaux A et AA (`wcag2a`, `wcag2aa`, `wcag21a`,
 * `wcag21aa`) et les bonnes pratiques (`best-practice`) — les mêmes que l'audit
 * du 01/11, pour que les chiffres se comparent — plus `wcag22aa`.
 *
 * Une page qui ne fait que RENVOYER vers une autre (redirection au chargement)
 * n'est pas mesurée : sa destination l'est, sous son propre nom. Elle est
 * comptée à part, jamais confondue avec une panne.
 *
 *   · Impact « critical » ou « serious » : comparé à la référence. REFUS si, pour
 *     une règle et une page, le nombre de nœuds dépasse celui de la référence
 *     (une page ou une règle absente de la référence vaut zéro).
 *   · Impact « moderate » ou « minor » : compté et rapporté, jamais refusé. Ce
 *     sont les défauts de structure (`region`, `heading-order`) que l'audit a
 *     laissés à la décision de Pascal.
 *
 * CE QU'IL NE MESURE PAS, ET LE DIT
 * ---------------------------------
 *   · axe-core ne voit que ce qu'une machine peut voir : contraste, nom des
 *     champs, rôles, attributs — une part seulement des problèmes
 *     d'accessibilité. Une consigne illisible pour un
 *     lecteur fragile, un ordre de lecture absurde, une alternative d'image
 *     fausse mais présente : rien de cela ne le fait réagir.
 *   · La page est mesurée À L'OUVERTURE : première séance, volets fermés, mode
 *     mission éteint. Ce qui s'ouvre au clic n'est pas vu.
 *   · Un seul gabarit d'écran (1 280 px) ; le téléphone a ses contrôles
 *     (`controle_tactile.py`, `controle_debordement.py`).
 *   · Un défaut corrigé sur une page et le même apparu sur une AUTRE page est
 *     vu (la mesure est par page). Un défaut corrigé et un autre apparu sur la
 *     MÊME page, pour la MÊME règle, ne l'est pas : le compte est le même.
 *
 * PRÉREQUIS
 * ---------
 * Playwright et Chromium, comme les autres `.mjs` du dossier, et le paquet
 * `axe-core` (licence MPL-2.0 ; il n'est PAS versionné dans le dépôt) :
 *     npm install axe-core          # dans le dossier parent du dépôt, ou
 *     AXE_CORE=/chemin/vers/axe.min.js node _outils/controle_axe.mjs
 * Sans lui, le contrôle est EN PANNE (sortie 2), pas vert.
 *
 * Usage :
 *   node _outils/controle_axe.mjs                  # tout le dépôt, contre la référence
 *   node _outils/controle_axe.mjs --muet           # synthèse seule
 *   node _outils/controle_axe.mjs <chemin>         # une page, ou un dossier
 *   node _outils/controle_axe.mjs --json <f>       # la mesure complète, nœuds compris
 *   node _outils/controle_axe.mjs --reference      # ÉCRIT la référence (tout le dépôt
 *                                                  # seulement) : geste de fin de lot,
 *                                                  # après lecture de ce qui a changé
 *
 * Sortie : 0 aucune page n'a reculé · 1 au moins un recul · 2 EN PANNE (axe-core
 * introuvable, aucune page mesurée, ou une page que l'outil n'a pas pu mesurer) —
 * règle d'or n°299.
 */
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const RACINE = path.resolve(ICI, '..');
export const REFERENCE = path.join(ICI, 'axe_reference.json');
export const ETIQUETTES = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'];
export const GRAVES = new Set(['critical', 'serious']);
const LARGEUR = 1280;
const EN_PARALLELE = 4;

const IGNORES = new Set(['.git', 'node_modules', '_archive-anciennes-versions', '_outils', '_exports']);

function pages(depart, racine) {
  if (!fs.statSync(depart).isDirectory()) return [path.resolve(depart)];
  const out = [];
  (function marcher(dossier) {
    for (const entree of fs.readdirSync(dossier, { withFileTypes: true })) {
      const complet = path.join(dossier, entree.name);
      if (entree.isDirectory()) {
        if (entree.name.startsWith('.') || IGNORES.has(entree.name)) continue;
        marcher(complet);
      } else if (entree.name.toLowerCase().endsWith('.html')) out.push(complet);
    }
  })(depart);
  return out.sort((a, b) => path.relative(racine, a).localeCompare(path.relative(racine, b), 'fr'));
}

/* Rend le chemin de `axe.min.js`, ou null. `AXE_CORE` l'emporte ; sinon la
 * résolution ordinaire de Node, depuis ce dossier puis depuis le dossier courant. */
export function trouverAxe(force = process.env.AXE_CORE) {
  if (force) return fs.existsSync(force) && fs.statSync(force).isFile() ? force : null;
  for (const base of [import.meta.url, pathToFileURL(path.join(process.cwd(), 'x.js')).href]) {
    try { return createRequire(base).resolve('axe-core/axe.min.js'); } catch { /* on essaie la base suivante */ }
  }
  return null;
}

/* Les reculs : pour chaque (règle grave, page), des nœuds en plus de la référence. */
export function comparer(mesure, reference) {
  const reculs = [];
  for (const [regle, parPage] of Object.entries(mesure)) {
    for (const [page, noeuds] of Object.entries(parPage)) {
      const avant = (reference[regle] && reference[regle][page]) || 0;
      if (noeuds > avant) reculs.push({ regle, page, avant, noeuds });
    }
  }
  return reculs.sort((a, b) => a.page.localeCompare(b.page, 'fr') || a.regle.localeCompare(b.regle));
}

function totaux(parRegle) {
  return Object.entries(parRegle)
    .map(([regle, parPage]) => ({ regle, noeuds: Object.values(parPage).reduce((s, n) => s + n, 0), pages: Object.keys(parPage).length }))
    .sort((a, b) => b.noeuds - a.noeuds);
}

export async function main({ muet = false, cible = RACINE, racine = RACINE, json = null, ecrireReference = false,
  reference = REFERENCE, axe = undefined } = {}) {
  if (!fs.existsSync(cible)) {
    console.error(`❌ EN PANNE : « ${cible} » n'existe pas (règle d'or n°299).`);
    return 2;
  }
  const source = trouverAxe(axe === undefined ? process.env.AXE_CORE : axe);
  if (!source) {
    console.error('❌ EN PANNE : axe-core est introuvable (règle d\'or n°299). Installer le paquet (`npm install axe-core`, '
      + 'dans le dossier parent du dépôt) ou donner `AXE_CORE=/chemin/vers/axe.min.js`.');
    return 2;
  }
  let chromium;
  try { ({ chromium } = await import('playwright')); } catch {
    console.error('❌ EN PANNE : le paquet `playwright` est introuvable (règle d\'or n°299).');
    return 2;
  }
  const fichiers = pages(cible, racine);
  if (fichiers.length === 0) {
    console.error(`❌ EN PANNE : aucune page HTML sous « ${cible} » (règle d'or n°299).`);
    return 2;
  }
  const partiel = path.resolve(cible) !== path.resolve(racine);
  if (ecrireReference && partiel) {
    console.error('❌ La référence ne s\'écrit que sur tout le dépôt : une mesure partielle effacerait les autres pages.');
    return 2;
  }

  const code = fs.readFileSync(source, 'utf8');
  const graves = {};
  const legers = {};
  const impacts = {};
  const details = [];
  const pannes = [];
  const renvois = [];
  let version = null;

  const navigateur = await chromium.launch();
  try {
    const contexte = await navigateur.newContext({ viewport: { width: LARGEUR, height: 900 } });
    let prochain = 0;
    const ouvrier = async () => {
      const page = await contexte.newPage();
      for (;;) {
        const i = prochain++;
        if (i >= fichiers.length) break;
        const fichier = fichiers[i];
        const nom = path.relative(racine, fichier).split(path.sep).join('/');
        try {
          const adresse = pathToFileURL(fichier).href;
          await page.goto(adresse, { waitUntil: 'load', timeout: 45000 });
          await page.waitForTimeout(250);
          await page.waitForLoadState('load');
          if (page.url().split('#')[0].split('?')[0] !== adresse) { renvois.push(nom); continue; }
          await page.addScriptTag({ content: code });
          const resultat = await page.evaluate(async (etiquettes) => {
            const r = await window.axe.run(document, { runOnly: { type: 'tag', values: etiquettes }, resultTypes: ['violations'] });
            return { version: window.axe.version, violations: r.violations.map((v) => ({ id: v.id, impact: v.impact, aide: v.help, noeuds: v.nodes.map((n) => n.target.join(' ')) })) };
          }, ETIQUETTES);
          version = resultat.version;
          for (const violation of resultat.violations) {
            const sac = GRAVES.has(violation.impact) ? graves : legers;
            (sac[violation.id] ||= {})[nom] = violation.noeuds.length;
            impacts[violation.id] = violation.impact;
            details.push({ page: nom, regle: violation.id, impact: violation.impact, aide: violation.aide, noeuds: violation.noeuds });
          }
        } catch (erreur) {
          pannes.push({ page: nom, erreur: String(erreur && erreur.message ? erreur.message : erreur).split('\n')[0] });
        }
      }
      await page.close();
    };
    await Promise.all(Array.from({ length: Math.min(EN_PARALLELE, fichiers.length) }, ouvrier));
  } finally {
    await navigateur.close();
  }

  const mesurees = fichiers.length - pannes.length - renvois.length;
  if (mesurees === 0) {
    console.error(`❌ EN PANNE : aucune des ${fichiers.length} page(s) n'a pu être mesurée (règle d'or n°299).${pannes.length ? ` Première erreur : ${pannes[0].erreur}` : ' Toutes renvoient ailleurs.'}`);
    return 2;
  }
  if (json) fs.writeFileSync(json, JSON.stringify({ axe: version, etiquettes: ETIQUETTES, largeur: LARGEUR, pages: mesurees, pannes, renvois, details }, null, 2));

  if (ecrireReference) {
    if (pannes.length) {
      console.error(`❌ Référence NON écrite : ${pannes.length} page(s) n'ont pas pu être mesurée(s) (${pannes[0].page} : ${pannes[0].erreur}).`);
      return 2;
    }
    const tri = (objet) => Object.fromEntries(Object.keys(objet).sort().map((cle) => [cle, objet[cle]]));
    const propre = Object.fromEntries(Object.keys(graves).sort().map((regle) => [regle, tri(graves[regle])]));
    fs.writeFileSync(reference, JSON.stringify({
      _lire: 'Écrit par `node _outils/controle_axe.mjs --reference`. Ne pas modifier à la main. Nœuds en défaut par règle axe-core (impact critical ou serious) et par page.',
      axe: version, etiquettes: ETIQUETTES, largeur: LARGEUR, pages: mesurees, regles: propre,
    }, null, 1) + '\n');
    console.log(`✎ référence écrite : ${path.relative(racine, reference)} — ${mesurees} page(s), axe-core ${version}`);
    for (const t of totaux(graves)) console.log(`    ${t.regle} (${impacts[t.regle]}) : ${t.noeuds} nœud(s), ${t.pages} page(s)`);
    return 0;
  }

  let connue = {};
  let sansReference = false;
  if (fs.existsSync(reference)) {
    try { connue = JSON.parse(fs.readFileSync(reference, 'utf8')).regles || {}; } catch {
      console.error(`❌ EN PANNE : la référence « ${reference} » ne se lit pas (règle d'or n°299).`);
      return 2;
    }
  } else sansReference = true;

  const reculs = comparer(graves, connue);
  if (!muet) {
    console.log(`axe-core ${version} · ${mesurees} page(s) · ${LARGEUR} px · ${ETIQUETTES.join(', ')}`);
    console.log('\nDéfauts graves (critical, serious) — comparés à la référence :');
    const tg = totaux(graves);
    if (!tg.length) console.log('    aucun');
    for (const t of tg) console.log(`    ${t.regle} (${impacts[t.regle]}) : ${t.noeuds} nœud(s), ${t.pages} page(s)`);
    console.log('\nDéfauts de structure (moderate, minor) — mesurés, jamais refusés :');
    const tl = totaux(legers);
    if (!tl.length) console.log('    aucun');
    for (const t of tl) console.log(`    ${t.regle} (${impacts[t.regle]}) : ${t.noeuds} nœud(s), ${t.pages} page(s)`);
    console.log('');
  }
  if (sansReference) console.log('ℹ Pas de référence : tout défaut grave compte comme un recul. L\'écrire par `--reference`, sur tout le dépôt.');
  console.log('ℹ Non vu par cet outil : ce qui s\'ouvre au clic, le téléphone, et tout ce qu\'une machine ne juge pas (axe-core ne trouve qu\'une part des problèmes).');
  if (renvois.length) console.log(`ℹ ${renvois.length} page(s) de renvoi, non mesurée(s) (leur destination l'est) : ${renvois.join(', ')}`);
  for (const panne of pannes) console.log(`⚠ non mesurée : ${panne.page} — ${panne.erreur}`);

  if (reculs.length) {
    for (const recul of reculs) console.log(`✘ ${recul.page} — ${recul.regle} (${impacts[recul.regle]}) : ${recul.noeuds} nœud(s), ${recul.avant} dans la référence`);
    console.log(`✘ ${reculs.length} recul(s) sur ${mesurees} page(s). Le détail des nœuds : --json <fichier>.`);
    return 1;
  }
  if (pannes.length) {
    console.log(`❌ EN PANNE : ${pannes.length} page(s) sur ${fichiers.length} n'ont pas pu être mesurées (règle d'or n°299).`);
    return 2;
  }
  const reste = totaux(graves).reduce((s, t) => s + t.noeuds, 0);
  console.log(`✅ aucune page ne porte plus de défauts graves que la référence (${mesurees} page(s) ; ${reste} nœud(s) connus restent à corriger).`);
  return 0;
}

export function lanceDirectement(url, argv1) {
  return Boolean(argv1) && url === pathToFileURL(path.resolve(argv1)).href;
}

if (lanceDirectement(import.meta.url, process.argv[1])) {
  const args = process.argv.slice(2);
  const iJson = args.indexOf('--json');
  const libres = args.filter((a, i) => !a.startsWith('--') && !(iJson >= 0 && i === iJson + 1));
  process.exit(await main({
    muet: args.includes('--muet'),
    ecrireReference: args.includes('--reference'),
    json: iJson >= 0 ? args[iJson + 1] : null,
    cible: libres[0] ? path.resolve(libres[0]) : RACINE,
  }));
}
