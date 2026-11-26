// Les trois freins de 5e_C1.2 (patins, disque, tambour) sur la même roue, en figure isométrique.
// Skill « anatomy » de Pascal : kit Anatomy (github.com/wheresryan22/anatomy, licence MIT © 2026 Ryan),
// commit audité 1482e8469b0a9e0d8cc18ea2740a01423d29ae80. Le kit n'est pas versé dans le dépôt :
//   ANATOMY_DIR=~/.cache/anatomy-1482e84 node build.mjs          → ../../Images/freins_iso.html (+ planche fixe)
// Le monde est en millimètres : x vers l'avant du vélo, y à travers la roue (vers l'élève), z vers le haut.
import { writeFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { homedir, tmpdir } from "node:os";

const KIT = process.env.ANATOMY_DIR || join(homedir(), ".cache", "anatomy-1482e84");
const k = await import(pathToFileURL(join(KIT, "kit/iso-kit.mjs")).href);
const G = await import(pathToFileURL(join(KIT, "kit/lathe.mjs")).href);
const { kitScript } = await import(pathToFileURL(join(KIT, "scripts/inline-kit.mjs")).href);

const ICI = dirname(fileURLToPath(import.meta.url));
const IMAGES = join(ICI, "..", "..", "Images");

// ── Les cotes, toutes vraies ──────────────────────────────────────────────────
// Roue de 26 pouces (ETRTO 559) : pneu Ø 660 mm, jante Ø 536 à 592 mm.
// Patins : ils pincent les flancs de la jante, à 285 mm de l'axe ; écart au repos 2 mm (relevé de la séquence).
// Disque : Ø 160 mm ; les plaquettes frottent sur la couronne, à 70 mm de l'axe ; écart moins d'1 mm.
// Tambour : Ø intérieur 70 mm ; les mâchoires frottent à 35 mm de l'axe ; écart environ 1 mm.
const R_PNEU = 330, R_PNEU_IN = 293, L_PNEU = 22;
const R_JANTE = 296, R_JANTE_IN = 268, L_JANTE = 10, R_PISTE = 285;
const AXE = [0, 0, R_PNEU];
const FW = G.frameOf(AXE, [0, 1, 0], [0, 0, 1], [1, 0, 0]);       // angle 0 en haut, vers l'avant (+x)
const W = (r, a, s) => G.pointOf(FW, s, r, a);
const DEG = Math.PI / 180;
const FOURCHE_Y = 52, FOURCHE_R = 11, TE_Z = 720;
const DISQUE = { s: 34, rIn: 55, rOut: 80, piste: 70 };
const TAMBOUR = { s0: 22, s1: 40, rExt: 42, rIn: 35, flasque: 3 };

const FREINS = {
  patins: { nom: "Frein à patins", court: "patins", contact: "28,5 cm", ecart: "2 mm", rayon: R_PISTE },
  disque: { nom: "Frein à disque", court: "disque", contact: "7 cm", ecart: "moins d'1 mm", rayon: DISQUE.piste },
  tambour: { nom: "Frein à tambour", court: "tambour", contact: "3,5 cm", ecart: "environ 1 mm", rayon: TAMBOUR.rIn },
};

// ── Petits outils ─────────────────────────────────────────────────────────────
const S = (paths, style = {}) => k.solidSvg(paths, style);
const L = (d, style = {}) => k.lineSvg(d, style);
const pathOf3 = (pts, P, closed = false) => k.pathOf(pts.map((p) => k.iso(p, P)), closed);
const grp = (attrs, body) => `<g ${Object.entries(attrs).map(([a, v]) => `${a}="${v}"`).join(" ")}>${body}</g>`;
const pin = (n, at, P) => {
  const [x, y] = k.iso(at, P);
  return `<g class="fr-pin" data-n="${n}"><circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="8.6"/><text x="${x.toFixed(1)}" y="${y.toFixed(1)}">${n}</text></g>`;
};

// un grand anneau (pneu, jante) : les facettes visibles, puis ses contours tracés à part, plus légers que l'enveloppe du kit
function anneau(s, rIn, rOut, P, tone, crease) {
  const corps = S(G.ringBand(-s, s, rIn, rOut, FW, P, { fill: "facets", steps: 64 }), { tone, crease });
  const bords = G.circleOf(FW, s, rOut, P, 120) + G.circleOf(FW, s, rIn, P, 120) + G.arcOf(FW, -s, rOut, P, { steps: 90 }) + G.arcOf(FW, -s, rIn, P, { steps: 90, inward: true });
  return corps + L(bords, { tone: "hi" });
}

// ── La scène, pour une projection P ──────────────────────────────────────────
function sol(P) {
  const plan = { x: -360, y: -150, w: 720, d: 300, r: 10 };
  const out = [S(k.slabOf(plan, -6, 6, P, 6, 0), { tone: "lo", flat: true })];
  for (let x = plan.x + 120; x < plan.x + plan.w; x += 120) out.push(L(k.lineOnTop([x, plan.y], [x, plan.y + plan.d], 0, P), { tone: "faint" }));
  return out.join("");
}

// le range-vélo : deux plaques qui tiennent le pneu (celles des vélos garés sous l'auvent)
function ratelier(P, cote) {
  const y = cote > 0 ? 27 : -33;
  const plaque = { x: -150, y, w: 300, d: 6, r: 2 };
  const out = [S(k.slabOf(plaque, 0, 120, P, 3, 0.6), { tone: "mid" })];
  out.push(L(k.sideSeam(plaque, 104, P, 3), { tone: "faint" }));
  if (cote > 0) out.push(k.dotsSvg(k.pointsAt([[-130, y + 6, 112], [130, y + 6, 112]], P), { size: 0.5 }));
  return out.join("");
}

function rayons(P, cote) {
  const out = [];
  const sF = cote * 28, rF = 26;
  for (let i = 0; i < 16; i++) {
    const a = (i * 22.5 + (cote > 0 ? 0 : 11.25)) * DEG;
    out.push(pathOf3([W(rF, a, sF), W(R_JANTE_IN + 1, a + cote * 9 * DEG, cote * 2)], P));
  }
  return L(out.join(""), { tone: cote > 0 ? "mid" : "lo" });
}

function moyeu(P, frein) {
  const out = [];
  out.push(S(G.disc(-56, 56, 4.5, FW, P), { tone: "mid" }));                 // l'axe
  out.push(S(G.disc(-30, -26, 26, FW, P), { tone: "mid" }));                 // flasque de rayons, côté loin
  out.push(S(G.disc(-26, frein === "tambour" ? TAMBOUR.s0 : 26, 13, FW, P), { tone: "mid" }));  // le corps du moyeu
  if (frein !== "tambour") out.push(S(G.disc(26, 30, 26, FW, P), { tone: "mid" }));
  return out.join("");
}

function disque(P) {
  const out = [];
  out.push(S(G.disc(28, DISQUE.s - 1, 22, FW, P), { tone: "mid" }));        // la bride du disque sur le moyeu
  out.push(S(G.ringBand(DISQUE.s - 1, DISQUE.s + 1, DISQUE.rIn, DISQUE.rOut, FW, P, { hole: [DISQUE.s + 1, DISQUE.rIn] }), { tone: "hi", crease: "lo" }));
  // les six bras qui portent la couronne, et leurs vis
  const bras = [];
  for (let i = 0; i < 6; i++) { const a = i * 60 * DEG + 0.3; bras.push(pathOf3([W(20, a, DISQUE.s + 1), W(DISQUE.rIn + 1, a + 0.18, DISQUE.s + 1)], P)); }
  out.push(L(bras.join(""), { tone: "mid" }));
  out.push(k.dotsSvg(Array.from({ length: 6 }, (_, i) => k.iso(W(16, i * 60 * DEG + 0.3, DISQUE.s + 1), P)), { size: 0.5 }));
  out.push(L(G.circleOf(FW, DISQUE.s + 1, 62, P) + G.circleOf(FW, DISQUE.s + 1, 78, P), { tone: "faint" }));
  return out.join("");
}

// le tambour : la coque, la flasque de rayons, la flasque de frein (qui ferme tout)
function tambour(P) {
  const out = [];
  out.push(S(G.disc(TAMBOUR.s0, TAMBOUR.s0 + 3, 48, FW, P), { tone: "mid" }));
  out.push(S(G.disc(TAMBOUR.s0 + 3, TAMBOUR.s1, TAMBOUR.rExt, FW, P), { tone: "mid" }));
  out.push(S(G.disc(TAMBOUR.s1, TAMBOUR.s1 + TAMBOUR.flasque, TAMBOUR.rExt - 1, FW, P), { tone: "hi", crease: "lo" }));
  out.push(k.dotsSvg(Array.from({ length: 4 }, (_, i) => k.iso(W(30, (45 + i * 90) * DEG, TAMBOUR.s1 + TAMBOUR.flasque), P)), { size: 0.5 }));
  return out.join("");
}

function jante(P) {
  const out = [anneau(L_JANTE, R_JANTE_IN, R_JANTE, P, "mid", "lo")];
  // la piste de freinage, usée par les patins : deux traits sur le flanc
  out.push(L(G.circleOf(FW, L_JANTE, R_PISTE - 7, P) + G.circleOf(FW, L_JANTE, R_PISTE + 7, P), { tone: "faint" }));
  // la valve
  out.push(S(G.disc(-3, 3, 3, G.frameAlong(W(R_JANTE_IN, 200 * DEG, 0), G.unit3(G.sub3(AXE, W(1, 200 * DEG, 0)))), P), { tone: "mid" }));
  return out.join("");
}

function pneu(P) {
  const out = [anneau(L_PNEU, R_PNEU_IN, R_PNEU, P, "lo", "faint")];
  out.push(L(G.circleOf(FW, L_PNEU, R_PNEU - 9, P), { tone: "faint" }));
  return out.join("");
}

function fourreau(P, cote) {
  const y = cote * FOURCHE_Y;
  const out = [];
  out.push(S(k.slabOf({ x: -9, y: y - 5, w: 18, d: 10, r: 3 }, R_PNEU - 14, 26, P, 3, 0.4), { tone: "mid" }));   // la patte
  out.push(S(k.cylinder(0, y, FOURCHE_R, R_PNEU + 12, TE_Z - R_PNEU - 12, P, 28), { tone: "hi", crease: "none" }));
  out.push(L(k.sideArc(0, y, FOURCHE_R, R_PNEU + 60, P, 20), { tone: "faint" }));
  if (cote > 0) out.push(S(G.disc(56, 62, 8, FW, P), { tone: "mid" }));                                      // l'écrou
  return out.join("");
}

function avant(P) {
  const out = [];
  out.push(S(k.slabOf({ x: -18, y: -FOURCHE_Y - 14, w: 36, d: 2 * FOURCHE_Y + 28, r: 8 }, TE_Z, 24, P, 6, 0.8), { tone: "hi" }));   // le té
  out.push(S(k.cylinder(0, 0, 15, TE_Z + 24, 150, P, 28), { tone: "mid", crease: "none" }));        // le pivot
  out.push(L(k.sideArc(0, 0, 15, TE_Z + 64, P) + k.sideArc(0, 0, 15, TE_Z + 70, P), { tone: "faint" }));
  out.push(S(k.slabOf({ x: -70, y: -17, w: 78, d: 34, r: 8 }, TE_Z + 160, 26, P, 6, 0.8), { tone: "mid" }));   // la potence
  const FC = G.frameAlong([-62, 0, TE_Z + 173], [0, 1, 0]);
  out.push(S(G.disc(-90, 300, 11, FC, P), { tone: "hi", crease: "none" }));                     // le cintre
  out.push(S(G.disc(180, 290, 16, FC, P), { tone: "lo" }));                                        // la poignée
  out.push(L(G.ribsOf(FC, 186, 284, 16, 18, P, { least: 0.2 }), { tone: "faint" }));
  out.push(S(G.disc(158, 176, 15, FC, P), { tone: "mid" }));                                       // le collier du levier
  return out.join("");
}

// le levier : un trait épais qui tourne autour de son axe, devant le cintre ; t = 0 relâché, 1 serré
const LEVIER = { pivot: [-46, 168, TE_Z + 173], long: 120, a0: 26 * DEG, a1: 6 * DEG };
function levierPts(t) {
  const a = LEVIER.a0 + (LEVIER.a1 - LEVIER.a0) * t;
  const [px, py, pz] = LEVIER.pivot;
  return [[px, py, pz], [px + 24 * Math.sin(a), py + 14, pz - 2], [px + 26 * Math.sin(a) + 2, py + LEVIER.long, pz - 4]];
}

// le patin et le bras du frein à patins, d'un côté ; « dy » les rapproche de la jante quand on serre
function brasPatins(P, cote) {
  const y = cote * (FOURCHE_Y - 4);
  const out = [];
  out.push(S(k.slabOf({ x: 12, y: y - 4, w: 12, d: 8, r: 2 }, R_PNEU + 230, 125, P, 3, 0.4), { tone: "hi", crease: "lo" }));
  out.push(k.dotsSvg(k.pointsAt([[24, y, R_PNEU + 240]], P), { size: 0.6, tone: "mid" }));    // l'axe du bras
  // la tige et le patin
  const yp = cote * (L_JANTE + 2), yb = cote * (FOURCHE_Y - 8);
  out.push(S(k.slabOf({ x: 15, y: Math.min(yp, yb), w: 4, d: Math.abs(yb - yp), r: 1 }, R_PISTE + R_PNEU - 2, 4, P, 2), { tone: "mid" }));
  out.push(`<g data-part="patin" data-cote="${cote}">${S(k.slabOf({ x: -2, y: cote > 0 ? yp : yp - 7, w: 36, d: 7, r: 1.5 }, R_PISTE + R_PNEU - 6, 12, P, 2, 0.3), { tone: "lo", lit: false })}</g>`);
  return out.join("");
}
function cablePatins(P) {
  const yN = FOURCHE_Y - 4, top = R_PNEU + 352;
  return `<g data-part="cable">${L(pathOf3([[18, yN, top], [18, -yN, top]], P), { tone: "lo" })}</g>`;
}

// l'étrier du frein à disque, en deux moitiés qui encadrent le disque ; les plaquettes dedans
const ETRIER_A = 200 * DEG;
function etrier(P, moitie) {
  const c = W(DISQUE.piste, ETRIER_A, 0);
  const out = [];
  if (moitie === "loin") {
    out.push(S(k.slabOf({ x: c[0] - 22, y: DISQUE.s - 12, w: 44, d: 10, r: 4 }, c[2] - 18, 36, P, 4, 0.5), { tone: "mid" }));
  } else {
    out.push(S(k.slabOf({ x: c[0] - 26, y: DISQUE.s - 12, w: 6, d: 26, r: 2 }, c[2] - 18, 36, P, 3, 0.4), { tone: "mid" }));   // le pont, au-delà du disque
    if (moitie === "pont") return out.join("");
    out.push(S(k.slabOf({ x: c[0] - 22, y: DISQUE.s + 2, w: 44, d: 12, r: 4 }, c[2] - 18, 36, P, 4, 0.6), { tone: "hi", crease: "lo" }));
    out.push(L(k.sideSeam({ x: c[0] - 22, y: DISQUE.s + 2, w: 44, d: 12, r: 4 }, c[2] + 6, P, 4), { tone: "faint" }));
    // le support qui fixe l'étrier sur le fourreau
    out.push(S(k.slabOf({ x: c[0] + 18, y: FOURCHE_Y - 9, w: -c[0] - 18 + 2, d: 8, r: 2 }, c[2] - 6, 14, P, 3, 0.4), { tone: "mid" }));
    out.push(k.dotsSvg(k.pointsAt([[c[0] + 26, FOURCHE_Y - 1, c[2] + 8]], P), { size: 0.55 }));
  }
  return out.join("");
}
function plaquette(P, cote) {
  const c = W(DISQUE.piste, ETRIER_A, 0);
  const y = cote > 0 ? DISQUE.s + 1.6 : DISQUE.s - 1.6 - 4;
  return `<g data-part="plaquette" data-cote="${cote}">${S(k.slabOf({ x: c[0] - 14, y, w: 28, d: 4, r: 1 }, c[2] - 9, 18, P, 2, 0.3), { tone: "lo" })}</g>`;
}

// le frein à tambour, vu de dehors : le levier de came et le bras de réaction
const CAME = W(26, 40 * DEG, TAMBOUR.s1 + TAMBOUR.flasque);
function levierCamePts(t) {
  const a = (40 - 18 * t) * DEG;
  return [CAME, [CAME[0] + 62 * Math.sin(a + 0.5), CAME[1] + 1, CAME[2] + 62 * Math.cos(a + 0.5)]];
}
function reaction(P) {
  const a = W(30, 160 * DEG, TAMBOUR.s1 + 1);
  return S(k.slabOf({ x: a[0] - 5, y: TAMBOUR.s1 + 2, w: 10, d: FOURCHE_Y - TAMBOUR.s1 - 2, r: 2 }, a[2] - 30, 30, P, 3, 0.4), { tone: "mid" })
    + S(k.slabOf({ x: -7, y: FOURCHE_Y - 14, w: 14, d: 4, r: 1.5 }, a[2] - 34, 12, P, 2), { tone: "mid" });
}

// ── La loupe : une coupe à plat de l'endroit qui frotte, grossie ──────────────
// Dessin 2D (vue de technicien), pas isométrique : on y voit d'un coup d'œil ce qui pince quoi. Les pièces qui
// bougent sont dans des groupes data-part ; le script les déplace de « écart × échelle » pixels.
const LP = 190;
const f1 = (v) => +v.toFixed(1);
const poly = (pts, cls) => `<path class="${cls}" d="M${pts.map(([x, y]) => `${f1(x)} ${f1(y)}`).join("L")}Z"/>`;
const rect = (x0, y0, x1, y1, cls) => poly([[x0, y0], [x1, y0], [x1, y1], [x0, y1]], cls);
const ligne = (pts, cls) => `<path class="${cls}" d="M${pts.map(([x, y]) => `${f1(x)} ${f1(y)}`).join("L")}"/>`;
const ECHELLE = { patins: 2.6, disque: 4, tambour: 2.05 };

// patins : coupe de la jante à l'endroit du patin ; horizontal = à travers la roue, vertical = vers l'axe (en bas)
function loupePatins() {
  const K = ECHELLE.patins, X = (y) => 95 + y * K, Y = (r) => 150 - (r - 266) * K;
  const out = [];
  // le pneu, coupé : ses deux flancs sortent des crochets de la jante
  out.push(`<path class="fl-pneu" d="M${f1(X(-8))} ${f1(Y(294))}C${f1(X(-20))} ${f1(Y(299))} ${f1(X(-24))} ${f1(Y(306))} ${f1(X(-23))} ${f1(Y(312))}M${f1(X(8))} ${f1(Y(294))}C${f1(X(20))} ${f1(Y(299))} ${f1(X(24))} ${f1(Y(306))} ${f1(X(23))} ${f1(Y(312))}"/>`);
  // la jante en U : deux flancs, un fond, deux crochets
  out.push(poly([[-10, 268], [-10, 296], [-7.5, 296], [-7.5, 293.5], [-8, 293.5], [-8, 272], [8, 272], [8, 293.5], [7.5, 293.5], [7.5, 296], [10, 296], [10, 268]].map(([y, r]) => [X(y), Y(r)]), "fl-piece"));
  out.push(ligne([[X(-8), Y(276)], [X(8), Y(276)]], "fl-trait"));
  for (const c of [-1, 1]) {
    out.push(`<g data-part="piste">${ligne([[X(c * 10), Y(279)], [X(c * 10), Y(291)]], "fl-chaud")}</g>`);
    const y0 = c * 12;   // écart de 2 mm au repos
    out.push(`<g data-part="patin" data-cote="${c}" data-k="${K}">`
      + rect(X(y0), Y(291), X(y0 + c * 7), Y(279), "fl-caoutchouc")          // le patin
      + rect(X(y0 + c * 7), Y(292), X(y0 + c * 9), Y(278), "fl-piece")        // son support
      + rect(X(y0 + c * 9), Y(306), X(y0 + c * 13), Y(266), "fl-piece")       // le bras
      + `</g>`);
  }
  out.push(`<text class="fl-mot" x="30" y="128">axe</text><text class="fl-mot" x="34" y="142">↓</text>`);
  return out.join("");
}
// disque : coupe de l'étrier ; horizontal = à travers la roue, vertical = vers l'axe (en bas)
function loupeDisque() {
  const K = ECHELLE.disque, X = (y) => 95 + y * K, Y = (r) => 150 - (r - 56) * K;
  const out = [];
  out.push(rect(X(-15), Y(88), X(15), Y(84), "fl-piece"));                       // le pont de l'étrier, au-delà du disque
  for (const c of [-1, 1]) out.push(rect(X(c * 15), Y(88), X(c * 7.4), Y(60), "fl-piece"));   // ses deux corps
  out.push(rect(X(-1), Y(80), X(1), Y(54), "fl-disque"));                         // le disque, vu par la tranche
  for (const c of [-1, 1]) {
    out.push(`<g data-part="piste">${ligne([[X(c), Y(62)], [X(c), Y(78)]], "fl-chaud")}</g>`);
    const y0 = c * 1.6;  // écart de 0,6 mm au repos
    out.push(`<g data-part="plaquette" data-cote="${c}" data-k="${K}">`
      + rect(X(y0), Y(78), X(y0 + c * 3), Y(62), "fl-garniture")              // la garniture
      + rect(X(y0 + c * 3), Y(79), X(y0 + c * 5), Y(61), "fl-piece")          // la plaque d'appui
      + `</g>`);
  }
  out.push(`<text class="fl-mot" x="30" y="128">axe</text><text class="fl-mot" x="34" y="142">↓</text>`);
  return out.join("");
}
// tambour : vu de face, flasque ôtée ; les mâchoires poussent vers l'extérieur
function loupeTambour() {
  const K = ECHELLE.tambour, cx = 95, cy = 86;
  const pt = (r, a) => [cx + r * K * Math.sin(a), cy - r * K * Math.cos(a)];
  const arc = (r, a0, a1, n = 28) => Array.from({ length: n + 1 }, (_, i) => pt(r, (a0 + ((a1 - a0) * i) / n) * DEG));
  const anneau = (r0, r1, a0, a1) => poly([...arc(r1, a0, a1), ...arc(r0, a1, a0)], "fl-piece");
  const out = [anneau(TAMBOUR.rIn, TAMBOUR.rExt, 0, 360)];
  out.push(`<circle class="fl-piece" cx="${cx}" cy="${cy}" r="${f1(6 * K)}"/>`);
  for (const c of [-1, 1]) {
    const a0 = c > 0 ? 22 : 202, a1 = c > 0 ? 158 : 338;
    out.push(`<g data-part="piste">${ligne(arc(TAMBOUR.rIn, a0 + 8, a1 - 8), "fl-chaud")}</g>`);
    // la mâchoire : une semelle en arc, sa garniture côté tambour ; écart de 1 mm au repos
    out.push(`<g data-part="machoire" data-cote="${c}" data-k="${K}">${anneau(TAMBOUR.rIn - 6, TAMBOUR.rIn - 3, a0, a1)}`
      + `${poly([...arc(TAMBOUR.rIn - 1, a0 + 8, a1 - 8), ...arc(TAMBOUR.rIn - 3, a1 - 8, a0 + 8)], "fl-garniture")}</g>`);
  }
  const [ux, uy] = pt(TAMBOUR.rIn - 5, 0), [bx, by] = pt(TAMBOUR.rIn - 5, Math.PI);
  out.push(`<g data-part="came-loupe"><rect class="fl-piece" x="${f1(ux - 5)}" y="${f1(uy - 3)}" width="10" height="6" rx="2"/></g>`);
  out.push(`<circle class="fl-piece" cx="${f1(bx)}" cy="${f1(by)}" r="3.4"/>`);
  const zig = Array.from({ length: 13 }, (_, i) => [cx - 27 + 4.5 * i, cy - 50 + (i % 2 ? 2.4 : -2.4) * (i && i < 12 ? 1 : 0)]);
  out.push(ligne(zig, "fl-trait"));
  return out.join("");
}

// le rayon de frottement : de l'axe au point où ça frotte, sur la face proche ; il s'allume quand on serre
const RAYON = { patins: [R_PISTE, -18 * DEG, L_JANTE], disque: [DISQUE.piste, ETRIER_A, DISQUE.s + 1], tambour: [TAMBOUR.rIn, -50 * DEG, TAMBOUR.s1 + TAMBOUR.flasque] };
function rayon(P, frein) {
  const [r, a, s] = RAYON[frein];
  return `<g data-part="piste" class="fr-rayon">${L(pathOf3([W(0, a, s), W(r, a, s)], P), { tone: "lit" })}${k.dotsSvg([k.iso(W(0, a, s), P), k.iso(W(r, a, s), P)], { size: 1.6, tone: "hi" })}</g>`;
}

// ── Assemblage d'une vue ─────────────────────────────────────────────────────
function scene(P, frein) {
  const out = [sol(P), ratelier(P, -1), fourreau(P, -1)];
  if (frein === "patins") out.push(brasPatins(P, -1));
  if (frein === "disque") out.push(etrier(P, "loin"), plaquette(P, -1));
  out.push(rayons(P, -1), moyeu(P, frein), rayons(P, 1));
  if (frein === "disque") out.push(disque(P), `<g data-part="piste">${L(G.circleOf(FW, DISQUE.s + 1, DISQUE.piste, P), { tone: "lit" })}</g>`, plaquette(P, 1));
  if (frein === "tambour") out.push(tambour(P));
  out.push(jante(P));
  if (frein === "patins") out.push(`<g data-part="piste">${L(G.circleOf(FW, L_JANTE, R_PISTE, P), { tone: "lit" })}</g>`);
  out.push(pneu(P), ratelier(P, 1), fourreau(P, 1));
  if (frein === "patins") out.push(brasPatins(P, 1), cablePatins(P));
  if (frein === "disque") out.push(etrier(P, "pres"));
  if (frein === "tambour") out.push(reaction(P), `<g data-part="came"><path class="fr-trait" d="${pathOf3(levierCamePts(0), P)}"/></g>`);
  out.push(avant(P));
  out.push(`<g data-part="levier"><path class="fr-trait" d="${pathOf3(levierPts(0), P)}"/></g>`);
  out.push(gaine(P, frein), rayon(P, frein));
  return out.join("");
}

// la gaine (patins, tambour) ou la durite (disque), du levier au frein
function gaine(P, frein) {
  const de = k.iso([LEVIER.pivot[0] - 6, LEVIER.pivot[1] - 4, LEVIER.pivot[2] - 8], P);
  const via = { patins: [[60, 120, TE_Z + 100], [40, FOURCHE_Y, R_PNEU + 420]], disque: [[40, 120, TE_Z + 60], [20, FOURCHE_Y + 16, TE_Z - 40], [8, FOURCHE_Y + 14, R_PNEU + 80]], tambour: [[40, 120, TE_Z + 60], [20, FOURCHE_Y + 16, TE_Z - 60], [40, FOURCHE_Y + 10, R_PNEU + 160]] }[frein];
  const fin = { patins: [18, FOURCHE_Y - 4, R_PNEU + 352], disque: [W(DISQUE.piste, ETRIER_A, 0)[0] + 10, DISQUE.s + 14, W(DISQUE.piste, ETRIER_A, 0)[2] + 18], tambour: levierCamePts(0)[1] }[frein];
  return `<g data-part="gaine">${k.wireSvg(de, k.iso(fin, P), { via: via.map((p) => k.iso(p, P)), tone: "lo", size: 1.4 })}</g>`;
}

// ── Les numéros (nomenclature) ───────────────────────────────────────────────
const PIECES = {
  commun: [
    { n: 1, nom: "le levier de frein", at: () => levierPts(0)[2] },
    { n: 3, nom: "la jante (le bord de la roue, en métal)", at: () => W(R_JANTE - 12, -62 * DEG, L_JANTE) },
    { n: 4, nom: "le pneu", at: () => W(R_PNEU - 16, -105 * DEG, L_PNEU) },
    { n: 5, nom: "le moyeu (le centre de la roue)", at: () => W(30, 235 * DEG, 0) },
    { n: 6, nom: "la fourche (elle tient la roue par son axe)", at: () => [0, FOURCHE_Y + 12, TE_Z - 90] },
  ],
  patins: [
    { n: 2, nom: "le câble, dans sa gaine (le tube qui le guide)", at: () => [52, 110, TE_Z + 60] },
    { n: 7, nom: "les deux bras du frein", at: () => [24, FOURCHE_Y + 2, R_PNEU + 248] },
    { n: 8, nom: "les patins (deux blocs de caoutchouc)", at: () => [40, L_JANTE + 6, R_PISTE + R_PNEU] },
  ],
  disque: [
    { n: 2, nom: "la durite (un tuyau rempli de liquide de frein)", at: () => [40, 110, TE_Z + 40] },
    { n: 7, nom: "le disque, fixé au moyeu", at: () => W(DISQUE.rOut - 6, 120 * DEG, DISQUE.s + 1) },
    { n: 8, nom: "l'étrier (une pince fixée à la fourche)", at: () => [W(DISQUE.piste, ETRIER_A, 0)[0] - 4, DISQUE.s + 14, W(DISQUE.piste, ETRIER_A, 0)[2] + 26] },
    { n: 9, nom: "les plaquettes (deux pastilles qui frottent), dans l'étrier : voir la loupe", at: null },
  ],
  tambour: [
    { n: 2, nom: "le câble, dans sa gaine (le tube qui le guide)", at: () => [40, FOURCHE_Y + 16, TE_Z - 40] },
    { n: 7, nom: "le tambour, fermé, dans le moyeu", at: () => W(TAMBOUR.rExt + 10, 225 * DEG, TAMBOUR.s1) },
    { n: 8, nom: "le levier de came (il fait tourner la came, en haut dans la loupe)", at: () => levierCamePts(0)[1] },
    { n: 9, nom: "les mâchoires (deux pièces en arc, garnies), cachées dans le tambour : voir la loupe", at: null },
  ],
};

// ── La vue entière et sa loupe ──────────────────────────────────────────────
const VW = 520, VH = 600;
const P = k.fitProjection([
  ...k.boxCorners({ x: -360, y: -150, w: 720, d: 300, r: 0 }, -6, 0),
  W(R_PNEU, 0, -L_PNEU), W(R_PNEU, 0, L_PNEU), [-62, 300, TE_Z + 190], [-62, -90, TE_Z + 190], levierPts(0)[2],
], VW, VH, { pad: 14, azimuth: 58 });
const LOUPES = { patins: loupePatins, disque: loupeDisque, tambour: loupeTambour };

function vue(frein, { avecNumeros = true } = {}) {
  const pieces = [...PIECES.commun, ...PIECES[frein]].filter((p) => p.at);
  return scene(P, frein) + (avecNumeros ? `<g class="fr-pins">${pieces.map((p) => pin(p.n, p.at(), P)).join("")}</g>` : "");
}
function loupe(frein) {
  return `<svg class="fr-loupe" viewBox="0 0 ${LP} ${LP}" aria-hidden="true"><defs><clipPath id="fr-rond-${frein}"><circle cx="${LP / 2}" cy="${LP / 2}" r="${LP / 2 - 2}"/></clipPath></defs>`
    + `<circle class="fr-loupe-fond" cx="${LP / 2}" cy="${LP / 2}" r="${LP / 2 - 2}"/><g clip-path="url(#fr-rond-${frein})">${LOUPES[frein]()}</g>`
    + `<circle class="fr-loupe-bord" cx="${LP / 2}" cy="${LP / 2}" r="${LP / 2 - 2}"/><text class="fr-loupe-mot" x="${LP / 2}" y="${LP - 12}">${{ patins: "coupe de la jante", disque: "coupe de l'étrier", tambour: "flasque ôtée" }[frein]}</text></svg>`;
}

// une illustration de l'objet réel, pas un schéma : déclarée pour le contrôle n°315 (_outils/controle_schemas.mjs)
const ILLUSTRATION = "vue isométrique de l'objet réel (skill anatomy) : ses pièces se touchent comme sur le vrai vélo ; les schémas de la séquence restent à part";
const illustration = (svg) => svg.replace("<svg ", `<svg data-illustration="${ILLUSTRATION}" `);
const LABEL = {
  patins: "La roue avant d'un vélo, posée dans un range-vélo, avec un frein à patins : deux bras fixés à la fourche portent chacun un patin de caoutchouc, de part et d'autre de la jante. Un câble relie le levier du guidon aux bras.",
  disque: "La même roue avec un frein à disque : un disque fixé au moyeu tourne avec la roue ; un étrier fixé à la fourche l'encadre et porte deux plaquettes. Une durite relie le levier du guidon à l'étrier.",
  tambour: "La même roue avec un frein à tambour : le tambour est dans le moyeu, fermé par une flasque ; un levier de came est relié au levier du guidon par un câble. Les mâchoires sont cachées à l'intérieur ; la loupe les montre, flasque ôtée.",
};

// ── La page à poser dans la séquence (iframe) ────────────────────────────────
const CSS = `
html,body{margin:0;background:#050f24}
.iso[data-theme="dark"]{--anatomy-muted:#9a9a9a}
.fr-legende li{color:#d4d8e0}
.fr-cache{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.iso{--anatomy-weight:1px}
.iso-solid>.iso-fill{fill-rule:evenodd}
body{font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--anatomy-text)}
.fr{max-width:600px;margin:0 auto;padding:4px}
.fr-choix{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 10px}
.fr-choix button,.fr-serrer{font:inherit;font-size:15px;min-height:44px;padding:8px 14px;border-radius:10px;border:1px solid var(--anatomy-muted);background:var(--anatomy-card);color:var(--anatomy-strong);cursor:pointer}
.fr-choix button[aria-pressed="true"]{outline:2px solid var(--anatomy-strong);outline-offset:1px;font-weight:600}
.fr-serrer{display:block;width:100%;margin:10px 0 0;font-weight:600}
.fr-serrer[aria-pressed="true"]{background:var(--anatomy-strong);color:var(--anatomy-card)}
.iso-stage{position:relative;touch-action:pan-y;cursor:pointer;outline:none}
.iso-stage:focus-visible{outline:1px solid var(--anatomy-muted);outline-offset:6px}
.fr-vue[hidden]{display:none}
.iso-plate-corner[data-corner="hint"]:empty{display:none}
.fr-loupe{position:absolute;right:0;top:0;width:34%;max-width:200px;height:auto}
.fr-loupe-fond{fill:var(--anatomy-card);stroke:none}
.fr-loupe-bord{fill:none;stroke:var(--anatomy-muted);stroke-width:1.2}
.fr-loupe-mot{fill:var(--anatomy-muted);font:600 11px system-ui,sans-serif;text-anchor:middle;letter-spacing:.06em}
.fl-piece{fill:var(--anatomy-card);stroke:var(--anatomy-hi);stroke-width:1.1;stroke-linejoin:round}
.fl-caoutchouc{fill:var(--anatomy-lo);stroke:var(--anatomy-hi);stroke-width:1.1}
.fl-garniture{fill:var(--anatomy-lo);stroke:var(--anatomy-hi);stroke-width:1}
.fl-disque{fill:var(--anatomy-mid);stroke:var(--anatomy-hi);stroke-width:1}
.fl-pneu{fill:none;stroke:var(--anatomy-mid);stroke-width:2.2;stroke-linecap:round}
.fl-trait{fill:none;stroke:var(--anatomy-hi);stroke-width:1}
.fl-chaud{fill:none;stroke:var(--anatomy-lit);stroke-width:3;stroke-linecap:round}
.fl-mot{fill:var(--anatomy-muted);font:600 10px system-ui,sans-serif}
.fr-trait{fill:none;stroke:var(--anatomy-strong);stroke-width:3.4;stroke-linecap:round;stroke-linejoin:round}
.fr-machoire{fill:none;stroke:var(--anatomy-strong);stroke-width:4.2;stroke-linecap:round}
.fr-garniture{fill:none;stroke:var(--anatomy-muted);stroke-width:2.4;stroke-linecap:round}
.fr-came circle{fill:var(--anatomy-card);stroke:var(--anatomy-strong);stroke-width:1.6}
[data-part="piste"]{opacity:0;transition:opacity .45s cubic-bezier(.2,0,0,1)}
.fr-serre [data-part="piste"]{opacity:1}
.fr-serre [data-part="cable"] .iso-line,.fr-serre [data-part="gaine"] .iso-line{stroke:var(--anatomy-strong)}
.fr-pin circle{fill:var(--anatomy-strong);stroke:var(--anatomy-card);stroke-width:1.4}
.fr-pin text{fill:var(--anatomy-card);font:700 11.5px system-ui,sans-serif;text-anchor:middle;dominant-baseline:central}
.fr-legende{margin:10px 0 0;padding:0 0 0 1.6em}
.fr-legende li{margin:2px 0}
.fr-legende[hidden]{display:none}
.fr-legende-papier{display:none}
.fr-mention{margin:4px 0 0;font-size:12px;color:var(--anatomy-muted)}
.licence-cc{color:var(--anatomy-muted)}
@media (prefers-reduced-motion: reduce){[data-part="piste"]{transition:none}}
@media (max-width:560px){
  .iso-plate-corner[data-corner="readout"]{white-space:normal;left:0;text-align:right;line-height:1.35}
  .iso-plate-corner[data-corner="hint"]{display:none}
  .iso-plate{padding-bottom:64px}
  .fr-loupe{width:44%}
  .fr-pin circle{r:17px}
  .fr-pin text{font-size:21px}
}
@media print{
  .iso{__CLAIR__}
  body{background:#fff}
  .fr-choix,.fr-serrer,.iso-plate-corners{display:none!important}
  .iso-plate{padding:0;box-shadow:none;background:#fff}
  .iso-stage{display:flex;gap:6px}
  .fr-vue,.fr-vue[hidden]{display:block!important;position:relative;flex:1 1 0;break-inside:avoid}
  .fr-vue::before{content:attr(data-nom);display:block;font:700 12px system-ui,sans-serif;color:#000;margin:0 0 2px}
  .fr-loupe{width:40%}
  [data-part="piste"]{opacity:0!important}
  .fr-legende,.fr-legende[hidden]{display:none!important}
  .fr-legende-papier{display:grid!important;grid-template-columns:repeat(3,1fr);gap:0 10px;font-size:10px;color:#000;margin:4px 0 0}
  .fr-legende-papier p{margin:0}
  .fr-legende-papier p:first-child{grid-column:1 / -1}
  .fr-mention{font-size:9px;margin:4px 0 0}
}
`;

const choix = Object.entries(FREINS).map(([f, x], i) => `<button type="button" data-frein="${f}" aria-pressed="${i === 0}">${x.nom}</button>`).join("");
const vues = Object.keys(FREINS).map((f, i) => `<div class="fr-vue" data-vue="${f}" data-nom="${FREINS[f].nom}"${i ? " hidden" : ""}>`
  + illustration(k.figureSvg({ width: VW, height: VH, label: LABEL[f], body: [vue(f)] })) + loupe(f) + `</div>`).join("");
const legendes = Object.keys(FREINS).map((f, i) => `<ol class="fr-legende" data-legende="${f}" data-nom="${FREINS[f].nom}"${i ? " hidden" : ""}>`
  + [...PIECES.commun, ...PIECES[f]].sort((a, b) => a.n - b.n).map((p) => `<li value="${p.n}">${p.nom}</li>`).join("") + `</ol>`).join("");

const corps = `<main class="fr"><h1 class="fr-cache">Trois freins, la même roue</h1>`
  + `<div class="fr-choix" role="group" aria-label="Choisir le frein">${choix}</div>`
  + k.plateHtml({
    fig: "Fig 1", title: "Trois freins, la même roue",
    hint: "",
    readout: "Frein à patins · levier relâché",
    body: `<div class="iso-stage" tabindex="0" role="group" aria-label="La roue et son frein. Espace ou Entrée serre et relâche le levier ; les touches 1, 2 et 3 changent de frein.">${vues}</div>`
      + `<button type="button" class="fr-serrer" aria-pressed="false">✊ Serrer le levier</button>`,
  })
  + legendes
  + `<div class="fr-legende-papier"><p><b>Pour les trois :</b> 1 levier de frein · 3 jante · 4 pneu · 5 moyeu · 6 fourche</p>`
  + `<p><b>Patins :</b> 2 câble · 7 bras · 8 patins</p><p><b>Disque :</b> 2 durite · 7 disque · 8 étrier · 9 plaquettes</p>`
  + `<p><b>Tambour :</b> 2 câble · 7 tambour · 8 levier de came · 9 mâchoires</p></div>`
  // la mention du dépôt (règle d'or n°321), recopiée de _outils/licence_cc.py (MENTION), puis celle du kit
  + `<style>.licence-cc a,.licence-cc a:visited{color:inherit;text-decoration:underline}@media print{.licence-cc a,.licence-cc a:visited{color:#000}}</style>`
  + `<p class="licence-cc" data-licence="cc-by-nc-sa" style="font-size:.85em;margin-top:.8em">📄 Ressource sous licence <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr" rel="license">CC BY-NC-SA 4.0</a> `
  + `— © Pascal Gouacide, 2026 · Technologie cycle 4 · réutilisation et adaptation libres à condition de citer l’auteur, sans usage commercial et en partageant dans les mêmes conditions.</p>`
  + `<p class="fr-mention">Dessin original, écrit pour cette séquence. Dessiné avec le kit Anatomy © 2026 Ryan, licence MIT.</p>`
  + `</main>`;

const live = `
/* Kit Anatomy © 2026 Ryan — licence MIT (github.com/wheresryan22/anatomy, commit 1482e84). Le reste : CC BY-NC-SA 4.0. */
const FREINS = ${JSON.stringify(FREINS)};
const PM = ${JSON.stringify(P)};
const LEVIER = ${JSON.stringify(LEVIER)}, CAME = ${JSON.stringify(CAME)};
const racine = document.querySelector(".fr"), stage = racine.querySelector(".iso-stage");
const sortie = racine.querySelector("[data-readout]"), bouton = racine.querySelector(".fr-serrer");
sortie.setAttribute("aria-live", "polite");
const calme = matchMedia("(prefers-reduced-motion: reduce)");
let frein = "patins", serre = false, t = 0, cible = 0, frame = 0, last = 0;
const P3 = (pts, P) => pathOf(pts.map((p) => iso(p, P)));
function levierPts(t) {
  const a = LEVIER.a0 + (LEVIER.a1 - LEVIER.a0) * t, [px, py, pz] = LEVIER.pivot;
  return [[px, py, pz], [px + 24 * Math.sin(a), py + 14, pz - 2], [px + 26 * Math.sin(a) + 2, py + LEVIER.long, pz - 4]];
}
function camePts(t) {
  const a = (40 - 18 * t) * Math.PI / 180;
  return [CAME, [CAME[0] + 62 * Math.sin(a + 0.5), CAME[1] + 1, CAME[2] + 62 * Math.cos(a + 0.5)]];
}
// le levier d'abord ; les pièces qui frottent arrivent quand le levier a fait 60 % de sa course (elles touchent, puis s'arrêtent)
const contact = (t) => Math.min(1, Math.max(0, (t - 0.4) / 0.6));
const ECART = { patins: 2, disque: 0.6, tambour: 1 };
function peindre() {
  const vue = racine.querySelector('[data-vue="' + frein + '"]'), c = contact(t), e = ECART[frein] * c;
  vue.querySelector('[data-part="levier"] path').setAttribute("d", P3(levierPts(t), PM));
  const came = vue.querySelector('[data-part="came"] path');
  if (came) came.setAttribute("d", P3(camePts(t), PM));
  const loupe = vue.querySelector(".fr-loupe");
  // dans la vue entière : le déplacement vrai, en millimètres ; dans la loupe : en pixels de la coupe (data-k)
  vue.querySelectorAll('[data-part="patin"],[data-part="plaquette"],[data-part="machoire"]').forEach((g) => {
    const cote = +g.getAttribute("data-cote");
    if (loupe.contains(g)) g.setAttribute("transform", "translate(" + (-cote * e * +g.getAttribute("data-k") * (g.dataset.part === "machoire" ? -1 : 1)).toFixed(2) + " 0)");
    else g.setAttribute("transform", translateAlong(PM, [0, -cote * e, 0]));
  });
}
function dire() {
  const f = FREINS[frein];
  sortie.textContent = f.nom + (serre ? " · levier serré · ça frotte à " + f.contact + " de l'axe" : " · levier relâché · écart " + f.ecart);
}
function tic(now) {
  const dt = last ? Math.min((now - last) / 1000, 1 / 30) : 1 / 60; last = now;
  // serrer : la main pousse (τ = 0,12 s) ; relâcher : le ressort ramène, un peu plus vite (τ = 0,09 s) ; métal rigide, sans rebond
  t = calme.matches ? cible : t + (cible - t) * (1 - Math.exp(-dt / (cible > t ? 0.12 : 0.09)));
  if (Math.abs(cible - t) < 0.002) t = cible;
  peindre();
  frame = t !== cible ? requestAnimationFrame(tic) : 0;
}
function serrer(oui) {
  serre = oui; cible = oui ? 1 : 0;
  stage.classList.toggle("fr-serre", oui);
  bouton.setAttribute("aria-pressed", String(oui));
  bouton.textContent = oui ? "✋ Relâcher le levier" : "✊ Serrer le levier";
  dire();
  if (!frame) { last = 0; frame = requestAnimationFrame(tic); }
}
function choisir(f) {
  if (!FREINS[f] || f === frein) return;
  frein = f; t = 0; cible = 0; serre = false;
  racine.querySelectorAll("[data-frein]").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.frein === f)));
  racine.querySelectorAll("[data-vue]").forEach((v) => { v.hidden = v.dataset.vue !== f; });
  racine.querySelectorAll("[data-legende]").forEach((v) => { v.hidden = v.dataset.legende !== f; });
  serrer(false); peindre();
}
racine.querySelectorAll("[data-frein]").forEach((b) => b.addEventListener("click", () => choisir(b.dataset.frein)));
stage.addEventListener("click", () => serrer(!serre));
bouton.addEventListener("click", () => serrer(!serre));
stage.addEventListener("keydown", (ev) => {
  if (ev.key === " " || ev.key === "Enter") { ev.preventDefault(); serrer(!serre); }
  if (ev.key === "Escape") serrer(false);
  const n = ["1", "2", "3"].indexOf(ev.key);
  if (n >= 0) choisir(Object.keys(FREINS)[n]);
});
// la hauteur, pour la page qui pose cette figure dans un cadre
const dire_hauteur = () => parent !== window && parent.postMessage({ freinsIso: document.documentElement.scrollHeight }, "*");
new ResizeObserver(dire_hauteur).observe(document.body);
peindre(); dire();
`;

const ISO_CSS = k.ISO_CSS
  .replace(/\.iso-line\[data-flow\]\{[^}]*\}/, "").replace(/\.iso-dots circle\[data-pulse\]\{[^}]*\}/, "")
  .replace(/@keyframes iso-flow\{[^{}]*(\{[^}]*\}[^{}]*)*\}/, "").replace(/@keyframes iso-pulse\{[^{}]*(\{[^}]*\}[^{}]*)*\}/, "");
