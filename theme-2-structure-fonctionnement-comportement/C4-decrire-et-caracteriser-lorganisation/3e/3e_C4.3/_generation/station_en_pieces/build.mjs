// La station d'alerte du collège, pièce par pièce : figure isométrique de 3e_C4.3 (skill « anatomy » de Pascal).
// Kit Anatomy © 2026 Ryan, licence MIT — github.com/wheresryan22/anatomy, commit audité 1482e84 (16/11/2026).
// Le kit n'est pas versé dans le dépôt : il est lu dans ANATOMY_DIR (par défaut ~/.cache/anatomy-1482e84).
// Modèle : le lampadaire de 5e_C4.1 (PR #745 et #747).
//
//   node build.mjs            → ../../station_en_pieces.html (la page du site, thème sombre)
//   node build.mjs --light    → le thème clair, hors du dépôt (ANATOMY_TRAVAIL, par défaut ~/.cache/anatomy-travail),
//                               avec fiche.mjs à côté : de là, la fiche A4 (voir imprimer_fiche.mjs).
//
// Les pièces et leurs noms viennent des séquences de la station (3e_C4.1, 3e_C4.3, 3e_C5.1, 3e_C6.1) : aucune donnée
// inventée. La figure dit où est chaque pièce, jamais à quoi elle sert dans la chaîne d'information (l'activité 1 de
// 3e_C4.3 le fait trouver), ni en quoi elle est faite, ni ses valeurs (3e_C4.1 les fait choisir et calculer).
import { execFileSync } from "node:child_process";
import { copyFileSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const KIT = process.env.ANATOMY_DIR || join(homedir(), ".cache", "anatomy-1482e84");
const k = await import(pathToFileURL(join(KIT, "kit", "iso-kit.mjs")).href);
const G = await import(pathToFileURL(join(KIT, "kit", "lathe.mjs")).href);
const { kitScript } = await import(pathToFileURL(join(KIT, "scripts", "inline-kit.mjs")).href);

const ICI = dirname(fileURLToPath(import.meta.url));
const theme = process.argv.includes("--light") ? "light" : "dark";
const W = 460, H = 680;

// ── le monde : x et y sur le toit, z vers le haut ; une unité ≈ 1 cm, le coffret un peu grossi pour qu'on voie dedans ──
const SOL = { x: -56, y: -56, w: 132, d: 112, r: 6 };
const PLATINE = { x: -17, y: -17, w: 34, d: 34, r: 2 }, PL_H = 2.5;
const MAT_R = 4.5, MAT_HAUT = 340;
const TOP_Z = MAT_HAUT + 3;                                     // la barre du haut, sous les instruments du vent
const BRAS_Z = 262;                                             // le bras : panneau d'un côté, gyrophare et antenne de l'autre
const PLUIE_Z = 300;                                            // le bras du pluviomètre, haut : rien au-dessus ne lui cache la pluie
const SIRENE_Z = 189;                                           // l'axe du pavillon
const COF = { x: MAT_R, y: -22, w: 24, d: 44, r: 1.5 }, COF_Z = 110, COF_H = 60;

// ── les pièces numérotées, de haut en bas : le nom et où on la trouve ──
export const PIECES = [
  { id: "anemometre", n: 1, nom: "Anémomètre", dit: "trois coupelles, tout en haut du mât ; le vent les fait tourner." },
  { id: "girouette", n: 2, nom: "Girouette", dit: "à côté de l'anémomètre ; le vent fait pivoter sa flèche." },
  { id: "antenne", n: 3, nom: "Antenne radio", dit: "la tige fine, au bout du bras." },
  { id: "gyrophare", n: 4, nom: "Gyrophare", dit: "la lampe au bout du bras, au pied de l'antenne." },
  { id: "panneau", n: 5, nom: "Panneau solaire", dit: "à l'autre bout du bras, tourné vers le ciel." },
  { id: "pluviometre", n: 6, nom: "Pluviomètre", dit: "un entonnoir sur son propre bras ; la pluie tombe dedans." },
  { id: "sirene", n: 7, nom: "Sirène", dit: "le pavillon, tourné vers le quartier." },
  { id: "cable", n: 8, nom: "Câble de la sirène", dit: "deux fils sous une gaine : ils sortent sous le coffret et montent jusqu'à la sirène." },
  { id: "coffret", n: 9, nom: "Coffret", dit: "fixé au mât, à hauteur de main ; sa porte s'ouvre sur les pièces 12 à 18." },
  { id: "led", n: 10, nom: "LED d'alimentation", dit: "sur la porte du coffret : on la voit sans l'ouvrir." },
  { id: "mat", n: 11, nom: "Mât", dit: "vissé sur le toit du collège par sa platine." },
  { id: "radio", n: 12, nom: "Module radio", dit: "une petite carte, reliée à l'antenne par un câble fin." },
  { id: "barometre", n: 13, nom: "Baromètre", dit: "une petite carte, posée dans le coffret et non au vent." },
  { id: "micro", n: 14, nom: "Microcontrôleur", dit: "la carte programmable, avec son lecteur de carte mémoire." },
  { id: "convertisseur", n: 15, nom: "Convertisseur 12 V → 5 V", dit: "un petit boîtier, à côté du microcontrôleur." },
  { id: "fusible", n: 16, nom: "Fusible", dit: "dans son porte-fusible, qu'on ouvre pour le changer." },
  { id: "regulateur", n: 17, nom: "Régulateur de charge", dit: "le boîtier posé à côté de la batterie." },
  { id: "batterie", n: 18, nom: "Batterie 12 V", dit: "la pièce la plus lourde, en bas du coffret." },
];
const NB = PIECES.length;

// ── les pièces du coffret : où elles sont, coffret fermé (plan au sol, hauteur du bas, épaisseur) ──
const zB = COF_Z + 2, zM = COF_Z + 25, zH = COF_Z + 42;
const DEDANS = {
  batterie: { plan: { x: 7, y: -17, w: 17, d: 20, r: 1 }, z: zB, h: 17 },
  regulateur: { plan: { x: 8, y: 6, w: 13, d: 12, r: 0.8 }, z: zB, h: 5 },
  fusible: { plan: { x: 10, y: -18, w: 6, d: 10, r: 0.6 }, z: zM, h: 4 },
  convertisseur: { plan: { x: 9, y: -6, w: 11, d: 9, r: 0.6 }, z: zM, h: 3.5 },
  micro: { plan: { x: 7, y: 5, w: 16, d: 14, r: 0.6 }, z: zM, h: 1.6 },
  barometre: { plan: { x: 9, y: -16, w: 9, d: 9, r: 0.4 }, z: zH, h: 1.6 },
  radio: { plan: { x: 8, y: -2, w: 10, d: 8, r: 0.5 }, z: zH, h: 1.6 },
};
// ── ce qui bouge quand on ouvre le coffret : la porte s'écarte, puis chaque pièce sort et se range en colonne, à droite,
//    de haut en bas dans l'ordre des numéros ; une colonne lisible, chaque pièce à sa hauteur ──
// les numéros de la colonne tombent tous les 26 unités : assez pour deux pastilles grandies, sur un téléphone
const COLONNE = { x: 96, z: { radio: 253, barometre: 227.3, micro: 201.2, convertisseur: 174.25, fusible: 148.25, regulateur: 121.5, batterie: 87 } };
const MOUV = { porte: [16, 0, 0] };
for (const [id, { plan, z }] of Object.entries(DEDANS)) MOUV[id] = [COLONNE.x - plan.x, -(plan.y + plan.d / 2), COLONNE.z[id] - z];
const ORDRE = ["porte", "radio", "barometre", "micro", "convertisseur", "fusible", "regulateur", "batterie"];

const P = k.fitProjection(
  [...k.boxCorners(SOL, -2, 0), [0, 0, TOP_Z + 30], [0, -40, 320], [0, 44, BRAS_Z], [-48, 0, PLUIE_Z + 22],
    ...k.boxCorners({ x: 96, y: -10, w: 30, d: 20 }, 90, 250)],
  W, H, { pad: 22, azimuth: 40 },
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
    + `<text x="${(x + dx).toFixed(1)}" y="${(y + dy).toFixed(1)}">${n}</text></g>`;
}
const groupe = (id, corps, mouv) => `<g data-piece="${id}"${mouv ? ` data-m="${mouv.join(",")}"` : ""}>${corps}</g>`;
const collier = (z, h = 5, r = MAT_R + 1.3) => S(k.cylinder(0, 0, r, z, h, P, 28, 0.3), { tone: "mid" });

function toit() {
  // le toit-terrasse du collège, avec son acrotère (le muret du bord) sur les deux côtés du fond
  const out = [S(k.slabOf(SOL, -2, 2, P, 6, 0), { tone: "lo", flat: true })];
  for (let x = SOL.x + 40; x < SOL.x + SOL.w; x += 40) out.push(L(k.lineOnTop([x, SOL.y], [x, SOL.y + SOL.d], 0, P), { tone: "faint" }));
  for (let y = SOL.y + 40; y < SOL.y + SOL.d; y += 40) out.push(L(k.lineOnTop([SOL.x, y], [SOL.x + SOL.w, y], 0, P), { tone: "faint" }));
  out.push(S(k.slabOf({ x: SOL.x, y: SOL.y, w: 6, d: SOL.d, r: 0 }, 0, 22, P, 1, 0.4), { tone: "lo" }));
  out.push(S(k.slabOf({ x: SOL.x + 6, y: SOL.y, w: SOL.w - 6, d: 6, r: 0 }, 0, 22, P, 1, 0.4), { tone: "lo" }));
  return out.join("");
}

function mat() {
  const out = [`<path class="iso-halo" d="${k.haloOf(PLATINE, 0, PL_H, P)}"/>`];
  out.push(S(k.slabOf(PLATINE, 0, PL_H, P, 3, 0.5), { tone: "mid" }));
  for (const [x, y] of k.corners(PLATINE, 4)) { out.push(S(k.cylinder(x, y, 1.5, PL_H, 2, P, 14), { tone: "mid" })); out.push(vis(x, y, PL_H + 2)); }
  out.push(S(k.cylinder(0, 0, MAT_R + 1.8, PL_H, 9, P, 32, 0.6), { tone: "mid" }));
  out.push(S(k.cylinder(0, 0, MAT_R, PL_H + 9, MAT_HAUT - PL_H - 9, P, 32), { tone: "mid", crease: "none" }));
  for (const z of [60, 200, 300]) out.push(L(k.sideArc(0, 0, MAT_R, z, P, 24), { tone: "faint" }));
  out.push(S(k.cylinder(0, 0, MAT_R + 0.8, MAT_HAUT, 3, P, 32, 0.4), { tone: "mid" }));
  out.push(pin(11, [0, MAT_R, 70], -15, 2));
  return groupe("mat", out.join(""));
}

function hautDuMat() {
  // la barre du haut porte l'anémomètre (vers l'avant) et la girouette (vers le fond)
  const out = [S(k.slabOf({ x: -1.5, y: -24, w: 3, d: 48, r: 0.8 }, TOP_Z, 3, P, 2, 0.3), { tone: "mid" })];
  return out.join("");
}

function anemometre() {
  const cx = 0, cy = 21, z0 = TOP_Z + 3;
  const out = [S(k.cylinder(cx, cy, 0.9, z0, 13, P, 12), { tone: "mid" })];
  out.push(S(k.cylinder(cx, cy, 2.2, z0 + 13, 3, P, 18, 0.3), { tone: "mid" }));
  const zc = z0 + 14.5;
  for (const a of [90, 210, 330]) {
    const r = (a * Math.PI) / 180, px = cx + 10 * Math.cos(r), py = cy + 10 * Math.sin(r);
    out.push(L(k.segment([cx, cy, zc], [px, py, zc], P), { tone: "mid" }));
    out.push(S(G.sphereOf([px, py, zc], 2.8, P), { tone: "hi" }));
  }
  out.push(pin(1, [cx, cy + 12, zc], -12, -6));
  return groupe("anemometre", out.join(""));
}

function girouette() {
  const cy = -21, z0 = TOP_Z + 3;
  const out = [S(k.cylinder(0, cy, 0.9, z0, 11, P, 12), { tone: "mid" })];
  out.push(S(k.slabOf({ x: -13, y: cy - 0.8, w: 24, d: 1.6, r: 0.4 }, z0 + 11, 1.6, P, 1), { tone: "mid" }));
  out.push(S(k.slabOf({ x: -13, y: cy - 0.4, w: 7, d: 0.8, r: 0 }, z0 + 8, 11, P, 1), { tone: "hi" }));
  out.push(S(k.cylinder(11, cy, 1.5, z0 + 10.8, 2, P, 12), { tone: "mid" }));
  out.push(pin(2, [11, cy, z0 + 12], 12, -6));
  return groupe("girouette", out.join(""));
}

function bras() {
  const out = [collier(BRAS_Z - 2, 7)];
  out.push(S(k.slabOf({ x: -1.6, y: -44, w: 3.2, d: 92, r: 0.8 }, BRAS_Z, 3.5, P, 2, 0.3), { tone: "mid" }));
  out.push(vis(1.6, -36, BRAS_Z + 3.5), vis(1.6, 40, BRAS_Z + 3.5));
  return out.join("");
}

function panneau() {
  const z = BRAS_Z + 3.5, pan = { x: -17, y: 28, w: 34, d: 24, r: 1.2 }, pz = z + 5;
  const out = [S(k.cylinder(0, 40, 1.4, z, 5, P, 14), { tone: "mid" })];
  out.push(S(k.slabOf(pan, pz, 2.5, P, 2, 0.4), { tone: "hi", crease: "lo" }));
  const c = k.insetPlan(pan, 2);
  for (let i = 1; i < 6; i++) { const x = c.x + (c.w * i) / 6; out.push(L(k.lineOnTop([x, c.y], [x, c.y + c.d], pz + 2.5, P), { tone: "lo" })); }
  for (let j = 1; j < 4; j++) { const y = c.y + (c.d * j) / 4; out.push(L(k.lineOnTop([c.x, y], [c.x + c.w, y], pz + 2.5, P), { tone: "lo" })); }
  out.push(L(k.planOutline(c, pz + 2.5, P), { tone: "mid" }));
  out.push(pin(5, [pan.x + pan.w, pan.y + pan.d, pz + 2.5], 10, 8));
  return groupe("panneau", out.join(""));
}

function gyrophare() {
  const z = BRAS_Z + 3.5, cy = -38;
  const out = [S(k.cylinder(0, cy, 3.8, z, 2, P, 24, 0.3), { tone: "mid" })];
  out.push(S(k.cylinder(0, cy, 3.2, z + 2, 7, P, 24), { tone: "hi", crease: "none" }));
  for (const zz of [z + 4.5, z + 6.5]) out.push(L(k.sideArc(0, cy, 3.2, zz, P, 20), { tone: "faint" }));
  out.push(S(G.sphereOf([0, cy, z + 9], 3.2, P), { tone: "hi" }));
  out.push(pin(4, [0, cy, z + 5], 14, 6));
  return groupe("gyrophare", out.join(""));
}

function antenne() {
  const z = BRAS_Z + 3.5, cy = -29;
  const out = [S(k.cylinder(0, cy, 1.3, z, 2.5, P, 14), { tone: "mid" })];
  out.push(S(k.cylinder(0, cy, 0.5, z + 2.5, 52, P, 10), { tone: "mid", crease: "none" }));
  out.push(S(k.cylinder(0, cy, 0.9, z + 54, 1.5, P, 10), { tone: "mid" }));
  out.push(pin(3, [0, cy, z + 44], 12, 0));
  return groupe("antenne", out.join(""));
}

function pluviometre() {
  const out = [collier(PLUIE_Z - 2, 6)];
  out.push(S(k.slabOf({ x: -38, y: -1.4, w: 35, d: 2.8, r: 0.7 }, PLUIE_Z, 2.5, P, 2, 0.3), { tone: "mid" }));
  const cx = -42, z0 = PLUIE_Z + 2.5;
  out.push(S(k.cylinder(cx, 0, 6, z0, 15, P, 32), { tone: "hi", crease: "none" }));
  out.push(S(k.cylinder(cx, 0, 6.7, z0 + 15, 1.6, P, 32, 0.3), { tone: "mid" }));
  out.push(L(k.onTop(k.circleRing(cx, 0, 5.2, 32), z0 + 16.6, P, true), { tone: "lo" }));
  out.push(D([at([cx, 0, z0 + 16.6])], { size: 0.8, tone: "lo" }));
  out.push(pin(6, [cx - 6, 0, z0 + 8], -13, 0));
  return groupe("pluviometre", out.join(""));
}

function sirene() {
  // le pavillon regarde vers l'avant (+y) ; son moteur est derrière, tenu au mât par une patte
  const o = [0, 9, SIRENE_Z], F = G.frameAlong(o, [0, 1, 0]);
  const out = [collier(SIRENE_Z + 6, 5)];
  out.push(S(k.slabOf({ x: -1.5, y: MAT_R, w: 3, d: 5, r: 0.5 }, SIRENE_Z + 6.5, 3, P, 1), { tone: "mid" }));
  out.push(S(G.disc(-5, 0, 4.6, F, P), { tone: "mid" }));
  out.push(S(G.lathe([[0, 2.6], [6, 3], [14, 6], [21, 10.5]], F, P), { tone: "hi", crease: "lo" }));
  out.push(L(G.circleOf(F, 21, 10.5, P), { tone: "mid" }));
  out.push(pin(7, [0, 9 + 21, SIRENE_Z], -20, 0));
  return groupe("sirene", out.join(""));
}

function cableSirene() {
  // deux fils sous une gaine : ils sortent sous le coffret (la boucle laisse l'eau goutter), montent contre son flanc
  // puis rejoignent le mât sous la sirène
  const Y = COF.y + COF.d + 6;
  const de = at([COF.x + 6, 14, COF_Z - 3]), a = at([0, 4.2, SIRENE_Z - 0.5]);
  const out = [k.wireSvg(de, a, { via: [at([COF.x + 6, 16, COF_Z - 9]), at([COF.x + 3, Y, COF_Z - 6]), at([COF.x + 3, Y, COF_Z + COF_H + 4]), at([1.5, 8, SIRENE_Z - 6])], tone: "mid", size: 1.8 })];
  for (const z of [COF_Z + 12, COF_Z + COF_H - 12]) out.push(vis(COF.x + 3, Y, z, 0.7));
  out.push(pin(8, [COF.x + 3, Y, COF_Z + 22], -14, 0));
  return groupe("cable", out.join(""));
}

function faisceau() {
  // les autres câbles (panneau, antenne, instruments) montent du coffret au bras, groupés, contre le mât
  return L(k.pathOf([at([COF.x + 4, -16, COF_Z + COF_H]), at([1.2, -6, COF_Z + COF_H + 6]), at([1.2, -6, BRAS_Z - 2])]), { tone: "faint" });
}

function coffret() {
  const out = [collier(COF_Z + 12, 3), collier(COF_Z + COF_H - 14, 3)];
  out.push(S(k.slabOf(COF, COF_Z, COF_H, P, 2, 0.6), { tone: "mid" }));
  out.push(S(k.cylinder(COF.x + 6, 14, 2, COF_Z - 3, 3, P, 16), { tone: "mid" }));
  out.push(S(k.cylinder(COF.x + 4, -16, 1.6, COF_Z - 3, 3, P, 16), { tone: "mid" }));
  // l'ouverture du coffret, porte ôtée : le creux sombre où les pièces étaient rangées (montré coffret ouvert)
  const fx = COF.x + COF.w, creux = [[fx, COF.y + 1.6, COF_Z + 1.6], [fx, COF.y + COF.d - 1.6, COF_Z + 1.6], [fx, COF.y + COF.d - 1.6, COF_Z + COF_H - 1.6], [fx, COF.y + 1.6, COF_Z + COF_H - 1.6]];
  out.push(`<path class="creux" d="${k.pathOf(creux.map(at), true)}"/>`);
  out.push(pin(9, [COF.x + COF.w / 2, COF.y + COF.d / 2, COF_Z + COF_H], 0, 0));
  return groupe("coffret", out.join(""));
}

function porte() {
  const fx = COF.x + COF.w;
  const plan = { x: fx, y: COF.y + 1, w: 1.4, d: COF.d - 2, r: 0.4 };
  const out = [S(k.slabOf(plan, COF_Z + 1, COF_H - 2, P, 1, 0.2), { tone: "hi" })];
  out.push(D([at([fx + 1.4, COF.y + 3, COF_Z + 10]), at([fx + 1.4, COF.y + 3, COF_Z + COF_H - 10])], { size: 0.6 }));
  out.push(S(k.cylinder(fx + 2.2, COF.y + COF.d - 5, 1.6, COF_Z + COF_H / 2 - 1, 2, P, 14), { tone: "mid" }));
  // la LED d'alimentation, en haut de la porte, et sa pièce numérotée (elle part avec la porte)
  const led = [fx + 1.4, COF.y + COF.d - 9, COF_Z + COF_H - 9];
  out.push(`<g data-led>${S(G.disc(0, 0.9, 1.5, G.frameAlong(led, [1, 0, 0]), P), { tone: "lit" })}</g>`);
  out.push(pin(10, led, 13, -3));
  return groupe("porte", out.join(""), MOUV.porte);
}

function interne(id, n, plan, z, h, details) {
  // le numéro se pose à droite de la colonne, à mi-hauteur de la pièce, une fois sortie : tous alignés
  const out = [S(k.slabOf(plan, z, h, P, 1, 0.3), { tone: "hi" })];
  out.push(details);
  out.push(pin(n, [plan.x + 22, plan.y + plan.d / 2, z + h / 2], 8, 0, true));
  return groupe(id, out.join(""), MOUV[id]);
}

function internes() {
  const bat = DEDANS.batterie.plan, reg = DEDANS.regulateur.plan, fus = DEDANS.fusible.plan, con = DEDANS.convertisseur.plan;
  const mic = DEDANS.micro.plan, bar = DEDANS.barometre.plan, rad = DEDANS.radio.plan;
  return [
    interne("batterie", 18, bat, zB, 17,
      [S(k.cylinder(bat.x + 4, bat.y + 4, 1.2, zB + 17, 1.6, P, 12), { tone: "mid" }), S(k.cylinder(bat.x + 4, bat.y + bat.d - 4, 1.2, zB + 17, 1.6, P, 12), { tone: "mid" }),
        L(k.lineOnTop([bat.x + 9, bat.y + 2], [bat.x + 9, bat.y + bat.d - 2], zB + 17, P), { tone: "faint" })].join("")),
    interne("regulateur", 17, reg, zB, 5,
      [L(k.planOutline(k.insetPlan(reg, 2.5), zB + 5, P), { tone: "lo" }), D([at([reg.x + 3, reg.y + reg.d - 2.5, zB + 5]), at([reg.x + 6, reg.y + reg.d - 2.5, zB + 5])], { size: 0.5 })].join("")),
    interne("fusible", 16, fus, zM, 4,
      [S(G.disc(-3.2, 3.2, 1.1, G.frameAlong([fus.x + fus.w / 2, fus.y + fus.d / 2, zM + 5.1], [0, 1, 0]), P), { tone: "lit" })].join("")),
    interne("convertisseur", 15, con, zM, 3.5,
      [S(k.cylinder(con.x + 3.5, con.y + 4.5, 1.8, zM + 3.5, 2, P, 14), { tone: "mid" }), D([at([con.x + 8, con.y + 2, zM + 3.5]), at([con.x + 8, con.y + 7, zM + 3.5])], { size: 0.45 })].join("")),
    interne("micro", 14, mic, zM, 1.6,
      [k.dotsSvg(k.dotGrid(mic.x + 3, mic.y + 3, 4, 4, 2.6, zM + 1.6, P), { size: 0.45 }), S(k.slabOf({ x: mic.x + mic.w - 6, y: mic.y + mic.d - 5, w: 5, d: 4, r: 0.4 }, zM + 1.6, 1.2, P, 1), { tone: "mid" })].join("")),
    interne("barometre", 13, bar, zH, 1.6,
      [S(k.cylinder(bar.x + 4.5, bar.y + 4.5, 1.7, zH + 1.6, 1.2, P, 14), { tone: "mid" })].join("")),
    interne("radio", 12, rad, zH, 1.6,
      [S(k.slabOf({ x: rad.x + 2, y: rad.y + 1.5, w: 5, d: 5, r: 0.3 }, zH + 1.6, 1, P, 1), { tone: "mid" }), S(k.cylinder(rad.x + 1.5, rad.y + rad.d - 1.5, 0.9, zH + 1.6, 3, P, 10), { tone: "mid" })].join("")),
  ].join("");
}

const STYLE_NUM = `<style>
.iso-stage .num circle{fill:var(--iso-paper,#141414);stroke:currentColor;stroke-width:1}
.iso-stage .num text{font:600 9.6px/1 ui-sans-serif,system-ui,sans-serif;text-anchor:middle;dominant-baseline:central;fill:currentColor}
.iso-stage .num{color:var(--num,#e8e8e8)} .iso[data-theme="light"] .iso-stage .num,[data-theme="light"] .iso-stage .num{color:#151517}
.iso-stage .num-interne{opacity:0;transition:opacity .4s ease-out} .iso-stage[data-ouvert] .num-interne{opacity:1}
@media (prefers-reduced-motion:reduce){.iso-stage .num-interne,.iso-stage .creux{transition:none}}
.creux{fill:#d2d2d5;stroke:var(--anatomy-lo);stroke-width:var(--anatomy-weight)}
/* le creux est noir sur la page sombre ; sur fond clair, sur la fiche et sur papier, un gris léger : pas d'aplat noir à imprimer */
[data-theme="dark"] .creux{fill:#050505}
@media print{[data-theme="dark"] .creux{fill:#d2d2d5}}
.iso-stage .creux{opacity:0;transition:opacity .3s ease-out} .iso-stage[data-ouvert] .creux{opacity:1}
.iso-stage[data-ouvert] .creux{opacity:1}
/* sur un téléphone, la figure tient en 280 à 340 px : pastilles et numéros grandis */
@media (max-width:480px){.iso-stage .num circle{r:11px}.iso-stage .num text{font-size:12px}}
</style>`;

const svg = k.figureSvg({
  width: W, height: H,
  label: `La station d'alerte du collège en vue isométrique, ses pièces numérotées de 1 à ${NB} : anémomètre, girouette, antenne radio, `
    + "gyrophare, panneau solaire, pluviomètre, sirène, câble de la sirène, coffret, LED d'alimentation, mât ; dans le coffret : module radio, "
    + "baromètre, microcontrôleur, convertisseur 12 V vers 5 V, fusible, régulateur de charge, batterie 12 V. Ouvert, le coffret montre ce qu'il contient.",
  // l'intérieur du coffret est peint avant lui (caché, fermé) ; ouvert, il passe devant (voir le script)
  body: [STYLE_NUM, toit(), mat(), pluviometre(), faisceau(), hautDuMat(), girouette(), anemometre(), bras(), gyrophare(), antenne(), panneau(),
    sirene(), cableSirene(), `<g data-interieur>${internes()}</g>`, coffret(), porte()],
// une illustration de l'objet réel, pas un schéma du programme (règle de Pascal) : controle_schemas.mjs la compte à part
}).replace('<svg xmlns="http://www.w3.org/2000/svg" class="iso-svg"',
  '<svg xmlns="http://www.w3.org/2000/svg" class="iso-svg" data-illustration="vue isométrique de la station réelle, pas un schéma technique : la chaîne d\'information et la chaîne d\'énergie restent dans les séquences"');
if (!svg.includes("data-illustration=")) throw new Error("la balise <svg> du kit a changé : la figure n'est plus déclarée illustration");

const live = `
// Ouvrir et refermer le coffret : un ressort par pièce, décalés, l'étape suivante au geste de l'élève seulement.
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
  const t = ouvert ? "Ouvert · ${NB} pièces" : "Fermé · tel que sur le toit";
  if (readout.textContent !== t) readout.textContent = t;
  bouton.textContent = ouvert ? "🔧 Refermer le coffret" : "🔧 Ouvrir le coffret";
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
// Ouverte depuis une autre séquence de la station (le lien du téléphone, dans 3e_C5.1), le retour y ramène.
try {
  const r = document.referrer && new URL(document.referrer), lien = document.querySelector(".retour a");
  if (r && lien && r.origin === location.origin && /^sequence_.+[.]html$/.test(r.pathname.split("/").pop()) && r.pathname !== new URL(lien.href).pathname) {
    lien.href = r.href; lien.textContent = "← Retour à la séquence";
  }
} catch (e) { /* le lien garde la séquence de la station */ }
// Posée dans une séquence par un cadre (activité 1 de 3e_C4.3 et de 3e_C5.1) : la page le sait, cache ce qui ne sert qu'en page seule,
// et donne sa hauteur à la séquence, qui la prend (pas de barre de défilement dans le cadre).
if (parent !== window) {
  document.documentElement.classList.add("dans-cadre");
  const hauteur = () => parent.postMessage({ stationIso: document.documentElement.scrollHeight }, "*");
  new ResizeObserver(hauteur).observe(document.body);
}
`;

const nomenclature = `<ol class="nomenclature">${PIECES.map((p) => `<li><b>${p.n}</b> <span><strong>${p.nom}</strong> : ${p.dit}</span></li>`).join("")}</ol>`;
const corps = k.plateHtml({
  fig: "Fig 1",
  title: "La station d'alerte du collège",
  hint: "Touche : le coffret s'ouvre",
  readout: "Fermé · tel que sur le toit",
  keys: [],
  caption: "La station telle qu'elle est posée sur le toit du collège, face à la mer. Fermée, on voit ce qui est dehors ; "
    + "ouverte, la porte s'écarte et les pièces du coffret sortent une à une.",
  body: `<p class="ouvrir-l"><button type="button" class="ouvrir" data-ouvrir aria-pressed="false">🔧 Ouvrir le coffret</button></p>`
    + `<div class="iso-stage" tabindex="0" role="group" aria-label="La station : Espace ou Entrée ouvre et referme le coffret">${svg}</div>`,
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
/* les mots du cadre et la légende en gris du texte, pas en gris discret (WCAG AA sur les deux fonds) */
.iso-plate-corner,.iso-legend{color:var(--anatomy-text)}
@media print{.ouvrir-l{display:none}}
/* dans le cadre de la séquence : son fond bleu nuit, le titre gardé pour les lecteurs d'écran, sans le lien de retour */
html.dans-cadre,html.dans-cadre body{background:#050f24}
.dans-cadre .iso-page{width:min(650px,100% - 8px);margin:4px auto 8px}
.dans-cadre .titre{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.dans-cadre .retour{display:none}
/* sur un très petit écran, le titre du cadre chevaucherait « Fig 1 » : le titre de la page le dit déjà */
@media (max-width:360px){.iso-plate-corner[data-corner="title"]{display:none}}
${IMPRESSION_CLAIRE}
</style>`;

const pied = `<footer class="pied"><p class="retour"><a href="sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html">← Retour à la séquence de la station</a> · `
  + `<a href="station_fiche_A4.pdf">📄 La fiche A4 à imprimer</a></p>`
  + `<p class="mentions">Figure faite avec le kit Anatomy © 2026 Ryan, licence MIT (github.com/wheresryan22/anatomy).</p></footer>`;

const html = k.pageHtml({ title: "La station d'alerte, pièce par pièce", theme, body: `<h1 class="titre">La station d'alerte, pièce par pièce</h1>` + corps + nomenclature + pied, script: "/*! Kit Anatomy (github.com/wheresryan22/anatomy, commit 1482e84), inclus dans cette page sous sa licence :\n" + readFileSync(join(KIT, "LICENSE"), "utf8").replace(/\*\//g, "* /") + "*/\n" + kitScript() + live })
  .replace("<html lang=\"en\"", "<html lang=\"fr\"")
  .replace("</head>", STYLE_PAGE + "</head>")
  // les deux boucles du kit (flux et pulsation) ne servent pas ici : retirées, la page n'a aucune boucle sans fin
  // (skill motion-design de Pascal, controle_mouvement.py M2) ; dans la feuille de style comme dans le script du kit
  .replace(/\.iso-line\[data-flow\]\{[^}]*\}/g, "").replace(/\.iso-dots circle\[data-pulse\]\{[^}]*\}/g, "")
  .replace(/@keyframes iso-flow\{[^{}]*(\{[^}]*\}[^{}]*)*\}/g, "").replace(/@keyframes iso-pulse\{[^{}]*(\{[^}]*\}[^{}]*)*\}/g, "");
const TRAVAIL = process.env.ANATOMY_TRAVAIL || join(homedir(), ".cache", "anatomy-travail");
if (theme === "light") { mkdirSync(TRAVAIL, { recursive: true }); copyFileSync(join(ICI, "fiche.mjs"), join(TRAVAIL, "fiche_station.mjs")); }
const sortie = theme === "light" ? join(TRAVAIL, "station_en_pieces-clair.html") : join(ICI, "..", "..", "station_en_pieces.html");
writeFileSync(sortie, html);
// la mention CC BY-NC-SA du site (règle d'or n°321), posée par sa source unique, _outils/licence_cc.py
if (theme === "dark") {
  const outils = join(ICI, "..", "..", "..", "..", "..", "..", "_outils");
  execFileSync("python3", ["-c", "import sys, pathlib; sys.path.insert(0, sys.argv[1]); from licence_cc import injecter; p = pathlib.Path(sys.argv[2]); p.write_text(injecter(p.read_text(encoding='utf-8')), encoding='utf-8')", outils, sortie]);
  // le mode mission (Pascal, 26/11/2026 : « tout doit être en mode mission »), posé par sa source unique,
  // _outils/mode_mission/poser.py ; il ne s'allume que sur la page ouverte seule, jamais dans le cadre de la séquence
  execFileSync("python3", [join(outils, "mode_mission", "poser.py"), sortie]);
  // la lisibilité à l'écran, source unique _outils/lisibilite_ecran/ : en dernier, une régénération ne l'efface pas (n°283)
  execFileSync("python3", [join(outils, "lisibilite_ecran", "poser.py"), sortie]);
}
console.log("écrit", sortie);
