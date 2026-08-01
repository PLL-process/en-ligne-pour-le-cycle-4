# 📖 JOURNAL DES DÉCISIONS

## 🗂 Registre central des règles d'or (règle n°10 — à consulter AVANT toute numérotation)
| N° | Titre | Rédacteur | Statut |
|----|-------|-----------|--------|
| 1 | Images v2 — SVG originaux CC0, jamais décoratives | Fondatrices (Pascal + Fable) | ✅ En vigueur |
| 2 | En-tête QCM standard (gabarit LOT 01) | Fondatrices | ✅ En vigueur |
| 3 | Versions 🅰 réel / 🅱 simulation / 🅲 sans matériel | Fondatrices | ✅ En vigueur |
| 4 | Blocs élève obligatoires (mission, 🧠 entraînement, 🎁 bonus) | Fondatrices | ✅ En vigueur |
| 5 | Gouvernance des livraisons (lot indivisible, tests réels) | Fondatrices | ✅ En vigueur — amendée le 30/07/2026 : autonomie de poussée pour Fable (voir entrée du jour) |
| 6 | Convention des chaînes : information en haut, énergie en bas | Fondatrices | ✅ En vigueur |
| 7 | CRCN observable, tracé, justifié | Fable (Thème 2) | ✅ Fusionnée (PR #71) |
| 8 | Représentations technologiques utiles, progressives, traçables | Fable (Thème 2) | ✅ Fusionnée (PR #71) |
| 9 | Représentations — formalisation détaillée (cadre d'application) | Codex (Thème 1) | ✅ Fusionnée (PR #74) |
| 10 | Le journal fait foi (la présente règle) | Fable, sur décision de Pascal | ✅ Fusionnée (PR #72) |
| 11 | Navigation persistante et retour à l'accueil | ChatGPT (`docs/specifications/regle-or-11-navigation-retour-accueil.md`) | ✅ Fusionnée (PR #76) — appliquée au Thème 2 par le lot d'harmonisation |
| 12 | Cycle de vie des ressources héritées (badge 🛠, archivage à la livraison) | Fable, validée par Pascal (30/07/2026) | ✅ Fusionnée (PR #86) |
| 13 | Code coloré façon IDE — palette commune des listings Python | Fable, sur demande de Pascal (30/07/2026) | ✅ Fusionnée (PR #101) |
| 14 | Aucun exercice muet (retour immédiat gradué : encoches, messages, verrous) | Fable, sur audit de Pascal (30/07/2026) | 🔄 PR en cours (branche `fable/theme-2/regles-14-17`) |
| 15 | Zéro papier obligatoire (toute production a son champ sauvegardé, Bonus compris) | Fable, sur audit de Pascal (30/07/2026) | 🔄 PR en cours (idem) |
| 16 | Blocs ↔ Python dans la page (éditeur embarqué, gabarit canonique `_outils/gabarits/`) | Fable, sur décision de Pascal (30/07/2026) | 🔄 PR en cours (idem) |
| 17 | 55 minutes pleines (densité vérifiée par séance, geste de code par séance de programmation) | Fable, sur audit de Pascal (30/07/2026) | 🔄 PR en cours (idem) |
| 18 | « Faire pour comprendre, comprendre pour faire » — répétition des représentations schématiques et du code par blocs, va-et-vient action ↔ conceptualisation | Pascal (credo fondateur, 01/08/2026), rédaction Fable | 🔄 PR en cours (branche `fable/infra/regle-18-faire-comprendre`) |

Règle de réservation : tout nouveau numéro se prend ICI, dans ce tableau, par une PR dédiée ou en tête du lot qui l'introduit — jamais dans son coin.

*À relire au début de chaque session de travail. Une entrée par décision
structurante. Les décisions « pédagogiques ou matérielles » restent à Pascal ;
les décisions de publication restent à ChatGPT.*

## 2026-07-21 — Lot 0 : audit initial (Claude, branche `audit/couverture-initiale-2026-07`)

1. **Référentiel opérationnel** : `_outils/data_competences.py` (114 codes
   vérifiés : 38 × 3 niveaux) est la transcription opérationnelle retenue,
   fondée sur la proposition Nathan correspondant au référentiel 2024.
   **CONFIRMÉ par la gouvernance le 21/07/2026** (le classeur Excel n'est pas
   versionné ; `data_competences.py` fait foi). La convention d'identifiants
   préfixés (`5e_C1.1`, `4e_C4.4`…) est la convention interne officielle du
   dépôt et est conservée.
2. **Générateur d'audit** : la matrice de couverture est produite par un script
   régénérable (`_outils/build_audit.py`) plutôt qu'à la main, pour rester
   synchronisable après chaque lot. Le script n'importe pas `make_index`
   (son import régénère l'index par effet de bord).
3. **Statuts** : `4e_C6.2` est le seul code `COMPLET ET VALIDABLE` (séquence
   modèle). Un QCM isolé = `PARTIEL`, jamais « séquence ».
4. **Mutualisations reconnues** : 5e_C1.4 → 5e_C1.3 (pointeur existant).
   Croisements déclarés mais sans pointeur (5e_C1.5/C1.6 → 4e_C1.4) : à
   matérialiser par des README dans un prochain lot.
5. **Progression 3e** : proposition de 5 séquences-projets (P1 station d'alerte
   cyclonique, P2 programmation, P3 réseaux/Internet, P4 réparation, P5 abri de
   cour) + fil rouge argumentaires — couvrant les 38 codes de 3e. **À VALIDER PAR PASCAL**
6. **Premier lot proposé** : 3e_C4.3, 3e_C4.4, 3e_C4.5+3e_C4.6 (mutualisés) +
   corrections des liens cassés 3e_C9.1 / 5e_C1.1 / 4e_C1.4. **À VALIDER**
7. **Aucune modification de ressource existante** dans ce lot 0 : uniquement des
   fichiers nouveaux (audit, feuille de route, inventaires, skills). Les `.pyc`
   versionnés et le `.gitignore` seront traités dans un lot ultérieur par
   ChatGPT (décision de dépôt, pas de contenu).
8. **Aucun téléchargement / aucune installation** effectués ; aucune skill
   externe ajoutée (skills locales uniquement — voir `SKILLS_AUDIT.md`).

### Arbitrages (état au 21/07/2026, mis à jour après retour gouvernance)

| # | Question | Décideur | Statut |
|---|---|---|---|
| A1 | Classeur Excel référentiel | — | **RÉSOLU** : `data_competences.py` fait foi (transcription retenue) |
| A2 | QCM eCall : 4e_C4.4 → 4e_C4.5 ? | — | **RÉSOLU** : reste en 4e_C4.4 (rattachement correct ; erreur d'analyse de l'audit initial, confondue avec 5e_C4.4) |
| A3 | `5e_C1.2/sequence.mhtml` : contenu 5e ou 4e ? | Pascal | ouvert |
| A4 | QCM domotique/éclairage : rester en 4e_C6.2 ? | Pascal | ouvert |
| A5 | Affiche Delagrave : droit de rediffusion ? | Pascal | ouvert |
| A6 | Progression 3e (P1→P5) et périmètre du LOT 1 | Pascal | ouvert |
| A7 | Publication du lot 0 (audit) sur `main` | ChatGPT | en cours (PR brouillon depuis `draft/agent-sequences`) |

## 2026-07-21 — Gouvernance GitHub configurée (retour ChatGPT/Pascal)

- `main` protégée : intégration uniquement par Pull Request ; fusion finale par
  ChatGPT après validation de Pascal.
- Branche de travail autorisée pour Claude : **`draft/agent-sequences`**
  (poussées et PR brouillon autorisées ; jamais de poussée sur `main`, de
  fusion, de modification des règles, de suppression de branche, ni de demande
  de clé/jeton).
- Corrections apportées au LOT 0 avant poussée : A1 et A2 résolus (voir tableau),
  convention d'identifiants préfixés explicitement confirmée dans l'audit.
- Lots suivants autorisés en préparation (PR distinctes, sans fusion) :
  corrections techniques rapides, puis LOT 1 « Station d'alerte cyclonique
  connectée » (3e_C4.3, 3e_C4.4, 3e_C4.5, 3e_C4.6) en versions A/B/C, avec QCM
  d'entraînement public et évaluation sommative à corrigé non publié.
- Statut de relecture : les séquences peuvent rester `A_RELIRE_PASCAL` sans
  bloquer la préparation des lots suivants.

## 2026-07-22 — Thème 2 · LOT 01 « Station d'alerte cyclonique connectée » (Fable, branche `fable/theme-2/lot-01-station-alerte-cyclonique`)

1. **LOT 1 réalisé** conformément à la feuille de route (P1) : séquence-projet
   mutualisée 3e_C4.3→C4.6 (4 séances, versions A/B/C), QCM d'entraînement
   32 q, synthèses élève/professeur, fiche pédagogique, matrice de couverture,
   5 SVG originaux CC0, jeu de données 48 h **simulé** (CSV/ODS/XLSX),
   rapport de tests automatisés. Périmètre limité au Thème 2 : les corrections
   rapides hors Thème 2 listées au §4 de la feuille de route (3e_C9.1, 5e_C1.1,
   4e_C1.4) sont laissées aux agents des thèmes concernés.
2. **Statuts** : `3e_C4.3` → `COMPLET ET VALIDABLE` ; `3e_C4.4`, `3e_C4.5`,
   `3e_C4.6` → `COUVERT PAR UNE SÉQUENCE MUTUALISÉE` (README pointeurs posés).
   Audit resynchronisé via `_outils/build_audit.py` (114 codes).
3. **Badge NEW (règle obligatoire de Pascal)** : création de `nouveautes.json`
   (durée 21 jours par défaut) et extension de `_outils/make_index.py` :
   badges automatiques thème/compétence/code/liens, ancres directes
   (`index.html#3e_C4.3` ouvre la compétence et défile jusqu'au code),
   pulsation désactivée avec `prefers-reduced-motion`, expiration automatique
   côté client sans regénération. Fichiers partagés modifiés en conséquence
   (make_index.py, index.html, README.md régénérés) — modification strictement
   additive, signalée dans le manifeste du lot.
4. **Gouvernance de publication** : sur instruction directe de Pascal
   (2026-07-22), l'agent Fable publie lui-même le lot sur GitHub (branche
   dédiée). La date `date_publication` de `nouveautes.json` est fixée au
   2026-07-22 ; si la fusion dans `main` intervient plus tard, l'ajuster avant
   fusion. **Évaluation sommative non incluse** (à construire par l'enseignant,
   corrigé non publié).

## 2026-07-22 (suite) — Thème 2 · LOT 02 « Internet jusqu'à Sainte-Luce » + unification nouveautes.json (Fable, branche `fable/theme-2/lot-02-internet-sainte-luce`)

1. **LOT 02 réalisé** : séquence-projet 3e_C4.7+C4.8 (3 séances, 3 simulateurs
   HTML intégrés — paquets, jeu du routeur, panne/résilience —, activité
   débranchée, versions A Filius / B Packet Tracer À CONFIRMER / C), QCM 30 q
   (15 par code), synthèses, fiche pédagogique, matrice, 4 SVG originaux CC0,
   README pointeur 3e_C4.8. Statuts : `3e_C4.7` → COMPLET ET VALIDABLE ;
   `3e_C4.8` → COUVERT PAR UNE SÉQUENCE MUTUALISÉE.
2. **Conflit nouveautes.json résolu** : le Thème 3 avait fusionné dans main un
   nouveautes.json au format différent (clé `nouveautes`, champs `date`/`url`).
   Branche Thème 2 rebasée sur main ; **format unifié** adopté (clé `entrees`,
   `date_publication`, `sequence`/`qcm`, `nature`, `competence`, bloc `config`)
   avec **entrée 4e_C7.1 du Thème 3 intégralement préservée et convertie**
   (aucune perte). Le badge NEW du tableau de bord (implémenté dans
   make_index.py par le Thème 2) fonctionne désormais pour les deux thèmes.
   **À entériner au Conseil du 28/07** ; si le Thème 3 préfère un autre format,
   l'adaptation est mécanique (le générateur lit un seul fichier).
3. **Publication** : lot-01 poussé sur GitHub par Pascal (bundle) ; lot-02
   suit le même canal tant que la session n'est pas reliée au dépôt.

## 2026-07-22 (soir) — Thème 2 · LOT 03 « SOS station : réparer plutôt que jeter » + règle images v2 (Fable, branche `fable/theme-2/lot-03-reparer-plutot-que-jeter`)

1. **Règle des images v2** (décision Pascal du 22/07, rédigée par Fable) ajoutée au
   skill `licences-medias-education` : images ENCOURAGÉES selon trois usages
   (image-objet prioritaire, image-explication, image-contexte), décoratif toujours
   interdit, critère de contrôle en fin de lot. À entériner au Conseil du 28/07.
2. **LOT 03 réalisé** : séquence 3e_C5.1→C5.4 (4 séances, simulateur de dépannage à
   2 pannes avec compteur de mesures et verrou pédagogique, arbre de diagnostic,
   plan coté, versions A/B/C), QCM 32 q dont 10 illustrées (moteur QCM étendu :
   champ `img` optionnel + alt), synthèses, fiche, matrice, 5 SVG CC0.
   Statuts : 3e_C5.1 → COMPLET ET VALIDABLE ; C5.2/C5.3/C5.4 → COUVERTS (pointeurs).
   La compétence C5 de 3e, entièrement vide ce matin, est couverte.
3. **Signalement inter-thèmes** : l'indice de réparabilité (3e_C3.3, Thème 1) est
   évoqué en ouverture EDD — l'agent du Thème 1 peut s'y référer pour sa séquence.

## 2026-07-23 — Thème 2 · LOT 04 « Programmer l'alerte » + CodeLab Techno + règle A/B/C (Fable, branche `fable/theme-2/lot-04-programmer-alerte`)

1. **CodeLab Techno implémenté** (composant commun prévu par le prompt maître) :
   coloration Python, gutter synchronisé, A−/A+, retour à la ligne, plein écran,
   export .py, import, sauvegarde locale automatique, surlignage de lignes piloté
   par les consignes, comparaison avec la version d'origine. Réutilisable par les
   trois thèmes (le code vit dans la séquence 3e_C6.1, extraction possible vers
   _ressources-communes sur décision du Conseil).
2. **LOT 04 réalisé** : 3e_C6.1 → COMPLET ET VALIDABLE ; 3e_C6.3 → COUVERT
   (pointeur). 3e_C6.2 volontairement non traité (séquence Algorigrammes DNB
   existante, non modifiée, liée en révision) : la compétence C6 de 3e est
   complète sans doublon. Innovation : les vérificateurs des activités 3-4
   analysent le code réellement écrit par l'élève dans l'éditeur.
3. **Règle d'or « Trois façons de vivre la séquence » (A/B/C)** (décision Pascal
   du 23/07) inscrite au skill sequence-pedagogique-engageante, avec la nuance
   « quand c'est possible » et l'exigence de justification en fiche pédagogique
   en cas d'omission. À entériner au Conseil du 28/07.
4. **Bilan 3e du Thème 2 après ce lot** : C4 (8/8), C5 (4/4), C6 (3/3, dont 1
   préexistant) = 15 codes de 3e couverts — la part 3e du Thème 2 est complète
   pour la rentrée 2026. Reste (seconde vague) : îlots 5e et 4e.

## 2026-07-23 — Thème 2 · Correctif QCM LOT 03 & 04 + LOT 05 « Le lampadaire intelligent » (Fable, branches `fable/theme-2/lot-04-programmer-alerte` et `fable/theme-2/lot-05-lampadaire-intelligent-5e`)

1. **Correctif qualité (commit dédié sur la branche lot-04)** : les banques des
   QCM LOT 03 (déjà publié) et LOT 04 plaçaient la bonne réponse toujours en
   position A — le moteur n'effectue pas de mélange à l'affichage, un élève
   l'aurait repéré en trois questions. Permutation déterministe appliquée
   (répartition 8/8/8/8 et 7/8/7/8), champ `d` permuté à l'identique, aucun
   contenu pédagogique modifié. Les QCM LOT 01, 02 et 05 sont équilibrés.
   **Point de vigilance pour le Conseil du 28/07** : contrôle « répartition
   des bonnes réponses » à ajouter au skill controle-qualite-lot.
2. **LOT 05 réalisé — îlot 5e COMPLET de la compétence C4** (les 8 codes du
   niveau sur un objet-fil unique, le lampadaire solaire du parking) :
   séquence 5 séances (fonctions/solutions + matériaux, chaîne d'énergie et
   natures, chaîne d'information avec simulateur interactif à verrou
   expérientiel, descripteurs et données, réseau local + jeu du courrier
   débranché prescrit par C4.8, réinvestissement sonnette connectée),
   QCM 32 q (4 par code, 6 illustrées, en-tête standard), synthèses ×2,
   fiche, matrice 1-32, 3 SVG CC0, 7 README pointeurs, versions A/B/C.
   Statuts : 5e_C4.1 → COMPLET ET VALIDABLE ; 5e_C4.2→C4.8 → COUVERTS.
   Première entrée 5e du Thème 2 : langue et guidage calibrés 12 ans.
3. **Choix pédagogique assumé** : un seul lot pour les 8 codes (au lieu de
   2-3 lots) car le programme de 5e les prescrit sur UN objet simple du
   quotidien ; l'éclatement aurait créé des redites. Le même objet-fil pourra
   porter l'îlot 5e_C6 (comportement programmé du lampadaire).

## 2026-07-23 — Progressions annuelles 2026-2027 : maquette 5e + canevas commun (Fable, branche `fable/progressions/maquette-5e`)

1. **Décision Pascal (23/07)** : un classeur de progression PAR CLASSE, adossé
   au Référentiel 2024, intégrant pour chaque séquence un « générateur de
   séquence » 2024 avec bloc « Cahier de texte Pronote » prêt à coller.
   Horaire retenu : 1 h 30 / semaine. Calendrier : Martinique 2026-2027 avec
   semaines tampon intégrées (~20 % de l'année non planifiée pour absorber
   les aléas — Fête de la science, sorties, ERASMUS…).
2. **Maquette 5e livrée et validée** : `_progressions/5e/…xlsx` — accueil-
   dashboard cliquable, calendrier teinté par période, frise gantt des 37
   semaines, référentiels cycle 4 (114 codes) et 5e (38 codes), progression
   7 séquences (29 séances + 8 tampons), générateurs S1→S7. S4/S5 remplis
   (ressources lampadaire en ligne), S6 pré-rempli ; S1-S3 → IA Thème 1,
   S7 → IA Thème 3 (canevas posés, voir `_progressions/README.md`).
3. **Pour le Conseil du 28/07** — deux points ajoutés à l'ordre du jour :
   (a) entériner le canevas obligatoire du générateur (socle par code +
   agrégé, CRCN/Pix avec niveaux, cahier de texte Pronote, répartition
   🏫/🏠/🔁, versions A/B/C) ;
   (b) **vérification croisée des « compétences écrites »** (demande Pascal :
   « parfois on se trompe ») — chaque IA relit les onglets des AUTRES thèmes :
   intitulés mot à mot conformes au référentiel, rattachements séquence↔codes,
   socle, CRCN, couverture des 38 codes 5e. Corrections par l'IA responsable
   uniquement.
4. Déclinaisons 4e et 3e : par Fable après le Conseil (ou avant si le temps
   le permet), sur le même canevas.

## 2026-07-23 — Progressions : classeur 4e + notification aux autres IA (Fable, branche `fable/progressions/maquette-5e`)

1. **Canevas 5e validé par Pascal** (tests réels du moteur d'imprévus en Excel :
   insertion, décalage, effacement, retour au nominal — tout confirmé), avec en
   version personnelle .xlsm : grandes fenêtres de saisie, ouverture sur la
   semaine en cours, copie du cahier de texte en un clic (installateur
   PowerShell : Excel fabrique lui-même les macros).
2. **Classeur 4e produit** sur le même canevas : 28 séances + 9 tampons,
   38 codes, Nathan 4e (11 problématiques mappées), générateurs S4-S5-S6
   pré-remplis par Fable avec les QCM 4e existants du dépôt (jardin connecté,
   eCall, automatisation, réseaux, éclairage, algorigrammes — non modifiés),
   S1-S3 → IA Thème 1, S7 → IA Thème 3.
3. **ANOMALIE RÉFÉRENTIEL DÉTECTÉE ET CORRIGÉE** : 4e_C4.3 (forme d'une pièce
   ↔ procédé) n'était rattaché à AUCUNE séquence de la progression 4e du
   référentiel — réintégré dans S6 « Réparer sans notice ». Illustre l'intérêt
   de la vérification croisée des compétences écrites (Conseil du 28/07).
4. **Notification aux autres IA** : messages prêts (transmis par Pascal dans
   leurs conversations) — voir `_progressions/README.md` pour le contrat.
   Classeur 3e : à produire (même canevas).

## 2026-07-23 — Progressions : classeur 3e (année DNB) — le triptyque est complet (Fable, branche `fable/progressions/classeur-3e`)

1. **Classeur 3e produit** : 9 séquences · 30 séances + 4 tampons + 3 semaines
   RÉVISIONS DNB (S35-S37, rien de neuf après début juin). AJUSTEMENT assumé :
   le référentiel prévoyait 35 séances, intenables à 1 h 30/sem avec le DNB —
   compressions documentées séquence par séquence, à entériner au Conseil.
2. Générateurs S4-S5-S6 REMPLIS avec les 4 séquences Thème 2 en ligne (station
   cyclonique, Internet Sainte-Luce, SOS station, Programmer l'alerte) et
   cahiers de texte Pronote rédigés. S7-S8-S9 (fil rouge) → IA Thème 3 ;
   S1-S3 → IA Thème 1.
3. **CORRECTION du journal du 23/07 (LOT 04)** : le bilan « C4 de 3e : 8/8 »
   était inexact — 3e_C4.1 (élaborer la chaîne d'énergie) et 3e_C4.2 (justifier
   matériau/procédé) sont À CRÉER (audit). Prochain lot Thème 2 : ces 2 codes,
   sur l'objet-fil station (séance 4 du générateur S4 les attend).
4. Le triptyque 5e/4e/3e est en place dans `_progressions/` : les IA des
   Thèmes 1 et 3 peuvent remplir leurs onglets des trois classeurs.

## 2026-07-23 — Thème 2 · LOT 06 « L'énergie de la station » (Fable, branche `fable/theme-2/lot-06-energie-station-3e`)

1. **LOT 06 réalisé — la compétence C4 de 3e est réellement complète** :
   3e_C4.1 (élaborer le schéma-bloc : palette avec intrus, natures,
   dimensionnement Wh/Ah avec marge raisonnée, simulateur d'autonomie 72 h à
   verrou expérientiel) et 3e_C4.2 (justifier matériau ET procédé : 5
   contraintes du site, abaque, 4 pièces, justification rédigée à 2 contraintes
   croisées, réinvestissement borne du stade en série). QCM 30 q (15/15,
   3 illustrées, réponses réparties 8/8/7/7), synthèses, fiche, matrice,
   3 SVG CC0, tests 23/23 (un lien inter-dossiers détecté par la suite et
   corrigé). Statuts : 3e_C4.1 → COMPLET ET VALIDABLE ; 3e_C4.2 → COUVERT.
2. Ce lot comble le manque signalé au journal précédent (audit « À CRÉER »)
   et remplit l'attente du générateur S4 du classeur de progression 3e
   (séance 4) — les liens y seront reportés après fusion.
3. Le projet-fil station est bouclé : comprise (C4.3-4.6), connectée (C4.7-4.8),
   réparée (C5), programmée (C6), alimentée (C4.1-4.2).

## 2026-07-23 — Thème 2 · LOT 07 « Programmer le lampadaire » (Fable, branche `fable/theme-2/lot-07-programmer-lampadaire-5e`)

1. **LOT 07 réalisé — îlot 5e_C6 complet** sur l'objet-fil du LOT 05 :
   carte d'identité du programme par blocs (C6.1), traduction en algorithme
   en langage naturel avec SI/ET/SINON (C6.2), simulateur PARAMÉTRABLE
   (SEUIL_NUIT, DURÉE) avec mission mairie et verrou expérientiel — réglage
   d'origine testé PUIS réglage modifié vérifié (C6.3). QCM 30 q (10/10/10,
   2 illustrées, réponses réparties 7/7/8/8), synthèses, fiche, matrice,
   2 SVG CC0, tests Playwright. Statuts : 5e_C6.1 → COMPLET ET VALIDABLE ;
   C6.2/C6.3 → COUVERTS (pointeurs).
2. **Bilan 5e du Thème 2** : C4 (8/8) + C6 (3/3) complets sur un objet-fil
   unique. Reste l'îlot 5e_C5 (dépannage 5e) en production future.
3. Le générateur S4 du classeur de progression 5e est câblé sur les nouvelles
   ressources (même commit) : séances 3-4 désormais 100 % outillées.

## 2026-07-24 — Thème 2 · Retour Pascal sur LOT 06 : bonus loi d'Ohm + correctif d'affichage (Fable, branche `fable/theme-2/lot-07-programmer-lampadaire-5e`)

1. **Demande Pascal** : les élèves voient peu (ou pas) la loi d'Ohm en physique
   faute de temps → activité BONUS ajoutée à « L'énergie de la station » :
   I = P÷U (0,5 A), chute de tension du câble U = R×I (0,2 V), choix du fusible
   1 A (rebouclage avec le fusible de « SOS station »). Hors barre de
   progression, aides ×2, correction complète. Pont interdisciplinaire
   physique-technologie assumé.
2. **Correctif d'affichage** signalé par Pascal : le bouton « M'entraîner : le
   QCM » du bilan débordait de sa pastille sur plusieurs lignes — display:block
   + white-space:normal appliqués aux TROIS séquences du gabarit (5e_C4.1,
   3e_C4.1, 5e_C6.1). À reporter dans le gabarit commun pour les futurs lots.

## 2026-07-24 — RÈGLE D'OR « Blocs élève obligatoires » (demande Pascal ; Fable, branche `fable/theme-2/regle-blocs-eleve`)

**Règle d'or n° 4 — structure minimale de toute séquence élève** (adoptée par
Pascal le 24/07/2026, applicable aux trois thèmes ; à inscrire au gabarit
commun lors du Conseil du 28/07) :

1. **Ouverture obligatoire** — la page commence par, dans cet ordre et avant
   tout autre contenu : un **titre** `<h1>` (emoji + nom court de la séquence,
   ex. « 🔋 L'énergie de la station ») puis un **sous-titre** d'une ligne qui
   annonce la mission de l'élève (ex. « Élaborer la chaîne d'énergie autonome
   de la station d'alerte — et justifier chaque matériau face au cyclone »).
2. **Bloc « 🧠 Prêt·e à t'entraîner ? »** — encadré centré, présent dans CHAQUE
   séquence élève, contenant : le nombre de questions du QCM, la mention du
   nombre de questions illustrées (schémas à lire), et un bouton unique
   « 🚀 Ouvrir le QCM d'entraînement » pointant vers le QCM du lot.
3. **Bloc « 🎁 Bonus (facultatif — hors parcours obligatoire) »** — encadré
   présent dans CHAQUE séquence élève, avec 2 à 3 défis ouverts (citoyen,
   technique, ancrage local Martinique…) clairement hors barre de progression
   et sans vérificateur : aucun élève ne doit être pénalisé de ne pas les faire.
4. **Emplacement** — ces deux blocs closent la séquence : après le bilan,
   avant le pied de page.

**Application immédiate (Thème 2)** : LOT 05 déjà conforme (modèle de
référence) ; LOT 06 (3e_C4.1-C4.2) et LOT 07 (5e_C6.1-C6.3) mis en conformité
dans ce lot (blocs standardisés ajoutés — le défi loi d'Ohm du LOT 06 reste
en activité bonus interne, les deux ne font pas doublon). LOTs 01-04 : déjà
conformes. Restent NON conformes dans le Thème 2 : `3e_C6.2
(sequence_algorigrammes_dnb.html)` et `4e_C6.2 (jardin connecté)` — contenus
antérieurs au gabarit, à traiter dans le lot de consolidation post-Conseil.
**Pour les Thèmes 1 et 3** : adoption à l'ordre du jour du Conseil du 28/07.

## 2026-07-24 — Gouvernance : garde-périmètre installée + décision d'autonomie reportée au Conseil (Pascal & Fable)

1. **Garde-périmètre active** (PR #33) : chaque PR vers main est vérifiée —
   une branche contenant `theme-1`/`theme-2`/`theme-3` ne peut modifier que
   le dossier de son thème (+ fichiers communs : index, README, audit,
   nouveautes.json, journal, _progressions/). `.github/` est intouchable
   depuis une branche de thème. Le thème 2 conserve `_outils/`.
   **Convention à respecter par toutes les IA : le nom de la branche porte le
   thème** (ex. `codex/theme-1/…`, `fable/theme-2/…`, `fable/theme-3/…`).
2. **Protection de main** : fusion uniquement par PR (ruleset actif) ; le
   contrôle `perimetre` sera rendu obligatoire dès sa première exécution.
3. **Décision de Pascal** : jusqu'au Conseil du 28/07, la fusion reste sa
   validation manuelle. À l'ordre du jour du Conseil : bilan de qualité des
   lots livrés par thème ; si concluant, passage à l'autonomie complète
   (auto-merge quand les contrôles sont verts), conditionné à un second
   contrôle obligatoire « contrôles de publication » (intégrité des classeurs
   _progressions, liens sans antislash, absence de correction d'évaluation
   sommative dans le dépôt public) que Fable tiendra prêt.

## 2026-07-24 — RÈGLE D'OR N° 5 « Gouvernance du dépôt » (décision Pascal)

Applicable immédiatement à toutes les intelligences artificielles du projet :

1. **Le nom de la branche porte les droits.** Toute branche de travail DOIT
   contenir le motif de son thème : `theme-1`, `theme-2` ou `theme-3`
   (ex. `codex/theme-1/lot-x`, `fable/theme-3/lot-y`). La garde-périmètre
   refuse toute PR dont les fichiers sortent du périmètre du motif :
   dossier du thème + fichiers communs (index.html, README.md,
   audit_couverture.csv/.json, nouveautes.json, JOURNAL_DES_DECISIONS.md,
   _progressions/). `_outils/` est réservé au Thème 2 ; `.github/` à Pascal.
2. **Main est protégé.** Aucune poussée directe : tout passe par une PR, et
   le contrôle `perimetre` doit être vert. Une PR refusée par la garde n'est
   pas un incident : c'est le système qui fonctionne — corriger la branche
   (ou son nom) et re-pousser.
3. **La fusion reste la validation manuelle de Pascal** jusqu'au Conseil du
   28/07, qui décidera du passage éventuel à l'autonomie complète
   (auto-merge sur contrôles verts + second contrôle « contrôles de
   publication »), sur la base de la qualité des lots livrés.
4. **Un refus de la garde ne se contourne jamais** (pas de fusion forcée,
   pas de modification de `.github/`) : toute évolution des périmètres se
   demande à Pascal et se décide au Conseil.

## 2026-07-24 — Thème 2 · LOT 08 « Dépanner le lampadaire » (Fable, branche `fable/theme-2/lot-08-depanner-lampadaire-5e`)

1. **LOT 08 réalisé — îlot 5e_C5 complet**, troisième et dernier volet de
   l'objet-fil « Lampadaire intelligent » : inspection visuelle interactive
   (6 zones, verrou expérientiel 6/6, distinction symptôme/cause, fausse
   piste du panneau sale traitée par comparaison), réparation en suivant le
   protocole fourni (simulateur pas à pas — une étape jouée trop tôt remet
   le chantier à zéro, volontairement ; verrou : test final exigé),
   découverte des procédés de l'atelier de fabrication (4 postes, familles
   additif/enlèvement, sécurité atelier), réinvestissement (vélo). QCM 30 q
   (10/10/10, 3 illustrées, réponses réparties 8/7/7/8 graine 83),
   synthèses, fiche, matrice, 3 SVG CC0, tests Playwright 22/22.
   Règle d'or n°4 appliquée dès la conception. Statuts : 5e_C5.1 → COMPLET ;
   C5.2/C5.3 → COUVERTS (pointeurs).
2. **La 5e du Thème 2 est bouclée** : C4 (8/8) + C5 (3/3) + C6 (3/3) sur un
   objet-fil unique, décrit → programmé → dépanné. Restent les îlots de 4e.
3. Le générateur S6 du classeur de progression 5e est câblé sur les
   ressources publiées (B14, liens Pronote des séances 1 et 3) — même
   commit, formules du classeur vérifiées intactes.

## 2026-07-24 — Thème 2 · LOT 09 « Le jardin connecté » (Fable, branche `fable/theme-2/lot-09-jardin-connecte-4e`)

1. **LOT 09 réalisé — îlot 4e_C4 complet (9 codes)** sur le nouvel objet-fil
   de 4e, le jardin connecté (choisi pour sa continuité avec la séquence
   « arrosage automatique » existante de 4e_C6.2) : chaîne d'énergie et
   transformations (C4.1-C4.2), chaîne d'information, données téléversées et
   table structurée avec explorateur à verrou 3 bacs (C4.4-C4.6), réseau,
   IP fixe et simulateur de dépannage à verrou 3 pannes (C4.7-C4.9), forme
   et procédé (C4.3). QCM 30 q (7/10/10/3 par famille, 3 illustrées,
   réponses 7/7/8/8 graine 91), synthèses, matrice, 3 SVG CC0, 8 README
   pointeurs, tests Playwright 21/21. Règle d'or n°4 native.
2. **Ressources existantes intégrées, pas remplacées** : les QCM
   « automatisation premium » (C4.1), eCall (C4.4) et XXL réseaux (C4.7)
   restent en entraînement complémentaire, référencés par les README et la
   séquence. Les anomalies de licence du QCM XXL restent tracées (audit).
3. Générateurs S4 ET S5 du classeur 4e câblés sur les ressources publiées
   (même commit) ; formules du classeur vérifiées intactes.
4. **Marche 5e → 4e assumée** : objet automatisé (lampadaire) → système
   connecté (données qui sortent sur un réseau). Le Thème 2 couvre
   désormais : 5e 14/14 · 4e C4 9/9 · 3e 15/15. Restent 4e_C5 et 4e_C6.

## 2026-07-24 — RÈGLE D'OR N° 6 « Convention des chaînes » + complément règle n° 4 (demande Pascal ; Fable, branche `fable/theme-2/regle-or-6-convention-chaines`)

**Règle d'or n° 6 — disposition des chaînes dans tous les schémas** (proposée
par Pascal, adoptée le 24/07/2026 ; à faire adopter par les Thèmes 1 et 3 au
Conseil du 28/07) :

1. Dans tout schéma représentant les deux chaînes, la **chaîne d'INFORMATION
   se place EN HAUT** et la **chaîne d'ÉNERGIE EN BAS**, conformément à la
   convention de la discipline (manuels, sujets de DNB).
2. La **flèche d'ORDRE descend** de la chaîne d'information vers la chaîne
   d'énergie — la disposition porte le sens : la commande au-dessus de la
   puissance (« le cerveau commande les muscles »).
3. Justification cognitive : cohérence spatiale avec tous les autres supports
   que rencontre l'élève (charge cognitive réduite, mémoire spatiale fiable
   en situation d'examen) ; la question métacognitive utile est « pourquoi
   l'information est-elle en haut ? », pas « pourquoi est-ce inversé ici ? ».

**Application immédiate** : les 2 SVG non conformes du Thème 2 corrigés
(`chaines_energie_information_lampadaire.svg` LOT 05,
`chaines_jardin_connecte.svg` LOT 09 — desc accessibles mises à jour, flèche
d'ordre descendante, convention explicitée dans l'image). Le schéma existant
de 4e_C6.2 était déjà conforme.

4. **Volet élève (demande Pascal)** : chaque fois qu'une consigne fait
   TRACER ou RECOPIER les chaînes, un encadré « 📐 Règle d'or du schéma »
   rappelle la convention avec sa formulation canonique : « l'INFORMATION
   en haut, l'ÉNERGIE en bas, la flèche d'ORDRE qui descend — le cerveau
   au-dessus des muscles, la commande au-dessus de la puissance. La
   disposition EST une leçon : elle montre qui commande, sans un mot. »
   Inséré dans les LOTs 05 (act. chaîne d'énergie, références haut/bas du
   schéma corrigées après l'inversion du SVG) et 09 (NB complet act. 1,
   rappel court act. 2, synthèse élève). À intégrer au gabarit commun pour
   tous les futurs lots des trois thèmes.

**Complément à la règle d'or n° 4** (signalé par Pascal : bouton QCM en
double) : le bouton « Ouvrir le QCM d'entraînement » figure **UNE SEULE
fois** par séquence, dans le bloc « 🧠 Prêt·e à t'entraîner ? ». Le bilan
conserve l'auto-positionnement et les liens vers les synthèses, sans bouton
QCM. Doublons retirés des LOTs 06, 07, 08 et 09.

## 2026-07-24 — Méthode Fable consolidée en un document unique (demande Pascal ; branche `fable/theme-2/methode-fable`)

`_outils/METHODE.md` : la méthode complète en trois piliers — produire un
lot premium (les 6 règles d'or, séquence, QCM, barre qualité), livrer et
gouverner (branches, garde-périmètre, fichiers générés, bancs d'essai,
circuits par IA), et RÉDIGER UNE PROGRESSION ANNUELLE (calendrier réel de
l'académie, 1 h 30/semaine, moteur d'imprévus à répercussion automatique,
tampons, générateurs avec socle/CRCN et cahier de texte Pronote — la partie
réutilisable chaque année). Le document fédère les six skills spécialisés
de `.claude/skills/` ; en cas d'écart, le journal fait foi. Même contenu
livré à Pascal en SKILL.md installable. ChatGPT et Grok sont invités à le
lire avant toute production — à entériner au Conseil du 28/07.

## 2026-07-24 — Thème 2 · LOT 10 « SOS jardin connecté » (Fable, branche `fable/theme-2/lot-10-depanner-jardin-4e`)

1. **LOT 10 réalisé — l'îlot C5 de 4e ouvre sur l'objet-fil du niveau** (le jardin
   connecté des LOTs 09 et 4e_C6.2) : 4e_C5.1 → COMPLET ET VALIDABLE ;
   4e_C5.2 et 4e_C5.3 → COUVERT (pointeurs). Progressivité 5e→4e assumée : le
   protocole n'est plus FOURNI (LOT 08), il est PROPOSÉ par l'élève — 6 tests
   ordonnés puis exécutés au poste de diagnostic (verrou 6/6, capteur menteur
   démasqué par le test discriminant mesure/réalité) ; remplacement en
   autonomie SANS protocole affiché (vignettes non numérotées, photo,
   comparaison, test final à l'eau, verrou 6/6) ; choix multicritère du
   procédé (impression 3D PETG, gamme, jeu fonctionnel), réinvestissement
   lampe du CDI avec frontière TBT/secteur nommée. QCM 30 q (10/10/10,
   3 illustrées, 8/7/7/8 graine 42), synthèses, fiche, matrice, 3 SVG CC0,
   rapport 23/23 (Playwright réel). La panne « capteur qui ment » amorce le
   LOT 11 (4e_C6.1/C6.3 : corriger le programme).
2. **`_outils/fix_r.js` recréé et commité** : l'outil de répartition des
   bonnes réponses, cité par la méthode et utilisé aux LOTs 01-09, n'avait
   jamais été commité. Version reconstruite : permutation déterministe
   (mulberry32 + Fisher-Yates, graine en argument), quotas équilibrés
   (écart max 1), échange `o[0]↔o[t]` / `d[0]↔d[t]`, réécriture du bloc
   `const QUESTIONS` à clés ordonnées. Usage :
   `node _outils/fix_r.js <fichier.html> <graine>`.
3. **Conseil des IA avancé au 25/07/2026, 8 h (heure de Martinique)**
   (décision Pascal, 24/07) : tous les points « à entériner au Conseil du
   28/07 » du présent journal sont réputés portés à l'ordre du jour du 25/07.

## 2026-07-24 — Thème 2 · LOT 11 « Ajuster le programme du jardin » (Fable, branche `fable/theme-2/lot-11-ajuster-programme-jardin-4e`)

1. **LOT 11 réalisé — la compétence C6 de 4e est complète et l'arc 4e de
   l'objet-fil est bouclé** (C4 structure → C6.2 programme → C5 dépannage →
   C6.1/C6.3 ajustement) : 4e_C6.1 → COMPLET ET VALIDABLE ; 4e_C6.3 → COUVERT
   (pointeur). **4e_C6.2 volontairement non traité** (séquence modèle
   « arrosage automatique » existante, NON modifiée, référencée au bilan) —
   même logique que 3e_C6.2 au LOT 04. Contenu : analyse des relevés USB
   (pompe qui bat 47 fois autour du seuil unique 40 %, arrosage à 13 h, cas
   normal de contrôle), spécification de l'hystérésis 35/45 (règle : écart >
   vibration de la mesure) et de la plage horaire (ET sur le démarrage
   seulement), banc de test à 4 scénarios en ordre libre (verrou __exp.scen),
   méthode de validation en 5 étapes (sauvegarde → simulation → plant témoin →
   non-régression, rollback), transfert lampadaire 5e (hystérésis 20/40 lux).
   QCM 30 q (15+15, 3 illustrées, 8/7/7/8 graine 57), synthèses, fiche,
   matrice, 3 SVG CC0, rapport 23/23 (Playwright réel).
2. **Branche empilée** : lot-11 est construit SUR lot-10 (même session, mêmes
   fichiers générés à la racine). Ordre de fusion : PR lot-10 d'abord, PR
   lot-11 ensuite — zéro conflit, zéro régénération intermédiaire. À
   entériner au Conseil du 25/07 comme pratique de « lots successifs d'une
   même session ».
3. **Bilan 4e du Thème 2 après ce lot** : C4 (9/9, LOT 09), C5 (3/3, LOT 10),
   C6 (3/3, dont C6.2 préexistant) = l'îlot 4e du Thème 2 est complet pour la
   rentrée 2026. Le Thème 2 entier (5e + 4e + 3e) est couvert.

## LOT 12 — Correctifs & illustrations Thème 2 (25/07/2026)
Suite à l'audit tranche 1 (Conseil des IA) : correction du QCM `4e_C4.1/qcm_automatisation_premium.html`
(image `undefined` sur les questions non illustrées — garde `if (q.img)`) ; insertion de l'encadré canonique
de la règle d'or n°6 dans les 3 séquences 3e_C4 ; compression de `4e_C4.7/Images/doc3_schema_parcours.png`
(2,6 Mo → < 300 Ko) ; ajout de 3 illustrations SVG originales CC0 (une par arc : 4e_C4 stockage/transformation,
4e_C5 capteur encroûté, 5e_C6 seuil jour/nuit) branchées sur les questions correspondantes, SOURCES_MEDIAS
des lots mis à jour. Constat aggravant (test Playwright réel) : `qcm_automatisation_premium.html` contient ~40 images HOTLINKÉES qui ne chargent pas (violation règle d'or n°1). Décision en attente du Conseil : archivage des 7 anciens QCM sans localStorage, premium en tête.

## Règle d'or n°7 — CRCN observable, tracé, justifié (25/07/2026, carte blanche de Pascal)
Toute association CRCN déclarée dans une ressource du dépôt DOIT comporter les cinq éléments :
1. la **compétence exacte** du cadre (code + intitulé officiel, ex. « 3.4 Programmer ») ;
2. le **niveau de maîtrise visé** (cycle 4 : viser surtout 2 à 4) ;
3. le **repère pour enseigner** correspondant, cité VERBATIM (libellé Pronote/Pix du document d'accompagnement) ;
4. une **action observable** de l'élève (ce qu'il fait réellement, pas « utilise l'ordinateur ») ;
5. une **trace produite** (fichier, réponse enregistrée, manipulation tracée, export) avec critère de réussite.
Pas de CRCN décoratif : sans action observable ni trace, la compétence est au mieux « travaillée », jamais « évaluée ».
Ressource étalon : `theme-2/.../4e/4e_C4.1/atelier_pix_crcn_jardin.html` (LOT 13).

## LOT 13 — Atelier Pix du jardin connecté + règle d'or n°7 (25/07/2026)
Carte blanche de Pascal. Création d'un atelier CRCN 100 % original (format inspiré des cahiers
d'entraînement Pix, contenus inventés dans l'univers du jardin) : 3 exercices — 1.3 Traiter des données
(tri RÉEL du tableau, tracé), 3.4 Programmer (algorithme d'hystérésis à compléter), 5.1 Résoudre des
problèmes techniques (démarche de dépannage ordonnée) — chacun avec cartouche complet règle n°7,
générateur de « trace Pix » à montrer au professeur, hors ligne, listes déroulantes (DYS), sauvegarde
localStorage. Lien ajouté au bloc Bonus de la séquence 4e_C4. Avis Copilot intégré : le CRCN devient
VISIBLE dans les pages web elles-mêmes.

## Règle d'or n°8 — Représentations technologiques utiles, progressives et traçables (25/07/2026)
Pierre angulaire de la discipline, validée par Pascal. Toute représentation d'une ressource du dépôt doit être :
1. **UTILE** — elle répond à un besoin précis (comprendre, communiquer, concevoir, valider), jamais décorative.
   Le bon outil pour la bonne question : croquis à main levée pour l'idée, schéma normalisé pour l'explication,
   diagramme fonctionnel pour l'organisation, modèle 3D/CAO pour la fabrication, graphique pour les données.
   Une représentation qui n'apprend rien est supprimée.
2. **PROGRESSIVE** — échelle du cycle : 5e LIT et COMPLÈTE des représentations fournies ; 4e CHOISIT le mode
   adapté et PRODUIT avec guidage ; 3e ÉLABORE seul (schéma-bloc, croquis coté, algorigramme) et JUSTIFIE son
   choix. Une même situation monte en gamme d'un niveau à l'autre.
3. **TRAÇABLE** — l'élève PRODUIT (papier photographié, fichier CAO, capture, export) ; la production est
   conservable, évaluable, reliée aux compétences (C2 du programme, D1.3 du socle « utiliser et produire des
   représentations d'objets » / « passer d'un langage à un autre », CRCN 3.2 si numérique). Lire un schéma
   n'est pas en produire un : les deux se distinguent dans la fiche de séquence.
4. **CONVENTIONNELLE** — légendes obligatoires, symboles normalisés quand ils existent, et règle n°6 pour
   les chaînes (information en haut, énergie en bas, l'ordre qui descend).
Gouvernance inter-thèmes (25/07/2026) : cette règle de Fable porte le n°8 ; la règle d'or n°9 est la formalisation détaillée de Codex (`theme-1/.../REGLE_OR_9_REPRESENTATIONS_TECHNOLOGIQUES.md`), qui la complète — principe (n°8) et cadre d'application (n°9) sont cohérents et se citent mutuellement.

## Règle d'or n°10 — Le journal fait foi (25/07/2026, sur décision de Pascal)
Le fichier `JOURNAL_DES_DECISIONS.md` est la mémoire officielle et l'autorité du dépôt. Quatre obligations :
1. **Lecture avant travail** : tout rédacteur (humain ou IA) lit le journal depuis `main` à jour AVANT de produire.
   Nul ne peut invoquer l'ignorance d'une décision consignée.
2. **Entrée par lot** : chaque lot ajoute son entrée au journal DANS LE MÊME COMMIT que le travail (date, contenu,
   décisions, tests réellement exécutés). Un lot sans entrée au journal est réputé inexistant.
3. **Réservation des transversaux** : tout numéro, nom ou convention transversale (règle d'or, standard, gabarit)
   se réserve dans le Registre central en tête de journal AVANT usage — leçon de la collision 8/9 du 25/07/2026.
4. **Accusé de lecture** : un nouveau rédacteur qui rejoint le projet prouve sa lecture en citant la dernière
   entrée du journal.
Le registre central des règles d'or (tableau en tête de fichier) est instauré par la présente règle.

## 2026-07-29 — Thème 2 · Lot d'harmonisation « titres charte + navigation règle n°11 » (Fable, branche `fable/theme-2/harmonisation-titres-navigation`)

1. **Charte des titres appliquée** (validée par Pascal, carte blanche du 26/07) :
   les 11 séquences, 11 QCM et l'atelier Pix du Thème 2 portent désormais
   `Thème 2 · Martinique — <niveau> · S<n> : <nom court>` en h1 et `<title>`
   (codes entre parenthèses dans le `<title>`). Le `S<n>` est aligné sur les
   onglets des classeurs de progression : 3e S4 (énergie + station), S5
   (Internet Sainte-Luce), S6 (SOS station + Programmer l'alerte) ; 4e S4-S5
   (jardin connecté), S6 (SOS jardin + Ajuster le programme) ; 5e S4-S5
   (lampadaire), S4 (programmer), S6 (SOS panne). AUCUN nom de fichier ni URL
   modifié. Les ressources héritées d'autres auteurs (premium, eCall, XXL,
   algorigrammes, éclairage, arrosage C6.2, DNB 3e_C6.2) sont INTOUCHÉES.
2. **Règle d'or n°11 appliquée au Thème 2** : barre de navigation collante
   `⌂ Accueil` sur les 45 pages Fable du thème (+ `← Séquence` sur QCM,
   synthèses et atelier). Écart assumé et documenté : lien RELATIF vers
   l'index (et non l'URL absolue de la règle) pour préserver le
   fonctionnement 100 % hors ligne du gabarit — l'esprit (retour en un clic,
   clavier, contraste, focus, pas de nouvel onglet, masqué à l'impression)
   est intégralement respecté. Registre central mis à jour (règles 9, 10, 11
   → fusionnées).
3. **METHODE.md enrichie** : préalables obligatoires (journal + registre,
   lecture de `_ressources-communes/`, doctrine « obligatoire sur classique,
   bonus sur trouvaille », skills externes = fond / règles d'or = forme) et
   section « Titres et navigation » documentant la charte.
4. **REVUE DU THÈME 2 (constats, nouvelle panoplie de skills)** :
   - Couverture : le Thème 2 (C4/C5/C6 des trois niveaux) est COMPLET —
     conformité règle n°4 revérifiée sur les LOTs 10 et 11 (un seul bouton
     QCM, blocs 🧠 et 🎁 présents).
   - **RÉGRESSION à corriger (hors périmètre de ce lot)** : les nouveaux
     classeurs `.xlsm` (PR #80) ont PERDU le câblage des séquences récentes —
     5e S6 sans aucun lien, 4e S4/S5/S6 ne pointant que vers les anciens QCM.
     À recâbler par un correctif dédié avec banc d'essai openpyxl
     (protocole du LOT S7). Les liens du classeur 3e sont intacts.
   - `docs/specifications/` (règle 11) est un emplacement nouveau introduit
     par ChatGPT ; à confirmer comme convention pour les règles longues.
5. **Tests réels** : suite Playwright dédiée (navigation visible en haut de
   page au défilement, liens cibles existants sur disque, un seul bouton QCM
   conservé par séquence, titres conformes à la charte, zéro erreur JS) —
   résultats consignés dans le message de livraison.

## 2026-07-29 — Correctif : recâblage des classeurs 5e/4e (.xlsm) — régression PR #80 (Fable, branche `fable/theme-2/recablage-classeurs-5e-4e`)

1. **Constat (revue du 29/07)** : les classeurs `.xlsm` reconstruits (PR #80)
   dataient d'avant la mise en ligne des LOTs 07-11 — 5e S4 pointait encore
   « îlot 5e_C6 🔜 », 5e S6 « À produire », 4e S4/S5/S6 « séquence 🔜 » avec
   les seuls anciens QCM. Le classeur 3e était intact.
2. **Correctif appliqué** : 18 cellules recâblées (11 en 5e — S4 : Programmer
   le lampadaire LOT 07 ; S6 : SOS panne LOT 08 · 7 en 4e — S4/S5 : Le jardin
   connecté LOT 09 + atelier Pix LOT 13 ; S6 : SOS jardin LOT 10 + Ajuster le
   programme LOT 11). Méthode : remplacements de SOUS-CHAÎNES ciblés — la
   pédagogie pré-remplie des déroulés n'est PAS réécrite ; les anciens QCM
   restent cités « en complément ». Gardes de structure avant écriture
   (S6!A18, libellés A4/A14) ; abandon si une chaîne attendue manque.
3. **Banc d'essai (protocole S7) réellement exécuté**, sur copies PUIS
   contre-vérifié sur les fichiers réels vs origin/main : comparaison cellule
   à cellule de TOUS les onglets non ciblés = 0 écart ; formules préservées
   (Calendrier 78/77, Frise 334, Progression 15) ; `vbaProject.bin` identique
   à l'octet près (macros intactes) ; openpyxl sans `data_only`.

## 2026-07-30 — Règle d'or n°12 « Cycle de vie des ressources héritées » + arbitrages fondateurs (Pascal & Fable, branche `fable/theme-2/regle-12-archives-outillage`)

1. **RÈGLE D'OR N°12 (validée par Pascal)** — que faire des séquences
   existantes d'avant le projet, sans jamais aborder une rentrée avec un
   mélange ambigu de ressources premium et datées :
   - **On n'archive qu'à la livraison du remplaçant.** Le lot qui livre la
     ressource premium déplace l'ancienne vers `_archive-anciennes-versions/`
     DANS LE MÊME COMMIT, avec README « remplacée par → lien » et mise à
     jour de TOUS les câblages (classeurs, README, séquences). Jamais de
     suppression sèche.
   - **En attendant leur tour**, les héritées restent en place et portent le
     badge 🛠 « ressource héritée — modernisation prévue » dans l'index
     (source : `_outils/heritees.json`, liste éditable ; 9 entrées posées :
     7 anciens QCM sans localStorage, séquence algorigrammes DNB,
     vittascience_variables).
   - **Une exception nommée** : `vittascience_variables.html` (3e_C9.1) est
     héritée mais INDISPENSABLE (enquête Vittascience améliorée par Pascal,
     donnée à tous les niveaux) — elle sera REFONDUE, pas simplement
     archivée : arc « variables » en trois marches (5e/4e/3e) ancré New York.
2. **Arbitrage §IV du projet pédagogique (décision Pascal, 30/07/2026)** :
   lecture PAR THÈME officialisée — Thème 1 · Chine, Thème 2 · Martinique,
   Thème 3 · New York, chaque élève traverse les trois villes chaque année ;
   la ligne « chaque niveau explore un thème » du §IV est à corriger dans le
   document (version corrigée fournie à Pascal pour `_ressources-communes/`).
   La charte des titres est généralisée en conséquence :
   `Thème <n> · <ville> — <niveau> · S<n> : <nom court>` (`Atelier` si pas
   de créneau de classeur).
3. **Standard « éditeur embarqué » (instruction Pascal)** : toute séquence de
   programmation intègre l'éditeur Vittascience DANS la page (iframe mode
   mixte) ; verrou adapté au cross-origin : prédire → tester → reporter.
   Consigné dans METHODE.md.
4. **Reprise des Thèmes 1 et 3 par Fable confirmée par Pascal** (« puisque tu
   vas reprendre les thèmes 1 et 3 ») — la mention du journal limitant Fable
   au Thème 2 est levée ; les circuits de livraison et la garde-périmètre
   restent inchangés (une branche par thème, motif du thème dans le nom).
5. **Outillage** : `make_index.py` charge `heritees.json` et pose le badge 🛠
   (CSS `.badge-herit`, infobulle) ; `_archive-anciennes-versions/` (déjà
   référencé au pied de l'index) est le lieu d'archivage officiel — aucun
   nouveau dossier créé. Test réel : index régénéré, 9 badges présents.



## 2026-07-30 — Infra : la garde-périmètre apprend la règle n°12 (Fable, branche `fable/infra/garde-regle-12`, PR #88)

La garde a refusé la PR #87 (arc variables 3e) — À RAISON : elle appliquait le
régime d'avant la règle n°12. Or l'archivage (`_archive-anciennes-versions/`)
et les registres transversaux (`_outils/heritees.json`, statuts OVERLAY dans
`_outils/build_audit.py`) font désormais partie de CHAQUE lot, quel que soit
le thème. Ces trois chemins rejoignent les fichiers COMMUNS de la garde.
Le reste du régime est inchangé (`_outils/` complet reste réservé aux
branches Thème 2 ; `.github/` reste refusé depuis toute branche de thème).
Vérification réelle : simulation locale du nouveau régime sur les fichiers
exacts de la PR #87 → 0 refus.

## 2026-07-30 — Thème 3 · Arc variables, marche 3e : refonte de « Vittascience variables » (Fable, branche `fable/theme-3/arc-variables-3e-refonte`, PR #87)

1. **Premier lot Fable sur le Thème 3 · New York depuis la levée du périmètre**,
   et PREMIÈRE APPLICATION de la règle d'or n°12 : l'atelier
   « Variables, types et systèmes » (3e_C9.1 → COMPLET ET VALIDABLE) refond la
   ressource héritée `vittascience_variables.html` (enquête Vittascience
   adaptée Pascal, désignée indispensable). L'ancienne version + ses captures
   PNG sont ARCHIVÉES (`_archive-anciennes-versions/C7_C9_…/3e_C9.1/`,
   README pointeur) ; l'URL historique porte un **stub de redirection**
   (complément pratique à la règle n°12 quand une URL a pu circuler) ;
   l'entrée `heritees.json` est retirée (8 badges 🛠 restants).
2. **Contenu** : 4 séances / 5 activités — simulateur de MÉMOIRE pas-à-pas
   (la variable = boîte étiquetée, verrou 6 étapes) ; table de suivi ;
   types et piège des guillemets en **prédire → tester → reporter** sur
   l'**éditeur Vittascience EMBARQUÉ** (standard Pascal : 3 iframes mode
   mixte, verrous d'ouverture) ; chasse aux 3 bugs du panneau du métro
   (96 St) avec preuve par la console ; algorithme → fonction → **banc de
   mise au point** (4 tests, cas limite 100 tranché par le besoin,
   non-régression). QCM 30 q (VAR/TYP/PRG/MAP 8/8/7/7, graine 47, 3
   illustrées), synthèses ×2, fiche, matrice 25 lignes, 3 SVG CC0 (aucune
   capture d'écran), README refondu. La substance pédagogique de la
   ressource d'origine (guillemets, VMC→ventilation de station, devis→
   MetroCard, conversions) est PRÉSERVÉE et new-yorkisée ; la vidéo YouTube
   n'est pas reprise (dépendance externe + RGPD, consultable aux archives).
3. **Tests réels** : 30/30 PASS (rapport dans le dossier) — verrous fermés
   puis ouverts, sauvegarde/restauration, répartition QCM, stub, archive,
   zéro erreur JS.
4. **À suivre** : marches 5e (« la boîte qu'on lit ») et 4e (« types et
   décisions ») du même arc ; remplacement éventuel du QCM hérité 24 q
   (`qcm_python_variables.html`, conservé en complément).

## 2026-07-30 — Journal : restauration des deux entrées perdues lors de la résolution de conflit de la PR #87 (Fable)

La résolution web du conflit sur ce fichier (PR #87) a conservé un seul côté :
les entrées « Infra garde règle n°12 » (PR #88) et « Arc variables 3e »
(PR #87) avaient disparu de main. Restaurées ci-dessus à l'identique.
Leçon consignée : lors d'une résolution de conflit sur le JOURNAL, on
GARDE TOUJOURS LES DEUX BLOCS (fichier à ajout permanent) — et côté méthode,
ne plus laisser deux branches vivantes toucher le journal simultanément.

## 2026-07-30 — Thème 3 · Enrichissement demandé par Pascal : le plan de la ligne Q dans la situation déclenchante (Fable, branche `fable/theme-3/carte-ligne-q`, empilée sur la restauration du journal)

Sur retour enthousiaste de Pascal (« je voyage déjà ») : ajout d'une image v2
`ligne_q_plan_simplifie.svg` (SVG original CC0, conventions des plans de
transport, AUCUN élément copié du plan MTA protégé) dans la situation
déclenchante de l'atelier 3e_C9.1 — repère 📍 « TU ES ICI » sur 96 St
(pulsation douce), tracé jaune jusqu'à Coney Island, ce que la ligne dessert,
encart « express/local », clin d'œil ingénierie (2e Avenue ouverte en 2017)
et question de lecture du plan (règle n°8 : représentation utile, à lire).
Branche EMPILÉE sur `fable/theme-2/journal-restauration-30-07` (leçon du
conflit : jamais deux branches indépendantes sur le journal) — ordre de
fusion : restauration d'abord, carte ensuite.

## 2026-07-30 — Thème 3 · Photos réelles dans l'atelier 3e_C9.1 (carte blanche Pascal ; Fable, même branche `fable/theme-3/carte-ligne-q`)

Précision de la règle n°1 actée avec Pascal : les PHOTOS authentiquement
libres sont bienvenues quand licence vérifiée À LA SOURCE + fichier téléchargé
dans le dépôt (jamais de hotlink) + attribution complète (SOURCES_MEDIAS et
légende) + image traitée en document à LIRE. Processus réel : Pascal fournit
les PAGES sources (.mhtml Flickr), Fable extrait et audite les licences.
Résultat : mezzanine 96 St (MTA « SAS_2665 », CC BY 2.0, avec LE panneau LED
de la situation déclenchante !) INTÉGRÉE en ouverture ; écartées et tracées :
CC BY-ND (+ visages identifiables), CC BY-NC-ND (trop restrictive) . Le train
R160 a retrouvé sa page source grâce à Pascal (Flickr MTA 31863535272,
« 86th Street Second Av. Subway Station Unveiled », CC BY 2.0, 30/12/2016) :
INTÉGRÉ en ouverture de la séance 3 — preuve que la règle tient : pas de
provenance, pas de publication ; provenance retrouvée, publication.

## 2026-07-30 — Thème 3 · La 3e photo : Coney Island, cueillie PAR Fable dans le navigateur de Pascal (branche `fable/theme-3/coney-terminus`)

Première récolte de média via l'extension Claude in Chrome (installée ce jour
par Pascal) : recherche Wikimedia Commons pilotée dans son navigateur,
sélection de « Coney Island Stillwell Avenue Entrance 001.jpg » (Kidfly182,
CC BY 4.0 — licence vérifiée SUR la fiche du fichier, attribution officielle
fournie par la boîte « Download this file »), téléchargement 3840 px,
rapatriement par le pont, compression 1400 px. Intégrée en tête du bloc
🎁 Bonus (la façade de 1919, reliée au défi convertisseurs). La candidate
CC BY-NC-ND initialement écartée reste écartée — remplacée proprement.
Le trio visuel du voyage est complet : la station, le train, le terminus.

## 2026-07-30 — Thème 3 · Arc variables, marche 5e : « La boîte étiquetée » (Fable, branche `fable/theme-3/arc-variables-5e`)

1. **Marche 5e livrée — l'îlot 5e_C9 passe de vide à complet** : 5e_C9.1 →
   COMPLET ET VALIDABLE ; 5e_C9.2 et C9.3 → COUVERT (README pointeurs).
   Ancrage : le compteur de places du Cyclone de Coney Island (terminus de la
   ligne Q — continuité avec l'atelier 3e, photo d'entrée de gare MUTUALISÉE,
   non dupliquée). Fidélité au référentiel 5e : analyser et TESTER un
   programme FOURNI (banc attendu/obtenu, bug des « descendus » soustraits),
   le MODIFIER (la bonne ligne, non-régression), RÉALISER/METTRE AU POINT la
   barrière commandée (condition, cas limite zéro pile — miroir 5e du cas
   limite « air ≥ 100 » de 3e : la spirale règle n°8 en acte).
2. **Standard Vittascience embarqué** (2 iframes) + prédire→tester→reporter ;
   verrous : simulateur 4 étapes, éditeur ouvert, 2 bancs de tests 3/3.
   QCM 30 q (BOI/LIR/MOD 10/10/10, graine 53, réponses 8/7/7/8, 3 illustrées,
   réfutation de chaque distracteur). 2 SVG originaux CC0 (compteur-boîtes,
   barrière avec règle n°6 : l'ordre qui descend). Synthèses ×2, fiche,
   matrice 23 lignes, manifest.
3. **TP mBot2 v4.5 inscrit aux héritées 🛠** (demande Pascal du jour) :
   fonctionnel mais à revoir — pédagogie, ergonomie, design ; refonte prévue
   dans l'arc (le lien variables→robot, salué par Pascal, sera renforcé).
4. **Tests réels** : suite Playwright dédiée (rapport dans le dossier).

## 2026-07-30 — AMENDEMENT DE LA RÈGLE D'OR N°5 : autonomie de poussée pour Fable (décision Pascal, branche `fable/infra/regle-5-autonomie`)

Pascal amende le volet « livraison » de la règle n°5 : « tu vas pouvoir
pousser en toute autonomie, vu qu'il n'y a que toi et moi à travailler
dessus. Moi, je vais lire les séquences et je vais te donner mon retour. »

1. **Fable pousse ses branches et ouvre ses PRs en autonomie.** Le circuit
   bundle → Downloads → poussée manuelle par Pascal sort du chemin nominal ;
   il reste le plan B documenté (jeton expiré, pont fermé).
2. **Rien d'autre ne change.** La fusion reste la validation manuelle de
   Pascal après lecture ; `main` reste protégé ; la garde-périmètre
   (contrôle `perimetre`) reste en place et ne se contourne jamais ;
   `.github/`, rulesets et paramètres du dépôt restent à Pascal.
3. **Le droit est porté par un jeton à grain fin** créé par Pascal le
   30/07/2026 : dépôt unique `en-ligne-pour-le-cycle-4`, permissions
   minimales (Contenu et Demandes de tirage en lecture/écriture,
   Métadonnées en lecture seule, Compte : aucune), expiration 30 jours
   (29/08/2026). Renouvellement à échéance, sur décision de Pascal.
4. **Hygiène du secret** : le jeton transite par fichier via le pont
   (`Downloads/fable_token.txt`, supprimé par Pascal après
   provisionnement) ; il ne s'écrit jamais dans la conversation, jamais
   dans le dépôt, jamais dans les rapports. Le bac à sable étant éphémère,
   une perte se répare en rejouant le provisionnement par fichier.
5. **Première application : la présente PR**, poussée et ouverte par Fable —
   l'amendement qui se publie lui-même. (La branche `arc-variables-5e`,
   d'abord réservée à ce rôle symbolique, avait été poussée et fusionnée
   entre-temps par Pascal en PR #97 : l'îlot 5e_C9 est en ligne.)

## 2026-07-30 — Thème 3 · Ergonomie des éditeurs embarqués 🧪 (Fable, branche `fable/theme-3/ergonomie-editeurs-vs`)

1. **Retour de Pascal (deux fois — signal fort)** : sur l'atelier 3e_C9.1, ni
   l'éditeur Vittascience embarqué, ni le simulateur de mémoire, ni les tables
   de suivi ne se laissent trouver. Diagnostic : les barres `details.vs`
   repliées ressemblaient à des lignes discrètes ; rien n'indiquait qu'un
   éditeur complet dort dessous.
2. **Correctif (séquences 3e_C9.1 et 5e_C9.1, mêmes styles)** : barres 🧪
   restylées — bordure cyan, halo, appel « ▼ CLIQUE ICI — l'éditeur Python
   s'ouvre dans la page, rien à installer » en pulsation douce (désactivée si
   `prefers-reduced-motion`), bascule « ▲ replier » à l'ouverture. Le bloc
   « façons de vivre l'atelier » nomme désormais l'EMPLACEMENT de chaque
   outil (séance + activité du simulateur, des tables de suivi, des barres 🧪).
3. **Tests réels** : suite ciblée 15/15 (styles calculés, pulsation, dépliage,
   verrou `__exp.vs1`, mentions) + régression complète 5e 27/27. La suite 3e
   d'origine a péri dans la réinitialisation du bac à sable (à reconstituer).
4. **Première livraison du circuit autonome** (règle n°5 amendée, PR #98) :
   branche poussée et PR ouverte par Fable ; lecture et fusion par Pascal.

## 2026-07-30 — Thème 3 · Encoches de vérification question par question (Fable, branche `fable/theme-3/encoches-verification`, empilée sur `ergonomie-editeurs-vs`)

1. **Retour de Pascal** : après « Vérifier l'activité », impossible de savoir
   si on a réussi sans lire toute la correction — « ce serait bien cool
   d'avoir des encoches vertes en face des réponses », et un mot qui
   encourage. Diagnostic en creusant : DEUX bugs dormants — le paragraphe
   de retour était `display:none` (la classe `show` n'était jamais posée,
   et `warn`/`ko` n'avaient aucun style) et les classes `ok`/`ko` posées
   sur les champs n'avaient AUCUNE règle CSS. Le bouton ne montrait donc
   rigoureusement rien.
2. **Correctif (séquences 3e_C9.1 et 5e_C9.1)** : encoche ✔ verte / ✘ rose
   au bout de chaque question + bordure du champ colorée ; messages enfin
   visibles et ENCOURAGEANTS, gradués : 🎉 « Bravo — activité validée ! » /
   🟡 « il y a du très bon ! Les encoches ✘ te montrent où regarder » /
   🔴 « pas de panique : … re-vérifie quand tu veux » ; le verrou 🔒
   expérientiel s'affiche aussi. Variable `--ko` manquante ajoutée en 3e
   (le banc d'essai y référençait `var(--ko)` indéfini).
3. **Tests réels** : suite dédiée 11/11 (verrou visible, encoches mixtes,
   couleur calculée, 🎉 à 4/4, parcours 5e) + régressions 27/27 (5e) et
   15/15 (barres 🧪). Capture validée : encoche rattachée à SA question.
4. Empilement (pas de branche parallèle sur les mêmes fichiers) : cette
   branche contient le lot « barres 🧪 » — fusionner les PR dans l'ordre.


## 2026-07-30 — RÈGLE D'OR N°13 « Code coloré façon IDE » (demande Pascal, branche `fable/theme-3/code-colore-ide`, empilée sur `encoches-verification`)

1. **Demande de Pascal** : « J'aimerais avoir des couleurs pour les variables,
   constantes…, comme un IDE, par exemple Sublime Text ou PyCharm. Il serait
   nécessaire d'établir une règle d'or par rapport à ça. » Numéro 13 réservé
   au registre (règle n°10).
2. **La règle** : tout listing de programme affiché est colorisé selon la
   palette commune du site — variables cyan, chaînes vertes, nombres orange,
   mots-clés violets gras, `=`/opérateurs jaunes gras, commentaires gris
   italique, numéros de ligne discrets. AUCUNE dépendance externe (pas de
   highlight.js/CDN : versions 🅲 hors ligne intactes) : un colorisateur
   embarqué `pyc()` de ~20 lignes, appliqué à `pre.code` et aux lignes du
   simulateur. Le `<code>` en ligne de la prose reste monochrome. Une
   légende 🎨 accompagne le premier listing de chaque page. Palette et
   doctrine documentées dans `_outils/METHODE.md`.
3. **Application immédiate** : séquences 3e_C9.1 et 5e_C9.1 (simulateurs,
   5 listings `pre.code`, valeurs des boîtes mémoire typées-colorées :
   texte vert / nombre orange — le TYPE devient visible, renfort direct de
   la séance types). Généralisation aux autres ressources : au fil des
   vagues de modernisation (règle n°12).
4. **Tests réels** : suite dédiée 17/17 (spans posés, couleurs calculées,
   légende, textes intacts, badges) + régressions 11/11, 27/27, 15/15.

## 2026-07-30 — Thème 3 · Bonus outillés + retrofit du TP mBot2 (Fable, branche `fable/theme-3/bonus-editeur-retrofit-tp`, empilée sur `code-colore-ide`)

1. **Retour de Pascal** : le défi du Bonus 3e dit « dans l'éditeur embarqué »…
   mais le bloc Bonus n'en avait pas. Corrigé : éditeur Vittascience embarqué
   AU BAS du bloc 🎁 des deux séquences de l'arc (3e : vs4 · 5e : vs3),
   même standard replié + appel « CLIQUE ICI ».
2. **TP mBot2 v4.5 (héritée 🛠)** — retrofit en attendant la refonte :
   navigation règle n°11 (⌂ Accueil + ← Séquence Variables 3e_C9.1) ;
   règle n°13 appliquée à ses listings via colorisateur + MutationObserver
   (la page re-génère ses <pre> : les nouveaux venus sont colorés à
   l'apparition), palette MAPPÉE sur les jetons locaux du TP (cyan/violet/
   or/vert/orange) — alignement complet sur la palette du site à la refonte.
3. **Jardin connecté 4e_C6.2** (séquence modèle historique) : navigation
   règle n°11 ajoutée — volet livré par la branche `fable/theme-2/
   jardin-navigation` (fichier seul ; l'entrée de journal voyage ici,
   même précédent que la PR méthode du jour). Constat au passage : le
   « code enseignant » de sa fiche professeur (GJEP) est lisible dans la
   source publique — loquet de confort, PAS une protection ; rappel :
   aucune correction sommative confidentielle dans le dépôt public.
4. **« Appliquer à tous les documents »** (demande Pascal) : la
   généralisation des règles 11 et 13 aux autres ressources à listings se
   fera par vagues (règle n°12), TP mBot2 refondu en tête.
5. **Tests réels** : suite retrofit 11/11 (éditeurs du Bonus en place, nav
   du TP, cibles des liens, 23/23 listings présents colorés, zéro erreur
   JS) + régressions 17/17, 11/11, 27/27, 15/15.

## 2026-07-30 — Thème 2 · Densification du « Jardin connecté » 4e_C6.2 (Fable, branche `fable/theme-2/jardin-densification`, empilée sur `jardin-navigation`)

1. **Audit de Pascal, implacable** : 3 séances de 55 min ne totalisaient que
   6 questions et 2 curseurs, sans AUCUN code à toucher (ni blocs ni Python)
   pour une compétence nommée « COMPLÉTER UN PROGRAMME » ; et le « niveau de
   maîtrise visé » restait imprécis. Ses trois formats demandés : code
   prérempli, blocs en désordre à ordonner, Python à trous.
2. **Refonte v2 (règle n°12)** : v1 archivée dans `_archive-anciennes-versions/
   C6-comprendre-et-modifier-un-programme-associe/4e_C6.2/` (+ README) ; URL
   et nom de fichier INCHANGÉS. La v2 garde l'histoire, les 3 séances, le
   simulateur de pompe et la fiche professeur (code GJEP, assumé « loquet de
   confort » avec avertissement), et passe à **8 activités vérifiées** :
   chaîne d'info · capteur analogique 0-1023 → % · **blocs en désordre**
   (table de positions, DYS-compatible) · décision + cas frontière ·
   **Python à trous** (3 trous dans le programme FOURNI) · banc de tests
   T1/T2/T3 (frontière 30 pile) · cahier des charges avec preuves · impact.
   3 éditeurs Vittascience embarqués (S1, S2, Bonus), verrous expérientiels,
   encoches ✔/✘, moteur de sauvegarde KEY, règles 4/6/7/11/13 natives.
3. **Référentiel précisé** : « niveau de maîtrise visé » détaillé par séance
   (découverte → consolidation → validation-évaluation LSU), capacité
   observable reformulée (remettre en ordre, compléter, exécuter, prouver).
4. **Titre charte** : « Thème 2 · Martinique — 4e · Atelier : Le jardin
   connecté — arrosage automatique (4e_C6.2) ».
5. **Tests réels** : suite dédiée **27/27** (rapport dans le dossier).
   Empilement : cette branche contient le volet navigation ; à fusionner
   APRÈS les PR theme-3 du jour (je rebaserai s'il faut réconcilier le
   journal — les deux blocs seront conservés).


## 2026-07-30 — RÈGLES D'OR N°14 À 17 : l'audit de Pascal devient loi (branche `fable/theme-2/regles-14-17`)

Pascal, en lisant les séquences (jardin 4e_C6.2, puis 4e_C9 « jardin-programme »
du Thème 3), a énoncé en une journée ce qui manquait partout. Quatre règles,
numéros 14-17 réservés au registre (règle n°10) :

1. **N°14 — Aucun exercice muet.** Tout exercice donne un retour immédiat,
   gradué et bienveillant : encoches ✔/✘ par question (champ coloré), message
   🎉 « Bravo » / 🟡 « il y a du très bon » / 🔴 « pas de panique » qui invite
   à re-vérifier, verrous expérientiels pour les gestes (éditeur ouvert, banc
   exécuté, simulateur déroulé). Un champ libre n'est jamais « corrigé » par
   simulation : présence vérifiée + sauvegarde + correction à déplier.
2. **N°15 — Zéro papier obligatoire.** Toute production demandée à l'élève —
   Bonus et défis COMPRIS — a son champ dans la page, sauvegardé localement
   (motif : « je tombe sur zéro papier », Pascal). Le cahier reste possible
   (version 🅲), jamais requis.
3. **N°16 — Blocs ↔ Python, dans la page.** Toute activité de programmation
   embarque l'éditeur Vittascience (mode mixte) et fait vivre LES DEUX SENS :
   construire en blocs → lire le Python généré ; modifier le Python → observer
   les blocs. Le gabarit canonique vit dans
   `_outils/gabarits/vittascience_embed.html` (source de vérité unique,
   CSS et suivi compris) : on l'INJECTE À LA CONCEPTION — jamais d'inclusion
   dynamique à l'exécution, pour préserver le standard « page monofichier
   hors ligne » (arbitrage rendu sur l'idée de « routine » de Pascal : oui au
   gabarit unique, non à l'appel à l'exécution).
4. **N°17 — 55 minutes pleines.** Une séance = 55 minutes réelles : des
   activités vérifiées en nombre suffisant (l'audit fondateur : « 3 × 55 min
   pour 6 questions et 2 curseurs »), un chronométrage indicatif par activité,
   au moins un GESTE de code vérifié par séance de programmation (ordonner,
   compléter, écrire), et un Bonus outillé (champ + éditeur) pour les rapides.
5. **Typographie des problématiques** (au METHODE) : espace insécable avant
   « ? ; : ! » — jamais de ponctuation orpheline en bout de ligne (signalement
   Pascal sur le « ? » isolé du 4e_C9).
6. **Application** : natives dans l'arc variables, le jardin 4e_C6.2 v2 et les
   retrofits du jour ; les quatre séquences Thème 3 héritées d'une session
   parallèle (3e_C7, 4e_C7, 4e_C8, 4e_C9 — champs muets, sans éditeur) passent
   en tête de la file de mise en conformité, 4e_C9 en premier (lot suivant).

## 2026-07-30 — Thème 3 · Mise en conformité du 4e_C9 « jardin-programme » (Fable, branche `fable/theme-3/conformite-4e-c9`)

1. **Première application des règles n°14-17** (lot précédent), sur la page
   que Pascal lisait : la séquence 4e_C9 d'une session parallèle (v1 « Agent
   Grok », 176 lignes — champs muets, deux sauvegardes sur six via alert(),
   aucun éditeur, listings monochromes, pas de navigation, « ? » orphelin).
   V1 archivée (règle n°12), URL inchangée, contenu et voix CONSERVÉS
   (l'hystérésis est une excellente idée — elle est gardée et outillée).
2. **Conformité complète** : nav ⌂+QCM (11) · listings colorés + légende (13) ·
   4 vérificateurs à encoches et messages gradués, verrous éditeur sur les
   activités 1 et 3 (14) · TOUS les champs sauvegardés, alert() supprimés,
   Bonus doté de champs ET d'un éditeur pour le défi technique (15) ·
   3 éditeurs Vittascience avec consignes blocs↔Python DANS LES DEUX SENS
   (16) · l'activité 2 devient une PRÉDICTION vérifiée (4 scénarios, dont la
   frontière 39/40) à confronter à l'éditeur (17 : geste de code par séance).
3. **Typographie** : « objet connecté&nbsp;? » — plus de ponctuation orpheline.
4. **Tests réels : 19/19** (Playwright mobile — verrous, encoches mixtes sur
   l'erreur volontaire « nuit », restauration bonus compris, zéro alert).
5. **File de conformité restante** (même session parallèle) : 3e_C7, 4e_C7,
   4e_C8 (+ QCMs à auditer) — prochaine vague.


## 2026-08-01 — RÈGLE D'OR N°18 « Faire pour comprendre, comprendre pour faire » (credo de Pascal, branche `fable/infra/regle-18-faire-comprendre`)

Pascal énonce la clef de voûte de la discipline, qui devient la règle-mère
des règles 1-17 :

1. **Le credo** : « Faire pour comprendre → l'élève manipule, expérimente,
   modélise, teste. Comprendre pour faire → il réinvestit pour concevoir,
   améliorer, programmer, fabriquer. » Alternance permanente entre action et
   conceptualisation — c'est l'esprit du cycle 4, et c'est déjà l'ADN de nos
   verrous expérientiels, du motif prédire→tester→reporter et des bancs de
   tests. Cette règle le rend OBLIGATOIRE et NOMMÉ.
2. **La répétition assumée** : les élèves comprennent par la répétition
   espacée des mêmes gestes sous des habits différents. Deux familles de
   gestes sont à répéter dans CHAQUE séquence qui s'y prête :
   - **les représentations schématiques** — algorigrammes et diagrammes de
     flux (construire, compléter, corriger — correction exhaustive bloc par
     bloc : entrées-sorties, traitements, décisions, tests), chaînes
     d'information/énergie (règle 6), croquis et schémas (règles 8-9) ;
   - **la programmation par blocs ET son double textuel** — le va-et-vient
     blocs ↔ code (règle 16) se pratique dans des environnements variés :
     Vittascience (standard embarqué), mBlock 5 (mBot2), Blockly, ArduBlock
     et Arduino (cartes réelles, très basse tension), Flowcode — le CONCEPT
     est invariant, l'habillage change : c'est ça qui fait comprendre.
3. **Le contrat de séquence** : chaque séquence déclare explicitement ses
   deux temps — au moins un moment « faire pour comprendre » (manipulation
   AVANT le formalisme) et un moment « comprendre pour faire »
   (réinvestissement conceptuel dans une production). Les corrections et
   synthèses nomment le concept invariant derrière le geste répété.
4. **Chantiers d'application immédiats** : l'atelier algorigramme interactif
   (diagrams.net / vérification par étapes — demandes Pascal des 30-31/07),
   la refonte du TP mBot2 (mBlock 5 ↔ Python), la marche 4e de l'arc
   variables, et les futures séquences DNB/CRCN (gabarits des skills v2).
5. Numéro 18 réservé au registre (règle n°10) ; entrée et registre dans le
   même commit.

5. **Formulation opératoire (précision exigée par Pascal — aucune place au
   doute, à l'imagination ou à l'erreur)** :
   a. TOUTE séquence comporte, dans cet ordre, un temps « FAIRE » (l'élève
      manipule un dispositif de la page ou du réel — simulateur, banc,
      curseurs, maquette TBT — AVANT toute définition) puis un temps
      « COMPRENDRE » (le concept est nommé dans un « À retenir ») puis un
      temps « REFAIRE » (réinvestissement du concept dans une production
      vérifiée). Une séquence sans ces trois temps est NON CONFORME.
   b. Toute séquence de programmation contient AU MINIMUM : un exercice de
      représentation schématique (algorigramme, diagramme de flux, chaîne
      règle 6 — construire, compléter OU corriger, correction exhaustive
      bloc par bloc) ET un exercice de code par blocs AVEC son double
      (blocs → lire le texte OU texte → observer les blocs).
   c. Répétition espacée mesurable : chaque concept-clé (variable,
      condition, boucle, chaîne, seuil, cas frontière…) apparaît dans AU
      MOINS DEUX habillages différents sur l'année du niveau (deux
      environnements parmi Vittascience, mBlock 5, Blockly, ArduBlock,
      Arduino, Flowcode, ou deux représentations différentes) — la matrice
      de couverture du lot en fait foi.
   d. Les synthèses NOMMENT le concept invariant en une phrase du type :
      « ce que tu viens de refaire avec X, tu l'avais déjà fait avec Y —
      le concept commun s'appelle Z ».
   e. Contrôle : ces quatre points entrent dans la check-list de fin de lot
      (contrôle qualité) et dans la fiche pédagogique ; un écart se justifie
      PAR ÉCRIT au journal, sinon il se corrige.
6. Numéro 18 réservé au registre (règle n°10) ; entrée et registre dans le
   même commit ; formulation opératoire ajoutée le même jour à la demande
   de précision de Pascal.
