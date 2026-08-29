# 5e_C7.4 — L'indicateur du hall

> **Choisir une source d'énergie parmi plusieurs proposées et une forme d'énergie possible.**
> Programme 2024 · cycle 4 · thème 3 · socle D1.3 · D4 · D5

➡ **[Ouvrir la séquence](sequence_5e_C7.4_indicateur-du-hall.html)** — 2 séances de 55 min, banc d'énergie intégré, hors ligne, sans
installation ni compte.

---

## Ce que le lot fait

Le verbe du code est **choisir parmi plusieurs sources proposées**. Le piège que
la séquence installe est le meilleur outil pour l'évaluer : **le panneau solaire suffit sur le
papier** — 3,7 Wh récoltés pour 2,85 consommés — **et ne marche pas**, parce qu'il n'y a pas
de soleil dans un hall.

L'élève qui décide au seul vu du banc se trompe. L'élève qui a compris que le lieu fait partie
du choix ne se trompe pas. Le REFAIRE ferme la démonstration : le même objet, posé sur le portail
à vélos, retrouve le panneau — **sans qu'un seul chiffre change**.


## La spirale C7.4

| Niveau | Ce qu'on demande | Ce qu'on donne |
|---|---|---|
| 5<sup>e</sup> | choisir une source pour l'indicateur du hall | une liste de cinq sources, et le lieu |
| 4<sup>e</sup> | comparer les sources du jardin connecté | les critères à identifier, une grille à remplir |
| 3<sup>e</sup> | choisir la source de la station d'alerte | rien — un objet réel et un avis à signer |

## Le banc d'énergie

Original, écrit pour ces trois lots, en HTML et JavaScript, sans dépendance et sans réseau.
Il fait, sous les yeux de l'élève, les deux multiplications et la division qu'un technicien fait
sur un coin de table — et il permet d'**éteindre** un consommateur pour voir ce qu'il pesait.

Ce montage consomme **2,85 Wh par jour**. Toutes les valeurs sont calculées par
[`energie.py`](energie.py) : courants constructeur usuels, capacités réelles du commerce,
rendement d'un régulateur linéaire = V<sub>sortie</sub> ÷ V<sub>entrée</sub>, ensoleillement de
la Martinique à 5,3 heures équivalent plein soleil par jour avec 30 % de pertes de chaîne.

## Sécurité

Très basse tension **5 V** partout. Le « secteur » est un **adaptateur USB fermé** — jamais la
prise, jamais le câble. Côté élève, il n'y a que du 5 V. C'est la règle de la skill
`arduino-grove-college`, et la fiche pédagogique détaille en outre lesquels de ses 20 éléments
sont tenus ici et lesquels sont **sans objet**, puisque rien n'est programmé dans ce lot.

## Tests

**34 / 34** sur la séquence, **26 / 26** sur le QCM, rejouables : les deux scripts et le jeu de
réponses sont livrés dans le dossier. Voir [`rapport_tests_5e_C7.4.md`](rapport_tests_5e_C7.4.md).

## Fichiers

| Fichier | Contenu |
|---|---|
| [`sequence_5e_C7.4_indicateur-du-hall.html`](sequence_5e_C7.4_indicateur-du-hall.html) | 6 activités chronométrées, banc intégré |
| [`qcm_5e_C7.4_indicateur-du-hall.html`](qcm_5e_C7.4_indicateur-du-hall.html) | 30 q · 90 réfutations · 5e_C7.4 ×20, 5e_C3.1 ×10 |
| [`lexique_5e_C7.4.html`](lexique_5e_C7.4.html) | 30 notions, générées depuis le QCM du lot |
| [`synthese_eleve_5e_C7.4.html`](synthese_eleve_5e_C7.4.html) | à imprimer, lisible en noir et blanc |
| [`synthese_professeur_5e_C7.4.html`](synthese_professeur_5e_C7.4.html) | pari didactique, limites, repères LSU |
| [`fiche_pedagogique_5e_C7.4.md`](fiche_pedagogique_5e_C7.4.md) | déroulé, valeurs, différenciation, skill |
| [`matrice_couverture_5e_C7.4.csv`](matrice_couverture_5e_C7.4.csv) | notion → activité → production → questions |
| [`rapport_tests_5e_C7.4.md`](rapport_tests_5e_C7.4.md) | la sortie des deux suites, telle quelle |
| [`energie.py`](energie.py) | recalcule toutes les valeurs du banc |
