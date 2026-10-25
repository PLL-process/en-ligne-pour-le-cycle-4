# Rapport de tests — Lot 3e_C9.2 + 3e_C8.3 « La station d'alerte cyclonique se programme »

Date : 2026-10-25 (**séances de 55 min** ; refonte v3 : 2026-08-26 ; v2 : 2026-08-21 ; 1re livraison : 2026-08-19) ·
Agent : Fable · Environnement : Chromium headless (Playwright 1.55),
viewport 1280×900 + émulation téléphone 390×844 · Suite : `tests_3e_C9.2-C8.3.mjs`
(committée dans ce dossier, rejouable : `node tests_3e_C9.2-C8.3.mjs .`).

La suite **simule la séquence comme un élève** (méthode du « dé de 5e ») et prend
une **capture d'écran à chaque action** (35 captures : accueil, billet, chaque
activité validée, chaque état du banc — les quatre niveaux, les six frontières,
l'acquittement, le ré-armement, le chrono —, bilan, persistance croisée entre
pages, mode essentiel, loupe, QCM et ses scénarios, mobile). Les captures sont
livrées à part (non committées).

## 0. Redécoupage en huit séances de 55 min (24-25/10/2026) — 156/156 réussis

Décision de Pascal : une heure par semaine et par classe. Les quatre séances de
1 h 30 deviennent **huit séances de 55 min**, sans rien retirer : une activité par
séance (30 à 40 min annoncées), l'activité 3 (~70 min) coupée en deux parties
nommées entre le palier 2 et le palier 3 (« première partie » en séance 3, « suite »
en séance 4, avec une phrase de reprise). Les quatre pages découpées gardent leurs
noms de fichier et portent chacune deux séances (1-2, 3-4, 5-6, 7-8) ; elles sont
régénérées par `generer_les_quatre_pages.py`, réparé au passage (il ne tournait
plus sur la source depuis le passage du Bonus avant le bilan).

Suite rejouée en entier : **135/135 avant** le redécoupage, **156/156 après**. Les
tests qui ouvraient les onglets s2 à s4 ouvrent désormais s2 à s8 ; 21 tests
ajoutés :

| Test ajouté | Résultat |
|---|---|
| Activité 3 en deux parties nommées (première partie / suite), 35 + 35 min, panneaux s3 et s4 | ✅ |
| La coupe tombe entre le palier 2 et le palier 3 | ✅ |
| La suite s'ouvre sur une phrase de reprise, sans « tu as fait » (n°304) | ✅ |
| Règle n°101 : 7 boutons « séance suivante » (test existant, 3 → 7), chacun vers la séance suivante, aucun en séance 8 (ajouté) | ✅ |
| Passage séance 3 → séance 4 (de la première partie à la suite) | ✅ |
| Bandeau « 8 séances de 55 min », plus aucune trace de « 1 h 30 » ni « 90 min » | ✅ |
| 8 onglets, 8 panneaux · tableau de bord qui suit la séance ouverte | ✅ (2 tests) |
| Une sauvegarde écrite avec l'ancien découpage se relit sans erreur JS (réponses, progression 6/7, coches réparties sur les 8 séances) | ✅ (2 tests) |
| Chaque page découpée annonce ses deux séances (« 2 séances de 55 min »), les ancre sous leur en-tête, et la première mène à la seconde par un lien interne | ✅ (8 tests) |
| Page 2 : le lien « Séance 4 » amène l'en-tête de la séance 4 en haut de l'écran | ✅ |
| Mobile 390 px : les 8 séances s'ouvrent par leur onglet sans débord ; de la séance 1 à la 8 par les boutons | ✅ (2 tests) |

**Correction des seuils et broches d'avant (25/10/2026) — 164/164.** L'expérience ② de
l'activité 4 (« sous 100, puis au-dessus de 150 ») ne faisait jamais repartir le
buzzer, qui ne sonne qu'en ouragan majeur : elle dit désormais « redescends sous 178
(à 177), puis remonte à 178 ou plus ». Corrigés aussi : le critère de l'activité 2
(178 avant 118 avant 63), l'aide 2, les erreurs fréquentes et l'alt de l'activité 4
(buzzer au niveau 3), la planche `blocs_palier4_acquitter.svg` (« niveauAlerte = 3 »),
le corrigé du défi « anémomètre réel » (63, 118, 178), la fiche 🅰 de l'activité 3
(un seul montage, celui du programme de référence ; légende sous le schéma qui ne
dessine qu'un voyant), et deux renvois de la synthèse professeur (essai 13, 13
verdicts). 8 tests ajoutés : l'expérience ② rejouée telle qu'écrite (177 puis 178),
sa consigne, et un garde-fou qui refuse le retour des anciens seuils et broches
dans les cinq fichiers et dans la planche du palier 4.

