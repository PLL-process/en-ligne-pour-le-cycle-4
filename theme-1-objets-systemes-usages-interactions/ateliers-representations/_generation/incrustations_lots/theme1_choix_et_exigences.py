# -*- coding: utf-8 -*-
"""Thème 1 — choisir un OST, caractéristiques, exigences, modes de représentation.

Les ateliers « besoin » (bête à cornes), « exigences » (flexibilité) et « cas d'utilisation » (choisir le mode)
entrent dans quatre séquences du thème 1. Chaque exercice tient dans le temps libre de la séance qui l'accueille
(séance de 55 min) ; les minutes sont comptées dans l'annonce de l'activité hôte.

    5e Shanghai (5e_C3.3)      séance 1 : 30 → 45 min   besoin 5e e1 + e3, en tête de l'activité 1
    4e Hangzhou (4e_C3.1)      séance 1 : 35 → 45 min   besoin 4e e5, en tête de l'activité 1
    3e Shenzhen (3e_C3.1)      séance 1 : 35 → 47 min   besoin 3e e6, en tête de l'activité 1
    3e Shenzhen (3e_C3.3)      séance 2 : 35 → 43 min   exigences 3e e5, avant « b) Construire la grille »
    3e Pékin (3e_C2.1)         séance 3 : 30 → 43 min   cas d'utilisation 3e e6, en tête de l'activité 4
                                                        (+ bilan personnel facultatif 10 min : 53 min)

Non posé ici : 4e Tsinghua (4e_C1.2, 4e_C1.3) — séances de 50, 50, 45 et 55 min ; au plus 10 min libres (séance 3),
alors que « Le besoin évolue » (besoin 4e e4) demande 12 min et la carte mentale 4e e3, 15 min.
Repris le 24/10/2026 dans une séance 5 créée pour eux (demande du professeur) : voir `tsinghua_s5.py`.
"""
T1 = "theme-1-objets-systemes-usages-interactions/"
C2 = T1 + "C2-decrire-les-interactions-entre-un-objet-ou/"
C3 = T1 + "C3-caracteriser-et-choisir-un-objet-ou-un/"

