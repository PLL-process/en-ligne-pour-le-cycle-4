# Fiche pédagogique — 3e_C7.5 « La station qu'il faut équiper »

| | |
|---|---|
| **Code** | `3e_C7.5` — Choisir les constituants et assembler un prototype. |
| **Appui** | `3e_C4.3` — Décrire un OST en caractérisant sa chaîne d'information. |
| **Niveau** | 3<sup>e</sup> · Thème 3 |
| **Durée** | 4 séances de 55 min (150 min d'activités) |
| **Socle** | D2 · D3 · D4 |
| **Matériel** | carte Arduino UNO + Base Shield V2 + modules Grove — **TBT 5 V uniquement** |

## Problématique

> Le catalogue contient plus de constituants qu'il n'en faut. Comment un cahier des charges décide-t-il, à lui seul, lesquels on garde ?

## Déroulé

| Séance | # | Activité | Durée | Verrou expérientiel |
|---|---|---|---|---|
| 1 | 0 | Ce que chaque exigence impose | 25 min | — |
| 2 | 1 | Choisir, et l'écrire | 35 min | — |
| 3 | 2 | Assembler et prouver | 30 min | verrou : `ok` |
| 3 | 3 | Ce que coûte chaque retrait | 25 min | verrou : `retire` |
| 4 | 4 | Le choix qui coûte | 20 min | verrou : `diag_budget` |
| 4 | 5 | REFAIRE — réinvestissement | 15 min | — |

**Quatre séances de 55 min** (une heure de cours par semaine, décision du 24/10/2026) :
25, 35, 55 et 35 min d'activités annoncées. La séance 1 porte aussi la lecture de la situation,
la problématique, l'hypothèse de départ et l'encadré de sécurité ; la séance 4 se termine par la
synthèse, le Bonus facultatif, le bilan (retour à l'hypothèse, positionnement) et le renvoi au
QCM. Aucune activité n'est coupée : l'activité 1 ne tient pas avec l'activité 0 (60 min), et
l'activité 3 est une seule question à quatre retraits. La séance 3 est pleine (55 min) : le
montage sur l'établi y est suivi des retraits, dans la même heure — ce qui compte, car le
verrou `retire` ne s'ouvre qu'après un essai réussi dans la même ouverture de la page.

À la séance 4, l'activité 4 demande le montage complet : s'il a été perdu (autre ordinateur,
sauvegarde effacée), l'en-tête de la séance invite à le remonter d'après la correction de
l'activité 2.

## Les trois versions

- **🅰 avec le matériel** — le montage réel, qui fait foi.
- **🅱 avec l'établi de la page** — hors ligne, sans installation, et il permet de retirer un
  constituant d'un montage qui marchait.
- **🅲 sans écran** — fiches cartonnées et raisonnement identique.

## Sécurité

Très basse tension **uniquement** : 5 V partout. Aucun élève ne manipule le secteur ; le bloc
d'alimentation, s'il y en a un, est raccordé par le professeur. **On câble hors tension**,
l'alimentation en dernier. **Le bandeau de 480 mA chauffe** : il ne reste pas allumé dans un boîtier fermé sans ventilation. Et le mât reste au sol pendant tout le montage.

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

## Les séances passent à onglets (04/11/2026, vague de la règle d'or n°311)

Le découpage en séances de 55 min ne change pas (activité 0 | activité 1 | activités 2 et 3 | activité 4 et REFAIRE, puis la clôture) : chaque en-tête « 🗓 Séance N » devient la tête de son onglet, chaque bouton de fin de séance ouvre la suivante, et l'onglet en cours est mémorisé. L'ouverture (étiquettes, liens « Aller à », « Avant de commencer », situation, problématique et hypothèse, sécurité, « Trois façons », billet d'entrée) est complète à la séance 1 et repliée dans le volet « 📖 Rappel » dès la séance 2, jamais supprimée. Sans JavaScript, la page reste d'un seul tenant.

Restent visibles à chaque séance : le titre, la mission, la barre d'outils et la navigation du site. L'établi sert aux séances 3 et 4 : dans l'activité 2 à la séance 3, juste après l'en-tête à la séance 4 ; aux séances 1 et 2, où l'on choisit avant de monter, il n'est pas à l'écran. L'encadré Sécurité reste dans l'ouverture : le lien « relis l'encadré Sécurité » de la séance 3 ouvre le volet et l'amène à l'écran. L'en-tête de la séance 4 dit « L'établi de l'activité 2 te suit » au lieu de « plus haut ».

Clôture : un corrigé du Bonus (le collège voisin : un seul constituant change, l'écran LCD remplace le bandeau, 580 → 120 mA lus à l'établi, et l'établi refuse parce qu'il juge avec le cahier des charges du collège), « Comment j'ai travaillé », « Je me positionne » sur 3e_C7.5 aux niveaux du livret : chaque phrase d'origine est rangée au niveau de son sens (« si on m'aide », « si on me rappelle » : fragile ; « seul » : satisfaisante), une phrase neuve dit la très bonne maîtrise (l'expliquer à un camarade ou le refaire ailleurs), et une réponse donnée avant se relit avec sa phrase et sur 3e_C4.3.

Sécurité visible (retouche du 04/11/2026) : l'en-tête de la séance 4 (retirer la batterie, re-tester) reçoit la même ligne que la séance 3 — « relis l'encadré Sécurité », très basse tension, bandeau qui chauffe, mât au sol —, dont le lien ouvre le volet.