**Schéma de câblage redessiné et QCM vérifié (25/10/2026) — 167/167.**
`Images/montage_station_grove.svg` ne montrait qu'une DEL « rouge » sur D3 : il est
redessiné d'après le programme de référence (A1, D2, I2C, D5, voyants D6 · D7 · D3 · D4),
en portrait pour le téléphone. Au QCM, cinq passages corrigés (question 2 « DEL sur D3 »,
alt de la question illustrée, question 10 « (niveau = 2) », exemple de la question 11
« vigilance → alerte », réfutation de la question 13 « DEL commandée par D3 ») et la
hauteur des figures plafonnée ; synthèse élève : buzzer au niveau 3. 3 tests ajoutés
(les huit branchements du schéma, plus de DEL unique, garde-fou sur les 30 questions).
`verif_qcm_coherence` : 30 q, 8/7/7/8, réfutations alignées · `controle_medias` vert.

Contrôles du dépôt après redécoupage : `controle_squelette` 0 refus (D1 à D6 : 0),
`controle_navigation_seances`, `controle_hierarchie`, `controle_regles_visibles`,
`controle_liens` (aucun lien mort), `controle_atteignabilite` (406/406),
`controle_debordement`, `controle_blocs_dessines`, `controle_impression` : verts.
`mesurer_temps_seances.py` : tout-en-un 8 × 55 = 440 min pour 285 min d'activités
(+155) ; chaque page découpée 2 × 55 = 110 min (+45, +40, +35, +35).
`verif_regles_audit.py` : 14 ✘ avant, 14 ✘ après, identiques ligne à ligne (n°298,
n°300, n°301 des pages 1 à 3 sans clôture, n°304, n°34 — tous antérieurs).
Playwright à 390 px sur les cinq fichiers : zéro erreur JS, débord 0, chaque séance
atteinte, passage d'une séance à la suivante, reprise après rechargement.

## 1. Tests automatisés exécutés — 113/113 réussis (refonte v3, 26/08/2026)

### Ce que la refonte v3 a ajouté à la suite (39 tests)

**L'échelle unique et les quatre niveaux (11 tests)**

| Test | Résultat |
|---|---|
| Act. 2 validée à **14/14** : trois seuils saisis (178, 118, 63) + le cas « sinon » + les 6 questions de lecture fine | ✅ |
| Banc : **VEILLE** à 40 km/h — vert seul, les trois autres voyants éteints | ✅ |
| Banc : **TEMPÊTE TROPICALE** à 90 — jaune seul, buzzer muet | ✅ |
| Banc : **OURAGAN** à 150 — orange seul, buzzer muet | ✅ |
| Banc : **OURAGAN MAJEUR** à 200 — rouge seul **+ buzzer** | ✅ |
| Invariant « un seul voyant à la fois » vérifié aux quatre paliers (vecteur des 4 DEL comparé à `[1,0,0,0]`, `[0,1,0,0]`, `[0,0,1,0]`, `[0,0,0,1]`) | ✅ |
| **Règle n°119** : le niveau est écrit **en toutes lettres** aux quatre paliers — jamais seulement une couleur | ✅ |
| Séance 2 : **une seule échelle**, affirmée dans la page ET vérifiée par l'absence de tout reste de la maquette 0-100 (`seuil_vigilance` introuvable) | ✅ |
| Séance 2 : les trois seuils Saffir-Simpson présents dans les paliers | ✅ |

**Les six frontières, une par une (6 tests)** — c'est le cœur de C8.3 :

| Frontière | Attendu | Résultat |
|---|---|---|
| 62 km/h | écran vert (veille) | ✅ |
| 63 km/h | écran jaune (tempête tropicale) | ✅ |
| 117 km/h | écran jaune | ✅ |
| 118 km/h | écran orange (ouragan) | ✅ |
| 177 km/h | écran orange | ✅ |
| 178 km/h | écran rouge (ouragan majeur) | ✅ |

**Les captures réelles Vittascience (16 tests)**

| Test | Résultat |
|---|---|
| Les **13 captures** sont référencées et chargées (7 de structure + 6 de frontières) | ✅ (13 tests) |
| **Règle n°117** : chaque capture porte un `alt` d'au moins 120 caractères | ✅ |
| La réserve est écrite noir sur blanc : le simulateur **dessine tous les voyants en vert** | ✅ |
| L'écart des **300 ms** du programme réel est expliqué dans la page, pas masqué | ✅ |

