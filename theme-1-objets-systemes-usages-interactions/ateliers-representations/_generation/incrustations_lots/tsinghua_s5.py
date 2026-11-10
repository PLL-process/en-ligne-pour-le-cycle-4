# -*- coding: utf-8 -*-
"""Tsinghua 4e (4e_C1.1 à C1.3) : la séance 5, faite d'exercices des ateliers des représentations.

Les quatre séances (50, 50, 45, 55 min) n'avaient pas le temps d'accueillir un exercice : le professeur a demandé une
séance 5 de 55 min (24/10/2026). La clôture (Bonus → Bilan → QCM) y passe, ce qui libère la séance 4.

    séance 4 : 55 → 45 min   activité 4 seule (le Bilan part en séance 5)
    séance 5 :  0 → 52 min   activité 5 = besoin 4e e4 (12 min, 4e_C1.3) + carte mentale 4e e3 et e4 (15 + 15 min,
                             4e_C1.2), puis Bilan (10 min) ; le Bonus est facultatif, hors temps.

Les deux blocs se suivent dans la même activité : le second continue la numérotation (« Exercice 2 »).
08/11/2026, à la demande de Pascal (« la couper en deux séances ») : la séance 5 dépassait 2 900 mots à lire. Elle garde
le besoin 4e e4 et la carte mentale 4e e3 (activité 5) ; la carte mentale 4e e4 ouvre la séance 6 (activité 6), avant
la clôture (Bonus → Bilan → QCM), qui passe en séance 6. Le vérificateur de l'activité 5 exige
`localStorage["rep_<slug>_4e_<id>"].reussi` des deux premiers exercices, celui de l'activité 6 du troisième.
"""
C1 = "theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/"
SEQ = C1 + "4e/4e_C1.1/sequence_4e_C1.1-C1.3_tsinghua_feux.html"
REPERE = '  <button class="btn small" data-check="5" type="button">'

ENTREES = [
    dict(id="bc-4e-tsinghua-s5", module="besoin", niveau="4e", exos=["e4"],
         sequence=SEQ, avant=REPERE,
         balise="h3", balise_exo="h4",
         titre="a) Justifier une évolution&nbsp;: le jardin passe de l'arrosoir au système connecté",
         intro="<b>Un autre objet, le même raisonnement.</b> En séance 4, le système de détection des feux a évolué parce "
               "que le besoin avait changé. <br>Ici, <b>le jardin partagé d'un collège</b> passe de l'arrosoir à un "
               "système d'arrosage connecté&nbsp;: compare les deux <b>bêtes à cornes</b> pour justifier ce changement. "
               "<br>Environ douze minutes&nbsp;; l'exercice se vérifie tout seul et a sa correction complète.",
         suite="un exercice pour passer du besoin aux caractéristiques, et le QCM de l'atelier"),
    dict(id="cm-4e-tsinghua-s5", module="carte_mentale", niveau="4e", exos=["e3"],
         sequence=SEQ, avant=REPERE, premier_numero=2,
         balise="h3", balise_exo="h4",
         titre="b) Peser le pour et le contre&nbsp;: la carte mentale de l'arrosage connecté",
         intro="<b>Le même jardin, cette fois pour peser le pour et le contre.</b> En séance 3, la détection des feux "
               "avait ses avantages et ses inconvénients&nbsp;; l'arrosage connecté aussi. <br>Pour les ranger face à face, "
               "on dessine une <b>carte mentale</b>&nbsp;: complète celle du club jardin. <br>Environ un quart d'heure&nbsp;; "
               "l'exercice se vérifie tout seul et a sa correction complète.",
         suite="un exercice pour corriger une carte mentale mal faite (en séance 6), et le QCM de l'atelier"),
    # 08/11/2026 : la séance 5 coupée en deux, à la demande de Pascal (« la couper en deux séances ») — sa lecture
    # dépassait 2 900 mots. Le troisième exercice ouvre la séance 6, avant la clôture.
    dict(id="cm-4e-tsinghua-s6", module="carte_mentale", niveau="4e", exos=["e4"],
         sequence=SEQ, avant='  <button class="btn small" data-check="6" type="button">',
         balise="h3", balise_exo="h4",
         titre="Une carte mentale qui se lit mal",
         intro="Environ un quart d'heure&nbsp;; l'exercice se vérifie tout seul et a sa correction complète.",
         suite="le QCM de l'atelier"),
]
