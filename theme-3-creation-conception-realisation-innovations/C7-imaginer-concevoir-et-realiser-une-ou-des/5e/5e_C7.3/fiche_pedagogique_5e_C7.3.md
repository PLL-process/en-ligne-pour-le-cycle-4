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

## Découpage en séances à onglets (04/11/2026, vague n°311, sur le modèle du pilote 4e_C8.1)

| Séance | Question directrice | Contenu | Temps |
|---|---|---|---|
| 1 — Lire, puis éliminer | Que dit chaque caractéristique d'un matériau, et comment le banc en élimine-t-il quatre sur six ? | Ouverture (avant de commencer, situation, problématique et idée de départ, climat, trois façons, billet), activités 0 et 1 | ouverture + 15 + 25 min |
| 2 — Retirer, choisir, refaire | Que se passe-t-il quand on retire une exigence, et comment trancher entre les deux matériaux qui restent ? | Activités 2 et 3, réinvestissement, billet de sortie, synthèse, Bonus (corrigé replié), bilan (idée de départ, « Comment j'ai travaillé », « Je me positionne » sur 5e_C7.3 et 5e_C4.4 aux quatre niveaux du livret), renvoi au QCM | 25 + 15 + 10 + 5 min + clôture |

Dès la séance 2, l'ouverture est repliée dans le volet « 📖 Rappel » (règle d'or n°311). Le banc des matériaux sert aux deux
séances : un seul exemplaire, que la page range dans la séance ouverte, sous son en-tête. Une barre d'outils (« 🖨 Imprimer /
PDF ») a été posée. Sans JavaScript, les deux séances s'affichent à la suite.

## Le billet de sortie et les documents du QCM (27/11/2026, règles d'or n°330 et n°345)

**Billet de sortie**, en fin de séance 2, juste avant le Bonus (environ 5 min, seul et sans aide ; le réinvestissement
passe à 10 min pour que la séance tienne en 55). Un objet que la séquence n'a pas étudié : **le panneau d'affichage de
la vie scolaire**, dehors, à l'entrée du collège.
- Question 1 (5e_C7.3) : retenir l'aluminium ou le contreplaqué peint, exigence par exigence. On regarde que chaque
  exigence est comparée à son seuil, pour les deux matériaux, et que le prix ne vient qu'après.
- Question 2 (5e_C4.4) : la famille et le matériau du cadre (gris, froid, léger, l'aimant n'y colle pas). On regarde
  que chaque conclusion s'appuie sur un indice observé : le toucher pour la famille, l'aimant et la masse pour le métal.
Les nombres du billet sont ceux de `materiaux.py` pour l'aluminium anodisé (25 ans au soleil, 4 sur 5 au sel).

**QCM** : sept questions sur trente se lisent sur un document dessiné pour le téléphone (q7 à q11, q14, q19), calculé
par `documents_qcm.py` depuis `materiaux.py` — « Six matériaux pour l'assise du banc » (les exigences, puis ce que tient
chaque matériau) et « Le prix de l'assise » (prix au kilogramme, masse, prix). La q9 fait maintenant lire le tableau :
chaque leurre est une ligne mal lue (le béton, l'acier), et chaque pourquoi renvoie à la ligne à relire.
