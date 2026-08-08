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
| 19 | Consignes a l infinitif (verbe d action en tete de chaque consigne) | ChatGPT/Fable (candidate referencee par les lots Book Train) | 🕐 Candidate - numero regularise le 02/08/2026, a enteriner |
| 20 | Guides logiciels inclusifs pas-a-pas (A->H, captures, aucune etape implicite) | Fable (candidate referencee par les lots Book Train) | 🕐 Candidate - numero regularise le 02/08/2026, a enteriner |
| 21 | Convocation systematique des skills - avant toute creation d exercice et toute redaction relevant des trois themes, convoquer les skills pertinents (curriculum-assessment-cycle4, methode-fable, explicit-instruction, questioning-discussion, dnb-technologie, skill-crcn-2026, manuels-2024-mecaniques) et faire arbitrer toute etiquette de competence par _outils/data_competences.py ; aucun code pose de memoire | Pascal (decision du 02/08/2026), redaction Fable | 🔄 PR en cours |

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

## 2026-08-01 — Thème 3 · VAGUE 1 de la revue générale : conformité C7/C8 + première application PLEINE de la règle n°18 (Fable, branche `fable/theme-3/vague-1-conformite-r18-c7-c8`)

Mission de Pascal du jour : « passe en revue TOUTES les séquences du dépôt,
une par une — vérifie les trois temps FAIRE→COMPRENDRE→REFAIRE, ajoute les
représentations schématiques et les doubles blocs↔texte manquants ». Un audit
automatisé des 31 séquences (marqueurs 11/13/14/15/16/17/18) a dressé la
carte ; la file officielle du 30/07 (3e_C7, 4e_C7, 4e_C8) passe en premier,
élargie à 5e_C7 (même famille v1 « Grok » : champs muets, alert(), aucun
éditeur, aucune manipulation).

1. **Quatre refontes v2 complètes** (v1 archivées dans
   `_archive-anciennes-versions/theme-3/`, URLs inchangées, contenu et voix
   CONSERVÉS — cartouches CRCN règle 7, ancrage New York, SVG image-objet du
   4e_C8 gardés tels quels) : 3e_C7.1 « capteur confort », 4e_C7.1 « jardin
   conception », 5e_C7.1 « mini-projet du hall », 4e_C8.1 « jardin
   validation ».
2. **Les trois temps de la règle n°18, structurels** : chaque page ouvre sur
   un bloc « 🔁 Contrat de la séquence » et une activité 0 « FAIRE d'abord »
   AVANT toute définition — simulateur thermique à curseur (3e_C7, verrou :
   franchir le seuil dans les deux sens), banc météo NY (4e_C7, verrou :
   3 essais), simulateur de place à LED (5e_C7, verrou : 2 allers-retours),
   banc de tests virtuel dont la nuit de gel qui fissure l'attache (4e_C8,
   verrou : 3 tests). COMPRENDRE : les « À retenir » nomment le concept
   (seuil, contrainte/critère, règle SI, protocole). REFAIRE : réinvestissement
   vérifié sur un cas neuf (humidité des archives, jardinière de Brooklyn,
   casier de bibliothèque, critère « vent de canyon ») avec la phrase
   canonique 18d « ce que tu viens de refaire avec X… le concept commun
   s'appelle Z » dans chaque correction ET chaque synthèse.
3. **Représentations schématiques partout (18b)** : un exercice
   d'algorigramme / diagramme de flux « remettre en ordre » à correction
   exhaustive bloc par bloc dans CHAQUE séquence (alerte 3e_C7, démarche de
   projet 4e_C7, règle SI 5e_C7, protocole de validation 4e_C8 — les
   corrections nomment entrées, traitements, décisions et la boucle qui
   remonte). Doubles blocs↔texte (16/18b) : éditeurs Vittascience mixtes
   dans les deux séquences à programmation (3e_C7, 5e_C7), consignes dans
   LES DEUX SENS, verrous __exp.
4. **Rattrapage complet 11/13/14/15/17** sur les quatre pages : nav ⌂+QCM,
   colorisation des listings + légende, encoches ✔/✘ et messages gradués
   🎉/🟡/🔴, tous les champs (Bonus compris) sauvegardés
   (`seq_<code>_<slug>`), zéro alert(), chronos ⏱ par activité.
5. **4e_C9.1 complété règle 18** (édition additive) : contrat de séquence,
   exercice d'algorigramme de l'arrosage (check 6, correction bloc par
   bloc), phrase d'invariant 18d en synthèse. Régression vérifiée.
6. **Tests réels : 57/57** (suite Playwright dédiée, rapport dans
   `theme-3-…/_notes/rapport_tests_vague1_conformite_r18.md`) : verrous
   avant/après manipulation, encoches mixtes sur erreurs volontaires,
   messages gradués, restauration localStorage (champs + __exp), liens QCM,
   zéro erreur JS, zéro alert.
7. **Gouvernance** : audit et index régénérés sur l'arbre du jour ;
   4 entrées nouveautes.json. Le périmètre « autre auteur » est levé par la
   mission explicite de Pascal (les v1 Grok sont archivées, pas écrasées).