**Le découpage en quatre pages, règle d'or n°116 (14 tests)**

| Test | Résultat |
|---|---|
| **Aucune question perdue** : l'union des champs interactifs des 4 pages recouvre exactement les **76 champs** de la page tout-en-un | ✅ |
| Zéro erreur JS au chargement des quatre pages | ✅ |
| Chaque page ramène au tout-en-un, et porte les 4 onglets-liens | ✅ (8 tests) |
| **Persistance croisée** : une réponse écrite page 1, puis une autre page 4 — la page 1 relue ensuite a **conservé** la sienne | ✅ |
| Le rappel d'hypothèse écrit page 1 **remonte** jusqu'au bilan de la page 4 | ✅ |
| Le tout-en-un relit les réponses des **deux** pages | ✅ |
| Le tout-en-un propose les 4 pages (4 liens) | ✅ |

> Ce dernier groupe est celui qui compte le plus : le découpage introduit un risque
> réel de **perte de données**, une page pouvant écraser les réponses des autres en
> réécrivant la clé partagée. Le test a été écrit **avant** la livraison, et il a
> effectivement attrapé le défaut : la fonction de collecte ne fusionnait pas avec
> l'état déjà enregistré. Corrigé, puis re-vérifié dans les deux sens.

### Séquence — tests de fond, tous rejoués

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS (début et fin de parcours) | ✅ |
| Billet d'entrée sans note : feedback affiché, hors progression | ✅ |
| Activité 1 : 9/9 + justification exigée | ✅ |
| **Verrou expérientiel** : l'activité 3 est REFUSÉE tant que le banc n'a pas été manipulé (message explicite) | ✅ |
| Activité 3 validée après manipulations (verrous lecture + les 4 niveaux) | ✅ |
| Acquittement : buzzer muet, écran TOUJOURS rouge, voyant rouge TOUJOURS allumé | ✅ |
| Ré-armement : redescente à 50 puis remontée à 210 → le buzzer REPART sans appui | ✅ |
| Activités 4 et 5 validées (expériences tracées exigées pour la 4) | ✅ |
| Activité 6 : protocole rédigé exigé — 4 familles, dont **au moins 4 des 6 frontières** citées, + règle de décision | ✅ |
| Activité 7 : exécution réelle exigée — **6 frontières** + chrono tracés, **13 verdicts**, 6 attendus justes, PV | ✅ |
| Chrono de performance : franchissement de **178** mesuré, verdict CONFORME (< 1 s) | ✅ |
| Progression 7/7, coches ✔ des séances (8 depuis le 25/10/2026), rappel d'hypothèse au bilan | ✅ |
| **Sauvegarde/restauration** après rechargement : progression, réponses, verrous du banc | ✅ |
| Encadré jumelage : présent, replié par défaut (encadré interne compris), 5 ouragans cités (1938, Irene, Sandy, Henri, Ida), 2 tableaux, hors parcours obligatoire, limite du prototype nommée | ✅ (10 tests) |
| Règle n°4 : un SEUL bouton QCM · Règle n°86 : 3 défis bonus, 3 corrigés repliés | ✅ |
| Règle n°29 : mode essentiel masque référentiel + corrections | ✅ |
| Règle n°92 : loupe (clic → grand format, Échap → fermeture) | ✅ |
| Mobile 390 px : aucun défilement horizontal (débord = 0), zéro erreur JS | ✅ |
| Zéro lien local cassé (parcours `href/src/data` des **8 HTML** du lot) | ✅ |

### QCM (`qcm_3e_C9.2-C8.3_station_alerte_cyclonique.html`)

| Test | Résultat |
|---|---|
| 30 questions · 15 C9.2 / 15 C8.3 · 4 illustrées · grille complète | ✅ |
| Bonnes réponses réparties A/B/C/D = 8/7/7/8 ; `d[r]` vide et 3 réfutations non vides sur CHAQUE question (assertion sur les 30) | ✅ |
| Réponse correcte : correction complète (bonne réponse, explication, exemple, erreur fréquente, réfutation des distracteurs, à retenir) | ✅ |
| Question illustrée : le document s'affiche avec son alt | ✅ |
| Réponse fausse comptée · marquage 🔖 · modes 10 questions / ciblée C8.3 (15) / mes erreurs (1) | ✅ |
| Minuteur : démarrage auto à la 1re validation, pause qui fige | ✅ |
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

