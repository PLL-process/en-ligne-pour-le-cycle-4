# Fiche pédagogique — 5e_C7.3 « Le banc de la cour »

| | |
|---|---|
| **Code** | `5e_C7.3` — Choisir un matériau parmi plusieurs proposés en fonction de leurs caractéristiques. |
| **Appui** | `5e_C4.4` — Identifier les principaux matériaux constitutifs d'un OST. |
| **Niveau** | 5<sup>e</sup> · Thème 3 |
| **Durée** | 2 séances de 55 min (95 min d'activités) |
| **Socle** | D3 · D4 · D5 |
| **Matériel** | aucun matériel obligatoire — le banc fonctionne dans un navigateur, hors ligne |

## Problématique

> Six matériaux, aucun mauvais. Comment un cahier des charges en élimine-t-il quatre ?

## Déroulé

| # | Activité | Durée | Verrou expérientiel |
|---|---|---|---|
| 0 | Ce que chaque caractéristique dit | 15 min | — |
| 1 | Le banc élimine, et il dit pourquoi | 25 min | verrou : `evalue` |
| 2 | Retirer une exigence, et voir ce qui entre | 25 min | verrou : `retireCritere` |
| 3 | Choisir, entre les deux qui restent | 15 min | — |
| 4 | REFAIRE — réinvestissement | 15 min | — |

## Les trois versions

| Version | Ce qu'elle demande |
|---|---|
| 🅰 avec des échantillons | six chutes de matériau, un thermomètre infrarouge, une heure de plein soleil |
| 🅱 avec le banc de la page | un navigateur, hors ligne, rien à installer |
| 🅲 sans écran | six fiches cartonnées et cinq bandes d'exigences |

## Sécurité

Aucune électricité dans cette séquence : le banc est une pièce de structure. La version
🅰 met six chutes de matériau au soleil et un **thermomètre infrarouge** entre les mains des
élèves — on relève une température de surface, on ne pose pas la main dessus pour vérifier.
Les chutes de **pin traité autoclave** ne se poncent pas sans aspiration et ne se brûlent jamais.

## D'où viennent les nombres

Toutes les valeurs affichées — masses, coûts, épaisseurs, verdicts — sont calculées par
`materiaux.py`, livré dans ce dossier. **Aucun nombre n'est recopié à la main dans une page.**
Ce sont des **ordres de grandeur d'usage pédagogique**, tirés de plages courantes en construction
et en aménagement : c'est le *classement* qui doit être juste, pas la troisième décimale. Deux
colonnes sont propres au climat de la Martinique et font le cœur du lot — la **tenue au
rayonnement solaire** et la **tenue au brouillard salin**. Un tableau générique retiendrait des
matériaux que ces deux colonnes éliminent.

Pour rejouer les tables des trois niveaux :

```bash
python3 materiaux.py
```

## Ce que la fiche ne dit pas

Ce qui se passe en classe. Un test vert dit que la page fait ce qu'elle annonce, pas qu'un élève
apprend. La grille LSU de la synthèse professeur est là pour observer, pas pour noter une page.