8. **File des vagues suivantes** (même mission) : Vague 2 = Thème 2
   (algorigrammes manquants dans 4e_C6.1 et 5e_C6.1, contrats règle 18,
   alert() résiduel du 4e_C6.2, compléments 3e_C9.1/5e_C9.1 côté Thème 3) ;
   Vague 3 = Thème 1 (le plus en retard : pas de nav, champs muets,
   alert(), hotlink d'image en 4e_C1.4 — coordination Codex à prévoir).

## 2026-08-01 — Thème 2 · VAGUE 2 de la revue générale : la famille C6 passe à la règle n°18 (Fable, branche `fable/theme-2/vague-2-regle-18`)

Suite de la mission « revue de toutes les séquences » (voir l'entrée Vague 1).
Les séquences C6 du Thème 2 étaient déjà conformes 11/14/15/17 ; il leur
manquait les éléments PROPRES à la règle n°18. Éditions additives, voix et
structure conservées :

1. **Contrats de séquence 🔁** (18a) en tête des quatre pages : 3e_C6.1
   « alerte graduée », 4e_C6.1 « ajuster le programme », 5e_C6.1
   « programmer le lampadaire », 4e_C6.2 « arrosage automatique » — chacun
   nomme SON temps FAIRE (relevés réels, banc, simulateur, prototype), son
   COMPRENDRE et son REFAIRE effectifs.
2. **Représentations schématiques** (18b) : 4e_C6.1 gagne l'algorigramme du
   programme corrigé (6 blocs à ordonner — les DEUX losanges de l'hystérésis,
   le bloc « ne rien changer », la boucle ; correction bloc par bloc ;
   vérificateur n°5 avec encoches ok/ko, hors barre de progression pour ne
   pas casser le « x / 4 ») ; 5e_C6.1 gagne l'exercice « chaque étape a sa
   forme » (▭/◇/↺ — dont « pas d'ellipse FIN : un lampadaire ne s'arrête
   jamais »). 3e_C6.1 avait déjà son atelier algorigramme (rien de forcé).
3. **Phrases d'invariant** (18d) dans les quatre bilans/synthèses :
   hystérésis (4e_C6.1), structure d'un programme (5e_C6.1), structure
   conditionnelle paramétrée (3e_C6.1), comparaison à un seuil (4e_C6.2).
4. **Nettoyage** : dernier alert() du Thème 2 supprimé (loquet enseignant du
   4e_C6.2 — message inline non bloquant) ; styles ok/ko ajoutés là où les
   nouvelles encoches en avaient besoin.
5. **Tests réels : 22/22** (rapport `theme-2-…/rapport_tests_vague2_regle18_C6.md`) —
   nouveaux vérificateurs (réussite ET erreur volontaire), régression des
   vérificateurs existants, barre de progression intacte, persistance après
   rechargement (debounce 600 ms respecté), zéro erreur JS, zéro alert.
6. **Reste à faire au Thème 2** (vague ultérieure, même mission) : contrats
   règle 18 des familles C4/C5 (les trois temps y EXISTENT déjà par les
   verrous — seule la déclaration manque) ; câblage 18c (matrice des
   habillages par concept) lors du prochain lot de fond.

## 2026-08-02 — Thème 2 · Audit Book Train : six règles d'or candidates + lot 4e_C4.1 Book Train en draft (Fable, branche `Fable/Thème-2/Book-Train-NYPL`)

- **Lot Book Train NYPL → Schœlcher** (`4e_C4.1_book-train/`, codes 4e_C4.1 · C4.2 · C4.4) livré en **PR draft** :
  la séquence et les schémas sont complets ; le QCM et les synthèses arrivent avant toute fusion (lot indivisible, règle n°5).
- **Six règles d'or candidates** issues de l'audit de Pascal (`_outils/REGLES_OR_CANDIDATES.md`, numéros à réserver au registre) :
  navigation cliquable + retour en haut · compétences affichées code + libellé intégral · consignes avec document de
  référence nommé · lisibilité en diagonale (une idée par ligne) · nommage élève `sujet_classe_NOM_Prenom` ·
  notation homogène des compétences.
- **Débat de notation tranché (option conservatrice)** : la convention en vigueur `4e_C4.1` (README, générateur xlsx)
  est MAINTENUE ; la proposition de format compact `4C4.1` reste consignée avec son coût chiffré (≈ 91 HTML + 126 MD)
  pour arbitrage ultérieur. Chasse immédiate : les codes NUS (`C4.1` sans niveau), ambigus par définition.
- **Décisions didactiques du lot** : le diagramme fonctionnel = fonctions techniques ↔ solutions techniques
  (2 colonnes, rappel 5e_C4.1) ; la colonne « fonction d'usage » n'apparaît qu'en 3e (schéma-bloc, 3e_C4.1) —
  déclinaison 5e/4e/3e du Book Train actée comme perspective. Les blocs fonctionnels ne contiennent QUE fonction et
  solution technique : les énergies d'entrée/sortie sont le travail de l'élève (4e_C4.2). Distinction des acteurs :
  magasinier (sous-sol) ≠ bibliothécaire du comptoir (3ᵉ étage).
- **Outillage** : `_outils/audit_conformite.py` (sondes RC-1→RC-6 réexécutables) + `_outils/AUDIT_GLOBAL.md`
  (état initial : 112 HTML · 156 MD du périmètre vivant). L'audit est un instrument permanent, pas un événement.
## 2026-08-02 - Regle d or n(o)21 : convocation systematique des skills (Fable, branche `fable/infra/regle-21-convocation-skills`)

- **Origine (clause 8)** : l etiquette de l activite 1.1 du Book Train avait ete posee de memoire
  (`4e_C4.4` au lieu de la competence-mere `4e_C4`), alors que le skill `curriculum-assessment-cycle4`
  existait precisement pour cet arbitrage (corrige en PR #117). L erreur vecue devient la regle.
- **Regle n(o)21 (decision de Pascal)** : avant toute creation d exercice et toute redaction relevant
  des trois themes, l agent convoque explicitement les skills pertinents et fait arbitrer chaque
  etiquette de competence par `_outils/data_competences.py`. Aucun code pose de memoire, aucun
  document redige sans ses skills.
- **Regularisation du registre** : les candidates n(o)19 (consignes a l infinitif) et n(o)20 (guides
  logiciels inclusifs), referencees par les lots sans reservation, prennent officiellement leurs
  numeros au tableau avec statut Candidate - a enteriner par Pascal.

## 2026-08-05 — Thème 2 · Lot réseau 5e « Le réseau de la salle techno » : fusion d'une esquisse ChatGPT + captures RÉELLES Packet Tracer (Fable, branche `fable/theme-2/lot-reseau-5e-packet-tracer`)

- **Origine** : Pascal apporte une esquisse ChatGPT de 3 séances réseaux (5e/4e/3e, Packet Tracer) avec
  consigne « profiler et faire la fusion ». Audit préalable (skills convoqués, règle n°21 ; codes arbitrés
  par `_outils/data_competences.py`) : vocabulaire de 4e/3e plaqué sur la 5e (masque, passerelle, table de
  routage dans le « vocabulaire obligatoire »), captures d'écran INVENTÉES (SVG génériques sans rapport avec
  le vrai logiciel), version « 9.0.0 » fictive, corrigés lisibles en clair dans le source, aucun élément du
  gabarit de lot. Conservé de l'esquisse : la trame débranché→simulation, le jeu du facteur, le scénario de
  l'imprimante ; tout le reste reconstruit méthode Fable.
- **Première du dépôt — captures pilotées en conditions réelles** : Fable a pris la main sur le poste de
  Pascal (pilotage à distance autorisé), construit le réseau complet dans **Cisco Packet Tracer 8.2**
  (2960, 2 PC, AP-PT SSID TECHNO-C4, portable à module WPC300N, et — demande des élèves — tablette et
  smartphone), adressé les 5 terminaux (.10→.50), validé ping filaire (<1 ms) et WiFi (57-260 ms), suivi
  l'enveloppe PDU en mode Simulation, puis sauvegardé le fichier maître `5e_reseau_local_TECHNO-C4.pkt`.
  Obstacles vécus et consignés pour les collègues : connexion Cisco obligatoire (pas de mode invité en
  8.2.0), clavier AZERTY refusant les chiffres dans le terminal (contourné par collage), fenêtre de
  connexion = fermeture du logiciel. Les captures ont ensuite été RECONSTITUÉES en 7 SVG originaux CC0
  (règles n°1 + n°20) fidèles aux écrans constatés : palette, menus de prises (24 ports), triangles,
  SSID, module WiFi, IP Configuration, transcriptions ping exactes, Event List.
- **Le lot** (`theme-2/.../5e/5e_C4.7/`) : séquence 3 séances (jeu du facteur amélioré — prénoms puis
  doublon —, topologie, guide inclusif A→H, adressage par l'analogie de la rue, preuves ping/Simulation,
  panne interdite du doublon, mini-simulateur d'enveloppe à verrou expérientiel), QCM 30 q (16/14,
  6 illustrées, 8/7/7/8 graine 5478), synthèses élève/professeur, fiche, matrice 30 lignes, SOURCES_MEDIAS,
  manifest, cartouche CRCN 5.1 niv. 2 (règle n°7), rapport de tests **Playwright 30/30 réellement
  exécutés** (verrous refus/validation compris). Garde-fou de progressivité écrit noir sur blanc :
  vocabulaire strictement 5e, masque montré comme « case qui se remplit toute seule », rendez-vous en 4e.
- **Statuts d'audit** : 5e_C4.7 passe de COUVERT (mutualisé lampadaire) à **COMPLET ET VALIDABLE**
  (dossier principal du lot) ; 5e_C4.8 reste COUVERT, mutualisé désormais vers 5e_C4.7 ; le lampadaire
  (5e_C4.1) n'est PAS modifié — il reste la première rencontre, l'atelier approfondit. OVERLAY mis à jour,
  audit et index régénérés. Note pour le lot 3e « Internet jusqu'à Sainte-Luce » : sa version B « Packet
  Tracer à confirmer » est désormais CONFIRMÉE (8.2 opérationnel sur poste enseignant).

## 2026-08-05 — RÈGLE D'OR N°22 « Concevoir guidé, comme une recette » (décision de Pascal, branche `fable/theme-2/regle-22-conception-guidee`)

- **Origine** : à la lecture du lot réseau 5e fraîchement fusionné (PR #119), Pascal constate que l'élève
  LIT le schéma du réseau (act. 2) et CONSTRUIT le montage (act. 3)… mais ne CONÇOIT jamais son propre
  schéma. Le constat devient la règle.
- **Règle n°22 (décidée par Pascal)** : dans toute séquence outillée, l'élève ne se contente ni de lire un
  schéma ni de reproduire un montage : il **CONÇOIT d'abord le sien**, dans le logiciel ou au cahier, en
  étant **exhaustivement guidé** — comme une recette de cuisine. Concrètement : ① une étape de conception
  PRÉCÈDE la lecture du document de référence, qui devient alors la CORRECTION de la conception ; ② chaque
  étape essentielle du geste logiciel a sa **capture d'écran fidèle** (règles n°1 + n°20) et son
  **explication exhaustive** — aucune étape implicite, aucun « débrouille-toi » ; ③ les choix de conception
  de l'élève (placements, liaisons, adresses…) sont les siens, questionnés et vérifiés — le guide enseigne
  le GESTE, pas la disposition ; ④ la pratique guidée est le régime par défaut (« faire pratiquer en étant
  exhaustivement guidé »), l'autonomie se gagne dans les Bonus.
- **Première application — rétrofit du lot réseau 5e (ce commit)** : l'activité 2 gagne une étape
  « 🖊 Conçois d'abord TON schéma » (4 questions-recette guidant la conception au cahier : par quoi
  commencer, combien de câbles, qui est sans fil, la forme obtenue — production enregistrée), le schéma de
  référence devient la correction de conception ; l'activité 3 précise que les placements dans Packet
  Tracer suivent le plan de L'ÉLÈVE, le guide A→H n'imposant que les gestes. Tests rejoués après rétrofit.
- **Champ d'application** : les lots 4e et 3e de la fusion réseaux (en cours) naîtront conformes ;
  audit rétroactif des trois thèmes à programmer comme pour les règles 14-18.

---

## 2026-08-07 — Lot « SOS serre » : atelier réseau 4e (4e_C4.7 · C4.8 · C4.9)

**Décision.** Le volet 4e de la fusion réseaux (esquisse ChatGPT auditée le 05/08) est livré comme
ATELIER DÉDIÉ dans `4e_C4.7`, complément de la séance 3 du « Jardin connecté » (4e_C4.1), qui n'est
pas modifié. Statuts d'audit : 4e_C4.7 passe à COMPLET ET VALIDABLE (dossier principal) ; 4e_C4.8 et
4e_C4.9 restent COUVERT, désormais mutualisés avec 4e_C4.7 (README pointeurs doubles atelier + îlot).

**Application native de la règle n°22.** L'activité 1 fait CONCEVOIR à l'élève son plan d'adressage
(recette illustrée en 4 étapes : recenser, rue, numéros uniques + .1 réservé, masque) AVANT le plan de
référence, production écrite exigée par le vérificateur ; la clinique du réseau (act. 4) porte un verrou
expérientiel (ping réussi + cas « mauvaise rue » obligatoires).

**Preuves en conditions réelles (sessions des 06-07/08/2026, pilotage à distance du poste enseignant).**
Montage `4e_serre_TECHNO-C4.pkt` construit et vérifié dans Packet Tracer 8.2 : plan .10→.100 appliqué,
passerelle 192.168.20.1, pings mesurés (<1 ms→12 ms, moy. 5 ms, TTL=128, 0% loss), panne « mauvaise rue »
192.168.21.50 réellement provoquée (Request timed out ×4, 100% loss) puis réparée, panne « liaison
coupée » (Port Status Off) reproduite. Les 9 figures du lot sont des SVG CC0 reconstitués de ces captures
(règles n°1 et n°20) et citent les valeurs mesurées telles quelles.

**Obstacles vécus (pour mémoire de méthode).** Écran de veille Windows (bureau « Screen-saver ») bloquant
l'injection d'entrées → suspension runtime puis réactivation en fin de session ; plantage de Packet Tracer
pendant une coupure du pont → règle confirmée « sauvegarder le .pkt AVANT les captures de pannes » ;
panneau Simulation recouvrant le canvas → détacher le panneau (consigné dans la synthèse professeur).

**Tests.** Suite Playwright dédiée : 36/36 verts (verrous, règle n°22, socle/CRCN en toutes lettres,
libellés officiels des 3 codes, QCM 8/7/7/8 graine 4789, images, sauvegardes).

## 2026-08-07 — Lot « Le pont numérique Martinique → New York » : atelier routage 3e (3e_C4.7 · C4.8)

**Décision.** Le volet 3e de la fusion réseaux (esquisse ChatGPT auditée le 05/08) est livré comme
ATELIER DÉDIÉ dans `3e_C4.8`, complément de la séquence-îlot « Internet jusqu'à Sainte-Luce » (3e_C4.7),
qui n'est pas modifiée. Statuts d'audit : 3e_C4.8 passe à COMPLET ET VALIDABLE (dossier principal de
l'atelier) ; 3e_C4.7 reste COMPLET ET VALIDABLE (îlot), les deux README se pointent mutuellement.
L'anomalie « Packet Tracer : comptes À CONFIRMER » du lot 02 est levée : **la version 🅱 Packet Tracer
est CONFIRMÉE en conditions réelles** (session du 07/08/2026). La fusion des trois lots réseaux
(5e → 4e → 3e) est ainsi terminée : PR #119-121 (5e), #122 (4e), présente PR (3e).

**Application native de la règle n°22.** L'activité 1 fait CONCEVOIR à l'élève son schéma à deux
réseaux (recette illustrée en 4 étapes : deux rues, un routeur par porte, la rue-pont, les commutateurs
restent) AVANT le schéma de référence, production écrite exigée ; l'activité 2 est l'activité DÉBRANCHÉE
du libellé, jouée avec la table de routage DONNÉE (les tables réelles du montage, recopiées) et exige
une justification rédigée du protocole ; l'activité 5 porte le verrou expérientiel du poste-frontière
(voyage complet Successful ET voyage « sans route » détruit à R-MQ, tous deux obligatoires).

**Preuves en conditions réelles (session du 07/08/2026, pilotage à distance du poste enseignant).**
Montage `3e_routage_MQ_NY_TECHNO-C4.pkt` construit et vérifié dans Packet Tracer 8.2 : deux réseaux
(192.168.10 / 192.168.30), deux routeurs 1941 en câble croisé sur la rue-pont 10.0.0.0/30, interfaces
allumées (Port Status On, journal « changed state to up »), routes statiques miroir
(192.168.30.0/24 via 10.0.0.2 et retour). Mesures citées telles quelles dans le lot : ping 2 timeouts
puis Reply TTL=126 ; second ping 4/4, 0% loss, 0-4 ms ; tracert 3 sauts (192.168.10.1 → 10.0.0.2 →
192.168.30.10, Trace complete) ; Event List 0.000 → 0.010 s, verdict Successful. Les 7 figures du lot
sont des SVG CC0 reconstitués de ces captures (règles n°1 et n°20).

**Obstacles vécus (pour mémoire de méthode).** Plantage de Packet Tracer pendant une coupure du pont
d'accès → le montage 3e non sauvegardé a été perdu et reconstruit : règle confirmée et appliquée ensuite,
« sauvegarder le .pkt AVANT toute manipulation risquée » ; menus d'interfaces du routeur qui se décalent
quand une prise est déjà configurée (repérage à refaire) ; PDU de simulation posé en Realtime puis
rejoué en Simulation (le panneau recouvre le canvas — consigné dans la synthèse professeur).

**Tests.** Suite Playwright dédiée : 37/37 verts (verrous act. 1/2/5, règle n°22, socle/CRCN en toutes
lettres, libellés officiels des 2 codes dont « activité débranchée, table de routage donnée », QCM
8/7/7/8 graine 3987, répartition 12/18, images, sauvegardes).

## 2026-08-08 — « SOS serre » v2 : un audit pédagogique externe appliqué en entier (4e_C4.7 · C4.8 · C4.9)

**Décision.** Pascal a soumis un audit pédagogique externe du lot 4e « SOS serre » et demandé
explicitement « plus de captures d'écran ». Les 12 priorités de l'audit sont appliquées, sans exception,
dans une refonte v2 du lot existant (aucun autre lot touché). La demande de captures est honorée
**dans le respect de la règle n°1** : cinq figures SVG originales CC0 supplémentaires ont été dessinées
d'après les enregistrements du poste enseignant (palette et choix du matériel, choix du câble droit et
du port FastEthernet0, renommage + Save As, ping de preuve vers le capteur, bascule Realtime/Simulation
et Add Simple PDU) — les PNG propriétaires servent de modèles, jamais de contenu publié. Le lot passe de
9 à 14 figures.

**Refonte pédagogique.** Passage de 3 à **4 séances de 55 min** (priorité 1 de l'audit), avec un
**passeport réseau** d'entrée : 5 questions de diagnostic des acquis de 5e, sans note, capsule de
rattrapage repliable, et une orientation automatique selon le score. Ajout d'un **mode essentiel**
(bouton persistant) qui masque référentiel, corrections et approfondissements pour les élèves que la
densité de la page met en difficulté. La preuve de C4.7 est recentrée sur **le ping vers l'objet qu'on
vient d'adresser** (`ping 192.168.20.50`), les deux autres pings devenant des preuves complémentaires.
Le diagnostic écrit reçoit une **version étayée** en six phrases guidées (J'observe / Je pense / Pour
vérifier / Le test montre / Je corrige / Je vérifie). La séance 4 se termine par un **défi SANS
tutoriel** : prouver la communication capteur↔serveur en choisissant seul son test et en le justifiant —
le vérificateur accepte le ping OU le PDU, mais exige la justification (geste de niveau 3 du CRCN).

**Corrections scientifiques et institutionnelles.** Le masque est désormais présenté comme vrai « dans
notre réseau, qui utilise 255.255.255.0 » et non comme une loi générale ; le `.1` est nommé pour ce
qu'il est, une **convention** répandue et non une règle de l'informatique ; le tableau d'adressage
précise que la passerelle est **prévue au plan mais non installée** (ce qui explique que les pings
entre voisins fonctionnent) ; les valeurs de ping sont annoncées comme « réellement observées pendant
notre simulation » ; les triangles orange sont requalifiés d'« état de préparation » plutôt que d'anomalie.
Le CRCN est restructuré : **2.3 Collaborer** et **5.2** sont les compétences que le programme 2024 cite
explicitement pour ces codes, **5.1** est présentée comme travaillée en complément (repère verbatim
conservé, règle n°7). Le **domaine 1** du socle est explicité. La version 🅰 devient « matériel réel sur
réseau **ISOLÉ** » avec un TP 2 PC + switch dédié, jamais le réseau pédagogique. La réservation DHCP
passe en approfondissement. Une note « ordinateur partagé » avertit que la sauvegarde est locale au
navigateur ET au profil.

**Trois vraies pannes, fabriquées et vérifiées.** L'audit demandait des fichiers en panne à diagnostiquer :
ils existent désormais, construits par pilotage à distance du poste enseignant (Packet Tracer 8.2, 07 et
08/08/2026) et **tous vérifiés au ping avant livraison** — `4e_serre_PANNE_A.pkt` (capteur en
192.168.21.50, 100 % loss vérifié), `4e_serre_PANNE_B.pkt` (Port Status de l'imprimante sur Off, triangle
rouge observé), `4e_serre_PANNE_C.pkt` (capteur au masque 255.255.255.240, 100 % loss vérifié). S'y ajoute
`4e_serre_DEPART.pkt` : le montage câblé avec **les quatre terminaux vidés** (IP, masque, passerelle),
pour que la compétence évaluée soit d'adresser et de prouver, pas de retrouver le 2960 dans la palette.
Le lot livre donc **cinq fichiers .pkt**. L'évaluation pratique proposée (« Serre de Rivière-Salée —
intervention n°47 », 10 min) s'appuie dessus, avec une grille à trois niveaux : les pannes et leurs
remèdes ne sont documentés **que dans la synthèse professeur**, aucun corrigé n'est publié.

**Ce qui n'a pas marché, et pourquoi c'est écrit.** La panne « doublon d'adresse IP » était prévue : elle
est **impossible à fabriquer** dans l'interface de Packet Tracer 8.2, qui refuse la saisie d'une adresse
déjà utilisée (« This address is already used in the network. ») et vide le champ. Elle a été remplacée
par la panne de masque — réelle, vérifiée, et pédagogiquement plus riche puisqu'elle oblige à lire le
masque. Le doublon reste traité à l'oral et en bonus. C'est consigné dans le rapport de tests, la
synthèse professeur et SOURCES_MEDIAS.md : **on ne déclare que ce qu'on a fait**.

**Leçons de pilotage à distance (pour les prochains lots).** Le champ IPv4 de l'onglet Config d'une
imprimante refuse le collage ET SendKeys, mais accepte l'effacement — d'où la fabrication du fichier de
départ par vidage plutôt que par ressaisie. Les classes C# créées par `Add-Type` **ne survivent pas** d'un
appel PowerShell au suivant (chaque appel est un nouveau processus) : un helper appelé depuis un second
appel échoue silencieusement et les frappes partent alors sur le canvas. Conséquence : `Ctrl+A` puis
`Suppr` sur un plan de travail sélectionne et **efface tout le montage** — c'est arrivé une fois, sans
dommage (le fichier maître n'est jamais écrasé, seul « Enregistrer sous » est utilisé), et la parade est
désormais le **triple-clic dans le champ** au lieu de Ctrl+A, plus une capture de vérification après
chaque fenêtre fermée. Les menus déroulants ne s'ouvrent pas au clic simple sur une fenêtre non active :
mettre la fenêtre au premier plan puis envoyer `Alt+F` fonctionne, là où `Ctrl+Maj+S` ne déclenche rien.

**Relecture après livraison (même PR).** Le vérificateur du défi sans tutoriel n'acceptait qu'UNE des
trois bonnes réponses (« l'un ou l'autre ») : un élève qui avait réellement lancé le ping et le déclarait
honnêtement était compté faux — exactement le contraire du message de l'activité. Corrigé : les trois
preuves honnêtes (ping, PDU, « l'un ou l'autre ») sont acceptées, seule la réponse « aucun test, les
câbles sont verts » est refusée, et un message signale à l'élève que l'autre test était valable lui aussi.
Leçon générale : **quand une activité dit « tous les chemins honnêtes mènent à la preuve », le
vérificateur doit le dire aussi** — sinon la page se contredit et punit la bonne démarche.

**Tests.** Suite Playwright étendue de 36 à **54 vérifications, 54/54 vertes** : 14 figures qui chargent,
4 onglets de séance dont la nouvelle séance 4, mode essentiel qui masque puis réaffiche, passeport qui
refuse les réponses vides, présence des cinq fichiers .pkt et validité de tous les liens `.pkt` de la page,
défi exposant bien son choix de test et sa justification, et acceptant les trois preuves honnêtes tout en refusant « aucun test » — en plus des vérifications v1 (verrous, règle
n°22, socle et CRCN en toutes lettres, libellés officiels, QCM 8/7/7/8, sauvegardes). Un SVG mal fermé
(`</g>` en trop) a été détecté par le test « les figures chargent » et corrigé avant livraison.

## 2026-08-08 — Rétrofit de l'audit externe sur l'atelier réseau 5e (5e_C4.7 · C4.8)

**Décision.** Les corrections obtenues par l'audit pédagogique externe du lot 4e ne valent pas que pour le 4e.
J'ai passé les deux autres lots réseaux (5e et 3e) au crible des mêmes critères : le 3e était largement
conforme, le 5e cumulait huit manques sur dix. Ce lot les corrige — **sans toucher au fichier `.pkt`, ni aux
figures, ni au QCM** : ce sont des ajouts de texte, un bouton et un billet d'entrée. Les preuves de la v1.0
(session Packet Tracer réelle du 05/08) restent valables telles quelles, ce qui est écrit dans le rapport de
tests. Règle de méthode qui en découle : **une correction obtenue sur un lot se propage aux lots frères** —
sinon la même erreur reste publiée deux fois.

**Apports.** Un *billet d'entrée* de 3 questions **sans note** ouvre la séance 1 (communiquer, adresser,
câble d'énergie ou d'information — les acquis de 6e), avec une capsule « Les mots de départ » de 3 minutes
pour ceux qui en ont besoin ; il oriente, il ne sanctionne pas, et le vérificateur le dit explicitement.
Un *mode essentiel* persistant masque référentiel, corrections et compléments. Le *domaine 1 du socle* est
explicité en complément du rattachement officiel D2·D4 — sans le modifier (règle n°21 : le référentiel du
dépôt fait foi) : c'est utile pour le LSU, la trace écrite de l'atelier étant évaluable côté langages.
*CRCN 2.3 Collaborer* est ajouté comme travaillée non évaluée (binôme pilote/copilote, jeu du facteur).
Un encadré *« Premier ping : ne panique pas »* nomme la fausse panne qui piège toute la classe. Les valeurs
de ping sont annoncées comme *réellement observées pendant notre simulation*, avec la précision que celles
de l'élève seront proches sans être identiques. La version 🅰 gagne une variante *TP sur réseau ISOLÉ*
(2 PC + commutateur dédié, 192.168.50.10/.20, puis doublon provoqué) — jamais le réseau pédagogique.
La synthèse professeur reçoit les notes « ordinateur partagé », « mode essentiel » et « billet d'entrée ».

**Ce qui n'a PAS été transposé, et pourquoi.** Le 5e ne parle ni de passerelle ni de masque : la nuance
« le .1 est une convention » et la relativisation du masque n'ont donc pas d'objet ici — le lot dit déjà
« la case Subnet Mask se remplit seule, tu l'étudieras en 4e », ce qui est la bonne progressivité. On ne
transpose pas mécaniquement : on transpose ce qui a un sens au niveau considéré.

**Tests.** Suite dédiée de **24 vérifications, 24/24 vertes** (rejouable) : chargement sans erreur JS,
figures, blocs règle n°4, les six apports de contenu, les trois états du mode essentiel dont la persistance
après rechargement, les trois issues du billet d'entrée (vide / 2 sur 3 / 3 sur 3), la capsule, l'indicateur
« prochaine étape », la restauration locale et l'existence du `.pkt` et du QCM.

## 2026-08-08 — Rétrofit de l'audit externe sur l'atelier routage 3e (3e_C4.7 · C4.8)

**Décision.** Deuxième volet de la propagation des corrections de l'audit externe (le premier portait sur le
5e). Le lot 3e était déjà largement conforme — il avait été écrit après plusieurs de ces leçons : premier
ping expliqué, valeurs annoncées comme réelles, convention du `.1` nommée. Il lui manquait quatre choses,
elles sont ajoutées. Comme pour le 5e, **rien n'est touché du fichier `.pkt`, des figures ni du QCM** : les
preuves de la v1 (session Packet Tracer réelle du 07/08) restent valables telles quelles.

**Apports.** Un *billet d'entrée* de 3 questions **sans note** ouvre la séquence, calibré non plus sur la 6e
mais sur les **acquis de 4e** : à quoi sert le masque, ce qu'est la passerelle, ce que prouve un ping à 0 %
de perte — exactement les trois notions dont le routage a besoin. La capsule « Je révise la 4e en 3 minutes »
fait le lien explicite avec l'atelier de la serre : *« en 4e tu as écrit l'adresse de la passerelle sans
forcément t'en servir — la serre n'avait qu'un seul réseau. Ici, la porte existe pour de bon, et elle mène
quelque part. »* C'est la progressivité du dépôt rendue lisible par l'élève lui-même.
Un *mode essentiel* persistant masque référentiel et corrections. Le *domaine 1 du socle* est explicité en
complément du rattachement officiel D2·D4 (lire une table de routage comme un document normalisé, écrire des
masques dans une notation stricte, rédiger ce qu'une preuve établit). *CRCN 2.3 Collaborer* est ajouté avec
l'argument propre à ce lot : le pont se construit à deux, les routes sont **miroir**, et une erreur d'un côté
fait échouer les deux moitiés — la meilleure démonstration de collaboration qu'un réseau puisse offrir.
La version 🅰 gagne une variante *TP sur réseau ISOLÉ* : deux commutateurs dédiés, deux groupes d'adresses,
et la constatation que **sans routeur, les deux moitiés ne se voient pas** — la preuve par le manque.

**Tests.** Suite dédiée de **25 vérifications, 25/25 vertes** : les quatre apports, les trois états du mode
essentiel dont la persistance, les trois issues du billet d'entrée, la capsule, le repère CRCN 5.1 verbatim
et le niveau 3 toujours en place, l'indicateur « prochaine étape », la restauration locale, le `.pkt` et le
QCM. La conformité v1 (37/37) n'est pas rejouée ici : elle est inchangée et reste déclarée à sa date.

## 2026-08-08 — Douze règles d'or nées de l'audit externe (n°23 à n°34) + extensions des n°3 et n°7

**Décision de Pascal.** L'audit pédagogique externe du lot 4e ne devait pas rester un correctif ponctuel.
Ses constats sont transformés en règles du dépôt, applicables à tous les thèmes et à tous les niveaux.
Douze règles nouvelles, deux extensions de règles existantes, et un rétrofit de l'existant décidé dans la
foulée. **Une règle qu'on ne peut pas vérifier est une règle qui meurt** : chacune indique donc comment on
la contrôle, et celles qui sont mécanisables sont outillées dans `_outils/`.

### n°23 — La durée annoncée est un engagement, pas une décoration
La somme des durées des activités ne dépasse jamais le temps réellement disponible dans le nombre de
séances annoncé — activités, plus lancement du logiciel, transitions, synthèse et bilan. Si ça ne rentre
pas, **on ajoute une séance** : on ne rogne pas sur les élèves lents. *Vérifiable par script.*
Origine : le seul défaut que l'audit qualifie de critique — 170 min annoncées pour 165 disponibles, l'élève
lent commençant chaque séance suivante avec du retard, et cumulant.

### n°24 — La preuve porte sur l'objet de la mission
Quand une compétence porte sur un objet précis, la preuve exigée porte sur **cet objet-là**. Les autres
tests sont des validations complémentaires, jamais le test principal. Origine : l'activité « L'adresse fixe
du capteur » faisait pinguer le serveur et l'imprimante, jamais le capteur.

### n°25 — On ne certifie pas un dépannage sans panne inconnue
Une compétence de diagnostic ne s'atteste pas par des listes déroulantes et un simulateur scénarisé : il
faut un **artefact réellement défectueux**, reçu sans savoir ce qu'il contient, et une trace écrite de la
démarche. **Clause de proportionnalité** : exigée quand le libellé officiel contient « résoudre un
problème », « diagnostiquer » ou « dépanner ». Ailleurs, surcharge sans objet.

### n°26 — Un diagnostic d'entrée avant toute séquence qui s'appuie sur l'année précédente
Dès qu'une séquence dit « tu l'as appris en 5e », elle ouvre par un diagnostic court **sans note** des
prérequis, avec capsule de rattrapage et aiguillage automatique. **Clause** : il oriente et ne sanctionne
jamais, et le vérificateur le dit à l'élève en toutes lettres — sinon le filet de sécurité devient une
épreuve d'entrée, soit l'inverse exact de l'effet recherché.

### n°27 — Ce qui n'est vrai que chez nous se dit comme tel
Toute simplification valable dans le lot mais fausse en général est **explicitement bornée** à ce cadre :
« dans notre réseau, qui utilise le masque 255.255.255.0… », jamais « les trois premiers nombres sont
toujours le réseau ». Un usage se nomme un usage, jamais une règle. **Inclut les valeurs affichées** :
toute valeur dit d'où elle vient, une valeur de simulateur s'annonce comme telle (« valeurs réellement
observées pendant notre simulation »), jamais comme une mesure du monde physique, et on précise que celles
de l'élève seront proches sans être identiques.

### n°28 — La compétence se prouve en situation ; le QCM, lui, entraîne
Le QCM reste un **entraînement aux connaissances**. Une compétence est la capacité à mobiliser des
ressources dans une situation **non strictement reproduite** (Éduscol distingue explicitement posséder et
mobiliser). Donc : toute séquence dont une compétence est « savoir faire » se termine par une tâche **sans
procédure sous les yeux**, où l'élève choisit son outil et justifie ; l'évaluation de la compétence se fait
par une **mini-situation pratique** ; le critère de réussite cesse de s'écrire « 5 bonnes réponses + fichier ».
**Clause d'implémentation, apprise à nos dépens** : quand une activité annonce que plusieurs chemins sont
valables, **le vérificateur doit tous les accepter** — sinon la page dit une chose et le code en fait une
autre, et c'est l'élève honnête qui est puni.

### n°29 — La charge de lecture est un obstacle qu'on doit pouvoir retirer
Toute séquence longue offre un **mode essentiel** : bouton persistant masquant référentiel, longues
explications, corrections, erreurs fréquentes et approfondissements. Ne restent que **mission → étape
actuelle → image → consigne → réponse → aide**, avec retour au mode complet à tout moment. **Clause** :
c'est un confort de lecture proposé à tous, jamais un parcours au rabais assigné à certains.

### n°30 — Le tableau de bord des tâches
Dès qu'une séance comporte plusieurs tâches enchaînées, la page affiche un **bandeau** qui les liste et
coche ce qui est fait (« SÉANCE 2 — ÉTAPE 3/5 · ☑ réseau construit · ☐ adresses configurées »). La barre de
progression **compte** ; ce bandeau **situe**. C'est ce dont un élève attentionnellement fragile a besoin :
savoir où il en est sans relire la page.

### n°31 — Toute production écrite exigée propose sa version étayée
Chaque fois qu'on demande de rédiger, la consigne existe en deux formes au choix : **autonome** et
**étayée** (phrases à compléter : « J'observe que… Je pense que… Pour vérifier, je… Le test montre que…
Je corrige… Je vérifie ensuite avec… »). Le niveau scientifique exigé reste **exactement le même** : on
retire l'obstacle linguistique, pas l'exigence.

### n°32 — Le triptyque de capture : où cliquer → quoi faire → ce que j'observe
Une figure montrant le résultat final ne répond pas à la question de l'élève bloqué (« où dois-je cliquer
maintenant ? »). Tout geste logiciel constituant un blocage prévisible est illustré en trois temps :
**où cliquer** (l'élément entouré dans son contexte), **quoi faire** (le geste, fléché), **ce que je dois
observer** (le résultat et ce qui prouve la réussite). On illustre les blocages, pas la routine — et
toujours sous la règle n°1 : SVG originaux reconstitués, jamais de capture propriétaire.

### n°33 — Aérer : une idée, un bloc ; une liste, des lignes *(règle proposée par Pascal)*
On ne fusionne pas deux idées distinctes dans un même pavé. Dès qu'un paragraphe change de sujet —
l'analogie, puis la précision scientifique — **il change de bloc**. Toute énumération va à la ligne, une
entrée par ligne, même courte, même dans une consigne ou une recette. L'exemple fondateur : dans l'étape 4
du lot 4e, l'analogie du masque et sa précision scientifique formaient un seul paragraphe de six lignes —
un lecteur lent y perdait le fil exactement au moment où la nuance comptait le plus. C'est une règle de
forme, mais elle décide de qui arrive au bout de la page.

### n°34 — L'audit d'accessibilité passe avant la livraison
Aucun lot n'est livré sans avoir passé la check-list d'accessibilité, et le rapport de tests dit lesquels
de ces points ont été **réellement vérifiés** — jamais « le lot est accessible ». Points contrôlés :
navigation `Tab` seule, focus toujours visible, zoom 200 % sans perte, pas de défilement horizontal sur
petit écran, `select` avec vraie étiquette, boutons compréhensibles sans la couleur, alternatives textuelles
pertinentes, emojis décoratifs ignorés du lecteur d'écran, contraste suffisant, réponses justes/fausses
jamais signalées par la seule couleur, champs de rédaction de taille suffisante, minuterie jamais bloquante.
La majorité est automatisable : l'outillage vit dans `_outils/`.

### Extension de la règle n°3 (versions 🅰/🅱/🅲)
La n°3 protège du courant (très basse tension uniquement). On lui ajoute le pendant réseau : **la version
🅰 d'un lot réseau ne branche jamais rien sur le réseau pédagogique**. Elle est soit de la pure observation,
soit un TP sur matériel **physiquement séparé**, décrit assez précisément pour être monté — ou écarté
sciemment. Le guide académique d'équipement recommande explicitement des équipements indépendants du réseau
pédagogique pour l'étude des réseaux et de l'IoT.

### Extension de la règle n°7 (CRCN observable, tracé, justifié)
Phrase de garde ajoutée : **le CRCN est le résultat d'une activité authentique, jamais une collection
d'étiquettes**. On n'ajoute pas une recherche Internet artificielle pour cocher « mener une veille » : mieux
vaut trois liens vrais que cinq domaines affichés. Corollaire institutionnel : on distingue **les CRCN que
le programme relie explicitement** au contenu et **les CRCN complémentaires réellement travaillés**, et on
le dit dans cet ordre.

### Ce qui n'a PAS été érigé en règle, et pourquoi
Le contrat de binôme nommant qui manipule quoi est une excellente modalité d'animation : sa place est dans
la fiche pédagogique, pas dans une loi du dépôt. La grille de compétences à trois niveaux appartient au
skill `curriculum-assessment-cycle4`. Le glossaire illustré pour élèves EANA est un bon gabarit, pas une
obligation. Enfin, l'audit relève un point de **couverture** et non de méthode : le **débit et ses ordres de
grandeur**, ainsi que le rôle explicite de la carte réseau, figurent au programme de la thématique réseau et
n'apparaissent dans aucun des trois lots réseaux — à vérifier dans la progression annuelle qu'ils sont
traités ailleurs.

### Outillage et état des lieux (même décision)
Un vérificateur `_outils/verif_regles_audit.py` contrôle les règles mécanisables (n°23, n°26, n°29, n°30,
n°31, n°33, n°34) sur toute séquence du dépôt, et **signale sans trancher** les règles de jugement (n°24,
n°25, n°27, n°28, n°32). Passé sur les 16 séquences du Thème 2 avant toute correction, il établit
**59 manquements mécaniques** — consignés tels quels dans `_outils/etat_des_lieux_regles_audit.md`.

Ce chiffre ne dit pas que le Thème 2 est mauvais : il dit que douze règles écrites aujourd'hui n'existaient
pas quand ces lots ont été produits. Trois d'entre elles (mode essentiel, tableau de bord des tâches,
version étayée) concentrent la majorité des lignes rouges et sont mécanisables — le rétrofit sera long mais
peu risqué. La règle n°23 sort majoritairement en « non mesurable » : la plupart des séquences n'annoncent
pas de durée par activité, ce qui n'est pas une conformité mais une **absence de donnée** à produire lot par
lot, à la main. C'est le poste le plus coûteux du chantier, et c'est écrit ici pour qu'on ne l'oublie pas.

**Chantier décidé par Pascal (08/08/2026) :** rétrofit de l'ensemble du Thème 2 aux nouvelles règles, plus
l'achèvement du lot **`4e_C4.1_book-train`** laissé en suspens — il ne comporte aujourd'hui qu'une séquence
et ses fichiers drawio, sans QCM, sans synthèses, sans fiche ni manifest, ce qui contredit la règle du lot
indivisible. Une PR par lot, la présente PR ne portant que les règles et l'outillage.

## 2026-08-08 — Le lot « Un Book Train pour la Schœlcher » est enfin complet (4e_C4.1 · C4.2 · C4.4)

**Décision.** Le dossier `4e_C4.1_book-train` contenait depuis le 05/08/2026 une séquence de très bonne
facture — analyse du Book Train de la New York Public Library au service d'un projet de modernisation de la
bibliothèque Schœlcher — mais **rien d'autre** : ni QCM, ni synthèses, ni fiche, ni matrice, ni manifest.
Elle contredisait donc la première règle de la méthode : **le lot est un ensemble indivisible**. Pascal
l'avait signalé comme « laissé en suspension ». Ce lot l'achève.

**Ce qui a été produit.** Un QCM de **30 questions** réparties 10 / 10 / 10 sur les trois codes, avec pour
chacune une explication, un exemple, l'erreur classique, la réfutation de **chaque** distracteur et un
« à retenir » ; quatre questions illustrées par les deux diagrammes fonctionnels du lot ; bonnes réponses
réparties 8/7/8/7 par `fix_r.js` (graine 4127). Synthèse élève (les cinq notions en une page A4) et synthèse
professeur (cadrage, déroulé minuté, points de vigilance, grille à trois niveaux). Fiche pédagogique, matrice
de couverture (36 notions tracées jusqu'aux questions du QCM), SOURCES_MEDIAS, README, manifest, rapport de
tests. **La séquence elle-même n'a pas été réécrite** : elle était bonne, elle a été complétée.

**Mise aux règles d'or n°23 à n°34.** Durées annoncées activité par activité — 154 min pour 165 disponibles,
marge de service comptée (n°23) ; billet d'entrée de 4 minutes **sans note** sur les acquis de 5e, avec
capsule de rattrapage et vérificateur qui dit explicitement qu'aucune note n'est prise (n°26) ; mode
essentiel persistant (n°29) ; **version étayée** pour chacune des trois productions écrites — hypothèse,
justification de format, bilan — à exigence scientifique identique (n°31) ; pavés de texte scindés (n°33) ;
**les 41 listes déroulantes de la page étiquetées** par `label` ou `aria-label`, alors qu'une bonne partie
n'était portée que par un en-tête de tableau (n°34).

**Ce que le lot ne fait pas, et qui est écrit.** La règle n°30 (tableau de bord des tâches) n'est pas
applicable en l'état : la progression de cette séquence n'utilise pas les vérificateurs numérotés des autres
lots. C'est un **écart assumé**, consigné au rapport de tests et au manifest plutôt que maquillé en
conformité. Par ailleurs, le CRCN 3.3 et 3.4 est travaillé par les activités et **pas** par le QCM, qui porte
sur les trois codes de technologie : le CRCN reste le résultat d'une activité authentique, jamais une
étiquette (règle n°7).

**Un bug de mon propre outil, trouvé en s'en servant.** Le vérificateur `verif_regles_audit.py` signalait
comme « sans étiquette » des champs qui en avaient une : son expression régulière s'arrêtait à l'attribut
`id` et ne voyait donc jamais un `aria-label` placé après. Le compte réel du Thème 2 n'est pas de 59
manquements mais de **54**. Leçon : un outil de contrôle se vérifie lui-même sur un cas connu-bon avant
qu'on lui fasse confiance.

**Où vit ce correctif — et pourquoi il n'est pas là où on l'attendrait.** Il devait accompagner la PR des
règles (#127). Il a été poussé quelques minutes APRÈS sa fusion : il est donc resté orphelin sur la branche,
et `main` a un moment porté l'outil bogué et le chiffre de 59. Le correctif voyage finalement avec le présent
lot, et l'état des lieux est recalculé ici. C'est consigné parce qu'un chiffre publié puis corrigé mérite de
dire quand et pourquoi il a changé.

**Statuts d'audit.** `4e_C4.2` et `4e_C4.4` passent de COUVERT PAR UNE SÉQUENCE MUTUALISÉE à **COMPLET ET
VALIDABLE** : ils disposent désormais d'un atelier dédié avec séquence, QCM, synthèses et évaluation.
Le Thème 2 compte 19 codes complets au lieu de 17.

**Tests.** Suite Playwright dédiée : **32/32 verts** — blocs règle n°4, figures, cohérence entre le nombre de
questions annoncé et le QCM livré, les quatre états du billet d'entrée, les cinq états du mode essentiel dont
la persistance, une version étayée par production écrite, l'étiquetage de tous les champs, et les onze
vérifications du QCM.

## 2026-08-08 — Rétrofit des trois lots « dépannage » (C5) et échec instructif du bandeau automatique

**Décision.** Premier rétrofit de masse après l'écriture des règles n°23 à n°34 : les trois séquences de la
compétence C5 (5e « dépanner le lampadaire », 4e « dépanner le jardin », 3e « SOS station : réparer ») sont
mises au **mode essentiel** (n°29) et leurs champs de saisie **entièrement étiquetés** (n°34). Un outil,
`_outils/retrofit_regles_audit.py`, fait ce travail répétitif et **annonce précisément ce qu'il a modifié**.

**L'échec qu'il faut raconter.** J'ai voulu mécaniser aussi la règle n°30 — le tableau de bord des tâches.
Le script savait lire la correspondance séance → activités (`const par`) et cocher les tâches faites ; tout
fonctionnait techniquement. Mais les libellés étaient **trompeurs** : les séquences du dépôt ne nomment pas
leurs activités. Leurs `<h2>` portent le titre de la *séance*, et les titres intermédiaires sont des
fragments du genre « c) Je conclus mon inspection ». Le bandeau annonçait donc « Séance 1 — étape 1/1 ·
☐ c) Je conclus mon inspection » : incompréhensible, et **pire que pas de bandeau du tout pour l'élève
attentionnellement fragile qu'il vise**. Le code a été retiré du script, et la raison écrite dans sa
documentation. La règle n°30 reste entière — elle se fera à la main, lot par lot, avec des libellés rédigés.

Leçon de méthode : **mécaniser une règle de forme est facile, mécaniser une règle de sens ne l'est pas.**
Un outil qui produit une aide fausse est plus nuisible qu'un outil qui refuse de la produire. Le script le
dit maintenant en toutes lettres : il fait le travail bête et refuse de faire semblant de faire l'autre.

**Trois étiquettes rectifiées à la main.** Sur le lot 3e, trois listes déroulantes sont insérées *dans une
phrase* (« la panne se situe entre le dernier point de test ▾ et le premier point ▾ »). L'étiquette
automatique y reprenait le libellé de l'exercice précédent — techniquement conforme, sémantiquement faux
pour qui écoute la page. Elles ont été réécrites une par une.

**Ce qui reste sur ces trois lots, et qui est écrit dans le rapport d'état :** les durées par activité (n°23),
le diagnostic d'entrée du lot 4e (n°26), le tableau de bord (n°30) et les versions étayées des productions
écrites (n°31) — 9 zones de rédaction rien que sur le lot 3e. Ce sont des travaux de rédaction, pas de
script.

**Tests.** Vérification navigateur des trois pages : aucune erreur JS, bouton présent, corrections
réellement masquées en mode essentiel, bascule d'onglet intacte. Vérificateur de règles : n°29 ✔ et n°34 ✔
sur les trois.

## 2026-08-08 — Rétrofit des lots « programmation » (C6), et une erreur d'emballage à consigner

**Ce qui a été fait.** Les trois séquences C6 bâties sur le gabarit maison — 5e « programmer le lampadaire »,
4e « ajuster le programme du jardin », 3e « programmer l'alerte » — ont reçu le **mode essentiel** (n°29) et
l'**étiquetage de leurs champs** (n°34). Vérification au navigateur des trois pages : aucune erreur JS,
corrections réellement masquées, bascule d'onglet intacte.

**La quatrième séquence n'a PAS été touchée, et c'est délibéré.** `sequence_algorigrammes_dnb.html`
(3e_C6.2, statut EXISTANT À AMÉLIORER) repose sur un autre gabarit : pas de barre d'outils, pas de
`restore()`. L'outil s'apprêtait à y poser le CSS du mode essentiel **sans le bouton ni la bascule** — du code
mort, et une séquence qui aurait eu l'air traitée sans l'être. Le garde-fou l'a arrêté et l'a écrit à
l'écran. Ce lot mérite mieux qu'un rustinage : il lui manque une situation déclenchante, une problématique,
une mission, une synthèse et un référentiel affiché. C'est une banque d'entraînement au brevet, pas une
séquence au sens du gabarit — sa reprise sera un lot à part entière, comme l'a été le Book Train.

**L'erreur d'emballage, et pourquoi elle est écrite ici.** Ce travail sur C6 devait faire l'objet de sa
propre PR. Il est en réalité parti **dans la PR #129**, celle du rétrofit C5 : en amendant le commit C5 pour
y corriger l'outil, un `git add -A` a balayé un arbre de travail qui portait déjà les modifications C6. La
PR #129 annonçait trois séquences et en a livré six. Rien n'est perdu ni cassé — les six fichiers sont
corrects et vérifiés — mais **le journal du dépôt doit dire ce qui s'est réellement passé**, sinon la trace
ment. Deux règles de méthode en découlent, pour moi comme pour les autres agents :

- avant tout `git commit --amend`, **relire `git status`** : un amendement n'est pas un ajout innocent, il
  absorbe tout ce qui traîne dans l'arbre de travail ;
- ne jamais changer de branche avec des modifications non commitées en cours sur une autre — la
  parade est de commiter d'abord, quitte à réécrire ensuite.

**Ce qui reste sur les lots C6 :** durées par activité (n°23), diagnostic d'entrée du 5e (n°26), tableau de
bord des tâches (n°30) et versions étayées des productions écrites (n°31). Travaux de rédaction, lot par lot.

**Une PR fermée sans fusion.** La PR #130 avait été ouverte depuis la branche des règles, déjà fusionnée en
#127 et jamais supprimée. Son contenu était intégralement dans `main` et sa fusion aurait ramené un état
ancien du dépôt. Fermée, branche supprimée. Règle : **une branche fusionnée se supprime le jour même**,
sinon elle finit par ressurgir en fausse PR.

## 2026-08-08 — Rétrofit des séquences-îlots C4, et deux de mes propres lots pris en faute

**Décision.** Dernière vague de rétrofit mécanisable : les neuf séquences de la compétence C4 — cinq
séquences-îlots (5e lampadaire, 4e jardin connecté, 3e énergie station, 3e station d'alerte cyclonique, 3e
Internet jusqu'à Sainte-Luce) et les quatre ateliers dédiés — reçoivent ce qui leur manquait. **Les seize
séquences du Thème 2 disposent désormais du mode essentiel**, chacune vérifiée au navigateur : aucune erreur
JS, corrections réellement masquées, onglets intacts.

**Deux de mes propres lots étaient en faute sur la règle n°23, celle que j'ai écrite ce matin.** Le
vérificateur ne fait pas de favoritisme, et c'est bien la preuve qu'il sert à quelque chose.

- L'atelier **3e « pont numérique »** annonçait **169 minutes pour 165 disponibles** — et sa séance 1
  cumulait à elle seule 59 minutes de contenu. Les durées ont été rééquilibrées : conception 25 min,
  poste-frontière 20 min, construction du pont 45 min, preuves 25 min, simulation 20 min. Total 139 minutes,
  marge de service comprise. Ce ne sont pas des chiffres inventés pour faire passer le test : c'est
  l'aveu que les premières estimations étaient optimistes, notamment sur l'activité 3, annoncée comme
  « séance entière » sans laisser une minute pour lancer le logiciel.
- L'atelier **4e « SOS serre »** dépassait de 5 minutes — mais pour une autre raison : il comptait comme
  activité de l'élève une **note destinée à l'enseignant** (« évaluation pratique courte (10 min…) »). La
  note a été reformulée ; elle dit la même chose sans se faire passer pour une activité. Le lot tombe à
  205 minutes pour 220 disponibles.

**Aération.** Six pavés de plus de 110 mots ont été scindés dans les deux ateliers réseaux — dont un de
244 mots. C'est la règle n°33, celle que Pascal a proposée, appliquée à mes propres pages.

**Ce qui reste, et qui ne sera jamais fait par un script.** Le compte du Thème 2 passe de 50 à **33
manquements**, et ceux-là se concentrent sur les trois règles de rédaction : le **diagnostic d'entrée**
(n°26) sur les trois séquences-îlots qui invoquent l'année précédente sans vérifier les acquis, le **tableau
de bord des tâches** (n°30) qui demande de nommer les tâches de chaque séance, et la **version étayée**
(n°31) — plus de quarante zones de rédaction sur l'ensemble du thème. La n°23 reste « non mesurable » sur les
séquences-îlots, qui n'annoncent aucune durée par activité : absence de donnée, pas conformité.

**Ménage.** Les **59 branches déjà fusionnées** du dépôt ont été supprimées, en application de la règle née
de la fausse PR #130. Quatre branches non fusionnées sont conservées telles quelles, dont deux relèvent d'un
autre agent.

---

## 08/08/2026 — Lot 3e_C6.2 « L'auto-test de la station » : écrire, et non plus lire

### Le libellé, pris au mot

Le dossier `3e_C6.2` contenait une banque d'entraînement DNB de bonne facture : 30 exercices
interactifs, 13 schémas inline, 32 aides rédigées. L'audit de couverture la signalait depuis le début
comme « une banque d'entraînement plus qu'une séquence ». Mais le vrai problème n'était pas là.

Le libellé officiel du code ne dit pas « lire des algorigrammes ». Il dit :

> **Programmer un algorithme lié à une nouvelle fonctionnalité.**

Le verbe est **programmer** ; l'objet est une **nouvelle fonctionnalité**. La banque fait *lire* et
*interpréter* — excellent entraînement au brevet, mais ce n'est pas la compétence. Compléter la banque
aurait produit une conformité de façade. Il fallait écrire la séquence qui manquait.

### Un scénario abandonné avant d'être écrit

Le plan initial prévoyait une **alerte graduée** : seuil de vigilance, seuil d'alerte, temporisation
pour ignorer les rafales isolées. J'ai relu 3e_C6.1 avant de commencer — elle couvrait déjà ce
scénario. Écrire le lot prévu aurait donné à l'élève l'impression de refaire la même chose deux fois,
et au dépôt deux séquences qui se marchent dessus.

D'où la répartition, désormais explicite au README du dossier :

- **3e_C6.1** — déterminer les données utilisées et produites : on **lit** ;
- **3e_C6.2** — ici : on **écrit**, à partir d'un besoin exprimé en français ;
- **3e_C6.3** — modifier et tester : on **retouche**.

*Leçon de méthode : lire les séquences voisines fait partie de la conception, pas de la relecture.*
Le coût de cette vérification est de quelques minutes ; celui de l'oubli aurait été un lot entier.

### La fonctionnalité retenue

L'**auto-test quotidien** de la station d'alerte cyclonique. Chaque matin à 7 h, la station teste ses
quatre organes — anémomètre, gyrophare, sirène, liaison radio —, compte les défauts et envoie **un
seul** message au gardien. La fonctionnalité est nouvelle, utile, et impossible à écrire sans un
compteur initialisé avant la boucle, une boucle, et une décision unique après la boucle.

Elle porte en outre un cas limite qui n'est pas un ornement : la **défaillance silencieuse**. La
liaison radio est à la fois un organe testé et le canal du message. Si elle tombe, le message est
calculé correctement — et ne part jamais. La classe découvre là qu'un système d'alerte doit prouver
qu'il est **vivant**, et pas seulement signaler qu'il va mal.

### Une séquence née conforme

C'est la première du dépôt écrite d'emblée sous les règles n°22 à n°34, au lieu d'être rétrofitée :
durées annoncées par activité avec marge de service (144 min pour 165), billet d'entrée sans note qui
oriente et ne sanctionne pas, mode essentiel, bandeau de tâches aux libellés écrits à la main, version
étayée pour chacune des cinq productions écrites, aération, étiquetage de tous les champs.

Le vérificateur la donne **7 règles sur 7 au vert**, et la suite `tests_3e_C6.2.py` — livrée avec le
lot, pas seulement décrite — passe **22 tests sur 22**. Écrire conforme s'est révélé nettement moins
coûteux que rétrofiter : la conformité rétroactive demande de comprendre du code déjà écrit, la
conformité native ne demande que de suivre une liste.

### Ce qui n'est pas déclaré conforme

Quatre points de la check-list n°34 n'ont pas été vérifiés automatiquement : l'impression A4, le
contraste mesuré, la lecture par un vrai lecteur d'écran, et le zoom navigateur à 200 %. Ils sont donc
déclarés **non vérifiés** au rapport de tests. La barre qualité du dépôt interdit de dire « accessible »
à la place de « ces points-là ont été testés ».

### La banque héritée : requalifiée, pas jetée ni rustinée

`sequence_algorigrammes_dnb.html` et son QCM de 17 questions sont **conservés tels quels**. Ils
deviennent la ressource d'appui de la séance 1 — on y pioche l'exercice utile au moment où il l'est.
Leur statut passe de « séquence incomplète » à **ressource d'entraînement**, ce qui est la vérité. Ils
resteront signalés en échec sur la règle n°29 : le rétrofit a refusé de les traiter, faute de gabarit
maison, et je n'y pose pas un mode essentiel à moitié câblé pour faire tomber un compteur. L'écart est
écrit au rapport de tests et à l'état des lieux — assumé, pas en attente.

### Trois défauts de mes propres lots, corrigés au passage

En vérifiant mes liens, j'ai trouvé chez moi ce que je cherchais ailleurs :

- le lien « ⌂ Accueil » de la séquence 3e_C6.2 et celui de `qcm_book-train.html` remontaient **cinq**
  niveaux au lieu de quatre : ils ne menaient nulle part ;
- `sequence_4e_C4.1-C4.2-C4.4_book-train.html` n'avait **aucune barre de navigation** — la règle n°11
  n'était pas respectée dans un lot que j'ai livré moi-même ;
- le filtre par compétence du QCM Book Train proposait C4.1 et C4.2, mais **pas C4.4**, alors que le
  QCM contient dix questions sur ce code.

*Leçon : un lien mort ne se voit pas à la relecture, il se voit à l'exécution.* La suite de tests du
lot vérifie désormais les liens de navigation ; c'est ce qui a permis de trouver le premier, et le
premier a fait chercher les autres.

### Le bilan chiffré

`3e_C6.2` passe de **EXISTANT À AMÉLIORER** à **COMPLET ET VALIDABLE** : le Thème 2 compte
**20 codes complets** au lieu de 19. Le dépôt totalise 17 séquences analysées pour 33 manquements
mécaniques inchangés — la nouvelle n'en apporte aucun.

---

## 08/08/2026 — Les versions étayées du Thème 2 : 67 blocs écrits à la main

### Pourquoi celles-ci d'abord

Trois chantiers restaient ouverts après le lot 3e_C6.2. Les versions étayées passent devant les
autres pour une raison simple : ce sont elles qui décident **qui arrive au bout de la page**. Un
élève qui sait ce qu'il faut répondre mais bute sur la mise en phrase rend une copie vide — et on
lit cette copie vide comme une lacune scientifique. C'est exactement l'inverse de ce qui s'est
passé.

Elles manquaient sur **treize séquences**, c'est-à-dire sur les plus fréquentées du dépôt.

### Ce qui a été fait

**67 zones de rédaction** ont reçu leur version étayée, écrite **une par une** à partir de la
consigne réelle. Le principe de la règle n°31 est tenu à la lettre : le niveau scientifique exigé
reste identique, seule l'entrée en écriture est facilitée. Chaque amorce est construite pour ne
pouvoir être complétée que par une réponse juste et complète.

Un exemple, sur la justification du CAN en 3e_C4.3 :

> La grandeur réelle (la pression) est continue&nbsp;: entre deux valeurs, il existe ____.
> Le CAN, lui, ne peut distinguer que ____ paliers&nbsp;: il est obligé de ____.
> La donnée numérique est donc une approximation, parce que ____.

L'élève ne peut pas remplir cela sans avoir compris la différence entre continu et discret. On lui
a retiré l'angoisse de la page blanche, pas le raisonnement.

### L'outil, et ce qu'il refuse de faire

Deux fichiers dans `_outils/` :

- `amorces_versions_etayees.py` — **le texte**, écrit à la main, indexé par fichier et par
  identifiant de zone. C'est le vrai travail ;
- `poser_versions_etayees.py` — **la pose**, et rien d'autre. Il refuse d'écrire un fichier dont
  toutes les amorces n'ont pas été rédigées, il annonce les zones qu'il a laissées de côté, et il
  ne repasse jamais sur un fichier déjà traité.

C'est la suite directe de la leçon du 08/08 au matin sur le bandeau de tâches : *mécaniser une
règle de forme est facile, mécaniser une règle de sens ne l'est pas.* La bonne réponse n'est pas
« pas d'outil », c'est « un outil qui pose ce qu'un humain a écrit ».

### Le textarea qui n'en était pas un

La séquence 3e_C6.1 contient un `textarea` nommé `clTa` : c'est l'**éditeur de code Python**, pas
une zone de rédaction. Y proposer des phrases à compléter aurait été absurde — et le vérificateur,
lui, l'avait bien compté comme une zone de rédaction de plus.

*Leçon : un compteur ne sait pas ce qu'il compte.* Le script l'a écarté et l'a dit en clair dans
son compte rendu, plutôt que de le traiter en silence ou de faire semblant de ne pas l'avoir vu.

### Les tests

Treize séquences rechargées au navigateur, et pour chacune : aucune erreur JavaScript, chaque bloc
posé **immédiatement après sa zone de rédaction**, au moins deux amorces par bloc contenant toutes
un espace à compléter, bloc **resté visible en mode essentiel** — c'était le point à vérifier, un
étayage masqué par le mode qui allège serait exactement le contraire du but — et aucun défilement
horizontal introduit. **13 séquences, 0 défaut, 67 blocs.**

### Le bilan chiffré

Manquements mécaniques du Thème 2 : **33 → 20**. La règle n°31 ne compte plus aucun échec sur le
thème. Restent les diagnostics d'entrée (n°26), les bandeaux de tâches (n°30), le mode essentiel de
la seule banque DNB héritée (écart assumé), et la règle n°23 en «&nbsp;?&nbsp;» sur les
séquences-îlots — une absence de donnée, pas une conformité.

---

## 08/08/2026 — Les tableaux de bord des tâches : 79 libellés écrits à la main

### La règle que j'avais échoué à mécaniser le matin même

C'est la deuxième tentative sur la règle n°30. La première, au matin, avait produit des lignes
comme «&nbsp;Séance 1 — étape 1/1 · ☐ c) Je conclus mon inspection&nbsp;»&nbsp;: l'extraction
automatique prenait les `<h2>` pour des noms d'activité alors qu'ils portent le titre de la
SÉANCE, et les titres intermédiaires sont des fragments de phrase. J'avais retiré le code et
écrit au journal que *mécaniser une règle de forme est facile, mécaniser une règle de sens ne
l'est pas*.

La bonne réponse n'était pas «&nbsp;pas d'outil&nbsp;». C'était **un outil qui pose ce qu'un
humain a écrit** — exactement la forme retenue pour les versions étayées quelques heures plus tôt,
et qui a bien fonctionné.

### Ce qui a été fait

**79 tâches** réparties sur **quatorze séquences**, chacune avec un libellé rédigé à la main. Un
libellé dit ce que l'élève **fait**, à l'infinitif, en une ligne lisible d'un coup d'œil&nbsp;:

> Séance 3 — Prouver le voyage — étape 1 sur 2
> ☐ Rapporter les preuves : ping, TTL et tracert
> ☐ Mener les deux expériences du poste-frontière

Le titre de l'activité disait «&nbsp;Les preuves du voyage&nbsp;»&nbsp;: c'est un thème. Le bandeau
dit «&nbsp;rapporter les preuves&nbsp;»&nbsp;: c'est une action qu'on peut cocher. La différence
tient en un verbe, et c'est toute la règle.

La barre de progression **compte**&nbsp;; ce bandeau **situe**. C'est ce dont a besoin l'élève
attentionnellement fragile&nbsp;: savoir où il en est sans relire la page.

### Les deux gardes du poseur

`poser_bandeaux_taches.py` refuse d'écrire un fichier dans deux cas&nbsp;:

- si la liste des tâches écrites ne recouvre pas **exactement** les boutons `data-check` présents
  dans la page — un libellé orphelin afficherait une case qu'on ne peut jamais cocher, et une
  tâche oubliée en cacherait une à faire&nbsp;;
- si une clé de séance n'existe pas dans la page.

Les deux gardes ont servi pendant l'écriture&nbsp;: elles ont attrapé deux séquences (4e_C6.1 et
5e_C6.1) où un bouton de vérification supplémentaire est **imbriqué dans une activité existante**,
et non à la suite. L'ordre des tâches du bandeau suit donc l'ordre de lecture de la page, pas la
numérotation des boutons.

