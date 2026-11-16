// Pilote de la veille du 16/11/2026 : le lampadaire de 5e_C4.1, en figure isométrique, avec le kit d'anatomy
// (github.com/wheresryan22/anatomy, licence MIT © 2026 Ryan, commit 1482e84). Le kit n'est pas versé dans le dépôt.
// Pour rejouer : cloner anatomy dans docs/veille/anatomy (à côté de ce dossier), puis, d'ici :
//   node pilote_lampadaire.build.mjs [--light]   → lampadaire.html (ou lampadaire-clair.html), page autonome, sans réseau.
// La page n'entre pas dans le site sans la décision de Pascal (README.md de ce dossier).
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../anatomy/kit/iso-kit.mjs";
import { kitScript } from "../anatomy/scripts/inline-kit.mjs";

const ICI = dirname(fileURLToPath(import.meta.url));
const theme = process.argv.includes("--light") ? "light" : "dark";
const W = 460, H = 560;

// le monde : x et y au sol, z vers le haut ; une unité ≈ 1 cm du vrai objet, à l'échelle de la figure
const SOL = { x: -110, y: -80, w: 220, d: 200, r: 6 };
const SOCLE = { x: -26, y: -26, w: 52, d: 52, r: 3 };
const SOCLE_H = 14;
const MAT_R = 5, MAT_HAUT = 300;
const COFFRET = { x: MAT_R, y: -11, w: 14, d: 22, r: 1.5 }, COF_Z = 70, COF_H = 46;
const PIR_Z = 190;
const BRAS = { x: -3, y: 0, w: 6, d: 92, r: 1.5 }, BRAS_Z = 286;
const TETE = { x: -15, y: 70, w: 30, d: 44, r: 4 }, TETE_Z = 280, TETE_H = 7;
const PANNEAU = { x: -34, y: -30, w: 68, d: 46, r: 1.5 }, PANNEAU_Z = 312;
const CONE = [0, 92], CONE_R = 62;

const P = k.fitProjection(
  [...k.boxCorners(SOL, -2, 0), ...k.boxCorners(PANNEAU, PANNEAU_Z, PANNEAU_Z + 3), ...k.boxCorners(TETE, TETE_Z, TETE_Z + TETE_H)],
  W, H, { pad: 22, azimuth: 40 },
);
const at = (p) => k.iso(p, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);

function sol() {
  const out = [S(k.slabOf(SOL, -2, 2, P, 6, 0), { tone: "lo", flat: true })];
  // les dalles de la cour : des joints d'un bord à l'autre
  for (let x = SOL.x + 40; x < SOL.x + SOL.w; x += 40) out.push(L(k.lineOnTop([x, SOL.y], [x, SOL.y + SOL.d], 0, P), { tone: "faint" }));
  for (let y = SOL.y + 40; y < SOL.y + SOL.d; y += 40) out.push(L(k.lineOnTop([SOL.x, y], [SOL.x + SOL.w, y], 0, P), { tone: "faint" }));
  return out.join("");
}

function cone() {
  // la lumière au sol, sous la tête : son opacité suit la LED
  return `<path data-part="cone" d="${k.ring(CONE[0], CONE[1], CONE_R, 0.2, P, 48)}Z" style="fill:#ffd66b;opacity:0;stroke:none"/>`;
}

function socle() {
  const out = [`<path class="iso-halo" d="${k.haloOf(SOCLE, 0, SOCLE_H, P)}"/>`];
  out.push(S(k.slabOf(SOCLE, 0, SOCLE_H, P, 4, 1.2), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(SOCLE, 4), SOCLE_H, P), { tone: "faint" }));
  // la platine du mât et ses quatre tiges d'ancrage
  out.push(S(k.slabOf({ x: -13, y: -13, w: 26, d: 26, r: 2 }, SOCLE_H, 2.5, P, 3, 0.5), { tone: "mid" }));
  const tiges = k.corners({ x: -13, y: -13, w: 26, d: 26 }, 4);
  for (const [x, y] of tiges) out.push(S(k.cylinder(x, y, 1.6, SOCLE_H + 2.5, 2.4, P, 16), { tone: "mid" }));
  out.push(D(tiges.map(([x, y]) => at([x, y, SOCLE_H + 4.9])), { size: 0.45 }));
  return out.join("");
}

function mat() {
  const z0 = SOCLE_H + 2.5;
  const out = [S(k.cylinder(0, 0, MAT_R + 1.5, z0, 10, P, 32, 0.6), { tone: "mid" })];
  out.push(S(k.cylinder(0, 0, MAT_R, z0 + 10, MAT_HAUT - z0 - 10, P, 32), { tone: "mid", crease: "none" }));
  // les soudures du mât, en anneaux
  for (const z of [z0 + 10, 160, 240]) out.push(L(k.sideArc(0, 0, MAT_R, z, P, 24), { tone: "faint" }));
  out.push(S(k.cylinder(0, 0, MAT_R + 1, MAT_HAUT, 3, P, 32, 0.4), { tone: "mid" }));
  return out.join("");
}

