#!/usr/bin/env node
/**
 * controle_contexte_fenetre.mjs — règle d'or n°375 (28/11/2026) : une question se lit avec son contexte, dans la
 * même fenêtre.
 *
 * Le motif (Pascal, 28/11/2026, TP « Algorigrammes de domotique », Bonus) : « Après quelques jours, quand je regarde
 * les questions, je ne me souviens plus du contexte. Pourquoi ? Parce que ce n'est pas dans la même fenêtre. » Le cas
 * (le store, 800 lux, 50 km/h) était écrit en haut de la carte ; la question ① arrivait huit lignes plus bas, et le
 * bandeau collant du TP (titre, mission, sept boutons) recouvrait le haut de l'écran. Dans la fenêtre restante : la
 * question, sans ce dont dépend sa réponse.
 *
 * CE QUI EST MESURÉ, pour chaque question visible (la légende d'un groupe de choix, l'étiquette d'un champ) :
 *   la hauteur entre le début de son contexte et le bas de la question (sa légende ; pour une étiquette, son champ),
 *   comparée à la place que laisse la
 *   fenêtre une fois le bandeau collant déduit. Le début du contexte, c'est le plus proche, en remontant la page :
 *   un rappel du cas (`.rappel-cas`, ou tout élément `[data-cas]`), sinon le titre (h2 à h5) sous lequel la question
 *   est posée.
 * Deux fenêtres : un téléphone (390 × 664, barres du navigateur déduites) et un portable zoomé à 125 % (1 024 × 576 en
 * pixels CSS : un écran de 1 280 × 720) — la fenêtre de Pascal ce jour-là.
 *
 * CE QUE L'OUTIL NE SAIT PAS : si la question nomme elle-même tout ce dont elle dépend (« Parallélogramme : quel
 * rôle ? » n'a besoin de rien d'autre). Il liste des CANDIDATES, à relire ; il ne refuse rien (règle n°375 en essai,
 * n°147). Pour une question qui se suffit, `data-cas="dans-la-question"` sur sa légende ou son étiquette le dit, et la
 * mesure la saute.
 * Il ne mesure ni les identifiants (nom, classe, date), ni ce qui dort dans un `<details>` fermé.
 *
 *   node _outils/controle_contexte_fenetre.mjs                 # tout le site (pages élève)
 *   node _outils/controle_contexte_fenetre.mjs <chemin…>       # des pages ou des dossiers
 *   node _outils/controle_contexte_fenetre.mjs --json f.json   # le détail, page par page
 * Sortie : 0 mesure faite (candidates listées) · 2 en panne (Playwright absent, page qui ne s'ouvre pas : n°299).
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const RACINE = path.resolve(ICI, '..');
const IGNORES = new Set(['.git', 'node_modules', '_archive-anciennes-versions', '_outils', '_exports', '_generation', 'captures']);
const PROFESSEUR = /^(synthese_professeur|fiche_|rapport_tests)/i;
export const FENETRES = [
  { nom: 'téléphone', width: 390, height: 664, mobile: true },
  { nom: 'portable zoomé', width: 1024, height: 576, mobile: false },
];

const args = process.argv.slice(2);
const iJson = args.indexOf('--json'); const JSON_OUT = iJson >= 0 ? args[iJson + 1] : null;
const chemins = args.filter((a, i) => !a.startsWith('--') && args[i - 1] !== '--json');

function pages(depart) {
  if (!fs.existsSync(depart)) { console.log(`⛔ EN PANNE : ${depart} n'existe pas (n°299)`); process.exit(2); }
  if (!fs.statSync(depart).isDirectory()) return [path.resolve(depart)];
  const out = [];
  (function marcher(d) {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const c = path.join(d, e.name);
      if (e.isDirectory()) { if (!e.name.startsWith('.') && !IGNORES.has(e.name)) marcher(c); }
      else if (e.name.toLowerCase().endsWith('.html') && !PROFESSEUR.test(e.name)) out.push(c);
    }
  })(depart);
  return out;
}

/* Dans la page : montre les onglets et les phases (chacun est une fenêtre où l'élève travaille), laisse fermés les
   `<details>` (corrections, aides), puis mesure chaque question. */