### Une leçon de méthode sur mes propres tests

La suite de tests a d'abord échoué sur une séquence… qui était **conforme**. Mon test lisait la
séance active dans `data-panel`, alors que la séquence 3e_C6.2 — celle que j'ai écrite ce matin —
identifie ses onglets par `id="tab-s1"`. Le défaut était dans le test, pas dans la page.

*Un test qui échoue ne prouve pas que la page est fausse&nbsp;: il prouve qu'il y a un désaccord.*
Il faut chercher lequel des deux a tort avant de corriger quoi que ce soit. Le test lit désormais
les deux conventions.

Corollaire à retenir pour la suite&nbsp;: le dépôt a **deux façons** de nommer un onglet de séance.
Ce n'est pas grave, mais tout code qui les parcourt doit accepter les deux.

### Les tests

Quinze séquences rechargées au navigateur, et pour chacune&nbsp;: aucune erreur JavaScript, bandeau
visible, mention «&nbsp;étape 1 sur N&nbsp;» présente, **chaque onglet de séance affichant son
propre bloc non vide**, case qui passe bien à ☑ quand l'activité est validée, bandeau **resté
visible en mode essentiel**, et aucun défilement horizontal introduit. **15 séquences, 0 défaut.**

### Le bilan chiffré

Manquements mécaniques du Thème 2 : **20 → 6**. Il ne reste que les cinq diagnostics d'entrée
(n°26) et le mode essentiel de la seule banque DNB héritée, écart déjà assumé. Le compteur était à
**61** ce matin.

