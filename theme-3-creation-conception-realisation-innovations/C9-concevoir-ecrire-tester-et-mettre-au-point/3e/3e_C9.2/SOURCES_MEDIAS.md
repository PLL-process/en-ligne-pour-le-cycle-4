# Sources des médias — Lot 3e_C9.2 + 3e_C8.3 « La station d'alerte cyclonique se programme »

Tous les médias de ce lot sont des **créations originales** réalisées pour le projet
(SVG écrits à la main). Aucune image extraite d'un manuel, de Google Images ou d'un
site tiers. Aucun hotlinking. Les planches de la séance 2 sont des **reconstitutions
schématiques** du programme en blocs Vittascience, étiquetées comme telles dans
l'image ET dans son texte alternatif (règles n°70/73/75 : pas de faux noms de
boutons, valeurs déclarées comme exemples).

**Les exceptions assumées** sont **quinze captures d'écran réelles**, toutes produites
conformément à la **règle d'or n°94** — une capture d'écran vient du vrai logiciel
exécuté sur un poste, jamais d'une reconstitution présentée comme une capture, jamais
d'une image trouvée en ligne :

* **deux captures d'ArduBlock Éducation 1.7** (bonus facultatif de la séance 2), prises
  sur le poste du laboratoire de technologie le 20/08/2026 ;
* **treize captures de Vittascience** (`Images/vittascience/`), prises le 25/08/2026
  pendant la construction et l'exécution du programme de référence à quatre niveaux :
  sept captures de la **structure du programme** (démarrage, haut et bas de la boucle,
  quatre sous-programmes de mode) et six captures du **simulateur aux six valeurs
  frontières** (62, 63, 117, 118, 177, 178 km/h).

Aucune de ces images n'est retouchée. Elles ne montrent que l'interface du logiciel et
le programme construit pour ce lot ; aucune donnée personnelle, aucun identifiant,
aucun nom de compte n'y figure.

