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
function lire(){ try { M = JSON.parse(localStorage.getItem(CLE) || "null"); } catch (e) { M = null; } if (!M || M.v !== 1) M = { v:1, on:false, k:{}, essais:{}, etoiles:{}, fait:{} }; if (!M.erreurs) M.erreurs = {}; }
function ecrire(){ try { localStorage.setItem(CLE, JSON.stringify(M)); } catch (e) {} }
function etoiles(n){ var s = ""; for (var i = 1; i <= 3; i++) s += ET.replace("{on}", i <= n ? " on" : ""); return '<span class="ms-etoiles" role="img" aria-label="' + n + " étoile" + (n > 1 ? "s" : "") + ' sur 3">' + s + "</span>"; }
/* prévenir la page qu'une réponse a changé, comme le ferait un appui : l'événement part du bouton radio coché (c'est
   lui que certaines pages écoutent pour sauvegarder), ou du groupe quand plus rien n'est coché */
function saisie(f){ var x = (f.tagName === "FIELDSET" && $("input[type=radio]:checked", f)) || f; x.dispatchEvent(new Event("input", { bubbles:true })); x.dispatchEvent(new Event("change", { bubbles:true })); }

/* Les séances : des panneaux. Trois écritures dans le dépôt :
     gabarit commun   .seance-tab[data-panel]     →  .seance-panel.active      cartes : section.card
     Book Train       [role=tab][aria-controls]   →  section.panneau.actif     cartes : div.carte
     page sans onglets (une grande étape d'une séquence découpée) : des `.seance-bloc` à la suite, tous visibles —
       ici c'est le mode qui n'en montre qu'un à la fois (`.ms-ici`), et qui mène de l'un à l'autre */
var G = null, CARTE = "section.card, div.carte";
function gabarit(){
  if ($(".seance-panel") && $(".seance-tab")) return { panneau:".seance-panel", onglet:".seance-tab", actif:"active", de:function(o){ return o.dataset.panel; } };
  if ($("section.panneau[role=tabpanel]") && $("[role=tablist] [role=tab][aria-controls]")) return { panneau:"section.panneau[role=tabpanel]", onglet:"[role=tablist] [role=tab][aria-controls]", actif:"actif", de:function(o){ return o.getAttribute("aria-controls"); } };
  if ($(".seance-bloc[id]")) return { panneau:".seance-bloc[id]", onglet:null, actif:"ms-ici" };
  return null;
}
function panneauActif(){ return $(G.panneau + "." + G.actif); }
function ongletActif(){ var P = panneauActif(); return P && G.onglet ? $$(G.onglet).filter(function(o){ return G.de(o) === P.id; })[0] || null : null; }
function nomOnglet(o){ for (var i = 0; i < o.childNodes.length; i++){ var n = o.childNodes[i]; if (n.nodeName !== "SMALL" && net(n.textContent)) return net(n.textContent); } return net(o.textContent); }
function nomSeance(){ var o = ongletActif(); if (o) return nomOnglet(o); var m = panneau && /^seance-(\d+)$/.exec(panneau.id); return m ? "Séance " + m[1] : ""; }
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
var CHECK = "button[data-check], button.verif[data-exo]";
function estCheck(c){ return c.matches(CHECK); }
function estMessage(c){ return c.classList.contains("feedback") || (!!c.id && c.id.indexOf("res-") === 0 && !!$('button.verif[data-exo="' + c.id.slice(4) + '"]')); }
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
  function designee(c){ return !!c.id && kids.some(function(b){ return estCheck(b) && b.getAttribute("data-exo") === c.id; }); }
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
  var tete = avant.filter(function(c){ return header.indexOf(c) >= 0 || c.classList.contains("meta-grid") || c.classList.contains("pastille-maison") || c.classList.contains("competence-visee"); });
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
      if (estCheck(c)){ var de = c.getAttribute("data-exo"), zc = zones.filter(function(z){ return !z.check && (!de || z.exo.id === de); }).pop(); if (zc){ zc.check = c; zc.dehors = true; return; } }
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
  var ressBtn = null;
  if (ress.length){ ressBtn = el("button", "ms-ressbtn ms-seul"); ressBtn.type = "button"; ressBtn.setAttribute("data-ms", "ress"); A.insertBefore(ressBtn, ress[0].parentNode === A ? ress[0] : kids[i]); }
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
    tous.forEach(function(x, r){
      var dernier = r === tous.length - 1, base = x.p.h ? net(x.p.h.textContent) : "À toi de jouer";
      E.push({ t:"partie", titre: base + (x.sur > 1 ? " · " + (x.q + 1) + " sur " + x.sur : ""), act:A, ress:ress, ressBtn:ressBtn, retour:retour, champs:x.st.champs, dernier:dernier, check:z.check, fb:z.fb[0],
               id:(A.id || nom) + "#" + x.j + "." + x.q, n:(ressBtn ? [ressBtn] : []).concat(carte ? header : [], x.st.n, [retour], dernier ? z.fb.concat(z.suite) : [], aides) });
    });
  });
  if (fin.length) E.push({ t:"retenir", titre:"Je retiens — " + nom, n:header.concat(fin) });
}
/* Une partie se joue pas à pas : chaque question à choix sur son écran, chaque jeu d'étiquettes sur le sien, une
   série de réponses courtes (rangée) ensemble, un écrit (zone de texte et sa version étayée) sur le sien.
   Ce qui précède une question sans rien demander (un simulateur, un tableau) l'accompagne. */
