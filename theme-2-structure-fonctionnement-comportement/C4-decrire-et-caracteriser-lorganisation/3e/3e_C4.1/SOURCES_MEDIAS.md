# Sources des médias — Lot 3e_C4.1 + C4.2 « L'énergie de la station »

Tous les médias sont des **créations originales** (règle images v2 : image-objet).
Aucune image de manuel, de Google Images ou de site tiers ; aucun hotlinking.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/chaine_energie_a_elaborer.svg` | SVG original (Fable) | image-objet : gabarit + palette à élaborer (act. 1, QCM) | CC0 | ~6 Ko |
| `Images/contraintes_site_cyclonique.svg` | SVG original (Fable) | image-objet : les 5 contraintes du site à lire (act. 3, QCM) | CC0 | ~5 Ko |
| `Images/materiaux_procedes_abaque.svg` | SVG original (Fable) | image-objet : l'abaque à exploiter (act. 4, QCM) | CC0 | ~6 Ko |

Les valeurs de dimensionnement (6 W, 72 h, 40 Ah) sont des données pédagogiques
réalistes créées pour le lot. Alt/desc complets (title + desc, role="img") dans
chaque SVG ; palette conforme à la charte commune du projet.

La synthèse élève n'affiche plus ces trois schémas depuis le 29/10/2026 (format deux pages A4) : elle montre la
chaîne d'énergie, les contraintes et les pièces en cases HTML. Sa carte « Ce que je dois retenir » montre l'objet
avec `../3e_C4.3/Images/station_alerte_annotee.svg`, le dessin de la même station, pris dans le lot voisin
(création originale CC0, sa provenance est écrite dans `3e_C4.3/SOURCES_MEDIAS.md`).

## Correction des chaînes — 21/10/2026

`Images/chaine_energie_a_elaborer.svg` : schéma fonctionnel corrigé, production originale CC0. Fonctions dans les blocs, composants en dessous, formes d’énergie sur les flèches ; « Énergie chimique stockée » sous les batteries. Les descriptions accessibles suivent le dessin.

Génération déterministe : `python _outils/regenerer_chaines_energie.py` depuis la racine. Source draw.io modifiable dans `_generation/chaines_energie/` (Book Train : `fichiers_drawio/`). Le SVG contient aussi cette source et utilise des textes SVG natifs, sans ressource distante.

## Image générée par IA (Canva) pour la situation déclenchante (05/11/2026)

Elle montre le problème de la séquence, jamais sa solution. Demande de Pascal du 05/11/2026 : « il manque aussi des images réalistes ».

| Fichier | Ce qu'elle montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/situation_station_reseau_coupe.png` | Sur un toit-terrasse, sous une pluie battante, un mât porte un boîtier gris et un capteur ; un câble descend vers le bâtiment. Autour, des palmiers pliés par le vent. PNG 1 536 × 1 024, 2.3 Mo. | **Image générée par IA** avec Canva (génération d'image), compte de Pascal, 05/11/2026. Demande : « Realistic photo of a small grey weather alert station box on a metal mast on the flat roof of a Caribbean school during a tropical storm, heavy rain and bending palm trees, a fallen electric power line in the street below and dark unlit houses, the station fed only by a single grey cable coming from the building, no people, no text, no logos » | Conditions Canva AI Product Terms : l'image appartient à Pascal, sans attribution exigée ; interdit de la présenter comme faite par un humain (légende « Image générée par IA (Canva) ») et d'en retirer les métadonnées de provenance (manifeste C2PA et XMP Canva gardés : **fichier non modifié**, d'où son poids). | Séquence, situation déclenchante (05/11/2026) |
