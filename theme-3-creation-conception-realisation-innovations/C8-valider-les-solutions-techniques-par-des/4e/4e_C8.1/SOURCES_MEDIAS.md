# SOURCES_MEDIAS — LOT 02 (4e_C8)

| Fichier / élément | Type | Licence | Usage | Alt / description |
|---|---|---|---|---|
| ~~Schéma protocole de test (SVG inline)~~ | SVG original | CC0 | **retiré le 25/10/2026** (décision 3b de Pascal) : remplacé par l'animation ci-dessous | — |
| Animation « Une année sur le toit » (SVG inline, bloc `#annee-sur-le-toit-pas-a-pas`) | dessin original, tracé à la main en SVG et animé en script (25/10/2026) | CC0 | situation déclenchante, 7 étapes | une phrase par étape (zone lue par les lecteurs d'écran) ; description du dessin par étape (`aria-label`) ; à l'impression, la liste des 7 étapes |
| Banc de tests animé (SVG inline `#bnDessin`, activité 0) | dessin original, tracé à la main en SVG et animé en script (25/10/2026) | CC0 | 4 postes d'essai | la mesure s'écrit dans `#simRes` (zone lue) ; description du poste (`aria-label`) |

Aucune image externe. Aucun hotlinking. Aucun scan de manuel.

## Images du QCM — ajoutées le 27/08/2026 (règle d'or n°1, images v2)

| Fichier | Origine | Licence | Ce qu'il donne à LIRE |
|---|---|---|---|
| `Images/protocole_quatre_tests.svg` | Création originale Fable (2026) | CC0 | le protocole complet : quatre attendus chiffrés, les observés, et la décision « à améliorer » |
| `Images/rejouer_tout_le_protocole.svg` | Création originale Fable (2026) | CC0 | l'attache inox répare le gel et fait tomber la stabilité — visible seulement si l'on rejoue tout |
| `Images/attendu_observable.svg` | Création originale Fable (2026) | CC0 | quatre attendus inutilisables et les mêmes rendus mesurables, côte à côte |

Trois documents originaux, tracés à la main en SVG dans la palette du dépôt.
Chacun porte un `<title>` et un `<desc>` : le `<desc>` est le **document de
remplacement complet**, pas une légende — un élève qui n'accède pas à l'image
dispose de la même information, en toutes lettres.

Aucune image externe. Aucun hotlinking. Aucun scan de manuel.

## La voix de la situation déclenchante — 25/10/2026 (décision « 2a » de Pascal)

| Fichier | Ce que c'est |
|---|---|
| `Audio/situation_scene1.ogg` · `.mp3` | Étape 1 : voix de synthèse, Opus mono 32 kb/s (44.2 Ko) et MP3 mono 48 kb/s de secours (63.2 Ko) |
| `Audio/situation_scene2.ogg` · `.mp3` | Étape 2 : voix de synthèse, Opus mono 32 kb/s (28.3 Ko) et MP3 mono 48 kb/s de secours (40.6 Ko) |
| `Audio/situation_scene3.ogg` · `.mp3` | Étape 3 : voix de synthèse, Opus mono 32 kb/s (22.4 Ko) et MP3 mono 48 kb/s de secours (32.3 Ko) |
| `Audio/situation_scene4.ogg` · `.mp3` | Étape 4 : voix de synthèse, Opus mono 32 kb/s (14.8 Ko) et MP3 mono 48 kb/s de secours (21.0 Ko) |
| `Audio/situation_scene5.ogg` · `.mp3` | Étape 5 : voix de synthèse, Opus mono 32 kb/s (19.7 Ko) et MP3 mono 48 kb/s de secours (27.9 Ko) |
| `Audio/situation_scene6.ogg` · `.mp3` | Étape 6 : voix de synthèse, Opus mono 32 kb/s (17.6 Ko) et MP3 mono 48 kb/s de secours (25.6 Ko) |
| `Audio/situation_scene7.ogg` · `.mp3` | Étape 7 : voix de synthèse, Opus mono 32 kb/s (38.2 Ko) et MP3 mono 48 kb/s de secours (54.9 Ko) |

- **Moteur** : Piper (`piper-tts` 1.8.0), sous GPL-3. Il n'est pas dans le dépôt, et un fichier audio qu'il produit n'est pas une œuvre dérivée du moteur.
- **Modèle** : `fr_FR-siwis-medium`, la voix du vélo-cargo (5e_C3.1) et des trois principes (5e_C1.1), entraînée sur la base **SIWIS** de
  l'Université d'Édimbourg (datashare.is.ed.ac.uk/handle/10283/2353) ; même fichier de modèle que les trois principes (empreinte dans
  `_generation/voix_situation/voix.json`).
- **Licence** : **CC BY 4.0** (fiche `MODEL_CARD` livrée avec le modèle).
- **Attribution exigée** : « Voix de synthèse Piper « fr_FR-siwis-medium », entraînée sur la base SIWIS (Université d'Édimbourg), CC BY 4.0. »
  Elle figure ici, dans `voix.json` et, en version courte (« Voix de synthèse : SIWIS (CC BY 4.0) »), sous l'animation.
- **Chaîne audio** : celle du vélo-cargo et des trois principes (silences coupés à −45 dB, −16 LUFS, crête −1,5 dB, mono).
- **Texte envoyé à la voix** : celui de la page, sauf « LED » dit « lède » (étapes 1 et 5 ; la phonétisation automatique épelait L-E-D à
  l'étape 5), « 3 mètres » et « −8 °C » écrits en toutes lettres (étapes 5 et 6). Détail dans
  `_generation/voix_situation/phrases.json`.
- **Prises validées à l'oreille par Pascal le 25/10/2026.** L'étape 3 a été refaite : « canyon » y était francisé (« canion ») ;
  de deux nouvelles versions, Pascal a choisi la prononciation automatique (« ka-nyonne »). Trace dans `voix.json` (clé `prises`).
  Reproductibilité à l'octet : non (Piper tire du bruit à chaque prise).
