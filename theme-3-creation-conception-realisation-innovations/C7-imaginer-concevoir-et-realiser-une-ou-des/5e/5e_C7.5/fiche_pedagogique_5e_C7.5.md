# Fiche pédagogique — 5e_C7.5 « L'éclairage du préau »

| | |
|---|---|
| **Code** | `5e_C7.5` — Assembler les constituants fournis pour réaliser un prototype. |
| **Appui** | `5e_C4.5` — Identifier des constituants de la chaîne d'information d'un OST (l'organisation de la chaîne d'information étant fournie). |
| **Niveau** | 5<sup>e</sup> · Thème 3 |
| **Durée** | 2 séances de 55 min (95 min d'activités) |
| **Socle** | D2 · D3 · D4 |
| **Matériel** | carte Arduino UNO + Base Shield V2 + modules Grove — **TBT 5 V uniquement** |

## Problématique

> Tous les constituants sont fournis. Alors pourquoi un prototype peut-il encore ne pas fonctionner ?

## Déroulé

| # | Activité | Durée | Verrou expérientiel |
|---|---|---|---|
| 0 | Quatre fonctions, pas cinq | 15 min | — |
| 1 | Monter le prototype | 25 min | verrou : `ok` |
| 2 | Retirer, pour voir | 20 min | verrou : `retire` |
| 3 | L'ordre du montage | 20 min | — |
| 4 | REFAIRE — réinvestissement | 15 min | — |

## Les trois versions

- **🅰 avec le matériel** — le montage réel, qui fait foi.
- **🅱 avec l'établi de la page** — hors ligne, sans installation, et il permet de retirer un
  constituant d'un montage qui marchait.
- **🅲 sans écran** — fiches cartonnées et raisonnement identique.

## Sécurité

Très basse tension **uniquement** : 5 V partout. Aucun élève ne manipule le secteur ; le bloc
d'alimentation, s'il y en a un, est raccordé par le professeur. **On câble hors tension**,
l'alimentation en dernier. 

## La skill `arduino-grove-college` — ce qui est tenu, et ce qui est sans objet

Cette skill impose vingt éléments à toute séquence mettant une carte en jeu. Cette séquence en
met une, et **rien n'y est programmé** : le programme est donné, chargé et lu, jamais modifié.
Plutôt que d'ignorer la skill en silence, voici le relevé, écrit pour être contesté.

| Élément imposé par la skill | Statut | Pourquoi |
|---|---|---|
| Rôle de chaque composant | **tenu** | activité 0, une association par constituant |
| Chaîne d'information | **tenu** | c'est le code d'appui du lot |
| Chaîne d'énergie | **tenu** | budget de courant et fonction « alimenter » |
| Versions 🅰 / 🅱 / 🅲 | **tenu** | section dédiée dans la séquence |
| Solution sans matériel | **tenu** | version 🅲, fiches cartonnées |
| Sécurité TBT | **tenu** | encadré dédié, et un test le vérifie |
| QCM de 30 questions | **tenu** | 20 sur le code, 10 sur l'appui |
| Grille d'évaluation | **tenu** | grille LSU en synthèse professeur |
| Approfondissement | **tenu** | bonus en fin de séquence |
| Figure du matériel | *partiel* | l'établi montre les ports et les fonctions, pas une photo du montage |
| Brochage détaillé | **sans objet** | les connecteurs Grove sont détrompés : il n'y a pas de brochage à choisir |
| Niveaux logiques | **sans objet** | aucun signal n'est câblé à la main |
| Algorigramme | **sans objet** | le programme est donné et n'est pas modifié |
| Code C++ ligne par ligne | **sans objet** | idem — le programme est lu, pas écrit |
| Moniteur série | **sans objet** | aucune trace n'est produite par l'élève |
| Dépannage matériel | **sans objet** | c'est le sujet de C5, pas de C7.5 |

## Ce que la fiche ne dit pas

Ce qui se passe en classe. Un test vert dit que la page fait ce qu'elle annonce, pas qu'un élève
apprend. La grille LSU de la synthèse professeur est là pour observer, pas pour noter une page.
