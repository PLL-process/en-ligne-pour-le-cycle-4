/* export_moodle_xml.mjs — les QCM du site deviennent une banque de questions Éléa (Moodle).
 *
 * Source : les 72 pages `qcm_*.html` qui portent `const QUESTIONS = [...]` (le format
 * de la séquence modèle 5e_C3.1, décision du 23/10/2026 : 30 questions fixes). Chaque
 * question (c, n, q, o, r, expl, ex, err, d, ret, img, nuance) devient une question
 * « Choix multiple » à réponse unique, dans la catégorie de son QCM, avec :
 *   - le corrigé exhaustif en rétroaction générale (pourquoi, exemple, erreur fréquente,
 *     nuance, à retenir) — les corrections restent exhaustives, pas seulement la bonne réponse ;
 *   - la rétroaction par distracteur (`d[i]`) sur chaque mauvaise réponse ;
 *   - l'image du dossier `Images/` encodée en base64 DANS le fichier (autonome, hors ligne) ;
 *   - une étiquette (tag) par code de compétence, et un idnumber stable par question
 *     (`<slug>-q<numéro>`) pour retrouver une question du site dans la banque — Moodle
 *     n'en déduit PAS de fusion : réimporter ajoute, d'où les fichiers par QCM pour les mises à jour.
 *
 * Pourquoi XML Moodle et pas GIFT : GIFT ne transporte pas d'images ; 212 questions en ont.
 *
 * Cible : Éléa (martinique.elea.apps.education.fr), Banque de questions → Importer →
 * « Format XML Moodle ». Un fichier par niveau suffit (5e, 4e, 3e, ateliers) : les
 * catégories sont créées à l'import.
 *
 * Usage : node _outils/export_moodle_xml.mjs [--sortie _exports/moodle] [--racine .]
 * Sortie : <sortie>/<niveau>.xml (4 fichiers), <sortie>/par-qcm/<slug>.xml (un par page),
 *          <sortie>/INVENTAIRE.md (ce qui est sorti, ce qui ne l'est pas, et pourquoi).
 * Code de sortie : 1 si aucune question n'a été exportée, ou si une page QUESTIONS ne se
 * lit pas, ou si une image référencée manque.
 */
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const opt = (nom, defaut) => { const i = args.indexOf(nom); return i >= 0 ? args[i + 1] : defaut; };
const RACINE = path.resolve(opt('--racine', path.dirname(ICI)));
const SORTIE = path.resolve(RACINE, opt('--sortie', '_exports/moodle'));
const EXCLUS = ['_archive-anciennes-versions', 'node_modules', '.git', '_exports'];

const MIME = { '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.webp': 'image/webp' };

/* ───────── parcours du dépôt ───────── */
function pagesQcm(dossier, acc = []) {
  for (const e of fs.readdirSync(dossier, { withFileTypes: true })) {
    if (EXCLUS.includes(e.name)) continue;
    const p = path.join(dossier, e.name);
    if (e.isDirectory()) pagesQcm(p, acc);
    else if (/^qcm.*\.html$/i.test(e.name)) acc.push(p);
  }
  return acc.sort();
}

/* ───────── lecture d'une page ───────── */
function lireQuestions(html) {
  const m = html.match(/const QUESTIONS\s*=\s*(\[[\s\S]*?\n\];)/);
  if (!m) return null;
  return vm.runInNewContext('(' + m[1].slice(0, -1) + ')', {}, { timeout: 2000 });
}

function titrePage(html) {
  const h1 = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i);
  let brut = (h1 ? h1[1] : (html.match(/<title>([\s\S]*?)<\/title>/i) || ['', ''])[1])
    .replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();
  /* Les en-têtes varient (« Thème 2 · Martinique — 3e · S6 : QCM — SOS station », « 🌱 QCM — Le jardin… »,
     « Thème 1 · 5e — QCM : Shanghai… ») : on garde ce qui suit le mot QCM et son séparateur. */
  const m = brut.match(/QCM\s*[:—–\-·]\s*(.+)$/);
  if (m && m[1].trim()) brut = m[1].trim();
  return brut.replace(/^[\p{Extended_Pictographic}\uFE0F\s]+/u, '').trim();
}

function niveauDe(rel) {
  const m = rel.match(/(^|\/)(5e|4e|3e)(\/|_)/);
  return m ? m[2] : 'ateliers';
}
function themeDe(rel) {
  const m = rel.match(/^theme-(\d)/);
  return m ? `Thème ${m[1]}` : 'Transversal';
}
function codeDe(rel) {
  const m = rel.match(/\/([345]e_C\d(?:\.\d+)?(?:-C\d(?:\.\d+)?)?)\//) || path.basename(rel).match(/qcm_([345]e_C[\d.]+(?:-C[\d.]+)?)/);
  if (m) return m[1];
  const a = rel.match(/ateliers-representations\/([^/]+)\//) || rel.match(/\/(atelier-[^/]+)\//);
  return a ? a[1] : path.basename(path.dirname(rel));
}

/* ───────── XML ───────── */
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const cdata = s => '<![CDATA[' + String(s).replace(/\]\]>/g, ']]]]><![CDATA[>') + ']]>';
/* Les textes des banques sont du texte brut (guillemets « », flèches, <, >). On les échappe
   toujours : un « < » dans une option (« S2 < S1 < S3 ») doit rester un « < » à l'écran. */
