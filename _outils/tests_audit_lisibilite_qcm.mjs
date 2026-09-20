/* tests_audit_lisibilite_qcm.mjs — le banc de l'audit de lisibilité.
 *
 * Il lance l'audit EN SOUS-PROCESSUS, par sa ligne de commande, et non en
 * important ses fonctions : un banc qui appelle `main()` ne passe jamais par le
 * point d'entrée, et c'est très exactement ainsi que `controle_impression.mjs`
 * est resté muet dix-sept jours sous un banc vert (règle d'or n°299, second
 * corollaire).
 *
 * Ce banc ne juge PAS les chiffres de l'audit — ils changent à chaque lot. Il
 * tient trois choses : que l'audit travaille quand on lui donne à lire, qu'il
 * tombe en panne quand il n'a rien à lire, et qu'il classe les gabarits qu'il
 * dit classer.
 *
 * Usage : node _outils/tests_audit_lisibilite_qcm.mjs
 */
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ICI = path.dirname(fileURLToPath(import.meta.url));
const SCRIPT = path.join(ICI, 'audit_lisibilite_qcm.mjs');
/* Les racines d'essai vivent SOUS le dépôt : `playwright` se résout en remontant
   les dossiers, et le banc doit le résoudre comme le fait le vrai outil. */
const BAC = path.join(path.dirname(ICI), '.banc-lisibilite');

function racineDessai(fichiers) {
  fs.rmSync(BAC, { recursive: true, force: true });
  fs.mkdirSync(path.join(BAC, '_outils'), { recursive: true });
  fs.copyFileSync(SCRIPT, path.join(BAC, '_outils', 'audit_lisibilite_qcm.mjs'));
  for (const [rel, contenu] of Object.entries(fichiers)) {
    const p = path.join(BAC, rel);
    fs.mkdirSync(path.dirname(p), { recursive: true });
    fs.writeFileSync(p, contenu, 'utf-8');
  }
  return path.join(BAC, '_outils', 'audit_lisibilite_qcm.mjs');
}

function lancer(fichiers, args = []) {
  const script = racineDessai(fichiers);
  const r = spawnSync(process.execPath, [script, ...args],
    { encoding: 'utf-8', timeout: 300000 });
  fs.rmSync(BAC, { recursive: true, force: true });
  return { code: r.status, sortie: r.stdout || '', erreur: r.stderr || '' };
}

/** Une séquence d'essai : un énoncé, un champ, des propositions à volonté. */
const sequence = (questions) => `<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<title>Essai</title></head><body><main>${questions}</main></body></html>`;

const parLabel = (id, enonce, props) =>
  `<div class="assoc"><label for="${id}">${enonce}</label><select id="${id}">`
  + `<option value="">— choisir —</option>`
  + props.map((p) => `<option>${p}</option>`).join('') + `</select></div>`;

const parP = (id, enonce, props) =>
  `<div class="exo"><p>${enonce}</p><select id="${id}">`
  + `<option value="">— choisir —</option>`
  + props.map((p) => `<option>${p}</option>`).join('') + `</select></div>`;

const enLigne = (id, enonce, props) =>
  `<table><tr><td><select id="${id}" aria-label="${enonce}">`
  + `<option value="">— choisir —</option>`
  + props.map((p) => `<option>${p}</option>`).join('') + `</select></td></tr></table>`;

const echecs = [];
let n = 0;
function cas(titre, fait) {
  n++;
  try { const m = fait(); if (m) echecs.push(`${titre} : ${m}`); }
  catch (e) { echecs.push(`${titre} : le banc lui-même a levé — ${e.message}`); }
}

/* ── 1. L'audit travaille, et il le chiffre ─────────────────────────────── */

cas("lancé en ligne de commande, l'audit mesure et écrit ses chiffres", () => {
  const r = lancer({
    'lot/sequence_essai.html': sequence(parLabel('q1', 'Une question ?', ['oui', 'non'])),
  });
  if (r.code === null) return "l'audit n'a pas rendu la main (délai dépassé)";
  if (r.code !== 0) return `sortie ${r.code}\n     ${(r.erreur || r.sortie).trim().slice(0, 300)}`;
  if (!/1 question\(s\) à liste déroulante/.test(r.sortie))
    return `la question n'a pas été comptée\n     ${r.sortie.trim().slice(0, 300)}`;
  return null;
});

/* ── 2. Les seuils de longueur mordent au bon endroit ───────────────────── */

cas('une proposition de 61 caractères dépasse le seuil de 60, pas celui de 90', () => {
  const courte = 'a'.repeat(20);
  const longue = 'b'.repeat(61);
  const r = lancer({ 'lot/sequence_essai.html': sequence(parLabel('q1', 'Énoncé', [courte, longue])) });
  if (r.code !== 0) return `sortie ${r.code}`;
  const m = r.sortie.match(/TOTAL\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)/);
  if (!m) return `tableau introuvable dans la sortie\n     ${r.sortie.slice(0, 400)}`;
  const [, , questions, s60, s90, s120] = m;
  if (questions !== '1') return `${questions} question(s) comptée(s) au lieu de 1`;
  if (s60 !== '1') return `> 60 : ${s60} au lieu de 1`;
  if (s90 !== '0') return `> 90 : ${s90} au lieu de 0 — 61 caractères ne dépassent pas 90`;
  if (s120 !== '0') return `> 120 : ${s120} au lieu de 0`;
  return null;
});

