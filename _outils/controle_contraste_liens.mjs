/* controle_contraste_liens.mjs — un lien se lit.
 *
 * LE CONSTAT QUI A DONNÉ CE CONTRÔLE
 * ----------------------------------
 * Dans le Bonus de `4e_C1.4`, la première activité proposée à l'élève est un
 * lien : « l'atelier double authentification ». Ce lien était affiché en
 * `rgb(0,0,238)` — le bleu que le navigateur met par défaut quand la page ne
 * dit rien — sur un fond bleu nuit `rgb(16,41,79)`. Contraste : **1,54**, là où
 * le minimum lisible est 4,5. Le lien était là, la page était « verte », et
 * l'activité était invisible.
 *
 * Aucun contrôle ne le voyait : `controle_impression.mjs` ne juge que le PAPIER.
 * Un texte peut donc être parfaitement imprimable et illisible à l'écran.
 *
 * CE QUE CET OUTIL MESURE
 * -----------------------
 * Il ouvre chaque page dans un vrai navigateur, à 1280 px, et pour chaque lien
 * VISIBLE porteur de texte il calcule le rapport de contraste entre la couleur
 * calculée du texte et LE FOND RÉEL — celui que les couches d'ancêtres
 * composent, pas celui qu'on croit. Il refuse sous 4,5:1 (WCAG 2.1, AA).
 *
 * Il le fait DEUX FOIS : en `media: screen`, puis en `media: print`. Un bleu
 * clair parfaitement lisible sur fond marine tombe vers 1,6:1 sur papier blanc,
 * et l'inverse est vrai aussi. La règle vaut des deux côtés, la mesure aussi.
 *
 * CE QU'IL NE MESURE PAS, ET LE DIT
 * ---------------------------------
 *   · L'ÉTAT VISITÉ. Les navigateurs mentent délibérément sur `:visited` :
 *     `getComputedStyle` rend la couleur de l'état non visité, quoi qu'il
 *     arrive. C'est une protection de la vie privée, et elle est juste. L'état
 *     visité ne peut donc PAS être mesuré ici. Il est exigé par la SOURCE :
 *     toute page qui donne une couleur à `a` doit en donner une à `a:visited`,
 *     sinon le lien redevient violet après le premier clic — tout aussi
 *     illisible sur fond sombre. C'est le second grief de cet outil.
 *   · Le reste du PAPIER : cet outil ne juge que les LIENS. Le texte courant,
 *     les encadrés, les tableaux restent l'affaire de `controle_impression.mjs`,
 *     qui refuse une chose et une seule — du texte sombre sur un fond sombre.
 *     Un lien pâle sur du blanc lui échappait, et c'est ce trou qu'on ferme ici.
 *   · Un fond en IMAGE ou en dégradé : le rapport n'a alors pas de valeur
 *     unique. Ces liens sont comptés à part et signalés, jamais silencieux.
 *   · La NAVIGATION (`nav`, `#navharm`, les onglets de séance) : elle a ses
 *     propres règles de contraste et son propre gabarit.
 *   · Les thèmes de couleur : mesuré, aucune page du dépôt ne déclare
 *     `prefers-color-scheme` ni ne propose de bascule. Une seule apparence à
 *     mesurer, donc. Le jour où une page en proposera, il faudra mesurer les
 *     deux — ce contrôle ne le fera pas tout seul.
 *
 * Usage :
 *   node _outils/controle_contraste_liens.mjs           # rapport complet
 *   node _outils/controle_contraste_liens.mjs --muet    # synthèse seule
 *   node _outils/controle_contraste_liens.mjs <chemin>  # une page, ou un dossier
 *
 * Sortie : 0 tout se lit · 1 au moins un lien sous le seuil · 2 EN PANNE,
 * rien n'a pu être mesuré (règle d'or n°299).
 */
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const RACINE = path.resolve(ICI, '..');