---

## 08/08/2026 — Diagnostics d'entrée : quatre manquements sur cinq n'existaient pas

### Ce que j'ai trouvé en allant vérifier

Le tableau de bord annonçait cinq séquences à traiter au titre de la règle n°26. Avant d'écrire
cinq billets d'entrée, je suis allé lire les cinq passages incriminés. **Quatre n'invoquaient
rien du tout.**

Le vérificateur cherchait «&nbsp;en 5e&nbsp;», «&nbsp;en 4e&nbsp;», «&nbsp;l'an dernier&nbsp;»
n'importe où dans le fichier. Il comptait donc comme prérequis&nbsp;:

- un **distracteur** de liste déroulante — «&nbsp;…parce que plier est interdit en 4e&nbsp;»,
  qui est une réponse *fausse*, proposée pour être écartée ;
- une **correction repliée** qui raconte la progression du cycle — «&nbsp;en 5e la chaîne était
  fournie, en 4e on la complétait&nbsp;: en 3e, tu l'as élaborée&nbsp;» ;
- une **annonce de la suite** — «&nbsp;tu la verras de près en 4e et en 3e&nbsp;», dans une
  séquence de 5e&nbsp;: c'est l'inverse d'un prérequis ;
- le **niveau de la séquence elle-même** — «&nbsp;en 4e, on ne reçoit plus le protocole&nbsp;:
  on le PROPOSE&nbsp;», dans une séquence de 4e.

