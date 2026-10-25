# -*- coding: utf-8 -*-
"""Règle d'or n°92 — une image qu'on ne peut pas agrandir est une image qu'on
ne peut pas lire.

Pose dans chaque page un agrandisseur d'images autonome : aucune
bibliothèque, aucun réseau, aucune donnée envoyée. Un clic — ou la touche
Entrée quand l'image a le focus — affiche l'image en grand ; Échap, un clic
dans le fond, ou le bouton de fermeture la referment.

    python3 audit/loupe.py <dossier>              # équipe les pages qui n'ont pas d'agrandisseur
    python3 audit/loupe.py --remplacer <dossier>  # remplace l'agrandisseur v1 par le v2, page par page
    python3 audit/loupe.py --verifier <dossier>   # dit, sans rien écrire, ce que --remplacer ferait

LE BLOC v2 (25/10/2026), et ce qu'il corrige du v1 :
  · un schéma SVG écrit DANS la page s'agrandit avec ses couleurs, sa police et
    son fond : le v1 le sérialisait seul, sans la feuille de style de la page,
    et l'image agrandie sortait en formes noires, en police par défaut, le texte
    débordant du cadre (constat de Pascal, 25/10/2026, Chengdu 5e). Le v2 recopie
    sur la copie les propriétés CALCULÉES de chaque élément (remplissage, trait,
    police, ancrage du texte…), y ajoute les dégradés et marqueurs définis
    ailleurs dans la page, et donne à l'image le fond sur lequel le schéma est
    dessiné ;
  · la légende ne recouvre plus l'image (journal du 24/09/2026) : l'agrandisseur
    est une colonne — bouton, image, légende —, la légende suit l'image, l'image
    reçoit la hauteur qui reste ; la légende est la figcaption visible de la
    figure, sinon le texte alternatif, réduit à sa première phrase s'il dépasse
    deux lignes ; l'alt complet reste sur l'image agrandie.

Ce que le script REFUSE de faire, et pourquoi :
  · il n'équipe pas deux fois la même page (marqueur, ou code de l'agrandisseur
    présent sans marqueur) ;
  · il ignore les gabarits, dont le corps contient encore des @@JETONS@@ ;
  · il n'ajoute rien à une page sans <img> ni <svg>, pour ne pas alourdir pour rien ;
  · --remplacer ne touche QUE les règles CSS de l'agrandisseur et sa fonction
    (function(){…})() : ce que d'autres lots ont glissé ensuite dans le même
    <style> (n°303, n°135) ou le même <script> (n°45, n°101, n°188) reste tel quel.
    Une page dont il ne reconnaît pas les repères est NOMMÉE et laissée intacte.

Ce qu'il ne sait PAS faire, et qu'il faut relire à l'œil : vérifier qu'une
image agrandie reste lisible. Une capture floue le reste en grand.
"""
import pathlib
import re
import sys

LOUPE_MARQUEUR = "loupe-images-v2"

COMMENTAIRE = """<!-- %s — agrandisseur d'images, règle d'or n°92. Aucune bibliothèque, aucun
     réseau. Clic ou Entrée pour agrandir, Échap ou clic dans le fond pour
     refermer. Le focus revient sur l'image quittée. -->""" % LOUPE_MARQUEUR

CSS = """  /* L'agrandisseur est une COLONNE — bouton, image, légende — : la légende suit l'image dans le
     flux, l'image reçoit une hauteur maximale calculée (ajuster()), et le fond défile si besoin. */
  .loupe-fond{position:fixed;inset:0;background:rgba(12,14,18,.92);display:none;
    z-index:9999;padding:1rem;box-sizing:border-box;overflow:auto;
    flex-direction:column;align-items:center;gap:.75rem}
  .loupe-fond[data-ouvert="oui"]{display:flex}
  /* centré quand tout tient, sans rien couper quand ça déborde : des marges automatiques,
     pas justify-content:center (qui rendrait le haut inaccessible au défilement) */
  .loupe-fond > .loupe-fermer{margin-top:auto}
  .loupe-fond > .loupe-legende{margin-bottom:auto}
  .loupe-fond img{display:block;flex:none;max-width:100%%;max-height:80vh;width:auto;height:auto;
    box-shadow:0 0 0 1px rgba(255,255,255,.15),0 24px 60px rgba(0,0,0,.6);
    background:#fff;border-radius:4px}
  .loupe-legende{position:static;flex:none;margin:0;max-width:min(70ch,100%%);text-align:center;
    color:#e7e9ee;font:400 .95rem/1.4 system-ui,sans-serif}
  .loupe-legende .loupe-aide{display:block;margin-top:.25rem;font-size:.85em;color:#b8bfcc}
  .loupe-fermer{position:sticky;top:0;align-self:flex-end;flex:none;z-index:1;background:#1b1f27;
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
"""

