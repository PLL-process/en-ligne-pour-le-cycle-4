// Générateur du dessin isométrique du vélo-cargo (5e_C3.1, bloc #velo-cargo-pas-a-pas).
//   node build.mjs            -> audit d'Anatomy (doit finir sur « audit passed »), puis écrit :
//                                · le dessin, le style et le script de rotation dans la séquence, entre les marqueurs
//                                  « figure_iso_velo_cargo : début / fin » ;
//                                · le schéma fixe (état final = scène 6) dans Images/chaine_energie_velo_cargo.svg.
//   node build.mjs --poids    -> en plus, les pièces les plus lourdes.
// Relancé, il redonne les mêmes fichiers à l'octet près. Le kit (iso-kit, lathe, tube, audit) est une copie du skill
// Anatomy (licence MIT : LICENSE, commit : VERSION) ; le dessin produit ici est original, CC0.
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "./iso-kit.mjs";
import * as G from "./lathe.mjs";
import * as A from "./audit.mjs";
import { tubePieces, tubeSvg } from "./tube.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const PAGE = join(HERE, "..", "..", "sequence_5e_C3.1-C3.4_shanghai.html");
const FIXE = join(HERE, "..", "..", "Images", "chaine_energie_velo_cargo.svg");

const W = 820;
const H = 570;
const CAM_H = 322;
const DEG = Math.PI / 180;

// ── Les quatre notions et leurs couleurs (n°120), lues dans la séquence ──
const COULEUR = { source: "#ffd66b", elec: "#61dafb", moteur: "#c68ef2", meca: "#81fba1" };

// ── Le monde : x vers l'arrière du vélo, y vers le spectateur, z vers le haut (1 unité ≈ 1 cm) ──
const RC = [0, 0, 33];
const RR = 33;
const FC = [-175, 0, 27];
const RF = 27;
const BALL = 2.4;
const T = 1.6; // rayon des tubes du cadre
const D = [Math.sin(17.5 * DEG), 0, Math.cos(17.5 * DEG)]; // axe de direction
const steer = (t) => G.add3(FC, G.mul3(D, t));
const JY = 11.5; // largeur des pattes arrière
const BB = [-62, 0, 31];
const FLOOR = { x: -214, y: -15, w: 256, d: 30, r: 8 };
const FLOOR_H = 6;

const P = k.fitProjection(
  [
    ...k.boxCorners(FLOOR, -FLOOR_H, 0),
    [-70, 0, 101],
    [-70, 21, 101],
    [-70, -21, 101],
    [20, 8, 95],
    [-200, 0, 54],
    [40, 12, 40],
  ],
  W,
  CAM_H,
  { pad: 16, azimuth: 76, elevation: 23 },
);
const V = G.viewOf(P);
const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const Ln = (d, style) => k.lineSvg(d, style);
const Dots = (points, style) => k.dotsSvg(points, style);

const R = A.recorder(P, {});
const record = R.solid;
function put(piece, ref, svg, { bias = 0, shapes = [], name } = {}) {
  R.put({ piece, ride: piece, at: ref, bias, svg, shapes, name: name ?? R.nameFor(`${piece}.item`) });
}

// ── Boules-jonctions et tubes : le cadre est un montage de tubes qui butent sur des boules ──
const joints = {};
function joint(name, pos, r = BALL, { tone = "mid", piece = "bike", owner = "bike", extra = "" } = {}) {
  const id = R.nameFor(`${piece}.${name}`);
  put(piece, pos, S(G.sphereOf(pos, r, P, { steps: 14 }), { tone }) + extra, { name: id, shapes: [record(A.ball(pos, r, { name: id, owner }))] });
  joints[name] = { pos, r };
  return joints[name];
}
const reach = (R0, r) => Math.sqrt(R0 * R0 - r * r);
function strut(a, b, r = T, { tone = "mid", piece = "bike", owner = "bike", name = "tube", seam = true } = {}) {
  const axis = G.unit3(G.sub3(b.pos, a.pos));
  const length = G.len3(G.sub3(b.pos, a.pos));
  const s0 = reach(a.r, r);
  const s1 = length - reach(b.r, r);
  const F = G.frameAlong(a.pos, axis);
  const id = R.nameFor(`${piece}.${name}`);
  const mid = G.lerp3(a.pos, b.pos, (s0 + s1) / 2 / length);
  const inner = "";
  put(piece, mid, S(G.disc(s0, s1, r, F, P, { steps: 10 }), { tone, inner }), { name: id, shapes: [record(A.disc(F, s0, s1, r, { name: id, owner }))] });
}
// un cylindre posé sur une face : de la position `from` sur l'axe `axis`, de s0 à s1
function post(from, axis, s0, s1, r, { tone = "mid", piece = "bike", owner = "bike", name = "post", extra = "", inner = "" } = {}) {
  const F = G.frameAlong(from, axis);
  const id = R.nameFor(`${piece}.${name}`);
  put(piece, G.add3(from, G.mul3(F.a, (s0 + s1) / 2)), S(G.disc(s0, s1, r, F, P, { steps: 10 }), { tone, inner }) + extra, { name: id, shapes: [record(A.disc(F, s0, s1, r, { name: id, owner }))] });
  return F;
}
function slabItem(piece, plan, z, h, { tone = "mid", steps = 4, bevel = 0.5, name = "slab", owner = piece, extra = "", inner = "", crease = "faint" } = {}) {
  const id = R.nameFor(`${piece}.${name}`);
  const mid = [plan.x + plan.w / 2, plan.y + plan.d / 2, z + h / 2];
  put(piece, mid, S(k.slabOf(plan, z, h, P, steps, bevel), { tone, inner, crease }) + extra, { name: id, shapes: [record(A.slab(plan, z, h, { name: id, owner }, steps))] });
}

