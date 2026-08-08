# Plan du lot — 4e_C2.1 · C2.2 « Hangzhou : ce que vit l'usager devant la borne »

## Les deux codes, dans le texte du référentiel

| Code | Formulation (BO n°9 du 29/02/2024, via `_outils/data_competences.py`) |
|---|---|
| `4e_C2.1` | Décrire l'expérience de l'utilisateur (ressenti et facilité d'usage) d'un OST **en partant du langage naturel (texte, croquis) pour aboutir aux schémas, graphiques, algorithmes**. |
| `4e_C2.2` | Repérer et expliquer les contraintes, exigences prises en compte (sécurité, incidences environnementales, formes et fonctions, ergonomie, qualité, fiabilité) **pour répondre aux attentes des utilisateurs**. |

**Socle** : D1.3, D3, D4, D5.

Ces formulations sont recopiées, pas reformulées (règle n°42, écrite ce matin après l'incident du
lot 5e_C2). La carte du référentiel de la séquence les portera telles quelles.

## Ce que le référentiel impose, et qu'on ne peut pas contourner

`4e_C2.1` ne dit pas seulement « décrire l'expérience ». Il décrit un **trajet de représentation** :
on part du **langage naturel** — ce que les gens disent, ce qu'on croque — et on aboutit à des
**schémas, des graphiques, des algorithmes**.

C'est la contrainte structurante du lot, et elle donne d'elle-même le déroulé : la séquence doit
faire parcourir ce trajet, pas seulement en parler.

| Étape | Ce que l'élève manipule | Ce qu'il produit |
|---|---|---|
| 1 | des **verbatims** d'usagers et un croquis | un relevé du ressenti, étape par étape |
| 2 | des **temps mesurés** par étape | un **graphique** qui montre où ça coince |
| 3 | le parcours | un **algorigramme** du parcours de l'usager |
| 4 | les points de friction | des **contraintes et exigences** nommées (`C2.2`) |

## La marche depuis la 5e

| | Ce que l'élève fait | Sur quoi il travaille |
|---|---|---|
| 5e — Shenzhen | il **recense** les interacteurs, il **repère** des choix dans la forme | l'objet, vu du dehors |
| **4e — ici** | il **décrit un vécu** et le **traduit** en schéma, graphique, algorithme ; puis il **remonte aux exigences** | l'objet, vu par celui qui s'en sert |

La séquence de 5e annonçait déjà cette marche à l'élève (« ce que tu feras en 4e, et pas encore
ici »). Celle-ci doit lui rappeler l'annonce et la tenir.

## L'objet-fil

**Hangzhou**, qui est déjà l'objet du lot 4e_C3 — la flotte de vélos de la ville. Ici, non plus la
flotte, mais **la borne de retrait**, et ce que vit l'usager entre le moment où il arrive et celui
où il repart à vélo.

Le fil chinois du Thème 1 se tient : Shanghai (5e_C3), Shenzhen (5e_C2, 3e_C3), Hangzhou (4e_C3 et
4e_C2). Un même pays, des villes différentes, des objets différents.

## Les données

Toutes **simulées**, et annoncées comme telles :

- **12 verbatims d'usagers** (texte libre, langage naturel) — dont deux qui se contredisent, parce
  qu'un ressenti n'est pas une mesure ;
- **les temps par étape** relevés sur 30 retraits (arriver, identifier, choisir, déverrouiller,
  partir), en secondes — de quoi tracer le graphique et voir où le temps part ;
- **une réclamation** du service client, qui servira de situation déclenchante.

## Le piège à nommer

**Un ressenti n'est pas une mesure, et une mesure n'est pas un ressenti.** Les deux se croisent :
l'étape la plus longue n'est pas toujours celle dont les gens se plaignent, et l'inverse est vrai
aussi. C'est exactement pourquoi le référentiel demande de passer du langage naturel au graphique —
et pas de choisir entre les deux.

## La ressource héritée

`qcm_fonctionnement_objet.html` (50 Ko, 25 questions, « Comment expliquer le fonctionnement d'un
objet ? ») est **le travail d'un autre auteur**. Il annonce lui-même couvrir `C2.1`, `C2.2` et
`C9.1` à `C9.3`, sur des notices, des contraintes et de la programmation.

**Il ne sera pas modifié** (règle : on ne touche pas aux lots existants d'un autre auteur). Il sera
**intégré comme ressource complémentaire**, référencé au README et depuis le bloc Bonus de la
séquence, avec sa portée dite honnêtement : il déborde sur le C9, et il ne remplace pas le QCM du
lot.

## Le paquet attendu

Séquence · QCM de 30 questions (15 par code, 4 illustrées) · 2 synthèses · fiche · matrice ·
SOURCES_MEDIAS · manifest · README + README pointeur `4e_C2.2` · rapport de tests · suite de tests ·
SVG originaux (le parcours de l'usager ; le passage verbatim → graphique → algorigramme) ·
générateur `_generation/` pour le QCM (règle n°38).

## Ce que je vérifierai avant de livrer

Outre les huit règles mécanisées — dont la **n°42**, qui n'existait pas ce matin — deux points
propres à ce lot :

1. que la séquence **fasse réellement parcourir** le trajet langage naturel → schéma → graphique →
   algorithme, et ne se contente pas de le décrire ;
2. que les exigences de `C2.2` soient **nommées dans les termes du référentiel** — sécurité,
   incidences environnementales, formes et fonctions, ergonomie, qualité, fiabilité — et pas dans
   des termes que j'aurais trouvés plus clairs.

Le second point est la leçon du lot précédent, appliquée avant d'écrire plutôt qu'après.