const CLAIR = k.ISO_CSS.match(/\.iso\[data-theme="light"\]\{([^}]*)\}/)[1].trim();
function page(theme) {
  return `<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">`
    + `<title>Trois freins, la même roue</title><style>${ISO_CSS}${CSS.replace("__CLAIR__", CLAIR)}</style></head>`
    + `<body class="iso" data-theme="${theme}">${corps}<script type="module">${(kitScript() + "\n" + live).replace(/<\/(script)/gi, "<\\/$1")}</script></body></html>`;
}
writeFileSync(join(IMAGES, "freins_iso.html"), page("dark"));
// le mode mission (Pascal, 26/11/2026 : « tout doit être en mode mission »), posé par sa source unique ; il ne s'allume
// que sur la page ouverte seule, jamais dans le cadre de la séquence
execFileSync("python3", [join(IMAGES, "..", "..", "..", "..", "..", "_outils", "mode_mission", "poser.py"), join(IMAGES, "freins_iso.html")]);
const CLAIRE = join(process.env.FREINS_TMP || tmpdir(), "freins_iso-clair.html");
writeFileSync(CLAIRE, page("light"));   // pour la fiche A4 (print.mjs lit la page claire), hors du dépôt

// ── La planche fixe, pour l'impression de la séquence (thème clair, les trois freins côte à côte, serrés) ──
const PW = VW * 3 + LP;
const planche = `<svg xmlns="http://www.w3.org/2000/svg" data-illustration="${ILLUSTRATION}" class="iso" data-theme="light" viewBox="0 0 ${VW * 3} ${VH + 60}" role="img" `
  + `aria-label="Les trois freins sur la même roue : à patins, à disque, à tambour. Les numéros renvoient à la légende de la séquence.">`
  + `<style>${ISO_CSS}${CSS.replace("__CLAIR__", CLAIR)}.fr-titre{font:700 22px system-ui,sans-serif;fill:#111;text-anchor:middle}</style><rect width="100%" height="100%" fill="#fff"/>`
  + Object.keys(FREINS).map((f, i) => `<g transform="translate(${i * VW} 40)"><text class="fr-titre" x="${VW / 2}" y="-12">${FREINS[f].nom}</text>${vue(f)}`
    + `<g transform="translate(${VW - LP * 0.7} 0) scale(0.7)">${loupe(f).replace(/^<svg[^>]*>/, "").replace(/<\/svg>$/, "")}</g></g>`).join("")
  + `</svg>`;
writeFileSync(join(IMAGES, "freins_iso_planche.svg"), planche);
console.log("écrit : Images/freins_iso.html, Images/freins_iso_planche.svg ; page claire : " + CLAIRE);