SCRIPT = r"""(function(){
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
    bouton.textContent = "Fermer ✕";
    grande = document.createElement("img");
    grande.alt = "";
    legende = document.createElement("p");
    legende.className = "loupe-legende";
    fond.appendChild(bouton); fond.appendChild(grande); fond.appendChild(legende);
    document.body.appendChild(fond);
    bouton.addEventListener("click", fermer);
    fond.addEventListener("click", function(e){ if (e.target === fond) fermer(); });
    grande.addEventListener("load", ajuster);
    window.addEventListener("resize", ajuster);
  }

  // La légende affichée : la figcaption VISIBLE de la figure si elle existe ; sinon le
  // texte alternatif, réduit à sa première phrase s'il dépasse deux lignes. L'alt complet
  // reste sur l'image agrandie, pour les lecteurs d'écran.
  function poserLegende(el, texteAlt){
    var fig = el.closest("figure");
    var cap = fig ? fig.querySelector("figcaption") : null;
    var visible = cap && cap.getClientRects().length && cap.textContent.trim();
    legende.textContent = "";
    var texte = visible ? cap.textContent.replace(/\s+/g, " ").trim() : (texteAlt || "");
    texte = texte.replace(/\s*\(clique[^()]*agrandir\)/gi, "").trim();   // l'image est déjà agrandie
    var corps = document.createElement("span");
    corps.textContent = texte;
    var aide = document.createElement("span");
    aide.className = "loupe-aide";
    aide.textContent = "Échap pour refermer";
    if (texte) legende.appendChild(corps);
    legende.appendChild(aide);
    if (!visible && texte) {
      var ligne = parseFloat(getComputedStyle(legende).lineHeight) || 20;
      if (corps.getBoundingClientRect().height > 2 * ligne + 1) {
        var m = texte.match(/^[\s\S]*?[.!?…](?=\s|$)/);
        if (m && m[0].length < texte.length) corps.textContent = m[0];
      }
    }
  }

  // L'image reçoit la place qui reste : hauteur du fond, moins le bouton, la légende,
  // les marges et les espacements — jamais moins de 40 % de l'écran ; au-delà, le fond défile.
  function ajuster(){
    if (!fond || !fond.getAttribute("data-ouvert")) return;
    var st = getComputedStyle(fond);
    var ecart = parseFloat(st.rowGap) || 0;
    var reste = fond.clientHeight - parseFloat(st.paddingTop) - parseFloat(st.paddingBottom)
              - fond.querySelector(".loupe-fermer").offsetHeight - legende.offsetHeight - 2 * ecart;
    grande.style.maxHeight = Math.max(reste, 0.4 * window.innerHeight) + "px";
  }

  function montrer(el, texteAlt){
    fond.setAttribute("data-ouvert", "oui");
    fond.scrollTop = 0;
    poserLegende(el, texteAlt);
    ajuster();
    fond.querySelector(".loupe-fermer").focus();
  }

  function ouvrir(img){
    if (!fond) construire();
    dernier = img;
    grande.style.background = "";
    grande.src = img.currentSrc || img.src;
    grande.alt = img.alt || "";
    montrer(img, img.alt);
  }

  function fermer(){
    if (!fond) return;
    fond.removeAttribute("data-ouvert");
    grande.removeAttribute("src");
    grande.style.maxHeight = "";
    if (dernier) { dernier.focus(); dernier = null; }
  }

  document.addEventListener("keydown", function(e){
    if (e.key === "Escape" && fond && fond.getAttribute("data-ouvert")) fermer();
  });

  // Les schémas du dépôt sont souvent des SVG écrits directement dans la page, et leurs
  // couleurs et leur police viennent de la feuille de style de la PAGE. Sérialisé seul, le
  // dessin les perdrait (formes noires, police par défaut, texte qui déborde) : on recopie
  // donc sur la copie les propriétés CALCULÉES de chaque élément, on y ajoute les dégradés
  // et marqueurs définis ailleurs dans la page, et l'image reçoit le fond du schéma.
  var PROPRIETES = ["fill", "fill-opacity", "fill-rule", "stroke", "stroke-width", "stroke-opacity",
    "stroke-dasharray", "stroke-dashoffset", "stroke-linecap", "stroke-linejoin", "stroke-miterlimit",
    "opacity", "visibility", "display", "color", "font-family", "font-size", "font-weight", "font-style",
    "font-variant-numeric", "letter-spacing", "word-spacing", "text-anchor", "dominant-baseline",
    "baseline-shift", "text-decoration", "white-space", "paint-order", "stop-color", "stop-opacity",
    "marker-start", "marker-mid", "marker-end", "clip-path", "mask", "filter"];
  // Une transformation posée par la feuille de style (pas par l'attribut transform, que la
  // copie garde déjà) : on la recopie avec son origine.
  var TRANSFORMATION = ["transform", "transform-origin", "transform-box"];

  function figer(source, copie){
    var a = [source].concat([].slice.call(source.querySelectorAll("*")));
    var b = [copie].concat([].slice.call(copie.querySelectorAll("*")));
    for (var i = 0; i < a.length && i < b.length; i++) {
      var cs = getComputedStyle(a[i]), decl = [], k, v;
      for (k = 0; k < PROPRIETES.length; k++) {
        v = cs.getPropertyValue(PROPRIETES[k]);
        if (v) decl.push(PROPRIETES[k] + ":" + v);
      }
      if (i > 0 && !a[i].hasAttribute("transform") && cs.getPropertyValue("transform") &&
          cs.getPropertyValue("transform") !== "none") {
        for (k = 0; k < TRANSFORMATION.length; k++) decl.push(TRANSFORMATION[k] + ":" + cs.getPropertyValue(TRANSFORMATION[k]));
      }
      var deja = b[i].getAttribute("style");
      b[i].setAttribute("style", decl.join(";") + (deja ? ";" + deja : ""));
    }
  }

  // Un dégradé ou un marqueur appelé par url(#…) mais défini hors du dessin : on le recopie dedans.
  function rapatrier(copie){
    var defs = null, faits = {}, tour = 0, trouve = true;
    while (trouve && tour++ < 4) {
      trouve = false;
      var refs = (new XMLSerializer().serializeToString(copie).match(/url\((?:&quot;|["'])?#([^"')&]+)/g) || [])
        .concat(new XMLSerializer().serializeToString(copie).match(/href="#[^"]+"/g) || []);
      refs.forEach(function(r){
        var id = r.replace(/^url\((?:&quot;|["'])?#/, "").replace(/^href="#/, "").replace(/"$/, "");
        if (faits[id] || copie.querySelector("[id='" + id.replace(/'/g, "") + "']")) return;
        faits[id] = true;
        var el = document.getElementById(id);
        if (!el || !el.closest("svg")) return;
        if (!defs) { defs = document.createElementNS("http://www.w3.org/2000/svg", "defs"); copie.insertBefore(defs, copie.firstChild); }
        var c = el.cloneNode(true); figer(el, c); defs.appendChild(c); trouve = true;
      });
    }
  }

  // Le fond sur lequel le schéma est dessiné : le sien, sinon celui du premier parent opaque.
  function fondDe(el){
    for (var e = el; e && e.nodeType === 1; e = e.parentElement) {
      var c = getComputedStyle(e).backgroundColor, m = c.match(/rgba?\(([^)]+)\)/);
      if (m) { var p = m[1].split(","); if (p.length < 4 || parseFloat(p[3]) > 0) return c; }
      else if (c && c !== "transparent") return c;
    }
    return "#fff";
  }

  function ouvrirSvg(svg){
    if (!fond) construire();
    dernier = svg;
    var copie = svg.cloneNode(true);
    copie.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    figer(svg, copie);
    rapatrier(copie);
    copie.style.background = "transparent";
    // Une taille propre au dessin (sans elle, une image SVG n'a que 300 × 150 px à offrir) :
    // celle de la viewBox, agrandie ; le CSS de la loupe la ramène à l'écran.
    var vb = svg.viewBox && svg.viewBox.baseVal, boite = svg.getBoundingClientRect();
    var w = vb && vb.width ? vb.width : boite.width, h = vb && vb.height ? vb.height : boite.height;
    if (!(vb && vb.width) && w && h) copie.setAttribute("viewBox", "0 0 " + w + " " + h);
    var k = w ? Math.max(1, 1600 / w) : 1;
    if (w && h) { copie.setAttribute("width", Math.round(w * k)); copie.setAttribute("height", Math.round(h * k)); }
    var texte = new XMLSerializer().serializeToString(copie);
    grande.style.background = fondDe(svg);
    grande.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(texte);
    var titre = svg.querySelector("title");
    var mot = titre ? titre.textContent : (svg.getAttribute("aria-label") || "");
    grande.alt = mot;
    montrer(svg, mot);
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
"""

