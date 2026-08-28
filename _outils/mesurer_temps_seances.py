# -*- coding: utf-8 -*-
"""mesurer_temps_seances.py — le temps annoncé par chaque séquence, mesuré.

Deux chiffres par séquence :

  - le **bandeau**   : « N séances de NN min » → le temps que la page s'attribue
  - les **activités**: somme des durées écrites, hors bonus et facultatif
                       → le temps qu'elle demande vraiment

Pourquoi cet outil existe
─────────────────────────
Il a fallu trois erreurs, toutes la même, pour l'écrire.

  1. J'ai cherché « ⏱ N séances de NN min ». Quatre pages écrivent la phrase
     sans l'emoji juste devant. Je les ai déclarées « sans durée annoncée » et
     j'en ai fait une découverte. Je comptais l'emoji.
  2. J'ai cherché le critère « 9/9 ». La page écrit « 9 / 9 ». J'ai déclaré
     fausse une affirmation d'audit qui était exacte. Je comptais les espaces.
  3. J'ai lu les durées d'activité sur « ⏱ NN min ». Une page écrit
     « ⏱ ≈ NN min ». Elle est ressortie à 4 minutes d'activité pour trois
     séances. Je comptais le signe.

C'est trois fois la règle d'or n°184 — un indicateur bâti sur une convention
d'écriture mesure la convention, pas la chose. Et trois fois commise dans le
document qui reprochait la même chose à trois audits externes.

Le remède n'est pas « faire attention » : c'est le CONTRÔLE ci-dessous. Une
séquence qui ressort à zéro n'est pas un résultat, c'est une panne de lecture —
et le script refuse alors de rendre un tableau. Règle d'or n°194.

Usage : python3 _outils/mesurer_temps_seances.py
"""

import html
import os
import re
import sys

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

#: « 3 séances de 55 min », avec ou sans ⏱ devant, avec ou sans accent.
BANDEAU = re.compile(r"(\d+)\s*s[ée]ances?\s*de\s*(\d+)\s*min", re.I)

#: « ⏱ 20 min », « ⏱ ≈ 20 min », « (~20 min) », « (25 min) ».
ACTIVITE = re.compile(r"(?:⏱|\()\s*[~≈≃]?\s*(\d{1,3})\s*min", re.I)

FACULTATIF = re.compile(r"bonus|facultat", re.I)


def texte_plat(chemin):
    with open(chemin, encoding="utf-8") as f:
        t = f.read()
    t = re.sub(r"<script.*?</script>", " ", t, flags=re.S)
    t = re.sub(r"<style.*?</style>", " ", t, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t)))


def sequences(racine):
    for dossier, _, fichiers in os.walk(racine):
        for f in sorted(fichiers):
            if re.match(r"sequence.*\.html$", f, re.I):
                yield os.path.join(dossier, f)


def mesurer(chemin):
    t = texte_plat(chemin)
    m = BANDEAU.search(t)
    nb, unite = (int(m.group(1)), int(m.group(2))) if m else (0, 0)

    obligatoire = facultatif = 0
    for mm in ACTIVITE.finditer(t):
        avant = t[max(0, mm.start() - 130):mm.start()]
        apres = t[mm.end():mm.end() + 22]
        if re.search(r"s[ée]ances?\s*de\s*$", avant):
            continue                                   # c'est le bandeau
        if FACULTATIF.search(avant) or FACULTATIF.search(apres):
            facultatif += int(mm.group(1))
        else:
            obligatoire += int(mm.group(1))

    return dict(fichier=os.path.basename(chemin), seances=nb, unite=unite,
                annonce=nb * unite, obligatoire=obligatoire, facultatif=facultatif)


#: Une séquence dont on ne lit AUCUNE durée d'activité est presque toujours une
#: panne de lecture, pas une page sans durées. On le dit, et on s'arrête.
def controle(mesures):
    muettes = [m["fichier"] for m in mesures if not m["obligatoire"]]
    return muettes


def main(argv):
    racine = argv[1] if len(argv) > 1 else os.path.join(
        RACINE, "theme-2-structure-fonctionnement-comportement")
    mesures = [mesurer(p) for p in sequences(racine)]
    if not mesures:
        print("Aucune séquence sous %s" % racine)
        return 1

    print("%-54s %-13s %-8s %-10s %-11s %s" % (
        "séquence", "bandeau", "= min", "activités", "facultatif", "marge"))
    print("─" * 118)
    for m in sorted(mesures, key=lambda x: x["fichier"]):
        if not m["annonce"]:
            marge = "AUCUN BANDEAU"
        else:
            d = m["annonce"] - m["obligatoire"]
            marge = "%+d min" % d if d else "0 — pile au bord"
        print("%-54s %-13s %-8s %-10s %-11s %s" % (
            m["fichier"][:52],
            "%d × %d min" % (m["seances"], m["unite"]) if m["seances"] else "—",
            m["annonce"] or "—", m["obligatoire"] or "—", m["facultatif"] or "—", marge))

    unites = sorted({m["unite"] for m in mesures if m["unite"]})
    serrees = [m for m in mesures if m["annonce"] and m["annonce"] - m["obligatoire"] <= 0]
    sans = [m["fichier"] for m in mesures if not m["annonce"]]

    print()
    print("%d séquences · %d annoncent un bandeau · unité(s) écrite(s) : %s"
          % (len(mesures), len(mesures) - len(sans), unites))
    print("Sans bandeau : %s" % (", ".join(sans) or "aucune"))
    print("Sans marge   : %s" % (", ".join(
        "%s (%+d)" % (m["fichier"][:40], m["annonce"] - m["obligatoire"]) for m in serrees) or "aucune"))

    muettes = controle(mesures)
    if muettes:
        print()
        print("⛔ CONTRÔLE — %d séquence(s) sans aucune durée d'activité lue :" % len(muettes))
        for f in muettes:
            print("     %s" % f)
        print("   Une page de séance sans une seule durée est presque toujours une panne")
        print("   de lecture (une écriture non prévue par ACTIVITE), pas une page sans")
        print("   durées. Vérifier à la main AVANT de publier ce tableau. Règle n°194.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
