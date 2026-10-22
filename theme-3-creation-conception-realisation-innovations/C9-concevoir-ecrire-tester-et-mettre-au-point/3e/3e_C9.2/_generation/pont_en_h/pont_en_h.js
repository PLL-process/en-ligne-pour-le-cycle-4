<script>
/* Pont en H — simulateur (pour aller plus loin, hors programme de cycle 4). Hors ligne, sans bibliothèque.
   Tout ce qui bouge est aussi dit en texte (n°119). Traces dans window.__exp.pontH, créées au premier geste seulement : enregistrées, jamais exigées (aucun verrou). */
(function(){
  "use strict";
  var racine = document.getElementById("ph_sim");
  if (!racine) return;
  var ferme = {A:false, B:false, C:false, D:false};
  var NOM = {A:"A (haut, à gauche)", B:"B (haut, à droite)", C:"C (bas, à gauche)", D:"D (bas, à droite)"};
  var OUVERT = {A:"M200 150 L222 118", B:"M400 150 L422 118", C:"M200 250 L222 218", D:"M400 250 L422 218"};
  var FERME  = {A:"M200 150 L200 110", B:"M400 150 L400 110", C:"M200 250 L200 210", D:"M400 250 L400 210"};
  var FILS = ["t0","t1","b0","b1","L1","L2","L3","L4","R1","R2","R3","R4","ML","MR"];
  var TRAJET = {
    sens1: ["t0","L1","L2","ML","MR","R3","R4","b1","b0"],
    sens2: ["t0","t1","R1","R2","MR","ML","L3","L4","b0"],
    ccG:   ["t0","L1","L2","L3","L4","b0"],
    ccD:   ["t0","t1","R1","R2","R3","R4","b1","b0"]
  };
  var svg = document.getElementById("ph_svg"), rotor = document.getElementById("ph_rotor");
  var dit = document.getElementById("ph_dit"), comp = document.getElementById("ph_comp"), etat = document.getElementById("ph_etat");
  var boutons = racine.querySelectorAll(".ph-sw[data-sw]");
  window.__exp = window.__exp || {};
  function trace(k){ window.__exp.pontH = window.__exp.pontH || {}; window.__exp.pontH[k] = true; }   // rien à l'initialisation : seulement ce que l'élève a fait

  function el(id){ return document.getElementById("ph_" + id); }
  function liste(l){ return l.length === 2 ? l[0] + " et " + l[1] : l.length > 2 ? l.slice(0, -1).join(", ") + " et " + l[l.length - 1] : l[0]; }

  function calcule(){
    var f = Object.keys(ferme).filter(function(k){ return ferme[k]; });
    var ccG = ferme.A && ferme.C, ccD = ferme.B && ferme.D, type;
    if (ccG || ccD) type = "cc";
    else if (ferme.A && ferme.D) type = "sens1";
    else if (ferme.B && ferme.C) type = "sens2";
    else type = "arret";
    return {f:f, ccG:ccG, ccD:ccD, type:type};
  }

  function phrase(e){
    var qui = e.f.length ? "Fermé" + (e.f.length > 1 ? "s" : "") + " : " + liste(e.f) + ". " : "";
    if (e.type === "sens1") return qui + "Le courant va du + vers le −, en traversant le moteur de gauche à droite : le moteur tourne dans le sens 1 (sens des aiguilles d'une montre).";
    if (e.type === "sens2") return qui + "Le courant va du + vers le −, en traversant le moteur de droite à gauche : le moteur tourne dans le sens 2 (sens inverse des aiguilles d'une montre).";
    if (e.type === "cc"){
      var cote = e.ccG && e.ccD ? "des côtés gauche et droit" : e.ccG ? "du côté gauche" : "du côté droit";
      return "⚠ Court-circuit ! " + qui + "Le courant va directement du + au − par les deux interrupteurs " + cote + ", sans traverser le moteur : intensité énorme, fils qui chauffent, protection qui saute. Le moteur est arrêté. Dans un vrai montage, la protection coupe vite ; ici, tu peux le voir sans danger. Pour y remédier, ouvre l'un des deux interrupteurs de ce côté.";
    }
    if (!e.f.length) return "Aucun interrupteur fermé : pas de courant, le moteur est arrêté.";
    if (e.f.length === 1) return qui + "Un seul interrupteur fermé : le courant ne peut pas revenir vers le −, le moteur est arrêté.";
    return qui + "Les deux bornes du moteur sont reliées au " + (ferme.A ? "+" : "−") + " : il ne passe aucun courant, le moteur est arrêté.";
  }

  function comparaison(e){
    var p = (document.getElementById("ph_pred") || {}).value || "";
    if (e.type !== "sens1" || e.f.length !== 2 || !p || p === "nsp") return "";
    if (p === "sens1") return "Tu avais prévu le sens 1 : bien vu.";
    if (p === "sens2") return "Tu avais prévu le sens 2. Avec A et D fermés, le courant traverse le moteur de gauche à droite : c'est le sens 1. Le sens 2 s'obtient avec B et C.";
    return "Tu avais prévu que le moteur ne tourne pas. Avec A et D fermés, le courant traverse le moteur : il tourne, dans le sens 1.";
  }

  function dessine(){
    var e = calcule();
    FILS.forEach(function(id){ el(id).setAttribute("class", "ph-w"); });
    var on = e.type === "sens1" || e.type === "sens2" ? TRAJET[e.type] : [];
    on.forEach(function(id){ el(id).setAttribute("class", "ph-w on"); });
    if (e.type === "cc"){
      (e.ccG ? TRAJET.ccG : []).concat(e.ccD ? TRAJET.ccD : []).forEach(function(id){ el(id).setAttribute("class", "ph-w cc"); });
    }
    Object.keys(ferme).forEach(function(k){
      el("sw" + k).querySelector(".ph-lev").setAttribute("d", ferme[k] ? FERME[k] : OUVERT[k]);
    });
    rotor.setAttribute("class", e.type === "sens1" ? "sens1" : e.type === "sens2" ? "sens2" : "");
    el("fl1").setAttribute("class", "ph-fl" + (e.type === "sens1" ? " on" : ""));
    el("fl2").setAttribute("class", "ph-fl" + (e.type === "sens2" ? " on" : ""));
    el("rot1").setAttribute("class", "ph-arc" + (e.type === "sens1" ? " on" : ""));
    el("rot2").setAttribute("class", "ph-arc" + (e.type === "sens2" ? " on" : ""));
    svg.setAttribute("class", "ph-svg" + (e.type === "cc" ? " cc" : ""));
    etat.textContent = e.type === "sens1" ? "Moteur : sens 1 ↻" : e.type === "sens2" ? "Moteur : sens 2 ↺" : e.type === "cc" ? "COURT-CIRCUIT !" : "Moteur arrêté";
    dit.textContent = phrase(e);
    dit.setAttribute("class", "ph-dit" + (e.type === "cc" ? " cc" : ""));
    comp.textContent = comparaison(e);
    boutons.forEach(function(b){
      var k = b.getAttribute("data-sw");
      b.setAttribute("aria-pressed", ferme[k] ? "true" : "false");
      b.textContent = NOM[k] + " : " + (ferme[k] ? "fermé" : "ouvert");
    });
    if (e.type === "sens1") trace("avant");
    if (e.type === "sens2") trace("arriere");
    if (e.type === "cc") trace("cc");
  }

  function bascule(k){ ferme[k] = !ferme[k]; dessine(); }
  boutons.forEach(function(b){ b.addEventListener("click", function(){ bascule(b.getAttribute("data-sw")); }); });
  ["A","B","C","D"].forEach(function(k){
    var g = el("sw" + k);
    g.style.cursor = "pointer";
    g.addEventListener("click", function(){ bascule(k); });
  });
  document.getElementById("ph_zero").addEventListener("click", function(){
    Object.keys(ferme).forEach(function(k){ ferme[k] = false; });
    dessine();
  });
  var pred = document.getElementById("ph_pred");
  if (pred) pred.addEventListener("change", dessine);
  dessine();
})();
</script>