function champsDe(c){ return estChamp(c) ? [c] : $$(CHAMP, c); }
function courte(f){ return f.classList.contains("qcm-rangee") || f.classList.contains("qcm-court"); }
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
function construire(P){
  var E = [];
  enfants(P).forEach(function(C){
    if (C.classList.contains("page-suivante") || !rendu(C)) return;          // ce que la page cache d'elle-même (fiche professeur) ne fait pas d'écran
    if (estActivite(C)){ activite(C, E); return; }
    var acts = enfants(C).filter(estActivite);
    if (!acts.length){ E.push({ t:"carte", titre:titreDe(C) || "Suite", n:[C] }); return; }
    var avant = [], vu = false, suite = [];
    function vider(){ if (suite.length){ var t = ""; suite.forEach(function(x){ t = t || titreDe(x); }); E.push({ t:"carte", titre:t || "À lire", n:suite }); suite = []; } }
    enfants(C).forEach(function(x){
      if (estActivite(x)){ if (!vu){ vu = true; E.push({ t:"intro", titre:titreDe(C) || "La séance", n:avant, ouverture:true }); } vider(); activite(x, E); }
      else if (!vu) avant.push(x); else if (rendu(x)) suite.push(x);
    });
    vider();
  });
  if (E.length && !E.some(function(e){ return e.ouverture; })) E[0].ouverture = true;       // la situation de départ s'ouvre au premier écran
  /* tous les blocs qui se montrent ou se cachent : ceux des écrans, et leurs conteneurs jusqu'au panneau */
  E.tous = [];
  E.forEach(function(e){ e.n.concat(e.ress || []).forEach(function(n){ for (var p = n; p && p !== P; p = p.parentNode) if (E.tous.indexOf(p) < 0) E.tous.push(p); }); });
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
var tete, pied, bMission, ancre;
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
  tete = el("div", "ms-tete ms-seul", '<div class="ms-ligne1"><p class="ms-ou" id="msOu"></p><button type="button" class="ms-quitter" id="msQuitter">📄 Page complète</button><div class="ms-gains" id="msGains"><span class="ms-jauge" aria-hidden="true"><i id="msJauge"></i></span>' + ET.replace("{on}", " on") + '<span id="msCompte"></span></div></div><nav aria-label="Écrans de la séance"><ol class="ms-rail" id="msRail"></ol></nav>');
  /* un repère sans hauteur juste avant la barre : collée en haut de l'écran, la barre ne dit plus où elle commence */
  var premier = $(G.panneau); ancre = el("div", "ms-ancre ms-seul"); premier.parentNode.insertBefore(ancre, premier); premier.parentNode.insertBefore(tete, premier);
  pied = el("div", "ms-pied ms-seul", '<div class="ms-pied-in"><button type="button" class="ms-btn ms-prec" id="msPrec" aria-label="Écran précédent">← <span>Précédent</span></button><button type="button" class="ms-btn ms-verif" id="msVerif">Vérifier</button><span class="ms-vide-f" id="msVide" hidden></span><button type="button" class="ms-btn ms-suiv" id="msSuiv">Suivant →</button></div>');
  D.body.appendChild(pied);
  $("#msQuitter").addEventListener("click", sortir);
  $("#msPrec").addEventListener("click", function(){ aller(k - 1); });
  $("#msSuiv").addEventListener("click", suivant);
  $("#msVerif").addEventListener("click", verifier);
  $("#msRail").addEventListener("click", function(ev){ var b = ev.target.closest("[data-k]"); if (b) aller(+b.dataset.k); });
}
function parties(seul){ var t = []; Object.keys(parPanneau).forEach(function(id){ if (seul && id !== seul) return; parPanneau[id].forEach(function(e){ if (e.t === "partie" && e.champs.some(function(f){ return cle(f) !== undefined; })) t.push(e); }); }); return t; }
function barre(){
  var s = ecrans[k];
  $("#msOu").innerHTML = esc(s.titre) + "<small>" + esc(nomSeance()) + " · écran " + (k + 1) + " sur " + ecrans.length + "</small>";
  var ps = parties(panneau && panneau.id), gagne = ps.reduce(function(a, e){ return a + (M.etoiles[e.id] || 0); }, 0), max = ps.length * 3;
  $("#msCompte").textContent = gagne + " / " + max; $("#msJauge").style.width = (max ? Math.round(100 * gagne / max) : 0) + "%";
  $("#msGains").setAttribute("aria-label", gagne + " étoiles gagnées sur " + max + " dans cette séance");
  $("#msRail").innerHTML = ecrans.map(function(e, j){ var fait = e.t === "partie" ? !!M.fait[e.id] : j < k; return '<li><button type="button" class="ms-pas' + (fait ? " fait" : "") + (j === k ? " ici" : "") + '" data-k="' + j + '"' + (j === k ? ' aria-current="step"' : "") + ' aria-label="Écran ' + (j + 1) + " sur " + ecrans.length + " : " + esc(e.titre) + (fait ? ", fait" : "") + '"></button></li>'; }).join("");
  var exo = s.t === "partie", aVerifier = exo && (s.champs.some(function(f){ return cle(f) !== undefined; }) || (s.dernier && s.check));
  $("#msPrec").disabled = k === 0 && !voisine(-1);
  $("#msVerif").hidden = !aVerifier; $("#msVide").hidden = aVerifier || !exo;
  var suiv = $("#msSuiv"), fin = k === ecrans.length - 1, apres = voisine(1);
  suiv.classList.toggle("seul", !exo); suiv.hidden = fin && !apres;
  suiv.textContent = fin ? "Séance suivante →" : s.t === "intro" ? "C'est parti →" : "Suivant →";
}