/** Le minimum lisible pour du texte normal — WCAG 2.1, niveau AA. */
export const SEUIL = 4.5;

const IGNORES = new Set(['.git', 'node_modules', '_archive-anciennes-versions', '_outils']);

function pages(depart) {
  const out = [];
  (function marcher(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      if (e.isDirectory()) {
        if (IGNORES.has(e.name) || e.name.startsWith('.')) continue;
        marcher(path.join(d, e.name));
      } else if (e.name.toLowerCase().endsWith('.html')) {
        out.push(path.join(d, e.name));
      }
    }
  })(fs.statSync(depart).isDirectory() ? depart : path.dirname(depart));
  if (!fs.statSync(depart).isDirectory()) return [path.resolve(depart)];
  return out.sort();
}

/* ── la mesure, faite DANS la page ─────────────────────────────────────────
   On n'interprète pas la feuille de style : on demande au navigateur ce qu'il
   a calculé, et on remonte les ancêtres jusqu'au premier fond opaque. C'est la
   seule façon d'obtenir « le fond réel » et non « le fond supposé ». */
const MESURE = () => {
  const nombres = (c) => (c.match(/[\d.]+/g) || []).map(Number);
  const lum = (c) => {
    const [r, g, b] = nombres(c).slice(0, 3).map((v) => {
      v /= 255;
      return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * r + 0.7152 * g + 0.0722 * b;
  };
  const alpha = (c) => { const n = nombres(c); return n.length > 3 ? n[3] : 1; };

  /* Le fond réel se COMPOSE : s'arrêter au premier `background-color` non nul
     donne des résultats faux dès qu'un voile translucide est posé par-dessus.
     Mesuré : un `rgba(155,190,252,0.06)` pris pour le fond donnait 1,16:1 là où
     le vrai rapport dépasse 7 — cinq séquences accusées à tort. On empile donc
     les couches jusqu'à l'opacité, puis sur blanc si rien ne l'atteint. */
  const composer = (dessus, dessous) => {
    const a = alpha(dessus), h = nombres(dessus), b = nombres(dessous);
    return `rgb(${[0, 1, 2].map((i) => Math.round(h[i] * a + b[i] * (1 - a))).join(', ')})`;
  };

  const fondReel = (e) => {
    let image = false;
    const couches = [];
    for (let n = e; n; n = n.parentElement) {
      const cs = getComputedStyle(n);
      if (cs.backgroundImage && cs.backgroundImage !== 'none') image = true;
      const a = alpha(cs.backgroundColor);
      if (a > 0) couches.push(cs.backgroundColor);
      if (a >= 1) break;
    }
    let fond = 'rgb(255, 255, 255)';                      // le papier du navigateur
    for (let i = couches.length - 1; i >= 0; i--) fond = composer(couches[i], fond);
    return { fond, image };
  };

  const dansNavigation = (e) => !!e.closest('nav, #navharm, [role="navigation"], .seance-tab, .tabs, .fil');
  const visible = (e) => {
    const r = e.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) return false;
    const cs = getComputedStyle(e);
    return cs.visibility !== 'hidden' && cs.display !== 'none' && Number(cs.opacity) > 0.05;
  };

  /* on déplie tout : un lien replié est un lien qu'on lira quand même */
  for (const d of document.querySelectorAll('details')) d.open = true;
  for (const s of document.querySelectorAll('.seance-panel')) {
    s.classList.add('active');
    s.style.display = 'block';
  }

  const liens = [];
  for (const a of document.querySelectorAll('a')) {
    const texte = (a.textContent || '').replace(/\s+/g, ' ').trim();
    if (!texte) continue;                      // une image cliquable n'a pas de couleur de texte
    if (dansNavigation(a)) continue;
    if (!visible(a)) continue;
    const cs = getComputedStyle(a);
    const { fond, image } = fondReel(a);
    const L1 = lum(cs.color);
    const L2 = lum(fond);
    const ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
    liens.push({
      texte: texte.slice(0, 46), couleur: cs.color, fond, image,
      ratio: Math.round(ratio * 100) / 100,
      defaut: /^rgb\(0,\s*0,\s*238\)$/.test(cs.color),
    });
  }

  /* Second grief, lu dans la SOURCE et non dans le rendu : une page qui colore
     `a` sans colorer `a:visited` laisse le violet par défaut revenir après le
     premier clic. `:visited` ne se mesure pas (voir l'en-tête) ; il s'impose. */
  let colore = false, visite = false;
  for (const f of document.styleSheets) {
    let regles;
    try { regles = f.cssRules; } catch (e) { continue; }
    for (const r of regles || []) {
      const s = r.selectorText;
      if (!s || !r.style || !r.style.color) continue;
      if (/(^|,)\s*a(?![\w-])(?!.*:visited)/.test(s)) colore = true;
      if (/a:visited/.test(s)) visite = true;
    }
  }
  /* un style en ligne compte aussi comme « la page colore ses liens » */
  if ([...document.querySelectorAll('a[style*="color"]')].length) colore = true;

  return { liens, colore, visite };
};

/* ── le rapport ────────────────────────────────────────────────────────────── */
export async function main(muet = false, cible = RACINE) {
const liste = pages(path.resolve(cible));

const nav = await chromium.launch();
const ctx = await nav.newContext({ viewport: { width: 1280, height: 900 } });
const page = await ctx.newPage();

let luesOk = 0, totalLiens = 0, surImage = 0;
const fautifs = [];      // { page, liens sous le seuil, à l'écran }
const fautifsPapier = []; // { page, liens sous le seuil, sur le papier }
const sansVisite = [];   // pages qui colorent `a` et pas `a:visited`
const erreurs = [];

for (const f of liste) {
  let r, rp;
  try {
    await page.emulateMedia({ media: 'screen' });
    await page.goto(pathToFileURL(f).href, { waitUntil: 'load', timeout: 45000 });
    await page.waitForTimeout(120);
    r = await page.evaluate(MESURE);
    /* Le PAPIER, dans la même page : un bleu clair parfaitement lisible à
       l'écran tombe vers 1,6:1 sur blanc. Les deux se mesurent, parce que la
       règle vaut des deux côtés.

       LES TRANSITIONS MENTENT. Changer de média déclenche les `transition` des
       boutons, et `getComputedStyle` rend alors une couleur INTERMÉDIAIRE : un
       `.btn` mesuré à `rgb(108,136,199)` valait en réalité `rgb(0,48,158)` une
       fois la transition finie — un faux coupable, trouvé en relançant la
       mesure autrement. On les coupe avant de mesurer. */
    await page.addStyleTag({ content:
      '*,*::before,*::after{transition:none!important;animation:none!important}' });
    await page.emulateMedia({ media: 'print' });
    await page.waitForTimeout(250);
    rp = await page.evaluate(MESURE);
  } catch (e) {
    erreurs.push([path.relative(RACINE, f), String(e).slice(0, 90)]);
    continue;
  }
  luesOk += 1;
  totalLiens += r.liens.length;
  surImage += r.liens.filter((l) => l.image).length;
  const sous = r.liens.filter((l) => !l.image && l.ratio < SEUIL);
  if (sous.length) fautifs.push({ page: path.relative(RACINE, f), liens: sous });
  const sousP = rp.liens.filter((l) => !l.image && l.ratio < SEUIL);
  if (sousP.length) fautifsPapier.push({ page: path.relative(RACINE, f), liens: sousP });
  if (r.colore && !r.visite) sansVisite.push(path.relative(RACINE, f));
}
await nav.close();

/* Règle d'or n°299 : un contrôle qui n'a rien pu lire n'est pas vert, il est
   en panne — et il le dit sur la sortie d'erreur, avec le code 2. */
if (!luesOk || !totalLiens) {
  console.error('⛔ EN PANNE — aucun lien n\'a pu être mesuré : '
    + `${liste.length} page(s) listée(s), ${luesOk} ouverte(s), ${totalLiens} lien(s) lu(s).`);
  return 2;
}

const nFautifs = fautifs.reduce((n, p) => n + p.liens.length, 0);
const nPapier = fautifsPapier.reduce((n, p) => n + p.liens.length, 0);

const detailler = (titre, liste) => {
  if (muet || !liste.length) return;
  console.log(`═══ ${titre} ═══\n`);
  for (const p of liste) {
    console.log(`  ${p.page}`);
    for (const l of p.liens) {
      console.log(`     ${String(l.ratio).padStart(5)} : 1   ${l.couleur} sur ${l.fond}`
        + `${l.defaut ? '   [bleu par défaut du navigateur]' : ''}`);
      console.log(`             « ${l.texte} »`);
    }
    console.log('');
  }
};
detailler('LES LIENS QUI NE SE LISENT PAS — À L\'ÉCRAN', fautifs);
detailler('LES LIENS QUI NE SE LISENT PAS — SUR LE PAPIER', fautifsPapier);

if (!muet && sansVisite.length) {
  console.log('═══ PAGES QUI COLORENT `a` SANS COLORER `a:visited` ═══');
  console.log('  Après le premier clic, le navigateur y remet son violet par défaut.');
  console.log('  L\'état visité ne se MESURE pas (protection de la vie privée) : il s\'impose.\n');
  for (const p of sansVisite) console.log(`     ${p}`);
  console.log('');
}

console.log(`${luesOk} page(s) lue(s) · ${totalLiens} lien(s) hors navigation · seuil ${SEUIL}:1`);
console.log(`  sous le seuil À L'ÉCRAN   : ${nFautifs} lien(s) sur ${fautifs.length} page(s)`);
console.log(`  sous le seuil SUR PAPIER  : ${nPapier} lien(s) sur ${fautifsPapier.length} page(s)`);
console.log(`  colorent \`a\` sans \`a:visited\` : ${sansVisite.length} page(s)`);
console.log(`  sur un fond en image ou en dégradé, non jugés : ${surImage}`);
if (erreurs.length) {
  console.log(`  ⛔ ${erreurs.length} page(s) n'ont pas pu être ouvertes :`);
  for (const [p, e] of erreurs.slice(0, 5)) console.log(`     ${p} — ${e}`);
}
console.log('');
console.log('  NON LU : l\'état visité (le navigateur ne le révèle pas — il est exigé par');
console.log('  la source), la navigation, et les fonds en image ou en dégradé.');

if (nFautifs || nPapier || sansVisite.length) {
  console.log('');
  console.log('⛔ Un lien qu\'on ne peut pas lire n\'est pas un lien. Règle d\'or n°303.');
  return 1;
}
console.log('');
console.log('✅ chaque lien de chaque page se lit sur son fond réel');
return 0;
}

/* LA GARDE DE LANCEMENT — deux CHEMINS RÉELS, jamais deux chaînes.
 *
 * `import.meta.url === \`file://${process.argv[1]}\`` est vrai sous Linux et
 * FAUX sous Windows : trois barres contre deux, « / » contre « \\ », « %7E »
 * contre « ~ ». Le contrôle ne partait alors pas, n'écrivait rien, et sortait à
 * 0 — c'est ce qui a rendu `controle_impression.mjs` muet trois semaines.
 * Exportée pour que le banc l'interroge dans les deux sens sans rien lancer. */
export function lanceDirectement(url, argv1) {
  if (!argv1) return false;
  return path.resolve(fileURLToPath(url)) === path.resolve(argv1);
}

if (lanceDirectement(import.meta.url, process.argv[1])) {
  const args = process.argv.slice(2);
  const ou = args.find((a) => !a.startsWith('--'));
  process.exit(await main(args.includes('--muet'), ou ? path.resolve(ou) : RACINE));
}
