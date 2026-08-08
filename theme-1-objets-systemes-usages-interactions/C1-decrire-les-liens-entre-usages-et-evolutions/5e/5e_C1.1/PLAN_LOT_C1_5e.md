# Plan du lot — 5e_C1.1 à C1.6 « Chengdu : le collège qui mesure son air »

## Les six codes, dans le texte du référentiel

| Code | Formulation (BO n°9 du 29/02/2024, via `_outils/data_competences.py`) | Socle |
|---|---|---|
| `5e_C1.1` | Collecter, trier et analyser des données. | D2, D4 |
| `5e_C1.2` | Comparer des principes techniques pour une même fonction technique. | D4 |
| `5e_C1.3` | Décrire le rôle des systèmes d'information dans le partage d'information. | D2, D5 |
| `5e_C1.4` | Recenser des données, les identifier, les classer, les représenter, les stocker, les retrouver dans une arborescence. | D2 |
| `5e_C1.5` | Identifier des règles permettant de sécuriser un environnement numérique (bases de la cybersécurité) et des règles de respect de la propriété intellectuelle. | D3 |
| `5e_C1.6` | Appréhender la responsabilité de chacun dans les dérives (cyberviolence, atteinte à la vie privée, aux données personnelles, usurpation d'identité). | D3 |

Formulations recopiées, non reformulées (règle n°42).

## Ce que j'ai trouvé avant d'estimer

**J'ai ouvert les sept séquences du C1 avant d'écrire ce plan** — la leçon du lot 5e_C2 a servi.
Elles font de 3,7 à 15 ko et présentent toutes le même profil : de bons scénarios, aucun
vérificateur (`data-check` : 0 partout), aucune carte de référentiel, presque aucune zone de
rédaction. **Ce sont des plans rédigés en HTML, pas des séquences au gabarit maison.**

Le C1 n'est donc pas un chantier de retrofit : c'est une reconstruction. Décision prise avec
Pascal : **trois lots, un par niveau**, plutôt que quinze lots ou un rafistolage.

## L'objet-fil : Chengdu 成都

Cinquième ville du fil chinois du Thème 1, après Shanghai, Shenzhen, Hangzhou et Pékin.

**L'objet : un collège de Chengdu qui installe une station de mesure de son air.** Chengdu est
connue pour ses épisodes de pollution — le sujet est réel, et il produit ce dont les six codes ont
besoin :

| Code | Ce que l'objet fournit |
|---|---|
| C1.1 | des relevés à collecter, trier et analyser — dont certains **manifestement faux** |
| C1.2 | trois **principes techniques** pour une même fonction : mesurer une poussière |
| C1.3 | un **système d'information** : qui produit, qui stocke, qui consulte, qui décide |
| C1.4 | une **arborescence** de fichiers à concevoir, puis à retrouver |
| C1.5 | des **règles de sécurité** et de propriété intellectuelle sur les données publiées |
| C1.6 | la **responsabilité** de chacun quand une donnée devient une accusation |

**Le fil qui tient les six ensemble** : une même donnée — le relevé du capteur de la cour — parcourt
tout le lot. Elle est mesurée (C1.2), collectée et triée (C1.1), rangée (C1.4), partagée (C1.3),
protégée (C1.5), et finit par désigner quelqu'un (C1.6).

## Le passage difficile : de C1.5 à C1.6

Les deux codes de sécurité sont ceux qui se traitent le plus mal, parce qu'on les réduit vite à une
liste de consignes (« mot de passe long », « ne pas partager »). Le lot les aborde autrement :

- **C1.5** part d'un incident concret : le fichier de relevés est publié sur l'ENT du collège, et
  quelqu'un le modifie. Qui pouvait ? Pourquoi ? Qu'aurait-il fallu ?
- **C1.6** part du moment où la donnée **désigne une personne** : le pic de particules du mardi
  correspond à l'heure où un agent passe la balayeuse. Le graphique est exact. Le publier avec le
  nom de l'agent ne l'est plus.

**La responsabilité ne s'enseigne pas comme une règle, mais comme un cas où l'on a le choix.**

## Durée et découpage

**5 séances de 55 min** (275 min disponibles) — ce lot est plus long que les précédents parce qu'il
porte six codes. Découpage prévu :

1. Mesurer : trois principes pour une fonction (C1.2)
2. Collecter et trier : les relevés, dont les faux (C1.1)
3. Ranger et retrouver : l'arborescence (C1.4)
4. Partager : le système d'information (C1.3)
5. Protéger et répondre : sécurité, puis responsabilité (C1.5, C1.6)

## Les données

Toutes **simulées**, effectifs et anomalies **fixés** et non tirés au sort — leçon du lot 3e_C2 :
une donnée simulée n'a pas à être imprévisible, elle a à être vraie par rapport à ce qu'on en dit.

- **relevés horaires sur 7 jours** (PM2.5, température, humidité), avec des anomalies délibérées :
  une valeur négative, un capteur bloqué sur la même valeur, un décalage d'une heure ;
- **trois principes de mesure** comparés sur des critères réels ;
- **une arborescence** de fichiers mal nommés, à réorganiser.

## Ce que je vérifierai avant de livrer

Outre les huit règles mécanisées et les trois neuves (n°43 corrigés y compris le Bonus, n°44
infobulles, n°45 entraînement ciblé) :

1. que les **six codes** aient chacun leur activité, leur production et leurs questions de QCM —
   avec six codes, le risque est qu'un ou deux ne soient que cités ;
2. que **C1.6 ne soit pas une leçon de morale** : l'élève doit avoir un cas et un choix, pas une
   liste d'interdits ;
3. que le QCM annonce ses questions **par code** (règle n°45), un lot à six codes étant précisément
   celui où l'entraînement ciblé sert le plus.
