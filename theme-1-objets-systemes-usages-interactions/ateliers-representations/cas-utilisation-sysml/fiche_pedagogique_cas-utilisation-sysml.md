# Fiche pédagogique — Atelier « Le diagramme de cas d'utilisation » (Le diagramme de cas d'utilisation, souvent appelé use case SysML (SysML : Systems Modeling Language, le langage de modélisation des systèmes))

**Niveaux** : 5e, 4e, 3e — une page par niveau, la même ressource.
**Thème** : 1 — Objets, systèmes, usages et interactions (représentation transversale : elle sert aussi les thèmes 2 et 3 quand ses codes l'y conduisent).
**Générée** le 2026-10-24 par `_generation/gouvernance.py` à partir de `donnees_cas_utilisation.py` : on corrige la donnée, pas la fiche.

## Deux noms

Son nom français est le diagramme de cas d'utilisation ; le programme de technologie le range parmi les modes de représentation (la modélisation). Les ingénieurs l'appellent souvent par son nom anglais, use case, et précisent qu'il vient du langage SysML (Systems Modeling Language, le langage de modélisation des systèmes) : on dit alors « le use case SysML ». Si tu rencontres l'un des deux noms, c'est le même schéma.

## Les codes, en toutes lettres

| Niveau | Code | Compétence du référentiel |
|---|---|---|
| 5e | 5e_C2.1 | Faire la liste des interacteurs extérieurs d’un OST. |
| 4e | 4e_C2.1 | Décrire l’expérience de l’utilisateur (ressenti et facilité d’usage) d’un OST en partant du langage naturel (texte, croquis) pour aboutir aux schémas, graphiques, algorithmes. |
| 3e | 3e_C2.1 | Décrire l’expérience de l’utilisateur d’un OST à l’aide de modes de représentation choisis. |

## Où elle se place dans la démarche

Analyse externe : besoin (bête à cornes) → qui interagit avec le système, et pour faire quoi : les interacteurs (diagramme des interacteurs, « pieuvre ») et, à côté, les acteurs et leurs cas d'utilisation (diagramme de cas d'utilisation, use case SysML) → contraintes et exigences (diagramme des exigences) → cahier des charges.Le diagramme pieuvre fait la liste de tout ce qui entoure l'objet ; le diagramme de cas d'utilisation n'en garde que les acteurs — ceux qui s'en servent avec un but — et dit ce qu'ils font avec le système. Les deux se lisent ensemble : un interacteur sans but (la pluie, le vent) devient une exigence, pas un cas d'utilisation.

## Les verbes, niveau par niveau

