# 4e_C7.4 — De quoi vit le jardin connecté

> **Comparer différentes sources d'énergie pour choisir la plus adaptée.**
> Programme 2024 · cycle 4 · thème 3 · socle D1.3 · D2 · D4 · D5

➡ **[Ouvrir la séquence](sequence_4e_C7.4_energie-du-jardin.html)** — 2 séances de 55 min, banc d'énergie intégré, hors ligne, sans
installation ni compte.

---

## Ce que le lot fait

Le verbe du code est **comparer**. Faire choisir sans grille n'évalue rien : tous
les élèves désignent le secteur, et personne n'a comparé. Le lot rend donc la comparaison
**nécessaire** en installant deux surprises que seul le banc peut lever.

**Première surprise :** la pompe, gros consommateur évident, pèse **0,4 %** ; la carte,
qui ne fait rien 99 % du temps, pèse **92 %**. L'intuition est démentie en trois clics.

**Seconde surprise, activité 4 :** comparer les sources finit par obliger à regarder la
**charge**. Avec une carte sobre, le besoin tombe de 5,87 à 1,07 Wh et le panneau qui perdait
toutes les comparaisons devient le meilleur. On croyait choisir une source ; on a changé le
problème.


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

Ce montage consomme **5,87 Wh par jour**. Toutes les valeurs sont calculées par
[`energie.py`](energie.py) : courants constructeur usuels, capacités réelles du commerce,
rendement d'un régulateur linéaire = V<sub>sortie</sub> ÷ V<sub>entrée</sub>, ensoleillement de
la Martinique à 5,3 heures équivalent plein soleil par jour avec 30 % de pertes de chaîne.

## Sécurité

Très basse tension **5 V** partout. Le « secteur » est un **adaptateur USB fermé** — jamais la
prise, jamais le câble. Côté élève, il n'y a que du 5 V. C'est la règle de la skill
`arduino-grove-college`, et la fiche pédagogique détaille en outre lesquels de ses 20 éléments
sont tenus ici et lesquels sont **sans objet**, puisque rien n'est programmé dans ce lot.

## Tests

**35 / 35** sur la séquence, **26 / 26** sur le QCM, rejouables : les deux scripts et le jeu de
réponses sont livrés dans le dossier. Voir [`rapport_tests_4e_C7.4.md`](rapport_tests_4e_C7.4.md).

## Fichiers

| Fichier | Contenu |
|---|---|
| [`sequence_4e_C7.4_energie-du-jardin.html`](sequence_4e_C7.4_energie-du-jardin.html) | 6 activités chronométrées, banc intégré |
| [`qcm_4e_C7.4_energie-du-jardin.html`](qcm_4e_C7.4_energie-du-jardin.html) | 30 q · 90 réfutations · 4e_C7.4 ×20, 4e_C3.1 ×10 |
| [`lexique_4e_C7.4.html`](lexique_4e_C7.4.html) | 30 notions, générées depuis le QCM du lot |
| [`synthese_eleve_4e_C7.4.html`](synthese_eleve_4e_C7.4.html) | à imprimer, lisible en noir et blanc |
| [`synthese_professeur_4e_C7.4.html`](synthese_professeur_4e_C7.4.html) | pari didactique, limites, repères LSU |
| [`fiche_pedagogique_4e_C7.4.md`](fiche_pedagogique_4e_C7.4.md) | déroulé, valeurs, différenciation, skill |
| [`matrice_couverture_4e_C7.4.csv`](matrice_couverture_4e_C7.4.csv) | notion → activité → production → questions |
| [`rapport_tests_4e_C7.4.md`](rapport_tests_4e_C7.4.md) | la sortie des deux suites, telle quelle |
| [`energie.py`](energie.py) | recalcule toutes les valeurs du banc |
