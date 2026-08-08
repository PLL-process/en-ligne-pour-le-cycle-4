# Rapport de tests — Lot 4e_C4.7 · C4.8 · C4.9 « SOS serre : l'objet connecté muet »

**Version 2** (refonte après audit pédagogique externe).
**Exécution réelle** le 08/08/2026, suite Playwright (Chromium headless) : **50/50 verts**.
Seuls des tests réellement exécutés sont déclarés ici (barre qualité du dépôt).
La v1 déclarait 36/36 le 07/08/2026 ; la suite a été étendue de 14 vérifications pour couvrir
les nouveautés de la v2 (4e séance, passeport, mode essentiel, fichiers .pkt, défi).

## Séquence (32 tests)

| Test | Vérifie | Résultat |
|---|---|---|
| SEQ-01 | chargement sans erreur JS | ✔ |
| SEQ-02 | titre conforme à la charte (`Thème 2 · Martinique — 4e · Atelier : …`) | ✔ |
| SEQ-03/04/05 | blocs règle n°4 : « 🧠 Prêt·e à t'entraîner ? », UN SEUL bouton QCM, « 🎁 Bonus » | ✔ |
| SEQ-06 | navigation règle n°11 (⌂ Accueil, lien relatif) | ✔ |
| SEQ-07 | les **14** figures SVG de la page se chargent (naturalWidth > 0) | ✔ |
| SEQ-07b | libellés intégraux du socle (D2/D4) présents | ✔ |
| SEQ-07c | CRCN 5.1 en toutes lettres + repère officiel verbatim | ✔ |
| SEQ-07e | CRCN **2.3 et 5.2** (compétences citées par le programme) présentes | ✔ |
| SEQ-07f | **domaine 1** du socle explicité dans la page | ✔ |
| SEQ-07g | durée annoncée « 4 séances de 55 min » | ✔ |
| SEQ-07d | les 3 libellés officiels 4e_C4.7/C4.8/C4.9 cités en entier | ✔ |
| SEQ-08/09 | bascule des onglets séance 2 et séance 3 | ✔ |
| SEQ-09b/09c | l'onglet **séance 4** s'active ; la page expose bien 4 onglets de séance | ✔ |
| SEQ-09d/09e | **mode essentiel** : le bouton masque puis réaffiche référentiel/corrections/approfondissements | ✔ |
| SEQ-09f | **passeport réseau** : le vérificateur refuse les réponses vides et oriente | ✔ |
| SEQ-10a | **règle n°22** : act. 1 refusée sans le plan d'adressage rédigé | ✔ |
| SEQ-10b | vérificateur act. 1 : 9/9 (4 étapes-recette de conception + 5 de lecture) + production | ✔ |
| SEQ-11 | **VERROU** : act. 4 refusée avec 5 bonnes réponses + diagnostic rédigé mais SANS les 2 consultations de la clinique | ✔ |
| SEQ-12 | **VERROU** : act. 4 validée après ping réussi + cas « mauvaise rue » réellement joués | ✔ |
| SEQ-13 | sauvegarde locale : champ restauré après rechargement (clé `seq_4e_C4.7-C4.9_sos_serre_pt`) | ✔ |
| SEQ-14 | rappel de l'hypothèse de départ au bilan | ✔ |
| SEQ-15 | trace `__exp` du verrou persistante après rechargement | ✔ |
| SEQ-16 | le bouton QCM pointe un fichier existant | ✔ |
| SEQ-17 | le lien de téléchargement du fichier fourni `4e_serre_TECHNO-C4.pkt` existe | ✔ |

## QCM (11 tests)

| Test | Vérifie | Résultat |
|---|---|---|
| QCM-01 | chargement sans erreur JS | ✔ |
| QCM-02 | 30 questions | ✔ |
| QCM-03 | bonnes réponses réparties **8/7/7/8** sur A/B/C/D (`fix_r.js`, graine 4789) | ✔ |
| QCM-04 | répartition par code : 4e_C4.7 = 10 · 4e_C4.8 = 10 · 4e_C4.9 = 10 | ✔ |
| QCM-05 | 7 questions illustrées (règle images v2) | ✔ |
| QCM-06 | chaque question : 4 options, réfutation de CHAQUE distracteur, expl + exemple + erreur classique + à retenir | ✔ |
| QCM-07/08 | validation d'une réponse → correction détaillée affichée + tableau de bord mis à jour | ✔ |
| QCM-09 | sauvegarde locale restaurée après rechargement (clé `qcm_4e_C4.7-C4.9_sos_serre_pt`) | ✔ |
| QCM-10 | navigation « ← Séquence » (règle n°11) | ✔ |
| QCM-11 | les 7 images des questions existent sur le disque | ✔ |

## Synthèses (4 tests)

Chargement sans erreur JS des deux synthèses ; les schémas embarqués (`<object>`) existent. ✔

## Fichiers Packet Tracer et séance 4 (tests ajoutés en v2)

| Test | Vérifie | Résultat |
|---|---|---|
| SEQ-17-* | les 4 nouveaux fichiers `.pkt` (DEPART, PANNE_A, PANNE_B, PANNE_C) sont présents dans le dossier | ✔ |
| SEQ-17b | **tous** les liens `.pkt` de la page pointent un fichier réellement présent | ✔ |
| SEQ-18 | le défi sans tutoriel expose bien `e5_defi` (choix du test) et `e5_preuve` (justification) | ✔ |

## Environnement et limites (honnêteté)

- Tests exécutés hors ligne : l'appel à la police Google Fonts échoue alors proprement
  (repli sur la police système) — non bloquant, identique aux autres lots du dépôt ;
  cet échec de ressource est journalisé mais non compté comme erreur.
- Non testé automatiquement : l'impression A4 (vérifiée visuellement), le rendu dans
  Packet Tracer lui-même. La suite vérifie la **présence** des cinq fichiers `.pkt` et la
  validité de leurs liens, pas leur contenu — celui-ci a été validé à la main, dans le
  logiciel, sur le poste enseignant.
- **Validation EN CONDITIONS RÉELLES dans Packet Tracer 8.2** (sessions des 06, 07 et
  08/08/2026, poste enseignant, pilotage à distance) :
  - `4e_serre_TECHNO-C4.pkt` — 5 équipements adressés (plan .10→.100, passerelle
    192.168.20.1), pings mesurés (`<1ms`→`12ms`, TTL=128, 0% loss) ;
  - `4e_serre_DEPART.pkt` — les 4 terminaux vidés un par un (IP, masque, passerelle),
    état vérifié fenêtre par fenêtre par capture avant l'enregistrement, câblage intact
    (liens verts) ;
  - `4e_serre_PANNE_A.pkt` — capteur en 192.168.21.50, `ping 192.168.20.50` → **100% loss
    vérifié** ;
  - `4e_serre_PANNE_B.pkt` — Port Status de l'imprimante sur Off, **triangle rouge observé** ;
  - `4e_serre_PANNE_C.pkt` — capteur au masque 255.255.255.240, `ping 192.168.20.50` →
    **100% loss vérifié**.
- **Ce qui n'a PAS pu être fait** (et qui est donc absent du lot) : la panne « doublon
  d'adresse IP ». L'interface de Packet Tracer 8.2 refuse la saisie d'une adresse déjà
  utilisée sur le réseau (« This address is already used in the network. ») et vide le
  champ ; le doublon est donc traité à l'oral et en bonus, pas en fichier. La panne
  « masque » l'a remplacée.
- Script de test : suite Playwright du lot (50 vérifications), rejouable.