/* la ressource de l'activité (schéma, tableau) accompagne chaque question : ouverte sur un grand écran, à un
   geste sur un téléphone — et l'élève garde la main */
function ressVue(){ return M.ress === undefined ? window.innerWidth >= 700 : M.ress; }
/* ═══ Montrer un écran : tout ce qui n'en fait pas partie se cache (à l'écran seulement) ═══ */
function vide(s){ return (s.t === "carte" || s.t === "retenir") && s.n.every(function(n){ return !n.offsetParent || (!net(n.innerText) && !$("img,svg,canvas,video,iframe,object,input,textarea,select", n)); }); }
function montrer(haut){
  var s = ecrans[k], vis = [];
  s.n.forEach(function(n){ vis.push(n); for (var p = n.parentNode; p && p !== panneau; p = p.parentNode) vis.push(p); });
  if (s.t === "partie" && s.ress.length && ressVue()) s.ress.forEach(function(n){ vis.push(n); for (var p = n.parentNode; p && p !== panneau; p = p.parentNode) vis.push(p); });
  ecrans.tous.forEach(function(n){ n.classList.toggle("ms-cache", vis.indexOf(n) < 0); });
  var ouv = $("#ouverture"); if (ouv) ouv.classList.toggle("ms-cache", !s.ouverture);
  if (s.ressBtn) s.ressBtn.textContent = ressVue() ? "📎 Masquer la ressource de l'activité" : "📎 Revoir la ressource de l'activité";
  $$(".ms-etq", panneau).forEach(peindre); peindreRetour(s); bilan(s);
  if (ecrans.length > 1 && vide(s)){ ecrans.splice(k, 1); k = Math.min(k, ecrans.length - 1); return montrer(haut); }
  if (!G.onglet){ var bout = k === ecrans.length - 1 && !voisine(1); $$(".page-suivante").forEach(function(x){ x.classList.toggle("ms-montre", bout && !x.closest(G.panneau)); }); }
  barre(); M.k[panneau.id] = k; ecrire();
  if (haut){ var y = Math.max(0, ancre.getBoundingClientRect().top + window.scrollY - 52); try { window.scrollTo({ top:y, behavior:"instant" }); } catch (e) { window.scrollTo(0, y); } }
}
function aller(j){
  if (j < 0){ var av = voisine(-1); if (av){ M.k[av] = 1e9; ouvrir(av); } return; }
  if (j >= ecrans.length) return;
  k = j; sel = null; reprendre(); montrer(true);
}
function suivant(){
  if (k < ecrans.length - 1) return aller(k + 1);
  var apres = voisine(1); if (apres){ M.k[apres] = 0; ouvrir(apres); }
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
  var r = f.tagName === "SELECT" ? f.selectedOptions[0] : $("input[type=radio]:checked", f), pq = (r && r.getAttribute("data-pourquoi")) || f.getAttribute("data-indice"); if (!pq) return "";
  if (f.classList.contains("ms-origine")) return "<b>« " + esc(lireV(f)) + " »</b> ne va pas avec « " + esc(intitule(f)) + " ». " + esc(pq);
  return seule ? esc(pq) : "<b>" + esc(intitule(f)) + "</b> " + esc(pq);
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
      var debut = seule ? "Pas encore." : "Pas encore. " + justes + " réponse" + (justes > 1 ? "s justes restent" : " juste reste") + " en place.";
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
    dire(s, "ok", n === 3 ? "Tout est juste, du premier coup." : "Tout est juste. Tu as corrigé tes erreurs : c'est comme ça qu'on apprend.", n);
  } else dire(s, "", "C'est noté. Lis le message de la vérification ci-dessous.");
  M.fait[s.id] = true; ecrire();
  if (s.dernier && s.check) s.check.click();          // la vérification de la page : c'est elle qui valide l'activité
  $$(".ms-etq", panneau).forEach(peindre); barre();
  if (gain){ var b = el("span", "ms-gain"); b.textContent = "+" + gain; $("#msGains").appendChild(b); setTimeout(function(){ b.remove(); }, 1600); }
  $("#msSuiv").focus({ preventScroll:true });
}

