/* tests_controle_verrous.mjs — le banc du contrôle des verrous expérientiels.
 *
 * POURQUOI CE BANC LANCE LE SCRIPT AU LIEU DE L'IMPORTER
 * ------------------------------------------------------
 * `controle_verrous.mjs` est entré le 31/08/2026 et n'a JAMAIS pu tourner sous
 * Windows : sa ligne 49 lisait `new URL(import.meta.url).pathname`, qui rend
 * « /C:/Users/… », d'où un chemin à deux lettres de lecteur et un `ENOENT` dès
 * le premier `readdirSync`. Aucun banc ne l'a vu, parce qu'il n'y avait aucun
 * banc — et un banc qui se serait contenté d'importer ses fonctions ne l'aurait
 * pas vu davantage : le défaut vit dans la façon dont le script établit sa
 * racine, c'est-à-dire dans son point d'entrée.
 *
 * Deuxième corollaire de la règle d'or n°299 : un banc qui vérifie un outil le
 * lance comme on le lance vraiment, EN SOUS-PROCESSUS. Chaque cas ci-dessous
 * recopie le script dans une fausse racine et exécute
 * `node …/_outils/controle_verrous.mjs`.
 *
 * Usage : node _outils/tests_controle_verrous.mjs
 */
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const SCRIPT = path.join(ICI, 'controle_verrous.mjs');

/* Les racines d'essai vivent SOUS le dépôt, et non dans le temporaire du
   système : `playwright` se résout en remontant les dossiers depuis le script,
   et le banc doit le résoudre exactement comme le fait le vrai contrôle. */
const BAC = path.join(path.dirname(ICI), '.banc-verrous');

/** Une fausse racine : `_outils/controle_verrous.mjs` recopié, plus des pages. */
function racineDessai(pages) {
  fs.rmSync(BAC, { recursive: true, force: true });
  fs.mkdirSync(path.join(BAC, '_outils'), { recursive: true });
  fs.copyFileSync(SCRIPT, path.join(BAC, '_outils', 'controle_verrous.mjs'));
  for (const [rel, contenu] of Object.entries(pages)) {
    const p = path.join(BAC, rel);
    fs.mkdirSync(path.dirname(p), { recursive: true });
    fs.writeFileSync(p, contenu, 'utf-8');
  }
  return path.join(BAC, '_outils', 'controle_verrous.mjs');
}

/** Le contrôle lancé comme Pascal le lance : en ligne de commande. */
function lancer(pages, args = []) {
  const script = racineDessai(pages);
  const r = spawnSync(process.execPath, [script, ...args], { encoding: 'utf-8', timeout: 180000 });
  fs.rmSync(BAC, { recursive: true, force: true });
  return { code: r.status, sortie: r.stdout || '', erreur: r.stderr || '' };
}

const page = (corps) => '<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
  + `<title>essai</title></head><body><script>${corps}</script></body></html>`;

const echecs = [];
let n = 0;
function cas(titre, fait) {
  n++;
  try {
    const m = fait();
    if (m) echecs.push(`${titre} : ${m}`);
  } catch (e) {
    echecs.push(`${titre} : le banc lui-même a levé — ${e.message}`);
  }
}

/* ---- 1. La garde de chemin : le script tourne, là où il tombait ---------- */

cas('lancé en ligne de commande, le script travaille et le dit', () => {
  const r = lancer({ 'lot/sequence_a.html': page('window.__exp = {};') });
  if (r.code === null) return "le script n'a pas rendu la main (délai dépassé)";
  if (r.code !== 0) return `sortie ${r.code} au lieu de 0\n     ${(r.erreur || r.sortie).trim().slice(0, 300)}`;
  if (!/1 page\(s\) à verrous ouvertes/.test(r.sortie))
    return `n'a pas compté sa page — c'est le défaut du 31/08 (chemin à deux lettres de lecteur)\n     ${(r.erreur || r.sortie).trim().slice(0, 300)}`;
  return null;
});

cas('une racine dont le chemin porte un accent et une espace reste lisible', () => {
  /* `new URL(...).pathname` encode en pour-cent : « été » devient « %C3%A9t%C3%A9 ».
     Ce cas-là échoue sur TOUTES les plateformes, Linux compris, avec l'ancien idiome. */
  const r = lancer({ 'lot été/sequence_a.html': page('window.__exp = {};') });
  if (r.code !== 0) return `sortie ${r.code}\n     ${(r.erreur || r.sortie).trim().slice(0, 300)}`;
  if (!/1 page\(s\) à verrous/.test(r.sortie)) return "la page sous un dossier accentué n'a pas été lue";
  return null;
});

/* ---- 2. Le verrou lui-même : le banc mord sur le fond -------------------- */

cas("un nom de page portant « # » ou « % » est ouvert, pas déclaré illisible", () => {
  /* `'file://' + chemin` marche pour un nom ordinaire, et même accentué — mais
     « # » y ouvre un fragment et « % » une séquence d'échappement : Chromium
     rend ERR_FILE_NOT_FOUND, le contrôle range la page en « illisible » et
     REFUSE une page qui n'a rien fait de mal. `pathToFileURL` échappe les deux.
     Aucune page du dépôt ne porte ces caractères aujourd'hui : c'est une panne
     en sommeil, pas une panne en cours — et elle tombait du bon côté, en refus
     bruyant. Le banc la tient fermée. */
  const r = lancer({
    'lot/sequence_lot #2.html': page('window.__exp = {};'),
    'lot/sequence_100%25.html': page('window.__exp = {};'),
  });
  if (r.code !== 0)
    return `sortie ${r.code} — une page au nom pourtant valide est déclarée illisible
     ${r.sortie.trim().slice(0, 400)}`;
  if (!/2 page\(s\) à verrous/.test(r.sortie)) return "les deux pages n'ont pas été comptées";
  return null;
});


