/* Mode mission v1 — un exercice à la fois (décision de Pascal du 11/11/2026).
   Source unique : _outils/mode_mission/ (poser.py). Ne pas le modifier dans la page.

   Ce script n'invente aucun exercice : il montre ceux de la page, un écran à la fois, et habille les grilles de
   boutons radio en étiquettes à placer. Les réponses attendues sont lues dans la page elle-même (ses vérifications,
   ou `data-bonne`) ; la sauvegarde, les verrous et la validation des activités restent ceux de la page. */
(function(){
"use strict";
/* posé une seule fois. Un attribut, pas une variable `window.__…` : le contrôle des verrous (n°226) lit ces
   variables comme des expériences enregistrées, et le mode mission n'en est pas une. */
if (document.documentElement.hasAttribute("data-mode-mission")) return; document.documentElement.setAttribute("data-mode-mission", "v1");
var D = document, CLE = "mission:" + (decodeURIComponent(location.pathname).split("/").pop() || "page");
var M, actif = false, parPanneau = {}, panneau = null, ecrans = [], k = 0, sel = null, glisse = false, cles = null, g = null, construit = false;
var ET = '<svg class="ms-et{on}" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6l2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.5 6.1 20.6l1.2-6.5L2.5 9.5l6.6-.9z"/></svg>';
var COCHE = '<svg class="ms-coche" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>';
function $(s, r){ return (r || D).querySelector(s); }
function $$(s, r){ return [].slice.call((r || D).querySelectorAll(s)); }
function el(t, c, h){ var e = D.createElement(t); if (c) e.className = c; if (h) e.innerHTML = h; return e; }
function esc(t){ return String(t).replace(/[&<>"]/g, function(c){ return { "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;" }[c]; }); }
function net(t){ return String(t || "").replace(/\s+/g, " ").trim(); }
/* Allumé d'emblée (décision de Pascal du 14/11/2026 : « le mode mission est, pour toutes les séquences, déclenché
   d'emblée ») : à sa première visite, l'élève arrive en mission ; s'il choisit « 📄 Page complète », la page s'en souvient
   (dans ce navigateur) ; « Effacer ma sauvegarde » le remet en mission. Un navigateur piloté par un robot de test
   (`navigator.webdriver`) ouvre la page complète, comme avant : les bancs et les contrôles mesurent la page qui défile,
   et ceux du mode (banc_generique, banc_mission, banc_defaut) l'allument eux-mêmes. */
var DEFAUT = !(navigator && navigator.webdriver);
/* Le bouton de la page qui efface TOUTE sa sauvegarde (règle d'or n°322 ; les mêmes identifiants que
   controle_sauvegarde_locale.py et banc_effacement.mjs). Deux usages :
   · une page qui n'en a pas n'enregistre rien d'elle-même (un TP, une activité : ses champs se vident au
     rechargement). Le mode n'y retient pas plus qu'elle — `garde` : les étoiles et les réussites vivent le temps de
     la page ; l'écran où l'on en est, le temps de l'onglet (un rechargement par mégarde ne renvoie pas au début) ;
     seul le choix d'affichage (mission ou page complète) reste dans le navigateur, comme une préférence. Rien de ce
     qu'a fait un élève n'attend le suivant ;
   · une page qui en a un efface parfois d'autres clés que celle que ce script sait lire (le kit des ateliers : une
     clé par exercice). Le geste est alors reconnu à son bouton : une clé retirée juste après un appui sur lui. */
var SIEN = "#btnReset, #btnEffacer, #btn-effacer, #clear", garde = true, appui = 0;
document.addEventListener("click", function(ev){ if (ev.target && ev.target.closest && ev.target.closest(SIEN)) appui = Date.now(); }, true);
try {
  var _rm = Storage.prototype.removeItem, _vide = Storage.prototype.clear, marque = function(){ try { sessionStorage.setItem("mission:efface", "1"); } catch (e) {} };
  /* La clé de sauvegarde de la page : un `const KEY` (« seq_… ») au premier niveau d'un script se voit d'ici ; dans près
     d'une séquence sur deux elle vit dans une fonction — on la lit alors dans le source (KEY, cle ou CLE, de valeur
     « seq_… »). Sans cela, « Effacer ma sauvegarde » laissait les étoiles de l'élève précédent sur 27 des 60 séquences
     (règle d'or n°322, point 4 ; banc_effacement.mjs, 20/11/2026). */
  var _cles = null, estCleDeLaPage = function(k){
    try { if (typeof KEY === "string" && k === KEY) return true; } catch (e) {}
    if (!_cles || document.readyState === "loading"){
      _cles = [];
      try { var motif = /(?:const|let|var)\s+(?:KEY|cle|CLE)\s*=\s*"(seq_[^"]+)"/g, sc = document.scripts, m;
        for (var i = 0; i < sc.length; i++){ if (sc[i].src || /json/.test(sc[i].type || "")) continue; var tx = sc[i].textContent; motif.lastIndex = 0; while ((m = motif.exec(tx))) _cles.push(m[1]); } } catch (e) {}
    }
    return _cles.indexOf(String(k)) !== -1;
  };
  Storage.prototype.removeItem = function(k){ if (this === window.localStorage && String(k) !== CLE && (estCleDeLaPage(k) || Date.now() - appui < 1500)) marque(); return _rm.apply(this, arguments); };
  Storage.prototype.clear = function(){ if (this === window.localStorage) marque(); return _vide.apply(this, arguments); };
} catch (e) {}
function lire(){ try { M = JSON.parse(localStorage.getItem(CLE) || "null"); } catch (e) { M = null; } if (!M || M.v !== 1) M = { v:1, on:DEFAUT, k:{}, essais:{}, etoiles:{}, fait:{} }; if (!M.erreurs) M.erreurs = {}; if (!M.loin) M.loin = {};
  if (!garde){ var t = null; try { t = JSON.parse(sessionStorage.getItem(CLE) || "null"); } catch (e) {}
    M = { v:1, on:M.on, k:(t && t.k) || {}, essais:{}, erreurs:{}, etoiles:{}, fait:{}, loin:(t && t.loin) || {} }; if (t && t.ici) M.ici = t.ici; } }
/* `vu` : la page a déjà enregistré quelque chose depuis que la mission tient ses comptes. Sa sauvegarde disparue ensuite,
   c'est « Effacer ma sauvegarde » : on le distingue ainsi d'une page où l'élève n'a encore rien enregistré. */
function ecrire(){ try { if (typeof KEY === "string" && localStorage.getItem(KEY) !== null) M.vu = true; localStorage.setItem(CLE, JSON.stringify(garde ? M : { v:1, on:M.on }));
  if (!garde) sessionStorage.setItem(CLE, JSON.stringify({ k:M.k, loin:M.loin, ici:M.ici })); } catch (e) {} }
function etoiles(n){ var s = ""; for (var i = 1; i <= 3; i++) s += ET.replace("{on}", i <= n ? " on" : ""); return '<span class="ms-etoiles" role="img" aria-label="' + n + " étoile" + (n > 1 ? "s" : "") + ' sur 3">' + s + "</span>"; }
/* prévenir la page qu'une réponse a changé, comme le ferait un appui : l'événement part du bouton radio coché (c'est
   lui que certaines pages écoutent pour sauvegarder), ou du groupe quand plus rien n'est coché */
function saisie(f){ var x = (f.tagName === "FIELDSET" && $("input[type=radio]:checked", f)) || f; x.dispatchEvent(new Event("input", { bubbles:true })); x.dispatchEvent(new Event("change", { bubbles:true })); }

/* Les séances : des panneaux. Trois écritures dans le dépôt :
     gabarit commun   .seance-tab[data-panel]     →  .seance-panel.active      cartes : section.card
     Book Train       [role=tab][aria-controls]   →  section.panneau.actif     cartes : div.carte
     page sans onglets (une grande étape d'une séquence découpée) : des `.seance-bloc` à la suite, tous visibles —
       ici c'est le mode qui n'en montre qu'un à la fois (`.ms-ici`), et qui mène de l'un à l'autre
   Depuis le 25/11/2026 (demande de Pascal : « que le mode mission soit pour tous les documents élèves ») :
     ateliers et cahiers des représentations : les mêmes onglets ARIA que Book Train, mais le panneau ouvert est
       celui qui n'est pas `hidden` (leur moteur, `kit.js`, ne pose pas de classe) ;
     page à cartes, sans séances (TP, activité, atelier d'une seule page) : son conteneur est l'unique panneau, et
       chacun de ses blocs (section, carte, palier) fait un écran ; ce qui précède un bloc l'accompagne. */
var G = null, CARTE = "section.card, div.carte";
var BLOC = "section, article, .card, .carte";
/* un bloc de la page : une section, une carte — ou un <div> qui s'ouvre sur son propre titre (« 📋 Ma trace Pix ») */
function estBloc(c){ return c.matches(BLOC) || (c.tagName === "DIV" && !!c.firstElementChild && c.firstElementChild.matches("h2, h3")); }
function conteneur(){
  /* le bloc qui range les cartes de la page : parmi <main>, .page, .wrap, .container, celui qui en porte le plus
     en enfants directs ; il en faut au moins trois, sinon la page n'a rien à découper */
  var meilleur = null, n = 2;
  $$("main, .page, .wrap, .container, #contenu").forEach(function(c){
    var k = enfants(c).filter(function(x){ return estBloc(x) && rendu(x); }).length;
    if (k > n){ meilleur = c; n = k; }
  });
  return meilleur;
}
function gabarit(){
  if ($(".seance-panel") && $(".seance-tab")) return { panneau:".seance-panel", onglet:".seance-tab", actif:"active", attr:"data-panel", de:function(o){ return o.dataset.panel; } };
  if ($("section.panneau[role=tabpanel]") && $("[role=tablist] [role=tab][aria-controls]")) return { panneau:"section.panneau[role=tabpanel]", onglet:"[role=tablist] [role=tab][aria-controls]", actif:$("section.panneau[role=tabpanel].actif") ? "actif" : null, kit:!$("section.panneau[role=tabpanel].actif") && !!$("#donnees-page"), attr:"aria-controls", de:function(o){ return o.getAttribute("aria-controls"); } };
  if ($(".seance-bloc[id]")) return { panneau:".seance-bloc[id]", onglet:null, actif:"ms-ici" };
  var c = conteneur();
  if (c){ c.classList.add("ms-page"); if (!c.id) c.id = "ms-page"; return { panneau:".ms-page", onglet:null, actif:"ms-ici", page:true }; }
  return null;
}
/* le panneau ouvert : celui qui porte la classe du gabarit ; sans classe, celui que la page ne cache pas (`hidden`) */
function selActif(){ return G.actif ? G.panneau + "." + G.actif : G.panneau + ":not([hidden])"; }
function panneauActif(){ return $(selActif()); }
function ongletActif(){ var P = panneauActif(); return P && G.onglet ? $$(G.onglet).filter(function(o){ return G.de(o) === P.id; })[0] || null : null; }
function nomOnglet(o){ for (var i = 0; i < o.childNodes.length; i++){ var n = o.childNodes[i]; if (n.nodeName !== "SMALL" && net(n.textContent)) return net(n.textContent); } return net(o.textContent); }
function nomSeance(){ var o = ongletActif(); if (o) return nomOnglet(o); var m = panneau && /^seance-(\d+)$/.exec(panneau.id); return m ? "Séance " + m[1] : ""; }
function nomPage(){ var h = $("h1"); return h ? net(h.textContent) : ""; }
/* la séance d'avant (-1) ou d'après (+1) : son identifiant, ou null ; et l'ouvrir */
function voisine(d){
  if (G.onglet){ var o = $$(G.onglet), i = o.indexOf(ongletActif()); return i < 0 || !o[i + d] ? null : G.de(o[i + d]); }
  var P = $$(G.panneau), j = P.indexOf(panneauActif()); return j < 0 || !P[j + d] ? null : P[j + d].id;
}
function ouvrir(id){
  if (G.onglet){ var o = $$(G.onglet).filter(function(x){ return G.de(x) === id; })[0]; if (o) o.click(); return; }
  $$(G.panneau).forEach(function(P){ P.classList.toggle(G.actif, P.id === id); }); M.ici = id; synchroniser();
}

/* Les réponses attendues, lues dans les vérifications de la page. Cinq écritures :
     const att = {id:"texte", …}  (ou `attendu`, ou `ATTENDUS = {1:{id:"texte"}, 2:{…}}`, une table par activité)
     $("id").value === "texte"      $("id").value.startsWith("début")      sv("id", "texte")  (l'ancien gabarit)
     <fieldset data-bonne="texte">                    (la réponse écrite sur la question elle-même : Book Train)
   Une réponse n'est retenue que si elle désigne UNE proposition du champ, et une seule : au moindre doute (deux
   textes pour la même question, un début commun à deux propositions), l'écran ne se vérifie pas ici — la page le
   vérifie toujours. Le banc générique rejoue chaque réponse retenue contre la vérification de la page. */
function candidats(){
  if (cles) return cles; cles = {};
  function note(id, sorte, v){ (cles[id] || (cles[id] = [])).push([sorte, v.replace(/\\(["'])/g, "$1")]); }
  var table = /const (?:att|ATT)\w*\s*=\s*\{([\s\S]*?)\};/g, paire = /(\w+)\s*:\s*"((?:[^"\\]|\\.)*)"/g,
      egal = /\(\s*["'](\w+)["']\s*\)\.value\s*===?\s*(["'])((?:(?!\2)[^\\]|\\.)*)\2/g,
      debut = /\(\s*["'](\w+)["']\s*\)\.value\.(?:startsWith\(\s*(["'])((?:(?!\2)[^\\]|\\.)*)\2\s*\)|indexOf\(\s*(["'])((?:(?!\4)[^\\]|\\.)*)\4\s*\)\s*===?\s*0)/g,
      svf = /\bsv\(\s*(["'])(\w+)\1\s*,\s*(["'])((?:(?!\3)[^\\]|\\.)*)\3\s*\)/g;
  $$("script:not([src])").forEach(function(sc){
    var t = sc.textContent, m, q; if (t.indexOf("data-mode-mission") >= 0) return;
    table.lastIndex = 0; while ((m = table.exec(t))){ paire.lastIndex = 0; while ((q = paire.exec(m[1]))) note(q[1], "=", q[2]); }
    egal.lastIndex = 0; while ((m = egal.exec(t))) note(m[1], "=", m[3]);
    debut.lastIndex = 0; while ((m = debut.exec(t))) note(m[1], "^", m[3] !== undefined ? m[3] : m[5]);
    svf.lastIndex = 0; while ((m = svf.exec(t))) note(m[2], "=", m[4]);
  });
  return cles;
}
/* Sixième écriture (25/11/2026) : les ateliers des représentations rangent leurs attendus dans
   `<script type="application/json" id="donnees-page">`, par NOM de champ : `choix` {name, bonne, retours},
   `classer` {items:[{name, bonne, indice}]}, `menus` et `tableau` {cases:[{name, bonne, indice, retours}]}.
   Seules ces réponses uniques sont lues ; un texte, des cases à cocher, un croquis restent vérifiés par la page. */
var _noms = null;
function parNom(){
  if (_noms) return _noms; _noms = {};
  var sc = D.getElementById("donnees-page"), d = null;
  try { d = sc ? JSON.parse(sc.textContent) : null; } catch (e) { d = null; }
  var ex = (d && d.exercices) || {};
  function note(x){ if (x && x.name && typeof x.bonne === "string") _noms[x.name] = { bonne:x.bonne, retours:x.retours || {}, indice:x.indice || "" }; }
  Object.keys(ex).forEach(function(id){ (ex[id].widgets || []).forEach(function(w){
    if (w.type === "choix") note(w);
    else if (w.type === "classer") (w.items || []).forEach(note);
    else if (w.type === "menus" || w.type === "tableau") (w.cases || []).forEach(note);
  }); });
  return _noms;
}
function nomDe(f){ if (f.tagName === "SELECT") return f.name || ""; var r = $("input[type=radio]", f); return r ? r.name : ""; }
/* Un champ à réponse unique : un groupe de boutons radio, ou une liste déroulante qui pose une question (les pages
   pas encore révisées). Une liste d'interface (`data-interface`) n'est pas une question. */
var CHAMP = "fieldset.qcm-groupe, select[id]:not([data-interface])";
function estChamp(c){ return c.matches(CHAMP); }
function valeurs(f){ return f.tagName === "SELECT" ? [].slice.call(f.options).map(function(o){ return o.value; }).filter(Boolean) : $$("input[type=radio]", f).map(function(x){ return x.value; }); }
function lireV(f){ if (f.tagName === "SELECT") return f.value; var c = $("input[type=radio]:checked", f); return c ? c.value : ""; }
function ecrireV(f, v){ if (f.tagName === "SELECT"){ f.value = v || ""; return; } $$("input[type=radio]", f).forEach(function(r){ r.checked = (v != null && r.value === v); }); }
function intitule(f){ var l = f.tagName === "SELECT" ? (f.id && $('label[for="' + f.id + '"]')) || f.closest("label") : $("legend", f); return net(l ? l.textContent : f.getAttribute("aria-label") || "Cette question").replace(/\s*[:…]\s*$/, ""); }
function cle(f){
  if (f._msCle !== undefined) return f._msCle === null ? undefined : f._msCle;
  var c = (candidats()[f.id] || []).slice(), r = null;
  if (f.hasAttribute("data-bonne")) c.push(["=", f.getAttribute("data-bonne")]);
  var pn = G.kit ? parNom()[nomDe(f)] : null; if (pn && !c.length) c.push(["=", pn.bonne]);
  if (c.length && estChamp(f) && !f.classList.contains("positionnement")){
    var vals = valeurs(f), bons = [];
    c.forEach(function(x){
      var ok = vals.filter(function(v){ return x[0] === "=" ? v === x[1] : v.indexOf(x[1]) === 0; });
      if (x[0] === "=" && !ok.length) return;                       // un texte qui n'est pas une proposition : il parle d'autre chose
      if (ok.length !== 1) bons.push(null); else if (bons.indexOf(ok[0]) < 0) bons.push(ok[0]);
    });
    if (bons.length === 1 && bons[0] !== null) r = bons[0];
  }
  f._msCle = r; return r === null ? undefined : r;
}

/* ═══ Les écrans d'une séance : la séance, puis pour chaque activité l'atelier, le départ, une question par écran,
       « je retiens » ; puis chaque autre carte ═══
   Une ACTIVITÉ est le bloc qui porte un exercice et sa vérification. Trois formes dans le dépôt :
     · `.activite` (gabarit commun) : une ou plusieurs zones `.exo`, la vérification dans la zone ou après les aides ;
     · une carte qui EST l'activité (thèmes 1 et 3) : sa zone `.exo` porte la vérification, ou la carte la porte ;
     · `.act` (ancien gabarit) : consigne, questions, aides et vérification à la suite, sans zone.
   Sans zone marquée, la zone est ce qui va de la première question à la première aide ou à la vérification. */
function titreDe(n){ var h = n.matches && n.matches("h2,h3,h4") ? n : $("h2,h3,h4", n); return h ? net(h.textContent) : ""; }
function enfants(n){ return [].slice.call(n.children).filter(function(c){ return !/^(SCRIPT|STYLE|TEMPLATE|LINK|NOSCRIPT)$/.test(c.tagName); }); }
function rendu(c){ return getComputedStyle(c).display !== "none" && !c.hidden; }
function estAide(c){ return c.matches("details.aide1,details.aide2,details.aide"); }
/* le bouton de vérification de la page, et le message qu'elle écrit : `button[data-check]` et `.feedback` (gabarit
   commun) ; `button.verif[data-exo="x"]` et `#res-x` (Book Train : le bouton désigne sa zone `#x`) */
/* Le bouton `button.verifier` et le message `.retour[data-retour]` sont ceux du kit des ateliers. Ils ne comptent que
   dans une page du kit (un atelier, un cahier — `G.kit`) : dans une séquence, un exercice du kit incrusté garde son
   écran entier, avec son bouton à lui, comme avant (le 25/11/2026, les lire partout coupait ces écrans en deux sur
   six séquences du thème 1 — vu par banc_generique avant la livraison). */
var CHECK_BASE = "button[data-check], button.verif[data-exo]", CHECK = CHECK_BASE;
/* le bouton lui-même, ou le paragraphe qui ne porte que lui (`<p><button class="btn verifier">` des ateliers) */
function estCheck(c){ return c.matches(CHECK) || (c.tagName === "P" && c.children.length === 1 && c.firstElementChild.matches(CHECK) && net(c.textContent) === net(c.firstElementChild.textContent)); }
function boutonDe(c){ return c.matches(CHECK) ? c : $(CHECK, c); }
function estMessage(c){ return c.classList.contains("feedback") || (!!G.kit && c.matches(".retour[data-retour]")) || (!!c.id && c.id.indexOf("res-") === 0 && !!$('button.verif[data-exo="' + c.id.slice(4) + '"]')); }
function porteChamp(c){ return estChamp(c) || !!$(CHAMP + ",textarea,input:not([type=radio]):not([type=checkbox]):not([type=hidden])", c); }
function estActivite(c){
  if (c.matches(".activite, .act")) return true;
  if (!c.matches(CARTE) || $(".activite, .act", c)) return false;
  var k = enfants(c);
  return k.some(estCheck) || k.some(function(x){ return x.classList.contains("exo") && !!$(CHECK, x); });
}
/* Les zones d'exercice d'une suite de blocs. Une zone : ses parties (une par titre de partie), son bouton de
   vérification, son message, et ce qui suit ce bouton (la correction de la zone). Après une vérification, un nouveau
   titre de partie, une nouvelle question ou un autre bouton de vérification ouvrent la zone suivante : une zone
   « 3a… vérifier… 3b… vérifier » en fait deux. `titres` : les balises qui ouvrent une partie. */
function zonesDe(nodes, titres){
  var liste = [], z = null, cur = null;
  function nouvelle(){ z = { parts:[], check:null, fb:[], suite:[], avant:[], exo:null }; cur = null; liste.push(z); }
  nouvelle();
  nodes.forEach(function(c){
    var t = titres.indexOf(c.tagName) >= 0;
    if (z.check && (t || (c.tagName !== "DETAILS" && !estMessage(c) && (estCheck(c) || porteChamp(c))))) nouvelle();
    if (!z.check && estCheck(c)){ z.check = c; return; }
    if (estMessage(c)){ z.fb.push(c); return; }
    if (z.check){ z.suite.push(c); return; }
    if (t || !cur){ cur = { h: t ? c : null, n:[] }; z.parts.push(cur); }
    cur.n.push(c);
  });
  return liste.filter(function(x){ return x.parts.length || x.check; });
}
function activite(A, E){
  var carte = A.matches(CARTE), kids = enfants(A), nom = titreDe(A) || "Activité";
  /* une zone d'exercice marquée : `.exo`, ou le bloc que le bouton de vérification désigne (`data-exo="x"` → `#x`) */
  function designee(c){ return !!c.id && kids.some(function(b){ return estCheck(b) && boutonDe(b).getAttribute("data-exo") === c.id; }); }
  var exos = kids.filter(function(c){ return c.classList.contains("exo") || designee(c); });
  var header = kids.filter(function(c){ return c.tagName === "HEADER" || (carte && (c.tagName === "H2" || (c === kids[0] && c.tagName === "H3"))); });
  var marquee = exos.length && (A.matches(".activite") || exos.some(function(x){ return !x.classList.contains("exo") || !!$(CHECK, x); }));
  var i = marquee ? kids.indexOf(exos[0]) : -1;
  /* pas de zone marquée (carte-activité, ancien gabarit) : de la première question à la première aide ou à la
     vérification. Une activité du gabarit commun sans zone (un Bonus replié) reste un seul écran, telle quelle ; un
     volet replié n'ouvre jamais une zone. */
  if (!marquee && !A.matches(".activite")){
    for (var q = 0; q < kids.length; q++){ if (estAide(kids[q]) || estCheck(kids[q])) break; if (header.indexOf(kids[q]) < 0 && kids[q].tagName !== "DETAILS" && !kids[q].classList.contains("consigne") && porteChamp(kids[q])){ i = q; break; } }
  }
  if (i < 0){ E.push({ t:"activite", titre:nom, n:kids }); return; }
  var avant = kids.slice(0, i);
  /* la fiche de l'activité, repliée (details.fiche-activite, 15/11/2026) ou non (meta-grid), va avec le titre */
  var tete = avant.filter(function(c){ return header.indexOf(c) >= 0 || c.classList.contains("meta-grid") || c.matches("div.meta") || c.classList.contains("fiche-activite") || c.classList.contains("pastille-maison") || c.classList.contains("competence-visee"); });
  /* un exercice incrusté (atelier, rappel replié du cahier des charges) a son écran, avant le départ de l'activité */
  var ateliers = avant.filter(function(c){ return c.matches(".atelier-incruste, details.incruste-repliee"); });
  var consigne = avant.filter(function(c){ return c.classList.contains("consigne"); });
  var ress = avant.filter(function(c){ return tete.indexOf(c) < 0 && ateliers.indexOf(c) < 0 && consigne.indexOf(c) < 0; });
  var titres = carte ? ["H3", "H4"] : ["H4"], zones = [], aides = [], attente = [];
  if (marquee){
    /* à partir de la première zone : les zones, les aides (communes à l'activité), le bouton de vérification et son
       message quand ils suivent les aides, ce qui sépare deux zones (il accompagne la suivante), et la fin */
    kids.slice(i).forEach(function(c){
      if (exos.indexOf(c) >= 0){ var zs = zonesDe(enfants(c), titres); zs.forEach(function(z, r){ z.exo = c; if (!r) z.avant = attente; }); attente = []; zones = zones.concat(zs); return; }
      if (estAide(c)){ aides.push(c); return; }
      if (estCheck(c)){ var de = boutonDe(c).getAttribute("data-exo"), zc = zones.filter(function(z){ return !z.check && (!de || z.exo.id === de); }).pop(); if (zc){ zc.check = c; zc.dehors = true;
        /* un outil posé entre la dernière zone et sa vérification (l'éditeur où l'on prouve, un écrit) se joue AVANT de
           vérifier : il a son écran, après la dernière question, et c'est là que la vérification de la page parle */
        if (zc === zones[zones.length - 1] && ecrit(attente)){ zc.preuve = attente; attente = []; }
        return; } }
      if (estMessage(c)){ var zf = zones.filter(function(z){ return z.dehors && !z.fb.length; }).pop(); if (zf){ zf.fb.push(c); return; } }
      attente.push(c);
    });
  } else {
    /* la zone court de la première question à la fin du bloc, aides mises à part ; ce qui suit la dernière
       vérification (correction, à retenir) part sur l'écran « je retiens » */
    var corps = [];
    kids.slice(i).forEach(function(c){ if (estAide(c)) aides.push(c); else corps.push(c); });
    zones = zonesDe(corps, titres);
    if (zones.length){ var zd = zones[zones.length - 1]; attente = zd.suite; zd.suite = []; }
  }
  if (!zones.length){ E.push({ t:"activite", titre:nom, n:kids }); return; }
  var fin = attente;
  ateliers.forEach(function(a){ var sm = a.matches("details") ? $("summary", a) : null; E.push({ t:"atelier", titre:(sm ? net(sm.textContent) : "") || titreDe(a) || "Atelier", n:header.concat([a]) }); });
  /* ce qui précède la première partie sans poser de question (un tableau, une figure) est une ressource */
  var p0 = zones[0].parts;
  if (p0.length > 1 && !p0[0].h && !p0[0].n.some(porteChamp)) ress = ress.concat(p0.shift().n);
  E.push({ t:"depart", titre:nom, n:tete.concat(ress, consigne) });
  /* sur un écran de question, la ressource ne repose pas une question déjà posée ailleurs (une question à la fois,
     règle d'or n°335) : un bloc de la ressource qui porte un champ de réponse reste sur l'écran de départ */
  var ressQ = ress.filter(function(c){ return !(estChamp(c) || $(CHAMP + ",textarea", c)); });
  var ressBtn = null;
  if (ressQ.length){ ressBtn = el("button", "ms-ressbtn ms-seul"); ressBtn.type = "button"; ressBtn.setAttribute("data-ms", "ress"); A.insertBefore(ressBtn, ress[0].parentNode === A ? ress[0] : kids[i]); }
  var J = 0;
  zones.forEach(function(z){
    var retour = el("div", "ms-retour ms-seul"); retour.setAttribute("aria-live", "polite");
    if (z.check) z.check.parentNode.insertBefore(retour, z.check);
    else if (z.exo) z.exo.appendChild(retour);
    else { var der = z.parts.length ? z.parts[z.parts.length - 1].n : []; var apres = der.length ? der[der.length - 1].nextSibling : null; A.insertBefore(retour, apres); }
    if (z.check) z.check.classList.add("ms-origine");
    var tous = [];
    z.parts.forEach(function(p){ habiller(p); var ps = pas(p); ps.forEach(function(st, q){ tous.push({ p:p, st:st, j:J, q:q, sur:ps.length }); }); J++; });
    if (z.avant.length && tous.length) tous[0].st.n = z.avant.concat(tous[0].st.n);
    if (z.preuve){ if (tous.length) tous.push({ p:{ h:null }, st:{ n:z.preuve, champs:[] }, j:"p" + J, q:0, sur:1, preuve:true }); else fin = z.preuve.concat(fin); }
    tous.forEach(function(x, r){
      var dernier = r === tous.length - 1, base = x.preuve ? "Avant de vérifier" : x.p.h ? net(x.p.h.textContent) : "À toi de jouer";
      E.push({ t:"partie", titre: base + (x.sur > 1 ? " · " + (x.q + 1) + " sur " + x.sur : ""), act:A, ress:ressQ, ressBtn:ressBtn, retour:retour, champs:x.st.champs, trou:x.st.trou || "", dernier:dernier, check:z.check, fb:z.fb[0],
               id:(A.id || nom) + "#" + x.j + "." + x.q, n:(ressBtn ? [ressBtn] : []).concat(carte ? header : [], x.st.n, [retour], dernier ? z.fb.concat(z.suite) : [], aides) });
    });
  });
  if (fin.length) E.push({ t:"retenir", titre:"Je retiens — " + nom, act:A, n:header.concat(fin) });
}
/* Une partie se joue pas à pas : chaque question à choix sur son écran, chaque jeu d'étiquettes sur le sien, une
   série de réponses courtes (rangée) ensemble, un écrit (zone de texte et sa version étayée) sur le sien.
   Ce qui précède une question sans rien demander (un simulateur, un tableau) l'accompagne. */
function champsDe(c){ return estChamp(c) ? [c] : $$(CHAMP, c); }
function courte(f){ return f.classList.contains("qcm-rangee") || f.classList.contains("qcm-court"); }
/* un trou de code : « ▢1 — … » (la marque ▢1 est dans le code) ou « Trou ① — … » (la marque ①, dans un .trou-num) */
function trou(f){ var x = intitule(f), m = /^▢ ?(\d+)/.exec(x); if (m) return "▢" + m[1]; m = /^Trou ([①-⑳])/.exec(x); return m ? m[1] : ""; }
function ecrit(nodes){ var q = "textarea,select[data-interface],input:not([type=radio]):not([type=checkbox]):not([type=hidden])"; return nodes.some(function(c){ return c.matches(q) || !!$(q, c); }); }
function pas(p){
  var steps = [], tampon = [], n = p.n.filter(function(x){ return x !== p.h; }), i = 0;
  function contexte(){ var t = tampon; tampon = []; if (ecrit(t)){ steps.push({ n:t, champs:[] }); return []; } return t; }
  while (i < n.length){
    var c = n[i];
    if (c.classList.contains("ms-etq")){
      var grp = [c]; i++; while (i < n.length && n[i].classList.contains("ms-origine")){ grp.push(n[i]); i++; }
      steps.push({ n:contexte().concat(grp), champs:c._sets }); continue;
    }
    var f = champsDe(c);
    /* les trous ▢1, ▢2… d'un même code : un écran par trou, le code (ce qui précède) redit sur chacun, le trou en
       cours marqué dans le code (une question à la fois, règle d'or n°335 ; décision de Pascal du 16/11/2026) */
    if (f.length === 1 && courte(f[0]) && trou(f[0])){
      var ctx = contexte(), lot = [[c, f[0]]]; i++;
      while (i < n.length && champsDe(n[i]).length === 1 && courte(champsDe(n[i])[0]) && trou(champsDe(n[i])[0])){ lot.push([n[i], champsDe(n[i])[0]]); i++; }
      lot.forEach(function(x){ steps.push({ n:ctx.concat([x[0]]), champs:[x[1]], trou:trou(x[1]) }); });
      continue;
    }
    if (f.length){
      var g2 = [c], ch = f.slice(), rangee = courte(f[0]); i++;
      if (rangee) while (i < n.length && champsDe(n[i]).length && courte(champsDe(n[i])[0])){ g2.push(n[i]); ch = ch.concat(champsDe(n[i])); i++; }
      steps.push({ n:contexte().concat(g2), champs:ch }); continue;
    }
    tampon.push(c); i++;
  }
  if (tampon.length){ if (steps.length && !ecrit(tampon)) steps[steps.length - 1].n = steps[steps.length - 1].n.concat(tampon); else steps.push({ n:tampon, champs:[] }); }
  steps.forEach(function(s){ if (p.h) s.n = [p.h].concat(s.n); });
  return steps;
}
/* Une carte sans titre (ni h2, ni h3, ni h4) : son écran s'appelait « Suite » ou « À lire », ce qui ne dit rien à
   l'élève (audit externe du 20/11/2026 ; relevé : 31 écrans sur 15 séquences). Son nom se lit maintenant, dans l'ordre :
   dans son nom accessible (aria-label : « Fin de la séance 1 », « Le banc des matériaux »), sinon dans le début de son
   texte, s'il tient en quelques mots (« 🧪 Atelier Pix — Les données du jardin connecté »). L'ancien nom ne reste qu'à
   défaut. Le premier nœud qui porte un nom ou du texte décide : on ne va pas chercher un titre plus loin dans la carte. */
function titreSans(noeuds){
  for (var i = 0; i < noeuds.length; i++){
    var n = noeuds[i]; if (!n || n.nodeType !== 1) continue;
    var ref = n.getAttribute("aria-labelledby"), cible = ref ? D.getElementById(ref) : null;
    var a = net(n.getAttribute("aria-label") || (cible ? cible.textContent : ""));
    if (a) return a;
    var c = n.cloneNode(true); $$("script,style,template,noscript", c).forEach(function(x){ x.remove(); });
    var t = net(c.textContent); if (!t) continue;
    var m = /^(.*?)(?:[.!?…]\s|\s[:?!]\s|$)/.exec(t), d = m ? m[1] : t;
    if (d.length > 56 && d.indexOf(" — ") > 0) d = d.slice(0, d.indexOf(" — "));
    d = d.replace(/[\s:;,.—–-]+$/, "");
    return d.length >= 4 && d.length <= 56 && d.split(" ").length >= 2 ? d : "";
  }
  return "";
}
/* un lien seul, sans titre ni question (« 📖 Les mots de cette séance ») */
function lienSeul(C){ return !titreDe(C) && !porteChamp(C) && !$("img,svg,canvas,video,iframe,object,button,details,table", C) && !!$("a[href]", C) && net(C.textContent).split(" ").length < 12; }
/* page à cartes : les blocs que la page range APRÈS son conteneur, au même niveau (« Prêt·e à t'entraîner » et le Bonus
   du TP mBot2, posés avant </body>) font des écrans comme les autres */
function suivants(P){ var o = []; for (var x = P.nextElementSibling; x; x = x.nextElementSibling) if (estBloc(x) && rendu(x)) o.push(x); return o; }
/* Une page à onglets qui range sa clôture APRÈS ses panneaux (l'atelier de planification : Bonus, Bilan, QCM, traces ;
   l'entraînement au brevet : « Pour aller plus loin ») la montre sous chaque onglet. En mission, ces cartes restaient
   sous chaque écran. Elles deviennent les derniers écrans du dernier panneau, et se cachent ailleurs (25/11/2026).
   Aucune des 60 séquences n'en porte : leur clôture vit dans la dernière séance (règle d'or n°306). */
var _hors = null;
function horsPanneaux(){
  if (_hors) return _hors; _hors = [];
  if (G.page) return _hors;
  var P = $$(G.panneau), der = P[P.length - 1]; if (!der) return _hors;
  $$(CARTE).forEach(function(c){
    if (!(der.compareDocumentPosition(c) & Node.DOCUMENT_POSITION_FOLLOWING) || der.contains(c)) return;      // après le dernier panneau, dans l'ordre de la page
    if (c.closest(G.panneau) || (c.parentElement && c.parentElement.closest(CARTE)) || c.closest(".ms-seul, .ms-invite, footer") || !rendu(c)) return;
    _hors.push(c);
  });
  return _hors;
}
function construire(P){
  var E = [], portes = [], devant = [], tousP = $$(G.panneau);
  enfants(P).concat(G.page ? suivants(P) : (P === tousP[tousP.length - 1] ? horsPanneaux() : [])).forEach(function(C){
    if (C.classList.contains("page-suivante") || !rendu(C)) return;          // ce que la page cache d'elle-même (fiche professeur) ne fait pas d'écran
    /* le bouton « Exercice 2 › » du kit des ateliers, seul dans son paragraphe : le mode porte le sien */
    if (C.tagName === "P" && C.children.length === 1 && C.firstElementChild.matches("button.suivant[data-vers]")){ C.classList.add("ms-origine"); return; }
    /* page à cartes : ce qui n'est pas un bloc (le titre de la page, sa mission, une note entre deux cartes) attend
       le bloc qui suit, et s'affiche avec son premier écran */
    if (G.page){
      if (!estBloc(C)){ devant.push(C); return; }
      var i0 = E.length; un(C);
      if (devant.length){ if (E.length > i0) E[i0].n = devant.concat(E[i0].n); else E.push({ t:"carte", titre:titreSans(devant) || nomPage() || "Pour commencer", n:devant }); devant = []; }
      if (E.length > i0 && E[i0].t === "carte" && (!E[i0].titre || E[i0].titre === "Suite" || E[i0].titre === "La séance")) E[i0].titre = nomPage() || "Pour commencer";
      return;
    }
    un(C);
  });
  if (devant.length){ if (E.length) E[E.length - 1].n = E[E.length - 1].n.concat(devant); else E.push({ t:"carte", titre:nomPage() || "La page", n:devant }); }
  function un(C){
    /* en tête de séance, un lien seul n'est pas un écran (il n'ouvrait la séance que sur lui) : il accompagne le premier */
    if (!E.length && lienSeul(C)){ portes.push(C); return; }
    if (estActivite(C)){ activite(C, E); return; }
    var acts = enfants(C).filter(estActivite);
    if (!acts.length){ E.push({ t:"carte", titre:titreDe(C) || (E.length ? titreSans([C]) || "Suite" : "La séance"), n:[C] }); return; }          // sans titre : le premier écran ouvre la séance
    var avant = [], vu = false, suite = [];
    function vider(){ if (suite.length){ var t = ""; suite.forEach(function(x){ t = t || titreDe(x); }); E.push({ t:"carte", titre:t || titreSans(suite) || "À lire", n:suite }); suite = []; } }
    enfants(C).forEach(function(x){
      if (estActivite(x)){ if (!vu){ vu = true; E.push({ t:"intro", titre:titreDe(C) || "La séance", n:avant, ouverture:true }); } vider(); activite(x, E); }
      /* le bouton « Séance suivante › » rangé DANS la carte de la séance (4e_C9.1) n'est pas un écran : le mode le cache et
         porte le sien. Il laissait dans la barre un écran fantôme, retiré au moment d'y arriver (20/11/2026). */
      else if (!vu) avant.push(x); else if (rendu(x) && !x.classList.contains("page-suivante")) suite.push(x);
    });
    vider();
  }
  if (portes.length){ if (E.length) E[0].n = portes.concat(E[0].n); else E.push({ t:"carte", titre:"La séance", n:portes }); }
  if (E.length && !E.some(function(e){ return e.ouverture; })) E[0].ouverture = true;       // la situation de départ s'ouvre au premier écran
  /* L'éditeur Python reste sous les yeux (Pascal, 17/11/2026 : « on dit que l'éditeur Python est intégré à
     l'activité, mais je ne le vois pas »). Une activité « prédire → tester → reporter » pose ses prédictions sans
     l'éditeur (on prédit avant d'essayer), puis l'éditeur arrive avec la première question qui le lit… et
     disparaissait aux suivantes, qui lisent pourtant la console. Une fois montré dans une activité, il accompagne
     désormais chaque écran de question qui suit, jusqu'à « je retiens ». Seul l'éditeur lui-même est repris : un bloc
     qui porterait aussi une question n'est pas répété (une question à la fois, règle d'or n°335). */
  function editeurDe(n){ return n.matches && (n.matches(".editeur-py") || !!$(".editeur-py", n)) && !$$(CHAMP, n).some(function(f){ return !f.closest(".editeur-py"); }) ? n : null; }
  var outils = [], enAttente = null;          // un éditeur posé sur l'écran de départ de l'activité vaut pour ses questions
  E.forEach(function(e){
    if (e.t === "depart"){ enAttente = null; e.n.forEach(function(n){ enAttente = enAttente || editeurDe(n); }); return; }
    if (e.t !== "partie" || !e.act) return;
    var deja = outils.filter(function(o){ return o.act === e.act; })[0];
    if (!deja && enAttente){ deja = { act:e.act, n:enAttente }; outils.push(deja); }
    enAttente = null;
    var ed = null; e.n.forEach(function(n){ ed = ed || editeurDe(n); });
    if (ed){ if (!deja) outils.push({ act:e.act, n:ed }); return; }
    if (deja && e.n.indexOf(deja.n) < 0){ e.n = e.n.concat([deja.n]); e.outil = deja.n; }
  });
  /* tous les blocs qui se montrent ou se cachent : ceux des écrans, et leurs conteneurs jusqu'au panneau */
  E.tous = [];
  E.forEach(function(e){ e.n.concat(e.ress || []).forEach(function(n){ for (var p = n; p && p !== P && (p === n || P.contains(p)); p = p.parentNode) if (E.tous.indexOf(p) < 0) E.tous.push(p); }); });
  return E;
}

/* ═══ Les étiquettes : une grille de boutons radio (mêmes réponses pour plusieurs questions) se joue en étiquettes
       à poser. Poser une étiquette coche le bouton radio de la page : rien d'autre ne change. ═══ */
function habiller(p){
  var j = 0;
  while (j < p.n.length){
    var c = p.n[j];
    if (c.classList.contains("qcm-cles")){
      var sets = [], q = j + 1; while (q < p.n.length && p.n[q].matches("fieldset.qcm-grille")){ sets.push(p.n[q]); q++; }
      if (sets.length >= 2){
        var comp = el("div", "ms-etq ms-seul"); comp._sets = sets;
        comp._libs = $$("input[type=radio]", sets[0]).map(function(r){ return r.value; });
        var att = sets.map(cle); comp._unique = att.every(function(a){ return a !== undefined; }) && att.filter(function(a, x){ return att.indexOf(a) === x; }).length === sets.length;   // chaque étiquette sert une fois au plus (il peut en rester : les leurres)
        c.parentNode.insertBefore(comp, c); c.classList.add("ms-origine"); sets.forEach(function(f){ f.classList.add("ms-origine"); });
        p.n.splice(j, 0, comp); j = q + 1; continue;
      }
    }
    j++;
  }
}
function peindre(comp){
  var pris = comp._sets.map(lireV), fini = comp._sets.every(function(f){ return f.classList.contains("ms-juste"); });
  var h = '<p class="ms-geste">Fais glisser chaque étiquette vers sa case. Tu peux aussi la toucher, puis toucher sa case.</p><div class="ms-lignes">'
    + comp._sets.map(function(f, i){
        var v = lireV(f), juste = f.classList.contains("ms-juste"), cl = "ms-case" + (v ? " pleine" : "") + (juste ? " juste" : "") + (f.classList.contains("ms-faux") ? " faux" : "");
        return '<div class="ms-l"><div class="ms-nom">' + $("legend", f).innerHTML + '</div><button type="button" class="' + cl + '" data-i="' + i + '"' + (juste ? " disabled" : "")
          + ' aria-label="' + esc(net($("legend", f).textContent) + " : " + (v || "case vide")) + '">' + (v ? "<span>" + esc(v) + "</span>" : '<span class="ms-vide">pose ici</span>') + (juste ? COCHE : "") + "</button></div>"; }).join("")
    + "</div>";
  if (!fini){
    var labs = comp._libs.map(function(t, j){ return (comp._unique && pris.indexOf(t) >= 0) ? "" : '<button type="button" class="ms-lab' + (sel && sel.comp === comp && sel.j === j ? " choisie" : "") + '" data-j="' + j + '" aria-pressed="' + !!(sel && sel.comp === comp && sel.j === j) + '">' + esc(t) + "</button>"; }).join("");
    var trop = comp._unique ? comp._libs.length - comp._sets.length : 0, plein = pris.every(function(v){ return !!v; });
    var titre = plein && labs ? "Toutes les cases sont remplies : appuie sur « Vérifier »" : "Étiquettes" + (!comp._unique ? " — chacune peut servir plusieurs fois" : trop > 0 ? " — attention, " + trop + " en trop" : "");
    h += '<div class="ms-reserve"><p class="ms-reserve-t">' + titre + '</p><div class="ms-reserve-l">' + (labs || '<span class="ms-geste">Toutes les étiquettes sont posées. Appuie sur « Vérifier ».</span>') + "</div></div>";
  }
  var act = D.activeElement, quoi = act && comp.contains(act) ? (act.dataset.i !== undefined ? '[data-i="' + act.dataset.i + '"]' : act.dataset.j !== undefined ? '[data-j="' + act.dataset.j + '"]' : null) : null;
  comp.innerHTML = h;
  if (quoi){ var x = $(quoi, comp); if (x && !x.disabled) x.focus({ preventScroll:true }); }
}
function poser(comp, i, valeur){
  var f = comp._sets[i]; if (f.classList.contains("ms-juste")) return;
  if (comp._unique && valeur) comp._sets.forEach(function(o){ if (o !== f && lireV(o) === valeur && !o.classList.contains("ms-juste")){ ecrireV(o, null); saisie(o); } });
  ecrireV(f, valeur); f.classList.remove("ms-faux"); saisie(f);
}

/* ═══ L'habillage de la page : la barre de la mission, la barre basse, le bouton de la barre d'outils ═══ */
var tete, pied, bMission, ancre, revenir, horsVue = false;
/* un bouton de la page déjà fixé en bas à droite (« ⬆ haut de page » de Book Train) : le nôtre se pose au-dessus, sans
   le toucher (cible tactile, WCAG 2.5.8). Mesuré une fois, à la première apparition. */
var place = false;
function placer(){
  place = true; var h = 0;
  $$("body *").forEach(function(x){
    if (x === revenir || x.closest(".ms-pied, .ms-tete")) return;
    var s = getComputedStyle(x); if (s.position !== "fixed") return;
    var r = parseFloat(s.right), bo = parseFloat(s.bottom); if (isNaN(r) || isNaN(bo) || r > 120 || bo > 120) return;
    h = Math.max(h, bo + (x.offsetHeight || parseFloat(s.height) || 48));
  });
  if (h) revenir.style.bottom = "calc(" + Math.ceil(h + 10) + "px + env(safe-area-inset-bottom,0px))";
}
/* La barre de la mission colle sous la navigation du site. La feuille de style la pose à 44 px (une navigation collante
   d'une ligne, le gabarit des séquences) ; une navigation qui ne colle pas (les TP) la laisserait flotter à 44 px du
   haut, le texte défilant au-dessus d'elle, et une navigation plus haute la recouvrirait : on mesure. */
function caler(){
  if (!tete) return; var n = $("#navharm"), h = 44;
  if (n){ var s = getComputedStyle(n); h = (s.display !== "none" && (s.position === "sticky" || s.position === "fixed")) ? Math.round(n.getBoundingClientRect().height + (parseFloat(s.top) || 0)) : 0; }
  tete.style.top = Math.abs(h - 44) > 4 ? h + "px" : "";
}
function voirRevenir(){ if (!revenir) return; var v = !actif && horsVue; if (v && !place) placer(); revenir.classList.toggle("voir", v); }
/* ═══ Figer les animations (WCAG 2.2.2 ; veille du 16/11/2026) : une boucle sans fin (un flux, un moteur qui tourne,
       un buzzer) s'arrête d'un bouton, en mission (⏸ dans la barre) comme en page complète (à côté du bouton de la
       mission). Le choix vaut pour tout le site, sur cet appareil. Le bouton n'apparaît que si la page a une boucle. ═══ */
var CLE_FIGE = "anim-figee";
function boucles(){
  var r = false;
  function voir(rs){ for (var i = 0; rs && i < rs.length && !r; i++){ var x = rs[i]; if (x.style && /infinite/.test((x.style.animationIterationCount || "") + " " + (x.style.animation || ""))) r = true; else if (x.cssRules && x.cssRules.length) voir(x.cssRules); } }
  [].slice.call(D.styleSheets).forEach(function(s){ try { voir(s.cssRules); } catch (e) {} });
  return r;
}
function figee(){ try { return localStorage.getItem(CLE_FIGE) === "1"; } catch (e) { return false; } }
function peindreFige(){
  var f = D.documentElement.classList.contains("anim-figee");
  $$("[data-pause-animations]").forEach(function(b){
    b.setAttribute("aria-pressed", f ? "true" : "false");
    var dit = f ? "Relancer les animations" : "Figer les animations";
    if (b.id === "msFiger"){ b.textContent = f ? "▶️" : "⏸️"; b.setAttribute("aria-label", dit); b.title = dit; }
    else b.textContent = (f ? "▶️ " : "⏸️ ") + dit;
  });
}
function figer(){
  if (!boucles()) return;
  D.documentElement.classList.toggle("anim-figee", figee());
  var b = el("button", "btn ms-figer-page"); b.type = "button"; b.setAttribute("data-pause-animations", "");
  if (bMission && bMission.parentNode) bMission.parentNode.appendChild(b);
  var m = $("#msFiger"); if (m) m.hidden = false;
  $$("[data-pause-animations]").forEach(function(x){ x.addEventListener("click", function(){
    var f = !D.documentElement.classList.contains("anim-figee");
    D.documentElement.classList.toggle("anim-figee", f);
    try { localStorage.setItem(CLE_FIGE, f ? "1" : "0"); } catch (e) {}
    peindreFige();
  }); });
  peindreFige();
}
function chrome(){
  /* le bouton d'entrée se range dans le cadre « Ma progression », AVANT les onglets : rien ne s'ajoute entre les
     onglets et les panneaux (controle_squelette, D5), ni dans la barre d'outils (deux lignes à 390 px), ni dans le
     panneau de la séance — celui que mesurent les contrôles */
  var cadre = $(".progress-wrap"), invite = el("div", "ms-invite");          // sans ce cadre : juste AVANT les onglets, jamais dans la barre d'outils
  bMission = el("button", "btn"); bMission.id = "btnMission"; bMission.type = "button";
  bMission.textContent = "🎮 Mode mission : un exercice à la fois";
  invite.appendChild(bMission);
  if (cadre) cadre.appendChild(invite); else { var b0 = $("#seances") || $(G.panneau); b0.parentNode.insertBefore(invite, b0); }
  bMission.addEventListener("click", entrer);
  /* Revenir en mission (Pascal, 16/11/2026 : « quand l'élève quitte ce mode, il a du mal à revenir : aucun bouton
     apparent ») : en page complète, dès que le bouton du haut sort de l'écran, un petit bouton reste en bas à droite. */
  revenir = el("button", "ms-revenir"); revenir.type = "button"; revenir.id = "msRevenir";
  revenir.innerHTML = '🎮 <span>Mode mission</span>'; revenir.setAttribute("aria-label", "Revenir au mode mission : un exercice à la fois");
  /* posé à côté du bouton du haut, AVANT les onglets (il flotte : sa place dans la page ne se voit pas) — jamais après
     la barre d'onglets, où controle_squelette (D5) le compterait comme un contenu hors de toute séance */
  invite.appendChild(revenir); revenir.addEventListener("click", entrer);
  if (window.IntersectionObserver) new IntersectionObserver(function(es){ horsVue = !es[es.length - 1].isIntersecting; voirRevenir(); }).observe(bMission);
  else horsVue = true;
  tete = el("div", "ms-tete ms-seul", '<div class="ms-ligne1"><p class="ms-ou" id="msOu" role="heading" aria-level="2"></p><button type="button" class="ms-figer" id="msFiger" hidden data-pause-animations aria-pressed="false" aria-label="Figer les animations">⏸️</button><button type="button" class="ms-quitter" id="msQuitter">📄 Page complète</button><div class="ms-gains" id="msGains"><span class="ms-jauge" aria-hidden="true"><i id="msJauge"></i></span>' + ET.replace("{on}", " on") + '<span id="msCompte"></span></div></div><nav aria-label="Écrans de la séance"><ol class="ms-rail" id="msRail"></ol></nav>');
  /* un repère sans hauteur juste avant la barre : collée en haut de l'écran, la barre ne dit plus où elle commence */
  var premier = $(G.panneau); ancre = el("div", "ms-ancre ms-seul"); premier.parentNode.insertBefore(ancre, premier); premier.parentNode.insertBefore(tete, premier);
  figer();
  pied = el("div", "ms-pied ms-seul", '<div class="ms-pied-in"><button type="button" class="ms-btn ms-prec" id="msPrec" aria-label="Écran précédent">← <span>Précédent</span></button><button type="button" class="ms-btn ms-verif" id="msVerif">Vérifier</button><span class="ms-vide-f" id="msVide" hidden></span><button type="button" class="ms-btn ms-suiv" id="msSuiv">Suivant →</button></div>');
  D.body.appendChild(pied);
  var tCale = null; window.addEventListener("resize", function(){ if (!actif) return; clearTimeout(tCale); tCale = setTimeout(caler, 120); });
  $("#msQuitter").addEventListener("click", sortir);
  $("#msPrec").addEventListener("click", function(){ aller(k - 1); });
  $("#msSuiv").addEventListener("click", suivant);
  $("#msVerif").addEventListener("click", verifier);
  $("#msRail").addEventListener("click", function(ev){ var b = ev.target.closest("[data-k]"); if (b) aller(+b.dataset.k); });
}
function parties(seul){ var t = []; Object.keys(parPanneau).forEach(function(id){ if (seul && id !== seul) return; parPanneau[id].forEach(function(e){ if (e.t === "partie" && e.champs.some(function(f){ return cle(f) !== undefined; })) t.push(e); }); }); return t; }
/* ═══ La barre d'étapes (Pascal, 16/11/2026 : « certaines leds n'étaient pas allumées alors que l'élève avait fait le
       parcours ») ═══
   Avant, un écran sans question ne s'allumait que s'il était AVANT l'écran en cours : revenir en arrière éteignait
   tout ce qui suivait, avancer le rallumait. Et un écran où l'on écrit, sans rien à vérifier ici, ne s'allumait jamais.
   Désormais : un écran sans question s'allume une fois dépassé, et le reste (M.loin, l'écran le plus loin atteint, par
   séance) ; une question s'allume une fois vérifiée ; répondue mais pas vérifiée, elle se cercle (« à vérifier ») ;
   un écrit s'allume une fois écrit. Jamais selon que la réponse est juste : la barre ne trahit rien.
   Audit du 17/11/2026 : « la barre emploie "fait" pour un écran visité, le tableau de bord "validé" pour une activité
   réussie ; un élève peut croire avoir réussi ». Un écran allumé se dit donc « vu », « vérifié » ou « écrit », et il
   s'allume dans la couleur neutre de la page : le vert reste aux étoiles, qui seules disent la réussite. */
function textes(e){ var q = "textarea,input[type=text],input[type=number],input:not([type])", o = []; e.n.forEach(function(n){ if (!n.matches) return; if (n.matches(q)) o.push(n); $$(q, n).forEach(function(x){ if (o.indexOf(x) < 0) o.push(x); }); }); return o; }
function etatPas(e, j){
  var passe = j < (M.loin[panneau.id] || 0);
  if (e.t !== "partie") return passe ? "fait" : "";
  if (M.fait[e.id]) return "fait";
  var avec = e.champs.filter(function(f){ return cle(f) !== undefined; });
  if (avec.length) return avec.every(function(f){ return lireV(f); }) ? "repondu" : "";
  if (e.dernier && e.check) return passe ? "repondu" : "";          // la vérification de la page attend son appui
  var ts = textes(e);
  /* une question à cases à cocher (le kit des ateliers : « coche tout ce qui manque ») n'a pas de valeur unique : elle
     est répondue dès qu'une case l'est. Lue comme un groupe de boutons radio, elle ne l'était jamais, et son écran
     restait éteint dans la barre, écrit et dépassé (banc_barre, B2, cinq pages du kit — 25/11/2026). */
  function repondu(f){ return !!lireV(f) || (f.tagName === "FIELDSET" && !$("input[type=radio]", f) && !!$("input[type=checkbox]:checked", f)); }
  if (e.champs.length || ts.length) return e.champs.every(repondu) && ts.every(function(x){ return net(x.value); }) ? "fait" : "";
  return passe ? "fait" : "";
}
function barre(){
  var s = ecrans[k];
  var ns = nomSeance();
  $("#msOu").innerHTML = esc(s.titre) + "<small>" + (ns ? esc(ns) + " · " : "") + "écran " + (k + 1) + " sur " + ecrans.length + "</small>";
  var ps = parties(panneau && panneau.id), gagne = ps.reduce(function(a, e){ return a + (M.etoiles[e.id] || 0); }, 0), max = ps.length * 3;
  $("#msCompte").textContent = gagne + " / " + max; $("#msJauge").style.width = (max ? Math.round(100 * gagne / max) : 0) + "%";
  $("#msGains").hidden = !max;                          // rien à gagner ici (un TP à suivre pas à pas) : pas de « ⭐ 0 / 0 »
  $("#msGains").setAttribute("aria-label", gagne + " étoiles gagnées sur " + max + " dans cette séance. Chaque écran en rapporte jusqu'à 3 : 3 sans erreur, 2 avec une erreur (deux si l'écran a trois réponses ou plus), 1 au-delà");
  $("#msGains").title = "Chaque écran rapporte jusqu'à 3 étoiles : 3 sans erreur, 2 avec une erreur (deux si l'écran a trois réponses ou plus), 1 au-delà. Ouvrir une aide ne retire rien.";
  $("#msRail").innerHTML = ecrans.map(function(e, j){ var et = etatPas(e, j); return '<li><button type="button" class="ms-pas' + (et ? " " + et : "") + (j === k ? " ici" : "") + '" data-k="' + j + '"' + (j === k ? ' aria-current="step"' : "") + ' aria-label="Écran ' + (j + 1) + " sur " + ecrans.length + " : " + esc(e.titre) + (et === "fait" ? (e.t !== "partie" ? ", vu" : (e.champs.some(function(f){ return cle(f) !== undefined; }) || e.check) ? ", vérifié" : ", écrit") : et === "repondu" ? ", répondu, pas encore vérifié" : "") + '"></button></li>'; }).join("");
  var exo = s.t === "partie", aVerifier = exo && (s.champs.some(function(f){ return cle(f) !== undefined; }) || (s.dernier && s.check));
  $("#msPrec").disabled = k === 0 && !voisine(-1);
  $("#msVerif").hidden = !aVerifier; $("#msVide").hidden = aVerifier || !exo;
  var suiv = $("#msSuiv"), fin = k === ecrans.length - 1, apres = voisine(1);
  suiv.classList.toggle("seul", !exo); suiv.hidden = fin && !apres;
  suiv.textContent = fin ? (G.attr === "aria-controls" && !G.actif ? "Exercice suivant →" : "Séance suivante →") : s.t === "intro" ? "C'est parti →" : "Suivant →";
}

/* la ressource de l'activité (schéma, tableau) accompagne chaque question : ouverte par défaut, téléphone compris
   (règles d'or n°331 et n°335, 15/11/2026 : l'élève répond le schéma sous les yeux) — et l'élève garde la main */
function ressVue(){ return M.ress === undefined ? true : M.ress; }
/* le trou de l'écran se marque dans le code qu'il complète : chaque « ▢N » du code devient une marque, la sienne
   s'allume (le texte du code ne change pas ; hors mission, rien ne se voit) */
function marquerTrou(s){
  $$(".ms-trou-ici", panneau).forEach(function(x){ x.classList.remove("ms-trou-ici"); });
  if (!s.trou) return;
  s.n.concat(s.ress || []).forEach(function(n){
    (n.matches("pre,.pytrous") ? [n] : $$("pre,.pytrous", n)).forEach(function(z){
      var marques = $$(".trou-num", z).filter(function(x){ return x.textContent.indexOf(s.trou) >= 0; });
      if (!marques.length){
        if (!z._trous){
          z._trous = true;
          var w = D.createTreeWalker(z, NodeFilter.SHOW_TEXT), t, l = [];
          while ((t = w.nextNode())) if (/▢ ?\d/.test(t.nodeValue)) l.push(t);
          l.forEach(function(t){
            var fr = D.createDocumentFragment();
            t.nodeValue.split(/(▢ ?\d+)/).forEach(function(b, j){
              if (!b) return;
              if (j % 2){ var sp = el("span", "ms-trou"); sp.textContent = b; sp.setAttribute("data-trou", b.replace(" ", "")); fr.appendChild(sp); }
              else fr.appendChild(D.createTextNode(b));
            });
            t.parentNode.replaceChild(fr, t);
          });
        }
        marques = $$('.ms-trou[data-trou="' + s.trou + '"]', z);
      }
      marques.forEach(function(x){ x.classList.add("ms-trou-ici"); });
    });
  });
}
/* ═══ La correction se voit (règle d'or n°336, 16/11/2026) ═══
   Pascal : « le mode mission ne contient pas les corrections ». Elles y étaient, repliées sous leur titre sur l'écran
   « je retiens », et passaient inaperçues. Une fois l'activité vérifiée (la dernière question a lancé la vérification
   de la page), sa correction s'ouvre d'elle-même, sur l'écran « je retiens » comme sous la dernière question. Avant,
   elle reste repliée et une ligne dit où elle est et quand elle s'ouvrira : on essaie d'abord, on se corrige ensuite. */
var CORR = "details.correction, details.corrige, details.correction-complete";
function corrections(s){ var o = []; s.n.forEach(function(n){ if (!n.matches) return; if (n.matches(CORR)) o.push(n); $$(CORR, n).forEach(function(c){ if (o.indexOf(c) < 0) o.push(c); }); }); return o; }
/* un écran qui se vérifie : des réponses connues, ou la vérification de la page sous sa dernière question */
function verifiable(e){ return e.t === "partie" && (e.champs.some(function(f){ return cle(f) !== undefined; }) || (e.dernier && !!e.check)); }
/* l'activité est vérifiée quand chacun de ses écrans qui se vérifie l'a été ; une activité sans rien à vérifier (des
   réponses écrites) ouvre sa correction dès l'écran « je retiens » : l'élève compare avec ce qu'il a écrit */
function etatActivite(A){
  var vs = ecrans.filter(function(e){ return e.t === "partie" && e.act === A && verifiable(e); });
  return !vs.length ? "ecrit" : vs.every(function(e){ return M.fait[e.id]; }) ? "verifiee" : "a-faire";
}
function ouvrirCorrections(s, A){
  var cs = corrections(s); if (!cs.length) return;
  var et = etatActivite(A), ok = et !== "a-faire";
  if (ok) cs.forEach(function(c){ if (!c._msOuverte){ c.open = true; c._msOuverte = true; } });
  var note = s._msCorNote;
  if (!note){ note = s._msCorNote = el("p", "ms-cor-note ms-seul"); cs[0].parentNode.insertBefore(note, cs[0]); s.n.push(note); ecrans.tous.push(note); }
  note.textContent = et === "verifiee" ? "✅ Ta correction est ouverte juste en dessous : compare-la avec tes réponses, une par une."
                   : et === "ecrit" ? "✅ Ta correction est ouverte juste en dessous : compare-la avec ce que tu as écrit, ligne par ligne."
                   : "🔎 La correction est juste en dessous. Réponds d'abord aux questions et vérifie : elle s'ouvrira toute seule.";
}

/* ═══ Montrer un écran : tout ce qui n'en fait pas partie se cache (à l'écran seulement) ═══ */
function vide(s){ return (s.t === "carte" || s.t === "retenir") && s.n.every(function(n){ return !n.offsetParent || (!net(n.innerText) && !$("img,svg,canvas,video,iframe,object,input,textarea,select", n)); }); }
function montrer(haut){
  var s = ecrans[k], vis = [];
  if (s.t === "retenir" && s.act) ouvrirCorrections(s, s.act);
  s.n.forEach(function(n){ vis.push(n); for (var p = n.parentNode; p && p !== panneau && panneau.contains(p); p = p.parentNode) vis.push(p); });
  if (s.t === "partie" && s.ress.length && ressVue()) s.ress.forEach(function(n){ vis.push(n); for (var p = n.parentNode; p && p !== panneau && panneau.contains(p); p = p.parentNode) vis.push(p); });
  ecrans.tous.forEach(function(n){ n.classList.toggle("ms-cache", vis.indexOf(n) < 0); });
  horsPanneaux().forEach(function(n){ if (ecrans.tous.indexOf(n) < 0) n.classList.add("ms-cache"); });      // la clôture rangée après les panneaux : au dernier seulement
  var ouv = $("#ouverture"); if (ouv) ouv.classList.toggle("ms-cache", !s.ouverture);
  /* « l'éditeur Python est intégré à l'activité » ne se dit que là où on le voit : sur les écrans de prédiction,
     qui viennent avant lui, l'annonce se tait (17/11/2026) */
  var edIci = s.n.some(function(n){ return n.matches && (n.matches(".editeur-py") || !!$(".editeur-py", n)); });
  $$(".activite-en-ligne", panneau).forEach(function(b){
    var A = b.closest(".activite, .act, .card, .carte, section"); if (!A || !$(".editeur-py", A)) return;
    b.classList.toggle("ms-sans-outil", !edIci);
  });
  if (s.ressBtn) s.ressBtn.textContent = ressVue() ? "📎 Masquer la ressource de l'activité" : "📎 Revoir la ressource de l'activité";
  $$(".ms-etq", panneau).forEach(peindre); peindreRetour(s); bilan(s); marquerTrou(s);
  if (ecrans.length > 1 && vide(s)){ ecrans.splice(k, 1); k = Math.min(k, ecrans.length - 1); return montrer(haut); }
  if (!G.onglet){ var bout = k === ecrans.length - 1 && !voisine(1); $$(".page-suivante").forEach(function(x){ x.classList.toggle("ms-montre", bout && !x.closest(G.panneau)); }); }
  M.loin[panneau.id] = Math.max(M.loin[panneau.id] || 0, k);
  barre(); M.k[panneau.id] = k; ecrire(); niveaux();
  /* l'écran qui ouvre la séquence commence par son ouverture dépliée — « 🎯 Avant de commencer : trois choses à lire »
     (n°337), la situation, la problématique — et non par la tête de la mission, plus bas : l'élève lit avant de faire
     (17/11/2026 ; avant, ce premier écran défilait de 3 000 à 5 500 px au-delà de l'ouverture). Repliée (« 📖 Rappel »,
     dès la séance 2), l'ouverture ne tient qu'une ligne : l'écran commence à la tête de la mission, comme avant.
     Une page sans volet d'ouverture (les pages engendrées de 3e_C9.2) : la carte seule, à la première séance de la page. */
  var ouvr = $("#ouverture"), carte = $("#trois-lignes"), premier = panneau === $(G.panneau);
  var debut = (ouvr && ouvr.open && ouvr.offsetParent) ? ouvr : (!ouvr && premier && carte && carte.offsetParent) ? carte : null;
  var cible = (s.ouverture && debut) ? debut : ancre;
  if (haut){ var y = Math.max(0, cible.getBoundingClientRect().top + window.scrollY - 52); try { window.scrollTo({ top:y, behavior:"instant" }); } catch (e) { window.scrollTo(0, y); } }
}
/* Les titres d'un écran se lisent sans sauter de niveau (audit du jardin connecté, 19/11/2026) : le titre d'écran est
   de niveau 2 ; un titre de l'écran ne descend que d'un niveau à la fois — « a) » (h4) sous le titre de l'activité (h2)
   s'annonce au niveau 3. Seul le niveau annoncé change (aria-level), pas la balise ; il revient en quittant la mission. */
function niveaux(){
  $$("[data-ms-niveau]").forEach(function(h){ h.removeAttribute("aria-level"); h.removeAttribute("data-ms-niveau"); });
  if (!actif || !panneau) return;
  var avant = 2;
  $$("h2,h3,h4,h5,h6", panneau).forEach(function(h){
    if (!h.getClientRects().length) return;
    var n = +h.tagName.charAt(1), v = Math.min(n, avant + 1);
    if (v !== n && !h.hasAttribute("aria-level")){ h.setAttribute("aria-level", String(v)); h.setAttribute("data-ms-niveau", ""); }
    avant = v;
  });
}
D.addEventListener("toggle", function(){ if (actif) niveaux(); }, true);
function aller(j){
  if (j < 0){ var av = voisine(-1); if (av){ M.k[av] = 1e9; ouvrir(av); } return; }
  if (j >= ecrans.length) return;
  k = j; sel = null; reprendre(); montrer(true);
}
function suivant(){
  if (k < ecrans.length - 1) return aller(k + 1);
  var apres = voisine(1); if (apres){ M.loin[panneau.id] = ecrans.length; M.k[apres] = 0; ouvrir(apres); }
}
function synchroniser(){
  panneau = panneauActif(); if (!panneau) return;
  ecrans = parPanneau[panneau.id] || (parPanneau[panneau.id] = construire(panneau));
  k = Math.min(Math.max(0, M.k[panneau.id] || 0), ecrans.length - 1);
  montrer(true);
}

/* ═══ Vérifier une partie : les réponses justes restent ; une étiquette fausse retourne dans la réserve ═══
   Contre le tâtonnement (essayer jusqu'à ce que ça passe, sans lire) :
   · les erreurs se comptent réponse par réponse, pas par appui sur « Vérifier » : ce sont elles qui font les étoiles ;
   · après une erreur, « Vérifier » souffle deux secondes — le temps de relire ;
   · au deuxième essai manqué sur le même écran, le coup de pouce de l'activité s'ouvre ; au quatrième, le second. */
var souffle = 0, minuterie = null;
function reprendre(){ souffle = 0; if (minuterie){ clearTimeout(minuterie); minuterie = null; } var b = $("#msVerif"); if (b){ b.removeAttribute("aria-disabled"); b.textContent = "Vérifier"; } }
function souffler(){ var b = $("#msVerif"); souffle = Date.now() + 2000; b.setAttribute("aria-disabled", "true"); b.textContent = "Relis d'abord…"; if (minuterie) clearTimeout(minuterie); minuterie = setTimeout(reprendre, 2000); }
function coupDePouce(s, niveau){
  var a = s.n.filter(function(c){ return c.matches && c.matches("details.aide1,details.aide2,details.aide"); }), d = a[Math.min(niveau, a.length) - 1];
  if (!d) return " Relis la consigne, puis réessaie.";
  var deja = d.open; d.open = true; d.classList.add("ms-pousse");
  return deja ? " Relis le coup de pouce ouvert juste en dessous, puis réessaie." : " Un coup de pouce vient de s'ouvrir juste en dessous : lis-le, puis réessaie.";
}
function dire(s, ton, html, n, liste, fin){ s.msg = html ? { ton:ton, html:html, n:n, liste:liste || [], fin:fin || "" } : null; peindreRetour(s); if (html && s.retour.scrollIntoView) s.retour.scrollIntoView({ block:"nearest" }); }
function peindreRetour(s){
  if (!s.retour) return; var m = s.msg; s.retour.className = "ms-retour ms-seul" + (m && m.ton ? " " + m.ton : "");
  s.retour.innerHTML = m ? (m.n ? etoiles(m.n) : "") + '<div class="ms-retour-t"><p>' + m.html + "</p>" + (m.liste && m.liste.length ? '<ul class="ms-pq">' + m.liste.map(function(x){ return "<li>" + x + "</li>"; }).join("") + "</ul>" : "") + (m.fin ? "<p>" + m.fin + "</p>" : "") + "</div>" : "";
}
/* Le pourquoi d'une erreur, écrit dans la page : `data-pourquoi` sur la proposition choisie (pourquoi elle ne convient
   pas), sinon `data-indice` sur la question (ce qu'elle demande). Jamais la bonne réponse. */
function raison(f, seule){
  var r = f.tagName === "SELECT" ? f.selectedOptions[0] : $("input[type=radio]:checked", f), pq = (r && r.getAttribute("data-pourquoi")) || f.getAttribute("data-indice");
  if (!pq){ var pn = G.kit ? parNom()[nomDe(f)] : null; pq = pn ? (pn.retours[lireV(f)] || pn.indice) : ""; }          // le pourquoi d'un atelier : dans ses données
  if (!pq) return "";
  if (f.classList.contains("ms-origine")) return "<b>« " + esc(lireV(f)) + " »</b> ne va pas avec « " + esc(intitule(f)) + " ». " + esc(pq);
  var t = intitule(f);          // l'intitulé de la question, puis son pourquoi : deux phrases, pas une seule
  return seule ? esc(pq) : "<b>" + esc(t) + (/[?!.»]$/.test(t) ? "" : "\u00a0:") + "</b> " + esc(pq);
}
function marquer(f, ok){
  f.classList.toggle("ms-juste", ok === true); f.classList.toggle("ms-faux", ok === false);
  if (f.tagName !== "SELECT") return;
  var m = f._msMarque; if (!m){ m = f._msMarque = el("span", "ms-marque ms-seul"); m.setAttribute("aria-live", "polite"); f.parentNode.insertBefore(m, f.nextSibling); }
  m.textContent = ok === true ? "✓ juste" : ok === false ? "✗ à revoir" : ""; m.className = "ms-marque ms-seul" + (ok === true ? " juste" : ok === false ? " faux" : "");
}
function verifier(){
  var s = ecrans[k]; if (s.t !== "partie" || Date.now() < souffle) return;
  var avec = s.champs.filter(function(f){ return cle(f) !== undefined; }), vides = avec.filter(function(f){ return !lireV(f); }).length;
  if (vides){ dire(s, "", "Il reste " + vides + " question" + (vides > 1 ? "s" : "") + " sans réponse. Réponds à tout avant de vérifier."); return; }
  var gain = 0;
  if (avec.length){
    var fautes = avec.filter(function(f){ return lireV(f) !== cle(f); });
    avec.forEach(function(f){ marquer(f, lireV(f) === cle(f)); });
    if (fautes.length){
      M.essais[s.id] = (M.essais[s.id] || 0) + 1; M.erreurs[s.id] = (M.erreurs[s.id] || 0) + fautes.length; ecrire();
      var justes = avec.length - fautes.length, enEtq = fautes.filter(function(f){ return f.classList.contains("ms-origine"); }), essais = M.essais[s.id];
      var seule = avec.length === 1, raisons = fautes.map(function(f){ return raison(f, seule); }).filter(Boolean);
      var debut = seule || !justes ? "Pas encore." : "Pas encore. " + justes + " réponse" + (justes > 1 ? "s justes restent" : " juste reste") + " en place.";
      debut += enEtq.length ? " " + enEtq.length + " étiquette" + (enEtq.length > 1 ? "s retournent" : " retourne") + " dans la réserve." : "";
      var suite = essais >= 2 ? coupDePouce(s, essais >= 4 ? 2 : 1).trim() : raisons.length ? "Corrige, puis vérifie de nouveau." : "Relis la consigne, puis réessaie.";
      if (seule && raisons.length) dire(s, "encore", debut + " " + raisons[0], 0, [], suite); else dire(s, "encore", debut, 0, raisons, suite);
      souffler();
      $$(".ms-etq", panneau).forEach(peindre);
      setTimeout(function(){ enEtq.forEach(function(f){ if (f.classList.contains("ms-faux")){ ecrireV(f, null); f.classList.remove("ms-faux"); saisie(f); } }); if (actif) $$(".ms-etq", panneau).forEach(peindre); }, 950);
      return;
    }
    /* 3 étoiles : aucune erreur · 2 : une erreur (deux sur un jeu de trois réponses ou plus) · 1 : au-delà.
       Ouvrir une aide ne retire rien. */
    var err = M.erreurs[s.id] || 0, n = !err ? 3 : err <= (avec.length >= 3 ? 2 : 1) ? 2 : 1, avant = M.etoiles[s.id] || 0;
    M.etoiles[s.id] = Math.max(avant, n); gain = M.etoiles[s.id] - avant;
    /* la règle des étoiles se dit au moment où elles tombent (audit du jardin connecté, 19/11/2026) */
    dire(s, "ok", n === 3 ? "Tout est juste, du premier coup : 3 étoiles sur 3." : "Tout est juste. Tu as corrigé tes erreurs : c'est comme ça qu'on apprend. " + (n === 2 ? "2 étoiles sur 3" : "1 étoile sur 3") + " : " + (err === 1 ? "une erreur" : err + " erreurs") + " en route.", n);
  } else dire(s, "", "C'est noté. Lis le message de la vérification ci-dessous.");
  M.fait[s.id] = true; ecrire();
  if (s.dernier && s.check){          // la vérification de la page : c'est elle qui valide l'activité — son message se lit au-dessus de la barre
    boutonDe(s.check).click();
    if (s.fb && net(s.fb.textContent) && s.fb.scrollIntoView){ s.fb.classList.add("ms-message"); s.fb.scrollIntoView({ block:"nearest" }); }
  }
  if (s.act) ouvrirCorrections(s, s.act);          // une correction posée sous la question s'ouvre aussi (n°336)
  $$(".ms-etq", panneau).forEach(peindre); barre();
  if (gain){ var b = el("span", "ms-gain"); b.textContent = "+" + gain; $("#msGains").appendChild(b); setTimeout(function(){ b.remove(); }, 1600); }
  $("#msSuiv").focus({ preventScroll:true });
}

/* Au bilan de la séquence : les étoiles gagnées, au-dessus de l'auto-positionnement — qui reste le choix de l'élève */
/* la séance qui porte la première question pas encore réussie, nommée comme son onglet ; "" si on ne sait pas la nommer */
function premiereAFaire(){
  var ids = Object.keys(parPanneau);
  for (var i = 0; i < ids.length; i++){
    if (!parties(ids[i]).some(function(e){ return !M.fait[e.id]; })) continue;
    var o = G.onglet ? $$(G.onglet).filter(function(x){ return G.de(x) === ids[i]; })[0] : null, m = /^seance-(\d+)$/.exec(ids[i]);
    return o ? nomOnglet(o) : m ? "Séance " + m[1] : "";
  }
  return "";
}
/* La carte du bilan de la séquence. Le mode la reconnaissait à son identifiant (« bilan ») ou à son positionnement
   (`#je-me-positionne`, `fieldset.positionnement`) : 22 séquences sur 56 n'ont ni l'un ni l'autre, et n'avaient donc
   jamais de « Ta mission : … » (relevé du 20/11/2026). À défaut de ces marques, c'est la DERNIÈRE carte dont le titre
   dit « bilan » (« 🪞 Mon bilan personnel », « 🏁 Bilan de la séquence ») : une seule par page. */
var _bilanParTitre;
function bilanParTitre(){
  if (_bilanParTitre !== undefined) return _bilanParTitre;
  var marque = false, c = null;
  Object.keys(parPanneau).forEach(function(id){ parPanneau[id].forEach(function(e){
    var n = e.t === "carte" ? e.n[0] : null; if (!n || n.nodeType !== 1 || n.matches("h2,h3,h4")) return;
    if (n.id === "bilan" || $("#je-me-positionne, fieldset.positionnement", n)) marque = true;
    else if (/\bbilan\b/i.test(e.titre || "") && $("h2,h3", n)) c = n;
  }); });
  return (_bilanParTitre = marque ? null : c);
}
function bilan(s){
  if ((s.t !== "carte" && s.t !== "intro") || !s.n[0] || s.n[0].nodeType !== 1) return;
  /* la carte que montre l'écran : le nœud lui-même ; ou, quand la carte du bilan porte une activité (« Où en es-tu ? » de
     4e_C6.2), le parent de son titre — l'écran n'en montre alors que le début, et il est de type « intro » */
  var titre = s.n[0].matches("h2,h3,h4"), C = titre ? s.n[0].parentNode : s.n[0];
  if (s.t === "intro" ? !(titre && C.id === "bilan") : !(C.id === "bilan" || $("#je-me-positionne, fieldset.positionnement", C) || C === bilanParTitre())) return;
  var b = s._msBilan || $(".ms-bilan", C);
  if (!b){
    b = el("div", "ms-bilan ms-seul");
    if (titre){ C.insertBefore(b, s.n[0].nextSibling); s.n.push(b); ecrans.tous.push(b); }          // il suit l'écran de son titre, pas ceux des activités de la carte
    else { var h = $("h2,h3", C); if (h) h.parentNode.insertBefore(b, h.nextSibling); else C.insertBefore(b, C.firstChild); }
  }
  s._msBilan = b;
  /* « Ton positionnement, ci-dessous » ne se dit que si la carte en porte un (des choix à cocher, ou le mot lui-même) */
  var positionne = !!$("#je-me-positionne, fieldset.positionnement, input[type=radio], select", C) || /positionn/i.test(C.textContent);
  var ps = parties(), gagne = ps.reduce(function(a, e){ return a + (M.etoiles[e.id] || 0); }, 0), faites = ps.filter(function(e){ return M.fait[e.id]; }).length;
  var corrigees = ps.reduce(function(a, e){ return a + (M.fait[e.id] ? (M.erreurs[e.id] || 0) : 0); }, 0);
  /* Tant qu'il reste des questions, le bilan le dit et nomme la séance où reprendre (audit du jardin de 4e, 20/11/2026 :
     après une seule question réussie, l'élève lisait au bilan un texte de fin de séquence et pouvait se croire arrivé). */
  var reste = ps.length - faites, ou = reste ? premiereAFaire() : "";
  b.innerHTML = "<p><b>Ta mission : " + gagne + " étoile" + (gagne > 1 ? "s" : "") + " sur " + (ps.length * 3) + "</b> — " + faites + " question" + (faites > 1 ? "s" : "") + " réussie" + (faites > 1 ? "s" : "") + " sur " + ps.length + ".</p>" + (reste ? '<p class="ms-reste">⏳ <b>Ta mission n\'est pas finie</b> : il te reste ' + reste + " question" + (reste > 1 ? "s" : "") + (ou ? ". La prochaine t'attend ici : " + esc(ou) : "") + ".</p>" : "") + (corrigees ? "<p>En route, tu as corrigé " + corrigees + " erreur" + (corrigees > 1 ? "s" : "") + " : c'est comme ça qu'on apprend.</p>" : "") + "<p>Trois étoiles : juste du premier coup." + (positionne ? " Ton positionnement, ci-dessous, c'est toi qui le choisis." : "") + "</p>";
}

/* ═══ Entrer, sortir ═══ */
function entrer(){
  if (!construit){
    $$(G.panneau).forEach(function(P){ parPanneau[P.id] = construire(P); });
    Object.keys(parPanneau).forEach(function(id){ parPanneau[id].forEach(function(e){            // ce qui était réussi le reste
      if (e.t === "partie" && M.fait[e.id]) e.champs.forEach(function(f){ if (cle(f) !== undefined && lireV(f) === cle(f)) marquer(f, true); }); }); });
    construit = true;
  }
  /* ce qui a été réussi en page complète (toutes les réponses justes, ou la vérification de la page passée) compte comme
     fait : l'élève qui sort du mode, travaille dans la page puis revient retrouve sa barre allumée. Lu à l'entrée
     seulement, jamais pendant la mission : la barre ne dit pas si une réponse en cours est juste. */
  Object.keys(parPanneau).forEach(function(id){ parPanneau[id].forEach(function(e){
    if (e.t !== "partie" || M.fait[e.id]) return;
    var avec = e.champs.filter(function(f){ return cle(f) !== undefined; });
    if (avec.length ? avec.every(function(f){ return lireV(f) === cle(f); }) : (e.dernier && e.fb && /(^|\s)ok(\s|$)/.test(e.fb.className))) M.fait[e.id] = true;
  }); });
  actif = true; M.on = true; D.body.classList.add("ms"); voirRevenir(); caler();
  if (!G.onglet && !panneauActif()) ((M.ici && $(G.panneau + '[id="' + M.ici + '"]')) || $(G.panneau)).classList.add(G.actif);
  synchroniser();
}
function sortir(){
  actif = false; M.on = false; ecrire(); D.body.classList.remove("ms"); voirRevenir();
  niveaux();
  var ouv = $("#ouverture"); if (ouv) ouv.classList.remove("ms-cache");
  bMission.focus({ preventScroll:true }); bMission.scrollIntoView({ block:"center" });
}

/* ═══ Les gestes sur les étiquettes : toucher, glisser, clavier ═══ */
function sousPointeur(ev){ var x = D.elementFromPoint(ev.clientX, ev.clientY); return x && x.closest(".ms-case:not(:disabled)"); }
D.addEventListener("click", function(ev){
  if (!actif) return;
  /* une séquence découpée en pages : qui passe à la page suivante en mission y arrive en mission */
  if (ev.target.closest(".page-suivante a[href], a.seance-tab[href]")){ try { sessionStorage.setItem("mission:suite", "1"); } catch (e) {} return; }
  var r = ev.target.closest("[data-ms=ress]"); if (r){ M.ress = !ressVue(); montrer(false); return; }
  if (glisse) return;
  var lab = ev.target.closest(".ms-lab"); if (lab){ var comp = lab.closest(".ms-etq"), j = +lab.dataset.j; sel = (sel && sel.comp === comp && sel.j === j) ? null : { comp:comp, j:j }; peindre(comp); return; }
  var c = ev.target.closest(".ms-case"); if (c && !c.disabled){ var co = c.closest(".ms-etq"), i = +c.dataset.i;
    if (sel && sel.comp === co){ poser(co, i, co._libs[sel.j]); sel = null; } else if (lireV(co._sets[i])) poser(co, i, null);
    else { var s = ecrans[k]; if (s.retour) dire(s, "", "Choisis d'abord une étiquette dans la réserve, puis touche cette case."); }
    peindre(co); }
});
D.addEventListener("input", function(){ if (actif && ecrans[k] && ecrans[k].t === "partie") barre(); });
D.addEventListener("change", function(ev){      // une réponse changée à la main n'est plus ni juste ni fausse : elle se revérifie
  if (!actif || !ev.isTrusted) return; var f = ev.target.closest && ev.target.closest(CHAMP);
  if (f && !f.classList.contains("ms-origine")) marquer(f, null); });
D.addEventListener("pointerdown", function(ev){
  if (!actif) return; var src = ev.target.closest(".ms-lab, .ms-case.pleine"); if (!src || src.disabled) return;
  if (ev.pointerType === "touch" && src.classList.contains("ms-case")) return;      // au doigt : toucher la case rend l'étiquette ; glisser fait défiler la page
  var comp = src.closest(".ms-etq"), depuis = src.dataset.i !== undefined ? +src.dataset.i : null;
  g = { x:ev.clientX, y:ev.clientY, id:ev.pointerId, src:src, comp:comp, depuis:depuis, val: depuis !== null ? lireV(comp._sets[depuis]) : comp._libs[+src.dataset.j], f:null };
});
window.addEventListener("pointermove", function(ev){
  if (!g || ev.pointerId !== g.id) return;
  if (!g.f){ if (Math.hypot(ev.clientX - g.x, ev.clientY - g.y) < 8) return; g.f = el("div", "ms-fantome"); g.f.textContent = g.val; D.body.appendChild(g.f); g.src.classList.add("part"); }
  g.f.style.transform = "translate(" + ev.clientX + "px," + ev.clientY + "px) translate(-50%,-65%) rotate(-2deg)";
  $$(".ms-case.vise").forEach(function(x){ x.classList.remove("vise"); });
  var c = sousPointeur(ev); if (c && c.closest(".ms-etq") === g.comp) c.classList.add("vise");
});
function lache(ev, annule){
  if (!g || ev.pointerId !== g.id) return; var d = g; g = null; if (!d.f) return;
  d.f.remove(); glisse = true; setTimeout(function(){ glisse = false; }, 0);
  var c = annule ? null : sousPointeur(ev);
  if (c && c.closest(".ms-etq") === d.comp){ var i = +c.dataset.i; if (d.depuis !== null && d.depuis !== i) poser(d.comp, d.depuis, null); poser(d.comp, i, d.val); }
  else if (d.depuis !== null && !annule) poser(d.comp, d.depuis, null);
  sel = null; peindre(d.comp);
}
window.addEventListener("pointerup", function(ev){ lache(ev, false); });
window.addEventListener("pointercancel", function(ev){ lache(ev, true); });

/* pour les bancs : la réponse que le mode retient pour un groupe, et l'écran en cours */
D.documentElement._mission = { cle: cle, gabarit: function(){ return G ? { P:G.panneau, T:G.onglet, A:G.actif || null, de:G.attr || null, actif:selActif(), page:!!G.page, kit:!!G.kit } : null; }, ecran: function(){ var s = ecrans[k]; return s ? { t:s.t, id:s.id || "", dernier:!!s.dernier, check:!!s.check, fb:s.fb ? s.fb.id || "" : null } : null; } };
function init(){
  G = gabarit(); if (!G) return;                                    // gabarit non reconnu : la page reste telle quelle
  if (G.kit) CHECK = CHECK_BASE + ", [data-exo] button.verifier";
  /* un groupe de boutons radio sans identifiant (ateliers) en reçoit un, tiré du nom de ses boutons : c'est par lui
     que les bancs désignent une question. Rien d'autre ne le lit. */
  if (G.kit) $$(G.panneau).forEach(function(P){ $$("fieldset.qcm-groupe:not([id])", P).forEach(function(f){ var nm = nomDe(f); if (nm && !D.getElementById("ms-q-" + nm)) f.id = "ms-q-" + nm; }); });
  garde = !!$(SIEN);
  lire();
  /* « Effacer ma sauvegarde » efface aussi la mission : sur un poste partagé, l'élève suivant ne trouve ni les
     étoiles ni l'écran du précédent. La page efface sa clé puis se recharge ; on le voit ici à sa clé absente. */
  /* « Effacer ma sauvegarde » : la page retire sa clé (ou vide tout) puis se recharge. Certaines pages réécrivent leur clé
     dès le chargement, avant ce script : le geste d'effacer est donc repéré au moment où il a lieu (marque de session). */
  var efface = false; try { efface = sessionStorage.getItem("mission:efface") === "1"; sessionStorage.removeItem("mission:efface"); } catch (e) {}
  try { if (efface || (typeof KEY === "string" && localStorage.getItem(KEY) === null && (M.vu || Object.keys(M.etoiles).length || Object.keys(M.fait).length || Object.keys(M.k).length || Object.keys(M.erreurs).length))){ M = { v:1, on:((efface || M.vu) ? DEFAUT : M.on), k:{}, essais:{}, erreurs:{}, etoiles:{}, fait:{}, loin:{} }; ecrire(); } } catch (e) {}
  chrome();
  /* la séance change (onglet, bouton « séance suivante », lien vers une ancre) : le mode suit le panneau ouvert */
  function suivre(){ if (actif && panneauActif() !== panneau) synchroniser(); }
  if (G.onglet) $$(G.onglet).forEach(function(o){ o.addEventListener("click", function(){ setTimeout(suivre, 0); }); });
  if (window.MutationObserver){ var obs = new MutationObserver(suivre); $$(G.panneau).forEach(function(P){ obs.observe(P, { attributes:true, attributeFilter:["class", "hidden"] }); }); }
  /* un lien de la page vers une ancre que le mode cache (un sommaire, « voir l'étape 3 ») mène à son écran */
  D.addEventListener("click", function(ev){
    if (!actif || !ev.target.closest) return;
    var a = ev.target.closest('a[href^="#"]'); if (!a || a.getAttribute("href").length < 2) return;
    var but = null; try { but = D.getElementById(decodeURIComponent(a.getAttribute("href").slice(1))); } catch (e) {}
    if (!but || !panneau || !panneau.contains(but) || but.getClientRects().length) return;
    for (var j = 0; j < ecrans.length; j++){
      if (ecrans[j].n.some(function(n){ return n === but || (n.contains && n.contains(but)) || (but.contains && but.contains(n)); })){ ev.preventDefault(); aller(j); try { but.scrollIntoView({ block:"start" }); } catch (e) {} return; }
    }
  });
  var suite = false; try { suite = sessionStorage.getItem("mission:suite") === "1"; sessionStorage.removeItem("mission:suite"); } catch (e) {}
  if (M.on || suite) entrer();
}
if (D.readyState === "loading") D.addEventListener("DOMContentLoaded", init); else init();
})();
