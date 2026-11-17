# -*- coding: utf-8 -*-
"""onglets_clavier.py — les onglets des séances se manient au clavier (règle d'or n°326, audit du 17/11/2026).

LE CONSTAT
----------
La n°326 (14/11/2026) demande des onglets maniables au clavier : ← →, Début, Fin ; un seul onglet dans l'ordre de
tabulation ; chaque onglet relié à son panneau. Elle a été posée sur `3e_C9.1` ; l'audit externe de `3e_C4.1` du
17/11/2026 relève qu'ailleurs, rien de tout cela n'existe : 30 séquences sur 60 ont des onglets (`role="tab"`) sans
aucune gestion des flèches, ni lien `aria-controls` vers leur panneau.

CE QUE POSE L'OUTIL
-------------------
Un petit script, entre deux marqueurs, avant `</body>`, sur chaque page dont les onglets ne savent pas encore le faire
(aucun `ArrowRight` dans la page). Il ne change rien au fonctionnement des onglets — c'est toujours le clic de la page
qui ouvre une séance — ; il ajoute :
  · le lien onglet ↔ panneau : `aria-controls` sur l'onglet (son `data-panel`, ou son `href="#…"`), `role="tabpanel"`
    et `aria-labelledby` sur le panneau ;
  · un seul onglet dans l'ordre de tabulation, celui de la séance ouverte (`tabindex` 0, les autres -1) ;
  · ← et → pour passer à l'onglet voisin (en boucle), Début et Fin pour le premier et le dernier : l'onglet atteint
    reçoit le focus et s'ouvre, comme au clic.

  python3 _outils/onglets_clavier.py [--ecrire] [page.html | dossier …]   (sans chemin : les trois thèmes)
  python3 _outils/onglets_clavier.py --etat [--strict]

Sortie : 0 rien à poser ou tout posé · 1 une page reste à poser (sans --ecrire, ou --strict) · 2 rien lu.
"""
from __future__ import annotations

import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUT = "<!-- onglets-clavier v1 : début — règle d'or n°326 ; source unique : _outils/onglets_clavier.py -->"
FIN = "<!-- onglets-clavier v1 : fin -->"
BLOC_RE = re.compile(r"<!-- onglets-clavier v1 : début.*?<!-- onglets-clavier v1 : fin -->\n?", re.S)
SCRIPT = r"""<script>
(function(){
  "use strict";
  function panneauDe(t){
    var id = t.getAttribute("data-panel") || (t.getAttribute("href") || "").replace(/^#/, "");
    return id ? document.getElementById(id) : null;
  }
  function ouvert(t){ return t.getAttribute("aria-selected") === "true" || t.classList.contains("active") || t.classList.contains("actif"); }
  function ranger(liste){
    var tabs = [].slice.call(liste.querySelectorAll('[role="tab"]')), un = tabs.filter(ouvert)[0] || tabs[0];
    tabs.forEach(function(t){ t.setAttribute("tabindex", t === un ? "0" : "-1"); });
  }
  [].forEach.call(document.querySelectorAll('[role="tablist"]'), function(liste){
    var tabs = [].slice.call(liste.querySelectorAll('[role="tab"]'));
    if (!tabs.length) return;
    tabs.forEach(function(t, i){
      if (!t.id) t.id = "onglet-" + (i + 1);
      var p = panneauDe(t);
      if (p){
        t.setAttribute("aria-controls", p.id);
        if (!p.getAttribute("role")) p.setAttribute("role", "tabpanel");
        if (!p.getAttribute("aria-labelledby")) p.setAttribute("aria-labelledby", t.id);
      }
    });
    ranger(liste);
    liste.addEventListener("click", function(){ setTimeout(function(){ ranger(liste); }, 0); });
    liste.addEventListener("keydown", function(e){
      var i = tabs.indexOf(document.activeElement), j = -1;
      if (i < 0) return;
      if (e.key === "ArrowRight") j = (i + 1) % tabs.length;
      else if (e.key === "ArrowLeft") j = (i - 1 + tabs.length) % tabs.length;
      else if (e.key === "Home") j = 0;
      else if (e.key === "End") j = tabs.length - 1;
      if (j < 0) return;
      e.preventDefault();
      tabs[j].focus(); tabs[j].click();
      setTimeout(function(){ ranger(liste); tabs[j].focus(); }, 0);
    });
  });
})();
</script>"""
BLOC = DEBUT + "\n" + SCRIPT + "\n" + FIN + "\n"


def a_poser(s: str) -> bool:
    return 'role="tab"' in s and "ArrowRight" not in s.replace(SCRIPT, "")


def poser(s: str) -> str:
    if BLOC_RE.search(s):
        return BLOC_RE.sub(lambda _: BLOC, s, count=1)
    if not a_poser(s):
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
            if "_archive" in d or "/." in d.replace(os.sep, "/") or "node_modules" in d:
                continue
            out += [os.path.join(d, f) for f in sorted(fs) if f.endswith(".html")]
    return sorted(out)


def main(argv):
    ecrire, etat, strict = "--ecrire" in argv, "--etat" in argv, "--strict" in argv
    ps = pages([a for a in argv if not a.startswith("--")])
    if not ps:
        print("✘ aucune page lue : rien n'a été vérifié")
        return 2
    avec = poses = reste = 0
    for p in ps:
        s = open(p, encoding="utf-8").read()
        if 'role="tab"' not in s:
            continue
        avec += 1
        u = poser(s)
        if u != s:
            if ecrire and not etat:
                open(p, "w", encoding="utf-8").write(u)
                poses += 1
            else:
                reste += 1
                print("  %s %s — onglets sans clavier" % ("✘" if strict else "⚠", os.path.relpath(p, DEPOT)))
    print("%d page(s) lues · %d avec des onglets · %d posée(s) · %d à poser" % (len(ps), avec, poses, reste))
    return 1 if (reste and (strict or not ecrire)) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
