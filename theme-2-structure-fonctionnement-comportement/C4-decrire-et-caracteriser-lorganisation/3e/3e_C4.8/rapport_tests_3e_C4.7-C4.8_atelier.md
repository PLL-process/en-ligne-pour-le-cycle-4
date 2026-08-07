# Rapport de tests — Lot 3e_C4.7 · C4.8 « Le pont numérique Martinique → New York »

**Exécution réelle** le 07/08/2026, suite Playwright (Chromium headless) : **37/37 verts**.
Seuls des tests réellement exécutés sont déclarés ici (barre qualité du dépôt).

## Séquence (23 tests)

| Test | Vérifie | Résultat |
|---|---|---|
| SEQ-01 | chargement sans erreur JS | ✔ |
| SEQ-02 | titre conforme à la charte (`Thème 2 · Martinique — 3e · Atelier : …`) | ✔ |
| SEQ-03/04/05 | blocs règle n°4 : « 🧠 Prêt·e à t'entraîner ? », UN SEUL bouton QCM, « 🎁 Bonus » | ✔ |
| SEQ-06 | navigation règle n°11 (⌂ Accueil, lien relatif) | ✔ |
| SEQ-07 | les 7 figures SVG de la page se chargent (naturalWidth > 0) | ✔ |
| SEQ-07b | libellés intégraux du socle (D2/D4) présents | ✔ |
| SEQ-07c | CRCN 5.1 en toutes lettres + repère officiel verbatim | ✔ |
| SEQ-07d | les 2 libellés officiels 3e_C4.7/C4.8 cités en entier (dont « activité débranchée, table de routage donnée ») | ✔ |
| SEQ-08/09 | bascule des onglets séance 2 et séance 3 | ✔ |
| SEQ-10a | **règle n°22** : act. 1 refusée sans le schéma de concepteur rédigé | ✔ |
| SEQ-10b | vérificateur act. 1 : 7/7 (4 étapes-recette de conception + 3 de lecture) + production | ✔ |
| SEQ-10c | act. 2 refusée avec 5 bonnes réponses mais SANS la justification rédigée du protocole | ✔ |
| SEQ-10d | act. 2 validée avec la justification (l'argument « à la main vs échelle d'Internet ») | ✔ |
| SEQ-11 | **VERROU** : act. 5 refusée avec 4 bonnes réponses mais SANS les 2 expériences du poste-frontière | ✔ |
| SEQ-12 | **VERROU** : act. 5 validée après le voyage complet (Successful) ET le voyage sans route (détruit à R-MQ) réellement joués | ✔ |
| SEQ-13 | sauvegarde locale : champ restauré après rechargement (clé `seq_3e_C4.7-C4.8_pont_numerique_pt`) | ✔ |
| SEQ-14 | rappel de l'hypothèse de départ au bilan | ✔ |
| SEQ-15 | trace `__exp` du verrou persistante après rechargement | ✔ |
| SEQ-16 | le bouton QCM pointe un fichier existant | ✔ |
| SEQ-17 | le fichier maître `3e_routage_MQ_NY_TECHNO-C4.pkt` existe dans le lot | ✔ |

## QCM (11 tests)

| Test | Vérifie | Résultat |
|---|---|---|
| QCM-01 | chargement sans erreur JS | ✔ |
| QCM-02 | 30 questions | ✔ |
| QCM-03 | bonnes réponses réparties **8/7/7/8** sur A/B/C/D (`fix_r.js`, graine 3987) | ✔ |
| QCM-04 | répartition par code : 3e_C4.7 = 12 · 3e_C4.8 = 18 | ✔ |
| QCM-05 | 6 questions illustrées (règle images v2) | ✔ |
| QCM-06 | chaque question : 4 options, réfutation de CHAQUE distracteur, expl + exemple + erreur classique + à retenir | ✔ |
| QCM-07/08 | validation d'une réponse → correction détaillée affichée + tableau de bord mis à jour | ✔ |
| QCM-09 | sauvegarde locale restaurée après rechargement (clé `qcm_3e_C4.7-C4.8_pont_numerique_pt`) | ✔ |
| QCM-10 | navigation « ← Séquence » (règle n°11) | ✔ |
| QCM-11 | les 6 images des questions existent sur le disque | ✔ |

## Synthèses (3 tests)

Chargement sans erreur JS des deux synthèses ; le schéma embarqué (`<object>`) existe. ✔

## Environnement et limites (honnêteté)

- Tests exécutés hors ligne : l'appel à la police Google Fonts échoue alors proprement
  (repli sur la police système) — non bloquant, identique aux autres lots du dépôt ;
  cet échec de ressource est journalisé mais non compté comme erreur.
- Non testé automatiquement : l'impression A4 (vérifiée visuellement), le rendu dans
  Packet Tracer lui-même. Le fichier `3e_routage_MQ_NY_TECHNO-C4.pkt` a été construit
  et validé EN CONDITIONS RÉELLES dans Packet Tracer 8.2 (session du 07/08/2026 sur le
  poste enseignant, pilotage à distance) : deux réseaux complets (192.168.10 / 192.168.30),
  deux routeurs 1941 reliés en câble croisé sur la rue-pont 10.0.0.0/30, 2×2 interfaces
  configurées (Port Status On), routes statiques miroir écrites (`192.168.30.0/24 via
  10.0.0.2` et retour), preuves mesurées : ping (2 `Request timed out` puis `Reply…
  TTL=126`), second ping 4/4 (0% loss, 0-4 ms), tracert 3 sauts (`192.168.10.1 →
  10.0.0.2 → 192.168.30.10`, `Trace complete`), Event List 0.000 → 0.010 s, verdict
  Successful.
- Script de test : suite Playwright du lot (37 vérifications), rejouable.
