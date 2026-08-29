# 3e_C8.2 — Le mât de la station : proposer un protocole

> **Proposer un protocole de test pour valider la tenue mécanique d'un matériau.**
> Programme 2024 · cycle 4 · thème 3 · socle D1.3 · D2 · D3 · D4

➡ **[Ouvrir la séquence](sequence_3e_C8.2_mat-de-la-station.html)** — 2 séances de 90 min,
banc d'essai intégré, hors ligne, sans installation ni compte.

---

## Ce que le lot fait

La station d'alerte cyclonique de [`3e_C9.2`](../../../C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2/README.md)
est programmée, sa recette est signée. La mairie pose alors la question suivante : elle va
vivre dehors, en tête d'un mât de 2 m, avec 180 km/h de vent le jour où elle sert. **De quoi
fait-on ce mât, et comment le prouve-t-on ?** Cette fois, personne ne fournit de protocole.

Le verbe du code est **proposer**. Pour que ce verbe soit évalué et pas seulement récité, le
lot rend l'erreur **mesurable** : l'élève applique d'abord le protocole de traction de
5<sup>e</sup> — juste, connu, correctement appliqué — et constate lui-même, banc en main, qu'il
désigne un mât que la flexion élimine.

| Candidat | Traction | Rang | Flexion | Rang |
|---|---|---|---|---|
| Barre pleine acier Ø20 | **125,7 kN** | **1<sup>er</sup>** | 157 N | **4<sup>e</sup>** |
| Tube aluminium Ø50 × 3 | 84,2 kN | 3<sup>e</sup> | **467 N** | **1<sup>er</sup>** |

Un protocole juste, appliqué correctement, peut donner une réponse fausse — parce qu'il
répond à une autre question. **Choisir la sollicitation est la première ligne d'un protocole,
et c'est celle qui décide de tout le reste.**

## La spirale C8, achevée

| Niveau | Code | Ce qu'on demande | Qui écrit le protocole |
|---|---|---|---|
| 5<sup>e</sup> | [`5e_C8.2`](../../5e/5e_C8.2/README.md) | éprouver cinq matériaux en traction | le laboratoire |
| 3<sup>e</sup> | [`3e_C8.3`](../3e_C8.3/README.md) | la recette de la station, avant livraison | l'élève — un **comportement** |
| 3<sup>e</sup> | **`3e_C8.2`** | de quoi sera fait le mât | l'élève — une **matière** |

La séquence de 5<sup>e</sup> laissait la porte ouverte : son activité REFAIRE se termine sur
« *une étagère plie, elle ne s'étire pas — reconnaître qu'un protocole ne convient pas à une
question, c'est déjà de la 3<sup>e</sup>* ». Ce lot reprend le fil exactement là.

## Le banc

Original, écrit pour ce lot, en SVG et JavaScript, sans aucune dépendance et sans réseau.
**Un seul mât, deux sollicitations** — c'est le geste qui porte tout : basculer de
⟂ flexion à ↕ traction ne change ni le profilé ni la matière, seulement la façon de charger.

* En flexion, le mât se courbe et rompt **au ras de l'encastrement**, là où le bras de levier
  est maximal ; la flèche en tête s'affiche en continu, et la charge d'essai commune de 100 N
  est signalée quand on l'atteint.
* En traction, le même profilé s'allonge à peine et rompt **en pleine longueur**, à une charge
  des centaines de fois plus élevée.

Toutes les valeurs sont **calculées** par [`profils_3e_C8.2.py`](profils_3e_C8.2.py) —
`F = σ·I/(v·L)`, `f = F·L³/(3·E·I)`, `F = σ·A` — avec **les résistances du banc de 5<sup>e</sup>**
(bois 40 MPa, PVC 52, aluminium 190, acier 400). Aucune n'a été saisie à la main dans la page.
Elles sont **simulées**, et la page le dit à l'élève à trois endroits, dont une question de QCM
entièrement consacrée à ce que vaut une valeur simulée.

## Trois verrous, et dix relevés vérifiés

