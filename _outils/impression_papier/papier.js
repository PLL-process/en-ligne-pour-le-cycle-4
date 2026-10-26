/* Fiche papier — source unique : _outils/impression_papier/papier.js (posé par poser.py ; ne pas modifier dans la page).
   Prépare, une fois, ce que le papier remplace (cachés à l'écran : .pp-papier) ; avant chaque impression, marque la séance
   affichée. Rien ne change à l'écran. */
(function(){
  "use strict";
  if (window.__fichePapier) return;
  window.__fichePapier = true;
  function el(tag, cls, txt){ var e = document.createElement(tag); if (cls) e.className = cls; if (txt) e.textContent = txt; return e; }
  var ECRAN = ".toolbar,.choix-parcours-boutons,#navharm,.pp-papier,[role=tablist]";
  var panneaux = [];

  function propre(t){ return String(t || "").replace(/\s+/g, " ").trim(); }
  function sansEmoji(t){ return propre(t).replace(/^[^0-9A-Za-zÀ-ÿ«"(]+/, ""); }

  function entete(){
    var h1 = document.querySelector("h1"), sous = document.querySelector(".subtitle");
    var titre = sansEmoji(h1 ? h1.textContent : document.title);
    var niv = document.querySelector(".badge.niveau"), code = document.querySelector(".badge.code");
    var niveau = niv ? propre(niv.textContent) : "";
    var e = el("header", "pp-papier pp-entete");
    var sur = el("div", "pp-surtitre", ["Technologie", niveau, code ? propre(code.textContent) : ""].filter(Boolean).join(" · "));
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
  var TITRES_ECRAN = /billet d.entrée|façons de vivre|où (en suis|j.en suis)|référentiel|ce que dit le programme|ce que tu as déjà fait|avant de commencer|en-tête pédagogique/i;
  function blocsEcran(){
    document.querySelectorAll("section, .card").forEach(function(c){
      var t = c.querySelector(":scope > h2, :scope > h3");
      if (t && TITRES_ECRAN.test(t.textContent)) c.classList.add("pp-ecran");
    });
  }

  function champs(){
    document.querySelectorAll("select").forEach(function(s){
      if (s.closest(ECRAN) || s.closest(".simu,.banc")) return;
      var c = el("span", "pp-papier pp-choix");
      [].slice.call(s.options).forEach(function(o){
        var t = propre(o.textContent);
        if (!t || /^[—–-]/.test(t)) return;
        c.appendChild(el("span", "pp-case", t)); c.appendChild(document.createTextNode(" "));
      });
      s.insertAdjacentElement("afterend", c);
    });
    document.querySelectorAll("textarea").forEach(function(t){
      if (t.closest(ECRAN)) return;
      var n = Math.max(2, Math.min(7, (+t.getAttribute("rows") || 2) + 1));
      var l = el("div", "pp-papier pp-lignes"); l.style.setProperty("--n", n);
      t.insertAdjacentElement("afterend", l);
    });
    document.querySelectorAll("input").forEach(function(i){
      if (i.closest(ECRAN) || i.closest(".simu,.banc")) return;
      var type = (i.getAttribute("type") || "text").toLowerCase();
      if (type === "radio" || type === "checkbox") {
        i.insertAdjacentElement("beforebegin", el("span", "pp-papier pp-coche" + (type === "radio" ? " pp-rond" : "")));
        // les réponses d'une question, alignées sur une ligne (sauf dans un tableau)
        var lab = i.closest("label") || (i.id && document.querySelector('label[for="' + i.id + '"]')) || null;
        var bloc = lab && lab.parentElement && lab.parentElement.contains(i) ? lab : i.parentElement;
        if (bloc && !bloc.closest("td, th") && bloc.parentElement) {
          bloc.classList.add("pp-option");
          if (bloc.parentElement.querySelectorAll(":scope > .pp-option").length >= 2) bloc.parentElement.classList.add("pp-options");
        }
      }
      else if (type === "text" || type === "number") {
        var w = i.getBoundingClientRect().width;
        var tr = el("span", "pp-papier pp-trait");
        if (w > 0) tr.style.setProperty("--l", Math.max(30, Math.min(160, w * .26)) + "mm");
        i.insertAdjacentElement("afterend", tr);
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
  function seanceAffichee(){
    var r = document.documentElement;
    if (!panneaux.length) { r.setAttribute("data-pp-premiere", ""); r.setAttribute("data-pp-derniere", ""); return; }
    var actif = panneaux.filter(function(p){ return getComputedStyle(p).display !== "none"; })[0] || panneaux[0];
    var i = panneaux.indexOf(actif);
    panneaux.forEach(function(p){ p.toggleAttribute("data-pp-actif", p === actif); });
    r.toggleAttribute("data-pp-premiere", i === 0);
    r.toggleAttribute("data-pp-derniere", i === panneaux.length - 1);
    var onglet = document.getElementById(actif.getAttribute("aria-labelledby") || "") ;
    var nomSeance = onglet ? sansEmoji((onglet.innerText || onglet.textContent).replace(/\s*\n\s*/g, " — ")) : "Séance " + (i + 1);
    if (surtitre) surtitre.textContent = surtitreBase + " · " + nomSeance + " (" + (i + 1) + " / " + panneaux.length + ")";
  }

  function preparer(){
    surtitre = entete(); surtitreBase = surtitre.textContent;
    blocsEcran(); simulateurs(); champs(); horsOnglets(); seanceAffichee();
    window.addEventListener("beforeprint", seanceAffichee);
    if (window.matchMedia) { var m = window.matchMedia("print"); if (m.addEventListener) m.addEventListener("change", function(e){ if (e.matches) seanceAffichee(); }); }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", preparer); else preparer();
})();
