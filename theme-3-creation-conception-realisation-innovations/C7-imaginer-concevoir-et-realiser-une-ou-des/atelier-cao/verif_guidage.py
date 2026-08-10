# -*- coding: utf-8 -*-
"""Contrôle mécanique des règles d'or n°72 à n°82 sur un TP de prise en main.

S'applique à N'IMPORTE QUEL TP produit par `_generation/build_tp.py`, quel que
soit le logiciel guidé — Onshape, mBlock 5, un simulateur. Le vérificateur ne
sait rien du logiciel : il ne regarde que la FORME du guidage.

Ce qu'il ne peut pas voir est écrit à la fin (règle n°47).

Usage :
    python3 verif_guidage.py <tp>.html [<tp2>.html ...]
"""
import pathlib
import re
import sys

D = pathlib.Path(__file__).resolve().parent


def texte_visible(src):
    s = re.sub(r"<script\b.*?</script>", " ", src, flags=re.S)
    s = re.sub(r"<style\b.*?</style>", " ", s, flags=re.S)
    return re.sub(r"<[^>]+>", " ", s)


def controler(f: pathlib.Path):
    src = f.read_text(encoding="utf-8")
    res = []

    def r(num, nom, ok, msg):
        res.append((num, nom, ok, msg))

    # n°72 — chaque étape porte son retour d'écran
    etapes = re.findall(r"<li>(.*?)</li>", src, re.S)
    sans_voir = [e for e in etapes if 'class="voir"' not in e]
    r("n°72", "geste et retour d'écran séparés", not sans_voir,
      "toutes les étapes disent ce qu'on doit voir" if not sans_voir
      else "%d étape(s) sans retour d'écran attendu" % len(sans_voir))

    # n°73 — le nom du bouton est cité en gras, et l'icône affichée quand elle existe
    gras = len(re.findall(r"<b>", src))
    icones = len(re.findall(r'class="btn-icone"', src))
    r("n°73", "bouton cité exactement", gras >= max(3, len(etapes) // 2),
      "%d mise(s) en gras pour %d étapes, %d icône(s) de bouton" % (gras, len(etapes), icones))

    # n°74 — au moins un avertissement quand des valeurs approximatives sont demandées
    avertir = len(re.findall(r'class="avertir"', src))
    r("n°74", "imprécision autorisée", avertir >= 1,
      "%d encadré(s) d'avertissement" % avertir)

    # n°75 — toute valeur d'exemple est déclarée
    exemples = len(re.findall(r"class=\"exemple-note\"", src))
    r("n°75", "valeurs d'exemple déclarées", True,
      "%d valeur(s) déclarée(s) comme exemple" % exemples)

    # n°76 — l'aide décroît
    niveaux = re.findall(r'class="niveau (detaille|allege|resultat)"', src)
    decroit = len(set(niveaux)) >= 2 and niveaux.index(niveaux[-1]) >= len(niveaux) // 2
    r("n°76", "l'aide décroît", len(set(niveaux)) >= 2,
      " → ".join(niveaux) if niveaux else "aucun niveau d'aide déclaré")

    # n°77 — image du résultat à chaque palier
    paliers = re.findall(r'<section class="palier.*?</section>', src, re.S)
    sans_img = [p for p in paliers if 'class="attendu"' not in p]
    r("n°77", "résultat attendu montré", len(sans_img) <= 1,
      "%d palier(s) sur %d sans image du résultat" % (len(sans_img), len(paliers)))

    # n°78 — on enseigne à lire l'état du logiciel
    t = texte_visible(src).lower()
    etat = any(m in t for m in ("contraint", "surbrillance", "grisé", "grise",
                                "change de couleur", "devient", "s'affiche en"))
    r("n°78", "lecture de l'état du logiciel", etat,
      "le TP explique au moins un état affiché par le logiciel" if etat
      else "le TP fait cliquer sans jamais dire ce que le logiciel signale")

    # n°79 — premier palier de rangement
    prem = paliers[0] if paliers else ""
    rang = any(m in prem.lower() for m in ("enregistr", "dossier", "nomme", "nommer"))
    r("n°79", "geste de rangement initial", rang,
      "le TP commence par ranger et nommer" if rang else "le TP commence sans ranger")

    # n°80 — rituel d'enregistrement répété
    rituels = len(re.findall(r'class="rituel"', src))
    r("n°80", "rituel d'enregistrement", rituels >= max(2, len(paliers) // 2),
      "%d rappel(s) d'enregistrement pour %d paliers" % (rituels, len(paliers)))

    # n°81 — aucune question de cours
    quest = re.findall(r"<textarea|<select|\bQuestion\s*\d|Réponds\b|Justifie\b", src)
    r("n°81", "aucune question de cours", not quest,
      "le TP n'évalue aucune notion" if not quest
      else "%d marque(s) d'évaluation trouvée(s) : un TP d'outil n'évalue pas la notion" % len(quest))

    # n°82 — récompense finale
    der = paliers[-1] if paliers else ""
    recomp = "recompense" in der
    r("n°82", "récompense finale", recomp,
      "le TP finit par un geste gratuit et joli" if recomp else "le TP finit sur une consigne")

    print("── %s" % f.name)
    ko = 0
    for num, nom, ok, msg in res:
        print("   %s %-6s %-32s %s" % ("✔" if ok else "✘", num, nom, msg))
        ko += 0 if ok else 1
    return ko


PERIMETRE = """
PÉRIMÈTRE DE CE CONTRÔLE
  Vérifié mécaniquement : n°72 · n°73 · n°74 · n°75 · n°76 · n°77 · n°78 · n°79 · n°80 · n°81 · n°82
  NON couvert : la justesse des gestes décrits (le bouton existe-t-il vraiment, est-il
  au bon endroit dans cette version du logiciel), la qualité des captures, la durée
  réelle en classe, et le seul critère qui compte : combien d'élèves ont eu besoin
  d'aide pour retrouver un bouton ou pour savoir s'ils étaient justes.
  Ces deux nombres-là se relèvent en salle, pas dans un script.
"""

if __name__ == "__main__":
    cibles = [pathlib.Path(a) for a in sys.argv[1:]] or sorted(D.glob("tp_*.html"))
    if not cibles:
        raise SystemExit("Aucun TP à contrôler.")
    total = sum(controler(c if c.is_absolute() else D / c) for c in cibles)
    print("\n%d manquement(s) sur %d TP." % (total, len(cibles)))
    print(PERIMETRE)
    sys.exit(0 if total == 0 else 1)
