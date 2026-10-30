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

## Les deux chaînes animées, et leur voix — 30/10/2026

L'animation pas à pas de la séance 2 (bloc `#chaines-lampadaire-pas-a-pas`) est **dessinée par le navigateur** à partir
d'une déclaration écrite dans la page (blocs, flèches, étapes) : aucune image nouvelle. Le moteur est une production
originale (`_generation/chaine_pas_a_pas/`, CC0, comme les schémas du lot) ; le parking, le ciel, le lampadaire et le
passant sont de simples formes tracées par le script de la page. Le schéma fixe ci-dessus reste celui du QCM, de la
synthèse et de l'impression.

| Fichier | Ce que c'est |
|---|---|
| `Audio/chaines_lampadaire_etape1.ogg` · `.mp3` | Étape 1 : voix de synthèse, 9.9 s, Opus mono 32 kb/s (40.4 Ko) et MP3 mono 48 kb/s de secours (58.2 Ko) |
| `Audio/chaines_lampadaire_etape2.ogg` · `.mp3` | Étape 2 : voix de synthèse, 9.1 s, Opus mono 32 kb/s (36.5 Ko) et MP3 mono 48 kb/s de secours (53.1 Ko) |
| `Audio/chaines_lampadaire_etape3.ogg` · `.mp3` | Étape 3 : voix de synthèse, 6.3 s, Opus mono 32 kb/s (25.4 Ko) et MP3 mono 48 kb/s de secours (36.9 Ko) |
| `Audio/chaines_lampadaire_etape4.ogg` · `.mp3` | Étape 4 : voix de synthèse, 5.0 s, Opus mono 32 kb/s (20.1 Ko) et MP3 mono 48 kb/s de secours (29.4 Ko) |
| `Audio/chaines_lampadaire_etape5.ogg` · `.mp3` | Étape 5 : voix de synthèse, 10.9 s, Opus mono 32 kb/s (43.6 Ko) et MP3 mono 48 kb/s de secours (63.7 Ko) |
| `Audio/chaines_lampadaire_etape6.ogg` · `.mp3` | Étape 6 : voix de synthèse, 6.6 s, Opus mono 32 kb/s (27.0 Ko) et MP3 mono 48 kb/s de secours (38.6 Ko) |
| `Audio/chaines_lampadaire_etape7.ogg` · `.mp3` | Étape 7 : voix de synthèse, 5.5 s, Opus mono 32 kb/s (22.8 Ko) et MP3 mono 48 kb/s de secours (32.3 Ko) |
| `Audio/chaines_lampadaire_etape8.ogg` · `.mp3` | Étape 8 : voix de synthèse, 10.4 s, Opus mono 32 kb/s (41.4 Ko) et MP3 mono 48 kb/s de secours (60.8 Ko) |
| `Audio/chaines_lampadaire_etape9.ogg` · `.mp3` | Étape 9 : voix de synthèse, 12.6 s, Opus mono 32 kb/s (50.1 Ko) et MP3 mono 48 kb/s de secours (73.8 Ko) |

- **Moteur** : Piper (`piper-tts` 1.8.0), sous GPL-3. Il n'est pas dans le dépôt, et un fichier audio qu'il produit n'est pas une œuvre dérivée du moteur.
- **Modèle** : `fr_FR-siwis-medium`, la voix du vélo-cargo (5e_C3.1), des trois principes (5e_C1.1) et du jardin (4e_C8.1), entraînée sur la
  base **SIWIS** de l'Université d'Édimbourg (datashare.is.ed.ac.uk/handle/10283/2353) ; même fichier de modèle que le jardin (empreinte
  `b015076c…` vérifiée le 30/10/2026, dans `_generation/voix_chaines/voix.json`).
- **Licence** : **CC BY 4.0** (fiche `MODEL_CARD` livrée avec le modèle).
- **Attribution exigée** : « Voix de synthèse Piper « fr_FR-siwis-medium », entraînée sur la base SIWIS (Université d'Édimbourg), CC BY 4.0. »
  Elle figure ici, dans `voix.json` et, en version courte (« Voix de synthèse : SIWIS (CC BY 4.0) »), sous l'animation.
- **Chaîne audio** : celle des trois autres animations (silences coupés à −45 dB, −16 LUFS, crête −1,5 dB, mono).
- **Texte envoyé à la voix** : celui de la page, sauf « LED » dit « lède » (étapes 7 et 8), les nombres et « activité 2 » en toutes lettres
  (étapes 2, 5 et 9), « parking » écrit « parkinng » (étape 3 : l'automatique le disait à l'anglaise), et la règle de l'étape 5 dite « si nuit
  et passage, allumer ». Détail dans `_generation/voix_chaines/phrases.json` ; `generer.py --verifier` compare les phrases à la page.
- **Prises produites le 30/10/2026, NON ÉCOUTÉES** : à faire écouter à Pascal (`voix.json`, clé `prises`). Reproductibilité à l'octet : non
  (Piper tire du bruit à chaque prise).
