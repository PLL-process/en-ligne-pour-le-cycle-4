# -*- coding: utf-8 -*-
"""onglets_seance.py — les onglets de séance se pilotent au clavier et la page rouvre la séance où l'élève était.

LE CONSTAT
----------
L'audit externe du jardin connecté (19/11/2026) l'a montré au navigateur, et la mesure du site le confirme :
  · les onglets portent le rôle ARIA `tab`, mais les flèches ne changent pas de séance (1 page sur 63 les gérait) ;
  · après un rechargement, la page revenait toujours à la séance 1 : l'élève parti de la séance 4 devait la rechercher.

CE QUE POSE L'OUTIL
-------------------
Un petit script, entre deux marqueurs, avant `</body>`, sur chaque page qui porte des onglets `.seance-tab` :
  · le modèle ARIA des onglets : ← et → passent à l'onglet voisin (en boucle), Début et Fin au premier et au dernier ;
    seul l'onglet choisi est dans l'ordre de tabulation (`tabindex` 0, les autres -1) ;
  · la séance ouverte est retenue dans ce navigateur (`localStorage`, clé « seance-active: » + chemin de la page) et
    rouverte au chargement suivant, sans faire défiler la page. Une adresse qui vise une ancre (`#partie-2`…)
    l'emporte : la page ne rouvre rien.
Des onglets qui sont des liens (une séquence découpée en pages) ne sont pas touchés. Une page qui gère déjà ses
flèches — elle-même, ou par `onglets_clavier.py` (n°326) — garde les siennes : le script écoute sur le document, donc
en dernier, et ne fait rien d'une touche déjà traitée (`preventDefault`). Mesure au navigateur, le 19/11/2026, sur les
47 pages à trois onglets ou plus : → depuis la séance 1 ouvre la séance 2 sur les 47 (26 avant ; poser l'écoute sur
l'onglet faisait sauter une séance là où `onglets_clavier.py` agissait aussi). Le script n'ouvre une séance qu'en
cliquant son onglet : c'est la page qui change de panneau, comme sous le doigt de l'élève (progression, tableau de
bord, mode mission suivent). Il ne touche ni aux réponses ni aux validations.

  python3 _outils/onglets_seance.py [--ecrire] [page.html | dossier …]   (sans chemin : les trois thèmes)

Sortie : 0 rien à poser ou tout posé · 1 une page reste à poser (sans --ecrire) · 2 rien lu (n°299).
"""
from __future__ import annotations

import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUT = "<!-- onglets-seance v1 : début — clavier et séance retenue ; source unique : _outils/onglets_seance.py -->"
FIN = "<!-- onglets-seance v1 : fin -->"
BLOC_RE = re.compile(r"<!-- onglets-seance v\d+ : début.*?<!-- onglets-seance v\d+ : fin -->\n?", re.S)
SCRIPT = r"""<script>
(function(){
  "use strict";
  var onglets = [].slice.call(document.querySelectorAll(".seance-tab"));
  /* des onglets qui sont des liens mènent à d'autres pages (séquence découpée) : rien à piloter ici */
  if (!onglets.length || onglets.some(function(o){ return o.matches("a[href]"); })) return;
  var cle = "seance-active:" + location.pathname;
  function actif(){
    for (var i = 0; i < onglets.length; i++)
      if (onglets[i].classList.contains("active") || onglets[i].getAttribute("aria-selected") === "true") return i;
    return 0;
  }
  function tabindex(){ var a = actif(); onglets.forEach(function(o, i){ o.tabIndex = (i === a) ? 0 : -1; }); }
  function retenir(o){ var v = o.getAttribute("data-panel") || o.id; try { if (v) localStorage.setItem(cle, v); } catch (e) {} }
  onglets.forEach(function(o){ o.addEventListener("click", function(){ retenir(o); setTimeout(tabindex, 0); }); });
  /* écouté sur le document, donc en dernier : si la page ou `onglets_clavier.py` (n°326) a déjà traité la touche
     (`preventDefault`), on ne déplace pas une seconde fois */
  document.addEventListener("keydown", function(e){
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey) return;
    var i = onglets.indexOf(e.target), j = null, n = onglets.length;
    if (i < 0) return;
    if (e.key === "ArrowRight") j = (i + 1) % n;
    else if (e.key === "ArrowLeft") j = (i - 1 + n) % n;
    else if (e.key === "Home") j = 0;
    else if (e.key === "End") j = n - 1;
    if (j === null) return;
    e.preventDefault();
    onglets[j].click();
    onglets[j].focus();
  });
  function rouvrir(){
    tabindex();
    if (location.hash && location.hash.length > 1) return;
    var v = null; try { v = localStorage.getItem(cle); } catch (e) {}
    if (!v) return;
    var o = onglets.filter(function(x){ return (x.getAttribute("data-panel") || x.id) === v; })[0];
    if (!o || onglets.indexOf(o) === actif()) return;
    var x = window.scrollX, y = window.scrollY;
    o.click();
    window.scrollTo(x, y);
    requestAnimationFrame(function(){ window.scrollTo(x, y); });
  }
  if (document.readyState === "complete") setTimeout(rouvrir, 0);
  else window.addEventListener("load", function(){ setTimeout(rouvrir, 0); });
})();
</script>"""
BLOC = DEBUT + "\n" + SCRIPT + "\n" + FIN + "\n"


def poser(s: str) -> str:
    if BLOC_RE.search(s):
        return BLOC_RE.sub(lambda _: BLOC, s, count=1)
    if 'class="seance-tab' not in s:
        return s
    i = s.rfind("</body>")
    if i < 0:
        return s
    return s[:i] + BLOC + s[i:]


def pages(chemins):
    out = []
    for c in chemins or [os.path.join(DEPOT, t) for t in sorted(os.listdir(DEPOT)) if t.startswith("theme-")]:
        if os.path.isfile(c):
            out.append(c)
            continue
        for d, _, fs in os.walk(c):
            if "_archive" in d or "/." in d.replace(os.sep, "/") or "node_modules" in d or "_generation" in d:
                continue
            out += [os.path.join(d, f) for f in sorted(fs) if f.endswith(".html")]
    return sorted(out)


def main(argv):
    ecrire = "--ecrire" in argv
    ps = pages([a for a in argv if not a.startswith("--")])
    if not ps:
        print("✘ aucune page lue : rien n'a été vérifié")
        return 2
    avec = poses = reste = 0
    for p in ps:
        s = open(p, encoding="utf-8").read()
        if 'class="seance-tab' not in s:
            continue
        avec += 1
        u = poser(s)
        if u != s:
            if ecrire:
                open(p, "w", encoding="utf-8").write(u)
                poses += 1
            else:
                reste += 1
                print("  ⚠ %s — onglets sans clavier ni séance retenue" % os.path.relpath(p, DEPOT))
    print("%d page(s) lues · %d à onglets de séance · %d posée(s) · %d à poser" % (len(ps), avec, poses, reste))
    return 1 if (reste and not ecrire) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
