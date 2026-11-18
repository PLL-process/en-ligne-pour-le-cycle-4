# -*- coding: utf-8 -*-
"""retrait_validation.py — une réponse changée après la vérification retire la validation (règle d'or n°340, V3).

LE CONSTAT
----------
L'audit externe de `3e_C4.1` (17/11/2026) l'a montré au navigateur : une activité validée restait « réussie » quand
l'élève changeait ensuite une réponse — la barre de progression comptait une réussite que la page ne montrait plus.
`3e_C4.1` a été corrigée ce jour-là ; `controle_validations.py` (V3) en a mesuré 34 autres pages. Pascal, le
18/11/2026 : tout corriger (n°340).

CE QUE POSE L'OUTIL
-------------------
Un petit script, entre deux marqueurs, avant `</body>`, sur chaque page qui garde ses validations dans
`window.__valid` (clé `n` ou `"act" + n`) sans jamais les retirer. Pour chaque bouton « Vérifier » (`data-check`),
la zone de l'activité est le plus grand bloc qui ne porte que CE bouton ; un champ changé dans cette zone (texte,
menu, bouton radio, case), après une validation, la retire :
  · `window.__valid[…] = false` ;
  · le retour de l'activité (`#fb<n>`) dit « Tu as changé une réponse après la vérification : vérifie de nouveau. » ;
  · la page enregistre (`save`) et recompte sa progression (`majProgress`, `majProgres`), si elle les a.
Un curseur (`type="range"`) est un essai, pas une réponse : il n'y touche pas. Rien ne change pour la vérification
elle-même, ni pour la reprise d'une sauvegarde : le script ne s'arme qu'une fois la page chargée. Une étiquette posée
dans une chaîne à compléter (`_outils/chaine_a_completer/`) coche le bouton radio de sa case : elle compte aussi.

  python3 _outils/retrait_validation.py [--ecrire] [page.html | dossier …]   (sans chemin : les trois thèmes)
  python3 _outils/retrait_validation.py --etat [--strict]

Sortie : 0 rien à poser ou tout posé · 1 une page reste à poser (sans --ecrire, ou --strict) · 2 rien lu (n°299).
"""
from __future__ import annotations

import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUT = "<!-- retrait-validation v1 : début — règle d'or n°340 ; source unique : _outils/retrait_validation.py -->"
FIN = "<!-- retrait-validation v1 : fin -->"
BLOC_RE = re.compile(r"<!-- retrait-validation v1 : début.*?<!-- retrait-validation v1 : fin -->\n?", re.S)
REVOQUE = re.compile(r"__valid\s*\[[^\]]+\]\s*=\s*false")
SCRIPT = r"""<script>
(function(){
  "use strict";
  /* Une réussite vaut pour les réponses vérifiées (n°340) : changer une réponse d'une activité validée la remet
     « à vérifier ». Un curseur est un essai, pas une réponse : il n'y touche pas. Armé une fois la page chargée : la
     reprise d'une sauvegarde, qui remet les réponses en place, ne retire rien. */
  var arme = false;
  function armer(){ setTimeout(function(){ arme = true; }, 0); }
  if (document.readyState === "complete") armer(); else window.addEventListener("load", armer);
  [].forEach.call(document.querySelectorAll("[data-check]"), function(btn){
    var n = btn.getAttribute("data-check"), zone = btn;
    while (zone.parentElement && zone.parentElement.querySelectorAll("[data-check]").length === 1) zone = zone.parentElement;
    function cle(){
      var v = window.__valid || {};
      return v[n] ? n : v["act" + n] ? "act" + n : null;
    }
    function revoir(e){
      var t = e.target;
      if (!arme || !t || !t.matches || !t.matches("input, select, textarea") || t.type === "range") return;
      var k = cle(); if (k === null) return;
      window.__valid[k] = false;
      var fb = document.getElementById("fb" + n);
      if (fb){
        fb.classList.remove("ok", "good", "succes", "success", "reussi", "valide");
        fb.textContent = "✏️ Tu as changé une réponse après la vérification : vérifie de nouveau.";
      }
      try { if (typeof save === "function") save(false); } catch (x) {}
      try { if (typeof majProgress === "function") majProgress(); } catch (x) {}
      try { if (typeof majProgres === "function") majProgres(); } catch (x) {}
    }
    zone.addEventListener("input", revoir);
    zone.addEventListener("change", revoir);
  });
})();
</script>"""
BLOC = DEBUT + "\n" + SCRIPT + "\n" + FIN + "\n"


def a_poser(s: str) -> bool:
    return "data-check" in s and "__valid" in s and not REVOQUE.search(s.replace(SCRIPT, ""))


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
            if "_archive" in d or "/." in d.replace(os.sep, "/") or "node_modules" in d or "_generation" in d:
                continue
            out += [os.path.join(d, f) for f in sorted(fs) if f.endswith(".html") and not f.startswith("qcm")]
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
        if "data-check" not in s or "__valid" not in s:
            continue
        avec += 1
        u = poser(s)
        if u != s:
            if ecrire and not etat:
                open(p, "w", encoding="utf-8").write(u)
                poses += 1
            else:
                reste += 1
                print("  %s %s — une réponse changée ne retire pas la validation" % ("✘" if strict else "⚠", os.path.relpath(p, DEPOT)))
    print("%d page(s) lues · %d avec des validations · %d posée(s) · %d à poser" % (len(ps), avec, poses, reste))
    return 1 if (reste and (strict or not ecrire)) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
