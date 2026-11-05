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
| `Images/transmission_stockage_fichiers.svg` | SVG original | Création Fable pour ce projet | CC0 | Parcours de la donnée : mise en forme, transmission, stockage, formats | ~7 Ko |
| `donnees/mesures_station_48h_simulees.csv/.ods/.xlsx` | Jeu de données | **Données SIMULÉES** générées par script (graine fixe), ordres de grandeur réalistes d'un épisode cyclonique aux Antilles | CC0 | En-tête du fichier signale explicitement la simulation | 3-8 Ko |

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

## Image reprise d'un lot voisin pour la situation déclenchante (05/11/2026)

Copie, octet pour octet, de `theme-2-structure-fonctionnement-comportement/C5-identifier-un-dysfonctionnement-dun-objet/3e/3e_C5.1/Images/synthese_station_alerte.png` (même provenance, mêmes droits) : elle montre le même objet, sans donner la réponse de la séquence. Demande de Pascal du 05/11/2026 : « il manque aussi des images réalistes ».

| Fichier | Ce qu'elle montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/synthese_station_alerte.png` | La station d'alerte cyclonique sur le toit d'un collège : mât, anémomètre, girouette, panneau solaire, sirène, gyrophare, boîtier ; la mer au loin. PNG 1 536 × 1 024, 2.0 Mo. | **Image générée par IA** avec Canva (génération d'image), compte de Pascal, 29/10/2026. Demande : « Realistic photo of a small autonomous cyclone warning station on a galvanized steel mast on the flat roof of a school in Martinique: cup anemometer and wind vane at the top, a small solar panel on a side arm, a white weatherproof electronics box, a horn siren and a small orange beacon light mounted on the mast, a short radio antenna, the sea in the distance, cloudy sky, no people, no text, no logos, the whole mast visible » | Conditions Canva AI Product Terms : l'image appartient à Pascal, sans attribution exigée ; interdit de la présenter comme faite par un humain (légende « Image générée par IA (Canva) ») et d'en retirer les métadonnées de provenance (manifeste C2PA et XMP Canva gardés : **fichier non modifié**, d'où son poids). | Séquence, situation déclenchante (05/11/2026) |
