# Sources des médias — Lot 5e_C4.1 → C4.8 « Le lampadaire intelligent »

Tous les médias sont des **créations originales** (règle images v2 : image-objet).
Aucune image de manuel, de Google Images ou de site tiers ; aucun hotlinking.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/lampadaire_fonctions_solutions.svg` | SVG original (Fable) | image-objet : fonctions ↔ solutions ↔ matériaux à associer (act. 1, QCM, synthèse) | CC0 | ~5 Ko |
| `Images/chaines_energie_information_lampadaire.svg` | SVG original (Fable) | image-objet : les deux chaînes à compléter et relier (act. 2-3, QCM, synthèse) | CC0 | ~5 Ko |
| `Images/reseau_local_college_5e.svg` | SVG original (Fable) | image-objet : composants du réseau à identifier, support du jeu du courrier (act. 5-6, QCM, synthèse) | CC0 | ~4 Ko |

La table des 6 lampadaires (act. 4) et les données du simulateur sont des données
fictives créées pour le lot. Alt/desc présents dans chaque SVG (title + desc,
role="img"). Palette conforme à la charte commune du projet.

## Correction des chaînes — 21/10/2026

`Images/chaines_energie_information_lampadaire.svg` : schéma fonctionnel corrigé, production originale CC0. Fonctions dans les blocs, composants en dessous, formes d’énergie sur les flèches ; « Énergie chimique stockée » sous les batteries. Les descriptions accessibles suivent le dessin.

Génération déterministe : `python _outils/regenerer_chaines_energie.py` depuis la racine. Source draw.io modifiable dans `_generation/chaines_energie/` (Book Train : `fichiers_drawio/`). Le SVG contient aussi cette source et utilise des textes SVG natifs, sans ressource distante.
