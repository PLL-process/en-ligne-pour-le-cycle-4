/**
 * controle_hors_ligne.mjs — règle d'or n°305 : UNE PAGE SE LIT SANS INTERNET.
 *
 * Première étape du « kit hors ligne » : Pascal emporte le dépôt sur une clé ou
 * le réseau du collège, là où la connexion manque. Une page qui va chercher une
 * police, un script ou une image sur le réseau s'y affiche mal ou pas du tout —
 * et rien ne le dit à l'élève.
 *
 * CE QUE LA RÈGLE DEMANDE
 * -----------------------
 *   1. Aucune page vivante ne CHARGE quoi que ce soit depuis le réseau pour
 *      s'afficher ou fonctionner.
 *   2. Un LIEN sortant (<a href>) reste permis : une source à consulter n'est
 *      pas une dépendance.
 *   3. Une ACTIVITÉ qui ne se fait pas sans un outil en ligne le dit à son
 *      début : un élément de classe `activite-en-ligne`, « 🌐 Cette activité
 *      demande une connexion Internet », avec le repli hors ligne s'il existe.
 *   4. L'archive est exclue : c'est une trace.
 *
 * DEUX MÉTHODES, ET ELLES SONT CONFRONTÉES
 * ----------------------------------------
 *   a. LA SOURCE. Chaque mécanisme de chargement est cherché là où il agit :
 *      attributs des balises (src, srcset, poster, data, <link rel=…>, <base>),
 *      CSS des blocs <style> et des attributs style (url(), @import), code des
 *      blocs <script> (fetch, XMLHttpRequest, import(), new Image().src,
 *      WebSocket, EventSource, Worker, sendBeacon, et le HTML écrit en chaîne).
 *      Les lire PARTOUT serait faux : 3e_C1.5 enseigne HTTP/HTTPS et affiche
 *      du code Python qui contient « https:// » — un exemple n'est pas un
 *      chargement.
 *   b. LE NAVIGATEUR, RÉSEAU COUPÉ. Chromium ouvre la page ; toute requête qui
 *      n'est pas un fichier local (file:, data:, blob:) est BLOQUÉE et notée.
 *      On fait défiler jusqu'en bas, on ouvre chaque onglet de séance (les
 *      boutons, pas les liens vers une autre page) et chaque repli <details>.
 *      C'est la méthode qui voit ce que la source cache : une adresse
 *      construite en JavaScript.
 *   Une page est refusée si l'UNE des deux méthodes trouve un chargement. Le
 *   rapport dit laquelle : un écart entre les deux est une information.
 *
 * LA MENTION 🌐 (point 3), jugée dans le navigateur
 * -------------------------------------------------
 * Un lien vers un OUTIL en ligne (éditeur, compilateur, CAO : voir OUTILS) est
 * accepté si un bloc qui le contient — section, article, .activite — porte un
 * `.activite-en-ligne` parmi ses QUATRE premiers enfants, avant le lien. Un
 * lien vers une VIDÉO (voir MEDIAS) est une source s'il est dans une
 * `.ressource` qui porte son `.ressource-repli` (« Si la vidéo ne s'ouvre
 * pas ») ; sinon il est jugé comme un outil. Tout lien peut être déclaré
 * source par `data-hors-ligne="source"`, sur lui ou un ancêtre.
 *
 * CE QUE CE CONTRÔLE NE VOIT PAS — et ne prétend pas voir
 * -------------------------------------------------------
 *   · une activité qui exige un outil en ligne SANS LE LIER : « va sur
 *     Onshape », « dans mBlock » écrits en texte. Les quatre TP Onshape portent
 *     la mention à la main ; les autres cas se jugent en lisant ;
 *   · un domaine d'outil absent de OUTILS : la liste est fermée, elle ne
 *     devine pas qu'un site inconnu est un éditeur ;
 *   · une requête déclenchée par un GESTE autre qu'un onglet de séance ou un
 *     repli (un bouton « Vérifier », une saisie) ;
 *   · la PERTINENCE du repli : qu'il permette réellement de faire l'activité
 *     se juge ; ce contrôle vérifie seulement que la mention existe, et où ;
 *   · les fichiers autres que .html (un .svg, un .pdf téléchargé).
 *
 * Usage :
 *     node _outils/controle_hors_ligne.mjs            # rapport complet
 *     node _outils/controle_hors_ligne.mjs --muet     # seulement les refus
 *     node _outils/controle_hors_ligne.mjs --source   # méthode a seule (rapide)
 *     node _outils/controle_hors_ligne.mjs <chemin>   # une page, ou un dossier
 * Sortie : 0  aucune page ne dépend du réseau ; 1  au moins une ;
 *          2  le contrôle n'a rien pu vérifier — en panne, et surtout pas vert.
 */

