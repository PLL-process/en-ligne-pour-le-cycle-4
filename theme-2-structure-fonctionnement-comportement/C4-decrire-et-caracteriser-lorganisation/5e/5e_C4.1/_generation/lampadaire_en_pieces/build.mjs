// Le lampadaire de la cour, pièce par pièce : figure isométrique de 5e_C4.1 (skill « anatomy » de Pascal).
// Kit Anatomy © 2026 Ryan, licence MIT — github.com/wheresryan22/anatomy, commit audité 1482e84 (16/11/2026).
// Le kit n'est pas versé dans le dépôt : il est lu dans ANATOMY_DIR (par défaut ~/.cache/anatomy-1482e84).
//
//   node build.mjs            → ../../lampadaire_en_pieces.html (la page du site, thème sombre)
//   node build.mjs --light    → le thème clair, hors du dépôt (ANATOMY_TRAVAIL, par défaut ~/.cache/anatomy-travail),
//                               avec fiche.mjs à côté : de là, la fiche A4 (voir fiche.mjs).
//
// Les mots viennent de la séquence 5e_C4.1 (son FAST, ses chaînes, son simulateur) : aucune donnée inventée.
import { execFileSync } from "node:child_process";
import { copyFileSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const KIT = process.env.ANATOMY_DIR || join(homedir(), ".cache", "anatomy-1482e84");
const k = await import(pathToFileURL(join(KIT, "kit", "iso-kit.mjs")).href);
const { kitScript } = await import(pathToFileURL(join(KIT, "scripts", "inline-kit.mjs")).href);

const ICI = dirname(fileURLToPath(import.meta.url));
const theme = process.argv.includes("--light") ? "light" : "dark";
const W = 460, H = 560;

// ── le monde : x et y au sol, z vers le haut ; une unité ≈ 1 cm du vrai objet, à l'échelle de la figure ──
const SOL = { x: -110, y: -80, w: 220, d: 200, r: 6 };
const SOCLE = { x: -26, y: -26, w: 52, d: 52, r: 3 }, SOCLE_H = 14;
const MAT_R = 5, MAT_HAUT = 300, Z0 = SOCLE_H + 2.5;
const COF = { x: MAT_R, y: -12, w: 15, d: 24, r: 1.5 }, COF_Z = 70, COF_H = 50;
const PIR_Z = 190;
const BRAS = { x: -3, y: 0, w: 6, d: 76, r: 1.5 }, BRAS_Z = 286;
const TETE = { x: -15, y: 70, w: 30, d: 44, r: 4 }, TETE_Z = 279, TETE_H = 7;
const PAN = { x: -34, y: -30, w: 68, d: 46, r: 1.5 }, PAN_Z = 312;

// ── les pièces numérotées : le nom et ce qu'elle fait, avec les mots de la séquence ──
export const PIECES = [
  { id: "panneau", n: 1, nom: "Panneau solaire", dit: "capte la lumière du soleil et la change en énergie électrique." },
  { id: "tete", n: 2, nom: "Bloc de LED (la tête)", dit: "change l'énergie électrique en lumière." },
  { id: "luminosite", n: 3, nom: "Capteur de luminosité", dit: "mesure la lumière : il dit à la carte s'il fait nuit." },
  { id: "bras", n: 4, nom: "Bras", dit: "porte la tête au-dessus de l'allée." },
  { id: "pir", n: 5, nom: "Détecteur de mouvement (PIR)", dit: "repère qu'une personne passe." },
  { id: "mat", n: 6, nom: "Mât", dit: "porte tout en hauteur." },
  { id: "coffret", n: 7, nom: "Coffret", dit: "abrite la batterie, le régulateur et la carte de la pluie." },
  { id: "batterie", n: 8, nom: "Batterie", dit: "stocke l'énergie du jour pour la nuit (sous forme chimique)." },
  { id: "regulateur", n: 9, nom: "Régulateur de charge", dit: "gère la charge et la décharge de la batterie." },
  { id: "carte", n: 10, nom: "Carte programmable", dit: "décide quand allumer la LED, et à quelle puissance." },
  { id: "interrupteur", n: 11, nom: "Interrupteur commandé", dit: "laisse passer l'énergie vers la LED quand la carte le décide." },
  { id: "cable", n: 12, nom: "Câble", dit: "relie le coffret à la tête, dans le mât." },
  { id: "socle", n: 13, nom: "Socle de béton", dit: "tient le mât debout, avec ses tiges d'ancrage." },
];

// ── ce qui bouge quand on ouvre le lampadaire : un vecteur par ensemble (unités du monde) ──
const MOUV = {
  panneau: [0, 0, 46], tete: [0, 36, 4], luminosite: [0, 36, 18], pir: [0, 26, 0],
  porte: [26, 0, 0], interrupteur: [40, 0, 18], carte: [58, 0, 8], regulateur: [76, 0, -2], batterie: [94, 0, -12],
};
const ORDRE = ["panneau", "tete", "luminosite", "pir", "porte", "interrupteur", "carte", "regulateur", "batterie"];

const P = k.fitProjection(
  [...k.boxCorners(SOL, -2, 0), ...k.boxCorners(PAN, PAN_Z + 46, PAN_Z + 49), ...k.boxCorners({ x: TETE.x, y: TETE.y + 36, w: TETE.w, d: TETE.d }, TETE_Z, TETE_Z + 30),
    [COF.x + COF.w + 110, 0, COF_Z]],
  W, H, { pad: 26, azimuth: 40 },
);
const at = (p) => k.iso(p, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const vis = (x, y, z, r = 0.45) => D([at([x, y, z])], { size: r });

// un numéro posé sur la figure, près de sa pièce (règle de Pascal : numéros sur la figure, noms sous la carte)
function pin(n, p, dx = 0, dy = 0, interne = false) {
  const [x, y] = at(p);
  return `<g class="num${interne ? " num-interne" : ""}" data-num="${n}" aria-hidden="true"><circle cx="${(x + dx).toFixed(1)}" cy="${(y + dy).toFixed(1)}" r="8.6"/>`
    + `<text x="${(x + dx).toFixed(1)}" y="${(y + dy + 3.2).toFixed(1)}">${n}</text></g>`;
}
const groupe = (id, corps, mouv) => `<g data-piece="${id}"${mouv ? ` data-m="${mouv.join(",")}"` : ""}>${corps}</g>`;

function sol() {
  const out = [S(k.slabOf(SOL, -2, 2, P, 6, 0), { tone: "lo", flat: true })];
  for (let x = SOL.x + 40; x < SOL.x + SOL.w; x += 40) out.push(L(k.lineOnTop([x, SOL.y], [x, SOL.y + SOL.d], 0, P), { tone: "faint" }));
  for (let y = SOL.y + 40; y < SOL.y + SOL.d; y += 40) out.push(L(k.lineOnTop([SOL.x, y], [SOL.x + SOL.w, y], 0, P), { tone: "faint" }));
  return out.join("");
}

function socle() {
  const out = [`<path class="iso-halo" d="${k.haloOf(SOCLE, 0, SOCLE_H, P)}"/>`];
  out.push(S(k.slabOf(SOCLE, 0, SOCLE_H, P, 4, 1.2), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(SOCLE, 4), SOCLE_H, P), { tone: "faint" }));
  const pl = { x: -13, y: -13, w: 26, d: 26, r: 2 };
  out.push(S(k.slabOf(pl, SOCLE_H, 2.5, P, 3, 0.5), { tone: "mid" }));
  for (const [x, y] of k.corners(pl, 4)) {
    out.push(S(k.cylinder(x, y, 1.6, Z0, 2.4, P, 16), { tone: "mid" }));
    out.push(vis(x, y, Z0 + 2.4));
  }
  // la plaque du constructeur, sur la face du socle
  out.push(L(k.segment([SOCLE.x + SOCLE.w, -8, 5], [SOCLE.x + SOCLE.w, 8, 5], P), { tone: "faint" }));
  out.push(L(k.segment([SOCLE.x + SOCLE.w, -8, 8], [SOCLE.x + SOCLE.w, 8, 8], P), { tone: "faint" }));
  out.push(pin(13, [SOCLE.x + SOCLE.w, SOCLE.y + SOCLE.d, SOCLE_H / 2], 14, 8));
  return groupe("socle", out.join(""));
}

function mat() {
  const out = [S(k.cylinder(0, 0, MAT_R + 1.6, Z0, 10, P, 32, 0.6), { tone: "mid" })];
  out.push(S(k.cylinder(0, 0, MAT_R, Z0 + 10, MAT_HAUT - Z0 - 10, P, 32), { tone: "mid", crease: "none" }));
  for (const z of [Z0 + 10, 160, 240]) out.push(L(k.sideArc(0, 0, MAT_R, z, P, 24), { tone: "faint" }));
  out.push(S(k.cylinder(0, 0, MAT_R + 1, MAT_HAUT, 3, P, 32, 0.4), { tone: "mid" }));
  out.push(pin(6, [0, 0, 236], -14, 0));
  return groupe("mat", out.join(""));
}

function cable() {
  // le câble monte du coffret à la tête, le long du mât ; ses deux bouts finissent sur un presse-étoupe
  const de = at([COF.x + 3, 0, COF_Z + COF_H]), a = at([0, 8, BRAS_Z]);
  const out = [k.wireSvg(de, a, { via: [at([MAT_R + 1.2, 0, COF_Z + COF_H + 8]), at([MAT_R + 1.2, 0, BRAS_Z - 8]), at([0, 4, BRAS_Z - 2])], tone: "lo", size: 1.1 })];
  for (const z of [140, 210]) out.push(vis(MAT_R + 1.2, 0, z, 0.7));
  out.push(pin(12, [MAT_R + 1.2, 0, 175], 13, 0));
  return groupe("cable", out.join(""));
}

function coffret() {
  // le corps du coffret, fixé au mât ; la porte se pose sur sa face avant (+x)
  const out = [S(k.slabOf(COF, COF_Z, COF_H, P, 2, 0.6), { tone: "mid" })];
  out.push(S(k.cylinder(COF.x + COF.w / 2, 0, 2, COF_Z - 3, 3, P, 16), { tone: "mid" }));
  out.push(pin(7, [COF.x, COF.y, COF_Z + COF_H], -6, -10));
  return groupe("coffret", out.join(""));
}

function porte() {
  const fx = COF.x + COF.w;
  const plan = { x: fx, y: COF.y + 1, w: 1.4, d: COF.d - 2, r: 0.4 };
  const out = [S(k.slabOf(plan, COF_Z + 1, COF_H - 2, P, 1, 0.2), { tone: "hi" })];
  out.push(D([at([fx + 1.4, COF.y + 3, COF_Z + 9]), at([fx + 1.4, COF.y + 3, COF_Z + COF_H - 9])], { size: 0.6 }));
  out.push(S(k.cylinder(fx + 2.2, COF.y + COF.d - 5, 1.6, COF_Z + COF_H / 2 - 1, 2, P, 14), { tone: "mid" }));
  for (const z of [COF_Z + 14, COF_Z + 20, COF_Z + 26]) out.push(L(k.segment([fx + 1.45, COF.y + 6, z], [fx + 1.45, COF.y + 14, z], P), { tone: "faint" }));
  return groupe("porte", out.join(""), MOUV.porte);
}

function interne(id, n, plan, z, h, details, decal) {
  const out = [S(k.slabOf(plan, z, h, P, 1, 0.3), { tone: "hi" })];
  out.push(details);
  out.push(pin(n, [plan.x + plan.w, plan.y + plan.d, z + h], decal[0], decal[1], true));
  return groupe(id, out.join(""), MOUV[id]);
}

function internes() {
  const x0 = COF.x + 2, w = COF.w - 4;
  const bat = { x: x0, y: COF.y + 3, w, d: COF.d - 6, r: 1 };
  const reg = { x: x0 + 2, y: COF.y + 5, w: w - 4, d: 9, r: 0.6 };
  const car = { x: x0 + 1, y: COF.y + 4, w: w - 2, d: COF.d - 8, r: 0.6 };
  const itr = { x: x0 + 3, y: COF.y + 8, w: w - 6, d: 7, r: 0.6 };
  return [
    interne("batterie", 8, bat, COF_Z + 4, 14,
      [S(k.cylinder(bat.x + 3, bat.y + 4, 1.2, COF_Z + 18, 1.4, P, 12), { tone: "mid" }), S(k.cylinder(bat.x + 3, bat.y + bat.d - 4, 1.2, COF_Z + 18, 1.4, P, 12), { tone: "mid" }),
        L(k.lineOnTop([bat.x + 6, bat.y + 2], [bat.x + 6, bat.y + bat.d - 2], COF_Z + 18, P), { tone: "faint" })].join(""), [12, 6]),
    interne("regulateur", 9, reg, COF_Z + 22, 4,
      [L(k.lineOnTop([reg.x + 2, reg.y + 3], [reg.x + reg.w - 2, reg.y + 3], COF_Z + 26, P), { tone: "lo" }), L(k.lineOnTop([reg.x + 2, reg.y + 6], [reg.x + reg.w - 2, reg.y + 6], COF_Z + 26, P), { tone: "lo" })].join(""), [12, 4]),
    interne("carte", 10, car, COF_Z + 30, 1.6,
      [k.dotsSvg(k.dotGrid(car.x + 2, car.y + 3, 3, 4, 3, COF_Z + 31.6, P), { size: 0.45 }), S(k.slabOf({ x: car.x + 2, y: car.y + car.d - 6, w: 5, d: 4, r: 0.4 }, COF_Z + 31.6, 1.4, P, 1), { tone: "mid" })].join(""), [12, 2]),
    interne("interrupteur", 11, itr, COF_Z + 38, 3,
      D([at([itr.x + itr.w / 2, itr.y + itr.d / 2, COF_Z + 41])], { size: 0.8, tone: "lo" }), [12, 0]),
  ].join("");
}

function pir() {
  const out = [S(k.slabOf({ x: -2, y: MAT_R - 1, w: 4, d: 9, r: 1 }, PIR_Z, 3, P, 2, 0.3), { tone: "mid" })];
  out.push(S(k.cylinder(0, MAT_R + 10, 4.2, PIR_Z - 2, 6, P, 28, 0.8), { tone: "hi" }));
  out.push(D([at([0, MAT_R + 10, PIR_Z + 4.2])], { size: 1.3, tone: "lo" }));
  out.push(pin(5, [0, MAT_R + 14, PIR_Z], -14, 4));
  return groupe("pir", out.join(""), MOUV.pir);
}

function bras() {
  const out = [S(k.slabOf(BRAS, BRAS_Z, 5, P, 2, 0.5), { tone: "mid" })];
  out.push(S(k.cylinder(0, 4, MAT_R + 1.4, BRAS_Z - 3, 3, P, 24, 0.3), { tone: "mid" }));
  out.push(vis(0, 14, BRAS_Z + 5), vis(0, BRAS.d - 8, BRAS_Z + 5));
  out.push(pin(4, [0, BRAS.d / 2, BRAS_Z + 5], -2, -12));
  return groupe("bras", out.join(""));
}

function tete() {
  const out = [`<path class="iso-halo" d="${k.haloOf(TETE, TETE_Z, TETE_H, P)}"/>`];
  out.push(S(k.slabOf(TETE, TETE_Z, TETE_H, P, 4, 1), { tone: "mid" }));
  // le dissipateur : des ailettes sur le dessus, d'un bord à l'autre
  for (let i = 1; i < 7; i++) { const x = TETE.x + 4 + (i * (TETE.w - 8)) / 7; out.push(L(k.lineOnTop([x, TETE.y + 5], [x, TETE.y + TETE.d - 5], TETE_Z + TETE_H, P), { tone: "faint" })); }
  out.push(L(k.planOutline(k.insetPlan(TETE, 3), TETE_Z + TETE_H, P), { tone: "faint" }));
  const yv = TETE.y + TETE.d;
  out.push(`<path class="iso-line vitre" data-tone="lo" d="${k.segment([TETE.x + 4, yv, TETE_Z + 2.2], [TETE.x + TETE.w - 4, yv, TETE_Z + 2.2], P)}" style="stroke-width:2.6;stroke-linecap:round"/>`);
  out.push(pin(2, [TETE.x + TETE.w, TETE.y + TETE.d, TETE_Z], 10, 10));
  return groupe("tete", out.join(""), MOUV.tete);
}

function luminosite() {
  // le capteur, sur la tête, à l'abri de sa propre lumière (la LED éclaire vers le bas)
  const cx = TETE.x + 8, cy = TETE.y + 10;
  const out = [S(k.cylinder(cx, cy, 2.8, TETE_Z + TETE_H, 2.4, P, 20, 0.6), { tone: "hi" })];
  out.push(D([at([cx, cy, TETE_Z + TETE_H + 2.4])], { size: 0.7, tone: "lo" }));
  out.push(pin(3, [cx, cy, TETE_Z + TETE_H + 2.4], -14, -6));
  return groupe("luminosite", out.join(""), MOUV.luminosite);
}

function panneau() {
  const out = [S(k.cylinder(0, 0, 2.5, MAT_HAUT + 3, PAN_Z - MAT_HAUT - 3, P, 20), { tone: "mid" })];
  out.push(S(k.slabOf({ x: -8, y: -4, w: 16, d: 8, r: 1 }, PAN_Z - 2.5, 2.5, P, 2, 0.3), { tone: "mid" }));
  out.push(S(k.slabOf(PAN, PAN_Z, 3, P, 2, 0.4), { tone: "hi", crease: "lo" }));
  const c = k.insetPlan(PAN, 2.5);
  for (let i = 1; i < 6; i++) { const x = c.x + (c.w * i) / 6; out.push(L(k.lineOnTop([x, c.y], [x, c.y + c.d], PAN_Z + 3, P), { tone: "lo" })); }
  for (let j = 1; j < 4; j++) { const y = c.y + (c.d * j) / 4; out.push(L(k.lineOnTop([c.x, y], [c.x + c.w, y], PAN_Z + 3, P), { tone: "lo" })); }
  out.push(L(k.planOutline(c, PAN_Z + 3, P), { tone: "mid" }));
  out.push(vis(PAN.x + 2, PAN.y + 2, PAN_Z + 3), vis(PAN.x + PAN.w - 2, PAN.y + 2, PAN_Z + 3), vis(PAN.x + 2, PAN.y + PAN.d - 2, PAN_Z + 3), vis(PAN.x + PAN.w - 2, PAN.y + PAN.d - 2, PAN_Z + 3));
  out.push(pin(1, [PAN.x + PAN.w, PAN.y + PAN.d, PAN_Z + 3], 10, 8));
  return groupe("panneau", out.join(""), MOUV.panneau);
}

const STYLE_NUM = `<style>
.iso-stage .num circle{fill:var(--iso-paper,#141414);stroke:currentColor;stroke-width:1}
.iso-stage .num text{font:600 9.6px/1 ui-sans-serif,system-ui,sans-serif;text-anchor:middle;fill:currentColor}
.iso-stage .num{color:var(--num,#e8e8e8)} .iso[data-theme="light"] .iso-stage .num,[data-theme="light"] .iso-stage .num{color:#151517}
.iso-stage .num-interne{opacity:0;transition:opacity .4s ease-out} .iso-stage[data-ouvert] .num-interne{opacity:1}
@media (prefers-reduced-motion:reduce){.iso-stage .num-interne{transition:none}}
</style>`;

const svg = k.figureSvg({
  width: W, height: H,
  label: "Le lampadaire de la cour en vue isométrique, ses pièces numérotées de 1 à 13 : panneau solaire, bloc de LED, capteur de "
    + "luminosité, bras, détecteur de mouvement, mât, coffret (batterie, régulateur de charge, carte programmable, interrupteur commandé), "
    + "câble et socle. Ouvert, le coffret montre ce qu'il contient et les pièces du haut s'écartent.",
  // l'intérieur du coffret est peint avant lui (caché, fermé) ; ouvert, il passe devant (voir le script)
  body: [STYLE_NUM, sol(), socle(), mat(), cable(), `<g data-interieur>${internes()}</g>`, coffret(), porte(), pir(), bras(), tete(), luminosite(), panneau()],
// une illustration de l'objet réel, pas un schéma du programme (règle de Pascal) : controle_schemas.mjs la compte à part
}).replace('<svg xmlns="http://www.w3.org/2000/svg" class="iso-svg"',
  '<svg xmlns="http://www.w3.org/2000/svg" class="iso-svg" data-illustration="vue isométrique du lampadaire réel, pas un schéma technique : les chaînes et le FAST restent dans la séquence"');
if (!svg.includes("data-illustration=")) throw new Error("la balise <svg> du kit a changé : la figure n'est plus déclarée illustration");

const live = `
// Ouvrir et refermer le lampadaire : un ressort par ensemble, décalés, l'étape suivante au geste de l'élève seulement.
const P = ${JSON.stringify(P)};
const ORDRE = ${JSON.stringify(ORDRE)};
const stage = document.querySelector(".iso-stage");
const bouton = document.querySelector("[data-ouvrir]");
const readout = document.querySelector("[data-readout]");
const calme = matchMedia("(prefers-reduced-motion: reduce)");
const parts = ORDRE.map((id) => { const g = stage.querySelector('[data-piece="' + id + '"]'); return { g, m: g.dataset.m.split(",").map(Number), v: 0, r: 0, cible: 0, depart: 0 }; });
let ouvert = false, frame = 0, last = 0, horloge = 0, devant = false;
const interieur = stage.querySelector("[data-interieur]"), coffretG = stage.querySelector('[data-piece="coffret"]'), porteG = stage.querySelector('[data-piece="porte"]');
const porteP = parts.find((p) => p.g === porteG);
// la porte ouverte, l'intérieur passe devant le coffret ; refermée, derrière : l'ordre du peintre suit le geste
function ordre() { const d = porteP.v > 0.35; if (d === devant) return; devant = d; if (d) porteG.after(interieur); else coffretG.before(interieur); }
function placer(p) { if (p.v < 0.001) p.g.removeAttribute("transform"); else p.g.setAttribute("transform", translateAlong(P, p.m.map((x) => x * p.v))); }
function dire() {
  const t = ouvert ? "Ouvert · 13 pièces" : "Fermé · tel que dans la cour";
  if (readout.textContent !== t) readout.textContent = t;
  bouton.textContent = ouvert ? "🔧 Refermer le lampadaire" : "🔧 Ouvrir le lampadaire";
  bouton.setAttribute("aria-pressed", ouvert ? "true" : "false");
  if (ouvert) stage.setAttribute("data-ouvert", ""); else stage.removeAttribute("data-ouvert");
}
function tic(now) {
  const dt = last ? Math.min((now - last) / 1000, 1 / 30) : 1 / 60; last = now; horloge += dt;
  let encore = false;
  for (const p of parts) {
    const cible = horloge >= p.depart ? p.cible : 1 - p.cible;
    for (let i = 0; i < 4; i++) { p.r += ((cible - p.v) * 64 - p.r * 15) * dt / 4; p.v += p.r * dt / 4; }
    if (Math.abs(cible - p.v) < 0.001 && Math.abs(p.r) < 0.001) { p.v = cible; p.r = 0; } else encore = true;
    if (horloge < p.depart) encore = true;
    placer(p);
  }
  ordre();
  frame = encore ? requestAnimationFrame(tic) : 0;
}
function basculer() {
  ouvert = !ouvert; dire();
  const liste = ouvert ? parts : [...parts].reverse();
  liste.forEach((p, i) => { p.cible = ouvert ? 1 : 0; p.depart = i * 0.06; });
  if (calme.matches) { parts.forEach((p) => { p.v = p.cible; p.r = 0; placer(p); }); ordre(); return; }
  horloge = 0; last = 0; if (!frame) frame = requestAnimationFrame(tic);
}
bouton.addEventListener("click", basculer);
stage.addEventListener("click", basculer);
stage.addEventListener("keydown", (e) => { if (e.key === " " || e.key === "Enter") { e.preventDefault(); basculer(); } });
dire();
`;

const nomenclature = `<ol class="nomenclature">${PIECES.map((p) => `<li><b>${p.n}</b> <span><strong>${p.nom}</strong> : ${p.dit}</span></li>`).join("")}</ol>`;
const corps = k.plateHtml({
  fig: "Fig 1",
  title: "Le lampadaire de la cour",
  hint: "Touche : il s'ouvre",
  readout: "Fermé · tel que dans la cour",
  keys: [],
  caption: "Le jour, le panneau solaire charge la batterie, par le régulateur de charge. La nuit, la carte met la LED en veille, faible ; "
    + "quand le détecteur de mouvement voit quelqu'un passer, elle la passe à pleine puissance. Le capteur de luminosité est sur la tête, "
    + "à l'abri de sa propre lumière.",
  body: `<p class="ouvrir-l"><button type="button" class="ouvrir" data-ouvrir aria-pressed="false">🔧 Ouvrir le lampadaire</button></p>`
    + `<div class="iso-stage" tabindex="0" role="group" aria-label="Le lampadaire : Espace ou Entrée l'ouvre et le referme">${svg}</div>`,
});

// À l'impression, la page prend le thème clair du kit : sur fond sombre, le texte noirci par l'imprimante disparaît
// et la laser dépense sa cartouche (controle_impression.mjs). Les couleurs sont celles du kit, prises à leur source.
const CLAIR = k.ISO_CSS.match(/\.iso\[data-theme="light"\]\{([^}]*)\}/)[1];
const IMPRESSION_CLAIRE = `@media print{html{color-scheme:light}.iso{${CLAIR.trim()}}.iso-stage .num{color:#151517}}`;

