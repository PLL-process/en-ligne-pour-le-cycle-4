# Sources des médias — Lot 4e_C4.1 → C4.9 « Le jardin connecté »

Tous les médias sont des **créations originales** pour le projet (règle images v2 :
chaque image est un document à LIRE — aucune image décorative). Aucune image de manuel,
de Google Images ou de site tiers ; aucun hotlinking.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/chaines_jardin_connecte.svg` | SVG original (Fable) | image-objet : deux chaînes et trois flux à lire (act. 1-2, QCM q1) | CC0 | ~7 Ko |
| `Images/table_donnees_jardin.svg` | SVG original (Fable) | image-objet : trajet de la donnée + table à analyser (act. 3, QCM) | CC0 | ~6 Ko |
| `Images/reseau_jardin_ip.svg` | SVG original (Fable), dessin d'après le simulateur Cisco Packet Tracer 8 — les appareils, câbles et liaisons sans fil tels que le simulateur les montre, aucune capture de l'interface ; Cisco et Packet Tracer sont des marques de Cisco. Modifié le 20/11/2026 : internet dessiné hors du collège (la passerelle y mène), la plage DHCP écrite sous la box (.20 à .49), les deux encadrés disent que la passerelle sert à sortir du réseau | image-objet : plan du réseau et adresses à exploiter (act. 4, QCM) ; même langage visuel que les figures de SOS serre (4e_C4.7) | CC0 | ~10 Ko |
| `Images/capture_corrige_atelier_pix_tri.png` | capture de LibreOffice Calc (export PDF de la feuille, rasterisé par `pdftoppm`, rogné), fabriquée par `_generation/corrige_tableur_atelier_pix.py` le 16/11/2026 à partir des relevés de la page | corrigé de l'atelier Pix 1 « Le tableau qui dit la vérité » : les huit relevés triés par humidité croissante et la moyenne par =MOYENNE(B2:B9) — règles d'or n°332 et n°336 ; le fichier, `atelier_pix_releves_corrige.ods`, est donné avec la correction | CC0 | 29 Ko |

La synthèse élève, réécrite en deux pages le 29/10/2026, n'affiche plus ces trois schémas : elle montre les
chaînes en cases (fonction et composant dans la case, forme d'énergie sur la flèche), la donnée en quatre étapes et
le réseau en trois cases. Les schémas restent dans la séquence et le QCM.

Alt/desc intégrés à chaque SVG et aux balises d'appel ; lisibilité en niveaux de gris
vérifiée (étiquettes textuelles systématiques) ; adresses IP en plage locale 192.168.x.x ;
valeurs électriques cohérentes (12 V TBT).
- `Images/energie_stockage_transformation.svg` — schéma original (LOT 12) : stockage (batterie) vs transformation (pompe). Auteur : Claude/Fable. Licence : CC0. 25/07/2026.

## Le QCM « Automatiser le jardin » (réécrit le 19/11/2026)

`qcm_automatisation_premium.html` est réécrit au gabarit commun (30 questions). Ses deux figures sont neuves,
écrites par `_generation/figures_qcm_automatisation.py` ; l'élève les **lit** pour répondre (n°331).

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/chronogramme_eclairage_jardin.svg` | SVG original (Fable), généré | image-objet : de 16 h à 22 h, la luminosité et son seuil « nuit » de 50 lux, la présence et la LED de l'allée ; la LED s'allume aussi en plein jour, le défaut que l'élève trouve (questions 9 à 13) | CC0 | ~8 Ko |
| `Images/algorigramme_eclairage_corrige.svg` | SVG original (Fable), généré | image-objet : le programme corrigé, test « nuit ET passage », boucle (questions 21 et 22) | CC0 | ~4 Ko |

