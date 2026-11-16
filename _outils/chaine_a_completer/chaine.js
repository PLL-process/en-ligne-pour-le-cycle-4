/* Chaîne à compléter — l'élève pose les étiquettes DANS le schéma des chaînes d'énergie et d'information.
   Source unique : _outils/chaine_a_completer/ (chaine.js, chaine.css), posée dans la page par poser.py, entre deux
   marqueurs. Ne pas la modifier dans une page.

   Pourquoi (demande de Pascal du 15/11/2026) : l'élève répondait à beaucoup de questions sur les chaînes sans avoir
   le schéma sous les yeux ; il n'en gardait pas l'image, et peinait ensuite à la construire. Ici, le schéma EST la
   question : les cases sont dans le dessin, le dessin reste sous les yeux, et il se bâtit d'une activité à l'autre
   (ce qui est trouvé reste écrit, ce qui viendra plus tard se voit en pointillés).

   LA PAGE DÉCLARE
     1. Le dessin, une fois par page (le même dessin sert à toutes les étapes) :
        window.CAC_DESSINS = {lampadaire: {large: {vue: [x, y, l, h], ...}, etroit: {vue: [...], max: 520, ...},
                                           elements: [ ... ]}};
        Éléments (chacun : id, type, groupe, puis sa géométrie dans `large` et dans `etroit`) :
          titre  {texte, couleur}                       géométrie {x, y}            (le coin haut gauche du texte)
          bloc   {fonction, composant, stock?, couleur} géométrie {x, y, l, tf?}    (le composant SOUS le bloc ; tf : taille de la fonction)
          fleche {nature, texte, double?}               géométrie {points, ex, ey, ancre, lt?}
                 nature : energie, information, ordre (pointillés), stock, lien (un branchement, sans flux) ; ancre : la place de l'étiquette par
                 rapport au point (ex, ey) — bas (au-dessus du point), haut, gauche, droite ; lt : largeur de la case
          texte  {texte, gras?, couleur?}               géométrie {x, y, ancre?, l?}      (l : sa largeur)
        Une géométrie peut redonner texte, composant ou stock pour couper les lignes autrement (\n), sans changer
        les mots.
     2. Chaque étape, à la place des questions :
        <div class="cac" data-cac='{"dessin": "lampadaire",
                                     "cases": {"convertir-panneau.fonction": "e2_f1", ...},
                                     "vides": ["g:information"], "reutilisables": true}'>
          <div class="cac-questions"> … les groupes de boutons radio (fieldset.qcm-groupe) … </div>
        </div>
        cases : la partie d'un élément (fonction, composant, stock, texte) → l'id du groupe de boutons radio qui garde
                la réponse. Poser une étiquette coche le bouton de cette valeur : la sauvegarde, la vérification,
                le mode mission et l'impression de la page lisent toujours ces groupes.
        vides : ce qui viendra plus tard (en pointillés, sans texte). Motifs : « id.partie », « id » (tout
                l'élément), « *.partie », « g:groupe » (tout un groupe : ses blocs et ses flèches en pointillés),
                « g:groupe.partie ».
        acquis : {"id.partie": "id du groupe"} — ce que l'élève a trouvé à une étape d'avant reste écrit dans le
                dessin (sa réponse, en clair ; en pointillés tant qu'il n'a rien posé) : le schéma se bâtit.
        titres : {id: "autre texte"} pour un titre ou un texte à cette étape (« … à construire en séance 3 »).
        vue    : {etroit: [x, y, l, h]} — recadrer le dessin à cette étape (au téléphone, la seule chaîne travaillée).
        reutilisables : une étiquette peut servir plusieurs fois (CONVERTIR, énergie électrique).
     Sans JavaScript, les questions restent visibles : rien ne se perd.

   LE MODE MISSION voit les groupes de la .cac comme un seul écran (une partie) et les vérifie comme d'habitude :
   les justes restent, les fausses (classe ms-origine) retournent dans la réserve. Le dessin suit leurs marques.

   GESTES : toucher une étiquette, puis toucher sa case ; ou la faire glisser ; au clavier, Entrée sur l'étiquette
   mène à la première case vide. Toucher une case pleine la vide (sauf une case déjà juste). */