**Deux écarts sont signalés à l'élève dans la page plutôt que corrigés dans l'image**,
parce qu'une capture ne se retouche pas : le programme réel attend **300 ms** là où la
consigne du palier 1 dit 200 ms, et le simulateur de Vittascience **dessine tous les
voyants en vert** quelle que soit la couleur réelle de la DEL. Le second point est
même devenu un argument pédagogique : il justifie que le niveau soit **toujours écrit
en toutes lettres** sur l'écran (règle d'or n°119).

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
| `Images/ordre_preactionneur_trois_cas.svg` | SVG original | Création Fable pour ce projet | CC0 | Image-objet : où atterrit la flèche d'ORDRE, en trois cas comparés (voyant 5 V direct · gyrophare 12 V avec relais · portail avec moteur ET transmission) — act. 1 | ~10 Ko |
| `Images/vittascience/C_1_demarrage.png` | **Capture d'écran réelle** (règle n°94) | Écran de Vittascience (interface Arduino, mode BLOCS), 25/08/2026 — programme de référence construit pour ce lot | Capture d'interface à usage pédagogique ; le programme photographié est une création originale du lot (CC0) | Image à LIRE : les neuf affectations du bloc « au démarrage », dont l'initialisation de `niveauPrecedent` | ~61 Ko |
| `Images/vittascience/C_2_boucle_haut.png` | **Capture d'écran réelle** | idem | idem | Image à LIRE : lecture + conversion + compteur de pulsation + cascade de décision (seuil le plus haut d'abord) | ~129 Ko |
| `Images/vittascience/C_3_boucle_bas.png` | **Capture d'écran réelle** | idem | idem | Image à LIRE : la cascade d'aiguillage vers les quatre sous-programmes, la trace console, le `attendre 300 ms` | ~98 Ko |
| `Images/vittascience/C_4_mode_vert.png` | **Capture d'écran réelle** | idem | idem | Image à LIRE : un mode qui impose TOUTES les sorties — et un vert volontairement FIXE | ~82 Ko |
| `Images/vittascience/C_5_mode_jaune.png` | **Capture d'écran réelle** | idem | idem | Image à LIRE : le double signal — voyant D7 conditionné par `pulsation`, et écran qui bascule du jaune vif (255,255,0) au jaune sombre (90,90,0) | ~108 Ko |
| `Images/vittascience/C_6_mode_orange.png` | **Capture d'écran réelle** | idem | idem | Image à LIRE : même structure, autre broche, autre texte — le buzzer reste muet | ~108 Ko |
| `Images/vittascience/C_7_mode_rouge.png` | **Capture d'écran réelle** | idem | idem | Image à LIRE : le seul mode qui fait sonner le buzzer | ~107 Ko |
| `Images/vittascience/C_frontiere_062kmh_brut254.png` … `C_frontiere_178kmh_brut729.png` (6 fichiers) | **Captures d'écran réelles du simulateur** | idem, prises l'une après l'autre en déplaçant le potentiomètre | idem | Images à LIRE **par paires** : la preuve exécutée du « ≥ ». 62→veille / 63→tempête ; 117→tempête / 118→ouragan ; 177→ouragan / 178→ouragan majeur, valeur brute affichée à chaque fois | ~34 à 38 Ko chacune |
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
- **faits historiques cités dans l'encadré « jumelage »** (ouragan de 1938 dit
  « Long Island Express », Irene 2011, Sandy 2012, Henri et Ida 2021) : aucun média
  n'est repris, seulement des faits publics, reformulés et vérifiés le 21/08/2026
  auprès de sources concordantes — notamment la fiche « Hurricane Sandy » du centre de
  données de Baruch College (CUNY) pour les chiffres new-yorkais de 2012 (onde de
  tempête à Battery Park, morts dans la ville, foyers privés d'électricité) et la
  notice de l'ouragan de 1938 pour la catégorie et la vitesse des vents au moment du
  passage sur Long Island. Les ordres de grandeur sont donnés comme tels (« environ
  4 mètres », « plus de quarante morts »), jamais avec une précision qu'ils n'ont pas ;
- aucune donnée Météo-France réelle : les seuils sont ceux du cahier des charges
  pédagogique de la mairie fictive, dit explicitement aux élèves. Les **cinq niveaux
  officiels** de la vigilance cyclonique aux Antilles (jaune → orange → rouge →
  violet → gris) sont en revanche cités correctement dans la situation déclenchante,
  et la page dit clairement que le prototype, lui, décide de **quatre états du vent**
  (veille, tempête tropicale, ouragan, ouragan majeur) qui ne sont **pas** les couleurs
  de la vigilance : un encadré sourcé distingue la **mesure** (la station), la
  **vigilance** (Météo-France) et l'**alerte** (le préfet) ;
- **la distinction capture / reconstitution est visible par l'élève** : les quinze
  captures réelles (ArduBlock et Vittascience) sont déclarées comme telles dans la
  page, dans leur légende et dans leur texte alternatif ; les planches `blocs_palier*`
  portent au contraire, dans l'image elle-même, la mention « reconstitution
  schématique ». Un élève ne peut pas confondre les deux ;
- **valeur des broches de l'Arduino UNO** citée dans l'encadré « où atterrit la flèche
  d'ORDRE » (20 mA nominaux par broche, 40 mA à ne jamais dépasser) : reprise de la
  fiche technique officielle de la carte, <https://store.arduino.cc/products/arduino-uno-rev3>,
  consultée le 26/08/2026. Aucune image du site n'est reprise, seulement la valeur ;
- **seuils de vent** (63, 118, 178 km/h) : seuils de l'échelle de Saffir-Simpson —
  entrée en tempête tropicale, en ouragan de catégorie 1, en ouragan majeur de
  catégorie 3. La page dit explicitement que ces seuils décrivent l'**intensité du
  vent** et ne sont **pas** la règle de décision d'une vigilance Météo-France, qui
  croise plusieurs paramètres.
