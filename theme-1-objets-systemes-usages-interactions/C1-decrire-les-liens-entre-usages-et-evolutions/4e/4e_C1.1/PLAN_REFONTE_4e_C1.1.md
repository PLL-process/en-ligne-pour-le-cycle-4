# Plan de refonte — 4e_C1.1 à C1.3 « Tsinghua : concevoir avant de connecter »

Écrit **après lecture intégrale** de l'existant (règle n°46) : la séquence, le cadrage, les données,
le rapport de contrôles et les sources.

## Ce lot est bien meilleur que son défaut ne le laissait croire

L'audit du 8 août l'a signalé pour un seul motif — **aucun champ de saisie** (règle n°67) — et il
avait raison. Mais la lecture montre un contenu **remarquable**, qu'il faut garder presque entier :

| Ce qui existe | Pourquoi c'est précieux |
|---|---|
| **Des données réelles et sourcées** | Ministère de l'Intérieur, JRC/EFFIS, ADEME Impact CO₂. C'est le **seul lot du dépôt** à travailler sur des chiffres publics vérifiables plutôt que simulés. |
| **La leçon des unités** | « 50 000 ha », « 32 feux » et « 50 % » ne s'additionnent pas — le tableur accepte l'opération, elle n'a pas de sens. |
| **Le proxy assumé** | Construire une estimation (39,68 tCO₂/ha appliqué à 50 000 ha ≈ 1,98 MtCO₂) **puis en annoncer les limites**, et interdire de la présenter comme une mesure officielle. |
| **Les périmètres** | Comparer à des équivalences — voiture, TGV, avion, repas — sans confondre véhicule-km et passager-km, et sans dire « mêmes impacts ». |
| **Le bloc CRCN** | « Utiliser un ordinateur n'est pas une compétence ; la compétence est démontrée par les transformations et les traces. » C'est **exactement** la règle n°60, écrite ici avant que nous ne la formulions. |
| **Les garde-fous humains** | Une alerte doit pouvoir être vérifiée ; une caméra tournée vers la forêt ne doit pas surveiller des personnes ; une absence de donnée n'est pas une absence de feu. |
| **L'honnêteté du bloc QCM** | « Le bouton sera activé après la création et le test du QCM afin d'éviter tout lien cassé. » On promet, on ne ment pas. |

## Ce qui manque, et qui justifie la refonte

- **Zéro `textarea`, zéro `select`, zéro `input`, zéro `button`** — alors que la page annonce quatre
  fois une « production attendue ». Les corrections existent, mais rien ne les déclenche et rien ne
  garde la trace de ce que l'élève a écrit.
- Pas d'hypothèse de départ, pas de mode essentiel, pas de tableau de bord, pas de version étayée,
  pas d'auto-positionnement, pas de découpage en séances.
- **Aucune image** : le dossier `Images/` est vide, et la lecture de données appelle au moins un
  corrigé graphique.
- **Aucun QCM**, aucune synthèse : les dossiers correspondants sont vides.
- **Aucune carte de référentiel** : les codes `4e_C1.1` à `C1.3` n'apparaissent nulle part dans la
  page, et leurs formulations non plus.

## Les codes, et le verbe du niveau (règle n°65)

| Code | Formulation du référentiel (recopiée) | Séance |
|---|---|---|
| **4e_C1.1** | Mettre en relation les OST avec leurs usages. | 1 et 4 |
| **4e_C1.2** | Identifier les avantages et les inconvénients associés aux évolutions technologiques et informatiques. | 3 et garde-fous |
| **4e_C1.3** | Justifier l'évolution d'un OST pour répondre à l'évolution des besoins. | 4 |

En 4e, le verbe est **justifier** : l'élève ne se contente plus de constater une évolution, il dit
de quel besoin elle procède.

## La séquence refondue

Quatre séances de 55 min. **195 min annoncés pour 220 disponibles.**

| Séance | Titre | Ce que l'élève produit |
|---|---|---|
| Billet | Trois réflexes de lecture de données — sans note | 3 réponses + aiguillage |
| 1 | **Lire avant de calculer** (~45 min) | Pourquoi trois valeurs ne s'additionnent pas, et le tri du fichier |
| 2 | **Estimer, et dire ce que l'estimation vaut** (~50 min) | Le ratio, l'estimation, **et l'avertissement méthodologique** |
| 3 | **Comparer sans confondre les périmètres** (~50 min) | Quatre équivalences, et la question critique de chacune |
| 4 | **Du nombre au besoin technique** (~50 min) | Le tableau besoin–information–contrainte et **cinq exigences vérifiables** |
| Bilan | Retour sur l'hypothèse, métacognition, auto-positionnement | ~10 min |

## Ce que la refonte ajoute au contenu

**Un corrigé graphique** (règle n°43) : les quatre équivalences mises en regard, avec pour chacune
son périmètre et sa question critique — c'est le point où les élèves se trompent le plus.

**Un second corrigé** : la chaîne du raisonnement, de la donnée brute à l'exigence vérifiable, qui
montre que chaque étape ajoute une incertitude et que la dernière ligne doit la porter.

**Une manipulation** (règle n°58) — plus légère qu'à Sainte-Luce, mais réelle : mesurer avec un
capteur de température du collège, ou à défaut un thermomètre, la différence entre l'air à l'ombre
et au soleil, et en déduire pourquoi un seuil de température seul déclencherait des fausses alertes.

## Ce qui ne sera pas repris

Rien de pédagogique. Seule la **forme** change. Les données réelles, les sources, les corrections,
les garde-fous et le bloc CRCN passent intégralement dans la nouvelle version.
