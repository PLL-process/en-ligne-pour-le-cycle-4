# Fiche pédagogique — Atelier « Le diagramme des interacteurs extérieurs » (Le diagramme des interacteurs extérieurs, souvent appelé diagramme pieuvre)

**Niveaux** : 5e, 4e — une page par niveau, la même ressource.
**Thème** : 1 — Objets, systèmes, usages et interactions (représentation transversale : elle sert aussi les thèmes 2 et 3 quand ses codes l'y conduisent).
**Générée** le 2026-10-24 par `_generation/gouvernance.py` à partir de `donnees_interacteurs.py` : on corrige la donnée, pas la fiche.

## Deux noms

Dans le programme de technologie, ce schéma s'appelle le diagramme des interacteurs extérieurs. Dans beaucoup de livres et de classes, on l'appelle aussi le diagramme pieuvre : l'objet est la tête, les traits vers ses interacteurs sont les tentacules. Si tu rencontres l'un des deux noms, tu sauras que c'est le même schéma.

## Les codes, en toutes lettres

| Niveau | Code | Compétence du référentiel |
|---|---|---|
| 5e | 5e_C2.1 | Faire la liste des interacteurs extérieurs d’un OST. |
| 5e | 5e_C2.2 | Repérer et expliquer les choix de conception dans les domaines de l’ergonomie et de la sécurité ou en lien avec des objectifs de développement durable. |
| 4e | 4e_C2.2 | Repérer et expliquer les contraintes, exigences prises en compte (sécurité, incidences environnementales, formes et fonctions, ergonomie, qualité, fiabilité) pour répondre aux attentes des utilisateurs. |

## Où elle se place dans la démarche

Analyse externe : besoin (bête à cornes) → fonction d'usage → interacteurs (diagramme des interacteurs, « pieuvre ») → contraintes et exigences → cahier des charges.Cet atelier est le deuxième maillon. Il suit la formulation du besoin et précède le tableau des contraintes et exigences (4e_C2.1, Hangzhou) et le diagramme des exigences.

## Les verbes, niveau par niveau

- **5e** : lister, classer, compléter le diagramme et lire ses fonctions (FP, FC), puis expliquer un choix de conception par un interacteur
- **4e** : distinguer service rendu et contraintes, puis formuler une contrainte avec critère et niveau
- **3e** : pas d'exercice de ce diagramme : en 3e, le programme demande de choisir ses modes de représentation pour décrire l'expérience de l'utilisateur (3e_C2.1). Le diagramme pieuvre y est un choix possible, parmi d'autres.

## 5e — Dessiner tout ce qui entoure un objet, puis voir que chacune de ses formes répond à l'un d'eux. (≈ 40 min)

**Question de départ** : Comment montrer, d'un seul coup d'œil, tout ce qui entoure un objet et agit sur lui — sans rien oublier ?

| Exercice | Code | Durée | Objectif | Production |
|---|---|---|---|---|
| 1. Lister ce qui entoure le vélo-cargo | 5e_C2.1 | 8 min | repérer, dans une scène, tout ce qui est en dehors du vélo-cargo et en relation avec lui. | ✍ conçoit seul : une liste de cinq interacteurs extérieurs, un par ligne. |
| 2. Classer les interacteurs, écarter les fausses bulles | 5e_C2.1 | 9 min | ranger chaque interacteur dans l'une des quatre familles du programme, et reconnaître ce qui n'est pas un interacteur. | le classement de quatre interacteurs du vélo-cargo, et les fausses bulles d'un diagramme écartées. |
| 3. Compléter le diagramme pieuvre et ses fonctions | 5e_C2.1 | 11 min | compléter un diagramme des interacteurs extérieurs, écarter ce qui n'en est pas, et lire ses fonctions. | le diagramme pieuvre du vélo-cargo complété, la raison des deux intrus, et deux fonctions retrouvées. |
| 4. Relier une forme à un interacteur | 5e_C2.2 | 12 min | expliquer un choix de conception par l'interacteur qu'il sert et par son domaine. | ✍ conçoit seul : trois choix reliés à leur interacteur et à leur domaine, et une explication écrite. |

**À retenir** : Le diagramme des interacteurs extérieurs — le diagramme pieuvre — met l'objet au centre et relie à lui, par un trait, tout ce qui est en relation avec lui.Un interacteur est toujours en dehors de l'objet. Il appartient à l'une des quatre familles : usagers, données, autres objets, éléments de l'environnement.Une fonction principale (FP) relie deux éléments extérieurs en passant par l'objet : c'est le service rendu. Une fonction contrainte (FC) relie l'objet à un seul élément : c'est ce qu'il doit respecter.Un choix de conception s'explique par l'interacteur qu'il sert et par son domaine : sécurité, ergonomie, développement durable.

## 4e — Passer du dessin des interacteurs à des contraintes écrites, que l'on peut vérifier. (≈ 37 min)

**Question de départ** : Comment passer du dessin des interacteurs à une liste de contraintes que l'on peut vérifier ?

| Exercice | Code | Durée | Objectif | Production |
|---|---|---|---|---|
| 1. Le service rendu et les contraintes | 4e_C2.2 | 10 min | distinguer, dans un diagramme pieuvre, le service rendu (FP) des contraintes (FC). | le type de chacun des six traits, et la phrase de trois contraintes. |
| 2. Le cahier des charges : critère, niveau, flexibilité | 4e_C2.2 | 15 min | donner à une contrainte un critère, un niveau et une flexibilité, et dire d'où vient ce niveau. | ✍ conçoit seul : trois critères choisis, l'origine d'un niveau, quatre classes de flexibilité, et une exigence écrite avec critère et niveau. |
| 3. Ce que le concepteur a oublié | 4e_C2.2 | 12 min | repérer, dans une plainte d'usager, la contrainte qui a été oubliée, et l'expliquer avec le diagramme. | ✍ conçoit seul : quatre plaintes rangées dans leur catégorie, et une explication écrite. |

**À retenir** : La fonction principale (FP) relie deux interacteurs en passant par l'objet : c'est le service rendu. Une fonction contrainte (FC) relie l'objet à un seul interacteur : c'est une condition.Une contrainte devient une exigence vérifiable avec un critère (ce qu'on mesure) et un niveau (la valeur à atteindre).Le cahier des charges fonctionnel range les fonctions dans un tableau : fonction, désignation, critère, niveau, flexibilité. La flexibilité dit l'écart accepté autour du niveau : F0 impératif, F1 peu négociable, F2 négociable, F3 très négociable.Le niveau vient d'une norme, d'un cahier des charges, d'un label ou d'une certification. Un interacteur oublié, c'est une contrainte que personne n'écrira.

## Différenciation

- Deux aides par exercice : l'aide 1 oriente, l'aide 2 donne le raisonnement ; puis un **exercice jumeau** à valeurs différentes, avec sa correction.
- Chaque champ libre a sa **version étayée** (débuts de phrase) ; le croquis peut se décrire en mots.
- Chaque exercice se vérifie seul (retour gradué, encoches ✔ / ✘ / ○ doublées d'un mot) et a sa **correction exhaustive**, même quand tout est juste.
- La sauvegarde est locale et partagée : l'élève retrouve son travail dans l'atelier, le cahier de niveau et la séquence où l'exercice est inséré.

## Évaluation

- Positionnement de l'élève, en fin de page, sur chaque code (quatre niveaux, formulation du référentiel mot pour mot).
- QCM d'entraînement : 30 questions fixes, dont 4 illustrées, chaque distracteur réfuté.
- Aucun corrigé d'évaluation sommative dans le dépôt.

## Notes et sources

Le cours (encadré « 📘 Le cours ») et deux mécaniques — écarter les fausses bulles (exercice 2), le tableau du cahier des charges avec la flexibilité (exercice 6) — s'inspirent du cahier « 123 Techno » (Bordas 2021) utilisé par Pascal, sans rien en reprendre : objets, mots et schémas sont ceux du site. Écarts assumés avec ce cahier : aucune caractéristique (masse, esthétique) ni « législation » en bulle ; FC lue « fonction contrainte » (on signale « fonction complémentaire ») ; classes F0–F3 définies et travaillées.Choix de Pascal (13/10/2026) : le diagramme pieuvre en 5e_C2.1, 5e_C2.2 et 4e_C2.2 seulement.Demande de Pascal (24/10/2026) : le diagramme montre ses fonctions dès la 5e — la fonction principale (FP) passe par l'objet entre deux éléments, chaque fonction contrainte (FC) relie l'objet à un seul élément — et le cahier des charges de 4e porte la flexibilité, par classes F0 à F3. En 5e, l'élève LIT et complète les fonctions ; en 4e, il les FORMULE avec critère, niveau et flexibilité.Le programme ne nomme ni « pieuvre » ni « fonction contrainte » : il dit interacteurs, contraintes, exigences, cahier des charges. Le diagramme est donc toujours nommé deux fois : d'abord par le mot du programme, puis par son nom courant.Les quatre familles d'interacteurs sont celles du programme, mot pour mot : usagers, données, autres objets, éléments de l'environnement. Une norme ou une règle de la ville n'est pas un interacteur : c'est une exigence.En 4e, l'élève n'a pas forcément fait l'atelier de 5e : l'ouverture renvoie aux exercices de 5e pour rattraper en vingt minutes.
