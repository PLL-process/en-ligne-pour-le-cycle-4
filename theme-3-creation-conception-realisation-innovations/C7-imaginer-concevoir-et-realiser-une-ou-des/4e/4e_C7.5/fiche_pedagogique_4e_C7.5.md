# Fiche pédagogique — 4e_C7.5 « Le jardin qui n'arrose pas encore »

| | |
|---|---|
| **Code** | `4e_C7.5` — Identifier les constituants manquants dans un prototype et le compléter. |
| **Appui** | `4e_C4.4` — Identifier les constituants de la chaîne d'information d'un objet réel et les associer à leur fonction. |
| **Niveau** | 4<sup>e</sup> · Thème 3 |
| **Durée** | 2 séances de 55 min (95 min d'activités) |
| **Socle** | D2 · D3 · D4 |
| **Matériel** | carte Arduino UNO + Base Shield V2 + modules Grove — **TBT 5 V uniquement** |

## Problématique

> Aucune pièce n'est défectueuse et le programme est juste. Comment trouve-t-on, alors, ce qui manque à un prototype ?

## Déroulé

| # | Activité | Durée | Verrou expérientiel |
|---|---|---|---|
| 0 | Chaque constituant, sa fonction | 15 min | — |
| 1 | Cas 1 : la pompe ne part jamais | 20 min | verrou : `diag_exige_relais` |
| 2 | Cas 2 : la carte redémarre | 20 min | verrou : `diag_budget` |
| 3 | Cas 3 : la pompe ne s'arrête plus | 20 min | verrou : `diag_requis_hum` |
| 4 | REFAIRE — réinvestissement | 20 min | — |

## Les trois versions

- **🅰 avec le matériel** — le montage réel, qui fait foi.
- **🅱 avec l'établi de la page** — hors ligne, sans installation, et il permet de retirer un
  constituant d'un montage qui marchait.
- **🅲 sans écran** — fiches cartonnées et raisonnement identique.

## Sécurité

Très basse tension **uniquement** : 5 V partout. Aucun élève ne manipule le secteur ; le bloc
d'alimentation, s'il y en a un, est raccordé par le professeur. **On câble hors tension**,
l'alimentation en dernier. **Une pompe met de l'eau et de l'électricité au même endroit** : essai à sec d'abord, bac rempli seulement sur un montage éprouvé.

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

## Découpage en séances à onglets (04/11/2026, vague de la règle d'or n°311)

La page était d'un seul tenant ; elle a maintenant deux séances à onglets, sur le modèle du pilote 4e_C8.1 et de la vague C8. Les blocs sont déplacés, pas réécrits ; le nombre de séances annoncé (2 × 55 min) ne change pas.

| Séance | Question directrice | Contenu | Temps annoncé |
|---|---|---|---|
| 1 — Chaque fonction, puis le cas 1 | Que devrait-il y avoir dans le prototype, et que manque-t-il au premier ? | Ouverture, activités 0 et 1 | ouverture + 15 + 20 min |
| 2 — Les cas 2 et 3, refaire, conclure | Quand les quatre fonctions semblent tenues, où se cache ce qui manque ? | Activités 2 et 3, réinvestissement, synthèse, Bonus (corrigé), bilan, QCM | 20 + 20 + 20 min + clôture |

**À trancher par Pascal :** la séance 2 porte 60 min d'activités pour 55 (l'autre coupe chargeait la séance 1 de l'ouverture et de 55 min). **L'établi, corrigé le 04/11/2026 :** il donnait ✔ à un montage sans pompe et écrivait alors « la pompe tourne six secondes ». La pompe entre dans les constituants sans lesquels le cahier des charges n'est pas tenu (`REQUIS`) : un montage sans pompe est refusé, et l'établi dit ce qui manque (« la pompe immergée manque »), comme pour les autres manques. Le gabarit `etabli.py` n'est pas touché : il reçoit `REQUIS` comme une donnée.

Dès la séance 2, l'ouverture (étiquettes, « Avant de commencer », situation, problématique et idée de départ, sécurité de la pompe, trois façons, billet d'entrée) est repliée dans le volet « 📖 Rappel » ; elle est complète à la séance 1. L'en-tête de la séance 2 rappelle en une ligne la consigne de sécurité de la carte, et renvoie au volet. Restent visibles à chaque séance : le titre, la mission (elle remplace le sous-titre « Thème 3 · 4e — … », comme au pilote), la barre d'outils (🖨 Imprimer / PDF, que la page n'avait pas) et **l'établi**, qui sert aux deux séances : un seul bloc ; à la séance 1, il reste à sa place, dans l'activité 1 (au-dessus de l'activité 0, il en donnerait les réponses : il dit ce que fait chaque constituant) ; dès la séance 2, le script des onglets le place juste après l'en-tête de la séance ouverte. Sans JavaScript, toutes les séances s'affichent à la suite, l'outil à sa place.

La clôture reçoit un corrigé replié du défi (le quatrième cas : il manque la pompe ; le symptôme au téléphone) ; au bilan, « Comment j'ai travaillé » et « Je me positionne » aux quatre niveaux du livret scolaire, sur `4e_C7.5` et `4e_C4.4` (appui) (le menu existant passe aux quatre niveaux ; une réponse sur l'ancienne échelle se relit au niveau voisin).
