# -*- coding: utf-8 -*-
"""Où chaque atelier entre dans les séquences : une ligne par incrustation.

Champs : id (unique), module, niveau, exos (identifiants d'exercices de l'atelier),
sequence (chemin depuis la racine du dépôt), et la première pose : `remplacer`
(début, fin) d'un passage remplacé, ou `avant` (une phrase repère unique). Puis le
titre et l'introduction de la section, et les niveaux de titre.
"""
T1 = "theme-1-objets-systemes-usages-interactions/"
C2 = T1 + "C2-decrire-les-interactions-entre-un-objet-ou/"

INCRUSTATIONS = [
    dict(id="pv-5e-shenzhen", module="interacteurs", niveau="5e", exos=["e1", "e3"],
         sequence=C2 + "5e/5e_C2.1/sequence_5e_C2_shenzhen_station_velos.html",
         remplacer=('<h4>c) Ta liste</h4>', '<li>«&nbsp;8. ____ (environnement).&nbsp;»</li>\n    </ul></details>\n'),
         balise="h4", balise_exo="h5",
         titre="c) Le diagramme pieuvre d'un autre objet&nbsp;: le vélo-cargo",
         intro="La liste de la station est faite, famille par famille. À toi maintenant, sur un autre objet&nbsp;: "
               "un <b>vélo-cargo</b>. Tu vas lister ce qui l'entoure, puis compléter son schéma — le <b>diagramme des "
               "interacteurs extérieurs</b>, qu'on appelle aussi le <b>diagramme pieuvre</b>. Deux exercices, environ "
               "un quart d'heure&nbsp;; chacun se vérifie tout seul et a sa correction complète.",
         suite="un exercice pour classer ses interacteurs, un autre sur ses choix de conception, et le QCM de l'atelier"),
]