(function(){
  "use strict";
  if (window.ChaineACompleter) return;
  var D = document, NS = "http://www.w3.org/2000/svg";
  var PARTIES = {bloc: ["fonction", "composant", "stock"], fleche: ["texte"], titre: ["texte"], texte: ["texte"]};
  var DEFAUT = {
    large:  {seuil: 760, h: 70, rx: 12, ecart: 10, lt: 170, lc: 20,
             tailles: {titre: 22, fonction: 24, composant: 21, stock: 19, fleche: 20, texte: 21}},
    etroit: {h: 44, rx: 8, ecart: 6, lt: 104, lc: 12, max: 520,
             tailles: {titre: 14, fonction: 16, composant: 13.5, stock: 12.5, fleche: 13, texte: 14}}
  };
  function $$(s, r){ return [].slice.call((r || D).querySelectorAll(s)); }
  function cree(nom, attrs, parent){ var e = D.createElementNS(NS, nom); for (var k in attrs) if (attrs[k] != null) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; }
  function el(t, c, h){ var e = D.createElement(t); if (c) e.className = c; if (h != null) e.innerHTML = h; return e; }
  function esc(t){ return String(t).replace(/[&<>"]/g, function(c){ return {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]; }); }
  function lignes(t){ return esc(t).replace(/\n/g, "<br>"); }
  function net(t){ return String(t || "").replace(/\s+/g, " ").trim(); }
  function fusion(a, b){ var r = {}, k; for (k in a) r[k] = a[k]; for (k in (b || {})) r[k] = b[k]; return r; }
  function lireV(f){ var c = f.querySelector("input[type=radio]:checked"); return c ? c.value : ""; }
  function valeurs(f){ return $$("input[type=radio]", f).map(function(r){ return r.value; }); }
  /* le texte que l'élève lit : celui du libellé de la proposition (il peut nommer une unité en toutes lettres,
     n°312, quand la valeur garde le texte que la vérification compare) */
  function libelle(f, v){ var r = $$("input[type=radio]", f).filter(function(x){ return x.value === v; })[0], l = r && f.querySelector('label[for="' + r.id + '"]'); return l ? net(l.textContent) : v; }
  function legende(f){ var l = f.querySelector("legend"); return net(l ? l.textContent : f.getAttribute("aria-label") || ""); }
  function ecrire(f, v){
    var r = null;
    $$("input[type=radio]", f).forEach(function(x){ x.checked = (v != null && x.value === v); if (x.checked) r = x; });
    var cible = r || f;
    cible.dispatchEvent(new Event("input", {bubbles: true}));
    cible.dispatchEvent(new Event("change", {bubbles: true}));
  }
  function etat(f){ return f.classList.contains("ms-juste") ? "juste" : f.classList.contains("ms-faux") ? "faux" : ""; }

  var choix = null, glisse = null, vientDeGlisser = false;          // l'étiquette choisie : {cac, v}

  function Chaine(racine){
    var conf = {};
    try { conf = JSON.parse(racine.getAttribute("data-cac") || "{}"); } catch (e) { console.warn("chaîne à compléter : data-cac illisible", e); return; }
    var dessin = (window.CAC_DESSINS || {})[conf.dessin];
    if (!dessin) { console.warn("chaîne à compléter : dessin inconnu", conf.dessin); return; }
    /* LE CORRIGÉ (règle d'or n°336, 16/11/2026) : `"corrige": true` dessine la même étape sans case — chaque partie
       porte le texte du dessin, c'est-à-dire la bonne réponse ; ce qui viendra plus tard reste en pointillés. Rien à
       toucher, rien à poser : c'est l'image de la correction. Posé de lui-même dans la correction de l'activité. */
    var corrige = !!conf.corrige;
    var cases = corrige ? {} : (conf.cases || {}), vides = conf.vides || [], titres = conf.titres || {}, acquis = corrige ? {} : (conf.acquis || {});
    var champs = {}, ordre = [];                                       // « id.partie » → fieldset ; ordre de lecture
    Object.keys(cases).forEach(function(k){ var f = D.getElementById(cases[k]); if (f) { champs[k] = f; ordre.push(k); f.classList.add("ms-origine"); } else console.warn("chaîne à compléter : groupe absent", cases[k]); });
    if (!ordre.length && !corrige) return;
    var etiquettes = [], textes = {};
    ordre.forEach(function(k){ valeurs(champs[k]).forEach(function(v){ if (etiquettes.indexOf(v) < 0) { etiquettes.push(v); textes[v] = libelle(champs[k], v); } }); });
    function tx(v){ return textes[v] || v; }
    var reutil = !!conf.reutilisables;
    var dispo = "", k = 1, zone, svg, calque, reserve, msg, papier;

    racine.classList.add("cac-pret");
    zone = el("div", "cac-dessin"); zone.setAttribute("role", corrige ? "img" : "group");
    zone.setAttribute("aria-label", corrige ? "Le schéma complet, corrigé : chaque bloc porte sa fonction et son constituant, chaque flèche ce qu'elle transporte"
                                            : conf.nom || "Le schéma des chaînes, à compléter avec les étiquettes");
    msg = el("p", "cac-msg"); msg.setAttribute("aria-live", "polite");
    reserve = el("div", "cac-reserve");
    papier = el("p", "cac-papier pp-papier");
    var q = racine.querySelector(".cac-questions");
    if (corrige) { racine.appendChild(zone); msg.hidden = reserve.hidden = papier.hidden = true; }
    else { racine.insertBefore(zone, q); racine.insertBefore(msg, q); racine.insertBefore(reserve, q); racine.insertBefore(papier, q); }
    papier.innerHTML = "<b>Les étiquettes à écrire dans les cases" + (reutil ? " (une étiquette peut servir plusieurs fois)" : "") + "&nbsp;:</b> " + etiquettes.map(function(v){ return esc(tx(v)); }).join(" · ");

    function correspond(m, e, partie){
      if (m === e.id || m === e.id + "." + partie || m === "*." + partie) return true;
      if (m.indexOf("g:") === 0) { var g = m.slice(2).split("."); return g[0] === e.groupe && (!g[1] || g[1] === partie); }
      return false;
    }
    function attente(e){ return vides.some(function(m){ return m === "g:" + e.groupe || m === e.id; }); }
    function sort(e, partie){
      var cle = e.id + "." + partie;
      if (champs[cle]) return "case";
      if (acquis[cle]) return "acquis";
      return vides.some(function(m){ return correspond(m, e, partie); }) ? "vide" : "vu";
    }

    function rendre(){
      var w = racine.clientWidth; if (!w) return;
      var nd = w >= (dessin.seuil || DEFAUT.large.seuil) && dessin.large ? "large" : "etroit";
      var G = fusion(DEFAUT[nd], dessin[nd]); G.tailles = fusion(DEFAUT[nd].tailles, (dessin[nd] || {}).tailles);
      var V = (conf.vue && conf.vue[nd]) || G.vue, larg = nd === "etroit" ? Math.min(w, G.max) : w;
      k = larg / V[2]; dispo = nd;
      zone.className = "cac-dessin cac-" + nd;
      /* le dessin se règle sur sa largeur (unités de conteneur) : il garde ses proportions à l'écran comme sur le papier */
      zone.style.width = nd === "etroit" ? "min(100%, " + G.max + "px)" : "100%"; zone.style.aspectRatio = V[2] + " / " + V[3]; zone.style.height = "";
      zone.innerHTML = "";
      svg = cree("svg", {viewBox: V.join(" "), width: "100%", height: "100%", "aria-hidden": "true", focusable: "false", "class": "cac-traits"}, zone);
      var defs = cree("defs", {}, svg);
      ["energie", "information", "ordre", "stock", "lien", "attente"].forEach(function(n){
        var m = cree("marker", {id: "cac-m-" + n + "-" + uid, viewBox: "0 0 10 10", refX: 8, refY: 5, markerWidth: 6, markerHeight: 6, orient: "auto-start-reverse", "class": "cac-m cac-n-" + n}, defs);
        cree("path", {d: "M0,0 L10,5 L0,10 z"}, m);
      });
      calque = el("div", "cac-calque"); zone.appendChild(calque);
      function px(v){ return Math.round(v / V[2] * 100000) / 1000 + "%"; }          // une largeur, en part du dessin
      function py(v){ return Math.round(v / V[3] * 100000) / 1000 + "%"; }          // une hauteur
      function cq(v){ return Math.round(v / V[2] * 100000) / 1000 + "cqw"; }        // une taille qui suit la largeur du dessin
      function pos(n, x, y){ n.style.left = px(x - V[0]); n.style.top = py(y - V[1]); }
      function taille(n, t){ n.style.fontSize = "max(11px, " + cq(t) + ")"; }
      function texte(e, g, cle){ return g[cle] != null ? g[cle] : e[cle]; }
      function partie(e, g, p, boite, classe, t){
        var s = sort(e, p);
        if (attente(e) && s === "vu") s = "vide";
        if (s === "acquis") {
          var fa = D.getElementById(acquis[e.id + "." + p]), va = fa ? lireV(fa) : "";
          if (!va) s = "vide";
          else { boite.className = classe + " cac-acquis"; boite.textContent = libelle(fa, va); taille(boite, p === "fonction" ? t * .86 : t); return boite; }
        }
        if (s === "vu") { boite.className = classe; boite.innerHTML = lignes(titres[e.id] && p === "texte" ? titres[e.id] : texte(e, g, p)); taille(boite, t); return boite; }
        var c = s === "case" ? el("button", classe + " cac-case") : el("span", classe + " cac-trou");
        taille(c, t);
        if (s === "case") {
          var f = champs[e.id + "." + p], v = lireV(f), st = etat(f);
          c.type = "button"; c.setAttribute("data-cle", e.id + "." + p);
          if (v) c.classList.add("pleine"); if (st) c.classList.add(st);
          if (st === "juste") c.disabled = true;
          c.innerHTML = v ? '<span class="cac-v">' + esc(tx(v)) + "</span>" + (st === "juste" ? '<span class="cac-marque" aria-hidden="true">✓</span>' : st === "faux" ? '<span class="cac-marque" aria-hidden="true">✗</span>' : "")
                          : '<span class="cac-q" aria-hidden="true">?</span>';
          c.setAttribute("aria-label", legende(f) + " : " + (v ? tx(v) + (st === "juste" ? ", juste" : st === "faux" ? ", à revoir" : "") : "case vide"));
        } else c.setAttribute("aria-hidden", "true");
        return c;
      }
      dessin.elements.forEach(function(e){
        var g = e[nd]; if (!g) return;
        var att = attente(e), coul = att ? null : e.couleur;
        if (e.type === "fleche") {
          var nat = att ? "attente" : e.nature, d = "M" + g.points.map(function(p){ return p[0] + "," + p[1]; }).join(" L");
          var tr = cree("path", {d: d, "class": "cac-fleche cac-n-" + nat, "marker-end": "url(#cac-m-" + nat + "-" + uid + ")"}, svg);
          if (e.double) tr.setAttribute("marker-start", "url(#cac-m-" + nat + "-" + uid + ")");
          tr.style.strokeWidth = (nd === "large" ? 3.4 : 2.6) / Math.min(1, k * 1.6) + "px";
          /* les flux animés (demande de Pascal du 15/11/2026) : des perles claires avancent dans le sens de la flèche,
             dans les deux sens pour une double flèche ; un branchement (« lien ») ne porte aucun flux, il reste fixe */
          if (nat !== "lien") (e.double ? ["", " retour"] : [""]).forEach(function(sens){
            var fl = cree("path", {d: d, "class": "cac-flux" + sens, "aria-hidden": "true"}, svg);
            fl.style.strokeWidth = ((nd === "large" ? 3.4 : 2.6) + 3) / Math.min(1, k * 1.6) + "px";
          });
          var b = partie(e, g, "texte", el("div"), "cac-et cac-et-" + (g.ancre || "bas") + " cac-c-" + nat, G.tailles.fleche);
          if (/cac-(case|trou|acquis)/.test(b.className)) b.style.width = px(g.lt || G.lt);
          pos(b, g.ex, g.ey); calque.appendChild(b);
        } else if (e.type === "bloc") {
          var bl = el("div", "cac-bloc" + (att ? " attente" : ""));
          pos(bl, g.x, g.y); bl.style.width = px(g.l); bl.style.height = py(G.h); bl.style.borderRadius = cq(G.rx);
          /* la couleur d'une fonction (n°120) se montre quand la fonction est écrite ou trouvée juste : tant qu'elle
             est à trouver, le bloc reste neutre, sinon la couleur la soufflerait */
          var sf = sort(e, "fonction"), ff = champs[e.id + ".fonction"];
          if (coul && (sf === "vu" || (sf === "case" && etat(ff) === "juste"))) bl.style.setProperty("--cac-coul", coul);
          else if (!att) bl.classList.add("neutre");
          var fo = partie(e, g, "fonction", el("div"), "cac-fonction", g.tf || G.tailles.fonction); bl.appendChild(fo);
          calque.appendChild(bl);
          var sous = el("div", "cac-sous"); pos(sous, g.x - G.lc / 2, g.y + G.h + G.ecart); sous.style.width = px(g.l + G.lc);
          if (e.composant != null) sous.appendChild(partie(e, g, "composant", el("div"), "cac-composant", G.tailles.composant));
          if (e.stock != null) sous.appendChild(partie(e, g, "stock", el("div"), "cac-stock", G.tailles.stock));
          calque.appendChild(sous);
        } else {
          var tx = partie(e, g, "texte", el("div"), (e.type === "titre" ? "cac-titre" : "cac-texte cac-et-" + (g.ancre || "centre")) + (e.gras ? " gras" : "") + (att ? " attente" : ""),
                          e.type === "titre" ? G.tailles.titre : G.tailles.texte);
          if (coul) tx.style.color = coul;
          if (e.type === "titre") tx.style.maxWidth = px(V[0] + V[2] - g.x - 6);
          else tx.style.width = px(g.l || (nd === "large" ? 220 : 300));          // une largeur à lui : au bord du dessin, il ne se tasse pas
          pos(tx, g.x, g.y); calque.appendChild(tx);
        }
      });
      peindreReserve();
    }
    var uid = Math.random().toString(36).slice(2, 7);

    function peindreReserve(){
      if (corrige) return;
      var pris = ordre.map(function(c){ return lireV(champs[c]); });
      var finies = ordre.every(function(c){ return etat(champs[c]) === "juste"; });
      reserve.hidden = finies;
      if (finies) return;
      var labs = etiquettes.map(function(v){
        if (!reutil && pris.indexOf(v) >= 0) return "";
        var on = !!(choix && choix.cac === api && choix.v === v);
        return '<button type="button" class="cac-lab' + (on ? " choisie" : "") + '" data-v="' + esc(v) + '" aria-pressed="' + on + '">' + esc(tx(v)) + "</button>";
      }).join("");
      var plein = pris.every(Boolean);
      var trop = reutil ? 0 : etiquettes.length - ordre.length;
      reserve.innerHTML = '<p class="cac-reserve-t">' + (plein ? "Toutes les cases sont remplies : vérifie." : "Étiquettes" + (reutil ? " — chacune peut servir plusieurs fois" : trop > 0 ? " — attention, " + trop + " en trop" : "")) + "</p>"
        + '<div class="cac-reserve-l">' + (labs || '<span class="cac-geste">Toutes les étiquettes sont posées.</span>') + "</div>";
    }
    function dire(t){ msg.textContent = t || ""; }
    function premiereVide(){ var c = ordre.filter(function(x){ return !lireV(champs[x]); })[0]; return c ? zone.querySelector('[data-cle="' + c + '"]') : null; }
    function montrerCase(c){ if (c && c.scrollIntoView) c.scrollIntoView({block: "nearest", inline: "nearest"}); }
    function poser(cle, v){
      var f = champs[cle]; if (!f || etat(f) === "juste") return;
      if (!reutil && v) ordre.forEach(function(o){ if (o !== cle && lireV(champs[o]) === v && etat(champs[o]) !== "juste") { ecrire(champs[o], null); champs[o].classList.remove("ms-faux"); } });
      f.classList.remove("ms-faux");
      ecrire(f, v);
      dire("");
    }
    var api = {racine: racine, rendre: rendre, poser: poser, champs: champs, ordre: ordre, etiquettes: etiquettes, peindre: peindreReserve, dispo: function(){ return dispo; }};

    racine.addEventListener("click", function(ev){
      if (vientDeGlisser) return;
      var lab = ev.target.closest(".cac-lab");
      if (lab) {
        var v = lab.getAttribute("data-v");
        choix = (choix && choix.cac === api && choix.v === v) ? null : {cac: api, v: v};
        peindreReserve();
        if (choix) {
          dire("« " + tx(v) + " » est prise : touche sa case dans le schéma.");
          if (ev.detail === 0) { var c0 = premiereVide(); if (c0) { c0.focus({preventScroll: true}); montrerCase(c0); } }
          else { var b = reserve.querySelector('.cac-lab[data-v="' + CSS.escape(v) + '"]'); if (b) b.focus({preventScroll: true}); }
        } else dire("");
        return;
      }
      var c = ev.target.closest(".cac-case");
      if (c && !c.disabled) {
        var cle = c.getAttribute("data-cle");
        if (choix && choix.cac === api) { poser(cle, choix.v); choix = null; rendre(); var s = premiereVide(); if (s && ev.detail === 0) s.focus({preventScroll: true}); montrerCase(s); }
        else if (lireV(champs[cle])) { poser(cle, null); rendre(); }
        else dire("Choisis d'abord une étiquette, en bas, puis touche cette case.");
      }
    });
    racine.addEventListener("keydown", function(ev){ if (ev.key === "Escape" && choix) { choix = null; peindreReserve(); dire(""); } });
    // la vérification (mode mission) marque les groupes ; une étiquette fausse est rendue : le dessin suit
    var obs = new MutationObserver(function(){ rendre(); });
    ordre.forEach(function(c){ obs.observe(champs[c], {attributes: true, attributeFilter: ["class"]}); });
    racine.addEventListener("change", function(ev){ if (ev.target.closest(".cac-questions")) rendre(); });
    if (window.ResizeObserver) new ResizeObserver(function(){ if (racine.clientWidth && racine.clientWidth !== api._w) { api._w = racine.clientWidth; rendre(); } }).observe(racine);
    rendre();
    racine._cac = api;
    return api;
  }

  /* ── Glisser une étiquette (ou une case pleine) vers une case ── */
  function caseSous(ev){ var x = D.elementFromPoint(ev.clientX, ev.clientY); return x && x.closest(".cac-case:not(:disabled)"); }
  D.addEventListener("pointerdown", function(ev){
    var src = ev.target.closest(".cac-lab, .cac-case.pleine"); if (!src || src.disabled) return;
    if (ev.pointerType === "touch" && src.classList.contains("cac-case")) return;      // au doigt, une case pleine se vide en la touchant
    var r = src.closest(".cac"); if (!r || !r._cac) return;
    var de = src.getAttribute("data-cle");
    glisse = {id: ev.pointerId, x: ev.clientX, y: ev.clientY, src: src, api: r._cac, de: de, v: de ? lireV(r._cac.champs[de]) : src.getAttribute("data-v"), f: null};
  });
  window.addEventListener("pointermove", function(ev){
    var g = glisse; if (!g || ev.pointerId !== g.id) return;
    if (!g.f) { if (Math.hypot(ev.clientX - g.x, ev.clientY - g.y) < 8) return; g.f = el("div", "cac-fantome"); g.f.textContent = net((g.src.querySelector(".cac-v") || g.src).textContent); D.body.appendChild(g.f); g.src.classList.add("part"); }
    g.f.style.transform = "translate(" + ev.clientX + "px," + ev.clientY + "px) translate(-50%,-70%) rotate(-2deg)";
    $$(".cac-case.vise").forEach(function(x){ x.classList.remove("vise"); });
    var c = caseSous(ev); if (c && c.closest(".cac") === g.api.racine) c.classList.add("vise");
  });
  function lache(ev, annule){
    var g = glisse; if (!g || ev.pointerId !== g.id) return; glisse = null; if (!g.f) return;
    g.f.remove(); vientDeGlisser = true; setTimeout(function(){ vientDeGlisser = false; }, 0);
    var c = annule ? null : caseSous(ev);
    if (c && c.closest(".cac") === g.api.racine) { var cle = c.getAttribute("data-cle"); if (g.de && g.de !== cle) g.api.poser(g.de, null); g.api.poser(cle, g.v); }
    else if (g.de && !annule) g.api.poser(g.de, null);
    choix = null; g.api.rendre();
  }
  window.addEventListener("pointerup", function(ev){ lache(ev, false); });
  window.addEventListener("pointercancel", function(ev){ lache(ev, true); });

  /* La correction de l'activité montre la chaîne complète (n°336) : le corrigé de sa DERNIÈRE étape (qui reprend, en
     clair, ce que les étapes d'avant ont fait trouver) est posé en tête de la correction (`details.correction`), sauf
     si la correction porte déjà sa figure. Il se dessine à l'ouverture. */
  function poserCorriges(){
    var parCor = [];
    $$(".cac[data-cac]:not(.cac-corrige)").forEach(function(r){
      var a = r.closest(".activite, .act, .carte, section.card, .exercice, section"); if (!a) return;
      var cor = a.querySelector("details.correction, details.corrige"); if (!cor || cor._cacCorrige) return;
      var deja = parCor.filter(function(x){ return x.cor === cor; })[0];
      if (deja) deja.r = r; else parCor.push({cor: cor, r: r});
    });
    parCor.forEach(function(x){
      var cor = x.cor; cor._cacCorrige = true;
      if (cor.querySelector("figure, img, object, svg[viewBox]")) return;          // la correction a déjà son schéma complet
      var conf = {}; try { conf = JSON.parse(x.r.getAttribute("data-cac") || "{}"); } catch (e) { return; }
      var boite = el("div", "cac-corriges");
      boite.innerHTML = '<p class="cac-corrige-t"><b>Le schéma complet</b>&nbsp;: compare-le avec tes réponses, case par case.</p>';
      var c = el("div", "cac cac-corrige");
      c.setAttribute("data-cac", JSON.stringify({dessin: conf.dessin, vides: conf.vides, titres: conf.titres, vue: conf.vue, corrige: true}));
      boite.appendChild(c);
      var sm = cor.querySelector(":scope > summary"); cor.insertBefore(boite, sm ? sm.nextSibling : cor.firstChild);
    });
  }
  function init(){ poserCorriges(); $$(".cac[data-cac]").forEach(function(r){ if (!r._cac) Chaine(r); }); }
  window.ChaineACompleter = {init: init, Chaine: Chaine};
  if (D.readyState === "loading") D.addEventListener("DOMContentLoaded", init); else init();
  // la page remet ses réponses après coup (sauvegarde relue) : le dessin se repeint une fois tout chargé
  window.addEventListener("load", function(){ $$(".cac").forEach(function(r){ if (r._cac) r._cac.rendre(); }); });
})();