cas("l'invite « — choisir — » n'est pas comptée comme une proposition", () => {
  /* Sans cette exclusion, toute question porterait une proposition de plus et
     la médiane des longueurs serait fausse. */
  const r = lancer({
    'lot/sequence_essai.html': sequence(parLabel('q1', 'Énoncé', ['oui', 'non'])),
  });
  if (r.code !== 0) return `sortie ${r.code}`;
  return /2 propositions/.test(r.sortie) ? null
    : `l'invite est comptée : ${(r.sortie.match(/\d+ propositions/) || ['(rien)'])[0]}`;
});

/* ── 3. Les trois gabarits sont classés, pas jetés ──────────────────────── */

cas('les trois gabarits de rattachement sont reconnus et comptés séparément', () => {
  const r = lancer({
    'lot/sequence_essai.html': sequence(
      parLabel('q1', 'Par label', ['oui', 'non'])
      + parP('q2', 'Par paragraphe', ['oui', 'non'])
      + enLigne('q3', 'En ligne', ['oui', 'non'])),
  });
  if (r.code !== 0) return `sortie ${r.code}\n     ${(r.erreur || r.sortie).trim().slice(0, 300)}`;
  for (const [fam, attendu] of [['label-for', 1], ['enonce-p', 1], ['aria-en-ligne', 1]]) {
    const m = r.sortie.match(new RegExp(fam + '\\s+(\\d+)'));
    if (!m) return `le gabarit « ${fam} » n'apparaît pas dans le rapport`;
    if (m[1] !== String(attendu)) return `${fam} : ${m[1]} au lieu de ${attendu}`;
  }
  if (!/3 question\(s\) à liste déroulante/.test(r.sortie))
    return 'les trois questions ne sont pas toutes comptées — un gabarit est jeté';
  return null;
});

cas("un champ EN LIGNE n'est pas compté comme « énoncé décollé du champ »", () => {
  /* Son énoncé n'est pas au-dessus de lui : la question ne se pose pas, et le
     compter comme exception gonflerait faussement le nombre d'écarts. */
  const r = lancer({ 'lot/sequence_essai.html': sequence(enLigne('q1', 'En ligne', ['oui', 'non'])) });
  if (r.code !== 0) return `sortie ${r.code}`;
  return /Sur les 0 question\(s\) dont l'énoncé PRÉCÈDE le champ/.test(r.sortie) ? null
    : `le champ en ligne est compté parmi ceux à énoncé au-dessus\n     ${r.sortie.slice(0, 300)}`;
});

cas("ce qui s'intercale entre l'énoncé et le champ est vu", () => {
  const avecImage = '<div class="assoc"><label for="q1">Énoncé</label>'
    + '<p style="height:40px">un paragraphe intercalé</p>'
    + '<select id="q1"><option value="">— choisir —</option><option>oui</option></select></div>';
  const r = lancer({ 'lot/sequence_essai.html': sequence(avecImage) });
  if (r.code !== 0) return `sortie ${r.code}`;
  return /1 ont quelque chose qui s'intercale/.test(r.sortie) ? null
    : `l'intercalation n'est pas vue\n     ${r.sortie.slice(0, 400)}`;
});

/* ── 4. La panne : règle d'or n°299 ─────────────────────────────────────── */

cas('une racine sans séquence ni QCM est une panne, pas un succès', () => {
  const r = lancer({ 'lot/notes.md': '# rien à mesurer ici' });
  if (r.code === 0) return "aucun fichier à lire, et l'audit sort à 0 — succès silencieux";
  if (r.code !== 2) return `sortie ${r.code} au lieu de 2`;
  return /EN PANNE/.test(r.erreur) ? null : "la panne n'est pas annoncée sur la sortie d'erreur";
});

cas('sous --muet, la panne reste visible — elle part sur stderr', () => {
  const r = lancer({ 'lot/notes.md': '# rien' }, ['--muet']);
  if (r.code !== 2) return `sortie ${r.code} au lieu de 2`;
  return /EN PANNE/.test(r.erreur) ? null : '--muet a étouffé la panne';
});

cas("des fichiers ouverts mais AUCUNE question est aussi une panne", () => {
  /* Une séquence sans le moindre champ de réponse : l'audit a bien ouvert un
     fichier, il n'a pourtant rien mesuré. Sortir à 0 serait mentir. */
  const r = lancer({ 'lot/sequence_vide.html': sequence('<p>aucune question ici</p>') });
  if (r.code === 0) return "fichier ouvert, aucune question, et l'audit sort à 0";
  if (r.code !== 2) return `sortie ${r.code} au lieu de 2`;
  return /aucune question mesurée/.test(r.erreur) ? null
    : `le motif de la panne ne dit pas laquelle : ${r.erreur.trim().slice(0, 200)}`;
});

/* ── 5. Le dépôt réel ───────────────────────────────────────────────────── */

cas("l'audit passe sur le dépôt réel et y compte des questions", () => {
  const r = spawnSync(process.execPath, [SCRIPT, '--muet'],
    { encoding: 'utf-8', timeout: 1800000 });
  if (r.status === 2)
    return `l'audit est EN PANNE sur le dépôt réel :\n     ${(r.stderr || '').trim().slice(0, 300)}`;
  if (r.status !== 0) return `sortie ${r.status}`;
  const m = (r.stdout || '').match(/(\d+) question\(s\) à liste déroulante/);
  if (!m) return "l'audit n'écrit pas son compte de questions";
  if (Number(m[1]) < 100) return `${m[1]} question(s) seulement — le balayage n'a pas eu lieu`;
  return null;
});

if (echecs.length) {
  for (const e of echecs) console.log('❌ ' + e);
  console.log(`\n${n - echecs.length} / ${n}`);
  process.exit(1);
}
console.log(`✅ ${n} contrôles — l'audit classe les trois gabarits, mesure les longueurs, `
  + `et refuse de sortir vert sans avoir rien mesuré`);
console.log(`\n${n} / ${n}`);
process.exit(0);
