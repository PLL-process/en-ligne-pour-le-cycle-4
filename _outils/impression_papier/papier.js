/* Fiche papier — source unique : _outils/impression_papier/papier.js (posé par poser.py ; ne pas modifier dans la page).
   Prépare, une fois, ce que le papier remplace (cachés à l'écran : .pp-papier) ; avant chaque impression, marque la séance
   affichée. Rien ne change à l'écran. */
(function(){
  "use strict";
  // Une seule fois par page. La garde est un attribut, pas une variable globale : une variable « __… » à vrai serait lue
  // par controle_verrous.mjs comme un verrou ouvert au chargement (règle n°226).
  var RACINE = document.documentElement;
  if (RACINE.hasAttribute("data-pp-script")) return;
  RACINE.setAttribute("data-pp-script", "v1");
  function el(tag, cls, txt){ var e = document.createElement(tag); if (cls) e.className = cls; if (txt) e.textContent = txt; return e; }
  var ECRAN = ".toolbar,.choix-parcours-boutons,#navharm,.pp-papier,[role=tablist]";
  var panneaux = [];

  function propre(t){ return String(t || "").replace(/\s+/g, " ").trim(); }
  function sansEmoji(t){ return propre(t).replace(/^[^0-9A-Za-zÀ-ÿ«"(]+/, ""); }

  function entete(){
    var h1 = document.querySelector("h1"), sous = document.querySelector(".subtitle");
    var titre = sansEmoji(h1 ? h1.textContent : document.title);
    var niv = document.querySelector(".badge.niveau");
    var codes = [].slice.call(document.querySelectorAll(".badge.code")).map(function(c){ return propre(c.textContent); }).filter(Boolean);
    var niveau = niv ? propre(niv.textContent) : "";
    if (!niveau || !codes.length) {                         // badges sans classe : reconnus à leur texte (« 4e », « 4e_C8.1 · C8.2 »)
      [].forEach.call(document.querySelectorAll(".badges .badge, .badges > span"), function(b){
        var x = propre(b.textContent);
        if (!niveau && /^[3-5]e$/.test(x)) niveau = x;
        else if (/^[3-5]e_C\d/.test(x) && codes.indexOf(x) < 0 && !document.querySelector(".badge.code")) codes.push(x);
      });
    }
    // un <div>, pas un <header> : des scripts et des bancs prennent « le » header de la page (querySelector("header"))
    var e = el("div", "pp-papier pp-entete");
    var sur = el("div", "pp-surtitre", ["Technologie", niveau, codes.join(", ")].filter(Boolean).join(" · "));
    e.appendChild(sur);
    e.appendChild(el("div", "pp-titre", titre));
    if (sous && propre(sous.textContent)) e.appendChild(el("div", "pp-sous", propre(sous.textContent)));
    var id = el("div", "pp-ident");
    ["Nom", "Prénom", "Classe", "Date"].forEach(function(n, i){ id.appendChild(el("span", i > 1 ? "pp-court" : "", n + " :")); });
    e.appendChild(id);
    document.body.insertBefore(e, document.body.firstChild);
    document.documentElement.style.setProperty("--pp-pied", JSON.stringify(titre + (niveau ? " · " + niveau : "")));
    return sur;
  }

  // Les blocs qui ne servent qu'à l'écran, reconnus à leur titre (ils n'ont pas de classe commune).
  var TITRES_ECRAN = /billet d.entrée|façons de vivre|où (en suis|j.en suis)|référentiel|ce que dit le programme|ce que tu as déjà fait|avant de commencer|en-tête pédagogique|crcn mobilisés/i;
  function blocsEcran(){
    document.querySelectorAll("section, .card").forEach(function(c){
      var t = c.querySelector(":scope > h2, :scope > h3");
      if (t && TITRES_ECRAN.test(t.textContent)) c.classList.add("pp-ecran");
    });
  }

  var menus = [];
  // Avant l'impression : la case de la réponse choisie dans un menu est cochée (un menu « — choisis — » ne coche rien).
  function reponsesChoisies(){
    menus.forEach(function(c){ [].forEach.call(c.querySelectorAll(".pp-case"), function(k){
      var o = k.ppOption; k.classList.toggle("pp-pris", !!o && o.selected && !!o.value && !/^[—–-]/.test(propre(o.textContent)));
    }); });
  }
  function avantImpression(){ seanceAffichee(); reponsesChoisies(); }
  function champs(){
    document.querySelectorAll("select").forEach(function(s){
      if (s.closest(ECRAN) || s.closest(".simu,.banc")) return;
      var c = el("span", "pp-papier pp-choix");
      [].slice.call(s.options).forEach(function(o){
        var t = propre(o.textContent);
        if (!t || /^[—–-]/.test(t)) return;
        var k = el("span", "pp-case", t); k.ppOption = o;
        c.appendChild(k); c.appendChild(document.createTextNode(" "));
      });
      s.insertAdjacentElement("afterend", c);
      menus.push(c);
    });
    // Les champs de texte, les cases et les boutons radio changent d'habit à l'impression (papier.css) : rien n'est inséré
    // à côté d'eux. On aligne seulement les réponses d'une même question sur une ligne (sauf dans un tableau).
    document.querySelectorAll("input[type=radio], input[type=checkbox]").forEach(function(i){
      if (i.closest(ECRAN) || i.closest(".simu,.banc")) return;
      var lab = i.closest("label") || (i.id && document.querySelector('label[for="' + i.id + '"]')) || null;
      var bloc = lab && lab.parentElement && lab.parentElement.contains(i) ? lab : i.parentElement;
      if (bloc && !bloc.closest("td, th") && bloc.parentElement) {
        bloc.classList.add("pp-option");
        if (bloc.parentElement.querySelectorAll(":scope > .pp-option").length >= 2) bloc.parentElement.classList.add("pp-options");
      }
    });
  }

  // Un simulateur se fait en ligne : sur papier, on dit où, et on garde une place pour noter ce qu'on observe.
  function simulateurs(){
    document.querySelectorAll(".simu, .banc").forEach(function(s){
      if (s.parentElement && s.parentElement.closest(".simu, .banc")) return;
      var b = el("div", "pp-papier pp-enligne");
      b.appendChild(el("div", "", "🖥  Cette partie se fait sur la page en ligne. Note ici ce que tu observes."));
      var sel = s.querySelector("select");
      var tab = el("table"), tr = el("tr");
      tr.appendChild(el("th", "", sel ? "Essai" : "Ce que je règle")); tr.appendChild(el("th", "", "Ce que j'observe")); tab.appendChild(tr);
      var lignes = sel ? [].slice.call(sel.options).map(function(o){ return propre(o.textContent); }).filter(function(t){ return t && !/^[—–-]/.test(t); }) : ["", "", ""];
      lignes.slice(0, 8).forEach(function(t){ var r = el("tr"); r.appendChild(el("td", "", t)); r.appendChild(el("td")); tab.appendChild(r); });
      b.appendChild(tab);
      s.insertAdjacentElement("afterend", b);
      s.classList.add("pp-ecran");
    });
  }

  // Les couleurs claires écrites dans la page (style="color:…") : pensées pour un fond d'écran sombre, elles
  // disparaissent sur le papier blanc. On les reconnaît ici (une couleur écrite dans la page est la même à l'écran et
  // à l'impression) et on calcule la même teinte, assez foncée pour le papier ; elle ne sert qu'à l'impression.
  var toile = null;
  function rvb(t){
    if (!t || /var\(|inherit|initial|unset|currentcolor|transparent/i.test(t)) return null;
    if (!/^rgb/i.test(t)) {                                  // « white », « #fff » : le navigateur les écrit en clair
      toile = toile || document.createElement("canvas").getContext("2d");
      if (!toile) return null;
      toile.fillStyle = "#010203"; toile.fillStyle = t;
      var h = /^#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i.exec(toile.fillStyle);
      return h && toile.fillStyle !== "#010203" ? [parseInt(h[1], 16), parseInt(h[2], 16), parseInt(h[3], 16)] : rvb(toile.fillStyle === "#010203" ? "" : toile.fillStyle);
    }
    var m = /rgba?\(\s*([\d.]+)[ ,]+([\d.]+)[ ,]+([\d.]+)(?:[ ,/]+([\d.]+))?/.exec(t);
    return m && (m[4] === undefined || +m[4] > .5) ? [+m[1], +m[2], +m[3]] : null;
  }
  function lum(c){ return c.reduce(function(s, v, k){ v /= 255; v = v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); return s + [.2126, .7152, .0722][k] * v; }, 0); }
  function fondDe(e){                                     // la couleur moyenne d'un fond écrit dans la page (couleur ou dégradé)
    var l = [], c = rvb(e.style.backgroundColor);
    if (c) l.push(lum(c));
    (String(e.style.backgroundImage || "").match(/rgba?\([^)]*\)|#[0-9a-f]{3,8}\b/gi) || []).forEach(function(x){ var d = rvb(x); if (d) l.push(lum(d)); });
    return l.length ? l.reduce(function(a, b){ return a + b; }) / l.length : null;
  }
  // Un bloc (pas une étiquette : celles-là gardent leur couleur et leur texte clair) au fond foncé écrit dans la page.
  // Il peut être caché au chargement (une autre séance) : on le reconnaît à sa balise, pas à sa taille.
  var BLOCS = /^(DIV|SECTION|ARTICLE|DETAILS|ASIDE|HEADER|FOOTER|FIGURE|FORM|FIELDSET|MAIN|NAV|UL|OL|BLOCKQUOTE)$/;
  function fonds(){
    document.querySelectorAll("body [style*='background' i]").forEach(function(e){
      var f = fondDe(e);
      if (f !== null && f < .3 && BLOCS.test(e.tagName)) e.classList.add("pp-fond");
    });
  }
  // Un bloc qui ne porte que des boutons (« Vérifier », « Correction ») : vide sur le papier, il laisserait un cadre vide.
  function boutonsSeuls(){
    document.querySelectorAll("body :is(div,p,nav,span,footer)").forEach(function(e){
      if (e.closest(ECRAN) || !e.querySelector("button, .btn")) return;
      var c = e.cloneNode(true);
      c.querySelectorAll("button, .btn, script, style, .pp-papier").forEach(function(x){ x.remove(); });
      if (!propre(c.textContent) && !c.querySelector("img, svg, canvas, video, object, input, select, textarea, table")) e.classList.add("pp-ecran");
    });
  }
  function encres(){
    document.querySelectorAll("body [style*='color' i]").forEach(function(e){
      var c = rvb(e.style.color);
      if (!c || lum(c) <= .18) return;                       // déjà lisible sur blanc (4,5 : 1 et plus)
      for (var a = e; a && a !== document.body; a = a.parentElement) {
        if (a.classList.contains("pp-fond")) break;          // ce fond-là devient blanc : le texte doit foncer
        var f = fondDe(a);
        if (f !== null && f < .3) return;                    // texte clair sur un petit fond foncé (une étiquette) : voulu
      }
      var k = 1, d = c;
      while (lum(d) > .05 && k > .05) { k -= .04; d = c.map(function(v){ return Math.round(v * k); }); }
      e.classList.add("pp-encre"); e.style.setProperty("--pp-encre", "rgb(" + d.join(",") + ")");
    });
  }

  // Séquence à séances : ce qui est hors des onglets, avant (l'ouverture) ou après (la clôture).
  function horsOnglets(){
    panneaux = [].slice.call(document.querySelectorAll("[role=tabpanel]"));
    if (!panneaux.length) return;
    var premier = panneaux[0], dernier = panneaux[panneaux.length - 1], vus = [];
    panneaux.forEach(function(p){
      for (var a = p; a && a.parentElement && a !== document.body; a = a.parentElement) {
        [].slice.call(a.parentElement.children).forEach(function(f){
          if (f === a || vus.indexOf(f) >= 0 || f.querySelector("[role=tabpanel]") || f.matches("[role=tabpanel], script, style, .pp-papier")) return;
          vus.push(f);
          var avant = f.compareDocumentPosition(premier) & Node.DOCUMENT_POSITION_FOLLOWING;
          var apres = f.compareDocumentPosition(dernier) & Node.DOCUMENT_POSITION_PRECEDING;
          if (avant) f.setAttribute("data-pp-hors", "avant"); else if (apres) f.setAttribute("data-pp-hors", "apres");
        });
      }
    });
  }

  var surtitre = null, surtitreBase = "";
  function morceaux(e){                                    // « Séance 3 » + « Mes traces » : les textes de l'onglet, un à un
    var out = [];
    [].forEach.call(e.childNodes, function(n){
      if (n.nodeType === 3) { if (propre(n.textContent)) out.push(propre(n.textContent)); }
      else if (n.nodeType === 1 && !/^(svg|img|script|style)$/i.test(n.tagName) && n.getAttribute("aria-hidden") !== "true") out = out.concat(morceaux(n));
    });
    return out;
  }
  function seanceAffichee(){
    var r = document.documentElement;
    if (!panneaux.length) { r.setAttribute("data-pp-premiere", ""); r.setAttribute("data-pp-derniere", ""); return; }
    var actif = panneaux.filter(function(p){ return getComputedStyle(p).display !== "none"; })[0] || panneaux[0];
    // le rang, dans l'ordre des onglets que voit l'élève (une page peut ranger ses panneaux autrement)
    var onglet = document.getElementById(actif.getAttribute("aria-labelledby") || "");
    var onglets = [].slice.call(document.querySelectorAll("[role=tab]"));
    var i = onglet && onglets.length === panneaux.length ? onglets.indexOf(onglet) : panneaux.indexOf(actif);
    if (i < 0) i = panneaux.indexOf(actif);
    panneaux.forEach(function(p){ p.toggleAttribute("data-pp-actif", p === actif); });
    r.toggleAttribute("data-pp-premiere", i === 0);
    r.toggleAttribute("data-pp-derniere", i === panneaux.length - 1);
    var nomSeance = actif.getAttribute("data-titre") ? sansEmoji(actif.getAttribute("data-titre"))
      : onglet ? sansEmoji(morceaux(onglet).join(" — ")) : "Séance " + (i + 1);
    if (surtitre) surtitre.textContent = surtitreBase + " · " + nomSeance + " (" + (i + 1) + " / " + panneaux.length + ")";
  }

  function preparer(){
    document.documentElement.setAttribute("data-pp", "");    // la fiche est prête : le choix de la séance peut s'appliquer
    surtitre = entete(); surtitreBase = surtitre.textContent;
    blocsEcran(); simulateurs(); champs(); boutonsSeuls(); fonds(); encres(); horsOnglets(); seanceAffichee();
    window.addEventListener("beforeprint", avantImpression);
    if (window.matchMedia) { var m = window.matchMedia("print"); if (m.addEventListener) m.addEventListener("change", function(e){ if (e.matches) avantImpression(); }); }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", preparer); else preparer();
})();
