# Rapport de tests — Lot 3e_C9.2 + 3e_C8.3 « La station d'alerte cyclonique se programme »

Date : 2026-08-21 (**refonte v2** ; 1re livraison : 2026-08-19) · Agent : Fable ·
Environnement : Chromium headless (Playwright 1.55),
viewport 1280×900 + émulation téléphone 390×844 · Suite : `tests_3e_C9.2-C8.3.mjs`
(committée dans ce dossier, rejouable : `node tests_3e_C9.2-C8.3.mjs .`).

La suite **simule la séquence comme un élève** (méthode du « dé de 5e ») et prend
une **capture d'écran à chaque action** (32 captures : accueil, billet, chaque
activité validée, chaque état du banc — veille/vigilance/alerte, acquittement,
ré-armement, frontières, chrono —, bilan, persistance, mode essentiel, loupe,
QCM et ses scénarios, mobile). Les captures sont livrées à part (non committées).

## 1. Tests automatisés exécutés — 74/74 réussis

### Ce que l'enrichissement de l'encadré « jumelage » a ajouté (10 tests)

| Test | Résultat |
|---|---|
| L'encadré jumelage existe | ✅ |
| Il est **replié par défaut**, encadré interne compris (il ne coupe pas la situation déclenchante) | ✅ |
| Les cinq cas sont cités : 1938, Irene, Sandy, Henri, Ida | ✅ (5 tests) |
| La comparaison Martinique / New York est bien en tableaux (2) | ✅ |
| L'encadré est déclaré **hors parcours obligatoire** | ✅ |
| La limite du prototype est nommée (il ne mesure que le vent, pas la montée des eaux) | ✅ |


### Ce que la refonte v2 a ajouté à la suite (13 tests)

| Test | Résultat |
|---|---|
| Act. 2 : les 6 questions de lecture fine de l'algorigramme existent (`a2_q5` à `a2_q10`) | ✅ |
| Act. 2 : validée à 13/13 (algorithme + lecture b + lecture fine c) | ✅ |
| Act. 2 : la question `a2_q7` oppose bien « commentaire » et « symbole » | ✅ |
| Act. 3 : validée à 6/6 sur l'échelle de la maquette (50 puis 125 km/h par correspondance) | ✅ |
| Séance 2 : l'emplacement de l'interface Vittascience existe (`#vitta-embed`) | ✅ |
| Séance 2 : repli hors-ligne présent (lien direct fr.vittascience.com + plan B) | ✅ |
| Séance 2 : tableau de correspondance des deux échelles présent | ✅ |
| Séance 2 : ArduBlock est bien devenu un bonus facultatif hors parcours | ✅ |
| Les 2 captures réelles ArduBlock sont référencées et chargées | ✅ |

Les tests de la 1re livraison sont tous rejoués et restent au vert (51 → 64 avec
les ajouts ci-dessus).

### Séquence (`sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html`)

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS (début et fin de parcours) | ✅ |
| Billet d'entrée sans note : feedback affiché, hors progression | ✅ |
| Activités 1 et 2 : vérificateurs exacts (9/9 et 7/7), feedback « validé » | ✅ |
| **Verrou expérientiel** : l'activité 3 est REFUSÉE tant que le banc n'a pas été manipulé (message explicite) | ✅ |
| Banc d'essai : veille à 42 (LCD vert), vigilance à 120 (orange + DEL), alerte à 187 (rouge + DEL + buzzer) | ✅ |
| Activité 3 validée après manipulations (verrous lecture + 3 niveaux) | ✅ |
| Acquittement : buzzer muet, écran TOUJOURS rouge, DEL allumée | ✅ |
| Ré-armement : redescente à 50 puis remontée à 210 → le buzzer REPART sans appui | ✅ |
| Activités 4 et 5 validées (expériences tracées exigées pour la 4) | ✅ |
| Activité 6 : protocole rédigé exigé (4 familles + règle de décision) | ✅ |
| Activité 7 : exécution réelle exigée — 4 frontières (99/100/149/150) + chrono tracés, 10 verdicts, PV | ✅ |
| Chrono de performance : mesure affichée, verdict CONFORME (< 1 s) | ✅ |
| Progression 7/7, coches ✔ des 4 séances, rappel d'hypothèse au bilan | ✅ |
| **Sauvegarde/restauration** après rechargement : progression, réponses, verrous du banc | ✅ |
| Règle n°4 : un SEUL bouton QCM · Règle n°86 : 3 défis bonus, 3 corrigés repliés | ✅ |
| Règle n°29 : mode essentiel masque référentiel + corrections | ✅ |
| Règle n°92 : loupe (clic → grand format, Échap → fermeture, focus rendu) | ✅ |
| Mobile 390 px : aucun défilement horizontal (débord = 0), zéro erreur JS | ✅ |
| Zéro lien local cassé (parcours `href/src/data` des 4 HTML du lot) | ✅ |

### QCM (`qcm_3e_C9.2-C8.3_station_alerte_cyclonique.html`)