BLOC = "\n" + COMMENTAIRE + "\n<style>\n" + (CSS % ()) + "</style>\n<script>\n" + SCRIPT + "</script>\n"


def injectable(html: str) -> bool:
    if LOUPE_MARQUEUR in html or "loupe-images-v1" in html or ".loupe-fond{" in html:
        return False
    if "@@" in html:                     # gabarit non rempli
        return False
    if not re.search(r"<img\b|<svg\b", html, re.I):
        return False
    return "</body>" in html


# ── Remplacement du v1 par le v2 ──────────────────────────────────────────────
# Repères du v1 (toutes ses variantes relevées le 25/10/2026, 133 pages) :
#   CSS : du premier « .loupe-fond{ » (ou du commentaire du 24/09 qui le précède) jusqu'à
#         la fin du bloc « @media (prefers-reduced-motion:no-preference){ … @keyframes loupe-ouvre … } » ;
#   JS  : la fonction « (function(){ "use strict"; var fond, grande, legende, dernier = null; … })(); ».
_COMMENT_V1 = re.compile(r"<!-- loupe-images-v1 — agrandisseur d'images.*?-->", re.S)
_DEBUT_CSS = re.compile(r"(?:  /\* 24/09/2026 — la légende était en position:fixed.*?\*/\n)?  \.loupe-fond\{position:fixed", re.S)
_FIN_CSS = re.compile(r"  @media \(prefers-reduced-motion:no-preference\)\{\n    \.loupe-fond\[data-ouvert=\"oui\"\] img\{animation:loupe-ouvre[^\n]*\n    @keyframes loupe-ouvre[^\n]*\n  \}\n")
_DEBUT_JS = re.compile(r"\(function\(\)\{\n  \"use strict\";\n  var fond, grande, legende, dernier = null;")
_FIN_JS = re.compile(r"  if \(document\.readyState === \"loading\"\) \{\n    document\.addEventListener\(\"DOMContentLoaded\", armer\);\n  \} else \{\n    armer\(\);\n  \}\n\}\)\(\);\n")