// ── La route : une chaussée qui sort du cadre, deux rives et des tirets (qui défilent à la scène 5) ──
// (le cadrage reste calculé sur l'ancien socle FLOOR : les zooms des scènes 2 à 4 ne bougent pas)
const ROAD = { x: -1000, y: -60, w: 2000, d: 140, r: 0 };
const DASH = 44; // période des tirets, en cm
const back = [];
const flatPlan = (plan, cls) => `<path class="${cls}" d="${k.planOutline(plan, 0, P)}"/>`;
back.push(`<g class="pv-route">` + S(k.slabOf(ROAD, -FLOOR_H, FLOOR_H, P, 2, 0), { tone: "lo" }) +
  flatPlan({ x: -1000, y: -34, w: 2000, d: 1.6, r: 0 }, "pv-rive") + flatPlan({ x: -1000, y: 44, w: 2000, d: 1.6, r: 0 }, "pv-rive") + `</g>`);
{
  const dashes = [];
  for (let x = -1000; x < 1000; x += DASH) dashes.push(flatPlan({ x, y: 20, w: 22, d: 2.4, r: 1 }, "pv-tiret"));
  back.push(`<g class="pv-tirets">${dashes.join("")}</g>`);
}
record(A.slab(ROAD, -FLOOR_H, FLOOR_H, { name: "stand.road", ground: true }, 2));

// ── Roues : pneu, rayons (qui tournent), jante et moyeu forment UNE pièce dessinée dans l'ordre ──
// (pneu et jante se touchent sur tout un cercle : séparés, ils s'entrecroisent pour l'audit)
// transmission (côté spectateur) : plateau et pignon dans la tranche y = 7,8 à 8,6 ; la chaîne posée devant, jusqu'à 9,2
const CHAIN_Y0 = 7.8;
const CHAIN_Y1 = 8.6;
const CHAIN_T = 0.6;
const RING_R = 8;
const SPROCKET_R = 5;
function wheel(id, C, Rout, { motor }) {
  const F = G.frameAlong(C, [0, 1, 0]);
  const tireHalf = 3.0;
  const tireIn = Rout - 3.4;
  const rimIn = Rout - 5.4;
  const hubR = motor ? 11 : 5;
  const tire = G.ringBand(-tireHalf, tireHalf, tireIn, Rout, F, P, { bevel: 0.5, steps: 56 });
  const rim = G.ringBand(-2.0, 2.0, rimIn, tireIn, F, P, { bevel: 0.3, steps: 56, hole: [2.0, rimIn] });
  const spokes = [];
  const spokeShapes = [];
  const count = 12;
  // les rayons sont posés sur la face avant de la jante (y = 2) : leurs bouts tombent sur son bord
  const onWheel = (r, i) => [C[0] + r * Math.cos((i / count) * Math.PI * 2), 2.0, C[2] + r * Math.sin((i / count) * Math.PI * 2)];
  for (let i = 0; i < count; i++) {
    const p0 = onWheel(hubR, i);
    const p1 = onWheel(rimIn, i);
    spokes.push(k.segment(onWheel(hubR - 2, i), p1, P));
    spokeShapes.push(A.tube([p0, p1], 0.3, { name: `${id}.spoke${i}`, owner: id }));
  }
  const rotor = `<g class="pv-rotor" data-wheel="${id}">${Ln(spokes.join(""), { tone: "lo" })}${Dots([at(onWheel(rimIn - 3, 0)), at(onWheel(hubR + 5, 5))], { size: 0.9, tone: "hi" })}</g>`;
  // moyeu : avant simple ; arrière = le moteur, un moyeu large et bagué
  const prof = motor ? [[-6.2, 9.4], [-5.5, 11], [5.5, 11], [6.2, 9.4]] : [[-3.4, 4.2], [-3, 5], [3, 5], [3.4, 4.2]];
  const face = motor ? 6.2 : 3.4;
  const hubSvg = S(G.solidOf(prof, F, P, { bevel: 0.25, steps: 32 }), { tone: "hi", inner: Ln(G.arcOf(F, motor ? 5.5 : 3, hubR, P), { tone: "faint" }) }) +
    Ln(G.circleOf(F, face, motor ? 7.2 : 3.2, P), { tone: "faint" }) +
    (motor ? Dots(G.dotsOf(F, face, 8.4, 10, P, { all: true }), { size: 0.55, tone: "mid" }) : "");
  const svg = S(tire, { tone: "mid", crease: "faint" }) + S(rim, { tone: "hi", crease: "faint" }) + rotor +
    (motor ? `<g class="pv-motor">${hubSvg}</g>` : hubSvg);
  put(id, C, svg, {
    name: `${id}.wheel`,
    shapes: [
      record(A.ring(F, -tireHalf, tireHalf, tireIn, Rout, { name: `${id}.tire`, owner: id })),
      record(A.ring(F, -2.0, 2.0, rimIn, tireIn, { name: `${id}.rim`, owner: id })),
      record(A.solid(F, prof, { name: `${id}.hub`, owner: id })),
      ...spokeShapes.map((sp) => record(sp)),
    ],
  });
  // bouts d'axe : du moyeu jusqu'aux boules du cadre
  const [stubR, y1] = motor ? [1.2, JY] : [1.0, 6.4];
  for (const sg of [1, -1]) {
    const Fs = G.frameAlong(C, [0, sg, 0]);
    const end = y1 - reach(BALL, stubR);
    const cuts = motor && sg === 1 ? [[face, CHAIN_Y0], [CHAIN_Y1, end]] : [[face, end]];
    for (const [a0, a1] of cuts) {
      const nm = R.nameFor(`${id}.stub`);
      put(id, G.add3(C, [0, (sg * (a0 + a1)) / 2, 0]), S(G.disc(a0, a1, stubR, Fs, P, { steps: 10 }), { tone: "mid" }), { name: nm, bias: 0.3, shapes: [record(A.disc(Fs, a0, a1, stubR, { name: nm, owner: id }))] });
    }
    if (motor && sg === 1) {
      const nm = R.nameFor(`${id}.sprocket`);
      put(id, G.add3(C, [0, (CHAIN_Y0 + CHAIN_Y1) / 2, 0]), S(G.disc(CHAIN_Y0, CHAIN_Y1, SPROCKET_R, Fs, P, { steps: 40 }), { tone: "mid", inner: Ln(G.circleOf(Fs, CHAIN_Y1, SPROCKET_R - 1.6, P), { tone: "faint" }) }),
        { name: nm, shapes: [record(A.disc(Fs, CHAIN_Y0, CHAIN_Y1, SPROCKET_R, { name: nm, owner: id }))] });
    }
  }
}