import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath, pathToFileURL } from 'url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
export const DEPOT = path.dirname(ICI);
const IGNORES = new Set(['.git', 'node_modules', '_archive-anciennes-versions']);
/* Les moules de `_outils/` sont lus : ils FABRIQUENT des pages élèves (même
   raisonnement que controle_contraste_liens.mjs). Le reste de `_outils/` non. */
const MOULES = ['dnb_gabarit.html', 'gabarits'];

/** Domaines d'OUTILS : sans eux, l'activité qui les demande ne se fait pas. */
export const OUTILS = [
  'vittascience.com', 'online-python.com', 'online-python-compiler.com', 'programiz.com',
  'onshape.com', 'tinkercad.com', 'scratch.mit.edu', 'makecode.microbit.org', 'makecode.com',
  'wokwi.com', 'replit.com', 'trinket.io', 'capytale2.ac-paris.fr', 'mblock.cc', 'python.org',
  'basthon.fr', 'jupyter.org', 'codepen.io', 'jsfiddle.net', 'geogebra.org', 'phet.colorado.edu',
];
/** Domaines de MÉDIAS : une source, si l'activité sait s'en passer. */
export const MEDIAS = ['youtube.com', 'youtu.be', 'vimeo.com', 'dailymotion.com', 'lumni.fr'];

export function pages(depart) {
  const abs = path.resolve(depart);
  if (!fs.statSync(abs).isDirectory()) return [abs];
  const out = [];
  (function marcher(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const complet = path.join(d, e.name);
      const rel = path.relative(DEPOT, complet).split(path.sep).join('/');
      if (e.isDirectory()) {
        if (e.name.startsWith('.') || IGNORES.has(e.name)) continue;
        if (rel.startsWith('_outils') && rel !== '_outils' && !MOULES.some((m) => rel.includes(m))) continue;
        marcher(complet);
      } else if (e.name.toLowerCase().endsWith('.html')) {
        if (rel.startsWith('_outils/') && !MOULES.some((m) => rel.includes(m))) continue;
        out.push(complet);
      }
    }
  })(abs);
  return out.sort();
}

