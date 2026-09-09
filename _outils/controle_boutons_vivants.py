# -*- coding: utf-8 -*-
"""controle_boutons_vivants.py — un bouton appelle une fonction qui existe dans sa page.

LE CONSTAT
----------
Le 09/09/2026, en vérifiant un point de l'audit externe sur `4e_C1.4` (des icônes ✅/❌ visibles
avant correction), la mesure a trouvé pire à côté : les six boutons « Vérifier » de la séquence
appelaient `checkSection()`, qui n'existait nulle part dans la page. Chaque clic levait une erreur
silencieuse — aucun score, aucune correction, aucun message. Sur tout le dépôt : trois fonctions
appelées par un bouton et jamais définies (`checkSection`, `toggleAnswer` dans `4e_C1.4`,
`saveProgress4` dans `3e_C1.5` — un « Sauvegarder mon travail » qui ne sauvegardait rien).

Un bouton mort ne fait pas de bruit (règle n°277) : l'élève clique, rien ne se passe, il conclut
que c'est lui. Ce contrôle lit ce qu'un navigateur ne signale qu'à la console.

CE QU'IL MESURE
---------------
Dans chaque page HTML hors archive : les noms de fonction appelés depuis un attribut `onclick`,
`onchange`, `oninput`, `onsubmit` ou `onkeyup`, et depuis une affectation `x.onclick = () => f(`.
Chacun doit être défini dans un `<script>` de la page — `function f(`, `const|let|var f =`,
`window.f =` ou `f = function`. Les noms natifs du navigateur (document, alert, print…) sont
ignorés.

CE QU'IL NE FAIT PAS
--------------------
Il ne suit pas les `addEventListener` (une fonction anonyme ne peut pas manquer), ne lit pas les
scripts externes (le dépôt n'en charge pas, règle n°40), et ne dit pas si la fonction FAIT ce que
le bouton promet — cela se mesure au navigateur, dans le banc du lot.

Usage :
    python3 _outils/controle_boutons_vivants.py           # rapport complet
    python3 _outils/controle_boutons_vivants.py --muet    # seulement les refus
Sortie : 0 si chaque bouton appelle une fonction définie, 1 sinon.
"""

import glob
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)

ATTRIBUT = re.compile(r'\bon(?:click|change|input|submit|keyup)="([^"]*)"', re.I)
APPEL = re.compile(r"\b([A-Za-z_]\w*)\s*\(")
AFFECTATION = re.compile(r"\.on(?:click|change|input)\s*=\s*\(\s*\)\s*=>\s*([A-Za-z_]\w*)\s*\(")
SCRIPT = re.compile(r"<script\b[^>]*>(.*?)</script>", re.S | re.I)

#: ce que le navigateur fournit, ou ce qui n'est pas un nom de fonction de la page
NATIFS = {
    "document", "window", "alert", "confirm", "prompt", "print", "open", "close", "setTimeout",
    "setInterval", "location", "navigator", "encodeURIComponent", "decodeURIComponent", "String",
    "Number", "parseInt", "parseFloat", "Math", "Array", "Object", "JSON", "Date", "Promise",
    "fetch", "event", "this", "if", "for", "while", "return", "new", "void", "typeof",
    "getElementById", "querySelector", "querySelectorAll", "scrollIntoView", "focus", "blur",
    "click", "reload", "preventDefault", "stopPropagation", "requestSubmit", "toggle", "remove",
    "add", "contains", "push", "trim", "then", "catch", "setAttribute", "removeAttribute",
    "getAttribute", "classList", "play", "pause", "reset", "select", "showModal", "closest",
    "requestFullscreen", "scrollTo", "back", "forward", "assign", "replace", "history", "console",
    "log", "closest", "matches", "dispatchEvent", "Event", "CustomEvent", "localStorage",
    "getItem", "setItem", "removeItem", "clear", "stopImmediatePropagation", "print",
}


def pages(racine):
    return sorted(f for f in glob.glob(os.path.join(racine, "**", "*.html"), recursive=True)
                  if not any(e in f for e in ECARTES))


def juger(chemin):
    """(nb d'appels, [noms appelés et jamais définis])."""
    texte = open(chemin, encoding="utf-8", errors="replace").read()
    scripts = "\n".join(SCRIPT.findall(texte))
    appels = set()
    for m in ATTRIBUT.finditer(texte):
        appels.update(APPEL.findall(m.group(1)))
    for m in AFFECTATION.finditer(scripts):
        appels.add(m.group(1))
    manquants = []
    for fn in sorted(appels):
        if fn in NATIFS:
            continue
        defini = (re.search(r"\bfunction\s+%s\s*\(" % fn, scripts)
                  or re.search(r"\b(?:const|let|var)\s+%s\s*=" % fn, scripts)
                  or re.search(r"\bwindow\.%s\s*=" % fn, scripts)
                  or re.search(r"\b%s\s*=\s*(?:function|\(|async)" % fn, scripts))
        if not defini:
            manquants.append(fn)
    return len(appels), manquants


def main(muet=False):
    total, ecarts, pages_lues = 0, [], 0
    for f in pages(DEPOT):
        n, manquants = juger(f)
        pages_lues += 1
        total += n
        if manquants:
            ecarts.append((os.path.relpath(f, DEPOT).replace(os.sep, "/"), manquants))
    if not muet:
        print("%d page(s) lues · %d nom(s) de fonction appelés par un bouton · %d page(s) en écart"
              % (pages_lues, total, len(ecarts)))
        print("     NON LU : les addEventListener (une fonction anonyme ne manque jamais), et ce que la\n"
              "     fonction FAIT une fois appelée — cela se mesure au navigateur, dans le banc du lot.")
    if ecarts:
        print("\n⛔ %d page(s) ont un bouton qui appelle une fonction absente — un clic qui ne fait rien, "
              "sans un mot :" % len(ecarts))
        for rel, manquants in ecarts:
            print("  %s\n     → %s" % (rel, ", ".join(m + "()" for m in manquants)))
        return 1
    print("\n✅ chaque bouton appelle une fonction qui existe dans sa page")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