def remplacer(html: str):
    """Rend (nouvelle page, None) ou (None, raison) si un repère manque. Une seule loupe par page."""
    if LOUPE_MARQUEUR in html:
        return None, "déjà en v2"
    debuts = list(_DEBUT_CSS.finditer(html))
    if len(debuts) != 1:
        return None, "%d début(s) de CSS de loupe" % len(debuts)
    d = debuts[0]
    f = _FIN_CSS.search(html, d.end())
    if not f:
        return None, "fin du CSS de loupe introuvable"
    j = _DEBUT_JS.search(html, f.end())
    if not j:
        return None, "fonction de la loupe introuvable"
    k = _FIN_JS.search(html, j.end())
    if not k:
        return None, "fin de la fonction de la loupe introuvable"
    if html.count('var fond, grande, legende, dernier = null;') != 1:
        return None, "plusieurs fonctions de loupe"
    neuf = html[:d.start()] + (CSS % ()) + html[f.end():j.start()] + SCRIPT + html[k.end():]
    if _COMMENT_V1.search(neuf):
        neuf = _COMMENT_V1.sub(lambda _m: COMMENTAIRE, neuf, count=1)
    else:                                   # code sans marqueur : on pose le commentaire devant son <style>
        s = neuf.rfind("<style>", 0, d.start())
        neuf = neuf[:s] + COMMENTAIRE + "\n" + neuf[s:]
    return neuf, None


def pages_a_remplacer(racine):
    for p in sorted(pathlib.Path(racine).rglob("*.html")):
        if "_archive-anciennes-versions" in p.parts:
            continue
        html = p.read_text(encoding="utf-8")
        if "loupe-images-v1" in html or (".loupe-fond{" in html and LOUPE_MARQUEUR not in html):
            yield p, html


def main(args):
    if args and args[0] in ("--remplacer", "--verifier"):
        ecrire = args[0] == "--remplacer"
        racine = args[1] if len(args) > 1 else "."
        faits, refus = [], []
        for p, html in pages_a_remplacer(racine):
            neuf, raison = remplacer(html)
            if raison:
                refus.append((p, raison))
                continue
            if ecrire:
                p.write_text(neuf, encoding="utf-8")
            faits.append(p)
        print("%d page(s) %s en v2, %d laissée(s) intacte(s)." % (len(faits), "passée(s)" if ecrire else "à passer", len(refus)))
        for p, r in refus:
            print("  ✘ %s — %s" % (p, r))
        print("  (les archives, _archive-anciennes-versions/, ne sont pas lues : versions gelées)")
        return 1 if refus else 0
    racine = args[0] if args else "."
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
  Ignorées volontairement : les pages sans <img> ni <svg> (rien à agrandir), les
  gabarits (@@JETONS@@ non remplis), et celles déjà équipées (v1, v2, ou code sans marqueur).
  Vérifié mécaniquement : le bloc est injecté une seule fois, avant </body>.
  NON couvert : la LISIBILITÉ de l'image agrandie. Une capture floue ou
  rognée trop court le reste en grand — cela se juge à l'œil, image par
  image. Le script rend l'agrandissement possible ; il ne rend pas les
  images bonnes.""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
