/* Mode lecture v1 — une partie par écran (demande de Pascal du 25/11/2026 : « que le mode mission soit pour tous les
   documents élèves » ; une synthèse et un lexique se lisent, ils ne se jouent pas).
   Source unique : _outils/mode_lecture/ (poser.py). Ne pas le modifier dans la page.

   Ce script n'écrit rien dans la page et n'en retire rien : il montre ses parties une à la fois, avec une barre
   d'étapes et deux boutons — Précédent · Suivant. Tout ce qui cache est sous @media screen : la page s'imprime
   entière, comme avant. Il ne garde dans le navigateur que le choix d'affichage de l'élève, et seulement s'il en fait
   un : « Page complète » y laisse une marque, « Mode lecture » la retire. Ni réponse, ni progression (n°322). */
(function(){
"use strict";
if (document.documentElement.hasAttribute("data-mode-lecture")) return; document.documentElement.setAttribute("data-mode-lecture", "v1");
var D = document, CLE = "lecture:" + (decodeURIComponent(location.pathname).split("/").pop() || "page");
/* Un navigateur piloté par un robot de test ouvre la page complète : les contrôles et les bancs du dépôt mesurent la
   page qui défile, comme avant ; le banc du mode (banc_lecture.mjs) l'allume lui-même. */
var DEFAUT = !(navigator && navigator.webdriver);
function $(s, r){ return (r || D).querySelector(s); }
function $$(s, r){ return [].slice.call((r || D).querySelectorAll(s)); }
function el(t, c, h){ var e = D.createElement(t); if (c) e.className = c; if (h) e.innerHTML = h; return e; }
function net(t){ return String(t || "").replace(/\s+/g, " ").trim(); }
function enfants(n){ return [].slice.call(n.children).filter(function(c){ return !/^(SCRIPT|STYLE|TEMPLATE|LINK|NOSCRIPT)$/.test(c.tagName); }); }

/* ═══ Les parties ═══
   Une partie : une carte de la page (section, article, .card, .carte, .bloc, .box), un bloc qui s'ouvre sur son titre,
   ou — dans une page écrite à plat — un titre h2 et ce qui le suit jusqu'au titre suivant. Ce qui précède la première
   partie (le titre de la page, sa barre d'outils) reste en haut de chaque écran ; ce qui suit une partie sans en être
   une (une note, le pied de page) l'accompagne. */
var PARTIE = "section, article, .card, .carte, .bloc, .box";
function estPartie(c){ return c.matches(PARTIE) || (c.tagName === "DIV" && !!c.firstElementChild && c.firstElementChild.matches("h2, h3")); }
function ouvre(c){ return estPartie(c) || c.tagName === "H2"; }
function conteneur(){
  var meilleur = null, n = 1;
  $$("main, .page, .wrap, .container, body").forEach(function(c){
    var k = enfants(c).filter(ouvre).length;
    if (k > n){ n = k; meilleur = c; }
  });
  return meilleur;
}
function titreDe(noeuds){
  for (var i = 0; i < noeuds.length; i++){
    var n = noeuds[i], h = n.matches("h2, h3") ? n : $("h2, h3", n);
    if (h){ var c = h.cloneNode(true); /* sans le compte de notions, « ↑ La carte », la pastille du niveau */ $$(".compte, .retour-carte, .niv, small", c).forEach(function(x){ x.remove(); }); if (net(c.textContent)) return net(c.textContent); }
    if (n.getAttribute("aria-label")) return net(n.getAttribute("aria-label"));
  }
  return "";
}
var C = null, ecrans = [], k = 0, actif = false, tete, pied, invite, ancre;
function decouper(){
  var cur = null, o = [], sousTitre = false;
  enfants(C).forEach(function(c){
    if (c.classList.contains("ml-seul") || c.classList.contains("ml-invite")) return;
    /* dans une page écrite à plat, un titre h2 emmène tout ce qui le suit jusqu'au titre suivant — sa boîte comprise */
    if (c.tagName === "H2"){ cur = { n:[c] }; o.push(cur); sousTitre = true; }
    else if (estPartie(c) && !sousTitre){ cur = { n:[c] }; o.push(cur); }
    else if (cur) cur.n.push(c);
    else if (c.tagName !== "H1" && c.tagName !== "NAV") c.classList.add("ml-entete");   // sous le titre : la question de la page, sa barre d'outils
  });
  o.forEach(function(e, i){ e.titre = titreDe(e.n) || "Partie " + (i + 1); });
  return o;
}

/* ═══ La barre, le pied ═══ */
function caler(){
  var n = $("#navharm"), h = 0;
  if (n){ var s = getComputedStyle(n); if (s.display !== "none" && (s.position === "sticky" || s.position === "fixed")) h = Math.round(n.getBoundingClientRect().height + (parseFloat(s.top) || 0)); }
  tete.style.top = h + "px";
}
function chrome(){
  invite = el("div", "ml-invite");
  var b = el("button", "ml-entrer"); b.type = "button"; b.id = "btnLecture"; b.textContent = "📖 Mode lecture : une partie à la fois";
  invite.appendChild(b); b.addEventListener("click", function(){ entrer(true); });
  var premier = ecrans[0].n[0]; premier.parentNode.insertBefore(invite, premier);
  ancre = el("div", "ml-ancre ml-seul"); premier.parentNode.insertBefore(ancre, premier);
  tete = el("div", "ml-tete ml-seul",
    '<div class="ml-ligne"><p class="ml-ou" id="mlOu" role="status" aria-live="polite"></p>' +
    '<button type="button" class="ml-quitter" id="mlQuitter">📄 Page complète</button></div>' +
    '<nav aria-label="Parties de la page"><ol class="ml-rail" id="mlRail"></ol></nav>');
  premier.parentNode.insertBefore(tete, premier);
  pied = el("div", "ml-pied ml-seul",
    '<div class="ml-pied-in"><button type="button" class="ml-btn ml-prec" id="mlPrec">← <span>Précédent</span></button>' +
    '<button type="button" class="ml-btn ml-suiv" id="mlSuiv">Suivant →</button></div>');
  D.body.appendChild(pied);
  var rail = $("#mlRail");
  ecrans.forEach(function(e, i){
    var li = el("li"), bt = el("button"); bt.type = "button"; bt.setAttribute("data-k", i);
    bt.setAttribute("aria-label", "Partie " + (i + 1) + " sur " + ecrans.length + " : " + e.titre);
    li.appendChild(bt); rail.appendChild(li);
  });
  rail.addEventListener("click", function(ev){ var x = ev.target.closest("[data-k]"); if (x) aller(+x.getAttribute("data-k"), true); });
  $("#mlQuitter").addEventListener("click", sortir);
  $("#mlPrec").addEventListener("click", function(){ aller(k - 1, true); });
  $("#mlSuiv").addEventListener("click", function(){ aller(k + 1, true); });
  var t = null; window.addEventListener("resize", function(){ if (!actif) return; clearTimeout(t); t = setTimeout(caler, 120); });
}
function montrer(haut){
  ecrans.forEach(function(e, i){ e.n.forEach(function(n){ n.classList.toggle("ml-cache", i !== k); }); });
  D.body.classList.toggle("ml-suite", k > 0);          // passé la première partie, le haut de la page se fait petit
  $("#mlOu").innerHTML = "<b>Partie " + (k + 1) + " sur " + ecrans.length + "</b> · " + ecrans[k].titre.replace(/[&<>]/g, function(c){ return { "&":"&amp;", "<":"&lt;", ">":"&gt;" }[c]; });
  $$("#mlRail [data-k]").forEach(function(b, i){ b.classList.toggle("ici", i === k); b.classList.toggle("lu", i < k); if (i === k) b.setAttribute("aria-current", "step"); else b.removeAttribute("aria-current"); });
  var p = $("#mlPrec"), s = $("#mlSuiv");
  p.disabled = k === 0; s.disabled = k === ecrans.length - 1;
  s.textContent = k === ecrans.length - 1 ? "Fin de la page ✓" : "Suivant →";
  if (haut){ var y = ancre.getBoundingClientRect().top + window.pageYOffset - (parseFloat(tete.style.top) || 0) - 6; if (window.pageYOffset > y) window.scrollTo(0, Math.max(0, y)); }
}
function aller(j, haut){ if (j < 0 || j >= ecrans.length) return; k = j; montrer(haut); }
function ecranDe(cible){ for (var j = 0; j < ecrans.length; j++){ if (ecrans[j].n.some(function(n){ return n === cible || n.contains(cible); })) return j; } return -1; }
function versAncre(nom, defile){
  var cible = null; try { cible = D.getElementById(decodeURIComponent(nom)); } catch (e) {}
  if (!cible) return false;
  var j = ecranDe(cible); if (j < 0) return false;
  aller(j, false);
  if (defile){ try { cible.scrollIntoView({ block:"start" }); window.scrollBy(0, -((parseFloat(tete.style.top) || 0) + tete.offsetHeight + 10)); } catch (e) {} }
  return true;
}
function entrer(choisi){
  actif = true; D.body.classList.add("ml"); caler();
  if (choisi){ try { localStorage.removeItem(CLE); } catch (e) {} }
  montrer(!!choisi);
}
function sortir(){
  actif = false; D.body.classList.remove("ml"); D.body.classList.remove("ml-suite");
  try { localStorage.setItem(CLE, "0"); } catch (e) {}
  var b = $("#btnLecture"); b.focus({ preventScroll:true }); b.scrollIntoView({ block:"center" });
}
function init(){
  C = conteneur(); if (!C) return;                       // moins de deux parties : rien à découper, la page reste telle quelle
  ecrans = decouper(); if (ecrans.length < 2) return;
  chrome();
  /* un lien de la page vers une ancre que le mode cache (« voir la partie 3 », « retour à la carte ») mène à son écran */
  D.addEventListener("click", function(ev){
    if (!actif || !ev.target.closest) return;
    var a = ev.target.closest('a[href^="#"]'); if (!a || a.getAttribute("href").length < 2) return;
    if (versAncre(a.getAttribute("href").slice(1), true)) ev.preventDefault();
  });
  window.addEventListener("hashchange", function(){ if (actif && location.hash.length > 1) versAncre(location.hash.slice(1), true); });
  var veut = DEFAUT; try { if (localStorage.getItem(CLE) === "0") veut = false; } catch (e) {}
  if (veut){ entrer(false); if (location.hash.length > 1) versAncre(location.hash.slice(1), true); }
}
/* pour le banc : les écrans, et celui qui est montré */
D.documentElement._lecture = { ecrans: function(){ return ecrans.map(function(e){ return e.titre; }); }, ici: function(){ return k; }, actif: function(){ return actif; } };
if (D.readyState === "loading") D.addEventListener("DOMContentLoaded", init); else init();
})();
