# Rapport de tests — Lot 5e_C4.7 · C4.8 « Le réseau de la salle techno »

**Exécution réelle** le 05/08/2026, suite Playwright (Chromium headless).
v1.0 (lot initial) : 30/30 verts · v1.1 (rétrofit règle n°22, étape de conception act. 2) : 31/31 verts ·
**v1.2 (rétrofit audit externe, 08/08/2026) : suite dédiée de 24 vérifications, 24/24 vertes** — elle
contrôle les apports du rétrofit : domaine 1 du socle explicité, CRCN 2.3 présent, encadré « premier ping :
ne panique pas » visible en séance 3, valeurs annoncées comme réellement observées, variante 🅰 sur réseau
ISOLÉ, repère CRCN 5.1 verbatim conservé, bouton mode essentiel qui masque puis réaffiche le référentiel et
persiste après rechargement, billet d'entrée qui refuse le vide / oriente à 2 sur 3 / valide à 3 sur 3,
capsule de rattrapage présente, indicateur « prochaine étape ».
La v1.1 disait :
la suite vérifie désormais aussi le REFUS sans description de conception (SEQ-10a) et la validation 11/11
avec conception (SEQ-10b) · **v1.2 (finitions : recette illustrée en 4 vignettes, correctif de chevauchement
du schéma du facteur, socle et CRCN en toutes lettres) : 33/33 verts** — dont la présence des 8 figures,
des libellés intégraux du socle (D2/D4) et du repère CRCN verbatim (SEQ-07/07b/07c).
Seuls des tests réellement exécutés sont déclarés ici (barre qualité du dépôt).

## Séquence (16 tests)

| Test | Vérifie | Résultat |
|---|---|---|
| SEQ-01 | chargement sans erreur JS | ✔ |
| SEQ-02 | titre conforme à la charte (`Thème 2 · Martinique — 5e · Atelier : …`) | ✔ |
| SEQ-03/04/05 | blocs règle n°4 : « 🧠 Prêt·e à t'entraîner ? », UN SEUL bouton QCM, « 🎁 Bonus » | ✔ |
| SEQ-06 | navigation règle n°11 (⌂ Accueil, lien relatif) | ✔ |
| SEQ-07 | les 6 figures SVG de la page se chargent (naturalWidth > 0) | ✔ |
| SEQ-08/09 | bascule des onglets séance 2 et séance 3 | ✔ |
| SEQ-10a | **règle n°22** : act. 2 refusée sans la description de SA conception | ✔ |
| SEQ-10b | vérificateur act. 2 : 11/11 (4 questions-recette de conception + 7 de lecture) | ✔ |
| SEQ-11 | **VERROU** : act. 5 refusée avec 5 bonnes réponses mais SANS les 2 expériences du mini-simulateur | ✔ |
| SEQ-12 | **VERROU** : act. 5 validée après livraison normale + livraison en doublon réellement jouées | ✔ |
| SEQ-13 | sauvegarde locale : champ restauré après rechargement (clé `seq_5e_C4.7-C4.8_reseau_pt`) | ✔ |
| SEQ-14 | rappel de l'hypothèse de départ au bilan | ✔ |
| SEQ-15 | trace `__exp` du verrou persistante après rechargement | ✔ |
| SEQ-16 | le bouton QCM pointe un fichier existant | ✔ |

## QCM (11 tests)

| Test | Vérifie | Résultat |
|---|---|---|
| QCM-01 | chargement sans erreur JS | ✔ |
| QCM-02 | 30 questions | ✔ |
| QCM-03 | bonnes réponses réparties **8/7/7/8** sur A/B/C/D (`fix_r.js`, graine 5478) | ✔ |
| QCM-04 | répartition par code : 5e_C4.7 = 16 · 5e_C4.8 = 14 | ✔ |
| QCM-05 | 6 questions illustrées (règle images v2) | ✔ |
| QCM-06 | chaque question : 4 options, réfutation de CHAQUE distracteur, expl + exemple + erreur classique + à retenir | ✔ |
| QCM-07/08 | validation d'une réponse → correction détaillée affichée + tableau de bord mis à jour | ✔ |
| QCM-09 | sauvegarde locale restaurée après rechargement (clé `qcm_5e_C4.7-C4.8_reseau_pt`) | ✔ |
| QCM-10 | navigation « ← Séquence » (règle n°11) | ✔ |
| QCM-11 | les 6 images des questions existent sur le disque | ✔ |

## Synthèses (3 tests)

Chargement sans erreur JS des deux synthèses ; le schéma embarqué (`<object>`) existe. ✔

## Environnement et limites (honnêteté)

- Tests exécutés hors ligne : l'appel à la police Google Fonts échoue alors proprement
  (repli sur la police système) — non bloquant, identique aux autres lots du dépôt ;
  cet échec de ressource est journalisé mais non compté comme erreur.
- Non testé automatiquement : l'impression A4 (vérifiée visuellement), le rendu dans
  Packet Tracer lui-même (le fichier `5e_reseau_local_TECHNO-C4.pkt` a été construit et
  validé EN CONDITIONS RÉELLES dans Packet Tracer 8.2 : câblages verts, SSID TECHNO-C4,
  5 terminaux adressés, ping filaire < 1 ms et WiFi 57-260 ms « Reply from » 4/4,
  enveloppe PDU suivie en mode Simulation — session de pilotage du 05/08/2026 sur le
  poste enseignant).
- Script de test : suite Playwright du lot (30 vérifications v1) + suite dédiée du rétrofit audit
  (24 vérifications v1.2), toutes deux rejouables.
- Le rétrofit v1.2 ne touche NI le fichier `.pkt`, NI les figures, NI le QCM : ce sont des ajouts de
  texte, un bouton et un billet d'entrée. Les preuves de la v1.0 restent valables telles quelles.