const p = s => (s && String(s).trim()) ? `<p>${esc(s)}</p>` : '';
const bloc = (etiquette, s) => (s && String(s).trim()) ? `<p><strong>${etiquette}</strong> ${esc(s)}</p>` : '';
const texte = (format, html, fichiers = '') => `<text>${cdata(html)}</text>${fichiers}`;

function fichierXml(nom, chemin) {
  const b64 = fs.readFileSync(chemin).toString('base64');
  return `<file name="${esc(nom)}" path="/" encoding="base64">${b64}</file>`;
}

function questionXml(q, idx, ctx) {
  const num = String(idx + 1).padStart(2, '0');
  const nom = `${num} · ${q.c} · ${q.n}`;
  let fichiers = '';
  let imgHtml = '';
  if (q.img && q.img.src) {
    const abs = path.resolve(path.dirname(ctx.abs), q.img.src);
    if (!fs.existsSync(abs)) { ctx.erreurs.push(`image manquante : ${q.img.src} (${ctx.rel}, q${num})`); }
    else {
      const ext = path.extname(abs).toLowerCase();
      if (!MIME[ext]) ctx.erreurs.push(`format d'image non géré : ${q.img.src} (${ctx.rel})`);
      const nomFichier = `${ctx.slug}-q${num}${ext}`;
      fichiers = fichierXml(nomFichier, abs);
      imgHtml = `<p><img src="@@PLUGINFILE@@/${esc(nomFichier)}" alt="${esc(q.img.alt || '')}" style="max-width:100%;height:auto"></p>`;
      ctx.images += 1;
    }
  }
  const enonce = p(q.q) + imgHtml;
  /* Le corrigé, dans l'ordre où un élève le lit : la bonne réponse, puis cinq temps numérotés
     (pourquoi → exemple → piège → nuance → à retenir). Même fond que la page du site, rien de réécrit. */
  const etapes = [
    ['Pourquoi', q.expl], ['Un exemple', q.ex], ['Le piège classique', q.err], ['Pour aller plus loin', q.nuance],
  ].filter(([, v]) => v && String(v).trim());
  const general = `<div class="corrige-cycle4">`
    + `<p><strong>✅ La bonne réponse :</strong> <em>${esc(q.o[q.r])}</em></p>`
    + (etapes.length ? `<ol>${etapes.map(([t, v]) => `<li><strong>${t}</strong> — ${esc(v)}</li>`).join('')}</ol>` : '')
    + bloc('📌 À retenir :', q.ret)
    + `</div>`;
  const reponses = q.o.map((o, i) => {
    const bonne = i === q.r;
    const d = Array.isArray(q.d) ? (q.d[i] || '') : '';
    const fb = bonne
      ? `✅ Exact. ${q.ret || ''}`
      : `❌ Pas celle-là. ${d || 'Relis l’énoncé et les autres propositions.'}`;
    return `    <answer fraction="${bonne ? 100 : 0}" format="html">\n      ${texte('html', p(o))}\n      <feedback format="html">${texte('html', p(fb))}</feedback>\n    </answer>`;
  }).join('\n');
  /* Deux indices pour le mode « Interactif avec essais multiples » : trois essais, l'élève est guidé
     avant de recommencer. clearwrong efface le choix faux ; shownumcorrect est muet à réponse unique. */
  const indices = [
    q.err ? `💡 Indice 1 — le piège classique : ${q.err}` : (q.expl ? `💡 Indice 1 : ${q.expl}` : ''),
    q.ret ? `💡 Indice 2 — à retenir : ${q.ret}` : (q.ex ? `💡 Indice 2 — un exemple : ${q.ex}` : ''),
  ].filter(Boolean).map(h => `    <hint format="html">\n      ${texte('html', p(h))}\n      <clearwrong/>\n    </hint>`).join('\n');
  const tags = [...new Set([q.c, ctx.niveau, ctx.code].filter(Boolean))].map(t => `      <tag><text>${esc(t)}</text></tag>`).join('\n');
  return `  <question type="multichoice">
    <name><text>${esc(nom)}</text></name>
    <questiontext format="html">
      ${texte('html', enonce, fichiers)}
    </questiontext>
    <generalfeedback format="html">${texte('html', general)}</generalfeedback>
    <defaultgrade>1</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <idnumber>${esc(`${ctx.slug}-q${num}`)}</idnumber>
    <single>true</single>
    <shuffleanswers>false</shuffleanswers>
    <answernumbering>abc</answernumbering>
    <showstandardinstruction>0</showstandardinstruction>
    <correctfeedback format="html"><text>Bonne réponse.</text></correctfeedback>
    <partiallycorrectfeedback format="html"><text>Réponse partiellement correcte.</text></partiallycorrectfeedback>
    <incorrectfeedback format="html"><text>Ce n’est pas la bonne réponse : lis le corrigé ci-dessous, il est fait pour ça.</text></incorrectfeedback>
${reponses}
${indices}
    <tags>
${tags}
    </tags>
  </question>`;
}