- **Syntaxe JavaScript** : `new Function()` sur chaque bloc `<script>` de la
  séquence, des quatre pages et du QCM → OK.
- **Poids des médias** : 10 SVG originaux de 3,7 à 10,4 Ko + 15 captures PNG
  réelles (2 ArduBlock de 223 et 328 Ko ; 13 Vittascience de 34 à 129 Ko, soit
  924 Ko au total pour le dossier `Images/vittascience/`). Les captures doivent
  rester lisibles : leur poids est assumé et déclaré ;
  `<title>/<desc>` accessibles dans chaque SVG.
- **Matrice de couverture** : les 30 questions rattachées à une notion enseignée ;
  aucune notion essentielle sans question ; aucune question hors séquence.
- **Aucun envoi réseau** : sauvegardes localStorage uniquement
  (`seq_3eC92-3eC83_station-alerte` / `qcm_3eC92-3eC83_station-alerte`), pages
  autonomes hors ligne. Seul l'`iframe` Vittascience sort, et son absence est
  prévue (repli déplié).

## 3. Programme de référence — ce qui a été vérifié, et ce qui ne l'a pas été

- **Vérification syntaxique C++ complète, faite dans cette session** :
  `station_alerte_cyclonique.ino` compilé avec `g++ -std=c++17 -fsyntax-only
  -Wall -Wextra` sur des bouchons Arduino (`pinMode`, `digitalWrite`, `map`,
  `millis`, LCD Grove) → **zéro erreur, zéro avertissement**. Cela prouve la
  syntaxe et la cohérence des types, **pas** la taille en mémoire AVR.
- **Compilation AVR : NON refaite dans cette session.** Le chiffre du 19/08/2026
  (`text 6764 · data 176 · bss 393` pour `arduino:avr:uno`) porte sur la version
  **v2** du programme. La v3 a renommé les seuils (`SEUIL_JAUNE / SEUIL_ORANGE /
  SEUIL_ROUGE`, pour coller aux blocs réels) et **ajouté la pulsation** des
  voyants : le binaire a donc changé. `arduino-cli` n'est pas atteignable depuis
  l'environnement de production de ce lot (téléchargement refusé) ; la
  recompilation reste **à faire sur le poste enseignant** avec le banc Docker
  fourni. C'est consigné ici plutôt que déclaré fait.

## 4. Contrôles restant manuels (non exécutés — à faire par un humain)

- `docker compose build && docker compose run --rm compile station_alerte_cyclonique`
  sur le poste enseignant, pour re-prouver la compilation AVR de la v3 ;
- test sur appareils réels (iOS/Android, tablette) — seul le viewport a été émulé ;
- **version 🅰 au labo** : le montage Grove complet (A1 potentiomètre, D2 bouton,
  D3 orange, D4 rouge, D5 buzzer, D6 vert, D7 jaune, LCD I2C) et le téléversement
  depuis Vittascience ;
- **accès réseau** : vérifier que `fr.vittascience.com` n'est pas filtré par le
  réseau du collège AVANT la séance 3 (sinon, le repli hors-ligne prend le relais) ;
- le **formulaire `/learn/form`** de Vittascience (déclaration publique de la
  ressource) : contenu rédigé et prêt, **non soumis** ;
- relecture orthotypographique humaine ; rendu GitHub Pages après publication.

## 5. Échecs

Aucun test exécuté en échec au moment de la remise (113/113). La suite complète a
été rejouée intégralement, pas seulement les tests ajoutés.

**Deux défauts ont été trouvés et corrigés pendant cette campagne**, tous deux par
des tests écrits avant la livraison :

1. **Le chrono de performance ne franchissait plus aucun seuil.** Il passait de
   140 à 160 km/h — deux valeurs qui, sur la nouvelle échelle, appartiennent au
   MÊME niveau (ouragan). La mesure ne se déclenchait donc jamais et restait
   bloquée sur « mesure en cours ». Corrigé : 170 → 185, de part et d'autre de 178.
   *Un changement de seuils avait rendu muet un dispositif qui, lui, n'avait pas
   changé d'une ligne.*
2. **La trace d'exécution de l'activité 5 était incohérente** avec sa propre
   question : la question parlait de 71 et 95 km/h, la trace affichait 97, 103,
   126, 161, et le niveau annoncé ne correspondait à aucun seuil de la v3.
   Réécrite pour porter un diagnostic exact et vérifiable (58 → 186, niveau bloqué
   à 0 sur toute la plage 63-117, niveaux 2 et 3 corrects), ce qui isole le défaut
   sur le seul test « ≥ 63 ».
