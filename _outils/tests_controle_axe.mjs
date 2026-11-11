/* tests_controle_axe.mjs — le banc de `controle_axe.mjs`.
 *
 * Sur des dépôts jetables, il rejoue ce que le contrôle doit refuser (un défaut
 * grave en plus de la référence), ce qu'il doit accepter (un défaut grave CONNU,
 * un défaut de structure), et ses pannes. Deux cas viennent de la première
 * exécution sur le dépôt, le 11/11/2026 :
 *
 *   · une page qui RENVOIE ailleurs au chargement (`vittascience_variables.html`)
 *     détruisait le contexte du navigateur et passait pour une panne ;
 *   · sans l'étiquette `best-practice`, les défauts de structure que l'audit du
 *     01/11 avait comptés (`region`, `heading-order`) n'étaient plus vus du tout.
 *
 * Usage : node _outils/tests_controle_axe.mjs
 * Sortie : 0 si tout passe, 1 sinon, 2 si axe-core ou Playwright manquent (le
 * banc ne peut alors rien dire : règle d'or n°299).
 */
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { main, comparer, trouverAxe, lanceDirectement, ETIQUETTES, GRAVES } from './controle_axe.mjs';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const SCRIPT = path.join(ICI, 'controle_axe.mjs');

if (!trouverAxe()) {
  console.error('❌ EN PANNE : axe-core introuvable, le banc ne peut rien vérifier (règle d\'or n°299).');
  process.exit(2);
}

const echecs = [];
let controles = 0;
function verifier(titre, condition, detail = '') {
  controles++;
  if (!condition) echecs.push(`${titre}${detail ? `\n     ${String(detail).trim().replace(/\n/g, '\n     ')}` : ''}`);
}

const page = (corps) => `<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>Page d'essai</title>
<style>body{background:#fff;color:#111}</style></head><body><main><h1>Essai</h1>${corps}</main></body></html>`;

const SAINE = page('<p>Un texte qui se lit.</p><label for="a">Ton prénom</label> <input id="a" type="text">');
const CHAMP_SANS_NOM = page('<p>Un texte.</p><input type="text">');
const DEUX_CHAMPS_SANS_NOM = page('<p>Un texte.</p><input type="text"><input type="text">');
const SANS_MAIN = `<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>Sans repère</title></head>
<body><h1>Essai</h1><p>Un texte hors de tout repère.</p></body></html>`;

function depot(fichiers) {
  const racine = fs.mkdtempSync(path.join(os.tmpdir(), 'cax-'));
  for (const [nom, contenu] of Object.entries(fichiers)) {
    fs.mkdirSync(path.dirname(path.join(racine, nom)), { recursive: true });
    fs.writeFileSync(path.join(racine, nom), contenu, 'utf8');
  }
  return racine;
}

async function jouer(racine, options = {}) {
  const vraiLog = console.log, vraiErr = console.error;
  let texte = '';
  const capter = (...a) => { texte += a.join(' ') + '\n'; };
  console.log = capter; console.error = capter;
  let code;
  try { code = await main({ cible: racine, racine, reference: path.join(racine, 'ref.json'), ...options }); }
  finally { console.log = vraiLog; console.error = vraiErr; }
  return { code, texte };
}

// ══ LA COMPARAISON, SANS NAVIGATEUR ══════════════════════════════════════════
verifier('comparer : un nœud de plus sur une page connue est un recul',
  comparer({ label: { 'a.html': 3 } }, { label: { 'a.html': 2 } }).length === 1);
verifier('comparer : autant ou moins n\'est pas un recul',
  comparer({ label: { 'a.html': 2, 'b.html': 1 } }, { label: { 'a.html': 2, 'b.html': 4 } }).length === 0);
verifier('comparer : une page absente de la référence vaut zéro',
  comparer({ label: { 'neuve.html': 1 } }, { label: { 'a.html': 9 } }).length === 1);
verifier('comparer : une règle absente de la référence vaut zéro',
  comparer({ 'select-name': { 'a.html': 1 } }, { label: { 'a.html': 9 } }).length === 1);
verifier('comparer : un défaut déplacé d\'une page à l\'autre est vu',
  comparer({ label: { 'b.html': 1 } }, { label: { 'a.html': 1 } }).length === 1);

// ══ CE QU'IL DOIT ACCEPTER ═══════════════════════════════════════════════════
{
  const racine = depot({ 'page.html': SAINE });
  const { code, texte } = await jouer(racine);
  verifier('ACCEPTÉ — une page saine, sans référence', code === 0 && texte.includes('✅'), texte);
  fs.rmSync(racine, { recursive: true, force: true });
}
{
  const racine = depot({ 'page.html': SANS_MAIN });
  const { code, texte } = await jouer(racine);
  verifier('ACCEPTÉ — un défaut de structure (texte hors repère) est mesuré, pas refusé',
    code === 0 && texte.includes('region'), texte);
  fs.rmSync(racine, { recursive: true, force: true });
}

