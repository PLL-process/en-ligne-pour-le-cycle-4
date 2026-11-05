# Fiche pédagogique — 3e_C7.3 « Le boîtier de la station »

| | |
|---|---|
| **Code** | `3e_C7.3` — Choisir un matériau constitutif d’un objet et/ou système technique. |
| **Appui** | `3e_C4.2` — Justifier le choix d’un matériau et de son procédé de mise en forme au regard des contraintes techniques et environnementales. |
| **Niveau** | 3<sup>e</sup> · Thème 3 |
| **Durée** | 4 séances de 55 min (160 min d'activités) |
| **Socle** | D1.3 · D3 · D4 · D5 |
| **Matériel** | aucun matériel obligatoire — le banc fonctionne dans un navigateur, hors ligne |

## Problématique

> Aucun matériau ne tient le cahier des charges. Que fait-on — et qui paie la sortie qu'on choisit ?

## Déroulé

| Séance | # | Activité | Durée | Verrou expérientiel |
|---|---|---|---|---|
| 1 · 50 min | 0 | L'épaisseur n'est pas donnée : elle se déduit | 25 min | — |
| 1 | 1a | Personne ne passe : le verdict du banc — évaluer, associer chaque candidat à son motif | 25 min | verrou : `evalue` |
| 2 · 50 min | 1b | Personne ne passe : ce que ce zéro veut dire — deux questions, la correction | 10 min | verrou : `evalue` |
| 2 | 2 | Trois sorties, une seule à la fois | 40 min | verrou : `unSeul` |
| 3 · 35 min | 3 | Justifier le matériau ET son procédé | 35 min | — |
| 4 · 25 min | 4 | REFAIRE — réinvestissement, puis synthèse, Bonus, bilan et QCM | 25 min | — |

**Quatre séances de 55 min, et pourquoi pas trois.** Une heure par semaine : aucune paire d'activités
voisines ne tient dans une séance (25 + 35, 35 + 40, 40 + 35, 35 + 25). Trois séances (165 min)
suffiraient en comptant au plus juste, mais ne laisseraient pas, pour 160 min d'activités, les dix minutes
de lancement, de transitions et de bilan que demande la règle n°23 — c'est exactement le défaut « 170 min
pour 165 » qui l'a fait naître. On garde donc quatre séances, et **une seule activité est coupée :
l'activité 1**, entre deux parties entières — la lecture du banc et les quatre motifs d'élimination (fin de la séance 1), puis les deux questions qui tirent la conclusion de ce zéro (début de la séance 2). Chaque partie a son bouton de vérification ;
celle de l'activité entière, en tête de la séance 2, reprend aussi les champs de la première partie.
Les séances 3 (35 min) et 4 (25 min, puis la synthèse, le Bonus, le bilan et les 30 questions du QCM
d'entraînement) laissent du temps : il n'est pas comblé par une activité inventée.

## Les trois versions

| Version | Ce qu'elle demande |
|---|---|
| 🅰 avec les éprouvettes | trois plaques imprimées à 1, 2 et 3 mm et le banc de flexion de `3e_C8.2` |
| 🅱 avec le banc de la page | un navigateur, hors ligne, rien à installer |
| 🅲 sans écran | six fiches, cinq bandes d'exigences, et un seul seuil déplaçable à la fois |

## Sécurité

Le **PVC ne passe jamais au laser** — chlorure d'hydrogène. L'impression du PLA et du
PETG se fait en **local ventilé**, capot fermé, sans se pencher sur le plateau. L'aluminium et
l'inox se percent **pièce bridée, lunettes, sans gants** ; les copeaux se retirent à la brosse,
jamais aux doigts ni à l'air comprimé. La station est alimentée en **très basse tension**, aucun
élève ne manipule le **secteur**, et la pose en tête de mât est un geste d'agent, pas d'élève.

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

## Les séances passent à onglets (04/11/2026, vague de la règle d'or n°311)

Le découpage en séances de 55 min ne change pas (activité 0 et activité 1a | activité 1b et activité 2 | activité 3 | REFAIRE, puis la clôture) : chaque en-tête « 🗓 Séance N » devient la tête de son onglet, chaque bouton de fin de séance ouvre la suivante, et l'onglet en cours est mémorisé. L'ouverture (étiquettes, liens « Aller à ma séance », « Avant de commencer », situation, problématique et hypothèse, ce que les six matériaux imposent à l'atelier, « Trois façons », billet d'entrée) est complète à la séance 1 et repliée dans le volet « 📖 Rappel » dès la séance 2, jamais supprimée. Sans JavaScript, la page reste d'un seul tenant.

Restent visibles à chaque séance : le titre, la mission (elle remplace le sous-titre « Thème 3 · 3e — … »), la barre d'outils (🖨 Imprimer / PDF) et le banc des matériaux, qui sert aux séances 1 à 3 : un seul bloc, qui reste dans l'activité 1a à la séance 1 et vient juste après l'en-tête des séances 2 et 3 ; à la séance 4, il n'est ni à l'écran ni sur la fiche papier. Le renvoi de l'activité 1b dit « activité 1a, séance 1 » au lieu de « plus haut ».

Clôture : un corrigé du Bonus (d'où vient « 10 ans » : durée de vie ou bon fonctionnement le jour du cyclone, et la question au commanditaire), « Comment j'ai travaillé », « Je me positionne » sur 3e_C7.3 aux niveaux du livret : chaque phrase d'origine est rangée au niveau de son sens (« si on m'aide », « si on me rappelle » : fragile ; « seul » : satisfaisante), une phrase neuve dit la très bonne maîtrise (l'expliquer à un camarade ou le refaire ailleurs), et une réponse donnée avant se relit avec sa phrase et sur 3e_C4.2.

Sécurité visible (retouche du 04/11/2026) : l'encadré reste dans le volet, mais l'en-tête de la séance 3, où l'on manipule (voie 🅰), en rappelle la consigne en une ligne — les consignes de l'atelier (PVC, impression ventilée, perçage avec lunettes) — avec un lien qui ouvre le volet sur l'encadré.
