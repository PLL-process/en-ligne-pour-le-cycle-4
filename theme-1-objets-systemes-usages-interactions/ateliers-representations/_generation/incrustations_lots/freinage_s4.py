# -*- coding: utf-8 -*-
"""Incrustation de l'atelier FAST (module `fast`) dans la séquence 5e_C1.2 « Sainte-Luce : quel frein pour les
vélos du collège ? », en séance 4.

Écartée le 24/10/2026 faute de temps (10 / 5 / 5 min libres par séance, voir `fast_et_flexibilite.py`), elle entre
avec la séance 4 de 55 min que le professeur a demandée le même jour, faite d'exercices :

    séance 4 « Conseiller »   activité 4 (~15 min) : fast 5e e3 « Deux principes pour une même fonction » (14 min,
                                                     le freinage du vélo-cargo de Léa), cours replié compris
                              activité 5 (~25 min) : Léa dans la grande descente (écrite dans la séquence)
                              bilan (~10 min)        → 50 min annoncées pour 55

Le vérificateur de l'activité 4 lit `localStorage["rep_fast_5e_e3"].reussi` ; la sauvegarde de la séquence exclut
`.atelier-incruste`.
"""
T1 = "theme-1-objets-systemes-usages-interactions/"
C1 = T1 + "C1-decrire-les-liens-entre-usages-et-evolutions/"

ENTREES = [
    dict(id="fa-5e-freinage", module="fast", niveau="5e", exos=["e3"],
         sequence=C1 + "5e/5e_C1.2/sequence_5e_C1.2_sainte_luce_freinage.html",
         avant='  <button class="btn small" data-check="4" type="button">',
         balise="h3", balise_exo="h4",
         titre="Deux principes dans un même schéma&nbsp;: le diagramme FAST du vélo-cargo",
         intro="Pour les vélos du collège, les trois principes de freinage étaient rangés dans un tableau. Les "
               "concepteurs les rangent aussi dans un schéma, le <b>diagramme FAST</b>&nbsp;: quand une fonction peut "
               "être réalisée de deux façons, sa ligne porte <b>deux cases reliées par «&nbsp;ou&nbsp;»</b>. Voici un "
               "extrait de celui du vélo-cargo de <b>Léa</b>, et un choix à faire pour elle&nbsp;; le cours, juste en "
               "dessous, présente le schéma. Un exercice d'environ un quart d'heure&nbsp;; il se vérifie tout seul et "
               "a sa correction complète.",
         suite="les exercices qui lisent puis complètent le diagramme FAST d'un lampadaire, et le QCM de l'atelier"),
]
