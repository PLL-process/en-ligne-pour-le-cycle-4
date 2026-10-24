# -*- coding: utf-8 -*-
"""Séance 3 du capteur de confort 3e (3e_C7.1, page à défilement continu) : exercices des ateliers FAST et croquis,
au service de 3e_C7.2 (« Proposer et fabriquer un ensemble de solutions pour produire un nouvel OST (croquis, schéma,
graphique, algorithme, modélisation) »). Demande du professeur du 24/10/2026 : la séquence n'avait pas le temps
d'accueillir un exercice (séance 1 : 55 min pour 55 ; séance 2 : 45), d'où une séance 3 de 55 min.

Temps mesuré avant la pose (durées annoncées des activités, hors Bonus) :
  · séance 1 — activités 0, 1, 2 : 10 + 20 + 25 = 55 min (pleine) ;
  · séance 2 — gestes Vittascience, activité 3, REFAIRE : 30 + 15 = 45 min ;
  · séance 3 (nouvelle) — activité 6 : fast 3e e6 (13 min) ; activité 7 : croquis 3e e4 (13) + e6 (12) = 25 min ;
    bilan 7 min → 13 + 25 + 7 = 45 min pour 55. Les trois exercices tiennent : aucun n'est retiré.

Les exercices portent sur la station d'alerte cyclonique ; l'introduction de chaque bloc le dit et les relie au
capteur de confort (mesurer → comparer à un seuil → prévenir).
"""
T3 = "theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/"
SEQ = T3 + "3e/3e_C7.1/sequence_3e_C7_capteur-confort-ny.html"

ENTREES = [
    dict(id="fa-3e-capteur-confort", module="fast", niveau="3e", exos=["e6"],
         sequence=SEQ,
         avant='<div class="exo">\n<button class="btn check" data-check="6" type="button">',
         balise="h3", balise_exo="h4",
         titre="Un FAST à contrôler&nbsp;: celui de la station d'alerte cyclonique",
         intro="Ton capteur de confort et une <b>station d'alerte cyclonique</b> sont construits sur la même idée&nbsp;: "
               "<b>mesurer</b> une grandeur (la température de la salle, la vitesse du vent), la <b>comparer</b> à un seuil, "
               "puis <b>prévenir</b> quelqu'un (le voyant rouge vu depuis la porte, la sirène entendue dans le quartier). "
               "L'exercice porte sur la station, pas sur ton capteur&nbsp;: une équipe a écrit son <b>diagramme FAST</b>, "
               "et il contient trois erreurs. Les trois questions qui les trouvent sont celles que tu poseras au FAST de "
               "ton capteur avant de le fabriquer. Un exercice, environ treize minutes&nbsp;; il se vérifie tout seul et "
               "a sa correction complète.",
         suite="l'exercice qui arbitre entre trois solutions pour diffuser l'alerte, et le QCM de l'atelier"),
    dict(id="cq-3e-capteur-confort", module="croquis", niveau="3e", exos=["e4", "e6"],
         sequence=SEQ,
         avant='<div class="exo">\n<button class="btn check" data-check="7" type="button">',
         balise="h3", balise_exo="h4",
         titre="Proposer par des croquis, puis choisir la bonne représentation",
         intro="Ton capteur de confort aura un boîtier, placé pour qu'on voie le voyant depuis la porte. Avant de le "
               "dessiner pour de bon, on cherche <b>plusieurs façons</b> de le tenir en place, par des croquis rapides. "
               "Les deux exercices portent sur la même <b>station d'alerte cyclonique</b>&nbsp;: d'abord trois façons de "
               "fixer sa sirène sur son poteau, puis les cinq façons de représenter une solution — croquis, schéma, "
               "graphique, algorithme, modélisation 3D — et laquelle choisir selon ce qu'on veut faire. Ton capteur les "
               "demande toutes&nbsp;: l'algorigramme de la séance 2 décrit un algorithme, la température d'un après-midi "
               "se lit sur un graphique, et le boîtier se modélise avant d'être imprimé. Deux exercices, environ "
               "vingt-cinq minutes&nbsp;; chacun se vérifie tout seul et a sa correction complète.",
         suite="l'exercice qui lit un croquis coté pour savoir si un boîtier se fabrique, et le QCM de l'atelier"),
]
