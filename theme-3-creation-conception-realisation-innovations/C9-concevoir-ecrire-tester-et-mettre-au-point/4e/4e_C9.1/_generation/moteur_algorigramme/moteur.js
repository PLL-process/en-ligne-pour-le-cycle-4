/* Moteur des algorigrammes et chronogrammes animés (pilote : 4e_C9.1, la pompe qui s'affole, 30/10/2026).
   Source unique : 4e_C9.1/_generation/moteur_algorigramme/moteur.js (et moteur.css), posée dans la page par
   poser.py, entre deux marqueurs « moteur-algorigramme v1 ». Ne pas le modifier dans la page.

   LA PAGE DÉCLARE                                     LE MOTEUR
   · ses blocs : forme, place, texte, et soit un test   · dessine l'algorigramme (formes, flèches, OUI / NON)
     (losange), soit un effet sur l'état (action)       · calcule, pour chaque valeur de la série, le chemin du
   · ses flèches : de, a, sortie (oui / non), points      jeton et l'état qui en sort (une mémoire : l'état d'avant)
   · ses variantes : le même dessin, une autre règle    · fait tourner le jeton, tour de boucle après tour de boucle
   · la série de valeurs : t, v, horloge                · dessine le chronogramme : la courbe, les seuils, les bandes,
   · le chronogramme : axes, seuils, bandes, voies        une voie d'état par règle, le compte des basculements
                                                        · écrit la ligne de console de chaque tour
   Le rendu est une fonction du temps : instant(t) dessine la course au temps t, finir() son image finale. Rien ne
   tourne seul : la page (le lecteur pas à pas) appelle instant() à chaque image, finir() sous « mouvement réduit ».
   Les couleurs sont des classes (moteur.css, puis la feuille de la page). Aucun réseau, aucune bibliothèque. */
