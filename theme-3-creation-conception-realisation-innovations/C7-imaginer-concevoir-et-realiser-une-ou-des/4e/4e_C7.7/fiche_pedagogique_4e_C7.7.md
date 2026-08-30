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
