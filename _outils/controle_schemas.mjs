/* controle_schemas.mjs — règle d'or n°315 : tout schéma est premium.
 *
 * LE CONSTAT QUI A DONNÉ CE CONTRÔLE
 * ----------------------------------
 * Le 28/10/2026, Pascal regarde la carte des interacteurs de la station de Shenzhen (5e_C2.1) : deux encadrés
 * « Toujours extérieur » et « Interacteur ≠ exigence » sont posés AU MILIEU des familles, collés l'un à l'autre,
 * sur le trajet des flèches. Un élève y lit deux interacteurs de plus — dont celui qui dit qu'une règle n'en est
 * pas un. « Avec le recul, ce schéma peut troubler les élèves… un premium où les entités ne semblent pas se
 * toucher. » Puis : « L'ensemble des schémas doivent être revus. »
 *
 * Un schéma qui trouble n'est pas un défaut de goût : c'est un contenu faux. Ce contrôle mesure ce qui se mesure
 * de ce trouble ; le reste (clarté, beauté, ce que le schéma enseigne) se juge à l'œil, sur la planche qu'il
 * fabrique (--planche).
 *
 * CE QU'IL MESURE, SCHÉMA PAR SCHÉMA
 * ----------------------------------
 * Un CADRE est une forme fermée (rect, ellipse, circle, polygon, path fermé) qui porte au moins un texte et n'est
 * pas le fond. Une FLÈCHE est un trait qui porte une pointe (marker). Les mesures sont en unités du schéma.
 *
 *   ✘ contact     deux cadres dont aucun ne contient l'autre se chevauchent, ou sont à moins de 8 unités.
 *                 (Les cellules d'un tableau — bord contre bord et alignées, ou coin contre coin — ne comptent pas, ni une
 *                 pastille — 32 unités au plus, un repère de 3 caractères au plus — posée sur le coin d'un cadre.)
 *   ✘ débordement un texte ancré dans un cadre (là où il commence, ou son milieu s'il est centré) en dépasse le bord,
 *                 en largeur ou en hauteur.
 *   ✘ superposés  deux textes se recouvrent.
 *   ✘ traversée   une flèche passe dans un cadre qui n'est ni son départ ni son arrivée, ou sur un texte.
 *   ✘ à cheval    un texte dont une partie est dans un cadre qui n'est pas le sien, et l'autre dehors.
 *   ✘ trait sur texte  un trait sans pointe (pointillé ou plein) passe sur un texte, sans fond opaque ni halo qui le cache.
 *   ✘ balise HTML une balise HTML (<b>, <br>, <p>…) dans le code d'un SVG, hors <foreignObject> : la page sort du schéma
 *                 à cette balise, ou le texte disparaît.
 *   ⚠ serré       un texte à moins de 4 unités du bord de son cadre ; deux cadres entre 8 et 16 unités.
 *   ⚠ écrasée     une taille de police posée en attribut, écrasée par la feuille de style du SVG (le titre
 *                 qu'on croyait grand ne l'est pas).
 *   ⚠ minuscule   un texte qui ferait moins de 10 px sur un schéma affiché à 800 px de large.
 *
 * Score = 3 × ✘ + ⚠. Les schémas sont rangés du pire au meilleur.
 *
 * OÙ IL REGARDE
 * -------------
 * Chaque fichier .svg, et chaque schéma écrit dans une page (.html) — un <svg> d'au moins 200 × 80 unités qui
 * porte au moins deux textes. L'archive, node_modules et les dossiers de captures ne sont pas lus.
 *
 * Usage : node _outils/controle_schemas.mjs [dossier ou fichier…] [--json fichier] [--planche dossier] [--muet]
 * Sortie : 0 aucun ✘ · 1 au moins un ✘ · 2 rien n'a pu être lu (règle n°299).
 */
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath, pathToFileURL } from 'url';

const RACINE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const EXCLUS = /(^|\/)(_archive[^/]*|node_modules|\.git|captures[^/]*|banc-docker)(\/|$)/;