/* Au bilan de la séquence : les étoiles gagnées, au-dessus de l'auto-positionnement — qui reste le choix de l'élève */
function bilan(s){
  if (s.t !== "carte" || !(s.n[0].id === "bilan" || $("#je-me-positionne, fieldset.positionnement", s.n[0]))) return;
  var b = $(".ms-bilan", s.n[0]); if (!b){ b = el("div", "ms-bilan ms-seul"); var h = $("h2", s.n[0]); s.n[0].insertBefore(b, h ? h.nextSibling : s.n[0].firstChild); }
  var ps = parties(), gagne = ps.reduce(function(a, e){ return a + (M.etoiles[e.id] || 0); }, 0), faites = ps.filter(function(e){ return M.fait[e.id]; }).length;
  var corrigees = ps.reduce(function(a, e){ return a + (M.fait[e.id] ? (M.erreurs[e.id] || 0) : 0); }, 0);
  b.innerHTML = "<p><b>Ta mission : " + gagne + " étoile" + (gagne > 1 ? "s" : "") + " sur " + (ps.length * 3) + "</b> — " + faites + " question" + (faites > 1 ? "s" : "") + " réussie" + (faites > 1 ? "s" : "") + " sur " + ps.length + ".</p>" + (corrigees ? "<p>En route, tu as corrigé " + corrigees + " erreur" + (corrigees > 1 ? "s" : "") + " : c'est comme ça qu'on apprend.</p>" : "") + "<p>Trois étoiles : juste du premier coup. Ton positionnement, ci-dessous, c'est toi qui le choisis.</p>";
}