| Test | Résultat |
|---|---|
| 30 questions · 15 C9.2 / 15 C8.3 · 4 illustrées · grille complète | ✅ |
| Bonnes réponses réparties A/B/C/D = 8/7/7/8 (`fix_r.js`, graine 20260819) ; `d[r]` vide et 3 réfutations non vides sur CHAQUE question (vérifié par assertion) | ✅ |
| Réponse correcte : correction complète (bonne réponse, explication, exemple, erreur fréquente, réfutation des distracteurs, à retenir, encouragement) | ✅ |
| Question illustrée : le document s'affiche avec son alt | ✅ |
| Réponse fausse comptée · marquage 🔖 · modes 10 questions / ciblée C8.3 (15) / mes erreurs (1) | ✅ |
| Minuteur : démarrage auto à la 1re validation, pause qui fige, option sans minuteur | ✅ |
| Sauvegarde/reprise après rechargement (réponses + marquages) | ✅ |
| Zéro erreur JS sur tout le parcours | ✅ |

### Scénarios de notes (attendus calculés à la main, puis vérifiés en machine)

| Scénario | Attendu | Obtenu |
|---|---|---|
| S1 : 30/30 correctes | 20,0/20 · 100 % · 2 compétences « maîtrisées » | ✅ identique |
| S2 : 15 correctes + 15 incorrectes | 10,0/20 · 50 % | ✅ identique |
| S3 : 6 correctes + 6 incorrectes + 18 non répondues | 4,0/20 · 18 NR | ✅ identique |

### Synthèses

Chargement des deux synthèses (élève, professeur) sans erreur JS : ✅.

## 2. Contrôles statiques

- **Règles d'or mécanisées** (`python3 _outils/verif_regles_audit.py …/3e_C9.2/`) :
  **0 manquement** — n°23 (285 min annoncées + 10 de service pour 360 disponibles),
  26, 29, 30, 31 (11 étayages pour 11 zones de rédaction), 33, 34, 42 (formulations
  officielles recopiées), 51, 53, 67 au vert.
- **Syntaxe JavaScript** : `new Function()` sur chaque bloc `<script>` de la
  séquence et du QCM → OK.
- **Poids des médias** : 9 SVG originaux de 3,7 à 8,7 Ko + 2 captures PNG réelles
  (223 et 328 Ko, redimensionnées à 1400 px) — sous le seuil de 300 Ko pour les SVG,
  et assumées pour les deux captures du bonus, qui doivent rester lisibles ;
  `<title>/<desc>` accessibles dans chaque SVG (desc de 504 à 1 188 caractères).
- **Matrice de couverture** : les 30 questions rattachées à une notion enseignée ;
  aucune notion essentielle sans question ; aucune question hors séquence.
- **Aucun envoi réseau** : sauvegardes localStorage uniquement
  (`seq_3eC92-3eC83_station-alerte` / `qcm_3eC92-3eC83_station-alerte`), page
  autonome hors ligne.

## 3. Compilation du programme de référence

- `station_alerte_cyclonique.ino` : compilation vérifiée le 19/08/2026 pour
  `arduino:avr:uno` (avr-gcc 7.3 + ArduinoCore-avr + Grove_LCD_RGB_Backlight) :
  `text 6764 · data 176 · bss 393` → **OK** pour atmega328p.
- Banc Docker (`banc-docker/`) fourni pour re-prouver la compilation avec la
  chaîne officielle arduino-cli — **exécution Docker non réalisée dans cette
  session** (réservée au poste de Pascal, compte Docker requis) : consignée
  comme restant à faire.

## 4. Contrôles restant manuels (non exécutés — à faire par un humain)

- Test sur appareils réels (iOS/Android, tablette) — seul le viewport a été émulé ;
- **version 🅰 au labo** : les deux montages Grove (maquette A0 + voyants D2/D3/D4 +
  buzzer D5 pour la séance 2 ; station A1 + bouton + DEL + buzzer + LCD pour les
  séances 3-4) et le téléversement depuis Vittascience ;
- **Vittascience** : construction réelle des 4 programmes, vérification des frontières
  39/40 et 69/70 au simulateur, récupération du lien de partage et du **code
  d'intégration iframe** — l'emplacement est réservé dans la séquence, le repli
  hors-ligne est en place en attendant. Les planches de paliers sont des
  reconstitutions étiquetées de l'écran Vittascience : à remplacer par des captures
  du poste réel dès que les programmes existent (règles n°70/73/94) ;
- **accès réseau** : vérifier que `fr.vittascience.com` n'est pas filtré par le réseau
  du collège AVANT la séance 2 (sinon, le repli hors-ligne prend le relais) ;
- les deux captures ArduBlock du bonus sont, elles, **réelles** (poste du labo,
  20/08/2026, règle d'or n°94) ;
- `docker compose build && docker compose run --rm compile station_alerte_cyclonique`
  sur le poste enseignant ;
- relecture orthotypographique humaine ; rendu GitHub Pages après publication.

## 5. Échecs

Aucun test exécuté en échec au moment de la remise (74/74).
La suite complète a été rejouée intégralement, pas seulement les tests ajoutés.