wheel("fw", FC, RF, { motor: false });
wheel("rw", RC, RR, { motor: true });

// ── Le cadre ──
const J = {};
J.rhP = joint("rh+", [0, JY, 33]);
J.rhM = joint("rh-", [0, -JY, 33]);
J.fhP = joint("fh+", [FC[0], 6.4, 27]);
J.fhM = joint("fh-", [FC[0], -6.4, 27]);
const s22 = steer(31);
const s30 = steer(39);
const s52 = steer(62);
J.fcP = joint("fc+", [s22[0], 6.4, s22[2]]);
J.fcM = joint("fc-", [s22[0], -6.4, s22[2]]);
J.fc0 = joint("fc0", s22);
J.hd = joint("hd", s30, 3.0);
J.top = joint("top", s52, 1.9);
const beamZ = (x) => s30[2] + ((x - s30[0]) * (34 - s30[2])) / (-70 - s30[0]);
J.p1 = joint("p1", [-130, 0, beamZ(-130)], 3.0);
J.p2 = joint("p2", [-96, 0, beamZ(-96)], 3.0);
J.b = joint("b", [-70, 0, 34], 3.0);
J.c = joint("c", BB, 3.6);
J.bbP = joint("bb+", [BB[0], 5, BB[2]]);
J.bbM = joint("bb-", [BB[0], -5, BB[2]]);
J.st0 = joint("st0", [-42, 0, 74]);
J.stP = joint("st+", [-42, 5, 74]);
J.stM = joint("st-", [-42, -5, 74]);
const onStay = (sg, x) => {
  const t = (x + 42) / 42;
  return [x, sg * (5 + (JY - 5) * t), 74 - 41 * t];
};
J.ssP = joint("ss+", onStay(1, -30));
J.ssM = joint("ss-", onStay(-1, -30));
J.sd = joint("sd", [-38.5, 0, 86], 1.9);
J.hb = joint("hb", [-70, 0, 98]);

strut(J.fhP, J.fcP, T, { name: "fork+" });
strut(J.fhM, J.fcM, T, { name: "fork-" });
strut(J.fcP, J.fc0, T, { name: "crown+" });
strut(J.fcM, J.fc0, T, { name: "crown-" });
strut(J.fc0, J.hd, 1.4, { name: "steer-low" });
strut(J.hd, J.top, 1.4, { name: "steer-up" });
strut(J.hd, J.p1, T, { name: "beam1" });
strut(J.p1, J.p2, T, { name: "beam2" });
strut(J.p2, J.b, T, { name: "beam3" });
strut(J.b, J.c, T, { name: "beam4" });
strut(J.c, J.bbP, T, { name: "bb+" });
strut(J.c, J.bbM, T, { name: "bb-" });
strut(J.c, J.st0, T, { name: "seat-tube" });
strut(J.st0, J.stP, T, { name: "cluster+" });
strut(J.st0, J.stM, T, { name: "cluster-" });
strut(J.st0, J.sd, 1.2, { name: "seat-post" });
strut(J.bbP, J.rhP, T, { name: "chainstay+" });
strut(J.bbM, J.rhM, T, { name: "chainstay-" });
strut(J.stP, J.ssP, T, { name: "seatstay+a" });
strut(J.ssP, J.rhP, T, { name: "seatstay+b" });
strut(J.stM, J.ssM, T, { name: "seatstay-a" });
strut(J.ssM, J.rhM, T, { name: "seatstay-b" });
strut(J.b, J.hb, T, { name: "column" });
strut(J.top, J.hb, 0.9, { name: "steer-rod", seam: false });
// guidon : deux tubes de part et d'autre de la boule, chacun fini par une poignée
for (const sg of [1, -1]) {
  const F = G.frameAlong(J.hb.pos, [0, sg, 0]);
  const s0 = reach(BALL, 1.1);
  const nm = R.nameFor("bike.bar");
  put("bike", G.add3(J.hb.pos, [0, sg * 9, 0]), S(G.disc(s0, 16, 1.1, F, P, { steps: 10 }), { tone: "mid" }), { name: nm, shapes: [record(A.disc(F, s0, 16, 1.1, { name: nm, owner: "bike" }))] });
  const gn = R.nameFor("bike.grip");
  put("bike", G.add3(J.hb.pos, [0, sg * 18.5, 0]), S(G.disc(16, 21, 1.8, F, P, { steps: 10 }), { tone: "hi" }), { name: gn, shapes: [record(A.disc(F, 16, 21, 1.8, { name: gn, owner: "bike" }))] });
}
// selle
slabItem("bike", { x: -48.5, y: -5.5, w: 20, d: 11, r: 4 }, J.sd.pos[2] + J.sd.r, 3, { tone: "hi", steps: 6, bevel: 0.8, name: "saddle", owner: "bike" });
// poteaux du plateau de caisse et du porte-bagages
for (const j of [J.p1, J.p2]) {
  const reachP = reach(3.0, 1.3);
  post(j.pos, [0, 0, 1], reachP, 62 - j.pos[2], 1.3, { name: "deck-post" });
}
for (const j of [J.ssP, J.ssM]) {
  post(j.pos, [0, 0, 1], reach(BALL, 1.3), 78 - j.pos[2], 1.3, { name: "rack-post" });
}

// ── Le porte-bagages ──
slabItem("rack", { x: -34, y: -8.5, w: 62, d: 17, r: 2 }, 78, 2, { tone: "mid", steps: 4, bevel: 0.5, name: "platform", owner: "bike",
  inner: "" , extra: Ln(k.planOutline(k.insetPlan({ x: -34, y: -8.5, w: 62, d: 17, r: 2 }, 2.4), 80, P), { tone: "faint" }) });

