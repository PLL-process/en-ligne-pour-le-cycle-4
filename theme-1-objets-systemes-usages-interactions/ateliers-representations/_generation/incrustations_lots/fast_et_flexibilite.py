# -*- coding: utf-8 -*-
"""Incrustations des ateliers FAST (module `fast`) et diagramme pieuvre (module `interacteurs`)
dans cinq séquences des thèmes 2 et 3. Trois posées, deux écartées faute de temps.

Le temps a été mesuré séance par séance avant la pose : somme des durées annoncées des activités
de chaque séance, contre 55 min. Un exercice n'entre que dans le temps libre de SA séance.

  POSÉES
  · lampadaire 5e (5e_C4.1) — fast 5e e1 « Lire le FAST du lampadaire » (10 min), en tête de
    l'activité 1 : séance 1, 40 → 50 min. e1 plutôt que e2 : l'activité associe déjà fonctions
    et solutions (dont les trois solutions que e2 fait compléter) ; ce qui lui manque, c'est la
    différence verbe / nom et la lecture du FAST dans les deux sens. Les deux ne tiennent pas
    ensemble (20 min pour 15 de libres).
  · jardin connecté 4e (4e_C4.1) — interacteurs 4e e6 « Le cahier des charges : critère, niveau,
    flexibilité » (15 min), demande du professeur, en tête de l'activité 5 : séance 4,
    40 → 55 min. La séquence ne parle nulle part de cahier des charges ; la séance 4 est la seule
    à avoir le temps, et son enquête porte sur les pièces du jardin (le boîtier de la carte, qui
    la protège de la pluie : c'est la contrainte « résister à la pluie, IPX4 »).
  · jardin-conception 4e (4e_C7.2) — fast 4e e5 « Ajouter une fonction au jardin » (15 min), en
    tête du REFAIRE. La page n'écrit pas où passe la séance : le seul découpage qui tient coupe
    après l'activité 2 (10 + 15 + 25 = 50 | 20 + 15 = 35). En tête de l'activité 2, la séance 1
    passerait à 65 min ; en tête du REFAIRE, la séance 2 passe de 35 à 50 min.

  ÉCARTÉES ICI (non posées dans le temps existant, exercices non raccourcis)
  · freinage 5e (5e_C1.2) — fast 5e e3 (14 min) : 10 / 5 / 5 min libres par séance.
  · jardin connecté 4e — fast 4e e4 (18 min) : 6 / 0 / 10 / 15 min libres, et la séance 4 est
    pleine une fois e6 posé (priorité à e6).
  · capteur de confort 3e (3e_C7.2) — fast 3e e6 (13 min) : 100 min d'activités pour 110, la
    séance 1 pleine (55), la séance 2 à 45 (10 min libres).

  REPRISES LE 24/10/2026 (demande du professeur : « une autre séance de 55 min »)
  · freinage 5e — fast 5e e3 posé dans une séance 4 créée pour lui : `freinage_s4.py`.
  · capteur de confort 3e — fast 3e e6 posé dans une séance 3 créée pour lui : `capteur_ny_s3.py`.
  · lampadaire 5e — fast 5e e2 posé dans une séance 6 : `lampadaire_s6.py`.
"""
T2 = "theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/"
T3 = "theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/"

ENTREES = [
    dict(id="fa-5e-lampadaire", module="fast", niveau="5e", exos=["e1"],
         sequence=T2 + "5e/5e_C4.1/sequence_5e_C4.1-C4.8_lampadaire_intelligent.html",
         avant='    <object class="figure" data="Images/lampadaire_fonctions_solutions.svg"',
         balise="h4", balise_exo="h5",
         titre="Pour commencer&nbsp;: le diagramme FAST d'un lampadaire",
         intro="Le schéma annoté, plus bas, relie chaque élément du lampadaire du parking à ce qu'il fait. "
               "Les concepteurs rangent ces informations dans un <b>diagramme FAST</b>, qui se lit dans deux "
               "sens&nbsp;: voici celui d'un lampadaire voisin, dans la rue qui monte au collège. Trois de ses "
               "solutions sont cachées&nbsp;: la partie a), juste après, te les fait retrouver. Un exercice "
               "d'environ dix minutes&nbsp;; il se vérifie tout seul et a sa correction complète.",
         suite="l'exercice qui complète ses trois solutions cachées, un autre sur deux principes de freinage, "
               "et le QCM de l'atelier"),
    dict(id="pv-4e-jardin-connecte", module="interacteurs", niveau="4e", exos=["e6"],
         sequence=T2 + "4e/4e_C4.1/sequence_4e_C4.1-C4.9_jardin_connecte.html",
         avant='    <div class="consigne"><b>Consigne :</b> pour chaque pièce, lis les INDICES',
         balise="h4", balise_exo="h5",
         titre="D'abord, le cahier des charges&nbsp;: ce que le système doit garantir",
         intro="Les pièces du jardin ne sont pas choisies au hasard&nbsp;: le boîtier de la carte, par exemple, "
               "doit la protéger de la pluie. Ces contraintes s'écrivent dans le <b>cahier des charges</b> du "
               "système, chacune avec un critère, un niveau et une <b>flexibilité</b>, notée de F0 à F3. "
               "Entraîne-toi sur celui d'un système d'arrosage très proche de celui du collège&nbsp;: le "
               "jardin partagé d'un quartier, et sa gardienne. Un exercice d'environ un quart d'heure&nbsp;; "
               "il se vérifie tout seul et a sa correction complète.",
         suite="le diagramme pieuvre de ce même système, ce que son concepteur a oublié, et le QCM de l'atelier"),
    dict(id="fa-4e-jardin-conception", module="fast", niveau="4e", exos=["e5"],
         sequence=T3 + "4e/4e_C7.1/sequence_4e_C7_jardin-conception.html",
         avant='<div class="exo">\n<p>Nouveau besoin&nbsp;: une <b>jardinière de balcon</b>',
         balise="h3", balise_exo="h4",
         titre="Refaire sur un système qui existe&nbsp;: lui ajouter une fonction",
         intro="La sonde que protège ton boîtier sert à arroser tout seul quand la terre est sèche. Voici un "
               "système d'arrosage de ce genre, déjà construit, dans le jardin partagé d'un autre quartier&nbsp;: "
               "sa gardienne lui demande une <b>nouvelle fonction</b>. Tu complètes son <b>diagramme FAST</b> — "
               "la fonction qui manque, sa solution, et ce qui change ailleurs —, puis tu déroules la démarche "
               "sur la jardinière de balcon. Un exercice d'environ un quart d'heure&nbsp;; il se vérifie tout "
               "seul et a sa correction complète.",
         suite="l'exercice qui relie chaque constituant de ce système à sa fonction, et le QCM de l'atelier"),
]
