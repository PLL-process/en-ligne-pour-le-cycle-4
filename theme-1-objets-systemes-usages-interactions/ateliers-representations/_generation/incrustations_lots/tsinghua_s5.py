# -*- coding: utf-8 -*-
"""Tsinghua 4e (4e_C1.1 à C1.3) : la séance 5, faite d'exercices des ateliers des représentations.

Les quatre séances (50, 50, 45, 55 min) n'avaient pas le temps d'accueillir un exercice : le professeur a demandé une
séance 5 de 55 min (24/10/2026). La clôture (Bonus → Bilan → QCM) y passe, ce qui libère la séance 4.

    séance 4 : 55 → 45 min   activité 4 seule (le Bilan part en séance 5)
    séance 5 :  0 → 52 min   activité 5 = besoin 4e e4 (12 min, 4e_C1.3) + carte mentale 4e e3 et e4 (15 + 15 min,
                             4e_C1.2), puis Bilan (10 min) ; le Bonus est facultatif, hors temps.

Les deux blocs se suivent dans la même activité : le second continue la numérotation (« Exercice 2 », « Exercice 3 »).
Le vérificateur de l'activité 5 exige `localStorage["rep_<slug>_4e_<id>"].reussi` des trois exercices.
"""
C1 = "theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/"
SEQ = C1 + "4e/4e_C1.1/sequence_4e_C1.1-C1.3_tsinghua_feux.html"
REPERE = '  <button class="btn small" data-check="5" type="button">'

ENTREES = [
    dict(id="bc-4e-tsinghua-s5", module="besoin", niveau="4e", exos=["e4"],
         sequence=SEQ, avant=REPERE,
         balise="h3", balise_exo="h4",
         titre="a) Justifier une évolution&nbsp;: le jardin passe de l'arrosoir au système connecté",
         intro="<b>Un autre objet, le même raisonnement.</b> En séance 4, le système de détection des feux a évolué&nbsp;: "
               "d'un seuil de température seul au croisement de plusieurs indices, parce que le besoin avait changé — moins "
               "de fausses alertes. Ici, ni forêt ni feu&nbsp;: <b>le jardin partagé d'un collège</b>, qui passe de "
               "l'arrosoir à un système d'arrosage connecté. Pour justifier ce changement, tu compares deux <b>bêtes à "
               "cornes</b>, le schéma du besoin&nbsp;; le cours, juste en dessous, le rappelle. Comme tes exigences, le "
               "nouveau but ne nomme aucune solution. Un exercice, environ douze minutes&nbsp;; il se vérifie tout seul et "
               "a sa correction complète.",
         suite="un exercice pour passer du besoin aux caractéristiques, et le QCM de l'atelier"),
    dict(id="cm-4e-tsinghua-s5", module="carte_mentale", niveau="4e", exos=["e3", "e4"],
         sequence=SEQ, avant=REPERE, premier_numero=2,
         balise="h3", balise_exo="h4",
         titre="b) Peser le pour et le contre&nbsp;: la carte mentale de l'arrosage connecté",
         intro="<b>Le même jardin, cette fois pour peser le pour et le contre.</b> En séance 3, la détection automatisée "
               "des feux avait ses deux faces&nbsp;: du temps gagné, mais aussi des fausses alertes, un coût, de l'énergie "
               "consommée. L'arrosage connecté est <b>un autre objet</b>, et il a lui aussi ses avantages et ses "
               "inconvénients. Pour les ranger face à face sans rien oublier, on dessine une <b>carte mentale</b>&nbsp;: "
               "complète celle du club jardin, puis corrige la carte mal faite d'un élève. Deux exercices, environ un quart "
               "d'heure chacun&nbsp;; chacun se vérifie tout seul et a sa correction complète.",
         suite="le QCM de l'atelier"),
]
