# Fiche pédagogique — 3e_C7.7 « Produire le boîtier »

| | |
|---|---|
| **Code** | `3e_C7.7` — Choisir les moyens et produire la forme voulue. |
| **Appui** | `3e_C8.1` — Mettre en œuvre une simulation pour valider la tenue mécanique d’un matériau. |
| **Niveau** | 3<sup>e</sup> · Thème 3 |
| **Durée** | 2 séances de 90 min (160 min d'activités) |
| **Socle** | D1.3 · D2 · D3 · D4 |
| **Matériel** | aucun matériel obligatoire — le banc fonctionne dans un navigateur, hors ligne |

## Problématique

> Le dessin est juste et la pièce est ratée. Que faut-il corriger — et surtout, que faut-il surtout ne pas toucher ?

## Déroulé

| # | Activité | Durée | Verrou expérientiel |
|---|---|---|---|
| 0 | Ce que la machine fera de ton dessin | 25 min | — |
| 1 | Personne ne sait produire ce dessin | 35 min | verrou : `zero` |
| 2 | Corriger le dessin, et rien d'autre | 40 min | verrou : `unSeul` |
| 3 | Une seule fournée | 35 min | — |
| 4 | REFAIRE — réinvestissement | 25 min | — |

## Les trois versions

| Version | Ce qu'elle demande |
|---|---|
| 🅰 avec l'imprimante | une éprouvette de coin — 15 mm de boîtier, 8 min — et une seconde après correction |
| 🅱 avec l'atelier de la page | un navigateur, hors ligne, rien à installer |
| 🅲 sans écran | le dessin coté au tableau et cinq bandes de papier, une par cote |

## Sécurité

Impression en **local ventilé, capot fermé** : une buse à 240 °C émet des particules
ultrafines, et l'on ne se penche pas au-dessus du plateau. La buse et le plateau restent chauds
longtemps après la fin : on décolle à la spatule, plateau refroidi, jamais aux doigts. Le retrait
des supports se fait **avec des lunettes** — un support arraché part en éclats. Le **PVC** ne
s'imprime pas et ne se découpe pas au laser. La station est alimentée en **très basse tension**,
aucun élève ne manipule le **secteur**, et la pose en tête de mât reste un geste d'agent.

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
