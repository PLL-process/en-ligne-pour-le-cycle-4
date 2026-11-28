/* objet3d-amorce.js — branche le bouton « Tourner l'objet en 3D » de chaque <figure class="o3d" data-o3d-modele>.
   Petit (chargé avec la page) : la vue et three.js (objet3d.js, 650 Ko) et le modèle ne se chargent qu'AU CLIC, en
   scripts classiques (lisibles en file://, où modules ES et fetch() sont refusés). Voir LISEZMOI.md. */
(function () {
  "use strict";
  function charger(src) {
    return new Promise(function (ok, ko) {
      var s = document.createElement("script");
      s.src = src; s.onload = ok; s.onerror = function () { ko(new Error("introuvable : " + src)); };
      document.head.appendChild(s);
    });
  }
  function webgl() {
    try { var c = document.createElement("canvas"); return !!(c.getContext("webgl2") || c.getContext("webgl")); }
    catch (e) { return false; }
  }
  function dire(fig, texte) {
    var aide = document.getElementById(fig.getAttribute("data-o3d-aide") || "");
    if (aide) aide.textContent = texte;
  }
  /* Le bouton est SOUS la figure (aria-controls = id de la figure) : posé sur l'image, il en cachait le bas à 390 px.
     Une fois la vue ouverte, il ne disparaît pas (rien ne bouge dans la page) : il ramène la vue de départ, ce que
     le doigt ne peut pas faire autrement (au clavier : « 0 »). */
  function brancher(fig) {
    var btn = fig.id ? document.querySelector('.o3d-btn[aria-controls="' + fig.id + '"]') : null, img = fig.querySelector("img");
    if (!btn) return;
    if (!webgl()) { btn.hidden = true; dire(fig, "Ce poste n'affiche pas la 3D : l'image fixe montre les mêmes pièces."); return; }
    btn.hidden = false;
    var vue = null;
    btn.addEventListener("click", function () {
      if (vue) { vue.revenir(); fig.focus({ preventScroll: true }); return; }
      var libelle = btn.textContent, nom = fig.getAttribute("data-o3d-global");
      btn.disabled = true; btn.textContent = "⏳ Ouverture de la 3D…";
      (window.Objet3D ? Promise.resolve() : charger(fig.getAttribute("data-o3d-moteur")))
        .then(function () { return window[nom] ? null : charger(fig.getAttribute("data-o3d-modele")); })
        .then(function () {
          var o = JSON.parse(fig.getAttribute("data-o3d-options") || "{}");
          o.modele = window[nom];
          return window.Objet3D.monter(fig, o);
        })
        .then(function (v) {
          vue = v;
          if (img) img.hidden = true; fig.classList.add("o3d-ouvert");
          btn.disabled = false; btn.textContent = "↺ Revenir à la vue de départ";
          /* le focus passe à la vue, qui se tourne aussi au clavier (l'aide dit les touches) */
          fig.tabIndex = 0;
          if (fig.getAttribute("data-o3d-aide")) fig.setAttribute("aria-describedby", fig.getAttribute("data-o3d-aide"));
          fig.focus({ preventScroll: true });
        })
        .catch(function () {
          btn.disabled = false; btn.textContent = libelle;
          dire(fig, "La 3D n'a pas pu s'ouvrir sur ce poste : l'image fixe montre les mêmes pièces.");
        });
    });
  }
  function tout() { Array.prototype.forEach.call(document.querySelectorAll("figure.o3d[data-o3d-modele]"), brancher); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", tout); else tout();
})();
