/* Chaîne pas à pas — moteur des chaînes d'énergie et d'information animées (pilote du 30/10/2026, 5e_C4.1).
   Source : 5e_C4.1/_generation/chaine_pas_a_pas/moteur_chaine.js, posé dans la page par poser.py (même dossier) :
   ne pas le modifier dans une page.

   La page DÉCLARE, le moteur DESSINE et ANIME. Le lecteur commun (LecteurPasAPas) garde le reste : étapes, voix,
   « Regarder », mouvement réduit, impression, lien direct. Rien ne bouge sans un geste : le moteur n'a pas de boucle,
   c'est le lecteur qui l'appelle (entrer, maj, fixe).

   DÉCLARATION (un objet JavaScript dans la page)
     { seuil: 820,                         // largeur du dessin (px) sous laquelle on passe à la disposition étroite
       large:  {vue: [x, y, l, h], tailles: {...}, bloc: {...}, particule: {...}, jeton: {...}},
       etroit: {vue: [...], ...},          // la même chose, en colonne (règle n°310, piège 8)
       elements: [ ... ],                  // une seule liste : les MOTS sont écrits une fois, pour les deux dispositions
       etapes: [ ... ] }                   // le tableau SCENES du lecteur, enrichi de ce que montre chaque étape
   Éléments (chacun : id, type, puis sa géométrie dans `large` et dans `etroit` ; absent d'une disposition = pas dessiné) :
     section  {texte, couleur}                              géométrie {x, y}
     bloc     {fonction, composant, stock?, couleur}        géométrie {x, y, l}        (le composant SOUS le bloc)
     absent   {fonction, raison}                            géométrie {x, y, l}        (pointillés grisés, n°131)
     fleche   {nature, texte?, double?, pointilles?}        géométrie {points, ex, ey, ancre?, taille?, jeton?: [dx, dy]}
              nature : energie (orange), information (cyan), ordre (vert), stock (jaune), matiere (bleu)
     texte    {texte, couleur?, gras?, taille?}             géométrie {x, y, ancre?}
   Une géométrie peut redonner `texte`, `composant` ou `stock` pour couper les lignes autrement (\n) : les mots doivent
   rester les mêmes, le moteur le vérifie (sinon il garde ceux de l'élément et le dit dans la console).
   Options d'élément : de / a (étapes où il se voit), garde (jamais en retrait).
   Étapes : actifs [ids] (mis en valeur ; les autres en retrait), tous (rien en retrait), flux [ids ; « -id » à rebours]
   (des grains d'énergie circulent), jetons [{texte (ou fonction du temps), chemin [ids de flèches], periode, fixe}]
   (un message porté le long des flèches ; entre deux flèches, il traverse le bloc ; fixe : sa place dans l'image fixe,
   une fraction du trajet ou [x, y] à côté de la flèche, ou {large: …, etroit: …}), vise [ids] (la zone à montrer
   dans la boîte qui défile, en disposition étroite ; par défaut les actifs).

   API : ChainePasAPas(svg, declaration, {boite, decor, apres}) → {entrer(n), maj(dt, n, t), fixe(n), dispo(), rendre()}
     boite : l'élément qui contient le dessin (sa largeur choisit la disposition ; il défile en disposition étroite) ;
     decor(calque, dispo) : la page dessine ce qui lui est propre (le ciel, le parking…) dans un calque sous la chaîne ;
     apres(n) : appelé quand la disposition change (le dessin a été refait), pour remettre le décor à l'étape n.
   Le texte d'un élément « texte » peut avoir une taille par disposition : taille: {large: 52, etroit: 30}.
   Couleurs (n°120, les mêmes que les schémas fixes) : CONVERTIR #c68ef2, ALIMENTER/STOCKER #ffd66b, DISTRIBUER #61dafb ;
   flux d'énergie #ffb454, d'information #61dafb, ordre #81fba1 en pointillés. */
