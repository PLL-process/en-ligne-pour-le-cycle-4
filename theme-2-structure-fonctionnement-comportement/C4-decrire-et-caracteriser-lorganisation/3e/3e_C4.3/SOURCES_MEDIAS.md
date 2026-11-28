# Sources des médias — Lot 3e_C4.3 → C4.6 « Station d'alerte cyclonique »

Tous les médias de ce lot sont des **créations originales** réalisées pour le projet
(SVG dessinés à la main, données générées par script). Aucune image extraite d'un manuel,
de Google Images ou d'un site tiers. Aucun hotlinking.

| Fichier | Type | Source / auteur | Licence | Alt/legende | Poids |
|---|---|---|---|---|---|
| `Images/station_alerte_annotee.svg` | SVG original | Création Fable (agent Thème 2) pour ce projet | CC0 (domaine public) | Schéma annoté de la station : capteurs, boîtier, antenne, sirène | ~6 Ko |
| `Images/chaine_information_station.svg` | SVG original | Création Fable pour ce projet | CC0 | Chaîne d'information Acquérir→Traiter→Communiquer avec natures de signaux | ~6 Ko |
| `Images/signal_analogique_vers_donnee.svg` | SVG original | Création Fable pour ce projet | CC0 | Conversion analogique→numérique (CAN 10 bits) avec formule | ~6 Ko |
| `Images/types_et_codage_donnees.svg` | SVG original | Création Fable pour ce projet | CC0 | Types de données de la station + codage binaire de la vigilance | ~7 Ko |
| `Images/types_et_codage_donnees_muet.svg` | SVG original | Création Fable pour ce projet | CC0 | Types de données de la station + codage binaire de la vigilance | version **muette** de `types_et_codage_donnees.svg` (types et descripteurs en « ? »), affichée avec les questions de l'activité 4 — règle d'or n°331, 15/11/2026 ; la version complète est dans la correction |
| `Images/transmission_stockage_fichiers.svg` | SVG original | Création Fable pour ce projet | CC0 | Parcours de la donnée : mise en forme, transmission, stockage, formats | ~7 Ko |
| `Images/transmission_stockage_fichiers_muet.svg` | SVG original | Création Fable pour ce projet | CC0 | Parcours de la donnée : mise en forme, transmission, stockage, formats | version **muette** de `transmission_stockage_fichiers.svg` (extensions en « ? »), affichée avec les questions de l'activité 5 — règle d'or n°331, 15/11/2026 ; la version complète est dans la correction |
| `donnees/mesures_station_48h_simulees.csv/.ods/.xlsx` | Jeu de données | **Données SIMULÉES** générées par script (graine fixe), ordres de grandeur réalistes d'un épisode cyclonique aux Antilles | CC0 | En-tête du fichier signale explicitement la simulation | 3-20 Ko |
| `donnees/mesures_station_48h_corrige.ods` | Classeur corrigé | Fabriqué par LibreOffice Calc piloté sans écran (`_generation/corrige_tableur.py`, outil `_outils/tableur_corrige.py`) à partir des mêmes données simulées | CC0 | Le fichier que l'élève aurait produit : 48 h colorées selon la vigilance, formules de l'enquête, feuille « Graphique » — règles d'or n°332 et n°336, 16/11/2026 | ~53 Ko |
| `Images/capture_corrige_enquete_donnees.png` | Capture d'écran | Export PDF de LibreOffice Calc (feuille « Corrigé »), rasterisé par `pdftoppm` et rogné — `_generation/corrige_tableur.py` | CC0 | Les réponses de l'enquête, leurs formules, et les lignes qui les portent ; affichée dans la correction de l'activité 6 | ~128 Ko |
| `Images/capture_corrige_graphique_vent_pression.png` | Capture d'écran | Graphique de LibreOffice Calc exporté en image par Calc lui-même (`GraphicExportFilter`) — `_generation/corrige_tableur.py` | CC0 | Vent (axe de gauche) et pression (axe secondaire) sur 48 h : la « pince » ; affichée dans le corrigé du Bonus | ~107 Ko |

Notes de conformité :
- lisibilité vérifiée en niveaux de gris (l'information ne repose jamais sur la seule couleur :
  étiquettes textuelles systématiques) ;
- textes alternatifs fournis dans les pages via `aria-label` + `<title>/<desc>` internes aux SVG ;
- aucune donnée Météo-France réelle n'est redistribuée (contrainte de licence) : les valeurs
  sont générées et signalées comme telles aux élèves dans la séquence et dans les fichiers.

