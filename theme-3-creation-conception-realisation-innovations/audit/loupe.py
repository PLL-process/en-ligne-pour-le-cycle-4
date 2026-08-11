# -*- coding: utf-8 -*-
"""Règle d'or n°92 — une image qu'on ne peut pas agrandir est une image qu'on
ne peut pas lire.

Injecte dans chaque page un agrandisseur d'images autonome : aucune
bibliothèque, aucun réseau, aucune donnée envoyée. Un clic — ou la touche
Entrée quand l'image a le focus — affiche l'image en grand ; Échap, un clic
dans le fond, ou le bouton de fermeture la referment.

    python3 audit/loupe.py <dossier>      # injecte, et dit ce qu'il a fait

Ce que le script REFUSE de faire, et pourquoi :
  · il ne touche pas deux fois la même page (marqueur LOUPE_MARQUEUR) ;
  · il ignore les gabarits, dont le corps contient encore des @@JETONS@@ ;
  · il n'ajoute rien à une page sans <img>, pour ne pas alourdir pour rien.

Ce qu'il ne sait PAS faire, et qu'il faut relire à l'œil : vérifier qu'une
image agrandie reste lisible. Une capture floue le reste en grand.
"""
import pathlib
import re
import sys

LOUPE_MARQUEUR = "loupe-images-v1"

BLOC = """
<!-- %s — agrandisseur d'images, règle d'or n°92. Aucune bibliothèque, aucun
     réseau. Clic ou Entrée pour agrandir, Échap ou clic dans le fond pour
     refermer. Le focus revient sur l'image quittée. -->
<style>
  .loupe-fond{position:fixed;inset:0;background:rgba(12,14,18,.92);display:none;
    z-index:9999;padding:2rem;box-sizing:border-box;overflow:auto;
    align-items:center;justify-content:center}
  .loupe-fond[data-ouvert="oui"]{display:flex}
  .loupe-fond img{max-width:100%%;max-height:88vh;height:auto;
    box-shadow:0 0 0 1px rgba(255,255,255,.15),0 24px 60px rgba(0,0,0,.6);
    background:#fff;border-radius:4px}
  .loupe-legende{position:fixed;left:0;right:0;bottom:.9rem;text-align:center;
    color:#e7e9ee;font:400 .95rem/1.4 system-ui,sans-serif;padding:0 2rem}
  .loupe-fermer{position:fixed;top:.8rem;right:1rem;background:#1b1f27;
    color:#e7e9ee;border:1px solid #3a4150;border-radius:6px;
    font:600 1rem/1 system-ui,sans-serif;padding:.6rem .9rem;cursor:pointer}
  .loupe-fermer:focus-visible,.loupe-cliquable:focus-visible{outline:3px solid #ffb300;
    outline-offset:3px}
  .loupe-cliquable{cursor:zoom-in}
  @media print{.loupe-fond{display:none !important}}
  @media (prefers-reduced-motion:no-preference){
    .loupe-fond[data-ouvert="oui"] img{animation:loupe-ouvre .16s ease-out}
    @keyframes loupe-ouvre{from{transform:scale(.97);opacity:.4}to{transform:none;opacity:1}}
  }
</style>
<script>
(function(){
  "use strict";
  var fond, grande, legende, dernier = null;

  function construire(){
    fond = document.createElement("div");
    fond.className = "loupe-fond";
    fond.setAttribute("role", "dialog");
    fond.setAttribute("aria-modal", "true");
    fond.setAttribute("aria-label", "Image agrandie");
    var bouton = document.createElement("button");
    bouton.type = "button";
    bouton.className = "loupe-fermer";
    bouton.textContent = "Fermer \\u2715";
    grande = document.createElement("img");
    grande.alt = "";
    legende = document.createElement("p");
    legende.className = "loupe-legende";
    fond.appendChild(bouton); fond.appendChild(grande); fond.appendChild(legende);
    document.body.appendChild(fond);
    bouton.addEventListener("click", fermer);
    fond.addEventListener("click", function(e){ if (e.target === fond) fermer(); });
  }

  function ouvrir(img){
    if (!fond) construire();
    dernier = img;
    grande.src = img.currentSrc || img.src;
    grande.alt = img.alt || "";
    // L'alternative textuelle sert de légende : elle DIT ce que l'image montre.
    legende.textContent = img.alt ? img.alt + "  \\u2014  \\u00c9chap pour refermer"
                                  : "\\u00c9chap pour refermer";
    fond.setAttribute("data-ouvert", "oui");
    fond.querySelector(".loupe-fermer").focus();
  }

  function fermer(){
    if (!fond) return;
    fond.removeAttribute("data-ouvert");
    grande.removeAttribute("src");
    if (dernier) { dernier.focus(); dernier = null; }
  }

  document.addEventListener("keydown", function(e){
    if (e.key === "Escape" && fond && fond.getAttribute("data-ouvert")) fermer();
  });

  // Les schémas du dépôt sont souvent des SVG écrits directement dans la page.
  // On les sérialise à la volée pour les afficher en grand — sans réseau : le
  // dessin est déjà là, on ne fait que le relire.
  function ouvrirSvg(svg){
    if (!fond) construire();
    dernier = svg;
    var copie = svg.cloneNode(true);
    if (!copie.getAttribute("xmlns")) {
      copie.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    }
    var texte = new XMLSerializer().serializeToString(copie);
    grande.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(texte);
    var titre = svg.querySelector("title");
    var mot = titre ? titre.textContent : (svg.getAttribute("aria-label") || "");
    grande.alt = mot;
    legende.textContent = mot ? mot + "  \\u2014  \\u00c9chap pour refermer"
                              : "\\u00c9chap pour refermer";
    fond.setAttribute("data-ouvert", "oui");
    fond.querySelector(".loupe-fermer").focus();
  }

  function armerSvg(){
    var dessins = document.querySelectorAll("svg");
    for (var i = 0; i < dessins.length; i++) {
      var svg = dessins[i];
      if (svg.closest(".loupe-fond")) continue;
      if (svg.dataset.loupe === "non") continue;
      // Une icône de 20 px n'a pas besoin d'être agrandie : seuls les
      // schémas, ceux qu'on doit LIRE, sont concernés.
      var boite = svg.getBoundingClientRect();
      if (boite.width < 120 || boite.height < 90) continue;
      svg.classList.add("loupe-cliquable");
      svg.setAttribute("tabindex", "0");
      svg.addEventListener("click", function(){ ouvrirSvg(this); });
      svg.addEventListener("keydown", function(e){
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); ouvrirSvg(this); }
      });
    }
  }

  function armer(){
    armerSvg();
    var images = document.querySelectorAll("img");
    for (var i = 0; i < images.length; i++) {
      var img = images[i];
      if (img.closest(".loupe-fond")) continue;
      if (img.dataset.loupe === "non") continue;      // opt-out explicite
      img.classList.add("loupe-cliquable");
      img.tabIndex = 0;
      if (!img.getAttribute("title")) {
        img.setAttribute("title", "Cliquer pour agrandir");
      }
      img.addEventListener("click", function(){ ouvrir(this); });
      img.addEventListener("keydown", function(e){
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); ouvrir(this); }
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", armer);
  } else {
    armer();
  }
})();
</script>
""" % LOUPE_MARQUEUR