/* ═══ Entrer, sortir ═══ */
function entrer(){
  if (!construit){
    $$(G.panneau).forEach(function(P){ parPanneau[P.id] = construire(P); });
    Object.keys(parPanneau).forEach(function(id){ parPanneau[id].forEach(function(e){            // ce qui était réussi le reste
      if (e.t === "partie" && M.fait[e.id]) e.champs.forEach(function(f){ if (cle(f) !== undefined && lireV(f) === cle(f)) marquer(f, true); }); }); });
    construit = true;
  }
  actif = true; M.on = true; D.body.classList.add("ms");
  if (!G.onglet && !panneauActif()) ((M.ici && $(G.panneau + '[id="' + M.ici + '"]')) || $(G.panneau)).classList.add(G.actif);
  synchroniser();
}
function sortir(){
  actif = false; M.on = false; ecrire(); D.body.classList.remove("ms");
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
D.documentElement._mission = { cle: cle, ecran: function(){ var s = ecrans[k]; return s ? { t:s.t, id:s.id || "", dernier:!!s.dernier, check:!!s.check, fb:s.fb ? s.fb.id || "" : null } : null; } };
function init(){
  G = gabarit(); if (!G) return;                                    // gabarit non reconnu : la page reste telle quelle
  lire();
  /* « Effacer ma sauvegarde » efface aussi la mission : sur un poste partagé, l'élève suivant ne trouve ni les
     étoiles ni l'écran du précédent. La page efface sa clé puis se recharge ; on le voit ici à sa clé absente. */
  try { if (typeof KEY === "string" && localStorage.getItem(KEY) === null && (Object.keys(M.etoiles).length || Object.keys(M.fait).length || Object.keys(M.k).length || Object.keys(M.erreurs).length)){ M = { v:1, on:M.on, k:{}, essais:{}, erreurs:{}, etoiles:{}, fait:{} }; ecrire(); } } catch (e) {}
  chrome();
  /* la séance change (onglet, bouton « séance suivante », lien vers une ancre) : le mode suit le panneau ouvert */
  function suivre(){ if (actif && panneauActif() !== panneau) synchroniser(); }
  if (G.onglet) $$(G.onglet).forEach(function(o){ o.addEventListener("click", function(){ setTimeout(suivre, 0); }); });
  if (window.MutationObserver){ var obs = new MutationObserver(suivre); $$(G.panneau).forEach(function(P){ obs.observe(P, { attributes:true, attributeFilter:["class"] }); }); }
  var suite = false; try { suite = sessionStorage.getItem("mission:suite") === "1"; sessionStorage.removeItem("mission:suite"); } catch (e) {}
  if (M.on || suite) entrer();
}
if (D.readyState === "loading") D.addEventListener("DOMContentLoaded", init); else init();
})();