const STYLE_PAGE = `<style>
.ouvrir-l{margin:0 0 10px;text-align:center}
.ouvrir{font:inherit;font-weight:600;min-height:44px;padding:8px 18px;border-radius:10px;border:1px solid currentColor;background:transparent;color:inherit;cursor:pointer}
.ouvrir:focus-visible,.iso-stage:focus-visible{outline:3px solid #61dafb;outline-offset:3px}
.nomenclature{list-style:none;margin:18px 0 0;padding:0;display:grid;gap:6px;font-size:.95em;line-height:1.35}
.nomenclature li{display:grid;grid-template-columns:2em 1fr;align-items:baseline}
.nomenclature b{display:inline-grid;place-items:center;width:1.6em;height:1.6em;border:1px solid currentColor;border-radius:50%;font-size:.85em}
.retour{margin:18px 0 0;font-size:.95em} .retour a{color:inherit}
.mentions{margin:22px 0 0;font-size:.82em;line-height:1.5}
.titre{margin:0 0 4px;font-size:1.45em;line-height:1.25;color:var(--anatomy-strong)}
/* les mots du cadre et la légende en gris du texte, pas en gris discret : 7,4:1 sur le fond sombre, 7:1 sur le clair (WCAG AA) */
.iso-plate-corner,.iso-legend{color:var(--anatomy-text)}
@media print{.ouvrir-l{display:none}}
${IMPRESSION_CLAIRE}
</style>`;

