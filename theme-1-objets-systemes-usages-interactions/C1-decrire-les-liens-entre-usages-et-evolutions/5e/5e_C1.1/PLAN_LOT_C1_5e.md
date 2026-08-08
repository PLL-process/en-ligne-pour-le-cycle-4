# Plan du lot — 5e_C1.1 à C1.6 « Chengdu : le collège qui mesure son air »

> **Ce plan est une v2.** La v1 avait été écrite sur un inventaire faux : mon relevé employait le
> même motif de recherche que le vérificateur, qui ne voyait pas les fichiers nommés avec des traits
> d'union. J'annonçais « des plans de 3,7 à 15 ko » — il y a en réalité **63 ko de contenu rien que
> sur le C1.1**. Le motif est corrigé (PR #149) ; ce plan est écrit **après lecture de l'existant**.

## Les six codes, dans le texte du référentiel

| Code | Formulation (BO n°9 du 29/02/2024) | Socle |
|---|---|---|
| `5e_C1.1` | Collecter, trier et analyser des données. | D2, D4 |
| `5e_C1.2` | Comparer des principes techniques pour une même fonction technique. | D4 |
| `5e_C1.3` | Décrire le rôle des systèmes d'information dans le partage d'information. | D2, D5 |
| `5e_C1.4` | Recenser des données, les identifier, les classer, les représenter, les stocker, les retrouver dans une arborescence. | D2 |
| `5e_C1.5` | Identifier des règles permettant de sécuriser un environnement numérique (bases de la cybersécurité) et des règles de respect de la propriété intellectuelle. | D3 |
| `5e_C1.6` | Appréhender la responsabilité de chacun dans les dérives (cyberviolence, atteinte à la vie privée, aux données personnelles, usurpation d'identité). | D3 |

Formulations recopiées, non reformulées (règle n°42).

## Ce que contient l'existant, et ce que j'en reprends

`5e_C1.1/sequence.html` (63 ko) — lu intégralement avant d'écrire ce plan.

**Ce qui est bon et sera repris :**

| Élément | Pourquoi |
|---|---|
| le triptyque **collecter · trier · analyser** | c'est la structure même du code, et elle est juste |
| les **modes opératoires tableur**, Excel FR **et** LibreOffice Calc FR | laborieux à écrire, souvent bâclés ailleurs, et un collège n'a pas toujours Excel |
| les **questions métacognitives** (« qu'ai-je réussi sans aide ? quelle stratégie m'a le plus aidé ? ») | elles vont bien au-delà d'un bilan ordinaire — elles rejoignent le skill `self-regulated-learning` |
| l'**autoévaluation à cocher** | complète bien l'auto-positionnement par code du gabarit maison |
| l'idée d'une **galerie de capteurs** avec la grandeur mesurée | utile au C1.2 — mais les images seront **refaites en SVG original** |

**Ce qui ne peut pas être repris :**

| Problème | Constat |
|---|---|
| **trois images cassées** | `{{analysis_icon}}`, `{{sensor_icon}}`, `{{sort_icon}}` — des variables de gabarit jamais remplacées. La page affiche trois images manquantes depuis sa mise en ligne. |
| **police distante** | `fonts.googleapis.com` — contraire à la règle n°40 |
| **niveau annoncé faux** | l'en-tête dit « classe de **4e** » alors que le fichier est rangé en 5e |
| **12 images en base64**, provenance inconnue | impossible d'établir leur licence : règle n°1 |
| **Arduino et pilotage d'un système** | déborde largement sur le C4 ; hors du périmètre du C1.1 |

**Décision (arrêtée avec Pascal)** : le contenu est **pillé**, puis la séquence est **archivée** dans
`_archive-anciennes-versions/` avec une note disant ce qui a été repris — et l'entrée
`_outils/heritees.json` est retirée **dans le même commit** (règle n°12).

Trois images cassées depuis la mise en ligne, c'est aussi une leçon à écrire au journal : **un
gabarit à variables qu'on ne teste pas rendu se publie avec ses variables**.

## L'objet-fil : Chengdu 成都

Cinquième ville du fil chinois. **Un collège de Chengdu installe une station de mesure de son air** —
ville réellement concernée par les épisodes de particules, ce qui rend la situation vraie.

**Le fil qui tient les six codes** : une même donnée — le relevé du capteur de la cour — les
parcourt tous. Elle est **mesurée** (C1.2), **collectée et triée** (C1.1), **rangée** (C1.4),
**partagée** (C1.3), **protégée** (C1.5), et finit par **désigner quelqu'un** (C1.6).

## Le passage difficile : de C1.5 à C1.6

Les deux codes de sécurité se traitent mal parce qu'on les réduit à une liste de consignes. Ici :

- **C1.5** part d'un incident : le fichier de relevés est publié sur l'ENT, et quelqu'un le modifie.
  Qui pouvait ? Pourquoi ? Qu'aurait-il fallu ?
- **C1.6** part du moment où la donnée **désigne une personne** : le pic de particules du mardi et
  du jeudi à 7 h correspond au passage de la balayeuse. **Le graphique est exact ; le publier avec
  le nom de l'agent ne l'est plus.**

**La responsabilité ne s'enseigne pas comme une règle, mais comme un cas où l'on a le choix.**

## Découpage — 5 séances de 55 min

1. **Mesurer** : trois principes pour une fonction (C1.2)
2. **Collecter et trier** : les relevés, dont les faux (C1.1) — tableur, Excel et LibreOffice
3. **Ranger et retrouver** : l'arborescence (C1.4)
4. **Partager** : le système d'information (C1.3)
5. **Protéger, puis répondre** : sécurité (C1.5), puis responsabilité (C1.6)

## Les données (déjà produites)

Toutes **simulées**, anomalies **posées** et non tirées au sort — leçon du lot 3e_C2.

- `releves_air_chengdu_simules.csv` — 90 relevés horaires sur 7 jours, avec **quatre anomalies
  délibérées** : une valeur négative, un capteur bloqué 6 h sur la même valeur, une heure manquante,
  une virgule décalée (251 au lieu de 25,1). Et le fait à découvrir : **pic à 7 h les mardis et
  jeudis** (67-69 µg/m³ contre 26-28 les autres jours).
- `principes_mesure_poussieres_simules.csv` — 3 principes comparés sur 7 critères réels.
- `arborescence_actuelle_simulee.csv` — 14 fichiers mal nommés (`truc.csv`, `finalV2 (copie).csv`,
  `Nouveau dossier/`), à réorganiser.

## Ce que je vérifierai avant de livrer

1. que les **six codes** aient chacun leur activité, leur production et leurs questions — avec six
   codes, le risque est qu'un ou deux ne soient que **cités** ;
2. que **C1.6 ne soit pas une leçon de morale** : un cas et un choix, pas une liste d'interdits ;
3. que les **modes opératoires tableur** couvrent **Excel et LibreOffice**, comme l'existant le
   faisait — c'est un service rendu au collège qui n'a pas de licence Microsoft ;
4. que l'archivage de l'existant retire l'entrée `heritees.json` **dans le même commit** (n°12).