(function(){
  "use strict";
  if (window.ChainePasAPas) return;
  var NS = "http://www.w3.org/2000/svg";
  var calme = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : {matches: false};
  var NATURE = {energie: "#ffb454", information: "#61dafb", ordre: "#81fba1", stock: "#ffd66b", matiere: "#7cc4ff"};
  var BLANC = "#e4eaf5", FOND = "#0d2347", PAPIER = "#050f24", GRIS = "#9aa5b8";
  var DEFAUT = {
    large:  {tailles: {section: 23, fonction: 23, composant: 21, stock: 20, fleche: 20, texte: 22, jeton: 20},
             bloc: {h: 76, rx: 12, trait: 3, ecart: 14, interligne: 7, halo: 16},
             particule: {r: 6, pas: 64, v: 150}, jeton: {h: 30, marge: 14}},
    etroit: {tailles: {section: 14, fonction: 16, composant: 14, stock: 13, fleche: 13, texte: 15, jeton: 13},
             bloc: {h: 40, rx: 8, trait: 2.4, ecart: 6, interligne: 4, halo: 10},
             particule: {r: 3.4, pas: 28, v: 62}, jeton: {h: 21, marge: 9}}
  };

  function cree(nom, attrs, parent){
    var e = document.createElementNS(NS, nom);
    for (var k in attrs) if (attrs[k] !== null && attrs[k] !== undefined) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function mots(t){ return String(t || "").replace(/\s+/g, " ").trim(); }
  function fusion(a, b){ var r = {}, k; for (k in a) r[k] = a[k]; for (k in (b || {})) r[k] = b[k]; return r; }
  function n1(v){ return Math.round(v * 10) / 10; }

  // ── Une ligne brisée : longueur, point à une distance donnée ──
  function troncons(pts){
    var t = [], tot = 0;
    for (var i = 1; i < pts.length; i++) {
      var dx = pts[i][0] - pts[i - 1][0], dy = pts[i][1] - pts[i - 1][1], l = Math.sqrt(dx * dx + dy * dy);
      t.push({a: pts[i - 1], dx: dx, dy: dy, l: l, d: tot}); tot += l;
    }
    return {t: t, L: tot};
  }
  function pointA(c, s){
    s = Math.max(0, Math.min(c.L, s));
    for (var i = 0; i < c.t.length; i++) {
      var u = c.t[i];
      if (s <= u.d + u.l || i === c.t.length - 1) { var f = u.l ? (s - u.d) / u.l : 0; return [u.a[0] + u.dx * f, u.a[1] + u.dy * f]; }
    }
    return [0, 0];
  }

  function ChainePasAPas(svg, decl, opts){
    if (!svg || !decl) return null;
    opts = opts || {};
    var boite = opts.boite || svg.parentNode;
    var prefixe = (svg.id || "chx") + "-";
    var ELEMENTS = decl.elements || [], ETAPES = decl.etapes || [];
    var dispo = null, etape = 1, P = null, groupes = {}, geos = {}, chemins = {};
    var calqueGrains = null, calqueJetons = null, calqueDecor = null;
    var grains = [], jetons = [];

    function choisir(){
      var w = boite ? boite.clientWidth : 0;
      if (!w) return dispo || "large";                    // caché (séance fermée) : on garde la disposition
      return w < (decl.seuil || 820) ? "etroit" : "large";
    }
    function texteDe(def, geo, cle){                       // mêmes mots dans les deux dispositions, coupés autrement
      var base = def[cle];
      if (geo && geo[cle] !== undefined) {
        if (mots(geo[cle]) === mots(base)) return geo[cle];
        if (window.console) console.error("ChainePasAPas : « " + mots(geo[cle]) + " » n'a pas les mots de « " + mots(base) + " »");
      }
      return base;
    }
    function lignes(parent, x, y, texte, attrs, taille, interligne){
      var ls = String(texte).split("\n");
      ls.forEach(function(l, i){
        var t = cree("text", fusion({x: x, y: n1(y + i * (taille + interligne)), "font-size": taille}, attrs), parent);
        t.textContent = l;
      });
      return ls.length;
    }
    function largeurTexte(t, taille, gras){ return t.length * taille * (gras ? .6 : .54); }

    // ── Dessiner, pour la disposition choisie ──
    function rendre(){
      dispo = choisir();
      var D = decl[dispo] || {};
      P = {
        tailles: fusion(DEFAUT[dispo].tailles, D.tailles), bloc: fusion(DEFAUT[dispo].bloc, D.bloc),
        particule: fusion(DEFAUT[dispo].particule, D.particule), jeton: fusion(DEFAUT[dispo].jeton, D.jeton)
      };
      while (svg.firstChild) svg.removeChild(svg.firstChild);
      svg.setAttribute("viewBox", D.vue.join(" "));
      svg.setAttribute("data-dispo", dispo);
      if (boite) { boite.classList.toggle("chx-etroite", dispo === "etroit"); if (D.max) boite.style.setProperty("--chx-max", D.max + "px"); }
      var defs = cree("defs", {}, svg);
      Object.keys(NATURE).forEach(function(n){
        var m = cree("marker", {id: prefixe + n, viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: dispo === "etroit" ? 8 : 12,
                                markerHeight: dispo === "etroit" ? 8 : 12, orient: "auto-start-reverse", markerUnits: "userSpaceOnUse"}, defs);
        cree("path", {d: "M0 0L10 5L0 10Z", fill: NATURE[n]}, m);
      });
      cree("rect", {"class": "chx-papier", x: D.vue[0], y: D.vue[1], width: D.vue[2], height: D.vue[3], fill: PAPIER}, svg);
      calqueDecor = cree("g", {"class": "chx-decor"}, svg);
      var calqueEl = cree("g", {"class": "chx-elements"}, svg);
      calqueGrains = cree("g", {"class": "chx-grains"}, svg);
      calqueJetons = cree("g", {"class": "chx-jetons"}, svg);
      groupes = {}; geos = {}; chemins = {};
      ELEMENTS.forEach(function(def){
        var geo = def[dispo];
        if (!geo) return;
        var g = cree("g", {"class": "chx-el chx-" + def.type, "data-id": def.id}, calqueEl);
        groupes[def.id] = g; geos[def.id] = geo;
        dessiner(def, geo, g);
      });
      if (opts.decor) opts.decor(calqueDecor, dispo);
      appliquer(etape, true);
    }

    function dessiner(def, geo, g){
      var T = P.tailles, B = P.bloc;
      if (def.type === "section") {
        lignes(g, geo.x, geo.y, texteDe(def, geo, "texte"), {fill: def.couleur || BLANC, "font-weight": 700}, T.section, 5);
      } else if (def.type === "bloc" || def.type === "absent") {
        var l = geo.l, h = B.h, cx = geo.x + l / 2, abs = def.type === "absent", c = abs ? GRIS : def.couleur;
        if (!abs) cree("rect", {"class": "chx-halo", x: geo.x, y: geo.y, width: l, height: h, rx: B.rx, fill: "none", stroke: c, "stroke-width": B.halo}, g);
        cree("rect", {"class": "chx-cadre", x: geo.x, y: geo.y, width: l, height: h, rx: B.rx, fill: abs ? "none" : FOND, stroke: c,
                      "stroke-width": B.trait, "stroke-dasharray": abs ? (dispo === "etroit" ? "5 4" : "8 6") : null}, g);
        var f = texteDe(def, geo, "fonction"), nf = String(f).split("\n").length;
        lignes(g, cx, geo.y + h / 2 + T.fonction * .36 - (nf - 1) * (T.fonction + 2) / 2, f,
               {fill: c, "font-weight": 700, "text-anchor": "middle", "letter-spacing": dispo === "etroit" ? ".02em" : null}, T.fonction, 2);
        var y = geo.y + h + B.ecart + T.composant;
        var sous = texteDe(def, geo, abs ? "raison" : "composant");
        if (sous) {
          var n = lignes(g, cx, y, sous, {fill: abs ? GRIS : BLANC, "text-anchor": "middle", "font-style": abs ? "italic" : null}, T.composant, B.interligne);
          y += n * (T.composant + B.interligne);
        }
        if (def.stock) lignes(g, cx, y, texteDe(def, geo, "stock"), {fill: NATURE.stock, "text-anchor": "middle"}, T.stock, B.interligne);
      } else if (def.type === "fleche") {
        var coul = NATURE[def.nature] || NATURE.energie, pts = geo.points;
        chemins[def.id] = troncons(pts);
        cree("path", {"class": "chx-trait", d: "M" + pts.map(function(p){ return p[0] + " " + p[1]; }).join(" L"), fill: "none",
                      stroke: coul, "stroke-width": B.trait, "stroke-linejoin": "round",
                      "stroke-dasharray": def.pointilles ? (dispo === "etroit" ? "6 4" : "8 6") : null,
                      "marker-end": "url(#" + prefixe + (def.nature || "energie") + ")",
                      "marker-start": def.double ? "url(#" + prefixe + (def.nature || "energie") + ")" : null}, g);
        if (def.texte) lignes(g, geo.ex, geo.ey, texteDe(def, geo, "texte"), {fill: coul, "text-anchor": geo.ancre || "middle"}, geo.taille || T.fleche, 5);
      } else if (def.type === "texte") {
        var tl = def.taille ? def.taille[dispo] || T.texte : T.texte;
        lignes(g, geo.x, geo.y, texteDe(def, geo, "texte"), {fill: def.couleur || BLANC, "font-weight": def.gras ? 700 : 400,
               "text-anchor": geo.ancre || "middle"}, tl, 6);
      }
    }

    // ── Une étape : ce qui est en valeur, ce qui circule ──
    function appliquer(n, sansDefiler){
      etape = n;
      var s = ETAPES[n - 1] || {}, actifs = {};
      (s.actifs || []).forEach(function(id){ actifs[id] = true; });
      ELEMENTS.forEach(function(def){
        var g = groupes[def.id];
        if (!g) return;
        var vu = !((def.de && n < def.de) || (def.a && n > def.a));
        g.classList.toggle("chx-cache", !vu);
        g.classList.toggle("chx-actif", !s.tous && !!actifs[def.id]);
        g.classList.toggle("chx-retrait", !s.tous && !actifs[def.id] && !def.garde);
      });
      // les grains d'énergie
      while (calqueGrains.firstChild) calqueGrains.removeChild(calqueGrains.firstChild);
      grains = [];
      (s.flux || []).forEach(function(f){
        var rebours = f.charAt(0) === "-", id = rebours ? f.slice(1) : f, c = chemins[id];
        if (!c) return;
        var def = ELEMENTS.filter(function(e){ return e.id === id; })[0] || {};
        var pts = geos[id].points.slice(); if (rebours) pts.reverse();
        var ch = rebours ? troncons(pts) : c, nb = Math.max(2, Math.round(ch.L / P.particule.pas));
        for (var i = 0; i < nb; i++) grains.push({c: ch, s: (i + .5) * ch.L / nb,
          e: cree("circle", {r: P.particule.r, fill: NATURE[def.nature] || NATURE.energie, "class": "chx-grain"}, calqueGrains)});
      });
      // les jetons : un message porté le long des flèches
      while (calqueJetons.firstChild) calqueJetons.removeChild(calqueJetons.firstChild);
      jetons = [];
      (s.jetons || []).forEach(function(j){
        var ids = (j.chemin || []).filter(function(id){ return chemins[id]; });
        var segs = ids.map(function(id){ return chemins[id]; });
        if (!segs.length) return;
        var def = ELEMENTS.filter(function(e){ return e.id === j.chemin[0]; })[0] || {};
        var coul = j.couleur || NATURE[def.nature] || NATURE.information;
        var g = cree("g", {"class": "chx-jeton"}, calqueJetons);
        var r = cree("rect", {rx: P.jeton.h / 2, height: P.jeton.h, fill: FOND, stroke: coul, "stroke-width": dispo === "etroit" ? 1.6 : 2.4}, g);
        var t = cree("text", {"text-anchor": "middle", fill: coul, "font-weight": 700, "font-size": P.tailles.jeton}, g);
        var J = {def: j, ids: ids, segs: segs, g: g, r: r, t: t, w: 0, lance: -1};
        texteJeton(J, 0);                                  // sa largeur sert à ses bornes
        jetons.push(J);
      });
      if (!sansDefiler) viser(s);
    }
    // Sur chaque flèche, le jeton laisse libres les deux bouts : la pastille ne touche ni le bloc qu'elle quitte ni
    // celui qu'elle rejoint (n°315). Une flèche trop courte la garde au milieu.
    function bornes(J, i){
      var c = J.segs[i], t0 = c.t[0], t1 = c.t[c.t.length - 1];
      function ext(t){ var l = t.l || 1; return Math.abs(t.dx) / l * J.w / 2 + Math.abs(t.dy) / l * P.jeton.h / 2 + 4; }
      var a = ext(t0), b = c.L - ext(t1);
      return a < b ? [a, b] : [c.L / 2, c.L / 2];
    }
    function placer(J, i, d){                              // le jeton sur la flèche i, à la distance d de sa première
      var bo = bornes(J, i), p = pointA(J.segs[i], bo[0] + d);              // borne ; une flèche peut le décaler
      var o = (geos[J.ids[i]] || {}).jeton || [0, 0];                       // (jeton: [dx, dy])
      J.g.setAttribute("transform", "translate(" + n1(p[0] + o[0]) + " " + n1(p[1] + o[1]) + ")");
      J.g.style.opacity = 1;
    }
    function utile(J, i){ var bo = bornes(J, i); return bo[1] - bo[0]; }
    var VJ = function(){ return P.particule.v * .9; }, PAUSE = .45;
    function poserJeton(J, tps){                          // tps : temps depuis le départ du jeton (s)
      var reste = tps, i;
      for (i = 0; i < J.segs.length; i++) {
        var duree = utile(J, i) / VJ();
        if (reste <= duree) break;
        reste -= duree;
        if (i < J.segs.length - 1) { if (reste <= PAUSE) { J.g.style.opacity = 0; return false; } reste -= PAUSE; }
      }
      if (i >= J.segs.length) { i = J.segs.length - 1; reste = utile(J, i) / VJ(); }
      placer(J, i, reste * VJ());
      return true;
    }
    function texteJeton(J, t){
      var txt = String(typeof J.def.texte === "function" ? J.def.texte(t) : J.def.texte);
      if (J.t.textContent !== txt) {
        J.t.textContent = txt;
        J.w = largeurTexte(txt, P.tailles.jeton, true) + 2 * P.jeton.marge;
        J.r.setAttribute("width", n1(J.w)); J.r.setAttribute("x", n1(-J.w / 2)); J.r.setAttribute("y", n1(-P.jeton.h / 2));
        J.t.setAttribute("y", n1(P.tailles.jeton * .36));
      }
    }
    function dureeChemin(J){
      var d = 0;
      J.segs.forEach(function(c, i){ d += utile(J, i) / VJ() + (i ? PAUSE : 0); });
      return d;
    }

    // ── Le temps : appelé par le lecteur, seulement à l'écran et si le mouvement est permis ──
    function maj(dt, n, t){
      grains.forEach(function(g){
        g.s = (g.s + P.particule.v * dt) % g.c.L;
        var p = pointA(g.c, g.s), bord = Math.min(g.s, g.c.L - g.s) / (P.particule.pas * .6);
        g.e.setAttribute("cx", n1(p[0])); g.e.setAttribute("cy", n1(p[1]));
        g.e.setAttribute("opacity", n1(Math.max(0, Math.min(1, bord))));
      });
      jetons.forEach(function(J){
        var periode = J.def.periode || dureeChemin(J) + 1.2, tps = t % periode, depart = t - tps;
        if (depart !== J.lance) { J.lance = depart; texteJeton(J, t); }
        if (tps > dureeChemin(J) + .6) J.g.style.opacity = 0; else poserJeton(J, tps);
      });
    }
    // ── Mouvement réduit, impression : une image fixe par étape ──
    function fixe(n){
      grains.forEach(function(g){
        var p = pointA(g.c, g.s);
        g.e.setAttribute("cx", n1(p[0])); g.e.setAttribute("cy", n1(p[1])); g.e.setAttribute("opacity", 1);
      });
      jetons.forEach(function(J){
        texteJeton(J, 1e6);
        var f = J.def.fixe !== undefined ? J.def.fixe : .8, total = 0, k;
        if (f && typeof f === "object" && !Array.isArray(f)) f = f[dispo] !== undefined ? f[dispo] : .8;
        if (Array.isArray(f)) {                           // une place choisie à la main, à côté de la flèche
          J.g.setAttribute("transform", "translate(" + f[0] + " " + f[1] + ")"); J.g.style.opacity = 1; return;
        }
        J.segs.forEach(function(c, i){ total += utile(J, i); });
        var d = f * total;
        for (k = 0; k < J.segs.length - 1 && d > utile(J, k); k++) d -= utile(J, k);
        placer(J, k, d);
      });
    }

    // ── Disposition étroite : la boîte défile jusqu'à ce qui se passe ──
    function viser(s){
      if (dispo !== "etroit" || !boite || boite.scrollHeight <= boite.clientHeight + 2) return;
      var ids = s.vise || (s.tous ? [] : s.actifs || []), haut = Infinity, bas = -Infinity;
      ids.forEach(function(id){
        var g = groupes[id];
        if (!g || g.classList.contains("chx-cache")) return;
        try { var b = g.getBBox(); haut = Math.min(haut, b.y); bas = Math.max(bas, b.y + b.height); } catch (e) {}
      });
      var vue = decl[dispo].vue, rs = svg.getBoundingClientRect(), k = rs.width / vue[2];
      var haut0 = rs.top - boite.getBoundingClientRect().top + boite.scrollTop;   // le haut du dessin, dans la boîte
      var cible = haut === Infinity ? 0 : haut0 + ((haut + bas) / 2 - vue[1]) * k - boite.clientHeight / 2;
      cible = Math.max(0, Math.min(boite.scrollHeight - boite.clientHeight, cible));
      if (boite.scrollTo) boite.scrollTo({top: cible, behavior: calme.matches ? "auto" : "smooth"}); else boite.scrollTop = cible;
    }

    if (window.ResizeObserver && boite) new ResizeObserver(function(){
      if (choisir() === dispo) { viser(ETAPES[etape - 1] || {}); return; }   // la boîte s'ouvre ou change de taille
      // la disposition change : on redessine
      rendre();                                           // la page redessine son décor (opts.decor), puis l'état
      if (opts.apres) opts.apres(etape);                  // de l'étape en cours : image fixe ou premier instant
      if (calme.matches) fixe(etape); else maj(0, etape, 0);
    }).observe(boite);
    rendre();

    return {
      entrer: function(n){ appliquer(n); },
      maj: maj,
      fixe: fixe,
      dispo: function(){ return dispo; },
      rendre: rendre,
      groupe: function(id){ return groupes[id] || null; }
    };
  }
  window.ChainePasAPas = ChainePasAPas;
})();