### La correction

`regle_26` ne lit plus que le **texte de consigne**&nbsp;: les `option` et les corrections
repliées sont retirées avant analyse. Et elle ne retient qu'un niveau **antérieur** à celui de la
séquence, déduit de son nom de fichier — citer son propre niveau n'est pas invoquer un prérequis,
citer un niveau postérieur encore moins.

*Leçon, qui rejoint celle de ce matin sur le textarea de l'éditeur de code&nbsp;: un compteur ne
sait pas ce qu'il compte.* Un vérificateur qui signale trop est aussi dangereux qu'un vérificateur
qui laisse passer&nbsp;: il fait produire du travail inutile, et il finit par ne plus être cru.
La bonne réaction devant un tableau de bord n'est pas d'exécuter la liste, c'est d'aller voir.

### Le seul manquement réel

`sequence_4e_C4.1-C4.9_jardin_connecte.html` écrit noir sur blanc «&nbsp;En 5e vous avez appris à
lire UN objet simple&nbsp;; cette année, vous lisez un système complet&nbsp;» — et n'offrait aucun
filet à l'élève pour qui la 5e est loin.

Elle a reçu un **billet d'entrée sans note** de trois questions (capteur, batterie dans la chaîne
d'énergie, fonction contre solution technique), avec **capsule de rattrapage de 5e** qui s'ouvre
d'elle-même en cas de besoin, et un message qui oriente sans jamais sanctionner. Il ne compte pas
dans les cinq activités validées&nbsp;: il coche seulement sa ligne au bandeau de tâches.

