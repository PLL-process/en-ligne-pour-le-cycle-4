# Fiche pédagogique — Atelier « Le diagramme des exigences » (Le diagramme des exigences, souvent appelé diagramme des exigences SysML)

**Niveaux** : 4e, 3e — une page par niveau, la même ressource.
**Thème** : 1 — Objets, systèmes, usages et interactions (représentation transversale : elle sert aussi les thèmes 2 et 3 quand ses codes l'y conduisent).
**Générée** le 2026-10-24 par `_generation/gouvernance.py` à partir de `donnees_exigences.py` : on corrige la donnée, pas la fiche.

## Deux noms

Le programme de technologie parle d'exigences et de cahier des charges. Le schéma qui dessine ces exigences dans des blocs reliés s'appelle le diagramme des exigences ; les ingénieurs l'appellent diagramme des exigences SysML (en anglais, requirement diagram). SysML veut dire Systems Modeling Language, « langage de modélisation des systèmes ». Si tu rencontres l'un des deux noms, tu sauras que c'est le même schéma.

## Les codes, en toutes lettres

| Niveau | Code | Compétence du référentiel |
|---|---|---|
| 4e | 4e_C2.2 | Repérer et expliquer les contraintes, exigences prises en compte (sécurité, incidences environnementales, formes et fonctions, ergonomie, qualité, fiabilité) pour répondre aux attentes des utilisateurs. |
| 4e | 4e_C8.3 | Proposer un protocole de test pour valider le comportement et les performances d’un objet technique. |
| 3e | 3e_C3.3 | Évaluer les OST selon des exigences ou des critères identifiés (caractéristiques, performances, coût, indice de réparabilité). |

## Où elle se place dans la démarche

Analyse externe : besoin (bête à cornes) → interacteurs (diagramme pieuvre) → contraintes et exigences → cahier des charges (diagramme des exigences SysML).Puis boucle de validation, en conception : une solution satisfait une exigence (lien « satisfy »), un test la vérifie (lien « verify »), et le résultat se compare au niveau et à la flexibilité — c'est ce que le programme appelle comparer les résultats obtenus aux exigences issues du cahier des charges.Cet atelier suit l'atelier du diagramme des interacteurs (4e_C2.2 : critère, niveau, flexibilité) et prolonge son cahier des charges du jardin. Il prépare la validation en conception (4e_C8.3) et le choix argumenté d'une solution en 3e (3e_C3.3).

## Les verbes, niveau par niveau

- **5e** : pas d'exercice de ce diagramme : la carte des représentations le classe en 4e / 3e, facultatif. En 5e, on reconnaît le cahier des charges et ses contraintes, sans les dessiner en blocs.
- **4e** : lire un diagramme des exigences, structurer une ligne du cahier des charges en bloc d'exigence, relier chaque exigence au test qui la vérifie (« verify »), proposer un protocole et valider un résultat avec la flexibilité
- **3e** : évaluer deux solutions exigence par exigence (« satisfy »), attribuer la flexibilité d'après ce que dit le client, puis arbitrer et justifier

## 4e — Dessiner les exigences d'un système, les ranger, et relier chacune au test qui la vérifie. (≈ 37 min)

**Question de départ** : Comment montrer d'un coup d'œil toutes les exigences d'un système — et comment prouver que chacune est tenue ?

| Exercice | Code | Durée | Objectif | Production |
|---|---|---|---|---|
| 1. Lire le diagramme des exigences du jardin | 4e_C2.2 | 10 min | lire un diagramme des exigences : ce que disent l'Id et le lien ⊕, où sont le critère et le niveau, et à quelle catégorie du programme appartient chaque exigence. | deux réponses sur la lecture du diagramme, le tri de quatre morceaux de texte (critère ou niveau) et le classement de quatre exigences. |
| 2. Du cahier des charges au bloc d'exigence | 4e_C2.2 | 12 min | transformer une ligne du cahier des charges en bloc d'exigence, et le ranger sous la bonne exigence-mère. | le nom et le texte de deux blocs, leur exigence-mère avec leur Id, et la raison d'un refus. |
| 3. Relier chaque exigence à son test, puis valider | 4e_C8.3 | 15 min | relier chaque exigence au test qui la vérifie, juger un résultat avec la flexibilité, puis proposer le protocole de test d'une nouvelle exigence. | ✍ conçoit seul : quatre liens exigence → test, quatre verdicts, et un protocole de test écrit. |

**À retenir** : Le diagramme des exigences — souvent appelé diagramme des exigences SysML — dessine chaque exigence dans un bloc : un nom, un Id, un texte avec critère et niveau.Le lien ⊕ dit qu'une exigence-mère contient ses filles ; elle n'est tenue que si toutes le sont. Une exigence dit ce que le système doit faire, jamais comment.Chaque exigence se vérifie par un test qui mesure : la flèche « verify » va du test vers l'exigence. Un protocole dit ce qu'on mesure, avec quoi, comment, et le seuil à atteindre.On valide en comparant l'écart à la flexibilité : dans la marge → validée ; hors de la marge → non validée ; en F0, aucun écart.

## 3e — Évaluer deux solutions avec un diagramme des exigences, puis choisir — et dire ce qu'on accepte. (≈ 33 min)

**Question de départ** : Quand aucune solution ne satisfait toutes les exigences, comment choisir — et comment le justifier ?

| Exercice | Code | Durée | Objectif | Production |
|---|---|---|---|---|
| 1. Évaluer deux boîtiers, exigence par exigence | 3e_C3.3 | 13 min | comparer, exigence par exigence, les valeurs déclarées de deux boîtiers aux niveaux du diagramme des exigences. | dix verdicts « satisfaite / non satisfaite » et une conclusion sur ce qu'on peut en dire. |
| 2. Ce que le client accepte : la flexibilité | 3e_C3.3 | 8 min | attribuer une classe de flexibilité (F0 à F3) à chaque exigence, d'après l'écart que le client accepte. | cinq classes de flexibilité, et la même marge écrite en chiffres. |
| 3. Arbitrer : choisir un boîtier et le justifier | 3e_C3.3 | 12 min | choisir entre deux solutions qui ne satisfont pas tout, avec les flexibilités, et justifier ce choix par écrit. | ✍ conçoit seul : un choix, une amélioration à demander, et une justification écrite. |

**À retenir** : Évaluer, c'est comparer la valeur d'une solution au niveau de chaque exigence : « au moins » → cette valeur ou plus ; « au plus » → cette valeur ou moins ; l'égalité satisfait.La flèche « satisfy » relie une solution à chaque exigence qu'elle satisfait ; la flèche « verify » relie une exigence au test qui la prouve.La flexibilité dit l'écart que le client accepte : une classe (F0 impératif → F3 très négociable) ou une tolérance chiffrée.Arbitrer : éliminer la solution qui manque une exigence F0, garder celle dont l'écart reste dans la marge, et dire l'écart accepté et l'amélioration demandée.

## Différenciation

- Deux aides par exercice : l'aide 1 oriente, l'aide 2 donne le raisonnement ; puis un **exercice jumeau** à valeurs différentes, avec sa correction.
- Chaque champ libre a sa **version étayée** (débuts de phrase) ; le croquis peut se décrire en mots.
- Chaque exercice se vérifie seul (retour gradué, encoches ✔ / ✘ / ○ doublées d'un mot) et a sa **correction exhaustive**, même quand tout est juste.
- La sauvegarde est locale et partagée : l'élève retrouve son travail dans l'atelier, le cahier de niveau et la séquence où l'exercice est inséré.

## Évaluation

- Positionnement de l'élève, en fin de page, sur chaque code (quatre niveaux, formulation du référentiel mot pour mot).
- QCM d'entraînement : 30 questions fixes, dont 5 illustrées, chaque distracteur réfuté.
- Aucun corrigé d'évaluation sommative dans le dépôt.

## Notes et sources

Plan de l'atelier, au 24/10/2026 : six exercices au lieu des cinq prévus. Ajout de l'exercice « Ce que le client accepte : la flexibilité » (3e_C3.3), demandé par Pascal : la phrase du client → la classe F0–F3, sur la station d'alerte cyclonique. L'exercice des tests (4e_C8.3) reçoit en plus un tableau de résultats à juger avec la flexibilité (un écart dans la marge F1/F2/F3 se valide, en F0 jamais).La flexibilité de 4e reprend mot pour mot celle de l'exercice 6 de l'atelier des interacteurs (12 V F0, IPX4 F1, 10 L F2, réglage F3) : même jardin, mêmes classes. En 3e, l'élève attribue lui-même les classes, puis s'en sert pour arbitrer.Convention de l'atelier : le texte d'un bloc porte toujours un critère et un niveau ; la flexibilité reste dans le tableau du cahier des charges, et peut s'ajouter au texte entre parenthèses (« (F2) »). SysML ne prévoit pas de champ « flexibilité » : c'est un usage scolaire, dit comme tel.Vocabulaire SysML retenu, et lui seul : « requirement », Id, Text, contenance (⊕), « verify » (testCase → exigence), « satisfy » (block → exigence). Pas de « refine », « deriveReqt » ni « trace » au collège.Inspiration (jamais recopiée) : cahier « 123 Techno » (Bordas 2021) — 3e DIC fiche 5 (gabarit d'exigences à légender, titre ou texte donné), 3e DIC fiche 4 (paires critère ↔ niveau, critère retrouvé par l'unité), 4e MSOST fiche 26 et 5e MSOST fiche 27 (extrait de cahier des charges + résultats de tests → écart → validé ou non, piège du minimum). Écarts de l'éditeur corrigés ici : exigences sans Id ni niveau chiffré, pas de « verify »/« satisfy », F0–F3 jamais définies, test qui exige « écart = 0 » malgré une tolérance.Faits réels, et leurs sources : codes IP — norme internationale CEI 60529 (NF EN 60529) ; IPX4 = projections d'eau de toutes directions, essai de 10 min ; indice de réparabilité — loi n°2020-105 du 10 février 2020 (dite AGEC), affichage obligatoire depuis le 1er janvier 2021 pour certaines familles d'appareils ; très basse tension : 12 V. Toutes les valeurs des boîtiers, des tests et les prix sont fictifs, et déclarés comme tels.La carte des représentations classe ce diagramme « 4e / 3e, facultatif » : aucune page de 5e. L'élève de 3e n'a pas forcément fait la 4e : le cours de 3e reprend la lecture d'un bloc, et l'ouverture renvoie aux exercices de 4e.