function coffret() {
  // le coffret : la batterie et la carte (le « cerveau ») ; porte, charnières, serrure, plaque
  const out = [S(k.slabOf(COFFRET, COF_Z, COF_H, P, 2, 0.6), { tone: "hi" })];
  const fx = COFFRET.x + COFFRET.w;
  out.push(L(k.segment([fx, COFFRET.y + 2, COF_Z + 2], [fx, COFFRET.y + 2, COF_Z + COF_H - 2], P), { tone: "lo" }));
  out.push(D([at([fx, COFFRET.y + 2, COF_Z + 8]), at([fx, COFFRET.y + 2, COF_Z + COF_H - 8])], { size: 0.55, tone: "mid" }));
  out.push(D([at([fx, COFFRET.y + COFFRET.d - 4, COF_Z + COF_H / 2])], { size: 0.9, tone: "mid" }));
  // la jauge de la batterie, peinte sur la porte
  out.push(`<path data-part="jauge" class="iso-line" data-tone="lit" d="${k.segment([fx + 0.1, COFFRET.y + 7, COF_Z + 12], [fx + 0.1, COFFRET.y + 7, COF_Z + 34], P)}" style="stroke-width:2.4"/>`);
  out.push(L(k.segment([fx + 0.1, COFFRET.y + 5, COF_Z + 11], [fx + 0.1, COFFRET.y + 5, COF_Z + 35], P), { tone: "faint" }));
  return out.join("");
}

function pir() {
  // le détecteur de présence : une console et un dôme tourné vers la cour
  const out = [S(k.slabOf({ x: -2, y: MAT_R - 1, w: 4, d: 9, r: 1 }, PIR_Z, 3, P, 2, 0.3), { tone: "mid" })];
  out.push(S(k.cylinder(0, MAT_R + 10, 4.2, PIR_Z - 2, 6, P, 28, 0.8), { tone: "hi" }));
  out.push(`<g data-part="pir">${D([at([0, MAT_R + 10, PIR_Z + 4.2])], { size: 1.3, tone: "lo" })}</g>`);
  return out.join("");
}

function bras() {
  const out = [S(k.slabOf(BRAS, BRAS_Z, 5, P, 2, 0.5), { tone: "mid" })];
  out.push(D([at([0, 10, BRAS_Z + 5]), at([0, BRAS.d - 26, BRAS_Z + 5])], { size: 0.45 }));
  return out.join("");
}

function tete() {
  const out = [`<path class="iso-halo" d="${k.haloOf(TETE, TETE_Z, TETE_H, P)}"/>`];
  out.push(S(k.slabOf(TETE, TETE_Z, TETE_H, P, 4, 1), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(TETE, 3), TETE_Z + TETE_H, P), { tone: "faint" }));
  // la vitre des LED, sur le chant qui regarde la cour : elle s'allume
  const yv = TETE.y + TETE.d;
  out.push(`<path data-part="vitre" class="iso-line" data-tone="lo" d="${k.segment([TETE.x + 4, yv, TETE_Z + 2.2], [TETE.x + TETE.w - 4, yv, TETE_Z + 2.2], P)}" style="stroke-width:2.6;stroke-linecap:round"/>`);
  // le capteur de lumière : un petit dôme sur la tête
  out.push(S(k.cylinder(TETE.x + 8, TETE.y + 10, 2.6, TETE_Z + TETE_H, 2.2, P, 20, 0.6), { tone: "hi" }));
  out.push(D([at([TETE.x + 8, TETE.y + 10, TETE_Z + TETE_H + 2.2])], { size: 0.6, tone: "lo" }));
  return out.join("");
}

function panneau() {
  const out = [S(k.cylinder(0, 0, 2.5, MAT_HAUT + 3, PANNEAU_Z - MAT_HAUT - 3, P, 20), { tone: "mid" })];
  out.push(S(k.slabOf(PANNEAU, PANNEAU_Z, 3, P, 2, 0.4), { tone: "hi", crease: "lo" }));
  // les cellules : une grille d'un bord à l'autre, dans le cadre
  const c = k.insetPlan(PANNEAU, 2.5);
  for (let i = 1; i < 6; i++) { const x = c.x + (c.w * i) / 6; out.push(L(k.lineOnTop([x, c.y], [x, c.y + c.d], PANNEAU_Z + 3, P), { tone: "lo" })); }
  for (let j = 1; j < 4; j++) { const y = c.y + (c.d * j) / 4; out.push(L(k.lineOnTop([c.x, y], [c.x + c.w, y], PANNEAU_Z + 3, P), { tone: "lo" })); }
  out.push(L(k.planOutline(c, PANNEAU_Z + 3, P), { tone: "mid" }));
  return out.join("");
}

function cable() {
  // le câble qui monte du coffret à la tête, le long du mât
  return k.wireSvg(at([COFFRET.x + 2, 0, COF_Z + COF_H]), at([0, TETE.y - 2, BRAS_Z]), {
    via: [at([MAT_R + 1, 0, COF_Z + COF_H + 6]), at([MAT_R + 1, 0, BRAS_Z - 4]), at([0, 6, BRAS_Z - 1])], tone: "lo", size: 1,
  });
}