### Une convention harmonisée au passage

Le dépôt avait **deux façons** de désigner l'onglet de séance actif — `data-panel` partout, sauf
dans la séquence 3e_C6.2 écrite ce matin, qui lisait `id="tab-s1"`. C'est ce qui avait fait échouer
ma suite de tests tout à l'heure.

Plutôt que d'apprendre aux tests à vivre avec les deux, j'ai **supprimé la divergence à la
source**&nbsp;: 3e_C6.2 lit désormais `data-panel` comme tout le monde, et son `majProgress()`
appelle `majTaches()` — une seule porte d'entrée, comme dans les quatorze autres séquences.

*Un test qui doit connaître deux conventions signale surtout qu'il ne devrait y en avoir qu'une.*

Corollaire tenu&nbsp;: dans les deux séquences qui en ont un, le billet d'entrée est **validé dès
qu'il est répondu**, pas dès qu'il est juste. Un diagnostic qui exige la perfection pour se cocher
n'est plus un diagnostic, c'est une épreuve d'entrée — exactement ce que la clause de la règle
n°26 interdit. 3e_C6.2 était dans ce cas&nbsp;: corrigé.

### Le bilan chiffré

Manquements mécaniques du Thème 2 : **6 → 1**. Il ne reste que le mode essentiel de la banque
d'entraînement DNB héritée, écart assumé depuis le lot 3e_C6.2. Le compteur était à **61** ce
matin.

---

## 08/08/2026 — L'entraînement DNB, réécrit plutôt que rustiné

### Pourquoi une réécriture

Le dossier 3e_C6.2 contenait une banque de 30 exercices d'algorigrammes, héritée d'une
organisation antérieure du dépôt. Elle est **bonne sur le fond** : les notions y sont justes, les
exercices bien choisis, les sujets de type brevet pertinents.

Mais elle n'est pas bâtie sur le gabarit maison — aucune sauvegarde locale, pas de mode essentiel,
pas de barre d'outils — et surtout, **ses corrections donnent la bonne réponse sans dire pourquoi
les trois autres sont fausses**.

C'est ce dernier point qui a décidé de la réécriture. Au brevet, les distracteurs sont conçus pour
être plausibles. Un élève qui sait *pourquoi* B est faux ne se fera pas prendre par une variante de
B ; un élève qui sait seulement que C est juste sera perdu dès que l'énoncé changera d'habit. Les
90 réfutations rédigées sont le vrai contenu de cette page — bien plus que les 30 questions.

### Ce que la page est, et ce qu'elle n'est pas

Elle **entraîne**. Elle ne revendique **aucun code** du référentiel, et le dit à l'élève dès son
badge. La couverture de 3e_C6.2 est assurée par « L'auto-test de la station », qui fait *écrire* un
algorithme — le verbe du libellé officiel.

Nommer honnêtement ce qu'on produit évite la tentation inverse : gonfler une bonne ressource
d'entraînement au rang de séquence pour cocher une case d'audit.

### Un défaut de qualité trouvé par le test, pas par la relecture

Le premier tirage plaçait **15 bonnes réponses sur 30 en position C**. Un élève répondant C au
hasard aurait eu la moyenne sans rien lire — et l'aurait remarqué avant nous.

Relire trente exercices ne fait pas voir ce déséquilibre : il n'apparaît qu'en comptant. Le
générateur applique désormais une répartition déterministe (8/8/7/7), comme `fix_r.js` le fait pour
les QCM, et un test vérifie que les quatre positions sont servies.

*Leçon : certaines propriétés d'un lot ne se voient qu'à l'échelle du lot entier.* La relecture
exercice par exercice est nécessaire ; elle n'est pas suffisante.

### Encore un test qui mentait

Le contrôle «&nbsp;le mode essentiel laisse les exercices visibles&nbsp;» a échoué alors que la
page était correcte&nbsp;: il interrogeait le premier exercice de la page, appartenant à une manche
que le test venait lui-même de masquer en changeant d'onglet. C'est la **deuxième fois
aujourd'hui** qu'un test accuse à tort une page conforme.

Le réflexe est désormais acquis, et mérite d'être écrit&nbsp;: devant un test rouge, on cherche
lequel des deux a tort **avant** de toucher au code.

### La banque héritée, laissée en place — et ce que ça coûte

`sequence_algorigrammes_dnb.html` et son QCM ne sont **ni modifiés ni déplacés**. Quatorze fichiers
du dépôt y font référence, dont la séquence 3e_C6.1 et plusieurs fichiers générés&nbsp;: les
déplacer casserait ces liens et sortirait du périmètre de ce lot.

Conséquence assumée, et qu'il faut nommer plutôt que masquer&nbsp;: l'ancienne banque reste
signalée sans mode essentiel, et c'est **le dernier manquement mécanique du Thème 2**. Il ne
disparaîtra pas par un correctif technique — il disparaîtra le jour où Pascal décidera d'archiver
ces deux fichiers dans `_archive-anciennes-versions/`, ce qui est une décision de gouvernance et
lui revient.

### Le lot, et ce qu'il ne contient pas

