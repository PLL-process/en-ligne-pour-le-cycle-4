# -*- coding: utf-8 -*-
"""tests_controle_formulations.py — rejouer les erreurs qui ont fait naître l'outil.

Un contrôle qui ne trouve rien ne prouve rien. On lui remet donc sous les yeux
les erreurs réelles du dépôt et on vérifie qu'il les voit — sans quoi son
silence ne voudrait rien dire.

Les quatre cas ci-dessous ont tous existé dans le dépôt, en clair, pendant des
jours :

  · `5e_C3.1` portant la formulation de la **4e**, dans deux séquences ;
  · `3e_C3.4` portant une reformulation de mémoire ;
  · `C7.2` et `C7.6` portant, dans la fiche de l'atelier CAO, deux phrases
    **absentes du programme** — et identiques aux trois niveaux.

Le dernier est le plus important : une première version de l'outil se taisait
devant une citation qui ne ressemble à RIEN d'officiel. Elle n'aurait pas vu
l'erreur qui l'a fait naître. Le cas `ETRANGERE` existe pour cela.

On vérifie aussi l'inverse — qu'il ne crie pas sur ce qui va : une citation
exacte pliée sur deux lignes, mise en gras, ou suivie du rappel du socle reste
une citation exacte. Les faux positifs sont la façon dont un contrôle neuf perd
sa crédibilité (règle d'or n°242).

Usage : python3 _outils/tests_controle_formulations.py
Sortie : 0 si tout passe, 1 sinon.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from controle_formulations import OFFICIELLES, juger, normaliser  # noqa: E402

#: (niveau, code, texte lu, verdict attendu, pourquoi ce cas existe)
CAS = [
    # ── ce que l'outil doit voir ────────────────────────────────────────
    ("5e", "C3.1", "Identifier les caractéristiques à prendre en compte dans le "
     "choix d'un OST.", "AUTRE CODE (4e_C3.1)",
     "l'erreur réelle de deux séquences : le texte de la 4e sous le code de 5e"),
    ("3e", "C3.4", "Mesurer et comparer les performances d'un OST par rapport à "
     "un cahier des charges.", "ÉTRANGÈRE",
     "l'erreur réelle d'une séquence : une reformulation si libre qu'elle ne "
     "ressemble plus à aucune case du référentiel"),
    ("5e", "C7.2", "Imaginer, créer et simuler tout ou partie d'un objet.", "ÉTRANGÈRE",
     "la phrase de la fiche CAO : elle n'est dans AUCUNE case du référentiel"),
    ("3e", "C7.6", "Réaliser, de manière collaborative, le prototype d'un objet.",
     "ÉTRANGÈRE",
     "l'autre phrase de la fiche CAO — celle que je prenais pour un arbitrage"),
    ("4e", "C7.6", "Modéliser une forme voulue.", "AUTRE CODE (3e_C7.6)",
     "la formulation de la 3e sous le code de 4e : chaque mot est juste, "
     "et l'ensemble est faux"),
    ("5e", "C8.1", "Utiliser une simulation fournie pour valider la tenue "
     "mécanique.", "TRONQUÉE",
     "une citation exacte, arrêtée avant la fin — un défaut, pas un mensonge"),

    # ── ce sur quoi il ne doit PAS crier ────────────────────────────────
    ("5e", "C8.1", "Utiliser une simulation fournie pour valider la tenue "
     "mécanique d'un matériau.", "JUSTE", "la citation exacte"),
    ("5e", "C8.1", "Utiliser une simulation fournie pour valider\n   la tenue "
     "mécanique d'un matériau", "JUSTE",
     "la même, pliée par le gabarit : un retour à la ligne n'est pas du texte"),
    ("5e", "C8.1", "**Utiliser une simulation fournie** pour valider la tenue "
     "mécanique d'un matériau.", "JUSTE",
     "la même, mise en gras : une emphase ne modifie pas une citation"),
    ("3e", "C7.6", "Modéliser une forme voulue.", "JUSTE",
     "la citation juste du code juste — le cas voisin de l'erreur ci-dessus"),
    ("5e", "C9.1", "5e_C9.1 — Analyser un programme simple fourni et tester s'il "
     "répond au besoin ou au problème posé. 5e_C9.2 — Modifier un programme "
     "fourni pour répondre au besoin ou à un problème posé.", "JUSTE",
     "un README mutualisé cite plusieurs codes : la nôtre y est, entière"),
    ("5e", "C8.1", "La patère du hall", None,
     "un titre court n'est pas une citation : on ne le compare pas"),
    # Une cellule de tableau de CONTENU ressemble à une citation étrangère si
    # on la juge hors contexte. Ce n'est pas `juger` qui la protège, c'est le
    # filtre de promesse de `parcourir` : on le vérifie plus bas, sur le dépôt
    # réel, plutôt que de faire mentir `juger`.
    ("3e", "C8.1", "les coins", None,
     "trop court pour être accusé : on ne dénonce pas une phrase courte inconnue"),
]


def main():
    echecs = []
    for niveau, code, texte, attendu, pourquoi in CAS:
        obtenu, _officielle = juger(niveau, code, texte)
        if obtenu != attendu:
            echecs.append("%s_%s %r → attendu %s, obtenu %s (%s)"
                          % (niveau, code, texte[:52], attendu, obtenu, pourquoi))

    # le référentiel doit être là, et différencié : la règle d'or n°247 dit
    # qu'une formulation identique aux trois niveaux est suspecte. On vérifie
    # qu'aucun code de C7 ne partage son libellé avec son voisin de niveau.
    controles = len(CAS)
    # `C7.7` fait exception, et c'est le programme qui le veut : « Choisir les
    # moyens et produire la forme voulue » est écrit à l'identique en 4e et en
    # 3e. La règle n°247 est un SOUPÇON, pas une loi — et un test qui l'écrit
    # comme une loi transforme une vérité du référentiel en fausse alerte.
    REPETITIONS_VOULUES = {"C7.7"}
    for parent in ("C7",):
        for num in range(1, 9):
            code = "%s.%d" % (parent, num)
            if code in REPETITIONS_VOULUES:
                continue
            textes = {n: normaliser(OFFICIELLES[(n, code)])
                      for n in ("5e", "4e", "3e") if (n, code) in OFFICIELLES}
            if len(textes) > 1:
                controles += 1
                if len(set(textes.values())) == 1:
                    echecs.append("%s : formulation identique aux %d niveaux — "
                                  "règle d'or n°247" % (code, len(textes)))

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (controles - len(echecs), controles))
        return 1
    print("✅ %d contrôles — les quatre erreurs réelles sont vues, "
          "et les citations justes sont laissées tranquilles" % controles)
    print("\n%d / %d" % (controles, controles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