// ── Méthode a : la source ────────────────────────────────────────────────
const DISTANT = /^\s*(?:(?:https?|wss?):)?\/\//i;
const LIENS_CHARGES = /\b(?:stylesheet|icon|apple-touch-icon|mask-icon|preload|prefetch|modulepreload|preconnect|dns-prefetch|manifest|import)\b/i;
const CSS_DISTANT = [
  [/@import\s+(?:url\(\s*)?["']?\s*(?:(?:https?:)?\/\/)[^"')\s;]*/gi, '@import distant'],
  [/url\(\s*["']?\s*(?:https?:)?\/\/[^"')\s]*/gi, 'url() distant'],
];
const JS_DISTANT = [
  [/\bfetch\s*\(\s*[`'"](?:https?:)?\/\/[^`'"]*/g, 'fetch()'],
  [/\.open\s*\(\s*[`'"][A-Za-z]+[`'"]\s*,\s*[`'"](?:https?:)?\/\/[^`'"]*/g, 'XMLHttpRequest.open()'],
  [/\bimport\s*\(\s*[`'"](?:https?:)?\/\/[^`'"]*/g, 'import()'],
  [/\bimport\b[^;'"`]*?\bfrom\s*[`'"](?:https?:)?\/\/[^`'"]*/g, 'import … from'],
  [/\bnew\s+(?:WebSocket|EventSource|Worker|SharedWorker)\s*\(\s*[`'"](?:(?:wss?|https?):)?\/\/[^`'"]*/g, 'WebSocket / EventSource / Worker'],
  [/\.(?:src|srcset|poster|data)\s*=\s*[`'"](?:https?:)?\/\/[^`'"]*/g, '.src = (new Image() …)'],
  [/\bsendBeacon\s*\(\s*[`'"](?:https?:)?\/\/[^`'"]*/g, 'sendBeacon()'],
  [/\bsetAttribute\s*\(\s*[`'"](?:src|srcset|poster|data)[`'"]\s*,\s*[`'"](?:https?:)?\/\/[^`'"]*/g, 'setAttribute(src)'],
  [/\b(?:src|srcset|poster)\s*=\s*\\?["'](?:https?:)?\/\/[^"'\\]*/g, 'HTML écrit en chaîne (src=)'],
  [/url\(\s*\\?["']?\s*(?:https?:)?\/\/[^"')\\\s]*/g, 'CSS écrit en chaîne (url())'],
];

function attributs(balise) {
  const out = {};
  for (const m of balise.matchAll(/([a-zA-Z_:][-a-zA-Z0-9_:.]*)\s*(?:=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'>]+)))?/g))
    out[m[1].toLowerCase()] = m[2] ?? m[3] ?? m[4] ?? '';
  return out;
}

/** Tous les chargements distants que la SOURCE annonce. Exporté pour le banc. */
export function chargementsDansLaSource(src) {
  const trouves = [];
  const sansCommentaires = src.replace(/<!--[\s\S]*?-->/g, ' ');
  const scripts = [], styles = [];
  const balisage = sansCommentaires
    .replace(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi, (t, att, corps) => { scripts.push(corps); return `<script${att}></script>`; })
    .replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (t, corps) => { styles.push(corps); return ' '; });
  // Les contenus de <textarea> et les exemples <pre>/<code> sont du TEXTE : leurs
  // balises y sont échappées (&lt;), donc invisibles ici — c'est voulu.
  for (const m of balisage.matchAll(/<([a-zA-Z][a-zA-Z0-9-]*)\b([^>]*)>/g)) {
    const tag = m[1].toLowerCase(), a = attributs(m[2]);
    const note = (quoi, url) => trouves.push({ quoi, url: url.trim().slice(0, 90) });
    if (tag === 'a' || tag === 'area' || tag === 'form') continue;   // naviguer n'est pas charger
    for (const k of ['src', 'poster', 'data', 'background', 'lowsrc'])
      if (a[k] && DISTANT.test(a[k])) note(`<${tag} ${k}>`, a[k]);
    for (const k of ['srcset', 'imagesrcset'])
      if (a[k]) for (const u of a[k].split(',')) if (DISTANT.test(u)) note(`<${tag} ${k}>`, u);
    if (tag === 'link' && a.href && DISTANT.test(a.href) && LIENS_CHARGES.test(a.rel || '')) note(`<link rel=${a.rel}>`, a.href);
    if (tag === 'base' && a.href && DISTANT.test(a.href)) note('<base href>', a.href);
    if (a.style) for (const [re, quoi] of CSS_DISTANT) for (const x of a.style.matchAll(re)) note(`style="" ${quoi}`, x[0]);
  }
  for (const css of styles) for (const [re, quoi] of CSS_DISTANT) for (const x of css.matchAll(re)) trouves.push({ quoi: `<style> ${quoi}`, url: x[0].slice(0, 90) });
  for (const js of scripts) {
    const code = js.replace(/\/\*[\s\S]*?\*\//g, ' ').replace(/(^|[^:\\'"`])\/\/[^\n]*/g, '$1');
    for (const [re, quoi] of JS_DISTANT) for (const x of code.matchAll(re)) trouves.push({ quoi: `<script> ${quoi}`, url: x[0].slice(0, 90) });
  }
  return trouves;
}

// ── Méthode b : le navigateur, réseau coupé ──────────────────────────────
const LOCAL = /^(?:file|data|blob|about|chrome-error|devtools):/i;

/** Ouvre une page réseau coupé ; rend les requêtes tentées et le verdict des liens d'outils. */
export async function mesurerNavigateur(ctx, url) {
  const p = await ctx.newPage();
  const tentees = [], erreurs = [];
  p.on('websocket', (w) => tentees.push({ quoi: 'WebSocket', url: w.url() }));
  p.on('pageerror', (e) => erreurs.push(String(e.message || e).slice(0, 120)));
  p.on('dialog', (d) => d.dismiss().catch(() => {}));
  await p.route('**/*', (r) => {
    const u = r.request().url();
    if (LOCAL.test(u)) return r.continue();
    tentees.push({ quoi: r.request().resourceType(), url: u.slice(0, 120) });
    return r.abort('internetdisconnected');
  });
  await p.goto(url, { waitUntil: 'load', timeout: 30000 });
  await p.waitForTimeout(150);
  // défiler (images paresseuses), ouvrir les replis, puis chaque onglet de séance
  await p.evaluate(async () => {
    const pas = Math.max(400, innerHeight);
    for (let y = 0; y < document.documentElement.scrollHeight; y += pas) { scrollTo(0, y); await new Promise((f) => setTimeout(f, 15)); }
    document.querySelectorAll('details').forEach((d) => { d.open = true; });
  });
  const onglets = await p.$$('button.seance-tab, [role="tab"]:not(a)');
  for (const o of onglets) { try { await o.click({ timeout: 1500 }); await p.waitForTimeout(60); } catch { /* onglet caché : ignoré */ } }
  await p.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await p.waitForTimeout(150);
  const liens = await p.evaluate(({ OUTILS, MEDIAS }) => {
    const dom = (h) => { try { return new URL(h).hostname.replace(/^www\./, ''); } catch { return ''; } };
    const dans = (h, liste) => liste.some((d) => h === d || h.endsWith('.' + d));
    const aMention = (a) => {
      for (let e = a.parentElement; e; e = e.parentElement) {
        if (!e.matches('section, article, .activite, main, body')) continue;
        // la mention elle-même, ou posée dans un ENCADRÉ (jamais dans un bloc
        // d'activité : la section entière n'est pas « le début » de body — le
        // banc l'a montré, la mention placée après le lien passait par là)
        const m = [...e.children].slice(0, 4).map((c) => c.matches('.activite-en-ligne') ? c
          : c.matches('section, article, .activite, main') ? null
          : c.querySelector(':scope > .activite-en-ligne')).find(Boolean);
        if (m && !m.contains(a) && (m.compareDocumentPosition(a) & Node.DOCUMENT_POSITION_FOLLOWING)) return true;
      }
      return false;
    };
    return [...document.querySelectorAll('a[href]')].map((a) => {
      const h = dom(a.href);
      const outil = dans(h, OUTILS), media = dans(h, MEDIAS);
      if (!outil && !media) return null;
      const declareSource = !!a.closest('[data-hors-ligne="source"]');
      const repliVideo = media && !!a.closest('.ressource')?.querySelector('.ressource-repli');
      const ok = declareSource || repliVideo || aMention(a);
      const pourquoi = declareSource ? 'déclaré source' : repliVideo ? 'vidéo avec repli' : ok ? 'mention 🌐' : '';
      return { href: a.getAttribute('href').slice(0, 80), outil, ok, pourquoi };
    }).filter(Boolean);
  }, { OUTILS, MEDIAS });
  const mentions = await p.$$eval('.activite-en-ligne', (l) => l.length);
  await p.close();
  return { tentees, liens, mentions, erreurs };
}

export async function main(argv = [], racine = DEPOT) {
  const muet = argv.includes('--muet'), sourceSeule = argv.includes('--source');
  const cible = argv.find((a) => !a.startsWith('--'));
  let liste;
  try { liste = pages(cible ? path.resolve(cible) : racine); }
  catch (e) {
    console.error(`⛔ EN PANNE : impossible de parcourir ${cible || racine}\n     ${String(e).slice(0, 100)}`
      + `\n     Le contrôle n'a rien vérifié. Ce n'est pas un succès.`);
    return 2;
  }
  if (!liste.length) {
    console.error(`⛔ EN PANNE : aucun fichier .html sous ${cible || racine}\n     Le contrôle n'a rien vérifié. Ce n'est pas un succès.`);
    return 2;
  }
  const nav = sourceSeule ? null : await chromium.launch();
  const ctx = nav ? await nav.newContext({ viewport: { width: 1280, height: 900 }, serviceWorkers: 'block' }) : null;
  const refus = [];
  let parSource = 0, parNavigateur = 0, parMention = 0, ouvertes = 0, nMentions = 0, nLiensOutils = 0;
  const pagesMention = [];
  for (const abs of liste) {
    const rel = path.relative(DEPOT, abs).split(path.sep).join('/');
    const a = chargementsDansLaSource(fs.readFileSync(abs, 'utf8'));
    let b = null;
    if (ctx) {
      try { b = await mesurerNavigateur(ctx, pathToFileURL(abs).href); ouvertes++; }
      catch (e) { refus.push({ rel, motifs: [`page illisible dans le navigateur — ${String(e).slice(0, 80)}`] }); continue; }
    }
    const motifs = [];
    if (a.length) { parSource++; for (const x of a.slice(0, 3)) motifs.push(`source : ${x.quoi} → ${x.url}`); }
    if (b?.tentees.length) { parNavigateur++; for (const x of b.tentees.slice(0, 3)) motifs.push(`navigateur : requête ${x.quoi} → ${x.url}`); }
    if (b) {
      nMentions += b.mentions; nLiensOutils += b.liens.length;
      if (b.mentions) pagesMention.push(rel);
      const sans = b.liens.filter((l) => !l.ok);
      if (sans.length) { parMention++; for (const l of sans.slice(0, 3)) motifs.push(`lien vers un ${l.outil ? 'outil' : 'média sans repli'} sans mention 🌐 au début de l'activité → ${l.href}`); }
    }
    if (motifs.length) refus.push({ rel, motifs });
  }
  if (nav) await nav.close();
  if (ctx && !ouvertes) {
    console.error(`⛔ EN PANNE : ${liste.length} fichier(s), aucune page ouverte dans le navigateur.\n     Le contrôle n'a rien vérifié. Ce n'est pas un succès.`);
    return 2;
  }

  if (!muet) {
    console.log(`${liste.length} page(s) lue(s) · méthode a (source) : ${parSource} page(s) chargent du réseau`
      + (ctx ? ` · méthode b (navigateur, réseau coupé) : ${parNavigateur} page(s) tentent une requête` : ' · méthode b NON LANCÉE (--source)'));
    if (ctx) {
      console.log(`     ${nLiensOutils} lien(s) vers un outil ou une vidéo · ${parMention} page(s) sans la mention 🌐 attendue`
        + ` · ${nMentions} mention(s) « activite-en-ligne » sur ${pagesMention.length} page(s)`);
      if (parSource !== parNavigateur)
        console.log(`     ⚠ les deux méthodes divergent (${parSource} contre ${parNavigateur}) : voir les motifs, chacun dit qui l'a vu.`);
    }
    console.log(`\n     NON VU : une activité qui exige un outil en ligne sans le lier (texte seul) ;`
      + `\n     un domaine d'outil absent de la liste OUTILS ; une requête déclenchée par un geste autre`
      + `\n     qu'un onglet de séance ou un repli ; la pertinence du repli ; les fichiers non HTML.`);
  }
  if (refus.length) {
    console.log(`\n⛔ ${refus.length} page(s) ne se lisent pas sans Internet :`);
    for (const r of refus.slice(0, 25)) { console.log(`  ${r.rel}`); for (const m of r.motifs) console.log(`     ${m}`); }
    if (refus.length > 25) console.log(`  … et ${refus.length - 25} de plus`);
    return 1;
  }
  console.log(ctx
    ? `\n✅ aucune page ne dépend du réseau pour s'afficher, et chaque activité en ligne le dit`
    : `\n✅ la source n'annonce aucun chargement réseau — la mention 🌐 et les adresses construites\n   en JavaScript n'ont PAS été vérifiées : relancer sans --source`);
  return 0;
}

export function lanceDirectement(url, argv1) {
  if (!argv1) return false;
  return path.resolve(fileURLToPath(url)) === path.resolve(argv1);
}

if (lanceDirectement(import.meta.url, process.argv[1])) {
  process.exit(await main(process.argv.slice(2)));
}