Les six pictogrammes de l'ancienne banque (`capteur_temperature`, `capteur_mouvement`, `carte_programmable`,
`moteur_cc`, `diode_led`, `signal_carre`, documentés le 31/08/2026) écrivaient la réponse dans l'image (« il
transforme l'électricité en mouvement »). Plus aucune page ne les affiche : ils sont archivés avec l'ancien QCM, dans
`_archive-anciennes-versions/C4-decrire-et-caracteriser-lorganisation/4e_C4.1/Images/`.

## Correction des chaînes — 21/10/2026

`Images/chaines_jardin_connecte.svg` : schéma fonctionnel corrigé, production originale CC0. Fonctions dans les blocs, composants en dessous, formes d’énergie sur les flèches ; « Énergie chimique stockée » sous les batteries. Les descriptions accessibles suivent le dessin.

Génération déterministe : `python _outils/regenerer_chaines_energie.py` depuis la racine. Source draw.io modifiable dans `_generation/chaines_energie/` (Book Train : `fichiers_drawio/`). Le SVG contient aussi cette source et utilise des textes SVG natifs, sans ressource distante.

## Image générée par IA (Canva) pour la synthèse élève

Demande de Pascal du 29/10/2026 : « une capture d'écran ou une illustration permet d'avoir une vision plus synthétique
de l'objet » ; Canva autorisé « pour des images réalistes et autres ». Règles : skill `synthese-vulgarisee`, §4.

| Fichier | Ce qu'elle montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/synthese_jardin_new_york_solaire.png` | Le jardin connecté dans la cour d'une école de Brooklyn : un bac en bois avec des plants de tomates, un petit panneau solaire sur un poteau, un boîtier gris de commande, une cuve d'eau avec sa pompe ; école en briques et tours au fond. PNG 1 536 × 1 024, 3.2 Mo. | **Image générée par IA** avec Canva (génération d'image), compte de Pascal, 30/10/2026 (média Canva MAHZgAqoc24). Demande : « Realistic photo of a small connected school vegetable garden in a Brooklyn, New York school courtyard: a raised wooden planter box with young tomato plants, a soil moisture sensor probe pushed into the soil with a thin cable, a small water tank with a small pump and a drip irrigation hose, a small solar panel on a pole, a grey weatherproof control box on a post, red brick school building and city towers behind, daylight, no people, no text, no logos, the whole garden visible » | Conditions Canva AI Product Terms : l'image appartient à Pascal, sans attribution exigée ; interdit de la présenter comme faite par un humain (légende « Image générée par IA (Canva) ») et d'en retirer les métadonnées de provenance (manifeste C2PA et XMP Canva gardés : **fichier non modifié**, d'où son poids). | Synthèse élève, carte « Ce que je dois retenir » ; et la situation déclenchante de la séquence (05/11/2026) |

*Le 30/10/2026, cette image remplace `synthese_jardin_connecte.png` (même demande, « in Martinique », avec des palmiers) : le jardin de 4e est à New York, et Pascal a demandé de « le passer à New York ». L'ancien fichier est retiré du lot.*

## Le réseau du jardin dans Packet Tracer (04/11/2026)

| Fichier | Type | Usage pédagogique | Licence | Poids |
|---|---|---|---|---|
| `4e_jardin_TECHNO-C4.pkt` | Fichier Packet Tracer 8.2.0 (Fable, sur le poste de Pascal) | le réseau du plan `Images/reseau_jardin_ip.svg`, construit dans le simulateur : Home Router « Box-Collège » 192.168.1.1 (DHCP de .23 à .72, son Wi-Fi coupé), Server-PT « Serveur-Collège » 192.168.1.10 sur GigabitEthernet 1, AccessPoint-PT « Borne-Cour » sur GigabitEthernet 2 (SSID « Default »), SBC-PT « Carte-Jardin » 192.168.1.50 fixe en Wi-Fi, Tablet PC-PT « Tablette-Classe » en DHCP (192.168.1.23). Pings vérifiés depuis la tablette : vers la carte et vers le serveur, 4 / 4. Activité 4, séance 3. | CC0 (montage original) ; Packet Tracer est un logiciel et une marque de Cisco | ~60 Ko |