// ── La batterie (source) ──
{
  const plan = { x: -8, y: -6, w: 34, d: 12, r: 2 };
  const zb = 80;
  const hb = 14;
  const seam = Ln(k.sideSeam(plan, zb + 9, P, 4), { tone: "faint" });
  const top = [
    Ln(k.planOutline(k.insetPlan(plan, 2.4), zb + hb, P), { tone: "faint" }),
    Dots([at([-4, -3.4, zb + hb]), at([-4, 3.4, zb + hb]), at([22, -3.4, zb + hb]), at([22, 3.4, zb + hb])], { size: 0.5, tone: "mid" }),
  ].join("");
  const bat = `<g class="pv-bat">` + S(k.slabOf(plan, zb, hb, P, 4, 0.8), { tone: "hi", inner: seam }) + top + `</g>`;
  // la serrure, sur le dessus
  const lock = S(k.cylinder(18, 0, 2.2, zb + hb, 1.2, P, 20), { tone: "mid" }) + Ln(k.lineOnTop([15.8, 0], [20.2, 0], zb + hb + 1.2, P), { tone: "hi" });
  const id = R.nameFor("bat.body");
  put("bat", [plan.x + plan.w / 2, 0, zb + hb / 2], `<g class="pv-bat">` + S(k.slabOf(plan, zb, hb, P, 4, 0.8), { tone: "hi", inner: seam }) + top + `</g>`, { name: id, shapes: [record(A.slab(plan, zb, hb, { name: id, owner: "bat" }, 4))] });
  const lk = R.nameFor("bat.lock");
  put("bat", [18, 0, zb + hb + 0.6], `<g class="pv-bat">` + lock + `</g>`, { name: lk, bias: 0.2, shapes: [record(A.cylinder(18, 0, 2.2, zb + hb, 1.2, { name: lk, owner: "bat" }))] });
  // embase de la prise, sur la face qui regarde le spectateur
  const F = G.frameAlong([18, 6, 87], [0, 1, 0]);
  const end = JY - reach(BALL, 1.4) - 6;
  const nb = R.nameFor("bat.boss");
  put("bat", [18, 6 + end / 2, 87], `<g class="pv-bat">` + S(G.disc(0, end, 1.4, F, P, { steps: 10 }), { tone: "mid" }) + `</g>`, { name: nb, bias: 0.2, shapes: [record(A.disc(F, 0, end, 1.4, { name: nb, owner: "bat" }))] });
}

// ── Le contrôleur de puissance, fixé entre la batterie et le moyeu moteur ──
{
  const plan = { x: 14, y: 8, w: 8, d: 7, r: 0.8 };
  const id = R.nameFor("controller.body");
  const fins = [60, 63, 66].map((z) => Ln(k.sideSeam(plan, z, P, 3), { tone: "mid" })).join("");
  put("controller", [18, JY, 64], `<g class="pv-controller"><title>Contrôleur de puissance</title>` + S(k.slabOf(plan, 57, 14, P, 3, 0.4), { tone: "hi", inner: fins }) + `</g>`,
    { name: id, shapes: [record(A.slab(plan, 57, 14, { name: id, owner: "controller" }, 3))] });
}

// ── Deux câbles : batterie → contrôleur, puis contrôleur → moyeu moteur ──
const CABLE_R = 0.8;
const plugPos = [18, JY, 87];
{
  const id = R.nameFor("cable.plug");
  put("cable", plugPos, `<g class="pv-cable">` + S(G.sphereOf(plugPos, BALL, P, { steps: 14 }), { tone: "hi" }) + `</g>`, { name: id, bias: 0.25, shapes: [record(A.ball(plugPos, BALL, { name: id, owner: "bat" }))] });
  const paths = [
    [[18, JY, plugPos[2] - BALL], [18, JY, 71]],
    [[18, JY, 57], [18, JY, 33], [BALL, JY, 33]],
  ];
  paths.forEach((pts, segment) => {
  const route = G.fillet(pts, 6, 12, { P, tube: CABLE_R });
  R.route("cable", route, CABLE_R, { owner: "cable", piece: "cable", ride: "cable" });
  tubePieces(route, CABLE_R, P, { maxLength: 14, spacing: 1 }).forEach((part, index) =>
    put("cable", part.mid, `<g class="pv-cable">` + tubeSvg(part, { tone: "hi" }) + `</g>`, { bias: 0.2, name: `cable:${segment}:${index}`, shapes: [A.tube(part.points, part.radii)] }),
  );
  });
}

// ── Pédalier : bras et pédales (tournent à la scène 5) ──
const ARM = 17.5;
const cranks = {};
for (const sg of [1, -1]) {
  const a0 = sg === 1 ? -65 : 115;
  const c = Math.cos(a0 * DEG);
  const s = Math.sin(a0 * DEG);
  const y0 = sg * 9.6;
  const tip = [BB[0] + ARM * c, BB[2] + ARM * s];
  // entretoise de l'axe de pédalier : de la boule jusqu'au bras
  // côté chaîne, l'entretoise est coupée par le plateau
  const Fb = G.frameAlong([BB[0], sg * (5 + BALL), BB[2]], [0, sg, 0]);
  const y9 = 9.6 - (5 + BALL);
  const cuts = sg === 1 ? [[0, CHAIN_Y0 - (5 + BALL)], [CHAIN_Y1 - (5 + BALL), y9]] : [[0, y9]];
  for (const [a0, a1] of cuts) {
    const nbb = R.nameFor("crank.axle");
    put("crank", [BB[0], sg * (5 + BALL + (a0 + a1) / 2), BB[2]], S(G.disc(a0, a1, 2.0, Fb, P), { tone: "mid" }), { name: nbb, shapes: [record(A.disc(Fb, a0, a1, 2.0, { name: nbb, owner: "crank" }))] });
  }
  if (sg === 1) {
    const Fr = G.frameAlong(BB, [0, 1, 0]);
    const nr = R.nameFor("crank.ring");
    put("crank", [BB[0], (CHAIN_Y0 + CHAIN_Y1) / 2, BB[2]], S(G.disc(CHAIN_Y0, CHAIN_Y1, RING_R, Fr, P, { steps: 48 }), { tone: "mid", inner: Ln(G.circleOf(Fr, CHAIN_Y1, RING_R - 2.2, P), { tone: "faint" }) }),
      { name: nr, shapes: [record(A.disc(Fr, CHAIN_Y0, CHAIN_Y1, RING_R, { name: nr, owner: "crank" }))] });
  }
  // bras
  const Fa = G.frameOf([BB[0], y0, BB[2]], [0, sg, 0], [c, 0, s], [sg * s, 0, -sg * c]);
  const poly = G.stadium(2.6, 1.9, ARM);
  const arm = G.prismOf(Fa, poly, 0, 1.2, P);
  const na = R.nameFor("crank.arm");
  const armHub = Ln(G.circleOf(Fa, sg * 1.2 > 0 ? 1.2 : 0, 1.0, P), { tone: "faint" });
  put("crank", [(BB[0] + tip[0]) / 2, y0, (BB[2] + tip[1]) / 2], `<g class="pv-arm" data-side="${sg}">` + S(arm, { tone: "hi" }) + `</g>`, { name: na, bias: 0.4, shapes: [record(A.prism(Fa, poly, 0, 1.2, { name: na, owner: "crank" }))] });
  // axe de pédale + pédale (la pédale reste à plat : elle se translate, elle ne tourne pas)
  const yf = y0 + sg * 1.2;
  const Fp = G.frameAlong([tip[0], yf, tip[1]], [0, sg, 0]);
  const planP = { x: tip[0] - 4.5, y: sg === 1 ? 11.4 : -16.4, w: 9, d: 5, r: 1 };
  const nsp = R.nameFor("crank.spindle");
  const spindle = S(G.disc(0, 1.2, 0.8, Fp, P, { steps: 10 }), { tone: "mid" });
  const pedal = S(k.slabOf(planP, tip[1] - 0.7, 1.4, P, 3, 0.3), { tone: "hi" });
  put("crank", [tip[0], sg * 13, tip[1]], `<g class="pv-pedal" data-side="${sg}">` + spindle + pedal + `</g>`, {
    name: nsp, bias: 0.5,
    shapes: [record(A.disc(Fp, 0, 1.2, 0.8, { name: nsp, owner: "crank" })), record(A.slab(planP, tip[1] - 0.7, 1.4, { name: R.nameFor("crank.pedal"), owner: "crank" }, 3))],
  });
  cranks[sg] = { tip, a0 };
}