const pied = `<footer class="pied"><p class="retour"><a href="sequence_5e_C4.1-C4.8_lampadaire_intelligent.html">← Retour à la séquence du lampadaire</a> · `
  + `<a href="lampadaire_fiche_A4.pdf">📄 La fiche A4 à imprimer</a></p>`
  + `<p class="mentions">Figure faite avec le kit Anatomy © 2026 Ryan, licence MIT (github.com/wheresryan22/anatomy).</p></footer>`;

const html = k.pageHtml({ title: "Le lampadaire de la cour, pièce par pièce", theme, body: `<h1 class="titre">Le lampadaire de la cour, pièce par pièce</h1>` + corps + nomenclature + pied, script: "/*! Kit Anatomy (github.com/wheresryan22/anatomy, commit 1482e84), inclus dans cette page sous sa licence :\n" + readFileSync(join(KIT, "LICENSE"), "utf8").replace(/\*\//g, "* /") + "*/\n" + kitScript() + live })
  .replace("<html lang=\"en\"", "<html lang=\"fr\"")
  .replace("</head>", STYLE_PAGE + "</head>");
const TRAVAIL = process.env.ANATOMY_TRAVAIL || join(homedir(), ".cache", "anatomy-travail");
if (theme === "light") { mkdirSync(TRAVAIL, { recursive: true }); copyFileSync(join(ICI, "fiche.mjs"), join(TRAVAIL, "fiche.mjs")); }
const sortie = theme === "light" ? join(TRAVAIL, "lampadaire_en_pieces-clair.html") : join(ICI, "..", "..", "lampadaire_en_pieces.html");
writeFileSync(sortie, html);
// la mention CC BY-NC-SA du site (règle d'or n°321), posée par sa source unique, _outils/licence_cc.py
if (theme === "dark") {
  const outils = join(ICI, "..", "..", "..", "..", "..", "..", "_outils");
  execFileSync("python3", ["-c", "import sys, pathlib; sys.path.insert(0, sys.argv[1]); from licence_cc import injecter; p = pathlib.Path(sys.argv[2]); p.write_text(injecter(p.read_text(encoding='utf-8')), encoding='utf-8')", outils, sortie]);
}
console.log("écrit", sortie);
