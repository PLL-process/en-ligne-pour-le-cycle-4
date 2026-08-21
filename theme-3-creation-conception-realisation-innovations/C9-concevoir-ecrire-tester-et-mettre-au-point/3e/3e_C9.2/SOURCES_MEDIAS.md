# Sources des médias — Lot 3e_C9.2 + 3e_C8.3 « La station d'alerte cyclonique se programme »

Tous les médias de ce lot sont des **créations originales** réalisées pour le projet
(SVG écrits à la main). Aucune image extraite d'un manuel, de Google Images ou d'un
site tiers. Aucun hotlinking. Les planches de la séance 2 sont des **reconstitutions
schématiques** du programme en blocs Vittascience, étiquetées comme telles dans
l'image ET dans son texte alternatif (règles n°70/73/75 : pas de faux noms de
boutons, valeurs déclarées comme exemples).

**Deux exceptions assumées, et une seule** : les deux images du bonus facultatif de la
séance 2 sont de **vraies captures d'écran** du logiciel **ArduBlock Éducation 1.7**,
prises sur le poste du laboratoire de technologie le 20/08/2026, pendant la
construction réelle du programme. Elles sont produites conformément à la **règle d'or
n°94** : toute capture d'écran d'un logiciel vient du vrai logiciel exécuté sur le
poste — jamais d'une reconstitution présentée comme une capture, jamais d'une image
trouvée en ligne. Elles ne montrent que l'interface du logiciel et le programme
construit pour ce lot ; aucune donnée personnelle n'y figure.

| Fichier | Type | Source / auteur | Licence | Rôle pédagogique (image à LIRE) | Poids |
|---|---|---|---|---|---|
| `Images/montage_station_grove.svg` | SVG original | Création Fable pour ce projet | CC0 (domaine public) | Image-objet : câblage à lire (broches A1/D2/D3/D5/I2C), utilisée en act. 3 (fiche 🅰) et au QCM (q. illustrée) | ~8 Ko |
| `Images/chaine_info_energie_station.svg` | SVG original | Création Fable pour ce projet | CC0 | Image-objet : les deux chaînes selon la règle n°6 (info en haut, énergie en bas, ordre qui descend), act. 1 | ~7 Ko |
| `Images/algorigramme_alerte.svg` | SVG original | Création Fable pour ce projet | CC0 | Image-objet : algorigramme normalisé (pont DNB) à lire en act. 2 et au QCM (q. illustrée) | ~7 Ko |
| `Images/ihm_acquittement_chronogramme.svg` | SVG original | Création Fable pour ce projet | CC0 | Image-objet : chronogramme de l'acquittement à lire en act. 4, au QCM (q. illustrée) et en synthèse | ~6 Ko |
| `Images/protocole_recette_anatomie.svg` | SVG original | Création Fable pour ce projet | CC0 | Image-objet : anatomie du protocole (frontières, tableau, performance) en act. 6, au QCM (q. illustrée) et en synthèse | ~7 Ko |
| `Images/blocs_palier1_lire_vent.svg` | SVG original (reconstitution schématique, PAS une capture) | Création Fable pour ce projet | CC0 | Image-explication : résultat attendu du palier 1 (règle n°77) | ~4 Ko |
| `Images/blocs_palier2_decider.svg` | SVG original (reconstitution schématique) | Création Fable pour ce projet | CC0 | Image-explication : résultat attendu du palier 2 | ~5 Ko |
| `Images/blocs_palier3_afficher.svg` | SVG original (reconstitution schématique) | Création Fable pour ce projet | CC0 | Image-explication : résultat attendu du palier 3 | ~5 Ko |
| `Images/blocs_palier4_acquitter.svg` | SVG original (reconstitution schématique) | Création Fable pour ce projet | CC0 | Image-explication : résultat attendu du palier 4 (act. 4) | ~5 Ko |
| `Images/bonus_ardublock_palier1.png` | **Capture d'écran réelle** (règle d'or n°94) | Écran du logiciel ArduBlock Éducation 1.7 exécuté sur le poste du labo, 20/08/2026 — programme `3e-STATION-palier1.abp` construit pour ce lot | Capture d'interface à usage pédagogique ; le programme photographié est une création originale du lot (CC0) | Image à LIRE : retrouver, dans un AUTRE logiciel de blocs, la boucle, la lecture analogique et la conversion d'échelle — bonus facultatif de la séance 2 | ~222 Ko |
| `Images/bonus_ardublock_palier2.png` | **Capture d'écran réelle** (règle d'or n°94) | Écran du logiciel ArduBlock Éducation 1.7 exécuté sur le poste du labo, 20/08/2026 — programme `3e-STATION-palier2.abp` construit pour ce lot | Capture d'interface à usage pédagogique ; le programme photographié est une création originale du lot (CC0) | Image à LIRE : retrouver la cascade de tests et l'ordre « seuil le plus haut d'abord » sous un autre habillage, à une autre échelle (km/h) — bonus facultatif | ~327 Ko |

Autres fichiers non graphiques du lot :

| Fichier | Nature | Licence |
|---|---|---|
| `station_alerte_cyclonique/station_alerte_cyclonique.ino` | Programme C++ de référence, commenté ligne à ligne en français (création originale du lot) | CC0 |
| `banc-docker/` (Dockerfile, compose.yaml, README_BANC.md) | Banc de compilation enseignant (création originale ; télécharge à la construction arduino-cli, le noyau AVR et la bibliothèque Grove LCD depuis leurs dépôts officiels) | CC0 (les outils téléchargés gardent leurs licences respectives) |
| Traces d'exécution des activités 5 et 7 | **Données SIMULÉES** écrites pour l'exercice, signalées comme telles dans la page | CC0 |

Notes de conformité :
- chaque image est un document à lire (image-objet ou image-explication) — aucune
  image décorative ;
- lisibilité vérifiée en niveaux de gris : l'information ne repose jamais sur la
  seule couleur (étiquettes textuelles systématiques, y compris sur le chronogramme
  et les écrans LCD reconstitués) ;
- textes alternatifs : `alt` complets dans les pages + `<title>/<desc>` internes à
  chaque SVG (504 à 1 188 caractères) ; toutes les images s'agrandissent à la loupe
  (règle n°92) ;
- aucune donnée Météo-France réelle : les seuils sont ceux du cahier des charges
  pédagogique de la mairie fictive, dit explicitement aux élèves. Les **cinq niveaux
  officiels** de la vigilance cyclonique aux Antilles (jaune → orange → rouge →
  violet → gris) sont en revanche cités correctement dans la situation déclenchante,
  et la page dit clairement que le prototype n'en programme que trois ;
- les deux captures ArduBlock du bonus sont des **captures réelles** du logiciel
  (règle d'or n°94) et sont déclarées comme telles dans la page, dans leur légende
  et dans leur texte alternatif — contrairement aux planches Vittascience, qui sont
  déclarées comme des reconstitutions. La distinction est visible par l'élève.
