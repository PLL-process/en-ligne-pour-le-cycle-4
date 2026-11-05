# Fiche pédagogique — 3e_C7.7 « Produire le boîtier »

| | |
|---|---|
| **Code** | `3e_C7.7` — Choisir les moyens et produire la forme voulue. |
| **Appui** | `3e_C8.1` — Mettre en œuvre une simulation pour valider la tenue mécanique d’un matériau. |
| **Niveau** | 3<sup>e</sup> · Thème 3 |
| **Durée** | 4 séances de 55 min (160 min d'activités) |
| **Socle** | D1.3 · D2 · D3 · D4 |
| **Matériel** | aucun matériel obligatoire — le banc fonctionne dans un navigateur, hors ligne |

## Problématique

> Le dessin est juste et la pièce est ratée. Que faut-il corriger — et surtout, que faut-il surtout ne pas toucher ?

## Déroulé

| Séance | # | Activité | Durée | Verrou expérientiel |
|---|---|---|---|---|
| 1 · 50 min | 0 | Ce que la machine fera de ton dessin | 25 min | — |
| 1 | 1a | Personne ne sait produire ce dessin : le verdict de l'atelier — lancer, associer chaque cote bloquante à son motif | 25 min | verrou : `zero` |
| 2 · 50 min | 1b | Personne ne sait produire ce dessin : ce qui bloque, et ce qui va — trois questions, la correction | 10 min | verrou : `zero` |
| 2 | 2 | Corriger le dessin, et rien d'autre | 40 min | verrou : `unSeul` |
| 3 · 35 min | 3 | Une seule fournée | 35 min | — |
| 4 · 25 min | 4 | REFAIRE — réinvestissement, puis synthèse, Bonus, bilan et QCM | 25 min | — |

**Quatre séances de 55 min, et pourquoi pas trois.** Une heure par semaine : aucune paire d'activités
voisines ne tient dans une séance (25 + 35, 35 + 40, 40 + 35, 35 + 25). Trois séances (165 min)
suffiraient en comptant au plus juste, mais ne laisseraient pas, pour 160 min d'activités, les dix minutes
de lancement, de transitions et de bilan que demande la règle n°23 — c'est exactement le défaut « 170 min
pour 165 » qui l'a fait naître. On garde donc quatre séances, et **une seule activité est coupée :
l'activité 1**, entre deux parties entières — le lancement de l'atelier et les trois cotes bloquantes (fin de la séance 1), puis les trois questions sur ce qu'on fait des deux cotes qui passent (début de la séance 2). Chaque partie a son bouton de vérification ;
celle de l'activité entière, en tête de la séance 2, reprend aussi les champs de la première partie.
Les séances 3 (35 min) et 4 (25 min, puis la synthèse, le Bonus, le bilan et les 30 questions du QCM
d'entraînement) laissent du temps : il n'est pas comblé par une activité inventée.

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

## Les séances passent à onglets (04/11/2026, vague de la règle d'or n°311)

Le découpage en séances de 55 min ne change pas (activité 0 et activité 1a | activité 1b et activité 2 | activité 3 | REFAIRE, puis la clôture) : chaque en-tête « 🗓 Séance N » devient la tête de son onglet, chaque bouton de fin de séance ouvre la suivante, et l'onglet en cours est mémorisé. L'ouverture (étiquettes, liens « Aller à ma séance », « Ce que tu sais déjà faire », situation, problématique et hypothèse, ce que l'impression impose, « Trois façons ») est complète à la séance 1 et repliée dans le volet « 📖 Rappel » dès la séance 2, jamais supprimée. Sans JavaScript, la page reste d'un seul tenant.

Restent visibles à chaque séance : le titre, la mission, la barre d'outils et l'atelier des moyens, qui sert aux quatre séances (le Bonus de la séance 4 s'en sert aussi) : dans l'activité 1a à la séance 1, juste après l'en-tête aux séances 2 à 4. Le renvoi de l'activité 1b dit « activité 1a, séance 1 ».

Clôture : un corrigé du Bonus (0 moyen capable après une ou deux cotes corrigées, 1 après les trois, vérifié sur l'atelier de la page ; un dessin de fabrication passe en entier ou pas), « Comment j'ai travaillé », « Je me positionne » sur 3e_C7.7 aux niveaux du livret : chaque phrase d'origine est rangée au niveau de son sens (« si on m'aide », « si on me rappelle » : fragile ; « seul » : satisfaisante), une phrase neuve dit la très bonne maîtrise (l'expliquer à un camarade ou le refaire ailleurs), et une réponse donnée avant se relit avec sa phrase et sur 3e_C8.1.

Sécurité visible (retouche du 04/11/2026) : l'encadré reste dans le volet, mais l'en-tête de la séance 2, où l'on manipule (voie 🅰), en rappelle la consigne en une ligne — l'impression ventilée, capot fermé, la pièce décollée plateau refroidi, les lunettes — avec un lien qui ouvre le volet sur l'encadré.