// ══ CE QU'IL DOIT REFUSER, ET LA RÉFÉRENCE ═══════════════════════════════════
{
  const racine = depot({ 'theme/page.html': CHAMP_SANS_NOM, '_archive-anciennes-versions/vieille.html': CHAMP_SANS_NOM });
  const sans = await jouer(racine);
  verifier('REFUS — un champ sans nom, sans référence', sans.code === 1 && sans.texte.includes('label'), sans.texte);
  verifier('le chemin du refus est relatif au dépôt, avec des « / »', sans.texte.includes('✘ theme/page.html'), sans.texte);
  verifier('les archives ne sont pas mesurées', !sans.texte.includes('vieille.html') && sans.texte.includes('1 page(s)'), sans.texte);

  const ecrite = await jouer(racine, { ecrireReference: true });
  const ref = JSON.parse(fs.readFileSync(path.join(racine, 'ref.json'), 'utf8'));
  verifier('--reference écrit la mesure, par règle et par page',
    ecrite.code === 0 && ref.regles.label && ref.regles.label['theme/page.html'] === 1, JSON.stringify(ref));

  const connue = await jouer(racine);
  verifier('ACCEPTÉ — le même défaut, une fois dans la référence', connue.code === 0 && connue.texte.includes('connus restent'), connue.texte);

  fs.writeFileSync(path.join(racine, 'theme/page.html'), DEUX_CHAMPS_SANS_NOM, 'utf8');
  const pire = await jouer(racine);
  verifier('REFUS — MUTATION : un second champ sans nom sur la même page',
    pire.code === 1 && pire.texte.includes('2 nœud(s), 1 dans la référence'), pire.texte);

  fs.writeFileSync(path.join(racine, 'theme/page.html'), SAINE, 'utf8');
  fs.writeFileSync(path.join(racine, 'theme/autre.html'), CHAMP_SANS_NOM, 'utf8');
  const deplace = await jouer(racine);
  verifier('REFUS — MUTATION : le défaut corrigé ici réapparaît sur une autre page', deplace.code === 1 && deplace.texte.includes('theme/autre.html'), deplace.texte);

  const partielle = await jouer(racine, { cible: path.join(racine, 'theme'), ecrireReference: true });
  verifier('PANNE — la référence ne s\'écrit pas sur une mesure partielle', partielle.code === 2, partielle.texte);
  fs.rmSync(racine, { recursive: true, force: true });
}

// ══ LE RENVOI N'EST PAS UNE PANNE ════════════════════════════════════════════
{
  const racine = depot({
    'cible.html': SAINE,
    'renvoi.html': '<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>Renvoi</title>'
      + '<script>location.replace("cible.html");</script></head><body><p>Renvoi…</p></body></html>',
  });
  const { code, texte } = await jouer(racine);
  verifier('ACCEPTÉ — FAUX COUPABLE : une page de renvoi est comptée à part, pas en panne',
    code === 0 && texte.includes('page(s) de renvoi') && !texte.includes('non mesurée :'), texte);
  fs.rmSync(racine, { recursive: true, force: true });
}

// ══ LES PANNES (règle d'or n°299) ════════════════════════════════════════════
{
  const racine = depot({ 'page.html': CHAMP_SANS_NOM });
  const sansAxe = await jouer(racine, { axe: path.join(racine, 'axe-absent.js') });
  verifier('PANNE — axe-core introuvable : sortie 2, pas « vert »', sansAxe.code === 2 && sansAxe.texte.includes('axe-core'), sansAxe.texte);
  fs.writeFileSync(path.join(racine, 'ref.json'), '{ ceci n\'est pas du JSON', 'utf8');
  const refCassee = await jouer(racine);
  verifier('PANNE — une référence illisible : sortie 2', refCassee.code === 2, refCassee.texte);
  fs.rmSync(racine, { recursive: true, force: true });
}
{
  const racine = depot({ 'lisezmoi.txt': 'aucune page ici' });
  const vide = await jouer(racine);
  verifier('PANNE — aucune page : sortie 2', vide.code === 2, vide.texte);
  const absent = await jouer(racine, { cible: path.join(racine, 'nexiste-pas') });
  verifier('PANNE — chemin absent : sortie 2', absent.code === 2, absent.texte);
  fs.rmSync(racine, { recursive: true, force: true });
}

// ══ LE LANCEMENT ═════════════════════════════════════════════════════════════
verifier('la garde de lancement ne part pas pour un autre script',
  !lanceDirectement(new URL('./controle_axe.mjs', import.meta.url).href, path.join(ICI, 'autre_script.mjs')));
{
  const r = spawnSync(process.execPath, ['--input-type=module', '-e',
    `import ${JSON.stringify(new URL('./controle_axe.mjs', import.meta.url).href)};`],
  { encoding: 'utf8', timeout: 120000 });
  verifier('importé, le contrôle n\'écrit rien', !(r.stdout || '').trim() && r.status === 0, r.stderr);
}
{
  // lancé comme on le lance vraiment, en sous-processus (n°299, second corollaire)
  const racine = depot({ 'page.html': SAINE });
  const r = spawnSync(process.execPath, [SCRIPT, '--muet', path.join(racine, 'page.html')], { encoding: 'utf8', timeout: 120000 });
  verifier('en sous-processus, sur une seule page : sortie 0', r.status === 0 && r.stdout.includes('✅'), r.stdout + r.stderr);
  fs.rmSync(racine, { recursive: true, force: true });
}
verifier('les étiquettes sont celles de l\'audit du 01/11, plus WCAG 2.2',
  ['wcag2a', 'wcag2aa', 'wcag21aa', 'best-practice', 'wcag22aa'].every((e) => ETIQUETTES.includes(e)));
verifier('seuls « critical » et « serious » sont refusés', GRAVES.size === 2 && GRAVES.has('critical') && GRAVES.has('serious'));

// ══ VERDICT ══════════════════════════════════════════════════════════════════
if (echecs.length) {
  console.log('');
  for (const e of echecs) console.log('❌ ' + e);
  console.log(`\n${controles - echecs.length} / ${controles}`);
  process.exit(1);
}
console.log(`✅ ${controles} contrôles — refusés : le champ sans nom hors référence, un nœud de plus, le défaut déplacé ;`);
console.log('   acceptés : la page saine, le défaut connu, le défaut de structure, la page de renvoi ;');
console.log('   en panne (sortie 2) : axe-core absent, référence illisible, aucune page, chemin absent, référence partielle.');
console.log(`\n${controles} / ${controles}`);
process.exit(0);