function categorieXml(chemin, info = '') {
  return `  <question type="category">
    <category><text>${esc(chemin)}</text></category>
    <info format="html"><text>${cdata(info)}</text></info>
    <idnumber></idnumber>
  </question>`;
}

/* ───────── export ───────── */
function main() {
  const pages = pagesQcm(RACINE);
  const parNiveau = { '5e': [], '4e': [], '3e': [], ateliers: [] };
  const inventaire = { exportes: [], ignores: [] };
  const erreurs = [];
  let totalQ = 0, totalImg = 0;
  fs.mkdirSync(path.join(SORTIE, 'par-qcm'), { recursive: true });

  for (const abs of pages) {
    const rel = path.relative(RACINE, abs).split(path.sep).join('/');
    const html = fs.readFileSync(abs, 'utf8');
    let questions;
    try { questions = lireQuestions(html); }
    catch (e) { erreurs.push(`QUESTIONS illisible : ${rel} — ${e.message}`); continue; }
    if (!questions) {
      inventaire.ignores.push({ rel, raison: html.includes('checkMCQ') ? 'ancien gabarit (cartes HTML, sans bloc QUESTIONS)' : 'page sans bloc QUESTIONS (QCM intégré ou atelier)' });
      continue;
    }
    const niveau = niveauDe(rel), theme = themeDe(rel), code = codeDe(rel);
    const slug = path.basename(abs, '.html').replace(/^qcm_/, '').replace(/[^A-Za-z0-9._-]+/g, '-');
    const titre = titrePage(html);
    const ctx = { abs, rel, slug, niveau, code, erreurs, images: 0 };
    const chemin = `$course$/top/Technologie Cycle 4/${niveau === 'ateliers' ? 'Ateliers de représentation' : niveau}/${theme} — ${code} · ${titre}`;
    const xmlQ = questions.map((q, i) => questionXml(q, i, ctx));
    const blocCat = categorieXml(chemin, `Source : ${rel} (site pll-process.github.io). ${questions.length} questions, corrigé exhaustif en rétroaction.`);
    parNiveau[niveau].push(blocCat, ...xmlQ);
    fs.writeFileSync(path.join(SORTIE, 'par-qcm', `${slug}.xml`), envelopper([blocCat, ...xmlQ]), 'utf8');
    inventaire.exportes.push({ rel, niveau, code, titre, n: questions.length, images: ctx.images });
    totalQ += questions.length; totalImg += ctx.images;
  }

  const fichiers = [];
  for (const [niveau, blocs] of Object.entries(parNiveau)) {
    if (!blocs.length) continue;
    const f = path.join(SORTIE, `${niveau}.xml`);
    fs.writeFileSync(f, envelopper(blocs), 'utf8');
    fichiers.push([niveau, f, blocs.filter(b => b.includes('type="multichoice"')).length]);
  }

  const md = [];
  md.push(`# Export Moodle XML des QCM — inventaire`, '',
    `Produit par \`_outils/export_moodle_xml.mjs\`. ${inventaire.exportes.length} QCM, **${totalQ} questions**, ${totalImg} images embarquées.`, '',
    `## Fichiers à importer dans Éléa (Banque de questions → Importer → Format XML Moodle)`, '',
    ...fichiers.map(([n, f, k]) => `- \`${path.relative(RACINE, f)}\` — ${k} questions`), '',
    `## QCM exportés`, '', `| Niveau | Code | QCM | Questions | Images |`, `|---|---|---|---:|---:|`,
    ...inventaire.exportes.map(e => `| ${e.niveau} | ${e.code} | ${e.titre.replace(/\|/g, '\\|')} | ${e.n} | ${e.images} |`), '',
    `## Pages QCM non exportées (${inventaire.ignores.length})`, '',
    ...(inventaire.ignores.length ? inventaire.ignores.map(i => `- \`${i.rel}\` — ${i.raison}`) : ['- aucune']), '');
  if (erreurs.length) md.push(`## Erreurs`, '', ...erreurs.map(e => `- ${e}`), '');
  fs.writeFileSync(path.join(SORTIE, 'INVENTAIRE.md'), md.join('\n'), 'utf8');

  console.log(`${inventaire.exportes.length} QCM → ${totalQ} questions, ${totalImg} images ; ${inventaire.ignores.length} pages laissées de côté.`);
  for (const [n, f, k] of fichiers) console.log(`  ${n.padEnd(8)} ${k.toString().padStart(4)} q  ${path.relative(RACINE, f)}`);
  for (const e of erreurs) console.error('ERREUR ' + e);
  if (erreurs.length || totalQ === 0) process.exit(1);
}

function envelopper(blocs) {
  return `<?xml version="1.0" encoding="UTF-8"?>\n<quiz>\n${blocs.join('\n')}\n</quiz>\n`;
}

main();