function parcourir(chemin, sortie) {
  const st = fs.statSync(chemin);
  if (st.isFile()) { sortie.push(chemin); return sortie; }
  for (const n of fs.readdirSync(chemin)) {
    const p = path.join(chemin, n);
    if (EXCLUS.test(path.relative(RACINE, p))) continue;
    const s = fs.statSync(p);
    if (s.isDirectory()) parcourir(p, sortie); else sortie.push(p);
  }
  return sortie;
}

/* La mesure, exécutée dans le navigateur, pour UN élément <svg>. Coordonnées d'écran (transformations comprises),
   ramenées en unités du schéma. */
const MESURER = (svg) => {
  const R = svg.getBoundingClientRect();
  if (R.width < 2 || R.height < 2) return null;
  const vb = (svg.viewBox && svg.viewBox.baseVal && svg.viewBox.baseVal.width) ? svg.viewBox.baseVal : { width: R.width, height: R.height };
  const k = R.width / vb.width;
  const U = v => v / k;
  const vis = el => { const c = getComputedStyle(el); return c.display !== 'none' && c.visibility !== 'hidden' && +c.opacity > 0.05; };
  const dans = el => !el.closest('defs,marker,clipPath,mask,pattern,symbol');
  const r = el => { const b = el.getBoundingClientRect(); return { x: b.left, y: b.top, w: b.width, h: b.height, X: b.right, Y: b.bottom }; };
  const contientPt = (b, p, m = 0) => p.x > b.x + m && p.x < b.X - m && p.y > b.y + m && p.y < b.Y - m;
  const contient = (A, B, t = 1) => B.x >= A.x - t && B.y >= A.y - t && B.X <= A.X + t && B.Y <= A.Y + t;
  const inter = (A, B) => Math.max(0, Math.min(A.X, B.X) - Math.max(A.x, B.x)) * Math.max(0, Math.min(A.Y, B.Y) - Math.max(A.y, B.y));
  const defauts = [];
  const dit = (g, type, detail) => defauts.push({ g, type, detail });
  const court = s => s.replace(/\s+/g, ' ').trim().slice(0, 48);

  // le point d'ancrage d'un texte : là où il commence (start), son milieu (middle), là où il finit (end)
  const ancre = (el, b) => { const a = getComputedStyle(el).textAnchor; const y = b.y + b.h / 2;
    return a === 'middle' ? { x: b.x + b.w / 2, y } : a === 'end' ? { x: b.X - 2, y } : { x: b.x + 2, y }; };
  // le noyau d'un texte : son encre, sans l'interligne au-dessus de la première ligne ni sous la dernière (mesuré en
  // taille de police, pour qu'un texte de trois lignes ne perde pas trois interlignes)
  const noyau = t => { const fs = parseFloat(getComputedStyle(t.el).fontSize) * k || t.b.h;
    return { x: t.b.x + 1, y: t.b.y + Math.min(0.25 * fs, t.b.h * 0.25), X: t.b.X - 1, Y: t.b.Y - Math.min(0.2 * fs, t.b.h * 0.2) }; };
  const textes = [...svg.querySelectorAll('text')].filter(t => dans(t) && vis(t) && t.textContent.trim())
    .map(t => { const b = r(t); return { el: t, b, s: t.textContent, a: ancre(t, b) }; });
  const peint = el => { const c = getComputedStyle(el); return (c.fill && c.fill !== 'none' && !/url\(/.test(c.fill) && +c.fillOpacity > 0.05) || (c.stroke && c.stroke !== 'none' && +c.strokeWidth > 0); };
  const surfaceSvg = R.width * R.height;
  let cadres = [...svg.querySelectorAll('rect,ellipse,circle,polygon,path')]
    .filter(e => dans(e) && vis(e) && peint(e) && !(e.tagName === 'path' && !/[zZ]\s*$/.test(e.getAttribute('d') || '')))
    .map(e => ({ el: e, b: r(e) }))
    .filter(c => c.b.w * c.b.h < 0.85 * surfaceSvg && U(c.b.w) >= 18 && U(c.b.h) >= 12)
    .filter(c => textes.some(t => contientPt(c.b, t.a)));
  // un voile posé exactement sur un cadre n'est pas un second cadre
  cadres = cadres.filter((c, i) => !cadres.some((d, j) => j < i && Math.abs(d.b.x - c.b.x) < 1 && Math.abs(d.b.y - c.b.y) < 1 && Math.abs(d.b.X - c.b.X) < 1 && Math.abs(d.b.Y - c.b.Y) < 1));

  // La forme vraie de chaque cadre, et non sa boîte englobante : une ellipse n'occupe pas les coins de son rectangle.
  // Contour : 72 points en coordonnées d'écran ; dedans : isPointInFill, dans le repère de la forme.
  for (const c of cadres) {
    const e = c.el, M = e.getScreenCTM(), Mi = M && M.inverse();
    c.rect = e.tagName === 'rect';
    let L = 0; try { L = e.getTotalLength(); } catch (x) { L = 0; }
    c.contour = [];
    if (L > 0 && M) for (let q = 0; q < 72; q++) { const P = e.getPointAtLength(L * q / 72); c.contour.push({ x: M.a * P.x + M.c * P.y + M.e, y: M.b * P.x + M.d * P.y + M.f }); }
    else c.contour = [{ x: c.b.x, y: c.b.y }, { x: c.b.X, y: c.b.y }, { x: c.b.X, y: c.b.Y }, { x: c.b.x, y: c.b.Y }];
    c.dedans = (pt) => {
      if (!Mi || typeof e.isPointInFill !== 'function') return contientPt(c.b, pt);
      const P = new DOMPoint(Mi.a * pt.x + Mi.c * pt.y + Mi.e, Mi.b * pt.x + Mi.d * pt.y + Mi.f);
      try { return e.isPointInFill(P); } catch (x) { return contientPt(c.b, pt); }
    };
    c.bord = (pt) => Math.min(...c.contour.map(q => Math.hypot(q.x - pt.x, q.y - pt.y)));
  }
  // Une PASTILLE (un rond ou un carré de 32 unités au plus, qui porte un repère de 3 caractères au plus : ①, FP1, 3)
  // posée sur le coin d'un cadre en fait partie : ce n'est pas une seconde entité.
  for (const c of cadres) {
    const t = textes.filter(t => c.dedans(t.a));
    c.pastille = U(c.b.w) <= 32 && U(c.b.h) <= 32 && t.length && t.every(t => t.s.trim().length <= 3);
  }
  // ✘ contact / ⚠ serré entre cadres
  for (let i = 0; i < cadres.length; i++) for (let j = i + 1; j < cadres.length; j++) {
    const A = cadres[i], B = cadres[j];
    if (A.pastille || B.pastille) continue;
    if (contient(A.b, B.b) && B.contour.every(A.dedans)) continue;          // B est dans A
    if (contient(B.b, A.b) && A.contour.every(B.dedans)) continue;          // A est dans B
    // les cellules d'un tableau : deux rectangles bord contre bord et alignés, ou coin contre coin
    if (A.rect && B.rect) {
      const dx = Math.max(B.b.x - A.b.X, A.b.x - B.b.X), dy = Math.max(B.b.y - A.b.Y, A.b.y - B.b.Y);
      const coin = Math.abs(U(dx)) <= 1.2 && Math.abs(U(dy)) <= 1.2;
      const ali = (Math.abs(A.b.y - B.b.y) < 1 && Math.abs(A.b.Y - B.b.Y) < 1) || (Math.abs(A.b.x - B.b.x) < 1 && Math.abs(A.b.X - B.b.X) < 1);
      if (coin || (Math.abs(U(Math.max(dx, dy))) <= 1.2 && ali)) continue;
    }
    // loin l'un de l'autre : inutile de mesurer finement
    const dxb = Math.max(B.b.x - A.b.X, A.b.x - B.b.X), dyb = Math.max(B.b.y - A.b.Y, A.b.y - B.b.Y);
    if (U(Math.max(dxb, dyb)) >= 16) continue;
    const chevauche = A.contour.some(B.dedans) || B.contour.some(A.dedans);
    let ecart = Infinity;
    if (!chevauche) for (const p of A.contour) for (const q of B.contour) ecart = Math.min(ecart, Math.hypot(p.x - q.x, p.y - q.y));
    ecart = U(ecart);
    const ta = textes.find(t => A.dedans(t.a)), tb = textes.find(t => B.dedans(t.a));
    const qui = `« ${court(ta ? ta.s : '?')} » / « ${court(tb ? tb.s : '?')} »`;
    if (chevauche) dit('✘', 'contact', `cadres qui se chevauchent : ${qui}`);
    else if (ecart < 8) dit('✘', 'contact', `cadres à ${ecart.toFixed(0)} u : ${qui}`);
    else if (ecart < 16) dit('⚠', 'serré', `cadres à ${ecart.toFixed(0)} u : ${qui}`);
  }
  // ✘ débordement / ⚠ serré pour les textes
  for (const t of textes) {
    const c = t.a;
    const hotes = cadres.filter(x => contientPt(x.b, c)).sort((a, b) => a.b.w * a.b.h - b.b.w * b.b.h);
    if (!hotes.length) continue;
    const H = hotes[0].b;
    const sort = U(Math.max(H.x - t.b.x, t.b.X - H.X, 0));
    if (sort > 1) { dit('✘', 'débordement', `« ${court(t.s)} » dépasse son cadre de ${sort.toFixed(0)} u`); continue; }
    // en hauteur : l'encre du texte (sans l'interligne) sort par le haut ou par le bas
    const n = noyau(t), sortV = U(Math.max(H.y - n.y, n.Y - H.Y, 0));
    if (sortV > 1) { dit('✘', 'débordement', `« ${court(t.s)} » dépasse son cadre de ${sortV.toFixed(0)} u en hauteur`); continue; }
    const marge = U(Math.min(t.b.x - H.x, H.X - t.b.X));
    if (marge < 4 && H.w > t.b.w + 2) dit('⚠', 'serré', `« ${court(t.s)} » à ${Math.max(0, marge).toFixed(0)} u du bord`);
  }
  // ✘ à cheval : un texte dont une partie est dans un cadre et l'autre dehors — ce cadre n'est pas le sien (le sien
  // relève du débordement) : l'élève ne sait pas à quelle entité il appartient. Neuf points de l'encre du texte.
  for (const t of textes) {
    const hote = cadres.filter(x => contientPt(x.b, t.a)).sort((a, b) => a.b.w * a.b.h - b.b.w * b.b.h)[0];
    if (hote && hote.pastille) continue;      // le repère d'une pastille est posé sur le coin d'un cadre, exprès
    const n = noyau(t);
    const pts = [];
    for (const fx of [0.02, 0.5, 0.98]) for (const fy of [0, 0.5, 1]) pts.push({ x: n.x + fx * (n.X - n.x), y: n.y + fy * (n.Y - n.y) });
    for (const c of cadres) {
      if (c === hote || c.pastille) continue;
      // le cadre du texte est lui-même posé à cheval sur c (une étiquette en onglet sur le bord d'une boîte, un fond
      // d'étiquette sur le bord d'un cadre) : c'est voulu, ou c'est un contact entre cadres, mesuré plus haut
      if (hote && hote.contour.some(c.dedans) && !hote.contour.every(c.dedans)) continue;
      const k2 = pts.filter(c.dedans).length;
      if (k2 > 0 && k2 < pts.length) {
        const tc = textes.find(x => x !== t && c.dedans(x.a));
        dit('✘', 'à cheval', `« ${court(t.s)} » à cheval sur le bord du cadre « ${court(tc ? tc.s : '?')} »`);
      }
    }
  }
  // ✘ textes superposés
  for (let i = 0; i < textes.length; i++) for (let j = i + 1; j < textes.length; j++) {
    const A = textes[i].b, B = textes[j].b;
    if (textes[i].el.contains(textes[j].el) || textes[j].el.contains(textes[i].el)) continue;
    const s = inter(A, B), m = Math.min(A.w * A.h, B.w * B.h);
    if (m > 0 && s / m > 0.25) dit('✘', 'superposés', `« ${court(textes[i].s)} » sur « ${court(textes[j].s)} »`);
  }
  // ✘ traversée : flèches
  const fleches = [...svg.querySelectorAll('path,line,polyline')].filter(e => {
    if (!dans(e) || !vis(e)) return false;
    const c = getComputedStyle(e);
    return (c.markerEnd && c.markerEnd !== 'none') || (c.markerStart && c.markerStart !== 'none');
  });
  for (const f of fleches) {
    let L; try { L = f.getTotalLength(); } catch (e) { continue; }
    if (!(L > 0)) continue;
    const M = f.getScreenCTM(); if (!M) continue;
    const pt = s => { const p = f.getPointAtLength(s); return { x: M.a * p.x + M.c * p.y + M.e, y: M.b * p.x + M.d * p.y + M.f }; };
    const p0 = pt(0), p1 = pt(L);
    const bout = 12 * k, pas = Math.max(1.5, L / 300);
    const vus = new Set();
    for (let s = 0; s <= L; s += pas) {
      const p = pt(s);
      const d0 = Math.hypot(p.x - p0.x, p.y - p0.y), d1 = Math.hypot(p.x - p1.x, p.y - p1.y);
      if (d0 < bout || d1 < bout) continue;
      for (const c of cadres) {
        if (vus.has(c) || c.dedans(p0) || c.dedans(p1) || c.bord(p0) < 3 * k || c.bord(p1) < 3 * k) continue;
        if (c.dedans(p) && c.bord(p) > 2 * k) { vus.add(c); const t = textes.find(t => contientPt(c.b, t.a)); dit('✘', 'traversée', `une flèche passe dans le cadre « ${court(t ? t.s : '?')} »`); }
      }
      for (const t of textes) {
        if (vus.has(t)) continue;
        const b = { x: t.b.x + 1, y: t.b.y + t.b.h * 0.25, X: t.b.X - 1, Y: t.b.Y - t.b.h * 0.2 };
        if (p.x > b.x && p.x < b.X && p.y > b.y && p.y < b.Y) { vus.add(t); dit('✘', 'traversée', `une flèche passe sur « ${court(t.s)} »`); }
      }
    }
  }
  // ✘ trait sur un texte : un trait SANS pointe (un pointillé « include », un lien, une courbe) qui passe sur
  // l'encre d'un texte, sans qu'une forme opaque peinte après lui (le fond de l'étiquette) ne le cache, ni un halo
  // autour du texte. Les flèches, elles, sont mesurées plus haut.
  const formesOpaques = [...svg.querySelectorAll('rect,ellipse,circle,polygon,path')].filter(e => {
    if (!dans(e) || !vis(e)) return false;
    const c = getComputedStyle(e);
    return c.fill && c.fill !== 'none' && !/url\(/.test(c.fill) && (+c.fillOpacity) * (+c.opacity) > 0.6;
  });
  const cache = (trait, p) => formesOpaques.some(f => {
    if (f === trait || !(trait.compareDocumentPosition(f) & Node.DOCUMENT_POSITION_FOLLOWING)) return false;
    const Mi = f.getScreenCTM() && f.getScreenCTM().inverse(); if (!Mi) return false;
    try { return f.isPointInFill(new DOMPoint(Mi.a * p.x + Mi.c * p.y + Mi.e, Mi.b * p.x + Mi.d * p.y + Mi.f)); } catch (x) { return false; }
  });
  const halo = t => { const c = getComputedStyle(t.el); return c.stroke && c.stroke !== 'none' && parseFloat(c.strokeWidth) >= 2; };
  const traits = [...svg.querySelectorAll('path,line,polyline')].filter(e => {
    if (!dans(e) || !vis(e) || fleches.includes(e) || cadres.some(c => c.el === e)) return false;
    // un trait découpé (clip-path, masque) n'est visible qu'en partie : on ne sait pas où, on ne le mesure pas
    for (let a = e; a && a !== svg.parentElement; a = a.parentElement) {
      const c = getComputedStyle(a);
      if ((c.clipPath && c.clipPath !== 'none') || (c.mask && c.mask !== 'none') || a.hasAttribute('clip-path') || a.hasAttribute('mask')) return false;
    }
    if (e.tagName === 'path' && /[zZ]\s*$/.test(e.getAttribute('d') || '')) return false;
    const c = getComputedStyle(e);
    return c.stroke && c.stroke !== 'none' && parseFloat(c.strokeWidth) > 0 && +c.strokeOpacity > 0.2;
  });
  for (const f of traits) {
    let L; try { L = f.getTotalLength(); } catch (e) { continue; }
    if (!(L > 0) || U(L) < 15) continue;
    const M = f.getScreenCTM(); if (!M) continue;
    const pt = s => { const p = f.getPointAtLength(s); return { x: M.a * p.x + M.c * p.y + M.e, y: M.b * p.x + M.d * p.y + M.f }; };
    const p0 = pt(0), p1 = pt(L), bout = 4 * k, pas = Math.max(1.5, L / 300);
    const vus = new Set();
    for (let s = 0; s <= L; s += pas) {
      const p = pt(s);
      if (Math.hypot(p.x - p0.x, p.y - p0.y) < bout || Math.hypot(p.x - p1.x, p.y - p1.y) < bout) continue;
      for (const t of textes) {
        if (vus.has(t) || halo(t)) continue;
        const b = noyau(t);
        if (p.x > b.x && p.x < b.X && p.y > b.y && p.y < b.Y && !cache(f, p)) {
          vus.add(t);
          dit('✘', 'trait sur texte', `un trait${getComputedStyle(f).strokeDasharray !== 'none' ? ' pointillé' : ''} passe sur « ${court(t.s)} »`);
        }
      }
    }
  }
  // ⚠ taille écrasée, ⚠ minuscule
  let ecrasees = 0, petits = 0;
  for (const t of textes) {
    const a = t.el.getAttribute('font-size');
    const cs = parseFloat(getComputedStyle(t.el).fontSize);
    if (a && !/%|em/.test(a) && Math.abs(parseFloat(a) - cs) > 0.5) ecrasees++;
    if (cs * 800 / vb.width < 10) petits++;
  }
  if (ecrasees) dit('⚠', 'écrasée', `${ecrasees} taille(s) de police posée(s) en attribut, écrasée(s) par la feuille de style`);
  if (petits) dit('⚠', 'minuscule', `${petits} texte(s) sous 10 px pour un schéma de 800 px de large`);
  return { largeur: Math.round(vb.width), hauteur: Math.round(vb.height), cadres: cadres.length, textes: textes.length, fleches: fleches.length, defauts };
};

async function main(argv) {
  const muet = argv.includes('--muet');
  const opt = n => { const i = argv.indexOf(n); return i >= 0 ? argv[i + 1] : null; };
  const json = opt('--json'), planche = opt('--planche');
  const cibles = argv.filter((a, i) => !a.startsWith('--') && !['--json', '--planche'].includes(argv[i - 1]));
  const racines = cibles.length ? cibles.map(c => path.resolve(c)) : fs.readdirSync(RACINE).filter(n => /^theme-/.test(n)).map(n => path.join(RACINE, n));
  const fichiers = racines.flatMap(r => parcourir(r, []));
  const svgs = fichiers.filter(f => f.endsWith('.svg'));
  const pages = fichiers.filter(f => f.endsWith('.html') && fs.readFileSync(f, 'utf8').includes('<svg'));
  if (planche) fs.mkdirSync(planche, { recursive: true });

  const nav = await chromium.launch();
  const ctx = await nav.newContext({ viewport: { width: 1000, height: 800 } });
  const p = await ctx.newPage();
  p.setDefaultTimeout(15000);
  // Une capture « page entière » d'un document SVG attend des polices qui ne viennent jamais (Chromium) : on capture
  // donc une zone (clip), en coordonnées de la fenêtre.
  const capturer = async (fichier, b) => p.screenshot({ path: fichier, clip: b, timeout: 10000 });
  const resultats = [];
  let n = 0;
  for (const f of svgs) {
    try {
      await p.setViewportSize({ width: 1000, height: 800 });
      await p.goto(pathToFileURL(f).href);
      // la fenêtre prend les proportions du schéma : 1 000 px de large
      const vb = await p.evaluate(() => { const v = document.documentElement.viewBox; return v && v.baseVal && v.baseVal.width ? [v.baseVal.width, v.baseVal.height] : null; });
      if (vb) await p.setViewportSize({ width: 1000, height: Math.max(100, Math.min(4000, Math.round(1000 * vb[1] / vb[0]))) });
      const m = await p.evaluate(`(${MESURER})(document.documentElement)`);
      if (!m) continue;
      const nom = path.relative(RACINE, f);
      const r = { schema: nom, ...m };
      if (planche) {
        r.image = `s${String(++n).padStart(4, '0')}.png`;
        const bb = await p.evaluate(() => { const r = document.documentElement.getBoundingClientRect(); return { x: 0, y: 0, width: Math.max(10, Math.min(innerWidth, Math.ceil(r.width))), height: Math.max(10, Math.min(innerHeight, Math.ceil(r.height))) }; });
        await capturer(path.join(planche, r.image), bb).catch(() => { r.image = null; });
      }
      resultats.push(r);
    } catch (e) { resultats.push({ schema: path.relative(RACINE, f), erreur: String(e).slice(0, 120), defauts: [] }); }
  }
  for (const f of pages) {
    try {
      await p.setViewportSize({ width: 1000, height: 2400 });
      await p.goto(pathToFileURL(f).href); await p.waitForTimeout(150);
      const nb = await p.evaluate(() => [...document.querySelectorAll('svg')].length);
      for (let i = 0; i < nb; i++) {
        const m = await p.evaluate(([i, src]) => {
          const svg = document.querySelectorAll('svg')[i];
          if (!svg || svg.closest('svg') !== svg || svg.parentElement.closest('svg')) return null;
          const vb = svg.viewBox && svg.viewBox.baseVal;
          if (!vb || vb.width < 200 || vb.height < 80 || svg.querySelectorAll('text').length < 2) return null;
          for (let a = svg; a; a = a.parentElement) {           // rendre visible ce qui est replié ou masqué
            if (a.tagName === 'DETAILS') a.open = true;
            if (a.hidden) a.hidden = false;
            if (getComputedStyle(a).display === 'none') a.style.display = 'block';
          }
          svg.setAttribute('data-mesure', String(i));
          return eval(src)(svg);
        }, [i, `(${MESURER})`]);
        if (!m) continue;
        const r = { schema: `${path.relative(RACINE, f)} › svg n°${i + 1}`, ...m };
        if (planche) {
          r.image = `s${String(++n).padStart(4, '0')}.png`;
          const b = await p.evaluate(i => { const s = document.querySelector(`svg[data-mesure="${i}"]`); s.scrollIntoView({ block: 'start' });
            const r = s.getBoundingClientRect(); return { x: Math.max(0, r.left), y: Math.max(0, r.top), width: Math.min(r.width, innerWidth), height: Math.min(r.height, innerHeight) }; }, i);
          if (b.width > 2 && b.height > 2) await capturer(path.join(planche, r.image), b).catch(() => { r.image = null; }); else r.image = null;
        }
        resultats.push(r);
      }
    } catch (e) { resultats.push({ schema: path.relative(RACINE, f), erreur: String(e).slice(0, 120), defauts: [] }); }
  }
  await nav.close();

  // ✘ balise HTML dans un SVG : lue dans le CODE, avant tout rendu. Dans une page, l'analyseur HTML sort du SVG à la
  // première balise <b>, <br>, <p>… : tout ce qui suit (P2, P3…) quitte le schéma, sans erreur visible. Dans un
  // fichier .svg, la balise est inconnue et son texte disparaît. Le HTML d'un <foreignObject> (exports draw.io) est
  // permis : il est fait pour ça.
  const HTML_SORT = /<(b|big|blockquote|body|br|center|code|dd|div|dl|dt|em|embed|h[1-6]|head|hr|i|img|li|listing|menu|meta|nobr|ol|p|pre|ruby|s|small|span|strike|strong|sub|sup|table|tt|u|ul|var)(?=[\s>\/])/g;
  const balises = (code) => {
    const net = code.replace(/<!--[\s\S]*?-->/g, '').replace(/<(style|script)[\s\S]*?<\/\1>/g, '')
      .replace(/<foreignObject[\s\S]*?<\/foreignObject>/g, '');
    return [...new Set([...net.matchAll(HTML_SORT)].map(m => '<' + m[1] + '>'))];
  };
  for (const f of svgs) {
    const l = balises(fs.readFileSync(f, 'utf8'));
    if (!l.length) continue;
    const nom = path.relative(RACINE, f);
    let r = resultats.find(x => x.schema === nom);
    if (!r) { r = { schema: nom, defauts: [] }; resultats.push(r); }
    r.defauts.push({ g: '✘', type: 'balise HTML', detail: `${l.join(', ')} dans le SVG : son texte ne s'affiche pas` });
  }
  for (const f of pages) {
    const code = fs.readFileSync(f, 'utf8').replace(/<script[\s\S]*?<\/script>/g, '');   // un SVG écrit par un script n'est pas lu par l'analyseur de la page
    const blocs = [...code.matchAll(/<svg[\s>][\s\S]*?<\/svg>/g)];
    blocs.forEach((m, i) => {
      const l = balises(m[0]);
      if (!l.length) return;
      resultats.push({ schema: `${path.relative(RACINE, f)} › code du svg n°${i + 1}`,
        defauts: [{ g: '✘', type: 'balise HTML', detail: `${l.join(', ')} dans le SVG : la page sort du schéma à cette balise` }] });
    });
  }

  for (const r of resultats) {
    r.croix = r.defauts.filter(d => d.g === '✘').length;
    r.alertes = r.defauts.filter(d => d.g === '⚠').length;
    r.score = 3 * r.croix + r.alertes;
  }
  resultats.sort((a, b) => b.score - a.score || a.schema.localeCompare(b.schema));
  const croix = resultats.reduce((s, r) => s + r.croix, 0);
  const touches = resultats.filter(r => r.croix).length;
  if (!muet) {
    for (const r of resultats.filter(r => r.score || r.erreur)) {
      console.log(`${String(r.score).padStart(3)}  ${r.schema}${r.erreur ? '  (illisible : ' + r.erreur + ')' : ''}`);
      const parType = {};
      for (const d of r.defauts) (parType[d.g + ' ' + d.type] ||= []).push(d.detail);
      for (const [t, l] of Object.entries(parType)) console.log(`       ${t} ×${l.length} — ${l[0]}`);
    }
    console.log(`\n${resultats.length} schémas lus (${svgs.length} fichiers SVG, ${resultats.length - svgs.length} écrits dans ${pages.length} pages)`);
    console.log(`${touches} schéma(s) avec au moins un ✘ · ${croix} ✘ · ${resultats.reduce((s, r) => s + r.alertes, 0)} ⚠`);
  }
  if (json) fs.writeFileSync(json, JSON.stringify(resultats, null, 1));
  if (planche) {
    const lignes = resultats.map(r => `<figure><figcaption><b>${r.score}</b> · ${r.schema.replace(/&/g, '&amp;').replace(/</g, '&lt;')}<br><small>${r.defauts.map(d => d.g + ' ' + d.type + ' : ' + d.detail).join('<br>').replace(/</g, '&lt;').replace(/&lt;br>/g, '<br>')}</small></figcaption>${r.image ? `<img src="${r.image}" loading="lazy">` : ''}</figure>`);
    fs.writeFileSync(path.join(planche, 'index.html'), `<!doctype html><meta charset="utf-8"><title>Planche des schémas</title><style>body{font:14px system-ui;background:#111;color:#eee;margin:16px}figure{margin:0 0 28px;padding:10px;background:#1b1b1b;border-radius:8px}img{max-width:100%;background:#fff}small{color:#f9b}</style>${lignes.join('\n')}`);
  }
  if (!resultats.length) return 2;
  return croix ? 1 : 0;
}

export function lanceDirectement(url, argv1) {
  if (!argv1) return false;
  return path.resolve(fileURLToPath(url)) === path.resolve(argv1);
}

if (lanceDirectement(import.meta.url, process.argv[1])) {
  process.exit(await main(process.argv.slice(2)));
}