def injectable(html: str) -> bool:
    if LOUPE_MARQUEUR in html:
        return False
    if "@@" in html:                     # gabarit non rempli
        return False
    if not re.search(r"<img\b|<svg\b", html, re.I):
        return False
    return "</body>" in html


def main(racine):
    pages = sorted(pathlib.Path(racine).rglob("*.html"))
    faits, sautes = [], []
    for p in pages:
        html = p.read_text(encoding="utf-8")
        if not injectable(html):
            sautes.append(p)
            continue
        p.write_text(html.replace("</body>", BLOC + "</body>"), encoding="utf-8")
        faits.append(p)

    print("%d page(s) équipée(s) de l'agrandisseur, %d ignorée(s)."
          % (len(faits), len(sautes)))
    print("""
PÉRIMÈTRE DE CE SCRIPT
  Ignorées volontairement : les pages sans <img> (rien à agrandir), les
  gabarits (@@JETONS@@ non remplis), et celles déjà équipées.
  Vérifié mécaniquement : le bloc est injecté une seule fois, avant </body>.
  NON couvert : la LISIBILITÉ de l'image agrandie. Une capture floue ou
  rognée trop court le reste en grand — cela se juge à l'œil, image par
  image. Le script rend l'agrandissement possible ; il ne rend pas les
  images bonnes.""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