ENTREES = [
    dict(id="bc-5e-shanghai-c3", module="besoin", niveau="5e", exos=["e1", "e3"],
         sequence=C3 + "5e/5e_C3.1/sequence_5e_C3.1-C3.4_shanghai.html",
         avant='  <figure class="fig">\n    <img src="Images/trois_solutions_shanghai.svg"',
         balise="h4", balise_exo="h5",
         titre="D'abord le besoin&nbsp;: la bête à cornes d'un autre vélo-cargo",
         intro="Avant de dire de quoi les trois véhicules sont faits, il faut savoir à quoi ils doivent servir&nbsp;: "
               "c'est leur <b>besoin</b>. On l'exprime souvent avec un schéma, la <b>bête à cornes</b>. Entraîne-toi "
               "sur un autre vélo-cargo, celui de <b>Léa</b>, qui emmène ses enfants et ses courses en ville&nbsp;: "
               "lis sa bête à cornes, puis choisis l'objet qui répond à son besoin. Deux exercices, environ un quart "
               "d'heure&nbsp;; chacun se vérifie tout seul et a sa correction complète. Le même geste servira en "
               "séance 4, pour choisir entre S1, S2 et S3.",
         suite="un exercice pour compléter la bête à cornes d'un lampadaire, et le QCM de l'atelier"),
    dict(id="bc-4e-hangzhou-c3", module="besoin", niveau="4e", exos=["e5"],
         sequence=C3 + "4e/4e_C3.1/sequence_4e_C3.1-C3.3_hangzhou.html",
         avant='  <figure class="fig">\n    <img src="Images/du_besoin_aux_caracteristiques.svg"',
         balise="h4", balise_exo="h5",
         titre="D'abord la méthode&nbsp;: de la bête à cornes aux caractéristiques",
         intro="Le maire a dit son besoin en une phrase&nbsp;; pour choisir, il faut en tirer des "
               "<b>caractéristiques</b> que l'on peut comparer d'un modèle à l'autre. Entraîne-toi d'abord sur un autre "
               "objet, le <b>système d'arrosage connecté</b> d'un jardin partagé, dont le besoin est écrit dans une "
               "<b>bête à cornes</b>&nbsp;: chaque partie du besoin demande une caractéristique, et ce qui ne sert pas "
               "le besoin ne compte pas. Un exercice, environ dix minutes&nbsp;; il se vérifie tout seul et a sa "
               "correction complète.",
         suite="un exercice sur le besoin qui évolue, de l'arrosoir au système connecté, et le QCM de l'atelier"),
    dict(id="bc-3e-shenzhen-c3", module="besoin", niveau="3e", exos=["e6"],
         sequence=C3 + "3e/3e_C3.1/sequence_3e_C3.1-C3.4_shenzhen.html",
         avant="  <p><b>Consigne.</b> Avant toute chose, et <b>avant d'ouvrir le tableau de données</b>",
         balise="h4", balise_exo="h5",
         titre="D'abord la méthode, sur un autre besoin&nbsp;: l'alerte cyclonique",
         intro="Établir une liste, c'est partir d'un <b>besoin</b> écrit sans solution, puis chercher des objets ou "
               "des systèmes techniques dans plusieurs familles. Avant le local de Shenzhen, entraîne-toi sur un besoin "
               "plus proche de nous&nbsp;: prévenir les habitants d'un quartier de Sainte-Luce de l'arrivée d'un "
               "cyclone. Un exercice, environ douze minutes&nbsp;; il se vérifie tout seul et a sa correction complète.",
         suite="un exercice sur le besoin mal formulé qui ferme la liste, et le QCM de l'atelier"),
    dict(id="ex-3e-shenzhen-c3", module="exigences", niveau="3e", exos=["e5"],
         sequence=C3 + "3e/3e_C3.1/sequence_3e_C3.1-C3.4_shenzhen.html",
         avant="  <h4>b) Construire la grille</h4>",
         balise="h4", balise_exo="h5",
         titre="Avant la grille&nbsp;: ce que le client accepte, la flexibilité",
         intro="Une exigence a un <b>niveau</b>&nbsp;; elle a aussi une <b>flexibilité</b>&nbsp;: l'écart que le "
               "client accepte sans refuser la solution. Une exigence qui n'accepte aucun écart écarte toute solution "
               "qui ne l'atteint pas, quel que soit son score&nbsp;; une exigence très négociable peut seulement peser "
               "dans la grille. Entraîne-toi sur un autre objet&nbsp;: la <b>station d'alerte cyclonique</b> d'un "
               "quartier de Martinique, dont la cliente, la présidente du comité de quartier, dit ce qu'elle accepte. "
               "Un exercice, environ huit minutes&nbsp;; il se vérifie tout seul et a sa correction complète.",
         suite="l'évaluation de deux boîtiers exigence par exigence, l'arbitrage entre eux, et le QCM de l'atelier"),
    dict(id="cu-3e-pekin-c2", module="cas_utilisation", niveau="3e", exos=["e6"],
         sequence=C2 + "3e/3e_C2.1/sequence_3e_C2_pekin_borne.html",
         avant="  <p>Tu as produit l'algorigramme du technicien.",
         balise="h4", balise_exo="h5",
         titre="D'abord, choisir le mode selon la question",
         intro="Un mode de représentation n'est jamais bon en soi&nbsp;: il est bon pour une <b>question</b>, et pour "
               "un destinataire. Avant de produire, un dernier entraînement sur une autre borne, celle d'une station de "
               "vélos du front de mer&nbsp;: six questions, et pour chacune le mode qui y répond. Deux modes s'ajoutent "
               "aux six de la séquence&nbsp;: le <b>diagramme de cas d'utilisation</b> (qui fait quoi avec le système) "
               "et le <b>diagramme des interacteurs</b> (tout ce qui entoure l'objet)&nbsp;; le cours, juste en dessous, "
               "les présente. Un exercice, environ un quart d'heure&nbsp;; il se vérifie tout seul et a sa correction "
               "complète.",
         suite="la construction du diagramme d'une station d'alerte cyclonique, et le QCM de l'atelier"),
]