// ── La chaîne, simplifiée : deux brins droits, tangents au plateau et au pignon, posés sur leurs faces ──
{
  const r1 = RING_R - 0.8;
  const r2 = SPROCKET_R - 0.8;
  const c1 = [BB[0], BB[2]];
  const c2 = [RC[0], RC[2]];
  const d = [c2[0] - c1[0], c2[1] - c1[1]];
  const L = Math.hypot(d[0], d[1]);
  const base = Math.atan2(d[1], d[0]);
  const phi = Math.acos((r1 - r2) / L);
  for (const [sg, nm] of [[1, "top"], [-1, "bottom"]]) {
    const n = [Math.cos(base + sg * phi), Math.sin(base + sg * phi)];
    const a = [c1[0] + r1 * n[0], c1[1] + r1 * n[1]];
    const b = [c2[0] + r2 * n[0], c2[1] + r2 * n[1]];
    const len = Math.hypot(b[0] - a[0], b[1] - a[1]);
    const u = [(b[0] - a[0]) / len, 0, (b[1] - a[1]) / len];
    const F = G.frameOf([a[0], CHAIN_Y1, a[1]], [0, 1, 0], u, [u[2], 0, -u[0]]);
    const poly = G.stadium(0.75, 0.75, len);
    const id = R.nameFor(`chain.${nm}`);
    put("chain", [(a[0] + b[0]) / 2, CHAIN_Y1 + CHAIN_T / 2, (a[1] + b[1]) / 2], S(G.prismOf(F, poly, 0, CHAIN_T, P), { tone: "mid" }),
      { name: id, shapes: [record(A.prism(F, poly, 0, CHAIN_T, { name: id, owner: "crank" }))] });
  }
}

// ── La caisse : plateau, quatre parois basses, le colis et son ruban ──
{
  const deck = { x: -142, y: -14, w: 64, d: 28, r: 2 };
  slabItem("bac", deck, 62, 2, { tone: "mid", steps: 4, bevel: 0.5, name: "deck", owner: "bike" });
  const walls = [
    { x: -142, y: -14, w: 1.4, d: 28, r: 0.4, n: "front" },
    { x: -79.4, y: -14, w: 1.4, d: 28, r: 0.4, n: "rear" },
    { x: -142, y: -14, w: 64, d: 1.4, r: 0.4, n: "left" },
    { x: -142, y: 12.6, w: 64, d: 1.4, r: 0.4, n: "right" },
  ];
  for (const w of walls) slabItem("bac", w, 64, 14, { tone: "mid", steps: 2, bevel: 0.3, name: `wall-${w.n}`, owner: "bike" });
  const colis = { x: -126, y: -10.5, w: 32, d: 21, r: 1.2 };
  const ruban = Ln(k.rise([-111, 10.5], 64, 86, P), { tone: "mid" });
  slabItem("colis", colis, 64, 22, { tone: "hi", steps: 3, bevel: 0.5, name: "parcel", owner: "colis", extra: ruban });
  slabItem("colis", { x: -113, y: -10.5, w: 4, d: 21, r: 0.3 }, 86, 0.5, { tone: "mid", steps: 2, bevel: 0, name: "tape", owner: "colis", crease: "none" });
}

// ── Tri de peinture ──
A.settle(R, P);
R.items.sort((a, b) => a.key - b.key);

// ── Flèche d'énergie mécanique (symbole de la scène 5), dans le plan de la roue arrière ──
const arrowArc = (() => {
  const r = 38;
  const y = 14;
  const pts = [];
  for (let a = -50; a <= 45; a += 5) pts.push(at([RC[0] + r * Math.cos(a * DEG), y, RC[2] + r * Math.sin(a * DEG)]));
  const tipA = 45 * DEG;
  const tan = [-Math.sin(tipA), Math.cos(tipA)]; // sens du mouvement (anti-horaire dans le plan x–z)
  const nor = [Math.cos(tipA), Math.sin(tipA)];
  const hp = (u, v) => at([RC[0] + r * Math.cos(tipA) + u * tan[0] + v * nor[0], y, RC[2] + r * Math.sin(tipA) + u * tan[1] + v * nor[1]]);
  const head = [hp(8, 0), hp(-2, 5), hp(-2, -5)];
  return { line: "M" + pts.map(([x, y2]) => `${x.toFixed(1)} ${y2.toFixed(1)}`).join("L"), head: "M" + head.map(([x, y2]) => `${x.toFixed(1)} ${y2.toFixed(1)}`).join("L") + "Z" };
})();