const svg = k.figureSvg({
  width: W, height: H,
  label: "Le lampadaire de la cour, en vue isométrique : un socle de béton, un mât, un coffret (la batterie, le régulateur de charge et la carte), "
    + "un détecteur de mouvement, un bras qui porte la tête à LED et son capteur de luminosité, et un panneau solaire au sommet. "
    + "La nuit, la LED reste en veille, faible ; quand quelqu'un passe, elle passe à pleine puissance.",
  body: [sol(), cone(), socle(), mat(), coffret(), pir(), cable(), bras(), tete(), panneau()],
});

const live = `
const ETATS = [
  { nom: "Jour", lux: 80, passage: false, led: 0, etat: "éteinte" },
  { nom: "Nuit", lux: 10, passage: false, led: 0.3, etat: "en veille, faible" },
  { nom: "Nuit", lux: 10, passage: true, led: 1, etat: "à pleine puissance" },
];
const stage = document.querySelector(".iso-stage");
const cone = stage.querySelector('[data-part="cone"]');
const vitre = stage.querySelector('[data-part="vitre"]');
const pir = stage.querySelector('[data-part="pir"]');
const readout = document.querySelector("[data-readout]");
const calme = matchMedia("(prefers-reduced-motion: reduce)");
let i = 0, led = 0, frame = 0, last = 0, visible = false;
function texte(e) { return e.nom + " · " + e.lux + " lux · " + (e.passage ? "passage" : "personne") + " → LED " + e.etat; }
function peindre() {
  const e = ETATS[i];
  cone.style.opacity = (0.42 * led).toFixed(3);
  vitre.style.stroke = led > 0.05 ? "#f5b400" : ""; vitre.style.opacity = led > 0.05 ? String(0.45 + 0.55 * led) : "";
  pir.style.opacity = e.passage ? "1" : "0.25";
  const t = texte(e);
  if (readout.textContent !== t) readout.textContent = t;
  stage.setAttribute("aria-valuenow", String(i));
  stage.setAttribute("aria-valuetext", t);
}
function tic(now) {
  const dt = last ? Math.min((now - last) / 1000, 1 / 30) : 1 / 60; last = now;
  const cible = ETATS[i].led;
  led = calme.matches ? cible : led + (cible - led) * (1 - Math.exp(-dt / 0.3));   // environ une seconde, puis l'état reste
  if (Math.abs(cible - led) < 0.002) led = cible;
  peindre();
  frame = visible && led !== cible ? requestAnimationFrame(tic) : 0;
}
const lancer = () => { if (!frame && visible) { last = 0; frame = requestAnimationFrame(tic); } };
// l'étape suivante part au toucher de l'élève, jamais toute seule (skill motion-design de Pascal, règle 3)
const aller = (n) => { i = (n + ETATS.length) % ETATS.length; lancer(); };
new IntersectionObserver((e) => { visible = e[e.length - 1].isIntersecting; if (visible) lancer(); }).observe(stage);
stage.addEventListener("click", () => aller(i + 1));
stage.addEventListener("keydown", (ev) => {
  if (ev.key === "ArrowRight" || ev.key === "ArrowUp" || ev.key === " " || ev.key === "Enter") { ev.preventDefault(); aller(i + 1); }
  if (ev.key === "ArrowLeft" || ev.key === "ArrowDown") { ev.preventDefault(); aller(i - 1); }
});
peindre();
`;

const corps = k.plateHtml({
  fig: "Fig 1",
  title: "Le lampadaire de la cour",
  hint: "Touche la figure : jour, nuit, passage",
  readout: "Jour · 80 lux · personne → LED éteinte",
  keys: [
    { mark: "lit", label: "La LED et la lumière au sol : ce qui change avec la nuit et le passage" },
    { mark: "raised", label: "Le coffret (batterie, régulateur de charge, carte programmable), le détecteur de mouvement (PIR), le capteur de luminosité, le panneau solaire" },
  ],
  caption: "Le jour, le panneau solaire charge la batterie, par le régulateur de charge. La nuit, la carte met la LED en veille, "
    + "faible ; quand le détecteur de mouvement voit quelqu'un passer, elle passe à pleine puissance quelques secondes. "
    + "Le capteur de luminosité est sur la tête, à l'abri de sa propre lumière.",
  body: `<div class="iso-stage" tabindex="0" role="slider" aria-label="Le lampadaire : les flèches font passer du jour à la nuit, puis au passage" aria-valuemin="0" aria-valuemax="2" aria-valuenow="0">${svg}</div>`,
});

const nom = theme === "light" ? "lampadaire-clair.html" : "lampadaire.html";
writeFileSync(join(ICI, nom), k.pageHtml({ title: "Le lampadaire de la cour", theme, body: corps, script: kitScript() + live }));
console.log("écrit", nom);
