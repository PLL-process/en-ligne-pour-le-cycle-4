# Plan — Atelier « Le diagramme de planification des tâches » (C7.1, les trois niveaux)

## Le constat qui l'a déclenché

Le programme 2024 nomme explicitement, dans la partie gestion de projet :

> **« Le diagramme de planification des tâches : notion de tâches, durée et contraintes entre
> tâches »**

L'inventaire du 8 août a compté **zéro occurrence** dans tout le dépôt. Et la confrontation des
trois séquences C7.1 au texte qu'elles portent est accablante :

| Séquence | Ce que le code exige | Occurrences de « tâche » | de « planification » |
|---|---|---|---|
| 5e_C7.1 | **Suivre** un processus… avec des tâches identifiées | 1 | 0 |
| 4e_C7.1 | **Organiser** un processus… avec des tâches identifiées | 2 | 0 |
| 3e_C7.1 | **Élaborer** un processus… avec des tâches identifiées | **0** | 0 |

La séquence de 3e doit faire élaborer un processus **avec des tâches identifiées**, et le mot
« tâche » n'y figure pas une fois. C'est la règle n°63 dans sa forme la plus nette : le code est
revendiqué, la chose n'est pas enseignée.

## Pourquoi un atelier, et non trois refontes

Les trois séquences C7.1 existantes sont **bonnes** sur ce qu'elles font — concevoir, fabriquer,
valider. Ce qui leur manque est une **notion transversale** qui, par nature, se travaille de la
même façon aux trois niveaux, avec le seul verbe qui change. Les refondre toutes les trois pour y
insérer le même contenu serait long, redondant, et produirait trois versions qui divergeront.

**Décision** : une ressource unique, `atelier-planification/`, portant les trois parcours, et
appelée depuis chacune des trois séquences. Elle se glisse au moment du lancement de projet, là où
elle sert.

## La progression, par le verbe (règle n°65)

| Niveau | Verbe du référentiel | Ce que l'élève reçoit | Ce qu'il produit |
|---|---|---|---|
| **5e** | **suivre** | un planning **déjà fait** | il pointe l'avancement, repère un retard, et dit ce que ce retard décale |
| **4e** | **organiser** | la liste des tâches **avec leurs durées** | il établit les contraintes d'antériorité et place les tâches |
| **3e** | **élaborer** | le projet, et rien d'autre | il identifie les tâches, estime les durées, pose les contraintes, trouve le chemin le plus long |

C'est la même notion trois fois, et ce n'est jamais le même travail.

## Les notions, et l'ordre où elles arrivent

1. **La tâche** — ce qui a un début, une fin, et quelqu'un qui la fait. Une tâche qu'on ne peut pas
   déclarer terminée n'est pas une tâche.
2. **La durée** — estimée, jamais connue. Et une estimation qui n'a jamais été comparée au réel ne
   s'améliore pas.
3. **La contrainte d'antériorité** — « B ne peut commencer qu'après A ». C'est la seule contrainte
   du programme, et c'est la plus utile : elle distingue *ce qui doit attendre* de *ce qui pourrait
   se faire en même temps*.
4. **Le parallélisme** — deux tâches sans contrainte entre elles peuvent avancer ensemble. C'est là
   qu'on gagne du temps, et c'est ce que les élèves voient le moins.
5. **Le jalon** — un point de contrôle sans durée. « Le prototype fonctionne » n'est pas une tâche,
   c'est un jalon.
6. **Le chemin le plus long** (3e) — la suite de tâches enchaînées qui fixe la durée totale.
   Raccourcir une tâche qui n'est pas dessus ne fait gagner **aucune** journée. C'est le résultat le
   plus contre-intuitif de la planification, et le plus utile.

Le mot **« chemin critique »** est donné entre parenthèses, comme nom du métier (règle n°62), après
avoir été compris sous son nom clair.

## Objets-fils : ceux des lots existants

L'atelier ne crée pas un projet de plus. Il planifie **les projets déjà en cours** dans les trois
séquences C7.1 : le mini-projet d'objet en 5e, le jardin connecté en 4e, le capteur de confort en
3e. L'élève planifie ce qu'il va réellement faire — c'est la seule façon que la planification ne
soit pas un exercice d'école.

## Ce que l'atelier produira

- **Trois corrigés graphiques CC0** : le vocabulaire (tâche, durée, antériorité, jalon,
  parallélisme), le diagramme du jardin connecté renseigné, et le chemin le plus long du capteur de
  confort avec la démonstration qu'une tâche hors chemin ne fait rien gagner.
- **Un jeu de données** : les tâches des trois projets, avec durées et antériorités.
- **Une page d'atelier** à trois parcours, avec champs, vérificateurs et corrigés repliés.
- **Un QCM de 30 questions** réparties sur les trois niveaux.
- **Trois liens** posés dans les séquences C7.1 existantes — le seul changement qu'elles subissent.