// ── Repères pour la page : matrices du plan de la roue, caméras des scènes ──
const o = at([0, 0, 0]);
const ex = at([1, 0, 0]).map((v, i) => v - o[i]);
const ez = at([0, 0, 1]).map((v, i) => v - o[i]);
const screenOf = (p) => at(p);
const hub = screenOf(RC);
const bat = screenOf([9, 0, 87]);
const cab = screenOf([10, JY, 60]);
// enveloppe du vélo à l'écran : roues, guidon, selle, batterie, caisse, pédales
const hull = [];
for (const [C, r] of [[FC, RF], [RC, RR]]) for (let i = 0; i < 72; i++) for (const y of [-3, 3]) hull.push(at([C[0] + r * Math.cos((i / 72) * Math.PI * 2), y, C[2] + r * Math.sin((i / 72) * Math.PI * 2)]));
for (const p of [[-70, 21, 101], [-70, -21, 101], s52, [-142, -14, 78], [-142, 14, 78], [-78, -14, 78], [-78, 14, 78], [-34, -8.5, 80], [28, 8.5, 80], [26, 6, 96], [-8, -6, 96], [BB[0], 16.4, BB[2] - ARM], [BB[0], -16.4, BB[2] + ARM]]) hull.push(at(p));
const bx = [Math.min(...hull.map((q) => q[0])), Math.max(...hull.map((q) => q[0]))];
const by = [Math.min(...hull.map((q) => q[1])), Math.max(...hull.map((q) => q[1]))];
// échelle telle que le rectangle du vélo couvre FILL de la surface du cadre, sans toucher ses bords
const FILL = 0.6;
const frameCam = (h, cy) => {
  const bw = bx[1] - bx[0];
  const bh = by[1] - by[0];
  const s = Math.min(Math.sqrt((FILL * W * h) / (bw * bh)), (W - 40) / bw, (h - 28) / bh);
  return [(bx[0] + bx[1]) / 2, (by[0] + by[1]) / 2, +s.toFixed(3), cy];
};
const CAM = {
  1: frameCam(H, H / 2),
  5: frameCam(H, H / 2),
  6: frameCam(CAM_H, CAM_H / 2),
  2: [bat[0], bat[1], 2.3],
  3: [(screenOf([18, JY, 85])[0] + hub[0]) / 2, (screenOf([18, JY, 85])[1] + hub[1]) / 2, 1.7],
  4: [hub[0], hub[1], 2.4],
};

// ── Le dessin ──
const body = [
  back.join(""),
  ...R.items.map((it) => it.svg),
  `<g class="pv-fleche vpp-meca-g" data-des="5"><path class="iso-line pv-fl" data-free="start" d="${arrowArc.line}"/><path class="pv-fl-tete" d="${arrowArc.head}"/></g>`,
].join("");
const dessin = `<g class="iso-g">${body}</g>`;

// ── CSS ──
const hex = (c) => [1, 3, 5].map((i) => parseInt(c.slice(i, i + 2), 16));
const toHex = (v) => "#" + v.map((n) => Math.round(Math.max(0, Math.min(255, n))).toString(16).padStart(2, "0")).join("");
const mix = (a, b, t) => toHex(hex(a).map((v, i) => v + (hex(b)[i] - v) * t));
const BG = "#050f24";
const ramp = (c, strength) => {
  const base = mix(BG, c, strength);
  return {
    "--anatomy-paper": mix(BG, c, strength * 0.35),
    "--anatomy-face": mix(BG, c, strength * 0.55),
    "--anatomy-shade-0": mix(BG, c, strength * 0.38),
    "--anatomy-shade-1": mix(BG, c, strength * 0.55),
    "--anatomy-shade-2": mix(BG, c, strength * 0.72),
    "--anatomy-shade-3": mix(BG, c, strength * 0.88),
    "--anatomy-top": base,
    "--anatomy-hi": mix(c, "#ffffff", 0.35),
    "--anatomy-mid": c,
    "--anatomy-lo": mix(BG, c, 0.55),
    "--anatomy-faint": mix(BG, c, 0.3),
  };
};
const decl = (o2) => Object.entries(o2).map(([n, v]) => `${n}:${v}`).join(";");
// état d'une pièce selon la scène : allumée (« on »), déjà vue (« was »), éteinte
const STATES = {
  bat: { c: COULEUR.source, on: [2, 6], was: [3, 4, 5] },
  cable: { c: COULEUR.elec, on: [3, 6], was: [4, 5] },
  controller: { c: COULEUR.elec, on: [3, 6], was: [4, 5] },
  motor: { c: COULEUR.moteur, on: [4, 6], was: [5] },
};
let css = "";
for (const [cls, st] of Object.entries(STATES)) {
  const sel = (list) => list.map((n) => `.vpp[data-scene="${n}"] .pv-${cls}`).join(",");
  css += `${sel(st.on)}{${decl(ramp(st.c, 1))}}\n`;
  css += `${sel(st.was)}{${decl(ramp(st.c, 0.42))}}\n`;
}
// seule la roue arrière est entraînée par le moteur : seule elle prend le vert de l'énergie mécanique
const rouesVertes = [5, 6].map((n) => `.vpp[data-scene="${n}"] .pv-rotor[data-wheel="rw"]`).join(",");
css += `${rouesVertes}{--anatomy-lo:${mix(BG, COULEUR.meca, 0.7)};--anatomy-hi:${COULEUR.meca}}\n`;
css += `.pv-fl{stroke:${COULEUR.meca};stroke-width:3;fill:none;stroke-linecap:round}\n.pv-fl-tete{fill:${COULEUR.meca};stroke:${COULEUR.meca};stroke-width:1.5;stroke-linejoin:round}\n`;
css += `.vpp[data-scene="4"] .pv-motor{animation:vppLueur 1.4s ease-in-out infinite alternate}\n`;
const ROUTE = { top: "#0d2042", rive: "#4b6597", tiret: "#a9c0e9" };
css += `.pv-route{--anatomy-top:${ROUTE.top};--anatomy-face:${ROUTE.top};--anatomy-shade-0:#0a1a37;--anatomy-shade-1:#0b1c3b;--anatomy-shade-2:#0c1e3f;--anatomy-shade-3:#0d2042;--anatomy-mid:${ROUTE.top}}.pv-rive{fill:${ROUTE.rive}}.pv-tiret{fill:${ROUTE.tiret}}
`;
css += `.vpp .iso-fill,.vpp .iso-shade,.vpp .iso-top{transition:fill .6s ease}\n`;
css += `@media (prefers-reduced-motion: reduce){.vpp .iso-fill,.vpp .iso-shade,.vpp .iso-top{transition:none}.vpp[data-scene="4"] .pv-motor{animation:none}}\n`;
const NEUTRE = { face: "#1c3c72", top: "#3f6db2", s0: "#183466", s1: "#20427c", s2: "#2a5192", s3: "#3561a6", hi: "#e2eafa", mid: "#a9c0e9", lo: "#7593c9", faint: "#4669aa" };
const TOKENS = `.iso-g{--anatomy-paper:${BG};--anatomy-face:${NEUTRE.face};--anatomy-top:${NEUTRE.top};--anatomy-shade-0:${NEUTRE.s0};--anatomy-shade-1:${NEUTRE.s1};--anatomy-shade-2:${NEUTRE.s2};--anatomy-shade-3:${NEUTRE.s3};--anatomy-hi:${NEUTRE.hi};--anatomy-mid:${NEUTRE.mid};--anatomy-lo:${NEUTRE.lo};--anatomy-faint:${NEUTRE.faint};--anatomy-dot:#c9d6ee;--anatomy-halo:#02081a;--anatomy-halo-opacity:.9;--anatomy-weight:.9px}\n`;