export function mesurerDansLaPage() {
  document.querySelectorAll('[role="tabpanel"][hidden]').forEach((el) => { el.hidden = false; });
  document.querySelectorAll('.phase.hidden, .seance-panel.hidden').forEach((el) => el.classList.remove('hidden'));
  const H = innerHeight;
  scrollTo(0, 600);
  const collants = [...document.querySelectorAll('body *')].filter((e) => {
    const s = getComputedStyle(e); if (!/sticky|fixed/.test(s.position)) return false;
    const r = e.getBoundingClientRect(); return r.top <= 2 && r.height > 20 && r.height < H * 0.6 && r.width > innerWidth * 0.5;
  });
  const bandeau = Math.round(Math.max(0, ...collants.map((e) => e.getBoundingClientRect().bottom)));
  scrollTo(0, 0);
  const IDENT = /\b(nom|pr[ée]nom|classe|date|groupe)\b/i;
  // le bas de la question : la légende d'un groupe de choix (les propositions suivent), le champ d'une étiquette
  const champ = (q) => (q.tagName === 'LEGEND' ? q : q.querySelector('select, textarea, input'));
  const texte = (q) => { const c = q.cloneNode(true); c.querySelectorAll('select, textarea, option').forEach((x) => x.remove());
    return c.textContent.replace(/\s+/g, ' ').trim().slice(0, 90); };
  const questions = [...document.querySelectorAll('fieldset > legend, label')].filter((q) => {
    if (!q.getClientRects().length || q.closest('details:not([open])')) return false;
    if (q.closest('[data-cas="dans-la-question"]') || q.dataset.cas === 'dans-la-question') return false;
    if (q.tagName === 'LABEL') {
      const c = q.querySelector('select, textarea, input:not([type=radio]):not([type=checkbox]):not([type=hidden])');
      if (!c) return false;
      if (IDENT.test(q.textContent.trim().slice(0, 40)) && q.textContent.trim().length < 40) return false;
    }
    return true;
  });
  const ancres = [...document.querySelectorAll('h2, h3, h4, h5, .rappel-cas, [data-cas]:not([data-cas="dans-la-question"])')]
    .filter((a) => a.getClientRects().length);
  const avant = (a, q) => !!(a.compareDocumentPosition(q) & Node.DOCUMENT_POSITION_FOLLOWING) && !a.contains(q);
  const res = [];
  for (const q of questions) {
    let ancre = null;
    for (const a of ancres) { if (avant(a, q)) ancre = a; else break; }
    if (!ancre) continue;
    const c = champ(q); if (!c) continue;
    const haut = ancre.getBoundingClientRect().top, bas = c.getBoundingClientRect().bottom;
    res.push({ question: texte(q), ancre: ancre.textContent.replace(/\s+/g, ' ').trim().slice(0, 50),
      rappel: ancre.matches('.rappel-cas, [data-cas]'), hauteur: Math.round(bas - haut) });
  }
  return { bandeau, place: H - bandeau, questions: res };
}

let chromium;
try { ({ chromium } = await import('playwright')); }
catch { console.error('⛔ EN PANNE : Playwright introuvable (n°299).'); process.exit(2); }

let liste = [];
if (chemins.length) chemins.forEach((c) => liste.push(...pages(path.resolve(c))));
else for (const d of fs.readdirSync(RACINE)) if (d.startsWith('theme-')) liste.push(...pages(path.join(RACINE, d)));
liste = [...new Set(liste)].sort((a, b) => a.localeCompare(b, 'fr'));

const b = await chromium.launch();
const resultats = []; let pannes = 0;
async function une(fichier) {
  const rel = path.relative(RACINE, fichier); const r = { rel, fenetres: [] };
  for (const F of FENETRES) {
    const ctx = await b.newContext({ viewport: { width: F.width, height: F.height }, isMobile: F.mobile, hasTouch: F.mobile });
    await ctx.route('**/*', (q) => (/^https?:/i.test(q.request().url()) ? q.abort() : q.continue()));
    const p = await ctx.newPage();
    try {
      await p.goto(pathToFileURL(fichier).href, { waitUntil: 'load', timeout: 20000 }); await p.waitForTimeout(250);
      const m = await p.evaluate(mesurerDansLaPage);
      r.fenetres.push({ nom: F.nom, ...m, hors: m.questions.filter((q) => q.hauteur > m.place) });
    } catch (e) { r.panne = String(e).slice(0, 160); }
    await ctx.close();
    if (r.panne) break;
  }
  if (r.panne) pannes++;
  resultats.push(r);
}
for (let i = 0; i < liste.length; i += 4) await Promise.all(liste.slice(i, i + 4).map(une));
await b.close();
resultats.sort((x, y) => x.rel.localeCompare(y.rel, 'fr'));

let nq = 0, nhors = 0, pagesHors = 0;
for (const r of resultats) {
  if (r.panne) { console.log(`⛔ ${r.rel} — ne s'ouvre pas : ${r.panne}`); continue; }
  const hors = new Map();
  for (const f of r.fenetres) for (const q of f.hors) { const k = q.question; if (!hors.has(k)) hors.set(k, { q, ou: [] }); hors.get(k).ou.push(`${f.nom} ${q.hauteur} px pour ${f.place}`); }
  nq += Math.max(...r.fenetres.map((f) => f.questions.length), 0);
  if (hors.size) {
    pagesHors++; nhors += hors.size;
    console.log(`\n${r.rel}`);
    for (const { q, ou } of hors.values()) console.log(`  · « ${q.question} » — depuis « ${q.ancre} » : ${ou.join(' ; ')}`);
  }
}
console.log(`\n${resultats.length - pannes} page(s) mesurées (${FENETRES.map((f) => `${f.nom} ${f.width} × ${f.height}`).join(', ')}, bandeau collant déduit) · ${pannes} en panne`);
console.log(`${nhors} question(s) sur ${nq}, dans ${pagesHors} page(s), dont le contexte sort de la fenêtre — candidates à relire (n°375, en essai : mesure, aucun refus)`);
if (JSON_OUT) fs.writeFileSync(JSON_OUT, JSON.stringify(resultats, null, 1));
if (!resultats.length || pannes) { console.log('⛔ EN PANNE (n°299)'); process.exit(2); }
process.exit(0);
