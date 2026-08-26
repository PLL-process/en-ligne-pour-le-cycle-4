# 3e_C9.2 — « La station d'alerte cyclonique se programme » (Thème 3 · Martinique)

> Réaliser et mettre au point un programme commandant un système réel incluant
> une interaction entre un humain et une machine.

Dossier principal du lot **3e_C9.2 + 3e_C8.3** (le dossier
[`../../../C8-valider-les-solutions-techniques-par-des/3e/3e_C8.3/`](../../../C8-valider-les-solutions-techniques-par-des/3e/3e_C8.3/README.md)
pointe ici). Objet-fil 3e du dépôt : la station décrite au Thème 2 (3e_C4.3) se
programme désormais — et se prouve.

## Ressources

* **`sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html`** — la séquence
  complète (4 séances de 1 h 30, 7 activités) : commande de la mairie avec
  exigence de PV de recette, algorithme → algorigramme (pont DNB), programmation
  **Vittascience** (interface Arduino, mode BLOCS, simulateur intégré) **par
  paliers** avec planche du résultat attendu à chaque palier — ArduBlock reste
  proposé en **bonus facultatif** avec deux captures réelles du logiciel —,
  acquittement et détection d'événement (interaction humain-machine), lecture du
  C++ généré, puis rédaction ET exécution du protocole de test.
  **Banc d'essai de la station intégré** (curseur de vent, LCD, DEL, buzzer,
  bouton d'acquittement, chrono de performance) avec verrous expérientiels —
  les activités 3, 4 et 7 exigent les manipulations réelles.
* **Les mêmes activités, découpées en quatre pages** — une par séance :
  `..._station_1_besoin-et-algorithme.html`, `..._station_2_programmer.html`,
  `..._station_3_interaction.html`, `..._station_4_recette.html`.
  **Rien n'est perdu au découpage** : l'union des quatre pages contient exactement
  les mêmes questions que la page complète (c'est un test de la suite), et les
  **réponses sont partagées** — un élève peut commencer sur une page et finir sur
  une autre sans rien réécrire, dans un sens comme dans l'autre. Chaque page
  ramène à la version tout-en-un, qui reste le **repli quand le réseau est
  capricieux** : un seul fichier, tout dedans.
* **`generer_les_quatre_pages.py`** — le générateur. Les quatre pages ne sont pas
  maintenues à la main : elles sont **engendrées** depuis la page tout-en-un.
  **On ne modifie jamais une page découpée directement** — on modifie la page
  complète, puis on relance `python3 generer_les_quatre_pages.py`. Une retouche
  faite dans une page découpée serait écrasée à la prochaine exécution, et aurait
  divergé en silence entre-temps.
* **`tests_3e_C9.2-C8.3.mjs`** — la suite de tests (125 tests, Playwright), qui
  vérifie entre autres qu'aucune question n'est perdue au découpage et que les
  réponses circulent bien entre les cinq fichiers : `node tests_3e_C9.2-C8.3.mjs .`
* **`Images/vittascience/`** — **treize captures d'écran réelles** du programme de
  référence sur Vittascience : la structure du programme (démarrage, boucle, quatre
  sous-programmes de mode) et le simulateur **aux six valeurs frontières**, à lire
  par paires (62/63, 117/118, 177/178). C'est la preuve exécutée du « ≥ ».
* **`qcm_3e_C9.2-C8.3_station_alerte_cyclonique.html`** — QCM 30 questions
  (15 par code, 4 illustrées), corrections détaillées avec réfutation de chaque
  distracteur, bilan par compétence.
* **`Synthèses/`** — synthèse élève (imprimable A4) et synthèse professeur
  (attendus, remédiations, organisation matérielle, CRCN).
* **`fiche_pedagogique_3e_C9.2-C8.3.md`**, **`matrice_couverture_3e_C9.2-C8.3.csv`**,
  **`SOURCES_MEDIAS.md`**, **`rapport_tests_3e_C9.2-C8.3.md`**.
* **`station_alerte_cyclonique/station_alerte_cyclonique.ino`** — programme C++
  de référence, commenté ligne à ligne en français (variables françaises,
  sous-programme `afficherEtat()`), compilation vérifiée pour `arduino:avr:uno`.
* **`banc-docker/`** — banc de compilation arduino-cli conteneurisé
  (**enseignant uniquement** : compte Docker requis, les élèves n'en ont pas
  besoin).

## Matériel (version 🅰) — un seul montage, une seule échelle

Arduino UNO + shield Grove (très basse tension 5 V uniquement) :

| Broche | Élément | Rôle |
|---|---|---|
| **A1** | potentiomètre / capteur rotatif Grove | anémomètre simulé, 0-1023 → **0-250 km/h** |
| **D2** | bouton Grove | acquittement de l'alarme |
| **D3** | DEL orange | ouragan (≥ 118 km/h) — pulse |
| **D4** | DEL rouge | ouragan majeur (≥ 178 km/h) — pulse |
| **D5** | buzzer Grove | alarme, en ouragan majeur seulement |
| **D6** | DEL verte | veille (< 63 km/h) — **fixe** |
| **D7** | DEL jaune | tempête tropicale (≥ 63 km/h) — pulse |
| **I2C** | écran LCD RGB 16×2 | niveau en toutes lettres + vitesse |

**Une seule échelle dans tout le dispositif : des km/h, toujours écrits avec leur
unité.** Les seuils **63 · 118 · 178** sont ceux de l'échelle de Saffir-Simpson
(entrée en tempête tropicale, entrée en ouragan, ouragan majeur) — ce ne sont pas
des valeurs inventées pour l'exercice. Les **six frontières** de recette sont donc
62/63, 117/118 et 177/178.

Le montage est **utilisable sans aucun matériel** grâce au simulateur intégré de
Vittascience, et le banc d'essai de la séquence reproduit exactement le même
comportement aux mêmes valeurs.

**Deux réserves, dites à l'élève plutôt que masquées.** Le simulateur de
Vittascience **dessine tous les voyants en vert**, quelle que soit la couleur réelle
de la DEL : on lit donc *quelle broche est ON*, jamais la couleur de l'image — et
c'est précisément pourquoi le niveau est **toujours écrit en toutes lettres** sur
l'écran. Par ailleurs, le programme de référence capturé attend **300 ms** par tour
de boucle là où la consigne du palier 1 propose 200 ms : un réglage, pas une règle,
et l'écart est expliqué en légende. Une capture ne se retouche pas.

**Logiciel** : **Vittascience**, interface Arduino en mode BLOCS
(`fr.vittascience.com/arduino`) — seul élément de la séquence qui demande une
connexion Internet, avec repli hors-ligne complet prévu en séance 2. ArduBlock
Éducation 1.7 reste disponible en **bonus facultatif** (hors parcours
obligatoire). Les versions 🅱 (banc intégré) et 🅲 (banc + traces fournies)
couvrent tout le parcours sans matériel.
