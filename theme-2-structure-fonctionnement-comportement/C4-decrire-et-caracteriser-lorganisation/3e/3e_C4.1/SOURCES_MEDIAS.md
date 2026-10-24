# Sources des médias — Lot 3e_C4.1 + C4.2 « L'énergie de la station »

Tous les médias sont des **créations originales** (règle images v2 : image-objet).
Aucune image de manuel, de Google Images ou de site tiers ; aucun hotlinking.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/chaine_energie_a_elaborer.svg` | SVG original (Fable) | image-objet : gabarit + palette à élaborer (act. 1, QCM, synthèse) | CC0 | ~6 Ko |
| `Images/contraintes_site_cyclonique.svg` | SVG original (Fable) | image-objet : les 5 contraintes du site à lire (act. 3, QCM, synthèse) | CC0 | ~5 Ko |
| `Images/materiaux_procedes_abaque.svg` | SVG original (Fable) | image-objet : l'abaque à exploiter (act. 4, QCM, synthèse) | CC0 | ~6 Ko |

Les valeurs de dimensionnement (6 W, 72 h, 40 Ah) sont des données pédagogiques
réalistes créées pour le lot. Alt/desc complets (title + desc, role="img") dans
chaque SVG ; palette conforme à la charte commune du projet.

## Correction des chaînes — 21/10/2026

`Images/chaine_energie_a_elaborer.svg` : schéma fonctionnel corrigé, production originale CC0. Fonctions dans les blocs, composants en dessous, formes d’énergie sur les flèches ; « Énergie chimique stockée » sous les batteries. Les descriptions accessibles suivent le dessin.

Génération déterministe : `python _outils/regenerer_chaines_energie.py` depuis la racine. Source draw.io modifiable dans `_generation/chaines_energie/` (Book Train : `fichiers_drawio/`). Le SVG contient aussi cette source et utilise des textes SVG natifs, sans ressource distante.