Page d'entraînement, fiche pédagogique, rapport de tests, suite de tests, manifest, générateur
reproductible (`_outils/dnb_exercices.py` porte les 30 exercices écrits à la main,
`_outils/dnb_build.py` et `_outils/dnb_gabarit.html` les mettent en page — régénération vérifiée
identique à l'octet près).

Pas de QCM séparé&nbsp;: la page **est** l'entraînement, un QCM ferait doublon. Pas de synthèses&nbsp;:
le rappel de cours est intégré, et celles de 3e_C6.2 couvrent les mêmes notions. Ces deux absences
sont des choix, pas des oublis — et c'est pour cela qu'elles sont écrites ici et au manifest.

**21 tests Playwright exécutés, 21 passés.**

---

## 08/08/2026 — Archivage de la banque DNB d'origine : le Thème 2 à zéro manquement

### Une erreur de comptage de ma part, d'abord

J'avais écrit la veille au soir que «&nbsp;quatorze fichiers du dépôt font référence&nbsp;» à la
banque d'origine, et j'en avais conclu que l'archivage serait coûteux. C'était faux&nbsp;: quatorze
fichiers la **mentionnent**, mais seuls **quatre liens cliquables** pointaient vers elle, dans trois
fichiers — dont `index.html`, qui est régénéré.

J'avais compté les occurrences d'une chaîne de caractères au lieu de compter les liens. C'est la
même erreur que celles de la journée, sous une troisième forme&nbsp;: *un compteur ne sait pas ce
qu'il compte*. Ici elle m'a fait recommander à Pascal de reporter une décision qui coûtait en
réalité une demi-heure.

### Ce qui a été fait

Les deux fichiers sont déplacés — `git mv`, **contenu non modifié** — vers
`_archive-anciennes-versions/C6-comprendre-et-modifier-un-programme-associe/3e_C6.2-banque-dnb-v1/`,
avec un README qui dit ce qu'ils sont, pourquoi ils ont été remplacés, et ce qui a changé au moment
du déplacement.

Les deux liens réels sont redirigés vers l'entraînement DNB. La synthèse professeur, le README du
dossier et les deux manifests sont mis à jour. Index et audit régénérés.

### Deux effets de bord qu'il fallait aller chercher

`_outils/heritees.json` porte la règle d'or n°12 dans sa propre note&nbsp;: «&nbsp;une entrée
disparaît quand le remplaçant est livré et l'ancienne version déplacée dans
`_archive-anciennes-versions/` (même commit)&nbsp;». Les deux entrées ont donc été retirées **dans
ce commit**, comme la règle l'exige — pas plus tard, pas dans un autre lot.

`_outils/build_qcms.py` **génère** `qcm_algorigrammes_dnb.html` à partir de `banks_a.ALGO_DNB`. Sans
rien faire, la prochaine régénération l'aurait **ressuscité dans le dossier actif**, à côté de son
remplaçant — et le manquement serait revenu sans que personne comprenne pourquoi. La cible du job
pointe désormais l'archive.

*Leçon&nbsp;: archiver un fichier généré ne se fait pas avec `git mv`.* Il faut suivre le fil
jusqu'à ce qui le fabrique, sinon l'archivage ne tient qu'un seul cycle de régénération.

### Le Thème 2 à zéro

**61 manquements mécaniques au réveil, 0 ce soir.** Le détail est dans
`_outils/etat_des_lieux_regles_audit.md`.

Ce qui reste est ce qui doit rester&nbsp;: la règle n°23 en «&nbsp;?&nbsp;» sur les
séquences-îlots, parce qu'annoncer une durée par activité demande de savoir ce que les classes
mettent réellement — c'est le jugement de Pascal, pas le mien. Et les règles n°24, 25, 27, 28 et 32,
que le vérificateur signale sans jamais trancher, par construction.

### Deux liens cassés signalés au Thème 1

Le contrôle des liens de tout le dépôt en a trouvé deux, **hors de mon périmètre**&nbsp;:

- `theme-1/…/5e_C2.1/sequence_5e_C2_shenzhen_station_velos.html` → `qcm_5e_C2_shenzhen_station_velos.html` (absent)&nbsp;;
- `theme-1/…/5e_C1.1/sequence_5e_C1.1_donnees_tableur_2026.html` → `synthese_eleve_5e_C1.1.html` (absent).

Je ne les corrige pas — ce sont des lots d'un autre auteur, et la garde-périmètre refuserait la PR.
Ils sont écrits ici pour que quelqu'un les prenne.

---

## 08/08/2026 — Sept règles d'or nées d'un audit externe de la page d'accueil (n°35 à n°41)

Pascal a fait auditer `index.html` par un regard extérieur. L'audit a **lu le code**, pas seulement
la page&nbsp;: j'ai vérifié ses cinq affirmations techniques avant de les reprendre, et **les cinq
étaient exactes** — `ctext` récupéré mais jamais affiché (ligne 171), troncature à 110 caractères
(ligne 193), aucun `:focus-visible`, aucun `<main>`, aucune `meta description`, et une dépendance à
Google Fonts.

Les trente-quatre règles existantes disent comment **produire un lot**. Aucune ne disait comment le
dépôt **se présente**. Ces sept-là couvrent ce manque.

### n°35 — Un code n'apparaît jamais seul

Tout code affiché porte sa **formulation complète**, jamais tronquée, jamais renvoyée à un autre
document. Cela vaut pour les neuf compétences de fin de cycle comme pour les 114 repères. Trois
lignes de texte valent mieux qu'un code que le lecteur doit aller décoder ailleurs.

### n°36 — On ne fait jamais passer une codification interne pour une nomenclature officielle

Le BO fournit les thèmes, les neuf compétences de fin de cycle, les connaissances, les capacités et
les repères de progressivité. Notre numérotation `5e_C4.1` est une **codification de classement
interne**, issue de notre transcription et de la structuration Nathan. Toute page qui affiche ces
codes le dit, et distingue par écrit **la référence normative** (BO n°9 du 29/02/2024) de **la
codification opérationnelle**.

C'est la règle la plus institutionnelle du recueil, et la plus urgente&nbsp;: l'index affirmait
« les 9 compétences C1-C9 du BO » — vrai pour C1-C9, **faux pour les 114 repères**.

### n°37 — L'interface montre des ressources pédagogiques, pas des fichiers

Manifest, rapport de tests, matrice, `SOURCES_MEDIAS.md`, suites de tests&nbsp;: des outils de
gouvernance. Ils restent dans le dépôt et restent accessibles, mais **hors de la vue pédagogique**,
et le nom affiché est un **nom pédagogique** — jamais le nom physique, qui reste dans le lien.

C'est notre méthode qui avait créé le problème&nbsp;: le lot indivisible impose ces fichiers, et
l'index les servait à l'enseignant comme s'ils étaient des ressources de classe.

### n°38 — Une seule source de vérité, un seul générateur

On ne ressaisit jamais dans une page un intitulé qui existe dans les données. Le chemin est
toujours&nbsp;: **référentiel de données → générateur → page à jour**. Deux copies d'un même texte
finissent par diverger, et c'est celle qu'on lit qui est fausse.

### n°39 — Un compteur compte ce que son étiquette annonce

Si une page affiche « 7 ressources », l'utilisateur doit trouver sept choses utilisables. Le
compteur de l'index annonçait **287 ressources** en comptant les manifests et les rapports de
tests&nbsp;; il en annonce **135 pédagogiques**, et l'étiquette le dit.

*Cette règle est née cinq fois dans la même journée*&nbsp;: un `textarea` d'éditeur de code compté
comme production écrite, quatre manquements de règle qui n'existaient pas, quinze bonnes réponses
sur la même position, quatorze références qui n'étaient que quatre liens, et ce compteur.
**Un compteur ne sait pas ce qu'il compte&nbsp;: c'est à nous de le lui dire.**

### n°40 — Hors ligne d'abord

Une page qui se revendique utilisable hors ligne n'a besoin d'**aucune ressource distante**. Nos
séquences promettent « page unique hors ligne » et appelaient toutes une police distante&nbsp;: une
contradiction entre ce qu'on promet et ce qu'on livre, visible dans un collège au réseau filtré.
L'index n'appelle plus rien&nbsp;; les séquences suivront lot par lot.

### n°41 — L'index est tenu au même niveau que ce qu'il indexe

Focus clavier visible, structure sémantique, information jamais portée par la seule couleur,
`meta description` renseignée. Une porte d'entrée moins accessible que les salles qu'elle dessert,
c'est une porte fermée.

---

## Ce que j'ai refusé de reprendre de l'audit, et pourquoi

**La vue « progression annuelle » en HTML.** Nous avons déjà les classeurs `_progressions/` avec
leur moteur d'imprévus. Une progression HTML en parallèle serait un **second référentiel de
progression**&nbsp;: deux sources, divergence garantie. Si on la veut, elle devra être *générée
depuis les classeurs* — c'est la règle n°38 appliquée à elle-même.

**Les 114 reformulations « Je suis capable de… ».** L'idée est bonne, mais 114 textes écrits à côté
du texte réglementaire, sans rien qui garantisse leur cohérence, c'est exactement ce que la n°38
interdit. À faire **uniquement sur les codes qui ont une séquence**, où la reformulation vient du
lot et reste vraie. Sur un code « À CRÉER », ce serait une promesse.

**Un septième statut « En expérimentation ».** Nous en avons déjà six dans `audit_couverture.csv`.
Le problème n'était pas leur nombre, c'est que l'index **ne les montrait pas** — il affichait
« — » pour tout ce qui manquait. Ils sont désormais tous affichés, avec leur puce. Ajouter un
statut que personne ne maintiendrait aurait dégradé les cinq autres.

---

## Ce que la mise en œuvre a appris

**Le titre pédagogique se construit par jeton, pas par expression régulière.** Ma première version
retirait le code par motif&nbsp;: `qcm_5e_C4.1-C4.8_lampadaire_intelligent.html` donnait
« QCM — 8 lampadaire intelligent ». Le motif coupait `C4.8` en deux et laissait un `8` orphelin. La
version retenue découpe le nom en jetons et écarte ceux qui *sont* un code — plus simple, et juste.

**L'ordre des tests de classement compte.** `atelier_procedes.svg` était annoncé comme une
« Activité »&nbsp;: le motif `^atelier` gagnait avant le contrôle d'extension. Les médias sont
désormais écartés en premier — ils se lisent **dans** une séquence, ils ne sont pas des ressources
autonomes.

**Contrainte de gouvernance à connaître.** `_outils/` appartient au Thème 2&nbsp;: le générateur
d'index ne peut donc pas être modifié depuis une branche de Thème 1. Toute évolution de l'interface
passe par une PR Thème 2, les contenus par leur thème. C'est pour cela que cette PR précède les
lots de Thème 1 à venir&nbsp;: ils s'afficheront d'emblée dans la bonne interface.

**Vingt contrôles automatiques** accompagnent ces règles (`_outils/tests_index.py`) — dont la
présence des 114 formulations, l'absence de troncature, l'absence de fichier de gouvernance dans la
vue pédagogique, l'absence de ressource distante, et l'accessibilité clavier. **20 / 20.**

---

## 08/08/2026 — Lot Shanghai 5e_C3 : le premier lot du Thème 1, et la première séquence hors ligne

### Ce que le lot ouvre

La compétence **C3 — caractériser et choisir un objet ou un système technique** n'avait **aucune
ressource sur les trois niveaux**&nbsp;: onze codes vides. Ce lot en couvre les quatre de 5e.

Il exécute le `PLAN_LOT_SHANGHAI.md` qui attendait dans le dossier depuis une session précédente,
et réutilise le fichier de données simulées qui y dormait — vingt colonnes, trois solutions.

### L'ordre des codes n'est pas celui des numéros

C3.1 → C3.2 → C3.4 → **C3.3 en dernier**. On ne peut pas *choisir* avant d'avoir caractérisé, situé
dans le cycle de vie et mesuré. C3.3 n'est pas une compétence parmi d'autres&nbsp;: c'est
l'aboutissement de la séquence, et la placer ailleurs qu'à la fin l'aurait vidée de son sens.

### Le fil qui tient la séquence

La **masse** explique la consommation en séance 1 (18 contre 165 Wh/km), pèse sur trois étapes du
cycle de vie en séance 2, puis explique la distance de freinage en séance 3 (1,6 contre 5,8 m).

Quand une même grandeur explique plusieurs phénomènes, l'élève cesse d'empiler des faits
séparés&nbsp;: il tient un modèle. C'est ce qu'on cherche, et c'est rare.

### Le retournement final

L'activité 5 change le besoin — 400 kg sur 150 km hors centre-ville — et la bonne réponse devient
S2, après trois séances où S1 gagnait. Ce n'est pas un piège&nbsp;: c'est la compétence C3.3
elle-même. **Une solution technique n'est jamais bonne dans l'absolu, elle est bonne pour un besoin
donné.** La synthèse professeur insiste sur la nuance à poser&nbsp;: la première réponse n'était
pas fausse, elle répondait à un autre besoin.

### Première séquence du dépôt sans aucune ressource distante

La règle n°40, écrite ce matin à partir de l'audit de l'index, s'applique ici **dès la
naissance**&nbsp;: ni la séquence ni le QCM n'appellent Google Fonts. Pile système, et rien
d'autre. Elles fonctionnent à l'identique derrière un filtrage de collège — ce que nos autres
séquences promettent sans le tenir encore.

Les anciennes suivront lot par lot. C'est un rétrofit mécanisable et peu risqué, mais il ne sera
pas fait à la sauvette dans une PR de contenu.

### Deux défauts trouvés par les tests

**Le champ `img` du QCM était un tableau, pas un objet.** Ma fonction rangeait le couple
`(source, alternative)` tel quel, alors que le gabarit attend `{src, alt}`. Les trois questions
illustrées n'auraient affiché **aucune image**, et rien ne se voyait à la lecture du source&nbsp;:
seulement à l'exécution.

**Un test qui interrogeait l'affichage au lieu du document.** Le contrôle des blocs de la règle n°4
utilisait `innerText`, qui ignore les panneaux de séance masqués&nbsp;: il déclarait absents des
blocs bien présents. C'est la **troisième fois de la journée** qu'un test accuse à tort une page
conforme. Le réflexe est acquis, et il valait la peine d'être appris&nbsp;: devant un test rouge,
chercher lequel des deux a tort avant de toucher au code.

### Le bilan

Quatre codes passent de « À CRÉER » à **COMPLET ET VALIDABLE** (5e_C3.1) et **COUVERT PAR UNE
SÉQUENCE MUTUALISÉE** (C3.2, C3.3, C3.4). Le dépôt compte **21 codes complets** au lieu de 20, et
41 « à créer » au lieu de 44.

Vérificateur&nbsp;: **7 règles sur 7**. Tests&nbsp;: **27 sur 27**.

---

## 08/08/2026 — Lot Hangzhou 4e_C3 : écrire les critères au lieu de les recevoir

### Le plan a servi à quelque chose

Ce lot a été précédé d'un `PLAN_LOT_HANGZHOU.md` écrit et commité **avant** la première ligne de
contenu, avec un avertissement en toutes lettres&nbsp;: *ne pas refaire Shanghai avec d'autres
véhicules*.

La marche à monter est précise&nbsp;: en 5e, le cahier des charges et le protocole sont
**fournis**, l'élève applique. En 4e, l'élève **écrit** les caractéristiques et **choisit** les
instruments. Un lot 4e qui comparerait des vélos sur des critères donnés ne couvrirait rien de
nouveau.

C'est la même vigilance qui avait sauvé le lot 3e_C6.2 ce matin, quand la relecture de la séquence
voisine avait révélé que le scénario prévu était déjà traité. *Écrire le piège avant de commencer
coûte dix minutes et évite de refaire un lot.*

### Le dispositif qui force la compétence

La situation déclenchante ne donne **aucun critère**&nbsp;: le maire a laissé une phrase — «&nbsp;qu'ils
durent, qu'ils ne coûtent pas un bras, qu'on puisse les réparer, et qu'on ne les retrouve pas au
fond du canal&nbsp;» — un relevé de pannes et un budget. Il n'y a rien à appliquer&nbsp;: il faut
construire.

Le vérificateur de l'activité 1 exige d'ailleurs un cahier des charges **contenant au moins quatre
chiffres**&nbsp;: on ne valide pas sur des adjectifs.

### Le tableau est construit pour que le classement se déplace

Quatre flottes, dix-sept colonnes. Sur le seul CO₂ de fabrication, F4 gagne largement (58 contre
210&nbsp;kg éq. pour F3). Rapporté au kilomètre offert sur toute la durée de vie, l'ordre se
confirme mais les **écarts changent de nature**&nbsp;: F3 n'est plus «&nbsp;3,6 fois pire&nbsp;»
mais «&nbsp;2,3 fois&nbsp;», et F1 se rapproche beaucoup de F4 alors qu'elle émet 1,7 fois plus à
la fabrication.

Et F3, la plus agréable à l'usage, celle qui roule le plus (3600&nbsp;km/an), termine
**dernière** — parce qu'elle cumule une empreinte lourde et une vie courte. C'est le moment où une
intuition d'usage cède devant un calcul, et il mérite d'être joué à voix haute en classe.

### Une nuance rare, posée explicitement

La séquence écrit qu'un **bilan carbone est un ordre de grandeur, pas une valeur exacte**&nbsp;:
deux méthodes de calcul donnent des résultats différents. On peut affirmer un écart net entre deux
solutions&nbsp;; on ne peut pas affirmer un gramme.

Les élèves ne rencontrent presque jamais cette nuance, et elle vaut pour toutes les données
environnementales qu'ils liront ailleurs. C'est la règle n°27 appliquée à un domaine où elle
manquait.

### Un test écrit pour un autre lot a servi ici

Quatre réfutations de distracteurs étaient trop courtes — «&nbsp;Aucun rapport.&nbsp;», «&nbsp;Une
seule suffit.&nbsp;» Le contrôle qui exige plus de vingt caractères par réfutation, écrit pour le
lot précédent, les a rejetées. Il avait raison&nbsp;: une réfutation de trois mots n'enseigne rien.

*Un contrôle utile survit à son lot d'origine.* C'est un argument de plus pour livrer les suites de
tests avec les lots plutôt que de les décrire dans un rapport.

### Une confusion de fichiers, nommée plutôt que subie

`donnees_velos_hangzhou_simulees.csv` existait déjà dans le dépôt, sous 5e_C1.3, produit pour un
autre usage&nbsp;: ses colonnes ne portent ni durée de vie, ni matière recyclée, ni bilan carbone.
J'ai donc produit `donnees_flottes_velos_hangzhou_simulees.csv`, distinct — et je l'ai **écrit dans
SOURCES_MEDIAS**, pour qu'on ne croie pas à un doublon dans six mois.

### Le bilan

Trois codes quittent «&nbsp;À CRÉER&nbsp;». Le dépôt compte **22 codes complets** et **38 à
créer** (contre 44 ce matin). Le C3 est couvert en 5e et en 4e&nbsp;; restent les quatre codes de
3e, qui demanderont de **définir** un protocole et non plus seulement de choisir l'instrument.

Vérificateur&nbsp;: **7 sur 7**. Tests du lot&nbsp;: **28 sur 28**. Contrôles de l'index&nbsp;:
**20 sur 20**.

---

## 08/08/2026 — Lot Shenzhen 3e_C3 : la compétence C3 achevée sur les trois niveaux

### La progression, enfin lisible

| Niveau | Ce que l'élève reçoit | Ce qu'il produit |
|---|---|---|
| 5e — Shanghai | solutions **et** critères **et** protocole | il applique |
| 4e — Hangzhou | les solutions seules | il écrit les critères, choisit les instruments |
| 3e — Shenzhen | **un besoin seul** | il **établit la liste** et **définit** le protocole |

Les onze codes du C3 sont couverts. Ce n'est pas un empilement de trois lots&nbsp;: c'est une
progression dont chaque marche retire un appui.

### La contrainte d'usage qui conditionne tout le lot

**Le tableau des six solutions ne se distribue pas en séance 1.** S'il est donné, l'élève lit une
liste au lieu de l'établir, et 3e_C3.1 n'est pas couvert.

C'est écrit au plan, au README, à la fiche pédagogique, à la synthèse professeur et à l'OVERLAY
d'audit — cinq endroits, parce qu'un lot se transmet et que cette contrainte ne se devine pas en
ouvrant les fichiers. *Une consigne d'usage qui n'est écrite qu'une fois n'est pas transmise.*

### Trois verrous de rédaction au lieu d'un

L'activité 1 refuse de valider tant que la liste ne nomme pas les trois familles&nbsp;; l'activité 3
exige un protocole en cinq étapes numérotées&nbsp;; l'activité 5 une note chiffrée sur les trois
piliers. En 3e, la production écrite **est** la preuve, pas un complément — les vérificateurs le
disent au lieu de le supposer.

### Le retournement de la séance 4

Seul le climatiseur atteint à lui seul les 9 °C que la mesure des élèves a rendus nécessaires. Mais
ventilation + extracteur + réduction du nombre de machines donne 11,5 °C, pour un coût
d'installation deux fois moindre et une **consommation nette négative**.

*On ne choisit pas toujours dans une liste&nbsp;: parfois on compose.* C'est ce qui sépare vraiment
la 3e de la 4e, et la synthèse professeur recommande de laisser un groupe le trouver plutôt que de
l'annoncer.

### Le pilier social, sous une forme inconfortable

Renoncer à deux serveurs, c'est retirer un service à des usagers réels. La séquence le pose ainsi
plutôt que de réduire le développement durable à l'écologie. C'est une occasion rare de travailler
le **D3 du socle** dans un cours de technologie, sur un arbitrage authentique et non sur un débat
abstrait.

### Un défaut que je reproduis

Quatre réfutations de distracteurs étaient trop courtes — «&nbsp;Aucun lien.&nbsp;», «&nbsp;Rien ne
le garantit.&nbsp;» Le même contrôle les avait déjà attrapées dans le lot de 4e.

Le motif est net, et il vaut d'être nommé&nbsp;: **quand une réponse fausse me paraît évidente,
j'écris une réfutation courte** — or c'est exactement là qu'un élève a besoin d'explication. Le test
compense un biais que ma relecture ne voit pas, parce que ma relecture partage le biais.

### Une seule figure, volontairement

Ce lot ne contient qu'un SVG, là où les précédents en avaient deux ou trois. Une planche de
solutions illustrées aurait **donné les réponses de l'activité 1**. La sobriété iconographique est
ici une décision pédagogique, pas une économie&nbsp;: elle est écrite au manifest et à
SOURCES_MEDIAS pour qu'on ne la prenne pas pour un manque.

### Le bilan

Quatre codes quittent «&nbsp;À CRÉER&nbsp;». Le dépôt compte **23 codes complets** et **34 à
créer** — contre 44 ce matin. Vérificateur&nbsp;: **7 sur 7**. Tests du lot&nbsp;: **28 sur 28**.
Contrôles de l'index&nbsp;: **20 sur 20**.

---

## 8 août 2026 — Lot Shenzhen 5e_C2.1 · C2.2 : « la station de vélos et tout ce qui l'entoure »

Premier lot du **C2**. Il achève une séquence qui existait déjà — 7,4 ko, huit titres justes, un
scénario qui tient — mais qui était **un plan rédigé en HTML, pas une séquence au gabarit maison**.
Aucun vérificateur, aucune zone de rédaction, aucune barre d'outils, aucun mode essentiel.

### Une estimation qui n'a pas ouvert le fichier n'est pas une estimation

J'avais annoncé à Pascal que ce lot serait «&nbsp;un achèvement, pas une création — le travail le
plus court des trois&nbsp;». C'était faux, et je l'ai dit sur la foi d'un statut d'audit et d'un nom
de fichier, **sans ouvrir le fichier**. Le lot final fait 43 tests et huit fichiers neufs.

### Ce que la séquence installe

Un seul geste, pris dans les deux sens&nbsp;: regarder à l'extérieur de l'objet. En séance 1 l'élève
**recense** les interacteurs&nbsp;; en séances 2 et 3 il **remonte** des formes aux décisions prises
pour ces interacteurs-là.

La situation déclenchante a été choisie contre une confusion tenace&nbsp;: la station fonctionne mal
alors que **rien n'est cassé**. Tant qu'un élève croit qu'une panne suppose une pièce cassée, la
notion d'interacteur reste décorative.

### La frontière de niveau, qui est le vrai risque de ce lot

«&nbsp;Décrire l'expérience de l'utilisateur&nbsp;» est au programme de **4e**. En 5e, on recense et
on repère. Le glissement est facile et il coûterait le lot suivant&nbsp;: si la 5e raconte déjà le
vécu de l'usager, la 4e n'a plus rien à apprendre.

La frontière est donc écrite **à l'élève**, dans la carte du référentiel («&nbsp;ce que tu feras en
4e, et pas encore ici&nbsp;»), à la fiche, à la synthèse professeur, et le QCM y consacre sa
trentième question. Un repère de progression qui n'est écrit que pour l'enseignant ne tient pas la
progression.

