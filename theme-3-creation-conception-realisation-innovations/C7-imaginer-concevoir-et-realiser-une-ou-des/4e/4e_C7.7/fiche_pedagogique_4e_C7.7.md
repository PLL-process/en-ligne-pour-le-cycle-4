# Fiche pédagogique — 4e_C7.7 « Le support du capteur »

| | |
|---|---|
| **Code** | `4e_C7.7` — Choisir les moyens et produire la forme voulue. |
| **Appui** | `4e_C4.3` — Mettre en relation la forme d’une pièce avec le procédé de réalisation. |
| **Niveau** | 4<sup>e</sup> · Thème 3 |
| **Durée** | 2 séances de 55 min (95 min d'activités) |
| **Socle** | D2 · D3 · D4 |
| **Matériel** | aucun matériel obligatoire — le banc fonctionne dans un navigateur, hors ligne |

## Problématique

> Le dessin est validé. Comment savoir, avant de lancer la machine, si elle rendra bien la pièce qu'on a dessinée ?

## Déroulé

| # | Activité | Durée | Verrou expérientiel |
|---|---|---|---|
| 0 | Ce que chaque moyen ne sait pas faire | 15 min | — |
| 1 | L'atelier trie, et il dit pourquoi | 25 min | verrou : `evalue` |
| 2 | Le même dessin, deux pièces différentes | 25 min | — |
| 3 | Quatre pièces, ou trente | 15 min | verrou : `quantite` |
| 4 | REFAIRE — réinvestissement | 15 min | — |

## Les trois versions

| Version | Ce qu'elle demande |
|---|---|
| 🅰 à l'atelier | une chute de PMMA, la découpeuse laser, la fraiseuse, un pied à coulisse |
| 🅱 avec l'atelier de la page | un navigateur, hors ligne, rien à installer |
| 🅲 sans écran | cinq fiches cartonnées, une par moyen, et le dessin coté au tableau |

## Sécurité

Le **PVC ne passe jamais à la découpe laser** : chauffé, il dégage du chlorure
d'hydrogène, qui brûle les voies respiratoires et corrode la machine. Le PMMA de ce support, lui,
se découpe très bien — capot fermé, **on ne regarde pas le faisceau**, extraction pendant toute
la découpe et une minute après. À la fraiseuse : **pièce bridée**, lunettes, cheveux attachés,
manches remontées, **aucun gant** — un gant happé entraîne la main. Les copeaux se retirent à la
brosse, broche arrêtée, jamais aux doigts ni à l'air comprimé. Côté électricité, la sonde et la
station du jardin sont en **très basse tension** : aucun élève ne manipule le **secteur**.

## D'où viennent les nombres

Tous les temps, les épaisseurs minimales et les verdicts de faisabilité sont calculés par
`moyens.py`, livré dans ce dossier. **Aucun nombre n'est recopié à la main dans une page.**
Ce sont des **ordres de grandeur d'atelier de collège** : imprimante à dépôt de fil (buse
0,4 mm, couche 0,2 mm), découpeuse laser CO₂ de 40 à 60 W, petite fraiseuse 3 axes à fraise
Ø 3 mm. Ce qui doit être vrai, c'est **quel moyen sait faire quoi** — pas la seconde près.

Le module rend deux idées calculables plutôt que déclarées :

- **un moyen n'a pas de qualité, il a un domaine** — hors de ce domaine il ne fait pas
  « moins bien », il ne fait pas, ou il fait autre chose ;
- **tout moyen déforme le dessin, à sa manière, et toujours** — c'est le champ `empreinte`.

Pour rejouer les tables des deux niveaux :

```bash
python3 moyens.py
```

## Ce que la fiche ne dit pas

Ce qui se passe en classe. Un test vert dit que la page fait ce qu'elle annonce, pas qu'un élève
apprend. La grille LSU de la synthèse professeur est là pour observer, pas pour noter une page.

## Découpage en séances à onglets (04/11/2026, vague de la règle d'or n°311)

La page était d'un seul tenant ; elle a maintenant deux séances à onglets, sur le modèle du pilote 4e_C8.1 et de la vague C8. Les blocs sont déplacés, pas réécrits ; le nombre de séances annoncé (2 × 55 min) ne change pas.

| Séance | Question directrice | Contenu | Temps annoncé |
|---|---|---|---|
| 1 — Le domaine de chaque moyen | Avant de lancer une machine, comment savoir si elle sait produire la pièce dessinée ? | Ouverture, activités 0 et 1 | ouverture + 15 + 25 min |
| 2 — Deux pièces, deux quantités, puis conclure | Rendent-ils la même pièce, et à temps ? | Activités 2 et 3, réinvestissement, synthèse, Bonus (corrigé), bilan, QCM | 25 + 15 + 15 min + clôture |

**À trancher par Pascal :** la séance 2 porte 55 min d'activités, plus la clôture.

Dès la séance 2, l'ouverture (étiquettes, « Avant de commencer », situation, problématique et idée de départ, ce que l'atelier impose, trois façons, billet d'entrée) est repliée dans le volet « 📖 Rappel » ; elle est complète à la séance 1. L'en-tête de la séance 2 rappelle en une ligne la consigne de sécurité de la carte, et renvoie au volet. Restent visibles à chaque séance : le titre, la mission (elle remplace le sous-titre « Thème 3 · 4e — … », comme au pilote), la barre d'outils (🖨 Imprimer / PDF, que la page n'avait pas) et **l'atelier des moyens**, qui sert aux deux séances : un seul bloc ; à la séance 1, il reste à sa place, dans l'activité 1 (au-dessus de l'activité 0, sa colonne « Ce qu'il fera de ton dessin » en donnerait les réponses) ; dès la séance 2, le script des onglets le place juste après l'en-tête de la séance ouverte. Sans JavaScript, toutes les séances s'affichent à la suite, l'outil à sa place.

La clôture reçoit un corrigé replié du défi (13 supports : 25 + 12 × 13 = 181 min ; d'où viennent les 3 h) ; au bilan, « Comment j'ai travaillé » et « Je me positionne » aux quatre niveaux du livret scolaire, sur `4e_C7.7` et `4e_C4.3` (appui) (le menu existant passe aux quatre niveaux ; une réponse sur l'ancienne échelle se relit au niveau voisin).
