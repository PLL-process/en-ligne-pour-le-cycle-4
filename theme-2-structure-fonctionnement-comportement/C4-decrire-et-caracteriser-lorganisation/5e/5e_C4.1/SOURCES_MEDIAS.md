# Sources des médias — Lot 5e_C4.1 → C4.8 « Le lampadaire intelligent »

Tous les médias sont des **créations originales** (règle images v2 : image-objet).
Aucune image de manuel, de Google Images ou de site tiers ; aucun hotlinking.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/lampadaire_fonctions_solutions.svg` | SVG original (Fable) | image-objet : fonctions ↔ solutions ↔ matériaux à associer (act. 1, QCM) ; repris tel quel dans la carte « Ce que je dois retenir » de la synthèse élève, comme image de l'objet (29/10/2026) | CC0 | ~5 Ko |
| `Images/chaines_energie_information_lampadaire.svg` | SVG original (Fable) | image-objet : les deux chaînes à compléter et relier (act. 2-3, QCM) | CC0 | ~5 Ko |
| `Images/reseau_local_college_5e.svg` | SVG original (Fable) | image-objet : composants du réseau à identifier, support du jeu du courrier (act. 5-6, QCM) | CC0 | ~4 Ko |

Depuis le 29/10/2026 (format deux pages A4), la synthèse élève n'affiche plus les deux chaînes ni le réseau en
schémas : elle les montre en cases HTML, avec les fonctions et les formes d'énergie du schéma (l'interrupteur y garde
le nom que lui donne la séquence, « interrupteur commandé »).

La table des 6 lampadaires (act. 4) et les données du simulateur sont des données
fictives créées pour le lot. Alt/desc présents dans chaque SVG (title + desc,
role="img"). Palette conforme à la charte commune du projet.

## Correction des chaînes — 21/10/2026

`Images/chaines_energie_information_lampadaire.svg` : schéma fonctionnel corrigé, production originale CC0. Fonctions dans les blocs, composants en dessous, formes d’énergie sur les flèches ; « Énergie chimique stockée » sous les batteries. Les descriptions accessibles suivent le dessin.

Génération déterministe : `python _outils/regenerer_chaines_energie.py` depuis la racine. Source draw.io modifiable dans `_generation/chaines_energie/` (Book Train : `fichiers_drawio/`). Le SVG contient aussi cette source et utilise des textes SVG natifs, sans ressource distante.
