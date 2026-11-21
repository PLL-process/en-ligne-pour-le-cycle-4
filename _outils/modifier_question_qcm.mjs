// modifier_question_qcm.mjs — réécrire des questions d'un QCM du gabarit maison, une à une, sans toucher au reste
// (règles d'or n°343 et n°344, 21/11/2026).
//
// POURQUOI
// --------
// 63 QCM sur 71 n'ont pas de générateur : leur page HTML est la source (skill `qcm-html-accessible`). Corriger une
// question à la main dans `const QUESTIONS` demande de garder la forme du gabarit, l'ordre des champs, la place de la
// bonne réponse et les champs rares (`nuance`). `fix_r.js` réécrit toute la banque depuis une liste fixe de champs et
// perd les autres ; cet outil ne réécrit que les questions nommées, et garde tous leurs champs.
//
// USAGE
// -----
//   node _outils/modifier_question_qcm.mjs <qcm.html> <retouches.json> [--verifier]
// `retouches.json` : [{ "q": 9, "attendu": "début de l'énoncé actuel", "poser": { champ: valeur, … }, "retirer": ["img"] }]
//   · "q" : le numéro de la question dans la banque (1 = la première) ;
//   · "attendu" : le début de l'énoncé actuel — l'outil refuse si la question à ce numéro ne commence pas ainsi
//     (une banque dont l'ordre a changé ne reçoit pas la retouche d'une autre question) ; une retouche déjà posée
//     (l'énoncé est celui de "poser") est reconnue et laissée ;
//   · "poser" : les champs à écrire (`q`, `o`, `r`, `d`, `expl`, `ex`, `err`, `ret`, `n`, `img`, `nuance`…) ;
//   · "retirer" : les champs à ôter.
// Refus (sortie 1, rien n'est écrit) : numéro absent, énoncé inattendu, `o` et `d` de longueurs différentes, `d` de la
// bonne réponse non vide ou `d` d'une mauvaise réponse vide, `r` hors des propositions.
// --verifier : n'écrit rien ; dit si la page porte déjà les retouches (0) ou non (1).
import fs from 'node:fs';
import vm from 'node:vm';

const args = process.argv.slice(2), verifier = args.includes('--verifier');
const [fichier, fRetouches] = args.filter(a => !a.startsWith('--'));
if (!fichier || !fRetouches) { console.error('usage : node _outils/modifier_question_qcm.mjs <qcm.html> <retouches.json> [--verifier]'); process.exit(2); }
let s = fs.readFileSync(fichier, 'utf8');
const retouches = JSON.parse(fs.readFileSync(fRetouches, 'utf8'));

// Les objets de premier niveau de `const QUESTIONS = [ … ]`, avec leur place dans le source.
function objets(src) {
  const debut = src.indexOf('const QUESTIONS');
  if (debut < 0) return null;
  const places = []; let prof = 0, dans = null, ech = false, depart = -1;
  for (let k = src.indexOf('[', debut); k < src.length; k++) {
    const ch = src[k];
    if (dans) { if (ech) ech = false; else if (ch === '\\') ech = true; else if (ch === dans) dans = null; continue; }
    if (ch === '"' || ch === "'" || ch === '`') { dans = ch; continue; }
    if (ch === '/' && src[k + 1] === '*') { k = src.indexOf('*/', k) + 1; continue; }
    if (ch === '/' && src[k + 1] === '/') { k = src.indexOf('\n', k); continue; }
    if (ch === '[' || ch === '{') { if (ch === '{' && prof === 1) depart = k; prof++; }
    if (ch === ']' || ch === '}') { prof--; if (ch === '}' && prof === 1) places.push([depart, k + 1]); if (prof === 0) break; }
  }
  return places;
}

const J = v => JSON.stringify(v);
const ORDRE = ['c', 'n', 'q', 'img', 'o', 'r', 'expl', 'ex', 'err', 'd', 'ret'];
function ecrire(Q) {
  const cles = [...ORDRE.filter(k => k in Q), ...Object.keys(Q).filter(k => !ORDRE.includes(k))];
  let out = '{', ligne = [];
  const vider = () => { if (ligne.length) { out += ligne.join(',') + ',\n '; ligne = []; } };
  for (const k of cles) {
    const v = Q[k];
    const txt = k === 'img' ? `img:{src:${J(v.src)},alt:${J(v.alt)}}` : k === 'o' || k === 'd' ? `${k}:[${v.map(J).join(',')}]` : `${k}:${J(v)}`;
    // la forme du gabarit : « c, n, q » sur la première ligne, « o » et « r » ensemble, un champ par ligne ensuite
    if (['c', 'n', 'q', 'o', 'r'].includes(k)) { ligne.push(txt); if (k === 'q' || k === 'r') vider(); }
    else { vider(); out += txt + ',\n '; }
  }
  vider();
  return out.replace(/,\n $/, '}');
}

const refus = []; let faites = 0, dejaLa = 0;
const places = objets(s);
if (!places) { console.error(`✘ ${fichier} : pas de « const QUESTIONS »`); process.exit(2); }
// de la dernière à la première : les places des questions précédentes ne bougent pas
for (const r of [...retouches].sort((a, b) => b.q - a.q)) {
  const place = places[r.q - 1];
  if (!place) { refus.push(`Q${r.q} : la banque n'a que ${places.length} questions`); continue; }
  const Q = vm.runInNewContext('(' + s.slice(place[0], place[1]) + ')', {});
  const net = t => String(t).replace(/\s+/g, ' ').trim();
  const poseDeja = r.poser && Object.entries(r.poser).every(([k, v]) => J(Q[k]) === J(v)) && (r.retirer || []).every(k => !(k in Q));
  if (poseDeja) { dejaLa++; continue; }
  if (!net(Q.q).startsWith(net(r.attendu))) { refus.push(`Q${r.q} : l'énoncé commence par « ${net(Q.q).slice(0, 50)} », pas par « ${r.attendu} »`); continue; }
  Object.assign(Q, r.poser || {});
  for (const k of r.retirer || []) delete Q[k];
  if (!Array.isArray(Q.o) || !Array.isArray(Q.d) || Q.o.length !== Q.d.length) { refus.push(`Q${r.q} : « o » et « d » n'ont pas la même longueur`); continue; }
  if (!(Q.r >= 0 && Q.r < Q.o.length)) { refus.push(`Q${r.q} : « r » hors des propositions`); continue; }
  if (Q.d[Q.r] !== '') { refus.push(`Q${r.q} : le « d » de la bonne réponse doit être vide`); continue; }
  if (Q.d.some((x, i) => i !== Q.r && !String(x).trim())) { refus.push(`Q${r.q} : une mauvaise réponse n'a pas son pourquoi`); continue; }
  s = s.slice(0, place[0]) + ecrire(Q) + s.slice(place[1]);
  faites++;
}
if (refus.length) { console.log(`✘ ${fichier}\n   · ` + refus.join('\n   · ')); process.exit(1); }
if (verifier) { console.log(`${fichier} : ${dejaLa} retouche(s) déjà posée(s), ${faites} à poser`); process.exit(faites ? 1 : 0); }
if (faites) fs.writeFileSync(fichier, s);
console.log(`✅ ${fichier} : ${faites} question(s) réécrite(s), ${dejaLa} déjà à jour`);
