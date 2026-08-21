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

## Matériel (version 🅰) — deux montages, deux échelles

**Maquette de programmation (séance 2, Vittascience)** : Arduino UNO + shield
Grove (5 V), capteur rotatif **A0**, voyants **D2** vert · **D3** orange ·
**D4** rouge, buzzer **D5**. Échelle `niveau_vent` **0-100** (sans unité),
seuils **40** (vigilance) et **70** (alerte). Utilisable **sans aucun matériel**
grâce au simulateur intégré de Vittascience.

**Station du labo (séances 3 et 4)** : potentiomètre **A1** (anémomètre simulé),
bouton **D2** (acquittement), DEL **D3**, buzzer **D5**, LCD RGB **I2C**.
Échelle **km/h 0-250**, seuils **100** et **150** — c'est la station que l'on
recette. Très basse tension uniquement.

Les deux échelles ne se mélangent jamais : la séquence fournit un **tableau de
correspondance** (0-100 ↔ 0-250 km/h ; 40 ↔ 100 ; 70 ↔ 150 ; frontières
39/40/69/70 ↔ 99/100/149/150), seul pont autorisé entre elles.

**Logiciel** : **Vittascience**, interface Arduino en mode BLOCS
(`fr.vittascience.com/arduino`) — seul élément de la séquence qui demande une
connexion Internet, avec repli hors-ligne complet prévu en séance 2. ArduBlock
Éducation 1.7 reste disponible en **bonus facultatif** (hors parcours
obligatoire). Les versions 🅱 (banc intégré) et 🅲 (banc + traces fournies)
couvrent tout le parcours sans matériel.