| Verrou | Exigence | Ce qu'il empêche |
|---|---|---|
| `__exp.flex3` | 3 profilés rompus en flexion | répondre à l'activité 0 sans toucher au banc |
| `__exp.trac5` | 5 profilés rompus en traction | recopier le tableau de traction |
| `__exp.flex5` | 5 profilés rompus en flexion | remplir les 10 relevés sans essai |

Les dix relevés de l'activité 3 sont comparés aux **vraies** valeurs du banc à 0,05 près :
41 au lieu de 41,1 est refusé, et le test le vérifie. C'est le cœur du code — on évalue la
mise en œuvre, pas la capacité à retrouver un ordre de grandeur.

## Ce que le lot ne fait pas, et le dit

* **Le vérificateur ne lit pas le protocole rédigé** : il compte des lignes et une longueur.
  La page l'écrit à l'élève, et c'est la raison d'être de la **grille de relecture croisée**
  en binôme, 7 critères, qui porte l'évaluation réelle du protocole.
* **Le modèle a un domaine** : la flèche de 723,8 mm annoncée pour le PVC est hors du domaine
  des petits déplacements. La page l'écrit et en tire une leçon plutôt qu'un chiffre.
* **Un seul essai par candidat** : une question de QCM (3e_C3.4) porte précisément sur ce manque.
* **Aucun essai physique.** Le laboratoire des matériaux du Réseau National Technologie Collège
  reste la version 🅰 — et il ne fait pas la flexion, ce que la séquence traite comme un objet
  d'étude plutôt que comme un obstacle.

## Fichiers

| Fichier | Contenu |
|---|---|
| [`sequence_3e_C8.2_mat-de-la-station.html`](sequence_3e_C8.2_mat-de-la-station.html) | 7 blocs chronométrés, banc intégré, 3 verrous |
| [`qcm_3e_C8.2_mat-de-la-station.html`](qcm_3e_C8.2_mat-de-la-station.html) | 30 q · 90 réfutations · 3e_C8.2 ×20, 3e_C3.4 ×10 |
| [`lexique_3e_C8.2.html`](lexique_3e_C8.2.html) | 30 notions, générées depuis le QCM du lot |
| [`synthese_eleve_3e_C8.2.html`](synthese_eleve_3e_C8.2.html) | à imprimer, lisible en noir et blanc |
| [`synthese_professeur_3e_C8.2.html`](synthese_professeur_3e_C8.2.html) | pari didactique, verrous, limites, repères LSU |
| [`fiche_pedagogique_3e_C8.2.md`](fiche_pedagogique_3e_C8.2.md) | déroulé, valeurs, différenciation, prolongements |
| [`matrice_couverture_3e_C8.2.csv`](matrice_couverture_3e_C8.2.csv) | 23 notions → activité → production → questions |
| [`rapport_tests_3e_C8.2.md`](rapport_tests_3e_C8.2.md) | **32/32** séquence · **26/26** QCM, rejouables |
| [`tests_3e_C8.2_sequence.mjs`](tests_3e_C8.2_sequence.mjs) · [`tests_3e_C8.2_qcm.mjs`](tests_3e_C8.2_qcm.mjs) | les tests eux-mêmes |
| [`profils_3e_C8.2.py`](profils_3e_C8.2.py) | recalcule toutes les valeurs du banc |

## Une mesure à porter ailleurs

Le gabarit de QCM hérité ouvre **trois boîtes `alert()`** — trois moments où la page bloque le
navigateur pour dire ce qu'un bandeau dit aussi bien. Ce lot les remplace, dans le seul fichier
qu'il produit, par `#savedNote` qui portait déjà `role="status"` et `aria-live="polite"`.

Le même défaut subsiste, hors archives, dans **46 QCM sur 51** (224 appels) et **35 séquences
sur 46** (38 appels). C'est la règle d'or n°188, écrite cette semaine et appliquée à une seule
page. Le reste demande une passe dédiée et mesurée — pas un balayage glissé dans un lot du
thème 3, que le garde-périmètre refuserait d'ailleurs à juste titre.
