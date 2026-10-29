# Sources des médias — Lot 4e_C4.1 → C4.9 « Le jardin connecté »

Tous les médias sont des **créations originales** pour le projet (règle images v2 :
chaque image est un document à LIRE — aucune image décorative). Aucune image de manuel,
de Google Images ou de site tiers ; aucun hotlinking.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/chaines_jardin_connecte.svg` | SVG original (Fable) | image-objet : deux chaînes et trois flux à lire (act. 1-2, QCM q1) | CC0 | ~7 Ko |
| `Images/table_donnees_jardin.svg` | SVG original (Fable) | image-objet : trajet de la donnée + table à analyser (act. 3, QCM) | CC0 | ~6 Ko |
| `Images/reseau_jardin_ip.svg` | SVG original (Fable) | image-objet : plan du réseau et adresses à exploiter (act. 4, QCM) | CC0 | ~6 Ko |

La synthèse élève, réécrite en deux pages le 29/10/2026, n'affiche plus ces trois schémas : elle montre les
chaînes en cases (fonction et composant dans la case, forme d'énergie sur la flèche), la donnée en quatre étapes et
le réseau en trois cases. Les schémas restent dans la séquence et le QCM.

Alt/desc intégrés à chaque SVG et aux balises d'appel ; lisibilité en niveaux de gris
vérifiée (étiquettes textuelles systématiques) ; adresses IP en plage locale 192.168.x.x ;
valeurs électriques cohérentes (12 V TBT).
- `Images/energie_stockage_transformation.svg` — schéma original (LOT 12) : stockage (batterie) vs transformation (pompe). Auteur : Claude/Fable. Licence : CC0. 25/07/2026.

## Les six pictogrammes du QCM « automatisation » (documentés le 31/08/2026)

Ce dossier porte une seconde banque, `qcm_automatisation_premium.html`, qui emploie six SVG
que ce fichier ne nommait pas — `_outils/controle_medias.py` les a relevés comme dette de
documentation. Vérifiés un par un : **SVG écrits à la main**, sans raster embarqué ni
référence distante, chacun porteur d'un `<title>` et d'un `<desc>`.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/capteur_temperature.svg` | SVG original (Fable) | image-objet : un capteur de température, à reconnaître dans la chaîne d'information | CC0 | ~1 Ko |
| `Images/capteur_mouvement.svg` | SVG original (Fable) | image-objet : un capteur de mouvement, même usage | CC0 | ~1 Ko |
| `Images/carte_programmable.svg` | SVG original (Fable) | image-objet : la carte programmable, bloc « traiter » | CC0 | ~2 Ko |
| `Images/moteur_cc.svg` | SVG original (Fable) | image-objet : un moteur à courant continu, bloc « convertir » | CC0 | ~1 Ko |
| `Images/diode_led.svg` | SVG original (Fable) | image-objet : une diode électroluminescente, sortie de la chaîne | CC0 | ~1 Ko |
| `Images/signal_carre.svg` | SVG original (Fable) | image-objet : un signal en créneaux, à lire pour distinguer TOUT ou RIEN d'une grandeur continue | CC0 | ~1 Ko |

Aucune photographie de composant réel, aucune capture de catalogue : ce sont des dessins,
lisibles en niveaux de gris et imprimables.

## Correction des chaînes — 21/10/2026

`Images/chaines_jardin_connecte.svg` : schéma fonctionnel corrigé, production originale CC0. Fonctions dans les blocs, composants en dessous, formes d’énergie sur les flèches ; « Énergie chimique stockée » sous les batteries. Les descriptions accessibles suivent le dessin.

Génération déterministe : `python _outils/regenerer_chaines_energie.py` depuis la racine. Source draw.io modifiable dans `_generation/chaines_energie/` (Book Train : `fichiers_drawio/`). Le SVG contient aussi cette source et utilise des textes SVG natifs, sans ressource distante.

## Image générée par IA (Canva) pour la synthèse élève

Demande de Pascal du 29/10/2026 : « une capture d'écran ou une illustration permet d'avoir une vision plus synthétique
de l'objet » ; Canva autorisé « pour des images réalistes et autres ». Règles : skill `synthese-vulgarisee`, §4.

| Fichier | Ce qu'elle montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/synthese_jardin_connecte.png` | Le jardin connecté du collège : un bac de culture, une cuve d'eau, un petit panneau solaire et un boîtier de commande sur un poteau. PNG 1 536 × 1 024, 3.7 Mo. | **Image générée par IA** avec Canva (génération d'image), compte de Pascal, 29/10/2026. Demande : « Realistic photo of a small connected school vegetable garden in Martinique: a raised wooden bed with young tomato plants, a soil moisture sensor probe pushed into the soil with a thin cable, a small water tank with a small pump and a drip irrigation hose, a small solar panel on a pole, a grey weatherproof control box on a post, bright tropical light, palm trees in the background, no people, no text, no logos, the whole garden visible » | Conditions Canva AI Product Terms : l'image appartient à Pascal, sans attribution exigée ; interdit de la présenter comme faite par un humain (légende « Image générée par IA (Canva) ») et d'en retirer les métadonnées de provenance (manifeste C2PA et XMP Canva gardés : **fichier non modifié**, d'où son poids). | Synthèse élève, carte « Ce que je dois retenir » |

