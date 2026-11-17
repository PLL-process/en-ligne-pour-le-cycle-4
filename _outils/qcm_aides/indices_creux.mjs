// indices_creux.mjs — dans un QCM du gabarit maison, chaque mauvaise proposition a un pourquoi qui sert d'indice
// (skill `propositions-sans-indice`, § QCM ; vagues 1 à 3 du lot 3, 17/11/2026).
//
// LE CONSTAT. L'indice 💡 de la règle d'or n°339 affiche le `d` de la proposition choisie. Trois défauts le vident :
//   · un `d` réduit à « ! » : la marque d'un intrus-plaisanterie que personne ne choisit (« parce que le nombre 118
//     est plus joli », « pour user le clavier de l'ordinateur ») — 7 sur le site le 17/11/2026 ;
//   · un `d` vide pour une mauvaise proposition : l'élève qui la choisit n'a aucun indice ;
//   · un `d` creux : moins de 25 caractères, ou une formule qui ne dit pas pourquoi (« Rien à voir. », « Python va très
//     bien. », « Faux. », « Ce n'est pas la bonne réponse ») et qui ne l'explique pas dans la suite (moins de 45 caractères).
//
//   node _outils/qcm_aides/indices_creux.mjs [qcm.html | dossier …] [--detail] [--liste] [--strict]
//     --detail  nomme chaque indice à revoir (question, proposition, indice)
//     --liste   un seul QCM : ses questions numérotées (notion, énoncé, bonne réponse) — pour écrire ses pièges
//     --strict  sortie 1 s'il reste un « ! » ou un indice vide (les creux restent une mesure)
//
// Sortie : 0 · 1 (--strict, un « ! » ou un vide) · 2 aucun QCM lu (n°299).
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { pathToFileURL } from 'node:url';

const RACINE = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..', '..');
const args = process.argv.slice(2);
const detail = args.includes('--detail'), liste = args.includes('--liste'), strict = args.includes('--strict');
const EXCLUS = new Set(['_archive-anciennes-versions', '.git', 'node_modules', '_exports', '_generation', '_outils']);
const GENERIQUE = /^(faux|non|rien à voir|pas du tout|aucun rapport|ce n'est pas (la bonne réponse|correct)|incorrect)\b/i;

function qcms(chemins) {
  const out = [];
  const marcher = (d) => {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      if (EXCLUS.has(e.name) || e.name.startsWith('.')) continue;
      const p = path.join(d, e.name);
      if (e.isDirectory()) marcher(p);
      else if (/^qcm.*\.html$/.test(e.name)) out.push(p);
    }
  };
  const racines = chemins.length ? chemins : fs.readdirSync(RACINE).filter((t) => t.startsWith('theme-')).map((t) => path.join(RACINE, t));
  for (const c of racines) fs.statSync(c).isDirectory() ? marcher(c) : out.push(c);
  return out.sort();
}

export function questions(page) {
  const s = fs.readFileSync(page, 'utf-8');
  const i = s.indexOf('const QUESTIONS');
  if (i < 0) return null;
  const j = s.indexOf('\n];', i);
  const ctx = {};
  try { vm.runInNewContext(s.slice(i, j + 3).replace('const QUESTIONS', 'QUESTIONS'), ctx); } catch { return null; }
  return Array.isArray(ctx.QUESTIONS) ? ctx.QUESTIONS : null;
}

const texte = (x) => String(x ?? '').replace(/<[^>]+>/g, '').replace(/\s+/g, ' ').trim();

export function analyser(Q) {
  const out = [];
  Q.forEach((q, k) => (q.o || []).forEach((o, m) => {
    if (m === q.r) return;
    const d = texte((q.d || [])[m]);
    const g = d === '!' ? '!' : d === '' ? 'vide' : (d.length < 25 || (GENERIQUE.test(d) && d.length < 45)) ? 'creux' : null;
    if (g) out.push({ g, n: k + 1, notion: q.n, o: texte(o), d });
  }));
  return out;
}

function main() {
  const pages = qcms(args.filter((a) => !a.startsWith('--')));
  if (liste) {
    if (pages.length !== 1) { console.error('--liste prend un seul QCM'); process.exit(2); }
    const Q = questions(pages[0]);
    if (!Q) { console.error('✘ pas de const QUESTIONS lisible'); process.exit(2); }
    Q.forEach((q, k) => console.log(`${k + 1}. [${q.c}] ${q.n} — ${texte(q.q).slice(0, 110)}\n    ✔ ${texte(q.o[q.r]).slice(0, 90)}`));
    const a = analyser(Q);
    console.log(`\n${Q.length} questions · à revoir : ${a.length}`);
    a.forEach((x) => console.log(`  ${x.g} ${x.n} « ${x.o.slice(0, 50)} » → « ${x.d} »`));
    process.exit(0);
  }
  let lus = 0, bang = 0, vides = 0, creux = 0;
  for (const p of pages) {
    const Q = questions(p);
    if (!Q) continue;
    lus++;
    const a = analyser(Q);
    bang += a.filter((x) => x.g === '!').length; vides += a.filter((x) => x.g === 'vide').length; creux += a.filter((x) => x.g === 'creux').length;
    if (a.length && (detail || a.some((x) => x.g !== 'creux'))) {
      console.log(`${a.some((x) => x.g !== 'creux') ? (strict ? '✘' : '⚠') : '·'} ${path.relative(RACINE, p)} — ${a.length} indice(s) à revoir`);
      if (detail) a.forEach((x) => console.log(`    ${x.g.padEnd(5)} q${x.n} [${x.notion}] « ${x.o.slice(0, 50)} » → « ${x.d} »`));
    }
  }
  if (!lus) { console.log('✘ aucun QCM lu : rien n\'a été vérifié'); process.exit(2); }
  console.log(`${lus} QCM lus · « ! » (intrus-plaisanterie) : ${bang} · indice vide : ${vides} · indice creux : ${creux}`);
  process.exit(strict && (bang || vides) ? 1 : 0);
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) main();
