# -*- coding: utf-8 -*-
"""Incrustations — lot « données et validation » : carte mentale (5e, 3e) et diagramme des exigences (4e).

Trois séquences, une entrée chacune (voir incrustations_table.py pour le sens des champs) :
  · 5e_C1.3-C1.4 (Hangzhou, système d'information) : carte mentale 5e, exercice e1, en tête de l'activité 1 ;
  · 3e_C1.5 (numérique et société) : carte mentale 3e, exercice e5, en fin de séance 2 (partie 2.d) ;
  · 4e_C8 (jardin connecté, valider) : diagramme des exigences 4e, exercice e3, en tête de l'activité 2.
"""
T1 = "theme-1-objets-systemes-usages-interactions/"
T3 = "theme-3-creation-conception-realisation-innovations/"
C1 = T1 + "C1-decrire-les-liens-entre-usages-et-evolutions/"
C8 = T3 + "C8-valider-les-solutions-techniques-par-des/"

ENTREES = [
    dict(id="cm-5e-hangzhou-donnees", module="carte_mentale", niveau="5e", exos=["e1"],
         sequence=C1 + "5e/5e_C1.3/sequence_C1.3-C1.4_SI_gestion_donnees.html",
         avant="<p><strong>Consigne :</strong> observe le schéma puis classe les éléments suivants",
         balise="h4", balise_exo="h5",
         titre="D'abord, qu'est-ce qu'une donnée&nbsp;? La carte mentale d'un autre projet",
         intro="Pour décrire le système d'information des vélos, il faut savoir reconnaître une <b>donnée</b>&nbsp;: une "
               "information que l'on peut enregistrer dans un fichier. Entraîne-toi sur un autre projet, le <b>lampadaire "
               "intelligent</b> d'une classe de 5e&nbsp;: recense ses données, puis range-les dans une <b>carte mentale</b>, "
               "qu'on appelle aussi carte heuristique. Un exercice, environ un quart d'heure&nbsp;; il se vérifie tout seul "
               "et a sa correction complète.",
         suite="un second exercice qui passe de la carte mentale aux dossiers de l'ordinateur, et le QCM de l'atelier"),
    dict(id="cm-3e-numerique-societe", module="carte_mentale", niveau="3e", exos=["e5"],
         sequence=C1 + "3e/3e_C1.5/sequence-numerique-societe-economie-environnement-sante.html",
         # en fin de partie 2, dans son cadre (.section), juste avant le bouton vers la séance 3
         avant='\n  </div>\n    \n\n  \n\n  \n\n<p class="page-suivante"><button class="btn vers-seance" data-vers="s3"',
         balise="h3", balise_exo="h4",
         titre="2.d – De la carte mentale à l'argumentaire court",
         intro="Le numérique transforme les métiers&nbsp;: c'est une <b>incidence sur la société</b>, avec des avantages et "
               "des inconvénients, comme ceux triés en 2.a. Pour en faire un <b>argumentaire court</b>, on prépare ses idées "
               "dans une <b>carte mentale</b>. Entraîne-toi sur un autre objet technique, la <b>station d'alerte "
               "cyclonique</b> d'une commune&nbsp;: trie les feuilles de sa carte, puis écris l'argumentaire. Un exercice, un "
               "peu moins de vingt minutes&nbsp;; il se vérifie tout seul et a sa correction complète. La même méthode te "
               "resservira à la séance 4, pour écrire ton propre argumentaire sur le smartphone.",
         # 24/10/2026 (séance 4 ajoutée) : l'exercice reste en séance 2 — la séance 4 n'aurait pas tenu en 55 min avec
         # lui, l'activité 5 et la clôture ; il y sert d'entraînement, l'activité 5 de réinvestissement.
         suite="un exercice pour choisir entre la carte mentale et une autre représentation, et le QCM de l'atelier"),
    dict(id="ex-4e-jardin-validation", module="exigences", niveau="4e", exos=["e3"],
         sequence=C8 + "4e/4e_C8.1/sequence_4e_C8_jardin-validation.html",
         avant="<p>Le banc virtuel (activité 0) t'a donné les observés. Juge la conformité de chacun&nbsp;:</p>",
         balise="h3", balise_exo="h4",
         titre="D'abord, relier chaque exigence à son test&nbsp;: le diagramme des exigences",
         intro="Juger un résultat, c'est le comparer à une <b>exigence</b>&nbsp;; et chaque exigence se vérifie par un "
               "<b>test</b> qui mesure. Entraîne-toi sur un autre objet du jardin connecté, le <b>système d'arrosage</b> "
               "d'un jardin partagé, avec son <b>diagramme des exigences</b>&nbsp;: relie chaque exigence à son test, juge "
               "les résultats du prototype avec la <b>flexibilité</b>, puis écris un protocole. Un exercice, environ un "
               "quart d'heure&nbsp;; il se vérifie tout seul et a sa correction complète.",
         suite="deux exercices pour lire le diagramme et écrire un bloc d'exigence, et le QCM de l'atelier"),
]