- **5e** : reconnaître les acteurs parmi les interacteurs, lire un diagramme de cas d'utilisation et faire la liste de ses acteurs (5e_C2.1)
- **4e** : passer du langage naturel (verbatims d'usagers) au schéma, compléter un diagramme, puis repérer et corriger ses erreurs (4e_C2.1)
- **3e** : choisir le mode de représentation selon la question, puis construire le diagramme d'un système à partir d'un texte (3e_C2.1)

## 5e — Reconnaître, parmi tout ce qui entoure un système, ceux qui s'en servent — et pour faire quoi. (≈ 30 min)

**Question de départ** : Parmi tout ce qui entoure un système, comment reconnaître ceux qui s'en servent vraiment ?

| Exercice | Code | Durée | Objectif | Production |
|---|---|---|---|---|
| 1. Qui sont les acteurs de la station ? | 5e_C2.1 | 15 min | reconnaître, parmi ce qui entoure une station de vélos, ceux qui en sont les acteurs, et dire pourquoi les autres n'en sont pas. | ✍ conçoit seul : le classement de sept éléments avec leur raison, trois acteurs placés dans le schéma, et une phrase sur l'écran tactile. |
| 2. Lire le diagramme du lampadaire, faire la liste de ses acteurs | 5e_C2.1 | 15 min | nommer les quatre éléments d'un diagramme de cas d'utilisation, le lire, et faire la liste des acteurs d'un système. | ✍ conçoit seul : quatre éléments nommés, la lecture d'une ellipse, la raison de l'absence du soleil, et la liste des acteurs du lampadaire. |

**À retenir** : Le diagramme de cas d'utilisation — le use case du langage SysML — dit qui se sert du système, et pour faire quoi.Il a quatre éléments : la frontière du système (le cadre), les acteurs (les bonshommes, dehors), les cas d'utilisation (les ellipses, une action avec un verbe à l'infinitif) et les associations (les traits).Un acteur est une personne ou un autre système, en dehors du système, qui s'en sert avec un but.La pluie, le soleil, une donnée, un objet prêté ou une pièce ne sont pas des acteurs : ce sont des interacteurs, ou des constituants.

## 4e — Passer de ce que racontent les usagers à un schéma clair : qui fait quoi avec le système. (≈ 32 min)

**Question de départ** : Comment passer de ce que disent les usagers à un schéma clair, sans rien perdre et sans rien inventer ?

| Exercice | Code | Durée | Objectif | Production |
|---|---|---|---|---|
| 1. Du verbatim au cas d'utilisation | 4e_C2.1 | 10 min | passer de ce que disent les usagers, avec leurs mots, aux cas d'utilisation de la borne. | le cas d'utilisation de sept verbatims, et la place du ressenti. |
| 2. Compléter le diagramme de la borne | 4e_C2.1 | 10 min | compléter un diagramme de cas d'utilisation avec les cas tirés des verbatims, et écarter ce qui n'est ni un cas ni un acteur. | deux ellipses et un acteur complétés, et la raison des deux intrus. |
| 3. Repérer et corriger les erreurs d'un diagramme | 4e_C2.1 | 12 min | vérifier un diagramme de cas d'utilisation avec les règles de construction, repérer ses erreurs et en corriger deux. | ✍ conçoit seul : les cinq erreurs cochées, un cas d'utilisation réécrit, et le sort de « La pompe ». |

**À retenir** : Pour passer du langage naturel au schéma, on cherche dans chaque phrase l'action faite avec le système et on l'écrit verbe à l'infinitif + complément.Le ressenti ne se dessine pas dans le diagramme : on le garde à côté, pour une exigence, un tableau ou un graphique.Une ellipse contient une action ; un bonhomme, quelqu'un ou un autre système qui se sert du système. Une pièce n'est ni l'un ni l'autre.Pour vérifier un diagramme : des acteurs hors du cadre, chacun avec un trait et un but ; des ellipses avec un verbe, jamais une pièce.

## 3e — Choisir le mode de représentation qui répond à chaque question, puis construire le diagramme de cas d'utilisation d'un système. (≈ 31 min)

**Question de départ** : Comment choisir le mode de représentation qui montre le mieux ce que l'on veut dire, et à qui ?

| Exercice | Code | Durée | Objectif | Production |
|---|---|---|---|---|
| 1. Choisir le mode de représentation selon la question | 3e_C2.1 | 13 min | choisir, pour chaque question sur l'expérience des usagers, le mode de représentation qui y répond, et dire ce que le diagramme de cas d'utilisation ne montre pas. | ✍ conçoit seul : six questions associées à leur mode, les deux modes de l'ordre des actions, et une justification écrite. |
| 2. Construire le diagramme de la station d'alerte cyclonique | 3e_C2.1 | 18 min | construire, à partir d'un texte, le diagramme de cas d'utilisation d'un système, et justifier qu'un autre système est un acteur. | ✍ conçoit seul : le diagramme complété (trois acteurs, deux cas d'utilisation), une justification écrite, et la place du vent. |

**À retenir** : On choisit un mode de représentation d'après la question : qui fait quoi → diagramme de cas d'utilisation ; dans quel ordre, si… → algorigramme ; ce que vit l'usager, en images → storyboard ; combien → graphique ; ce qui entoure → diagramme des interacteurs.Le diagramme de cas d'utilisation ne montre ni l'ordre, ni les quantités, ni le ressenti.Pour le construire à partir d'un texte : qui agit avec un but → un acteur ; ce qu'il fait → un cas d'utilisation ; la nature et les pièces → ailleurs.Un autre système (service météo, serveur de paiement) peut être un acteur ; le vent, non.

## Différenciation

- Deux aides par exercice : l'aide 1 oriente, l'aide 2 donne le raisonnement ; puis un **exercice jumeau** à valeurs différentes, avec sa correction.
- Chaque champ libre a sa **version étayée** (débuts de phrase) ; le croquis peut se décrire en mots.
- Chaque exercice se vérifie seul (retour gradué, encoches ✔ / ✘ / ○ doublées d'un mot) et a sa **correction exhaustive**, même quand tout est juste.
- La sauvegarde est locale et partagée : l'élève retrouve son travail dans l'atelier, le cahier de niveau et la séquence où l'exercice est inséré.

## Évaluation

- Positionnement de l'élève, en fin de page, sur chaque code (quatre niveaux, formulation du référentiel mot pour mot).
- QCM d'entraînement : 30 questions fixes, dont 8 illustrées, chaque distracteur réfuté.
- Aucun corrigé d'évaluation sommative dans le dépôt.

## Notes et sources

Plan demandé par Pascal (24/10/2026) : 5e_C2.1 (reconnaître les acteurs), 4e_C2.1 (du langage naturel au schéma), 3e_C2.1 (choisir le mode, construire). Un exercice a été ajouté en 5e (lire le diagramme du lampadaire, légender ses éléments, faire la liste de ses acteurs) pour que la page de 5e atteigne 30 minutes : 7 exercices en tout (5e : 2, 4e : 3, 3e : 2).Définition retenue : un acteur est une personne ou un autre système, extérieur, qui interagit avec le système dans un cas d'utilisation, avec un but. La pluie, le vent, le soleil, une donnée, un objet prêté ne sont pas des acteurs : ils restent des interacteurs (diagramme pieuvre) et nourrissent les exigences.Inspiration : le cahier « 123 Techno » (Bordas 2021, 3e, fiche du diagramme SysML des cas d'utilisation). Mécaniques reprises, transposées à nos objets : légender les éléments du diagramme (5e, exercice 2) ; extraire acteurs et cas d'un court texte de description (3e, exercice 2) ; « lesquels sont des acteurs ? » (5e, exercice 1) ; et, du cahier de 5e (fiche croquis, schéma, algorithme), le tableau « pour chaque cas, choisir le mode de représentation », élargi ici aux modes de 3e (3e, exercice 1). Aucun énoncé, aucune image ni tournure de l'éditeur n'est repris.Divergence assumée avec ce cahier : il dessine des phénomènes (pluie, vent, température) et des matières d'œuvre (pelouse, terrasse) comme acteurs non humains, et formule parfois les cas au passif. Ici, ce sont des interacteurs, et les cas s'écrivent du point de vue de l'acteur (verbe à l'infinitif + complément). À signaler aux élèves qui ont le cahier entre les mains.Tous les acteurs sont dessinés en bonhomme, y compris les autres systèmes (serveur de paiement, service météo) : le générateur de schémas ne sait pas encore dessiner le rectangle « actor » de SysML. Le cours de 3e signale cette autre convention.Pas de relations « include » / « extend » au collège : « Payer la location » est un cas à part entière, relié à l'usager et au serveur de paiement.Le diagramme ne montre ni l'ordre ni le ressenti : c'est l'argument central de 4e (le ressenti se garde à côté, il deviendra une exigence) et de 3e (choisir l'algorigramme, le storyboard ou le graphique quand la question l'exige).Les verbatims de 4e sont imaginés, dans l'esprit de ceux de la séquence de Hangzhou (4e_C2.1) ; les modes de 3e reprennent ceux de la séquence de Pékin (3e_C2.1) ; le texte de la station d'alerte suit l'objet-fil de 3e (anémomètre, sirène, gyrophare, technicien qui teste chaque matin).