Synthèse élève (29/10/2026, format deux pages A4) : `Images/station_alerte_annotee.svg` est repris tel quel dans la
carte « Ce que je dois retenir », comme image de l'objet ; la séquence l'a déjà montré à l'activité 1. La synthèse
élève de `3e_C4.1` (l'énergie de la même station) le montre aussi dans sa carte. `Images/chaine_information_station.svg`
n'est plus affiché par la synthèse élève : la chaîne d'information y est montrée en cases HTML.

## La station pièce par pièce (16/11/2026, skill anatomy)

Une figure à manipuler, posée dans l'activité 1 (séance 1) sous le schéma annoté, dans un dépliant fermé. Elle montre
chaque pièce à sa place sur la vraie station et ce que cache le coffret, qu'aucune autre image du site ne montre.
Elle dit où est chaque pièce, jamais à quoi elle sert dans la chaîne d'information (c'est l'activité), ni en quoi
elle est faite ni ses valeurs (`3e_C4.1` les fait choisir et calculer).

| Fichier | Ce qu'il montre | Provenance | Droits |
|---|---|---|---|
| `station_en_pieces.html` | La station d'alerte du collège en vue isométrique, 18 pièces numérotées et nommées ; un bouton ouvre le coffret (la porte s'écarte, ses 7 pièces sortent en colonne : module radio, baromètre, microcontrôleur, convertisseur 12 V → 5 V, fusible, régulateur de charge, batterie 12 V). | **Dessin original**, construit par programme (`_generation/station_en_pieces/build.mjs`), avec le kit Anatomy ; les pièces et leurs noms viennent des séquences de la station (`3e_C4.1`, `3e_C4.3`, `3e_C5.1`, `3e_C6.1`) | Dessin : CC BY-NC-SA 4.0, Pascal Gouacide. Le code du kit, inclus dans la page : **licence MIT, © 2026 Ryan** (texte de la licence en tête du script de la page) |
| `station_fiche_A4.pdf` | La même figure en dessin expliqué A4 : ouverte, fermée en médaillon, la liste des pièces, quatre caractéristiques, trois vues (tout en haut, sur le bras, dans le coffret). | Imprimée depuis la figure claire (`_generation/station_en_pieces/imprimer_fiche.mjs` : `scripts/print.mjs` du kit, mots passés en français, PDF par Chromium) | Comme la figure |

- **Kit** : github.com/wheresryan22/anatomy, **commit audité `1482e84`** (skill `anatomy` de Pascal, 16/11/2026). Il n'est pas
  versé dans le dépôt : la construction le lit dans `ANATOMY_DIR` (par défaut `~/.cache/anatomy-1482e84`). Aucune
  publication dans la galerie du kit.
- **Pas à l'échelle** : le coffret est un peu grossi pour qu'on voie dedans ; aucune cote n'est écrite.

## Image reprise d'un lot voisin pour la situation déclenchante (05/11/2026)

Copie, octet pour octet, de `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/3e/3e_C5.1/Images/synthese_station_alerte.png` (même provenance, mêmes droits) : elle montre le même objet, sans donner la réponse de la séquence. Demande de Pascal du 05/11/2026 : « il manque aussi des images réalistes ».

| Fichier | Ce qu'elle montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/synthese_station_alerte.png` | La station d'alerte cyclonique sur le toit d'un collège : mât, anémomètre, girouette, panneau solaire, sirène, gyrophare, boîtier ; la mer au loin. PNG 1 536 × 1 024, 2.0 Mo. | **Image générée par IA** avec Canva (génération d'image), compte de Pascal, 29/10/2026. Demande : « Realistic photo of a small autonomous cyclone warning station on a galvanized steel mast on the flat roof of a school in Martinique: cup anemometer and wind vane at the top, a small solar panel on a side arm, a white weatherproof electronics box, a horn siren and a small orange beacon light mounted on the mast, a short radio antenna, the sea in the distance, cloudy sky, no people, no text, no logos, the whole mast visible » | Conditions Canva AI Product Terms : l'image appartient à Pascal, sans attribution exigée ; interdit de la présenter comme faite par un humain (légende « Image générée par IA (Canva) ») et d'en retirer les métadonnées de provenance (manifeste C2PA et XMP Canva gardés : **fichier non modifié**, d'où son poids). | Séquence, situation déclenchante (05/11/2026) |

## Documents du QCM, dessinés pour le téléphone (28/11/2026, règle d'or n°345)

| Fichier | Ce qu'il montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/doc_extrait_mesures_station.svg` | Six lignes des mesures simulées de la station (heure, vent, pression, vigilance), une toutes les huit heures. | SVG original, dessiné par `_outils/document_qcm.py` depuis `documents_qcm_3e_C4.3.json`, lui-même LU par `documents_qcm.py` dans `donnees/mesures_station_48h_simulees.csv` (données simulées, aucune mesure réelle). | CC0, comme les images du dépôt | QCM, q17, q20, q25 |
| `Images/doc_can_barometre.svg` | L'étendue du baromètre et le nombre de bits de son CAN — sans le plus grand N ni la valeur d'un palier. | Même chaîne, lu dans la consigne de l'activité 3 de la séquence. | CC0 | QCM, q11, q13, q14 |