### Un compteur qui comptait quatre choses et en annonçait trois

La barre de progression annonçait «&nbsp;0 / 4 activités&nbsp;» pour trois activités et un billet
d'entrée. Or le billet **oriente sans note**&nbsp;: il ne se valide pas comme une activité. Le
compteur annonce désormais 3 et compte 3 (règle n°39).

### Des durées qui ne remplissaient pas la séance

Le vérificateur acceptait 94 minutes annoncées pour 165 disponibles — la règle n°23 ne contrôle que
le dépassement. Mais 71 minutes sans emploi ne sont pas une marge, ce sont des minutes que
l'enseignant devra inventer devant sa classe. Relevé à **149 minutes**. Une durée qui ne remplit pas
la séance n'est pas une durée, c'est un vœu.

### Ouvrir un fichier en écriture le vide avant d'écrire

Un script de correction a détruit le QCM en cours de fabrication&nbsp;: `open(p, 'w')` **tronque
immédiatement**, et l'erreur qui a suivi n'a pas laissé le fichier intact — elle l'a laissé à zéro
octet. Le générateur livré (`_generation/build_qcm.py`) n'ouvre son fichier de sortie qu'une fois
toutes ses vérifications passées.

Ce n'était pas une perte grave — le fichier était régénérable, précisément parce que la règle n°38
avait été suivie. C'est le meilleur argument pour elle&nbsp;: **une source de vérité et un
générateur, c'est aussi ce qui rend un accident réparable en une commande.**

### Un fichier hérité qu'on garde sans l'utiliser

`solutions_station_shenzhen_simulees.csv` compare quatre variantes de station sur six critères.
C'est un geste de la compétence **C3**, pas du C2. Il n'est donc pas utilisé par la séquence — et
c'est **écrit** au SOURCES_MEDIAS plutôt que masqué. Un fichier présent et inexpliqué se lit comme
un oubli&nbsp;; un fichier présent et expliqué se lit comme une ressource.

### Un lien cassé de moins

La séquence pointait depuis des mois vers `qcm_5e_C2_shenzhen_station_velos.html`, qui n'existait
pas. Il existe. Reste la deuxième dette signalée&nbsp;: `synthese_eleve_5e_C1.1.html`.

### Le bilan

Deux codes quittent «&nbsp;À CRÉER&nbsp;». Le dépôt compte **24 codes complets** et **33 à créer**.
Vérificateur&nbsp;: **7 sur 7**. Tests du lot&nbsp;: **43 sur 43**. Contrôles de l'index&nbsp;:
**20 sur 20**.
