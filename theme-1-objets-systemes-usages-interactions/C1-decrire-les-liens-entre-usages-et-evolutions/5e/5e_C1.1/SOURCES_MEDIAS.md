# Sources et licences des médias — lot 5e_C1.1 à C1.6 (Chengdu)

## Principe (règle d'or n°1)

Aucune image de ce lot ne vient d'une recherche d'images, d'un scan, ni d'un site tiers. **Les
quatre schémas sont des SVG originaux**, écrits à la main pour cette séquence, placés sous **CC0**
(domaine public), et portant chacun un `<title>` et un `<desc>` accessibles — un lecteur d'écran
restitue l'intégralité du document, pas une étiquette.

Chaque image est un **document à lire**, pas une décoration : si on la retire, une information
disparaît de la séquence.

## Les quatre schémas

| Fichier | Ce qu'il donne à lire | `desc` |
|---|---|---|
| `Images/trois_principes_de_mesure.svg` | Les trois principes de mesure des poussières, avec délai, incertitude, prix, consommation et contrainte d'entretien de chacun. Sans lui, l'activité 1 n'a pas de données. | 1 509 car. |
| `Images/corrige_arborescence.svg` | **Corrigé** (règle n°43) : les quatorze entrées mal nommées à gauche, l'arborescence rangée à droite, et les quatre règles de nommage. | 1 384 car. |
| `Images/corrige_systeme_information.svg` | **Corrigé** : les quatre étages du système d'information, et pour chacun qui a le droit d'y écrire. | 1 360 car. |
| `Images/la_donnee_qui_designe.svg` | Les trois publications du même fait vrai — nommer l'agent, taire la cause, désigner l'organisation. C'est le document central de la séance 5. | 1 476 car. |

Auteur : **Fable**, agent de production du dépôt, pour ce lot. Licence **CC0 1.0**.
Aucune police externe n'est appelée : les schémas utilisent la pile système
(`Segoe UI, system-ui, sans-serif`), et la page fonctionne **entièrement hors ligne** (règle n°40).

## Les jeux de données

Tous **simulés**, et la séquence le dit à l'élève en toutes lettres. Ils sont **déterministes**
(règle n°48) : les valeurs sur lesquelles s'appuie un corrigé sont fixées, pas tirées au sort — un
corrigé qui dépendrait d'un tirage serait faux à la régénération suivante.

| Fichier | Contenu | Ce qui y est planté |
|---|---|---|
| `releves_air_chengdu_simules.csv` | 90 relevés horaires — 7 jours × 13 h, moins une ligne | les quatre anomalies, et le pic du mardi et jeudi 7 h |
| `principes_mesure_poussieres_simules.csv` | Les trois principes et leurs cinq critères | rien — ce sont des ordres de grandeur réalistes |
| `arborescence_actuelle_simulee.csv` | 14 entrées mal nommées | les six défauts de nommage travaillés en séance 3 |

**Aucune donnée réelle, aucune personne réelle.** L'agent d'entretien de la séquence est une
construction ; la fiche pédagogique prévient qu'un élève pourra malgré tout nommer une personne de
son collège, et ce qu'il faut en faire.

Les ordres de grandeur des trois principes de mesure (temps de réponse, incertitude, prix,
consommation) sont **plausibles et arrondis**, à usage pédagogique : ils permettent de comparer, ils
ne valent pas fiche technique.

## Ce que le lot ne contient pas

- aucune capture d'écran de logiciel — les modes opératoires tableur sont **écrits**, pour
  LibreOffice Calc et Excel, et restent valables d'une version à l'autre ;
- aucune photographie ;
- aucun appel réseau, aucune police distante, aucun script tiers.

## Quatre SVG présents mais employés par aucune page (relevé du 31/08/2026)

Ces quatre fichiers sont, comme les autres, des **créations originales (Fable, CC0)**, du SVG
écrit à la main, sans raster embarqué ni référence distante. Ils sont documentés ici pour que
leur licence ne dépende de personne. Mais **aucune page du lot ne les affiche** :

| Fichier | Titre porté par le SVG | Poids |
|---|---|---|
| `Images/collecte_temperature_salles.svg` | Collecte de températures dans quatre salles | ~2 Ko |
| `Images/donnee_information_tableur.svg` | De la donnée à l'information | ~1 Ko |
| `Images/tri_filtre_moyenne.svg` | Trier, filtrer et calculer dans un tableur | ~2 Ko |
| `Images/choisir_graphique.svg` | Choisir un graphique adapté | ~2 Ko |

Deux lectures possibles, et c'est à trancher, pas à deviner : ou bien ces schémas ont été
dessinés pour des activités qui ont changé de forme et n'ont plus de place — alors ils sont à
retirer ; ou bien ils devaient illustrer la séquence et le câblage a été oublié — alors ce sont
quatre images-objets qui manquent à l'élève. `_outils/controle_medias.py` les compte et les
nomme sans les refuser : un fichier inemployé est une dette, pas un mensonge.