// ── Quatre fonctions, composants dessous et énergies sur les flèches ──
const band = readFileSync(join(HERE, "bande_quatre_cases.svg.fragment"), "utf8").replace(/\r\n/g, "\n");
const bandCss = readFileSync(join(HERE, "bande_quatre_cases.css"), "utf8").replace(/\r\n/g, "\n");

const svgInner = `<defs><clipPath id="vppClip"><rect x="0" y="0" width="${W}" height="${CAM_H}"/></clipPath></defs><rect width="${W}" height="${H}" fill="${BG}"/><g clip-path="url(#vppClip)"><g class="vpp-cam" id="vppCam">${dessin}</g></g>${band}`;
const svg = `<svg class="vpp-dessin iso-svg" data-loupe="non" viewBox="0 0 ${W} ${H}" aria-hidden="true" focusable="false" font-family="Segoe UI, system-ui, -apple-system, Helvetica Neue, Arial, sans-serif">${svgInner}</svg>`;

console.log("items", R.items.length, "· dessin", (Buffer.byteLength(dessin) / 1024).toFixed(1), "Ko");

// ── Page d'essai : le lecteur de la page, recopié, et la rotation en JavaScript ──
const live = `
(function(){
  var M = [${ex[0]}, ${ex[1]}, ${ez[0]}, ${ez[1]}];       // colonnes : x et z du monde, vus à l'écran
  var det = M[0]*M[3] - M[2]*M[1];
  var HUB = {rw: ${JSON.stringify(screenOf([RC[0], 2, RC[2]]))}, fw: ${JSON.stringify(screenOf([FC[0], 2, FC[2]]))}};   // centre des rayons : sur la face avant de la jante
  var ARMC = {"1": ${JSON.stringify(screenOf([BB[0], 9.6, BB[2]]))}, "-1": ${JSON.stringify(screenOf([BB[0], -9.6, BB[2]]))}};
  var BBs = ${JSON.stringify(screenOf(BB))};
  // rotation d'angle t dans le plan de la roue (x, z), vue à l'écran : A = M R M⁻¹
  function mat(t, c){
    var co = Math.cos(t), si = Math.sin(t);
    var r = [co, si, -si, co];                              // R en colonnes : (co, si), (-si, co)
    var a = M[0]*r[0] + M[2]*r[1], b = M[1]*r[0] + M[3]*r[1];
    var cc = M[0]*r[2] + M[2]*r[3], d = M[1]*r[2] + M[3]*r[3];
    var iv = [M[3]/det, -M[1]/det, -M[2]/det, M[0]/det];
    var A = [a*iv[0] + cc*iv[1], b*iv[0] + d*iv[1], a*iv[2] + cc*iv[3], b*iv[2] + d*iv[3]];
    return {A: A, e: c[0] - (A[0]*c[0] + A[2]*c[1]), f: c[1] - (A[1]*c[0] + A[3]*c[1])};
  }
  var cranks = ${JSON.stringify(Object.fromEntries(Object.entries(cranks).map(([s, v]) => [s, v.tip])))};
  var bloc = document.getElementById("velo-cargo-pas-a-pas");
  var still = matchMedia("(prefers-reduced-motion: reduce)");
  var rotors = bloc.querySelectorAll(".pv-rotor"), arms = bloc.querySelectorAll(".pv-arm"), pedals = bloc.querySelectorAll(".pv-pedal"), dashes = bloc.querySelector(".pv-tirets");
  var raf = 0, t0 = 0;
  function pose(a){
    rotors.forEach(function(g){ var w = g.getAttribute("data-wheel"), m = mat(w === "fw" ? a * ${RR / RF} : a, HUB[w]); g.setAttribute("transform", "matrix("+m.A[0]+" "+m.A[1]+" "+m.A[2]+" "+m.A[3]+" "+m.e+" "+m.f+")"); });
    // la route recule d'un arc de roue arrière : a × ${RR} cm, modulo la période des tirets
    var sh = ((a * ${RR}) % ${DASH} + ${DASH}) % ${DASH};
    dashes.setAttribute("transform", "translate(" + (M[0] * sh) + " " + (M[1] * sh) + ")");
    var mc = mat(a * 0.7, BBs);
    arms.forEach(function(g){ var m = mat(a * 0.7, ARMC[g.getAttribute("data-side")]); g.setAttribute("transform", "matrix("+m.A[0]+" "+m.A[1]+" "+m.A[2]+" "+m.A[3]+" "+m.e+" "+m.f+")"); });
    pedals.forEach(function(g){ var tip = cranks[g.getAttribute("data-side")], p = [BBs[0] + M[0]*(tip[0]-(${BB[0]})) + M[2]*(tip[1]-(${BB[2]})), BBs[1] + M[1]*(tip[0]-(${BB[0]})) + M[3]*(tip[1]-(${BB[2]}))];
      var q = [mc.A[0]*p[0] + mc.A[2]*p[1] + mc.e, mc.A[1]*p[0] + mc.A[3]*p[1] + mc.f];
      g.setAttribute("transform", "translate("+(q[0]-p[0])+" "+(q[1]-p[1])+")"); });
  }
  function tourne(now){
    if (!t0) t0 = now;
    pose(((now - t0) / 6000) * Math.PI * 2);
    raf = bloc.getAttribute("data-scene") === "5" && !still.matches ? requestAnimationFrame(tourne) : 0;
  }
  new MutationObserver(function(){
    var s = bloc.getAttribute("data-scene");
    if (s === "5" && !still.matches && !raf) { t0 = 0; raf = requestAnimationFrame(tourne); }
    if (s !== "5") { cancelAnimationFrame(raf); raf = 0; pose(0); }
  }).observe(bloc, {attributes: true, attributeFilter: ["data-scene"]});
})();
`;

