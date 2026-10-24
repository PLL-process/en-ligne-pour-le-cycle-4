# -*- coding: utf-8 -*-
"""Séance 6 du lampadaire intelligent (5e_C4.1 → C4.8) : l'atelier FAST, exercice 2, en réinvestissement.

La séance 5 annonçait 25 + 25 + 25 = 75 min pour 55. Le réinvestissement (la sonnette connectée)
et la clôture (synthèse, Bonus, bilan, QCM) passent dans une séance 6 ; la séance 5 garde le réseau
local et le jeu du courrier (50 min).

  POSÉ
  · fast 5e e2 « Compléter les solutions techniques » (10 min), dans l'activité 7 « Le FAST du
    lampadaire, complet », en tête de la séance 6 : 10 + 25 (sonnette) = 35 min d'activités,
    le reste pour la synthèse, le bilan et le renvoi au QCM. L'exercice remplit les trois cases
    que le FAST de la séance 1 (exercice e1, entrée `fa-5e-lampadaire` de fast_et_flexibilite.py)
    laissait cachées, avec ce que les séances 2 (qui capte, qui stocke) et 3 (qui repère un passage)
    ont établi ; son intrus (l'interrupteur à bouton) et sa lecture « pourquoi ? » de la batterie
    préparent la première question de la sonnette (fonction → solution, sur un objet inconnu).
    Le cours replié est gardé : plusieurs semaines séparent la séance 1 de la séance 6.

  ÉCARTÉ
  · besoin 5e e2 « Compléter la bête à cornes du lampadaire » (10 min) : son code est 5e_C3.3
    (choisir un objet pour répondre à un besoin), hors des huit codes de la séquence ; il n'en
    exerce aucun.
"""
T2 = "theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/"

ENTREES = [
    dict(id="fa-5e-lampadaire-s6", module="fast", niveau="5e", exos=["e2"],
         sequence=T2 + "5e/5e_C4.1/sequence_5e_C4.1-C4.8_lampadaire_intelligent.html",
         avant='    <div class="exo"><p>Quand l\'exercice du FAST affiche',
         balise="h4", balise_exo="h5",
         titre="Retour au diagramme FAST de la séance 1",
         intro="Le diagramme FAST de la séance 1 cachait trois solutions, sur les lignes «&nbsp;détecter un "
               "passant&nbsp;», «&nbsp;stocker l'énergie pour la nuit&nbsp;» et «&nbsp;capter l'énergie du "
               "soleil&nbsp;». Depuis, la chaîne d'énergie (séance 2) a dit qui capte et qui stocke, et la "
               "chaîne d'information (séance 3) qui repère un passage. Remplis maintenant ces trois cases, "
               "écarte l'intrus, puis remonte de la batterie jusqu'à la fonction d'usage&nbsp;: tout le "
               "lampadaire tient alors dans un seul schéma. Un exercice d'environ dix minutes&nbsp;; il se "
               "vérifie tout seul et a sa correction complète.",
         suite="l'exercice qui lit ce FAST dans les deux sens, un autre sur deux principes de freinage, "
               "et le QCM de l'atelier"),
]
