# 📣 Le compte du club — `5e_C1.5` + `5e_C1.6`

> Une publication ne dit pas seulement ce qu'on a voulu écrire. Que révèle-t-elle en plus, et qui en devient responsable ?

**Thème 1 · 5<sup>e</sup>** · 3 séances de 55 min (140 min d'activités) · aucun matériel, aucune connexion

## Deux codes, une situation

Le club robotique publie la photo du jardin connecté sur le compte du collège : six élèves, un
compte, un mot de passe écrit au tableau. De cette seule publication sortent les deux codes.

| Code | Intitulé du programme 2024 |
|---|---|
| `5e_C1.5` | Identifier des règles permettant de sécuriser un environnement numérique (bases de la cybersécurité) et des règles de respect de la propriété intellectuelle. |
| `5e_C1.6` | Appréhender la responsabilité de chacun dans les dérives (cyberviolence, atteinte à la vie privée, aux données personnelles, usurpation d'identité). |

Le lien entre les deux n'est pas décoratif : **la responsabilité suppose qu'on puisse dire qui a
agi**, et un compte partagé la rend indécidable. C'est la charnière de la séquence.

## Ce qui change par rapport à ce qui existait

Ces deux codes étaient jusqu'ici couverts par deux **pages pointeur** vers la séquence
`4e_C1.4`. Elles sont archivées, pour trois raisons écrites dans
[`_archive-anciennes-versions/theme-1/5e_C1.5-C1.6_pointeurs-vers-4e_avant-2026-08-30/`](../../../../_archive-anciennes-versions/theme-1/5e_C1.5-C1.6_pointeurs-vers-4e_avant-2026-08-30/README.md) :
la 5<sup>e</sup> vient avant la 4<sup>e</sup> ; le pointeur écartait la propriété intellectuelle
que l'intitulé de `5e_C1.5` nomme explicitement ; et `5e_C1.6` n'était couvert par aucune
situation.

À noter, pour ne pas le découvrir plus tard : le QCM du lot **Chengdu** (`5e_C1.1`) porte déjà
**5 questions codées C1.5 et 4 codées C1.6**. Les deux ressources coexistent — celle-ci est la
séance, celle-là un rappel croisé dans un autre parcours. Aucune des deux n'est modifiée par
l'autre.

**La séquence `4e_C1.4` n'est pas modifiée.** Voici ce que chacune travaille :

| Ce qui est travaillé | 5<sup>e</sup> (ce lot) | 4<sup>e</sup> (4e_C1.4) |
|---|---|---|
| Ce qu'une publication révèle (métadonnées, combinaison d'indices) | **ce lot** | — |
| Droit à l'image et autorisation des responsables légaux | **ce lot** | rappelé |
| Propriété intellectuelle, licences Creative Commons | **ce lot** | — |
| Compte partagé, rôles, traçabilité des actions | **ce lot** | — |
| Responsabilité de chacun autour d'un contenu qui blesse | **ce lot** | approfondi |
| Mot de passe solide, hameçonnage, wifi public, mises à jour | mobilisé | **4e_C1.4** |
| Double authentification, gestionnaire de mots de passe | — | **4e_C1.4** |
| Identité numérique, témoins de connexion, géolocalisation des objets | — | **4e_C1.4** |
| Droit à l'oubli, e-réputation, signalement | — | **4e_C1.4** |

## L'instrument

`publication.py` engendre un **banc de publication**. On coche les éléments d'une publication,
et le banc affiche deux compteurs : les **indices** qui mènent encore à une personne réelle, et
les **règles** enfreintes. On décoche, et les deux bougent — séparément.

Deux choses que le banc rend visibles et qu'aucun cours ne rend évidentes :

* **une autorisation rend licite, elle ne rend pas anonyme** — avec l'accord écrit, le compteur
  de règles baisse et celui des indices ne bouge pas d'un seul ;
* **ce n'est pas un élément qui identifie, c'est leur combinaison** — retirer le visage fait
  passer de sept indices à six.

## Ce que contient le dossier

| Fichier | Ce que c'est |
|---|---|
| [`sequence_5e_C1.5-C1.6_le-compte-du-club.html`](sequence_5e_C1.5-C1.6_le-compte-du-club.html) | la séquence élève, hors ligne, avec le banc |
| [`qcm_5e_C1.5-C1.6_le-compte-du-club.html`](qcm_5e_C1.5-C1.6_le-compte-du-club.html) | 30 questions — 15 sur `5e_C1.5`, 15 sur `5e_C1.6`, 90 réfutations |
| [`lexique_5e_C1.5.html`](lexique_5e_C1.5.html) | 30 notions, engendrées depuis le QCM |
| [`synthese_eleve_5e_C1.5-C1.6.html`](synthese_eleve_5e_C1.5-C1.6.html) | à retenir, imprimable |
| [`synthese_professeur_5e_C1.5-C1.6.html`](synthese_professeur_5e_C1.5-C1.6.html) | le pari, la frontière avec la 4<sup>e</sup>, les limites, la grille LSU |
| [`fiche_pedagogique_5e_C1.5-C1.6.md`](fiche_pedagogique_5e_C1.5-C1.6.md) | déroulé, frontière, règle de la séquence |
| [`matrice_couverture_5e_C1.5-C1.6.csv`](matrice_couverture_5e_C1.5-C1.6.csv) | notion → activité → production → question |
| [`rapport_tests_5e_C1.5-C1.6.md`](rapport_tests_5e_C1.5-C1.6.md) | la sortie des deux suites, telle quelle |
| `tests_*.mjs` · `reponses_*.json` · `publication.py` | de quoi tout rejouer |

**Tests réels : 38/38 sur la séquence, 32/32 sur le QCM.**

## La règle de la séquence

Aucune donnée réelle n'entre dans la page : les personnes sont inventées, la page ne demande ni
nom, ni photo, ni mot de passe, et n'envoie rien nulle part. Elle rappelle aux élèves de **ne
jamais taper un vrai mot de passe dans un exercice**, et donne le **3018**, numéro national
gratuit pour les violences numériques.
