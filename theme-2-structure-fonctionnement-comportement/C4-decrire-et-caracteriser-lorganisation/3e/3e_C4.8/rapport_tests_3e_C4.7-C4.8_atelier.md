# Rapport de tests — Lot 3e_C4.7 · C4.8 « Le pont numérique Martinique → New York »

**Exécution réelle** le 07/08/2026, suite Playwright (Chromium headless) : **37/37 verts**.
**Rétrofit audit externe du 08/08/2026** : suite dédiée de **25 vérifications, 25/25 vertes** — domaine 1 du
socle explicité, CRCN 2.3 présent, repère CRCN 5.1 verbatim et niveau 3 maintenus, variante 🅰 sur réseau
ISOLÉ, mode essentiel qui masque puis réaffiche le référentiel et persiste après rechargement, billet
d'entrée qui refuse le vide / oriente à 2 sur 3 / valide à 3 sur 3, capsule de révision de 4e, indicateur
« prochaine étape ». Le rétrofit ne touche NI le fichier `.pkt`, NI les figures, NI le QCM : les preuves de
la v1 restent valables telles quelles.
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

## 22/11/2026 — Trois explications écrites après l'activité 5 (règle d'or n°346)

La séance 3 finissait sans aucune réponse écrite (0 zone de texte, 9 groupes de boutons radio). Après l'activité 5, une
carte « ✍️ Explique comme au brevet — sans propositions » (~10 min, faisable à la maison sans matériel) : une
transcription imaginée (un ping puis un tracert depuis le CDI vers le serveur de la médiathèque, TTL=125, quatre sauts),
trois questions — le nombre de routeurs justifié par le TTL et vérifié par le tracert ; le « Request timed out » du
premier ping, qui n'est pas une panne ; le tracert d'un routeur en panne et ce qu'il localise —, une version étayée par
question, deux aides repliées (un indice, puis la démarche, n°367), une correction repliée avec trois phrases de copie
(n°356), une grille à trois critères. Rien n'est noté (n°340) ; la carte est hors de la zone de vérification de
l'activité 5. Les sigles du bloc sont écrits en clair (TTL, CDI ; n°44, consigne de Pascal du 22/11/2026).

| Contrôle | Sortie | Résultat |
|---|---|---|
| `_outils/tests_ecrit_brevet.py` (banc commun des écrits, nouveau) | 0 | 11 / 11 |
| `tests_regle_311_3e_C4.8.mjs` | 0 | 34 / 34 |
| `mode_mission/banc_generique.mjs` | 0 | aucun refus |
| `controle_page_ouverte.mjs`, `controle_impression.mjs`, `controle_hors_ligne.mjs`, `controle_squelette.mjs` | 0 | rien à signaler |
| `controle_regles_visibles`, `controle_hierarchie`, `controle_consignes_a_la_ligne`, `controle_propositions_indices`, `controle_tactile`, `controle_validations`, `eleve_qui_ne_lit_pas.py` | 0 | rien à signaler |

Revue d'écran à 390 px : deux tours ; au premier, les lignes de la transcription se coupaient (« TTL=125 » seul sur sa
ligne, « Request timed / out ») : lignes raccourcies, plus aucune ligne coupée.

**Non vérifié** : la durée réelle (~10 min annoncées) ; un essai en classe.