(function(){
  "use strict";
  if (window.MoteurAlgorigramme) return;
  var NS = "http://www.w3.org/2000/svg", numero = 0;

  function el(nom, attrs, parent, texte){
    var e = document.createElementNS(NS, nom);
    if (attrs) for (var k in attrs) if (attrs[k] !== undefined && attrs[k] !== null) e.setAttribute(k, attrs[k]);
    if (texte !== undefined) e.textContent = texte;
    if (parent) parent.appendChild(e);
    return e;
  }
  function r1(v){ return Math.round(v * 10) / 10; }
  function borne(x){ return x < 0 ? 0 : x > 1 ? 1 : x; }
  function doux(x){ x = borne(x); return x * x * (3 - 2 * x); }
  function longueur(p){ var L = 0; for (var i = 1; i < p.length; i++) L += Math.hypot(p[i][0] - p[i-1][0], p[i][1] - p[i-1][1]); return L; }
  function pointA(p, d){
    for (var i = 1; i < p.length; i++) {
      var s = Math.hypot(p[i][0] - p[i-1][0], p[i][1] - p[i-1][1]);
      if (d <= s || i === p.length - 1) { var k = s ? borne(d / s) : 1; return [p[i-1][0] + (p[i][0] - p[i-1][0]) * k, p[i-1][1] + (p[i][1] - p[i-1][1]) * k]; }
      d -= s;
    }
    return p[p.length - 1];
  }
  function classe(e, nom, oui){ if (e && e.classList.contains(nom) !== !!oui) e.classList.toggle(nom, !!oui); }

  function MoteurAlgorigramme(o){
    var A = o.algo, C = o.chrono, id = "ma" + (++numero), VAR = o.variable || "H";
    var avecVar = new RegExp("(^|[^0-9A-Za-zÀ-ÿ_])(" + VAR + ")(?![0-9A-Za-zÀ-ÿ_])");
    A.classList.add("ma-algo"); C.classList.add("ma-chrono");

    // ── Les pointes de flèches : une par sorte (la couleur vient de la feuille de style) ──
    function pointes(svg){
      var defs = el("defs", null, svg);
      ["", "oui", "non", "boucle"].forEach(function(s){
        var m = el("marker", {id: id + "-p-" + (s || "f"), viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 11, markerHeight: 11,
                              orient: "auto", markerUnits: "userSpaceOnUse"}, defs);
        el("path", {d: "M0 0 L10 5 L0 10 z", "class": "ma-pointe" + (s ? " ma-pointe-" + s : "")}, m);
      });
    }
    pointes(A);

    // ── Les variantes de l'algorigramme : chacune son dessin, sa règle ──
    var variantes = {};
    Object.keys(o.variantes).forEach(function(nom){
      var D = o.variantes[nom], g = el("g", {"class": "ma-variante", "data-variante": nom}, A);
      var gF = el("g", {"class": "ma-fleches"}, g), gB = el("g", {"class": "ma-blocs"}, g);
      var V = {nom: nom, decl: D, g: g, blocs: {}, fleches: []};
      D.fleches.forEach(function(f){
        var sorte = f.sortie || (f.boucle ? "boucle" : "");
        var p = el("path", {d: "M" + f.points.map(function(q){ return q[0] + " " + q[1]; }).join(" L"), fill: "none",
                            "class": "ma-fleche" + (sorte ? " ma-" + sorte : ""), "marker-end": "url(#" + id + "-p-" + (sorte || "f") + ")"}, gF);
        var et = f.etiquette ? el("text", {x: f.etiquette.x, y: f.etiquette.y, "text-anchor": f.etiquette.ancre || "middle",
                                           "font-size": f.etiquette.taille || 13, "class": "ma-etiquette" + (sorte ? " ma-" + sorte : "")}, gF, f.etiquette.texte) : null;
        V.fleches.push({decl: f, de: f.de, a: f.a, sortie: f.sortie || null, boucle: !!f.boucle, points: f.points,
                        longueur: longueur(f.points), el: p, etiquette: et});
      });
      Object.keys(D.blocs).forEach(function(bid){
        var b = D.blocs[bid], gb = el("g", {"class": "ma-bloc ma-" + b.forme + (b.classe ? " " + b.classe : ""), "data-bloc": bid}, gB);
        var cx, cy;
        if (b.forme === "decision") {
          cx = b.cx; cy = b.cy;
          el("path", {d: "M" + cx + " " + (cy - b.dh) + " L" + (cx + b.dl) + " " + cy + " L" + cx + " " + (cy + b.dh) + " L" + (cx - b.dl) + " " + cy + " Z", "class": "ma-forme"}, gb);
        } else {
          cx = b.x + b.l / 2; cy = b.y + b.h / 2;
          el("rect", {x: b.x, y: b.y, width: b.l, height: b.h, rx: b.forme === "terminal" ? b.h / 2 : 6, "class": "ma-forme"}, gb);
        }
        var fs = b.taille || 14, lh = fs * 1.22, n = b.texte.length, y0 = cy - (n - 1) * lh / 2 + fs * 0.35;
        var textes = b.texte.map(function(t, i){
          return el("text", {x: cx, y: r1(y0 + i * lh), "text-anchor": "middle", "font-size": fs, "class": "ma-texte"}, gb, t);
        });
        V.blocs[bid] = {id: bid, decl: b, g: gb, textes: textes, valeur: null};
      });
      variantes[nom] = V;
    });

    // Dans un losange, la variable laisse place à sa valeur le temps de la question : « H < 40 ? » devient « 39 < 40 ? ».
    function poserValeur(B, v){
      if (B.valeur === v) return;
      B.valeur = v;
      B.textes.forEach(function(t, i){
        var brut = B.decl.texte[i], m = v === null ? null : avecVar.exec(brut);
        while (t.firstChild) t.removeChild(t.firstChild);
        if (!m) { t.textContent = brut; return; }
        var debut = m.index + m[1].length;
        t.appendChild(document.createTextNode(brut.slice(0, debut)));
        el("tspan", {"class": "ma-valeur"}, t, String(v));
        t.appendChild(document.createTextNode(brut.slice(debut + VAR.length)));
      });
    }

    // ── Le jeton (un rond qui porte la valeur), la console ──
    var RJ = o.rayonJeton || 12, MARGE = RJ + 1;           // le jeton s'arrête à un rayon d'un bloc : il ne le chevauche pas
    var jeton = el("g", {"class": "ma-jeton", opacity: 0}, A);
    el("circle", {r: RJ}, jeton);
    var jTexte = el("text", {x: 0, y: r1(RJ * 0.38), "text-anchor": "middle", "font-size": o.tailleJeton || 13}, jeton, "");
    function poserJeton(x, y, op, texte){
      if (texte !== undefined && jTexte.textContent !== texte) jTexte.textContent = texte;
      jeton.setAttribute("transform", "translate(" + r1(x) + " " + r1(y) + ")");
      jeton.setAttribute("opacity", r1(op * 100) / 100);
    }
    function surFleche(F, x){                             // x de 0 à 1 : du départ à l'arrivée, un rayon de chaque bout
      var m = Math.min(MARGE, F.longueur / 2);
      return pointA(F.points, m + (F.longueur - 2 * m) * x);
    }
    var cons = null;
    if (o.console) {
      var K = o.console, gc = el("g", {"class": "ma-console"}, A);
      if (K.titre) el("text", {x: K.x, y: K.y - 7, "font-size": 12, "class": "ma-console-titre"}, gc, K.titre);
      el("rect", {x: K.x, y: K.y, width: K.l, height: K.h, rx: 6}, gc);
      cons = el("text", {x: K.x + 9, y: r1(K.y + K.h / 2 + 4.4), "font-size": K.taille || 12.5, "class": "ma-console-ligne"}, gc, K.vide || "");
    }

    // ── Le chronogramme ──
    var CH = o.chronogramme, Z = CH.cadre, T = CH.t, VV = CH.v, S = o.serie, FS = CH.taille || 12;
    function X(t){ return Z.x + (t - T.min) / (T.max - T.min) * Z.l; }
    function Y(v){ return Z.y + (VV.max - v) / (VV.max - VV.min) * Z.h; }
    var pas = S.length > 1 ? S[1].t - S[0].t : 1;
    var gFond = el("g", {"class": "ma-fond"}, C);
    (CH.bandes || []).forEach(function(b){
      var g = el("g", {"class": "ma-bande" + (b.classe ? " " + b.classe : ""), "data-de": b.de, "data-a": b.a}, gFond);
      el("rect", {x: Z.x, y: r1(Y(b.haut)), width: Z.l, height: r1(Y(b.bas) - Y(b.haut))}, g);
      if (b.etiquette) el("text", {x: Z.x + 7, y: r1(Y(b.haut) + 5 + FS), "font-size": FS}, g, b.etiquette);
    });
    (CH.seuils || []).forEach(function(s){
      el("line", {x1: Z.x, y1: r1(Y(s.v)), x2: Z.x + Z.l, y2: r1(Y(s.v)), "class": "ma-seuil" + (s.classe ? " " + s.classe : ""), "data-de": s.de, "data-a": s.a}, gFond);
    });
    el("line", {x1: Z.x, y1: Z.y - 6, x2: Z.x, y2: Z.y + Z.h, "class": "ma-axe"}, gFond);
    el("line", {x1: Z.x, y1: Z.y + Z.h, x2: Z.x + Z.l, y2: Z.y + Z.h, "class": "ma-axe"}, gFond);
    if (VV.titre) el("text", {x: VV.tx !== undefined ? VV.tx : 6, y: Z.y - 12, "font-size": FS + 1, "class": "ma-titre-valeur"}, gFond, VV.titre);
    (VV.graduations || []).forEach(function(g){
      var v = typeof g === "number" ? g : g.v;
      el("line", {x1: Z.x - 4, y1: r1(Y(v)), x2: Z.x, y2: r1(Y(v)), "class": "ma-axe"}, gFond);
      el("text", {x: Z.x - 6, y: r1(Y(v) + FS * 0.36), "text-anchor": "end", "font-size": FS,
                  "class": "ma-graduation" + (g.classe ? " " + g.classe : "")}, gFond, String(v));
    });
    (T.graduations || []).forEach(function(t){
      el("line", {x1: r1(X(t)), y1: Z.y + Z.h, x2: r1(X(t)), y2: Z.y + Z.h + 4, "class": "ma-axe"}, gFond);
      el("text", {x: r1(X(t)), y: T.y, "text-anchor": "middle", "font-size": FS, "class": "ma-graduation"}, gFond, String(t));
    });
    if (T.titre) el("text", {x: Z.x + Z.l, y: T.y + FS + 6, "text-anchor": "end", "font-size": FS, "class": "ma-graduation"}, gFond, T.titre);

    var gCourbe = el("g", {"class": "ma-courbe-g"}, C);
    var courbe = el("polyline", {points: "", "class": "ma-courbe"}, gCourbe);
    var points = S.map(function(p){ return el("circle", {cx: r1(X(p.t)), cy: r1(Y(p.v)), r: 2.8, "class": "ma-point", display: "none"}, gCourbe); });
    // (un élément caché par display:none garde, pour les mesures, sa propre valeur de display : on cache aussi par visibility)
    var anneau = el("circle", {r: 6.5, "class": "ma-mesure", display: "none"}, gCourbe);

    // ── Les voies d'état : la règle de chaque variante, appliquée à toute la série, une fois pour toutes ──
    var voies = {};
    function parcours(V, v, etat){
      var b = V.decl.depart, chemin = [], e = etat, garde = 0;
      while (garde++ < 40) {
        var B = V.decl.blocs[b], sortie = null;
        if (chemin.length && B.etat !== undefined) e = B.etat;
        if (B.test) sortie = B.test(v, e) ? "oui" : "non";
        var f = null;
        for (var i = 0; i < V.fleches.length; i++) if (V.fleches[i].de === b && (!B.test || V.fleches[i].sortie === sortie)) { f = V.fleches[i]; break; }
        chemin.push({bloc: b, sortie: sortie, fleche: f});
        if (!f || f.a === V.decl.depart) break;
        b = f.a;
      }
      return {chemin: chemin, etat: e};
    }
    (CH.voies || []).forEach(function(d){
      var V = variantes[d.variante], e = !!d.etat0, hist = [];
      S.forEach(function(p, i){
        var r = parcours(V, p.v, e);
        hist.push({i: i, t: p.t, v: p.v, avant: e, etat: r.etat, bascule: r.etat !== e, chemin: r.chemin,
                   ligne: o.ligne ? o.ligne(p, r.etat) : ""});
        e = r.etat;
      });
      var g = el("g", {"class": "ma-voie" + (d.classe ? " " + d.classe : ""), "data-voie": d.id, "data-de": d.de, "data-a": d.a}, C);
      var yOn = d.y, yOff = d.y + d.h, etiq = CH.etats || ["OFF", "ON"];
      el("line", {x1: Z.x, y1: yOn, x2: Z.x + Z.l, y2: yOn, "class": "ma-guide ma-guide-on"}, g);
      el("line", {x1: Z.x, y1: yOff, x2: Z.x + Z.l, y2: yOff, "class": "ma-guide"}, g);
      el("text", {x: Z.x - 6, y: r1(yOn + FS * 0.36), "text-anchor": "end", "font-size": FS, "class": "ma-graduation"}, g, etiq[1]);
      el("text", {x: Z.x - 6, y: r1(yOff + FS * 0.36), "text-anchor": "end", "font-size": FS, "class": "ma-graduation"}, g, etiq[0]);
      var trace = el("path", {d: "", "class": "ma-etat"}, g);
      el("text", {x: Z.x, y: yOff + FS + 8, "font-size": FS + 0.5, "class": "ma-titre-voie"}, g, d.titre);
      var compte = el("text", {x: Z.x + Z.l, y: yOff + FS + 8, "text-anchor": "end", "font-size": FS + 0.5, "class": "ma-compte"}, g, "");
      var gm = el("g", {"class": "ma-marques", display: "none"}, C);
      var marques = [];
      hist.forEach(function(h){
        if (!h.bascule) return;
        var m = el("g", {"class": "ma-marque", display: "none", visibility: "hidden"}, gm);
        el("circle", {cx: r1(X(h.t)), cy: r1(Y(h.v)), r: 6.5}, m);
        el("line", {x1: r1(X(h.t)), y1: r1(Y(h.v) + 8), x2: r1(X(h.t)), y2: yOn - 5}, m);
        marques.push({g: m, i: h.i});
      });
      voies[d.id] = {decl: d, V: V, hist: hist, fin: -1, curseur: null, trace: trace, compte: compte, yOn: yOn, yOff: yOff,
                     gm: gm, marques: marques, debut: d.debut || 0};
    });

    function dessinerVoie(W){
      var h = W.hist, d = "", n = 0;
      if (W.fin >= W.debut) {
        var y = function(e){ return e ? W.yOn : W.yOff; };
        d = "M" + r1(X(h[W.debut].t)) + " " + y(h[W.debut].etat);
        for (var k = W.debut + 1; k <= W.fin; k++) {
          d += " H" + r1(X(h[k].t));
          if (h[k].etat !== h[k - 1].etat) d += " V" + y(h[k].etat);
        }
        d += " H" + r1(X(W.curseur !== null ? W.curseur : h[W.fin].t + pas));
        for (k = W.debut; k <= W.fin; k++) if (h[k].bascule) n++;
      }
      if (W.trace.getAttribute("d") !== d) W.trace.setAttribute("d", d);
      var txt = n + " basculement" + (n > 1 ? "s" : "");
      if (W.compte.textContent !== txt) W.compte.textContent = txt;
    }
    var hFixe = -1;
    function dessinerCourbe(fin){
      var pts = [];
      S.forEach(function(p, i){
        var vu = i <= fin;
        if ((points[i].getAttribute("display") === "none") === vu) points[i].setAttribute("display", vu ? "inline" : "none");
        if (vu) pts.push(r1(X(p.t)) + "," + r1(Y(p.v)));
      });
      var s = pts.join(" ");
      if (courbe.getAttribute("points") !== s) courbe.setAttribute("points", s);
    }
    function hFin(){ var m = hFixe; Object.keys(voies).forEach(function(k){ if (voies[k].fin > m) m = voies[k].fin; }); return m; }

    // ── La course : une suite de tours de boucle, chacun découpé en pas (mesure, trajets, questions, actions) ──
    var course = null, actifs = [], valeurs = [];
    function preparer(vid, de, a, opt){
      opt = opt || {};
      var W = voies[vid], V = W.V, tours = [], t = 0, depart = V.decl.depart;
      for (var i = de; i <= a; i++) {
        var h = W.hist[i], tour = {i: i, debut: t, pas: [], effet: null};
        var f0 = h.chemin[0].fleche;
        tour.pas.push({type: "mesure", bloc: depart, fleche: f0, de: t, a: t += 0.34});
        for (var j = 0; j < h.chemin.length; j++) {
          var F = h.chemin[j].fleche;
          if (!F) break;
          tour.pas.push({type: "trajet", fleche: F, de: t, a: t += Math.max(0.16, F.longueur / (F.boucle ? 900 : 340))});
          if (F.a === depart) break;
          var B = V.decl.blocs[F.a], suite = h.chemin[j + 1];
          if (B.test) {
            tour.pas.push({type: "question", bloc: F.a, sortie: suite.sortie, fleche: suite.fleche, de: t, a: t += 0.7});
          } else {
            if (B.etat !== undefined && tour.effet === null) tour.effet = t;
            tour.pas.push({type: "bloc", bloc: F.a, de: t, a: t += B.etat !== undefined ? 0.42 : 0.26});
          }
        }
        if (tour.effet === null) {                      // aucune action : l'état ne change pas ; le tour compte à la fin de la question
          for (var q = tour.pas.length - 1; q >= 0; q--) if (tour.pas[q].type === "question") { tour.effet = tour.pas[q].a; break; }
          if (tour.effet === null) tour.effet = t;
        }
        tour.fin = t;
        tours.push(tour);
      }
      // opt.premier : le premier tour dure « premier » fois plus que les autres (on lit, puis on voit le rythme)
      var P = opt.premier || 1, l0 = tours.length ? tours[0].fin : 0, naturel = t + (P - 1) * l0;
      var k = opt.duree ? naturel / opt.duree : (opt.vitesse || 1), delai = opt.delai || 0;
      function cal(x){ return delai + (x <= l0 ? x * P : l0 * P + (x - l0)) / k; }
      tours.forEach(function(tr){
        tr.debut = cal(tr.debut); tr.effet = cal(tr.effet); tr.fin = cal(tr.fin);
        tr.pas.forEach(function(p){ p.de = cal(p.de); p.a = cal(p.a); });
      });
      return {voie: vid, de: de, a: a, tours: tours, duree: delai + naturel / k};
    }

    function marquer(liste){                              // le bloc ou la flèche où est le jeton : en valeur
      actifs.forEach(function(e){ if (liste.indexOf(e) < 0) e.classList.remove("ma-actif"); });
      liste.forEach(function(e){ if (e) e.classList.add("ma-actif"); });
      actifs = liste.filter(Boolean);
    }
    function questions(liste){                            // les losanges qui montrent une valeur
      valeurs.forEach(function(B){ if (liste.indexOf(B) < 0) poserValeur(B, null); });
      valeurs = liste;
    }

    function instant(t){
      if (!course) return;
      var c = course, W = voies[c.voie], V = W.V, fin = c.de - 1, tour = null, vu = c.de - 1;
      if (t >= c.duree) t = c.duree;
      c.tours.forEach(function(tr){
        if (t >= tr.effet) fin = tr.i;
        if (t >= tr.debut) vu = tr.i;
        if (t >= tr.debut && t < tr.fin) tour = tr;
      });
      // la voie : jusqu'au tour fait ; après l'action, le temps avance jusqu'à la mesure suivante
      W.fin = fin;
      if (fin >= c.de) {
        var tr = c.tours[fin - c.de], t0 = W.hist[fin].t;
        W.curseur = t0 + pas * borne((t - tr.effet) / Math.max(0.001, tr.fin - tr.effet));
      } else W.curseur = null;
      dessinerVoie(W);
      dessinerCourbe(Math.max(hFin(), vu));
      if (fin >= 0 && cons && W.hist[fin].ligne && cons.textContent !== W.hist[fin].ligne) cons.textContent = W.hist[fin].ligne;
      // le jeton
      classe(A, "ma-en-course", t < c.duree);
      if (!tour) { poserJeton(0, 0, 0); marquer([]); questions([]); anneau.setAttribute("display", "none"); return; }
      var h = W.hist[tour.i], p = null;
      for (var i = 0; i < tour.pas.length; i++) if (t >= tour.pas[i].de && t < tour.pas[i].a) { p = tour.pas[i]; break; }
      if (!p) p = tour.pas[tour.pas.length - 1];
      var x = (t - p.de) / Math.max(0.001, p.a - p.de), lab = o.jeton ? o.jeton(h.v) : String(h.v);
      anneau.setAttribute("cx", r1(X(h.t))); anneau.setAttribute("cy", r1(Y(h.v))); anneau.setAttribute("display", "inline");
      var B = p.bloc ? V.blocs[p.bloc] : null;
      if (p.type === "mesure") {
        var q0 = surFleche(p.fleche, 0);
        poserJeton(q0[0], q0[1], doux(x / 0.7), lab);
        marquer([B.g]); questions([]);
      } else if (p.type === "trajet") {
        var q = surFleche(p.fleche, doux(x));
        poserJeton(q[0], q[1], 1, lab);
        marquer([p.fleche.el]); questions([]);
      } else if (p.type === "question") {
        poserJeton(0, 0, 0);
        poserValeur(B, h.v); questions([B]);
        marquer(x > 0.55 ? [B.g, p.fleche && p.fleche.etiquette, p.fleche && p.fleche.el] : [B.g]);
      } else {
        poserJeton(0, 0, 0);
        marquer([B.g]); questions([]);
      }
    }

    var M = {
      variante: function(nom){
        Object.keys(variantes).forEach(function(k){ classe(variantes[k].g, "ma-montre", k === nom); });
      },
      // la voie dessinée jusqu'au tour « fin » (−1 : vide), sans course
      voie: function(vid, fin){
        var W = voies[vid]; W.fin = fin; W.curseur = null; dessinerVoie(W); dessinerCourbe(hFin());
      },
      courbe: function(fin){ hFixe = fin; dessinerCourbe(hFin()); },
      // une course : les tours de..a de la voie vid ; opt.duree (s) ou opt.vitesse, opt.delai (s), opt.premier. Rend sa durée.
      course: function(vid, de, a, opt){
        M.arreter();
        course = preparer(vid, de, a, opt);
        var W = voies[vid]; W.fin = de - 1; W.curseur = null; dessinerVoie(W);
        instant(0);
        return course.duree;
      },
      instant: instant,
      finir: function(){ if (course) { instant(Infinity); classe(A, "ma-en-course", false); } },
      arreter: function(){
        course = null; poserJeton(0, 0, 0); marquer([]); questions([]); classe(A, "ma-en-course", false);
        anneau.setAttribute("display", "none");
      },
      ligne: function(vid, i){ if (cons) cons.textContent = i >= 0 ? voies[vid].hist[i].ligne : (o.console.vide || ""); },
      // les basculements de la voie : marqués sur la courbe (n premiers ; −1 : aucun groupe)
      marques: function(vid, n){
        var W = voies[vid];
        W.gm.setAttribute("display", n < 0 ? "none" : "inline");
        var dans = W.marques.filter(function(m){ return m.i <= W.fin; });          // seulement les tours dessinés
        W.marques.forEach(function(m){
          var vu = dans.indexOf(m) >= 0 && dans.indexOf(m) < n;
          if ((m.g.getAttribute("display") === "none") === vu) { m.g.setAttribute("display", vu ? "inline" : "none"); m.g.setAttribute("visibility", vu ? "visible" : "hidden"); }
        });
        return dans.length;
      },
      // des blocs en valeur, les autres en retrait (null : aucun)
      focus: function(ids){
        classe(A, "ma-focus", !!(ids && ids.length));
        Object.keys(variantes).forEach(function(k){
          Object.keys(variantes[k].blocs).forEach(function(b){ classe(variantes[k].blocs[b].g, "ma-cible", !!ids && ids.indexOf(b) >= 0); });
        });
      },
      bascules: function(vid, fin){ var W = voies[vid], n = 0; for (var k = W.debut; k <= fin; k++) if (W.hist[k].bascule) n++; return n; },
      historique: function(vid){ return voies[vid].hist; },
      duree: function(){ return course ? course.duree : 0; }
    };
    return M;
  }
  window.MoteurAlgorigramme = MoteurAlgorigramme;
})();