cas('un verrou ouvert au chargement est refusé (le lampadaire du 31/08)', () => {
  const r = lancer({ 'lot/sequence_a.html': page('window.__exp = {"jour":"eteint"};') });
  if (r.code !== 1) return `sortie ${r.code} au lieu de 1`;
  if (!/__exp\.jour/.test(r.sortie)) return "la clé ouverte n'est pas nommée dans le rapport";
  return null;
});

cas("un casier vide déclaré d'avance n'est pas un verrou", () => {
  const r = lancer({ 'lot/sequence_a.html': page('window.__exp = {"bench":{}}; window.__zoom = false;') });
  return r.code === 0 ? null
    : `sortie ${r.code} — un casier vide a été pris pour un verrou\n     ${r.sortie.trim().slice(0, 300)}`;
});

cas('un nom autre que __exp est vu aussi (règle n°269)', () => {
  const r = lancer({ 'lot/sequence_a.html': page('window.__simOk = true;') });
  if (r.code !== 1) return `sortie ${r.code} au lieu de 1 — seul __exp serait donc regardé`;
  return /__simOk/.test(r.sortie) ? null : "__simOk n'est pas nommé dans le rapport";
});

cas('les noms écartés par déclaration ne sont pas des verrous', () => {
  const r = lancer({ 'lot/sequence_a.html': page('window.__valid = {"a1":true}; window.__clFs = 14;') });
  return r.code === 0 ? null : `sortie ${r.code} — un état d'interface a été pris pour un verrou`;
});

cas("une archive est une trace, pas une ressource — et le contrôle travaille quand même", () => {
  /* Deux pages, pas une : sans la page hors archive, ce cas passerait au vert
     sur une racine où le contrôle n'aurait RIEN ouvert (règle n°299). */
  const r = lancer({
    '_archive-anciennes-versions/sequence_v1.html': page('window.__exp = {"jour":"eteint"};'),
    'lot/sequence_a.html': page('window.__exp = {};'),
  });
  if (r.code !== 0) return `sortie ${r.code} — l'archive n'est pas écartée\n     ${r.sortie.trim().slice(0, 300)}`;
  if (!/1 page\(s\) à verrous/.test(r.sortie))
    return "l'archive est bien écartée, mais la page hors archive n'a pas été lue non plus";
  return null;
});

/* ---- 3. La panne : règle d'or n°299 ------------------------------------- */

cas('une racine SANS page à verrous est une panne, pas un succès', () => {
  const r = lancer({ 'lot/notes.md': '# rien à ouvrir ici' });
  if (r.code === 0)
    return "aucune page à ouvrir, et le contrôle sort à 0 — c'est le succès silencieux de la règle n°299";
  if (r.code !== 2) return `sortie ${r.code} au lieu de 2`;
  if (!/EN PANNE/.test(r.erreur)) return "la panne n'est pas annoncée sur la sortie d'erreur";
  return null;
});

cas('sous --muet, la panne reste visible — elle part sur stderr', () => {
  const r = lancer({ 'lot/notes.md': '# rien' }, ['--muet']);
  if (r.code !== 2) return `sortie ${r.code} au lieu de 2`;
  return /EN PANNE/.test(r.erreur) ? null : '--muet a étouffé la panne';
});

cas("une racine qui n'a que `_outils` et rien d'autre est une panne", () => {
  /* Le cas du dépôt fraîchement cloné à moitié, ou d'un outil déplacé : le
     script est bien là, sa racine existe, elle ne contient aucune page. */
  const r = lancer({});
  if (r.code === 0) return 'racine sans la moindre page, et le contrôle sort à 0';
  if (r.code !== 2) return `sortie ${r.code} au lieu de 2`;
  return /EN PANNE/.test(r.erreur) ? null : "la panne n'est pas annoncée sur stderr";
});

/* La troisième panne prévue par le script — « racine impossible à parcourir » —
   n'a pas de cas ici : sous Windows, on ne peut pas rendre un dossier illisible
   sans rendre aussi le script illisible, et un banc qui prétendrait la couvrir
   sans la produire serait exactement le genre de contrôle que la règle n°299
   interdit. Elle reste une garde défensive, écrite et non éprouvée — c'est dit. */

/* ---- 4. Le dépôt réel --------------------------------------------------- */

cas("le dépôt réel n'ouvre aucun verrou au chargement", () => {
  const r = spawnSync(process.execPath, [SCRIPT, '--muet'], { encoding: 'utf-8', timeout: 900000 });
  if (r.status === 2)
    return `le contrôle est EN PANNE sur le dépôt réel :\n     ${(r.stderr || '').trim().slice(0, 300)}`;
  if (r.status !== 0)
    return `le dépôt porte des verrous ouverts :\n     ${(r.stdout || '').trim().slice(0, 500)}`;
  return null;
});

if (echecs.length) {
  for (const e of echecs) console.log('❌ ' + e);
  console.log(`\n${n - echecs.length} / ${n}`);
  process.exit(1);
}
console.log(`✅ ${n} contrôles — un verrou ne s'ouvre que par un geste, et un contrôle qui n'a rien vu le dit`);
console.log(`\n${n} / ${n}`);
process.exit(0);