// ── Écriture dans la séquence, entre les marqueurs (le reste de la page n'est jamais touché) ──
const kept = k.ISO_CSS.split("\n").filter((l) => /^\.(iso-fill|iso-shade|iso-top|iso-solid|iso-line|iso-dots|iso-halo|iso-svg|tb-)/.test(l)).join("\n");
const pageCss = `${kept}\n${TOKENS}${css}\n${bandCss}`;
const cameraJs = `var CAMERA = ${JSON.stringify(CAM)}, VUE_H = ${H}, CADRE_H = ${CAM_H};`;
{
  const brut = readFileSync(PAGE, "utf8");
  const eol = brut.includes("\r\n") ? "\r\n" : "\n";
  let page = brut.replace(/\r\n/g, "\n");
  const entre = (debut, fin, corps) => {
    const i = page.indexOf(debut);
    const j = page.indexOf(fin, i);
    if (i < 0 || j < 0) throw new Error(`marqueurs absents : ${debut}`);
    page = page.slice(0, i + debut.length) + "\n" + corps + "\n" + page.slice(j);
  };
  entre("<!-- figure_iso_velo_cargo : début -->", "<!-- figure_iso_velo_cargo : fin -->", svg);
  entre("/* figure_iso_velo_cargo (style) : début */", "/* figure_iso_velo_cargo (style) : fin */", pageCss);
  entre("// figure_iso_velo_cargo (caméra) : début", "// figure_iso_velo_cargo (caméra) : fin", cameraJs);
  entre("<!-- figure_iso_velo_cargo (rotation) : début -->", "<!-- figure_iso_velo_cargo (rotation) : fin -->", `<script>${live}</script>`);
  writeFileSync(PAGE, page.replace(/\n/g, eol));
  console.log("page : dessin", (Buffer.byteLength(svg) / 1024).toFixed(1), "Ko · style", (Buffer.byteLength(pageCss) / 1024).toFixed(1), "Ko · rotation", (Buffer.byteLength(live) / 1024).toFixed(1), "Ko");
}

A.auditOrExit(R, P, { argv: [...process.argv, "--audit"] });
if (process.exitCode) process.exit(process.exitCode);

if (process.argv.includes("--poids")) {
  const rows = R.items.map((it) => [Buffer.byteLength(it.svg), it.name]).sort((a, b) => b[0] - a[0]);
  const byGroup = {};
  for (const [n, name] of rows) { const g = name.split(/[.:]/)[0] + "." + (name.split(".")[1] || "").split(/[0-9:]/)[0]; byGroup[g] = (byGroup[g] || 0) + n; }
  console.log(rows.slice(0, 14).map(([n, name]) => `${(n / 1024).toFixed(1)} Ko  ${name}`).join("\n"));
  console.log(Object.entries(byGroup).sort((a, b) => b[1] - a[1]).slice(0, 10).map(([g, n]) => `${(n / 1024).toFixed(1)} Ko  ${g}`).join("\n"));
}

// ── Le schéma fixe (= scène 6) : un SVG autonome, avec <title> et <desc> ──
{
  const sixOnly = css.split("\n").filter((l) => l.includes('data-scene="6"') && !l.includes("@media")).map((l) => l.replace(/\.vpp\[data-scene="[\d"\],.\[a-z=\-\s]*?\](\s+[^,{]+)/g, "$1")).join("\n");
  const fixe = `<svg xmlns="http://www.w3.org/2000/svg" class="iso-svg vpp" data-scene="6" viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="t d" font-family="Segoe UI, system-ui, -apple-system, Helvetica Neue, Arial, sans-serif">
<title id="t">La chaîne d'énergie du vélo-cargo</title>
<desc id="d">L’assistance électrique du vélo-cargo : la batterie stocke de l’énergie chimique et fournit de l’énergie électrique au contrôleur de puissance, dessiné entre la batterie et le moteur du moyeu arrière. Le moteur convertit l’énergie électrique en énergie mécanique et entraîne la roue. Le bandeau distingue les fonctions ALIMENTER, DISTRIBUER, CONVERTIR et TRANSMETTRE, les composants en dessous et les formes d’énergie sur les flèches. L’effort du cycliste n’est pas représenté.</desc>
<style>${TOKENS}${kept}\n${css.split("\n").filter((l) => !l.includes("@media") && !l.includes("vppLueur") && !l.includes("transition")).join("\n")}\n${bandCss}</style>
<defs><clipPath id="fixeClip"><rect width="${W}" height="${CAM_H}"/></clipPath></defs><rect width="${W}" height="${H}" fill="${BG}"/><g clip-path="url(#fixeClip)"><g transform="translate(${410 - CAM[6][0] * CAM[6][2]} ${CAM[6][3] - CAM[6][1] * CAM[6][2]}) scale(${CAM[6][2]})">${dessin}</g></g>${band}</svg>`;
  writeFileSync(FIXE, fixe);
  console.log("schéma fixe", (Buffer.byteLength(fixe) / 1024).toFixed(1), "Ko");
}
