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

---

## 8 août 2026 — Correction du lot 5e_C2 : j'avais remplacé une dimension du programme par une que j'avais inventée

### Ce qui s'est passé

Le référentiel du code `5e_C2.2` dit&nbsp;: «&nbsp;Repérer et expliquer les choix de conception dans
les domaines de l'**ergonomie** et de la **sécurité**, ou en lien avec des objectifs de
**développement durable**.&nbsp;»

J'ai écrit, dans la carte du référentiel de la séquence&nbsp;: «&nbsp;ergonomie, sécurité et
**esthétique**&nbsp;». Puis j'ai construit l'activité 2 sur ce trio, et la question 18 du QCM en a
fait la bonne réponse à «&nbsp;les trois domaines sont…&nbsp;».

Le **plan hérité du lot**, écrit par quelqu'un d'autre, disait juste&nbsp;: «&nbsp;liés à
l'ergonomie, à la sécurité et au développement durable&nbsp;». J'ai substitué en silence, sans le
remarquer et sans le signaler.

### Pourquoi c'est plus grave qu'une coquille

Une coquille se voit. Celle-ci était **cohérente**&nbsp;: trois domaines, trois définitions, des
exemples justes, un piège pédagogique bien construit autour de l'esthétique. L'ensemble se tenait
parfaitement — autour d'une donnée fausse.

C'est exactement le cas que la règle n°36 vise, et je ne l'avais lue que dans un sens. Je vérifiais
qu'un **code de classement interne** ne soit pas présenté comme une nomenclature officielle. Je ne
vérifiais pas que la **formulation** d'une compétence soit celle du référentiel. Or réécrire la
formulation, c'est fabriquer du contenu institutionnel — plus discrètement, et plus profondément.

**Règle n°36, second volet&nbsp;: la formulation d'une compétence se recopie, elle ne se reformule
pas.** Si la reformulation aide l'élève, elle s'ajoute à côté du texte, elle ne le remplace pas.

### Ce que les 43 tests n'ont pas vu

Ils passaient tous. Aucun ne comparait le contenu enseigné au texte du référentiel&nbsp;: ils
vérifiaient la mécanique, la cohérence interne, l'accessibilité — tout sauf la seule chose qui était
fausse. **Une suite de tests vérifie ce que son auteur soupçonne**, et je ne me soupçonnais pas de
réécrire le programme.

Un test a été ajouté&nbsp;: il lit la bonne réponse de la question «&nbsp;Trois domaines&nbsp;» et la
compare à la formulation attendue. C'est le premier contrôle de ce dépôt qui porte sur un **contenu
institutionnel** plutôt que sur un comportement. Il faudra en écrire d'autres&nbsp;: le vérificateur
`_outils/verif_regles_audit.py` gagnerait à confronter les cartes de référentiel des séquences aux
formulations de `_outils/data_competences.py`.

### Ce que la correction change, pédagogiquement

Le développement durable **convient mieux** à ce lot que l'esthétique. La station de Shenzhen, son
air salin martiniquais, ses pièces remplaçables&nbsp;: la matière, l'énergie et la durée de vie sont
lisibles à l'œil nu sur cet objet. L'activité 2 gagne deux questions et une exigence — au moins un
des quatre choix relevés doit relever du développement durable — et la figure une cinquième ligne.

L'esthétique reste dans la séquence, nommée pour ce qu'elle est&nbsp;: une vraie question de
conception, qui n'est pas l'un des trois domaines de ce code. Le dire ainsi vaut mieux que
l'effacer&nbsp;: c'est un cas exemplaire de la règle n°27 — **ce qui n'est vrai que chez nous se dit
comme tel**.

### Le bilan

Séquence, QCM, deux synthèses, fiche, matrice, deux READMEs, manifest, figure SVG et suite de tests
corrigés. **45 tests sur 45.** Vérificateur&nbsp;: 7 sur 7. Index&nbsp;: 20 sur 20.

---

## 8 août 2026 — Le balayage : trois cartes de référentiel du Thème 1 remises au texte

Après la correction du lot 5e_C2, j'ai écrit un contrôle qui compare la **carte de référentiel de
chaque séquence du dépôt** aux formulations de `_outils/data_competences.py`. Onze écarts. Aucun
n'était une substitution comme celle du C2&nbsp;: **tous étaient des troncatures**.

Ce qui ne les rend pas anodines, parce que **ce qu'on coupe en premier, c'est la parenthèse** — et
c'est souvent la parenthèse qui fixe le niveau.

- `4e_C3.3` disait «&nbsp;à partir d'un protocole&nbsp;»&nbsp;; le référentiel dit «&nbsp;à partir
  d'un protocole **donné**&nbsp;». Ce mot est toute la différence avec la 3e, qui **définit** le
  protocole.
- `4e_C3.2` avait perdu «&nbsp;efficacité énergétique&nbsp;» et surtout «&nbsp;**et arrêter un
  choix**&nbsp;». La séquence faisait bien arrêter le choix — en séances 4 et 5 — mais la carte
  annonçait la seule séance 2. La couverture était vraie&nbsp;; la carte la sous-déclarait.
- `5e_C3.1` écrivait «&nbsp;les formes d'énergie&nbsp;» au singulier là où le référentiel met le
  pluriel. Minuscule, et corrigé quand même&nbsp;: on ne choisit pas les endroits où l'on recopie
  fidèlement.

### Ce que je ne corrige pas, et pourquoi

Huit écarts restent, tous dans les lots hérités du **Thème 2** — dont `5e_C4.2` et `5e_C4.5`, qui
omettent «&nbsp;l'organisation de la chaîne d'énergie **étant fournie**&nbsp;», c'est-à-dire
exactement la frontière 5e/4e&nbsp;; et `3e_C4.6`, qui écrit «&nbsp;(texte, image, **son**)&nbsp;»
là où le référentiel dit «&nbsp;(texte, image, **nombre**)&nbsp;».

Ce sont des lots existants d'un autre auteur, et ils sont hors du périmètre d'une branche
`theme-1`. Signalés à Pascal, non touchés.

### La suite mécanique

Le contrôle a sa place dans `_outils/verif_regles_audit.py`, comme huitième règle vérifiable&nbsp;:
il viendra par une branche `infra`, `_outils/` étant hors du périmètre du Thème 1.

Une leçon d'outillage vaut d'être notée&nbsp;: ma **première** version du contrôle a signalé dix-neuf
écarts, dont la quasi-totalité étaient faux. Elle indexait les formulations par le seul code
(`C2.1`) au lieu du couple niveau + code, si bien qu'elle comparait la 5e au texte de la 3e. Le
motif est le même que celui de la règle n°26 en juillet et des trois suites de tests qui accusaient
des pages conformes&nbsp;: **devant un contrôle qui accuse largement, douter du contrôle avant de
douter du contenu.**

---

## 8 août 2026 — Règle d'or n°42 : la formulation d'une compétence se recopie, elle ne se reformule pas

**Second volet de la règle n°36.** Le premier volet interdit de faire passer un **code de
classement interne** pour une nomenclature officielle. Celui-ci interdit de réécrire le **texte**
d'une compétence.

La reformulation est la plus discrète des deux, et la plus profonde&nbsp;: elle ne se signale par
aucune anomalie de forme. Le lot 5e_C2 a enseigné «&nbsp;esthétique&nbsp;» là où le programme dit
«&nbsp;développement durable&nbsp;», et quarante-trois tests l'ont laissé passer.

Si une reformulation aide l'élève, elle **s'ajoute à côté** du texte&nbsp;; elle ne le remplace
pas. Développer «&nbsp;OST&nbsp;» en «&nbsp;objet ou système technique&nbsp;» reste permis&nbsp;:
c'est expliciter une abréviation, pas réécrire une exigence.

### La règle est désormais mécanisée

`_outils/verif_regles_audit.py` porte une huitième règle vérifiable. Elle lit la carte de
référentiel de chaque séquence, la compare aux formulations de `_outils/data_competences.py`, et
échoue en nommant les mots absents.

Sur les 40 séquences du dépôt&nbsp;: **4 conformes, 5 en écart, 31 sans objet** (pas encore de carte
de référentiel — c'est-à-dire pas encore passées au gabarit maison). Les cinq écarts sont ceux que
le balayage manuel avait trouvés, aux mêmes codes&nbsp;: le contrôle ne découvre rien de plus, mais
il empêchera la récidive, et c'est tout ce qu'on lui demande.

### Une note d'outillage

Ma **première** version de ce contrôle signalait dix-neuf écarts, dont la quasi-totalité étaient
faux&nbsp;: elle indexait les formulations par le seul code (`C2.1`) au lieu du couple niveau + code,
et comparait donc la 5e au texte de la 3e.

C'est le même motif que la règle n°26 en juillet, et que les trois suites de tests qui accusaient
des pages conformes&nbsp;: **devant un contrôle qui accuse largement, douter du contrôle avant de
douter du contenu.**

### Pourquoi cette PR est sur une branche `theme-2`

`_outils/` appartient au Thème 2. J'y touche pour un outil de gouvernance que je maintiens, sur une
branche portant le motif du thème, afin que la garde-périmètre **s'applique** — plutôt que sur une
branche `infra` sans motif, où elle se serait désactivée d'elle-même. Une garde qu'on contourne en
nommant sa branche autrement n'est pas une garde.

---

## 8 août 2026 — Règle d'or n°43 : toute production demandée à l'élève a son corrigé, et ce corrigé arrive après

**Énoncé.** Chaque production que la séquence exige de l'élève — une liste, un relevé, un schéma,
un graphique, un algorigramme, une note — doit avoir son **corrigé complet dans la page**, sous la
forme même que l'élève devait produire. Ce corrigé est **replié**, et il n'apparaît **jamais avant**
l'activité qui le demande.

### D'où elle vient

Deux exigences que je traitais séparément, et qui se contredisaient à chaque lot.

D'un côté, la règle apprise au lot de 3e à Shenzhen&nbsp;: **ne pas donner la figure qui contient
la réponse**. Une planche de solutions illustrées y aurait vidé l'activité 1 de son sens, alors ce
lot ne porte volontairement qu'un seul SVG.

De l'autre, l'objection de Pascal sur le lot de 4e&nbsp;: si l'élève doit tracer un graphique et
qu'aucun graphique fini n'existe nulle part, **l'élève qui travaille seul n'a rien pour se
corriger**. Il produit, et il ne sait pas.

Les deux ont raison, et la contradiction n'est pas dans le contenu&nbsp;: elle est dans le
**moment**. Le corrigé n'est pas interdit, il est **différé**. Le repli du `<details>` n'est pas un
détail de mise en forme, c'est ce qui rend les deux exigences compatibles.

### Ce qu'elle change concrètement

- Une production **graphique ou schématique** exige un corrigé **de même nature**&nbsp;: un
  graphique se corrige par un graphique, pas par une phrase qui le décrit. Un élève ne peut pas
  comparer son tracé à un paragraphe.
- Le corrigé porte le mot **« corrigé »** dans son nom de fichier et dans son titre, pour qu'on ne
  puisse pas le glisser par erreur dans le fil de la page.
- Le corrigé va **plus loin que la réponse**&nbsp;: il dit aussi ce qu'on doit y lire. Le corrigé
  du graphique de Hangzhou ne se contente pas des barres — il nomme les deux lectures qui comptent,
  «&nbsp;la plus longue n'est pas celle dont on se plaint&nbsp;» et «&nbsp;une moyenne cache sa
  queue&nbsp;».
- Rien de tout cela ne s'applique aux **évaluations sommatives**, qui n'ont pas de corrigé dans le
  dépôt public — la barre qualité de la méthode reste inchangée sur ce point.

### Ce qu'elle rend possible

Un élève absent, un élève qui reprend chez lui, un élève qui va plus vite que la classe&nbsp;:
tous les trois travaillent seuls, et tous les trois ont besoin de savoir s'ils ont réussi. Une
séquence qui exige une production sans jamais montrer à quoi elle ressemble, réussie, ne fonctionne
qu'en présence du professeur.

**L'autonomie de l'élève est une propriété de la page, pas une qualité de l'élève.**

---

## 8 août 2026 — Trois précisions demandées par Pascal : le Bonus, les sigles nus, et l'entraînement prématuré

Trois remarques de Pascal, le même jour, qui touchent toutes au même endroit&nbsp;: **ce que l'élève
peut faire seul devant la page.**

### La règle n°43 s'étend au Bonus

Le Bonus est «&nbsp;facultatif, hors parcours obligatoire&nbsp;» — mais celui qui le fait est
précisément **celui qui travaille seul**, souvent chez lui, souvent le plus avancé. Lui refuser un
corrigé, c'est réserver la correction à ceux qui n'en ont pas besoin.

**La règle n°43 s'applique donc au Bonus comme au reste**&nbsp;: chaque défi porte son corrigé
replié. Quand le défi demande un dessin, un schéma ou une trace, le corrigé porte l'image
correspondante — un dessin ne se corrige pas par une phrase.

Le chiffre&nbsp;: **33 séquences du dépôt portent un bloc Bonus. Zéro n'a de corrigé.** C'est une
dette homogène, ce qui la rend au moins facile à traiter en série.

Pour les trois séquences **Packet Tracer**, l'image du corrigé sera un **SVG reconstruit**, pas une
capture d'écran&nbsp;: la règle n°1 ne se plie pas parce qu'un corrigé serait plus vite fait.
Décision confirmée par Pascal.

### Règle d'or n°44 — aucun sigle, aucun bouton ne reste nu

La règle n°35 disait déjà «&nbsp;un code n'apparaît jamais seul&nbsp;». Elle visait le texte. Elle
ne visait pas l'**interface**&nbsp;: nos badges de niveau, nos codes CRCN, nos boutons «&nbsp;mode
essentiel&nbsp;», «&nbsp;révision ciblée&nbsp;», «&nbsp;marquer à revoir&nbsp;» s'affichent nus, et
l'élève doit deviner.

**Énoncé.** Tout badge, code, sigle ou bouton porte une explication **à portée immédiate**&nbsp;:
un `title` pour la souris, un `aria-label` ou `aria-describedby` pour le lecteur d'écran, **et une
mention en clair** quelque part sur la page.

Le troisième élément n'est pas une redondance de zèle&nbsp;: **une infobulle ne s'ouvre pas au
doigt.** Sur la tablette d'un collégien, `title` ne s'affiche jamais. Une interface qui ne
s'explique qu'au survol ne s'explique pas aux élèves qui en ont le plus besoin.

### Règle d'or n°45 — un entraînement s'ouvre sur ce qui a été fait

Pascal signale que le QCM est proposé «&nbsp;presque sur toutes les pages, alors que toutes les
compétences ne sont pas atteintes&nbsp;».

**Vérification faite** — et elle nuance le constat sans l'annuler. Les 35 séquences du dépôt portent
**exactement un bouton QCM chacune** (règle n°4 tenue partout), placé dans le dernier panneau de
séance. Le QCM n'est donc pas sur toutes les pages d'une séquence.

Mais le fond est juste, et il est même plus gênant que la forme&nbsp;: **le QCM couvre tous les
codes de la séquence**, et rien n'empêche un élève de le lancer après la première séance. Il tombe
alors sur des questions portant sur ce qu'on ne lui a pas encore enseigné, et il conclut qu'il n'y
arrive pas.

Le plus intéressant, c'est que **la machine existe déjà**&nbsp;: le gabarit de QCM porte un mode
«&nbsp;révision ciblée&nbsp;» et un filtre par code. Ce qui manque n'est pas une fonction, c'est de
le **dire à l'élève** — et de ne pas ouvrir par défaut sur «&nbsp;parcours complet&nbsp;».

**Énoncé.** Un entraînement ne présente jamais par défaut ce qui n'a pas été enseigné. Le bloc
«&nbsp;Prêt·e à t'entraîner&nbsp;» annonce **le nombre de questions par code**, et le lien porte les
codes déjà travaillés&nbsp;; le QCM s'ouvre dessus. L'élève garde évidemment l'accès au parcours
complet — on ne lui interdit rien, on choisit seulement ce qu'on lui propose **en premier**.

Un seul bouton reste la règle (n°4)&nbsp;: c'est la **cible** du bouton qui devient contextuelle,
pas le nombre de boutons.

### Ce que ces trois règles ont en commun

Aucune ne demande d'écrire un contenu nouveau. Toutes les trois demandent de rendre utilisable ce
qui existe déjà — un corrigé qu'on avait gardé pour la classe, une fonction qu'on n'avait pas
annoncée, un sigle qu'on n'avait pas traduit.

C'est le prolongement direct de ce que Pascal a formulé ce matin&nbsp;: **l'autonomie de l'élève est
une propriété de la page, pas une qualité de l'élève.**

### Ordonnancement

La rentrée approche&nbsp;: le **Thème 1 se termine d'abord** (3e_C2, puis les 15 codes du C1).
L'audit des corrigés, les infobulles et l'entraînement ciblé se font ensuite, thème par thème. Les
règles n°43 étendue, n°44 et n°45 s'appliquent **dès maintenant aux lots neufs** — le retrofit des
anciens attend son tour, mais la dette cesse de croître.

---

## 8 août 2026 — Lot Hangzhou 4e_C2.1 · C2.2 : « ce que vit l'usager devant la borne »

Deuxième lot du **C2**, et premier lot où s'appliquent les trois règles écrites dans la journée.

### Le référentiel dicte le déroulé

`4e_C2.1` n'est pas un code de description, c'est un code de **traduction**&nbsp;: «&nbsp;en partant
du langage naturel (texte, croquis) pour aboutir aux schémas, graphiques, algorithmes&nbsp;».

Le déroulé n'est donc pas un choix pédagogique parmi d'autres — il est **imposé**. D'où quatre
activités, une par case du trajet&nbsp;: verbatims, graphique, algorigramme, exigences. Et chaque
case est justifiée par ce qui **manque** à la précédente, ce que la figure d'ouverture montre
explicitement.

C'est la première fois que je conçois un déroulé en partant de la **forme** de la formulation plutôt
que de son sujet. Après l'incident de l'esthétique, lire la formulation mot à mot n'est plus une
précaution&nbsp;: c'est devenu une méthode.

### Les données portent la leçon, pas le commentaire

Les chiffres sont construits pour qu'un résultat contre-intuitif apparaisse **sans que le professeur
l'annonce**&nbsp;:

- «&nbsp;choisir&nbsp;» est l'étape la plus longue en **moyenne** (40&nbsp;s), et personne ne s'en
  plaint&nbsp;; un usager la trouve même pratique&nbsp;;
- «&nbsp;déverrouiller&nbsp;» ne fait que 29&nbsp;s de moyenne, mais monte à **83&nbsp;s** pour les
  **9 retraits sur 30** qui ont demandé une reprise — et trois verbatims sur douze en parlent.

Un élève qui n'aurait que le chronomètre corrigerait la mauvaise étape&nbsp;; un élève qui n'aurait
que les témoignages ignorerait 40&nbsp;secondes. **C'est le croisement qui décide.**

Deux verbatims se contredisent aussi, volontairement. Ce n'est pas une incohérence à corriger&nbsp;:
c'est le résultat que l'activité 1 doit faire écrire.

### Première application des règles n°43, n°44 et n°45

- **n°43 étendue** — le Bonus a son corrigé, entièrement traité sur le distributeur de boissons du
  hall&nbsp;: les mots exacts de trois élèves, dix chronométrages (3, 4, 3, 5, 4, 3, **22**, 4, 3, 4),
  et l'écart moyenne / pire cas qui rejoue en petit ce que l'élève a découvert sur la borne.
- **n°44** — zéro badge et zéro bouton nus, plus une légende en clair sous les badges.
- **n°45** — le bouton du QCM vise `#codes=C2.1` après la seule séance 1, et annonce 15 questions au
  lieu de 30. Le QCM lit l'ancre, bascule en révision ciblée, et le dit.

**Conséquence, et c'est elle qui compte**&nbsp;: un élève absent, ou qui reprend chez lui, peut faire
cette séquence **seule du début à la fin**. Tout ce qui lui est demandé a son corrigé.

### Un test rouge, et qui avait tort — la quatrième fois

Le contrôle du corrigé du Bonus a échoué. Le corrigé était là&nbsp;: le test lisait `inner_text` sur
un `<details>` **replié**, qui n'expose que son `summary`.

Quatrième occurrence du même piège dans ce dépôt. Le réflexe est acquis — chercher lequel des deux a
tort avant de toucher au contenu — mais **le piège, lui, ne s'use pas**. Le fichier de tests porte
maintenant un commentaire qui l'explique, pour que le prochain le voie avant de le vivre.

### Un point-virgule dans une phrase

La matrice de couverture est un CSV à points-virgules. J'avais écrit une notion contenant un
point-virgule&nbsp;: toute la ligne s'est décalée d'une colonne, silencieusement. C'est mon contrôle
de couverture — «&nbsp;quelles questions ne sont citées nulle part&nbsp;?&nbsp;» — qui l'a vu, pas ma
relecture. Une ligne de CSV mal découpée ne se voit pas&nbsp;: elle se calcule.

### L'état du dépôt, mesuré

Deux codes quittent «&nbsp;À CRÉER&nbsp;»&nbsp;; `4e_C2.1` quitte en outre le statut PARTIEL, qu'il
tenait d'un QCM isolé. **25 codes complets, 32 à créer.**

Le vérificateur, sur les 41 séquences du dépôt, relève **56 manquements sur 23 séquences**&nbsp;:
20 modes essentiels absents, 13 séquences sans version étayée, 12 défauts d'accessibilité,
7 bandeaux de tâches manquants, 3 formulations de référentiel réécrites, 1 diagnostic d'entrée. Les
lots neufs sont à zéro&nbsp;; toute la dette est dans l'existant — et elle est maintenant **chiffrée
règle par règle**, ce qui la rend traitable en série plutôt qu'au jugé.

### La suite

Thème 1 d'abord, comme convenu&nbsp;: **3e_C2**, puis les 15 codes du **C1** — dont les sept
séquences qui n'ont ni mode essentiel ni carte de référentiel. Le retrofit des corrigés, des
infobulles et de l'entraînement ciblé viendra ensuite, thème par thème.

---

## 8 août 2026 — Précision de la règle n°43 : « toute production » veut dire toutes les options offertes

Pascal, sur le lot 3e_C2 en cours&nbsp;: «&nbsp;quel que soit le choix de l'utilisateur, puisqu'il y
a le mot <i>choisi</i>, il aura une correction, c'est ça&nbsp;?&nbsp;»

**En l'état, la réponse était non.** Et c'est le lot qui inaugure la règle n°43 qui l'enfreignait.

### Ce que j'avais fait

La séquence propose **six modes de représentation** à l'élève et lui demande d'en choisir. Mon
corrigé en traitait **trois** — algorigramme, graphique, storyboard — parce que j'avais raisonné
«&nbsp;trois destinataires, trois modes&nbsp;».

Un élève choisissant la carte d'empathie, le parcours utilisateur ou le tableau comparatif produisait
donc quelque chose dont il n'avait **aucun modèle**. Proposer six portes et n'en corriger que trois,
c'est pénaliser celui qui prend une porte qu'on a soi-même ouverte.

### La précision

**Quand une consigne offre un choix, le corrigé couvre toutes les options offertes** — pas
seulement celles que l'auteur trouvait les meilleures. Autrement, «&nbsp;choisis&nbsp;» est un
mensonge&nbsp;: il n'y a de vrai choix que si toutes les branches sont soutenues.

Le corollaire est utile à l'auteur&nbsp;: si corriger toutes les options coûte trop cher, alors il
faut **réduire le nombre d'options**, et non réduire le corrigé. Une consigne qui propose six modes
engage à six corrigés — c'est le prix du mot «&nbsp;choisis&nbsp;».

### Ce que ça a produit

Une seconde planche de corrigé, `corrige_trois_autres_modes.svg`&nbsp;: le même constat rendu en
parcours utilisateur, en carte d'empathie et en tableau comparatif. Elle porte, comme la première,
l'**angle mort** de chaque mode — ce qui en fait autre chose qu'un rattrapage&nbsp;: les six fiches
mises côte à côte démontrent la thèse de la séquence mieux qu'aucune phrase. Les six disent la
vérité, aucun ne la dit tout entière.

C'est la deuxième fois aujourd'hui qu'une question de Pascal améliore le lot au lieu de simplement
le corriger. La première avait produit la règle n°43&nbsp;; celle-ci lui donne sa portée exacte.

---

## 8 août 2026 — Deux questions de Pascal sur le lot 3e_C2 : le vocabulaire, et qui choisit

### «&nbsp;Les élèves savent-ils définir ces choix&nbsp;?&nbsp;»

Non, et je ne le vérifiais pas. La séquence proposait six modes de représentation — dont
<b>storyboard</b> et <b>carte d'empathie</b>, qui ne sont pas des mots de collège — et demandait
d'en choisir trois. Elle donnait de chaque mode ce qu'il montre et son angle mort&nbsp;; elle ne
demandait jamais à l'élève de <b>reconnaître</b> ce que le mot désigne.

Pascal se souvient que les anciens manuels traitaient cela par un appariement — «&nbsp;relie le mot
<i>croquis</i>, <i>esquisse</i>, à sa représentation&nbsp;». C'est exactement ce qui manquait. Six
appariements ont été ajoutés en tête de l'activité 2, et le vérificateur **refuse d'aller plus
loin** tant qu'ils ne sont pas tenus&nbsp;: «&nbsp;on ne choisit pas parmi des mots qu'on ne connaît
pas&nbsp;».

C'est le même défaut que celui corrigé une heure plus tôt sur les corrigés, sous une autre
forme&nbsp;: **offrir un choix sans donner de quoi choisir.** Là c'étaient les corrigés qui
manquaient, ici c'est le vocabulaire. Dans les deux cas, le mot «&nbsp;choisis&nbsp;» promettait
plus que la page ne tenait.

### «&nbsp;Choisis par l'élève, ou par le concepteur&nbsp;?&nbsp;»

**Le texte ne le dit pas.** «&nbsp;À l'aide de modes de représentation choisis&nbsp;» — le
participe qualifie les modes, il ne nomme pas l'auteur du choix. Les deux lectures tiennent
grammaticalement.

Mon argument pour la première&nbsp;: en **4e**, le programme énumère lui-même les modes
(«&nbsp;pour aboutir aux schémas, graphiques, algorithmes&nbsp;»)&nbsp;; en **3e** il retire
l'énumération et ajoute «&nbsp;choisis&nbsp;». Un texte qui cesse de nommer les modes au moment où
il ajoute ce mot me paraît transférer la sélection à l'élève, dans une logique d'autonomie
croissante sur le cycle.

**Mais c'est une lecture, pas une certitude — et je l'avais construite en silence.** C'est
précisément ce que la règle n°42 interdit, appliqué non plus à la formulation mais à son
**interprétation**&nbsp;: une lecture du programme se déclare comme lecture.

La séquence porte désormais la note, écrite à l'élève&nbsp;: le programme ne dit pas par qui&nbsp;;
ici c'est toi qui choisis&nbsp;; ton professeur peut faire autrement et t'imposer le mode&nbsp;; et
dans les deux cas l'exercice difficile reste le même — **justifier**.

**Règle n°42, troisième volet&nbsp;: quand une formulation du référentiel est ambiguë, on ne tranche
pas en silence. On dit qu'elle l'est, on donne sa lecture, et on laisse la porte ouverte.**

### Ce que la conclusion de Pascal apporte

«&nbsp;Les six cas de figure sont présents, et l'enseignant qui prend en main la séquence aura le
choix.&nbsp;» C'est la bonne réponse au problème, et elle vaut mieux que de trancher&nbsp;: une
séquence qui traite les six modes fonctionne <b>dans les deux lectures</b>. L'enseignant qui préfère
imposer garde l'exercice de justification intact&nbsp;; celui qui laisse choisir a de quoi corriger
n'importe quelle réponse.

Ce sera noté à la fiche pédagogique comme une **variante d'usage**, pas comme une réserve.

---

## 8 août 2026 — Lot Pékin 3e_C2.1 : la compétence C2 est achevée sur les trois niveaux

Dernier lot du C2. Avec lui, la compétence est couverte en 5e, en 4e et en 3e — et c'est le
**premier lot du dépôt à achever une compétence dont les deux autres niveaux existaient déjà**.

### La marche est écrite à l'élève

Puisque le lot termine, la progression complète devait se **voir**, et pas seulement dans la fiche
du professeur. La séquence porte donc un tableau, adressé à l'élève&nbsp;: en 5e tu regardais
l'objet **du dehors**&nbsp;; en 4e tu partais de **ce que vivent les gens**, mais l'itinéraire
t'était donné&nbsp;; en 3e tu décides de **la forme**, et tu la **défends**.

Trois ans pour apprendre une chose difficile&nbsp;: un objet technique ne se décrit pas seulement
par ce qu'il est, mais par ce qu'il fait vivre — et par la façon dont on le raconte à ceux qui
peuvent le changer. L'élève a le droit de voir ce chemin.

### Le mot «&nbsp;choisis&nbsp;», et sa contrainte

La difficulté propre à la 3e tient dans un mot. Et **choisir n'est un vrai geste que s'il existe une
contrainte** qui rende un choix meilleur qu'un autre&nbsp;: sans contrainte, l'élève prend le mode
qu'il préfère, et il a raison — il n'y a rien à justifier.

La contrainte retenue est le **destinataire**&nbsp;: le technicien, l'élue qui vote le budget,
l'usager debout dans la station. Trois temps, trois vocabulaires, trois pouvoirs. Le même constat ne
se dit pas de la même façon à ces trois-là.

D'où la thèse du lot, qui est aussi son titre implicite&nbsp;: **un mode n'est jamais bon en soi, il
est bon pour quelqu'un.** Et son corollaire méthodique&nbsp;: **on justifie un mode par son angle
mort, pas par son point fort** — tous ont un point fort, donc l'invoquer ne désigne personne.

### Ce que les données produisent seules

«&nbsp;Un usager sur cinq abandonne&nbsp;» est exact — 8 sur 40. Mais **0&nbsp;% chez les
habitués**, 43&nbsp;% chez les touristes, 50&nbsp;% chez les personnes âgées. Et 77&nbsp;s de durée
moyenne quand l'habitué met 41&nbsp;s et la personne âgée 123&nbsp;s.

La phrase que la séquence fait écrire&nbsp;: **ceux qui décident sont presque toujours des habitués,
et les habitués réussissent.** C'est pour cela qu'un problème d'usage reste invisible — et ce n'est
pas une question de mauvaise volonté, c'est structurel.

### Un test rouge, et cette fois c'est le vérificateur qui avait tort

Le contrôle «&nbsp;une lecture qui ne nomme pas les extrêmes est refusée&nbsp;» a échoué. J'ai
cherché lequel des deux avait tort, comme d'habitude — et pour la première fois, **ce n'était pas le
test**.

Mon vérificateur pédagogique cherchait `0 %` sans garde de chiffre. Or «&nbsp;0&nbsp;%&nbsp;» se
trouve aussi dans «&nbsp;**3**0&nbsp;%&nbsp;» et «&nbsp;4**0**&nbsp;%&nbsp;»&nbsp;: une lecture
fausse — 5&nbsp;% aux habitués, 30&nbsp;% aux personnes âgées — était **acceptée**. Le verrou
validait une réponse erronée.

La leçon de juillet disait&nbsp;: «&nbsp;devant un test rouge, chercher lequel des deux a tort avant
de toucher au code&nbsp;». Elle vaut **dans les deux sens**, et c'est la première fois que le second
sens se réalise. Corrigé par `(?:^|[^0-9])0\s*%`, avec un commentaire qui dit pourquoi.

### Ce que ce lot doit aux questions de Pascal

Trois de ses remarques, le même jour, ont directement modifié le lot&nbsp;:

1. **le Bonus a son corrigé** (règle n°43 étendue)&nbsp;;
2. **un choix offert engage un corrigé par option** — la séquence propose six modes, il a fallu
   deux planches de corrigé au lieu d'une&nbsp;;
3. **le vocabulaire avant le choix** — six appariements ouvrent l'activité 2, et le vérificateur
   refuse d'aller plus loin tant qu'ils ne sont pas tenus.

Et une quatrième a produit un volet de règle&nbsp;: «&nbsp;choisis par l'élève ou par le
concepteur&nbsp;?&nbsp;» — l'ambiguïté est déclarée, la lecture est donnée comme lecture, et les
deux variantes d'usage sont décrites à la fiche.

### Le bilan

Un code quitte «&nbsp;À CRÉER&nbsp;». Le dépôt compte **26 codes complets** et **31 à créer**.
Vérificateur&nbsp;: **8 sur 8**. Tests du lot&nbsp;: **54 sur 54**. Index&nbsp;: 20 sur 20.

**La compétence C2 est terminée.** Reste, pour achever le Thème 1&nbsp;: les 15 codes du **C1** —
dont sept séquences qui n'ont ni mode essentiel, ni version étayée, ni carte de référentiel.

---

## 8 août 2026 — Six séquences que le vérificateur n'avait jamais vues

En préparant le lot 5e_C1, j'ai annoncé à Pascal que «&nbsp;les sept séquences du C1 sont des plans
de 3,7 à 15 ko&nbsp;». **C'était faux**, et l'erreur mérite d'être écrite parce qu'elle a une cause
mécanique.

### Ce qui s'est passé

`_outils/verif_regles_audit.py` cherchait ses fichiers avec le motif `sequence_*.html`. Toutes les
séquences nommées avec des **traits d'union** lui échappaient. Six fichiers, dont&nbsp;:

| Taille | Fichier |
|---|---|
| **121 ko** | `4e_C1.4/sequence-cybersecurite-protection-donnees.html` — la plus grosse séquence du dépôt |
| 68 ko | `3e_C1.5/sequence-numerique-societe-economie-environnement-sante.html` |
| 63 ko | `5e_C1.1/sequence.html` |
| 60 ko | `4e_C6.2/sequence-jardin-connecte-arrosage-automatique.html` (Thème 2) |
| 18 ko | `4e_C1.4/activite-bonus-cyber-immersive-2fa.html` |
| 7 ko | `5e_C1.2/activite_crcn_donnees_freinage_5e_C1.2.html` |

Ces séquences **n'avaient aucune anomalie&nbsp;: elles étaient invisibles.** Depuis la création de
l'outil, elles n'ont jamais été comptées ni contrôlées.

### Pourquoi je m'y suis laissé prendre

Parce que **mon relevé d'état des lieux employait le même motif que le vérificateur**. J'ai cru
inventorier le C1 alors que je récitais l'angle mort de mon propre outil.

C'est la troisième forme que prend la même leçon dans ce dépôt&nbsp;:

- juillet — «&nbsp;un compteur ne sait pas ce qu'il compte&nbsp;» (règle n°26, 4 faux positifs)&nbsp;;
- ce matin — «&nbsp;une suite de tests vérifie ce que son auteur soupçonne&nbsp;» (43 tests verts
  sur un contenu faux)&nbsp;;
- maintenant — **un contrôle ne vérifie que ce qu'il regarde.**

Les trois disent la même chose sous trois angles&nbsp;: le silence d'un outil n'est pas une preuve.
Il faut savoir, à chaque fois, **quel est son périmètre**, et le comparer à ce qu'on croit couvrir.

### Ce que ça change

Le motif accepte désormais `sequence_*.html`, `sequence-*.html` et `sequence.html`. Le dépôt passe
de **41 à 47 séquences analysées**, et de **56 à 74 manquements** — dix-huit défauts qui existaient
depuis toujours et que personne ne pouvait voir.

**Et le plan du C1 change.** Ce que j'annonçais comme «&nbsp;tout le C1 à refaire&nbsp;» est
inexact&nbsp;: `4e_C1.4` porte une séquence de 121 ko, `3e_C1.5` une de 68 ko. Elles n'ont ni carte
de référentiel, ni vérificateur, ni mode essentiel — mais elles ont du contenu, et beaucoup. Le
chantier n'est pas le même selon qu'on écrit ou qu'on met au gabarit.

Je reprends l'état des lieux du C1 **avec le vérificateur corrigé** avant d'écrire une ligne de plus.

---

## 8 août 2026 — Cinq règles d'or tirées de la journée (n°46 à n°50)

Pascal&nbsp;: «&nbsp;de ces expériences passées, il serait utile d'écrire d'autres règles d'or&nbsp;;
ça nous permettra de gagner du temps et d'être plus efficaces.&nbsp;»

Le critère que j'applique pour décider si une leçon mérite un numéro&nbsp;: **elle doit avoir coûté
quelque chose**. Pas «&nbsp;bien faire son travail&nbsp;», mais «&nbsp;voici ce qui se paie quand on
ne le fait pas&nbsp;». Les cinq ci-dessous ont toutes un incident daté derrière elles.

### Règle d'or n°46 — Une estimation qui n'a pas ouvert le fichier n'est pas une estimation

**L'incident.** J'ai annoncé que le lot 5e_C2 serait «&nbsp;un achèvement, pas une création — le
travail le plus court des trois&nbsp;», sur la foi d'un statut d'audit et d'un nom de fichier. Le
lot a demandé 43 tests et huit fichiers neufs. Quelques heures plus tard, j'ai annoncé que le C1
n'était que «&nbsp;des plans de 3,7 à 15 ko&nbsp;»&nbsp;: il y avait 63 ko rien que sur le C1.1.

**Le coût.** Deux fois, Pascal a décidé de l'ordre du travail sur une estimation fausse.

**La règle.** Avant d'annoncer l'ampleur d'un travail, **ouvrir les fichiers concernés**. Un statut
d'audit, un nom de fichier ou une taille en octets ne sont pas des estimations&nbsp;: ce sont des
indices. Et si l'on estime sans ouvrir — par exemple pour répondre vite — **le dire**&nbsp;:
«&nbsp;sans avoir ouvert, il me semble que…&nbsp;».

### Règle d'or n°47 — Le silence d'un outil n'est pas une preuve : tout contrôle déclare son périmètre

**L'incident.** Le vérificateur cherchait `sequence_*.html`. Six séquences nommées avec des traits
d'union — dont la plus grosse du dépôt, 121 ko — n'ont jamais été analysées. Elles n'avaient aucune
anomalie&nbsp;: **elles étaient invisibles**. Et je m'y suis laissé prendre parce que mon propre
relevé employait le même motif.

**Le coût.** Dix-huit défauts non vus depuis la création de l'outil, et un plan de travail bâti sur
un inventaire faux.

**La règle.** Un contrôle ne vérifie que ce qu'il regarde. Tout outil de contrôle **annonce ce qu'il
a examiné et ce qu'il a écarté** — nombre de fichiers, motif employé. Et celui qui lit un rapport
vert **compare ce périmètre à ce qu'il croit couvrir** avant d'en tirer une conclusion.

Cette règle est mécanisable, et elle le sera&nbsp;: chaque outil du dépôt doit imprimer son
périmètre en fin de rapport.

### Règle d'or n°48 — Une donnée simulée est déterministe là où un corrigé s'appuie sur elle

**L'incident.** Le premier tirage aléatoire des observations de Pékin a donné **zéro abandon chez
les touristes** — alors que tout le lot repose sur eux. Les corrigés auraient décrit une réalité que
le fichier ne contenait pas.

**Le coût.** Détecté avant livraison, par chance&nbsp;: j'ai relu les statistiques produites. Un
lot livré dans cet état aurait donné à des élèves des corrigés faux.

**La règle.** Dans un jeu de données simulé, tout ce sur quoi un corrigé s'appuie est **posé, pas
tiré au sort**&nbsp;: effectifs, anomalies, pics, valeurs remarquables. L'aléa ne sert qu'au
décor — les durées, le bruit de mesure — et toujours avec une graine.

**Une donnée simulée n'a pas à être imprévisible&nbsp;: elle a à être vraie par rapport à ce qu'on
en dit.**

### Règle d'or n°49 — On teste ce qui est rendu, pas ce qui est écrit

**Les incidents**, il y en a trois, et ils se ressemblent&nbsp;:

- une séquence héritée affiche depuis sa mise en ligne trois images nommées `{{analysis_icon}}`,
  `{{sensor_icon}}`, `{{sort_icon}}` — des variables de gabarit jamais remplacées&nbsp;;
- un QCM du lot Shanghai portait un champ `img` sous forme de tuple au lieu d'un objet&nbsp;: les
  trois questions illustrées n'auraient affiché **aucune image**, et la source ne le montrait
  pas&nbsp;;
- quatre fois, une suite de tests a lu `inner_text` sur un `<details>` **replié**, qui n'expose que
  son `summary`, et a déclaré absent un contenu présent.

**Le coût.** Des pages publiées avec des trous que personne ne voyait, et des heures perdues à
soupçonner un contenu juste.

**La règle.** Un contrôle porte sur la page **telle que le navigateur la rend** — images
effectivement chargées, texte effectivement présent dans le DOM, y compris replié. Lire le source ne
prouve rien, et lire ce qui est visible ne prouve pas ce qui existe.

### Règle d'or n°50 — Devant un contrôle rouge, chercher lequel des deux a tort avant de corriger

**Les incidents.** Cinq fois en trois semaines. Quatre fois, c'était le **contrôle** qui avait
tort&nbsp;: la règle n°26 accusait quatre pages conformes sur cinq, et trois suites de tests
accusaient des séquences justes. La cinquième fois — aujourd'hui, lot 3e_C2 — c'était le
**vérificateur pédagogique**&nbsp;: il cherchait «&nbsp;0&nbsp;%&nbsp;» sans garde de chiffre et
acceptait «&nbsp;30&nbsp;%&nbsp;».

**Le coût.** Quand on corrige le contenu à cause d'un contrôle fautif, on abîme du travail juste et
on garde le défaut.

**La règle.** Un rouge est une **contradiction entre deux affirmations**, pas un verdict. Avant de
toucher à quoi que ce soit, établir laquelle des deux est fausse. Et le corollaire, qui s'est
vérifié aujourd'hui&nbsp;: **cela vaut dans les deux sens** — un contrôle peut être trop sévère,
mais aussi trop indulgent.

### Ce que ces cinq règles ont en commun

Aucune ne porte sur la pédagogie. Toutes portent sur **la confiance qu'on accorde à ce qui nous
informe** — un statut, un rapport vert, un tirage aléatoire, un fichier source, un test rouge.

Le dépôt avait quarante-cinq règles sur ce qu'il faut produire. Il lui en manquait cinq sur **ce
qu'il faut croire**.

---

### Règle d'or n°51 — Le premier texte que l'élève lit n'est jamais vérifié par personne

**L'incident.** Le gabarit de QCM du dépôt vient du lot «&nbsp;SOS serre&nbsp;» (Thème 2, 4e).
Chaque lot de Thème 1 en a repris le moteur, et chaque générateur a remplacé consciencieusement ce
qu'il fallait&nbsp;: le `<title>` de l'onglet, les badges de niveau et de code, les libellés du
filtre par compétence, la clé de sauvegarde, le lien vers la séquence. Aucun n'a remplacé le `<h1>`
ni le sous-titre — c'est-à-dire **les deux premières lignes affichées de la page**.

Résultat&nbsp;: **six QCM de Thème 1** — 5e, 4e et 3e du C2, 5e, 4e et 3e du C3 — annonçaient à
l'élève «&nbsp;Thème 2 · Martinique — 4e · Atelier&nbsp;: QCM — SOS serre&nbsp;», suivi d'un
sous-titre sur les adresses IP fixes et le montage Packet Tracer. Un élève de 5e ouvrant le QCM de
Shanghai lisait qu'il était en 4e, sur un autre thème, à propos d'un objet qu'il n'a jamais vu.

**Pourquoi rien ne l'a vu.** Toutes les suites de tests vérifiaient le `<title>` de l'onglet, le
nombre de questions, les modes, la sauvegarde, les liens. Aucune ne vérifiait le titre **affiché**.
Le `<title>` est ce que le développeur regarde&nbsp;; le `<h1>` est ce que l'élève lit. Nous avions
testé le premier pendant six lots et jamais le second.

**Le coût.** Six pages publiées, fusionnées, et lues par personne d'assez près pour voir la première
ligne. C'est la sixième fois qu'un défaut survit parce qu'il se trouvait à un endroit que le
contrôle ne regardait pas (règle n°47) — mais cette fois l'endroit était le plus visible de tous.

**La règle.** **Ce que l'élève voit en premier se vérifie en premier.** Titre affiché, sous-titre,
badges, première phrase&nbsp;: tout élément d'identification visible doit nommer le bon thème, le
bon niveau et le bon objet. Tout générateur travaillant à partir d'un gabarit emprunté à un autre
lot **refuse d'écrire** tant qu'il reste dans le résultat une trace du lot d'origine — le garde-fou
est posé dans le générateur, pas dans une relecture.

**Mécanisation.** Le garde-fou est en place dans les trois générateurs existants et dans celui du
lot 5e_C1. Le contrôle correspondant appartient à `_outils/verif_regles_audit.py`, donc à une
branche Thème 2&nbsp;: il y rejoint la mécanisation de la règle n°47, encore en attente.

---

## Dix règles tirées d'un audit extérieur du C2 (8 août 2026)

Pascal a fait auditer les trois séquences C2 du Thème 1 — 5e Shenzhen, 4e Hangzhou, 3e Pékin — par un
regard extérieur, qui n'a lu que les pages publiées. Son verdict sur l'ossature est bon et il ne
demande pas de tout refaire. Ce qui suit ne retient de l'audit que **ce qui se vérifie dans le
dépôt** et **ce qui se généralise en règle**. Les propositions d'enrichissement, elles, sont notées
comme travaux, pas comme règles.

### Règle d'or n°52 — Une notion du programme se range dans les catégories du programme

**L'incident.** La séquence 5e_C2.1 classe les interacteurs en **« personne, objet, condition »**.
C'est une invention — cohérente, enseignable, et à côté. Le programme 2024 énumère quatre familles
d'interacteurs extérieurs : **utilisateurs, données, autres objets, éléments de l'environnement**.
La catégorie **données** est entièrement absente de la séquence, alors qu'une station de vélos ne
fonctionne que par elles : identifiant de l'abonné, état du vélo, numéro de borne. Et « les règles
de la ville », que la séquence range parmi les interacteurs, n'en est pas un : c'est une source
d'exigence.

**Le coût.** Un élève apprend une taxonomie qui ne se retrouve nulle part ailleurs, ni dans les
ressources nationales, ni au niveau suivant, ni au brevet.

**La règle.** La règle n°42 disait : *une formulation de compétence se recopie, elle ne se
reformule pas*. Elle s'étend ici aux **notions** : quand le programme énumère des catégories, on
enseigne **ses** catégories, avec **ses** mots. On peut y ajouter, on ne peut pas y substituer.
Corollaire de méthode : avant de réécrire, **on ouvre le texte officiel** — la règle n°46 vaut aussi
pour les programmes, et cet audit-ci, aussi juste soit-il, n'est pas le texte.

### Règle d'or n°53 — Une notion qui a une voisine se définit contre elle

**L'incident.** Le billet d'entrée du 5e_C2 demande à quoi se reconnaît une **fonction technique**,
et donne pour bonne réponse : « un verbe à l'infinitif : **elle dit à quoi ça sert** ». Or « à quoi
ça sert » est la définition de la **fonction d'usage**. La bonne réponse enseigne la confusion
qu'elle prétend lever — et le distracteur exact, celui qu'il fallait écarter, n'était même pas dans
la liste.

**Le coût.** Une définition fausse placée dans un diagnostic d'entrée : l'élève la retient d'autant
mieux qu'elle arrive en premier, et qu'elle est validée.

**La règle.** Toute notion qui possède une voisine proche — fonction d'usage / fonction technique,
donnée / information, exigence / solution, écarter / effacer, contrainte / interacteur — se définit
**en nommant sa voisine et ce qui l'en sépare**. Une définition qui tient sans mentionner sa voisine
est presque toujours la définition de la voisine.

### Règle d'or n°54 — Un nombre établi ailleurs se calcule, il ne se recopie pas

**L'incident.** La séquence 5e_C2 annonce « 30 questions, dont **3 illustrées** ». Le QCM en compte
**4**. Personne n'a menti : quelqu'un a écrit une phrase, puis a ajouté une image.

**Le coût.** Faible, isolément. Répété, il donne l'impression exacte d'un ensemble non synchronisé —
et c'est cette impression qui décide un collègue à ne pas réutiliser le lot.

**La règle.** Tout nombre qu'un fichier affirme d'un autre fichier — nombre de questions,
d'illustrées, de séances, de minutes, de codes — est **produit par un contrôle**, pas par la
mémoire. Mécanisable, et à mécaniser avec les n°47 et n°51.

### Règle d'or n°55 — Un profil d'usager nomme une situation, pas une catégorie de personnes

**L'incident.** Le lot 3e_C2 fait calculer des taux d'abandon par profil : habitués 0 %,
occasionnels 11 %, poussette 25 %, touristes 43 %, **personnes âgées 50 %**. La séquence réfute déjà
explicitement la lecture « les habitués sont plus doués » — c'est un distracteur, et il est réfuté.
Mais le tableau, lui, met un âge en face d'un échec.

**Le coût.** On voulait enseigner que l'interface exclut ; on risque d'enseigner que certaines
personnes sont incapables. C'est exactement l'inverse de la compétence visée.

**La règle.** Un profil se nomme par une **situation d'usage** — première utilisation, mains
encombrées, écran en plein soleil, langue peu maîtrisée, une seule main disponible, poussette,
mobilité réduite — jamais par une catégorie de personnes. Et la question posée aux élèves porte sur
l'objet : *quelles caractéristiques de l'interface expliquent cet écart&nbsp;?* On mesure
l'accessibilité de l'objet, jamais la capacité supposée des gens.

### Règle d'or n°56 — Un outil professionnel s'enseigne rattaché au mot du programme

**L'incident.** Le 3e_C2 propose six modes de représentation : parcours utilisateur, algorigramme,
graphique, carte d'empathie, storyboard, tableau comparatif. Le programme, lui, nomme : **croquis,
schéma, graphique, algorithme, modélisation**. Deux listes qui ne se recouvrent qu'à moitié — et
c'était déjà l'inquiétude de Pascal quand il demandait si les élèves savaient définir ces choix.

**Le coût.** L'élève apprend un vocabulaire de métier sans savoir à quelle case officielle il
correspond. Au moment de l'évaluation, il ne reconnaît pas le mot de la consigne.

**La règle.** On garde les outils professionnels — ils valent mieux que les étiquettes — mais chacun
est **explicitement raccroché** au mot du programme : un storyboard est une suite de **croquis**, un
parcours utilisateur est un **schéma**, un algorigramme représente un **algorithme**. Et parmi les
représentations qu'un élève choisit, **au moins une appartient explicitement aux modes du
programme**. La **modélisation**, absente de nos C2, reste à introduire.

### Règle d'or n°57 — Une formule frappante doit rester vraie quand on la prend au mot

**Les incidents.** Trois, tous du même genre. « La moyenne décrit **une personne qui n'existe
pas** » — souvent vrai, pas toujours. « **Chaque** détail de la station est une décision » — non :
beaucoup viennent d'une norme, d'un coût, d'un composant standard. « L'objet peut fonctionner
**parfaitement** et échouer à rendre son service » — si le service n'est pas rendu, « parfaitement »
est de trop.

**Le coût.** L'élève qui prend la phrase au mot a raison, et c'est nous qui avons tort. On perd
exactement l'élève le plus attentif.

**La règle.** Une formule doit sa force à sa brièveté, jamais à son approximation. Avant de la
garder, on la prend **au pied de la lettre** et l'on cherche le contre-exemple. S'il existe, on
resserre sans s'affadir : « une moyenne peut ne correspondre à personne, et masquer de forts
écarts » ; « beaucoup de détails observables résultent d'un choix — ou d'une contrainte » ; « aucun
composant n'est en panne, et pourtant le service n'est pas rendu ».

### Règle d'or n°58 — Le réel n'est pas un bonus

**Le constat.** Le programme recommande explicitement de faire **manipuler et mettre en service des
objets réels**, pour que les descriptions produites par les élèves soient ancrées. Nos trois lots C2
reposent presque entièrement sur des données simulées ; l'observation d'un objet réel, quand elle
apparaît, est un prolongement facultatif. C'est le seul reproche **structurel** de l'audit, et il
est fondé.

**Le coût.** Des élèves qui décrivent parfaitement l'expérience d'un usager qu'ils n'ont jamais vue,
devant un objet qu'ils n'ont jamais touché. Et une discipline qui, sur écran, ressemble à toutes les
autres.

**La règle.** Chaque lot comporte **au moins une production qui repose sur un objet réellement
manipulé** — et elle est dans le parcours obligatoire, jamais dans le Bonus. L'objet est celui du
collège : imprimante, sèche-mains, porte à badge, fontaine, vidéoprojecteur. Le simulé garde son
rôle — il donne l'échelle et les cas qu'on ne peut pas produire en une heure — mais il ne remplace
pas le geste.

### Règle d'or n°59 — L'outil ne doit jamais devenir la compétence évaluée

**L'incident.** L'activité tableur du 4e_C2 impose un seul chemin : ouvrir un CSV de 150 lignes,
calculer, produire un graphique. Un élève qui comprend parfaitement l'expérience de l'usager mais
maîtrise mal le tableur est évalué plus bas qu'un élève qui produit une moyenne sans rien comprendre
à l'usage. Or **C2 n'est pas une compétence de tableur**.

**Le coût.** On croit mesurer une compétence, on mesure l'accès à un outil — c'est-à-dire, très
souvent, ce que l'élève a chez lui.

**La règle.** Quand une production passe par un outil, on offre **deux chemins vers la même
exigence** : un chemin guidé (tableau partiellement calculé, graphique fourni à interpréter) et un
chemin autonome (données brutes, calculs et graphique à produire). **Les mêmes questions, la même
exigence, deux accès.** Et la page dit à l'élève ce qui est évalué : « le graphique est un outil ;
ce qui compte est ce que tu en conclus ». Corollaire qui vaut pour tout le dépôt : **un logiciel
n'appartient à aucune compétence** — c'est ce que l'élève en fait qui décide de laquelle il relève.

### Règle d'or n°60 — On ne coche un domaine que devant une production observable

**L'incident.** Le rattachement au socle et au CRCN, dans plusieurs fiches, tient à la nature de
l'activité plutôt qu'à une trace. **Utiliser une page HTML n'est pas une compétence CRCN.**

**Le coût.** Des cartes de couverture qui promettent plus que ce que l'élève a réellement produit —
et un enseignant qui, le jour du bilan, n'a rien à montrer.

**La règle.** Un domaine du socle ou une compétence CRCN n'est déclaré que si le lot **nomme la
production** qui en apporte la preuve. Pas de production nommée, pas de case cochée.

### Règle d'or n°61 — Une évaluation ne mesure qu'un construit à la fois

**L'incident.** Une ressource héritée du 4e, `qcm_fonctionnement_objet.html`, est rattachée à C2
tout en interrogeant des compétences de programmation. Elle mesure deux choses et n'en note qu'une.

**Le coût.** Un résultat bas ne dit plus lequel des deux apprentissages manque — donc ne dit rien
d'exploitable.

**La règle.** Un QCM, un exercice, une évaluation portent sur **un seul construit**. Une ressource
qui en mêle plusieurs n'est pas supprimée pour autant : elle est **présentée pour ce qu'elle est**,
et jamais annoncée comme une mesure de la compétence.

### Ce que cet audit prouve accessoirement

Il a trouvé, par un chemin entièrement différent du mien, **le défaut des en-têtes de QCM** — « SOS
serre », adresse IP, Packet Tracer — que j'avais découvert le matin même en ouvrant le gabarit. Deux
regards indépendants l'ont vu en une journée ; six lots ne l'avaient pas vu en trois semaines. C'est
l'argument le plus net possible pour la règle n°51, et pour le principe qui la porte : **un contrôle
ne trouve que ce qu'il regarde** (n°47).

Et il faut lui appliquer sa propre médecine : cet audit n'a lu que les **pages publiées**. Il ne
pouvait voir ni les 74 manquements que le vérificateur relève sur 28 séquences, ni la dette des
corrigés absents (n°43), ni les infobulles manquantes (n°44). Son périmètre est réel, et il ne le
déclare pas.

---

## La grammaire manquante — inventaire des représentations (8 août 2026)

Pascal signale que le point 10 de l'audit — la table des représentations à conserver — est peut-être
la raison pour laquelle « on bloquait ». Il a raison, et il faut le dire plus nettement que l'audit
ne le dit : **le programme 2024 a retiré la grammaire graphique sans la remplacer, nous l'avons
suivi fidèlement, et nous avons construit des concepts sans vocabulaire partagé.** Or l'inspection
et les sujets de DNB, eux, parlent encore cette grammaire.

### Ce que le dépôt contient réellement, au 8 août 2026

Inventaire mécanique sur les **156 pages HTML** des trois thèmes, en distinguant « le mot
apparaît » de « l'élève produit la représentation ».

| Représentation | Présence réelle | Emplacement |
| --- | --- | --- |
| Algorigramme | **319 occurrences, enseigné et produit** | Th. 1, 2 et 3 |
| Chaîne d'information | **166, enseignée et produite** | Thème 2 |
| Chaîne d'énergie | **164, enseignée et produite** | Thème 2 |
| Tableau contraintes / exigences | **341, enseigné et produit** | Th. 1 (4e_C2) et 2 |
| Cahier des charges | **58, réellement rédigé par l'élève** | 4e_C2, 3e et 4e C1 hérités |
| Schéma fonctionnel / blocs | **36, enseigné** | Thème 2 |
| Croquis | 7 occurrences — **toutes des citations du référentiel** | jamais produit par l'élève |
| Modélisation | 5 occurrences — le mot, jamais la chose | Thème 2 |
| FAST | 8 occurrences — **dont zéro pertinente** : c'était « fast-food » dans un QCM wifi | **absent** |
| Bête à cornes | **0** | absent |
| Diagramme des interacteurs / pieuvre | **0** — le mot « interacteur » apparaît 175 fois, la représentation jamais | absent |
| SysML — exigences | **0** | absent |
| SysML — cas d'utilisation | **0** | absent |
| Carte mentale | **0** | absent |
| Diagramme de Gantt / planification des tâches | **0** | absent — **alors que le programme l'impose** en gestion de projet |
| Modélisation 3D / CAO | **0** | absent |

Sept représentations nommées sont **entièrement absentes**, une huitième — le croquis — n'existe
qu'en citation, et le seul « FAST » du dépôt était un fast-food. Ce n'est pas un oubli de détail :
c'est la moitié de la langue du métier.

### Règle d'or n°62 — Le concept prend le mot du programme, l'outil garde le nom du métier

**Le raisonnement.** Le programme 2024 a cessé d'imposer « bête à cornes », « pieuvre », « FAST »,
« SysML ». **Il ne les a pas interdits** : il a déspécifié. Nous avons lu le retrait comme une
interdiction, et nous avons enseigné des concepts que personne ne sait nommer — ni l'inspecteur qui
visite, ni le sujet de DNB, ni le collègue qui reprend la séquence, ni l'élève qui change
d'établissement.

**La règle.** Chaque représentation est nommée **deux fois** : par le mot du programme, qui fait
foi, et par le nom que la profession emploie, entre parenthèses.

> **Diagramme des interacteurs extérieurs** *(historiquement appelé diagramme pieuvre)*
> **Suite de croquis** *(storyboard)* · **Schéma du parcours** *(parcours utilisateur)*

Le mot du programme est celui de l'évaluation et de la carte de compétence (règle n°42) ; le nom du
métier est celui qui circule. Ni l'un sans l'autre. Et **aucun outil n'appartient à une
compétence** : c'est ce que l'élève en fait qui décide de laquelle il relève — Sweet Home 3D sert
C2 quand il représente un parcours d'usager, et le Thème 3 quand il modélise une forme.

### Règle d'or n°63 — Ce que le programme impose nommément se produit, pas se mentionne

**L'incident.** Le programme cite explicitement le **diagramme de planification des tâches** en
gestion de projet. Le dépôt en compte **zéro**. Il cite le **croquis** comme point de départ du
langage naturel en 4e : sept occurrences, toutes des citations du texte officiel, aucune production
d'élève. Il cite la **modélisation** parmi les modes de représentation de 3e : cinq occurrences du
mot, aucune chose.

**Le coût.** Une carte de couverture verte au-dessus d'un enseignement qui n'a pas eu lieu. C'est
le défaut le plus grave qu'un dépôt pédagogique puisse porter, parce qu'il est **invisible depuis
l'intérieur** : nos vérificateurs comptaient des séquences, jamais des gestes.

**La règle.** Quand le programme **nomme** une représentation, le lot qui porte le code
correspondant **fait produire cette représentation par l'élève**, et le rapport de tests le déclare.
Citer le texte officiel n'est pas l'enseigner. À mécaniser avec les n°47, n°51 et n°54.

### Règle d'or n°64 — Tout lot se situe sur la chaîne d'analyse

**Le constat.** L'audit reconstitue la chaîne complète, et elle est juste :

> **Analyse externe** — besoin *(bête à cornes)* → fonction d'usage → interacteurs *(diagramme des
> interacteurs, « pieuvre »)* → contraintes et exigences → **cahier des charges**
> **Analyse interne** — fonctions techniques *(FAST)* → solutions techniques → chaînes énergie et
> information → constituants
> **Conception** — croquis, schéma, modélisation → prototype → tests et mesures →
> **comparaison au cahier des charges**

Le programme 2024 n'a pas supprimé cette chaîne : il a cessé d'imposer les outils graphiques qui la
jalonnaient. Et il referme lui-même la boucle, puisqu'il demande de comparer les résultats obtenus
ou simulés aux **exigences issues d'un cahier des charges**. Le cahier des charges n'est donc pas un
vestige : c'est le **référentiel qui valide la solution**.

**Le coût de l'avoir ignorée.** Nos lots sont bons un par un et ne se répondent pas. L'élève traverse
trois ans de technologie sans jamais voir qu'il parcourt **une seule démarche**, ni où il en est.

**La règle.** Chaque lot indique, dans sa synthèse professeur et dans sa fiche, **où il se situe sur
la chaîne** — ce qui le précède, ce qui le suit. Et la boucle finale — cahier des charges →
conception → prototype → essai → **retour au cahier des charges** — est enseignée comme une boucle,
pas comme une fin de parcours.

### Règle d'or n°65 — Une notion traverse les niveaux en changeant de verbe, pas de sujet

**Le constat.** L'audit propose, pour le cahier des charges : **5e reconnaître → 4e formuler →
3e choisir, justifier, arbitrer**. C'est exactement la bonne forme d'une progression spiralaire, et
c'est celle que nos meilleurs lots suivent sans l'avoir nommée — le C2 va bien de « regarder l'objet
du dehors » à « décider de la forme et la défendre ».

**Le contre-modèle.** Trois années à refaire le même diagramme en changeant d'objet. L'élève croit
réviser ; il n'apprend rien de nouveau, et il s'ennuie à juste titre.

**La règle.** Quand une notion revient d'un niveau à l'autre, ce n'est pas l'objet d'étude qui
change, c'est **le verbe** : reconnaître, puis produire, puis arbitrer. La fiche pédagogique de
chaque lot **nomme le verbe du niveau** et celui des deux autres. Si l'on ne sait pas dire en quoi
le geste de 4e diffère de celui de 5e, la progression n'existe pas — il n'y a qu'une répétition.

### Décision du 8 août 2026 — ce qui est fait avant la rentrée

Pascal tranche, après inventaire :

1. **Les quatre corrections P0 du C2**, puis **la carte des représentations** — une page de
   référence portant les quinze représentations, chacune nommée deux fois (règle n°62), situées sur
   la chaîne d'analyse (n°64), avec pour chacune le niveau et le verbe (n°65).
2. **Quatre représentations absentes sont intégrées cette année** : le **diagramme des interacteurs**
   modernisé à quatre familles (5e_C2), la **bête à cornes** courte en entrée d'étude, le **FAST**
   à la charnière Thème 1 / Thème 2, et le **diagramme de Gantt**, que Pascal rattache à **C7.1**
   (Thème 3, projet robot). SysML et carte mentale restent hors périmètre cette année.
3. **Le C1 en 4e et 3e** reprend ensuite.

Le motif de cet ordre est écrit ici pour qu'on ne le rediscute pas : les P0 sont des **erreurs
enseignées**, et une erreur enseignée coûte plus cher qu'un lot manquant.

---

### Règle d'or n°66 — On n'écrit pas dans le dossier d'un autre, même pour l'améliorer

**L'incident, aujourd'hui, de ma main.** En clôturant le lot Chengdu, j'ai voulu poser les README
pointeurs d'usage vers les cinq autres codes du C1 en 5e. Je n'ai pas ouvert les dossiers avant
d'écrire. Ils n'étaient pas vides : **5e_C1.2 et 5e_C1.3 contiennent des lots complets** d'un autre
auteur — séquence, QCM, synthèses, fiche, manifeste — et **5e_C1.4, C1.5 et C1.6 portaient des
README écrits par cet auteur**, qui pointaient vers ses propres séquences mutualisées.

J'ai **écrasé trois de ces README** et déposé deux fichiers dans des lots qui n'avaient rien
demandé. Le contenu que j'ai effacé était juste : il décrivait des preuves CRCN observables et des
mutualisations légitimes.

**Ce qui a permis de le voir.** Rien d'automatique. `git status` a montré trois ` M ` là où
j'attendais des créations. Sans ce coup d'œil, la faute partait dans le bundle.

**Le coût évité.** Le travail d'un collègue effacé par une régénération, et une PR qui viole la
contrainte la plus ancienne du dépôt — *ne jamais modifier les lots existants d'un autre auteur*.

**La règle, en deux temps.**

1. **La n°46 vaut aussi pour l'écriture.** « Une estimation qui n'a pas ouvert le fichier n'est pas
   une estimation » — et une écriture qui n'a pas ouvert le dossier est un écrasement en puissance.
   Avant d'écrire dans un dossier, on liste son contenu.
2. **Un fichier d'un autre auteur ne s'écrase jamais, même pour l'améliorer.** Quand une ressource
   nouvelle recouvre un code déjà servi, la déclaration se fait **chez soi** — dans son propre
   README et dans la carte de couverture, qui est un fichier commun — jamais chez l'autre. Le
   dépôt n'a pas à choisir un vainqueur : il doit permettre à l'enseignant de choisir.

**Ce qui a été fait à la place.** Les trois README sont restaurés à l'identique, les deux fichiers
parasites retirés, et le README de `5e_C1.1` porte un **tableau comparatif** qui nomme, pour chacun
des cinq codes, la ressource existante et ce que Chengdu apporte de différent — en disant
explicitement que les deux peuvent se suivre et qu'aucune n'est moins bonne. La carte de couverture
reçoit un champ `pointeur_second_parcours` sur les cinq entrées, sans rien retirer de ce que l'audit
disait des ressources en place.

### Lot livré — 5e_C1.1 à C1.6 « Chengdu : le collège qui mesure son air »

Premier lot du dépôt à porter **six codes** dans une seule séquence, tenus par un seul objet : le
relevé du capteur de la cour. 5 séances, 215 min pour 275 disponibles. QCM de 30 questions dont 13
illustrées, ouverture ciblée sur les compétences déjà validées (n°45). **43 tests exécutés, 43
verts.** Vérificateur de règles : 8 sur 8.

Trois nouveautés de méthode y ont été appliquées le jour même de leur écriture : la n°51 (le titre
affiché du QCM), la n°59 (deux chemins vers l'activité tableur, parce que le calcul n'est pas la
compétence) et la n°66 ci-dessus. Le lot déclare aussi ce qu'il ne fait pas : **aucune manipulation
d'objet réel** (n°58), et une donnée traitée mais jamais produite.

Le dépôt passe de **26 à 27 codes COMPLET ET VALIDABLE**.

---

### Règle d'or n°67 — Une consigne qui annonce une production sans offrir de champ n'est pas une consigne

**L'incident.** Pascal signale que la séquence `5e_C1.2` (« Comparer des principes techniques »,
d'un autre auteur) va contre plusieurs de nos règles. Vérification faite en ouvrant le fichier :
il a raison sur l'essentiel, et le défaut central est plus net encore que dit. La page contient
**zéro `<textarea>`, zéro `<select>`, zéro `<input>`, zéro `<button>`** — et pourtant elle écrit
trois fois «&nbsp;<b>Production attendue</b>&nbsp;: un tableau complété…&nbsp;», «&nbsp;une matrice
de comparaison et deux phrases de justification…&nbsp;». Le tableau de l'activité 1 est un tableau
HTML statique dont les cellules contiennent «&nbsp;…&nbsp;».

L'élève lit qu'on attend de lui une production, et n'a **nulle part où la faire**. Il n'y a donc ni
vérificateur, ni sauvegarde, ni trace — et rien à corriger.

**Ce qui est plus grave que le reste.** Le contrôle mécanisé n'a relevé qu'**un seul** manquement.
La règle n°31 (version étayée) a répondu «&nbsp;aucune production écrite exigée&nbsp;» et est passée
au vert&nbsp;: elle cherche des zones de rédaction pour vérifier qu'elles sont étayées, et une page
qui n'en a aucune lui échappe entièrement. **Une séquence vide passe mieux qu'une séquence
imparfaite.** C'est le pire réglage possible.

**La règle.** Toute phrase qui annonce une production — «&nbsp;production attendue&nbsp;»,
«&nbsp;complète le tableau&nbsp;», «&nbsp;rédige&nbsp;», «&nbsp;justifie&nbsp;» — engage un
**champ où l'élève écrit**, un **vérificateur**, une **correction** et une **sauvegarde**. Sinon la
consigne est décorative, et la séquence est un document à lire déguisé en activité.

**Mécanisation à faire** (branche Thème 2, avec les n°47, n°51 et n°54)&nbsp;: la n°31 doit
**échouer**, et non passer, quand une page emploie un verbe de production sans offrir un seul champ.
Le silence d'un outil n'est pas une preuve (n°47) — et son indulgence non plus.

**Ce qui n'est pas fait, et pourquoi.** La séquence n'est pas corrigée : elle appartient à un autre
auteur (règle n°66). Le constat est porté ici et dans la carte de couverture, qui sont nos fichiers
communs. Le code `5e_C1.2` est par ailleurs couvert depuis aujourd'hui par le lot Chengdu, dont
l'activité 1 fait exactement ce travail — trois principes pour une même fonction, cinq critères, et
l'obligation de nommer ce qu'on perd en choisissant.

**Un défaut de contenu, aussi, et c'est le nôtre autant que le sien.** L'aide de l'activité 1 écrit
«&nbsp;La fonction répond à&nbsp;: <i>À quoi cela sert-il&nbsp;?</i>&nbsp;», et l'en-tête du tableau
«&nbsp;Fonction&nbsp;: à quoi sert-il&nbsp;?&nbsp;». C'est **exactement** la confusion corrigée ce
matin dans le billet d'entrée du 5e_C2 : «&nbsp;à quoi ça sert&nbsp;» décrit le service rendu à
l'usager, pas la fonction technique. Deux séquences de deux auteurs différents portaient la même
erreur, ce qui indique moins une négligence qu'un **contresens partagé dans la discipline** — et
justifie la règle n°53 : une notion qui a une voisine se définit contre elle.

---

## Changement de gouvernance — 8 août 2026 : un seul auteur pour les trois thèmes

Pascal&nbsp;: «&nbsp;Il n'y a plus d'autres auteurs. Tu es en charge de la rédaction et de la
conception des 3 thèmes.&nbsp;»

Cette phrase lève la contrainte la plus ancienne du dépôt — *ne jamais modifier les lots existants
d'un autre auteur* — qui datait de l'époque où Fable, Codex et Grok produisaient en parallèle. Elle
a servi&nbsp;: elle a évité des écrasements et des doublons. Elle n'a plus d'objet.

**Ce qui change.** Toute ressource des trois thèmes peut désormais être reprise, corrigée,
refondue ou archivée par Fable, sans demander la permission d'un tiers qui n'existe plus. Les
séquences héritées cessent d'être un patrimoine intouchable pour devenir un **chantier**.

**Ce qui ne change pas — et c'est le point important.** La discipline qui entourait cette contrainte
ne venait pas de la propriété, mais de la prudence. Elle reste entière&nbsp;:

- **On ouvre avant d'écrire** (n°66, premier volet, et n°46). Une écriture qui n'a pas listé le
  dossier est un écrasement en puissance. Ce volet-là n'était jamais une question d'auteur.
- **On pille avant d'archiver** (n°12). Une ressource qu'on remplace a presque toujours quelque
  chose à donner&nbsp;: un cas, un mode opératoire, une question métacognitive. Le README d'archive
  dit ce qui a été repris et ce qui ne pouvait pas l'être.
- **On archive, on ne supprime pas.** `_archive-anciennes-versions/` garde la trace, avec la date
  et le motif.
- **On déclare la seconde route.** Quand deux ressources couvrent le même code, le dépôt ne choisit
  pas un vainqueur en silence&nbsp;: il dit en quoi elles diffèrent, pour que l'enseignant choisisse.

### Règle d'or n°66, amendée

**Ancien second volet**&nbsp;: «&nbsp;un fichier d'un autre auteur ne s'écrase jamais, même pour
l'améliorer&nbsp;».

**Nouveau second volet**&nbsp;: **une ressource qui fonctionne ne s'écrase jamais sans laisser de
trace, même quand elle nous appartient.** On la lit d'abord, on en tire ce qui vaut, on l'archive
avec le motif, et on écrit ce qu'on a repris. La propriété donne le droit de refondre&nbsp;; elle
ne donne pas celui d'effacer sans mémoire.

Le premier volet — *on ouvre le dossier avant d'y écrire* — est inchangé, et reste celui des deux
qui m'a réellement pris en défaut.

---

## Audit global des trois thèmes — 8 août 2026

Premier audit mené sur l'ensemble du dépôt depuis que Fable en a la charge complète. **39 séquences
vivantes** dans les trois thèmes (9 autres sont archivées et hors périmètre), passées à **neuf
contrôles mécanisés**.

### Ce que cet audit regarde — et ce qu'il ne regarde pas (règle n°47)

**Mécanisé, donc établi** : les consignes de production sans champ de saisie (n°67), la définition
de la fonction technique par « à quoi ça sert » (n°53), les blocs obligatoires de la règle n°4, le
mode essentiel (n°29), les corrigés absents derrière un Bonus (n°43), les appels réseau (n°40), les
variables de gabarit non remplacées, les sauvegardes locales manquantes.

**Non mécanisable, donc NON couvert** : la justesse pédagogique du contenu, la qualité des corrigés,
la progressivité réelle, l'ergonomie en classe. Ce rapport ne dit rien de ce qui s'enseigne bien.

Toutes les comparaisons normalisent apostrophes et accents. Le premier jet cherchait
« t'entraîner » avec une apostrophe droite et déclarait absents des blocs présents.

### Le résultat

| Règle | Défaut | Nombre |
|---|---|---|
| **n°40** | appel réseau (la page ne fonctionne pas hors ligne) | 26 |
| **n°43** | Bonus sans corrigé | 23 |
| **n°29** | mode essentiel absent | 16 |
| **n°67** | consigne de production sans aucun champ de saisie | 3 |
| **n°4** | bloc d'entraînement absent | 3 |
| **n°4** | bloc Bonus absent | 3 |
| **n°53** | fonction technique définie comme fonction d'usage | 3 |
| **n°49** | sauvegarde locale absente alors qu'il y a des champs | 1 |

| Thème | Manquements | Séquences en défaut |
|---|---|---|
| theme-1 | 23 | 10 |
| theme-2 | 35 | 17 |
| theme-3 | 20 | 7 |
**78 manquements sur 34 séquences.** Cinq séquences seulement sont mécaniquement propres, et ce sont
les cinq dernières produites : Chengdu 5e_C1, Pékin 3e_C2, Hangzhou 4e_C2, Shenzhen 3e_C3, Shanghai
5e_C3. Le gabarit actuel tient ; c'est tout ce qui le précède qui ne le suit pas.

### Ce qui compte vraiment, dans l'ordre

**1. Les erreurs enseignées — trois pages définissent la fonction technique par « à quoi ça sert »,
qui est la fonction d'usage.** `5e_C1.2` (freins), `4e_C4.1` (jardin connecté) et `4e_C4.1_book-train`.
Nuance importante pour les deux dernières : leur *intention* est juste — elles opposent la fonction
technique (« à quoi ça sert ») à la solution technique (« avec quoi on le fait »), et cette
opposition est excellente. C'est la *formulation* qui entre en collision avec la notion voisine. La
réparation n'est donc pas de supprimer l'opposition mais de la dire autrement : **ce que ça doit
FAIRE** contre **avec quoi on le fait**.

**Une quatrième page était en défaut : la mienne, corrigée le matin même.** J'avais réparé le billet
d'entrée du 5e_C2 et laissé, trois lignes plus bas, la capsule de révision qui répétait la même
définition fausse — plus l'ancienne triade des interacteurs, règles comprises. Le motif m'avait
échappé parce qu'il était coupé par un retour à la ligne. **Une correction qui n'a pas cherché
toutes les occurrences n'est pas une correction.** Corrigé, et les 47 tests du lot repassent.

**2. Trois séquences annoncent une production et n'offrent aucun champ** (n°67) : `5e_C1.2`,
`4e_C1.1` et `3e_C1.1` — les deux dernières étant les séquences « Tsinghua » de 12 ko. Ce sont des
documents à lire déguisés en activités.

**3. Vingt-trois Bonus sans corrigé** (n°43) : la dette annoncée en juillet, maintenant chiffrée.

**4. Vingt-six pages appellent le réseau** (n°40) : elles ne fonctionnent pas hors ligne, ce qui est
la promesse du dépôt.

**5. Seize pages sans mode essentiel** (n°29), trois sans bloc d'entraînement et trois sans Bonus.

### Ce que l'audit n'a pas pu faire, et qui revient à une branche Thème 2

L'outil vit dans `/tmp` : `_outils/` appartient au périmètre du Thème 2, et cette branche est une
branche Thème 1. Il doit y être versé, avec les mécanisations en attente — n°47 (périmètre déclaré),
n°51 (titre affiché), n°53, n°54 (nombres recalculés) et n°67. Et la n°31 doit être **retournée** :
elle passe au vert devant une page sans aucune zone de rédaction, si bien qu'une séquence vide se
note mieux qu'une séquence imparfaite.

---

### Lot livré — 5e_C1.2 « Sainte-Luce : quel frein pour les vélos du collège ? » (refonte)

Première **refonte complète** d'un lot existant depuis que Fable a la charge des trois thèmes, et
premier lot du dépôt à placer une **manipulation d'objet réel au parcours obligatoire** (règle
n°58) : un vélo, cinq minutes, aucun achat, trois versions 🅰🅱🅲 validées par le même vérificateur.

**Ce que la version précédente enseignait, et qui est corrigé** : « La fonction répond à : *à quoi
cela sert-il ?* » — la définition de la fonction d'usage — dans l'aide, dans l'en-tête du tableau et
dans les deux synthèses. Et une page qui annonçait **trois fois** une « production attendue » sans
offrir **aucun** champ de saisie (règle n°67). Elle en compte désormais 18 et 9.

**Ce qui a été repris** (règle n°12) : la situation de Sainte-Luce — seul ancrage martiniquais du C1
— le cas du freinage, l'exemple de l'éclairage, et surtout le jeu de données, **plus riche que
l'usage qu'on en faisait** : trois solutions et six critères chiffrés là où la séquence n'en
comparait que deux, qualitativement. Un second jeu a été ajouté, quinze relevés d'essai dont la
fiche est la moyenne exacte — l'élève peut donc la vérifier, et découvrir qu'une fiche technique
n'est qu'un résumé de mesures.

**La thèse du lot** : le mot difficile du référentiel n'est pas « principe », c'est **comparer**. Le
frein à patins gagne sur trois critères sur six — masse, prix, réparabilité — et c'est pourtant le
mauvais choix ici. Compter les colonnes revient à décider en silence que la masse pèse autant que la
distance d'arrêt sous la pluie, dans une descente, au bord de la mer. Le Bonus 1 referme la
démonstration : le **même tableau**, lu pour Fort-de-France, désigne les patins, sans qu'aucun
chiffre n'ait changé.

**Un geste nouveau dans le dépôt : le refus argumenté.** Le vérificateur de la séance 3 refuse le
frein à patins, cite le chiffre qui le disqualifie, et renvoie au Bonus où ce même choix devient le
bon. C'est le premier endroit où un refus indique **dans quel contexte la réponse serait juste**.
Un refus qui n'aide pas l'élève à repartir n'est pas un vérificateur, c'est un mur.

36 tests exécutés, 36 verts. Vérificateur de règles : 8 sur 8. Le dépôt passe de **27 à 28 codes
COMPLET ET VALIDABLE**, et le décompte des séquences mécaniquement propres passe de 5 à 7.

---

### Lot livré — 4e_C1.1 à C1.3 « Tsinghua : concevoir avant de connecter » (refonte)

**Le seul lot du dépôt bâti sur des données réelles et sourcées** : ministère de l'Intérieur,
JRC/EFFIS, ADEME Impact CO₂. Partout ailleurs nos jeux de données sont simulés — ce qui est
confortable, parce qu'on les range avant de les donner. Ici les unités ne se parlent pas, les
statuts sont hétérogènes et les périmètres incompatibles. **C'est ce qui fait le travail.**

**Ce que la refonte n'a pas touché.** Le fond. La leçon des unités, le proxy assumé, les quatre
équivalences et leurs périmètres, les garde-fous humains, le bloc CRCN — tout est passé
intégralement. L'audit du 8 août ne signalait qu'un motif, l'absence totale de champs de saisie
(n°67), et il avait raison ; mais il aurait été absurde de jeter le contenu avec la mécanique.

**Une leçon d'humilité, consignée parce qu'elle vaut.** Le bloc CRCN de la version précédente
portait cette phrase : «&nbsp;utiliser un ordinateur n'est pas une compétence&nbsp;; la compétence
est démontrée par les transformations et les traces&nbsp;». C'est **exactement la règle n°60**, que
j'ai écrite le 8 août à partir d'un audit extérieur, en croyant la découvrir. Elle était déjà dans
le dépôt, dans une séquence que je m'apprêtais à qualifier de défectueuse. **Le dépôt en savait plus
que moi sur ce point précis.**

**Ce que la refonte ajoute.** Les champs et les vérificateurs, une mesure de température dans la
cour (n°58) qui justifie le croisement de deux indices — sans elle c'est une consigne, avec elle
c'est une conclusion de l'élève —, deux corrigés graphiques, un QCM de 30 questions, deux synthèses,
et **deux refus argumentés** : une exigence qui nomme un composant, et l'oubli du mot
«&nbsp;passager&nbsp;» dans une équivalence.

**Un défaut que seul un test pouvait voir.** Mon découpage du script coupait entre les vérificateurs
et le bloc qui **attache les écouteurs aux boutons**. Cinq boutons muets, aucune erreur JavaScript,
une page qui se charge parfaitement et ne répond à rien. Une relecture ne l'aurait jamais vu.

42 tests exécutés, 42 verts. Vérificateur de règles : 8 sur 8. Le dépôt passe de **28 à 29 codes
COMPLET ET VALIDABLE**, et de 39 à 41 codes couverts par une séquence mutualisée.

---

### Règle d'or n°68 — Quand un lot s'appuie sur une catastrophe humaine, il dit ce qu'il compare et ce qu'il ne compare pas

**L'origine.** Cette règle ne vient pas d'un incident : elle vient d'une **réussite**, trouvée dans
la séquence 3e_C1.1 en la relisant pour la refondre. Son activité sur les évaluations
environnementales du PNUE à Gaza porte une consigne encadrée, que son auteur a nommée « phrase
éthique obligatoire » :

> «&nbsp;Nous comparons des indicateurs et des méthodes de mesure&nbsp;; nous ne comparons ni la
> valeur des vies, ni la gravité des souffrances, ni la légitimité des victimes.&nbsp;»

**Pourquoi c'est juste.** Un cours de technologie peut avoir besoin de données issues d'une guerre,
d'une catastrophe ou d'une épidémie — elles existent, elles sont publiques, et les ignorer
appauvrirait l'enseignement. Mais un tableur met tout sur la même ligne, et un graphique met tout à
la même échelle. **L'outil efface la différence de nature entre ce qu'on mesure et ce qu'on
éprouve.** La phrase rétablit cette différence, avant que l'élève ne l'ait perdue.

**La règle.** Tout lot qui exploite des données issues d'une catastrophe humaine énonce, **de façon
visible et non repliée**, ce qui est comparé — des indicateurs, des méthodes, des ordres de
grandeur — et ce qui ne l'est pas : la valeur des vies, la gravité des souffrances, la légitimité
des victimes. La leçon technique qui accompagne cette phrase est la plus solide qui soit :
**certaines grandeurs ne se convertissent pas les unes dans les autres**. Des débris, des cultures
détruites et une eau contaminée ne se remplacent pas par un chiffre carbone — ni par aucun autre
chiffre unique.

**Corollaire.** On ne va pas chercher ces données pour l'effet qu'elles produisent. On les emploie
quand elles servent la leçon — ici, l'incommensurabilité — et jamais comme illustration.

---

## Lot 3e_C1.1 à C1.4 — refonte du 9 août 2026

Troisième et dernière refonte de la série ouverte par l'audit du 8 août. Le lot « Tsinghua 3e »
était signalé pour un motif mécanique — aucun champ de saisie — et la lecture en a révélé un plus
grave&nbsp;: **il annonçait quatre codes et n'en servait qu'un**.

**Ce que la confrontation au référentiel a montré.** Le mot «&nbsp;rupture&nbsp;» n'apparaissait
nulle part, aucune découverte scientifique n'était nommée, les contraintes traitées étaient
techniques et non sociétales, et aucun des quatre codes ne figurait dans la page. Son contenu —
excellent — relevait en réalité du **traitement de données**, c'est-à-dire du C1 de 5e. Le lot était
rangé sous les mauvais codes, ce qui est la forme la plus discrète du défaut de la règle n°63.

**Ce qui a été fait.** Le contenu est conservé **intégralement** et devient la base factuelle. Deux
séances neuves l'encadrent&nbsp;: les trois régimes de surveillance des feux et le critère de la
rupture — *le métier change* — puis Herschel en 1800 et les deux siècles qui séparent sa mesure du
drone qui l'utilise. Et deux argumentaires courts en production terminale, dans les deux sens.

**Trois enseignements de méthode, notés pour la suite.**

1. **Le dépôt savait déjà.** Le bloc CRCN de la version 4e portait la phrase «&nbsp;utiliser un
   ordinateur n'est pas une compétence&nbsp;; la compétence est démontrée par les transformations
   et les traces&nbsp;» — c'est-à-dire la règle n°60, que nous avons cru découvrir hier grâce à un
   audit extérieur. Avant d'écrire une règle, il vaut la peine de chercher si le dépôt ne l'énonce
   pas déjà quelque part.
2. **La règle n°68 est née d'une réussite**, pas d'un incident. C'est la première du recueil dans ce
   cas. Il faudra en chercher d'autres&nbsp;: nos règles viennent presque toutes de nos erreurs, ce
   qui donne du recueil une image plus sombre que le dépôt ne le mérite.
3. **Deux fois dans la journée, un `cd` résiduel a fait écrire hors du dépôt.** Sans conséquence —
   les fichiers ont été récupérés et remis en place, jamais réécrits — mais c'est le genre de
   dérive qui finit par coûter cher. Désormais&nbsp;: chemins absolus, et jamais de confiance
   accordée au répertoire courant entre deux commandes.

**Bilan de couverture** — le dépôt passe à **30 codes COMPLET ET VALIDABLE** et 26 « À CRÉER ».

42 tests exécutés, 42 verts. Vérificateur de règles : 8 sur 8. Le dépôt passe de **28 à 29 codes
COMPLET ET VALIDABLE**, et de 39 à 41 codes couverts par une séquence mutualisée.

---

## Mécanisation de cinq règles, et retournement de la n°31 — 9 août 2026

Le vérificateur passe de **8 à 12 contrôles**. Les règles n°51, n°53, n°54 et n°67 étaient écrites
au journal et vérifiées à la main&nbsp;; elles sont désormais mécanisées. La n°47 s'applique à
l'outil lui-même&nbsp;: il imprime en fin d'exécution ce qu'il a regardé, ce qui relève du jugement
humain, ce qu'il ne couvre pas, et **quels fichiers il n'ouvre pas**.

### La n°31 était un piège

Elle répondait «&nbsp;SANS OBJET&nbsp;» — donc au vert — devant une page **sans la moindre zone de
rédaction**. Une séquence vide se notait ainsi mieux qu'une séquence imparfaite. C'est le pire
défaut qu'un contrôle puisse avoir&nbsp;: **récompenser l'absence**. Elle échoue maintenant quand
une page annonce une production sans offrir de champ, et renvoie à la n°67.

### Deux contrôles neufs se sont trompés, et ce sont eux qu'on a corrigés

**La n°51, première version&nbsp;: une liste noire de mots** — «&nbsp;SOS serre&nbsp;»,
«&nbsp;Packet Tracer&nbsp;», «&nbsp;adresse IP fixe&nbsp;». Elle a immédiatement accusé **quatre
séquences qui parlent légitimement de Packet Tracer**, dont celle qui s'appelle « SOS serre ». Une
liste de mots ne peut pas distinguer un reste de gabarit d'un sujet réel. Réécrite&nbsp;: le titre
affiché est comparé au **niveau et aux codes du fichier lui-même**. Un titre qui annonce un autre
niveau que son dossier est un reste de gabarit, quel que soit son vocabulaire. Zéro faux positif
depuis.

**Le vérificateur jugeait les archives.** `_archive-anciennes-versions/` contient précisément les
pages qu'on a remplacées parce qu'elles étaient en défaut&nbsp;: les compter revient à s'accuser
d'avoir corrigé. Le compte passait de 50 séquences à 39, et de 90 manquements à 50. Une archive est
une **trace**, pas une ressource — et le périmètre le dit maintenant.

### Ce que les nouvelles règles ont trouvé, et qui est corrigé

- **n°53** — deux séquences de Thème 2 définissaient la fonction technique par «&nbsp;à quoi ça
  sert&nbsp;», qui est la fonction d'usage. Leur **intention était juste** : elles opposent la
  fonction technique à la solution technique, et cette opposition est excellente. Seule la
  formulation entrait en collision avec la notion voisine. On a donc gardé l'opposition en la
  disant autrement — *ce que ça doit faire* contre *avec quoi on le fait* — et ajouté, dans le
  jardin connecté, le distracteur qui manquait : «&nbsp;une fonction d'usage&nbsp;».
- **n°54** — la séquence 5e_C4.7 annonçait 4 questions illustrées, le QCM en compte 6, tirées de
  5 documents. L'annonce dit maintenant les deux nombres.

### Une demi-correction rattrapée par le contrôle

En corrigeant le jardin connecté, j'ai d'abord changé **la valeur attendue par le vérificateur JS**
sans changer **le texte de l'option affichée**. Le billet d'entrée serait devenu insoluble&nbsp;:
aucune option ne correspondait plus à la bonne réponse. Trouvé en vérifiant que la valeur attendue
figure bien parmi les options — un contrôle qui porte sur ce qui est **rendu** (n°49). Une
correction à deux endroits doit toucher les deux, ou elle casse ce qu'elle prétend réparer.

### État après cette passe

**39 séquences vivantes, 50 manquements mécaniquement établis** — contre 78 relevés le 8 août sur
un périmètre plus large et avec quatre contrôles de moins. Le reste se concentre sur quatre
règles&nbsp;: mode essentiel (14), version étayée (12), accessibilité (10), tableau de bord (8).
Ce sont des ajouts de gabarit, pas des erreurs enseignées&nbsp;: ils peuvent attendre la rentrée.

### Règle d'or n°69 — On ne remet pas un colis sans avoir lu son étiquette

**L'incident.** Le 9 août, j'ai construit un bundle de livraison avec
`git bundle create X.bundle origin/main..HEAD` au lieu de
`origin/main..<nom-de-branche>`. Un bundle bâti sur `HEAD` n'empaquette **aucune référence
nommée**&nbsp;: il contient un commit anonyme. Pascal a exécuté les trois commandes du circuit et
reçu trois erreurs en cascade — `couldn't find remote ref`, puis `src refspec does not match any`,
puis l'échec de `gh pr create`. Les quatre bundles précédents étaient corrects&nbsp;; j'ai raccourci
sur celui-là.

**Le coût.** Un aller-retour complet, et trois messages d'erreur que rien ne rattachait à leur
cause réelle — le contenu du colis, pas les commandes de Pascal.

**La règle.** Avant toute remise, **on liste ce que le colis contient réellement** :

    git bundle list-heads <fichier>.bundle    # la référence attendue doit apparaître
    git bundle verify <fichier>.bundle        # et le prérequis doit être un commit de main

Un bundle se construit **toujours** avec le nom de branche, jamais avec `HEAD`. C'est le même
principe que la n°47 et la n°49, appliqué à la livraison&nbsp;: on ne déclare pas un test qu'on n'a
pas exécuté, et on ne remet pas un colis dont on n'a pas lu l'étiquette.

**Mécanisation.** Deux lignes dans le circuit de livraison de la méthode Fable, à exécuter avant
tout `SendUserFile`.

---

## 9 août 2026 — L'atelier de planification des tâches, et deux règles nées de mes propres fautes

### Ce qui a été livré

Le programme 2024 nomme, dans les connaissances associées de la gestion de projet :
« **Le diagramme de planification des tâches : notion de tâches, durée et contraintes entre
tâches.** » L'inventaire du 8 août avait compté **zéro occurrence** dans tout le dépôt, alors que
les trois codes C7.1 étaient revendiqués — et que la séquence de 3e, qui doit faire *élaborer* un
processus « avec des tâches identifiées », ne contenait pas une seule fois le mot « tâche ».

`atelier-planification/` répond à ce manque par **une ressource unique à trois parcours**, appelée
depuis les trois séquences C7.1 au moment du lancement de projet — la 5e **suit** un planning déjà
fait, la 4e l'**organise**, la 3e l'**élabore** et cherche le chemin le plus long. Trois refontes
auraient produit trois versions qui divergeraient ; une ressource partagée n'en produit qu'une.

L'atelier commence par des **bandes de papier découpées** — 2 cm par séance — et n'ouvre le logiciel
qu'après. La **voie B sans ordinateur** vaut la voie A partout, et pose les mêmes questions.

### Règle d'or n°70 — Une capture d'écran doit parler la langue du poste

**L'incident.** J'avais produit quatre schémas SVG de l'interface de GanttProject, dessinés à la
main faute d'avoir pu ouvrir le logiciel, avec des libellés **en anglais** : *Show critical path*,
*Predecessors*, *Duration*. Le `SOURCES_MEDIAS.md` du lot était pourtant honnête : il déclarait
noir sur blanc « ce ne sont pas des captures d'écran » et séparait le vérifié du non-vérifié. Cela
n'a rien sauvé. Pascal a envoyé deux copies d'écran de **son** poste : l'interface est en
**français**.

**Le coût.** Un élève qui cherche *Show critical path* dans une fenêtre où est écrit « Afficher le
chemin critique » ne trouve rien — et conclut que c'est lui qui se trompe. Une ressource
d'accompagnement qui égare est pire qu'une absence de ressource.

**La règle.** Quand un lot guide un geste dans un logiciel, **l'image doit montrer l'écran tel
qu'il apparaît sur le poste de l'élève** — même version, même langue. Si le logiciel est libre, on
l'ouvre et on capture. S'il est propriétaire (règle n°1), on ne le montre pas du tout et on
enseigne le geste autrement. **Un schéma reconstruit n'est acceptable que s'il ne prétend nommer
aucun bouton.**

**Conséquence pratique.** Les quatre SVG ont été supprimés. GanttProject 3.3 a été lancé sur le
poste, sur le fichier `jardin_connecte_brooklyn.gan` produit par le lot lui-même, et cinq écrans
ont été capturés aux moments choisis : la table des tâches, le champ *Durée*, l'onglet
*Prédécesseurs* avec sa relation *Fin-Début*, les barres, puis le même diagramme après *Afficher le
chemin critique*. GanttProject étant libre (GPL v3), reproduire son interface est permis — ce qui
n'était pas le cas de Packet Tracer, à l'origine de la règle n°1.

**Un corollaire, écrit dans l'atelier lui-même :** on ne dit jamais « les barres rouges ». La mise
en évidence est une hachure dans cette version, une couleur ailleurs. On dit « les tâches mises en
évidence » — c'est vrai partout.

### Règle d'or n°71 — Un corrigé qui n'est pas écrit par le calcul qui le vérifie n'est pas un corrigé

**L'incident.** `_verifier_planning.py` imprimait à l'écran des résultats **justes** : chemin le
plus long, tâches critiques, marges. À côté, `_corrige_calcule.json` — le fichier dont l'atelier
allait tirer ses questions et ses réponses — annonçait des marges **non nulles sur les tâches du
chemin le plus long**. C'est-à-dire l'inverse exact de ce que l'atelier enseigne.

L'explication est banale et c'est ce qui la rend dangereuse : le JSON avait été écrit à la main,
avant la correction du calcul des dates au plus tard, et le script qui imprimait les bonnes valeurs
ne les écrivait nulle part. Deux vérités coexistaient, l'une contrôlée et l'autre publiée.

**Le coût évité de justesse.** Trente questions de QCM et quatre exercices auraient été bâtis sur
des marges fausses, avec un vérificateur qui aurait refusé les bonnes réponses des élèves.

**La règle.** Le fichier de corrigé est **écrit par le script qui le vérifie**, jamais à côté. Et
le script ne l'écrit **que si tous ses contrôles passent** — un corrigé produit à partir d'un
calcul incohérent est pire que pas de corrigé. Après écriture, il **relit le fichier** et contrôle
qu'il redonne bien le résultat attendu.

C'est la règle n°54 (« un nombre établi ailleurs se calcule, il ne se recopie pas ») prise en
défaut chez moi, et poussée d'un cran : il ne suffit pas de calculer le nombre quelque part, il
faut que **le publieur soit le calculateur**.

**Mécanisation.** Trois blocs dans `_verifier_planning.py` : écriture conditionnée à `ok`,
relecture, contrôle de l'invariant sur le fichier relu. Et, côté page, un générateur qui fabrique
les tableaux, les questions **et les réponses attendues** à partir du même JSON — de sorte qu'une
réponse ne peut pas diverger de la question.

### Une décision de barème, au passage

Dans le parcours de 4e, les dates au plus tôt sont contrôlées **sans aucune tolérance**, alors que
les questions de raisonnement en admettent une. Une date fausse n'est pas une inattention : c'est
un calcul faux, et l'accepter apprendrait à l'élève que « à peu près » suffit sur un résultat de
calcul. La tolérance est légitime sur ce qui se discute, jamais sur ce qui se calcule.

---

## 9 août 2026 — Ce que le TP « Dé » de Pascal nous apprend sur le guidage pas à pas

Pascal m'a transmis un TP qu'il a **réellement mené en classe** et qui a marché : quatorze pages
pour construire un dé en CAO, du fichier vide jusqu'à la pièce colorée. Son commentaire vaut
cahier des charges : « **C'est long mais il arrive à être autonome et personne ne reste sur la
touche.** »

Ce TP est un objet d'étude. Il ne contient presque aucune phrase de cours, et pourtant il
enseigne. Voici ce que j'en retiens, sous forme de règles — parce que nous allons devoir écrire la
même chose pour Onshape, et trois fois.

### Règle d'or n°72 — Un guidage sépare typographiquement ce qu'on FAIT de ce qu'on doit VOIR

Dans le TP de Pascal, l'action est en noir (« Cliquez sur **Rectangle** ») et le retour attendu est
en couleur et en italique (« *Le pointeur prend la forme…* », « *Un point rouge apparaît sur
l'origine lorsque la souris est bien placée* »).

Ce second registre n'est pas du décor : c'est **le seul moyen qu'a l'élève de savoir qu'il vient de
se tromper**. Sans lui, l'erreur ne se découvre que trois étapes plus loin, quand plus rien ne
ressemble à l'image — et là il faut lever la main.

**La règle.** Toute consigne de manipulation logicielle s'écrit en deux temps : *le geste*, puis
*ce qui doit se produire à l'écran*. Deux registres visuellement distincts, toujours les mêmes.

### Règle d'or n°73 — Le nom d'un bouton se cite tel qu'il est écrit, avec son icône à côté

« Cliquez sur **Cotation intelligente** [icône] ». Le mot exact du logiciel, en gras, **et** l'image
du bouton. L'élève reconnaît l'icône avant d'avoir fini de lire le mot ; l'élève dyslexique la
reconnaît sans lire du tout.

C'est la règle n°70 (l'image doit parler la langue du poste) poussée d'un cran : **non seulement la
langue, mais le mot exact et le dessin exact.**

### Règle d'or n°74 — Avant de guider un geste imprécis, on autorise l'imprécision

Encadré orange de Pascal, page 2 : « *Il n'est pas nécessaire d'être précis dans les dimensions ;
les cotes exactes seront définies ultérieurement.* »

Sans cette phrase, un élève passe cinq minutes à essayer de tracer un rectangle de 50,00 mm à la
souris, échoue, et se croit nul. Avec elle, il trace n'importe quoi et avance.

**La règle.** Chaque fois qu'une étape produit un résultat volontairement approximatif, on le
**dit avant**, à l'endroit où l'élève va bloquer.

### Règle d'or n°75 — Toute valeur visible dans une capture est déclarée comme exemple

Deuxième encadré orange : « *La cote 74,13 est un exemple.* »

Sans cette ligne, une partie de la classe tape 74,13. Ce n'est pas de la bêtise : c'est de la
confiance dans le document. Un élève qui suit une consigne à la lettre a raison de le faire ; c'est
au document d'être clair sur ce qui est prescriptif et ce qui est illustratif.

### Règle d'or n°76 — L'aide décroît à mesure que le geste se répète

Le TP construit la **première** face en douze étapes détaillées, la **deuxième** en neuf étapes
allégées, et les **quatre dernières** en une ligne chacune avec l'image du résultat.

C'est la structure entière du document, et c'est elle qui produit l'autonomie. On ne devient pas
autonome parce qu'on nous dit de l'être : on le devient parce que l'étayage se retire, geste après
geste, assez lentement pour qu'on ne s'en aperçoive pas.

**La règle.** Un guidage qui répète le même niveau de détail du début à la fin n'apprend rien : il
fait exécuter. On détaille une fois, on allège la deuxième, on ne montre plus que le résultat
ensuite.

### Règle d'or n°77 — À chaque palier, l'image du résultat attendu

Le TP montre le cube après extrusion, le trou après enlèvement de matière, le dé après les congés,
le dé rouge à la fin. À chaque fois, l'élève **compare son écran à l'image** et sait tout seul s'il
est juste.

C'est très exactement le mécanisme qui fait que « personne ne reste sur la touche » : l'élève qui
doute n'a pas besoin du professeur, et le professeur reste disponible pour celui qui est vraiment
bloqué.

### Règle d'or n°78 — On enseigne à lire l'état du logiciel, pas seulement à cliquer

Page 2 : « *Les deux côtés du rectangle qui touchent l'origine sont en noir… Les deux autres côtés
sont en bleu. Ceci indique qu'ils sont sous-contraints et, de ce fait, libres de mouvement.* »

Rien n'oblige à dire ça pour finir le dé. Mais c'est le seul passage du TP qui enseigne une
**notion de CAO** : une esquisse est un système de contraintes, et le logiciel dit en permanence où
il en est. L'élève qui l'a compris se débrouillera dans n'importe quel modeleur ; celui qui a
seulement cliqué ne saura refaire que ce dé-là.

### Règle d'or n°79 — Le premier geste d'un TP est un geste de rangement

Avant la moindre esquisse : créer un dossier « Construction + Nom élève », un sous-dossier au nom
du TP, et enregistrer sous un nom **imposé**. Le TP y consacre sa deuxième page.

Un travail qu'on ne retrouve pas à la séance suivante n'a pas eu lieu. Et en salle de technologie,
avec des sessions partagées, c'est la première cause de séance perdue.

### Règle d'or n°80 — Le rituel d'enregistrement se répète à chaque palier, avec son icône

« Enregistrer le document [icône] » revient huit fois dans les quatorze pages. Ce n'est pas de la
redondance : c'est un **rituel**, et un rituel s'installe par la répétition à date fixe.

### Règle d'or n°81 — Un TP de prise en main ne pose aucune question de cours

Quatorze pages, zéro question à répondre. Pascal n'évalue pas la notion pendant qu'il enseigne
l'outil, et c'est pour ça que ça marche : l'élève n'a qu'une seule chose à faire à la fois.

C'est la n°59 (l'outil ne doit jamais devenir la compétence évaluée) et la n°61 (une évaluation ne
mesure qu'un construit à la fois) vues depuis l'autre bout : **on peut consacrer une séance
entière à l'outil, à condition de dire que c'est ce qu'on fait.** Les questions viennent après,
dans la séquence, sur la notion.

### Règle d'or n°82 — Un TP long se termine par une récompense visuelle gratuite

Les deux dernières pages colorent le dé en rouge et les creux en blanc. Techniquement : inutile.
Pédagogiquement : décisif. Après quatorze pages, l'élève repart avec **une image dont il est
fier**, et c'est ce qu'il montrera chez lui.

Aucune de nos séquences ne fait ça. Toutes finissent sur un bilan.

### Ce que ça change pour la suite

La progression CAO en Onshape reprendra cette architecture, avec les objets déjà décidés :
**5e — le dé** (prise en main : esquisse, cotation, extrusion, enlèvement de matière, congé,
apparence) ; **4e — l'assemblage** du dé et d'un socle de style romain, dé **centré sur l'axe du
socle** ; **3e — le boîtier étanche du capteur de confort**, où la forme n'est plus donnée mais
déduite d'un besoin.

Et le TP de Pascal reste sa propriété : il sert de **modèle de forme**, jamais de source de texte.

---

### Règle d'or n°83 — Une ressource partagée doit être atteignable depuis chaque code qu'elle sert

**L'incident.** Pascal, le 10 août : « *je suis en panique parce que je n'ai pas vu de diagramme de
Gantt* ». L'atelier de planification était pourtant livré, fusionné, et il contenait cinq vraies
captures de GanttProject. Mais depuis l'index du site, **il n'existait pas**.

`make_index.py` ne liste que les fichiers rangés directement sous
`<thème>/<Cx>/<niveau>/<niveau>_<code>/`. L'atelier, lui, vit dans un dossier commun
`atelier-planification/` un cran plus haut — précisément parce qu'il est **partagé** par les trois
niveaux et qu'on ne voulait pas le tripler. J'avais posé des liens dans les trois séquences C7.1,
et j'avais cru que cela suffisait. Cela ne suffit pas : personne ne trouve une ressource en ouvrant
d'abord une autre ressource.

**Ce que ça dit de plus général.** Mutualiser un contenu est presque toujours juste — c'est ce qui
empêche trois versions de diverger. Mais **mutualiser le contenu n'autorise pas à mutualiser
l'accès**. Un code du référentiel est une porte d'entrée ; si la ressource qui le sert n'est pas
derrière cette porte, elle n'existe pas pour celui qui cherche.

**La règle.** Toute ressource rangée hors des dossiers de code porte, **dans chaque dossier de code
qu'elle sert**, un <b>panneau indicateur</b> : une page courte qui dit ce qu'est la ressource,
pourquoi elle est ailleurs, ce que ce niveau-là y fait, et qui donne le lien. Le contenu reste en
**un seul exemplaire** ; seul l'accès est dupliqué.

**Mécanisation.** Les panneaux sont nommés d'après la ressource (`atelier_…`, `tp_…`), motif que
`make_index.py` reconnaît déjà et affiche comme « 🔧 Activité ». Trois panneaux ont été posés pour
l'atelier de planification, et l'index passe de 164 à 167 ressources.

### Règle d'or n°84 — On vérifie avant de demander

**L'incident, le même jour.** Pascal signale que le mini-projet de 5e annonce « 5e_C7 · 5e_C8 ·
5e_C9 », des familles et non des compétences. Ma réaction a été de lui **proposer** de vérifier
lesquels des douze codes étaient réellement servis. Sa réponse&nbsp;: « *pourquoi ne vérifies-tu pas
avant de produire une question&nbsp;? Or, on a mis des balises justement pour ne pas tomber dans ce
piège.* »

Il a raison. Le fichier était sur mon disque, le référentiel est dans `audit_couverture.csv`, et le
vérificateur existe. La réponse était à trente secondes.

**La règle.** Quand la réponse tient dans un fichier que j'ai sous la main, **poser la question
n'est pas de la prudence : c'est du travail renvoyé à l'autre**. On demande pour arbitrer un choix
qui appartient à Pascal — jamais pour établir un fait qu'on peut lire.

Le corollaire est plus dur, et c'est le vrai enseignement de la journée&nbsp;: une règle en prose
se contourne, y compris par celui qui l'a écrite. Les seules qui n'ont jamais échoué sont celles
qu'un script **refuse** de violer.

---

### Règle d'or n°85 — Un élève doit pouvoir dessiner l'objet avant qu'on lui en donne le nom

**L'observation.** Pascal, le 10 août, à propos du mini-projet de 5e&nbsp;: « *indicateur de
rangement pour le hall du collège&nbsp;: un élève peut se demander, qu'est-ce que c'est, à quoi ça
sert&nbsp;?* »

Il a raison, et la situation déclenchante le prouvait&nbsp;: trois lignes, dont « *on te demande un
indicateur simple&nbsp;: place de rangement libre ou occupée (LED + bouton ou capteur)* ». Un
indicateur n'est pas un objet, c'est une **catégorie**. On ne peut pas le dessiner, donc on ne peut
pas le vouloir.

**Ce qui se joue.** Une situation déclenchante n'a pas pour fonction d'annoncer le programme&nbsp;:
elle a pour fonction de faire **désirer un objet**. Tant que l'élève ne voit pas la chose, il
exécute des consignes — et tout le reste de la séquence, si bonne soit-elle, se fait sans lui.

**La règle.** L'objet d'une séquence se présente d'abord **en mots ordinaires et en images
mentales** : un lieu, une heure, quelqu'un qui a un problème, et la chose qu'il réclame décrite
comme il la décrirait. Le **mot du métier arrive après**, une fois la chose vue — jamais avant.

**Le test.** *Un élève qui vient de lire la situation déclenchante peut-il expliquer l'objet à son
voisin, en une phrase, sans employer un mot technique&nbsp;?* Si non, la situation déclenchante n'a
pas eu lieu.

C'est la règle n°62 (le concept prend le mot du programme, l'outil garde le nom du métier) appliquée
à l'entrée de séquence, et poussée d'un cran&nbsp;: **avant même les deux noms, il faut la chose.**

**Ce qui a été corrigé.** Le hall de la Brooklyn Middle School à huit heures moins dix, deux cents
élèves en huit minutes, vingt casiers sans porte où l'on ne voit pas lesquels sont libres, les sacs
posés par terre, trois chutes en un mois comptées par M. Alvarez — et sa demande, dans ses mots
à lui&nbsp;: «&nbsp;un petit voyant au-dessus de chaque case, vert elle est libre, rouge elle est
prise&nbsp;». Le mot *indicateur d'occupation* n'arrive qu'ensuite, avec ses cousins des gares et
des parkings.

Au passage, le bloc «&nbsp;Idée de départ&nbsp;» de cette séquence ne contenait aucune idée&nbsp;:
seulement une note technique sur la sauvegarde automatique. Il pose désormais la vraie question
d'ouverture — *comment ton voyant peut-il savoir qu'un sac est posé&nbsp;?* — avec un champ pour y
répondre, et on la relit au bilan.

---

### Règle d'or n°86 — Un bonus sans corrigé n'est pas un bonus, c'est un devoir non rendu

**L'origine.** Pascal, le 10 août&nbsp;: « *on disait aussi que le BONUS devrait toujours avoir des
corrections* ». L'audit du 8 août en avait déjà compté **vingt-trois** sans corrigé. J'avais moi-même
écrit, dans l'atelier de planification&nbsp;: « ces défis n'ont pas de vérificateur — on en discute
ensemble ». C'est une façon polie de dire que l'élève qui le fait chez lui, le soir, ne saura jamais
s'il a réussi.

**Ce qui se joue.** Le bonus s'adresse par construction à celui qui travaille **seul et sans
demande** — le plus autonome, souvent le plus rapide, parfois le plus discret. C'est exactement
l'élève qui ne lèvera pas la main pour demander la réponse. Lui refuser le corrigé, c'est punir la
curiosité.

**La règle.** Tout bloc bonus porte son **corrigé replié**. Pas nécessairement un vérificateur
automatique — un défi ouvert n'en a pas toujours — mais toujours **une réponse à lire**, écrite avec
le même soin que les corrections du parcours obligatoire&nbsp;: ce qui était attendu, pourquoi, et
l'erreur classique.

**Dette connue** : vingt-trois blocs bonus du dépôt sont dans ce cas. À traiter groupé, après les
trois séquences en cours.

### Règle d'or n°87 — LA CLÉ DE VOÛTE : toute séance qui s'appuie sur un prérequis s'ouvre par un rappel de ce que l'élève a déjà fait

**L'origine.** Pascal, le 10 août, à propos du découpage de l'atelier de planification&nbsp;:
« *il faudrait que ce soit à part, avec un rappel spiralaire de ce qu'il a fait l'année dernière* ».
Puis&nbsp;: « *le rappel spiralaire devrait être une règle d'or et même clé de voûte, pour toutes
les séances qui font appel à des prérequis. Ça me rappelle mon prof de maths en IUT.* »

**Pourquoi «&nbsp;clé de voûte&nbsp;» et pas simplement «&nbsp;règle&nbsp;».** Une clé de voûte
n'est pas la plus grosse pierre&nbsp;: c'est celle sans laquelle les autres tombent. Un cycle de
quatre ans n'est pas quatre années juxtaposées&nbsp;; c'est **la même poignée de notions revisitées
avec un verbe plus exigeant**. Si le rappel manque, l'élève ne vit pas une progression&nbsp;: il vit
une succession de nouveautés, et il oublie chaque été ce qu'il a fait l'année précédente. Toutes nos
autres règles supposent silencieusement cette continuité — la n°65 (une notion traverse les niveaux
en changeant de verbe, pas de sujet) n'a aucun effet si personne ne dit à l'élève qu'il traverse.

**La règle.** Toute séance qui mobilise un prérequis **s'ouvre** par un rappel court et concret de
ce que l'élève a **déjà produit**, et nomme explicitement ce qui change cette année.

**La forme.** Le rappel nomme une **production**, pas une notion&nbsp;:

> «&nbsp;L'an dernier, tu as **suivi** un planning qu'on t'avait donné&nbsp;: tu disais ce qui était
> en retard et ce que ce retard décalait. Cette année, c'est **toi** qui l'organises.&nbsp;»

et non «&nbsp;tu as vu la planification en 5e&nbsp;». Un élève ne se souvient pas d'une notion&nbsp;;
il se souvient de ce qu'il a **fait**. Et si le prérequis n'a pas été vu — élève arrivé en cours de
cycle, année sautée, séquence non faite — le rappel doit être **suffisant en lui-même** pour que la
séance reste possible. Un rappel qui suppose le passé exclut celui qui ne l'a pas.

**Ce que ça implique pour l'audit à venir.** La prochaine inspection générale des séquences vérifiera
cette clé de voûte **en action**, séquence par séquence&nbsp;: le rappel existe-t-il, nomme-t-il une
production, dit-il ce qui change&nbsp;? C'est mécanisable en partie — la présence d'un bloc de rappel
en ouverture, et le fait qu'il cite un verbe d'action plutôt qu'un nom de notion.

**Calendrier arrêté avec Pascal** : la clé de voûte s'applique d'abord aux trois séquences en cours
(5e, 4e, 3e du Thème 3). L'audit général vient **après**, une fois ces trois-là terminées.

---

## Feuille de route notée le 10 août — la révision générale

Décision de Pascal, écrite ici pour ne pas être oubliée&nbsp;:

> «&nbsp;Après avoir terminé la séquence de 5e, 4e et de 3e, on va transposer ce savoir et les
> autres aussi aux autres séances, donc on va faire une révision générale.&nbsp;»

**L'ordre est arrêté** :

1. **Terminer les trois séquences du Thème 3** — 5e, 4e, 3e — en y appliquant tout ce qui a été
   appris ces jours-ci&nbsp;: objets reconnaissables (n°85), pages séparées par niveau, rappel
   spiralaire en ouverture (n°87), captures dans les corrections, bonus corrigés (n°86).
2. **Elles servent alors d'étalon.** C'est sur elles qu'on jugera de ce que doit être une séquence
   du dépôt — pas sur une liste de règles, sur trois exemples qu'on peut ouvrir.
3. **Révision générale** de toutes les séquences existantes, à l'étalon de ces trois-là, avec le
   guidage transposable (`GUIDAGE_PAS_A_PAS.md`) et les vérificateurs mécanisés.

**Pourquoi cet ordre et pas l'inverse.** Réviser trente-neuf séquences contre un recueil de
quatre-vingt-sept règles écrites, c'est trente-neuf jugements subjectifs. Les réviser contre **trois
séquences exemplaires** qu'on peut ouvrir côte à côte, c'est une comparaison. Et ce qui aura résisté
à l'usage sur trois lots mérite d'être imposé aux trente-six autres — ce qui n'y aura pas résisté
sera abandonné avant d'avoir coûté trente-six fois.

---

## 10 août 2026 — Le dé de 5e est modélisé, et ce que ça nous apprend

Six des seize images du TP de 5e sont faites : les résultats de palier `R2` à `R7`,
produits par l'**API Onshape** et non à la souris. Le mur qu'on avait rencontré — le
canevas 3D n'accepte ni mouvement de souris ni frappe pilotés — se contourne par
l'API REST, qui ne passe pas par le canevas. C'est le seul chemin fiable vers des
images 3D produites sans intervention humaine, et il faut le retenir.

**Trois enseignements, plus durables que les images.**

**Un contrôle ne vaut que s'il porte sur la pièce, pas sur l'intention.** Une face du
dé a d'abord été percée au mauvais endroit — une hypothèse fausse sur l'origine du
repère d'esquisse des faces latérales, un creux mal placé, l'autre tombé hors de la
face et silencieusement ignoré par le logiciel. Ce n'est pas le rendu qui l'a
attrapé : c'est le relevé des positions réelles des cylindres. On a compté 21 creux
répartis 1 · 6 · 2 · 5 · 3 · 4, paires opposées à 7, puis recoupé à l'œil sur les six
vues orthogonales. Même esprit que la règle n°71 : ce qui vérifie doit lire le
résultat, pas l'énoncé.

**Un signal peut être faux sans être une erreur.** Le centroïde annoncé à l'origine
paraissait impossible avec un creux en haut et six en bas. C'était un artefact : sans
matériau affecté, Onshape renvoie un tenseur dégénéré. Seul le volume était
exploitable — et il tombait exactement sur 125 000 − 21 × π × 5² × 5. Douter du signal
avant de douter de la pièce, puis vérifier autrement.

**Ce qu'on voit à l'écran n'est pas ce qui est dans le fichier.** Les PNG rendus par
`/shadedviews` ont un fond **transparent**. À l'écran ils apparaissaient sur blanc,
composités par l'outil ; sur disque, ils s'affichaient sur noir. Il a fallu les aplatir
après coup. À retenir pour toute image livrée : **contrôler le fichier, pas l'aperçu**.

**Limite d'outil consignée.** Les constructeurs d'extrusion et de congé du plugin
Onshape émettent un champ `libraryRelationType: "NONE"` que l'API rejette (HTTP 400,
`BTWeirdStringValueException`). Les esquisses passent, ces deux-là non ; on est passé
en REST direct. À savoir avant la prochaine séance de modélisation.

**Reste à la main** : `tp5e_R1_carre.png` (une esquisse sans matière ne se rend pas
ombrée) et les neuf captures d'interface, qui doivent montrer les panneaux d'Onshape
**en français** (règle n°70). Les prendre, c'est aussi tester le TP — et le seul
chiffre qui compte reste le nombre de fois où l'on ne sait pas quoi cliquer.

---

## Règle d'or n°88 — une page se juge aussi sur ce qu'on peut en faire quand on y est arrivé

> **Toute page destinée aux élèves doit être atteignable depuis l'index, dire
> d'où l'on vient et où l'on va, et porter un lien de retour vers sa séquence.**

Née d'un constat de Pascal, arrivé sur le panneau indicateur de 4e : « j'aimerais
savoir cet atelier va après quoi, et comment retourner à la séquence pédagogique —
il n'y a pas le retour vers l'accueil ». Puis, une fois le correctif livré :
« on entrait dans l'atelier sans pouvoir en ressortir — je l'ai compris après ».

C'est la **troisième fois** que la même famille de défaut nous coûte du temps, et
c'est ce qui justifie une règle plutôt qu'un correctif de plus :

1. l'atelier de planification existait mais n'était listé nulle part — invisible ;
2. les dossiers en `_` étaient exclus par Jekyll — publiés mais en 404 ;
3. l'atelier s'ouvrait sans aucun chemin de retour — une impasse.

Chaque fois, le **contenu était juste**. C'est le chemin qui manquait. Un défaut de
contenu se voit à la relecture ; un défaut de chemin ne se voit qu'en se mettant à
la place de quelqu'un qui n'a pas construit la page. Celui qui l'a écrite sait
toujours d'où il vient : c'est précisément l'angle mort.

### Les quatre questions, du point de vue de l'élève

**Comment j'arrive ici ?** La page est listée dans l'index et atteignable depuis
chaque code qu'elle sert (règle n°83).
**Où suis-je ?** Un fil d'ariane, ou au minimum une phrase qui situe le moment dans
la séquence : après quoi, pour combien de temps, avant quoi.
**Comment je repars ?** Un lien de retour vers **sa** séquence — celle de son
niveau, pas un index générique.
**Et ensuite ?** La suite est nommée : le QCM, l'activité d'après, le bilan.

### Ce qui est mécanisable

Un contrôle par page destinée aux élèves : elle apparaît dans `index.html` ; sa
barre de navigation existe ; **chacun de ses liens résout vers un fichier qui
existe** ; au moins un de ces liens pointe vers une séquence. Ce dernier point est
le cœur — c'est lui qui distingue une page d'une impasse. Le contrôle se fait sur
les fichiers, pas sur l'intention : on suit les liens, on ne les lit pas.

### Le corollaire, pour les refontes

Quand une page est découpée ou renommée, les textes qui la décrivaient ailleurs
deviennent faux **en silence**. Le découpage de l'atelier en trois pages a laissé
derrière lui deux consignes mortes — « choisis l'onglet 4e », alors que l'onglet
n'existait plus, et « c'est la même page pour tout le monde », devenu faux. Elles
n'ont été vues que parce qu'on relisait la page pour une autre raison. Toute
refonte doit donc **relire ce que les autres pages disent de celle qu'on change**.

---

## 11 août 2026 — La progression CAO est complète, et le dépôt s'est fait auditer

Les trois TP de prise en main existent : le dé en 5e, le dé sur son socle en
4e, le boîtier étanche en 3e. Ce qui les tient ensemble n'est pas la
difficulté des outils — la révolution n'est pas plus dure que l'extrusion —
mais **l'enjeu**. En 5e une pièce ratée reste jolie à l'écran ; en 4e elle ne
s'assemble pas, et ça se voit tout de suite ; en 3e elle prend l'eau, et on ne
l'apprend qu'à la première averse. C'est cette montée-là qu'un élève doit
sentir, et c'est elle que le rappel spiralaire nomme à chaque niveau.

Le lot est complété : fiche pédagogique, synthèse élève, synthèse professeur,
manifeste, et les trois relevés de captures engendrés depuis les scénarios —
ils ne peuvent donc pas se désynchroniser des TP.

**La problématique de la CAO est écrite** : *comment décrire un objet assez
précisément pour qu'une machine le fabrique sans nous ?* Elle rend enfin
lisibles C7.2 et C7.6, qui flottaient. Pascal avait posé la question — cette
compétence ne mérite-t-elle pas une problématique à part entière ? — et la
réponse est oui : sans elle, l'élève apprend un logiciel sans savoir à quelle
question il répond.

### L'audit d'harmonisation

Pascal, avant de se coucher : « il y a certains TP, certaines séances qui
mériteront une certaine harmonisation ». Le script `audit_spiralaire.py`
passe les 181 pages du dépôt au crible des règles mécanisables et écrit
`AUDIT_HARMONISATION.md`. Le rapport est **engendré**, jamais rédigé : il se
régénère d'une commande et ne peut pas mentir sur l'état réel.

Ce qu'il trouve, par ordre de rentabilité :

**31 séances de 4e et de 3e sans rappel spiralaire.** C'est le chantier qui
change quelque chose pour l'élève, et il demande de remonter la progression
pour savoir ce qui précède. C'est là que se joue la cohérence du cycle.

**47 pages sans sortie** — presque toutes des synthèses et des QCM sans barre
de navigation. Mécanique, rapide, corrigeable par lot puisqu'elles partagent
leur gabarit.

**3 pages aux images manquantes** (les TP de CAO, en cours), **1 bonus sans
corrigé** — bien moins que les 23 craints, mais à vérifier à la main avant de
conclure : un chiffre bas peut vouloir dire « tout va bien » ou « le script ne
voit pas » —, et **84 pages qui appellent le réseau**, dette ancienne et
assumée.

### Ce que cet audit ne dit pas, et qu'il faut se répéter

Un script détecte l'**absence** d'un bloc, jamais la **platitude** de son
contenu. Une séance peut porter un rappel spiralaire parfaitement conforme et
parfaitement inutile : « tu as vu les capteurs en 4e » coche la case et
n'apprend rien. Les trois questions qui comptent — le rappel nomme-t-il une
**production**, dit-il ce qui **change**, tient-il debout pour celui qui
n'était pas là — ne se mesurent pas. Elles se lisent.

Le rapport le dit lui-même dans son périmètre. C'est la même discipline que
pour les vérificateurs de guidage : dire ce qu'on contrôle, et surtout ce
qu'on ne contrôle pas.

---

## 11 août 2026 (suite) — l'audit au navigateur, et ce qu'il a trouvé chez les autres

Pascal a demandé un audit de tout ce qui a été produit précédemment, sur les
trois thèmes. Le script statique avait déjà nettoyé beaucoup ; c'est le
**navigateur** qui a trouvé le reste, et l'écart entre les deux mérite d'être
écrit.

### Ce qu'un script qui lit le HTML ne peut pas voir

**Une page morte qui a l'air vivante.** La séquence de cybersécurité de 4e
contenait `document.getElementById('score1a')?.textContent = ...` — un `?.` à
gauche d'une affectation, ce que JavaScript interdit. Ce n'est pas une erreur
d'exécution : c'est une erreur de **syntaxe**, donc le navigateur refusait
**tout** le bloc de script. Vingt-sept boutons, cent vingt-cinq éléments
interactifs : rien ne fonctionnait. À la lecture du fichier, la page semblait
complète. Deux autres défauts se cachaient derrière : un `startTime` jamais
déclaré, et deux accès à des éléments inexistants (`#saveBtn`, `#scoreTotal2`)
qui interrompaient le script à la première interaction. Les trois sont
corrigés ; les fonctions dont l'élément n'existe pas sont signalées en clair
dans le fichier plutôt que masquées.

**Des images invisibles dans le code.** Un QCM du thème 2 chargeait six images
de Wikimedia **injectées par JavaScript** — donc absentes du HTML, donc
invisibles à tout script qui lit le fichier. Quarante balises cassées hors
connexion. Remplacées par six schémas originaux.

### Ce que le navigateur croit voir à tort

Il a fallu apprendre à l'audit à ne pas crier au loup, ce qui compte autant.
Un `<img>` **sans attribut src** est un emplacement que le script remplira, pas
une image cassée. Une image en **chargement paresseux** située sous la ligne de
flottaison n'est pas chargée tant qu'on n'a pas défilé : sans défilement, on les
compte toutes comme mortes. Et un **gabarit** n'est pas une page — `@@CHECKS@@`
n'est pas une faute de JavaScript. Trois faux positifs écartés, sinon le rapport
aurait annoncé seize défauts là où il y en avait deux, et un audit qui crie au
loup finit par ne plus être lu.

### Les liens vers ChatGPT

Deux pages de 4e proposaient d'« ouvrir ChatGPT » d'un clic. Le service exige
un compte, un âge minimum de 13 ans, et l'accord d'un adulte avant 18. Le lien
direct est remplacé par un encadré qui pose les trois conditions — dont
l'accord de l'établissement — et rappelle que **tout ce qu'on écrit à un
assistant part sur les serveurs de l'entreprise qui le fait tourner**. Ce qui
est, exactement, le sujet de cette séquence-là. L'intention pédagogique est
conservée, l'envoi automatique ne l'est pas ; la décision finale appartient à
Pascal.

### L'outil qui manquait

`audit_navigateur.py` rejoint `audit_spiralaire.py` : le premier ouvre chaque
page dans Chromium, le second lit les fichiers. Aucun des deux ne remplace
l'autre. Écrit noir sur blanc dans leur périmètre : *un script sans erreur peut
être un script qui ne fait rien* — la justesse des réponses et le fait que la
page enseigne quelque chose ne se mesurent toujours pas.

**État après ce chantier : 181 pages, aucune erreur JavaScript, aucune image
cassée, aucun manquement aux règles n°86, n°87 et n°88.**

---

## 11 août 2026 — Les trois TP de CAO sont complets

Seize rendus produits par l'API Onshape. Les TP de 4e et de 3e passent les onze
règles de guidage sans manquement ; celui de 5e attend encore ses neuf captures
d'interface, qui ne s'obtiennent qu'à la main sur un poste en français.

**Ce que les contrôles ont vraiment prouvé.** Le dé reconstruit pour la 4e fait
115 482,72356945986 mm³ contre 115 482,72356945979 pour l'original de 5e —
identiques à treize chiffres. La gorge du boîtier est prouvée continue non pas à
l'œil mais parce que son fond est **une seule face** de 136,00 mm², exactement
l'aire de l'anneau complet : une rainure interrompue à un coin aurait donné deux
faces. Le centrage du dé est à 0,00 mm, et il est tenu par une contrainte
résolue, pas par des coordonnées saisies. Le jeu du joint mesure 0,50 mm.

**Un chiffre corrigé.** Les 116 753 mm³ notés la veille pour le dé étaient le
volume **avant** congés. Après les congés de 3 mm et de 1 mm : 115 482,72 mm³.

**Une leçon d'image qui devient une leçon de méthode.** Le premier rendu de la
coupe de 3e était inutilisable : nervure et gorge faisant 1 mm chacune et
jointives, dans une même teinte on ne distinguait rien. Il a fallu colorer les
deux pièces pour que l'image enseigne quelque chose. C'est exactement ce qu'on
reproche à une image décorative — sauf qu'ici elle était géométriquement juste
et pédagogiquement vide. **Une image correcte n'est pas une image qui montre.**

**Une limite d'outil devenue contenu du TP.** `create_fastened_mate` aligne les
axes Z des connecteurs au lieu de les opposer : mater le dessous du dé sur le
dessus du socle le retourne et l'enfonce. Plutôt que de cacher le contournement,
le TP de 4e prévient maintenant l'élève que le cas arrive « à tout le monde » et
lui indique le bouton d'inversion. Un piège rencontré en production vaut mieux
qu'un piège découvert en classe.

**Trois limites déclarées dans SOURCES_MEDIAS.** La coupe de 3e n'est pas une
coupe des pièces de production mais une reconstruction — l'API publique
d'Onshape ne sait pas produire de vue en coupe — prouvée équivalente au volume.
Le profil de 4e n'est pas un rendu Onshape mais un tracé de l'esquisse réelle.
Et l'image du couvercle est honnête, mais peu démonstrative : à l'échelle de la
pièce entière, la nervure de 1 mm reste un liseré.

---

## 11 août 2026 — Le TP nommait des boutons qui n'existent pas

Pascal a commencé à dérouler le TP de 5e pour en prendre les captures. Il n'a
pas eu à aller loin&nbsp;: dès le deuxième palier, il a demandé « après avoir
cliqué sur Esquisse, quel plan je choisis ? ». Le TP répondait « le plan
**Top** ». Ses captures montrent que dans l'interface française d'Onshape, la
liste de gauche affiche **Origine, Haut, Avant, Exact**. Un élève qui cherche
« Top » ne le trouve pas.

Trois écarts relevés, tous du même genre&nbsp;:

- `Top` / `Front` / `Right` → **Haut** / **Avant** / **Exact** dans l'arbre.
  (« Exact » est la traduction — mauvaise — que fait Onshape de *Right*. La
  règle n°73 impose de citer le bouton **tel qu'il est écrit**, même quand
  c'est écrit mal.)
- `Part Studio` → **Partie Studio**, et le document s'ouvre avec **deux**
  onglets, pas un&nbsp;: *Partie Studio 1* et *Assemblée 1*.
- Le champ du panneau affiche **Haut du plan** une fois le plan choisi.

Et un piège qu'aucune traduction ne résout&nbsp;: les étiquettes dessinées
**dans la zone 3D** sont restées en anglais (*Top*, *Front*, *Right*) alors que
la liste de gauche est en français. Le même plan porte deux noms sur le même
écran. Le TP le dit maintenant explicitement — c'est exactement le genre de
détail qui fait lever une main.

### Ce que ça confirme

La règle n°70 disait qu'une capture doit parler la langue du poste. Il faut
l'étendre&nbsp;: **le texte aussi**. Un TP rédigé d'après une documentation
anglophone décrit un logiciel que l'élève n'a pas sous les yeux, et aucune
relecture ne le révèle — seul le fait de dérouler le TP sur le poste réel le
montre.

Et la méthode a fonctionné exactement comme prévu. Le TP est écrit pour
quelqu'un qui ne connaît pas le logiciel&nbsp;; le faire dérouler par quelqu'un
qui ne le connaît pas vraiment était le meilleur test possible. Deux questions
posées, trois défauts trouvés, et ils étaient dans le TP, pas chez le lecteur.

Les trois scénarios — 5e, 4e, 3e — sont corrigés d'un coup&nbsp;: les mêmes
termes anglais s'y étaient propagés.


---

## Règle d'or n°89 — un nombre sans son unité n'est pas une mesure

*11 août 2026. Trouvée en déroulant l'export du TP de 5e sur poste réel.*

La fenêtre d'export STL d'Onshape propose **Mètre** par défaut. Un dé de 50 mm
part alors dans le fichier sous la forme du nombre `0,05`. Le fichier est
valide, la géométrie est exacte, l'imprimante obéit — et fabrique un grain de
cinquante microns. Rien n'a échoué&nbsp;: la description était juste, l'unité
manquait, et la machine s'est trompée d'un facteur mille.

**Toute grandeur qui sort d'un logiciel pour entrer dans un autre doit être
accompagnée de son unité, et le TP doit faire vérifier cette unité comme un
geste à part entière — pas comme une remarque.** Un réglage par défaut n'est
pas un choix&nbsp;: c'est ce que quelqu'un d'autre a choisi pour nous.

### Pourquoi c'est une règle et pas une astuce

Parce que c'est la problématique de la séquence CAO prise en flagrant délit&nbsp;:
*« comment décrire un objet assez précisément pour qu'une machine le fabrique
sans nous ? »* La réponse que donne ce piège est plus forte que n'importe quel
cours&nbsp;: la précision ne suffit pas, il faut aussi que la machine et nous
parlions de la même chose. Un STL ne contient que des nombres&nbsp;; c'est
l'humain qui garantit ce qu'ils signifient.

### Portée

Au-delà de la CAO&nbsp;: une tension relevée sans « V », une durée de séance
sans « min », une vitesse sans « km/h » dans un tableau d'élève relèvent du
même défaut. Partout où un lot fait transiter une valeur — export, saisie,
tableau, capteur — l'unité fait partie de la valeur.

### Ce qui est mécanisé

Rien, pour l'instant, et il faut le dire&nbsp;: aucun script ne peut savoir
qu'un `50` désigne des millimètres. Ce qui est mécanisable, en revanche, c'est
la **présence** d'une unité à côté d'un nombre dans une consigne d'export.
À écrire dans `verif_guidage.py` quand un deuxième cas se présentera&nbsp;:
une règle se mécanise sur deux occurrences, pas sur une.

---

## Règle d'or n°90 — un rituel qui demande un geste impossible fabrique du doute

*11 août 2026. Relevée par Pascal en lisant la page du TP de 5e.*

La règle n°80 impose un rituel d'enregistrement à la fin de chaque palier. Elle
a été écrite pour des logiciels où l'on perd tout si l'on oublie. Onshape
enregistre en continu et **n'a pas de bouton Enregistrer** — le TP le dit
lui-même au premier palier. Résultat&nbsp;: la page expliquait qu'il n'y a pas
de bouton, puis demandait neuf fois d'appuyer dessus.

**Quand un rituel mécanisé rencontre un logiciel qui ne fonctionne pas comme
celui pour lequel la règle a été écrite, on tient l'INTENTION de la règle, pas
sa lettre — et on le mécanise, au lieu de le corriger à la main.** Le scénario
porte désormais un drapeau `logiciel_sans_enregistrement`, et le rituel devient
un **point de reprise**&nbsp;: « tu n'as rien à enregistrer, c'est déjà fait,
tout seul, depuis le début ; si le poste redémarrait maintenant, tu retrouverais
ton travail exactement ici. »

### Ce que ça coûte de ne pas le faire

Un élève de 5e qui lit deux consignes contradictoires ne conclut pas que le TP
se trompe&nbsp;: il conclut qu'il n'a pas compris. Une contradiction visible
coûte plus cher qu'une lacune, parce qu'elle attaque la confiance dans tout le
reste du document.

### Portée

Tout logiciel à sauvegarde continue ou en ligne — Onshape, les suites
bureautiques en ligne, Vittascience, Scratch en ligne. À l'inverse, le rituel
d'origine reste indispensable pour GanttProject, LibreOffice hors ligne,
l'IDE Arduino, Packet Tracer&nbsp;: là, un oubli fait vraiment perdre la séance.
Le drapeau se pose scénario par scénario, jamais globalement.

### Ce qui est mécanisé

Le texte du rituel, dans `build_tp.py`. Ce qui ne l'est pas&nbsp;: décider si un
logiciel enregistre seul. Cela se constate en l'utilisant — et c'est exactement
ainsi que celui-ci a été trouvé, en déroulant le TP sur un poste réel.

---

## Règle d'or n°91 (clé de voûte) — quand une affirmation surprend, donner le moyen de la vérifier

*11 août 2026. Trouvée par Pascal en déroulant le TP de 5e, dans le prolongement
de la n°90.*

Le TP annonçait qu'Onshape enregistre tout seul et qu'il n'existe pas de bouton
Enregistrer. C'est vrai, c'est surprenant, et l'élève n'avait qu'une chose à
faire de cette information&nbsp;: **croire le professeur**.

**Toute affirmation qui contredit l'expérience de l'élève doit être suivie du
geste qui permet de la vérifier — immédiatement, et par lui.** Pas plus tard,
pas ailleurs dans le document&nbsp;: au moment où elle surprend.

Ici&nbsp;: « clique sur le logo Onshape, rouvre ton document — tout est là. »
Trois clics, et l'affirmation devient un constat.

### Pourquoi c'est une clé de voûte et pas un détail de rédaction

Parce que ce qui est transmis n'est pas l'information mais le **moyen de la
vérifier**. Un élève à qui l'on a montré comment vérifier saura le refaire dans
un autre logiciel, l'an prochain, sans nous. Un élève à qui l'on a demandé de
croire dépend de celui qui affirme — et se retrouve démuni dès qu'il change
d'outil ou de professeur. C'est la différence entre enseigner un fait et
enseigner un rapport aux faits&nbsp;; le second est le seul qui survive à la
sortie du collège.

Corollaire pour l'auteur du lot&nbsp;: **si l'on ne sait pas décrire le geste de
vérification, c'est peut-être qu'on n'a pas vérifié soi-même.** L'affirmation
mérite alors d'être testée avant d'être écrite (règle n°71).

### Ce qui est mécanisé

Rien. Aucun script ne sait reconnaître qu'une phrase surprendra un élève de 5e.
Ce qui se relève, en revanche, c'est la présence d'un geste vérifiable après
chaque affirmation contre-intuitive — et ça, seule une relecture humaine le
fait. Elle se conduit en salle, ou en déroulant le TP comme Pascal l'a fait.

---

## Règle d'or n°92 — une image qu'on ne peut pas agrandir est une image qu'on ne peut pas lire

*11 août 2026. Demandée par Pascal, qui n'arrivait pas à lire une capture
d'écran dans le TP de 5e.*

Les images du dépôt sont des **documents à lire** (règle n°1), pas des
décorations. Une capture d'interface au huitième de sa taille, un schéma
réseau, un Gantt&nbsp;: à la largeur d'une colonne de texte, le texte qu'ils
contiennent est illisible. L'élève voit qu'il y a quelque chose, et ne peut pas
le lire — ce qui est pire que ne rien montrer, puisqu'il sait qu'il lui manque
une information.

**Toute image d'une page destinée aux élèves doit pouvoir s'agrandir&nbsp;:
d'un clic, d'une touche au clavier, et se refermer par Échap.** Sans
bibliothèque, sans réseau, sans donnée envoyée — comme le reste du dépôt.

### Ce que ça implique, au-delà du clic

L'agrandissement affiche **l'alternative textuelle en légende**. Une image dont
le `alt` est vide ou creux se dénonce donc toute seule à l'usage&nbsp;: le grand
format ne montre rien d'écrit sous l'image. La loupe devient un révélateur
d'images mal décrites — c'est un effet secondaire, et il est bienvenu.

Les schémas SVG écrits **dans** la page sont concernés au même titre que les
`<img>`&nbsp;: ils sont sérialisés à la volée, sans réseau, puisque le dessin
est déjà là. Les icônes de moins de 120 × 90 pixels sont laissées tranquilles —
on agrandit ce qui se lit, pas ce qui décore.

### Ce qui est mécanisé

`audit/loupe.py` injecte le bloc dans chaque page, une seule fois, en refusant
les gabarits et les pages sans image. **Testé au navigateur, pas déclaré**&nbsp;:
22 images armées sur le TP de 5e, ouverture, légende, fermeture par Échap,
zéro erreur JS&nbsp;; 1 SVG sérialisé sur la séquence 4e C8.1.

Ce qui n'est PAS couvert, et qu'aucun script ne saura faire&nbsp;: savoir si
l'image agrandie est **lisible**. Une capture floue le reste en grand, et une
capture rognée trop court ne montrera jamais ce qu'il fallait voir. Le script
rend l'agrandissement possible&nbsp;; il ne rend pas les images bonnes.

---

## Règle d'or n°93 (clé de voûte) — un TP ne suppose acquis aucun GESTE d'outil

*11 août 2026. Posée par Pascal&nbsp;: « j'arrive dans un établissement et
l'année dernière je n'ai pas fait certaines choses avec les cinquièmes. »*

La règle n°87 impose à tout TP de 4e et de 3e un rappel spiralaire
auto-suffisant. Elle porte sur les **notions**. Il manquait son pendant, qui
porte sur les **gestes du logiciel**&nbsp;: créer et nommer son document,
comprendre qu'il n'y a pas de bouton Enregistrer, retrouver son travail,
exporter au bon format et à la bonne unité.

**Les gestes d'outil se réenseignent à chaque niveau, en trois lignes, sans
excuse ni renvoi à l'année précédente.** Pas « comme tu l'as vu en 5e »&nbsp;:
la formulation doit tenir pour quelqu'un qui ne l'a jamais vu.

### Pourquoi cette règle-là, et pas seulement le rappel des notions

Parce que l'année précédente n'a pas toujours eu lieu. Un professeur muté en
cours de cycle, un emploi du temps amputé, un collègue qui a fait d'autres
choix, un élève arrivé d'un autre collège, une année où la salle informatique
était indisponible&nbsp;: dans tous ces cas, la progression spiralaire existe
sur le papier et pas dans la classe. **Un lot qui suppose sa propre continuité
ne survit pas à la réalité d'un établissement.**

Et le coût de la redite est faible. Un élève qui sait déjà passe en dix
secondes&nbsp;; un élève qui ne sait pas est sauvé. L'asymétrie tranche seule.

### Ce qui est fait

Les trois TP de CAO portent désormais les mêmes gestes d'ouverture — pas de
bouton Enregistrer, vérification immédiate qu'Onshape a bien gardé le
travail — et le même palier de clôture pour exporter et retrouver son fichier.
Le rappel de vérification en 4e et 3e dit explicitement&nbsp;: « tu l'as
peut-être déjà fait l'an dernier&nbsp;; refais-le, c'est court. »

### Ce qui n'est pas mécanisé

Décider ce qui compte comme « geste d'outil » relève du jugement. Ce qui se
mécanisera, quand la liste sera stable&nbsp;: vérifier que chaque TP d'un même
logiciel contient bien les gestes de la liste commune. À écrire dans
`verif_guidage.py` lorsque la progression CAO aura été menée une fois en
classe — pas avant, sous peine de figer une liste inventée au bureau.

## 19 août 2026 — Lot « La station d'alerte cyclonique se programme » (3e_C9.2 + 3e_C8.3)

### Ce qui a été livré

L'objet-fil de 3e franchit le pas : la station que les élèves avaient DÉCRITE au
Thème 2 (3e_C4.3), la mairie la COMMANDE désormais — courrier de commande à
l'appui, avec une exigence qui structure tout le lot : un procès-verbal de
recette avant mise en service. Dossier principal `3e_C9.2` (COMPLET ET
VALIDABLE), pointeur `3e_C8.3` (COUVERT PAR UNE SÉQUENCE MUTUALISÉE).

Le lot indivisible : séquence 4 séances de 1 h 30 (7 activités), QCM 30 q
(15/15 par code, 4 illustrées, répartition 8/7/7/8 par `fix_r.js` graine
20260819), deux synthèses, fiche pédagogique, matrice de 23 notions,
SOURCES_MEDIAS (9 SVG originaux CC0), programme C++ de référence commenté ligne
à ligne (compilation `arduino:avr:uno` vérifiée : 6 764 o) avec banc Docker
enseignant, suite Playwright de 51 tests committée, rapport de tests.

### Trois choix qui méritent d'être retenus

**Le banc d'essai INTÉGRÉ comme colonne vertébrale.** La station simulée vit en
haut de page (boucle à 200 ms comme le vrai programme, LCD, DEL, buzzer, bouton
d'acquittement, chrono de performance) et sert les quatre séances : découverte
en S2, expériences d'acquittement en S3, exécution de la recette en S4. Les
verrous `window.__exp` y tracent dix expériences (variation, trois niveaux,
acquittement, ré-armement, quatre frontières, chrono) : les activités 3, 4 et 7
REFUSENT la validation tant que la manipulation n'a pas réellement eu lieu.

**La séance 2 au gabarit du « dé de 5e ».** Demande explicite de Pascal : la
programmation se guide palier par palier (règles n°72-82) — un geste, l'image du
résultat attendu, le rituel d'enregistrement, l'aide qui décroît. Contrainte
assumée : pas d'accès à ArduBlock Éducation depuis la session (site DuinoEdu
inaccessible le 19/08), donc les planches sont des RECONSTITUTIONS schématiques
du programme en blocs, étiquetées comme telles dans l'image ET dans l'alt —
jamais de faux noms de boutons (règle n°73), valeurs déclarées comme exemples
(règle n°75). Les emplacements accueilleront des captures du poste réel si
Pascal en fournit.

**C8.3 pris au verbe.** « PROPOSER un protocole de test » : l'activité 6 fait
rédiger le protocole AVANT toute exécution (nominaux, frontières 99/100/149/150,
performance chronométrée, deux essais d'interaction, règle de décision), et
l'activité 7 le fait exécuter au banc — tableau essai/attendu/observé/verdict
rempli PENDANT, PV signé. Le QCM consolide, il ne remplace pas la production.

### La vérification, dans l'esprit de la maison

La suite Playwright SIMULE la séquence comme un élève et prend une capture
d'écran à chaque action (32 captures livrées avec le lot, hors dépôt) — y
compris la preuve que le verrou refuse AVANT la manipulation et accepte APRÈS.
Trois scénarios de notes calculés à la main puis vérifiés en machine.
`verif_regles_audit.py` : 0 manquement mécanique (étayages 11/11, durées 285+10
pour 360, formulations officielles recopiées, accessibilité statique).
Mobile 390 px : débordement horizontal ramené de 137 px à 0 (tables passées en
défilement local sous 680 px).

### Restes à faire consignés

Banc Docker à exécuter sur le poste de Pascal ; version d'ArduBlock Éducation à
revalider d'un clic à la rentrée ; montage 🅰 à faire vivre au labo ; captures
réelles d'ArduBlock bienvenues en remplacement des reconstitutions.

---

## Règle d'or n°94 — une capture d'écran vient du vrai logiciel, exécuté sur le poste

*21 août 2026. Née d'un travail réel : deux paliers du programme de la station
construits dans ArduBlock sur le poste de Pascal, puis capturés — après une
séquence entière livrée avec des « planches » dessinées à la main.*

Le dépôt distingue depuis longtemps l'**image-objet** (un document à lire) de
l'**image-explication** (un schéma qui enseigne). Il manquait une frontière plus
grossière, et plus dangereuse : celle entre **ce qui montre un logiciel** et
**ce qui prétend le montrer**.

**Quand une page dit à l'élève « voilà ce que tu dois voir à l'écran », l'image
vient du logiciel lui-même, lancé sur le poste, avec le programme réellement
construit.** Pas d'une reconstitution habillée en capture, pas d'une image
trouvée en ligne, pas d'un rendu de l'IA. Et la capture porte sa date et son
poste.

### Pourquoi c'est une règle et pas une préférence

Une reconstitution est une **hypothèse sur l'interface**. Elle nomme des boutons
de mémoire, invente une disposition plausible, oublie une barre d'outils. En
classe, l'élève cherche à l'écran ce que la page lui a montré — et ne le trouve
pas. Il en conclut, dans l'ordre : que son écran a un problème, puis qu'il n'a
pas compris, puis que la page ment. La règle n°80 avait déjà attrapé ce cas sur
les **noms de boutons** ; la n°94 l'étend à **l'image entière**, qui est un nom
de bouton de mille pixels de large.

Il y a un second effet, moins évident. Capturer oblige à **faire réellement le
travail** : ouvrir le logiciel, construire le programme, l'enregistrer, le voir
tourner. Un lot dont les captures sont réelles est un lot dont quelqu'un a
vérifié, avec ses mains, que l'activité est faisable dans le temps annoncé.
C'est le prolongement direct de la règle n°93 : on ne suppose pas les gestes,
donc on les fait.

### Ce que la règle n'interdit pas

Elle n'interdit pas les **reconstitutions schématiques** : elles restent utiles,
notamment quand l'outil n'est pas encore choisi, quand le repli hors ligne doit
fonctionner sans le logiciel, ou quand on veut épurer un écran chargé pour
montrer une seule idée. Elle exige seulement qu'elles soient **déclarées comme
telles** — dans l'image, dans la légende, et dans le texte alternatif — et
qu'elles ne soient jamais présentées comme « ce que tu verras ». Une page peut
porter les deux, côte à côte ; l'élève doit pouvoir dire laquelle est laquelle
sans hésiter.

### Portée

Toute page élève ou professeur qui montre une interface logicielle : TP de CAO,
séquences de programmation, tutoriels d'outil. Les captures réelles sont
inventoriées dans `SOURCES_MEDIAS.md` avec leur **origine, leur date et leur
poste**, et distinguées ligne à ligne des reconstitutions.

### Ce qui n'est pas mécanisé

Aucun script ne saura dire si une image est une vraie capture. Ce qui est
mécanisable, et qui reste à faire : vérifier que chaque image bitmap d'une page
élève possède **une ligne dans `SOURCES_MEDIAS.md` déclarant son statut**
(capture réelle ou reconstitution) — l'absence de déclaration devient le
manquement, faute de pouvoir juger l'image elle-même.

---

## 21 août 2026 — Refonte v2 de la station d'alerte cyclonique : le simulateur a fait le choix de l'outil

*Suite du lot du 19 août (3e_C9.2 + 3e_C8.3, PR #232). Même branche, même lot :
une refonte, pas un nouveau lot.*

### Le pivot : ArduBlock → Vittascience

La séance 2 était écrite pour **ArduBlock Éducation 1.7**, le logiciel du labo.
Le travail avait même commencé pour de vrai : deux paliers construits et
enregistrés sur le poste. Le pivot ne vient pas d'un défaut d'ArduBlock, mais
d'une exigence de la séquence elle-même. La compétence **C8.3** demande de
**tester aux valeurs frontières** — 39 et 40, 69 et 70. Or tester une frontière,
c'est poser une valeur exacte, regarder, la changer d'une unité, regarder encore.
Avec ArduBlock, chaque essai coûte un téléversement, une carte disponible et un
tour d'îlot. **ArduBlock ne simule pas.** Vittascience simule.

Autrement dit : ce n'est pas « quel logiciel de blocs préférons-nous », c'est
**quel logiciel rend le geste central de la séance possible pour 28 élèves en
1 h 30**. Posée ainsi, la question n'en était plus une.

Le prix est réel et il est écrit dans la page : Vittascience demande une
**connexion Internet**, seul élément de la séquence dans ce cas. D'où un
**repli hors-ligne** complet — lien direct, planches de blocs, banc d'essai
intégré — qui permet de répondre à toutes les questions et de valider
l'activité sans réseau. Un emplacement d'**iframe** est réservé dans la page,
à remplir avec le code d'intégration officiel dès qu'il existe.

### ArduBlock n'est pas jeté : il devient une leçon

Le travail déjà fait sur le poste devient un **bonus facultatif — hors parcours
obligatoire**, avec ses **deux captures réelles** (règle n°94, née là). Et il y
gagne : mis côte à côte, ArduBlock et Vittascience montrent le **même
raisonnement** sous deux habillages et à deux échelles. C'est exactement la
réponse à la question ajoutée en activité 2 — *ce qu'un algorigramme ne dit
pas, c'est le langage*. Un pivot d'outil s'est transformé en argument
pédagogique.

### Deux échelles, et la discipline de ne jamais les mélanger

La maquette Vittascience travaille en `niveau_vent` de **0 à 100**, seuils
**40 / 70**, capteur rotatif sur A0, trois voyants et un buzzer. La station du
labo travaille en **km/h de 0 à 250**, seuils **100 / 150**, avec LCD et bouton
d'acquittement. Deux échelles, deux câblages, une seule logique.

La tentation était d'unifier. On ne l'a pas fait, pour deux raisons. La première
est pratique : unifier obligeait à refaire le banc d'essai, le programme C++ de
référence, les séances 3 et 4 et la moitié du QCM — pour un lot déjà en PR. La
seconde est meilleure : **cette dualité est la leçon**. Un élève de 3e qui
comprend que la même décision se code sur deux échelles et deux câblages a
compris ce qu'est un algorithme. Un **tableau de correspondance** est donc posé
en tête de séance 2, déclaré comme le **seul pont autorisé** entre les deux, et
une règle de travail est écrite noir sur blanc : *dans l'interface tu parles en
niveau de vent, dans le PV tu parles en km/h, une phrase ne mélange jamais les
deux*. C'est aussi devenu une erreur fréquente listée et un point de vigilance
pour le professeur.

### Les quatre corrections v2 demandées par Pascal

**L'encart « LA BOUCLE » de l'algorigramme ressemblait à un rectangle de
traitement.** Dans un algorigramme, la forme EST la grammaire : un rectangle dit
« action ». Un commentaire dessiné en rectangle enseigne donc une action qui
n'existe pas — un code trompeur au sens de la règle n°80, mais graphique. Il est
devenu une bulle très arrondie, à contour **violet pointillé** (couleur réservée
aux commentaires, jamais celle du flux), hors du tracé des flèches, portant la
mention *« commentaire — pas un symbole »*, avec sa ligne dans la légende des
symboles. La `<desc>` du SVG le dit aussi.

**Six questions ont été ajoutées sous l'algorigramme** (activité 2 c), qui font
passer l'activité de 7 à 13 points : le cas de la frontière exacte (150 km/h
pile → alerte, parce que « ≥ » comprend la valeur), le comptage des rectangles
de traitement, la distinction commentaire / symbole — qui verrouille la
correction précédente —, l'effacement de la flèche de retour, le comptage des
chemins, et enfin *ce qu'un algorigramme ne dit pas*. Aides, correction,
erreurs fréquentes, critère de réussite, matrice de couverture et suite
Playwright ont suivi.

**Les niveaux de vigilance étaient incomplets.** Aux Antilles la vigilance
cyclonique ne s'arrête pas au rouge : **jaune → orange → rouge → violet → gris**.
Un encadré le dit dans la situation déclenchante, en précisant que le prototype
n'en programme que trois. Le défi bonus « violet » gagne une seconde question,
autrement plus intéressante que la première : *pourquoi le niveau gris ne peut-il
PAS se déduire de la seule vitesse du vent ?* Réponse : le gris est un état de
l'**après**, décidé par un humain ; une même entrée peut donner plusieurs
sorties. Il faudrait une mémoire et une décision humaine — la limite d'une
maquette, et la raison pour laquelle un dispositif d'alerte réel n'est jamais
entièrement automatique.

**La loupe superposait sa légende à l'image.** L'agrandissement de la règle n°92
affichait le texte alternatif par-dessus le bas de l'image. Corrigé dans la
séquence ET dans le QCM : barre de légende opaque collée en bas, image ramenée à
68 % de la hauteur, réserve de place sous l'image. Une loupe qui cache ce qu'on
agrandit ne remplit pas son office.

### Le fil rouge : New York lit le PV

Le Thème 3 a New York pour fil rouge, la séquence est martiniquaise. Le nœud
tient en une ligne du courrier de la mairie : le procès-verbal est demandé en
**deux exemplaires**, dont un pour la ville **jumelée**. Depuis **Sandy (2012)**,
New York échange avec les territoires qui vivent le risque cyclonique chaque
année. Ce que la ville demande n'est pas la station, c'est la **recette** — et
c'est un excellent critère de rédaction : *un PV qui se lit à 6 800 km, par des
gens qui n'ont jamais vu le prototype, est un PV bien écrit*. Le renversement
vaut d'être noté : ici, ce n'est plus la Martinique qui apprend de New York.

### Restes à faire consignés

Code d'intégration iframe Vittascience à coller (emplacement réservé, repli en
place) ; captures réelles de l'interface Vittascience à substituer aux planches
schématiques dès que les programmes de la classe existent (règle n°94) ;
vérifier que `fr.vittascience.com` n'est pas filtré par le réseau du collège
avant la séance 2 ; nettoyage du poste (chemin `sketchbook.path` d'origine à
restaurer, flag DPI de `javaw.exe` à retirer, fichiers de travail de
`Downloads` à supprimer).

---

## 21 août 2026 (suite) — L'encadré « jumelage » gagne quatre ouragans, et reste replié

*Demande de Pascal, qui a trouvé la situation déclenchante « accrochante » mais trop
courte sur les cyclones : « il serait intéressant de citer tous les cyclones… et je te
laisse carte blanche, car ce sujet peut être très long et pourrait être considéré comme
un distracteur ».*

La demande contenait déjà sa propre contrainte, et c'est elle qui a guidé le travail :
**enrichir sans détourner**. Un élève de 3e qui découvre l'histoire des ouragans de New
York peut y passer la séance — et rater la station.

### Ce qui a été fait

L'encadré cite maintenant **cinq cas** au lieu d'un : l'ouragan de **1938** (« Long
Island Express », catégorie 3, ~190 km/h sur Long Island — le seul vrai coup direct),
**Irene** (2011), **Sandy** (2012), **Henri** et **Ida** (2021). Puis une comparaison
**Martinique / New York** en quatre lignes : fréquence, danger principal, point faible,
population.

### Les trois garde-fous qui empêchent le distracteur

1. **Tout est replié, à deux niveaux.** L'encadré était déjà un `<details>` ; les
   ouragans vivent dans un `<details>` **imbriqué**. Il faut donc deux gestes délibérés
   pour y entrer. Une suite de tests vérifie que les deux restent fermés au chargement —
   c'est mécanisable, donc mécanisé.
2. **C'est écrit noir sur blanc** : « complément de culture, hors parcours obligatoire ;
   rien ici n'est demandé au vérificateur ni au QCM ». L'élève sait ce qu'il lit, et ce
   qu'il ne risque pas de manquer.
3. **Le contenu revient à l'objet technique.** Le fil conducteur n'est pas « voici des
   ouragans », c'est : *sauf en 1938, le danger new-yorkais n'était pas le vent, c'était
   l'eau*. D'où la chute, qui est la seule chose vraiment utile de tout l'encadré —
   **notre prototype ne mesure que le vent** : utile à Sainte-Luce, très insuffisant à
   New York, où il faudrait mesurer la montée des eaux. Un objet technique ne vaut que
   pour le besoin auquel il répond. Un encadré de culture qui se termine sur une limite
   du prototype n'est plus un distracteur : c'est une leçon d'analyse du besoin.

### Une règle de rédaction qui se dégage

Quand un complément risque de manger la séance, la question n'est pas « faut-il le
mettre ? » mais **« par quoi le fait-on finir ? »**. Un complément qui se termine sur
l'objet de la séquence ramène l'élève ; un complément qui se termine sur lui-même
l'emmène ailleurs. C'est peut-être une future règle d'or ; elle mérite d'abord d'être
éprouvée sur deux ou trois lots.

### Vérification et point de vigilance sur l'outillage

`verif_regles_audit.py` : 0 manquement. Suite Playwright : **74/74** (64 + 10 ajoutés
pour cet encadré). Les faits historiques ont été vérifiés sur sources concordantes et
sont donnés en ordres de grandeur, jamais avec une précision qu'ils n'ont pas ;
`SOURCES_MEDIAS.md` le consigne.

**Bogue repéré dans l'outillage, hors périmètre** : la règle n°42 s'ancre sur
`re.search(r"referentiel-card.*?</table>")`, qui tombe sur la **première** occurrence de
`referentiel-card` — celle de la feuille de style — puis s'arrête au premier `</table>`
rencontré. Ajouter un tableau AVANT la carte de référentiel suffit donc à faire passer
la règle en « SANS OBJET » : elle ne vérifie plus rien, sans rien signaler. C'est ce qui
est arrivé ici. Les deux formulations ont été revérifiées à la main (conformes), et
l'ancre correcte serait `class="card referentiel-card"`. À corriger par le responsable
de `_outils/`. La leçon dépasse ce bogue : **une règle qui devient silencieusement
« sans objet » est plus dangereuse qu'une règle qui échoue** — l'échec se voit, le
silence non.

---

## 21 août 2026 — Deux audits de C9, et trente-deux règles qui en sortent

*Pascal a conduit deux audits du parcours C9 (5e, 4e, 3e_C9.1, 3e_C9.2) : le sien, en
se mettant en position d'élève qui bute, et un audit demandé à ChatGPT, en position
d'inspecteur qui vérifie. Les deux ne trouvent pas les mêmes choses — et c'est
exactement pour cela qu'il fallait les deux.*

L'audit-élève trouve ce qui **empêche d'avancer** : une correction qu'on ne comprend
pas, un banc de tests qu'on ne trouve pas, un mot qui change de sens en route, quatre
options sur une même ligne. Rien de tout cela n'est faux ; tout cela coûte. L'audit-
inspecteur trouve ce qui est **faux** : une proportionnalité erronée, un exemple qui se
contredit, un code de compétence qui ne correspond pas au verbe travaillé, un QCM dont
la bonne réponse est toujours la deuxième.

Aucun des deux ne remplace l'autre. Un dépôt juste mais impraticable ne sert personne ;
un dépôt confortable et faux non plus.

Les trente-deux règles ci-dessous en sortent. Trois sont des **clés de voûte** (n°95,
n°104, n°109). Quelques-unes ne sont pas neuves : elles constatent qu'une règle
existante n'a jamais été appliquée à l'existant — et c'est précisément l'objet de la
première.

---

## Règle d'or n°95 (clé de voûte) — une règle d'or non harmonisée n'est pas une règle, c'est un vœu

*Posée par Pascal, à partir d'un constat qu'il fait dans son propre dépôt.*

**Toute règle d'or nouvellement écrite déclenche, dans le même mouvement, une passe
d'harmonisation sur les séquences déjà publiées des trois thèmes.** Tant que cette
passe n'est pas faite et consignée, la règle est marquée **« écrite, non harmonisée »**.

La preuve était déjà là, sous nos yeux. La règle n°4 impose que les blocs « Prêt·e à
t'entraîner ? » et « Bonus » closent la page, une seule fois, à la fin : la séquence de
5e les place en fin de séance intermédiaire. La règle n°86 impose que chaque défi bonus
ait son corrigé replié : la 5e a des bonus sans correction. Ces deux règles ont été
écrites *après* la séquence de 5e, et jamais répercutées.

Une règle qui ne vaut que pour les lots futurs crée **deux dépôts dans le dépôt** :
celui d'avant la règle et celui d'après. L'élève, lui, ne sait pas de quelle époque est
la page qu'il a sous les yeux. Il en tire la seule conclusion disponible : les
conventions du site ne sont pas fiables.

### Ce qui est mécanisé

Un **tableau d'harmonisation** au journal (voir plus bas) : une ligne par règle, une
colonne par séquence publiée, trois états — conforme, non conforme, sans objet. Pour
les règles déjà mécanisées, `verif_regles_audit.py` remplit les cases. Le tableau EST
le reste-à-faire ; il remplace notre mémoire, qui a démontré qu'elle ne suffisait pas.

### Ce qui ne l'est pas

Décider si l'harmonisation vaut une retouche ou une refonte. Certaines règles nouvelles
condamneraient une séquence entière ; dans ce cas la règle vaut pour les nouveaux lots
et la séquence ancienne est **datée** au tableau — jamais réputée conforme par
commodité.

---

## Règle d'or n°96 — une correction est exhaustive, même quand l'élève a tout juste

Chaque question posée a sa correction, **y compris celles que l'élève a réussies**, et
la correction reste accessible après un sans-faute.

Le motif est de Pascal, et il vaut d'être cité : *« quand un élève a 100 % de bonnes
réponses, il s'attend quand même à une correction exhaustive, car elle lui apprend
davantage ou conforte ses acquis, et cela le met en confiance. »* Une correction n'est
pas une sanction d'erreur. C'est le moment où l'élève découvre qu'il avait raison — ou
qu'il avait raison **pour une mauvaise raison**, ce qu'aucun score ne lui dira jamais.

Corollaire : une correction partielle, qui ne reprend que « les questions difficiles »,
enseigne implicitement que le reste n'avait pas d'intérêt.

---

## Règle d'or n°97 — une correction se met en page comme une démonstration de mathématiques

Une idée par ligne. Un retour à la ligne à chaque moment-clé. Les valeurs numériques
alignées. Le raisonnement doit être visible **dans la forme** avant d'être compris dans
le fond. Interdit : le pavé où le lecteur doit lui-même séparer les étapes.

Le cas d'école est cruel : la correction de la barrière du Cyclone, en 5e — *« Ligne 5
→ places = places + descendus ; nouveau train → ligne 1 : places = 32 … ② B1 OUVERTE ✔,
B2 OUVERTE ✔, B3 : 0 > 0 est FAUX → FERMÉE ✔ »* — n'a pas été comprise **par l'auteur
du dépôt lui-même**. Si l'auteur ne suit pas sa propre correction, l'élève n'a aucune
chance.

---

## Règle d'or n°98 — les options d'un choix se lisent en colonne, jamais en ligne

Les réponses possibles s'empilent verticalement, une par ligne. Une suite d'options sur
une même ligne oblige à toutes les tenir en mémoire de travail avant de choisir : c'est
une charge inutile, et elle frappe d'abord ceux qui lisent lentement.

C'est la même famille que la n°97 : **la mise en page fait partie de la compréhension**,
elle n'est pas une décoration appliquée après coup.

---

## Règle d'or n°99 — une aide qui donne le raisonnement ouvre sur un exercice jumeau

Quand l'aide de niveau 2 livre la solution — et c'est son rôle, elle est un filet —
elle est immédiatement suivie d'une **situation analogue à valeurs différentes**, à
traiter seul.

Sans cela, rien ne distingue « j'ai compris grâce à l'aide » de « j'ai recopié l'aide ».
Ni pour le professeur, ni, ce qui est plus grave, **pour l'élève lui-même** : il croira
savoir jusqu'à l'évaluation.

Exemple : après l'aide sur la table de suivi, *« le nouveau train compte 28 places,
quatre visiteurs montent et deux descendent — complète la table sans reprendre les
nombres de l'exemple. »*

---

## Règle d'or n°100 — un dispositif intégré s'annonce par un titre qui le nomme

Banc de tests, simulateur, éditeur embarqué, banc d'essai : chacun porte un **intitulé
visible** (« 🧪 Banc de tests intégré ») et un cadre qui le délimite. L'élève doit voir
où le dispositif commence sans avoir à lire la consigne jusqu'au bout.

Le constat de Pascal dit tout : *« ce banc de test est révélé en lisant l'intégralité
de la consigne, mais comme les élèves atypiques, je me suis arrêté de lire pour le
repérer — et je n'ai eu aucun repère. »* Chercher un objet qui existe pourtant à
l'écran est une expérience d'échec, et elle se produit avant même la première question.

---

## Règle d'or n°101 — chaque séance se termine par un bouton qui mène à la suivante

Fin de séance = un bouton explicite, nommé par sa destination (« Séance 2 → Lire et
tester »). L'élève ne cherche jamais où continuer, et la progression reste sous ses
yeux. À harmoniser sur les trois thèmes (n°95).

---

## Règle d'or n°102 — toute page élève s'imprime en document propre, sans fond sombre

Le thème sombre est un confort d'écran. À la reprographie, c'est une page noire et une
cartouche vidée. La feuille d'impression force fond blanc et texte noir, masque les
éléments interactifs, et produit un **document de qualité livrable**, mis en page pour
le A4.

Pascal en donne le motif complet, qui dépasse l'encre : *si le réseau du collège est
indisponible, ou si l'enseignant préfère mener la séance sur papier, il doit pouvoir
imprimer sa séquence sans rien perdre.* L'impression n'est donc pas une commodité :
c'est **le dernier repli du dispositif**, celui qui garantit que la séance a lieu.

---

## Règle d'or n°103 — les blocs de fin ferment la page, et rien ne les suit

« 🪞 Bilan », « 🧠 Prêt·e à t'entraîner ? » et « 🎁 Bonus » apparaissent **une seule
fois**, à la toute fin de la séquence — jamais en fin de séance intermédiaire.

Ce n'est pas une règle neuve : la n°4 le disait. C'est une **dette** que la n°95 rend
visible et exigible. On la réécrit ici parce qu'une règle violée dans le dépôt même qui
la porte doit être re-signée.

---

## Règle d'or n°104 (clé de voûte) — un code de compétence s'écrit toujours avec son niveau

Jamais `C9.2` seul : toujours **`5e_C9.2`**, `4e_C9.2`, `3e_C9.2` — dans la page, dans
la fiche, dans la matrice, dans le QCM, dans l'index, dans le journal.

Le même numéro désigne des attendus **différents** selon le niveau : en 5e on modifie,
en 4e on traduit, en 3e on conçoit. Écrire le code nu fabrique une confusion entre
trois compétences distinctes — et cette confusion voyage jusqu'au LSU, où elle devient
un positionnement faux sur le bulletin d'un élève.

C'est une clé de voûte parce qu'elle ne coûte rien à respecter et qu'elle coûte cher à
réparer.

---

## Règle d'or n°105 — la formulation d'une compétence est celle du BO, au mot près, partout

La règle n°42 mécanise déjà ce contrôle sur la **carte de référentiel**. Elle est ici
**étendue** : la formulation doit être exacte aussi dans la **fiche pédagogique**, la
**matrice de couverture**, le **QCM** et l'**index**.

Une compétence reformulée « pour que ce soit plus clair » devient une compétence
différente. Si la formulation officielle est obscure pour l'élève, on l'accompagne
d'une reformulation **déclarée comme telle** — on ne la remplace pas.

---

## Règle d'or n°106 — le code annoncé doit correspondre au VERBE réellement travaillé

Annoncer `4e_C9.1` (« modifier un algorithme ») pour une activité qui **traduit** un
algorithme en programme, c'est fausser la matrice, la couverture du référentiel et le
positionnement final.

Le contrôle est simple et se fait à voix haute : *le verbe officiel du code est-il le
verbe de la consigne ?* Si la consigne dit « traduis », le code ne peut pas être celui
qui dit « modifie ».

Cas fondateur : les trois activités de la séquence 4e « Jardin programmé » sont
décalées d'un cran par rapport aux codes annoncés.

---

## Règle d'or n°107 — un nom propre du récit s'explique une fois, puis ne change plus

Un nom propre est présenté à sa première occurrence — *le Cyclone est une montagne
russe en bois de Coney Island, à New York* — puis désigné **toujours du même mot**.

Alterner « le Cyclone » et « le manège » oblige l'élève à deviner qu'il s'agit du même
objet, et cette dépense n'enseigne rien. Le cas est aggravé ici par l'homonymie : dans
un dépôt où l'on programme une **station d'alerte cyclonique**, appeler un manège « le
Cyclone » sans le dire est un piège qu'il faut désamorcer explicitement.

---

## Règle d'or n°108 — l'outil est nommé avec sa modalité exacte, et ce qui s'ouvre est ce qui est annoncé

« Vittascience » ne suffit pas : **« l'éditeur Vittascience, interface Python »** ou
**« interface Arduino, mode blocs »**. Et l'annonce doit être **vérifiée dans le
navigateur** : la séquence de 5e annonce l'éditeur Python, l'iframe s'ouvre en mode
blocs sans bascule visible.

Un outil qui n'est pas celui annoncé fait douter l'élève de lui-même — jamais de la
page. C'est la même famille que la n°80 (les noms de boutons) et la n°94 (les captures
réelles) : **on ne décrit pas un logiciel de mémoire.**

Corollaire : quand un outil embarqué met du temps à charger, on le dit — *« compte 1 à
2 minutes à l'ouverture »*. Un élève qui croit la page cassée ferme l'onglet.

---

## Règle d'or n°109 (clé de voûte) — tout nombre calculable est recalculé, et le calcul est testé

Toute correspondance, conversion, échelle, proportion ou valeur dérivée figurant dans
une page élève est **recalculée** et couverte par un **test automatique**.

La faute qui fonde la règle est la nôtre, et elle est exemplaire. Le tableau de
correspondance de la station annonçait 40 ↔ 100 km/h — juste — **et** 70 ↔ 150 km/h.
Or 70 × 250 ÷ 100 = **175**. Vingt-cinq kilomètres-heure d'erreur, dans un tableau
présenté comme « le seul pont autorisé » entre deux échelles, à trois écrans d'une
activité qui enseigne la proportionnalité. Ni l'auteur, ni la relecture, ni la suite de
74 tests ne l'ont vue. Il aurait fallu trois lignes.

C'est une clé de voûte parce qu'elle attrape une classe entière de fautes que la
relecture humaine ne voit **jamais** : celles où le texte est cohérent, plausible, bien
écrit — et faux.

---

## Règle d'or n°110 — un exemple filé raconte une seule histoire, du début à la fin

Les valeurs de la consigne, celles du programme, celles de la correction et celles de
la capture décrivent **le même déroulé**. Un seul contre-exemple ruine la confiance
dans tout le reste de la page.

Cas fondateur : en 3e_C9.1, la consigne annonce un panneau affichant « St - 3 min », le
programme corrigé produit 2, et la correction annonce 2. L'élève qui a suivi ne sait
plus s'il a mal lu, mal compris, ou si la page se trompe — et il n'a aucun moyen de
trancher.

---

## Règle d'or n°111 — fiction déclarée, chiffre sourcé

Les courriers, commandes, clients et personnages sont signalés comme **scénarios
pédagogiques fictifs inspirés de situations réelles** — une mention discrète, une fois
par page, suffit. Et tout chiffre présenté comme un fait porte sa source, ou disparaît.

À corriger dans le dépôt : « 9 collégiens sur 10 ignorent… », qui est inventé, et qui
doit devenir « une notion souvent difficile ». Fabriquer une statistique pour rendre une
accroche plus frappante, c'est enseigner en creux qu'un chiffre bien tourné n'a pas
besoin d'être vrai. Dans un dépôt de technologie, où l'on va exiger des élèves un
procès-verbal honnête, c'est intenable.

---

## Règle d'or n°112 — le statut de chaque ressource est écrit

Sur l'index et dans la page : **obligatoire · entraînement · prolongement facultatif ·
ancienne adresse (redirection)**. L'élève ne doit jamais avoir à deviner si une
ressource compte.

Cas relevé : en 3e_C9.1 coexistent le QCM de 30 questions, un ancien QCM de 24, un TP
mBot2 et une page de redirection — sans hiérarchie visible. Devant quatre portes non
étiquetées, l'élève consciencieux les ouvre toutes et perd sa séance ; l'autre n'en
ouvre aucune.

---

## Règle d'or n°113 — « réaliser un programme » exige une trace du programme réalisé

Quand le verbe officiel est *réaliser et mettre au point un programme*, un banc de
simulation intégré ne suffit pas à valider la compétence. Il faut une **preuve
minimale** : nom du projet enregistré, capture du programme, trace des tests, et une
phrase sur le cas limite.

La simulation reste le chemin de ceux qui n'ont pas de matériel — elle ne remplace pas
la production. Sans cette règle, 5e_C9.3 peut être validée sans qu'aucun programme
n'ait jamais été écrit, ce qui est exactement ce que le libellé interdit.

---

## Règle d'or n°114 — en 3e, l'élève conçoit au moins une fois sans squelette

Le verbe de 3e est **concevoir**. Une activité qui fournit déjà le nom de la fonction,
ses paramètres et la structure `si / sinon si / sinon` fait *traduire* — c'est le verbe
de la 4e.

Chaque séquence de 3e comporte donc au moins un transfert où l'élève part des entrées
et des sorties et écrit lui-même l'algorithme, en français d'abord. Le squelette est
une aide légitime ; il ne peut pas être le régime permanent d'un niveau dont la
compétence est la conception.

---

## Règle d'or n°115 — on fait observer le problème avant d'en expliquer la solution

Une notion corrective — hystérésis, anti-rebond, lissage, temporisation — est d'abord
**subie** : une série de mesures qui fait osciller la sortie, un tableau qui montre le
défaut, un chronogramme qui le rend visible. L'explication ne vient qu'après, comme
réponse à une gêne réelle.

Expliquée avant d'être rencontrée, la solution est un mot à retenir. Rencontrée
d'abord, elle est un soulagement — et un soulagement ne s'oublie pas.

---

## Règle d'or n°116 — une séquence trop dense se découpe en pages reliées, sans rien perdre

Au-delà de l'ordre de grandeur de **8 000 mots** (ou ~30 volets repliables), une page
élève se découpe en **pages séparées reliées par une même barre de progression**, et la
progression se conserve d'une page à l'autre.

**Aucune question, aucune activité, aucun corrigé ne disparaît au découpage** : on
répartit, on ne coupe pas. C'est la condition sans laquelle le découpage devient un
allègement déguisé.

La mesure qui fonde la règle : la station d'alerte cyclonique compte ≈ 12 400 mots,
41 volets repliables, 55 listes déroulantes, 29 zones de saisie, 7 activités. Le mode
essentiel réduit ce qui s'affiche, pas ce qui existe : **la longueur seule décourage,
avant même la première consigne**.

Découpage retenu pour la station, qui vaut modèle :

1. Besoin et algorithme ;
2. Programmer par paliers ;
3. Interaction humain-machine et mise au point ;
4. Protocole et recette.

Bénéfice inattendu et décisif : ce découpage-là sépare aussi **ce qui relève de C9** de
**ce qui relève de C8**, que la page unique mélangeait.

---

## Règle d'or n°117 — un `alt` court, une description longue à côté

Le texte alternatif dit la **fonction** de l'image, en une phrase. La description
détaillée vit **à côté de l'image**, dans un volet dépliable ouvert à tous. Les
chronogrammes, câblages et algorigrammes reçoivent en plus un **équivalent en tableau**.

Cette règle corrige une dérive du dépôt, née de la meilleure intention. La règle n°1
dit que l'image est un document à lire ; nous en avons conclu qu'il fallait tout mettre
dans le `alt`, jusqu'à 1 200 caractères. Or **un `alt` ne se parcourt pas** : au lecteur
d'écran, il se déroule d'un bloc, sans titres, sans possibilité de sauter à l'essentiel
ni d'y revenir. Un mur de mots n'est pas une alternative accessible : c'est le même
problème que le pavé de la n°97, transposé à l'oreille.

La description dépliable, elle, profite à tout le monde — y compris à l'élève voyant
qui n'arrive pas à lire un schéma.

---

## Règle d'or n°118 — socle accessible minimal, sur toute page élève

Lien d'évitement vers le contenu, balise `<main>`, et **un nom accessible explicite
pour chaque contrôle** (`<label>` relié, ou `aria-labelledby`). Un utilisateur de
lecteur d'écran doit entendre la question, pas « liste déroulante ».

Constat qui fonde la règle : la séquence de 4e n'a ni lien d'évitement ni `<main>`, et
3 contrôles sur 22 portent un nom accessible. Ce n'est pas un raffinement : sans nom,
la page est **inutilisable**, pas seulement inconfortable.

---

## Règle d'or n°119 — jamais la couleur seule, jamais l'animation seule

Toute information portée par une couleur l'est aussi par un texte ou une forme. La
règle est étendue ici : **il en va de même pour une pulsation, un clignotement ou une
animation**. Un écran qui passe du vert foncé au vert clair pour signaler un état doit
aussi l'écrire.

Motifs : le daltonisme, un écran en plein soleil, `prefers-reduced-motion` actif — et,
plus banal que tout le reste, un regard ailleurs au moment précis où la chose clignote.
Une information qui n'existe que pendant un instant n'existe pas.

---

## Règle d'or n°120 — la couleur d'une notion est constante dans toute la séquence

Si la variable est bleue dans le cours, elle est bleue dans la question, dans la
réponse, dans la correction, dans le schéma et dans le QCM. Idem pour la valeur, le
type, l'entrée, la sortie.

Un code couleur stable **allège la charge mentale** : l'élève reconnaît avant de lire.
Un code couleur qui change de sens d'un bloc à l'autre fait pire que rien — il installe
une attente, puis la trahit, et l'élève finit par ignorer la couleur, y compris quand
elle disait vrai.

---

## Règle d'or n°121 — une capture montre un geste nécessaire

Toute capture répond à deux questions : *que dois-je faire ?* et *comment saurai-je que
c'est fait ?* Donc : l'interface au moment du geste, le résultat attendu, et le message
d'erreur typique quand il existe.

Les images d'ambiance restent permises — elles installent le récit — mais elles ne
comptent pas comme représentation opératoire, et ne dispensent d'aucune capture utile.
Se combine avec la n°94 : ces captures viennent du vrai logiciel, exécuté sur le poste.

---

## Règle d'or n°122 — les trois façons de vivre la séquence sont trois parcours, pas trois paragraphes

Les versions 🅰 / 🅱 / 🅲 se choisissent **en tête de page** et **modifient l'affichage** :
les consignes, les boutons et les dispositifs de la voie choisie apparaissent, les
autres se replient. Le choix est mémorisé, et réversible à tout moment.

Décrire les trois modalités dans un texte que tout le monde lit laisse chaque élève
trier lui-même ce qui le concerne — c'est-à-dire lire les deux tiers d'une page pour
rien, et risquer d'appliquer la consigne d'une autre voie.

Pascal en donne le motif fort, qui va au-delà du confort : **le réseau du collège peut
être indisponible**, ou l'enseignant peut décider de mener la séance sur papier. Un
parcours réellement isolable est alors imprimable seul (n°102) et la séance a lieu
quand même. Les trois voies ne sont pas trois niveaux de confort : ce sont **trois
plans de secours les uns pour les autres**.

---

## Règle d'or n°123 — les fonctions techniques des deux chaînes sont nommées, complètes, en majuscules

Les fonctions de chaque chaîne sont écrites en toutes lettres et en majuscules —
ACQUÉRIR · TRAITER · COMMUNIQUER pour l'information ; ALIMENTER · DISTRIBUER ·
CONVERTIR · TRANSMETTRE pour l'énergie — et **l'action sur la matière d'œuvre figure à
droite, hors chaîne**.

Complète la n°6, qui fixe la disposition (information en haut, énergie en bas, ordre
qui descend). Cas relevé : la barrière du Cyclone était rangée **dans** la chaîne
d'énergie alors qu'elle en est le résultat — l'action —, et « distribuer » était en
minuscules parmi des fonctions capitalisées. Une chaîne mal peuplée enseigne un
contresens sur ce qu'est une fonction technique.

---

## Règle d'or n°124 — la matrice de couverture a des colonnes normalisées

Code (avec son niveau, n°104) · verbe officiel · activité · production attendue ·
questions de QCM · niveau cognitif · socle · CRCN · critère de réussite.

Et la colonne **production** doit montrer où l'élève **conçoit seul**, pas seulement où
il répond juste. Une matrice qui n'aligne que des réponses à des questions fermées
prouve une reconnaissance, pas une compétence.

---

## Règle d'or n°125 — un distracteur est plausible, et il est réfuté

Aucune option ne doit pouvoir s'éliminer sans connaître la notion : « décorer »,
« rien », « perdre du temps », « acheter un robot » ne sont pas des distracteurs, ce
sont des remplissages. Chaque distracteur reçoit sa réfutation propre. Et les bonnes
réponses sont réparties sur A/B/C/D.

Cette dernière exigence existait déjà, et **elle n'est pas tenue** : dans le QCM de 4e,
la bonne réponse est systématiquement la deuxième ; en 5e, elle est souvent la première
et la plus détaillée. Un élève peut donc réussir par détection du motif, sans rien
savoir — et il le fera, parce qu'il est intelligent. **Dette d'harmonisation (n°95).**

---

## Règle d'or n°126 — distinguer le domaine contextualisé du domaine évalué

Une séquence peut **mobiliser** D3 ou D5 par son contexte sans les **évaluer**. Les
domaines évalués sont ceux dont une production porte la preuve ; les autres sont
mentionnés comme contexte, et dits comme tels.

Et les trois endroits qui annoncent les domaines — index, fiche pédagogique, séquence —
doivent annoncer les mêmes. Incohérence relevée en 4e : D1.3/D2/D4 à l'index,
D2/D4/D5 dans la fiche.

---

## Le tableau d'harmonisation (règle n°95)

*État au **26 août 2026**. « ✔ » conforme · « ✘ » non conforme, à reprendre · « — » sans
objet · « ? » non encore vérifié. Ce tableau est le reste-à-faire du dépôt : il se met
à jour à chaque lot, et aucune règle n'est réputée appliquée tant que sa ligne n'est
pas pleine.*

*Mise à jour du 26 août (soir) : la colonne **4e_C9** est reprise après la
réécriture complète du lot du jardin connecté. Deux lignes restent **rouges et le
disent** : la n°99 (aucun exercice jumeau après l'aide de niveau 2 — c'est le
prochain chantier de ce lot) et la n°124 (la matrice a huit colonnes normalisées,
mais pas encore le niveau cognitif, le CRCN ni le critère de réussite). Le reste
est couvert par la suite de tests ou par `verif_regles_audit.py`.*

*Mise à jour du 26 août : la colonne **3e_C9.2** passe au vert sur quatorze lignes
supplémentaires (n°100, 101, 109 à 114, 116, 117, 119 à 122). Chacune est **couverte
par un test de la suite** `tests_3e_C9.2-C8.3.mjs` ou par un contrôle de
`_outils/verif_regles_audit.py`, pas par une relecture : n°116 par le test d'union des
champs et de persistance croisée, n°122 par le test du sélecteur de parcours, n°119 par
la vérification que le niveau est écrit en toutes lettres aux quatre paliers, n°121 par
la présence des treize captures réelles, n°101 par le clic sur le bouton de fin de
séance. Les lignes qui restent au « ? » ou au « ✘ » (n°96 à 99, 115, 124, 126) n'ont
pas été touchées par cette refonte : elles concernent la mise en page des corrections,
les exercices jumeaux et la matrice, et attendent leur tour.*

| Règle | 5e_C9.1 | 4e_C9 | 3e_C9.1 | 3e_C9.2 |
|---|---|---|---|---|
| n°96 correction exhaustive | ✘ | ✔ | ? | ? |
| n°97 correction mise en page | ✘ | ✔ | ? | ? |
| n°98 options en colonne | ✘ | ✔ | ? | ? |
| n°99 exercice jumeau après aide | ✘ | ✘ | ✘ | ✘ |
| n°100 dispositif intégré nommé | ✘ | ✔ | ✔ | ✔ |
| n°101 bouton de séance suivante | ✘ | ✔ | ✔ | ✔ |
| n°102 impression propre | ? | ✔ | ✔ | ✔ |
| n°103 blocs de fin en fin de page | ✘ | ✔ | ✔ | ✔ |
| n°104 code avec niveau | ✘ | ✔ | ✔ | ✔ |
| n°105 formulation BO partout | ✘ | ✔ | ✔ | ✔ |
| n°106 code = verbe travaillé | ? | ✔ | ✔ | ✔ |
| n°107 nom propre expliqué | ✘ | ✔ | — | ✔ |
| n°108 outil nommé et vérifié | ✘ | ✔ | ? | ✔ |
| n°109 nombres recalculés et testés | ? | ✔ | ✘ | ✔ |
| n°110 exemple filé cohérent | ? | ✔ | ✘ | ✔ |
| n°111 fiction déclarée, chiffre sourcé | ✘ | ✔ | ? | ✔ |
| n°112 statut des ressources | ? | ✔ | ✔ | ✔ |
| n°113 trace du programme réalisé | ✘ | ✔ | ? | ✔ |
| n°114 conception sans squelette (3e) | — | ✔ | ✘ | ✔ |
| n°115 problème observé avant solution | ? | ✔ | ? | ? |
| n°116 découpage au-delà du seuil | ✔ | ✔ | ? | ✔ |
| n°117 alt court + description | ✘ | ✔ | ✔ | ✔ |
| n°118 socle accessible minimal | ? | ✔ | ✔ | ✔ |
| n°119 ni couleur seule, ni animation seule | ? | ✔ | ? | ✔ |
| n°120 couleur constante par notion | ✘ | ✔ | ✔ | ✔ |
| n°121 capture d'un geste nécessaire | ✘ | ✔ | ✘ | ✔ |
| n°122 trois parcours, trois affichages | ✘ | ✔ | ✔ | ✔ |
| n°123 fonctions des chaînes nommées | ✘ | ✔ | — | ✔ |
| n°124 colonnes de la matrice | ✘ | ✘ | ✘ | ✘ |
| n°125 distracteurs plausibles et réfutés | ✘ | ✔ | ✔ | ✔ |
| n°126 domaine contextualisé vs évalué | ? | ✔ | ✔ | ? |

**Ordre de traitement retenu** : 3e_C9.2 (station) d'abord — elle cumule le découpage
en quatre pages, la bascule des seuils, le quatrième niveau et l'écran ; puis 4e, la
plus en retard ; puis 3e_C9.1 ; puis 5e.

**Ce que ce tableau dit de nous, et qu'il faut lire en face** : les lignes les plus
noires ne sont pas les plus difficiles (n°101 un bouton, n°121 des captures, n°122 un
sélecteur de parcours). Ce sont celles auxquelles personne n'avait pensé — et le seul
moyen d'y penser a été de **regarder la page en élève**, puis de la faire auditer par
quelqu'un d'autre. Aucun des deux audits, seul, n'aurait produit cette liste.

---

# 26 août 2026 — La station d'alerte cyclonique, v3 : quatre niveaux, quatre pages, treize captures

*Refonte v3 du lot 3e_C9.2 + 3e_C8.3, en application des 32 règles dégagées des deux
audits du 21 août. C'est le premier lot à passer entièrement au nouveau standard : il
sert de gabarit pour l'harmonisation des autres.*

## Ce qui a changé, et pourquoi

**Une seule échelle.** La version précédente faisait cohabiter une « maquette »
graduée 0-100 sans unité et une « station » en km/h, reliées par un tableau de
correspondance. C'était le premier risque de confusion de la séquence — et c'est là
qu'une erreur de correspondance s'était glissée (règle n°109). La v3 supprime le
problème par construction : **des km/h, de 0 à 250, du premier bloc au procès-verbal**.
Il n'y a plus de pont à traverser, donc plus de pont où tomber.

**Quatre niveaux, trois seuils, six frontières.** Les seuils 63 / 118 / 178 km/h sont
ceux de l'échelle de Saffir-Simpson — entrée en tempête tropicale, en ouragan, en
ouragan majeur. Ce ne sont plus des nombres d'exercice, et la page le dit. Le
quatrième niveau entre dans le parcours **obligatoire** : ajouter un niveau ne
complique pas l'algorithme, il rend l'erreur d'ordre des tests deux fois plus coûteuse
— un vent à 200 km/h mal testé ne perd plus un niveau mais **deux**. La compétence
C8.3 y gagne : trois seuils font **six** frontières à éprouver, et le protocole de
recette passe de dix à **treize essais**.

**Quatre pages, sans rien perdre.** La séquence existe désormais en cinq fichiers :
la page complète, et quatre pages d'une séance chacune, engendrées par un générateur
à partir de la même source. Les cinq partagent la même clé d'enregistrement. La page
complète n'est pas dépréciée : elle reste le **repli** quand le réseau tombe
(règle n°122), et chaque page y ramène.

**Treize captures réelles.** Le programme de référence a été construit sur
Vittascience et photographié : la structure (démarrage, boucle, quatre modes) et le
simulateur **aux six frontières**, prises l'une après l'autre. Ces six-là sont la
pièce maîtresse du lot : entre 177 et 178 km/h, la valeur brute du potentiomètre passe
de 725 à 729 — presque rien — et le niveau **bascule**. Le « ≥ » cesse d'être une
convention d'écriture pour devenir un fait observable.

## Deux défauts trouvés par les tests, et ce qu'ils enseignent

**Le chrono était devenu muet.** Le bouton « mesurer le temps de réponse » stabilisait
le vent à 140 km/h puis le portait à 160 — deux valeurs qui, sur l'ancienne échelle,
encadraient le seuil de 150, et qui sur la nouvelle appartiennent **au même niveau**.
Le dispositif n'avait pas changé d'une ligne ; il ne mesurait plus rien. Aucune erreur
n'était levée : il affichait paisiblement « mesure en cours » pour l'éternité.

**La trace d'exécution mentait.** L'activité 5 demandait de diagnostiquer une panne à
partir d'un relevé du moniteur série. La question parlait de 71 et 95 km/h, la trace
affichait 97, 103, 126, 161, et les niveaux annoncés ne correspondaient à aucun seuil
de la v3. Un élève appliquant correctement la méthode serait arrivé à une conclusion
fausse — le pire des cas.

Les deux ont la même cause : **on avait changé les seuils, pas les données d'exercice
qui en dépendaient**. Les nombres d'un exemple vieillissent comme le code, sauf que
rien ne les compile.

## Un arbitrage qui mérite d'être dit, parce qu'il est discutable

Les captures montrent des variables nommées `seuilJaune`, `seuilOrange`, `seuilRouge`
et des sous-programmes `mode_vert` … `mode_rouge`. La séquence, elle, écrivait
`seuilTempete`, `seuilOuragan`, `seuilMajeur`, `mode_veille` … `mode_majeur` — des noms
qui désignent le **phénomène** plutôt que la couleur, ce qui est en principe préférable.

**C'est le texte qui a plié, pas la capture.** Une capture ne se refait pas à volonté :
elle demande le poste, le compte, le logiciel et le temps. Un texte se réécrit en une
commande. Et l'élève, lui, a les deux sous les yeux en même temps : le moindre écart
de nom lui coûte plus cher que le gain de précision du meilleur vocabulaire. Le
vocabulaire du phénomène n'est pas perdu pour autant — il est là où il compte, **sur
l'écran de la station**, en toutes lettres, là où un habitant le lira.

**Arbitrage validé par Pascal le 26 août** : « j'ai aligné le texte sur les captures,
pas l'inverse — c'est parfait ». La règle n°128 s'applique donc au dépôt entier, et
son corollaire avec elle : **fixer les noms AVANT de construire quoi que ce soit sur
un poste**, parce qu'une capture les gèle.

## Ce qui n'a pas été fait, et qui est écrit comme tel

La **compilation AVR** du programme de référence n'a pas été refaite : `arduino-cli`
n'est pas atteignable depuis l'environnement de production du lot. Le programme a en
revanche passé une vérification syntaxique C++ complète (`g++ -Wall -Wextra` sur
bouchons), et le banc Docker du dossier reste là pour la vraie compilation sur le
poste. Le chiffre de taille mémoire du 19 août porte sur la v2 : il est **périmé**, et
le rapport de tests le dit plutôt que de le recopier.

---

## Règle d'or n°127 — une capture ne se retouche pas ; l'écart s'explique

Quand une capture d'écran réelle diverge de ce que la page annonce — une temporisation
de 300 ms là où la consigne dit 200, des seuils antérieurs à un changement — on
**n'efface pas l'écart, on l'écrit**. En légende, en une phrase, avec ce qui le rend
sans conséquence, ou avec ce qu'il apprend.

Retoucher une capture, c'est fabriquer une preuve. La règle n°94 interdit de présenter
une reconstitution comme une capture ; celle-ci en est le prolongement : une capture
authentique le reste jusqu'au bout, y compris quand elle dérange.

Mieux : l'écart est souvent un meilleur exercice que l'accord. « Repère les deux
différences entre cette capture et ton programme » vaut mieux qu'une image lisse que
personne ne regarde.

---

## Règle d'or n°128 — entre un texte et une capture, c'est le texte qui plie

Quand un document rédigé et une capture réelle nomment différemment la même chose,
**c'est le document qu'on aligne**, jamais l'inverse.

La raison est pratique et sans appel : une capture demande le poste, le compte, le
logiciel et le temps de quelqu'un ; un texte se réécrit en une commande. Et l'élève a
les deux sous les yeux **en même temps** : un écart de nom lui coûte plus cher que ne
lui rapporte le vocabulaire le mieux choisi.

Le corollaire compte autant : **avant** de construire quoi que ce soit sur un poste,
on fixe les noms — variables, sous-programmes, fichiers — et on les écrit quelque part.
Un nom choisi à la volée pendant la construction devient, une capture plus tard, un
nom qu'on ne peut plus changer.

---

## Règle d'or n°129 — changer un seuil, c'est casser tout ce qui le franchissait

Un seuil n'est pas seulement un nombre dans une comparaison : c'est aussi **la
frontière que d'autres dispositifs traversent** — un chronomètre qui se déclenche au
franchissement, une animation qui bascule, un test qui compare un avant et un après.

Après tout changement de seuil, on rejoue **explicitement** chaque mécanisme qui
dépend d'un franchissement, et pas seulement les comparaisons elles-mêmes. Ces
dispositifs-là ne lèvent aucune erreur quand ils cessent de fonctionner : ils attendent
un événement qui n'arrive plus, et affichent tranquillement « en cours ».

Le pire des défauts n'est pas celui qui plante. C'est celui qui patiente.

---

## Règle d'or n°130 — un découpage se prouve sans perte, avant d'être livré

Découper une séquence en pages crée deux risques qu'aucune relecture ne voit :
une question **oubliée** en route, et des réponses **écrasées** quand deux pages
partagent le même enregistrement.

Les deux se prouvent par un test, écrit **avant** la livraison :

1. **l'union** des champs interactifs des pages découpées recouvre exactement ceux de
   la page d'origine — pas « à peu près », exactement, la liste à la main ;
2. la **persistance croisée** : répondre sur la page A, aller répondre sur la page B,
   revenir sur A — et retrouver sa réponse. Dans les deux sens, et en relisant depuis
   la page complète.

Ce test a effectivement attrapé le défaut dans ce lot : la fonction qui rassemblait les
réponses écrasait l'enregistrement au lieu de le fusionner. Chaque changement de page
aurait effacé la séance précédente — silencieusement, et seulement chez l'élève.

---

## Règle d'or n°131 — la flèche d'ORDRE atterrit quelque part, et on dit où

Dans un schéma des deux chaînes, la flèche d'ordre ne descend pas « vers la chaîne
d'énergie » en général : elle arrive sur **le premier bloc qu'elle commande**. Le
préactionneur quand il y en a un ; le convertisseur lui-même quand la puissance est
assez faible pour qu'une broche de microcontrôleur l'alimente directement.

Et une fonction **absente** de la chaîne se dessine — en pointillés, grisée — avec sa
raison écrite à côté. Une station qui allume et qui sonne n'a pas de fonction
TRANSMETTRE, parce que rien ne s'y déplace : le dire vaut mieux que le taire, car
l'élève qui a appris la liste des fonctions cherchera celle qui manque.

La question « et si c'était un gyrophare de 12 V ? » n'est pas un supplément : c'est
ce qui rend la règle visible. Trois cas côte à côte — le voyant direct, le relais, le
portail avec sa transmission — enseignent plus que le cas seul, quel qu'il soit.

---

## Règle d'or n°132 — les données d'exercice vieillissent comme le code, sans compilateur

Une trace d'exécution, un tableau de recette, un relevé de moniteur série, un exemple
chiffré dans un corrigé : ce sont des **données dérivées** des paramètres de la
séquence. Quand un paramètre change, elles deviennent fausses — et rien ne le signale,
parce qu'aucun outil ne les vérifie.

Elles doivent donc figurer explicitement dans la liste de ce qu'on rejoue à chaque
changement de barème, de seuil ou d'échelle. Et le test qui les couvre doit vérifier
la **cohérence interne** de l'exemple (la question parle-t-elle des mêmes valeurs que
la trace ?), pas seulement sa présence.

Un exemple faux est plus nuisible qu'un exemple absent : l'élève qui applique
correctement la méthode y arrive à une conclusion fausse, et conclut que la méthode
est mauvaise.

---

# 26 août 2026 (soir) — Le jardin connecté de 4e, refait au standard

*Deuxième lot passé au standard dégagé des audits du 21 août, dans l'ordre décidé :
la 4e, la plus en retard. Réécriture complète — il ne restait à peu près que le
sujet.*

## Ce qui n'allait pas, et ce que le contrôle a trouvé tout seul

Le vérificateur mécanisé relevait **cinq manquements** d'entrée : aucune durée
annoncée (n°23), pas de diagnostic d'entrée (n°26), pas de mode essentiel (n°29),
cinq tâches enchaînées sans tableau de bord (n°30), six zones de rédaction sans la
moindre version étayée (n°31), seize champs sans étiquette (n°34). Le lot n'avait
par ailleurs **aucune image** — pas une seule — dans une séquence dont le cœur est
un phénomène temporel.

Mais le défaut le plus grave ne se voyait ni à l'écran ni à l'exécution.

## Les mauvais verbes en face des codes

Le lot annonçait, pour 4e_C9.1, « concevoir le programme avant de l'écrire », et
pour 4e_C9.3, « réinvestir une structure ». Le programme 2024 dit :

* **4e_C9.1** — *Modifier* un algorithme permettant de répondre au besoin ou au problème posé.
* **4e_C9.2** — *Traduire* un algorithme … en un programme.
* **4e_C9.3** — *Réaliser et mettre au point* un programme commandant un système réel…

« Concevoir » est un verbe de **3e**. En annonçant ce verbe-là en 4e, le lot
promettait — et pouvait demander — autre chose que ce que le cycle prévoit à ce
moment-là. **« Modifier » interdit la page blanche** : il faut fournir un
algorithme amputé d'une exigence, et faire chercher l'endroit où intervenir. Ce
n'est pas la même séance.

Ce défaut a survécu un mois parce qu'il est **invisible à l'usage** : la page
fonctionnait très bien. Il a fallu le contrôle n°42, qui compare la carte de
référentiel au texte officiel **mot à mot**, pour qu'il apparaisse — et il est
apparu en trois secondes.

## Ce qui a été bâti

**Le banc d'essai du jardin**, intégré, hors ligne, qui rend visible ce qu'aucun
texte ne montre : curseurs d'humidité et d'heure, sélecteur de règle (un seuil /
deux seuils), et surtout un **compteur de basculements**. Mode un seuil, on fait
trembler la mesure : huit basculements. Mode deux seuils, même tremblement : zéro.
La mesure n'a pas bougé d'un point.

Le tremblement est une **suite figée dans le code**, pas un tirage aléatoire. Sans
cela on comparerait deux mesures différentes, et la démonstration ne prouverait
rien. C'est aussi ce qui la rend reproductible d'un poste à l'autre — un élève
peut inscrire les nombres obtenus dans son compte rendu et être sûr qu'ils
tiendront.

**Quatre figures**, dont une qui porte toute la séance 3 : le chronogramme qui
superpose la même mesure traitée à un seuil et à deux, avec la bande morte tramée.

**Trente questions de QCM** en remplacement de vingt-huit sommaires, dix par code,
quatre illustrées, chaque distracteur réfuté nommément.

## L'idée que la séquence essaie de faire passer

Elle tient dans l'activité 5, et c'est la seule chose qui devrait rester dans dix
ans : **un programme peut être parfaitement juste et parfaitement inutilisable.**
La pompe qui claque six fois par minute n'a aucun bug — chaque décision qu'elle
prend est correcte. C'est la *règle* qui est mal choisie.

Les élèves vont chercher le bug. Il faut les laisser chercher un peu, puis
demander : « et si aucune ligne n'était fausse ? ».

## Et le prix de la correction, dit lui aussi

L'hystérésis n'est pas un progrès gratuit : à 39 % d'humidité, la pompe ne
s'allume plus. On gagne en stabilité ce qu'on perd en réactivité. La séquence le
dit, le banc le montre, et l'activité 6 demande de **justifier** la largeur de
bande choisie plutôt que de la recopier. Une décision technique est presque
toujours un arbitrage — c'est vrai du jardin comme du reste.

---

## Règle d'or n°133 — le contrôle qui compare mot à mot est le seul qui voie les erreurs de niveau

Une formulation de compétence réécrite « avec ses mots » se lit très bien. Elle
peut pourtant annoncer un **autre niveau du cycle** que celui de la page — et rien,
dans l'usage, ne le signale : la séquence fonctionne, les élèves travaillent, le
professeur ne voit rien.

C'est pourquoi la carte de référentiel se recopie **au mot près**, et pourquoi ce
contrôle-là doit rester mécanisé : l'œil humain lit le sens et pardonne la
paraphrase. La machine compare les mots et ne pardonne rien — c'est exactement ce
qu'on lui demande.

Corollaire, dégagé en corrigeant le lot 4e : **le verbe du référentiel décide du
dispositif**. « Modifier » impose de fournir l'existant ; « écrire » impose de ne
rien fournir ; « concevoir » impose de partir du besoin. Choisir le mauvais verbe,
ce n'est pas mal rédiger un tableau : c'est préparer la mauvaise séance.

---

## Règle d'or n°134 — un verrou expérientiel se mesure sur le geste, pas sur le compteur

Le banc du jardin exigeait d'avoir « fait varier l'humidité », et le vérifiait en
comptant **six valeurs distinctes touchées**. Un élève qui saisit 25 puis 55 dans
le champ de valeur exacte n'en touche que deux : il a parfaitement fait le geste
demandé, et la page le refusait — sans lui dire pourquoi, puisque le compteur
n'était affiché nulle part.

Un verrou doit vérifier **ce qui prouve le geste**, pas ce qui est facile à
compter. Le verrou juste, ici : *avoir vu la pompe des deux côtés du seuil*. Il se
franchit en deux manipulations sensées, et il est infranchissable sans avoir
compris ce qu'on cherchait.

La question à se poser en écrivant un verrou : **« quelle est la plus petite
manipulation honnête qui le franchit ? »** Si la réponse est plus longue que le
geste enseigné, le verrou est mal réglé.

---

## Règle d'or n°135 — on habille l'élément, pas seulement la classe

*Née d'une remarque de Pascal, le 26 août : « il y a 3 colonnes, mais elles sont
difficiles à départager visuellement. Y compris pour moi. »*

Une mise en forme qui **dépend d'une classe** n'est pas une mise en forme : c'est
un **pari** sur le fait qu'on n'oubliera jamais de l'écrire. Le jour où on
l'oublie — et ce jour arrive —, l'élément se retrouve **entièrement nu**, sans
même le minimum vital.

Le cas d'école : dans le lot 3e_C9.2, un tableau à trois colonnes portait
`style="border-collapse:collapse"` et **aucune classe**. Les feuilles du dépôt ne
stylent que `table.refs` et `table.recette` : ce tableau-là n'avait donc **pas une
seule bordure**, et trois colonnes de texte long flottaient côte à côte. Pascal l'a
signalé en disant qu'il n'arrivait pas lui-même à les départager — un élève de 3e
n'avait aucune chance.

**La règle.** Tout élément dont la lisibilité dépend de sa mise en forme reçoit un
**filet de sécurité posé sur le sélecteur d'élément**, pas seulement sur la classe.
Pour les tableaux, dans chaque feuille de séquence :

```css
section.card table{border-collapse:collapse;width:100%}
section.card table th,section.card table td{padding:8px 11px;border-bottom:1px solid var(--border)}
section.card table th + th,section.card table td + td{border-left:1px solid var(--border)}
section.card table tbody tr:nth-child(even) td{background:rgba(155,190,252,.05)}
```

Oublier la classe ne produit alors plus une page **illisible**, seulement une page
**moins soignée**. C'est toute la différence entre un défaut et un accident.

**Ce qui rend un tableau illisible, précisément.** Ce n'est pas l'absence totale de
bordure : c'est l'absence de **séparateur vertical** entre colonnes. Sans lui, l'œil
doit deviner quelle cellule appartient à quelle ligne, et l'effort croît avec le
nombre de colonnes. Le contrôle mécanisable est donc celui-là — *un tableau de trois
colonnes ou plus a-t-il un séparateur de colonne ou une alternance de lignes ?* —
et non « a-t-il une bordure ».

**Ce que la mesure a donné.** Sur les 44 séquences du dépôt : 19 portent au moins un
`<table>` sans classe, mais **une seule** avait des cellules totalement dépourvues
de bordure. En revanche, **quatre tableaux** dans **trois séquences** échouaient au
bon critère — dont deux tableaux à **six colonnes**, les bancs d'essai de 5e_C9.1 et
3e_C9.1. Les quatre sont corrigés ; le filet est posé dans les trois séquences.

> **La leçon de méthode.** La recherche par `grep` annonçait 19 fichiers en défaut ;
> le rendu réel en donnait 1, puis 3 avec le bon critère. Chercher dans le texte
> source répond à « la classe est-elle écrite ? » ; **rendre la page** répond à « le
> lecteur voit-il quelque chose de lisible ? ». Ce sont deux questions différentes,
> et seule la seconde nous intéresse.

**Deuxième volet, trouvé en balayant : le débordement sur téléphone.** Même
famille, même cause. Deux choses font défiler une page horizontalement à 390 px —
un tableau plus large que l'écran, et une URL longue sans point de coupure — et
les deux sont **invisibles au bureau**. Sur les 44 séquences du dépôt, **huit**
débordaient, de 3 à 218 pixels. Le filet, encore une fois, se pose sur l'élément :

```css
@media(max-width:680px){ section.card table{display:block;overflow-x:auto} }
figcaption,.saved-note{overflow-wrap:anywhere}
```

Le pire cas était une légende de photo : `commons.wikimedia.org/wiki/File:Coney_Island_Stillwell_Avenue_Entrance_001.jpg`.
Les traits de soulignement n'offrent aucune coupure par défaut, et 218 pixels de
page partaient hors écran — sur une séquence par ailleurs excellente. **Personne
ne l'aurait vu en la relisant**, parce qu'on relit sur un écran d'ordinateur.

**Et quand trois colonnes restent trois colonnes de trop.** Le filet rend un tableau
lisible ; il ne le rend pas *évident*. Quand chaque colonne porte une idée et non
une donnée — « ce que c'est / qui la produit / ce que ça dit » —, ce n'est plus un
tableau qu'il faut, ce sont des **cartes** : une par ligne, empilées, chacune avec
son titre, sa couleur et sa hiérarchie interne. C'est ce qu'est devenu l'encadré
mesure / vigilance / alerte. Bénéfice second, et gratuit : sur un téléphone, trois
cartes s'empilent alors que trois colonnes s'écrasent.

---

## Règle d'or n°136 — un dispositif est installé quand son effet est mesuré, pas quand ses commandes sont posées

*Née le 26 août, en écrivant la suite de tests du lot 3e_C9.1 — c'est-à-dire en
essayant de prouver ce que je venais de déclarer fait.*

Le sélecteur de parcours du lot était complet : trois boutons 🅰/🅱/🅲, l'état
`aria-pressed` correct, la classe `parcours-a|b|c` appliquée au `body`, la note
« Parcours affiché : 🅲 sans matériel » qui s'écrivait bien. Sept lignes de CSS
prêtes à masquer `[data-parcours]`. Et **aucun élément de la page ne portait
`data-parcours`**.

Le dispositif masquait donc **zéro bloc sur zéro bloc concerné** — et affichait
sereinement qu'il avait changé de parcours. Toute question de la forme « le
sélecteur est-il présent ? », « la classe s'applique-t-elle ? », « la note
change-t-elle ? » répondait **oui**. Il a fallu la seule question qui compte —
*combien de blocs sont effectivement masqués ?* — pour que le vide apparaisse.

**La règle.** Un dispositif ne se déclare pas installé sur la présence de ses
commandes. Il se déclare installé sur la **mesure de son effet**, exprimée en
nombre : *n blocs masqués sur n concernés*, *la carte de référentiel passe de
visible à invisible*, *le panneau actif change*, *la progression reste à 0*. Un
contrôle dont le résultat attendu est « oui » plutôt qu'un nombre ne contrôle rien.

C'est la sœur de la règle n°135 : là, on avait posé la classe sans l'habillage ;
ici, on avait posé le sélecteur sans ce qu'il sélectionne. Même famille de
défaut — **le mécanisme complet, branché sur rien** — et même remède : mesurer au
rendu, pas dans la source.

**Corollaire pour les tests.** Un test qui ne peut pas échouer ne prouve rien.
`0 masqués sur 0 concernés` doit être un **échec**, pas un succès : c'est ce
choix-là, dans une seule ligne de la suite, qui a fait apparaître le défaut.

---

# 26 août 2026 (nuit) — 3e_C9.1 harmonisée, et deux balayages du dépôt

*Troisième lot repris dans l'ordre décidé. Contrairement au 4e, celui-ci n'avait
pas besoin d'être réécrit : le contenu est excellent — l'exécution à la main dans
un simulateur de mémoire, le piège des guillemets, la chasse aux bugs. Il lui
manquait les **dispositifs communs** du dépôt, pas des idées.*

## Ce qui a été posé, sans toucher au fond

Billet d'entrée (n°26), mode essentiel (n°29), tableau de bord des tâches (n°30),
versions étayées pour les deux zones de rédaction (n°31), sélecteur de parcours
(n°122), boutons de séance suivante (n°101), carte de référentiel (n°42). Cinq
manquements mécanisés → zéro.

## Un faux positif du contrôle, et ce qu'il enseigne

La règle n°34 signalait **trente champs sans étiquette**. Vérification faite :
les trente étaient enveloppés dans un `<label>`, ce qui est parfaitement valide —
c'est la forme *implicite* de l'étiquetage, et les lecteurs d'écran la gèrent.
Le contrôle ne cherchait que la forme *explicite*, `<label for="…">`.

**Le contrôle avait tort, et il avait raison de le dire quand même.** La forme
explicite est plus robuste : elle survit à un déplacement du champ hors du label,
ce que la forme implicite ne fait pas. J'ai donc ajouté `for="…"` aux trente
labels — un attribut, aucun changement visuel — plutôt que de discuter avec
l'outil. Mais le faux positif est signalé à Pascal : un contrôle qui accuse à tort
finit par être ignoré, et c'est alors qu'il laissera passer un vrai défaut.

## Ce que les durées annoncées cachaient

Le contrôle n°23 ne voyait aucune durée : la page écrivait « ⏱ 25 min » quand la
convention du dépôt est « ⏱ ~25 min », avec le tilde. Un détail — sauf qu'en les
rendant visibles, le total apparaissait : **215 minutes annoncées pour 220
disponibles**, marge de service comprise. Autrement dit, quatre séances remplies à
ras bord, sans une minute pour installer, ranger, ou laisser un élève finir.

Les durées ont été ramenées à 45 minutes de travail dans un créneau de 55. Ce
n'est pas un ajustement cosmétique : c'est la différence entre une séance qui
tient et une séance qui déborde toujours de dix minutes.

## Le progrès du cycle, enfin visible en un tableau

En recopiant la formulation officielle de 3e_C9.1 — *« Élaborer ou concevoir un
algorithme … puis le traduire en un programme structuré … le tester et le mettre
au point »* —, la progression du cycle est apparue d'un bloc :

| Niveau | Le verbe | Ce qu'on fournit à l'élève |
|---|---|---|
| 5e_C9.1 | **analyser** un programme fourni, et le **tester** | tout : le programme existe et fonctionne |
| 5e_C9.2 | **modifier** un programme fourni | le programme, à retoucher |
| 4e_C9.1 | **modifier** un *algorithme* | l'algorithme, amputé d'une exigence |
| 4e_C9.2 | **traduire** un algorithme en programme | l'algorithme complet |
| 3e_C9.1 | **élaborer**, traduire, tester, mettre au point | **rien que le besoin** |
| 3e_C9.2 | **réaliser et mettre au point**, avec IHM | rien que le cahier des charges |

Lue de haut en bas, la dernière colonne dit tout : **on retire progressivement ce
qu'on donne**. La difficulté du cycle ne tient pas à des programmes plus longs,
elle tient à ce qui manque au départ. Ce tableau est entré dans la séquence, en
encadré dépliable — un élève de 3e a le droit de savoir où il en est.

## Le sélecteur de parcours branché sur rien — et la suite qui l'a trouvé

Le lot n'avait **aucune suite de tests committée**. Son rapport annonçait 30/30 au
30 juillet : la campagne avait bien eu lieu, mais rien dans le dépôt ne permettait
de la rejouer. Un rapport qu'on ne peut pas rejouer est une affirmation, pas une
preuve — et il vieillit en silence pendant qu'on modifie la page.

`tests_3e_C9.1.mjs` est donc écrite et committée : **35 tests**, tous verts, qui
vérifient chacun des six dispositifs posés *par son effet à l'écran*. Elle a
immédiatement rapporté deux échecs, dont celui qui a fondé la règle n°136 : le
sélecteur de parcours ne masquait rien.

Ce qui n'a **pas** été masqué en 🅲, et c'est délibéré : les barres 🧪 des éditeurs
Vittascience. Ce sont elles qui portent le verrou d'expérience des activités 3 et
4 ; les masquer aurait retiré deux validations, ce qu'interdit la règle n°122. En
🅲, une consigne dédiée dit quoi faire au cahier — on remplace le geste, on ne
supprime pas la question.

> **Ce que je retiens pour les lots suivants.** Écrire la suite de tests n'est pas
> la formalité qui clôt une harmonisation : c'est l'opération qui la vérifie. Les
> six dispositifs, je les avais déclarés posés — et l'un des sept était creux. Je
> ne l'aurais jamais vu en relisant mon propre travail, parce qu'en relisant on
> retrouve ce qu'on croit avoir écrit.

---

# 26 août 2026 (soir) — 5e_C9.1 harmonisée : le C9 est complet

*Dernière marche du C9 reprise, dans l'ordre annoncé. Comme pour le 3e, le contenu
n'avait pas besoin d'être touché — le compteur du Cyclone de Coney Island, le
programme fourni qui ment sans planter, le cas frontière de la barrière à zéro
place. Il manquait les dispositifs communs, et une carte de référentiel.*

## Ce qui a été posé

Billet d'entrée (n°26 — sur les acquis de **cycle 3**, pas de 4e : c'est la première
marche), mode essentiel (n°29), tableau de bord (n°30), versions étayées (n°31),
étiquettes explicites (n°34), durées à la convention (n°23), carte de référentiel
(n°42), sélecteur de parcours (n°122) et boutons de séance suivante (n°101).
Quatre manquements mécanisés → zéro. `tests_5e_C9.1-C9.3.mjs` : **44 tests, tous verts**.

## Les deux fautes que la suite a rattrapées — et ce qu'elles confirment

**Première.** La feuille de style des nouveaux dispositifs a été insérée **hors de
toute balise `<style>`**. Le bouton basculait, la classe `parcours-c` s'appliquait au
`body`, la note s'écrivait — et rien ne se masquait. C'est mot pour mot le défaut de
la règle n°136, commis **le jour même où je l'ai écrite**, sur le lot suivant.

Ce n'est pas une ironie, c'est une confirmation : ce défaut-là ne se voit pas en
relisant, parce que tout ce qu'on relit est correct. Le CSS est juste, le JS est
juste, le HTML est juste. Seul le **lien** entre eux manque, et il ne s'écrit nulle
part. Il n'y a qu'une façon de le voir : compter, au rendu, ce qui a effectivement
disparu.

**Seconde.** L'ajout automatique des `for=` sur les étiquettes a mangé le `>` fermant
de la balise `<label>`, avalant les listes déroulantes dans leur propre étiquette. La
page se chargeait **sans la moindre erreur** — un navigateur répare ce genre de HTML
en silence. C'est Playwright qui a refusé de sélectionner une option « dans un élément
qui n'est pas un `<select>` ».

> **Ce que j'en retiens.** Une transformation automatique sur du HTML doit être
> vérifiée par un test qui **manipule** le résultat, jamais par une relecture ni par
> un compte d'occurrences : le compte était bon (21 étiquettes ajoutées), et le
> fichier était cassé. L'avertissement est désormais écrit en commentaire dans le
> script de transformation, à l'endroit exact où la faute est possible.

## Un README qui renvoyait ailleurs

`5e_C9.1/README.md` annonçait encore « **COUVERT** — mutualisé dans le mini-projet
Thème 3 ». C'était vrai avant que l'atelier existe. Depuis, un collègue arrivant dans
le dossier était renvoyé vers une autre ressource alors que celle qu'il cherchait
était sous ses yeux, complète, avec son QCM et ses synthèses. Réécrit.

C'est le genre de désaccord qu'aucun contrôle mécanisé ne voit : le README est
présent, il est bien formé, il pointe vers un fichier qui existe. Il est simplement
**périmé**. La seule parade connue reste de relire le README quand on touche au lot —
ce qui n'arrive que si l'on s'astreint à le faire.

## Où en est le C9

| Lot | Contrôle mécanisé | Suite committée |
|---|---|---|
| 5e_C9.1 → C9.3 | 0 manquement | ✔ 44 tests |
| 4e_C9.1 → C9.3 | 0 manquement | ✔ 61 tests |
| 3e_C9.1 | 0 manquement | ✔ 35 tests |
| 3e_C9.2 + 3e_C8.3 | 0 manquement | ✔ 129 tests |

**La compétence C9 est harmonisée sur les trois niveaux du cycle**, et chacun des
quatre lots porte désormais une suite qu'un autre que moi peut rejouer.

---

## Règle d'or n°137 — un QCM se mesure aussi par la POSITION de ses bonnes réponses

*Née le 26 août, en harmonisant l'arc « jardin connecté » de 4e. Trouvée par un test
qui comptait, pas par une relecture — comme les deux précédentes.*

Dans le QCM de 4e_C7, les **28 bonnes réponses étaient en position B**. Dans celui de
4e_C8 aussi. Un élève qui clique la deuxième proposition à chaque question obtenait
**28/28** — sans rien savoir, et sans tricher : en découvrant un motif.

**Ce que ce défaut a de particulier**, c'est qu'il est invisible partout où l'on
regarde d'habitude. Chaque question, prise seule, est irréprochable : l'énoncé est
juste, les distracteurs sont plausibles, l'explication est bonne. Le défaut n'existe
qu'au **niveau de la collection**, et aucune relecture question par question ne peut
le voir. Il faut compter.

**La règle.** Tout QCM du dépôt répartit ses bonnes réponses sur les quatre positions,
à une unité près. Le contrôle est une ligne : compter les positions, et échouer si
l'une manque. Un QCM dont les bonnes réponses sont concentrées ne mesure plus la
connaissance : il mesure la vitesse à laquelle l'élève trouve le motif.

**Corollaire sur la façon de corriger.** On ne redistribue pas au hasard : un tirage
aléatoire donne un fichier différent à chaque exécution, impossible à relire et
impossible à rejouer. On fait **tourner** les propositions (l'ordre relatif des
distracteurs est conservé) vers une suite de positions **écrite en clair** dans
l'outil. Et l'outil vérifie, après rotation, que la proposition arrivée à la nouvelle
position est bien le texte de l'ancienne bonne réponse — sans cette assertion, une
erreur de rotation fausserait silencieusement tout le QCM.

---

# 26 août 2026 (nuit) — l'arc « jardin connecté » de 4e harmonisé, et un QCM qui ne mesurait rien

*Le C9 étant complet sur les trois niveaux, la suite logique était l'amont : C7
(concevoir le support) et C8 (le valider), même objet-fil, même année. Les deux
séquences sont d'une génération antérieure du dépôt — pas de tableau de bord, pas de
mode essentiel, pas de progression.*

## Ce qui a été posé, sans toucher au fond

Billet d'entrée, mode essentiel, tableau de bord des six activités, versions étayées,
durées à la convention, carte de référentiel, sélecteur de parcours agissant, barre de
progression reliée aux validations. **Cinq manquements mécanisés → zéro**, sur chacun
des deux lots. Deux suites committées, **41 tests chacune**, toutes vertes.

## Le défaut qui comptait vraiment

Voir la règle n°137 ci-dessus : les 56 bonnes réponses des deux QCM étaient en position
B. Le balayage des 40 QCM du dépôt a ensuite trouvé **deux autres cas dans le Thème 3**
(5e_C7 : 24 questions, 3e_C7 : 26 questions — corrigés) et **trois dans le Thème 2**,
hors périmètre :

| Fichier (Thème 2 — pour Pascal) | Constat |
|---|---|
| `3e_C4.7/qcm_3e_C4.7-C4.8_internet_sainte_luce.html` | 30 q · 8 / **21** / 1 / 0 |
| `3e_C4.3/qcm_3e_C4.3-C4.6_station_alerte_cyclonique.html` | 32 q · 4 / **20** / 8 / 0 |
| `4e_C4.1/qcm_automatisation_premium.html` | 10 q · format différent, position non lisible |

Je n'y touche pas — c'est le périmètre du Thème 2. L'outil qui corrige,
`repartir_qcm.mjs`, est committé dans `4e_C7.1/` et fonctionne sur n'importe quel QCM
de ce format.

## Une décision de formulation, à valider

La séquence 4e_C7 annonçait « 4 × 55 min » pour **85 minutes** d'activités. Les deux
séances manquantes ne sont pas perdues : elles se passent sur le TP « Le dé sur son
socle » et sur l'atelier de planification, tous deux liés en bas de page. L'en-tête dit
maintenant « 2 séances de 55 min **sur cette page** (+ 2 séances sur le TP et
l'atelier) ». C'est une formulation, pas un changement de contenu — mais elle engage la
lecture du lot, et si le découpage réel est autre, c'est à corriger d'un mot.

## Ce que les trois dernières règles ont en commun

n°135 (l'habillage posé sur la classe, pas sur l'élément), n°136 (le sélecteur branché
sur rien), n°137 (les bonnes réponses toutes au même endroit) : **aucune des trois ne
se voit en relisant**. Chaque pièce, prise seule, est correcte. Le défaut n'apparaît
qu'en mesurant quelque chose au niveau de l'ensemble — une couleur calculée, un compte
de blocs masqués, une distribution de positions.

C'est, je crois, la leçon de méthode de ces deux journées : **relire prouve que chaque
morceau est juste ; seul un compte prouve que l'ensemble l'est**.

---

# 26 août 2026 (fin de nuit) — le Thème 3 est harmonisé en entier

*Les deux dernières séquences de l'ancienne génération — 5e_C7.1 (le voyant du hall)
et 3e_C7.1 (le capteur de confort) — reçoivent la même recette que l'arc de 4e.*

## L'état du thème, en un tableau

| Lot | Contrôle mécanisé | Suite rejouable |
|---|---|---|
| 5e_C7.1 · C8.3 · C9.3 | 0 manquement | 37 tests |
| 4e_C7.1 · C7.2 · C7.3 | 0 manquement | 41 tests |
| 3e_C7.1 · 3e_C8.1 | 0 manquement | 37 tests |
| 4e_C8.1 · C8.2 · C8.3 | 0 manquement | 41 tests |
| 5e_C9.1 → C9.3 | 0 manquement | 44 tests |
| 4e_C9.1 → C9.3 | 0 manquement | 61 tests |
| 3e_C9.1 | 0 manquement | 35 tests |
| 3e_C9.2 + 3e_C8.3 | 0 manquement | 129 tests |

**12 séquences analysées, 0 manquement mécaniquement établi, 8 suites committées,
425 tests, tous verts.** C'est la première fois qu'un thème entier du dépôt est dans
cet état.

## Trois choses trouvées sur ces deux derniers lots

**Une carte de référentiel en double.** Le lot 5e en possédait déjà une, et mieux écrite
que celle que j'allais poser : elle porte l'histoire de la correction des codes — « cette
séquence annonçait auparavant C7 · C8 · C9, c'est-à-dire douze compétences pour en servir
trois ». J'ai retiré la mienne. Poser un dispositif sans regarder si le lot en avait déjà
un, c'est écraser un travail antérieur au motif qu'on ne l'a pas cherché.

**Un raccourci du contrôle n°42, à signaler à Pascal.** La règle cherche
`referentiel-card`, puis le **premier `</table>` qui suit**. Comme le mot apparaît d'abord
dans la feuille de style (`body.essentiel .referentiel-card{display:none}`), c'est le
premier tableau de la page qui est lu — pas la carte. Le contrôle annonce alors « aucun
code reconnu » sur une page qui porte pourtant une carte parfaitement conforme. Contourné
en plaçant la carte avant tout autre tableau — ce qui est de toute façon sa place logique —
mais le raccourci reste à corriger dans `_outils/` (périmètre Thème 2).

**Un verrou qui n'existe pas.** Ces deux lots n'ont pas de verrou expérientiel à
l'activité 0, contrairement à ceux de 4e. La suite l'écrit noir sur blanc — « contrôle NON
applicable, donc NON exécuté » — au lieu de compter un succès qu'elle n'a pas obtenu. Un
test qui ne s'exécute pas ne doit jamais ressembler à un test qui passe.

## Ce qui reste, et qu'il faut dire

Les six QCM de C7 et C8 sont de la **génération ancienne** : 24 à 28 questions au lieu de
30, et **aucune réfutation par distracteur**. Leurs bonnes réponses sont maintenant bien
réparties, leurs explications sont là — mais ils n'expliquent pas pourquoi chaque mauvaise
réponse est fausse, ce que font les QCM des lots C9. C'est le prochain chantier naturel du
thème, et il est écrit dans chaque rapport plutôt que laissé à deviner.

---

# 27 août 2026 — le dépôt entier passé au crible des règles récentes

*Demande de Pascal en partant : « on a ajouté de nouvelles règles et ces règles
changent certaines choses, pour ne pas dire beaucoup de choses ». Il a raison, et
la seule façon honnête de le savoir était de MESURER les 44 séquences.*

## Ce qu'il fallait mesurer, et pourquoi aucun grep ne suffit

Les règles n°135, n°136 et n°137 ont ceci de commun qu'elles décrivent des défauts
**invisibles dans la source**. Un tableau sans séparation a une balise `<table>`
parfaitement valide ; un sélecteur branché sur rien a ses boutons, sa classe et sa
note ; un QCM concentré en position B a trente questions irréprochables. Il faut
rendre la page et compter.

D'où `mesures_rendu.mjs` : il ouvre les 44 séquences dans un vrai navigateur, aux
deux tailles d'écran, clique les dispositifs et **compte leur effet**.

## Trois fois de suite, ma mesure a menti — et c'est instructif

**Premier mensonge : la contamination par le stockage local.** Toutes les
séquences ouvertes en `file://` partagent la **même origine**, donc le même
`localStorage`. Une page qui enregistrait « parcours = c » contaminait la suivante,
qui se chargeait déjà dans cet état : le clic ne masquait plus rien, et la page
saine était déclarée en défaut. Quatre fausses alertes. Correctif : vider le
stockage avant chaque séquence.

**Deuxième mensonge : compter les éléments invisibles.** Je comptais les blocs
cachés avant et après le clic. Or un bloc rangé dans un onglet inactif est déjà
invisible — sans que le dispositif y soit pour quoi que ce soit. Correctif : ne
compter que ce qui était visible avant.

**Troisième mensonge, le plus subtil.** Même corrigée, la mesure accusait le lot
book-train : « mode essentiel branché sur rien ». Vérification faite, ses neuf
cibles étaient toutes dans des panneaux inactifs — le dispositif fonctionne
parfaitement dès qu'on est sur le bon onglet. Correctif : mesurer le `display`
**propre** de la cible, qui ne dépend pas de celui de ses ancêtres.

> **Ce que ces trois erreurs enseignent.** Un contrôle qui accuse à tort est pire
> qu'un contrôle absent : il use la confiance, et le jour où il a raison, on ne le
> croit plus. Avant de publier un chiffre, il faut se demander *ce que la mesure
> mesure vraiment* — et aller vérifier à la main le premier cas qu'elle dénonce.
> Sans cette vérification, j'annonçais neuf défauts là où il y en a six.

## Le résultat, une fois la mesure fiable

**44 séquences, 38 sans le moindre défaut de rendu.** Six défauts réels :

| Où | Défaut |
|---|---|
| 3e_C9.2 — pages 3 et 4 (Thème 3) | sélecteur de parcours branché sur **rien** |
| 3e_C4.3, 3e_C4.7, 3e_C5.1, 3e_C6.1 (Thème 2) | débordement horizontal sur téléphone (3 à 61 px) |

## Ce qui est corrigé ici (Thème 3)

Les pages 3 et 4 du découpage de la station portaient les quatre boutons
🅰/🅱/🅲/tous, changeaient la classe du `body`, écrivaient leur note — et n'avaient
**aucun bloc `data-parcours`** à filtrer. Le générateur retire désormais le
sélecteur des pages qui n'ont rien à masquer, et le remplace par un rappel : le
choix se fait en page 1, il est retenu pour toute la séquence.

Deux tests l'exigent maintenant, page par page : *le sélecteur n'est présent que
s'il a des blocs à masquer*, et *quand il est absent, l'élève est renvoyé à
l'endroit où le choix se fait*. Ce second test a d'ailleurs immédiatement échoué :
ma note de rappel portait `id="parcoursNote"`, l'identifiant que le script commun
réécrit à chaque affichage — ma phrase était remplacée au chargement par
« Parcours affiché : tous ». Un identifiant propre a réglé la chose. Encore un
défaut qu'aucune relecture n'aurait vu : le HTML était juste, le JS était juste.

**Thème 3 : 12 séquences, 0 manquement mécanisé, 0 défaut de rendu, 8 suites,
431 tests.**

## Ce qui reste, et pour qui

Les quatre débordements mobiles sont dans le **Thème 2** : ils font l'objet d'une
livraison séparée, sur une branche à ce nom, avec l'outil de mesure lui-même
(`_outils/mesures_rendu.mjs`) pour que le contrôle soit rejouable par n'importe
qui — et pas seulement par moi.

---

# 27 août 2026 — la série des TP de CAO renumérotée, sur arbitrage de Pascal

*Erreur de ma part, tranchée par lui. En écrivant un second TP de 4e, j'ai pris
le numéro « n°3 » parce qu'il suivait le n°2 du TP de 4e que je venais de lire.
Je n'avais pas regardé qu'un n°3 existait déjà.*

## Ce que la numérotation voulait dire, et ce qu'elle veut dire maintenant

Elle désignait le **niveau** : n°1 pour la 5e, n°2 pour la 4e, n°3 pour la 3e.
Un seul TP par année, un numéro par année. Cette convention n'avait pas de place
pour un **second TP de 4e** — et c'est exactement ce que « Le dé sur sa pointe »
est venu être.

Arbitrage de Pascal : le numéro devient un **rang dans la série**, pas un code de
niveau.

| Rang | TP | Niveau |
|---|---|---|
| n°1 | Le dé, dans Onshape | 5e |
| n°2 | Le dé sur son socle | 4e |
| n°3 | Le dé sur sa pointe, et la porte n°2 | 4e |
| n°4 | Le boîtier étanche | 3e |

Le boîtier étanche passe donc de n°3 à n°4 — quatre remplacements, dans les trois
copies du fichier et dans son scénario JSON. Les quatre titres ont été relus au
rendu réel, pas dans la source.

> **Ce que je retiens.** Un numéro dans un titre n'est jamais un simple ornement :
> il porte une convention, et cette convention porte une hypothèse — ici « un TP
> par niveau ». Avant d'ajouter un élément à une série numérotée, il faut lire la
> série entière et se demander **ce que le numéro compte**. J'ai pris le suivant
> du seul fichier que j'avais sous les yeux, ce qui revenait à supposer une
> convention au lieu de la vérifier.

---

## Règle d'or n°138 — une ressource qui se nomme elle-même l'emporte sur son nom de fichier

*Née le 27 août, d'une observation de Pascal devant l'index : « 4e_C7.2 » et
« 4e_C7.6 » affichaient tous deux « Travaux pratiques — Socle assemblage ». Deux
repères, un seul intitulé, et aucun moyen de voir qu'il existe une série.*

La règle n°37 dit déjà que l'interface montre des **ressources**, pas des
fichiers. L'index l'appliquait en nettoyant le nom de fichier : préfixe retiré,
codes retirés, jetons recollés. Ce nettoyage produit un libellé lisible — mais il
ne peut produire que ce que le nom de fichier contient. Or `tp_4e_socle_assemblage.html`
ne sait ni que ce TP est le **n°2**, ni qu'il y en a **quatre**, ni que la série
va de la 5e à la 3e.

**La règle.** Quand une ressource porte un titre canonique dans son contenu —
le `<h1>` d'une page — c'est ce titre qui fait foi dans l'index, et non le nom du
fichier. Le nom de fichier reste le repli, pour les ressources qui ne se nomment
pas.

Appliqué aux TP : l'index lit `TP n°2 — Le dé sur son socle` dans le `<h1>`, y
ajoute le niveau tiré du chemin, et affiche **« TP n°2 · 4e — Le dé sur son
socle »**. La série entière et sa chronologie deviennent lisibles d'un coup d'œil,
ce qui est précisément l'esprit du programme 2024 — une progression, pas quatre
activités indépendantes.

**Mesuré, pas supposé** : sur les 188 libellés de l'index, **six** changent — les
trois TP, chacun présent en deux exemplaires sous deux codes. Les 182 autres sont
identiques au caractère près. Un TP dont le `<h1>` ne suit pas la forme
« TP n°N — … » garde son ancien libellé, sans traitement particulier : c'est le
cas du TP mBot2, et c'est voulu.

---

# 27 août 2026 — la série des TP lisible depuis l'index

Suite immédiate de la renumérotation : le numéro ne servait à rien tant qu'il
n'était pas **visible là où l'on choisit une ressource**. `_outils/make_index.py`
lit désormais le `<h1>` des TP (règle n°138 ci-dessus).

| Avant | Après |
|---|---|
| Travaux pratiques — De onshape | TP n°1 · 5e — Le dé, dans Onshape |
| Travaux pratiques — Socle assemblage | TP n°2 · 4e — Le dé sur son socle |
| Travaux pratiques — Boitier etanche | TP n°4 · 3e — Le boîtier étanche |

Au passage, les accents reviennent — « Boitier etanche » redevient « boîtier
étanche ». Le nettoyage par jetons les avait perdus en chemin, et personne ne
l'avait relevé parce qu'on lit l'index en diagonale.

---

# 27 août 2026 — les QCM de C7 et C8 changent de génération

Quatre QCM du Thème 3 dataient d'avant le standard C9 : 5e_C7.1, 4e_C7.1,
4e_C8.1 et 3e_C7.1. On les disait « sans réfutation par distracteur ». En les
ouvrant, le défaut était plus grave que ça.

**Les distracteurs n'étaient pas des distracteurs.** Extraits authentiques du
QCM de 5e :

| Question | Propositions offertes |
|---|---|
| « Un planning sert à : » | Remplacer les tests · Éviter de réfléchir · **Rien** · Organiser les tâches |
| « A / B / C = » | Trois profs · Trois notes · Matériel / simulation / papier · Trois langues |
| « LED qui ne s'allume pas → » | Ignorer · **Changer d'école** · Valider quand même · Non conforme |

Un élève qui ne sait rien élimine « Rien », « Trois profs » et « Changer
d'école » en trois secondes, et tombe sur la bonne réponse par soustraction. Le
QCM ne mesurait pas la connaissance : il mesurait la lecture.

**Décision : on ne rajoute pas de réfutations sous ces questions-là.** Une
réfutation de « Trois profs » n'enseignerait rien. Les quatre banques sont
**réécrites**, ancrées dans le contenu réel de leur séquence — M. Alvarez et ses
trois chutes en un mois, M. Ortiz qui ne replante pas sans arrosage, Mme Reyes
qui n'a aucun chiffre à opposer à l'emploi du temps.

**Ce qui change, en chiffres** : 24-28 questions → **30** · 0 réfutation →
**90 par QCM** · 0 image → **3 documents SVG à lire** · 0 test → **13 par QCM**.
Soit 120 questions, 360 réfutations, 12 SVG originaux, 52 tests verts.

**Les fichiers gardent leur nom.** `qcm_5e_C7_mini-projet.html` reste
`qcm_5e_C7_mini-projet.html` : aucun lien du dépôt n'est cassé, aucun orphelin
n'est créé. C'est le contenu qui change de génération, pas l'adresse — et la
règle n°138 veut de toute façon que la ressource se nomme dans son `<h1>`.

**Un contrôle nouveau, et il compte.** La suite vérifie que la réfutation
affichée après une réponse fausse est bien celle de la proposition CHOISIE.
C'est le garde-fou contre le piège rencontré en juillet sur les QCM du Thème 2 :
les tableaux `o` et `d` sont parallèles, et les permuter séparément colle à
chaque mauvaise réponse l'explication d'une autre — un QCM qui explique de
travers, sans que rien ne le signale.

**Ce qui reste à faire, et qui n'appartient pas à la machine** : relire les
120 questions. Aucun test ne dira qu'un distracteur est plausible ni qu'une
réfutation enseigne. C'est écrit en toutes lettres dans le rapport.


---

## Règle d'or n°139 — une réfutation écarte une proposition DANS LE CAS ÉTUDIÉ ; elle n'énonce pas une loi

*Née le 27 août 2026, de la relecture des quatre banques de C7 et C8 par
ChatGPT à la demande de Pascal. Vingt-huit questions en rouge, trente-cinq en
orange — et, une fois les objections examinées une par une, presque toujours le
même geste fautif.*

Le défaut n'est pas dans les questions. Il est dans les phrases qui les
entourent : la réfutation qui, pour écarter une mauvaise proposition, se donne
de l'élan et énonce une règle générale. Trois exemples authentiques, tous
retirés dans ce lot :

| Ce qui était écrit | Pourquoi c'est faux |
|---|---|
| « L'épaisseur ne change rien à l'absorption. » | Elle retarde, et sur un carton enduit elle change tout. |
| « Une découpe bien faite n'abîme rien. » | Toute découpe modifie la tranche — c'est même pour cela que la tranche est le point faible d'une pièce. |
| « La règle vient du métier, pas de la classe. » | Le professeur l'exige bel et bien. La réfutation niait un fait vrai. |

Le mécanisme est toujours le même : pour être convaincante, la réfutation
monte d'un cran en généralité — et à ce cran-là, elle devient fausse. Elle est
lue par **tous** les élèves, y compris ceux qui ont répondu juste. Une banque
de trente questions et quatre-vingt-dix réfutations peut ainsi enseigner
tranquillement une dizaine de contre-vérités que personne ne relit jamais,
parce qu'on relit les questions et pas leurs marges.

**La règle.** Une réfutation dit pourquoi CETTE proposition ne convient pas
POUR CE CAS. Elle ne dit pas ce qui est vrai en général. Quand la
généralisation est utile à l'élève, elle a un autre endroit : l'explication,
le « à retenir », ou la nuance.

---

## Règle d'or n°140 — ce qu'on refuse de changer doit être expliqué à l'élève, pas défendu au relecteur

*Née de la consigne de Pascal, le 27 août 2026 : « tout ce qui est en orange
ou en rouge doit être soit changé, soit justifié, exhaustivement dans les
corrections » — puis, aussitôt après : « de façon vulgarisée, abordable à un
élève, même en difficulté ».*

Une relecture produit deux sortes de remarques : celles qu'on accepte, et
celles qu'on écarte. Le réflexe ordinaire consiste à répondre au relecteur —
dans un fil de discussion, dans un compte rendu — et à laisser la ressource en
l'état. Or si un relecteur adulte a buté sur un point, un élève y butera aussi.
La réponse existe, elle est bonne, et elle est rangée là où l'élève ne la
lira jamais.

**La règle.** Une objection écartée se traite DANS la ressource, à l'endroit
exact où elle naît, et dans la langue de celui qui apprend. Le compte rendu au
relecteur dit ce qui a été fait ; il ne remplace jamais ce qui a été fait.

**La mise en œuvre.** Un champ facultatif `nuance` entre dans le schéma des
questions, rendu dans le bloc de correction sous le titre **« 🤔 Et si tu te
disais… »**. Il est écrit pour l'élève qui a hésité, pas pour le relecteur :
il commence par l'objection, entre guillemets, dans les mots que l'élève
emploierait — puis il y répond sans esquiver.

Soixante-trois questions en portent une aujourd'hui. Quelques-unes disent
franchement « tu as raison » : le bouton pressé par un humain n'est pas un
capteur, le parallélogramme des entrées existe bel et bien, « deux cents élèves
en huit minutes » est bien un fait compté. Une objection recevable rend la
correction meilleure ; il n'y a aucune raison de la cacher.

---

## Règle d'or n°141 — une validation ne vaut que pour le protocole exécuté, et le dire fait partie de la leçon

*Née d'une contradiction interne, trouvée en relisant la banque de 3e : la
question 16 faisait valider l'objet sur quatre scénarios, et la question 17 —
la suivante — montrait que ces quatre scénarios avaient laissé passer le
clignotement au seuil.*

La tentation était d'ajouter un cinquième scénario et de faire disparaître la
gêne. C'est l'inverse qui a été fait : **les deux questions restent, dans cet
ordre**, et la nuance de la question 16 annonce que la suivante va la
contredire. « Validé » ne veut pas dire « parfait » : cela veut dire
« conforme à tout ce qui a été testé » — une phrase qui contient sa propre
limite, et qu'il faut apprendre à lire en entier.

Deux autres énoncés ont été corrigés au même titre, parce qu'ils promettaient
plus qu'un essai ne peut donner : « un prototype qui passe tous les tests du
premier coup a surtout mal été testé » (faux, et décourageant — remplacé par la
lecture des marges), et « réinvestir la même règle sur un autre objet prouve
qu'on l'a comprise » (c'est un signe, pas une preuve).

**La règle.** Toute affirmation de validité s'écrit avec son domaine :
pour quels cas, avec quel instrument, dans quel modèle. Un résultat sans
domaine est un résultat qu'on ne peut ni contester ni réutiliser.

---

## Règle d'or n°142 — un test discriminant ne fait varier qu'une seule chose

*Née de l'erreur la plus grave du lot, et elle était de moi.*

La banque de 4e proposait, pour départager « l'attache a cassé à cause du
froid » d'une autre cause, de la remplacer par une attache en inox : si elle
tient, c'était bien le matériau. Vingt questions plus loin, la même banque
expliquait que **l'attache inox est plus lourde** et fait tomber la stabilité de
0,5 à 1,2 cm. Le test proposé changeait donc deux choses à la fois, et ne
départageait rien du tout — et le lot contenait lui-même la démonstration de
son erreur.

Le bon test ne remplace rien : il reprend l'attache d'origine et la sollicite
deux fois, une fois à −8 °C et une fois à température ambiante. Une seule
grandeur change. C'est le même principe qu'à la question 19 de la 3e, où
l'on affiche la valeur mesurée plutôt que de rebrancher le capteur au hasard.

**La règle.** Entre les deux essais d'un test discriminant, une seule chose
change. Un essai qui en change deux ne prouve rien, quel que soit son résultat
— et il est d'autant plus dangereux qu'il donne l'impression d'avoir conclu.

---

## Règle d'or n°143 — un outil qui ne sait pas juger doit au moins empêcher de dériver

*Née de la question : comment empêcher la règle n°139 de se défaire au lot
suivant ?*

Aucun programme ne peut décider si « on ne câble jamais sur le secteur » est
une exagération — ce n'en est pas une, c'est une règle de sécurité — ni si
« l'épaisseur ne change jamais rien » en est une. Un correcteur automatique
d'absolus produirait du bruit, on l'ignorerait, et la règle mourrait là.

**La règle.** Quand une exigence ne peut pas être vérifiée par une machine, on
n'écrit pas un juge : on écrit un **cliquet**. L'outil inventorie, un humain
justifie une fois pour toutes, et l'outil échoue dès qu'apparaît quelque chose
qui n'a pas été justifié.

`linter_absolus.mjs` relève les tournures de loi — *toujours, jamais,
systématiquement, il suffit de, tous les* — dans les réfutations et les
« à retenir » des quatre QCM. `absolus_declares.json` en contient treize, chacun
avec la raison écrite de sa présence. Le quatorzième fera échouer les tests,
et il faudra décider : est-ce une règle, ou une exagération ? C'est exactement
la question qu'on veut se voir poser.

Le champ `nuance` est volontairement hors périmètre : c'est le champ dont le
rôle est de discuter les absolus, et il en contient donc beaucoup, à dessein.

---

## Ce que fix_r.js effaçait, et qui n'est toujours pas réparé à la source

*Trouvé en ajoutant le champ `nuance` : il disparaissait des fichiers produits.*

`_outils/fix_r.js` ne permute pas les questions, il les **réécrit**, champ par
champ, à partir d'une liste fixe. Deux conséquences, l'une gênante, l'autre
visible par les élèves :

1. **tout champ inconnu de la liste disparaît** — c'est ce qui arrivait à
   `nuance` ;
2. **il écrit `err:undefined`** sur les questions dépourvues d'erreur fréquente.
   Le moteur affichait alors, dans la correction, **« Erreur fréquente :
   undefined »**.

Le second défaut était en production. Il touchait **140 questions du Thème 3** :
80 dans les quatre QCM de ce lot, et **60 dans les deux gabarits déjà fusionnés**
— `qcm_5e_C9.1-C9.3_boite_etiquetee.html` et
`qcm_3e_C9.1_variables_types_systemes.html`, qui portaient chacun `err:undefined`
trente fois. Il n'était signalé par aucun test, parce qu'un `undefined` affiché
ne lève aucune erreur JavaScript.

**Ce que ce lot fait.** Le rendu est mis derrière une garde dans les neuf QCM du
Thème 3 : plus aucun « undefined » à l'écran. Les littéraux sont retirés des
banques. Un test nouveau valide les trente questions d'un QCM et relit chaque
bloc de correction produit — c'était le seul moyen de voir le défaut.

**Ce que ce lot ne fait pas.** `_outils/` est hors du périmètre d'une branche
Thème 3 : `fix_r.js` n'est pas corrigé à la source. La chaîne de construction
répare sa sortie et le dit. Deux corrections restent à faire par Pascal, sur une
branche qui en a le droit : écrire les champs optionnels seulement s'ils
existent, et recopier les champs inconnus au lieu de les perdre.

**Et une vérification qui rassure.** Les **vingt-six** QCM des Thèmes 1 et 2
portent le même rendu sans garde. Aucun n'affiche « undefined » aujourd'hui :
toutes leurs questions possèdent une erreur fréquente, et la garde manquante y
reste donc latente. Elle se réveillerait à la première question écrite sans
`err`. La retouche est à faire, elle n'est pas urgente — et elle appartient à
une branche de Thème 1 ou 2.

---

## Règle d'or n°144 — la bonne réponse ne doit pas être la plus longue

*Née le 27 août 2026 d'une mesure que personne n'avait demandée. Pascal
venait de me transmettre le rapport de relecture original ; je l'ai lu, j'ai
traité ce qu'il disait, puis j'ai cherché ce qu'il ne disait pas.*

Le résultat était sans appel. Sur les 120 questions des quatre QCM de C7 et
C8, la bonne réponse était **107 fois la proposition la plus longue**. Un
élève qui n'ouvre aucun cours, ne lit aucune question, et coche
systématiquement la ligne la plus longue obtenait **89 %**.

Le QCM ne mesurait plus une connaissance. Il mesurait une habileté de
candidat — et il récompensait exactement l'élève qui n'avait rien appris,
tout en pénalisant celui qui lisait vraiment les quatre propositions.

**La cause est mécanique, et elle vient d'une bonne intention.** La bonne
réponse portait sa justification :

> « un rectangle : c'est un traitement, l'entrée de l'information »

Les distracteurs, eux, n'avaient rien à justifier : ils tenaient en quatre
mots. On croit écrire une réponse claire ; on écrit une réponse repérable.

**La règle.** Une proposition porte une AFFIRMATION, jamais sa
démonstration. La justification vit dans `expl`, qui est fait pour cela et
qui s'affiche de toute façon. Les quatre propositions d'une question doivent
avoir une densité comparable — sans quoi la plus dense se signale d'elle-même.

**Ce que le lot fait.** Les 120 questions sont repassées une par une : la
bonne réponse est ramenée à son affirmation, les distracteurs trop brefs
reçoivent la même densité — sans changer d'un mot ce qu'ils affirment, pour
que les réfutations `d` restent exactes. Résultat mesuré : « cocher la plus
longue » tombe de **89 % à 52 %**, et la bonne réponse n'est plus
**visiblement** la plus longue (plus de 20 % d'écart avec la deuxième) que
dans deux questions sur 120 — deux questions dont les propositions sont du
code, où l'écart est inhérent et se trouve déclaré.

**Deux contrôles nouveaux**, dans la suite de tests : aucune bonne réponse
visiblement la plus longue hors exceptions nommées, et « cocher la plus
longue » plafonné à 60 % par QCM. Ils s'ajoutent au cliquet des absolus de la
règle n°143 : même principe — la machine ne juge pas, elle empêche de dériver.

**Ce qu'il faut en retenir au-delà de ce lot.** Les 26 QCM des Thèmes 1 et 2
n'ont jamais été mesurés sur ce critère. Rien ne dit qu'ils y échappent, et
le contraire est probable : ils ont été écrits avec le même réflexe. La
mesure prend quelques secondes — `linter_absolus.mjs` montre comment lire
une banque depuis la page. C'est un chantier à ouvrir.

---

## Ce que la relecture originale m'a appris sur ma propre re-dérivation

*Le lot précédent avait été produit sans le rapport de relecture : la
conversation avait été compactée, et le fichier n'était plus dans mon
contexte. J'avais rouvert les 63 questions signalées et re-dérivé les
objections à partir du texte réel. Pascal m'a transmis le rapport ensuite.*

Le résultat de la confrontation vaut d'être noté, parce qu'il dit quelque
chose sur ce que vaut une reconstruction.

**Sur 28 rouges : 18 exactement retrouvés, 10 manqués ou traités trop court.**
Les manques ne sont pas aléatoires, et ils ont tous la même forme : j'avais
corrigé l'excès logé dans la RÉFUTATION, sans voir que la BONNE RÉPONSE
elle-même était fausse.

| Question | Ce que j'avais fait | Ce qui restait faux |
|---|---|---|
| 5e Q30 | corrigé « prouve qu'on l'a comprise » | la réponse disait « seul le capteur change » — le sens des couleurs change aussi |
| 4e C8 Q24 | ajouté une nuance sur la maîtrise | la réponse disait « rien ne change » — le montage et les conditions changent |
| 4e C8 Q8 | ajouté l'incertitude de mesure | la réponse disait encore « observé = attendu », au lieu du critère d'acceptation et de sa tolérance |
| 4e C7 Q4 | corrigé l'exemple | les trois distracteurs restaient des plaisanteries |

**La leçon.** Une reconstruction de bonne foi retrouve les erreurs de
raisonnement — celles qui se voient en relisant. Elle ne retrouve pas les
erreurs de FAIT logées dans la réponse qu'on croit juste : pour les voir, il
faut quelqu'un qui ne les a pas écrites. Le rapport valait donc bien plus que
sa liste de numéros, et il fallait le demander plutôt que de s'en passer.

---

## La règle n°144 mesurée sur les 46 QCM du dépôt

*Écrit le 27 août 2026, aussitôt après la règle elle-même. Elle était née de
quatre QCM ; il fallait savoir si elle valait pour les autres.*

Elle vaut, et davantage.

> **945 questions sur 1086 — 87 % — ont pour bonne réponse la proposition la
> plus longue. Sur 807 d'entre elles, l'écart dépasse 20 % : il se VOIT.**

Le hasard donnerait 25 %. Autrement dit, sur l'ensemble du dépôt, un élève qui
n'ouvre aucun cours et coche systématiquement la ligne la plus longue obtient
environ **87 %**.

L'outil qui le mesure est versionné : `audit_qcm_trois_themes.mjs`, avec son
CSV et l'état des lieux QCM par QCM. Il ne corrige rien et ne juge rien — il
compte ce que les règles d'or permettent de compter, et il déclare
explicitement les dix QCM d'anciennes générations qu'il ne sait pas lire :
**non mesurés**, jamais **sains**.

**Ce que la mesure dit d'encourageant.** La répartition A/B/C/D de la règle
n°137 est tenue sur 34 QCM sur 36. Aucune question incomplète sur 1086. Plus
aucun « undefined » affiché nulle part. Le fond est là — c'est justement ce
qui rend le défaut de forme coûteux : il permet de s'en passer.

**Une anomalie isolée à traiter** : `qcm_systemes_information_donnees` porte
une répartition **7/16/6/1**. Seize bonnes réponses en B, une seule en D. Ce
fichier a un moteur différent et n'est jamais passé par `fix_r.js`.

**L'ordre de bataille**, un lot par thème parce que la garde-périmètre l'impose
et parce que c'est la bonne granularité de relecture : Thème 3 (5 QCM restants,
150 questions), puis Thème 1 (11 QCM, 330), puis Thème 2 (16 QCM, 490), puis
les 10 QCM non lisibles — qu'il faudra d'abord rendre mesurables.

**Ce que la mesure ne dit pas, et qu'aucune mesure ne dira.** Rien de la
justesse pédagogique. Les 87 % disent qu'un défaut de FORME rend les QCM
devinables ; ils ne disent pas que le fond est mauvais.

---

## Règle d'or n°145 — un contre-exemple doit être vrai ET rencontrable

*Née le 27 août 2026 d'une objection de Pascal, en une phrase : « un IP38
protège mieux de l'eau qu'un IP54. Tous voulaient peut-être dire IP68. »*

J'avais écrit, pour montrer qu'on ne lit pas un indice IP comme un nombre :

> « Un IP38 protège MIEUX de l'eau qu'un IP54 — 8 contre 4 sur le second
> chiffre — alors que 38 est plus petit que 54. »

L'affirmation est **exacte**. La norme IEC 60529 autorise toutes les
combinaisons des deux chiffres, et 8 bat 4 sur la protection contre l'eau.
Elle est aussi **inutilisable** : IP38 ne se rencontre dans aucun catalogue.
Un appareil qui supporte l'immersion est en pratique scellé, donc étanche à la
poussière, donc 6 en premier chiffre. Les codes courants sont IP23, IP44,
IP54, IP65, IP67, IP68, IP69K.

Un élève qui vérifie « IP38 » ne trouve rien — et l'exemple s'effondre au
moment précis où il devait convaincre. Pire : il apprend que ce qu'on lui dit
en classe ne se retrouve pas dans le monde.

**La règle.** Un contre-exemple ne se contente pas d'être licite au regard
d'une règle : il doit exister quelque part où l'élève peut aller le voir. Un
cas seulement permis par une norme ne prouve rien à qui ne le croisera jamais.

Remplacé par **IPX8**, l'indice des montres et des téléphones étanches. Le X
n'est pas un chiffre : il dit que la poussière n'a pas été testée. Comparer
IPX8 et IP65 comme deux nombres devient alors visiblement impossible — et
l'élève a l'objet dans la poche.

---

## Règle d'or n°146 — un outil de mesure déclare ce qu'il n'a pas su lire

*Née en écrivant `audit_qcm_trois_themes.mjs`.*

L'outil lit 36 QCM sur 46. Les dix autres sont d'anciennes générations, avec
un moteur et un schéma de banque différents. Il aurait été facile — et
confortable — de les ignorer silencieusement : le rapport aurait porté sur
« les QCM du dépôt » et affiché des totaux propres.

C'est exactement le mensonge à ne pas faire. Un QCM qu'un outil ne sait pas
lire n'est pas un QCM sain : c'est un QCM **non mesuré**, et rien ne dit qu'il
échappe au défaut cherché — au contraire, son ancienneté le rend suspect.

**La règle.** Tout outil de mesure publie, à côté de son résultat, la liste
nominative de ce qu'il n'a pas su traiter. Un dénominateur qui exclut
silencieusement les cas difficiles fabrique un résultat flatteur et faux.

C'est la sœur de la règle n°136 : un dispositif s'installe quand son effet est
mesuré. Encore faut-il savoir sur quoi la mesure a porté.

---

## Règle d'or n°147 — une règle d'or naît sur un lot, elle s'adopte après mesure sur l'ensemble

*Née de l'enchaînement des 26 et 27 août.*

La règle n°144 — la bonne réponse ne doit pas être la plus longue — est née
sur quatre QCM. Elle aurait pu y rester : quatre fichiers corrigés, une règle
écrite, un lot fermé. La mesure sur les 46 QCM du dépôt a montré autre chose :
**945 questions sur 1086, soit 87 %**. La règle ne décrivait pas un accident
de rédaction, elle décrivait une habitude d'écriture — la mienne.

Une règle écrite sans mesure d'ensemble reste une anecdote élevée au rang de
principe. Une règle mesurée devient un chantier, avec son ordre de bataille et
ses chiffres avant/après.

**La règle.** Toute règle d'or nouvelle est suivie d'une mesure sur l'ensemble
du dépôt, si cette mesure est mécanisable — et l'outil qui la produit est
versionné avec elle. Ce qui n'est pas mesurable se dit tel quel.

---

## Règle d'or n°148 — le meilleur distracteur est vrai, mais hors sujet

*Née en réécrivant les 150 questions des cinq QCM restants du Thème 3.*

Le principe n°1 de la relecture d'août disait : « un distracteur doit
représenter une erreur concevable d'élève, pas une plaisanterie ». En
appliquant ce principe à 150 questions, une hiérarchie est apparue entre les
distracteurs plausibles eux-mêmes.

| Qualité | Exemple | Ce que l'élève apprend |
|---|---|---|
| plaisanterie | « pour user les boutons » | rien : il l'élimine sans savoir |
| erreur franche | « 99 : b suit toujours a » | on lui dit qu'il a tort |
| **vrai mais hors sujet** | « vérifier qu'il s'exécute sans message d'erreur » | il découvre une DISTINCTION |

Le troisième est le seul qui enseigne quelque chose à l'élève qui le choisit.
« Vérifier qu'il s'exécute sans erreur » est une vraie vérification — et elle
est insuffisante : un programme peut tourner parfaitement et compter faux.
« Le réécrire à ma façon pour mieux le comprendre » est une vraie méthode —
qui détruit le travail d'un collègue avant d'avoir compris ce qu'il faisait.
« Il y a un bug quelque part, je cherche » est une vraie réponse — celle qu'on
donne AVANT d'avoir trouvé, et qui gaspille un diagnostic déjà fait.

**La règle.** Un bon distracteur n'est pas une erreur : c'est une vérité mal
placée. Sa réfutation ne dit alors pas « c'est faux » mais « c'est vrai, et ce
n'est pas la question » — et c'est cette phrase-là qui fait comprendre.

**Conséquence pratique.** Ces distracteurs-là sont naturellement de la même
longueur que la bonne réponse, puisqu'ils portent une idée complète. La règle
n°148 sert donc aussi la n°144 : chercher des vérités hors sujet équilibre les
propositions sans y penser.

---

## Règle d'or n°149 — un outil qui réécrit prouve d'abord qu'il sait ne rien changer

*Née de deux outils : un qui perdait des données depuis des mois, et trois qui
n'en ont perdu aucune — pour une seule raison de conception.*

**Le contre-exemple.** `_outils/fix_r.js` répartit les bonnes réponses d'un QCM
sur A / B / C / D. Il ne PERMUTE pas les questions : il les **réécrit**, champ
par champ, à partir d'une liste fixe de noms connus. Deux conséquences,
invisibles dans un diff parce qu'elles ressemblent à une mise en forme :

1. **tout champ absent de sa liste disparaît.** C'est ce qui est arrivé au
   champ `nuance` : ajouté à la banque, il s'évaporait à la construction, et
   rien ne le signalait ;
2. **il écrit les champs manquants avec la valeur « indéfini ».** Le moteur
   affichait alors, à l'élève, « **Erreur fréquente : undefined** ». Cent
   quarante questions du Thème 3 étaient dans ce cas, dont soixante déjà en
   production depuis des semaines.

**Les trois outils sains.** `appliquer_corrections.py`, `patch_html.py` et
leurs dérivés font l'inverse : ils découpent, remplacent le champ demandé, et
recomposent. Avant la première écriture, chacun a été passé au **round-trip à
vide** — appliquer zéro correction, et vérifier que le fichier ressort
identique à l'octet près. Les quatre banques et les cinq QCM HTML ont tous
passé ce contrôle avant qu'une seule ligne ne soit modifiée.

**La règle.** Un outil qui modifie un fichier ne le reconstruit pas : il le
recopie et n'y touche qu'aux endroits nommés. Et avant de servir, il prouve
qu'appliquer AUCUNE modification laisse le fichier rigoureusement intact.

Le round-trip à vide coûte trois lignes. Il aurait fait tomber le défaut de
`fix_r.js` le premier jour.

---

## Règle d'or n°150 — tout chiffre d'un attendu dit d'où il vient

*Née d'une objection d'élève imaginée, puis retrouvée partout : « d'où sortent
ce 10 secondes et ce 1 centimètre ? »*

Un protocole se remplit de nombres : secouer 10 s, bouger de moins de 1 cm,
alerter au-dessus de 28 °C, ventiler à partir de 100. Ces nombres ont l'air
solides parce qu'ils sont précis. Mais un seuil que personne ne sait justifier
ne vaut pas mieux qu'une impression — il en a seulement l'apparence.

Il y a exactement **trois provenances honnêtes**, et il faut savoir dire
laquelle :

| Provenance | Exemple |
|---|---|
| un **texte** qui fait autorité | le cahier des charges de la mairie fixe 63, 118 et 178 km/h |
| une **mesure** | au-delà d'un centimètre, la sonde sort de la terre et fausse tout |
| une **décision assumée**, écrite comme telle | « nous choisissons 28 °C parce que c'est là que trois salles basculent » |

La quatrième provenance — un nombre rond dont personne ne sait rien — est la
seule à refuser. Elle se reconnaît à ce qu'aucune des trois questions ne trouve
de réponse : quel texte ? quelle mesure ? quelle décision, prise par qui ?

**La règle.** Un attendu chiffré s'accompagne de sa provenance, et l'élève
apprend à la réclamer. C'est le prolongement naturel de la règle n°129 : on ne
peut pas mesurer ce qu'on casse en changeant un seuil si l'on n'a jamais su
pourquoi il valait ça.

---

## Règle d'or n°151 — la correction est lue par ceux qui ont juste

*Née en mesurant le coût réel des erreurs trouvées dans les réfutations.*

C'est l'observation qui donne à la règle n°139 toute sa portée, et elle mérite
d'être dite séparément parce qu'elle change les priorités de relecture.

Une erreur dans une **question** est vue par ceux qui la lisent, et elle se
corrige dans la tête de l'élève au moment où il découvre la bonne réponse.
Une erreur dans la **correction** — dans une explication, une réfutation, un
« à retenir » — est lue par **toute la classe**, y compris par les élèves qui
ont répondu juste et qui n'ont, eux, aucune raison de se méfier. Elle arrive
au moment exact où l'élève a baissé sa garde : celui où on lui dit la vérité.

Une banque de 30 questions porte 30 questions et **120 phrases de correction**.
Le déséquilibre est écrasant, et l'attention le suit rarement : on relit les
questions, on parcourt les corrections.

**La règle.** Le temps de relecture se répartit à l'inverse de l'intuition :
d'abord les réfutations et les « à retenir », ensuite les questions. Et une
erreur trouvée dans une correction est traitée avec la gravité d'une erreur de
cours — parce que c'en est une.

---

## Règle d'or n°152 — deux questions voisines qui se contredisent : défaut, ou leçon, jamais hasard

*Née de deux contradictions internes trouvées le même jour, et traitées de deux
manières opposées — délibérément.*

**Le défaut.** En 4e_C8, la question 16 proposait, comme test discriminant, de
remplacer l'attache par de l'inox. La question 20 de la même banque explique
que l'inox est plus lourd et fait tomber la stabilité. Le test changeait donc
deux choses à la fois : il ne départageait rien. La banque contenait la
démonstration de sa propre erreur, à vingt questions d'écart. **Corrigé.**

**La leçon.** En 3e, la question 16 fait valider l'objet sur quatre scénarios ;
la question 17 montre que ces quatre scénarios ont laissé passer le
clignotement au seuil. La tentation était d'ajouter un cinquième scénario et de
faire disparaître la gêne. **Gardé** — et la nuance de la 16 annonce désormais
que la suivante va la contredire. « Validé » ne veut pas dire « parfait » : cela
veut dire « conforme à tout ce qui a été testé ». Cet enchaînement enseigne plus
qu'une validation propre.

**La règle.** Une banque de questions se relit comme un texte, pas comme une
liste. Quand deux questions se contredisent, il n'y a que deux issues : c'est
un défaut, et on corrige ; ou c'est une leçon, et on l'assume en l'écrivant
noir sur blanc dans la correction. Laisser la contradiction sans trancher est
la seule chose interdite — l'élève attentif la verra, et il en conclura que
personne ne relit.

**Conséquence pratique.** Aucun outil ne détecte cela. C'est le seul défaut de
cette campagne qui ait exigé de lire une banque entière d'un bout à l'autre,
et il faudra le refaire à chaque thème.

---

## Règle d'or n°153 — une branche préparée hier se rebase sur le `main` d'aujourd'hui, ou elle efface le travail d'hier

**Le fait.** La branche du Thème 1 avait été préparée sur un `main` antérieur à
la fusion du Thème 3. Fusionnée telle quelle, elle aurait **supprimé** l'outil
d'audit des 46 QCM, son CSV, l'état des lieux, et 269 lignes de ce journal.
Elle touchait par-dessus le marché des fichiers du Thème 3, que la
garde-périmètre aurait refusés.

**Ce qui trompe.** L'intuition dit qu'une branche ancienne « n'a pas » les
changements récents. C'est faux : au moment de la fusion, elle les **défait**.
Un fichier qu'elle ne connaît pas est un fichier qu'elle propose de supprimer.

**La règle.** Le diff d'une branche ne se lit jamais contre l'état où on l'a
créée, mais contre l'état où elle va atterrir. `git diff --stat origin/main
<branche>` avant chaque livraison, et une lecture simple : **des suppressions
dans des fichiers qu'on n'a pas touchés = base périmée, on refait la branche.**

**Ce que ça dit de la garde-périmètre.** Elle aurait arrêté celle-ci — par
accident, parce que la branche débordait aussi de son thème. Une branche
périmée qui reste dans son périmètre passerait sans bruit. Le contrôle
appartient à celui qui prépare, pas au filet.

---

## Règle d'or n°154 — un indicateur qui crie pour un caractère apprend à ne plus l'écouter

**Le fait.** L'indicateur « bonne réponse visiblement la plus longue » se
déclenchait dès +20 %. Sur une question dont les propositions sont `int`,
`str`, `float`, `bool`, il signalait un défaut : `float` (5 lettres) dépasse
`bool` (4) de 25 %. Rien ne se voit à l'œil. Rien ne se voyait non plus dans
`Un dessin` contre `Une carte`.

**La règle.** Un seuil relatif seul est faux aux petites valeurs. Il faut un
écart **relatif** (+20 %) ET un écart **absolu** (au moins 8 caractères). Les
deux outils de mesure ont été corrigés ensemble ; les chiffres des lots
précédents n'ont pas bougé, ce qui confirme que le plancher ne cachait rien de
réel — il ne supprime que du bruit.

**Pourquoi ça compte plus qu'il n'y paraît.** Un indicateur qui signale du
bruit se fait ignorer, puis désactiver, puis oublier. Le jour où il a raison,
plus personne ne le regarde. Le régler n'est pas du confort : c'est ce qui le
garde utilisable.

---

## Règle d'or n°155 — compléter une banque par une boucle, c'est mentir sur le dénominateur

**Le fait.** `qcm_automatisation_premium.html` annonçait « 40 questions
uniques ». Il en contenait onze. Une boucle
`while(questions.length < 40) questions.push({…})` répétait la **même**
question — même énoncé, même bonne réponse — vingt-neuf fois, et la note était
calculée sur 40.

**Ce que vivait l'élève.** Onze questions, puis la même vingt-neuf fois. Et une
note où 29 points sur 40 s'obtenaient en répondant une fois juste, puis en
recopiant. Le score ne mesurait plus rien — ni la connaissance, ni même
l'attention.

**La règle.** Le dénominateur d'une note dit ce qui a été demandé. Il se lit sur
la banque (`questions.length`), jamais sur un nombre écrit à la main, et
surtout jamais sur un nombre atteint par duplication. Un QCM porte le nombre de
questions qu'il a réellement ; s'il en faut davantage, on les **écrit**.

**Ce qui a été fait.** La boucle est retirée, la onzième question réintégrée
comme une entrée normale, et les trois dénominateurs figés (`/40`) remplacés
par `questions.length`. Le QCM annonce désormais onze questions et note sur
onze. Les vingt-neuf qui manquent restent à écrire : c'est un travail
d'auteur, pas de correcteur, et il n'a pas été fait à la sauvette.

**Le rapport avec la n°146.** Un outil déclare ce qu'il n'a pas su lire ; un
QCM déclare ce qu'il n'a pas. Dans les deux cas, le mensonge n'est pas dans le
chiffre affiché, il est dans le silence sur ce qui manque.

---

# Deux audits externes, vérifiés puis appliqués — six règles et deux clefs de voûte

*À coller à la suite du `JOURNAL_DES_DECISIONS.md`.*

Deux audits du Thème 1 (C1 à C3) ont été remis le même jour, produits par deux systèmes
différents à partir du même prompt maître. Ils sont l'un et l'autre sérieux, documentés,
hiérarchisés. Ils ne disent pas la même chose, et **aucun des deux n'a été appliqué tel quel** :
chaque affirmation vérifiable a d'abord été confrontée aux fichiers.

C'est de cette confrontation que sortent les règles ci-dessous.

---

## 1. Ce que la vérification a donné

| Affirmation | Auteur | Verdict | Preuve |
|---|---|---|---|
| `4e_C1.4` : la barre affiche `/65` alors que les blocs totalisent 69 | ChatGPT | **CONFIRMÉ** | `W = {14,8,11,11,10,15}` → 69 ; pastille figée à `/65` |
| `3e_C1.5` : le titre annonce une séquence de 5ᵉ | les deux | **CONFIRMÉ** | `<title>Séquence 5ᵉ …</title>` dans une page 3ᵉ |
| `5e_C1.3` : « six fichiers » annoncés, jamais fournis | ChatGPT | **CONFIRMÉ** | consigne « indiqués par le professeur », aucun fichier dans le lot ni en lien |
| `5e_C3` : la masse « explique » la distance de freinage | ChatGPT | **CONFIRMÉ, et pire que dit** | la phrase est dans **cinq** fichiers, dont le QCM et la matrice de couverture |
| `4e_C1.4` : « l'humain est le maillon faible » | ChatGPT | **CONFIRMÉ** | deux occurrences, dont une question posée aux élèves |
| `3e_C1.5` : `.slice()` donné comme exemple Python | ChatGPT | **RÉFUTÉ** | zéro occurrence dans le lot |
| `5e_C2` : « quatre familles » puis « trois natures » d'interacteurs | ChatGPT | **RÉFUTÉ** | dix occurrences de « quatre familles », aucune de « natures » |
| `4e_C1.4` : « changer de mot de passe tous les 3 mois », « 15 ans », « cadenas = confiance » | ChatGPT | **NON TROUVÉ** | aucune de ces formulations dans le fichier |
| `3e_C3` : additivité des baisses de température non signalée | ChatGPT | **DÉJÀ TRAITÉ** | la correction dit déjà « les effets ne se cumulent pas parfaitement » |

Soit, sur neuf affirmations vérifiables : **cinq confirmées, deux réfutées, une introuvable, une
déjà corrigée**. Un audit sur trois portait à faux.

Cela ne disqualifie ni l'un ni l'autre : les cinq confirmées valaient largement la lecture, et la
quatrième — la masse — est le défaut le plus grave trouvé sur le dépôt depuis le début de l'année.
Mais cela règle une question de méthode.

---

## CLEF DE VOÛTE — un audit est une production, pas un verdict

Un audit arrive avec tous les signes de l'autorité : structure, priorités P0 à P3, références au
BO, tableaux à onze colonnes. Rien dans sa forme ne distingue l'affirmation vérifiée de
l'affirmation plausible. Et une affirmation plausible et fausse, appliquée telle quelle, **remplace
un défaut par un autre** — avec, cette fois, la bonne conscience d'avoir suivi une recommandation.

Un audit se lit donc comme on lit une mesure : en demandant d'où elle sort. Trois classes, et
trois traitements :

| Ce que l'audit avance | Traitement |
|---|---|
| un fait **vérifiable dans les fichiers** (un compteur, un titre, une phrase) | on vérifie, puis on corrige — jamais l'inverse |
| un fait **du monde** (un chiffre ADEME, une recommandation CNIL) | on remonte à la source, on la date, on la fige |
| un **jugement pédagogique** (« trop dense », « objet trop lointain ») | il ne se vérifie pas : il se discute, et il se décide |

Le troisième cas est le plus intéressant, parce qu'il n'a pas de valeur de vérité et garde toute sa
valeur d'alerte. Les deux audits disent, chacun à sa façon, que le geste technique manque. Aucune
mesure ne peut trancher cela. C'est un jugement — et il se trouve qu'il est juste.

---

## CLEF DE VOÛTE — une erreur ne vit pas dans un fichier, elle vit dans un lot

L'audit signalait une phrase dans une séquence. Elle était dans **cinq fichiers** :

| Fichier | Ce qu'il en faisait |
|---|---|
| la séquence | « La masse explique l'ordre des distances… un bon signe qu'on tient quelque chose de solide » |
| la synthèse élève | « La masse explique la distance de freinage comme elle expliquait la consommation » |
| la synthèse professeur | « séance 3 — elle explique la distance de freinage » |
| la fiche pédagogique | idem, dans les intentions du lot |
| **le QCM** | une question entière, dont la bonne réponse était « la masse lancée », et dont la réfutation écartait l'hypothèse « des freins de mauvaise qualité » par « l'écart suit exactement les masses » |
| **la matrice de couverture** | l'énoncé figurait comme **objectif d'apprentissage couvert** |

Corriger la seule séquence aurait laissé le QCM enseigner l'erreur, la synthèse la répéter, et la
matrice attester qu'elle était acquise.

**La règle :** une correction de fond se cherche par `grep` dans tout le lot avant d'être écrite
quelque part. Un lot est un organisme ; une idée fausse y circule. Et le dernier endroit où l'on
pense à regarder — la matrice de couverture — est précisément celui qui transforme l'erreur en
compétence validée.

---

## Règle d'or n°167 — vérifier avant de corriger, y compris quand l'auditeur a raison neuf fois sur dix

Une recommandation appliquée sans vérification n'est pas une correction : c'est un pari. Deux des
neuf points vérifiables de l'audit le plus détaillé ne correspondaient à rien dans les fichiers.
S'ils avaient été « corrigés », on aurait réécrit du texte juste, et le diff aurait porté la
mention rassurante « suite à l'audit ».

Le coût de la vérification est dérisoire : `grep`, dix secondes. Le coût de son absence est une
régression silencieuse, justifiée par une autorité extérieure.

---

## Règle d'or n°168 — une corrélation présentée comme une explication est l'erreur la plus coûteuse qu'un cours puisse contenir

Le lot 5e_C3 faisait tout bien : protocole fourni, charge identique, revêtement identique, vitesse
identique, trois essais et une moyenne, et cette phrase excellente — « sans cela, on ne compare
plus des véhicules, on compare des essais ».

Puis, à la synthèse, il attribuait l'ordre des distances de freinage à la masse — alors que les
trois véhicules diffèrent aussi par leurs freins, leurs pneus et leur empattement. Et il ajoutait :
« un bon signe qu'on tient quelque chose de solide ».

C'est le pire des deux mondes : la démarche rigoureuse **installe la confiance**, et la conclusion
hâtive **en profite**. L'élève n'apprend pas seulement un fait faux ; il apprend une **méthode**
fausse — que deux colonnes qui varient ensemble se valident l'une l'autre.

**La règle.** Dans tout lot où l'on fait mesurer, la question « qu'est-ce qui varie encore, à part
ce que je crois observer ? » doit être posée **dans le lot lui-même**, pas seulement dans la tête
de l'auteur. Une leçon sur le contrôle des variables qui se termine par une conclusion non
contrôlée détruit ce qu'elle vient de construire.

*(La question du QCM a été réécrite : sa bonne réponse est désormais « les deux colonnes varient
dans le même sens », et sa nuance répond à l'objection de l'élève qui sait, par ailleurs, qu'un
camion s'arrête moins vite.)*

---

## Règle d'or n°169 — une activité qui repose sur un fichier absent n'est pas une activité

L'activité 2 du lot 5e_C1.3 demandait de renommer et ranger « les six fichiers indiqués par le
professeur ». Ces six fichiers n'existaient nulle part. La séquence était donc, sur ce point, une
**intention**, pas une ressource : chaque enseignant devait les inventer, et chaque classe aurait
travaillé sur un jeu différent.

Le défaut est invisible à la lecture — la consigne est claire, la correction est écrite, l'aide
graduée est là. Il n'apparaît qu'au moment où quelqu'un essaie de faire l'activité. C'est encore
la clef de voûte des séquences : le manque ne produit aucun signal.

**La règle.** Toute consigne qui désigne une ressource — un fichier, un objet, un jeu de données,
une photo — la **fournit** ou dit explicitement où la prendre. Un lot se vérifie en suivant ses
propres consignes, une par une, comme un élève les suivrait.

*(Le paquet est créé : six fichiers volontairement mal nommés, deux pièges assumés — une case vide
qui n'est pas un zéro, deux extractions de dates différentes — et une fiche de correction. Plus
une variante papier pour le jour où la salle informatique tombe.)*

---

## Règle d'or n°170 — un dénominateur figé finit toujours par mentir

`4e_C1.4` affichait `0/65`. Les six blocs pèsent 14 + 8 + 11 + 11 + 10 + 15 = **69**. Un élève
parfait obtenait 69/65.

C'est la règle n°155 — compléter une banque par une boucle, c'est mentir sur le dénominateur —
rencontrée par l'autre bout : ici, rien n'a été gonflé ; c'est le total qui a été **recopié à la
main**, puis les poids ont bougé.

**La règle, dans sa forme générale :** un total ne se recopie jamais. Il se **calcule** à partir de
ce qu'il totalise, et il s'affiche depuis ce calcul. Tout nombre écrit deux fois dans un fichier
finira par exister en deux versions.

*(Corrigé : la pastille lit désormais `scoreMax`, alimenté par la somme des poids. Au passage, un
`FIXME` signalait depuis longtemps un élément `scoreTotal2` inexistant — il a été retiré.)*

---

## Règle d'or n°171 — on n'enseigne pas à un élève qu'il est le maillon faible

Le lot cybersécurité disait à l'élève qu'en adoptant de bonnes habitudes, il éviterait « de devenir
le maillon faible ». Et il lui demandait : « Pourquoi dit-on que les humains sont le maillon
faible ? »

La formule est répandue chez les professionnels. Adressée à un élève de 4ᵉ, elle enseigne trois
choses fausses ou nuisibles : que la sécurité est d'abord une affaire de mérite individuel ; que
celui qui se fait piéger a failli ; et donc qu'il vaut mieux ne rien dire. Or ce qui protège
réellement un adolescent, c'est de **signaler vite**, sans honte.

**La règle.** Aucune formulation ne doit désigner l'élève comme la cause du risque. On décrit ce
que l'attaque exploite, jamais ce que la victime aurait dû être. La question est devenue :
« Pourquoi les attaques visent-elles d'abord les personnes, plutôt que les machines ? » — même
contenu technique, et l'élève n'est plus l'accusé.

*(La même passe a nuancé le VPN : « masque ton IP et chiffre ta connexion » est devenu « chiffre ta
connexion jusqu'à son fournisseur, à qui tu accordes alors ta confiance ». Et `3e_C1.5` ne dit plus
« HTTPS (sécurisé), HTTP (non sécurisé) » mais « échange chiffré / échange en clair » : HTTPS
protège le transport, il ne certifie pas le destinataire.)*

---

## Règle d'or n°172 — deux audits qui divergent désignent la frontière entre le vérifiable et le discutable

Les deux audits ont lu le même corpus avec le même prompt. Là où ils portent sur des faits, ils
**convergent** — les deux ont vu le titre « 5ᵉ », les deux ont vu les deux lots hors gabarit. Là où
ils portent sur des jugements, ils **divergent**, et proprement :

| Question | Audit A | Audit B |
|---|---|---|
| Ce qui manque le plus | la manipulation d'objets réels et la mesure | le geste technique **et** l'ancrage territorial martiniquais |
| Le contexte chinois | non discuté | « puissant intellectuellement, mais lointain » — à faire précéder de trois minutes d'objet local |
| Le matériel | « aucun équipement spécialisé garanti » | « l'atelier a Grove, Arduino, imprimante 3D : le Thème 1 ne s'en sert pas » |

La divergence n'est pas un désaccord sur les faits : elle vient de ce que chacun a supposé de la
salle. L'un a posé « aucun équipement garanti », l'autre « Grove et Arduino disponibles ». Les deux
conclusions sont justes **sous leur hypothèse**.

**La règle.** Quand deux lectures divergent, on cherche d'abord l'hypothèse qui les sépare, avant
de chercher qui a raison. Et l'on en tire la conséquence pratique : un lot doit dire de quel
matériel il a besoin, et prévoir le chemin sans ce matériel — nos parcours A réel / B simulé /
C sans matériel existent pour cela, et le Thème 1 ne les tient pas partout.

---

## Ce qui a été corrigé, et ce qui ne l'a pas été

**Corrigé** (branche `fable/theme-1/corrections-audits-externes`) : les cinq points confirmés, dans
les onze fichiers concernés.

**Non corrigé, et assumé :** les deux audits demandent d'ajouter un geste technique réel à chaque
lot, d'ouvrir sur un objet local, et de recaler deux lots hors gabarit. Ce sont des **jugements
pédagogiques**, ils portent sur le fond, et ils engagent des heures de classe. Ils appartiennent à
l'enseignant, pas à l'auditeur — et pas davantage à moi.

Ils rejoignent exactement ce que la mesure des 41 séquences avait montré de son côté : 18 séquences
sans un seul visuel, un « mode essentiel » qui allège de 9 %, et un budget de lecture qui dépasse
le tiers de la séance. Deux audits externes et une mesure interne, partis de trois endroits
différents, désignent le même manque.

---

## Règle d'or n°173 — un défaut trouvé une fois se cherche partout, tout de suite

Les cinq points confirmés par les audits externes ont tous une **forme**. Une fois la forme
connue, elle se cherche par script sur l'ensemble du dépôt — c'est vingt minutes, et c'est le seul
moment où on le fera.

Ce balayage, mené juste après les corrections, a trouvé quatre défauts que **ni l'un ni l'autre
des deux audits n'avait vus** :

| Trouvé par balayage | Forme cherchée | Gravité |
|---|---|---|
| **Le bouton « QCM » de la séquence 5e Chengdu ne mène nulle part** — il pointe vers `qcm_5e_C1_chengdu_air.html`, renommé depuis en `qcm_5e_C1.1-C1.6_chengdu.html` | lien relatif dont la cible n'existe pas | l'élève ne peut pas atteindre le QCM de la séquence phare du niveau |
| **Le bouton « Enregistrer » de la séquence cybersécurité n'existe pas** — le code le cherchait, un `FIXME` le disait, personne ne l'avait lu | élément commandé par le script mais absent du HTML | plus de cent champs à remplir sur trois séances, et rien ne se garde |
| `activite_crcn_donnees_freinage_5e_C1.2` pointait vers la séquence d'avant la réécriture Sainte-Luce, et vers un jeu de données resté dans l'archive | liens survivant à un renommage | activité injouable |
| Le programme Python de `3e_C1.5` affichait « Connexion sécurisée » dès qu'une URL commence par `https://` | la confusion HTTPS / fiabilité, cherchée partout | enseigne exactement ce que la séquence corrige par ailleurs |

**Le lien mort de Chengdu mérite qu'on s'y arrête.** Il date d'un renommage de fichier. Aucun
test ne l'a vu, aucune relecture non plus — parce qu'on relit le contenu d'une page, pas ses
liens. Il a fallu six lignes de script pour le trouver, et il n'y a **plus aucun lien mort** dans
le Thème 1.

**La règle.** Quand un défaut est confirmé, on ne corrige pas l'occurrence : on écrit la requête
qui trouve toutes ses sœurs, et on la garde. Corriger un cas signalé, c'est traiter le symptôme
que quelqu'un a eu la chance de voir.

**Le contrôle a été écrit, et il a immédiatement rendu deux défauts de plus dans la même
séquence :**

- l'activité 5.b lisait `q5b` ; la zone de saisie s'appelle `q5b-response`. Quoi que l'élève
  écrive, on lui répondait que sa réponse était trop courte. Le seul élève épargné était celui qui
  n'écrivait rien ;
- la barre de progression cherchait un élément `prog` qui n'a jamais existé. La séquence affichait
  une barre — vide, et immobile du début à la fin.

Trois boutons ou repères commandés par le code et absents de la page, dans un seul fichier. Aucun
ne produit d'erreur JavaScript : le code est prudent, il teste avant d'agir. **La prudence du code
a rendu le défaut silencieux** — et c'est encore la clef de voûte : ce qui ne produit aucun signal
se lit comme une réussite.

*(Les deux vérifications sont désormais **versionnées** : `verificateur_lots.mjs`, à côté de
l'audit des QCM. Elles ont trouvé, dès leur première exécution, tout ce que ce lot corrige — et
rien d'autre : le dépôt vivant est à zéro lien mort.)*

**Une décision de conception mérite d'être notée.** Le second contrôle signalait `parcoursNote`
dans deux séquences du Thème 3. Vérification faite, l'absence y est **voulue** : le moteur des
parcours 🅰/🅱/🅲 est partagé par les quatre pages d'une station, et ces deux-là n'ont aucun bloc
propre à un parcours — elles l'écrivent à l'élève. On aurait pu apprendre à l'outil à tolérer les
recherches gardées par un `if`. C'eût été une erreur : le bouton « Enregistrer » était gardé lui
aussi, et c'était un vrai défaut. Ce qui les sépare n'est pas la forme du code, c'est l'INTENTION —
qu'aucun outil ne lit.

Les exceptions sont donc **déclarées**, dans `elements_optionnels.json`, sur le modèle de
l'inventaire des absolus : chacune porte sa raison et la réponse à une question unique — *qu'est-ce
que l'élève perd si cet élément n'existe pas ?* Si la réponse est « rien », c'est une exception ; si
elle est « quelque chose », c'est un défaut, et sa place n'est pas dans l'inventaire.

---

## 2026-08-28 — On renonce à dessiner les mécanismes, et on encadre la vidéo

Pascal a tranché, et il a raison : **pour un mécanisme, un schéma que j'écris en code ne remplace
pas le réel.** Un frein à tambour se comprend en le voyant tourner, pas en lisant un dessin. Le
prompt maître des images reste bon pour ce qui est *comparaison* — trois roues au même diamètre
n'existent dans aucune vidéo — mais pour le *fonctionnement*, on passe à la vidéo.

**Ce que ce choix coûte, et qu'il faut payer plutôt que masquer.** Une vidéo ne vit pas dans le
dépôt. Quatre risques, tous réels en collège :

| | |
|---|---|
| le filtre réseau | YouTube est bloqué sur beaucoup de réseaux d'établissement |
| le RGPD | une vidéo intégrée dépose des traceurs sur des mineurs ; `youtube-nocookie` n'est pas le laissez-passer qu'on croit |
| la pourriture des liens | une vidéo supprimée dans dix-huit mois, c'est une séance morte |
| la publicité et les suggestions | un élève de treize ans envoyé sur YouTube arrive avec les recommandations |

Trois des quatre se règlent avec **Digiview** (La Digitale) : segment découpé, ni publicité, ni
suggestions, ni pistage, lien stable. Le quatrième se règle en changeant de source : **Lumni
Enseignement**, gratuit, français, droits déjà réglés pour la classe.

**Le reste se règle par un outil, parce qu'une règle qu'aucun outil n'applique revient toujours.**
`ressources_externes.json` tient le registre ; `poser_ressource.py` pose le bloc et **refuse** une
ressource sans URL, sans consigne minutée ou sans repli imprimé ;
`verificateur_ressources.mjs` vérifie que le lien répond, que la vidéo existe encore, que le bloc
est toujours dans sa page.

### Une limite que je dois écrire noir sur blanc

**Je ne peux vérifier aucune URL de vidéo depuis le conteneur où je travaille** : YouTube répond
429, Wikimedia Commons est en cache seul, Lumni répond 403, et même `example.com` est refusé par
le mandataire. Le contrôle des liens externes ne peut donc s'exécuter que **depuis la machine de
Pascal**. C'est la raison d'être de `verificateur_ressources.mjs`, et la raison pour laquelle le
registre est livré **sans une seule URL** : six emplacements, chacun avec sa spécification et son
repli déjà écrits, et le champ `url` vide.

Ce n'est pas de la prudence de façade. Le jour même, une liste de douze « animations libres de
droits » nous est arrivée, parfaitement présentée — sections, licences annoncées, sources entre
parenthèses. **Les six fichiers Wikimedia annoncés n'existent pas.** Deux fichiers réels existent
bien (`File:Bicycle brakes - animated.gif` et sa variante), mais aucun de ceux qui étaient cités.
La forme d'une liste bien tenue n'est pas une preuve : c'est du rendu.

### Les règles

- **n°179** — une ressource qui vit hors du dépôt porte toujours son repli imprimé. Sans lui,
  ce n'est pas une ressource, c'est un pari sur le réseau.
- **n°180** — un lien externe porte la date de sa dernière vérification, et cette date s'affiche
  dans la page. Un lien sans date se croit éternel.
- **n°181** — ce que je ne peux pas vérifier moi-même, je ne le livre pas rempli : je livre
  l'emplacement, la spécification et le contrôle qui le vérifiera ailleurs.
- **n°182** — on ne code pas ce qui se filme, et on ne filme pas ce qui se compare. La vidéo
  montre un fonctionnement ; le schéma met des solutions côte à côte. Chacun sur ce qu'il sait
  faire.

---

## 2026-08-28 (suite) — Deux chiffres de l'état des lieux étaient faux, et pour la même raison

L'état des lieux du Thème 1 annonçait **« rôles de groupe : 15 séquences sur 15 »** et
**« bilan personnel : 6 sur 15 »**. Les deux sont à corriger, et l'erreur est la même dans les
deux cas : **j'avais compté une convention de nommage, pas une chose.**

| Annoncé | Réel | Ce que je comptais |
|---|---|---|
| bilan personnel manquant : **6 sur 15** | **1 sur 15** — `5e_C1.3` | l'emoji 🪞 |
| rôles à poser : **15 sur 15** | **5 sur 15** | le mot « à deux », n'importe où dans la page |

Trois séquences portent le dispositif complet de bilan — rappel de l'hypothèse, `bilan1`,
`bilan2`, versions étayées — sous un titre « 🏁 Bilan » ou « 🧩 Bilan ». Une quatrième l'a sous
« 🧠 Synthèse et métacognition », une cinquième sous « 🧠 Métacognition » avec `meta1` à `meta3`.
Aucune n'écrit 🪞. Mon indicateur ne mesurait pas la présence du bilan : il mesurait la
**conformité au gabarit le plus récent**.

Même mécanique pour les rôles. La première version de `poser_roles.py` cherchait « à deux » ou
« en groupe » n'importe où et remontait au titre précédent. Le bloc atterrissait sous « 📚 Le
référentiel de la séquence » et sous « 🎫 Billet d'entrée » — des sections qui **citent** le
travail de groupe sans en être un. Il fallait deux conditions, pas une : un titre qui annonce
une **activité**, et du vocabulaire de groupe **dans cette activité-là**.

### Ce que ça change, au-delà des deux chiffres

Une fois l'outil rendu exigeant, **deux lots refusent la pose faute d'avoir la moindre section
« Activité » : `4e_C1.4` et `3e_C1.5`.** Ce sont les deux lots héritage. C'est le **cinquième
indicateur indépendant** à les désigner, après le budget de lecture, le nombre d'aides repliées,
le mode essentiel et les QCM sans réfutation. Aucun de ces cinq n'a été construit pour les
trouver.

### Les règles

- **n°184** — un indicateur bâti sur une convention de nommage mesure la conformité à la
  convention, jamais la présence de la chose. Quand la maison a changé de gabarit en cours de
  route, il compte les lots récents et déclare les anciens vides. *(Précision de la n°146 : ici
  ce n'est pas le mot qui manque, c'est le mot qui a changé.)*
- **n°185** — chercher un mot, ce n'est pas trouver une situation. « À deux » dans un référentiel
  décrit une compétence ; « à deux » dans une activité décrit ce que font deux élèves à cet
  instant. Un outil qui ne distingue pas les deux pose ses dispositifs au mauvais endroit — et
  un dispositif au mauvais endroit apprend à ne plus lire les dispositifs.
- **n°186** — on ne pose pas un dispositif là où il ne sert pas. Dix séquences du Thème 1 se font
  seul : leur ajouter des rôles de groupe aurait fait du bruit, et le bruit se paie sur tous les
  autres blocs de la page.
- **n°187** — une note qui compte quelque chose se calcule. « Les trois zones de réponse sont
  enregistrées » est devenue fausse en ajoutant un bilan ; elle compte désormais les zones
  elle-même.

---

## 2026-08-28 (fin) — Pascal soupçonnait des fusions manquées. Il en manquait, mais pas là où on regardait

Question posée : « j'ai l'impression que j'ai gratté quelques fusions ». Vérification faite,
d'abord par la mauvaise méthode, puis par la bonne.

**La mauvaise méthode** — comparer les SHA (`git log main..branche`) désignait trois branches du
Thème 1 comme non fusionnées. C'est faux : leurs commits ont été *cherry-pickés* dans
`lots-heritage`, et un cherry-pick fabrique un nouveau SHA. Une branche reprise par cherry-pick
paraîtra non fusionnée pour toujours. Le SHA mesure le chemin, pas le contenu.

**La bonne méthode** — vérifier que **l'artefact est là**. Sur `origin/main`, à ce jour :

| Ce qu'on cherche | Attendu | Trouvé |
|---|---|---|
| Outils de la méthode (`verificateur_lots`, `generer_lexique`, `poser_ressource`, `poser_roles`, `verificateur_ressources`, `elements_optionnels`, `ressources_externes`) | 7 | **7** |
| Lexiques du Thème 1 | 13 | **13** |
| QCM du Thème 1 au gabarit (30 questions, 30 blocs `d:[]`) | 13 | **13** |
| Blocs de rôles de groupe posés | 5 | **5** |
| Séquences portant un bloc ressource externe | 3 | **3** |
| Séquences du Thème 1 avec navigation de retour | 15 | **15** |

Rien de ce qui a été livré ces derniers jours ne manque. Les 21 branches encore non fusionnées
datent toutes de juillet ou du 1ᵉʳ août, et pour deux d'entre elles — `atelier-trois-pages`,
`lot-02-4e-C8-validation-jardin` — **le contenu est bien sur `main`**, arrivé par une autre PR.

### Ce qui manquait vraiment

**1. Une branche jamais fusionnée, devenue inapplicable.**
`fable/theme-1/vague-3-conformite-socle` (1ᵉʳ août) portait la navigation de retour, la
suppression des boîtes modales et un « contrat de séquence ». La navigation est arrivée depuis
par un autre chemin ; le contrat n'est nulle part ; et **quatre des huit fichiers qu'elle
modifiait ont été renommés depuis**. La reprendre telle quelle est impossible. On en reprend donc
l'intention, pas le patch : les trois `alert()` de `4e_C1.4` partent aujourd'hui.

Test réel, avant et après, sur la page ouverte dans un navigateur :

| | boîtes modales ouvertes | erreurs JS | panneaux de séance |
|---|---|---|---|
| avant | **1** (à la première saisie) | 0 | 4 |
| après | **0** | 0 | 4 |

La modale n'était pas seulement inélégante : l'enregistrement de cette page se déclenche **aussi
tout seul à chaque frappe**. Une modale qui s'ouvre en pleine phrase coûte la phrase.

**2. Onze règles d'or citées mais jamais écrites.**
Le journal cite les numéros jusqu'à n°187. En les comptant un par un, **dix-huit numéros n'ont de
texte nulle part dans le dépôt : n°17, n°19, n°156 à n°165, n°174 à n°178 et n°183** — annoncés en
séance de travail, jamais déposés. Deux autres, n°15 et n°16, ne vivent que dans des pages du
Thème 3 et dans `_outils/METHODE.md` ; la n°166 n'existe que dans un commentaire de
`poser_roles.py`. Une règle qui n'existe que dans une conversation ne protège rien : le lendemain,
personne ne peut la citer. Les six que je peux restituer mot pour mot sont rétablies ci-dessous.
Les autres restent un trou **déclaré** : je ne les invente pas.

### Les règles rétablies

- **n°174** — une animation ne se justifie que si son sujet **change dans le temps**. Un schéma
  qui ne bouge pas se lit mieux fixe.
- **n°175** — une animation qui tourne toute seule est un spectacle. Celle que l'élève déclenche
  est un instrument.
- **n°176** — l'état final d'une animation doit être **l'image complète**. Un élève qui arrive en
  retard, ou qui imprime, doit voir la même chose que les autres.
- **n°177** — une animation qui montre la réponse **remplace le travail** au lieu de le préparer.
- **n°178** — rien d'essentiel ne repose sur le mouvement seul : ni la consigne, ni la donnée, ni
  la correction.
- **n°183** — un aperçu ne fabrique pas de faux contrôle. Un bouton qui ne mène nulle part apprend
  à ne plus cliquer sur les boutons.

**Clef de voûte des six** : *le mouvement n'est pas une information, c'est une dépense
d'attention. On ne la fait payer à l'élève que pour ce qui change dans le temps.*

### Les règles nouvelles

- **n°188** — une page d'élève ne s'arrête pas pour parler. Pas de boîte modale : un message
  d'état dans la page, annoncé aux lecteurs d'écran, qui n'attrape pas le focus et s'efface seul.
  Sur une page qui enregistre à chaque frappe, une modale coûte une phrase à celui qui écrit.
- **n°189** — une règle qui n'est pas écrite dans le dépôt n'existe pas. Le journal est la seule
  preuve ; ce qui est resté dans la conversation est perdu à la session suivante. *(Corollaire
  opératoire : la numérotation se vérifie — un trou dans la suite est une règle tombée, pas un
  numéro sauté.)*

---

## 2026-08-28 — Trois audits du Thème 2, vérifiés affirmation par affirmation

Pascal a déposé trois audits externes de C4–C6 : une matrice de remplacements (25 défauts,
24 activités rédigées), un audit ChatGPT et un audit Grok. Trois documents sérieux, longs,
ancrés sur des noms de fichiers. La tentation était d'ouvrir un chantier de 25 correctifs.

**Un audit est une production, pas un verdict.** Chaque affirmation vérifiable a donc été
transformée en mesure sur le dépôt avant d'être retenue. Sur **24 affirmations vérifiables :
17 exactes, 4 fausses, 3 exactes sur le fond et fausses sur le chiffre.**

Lecture complète : `theme-2-…/_gouvernance/LECTURE_DES_TROIS_AUDITS_C4-C6.md`.

### La plus grave était fausse

ChatGPT annonçait une erreur technique dans du matériel élève : dans SOS serre,
`192.168.20.1` serait posée en passerelle par défaut sans routeur pour la porter. Il proposait
trois correctifs, dont « laisser la passerelle vide et expliquer » et « préciser que le `.1`
est une convention ». **La page fait déjà les deux**, en toutes lettres — « la passerelle est
prévue au plan mais non installée dans notre montage d'entraînement », « le `.1` n'est pas une
loi d'Internet, c'est le choix du gestionnaire ». L'objection avait été anticipée et traitée
avant d'être formulée. Appliquer le correctif aurait **retiré** l'explication qui répondait à
l'objection.

### « Le corpus déborde » : deux lots sur douze

Les trois audits s'accordent sur le débordement horaire. Mesuré en lisant tous les marqueurs
`⏱` des 17 séquences : **deux séquences sur douze sont sans marge** (`3e_C4.1–C4.2` à
115 min pour 110 ; `4e_C6.1–C6.3` à 110 pour 110 — les deux chiffres annoncés par ChatGPT sont
exacts au chiffre près). **Les dix autres ont entre 5 et 40 minutes de marge.**

Le vrai décalage est ailleurs, et les trois l'ont manqué : douze séquences écrivent « séances
de **55 min** », le créneau réel est de **90**. Une page qui tient dans 2 × 55 tient à l'aise
dans 2 × 90. Le problème n'est pas qu'elle déborde, c'est qu'elle annonce un **nombre de
séances** qui ne se pose pas sur les semaines. Bon remède (le calage Pronote), mauvais
diagnostic.

Et **cinq séquences n'annoncent aucune durée du tout**. Les trois audits ont calculé ces
pages activité par activité ; aucun n'a vu que l'enseignant qui les ouvre n'a aucun chiffre
sous les yeux. Chercher un défaut empêche de voir une absence.

### Le statut cesse d'être une déclaration

Les trois disent « la gouvernance de validation est trop généreuse ». Aucun ne dit de combien,
parce qu'aucun ne comptait. `build_audit.py` déclarait « COMPLET ET VALIDABLE » code par code,
à la main, dans son OVERLAY — et une déclaration ne se trompe jamais : elle se contente d'être
fausse en silence.

`_outils/controle_statut.py` mesure désormais, pour chaque code qui revendique ce statut, la
présence effective des six pièces que le label implique : séquence, QCM **portant une vraie
banque de questions**, fiche, matrice, synthèses, rapport de tests. Le contrôle ne promeut
rien ; il refuse une revendication non tenue.

Sur 31 codes qui le revendiquaient, **27 tiennent**. Quatre sont recalés :

| Code | Manque | Devient |
|---|---|---|
| `4e_C4.1` jardin connecté | fiche pédagogique | À vérifier |
| `4e_C4.2` Book Train | dossier vide | Mutualisé (ce qu'il est) |
| `4e_C4.4` Book Train | dossier vide | Mutualisé |
| `4e_C6.2` arrosage automatique | fiche, matrice, synthèses | À vérifier |

Deux dossiers **vides** portaient l'étiquette « complet et validable ». Aucun des trois audits
ne l'a vu — ils lisaient les pages, pas les dossiers.

Le contrôle lit la **banque de questions**, jamais le nom du fichier : trois fichiers du dépôt
s'appellent `qcm_*.html` sans porter la moindre question (`qcm_algorigrammes_domotique`, qui
est un TP, `qcm_jardin_connecte`, `qcm_ecall_chaine_information`). Compter les noms les aurait
validés tous les trois. C'est la règle n°184, appliquée à l'outil qui applique les règles.

### Les règles

- **n°190** — un statut qu'aucun contrôle ne peut retirer n'est pas un statut, c'est une
  décoration. « Complet et validable » doit pouvoir être **perdu** par une mesure, sinon il ne
  dit rien de plus que « quelqu'un l'a écrit un jour ».
- **n°191** — un audit est une production, pas un verdict. Chaque affirmation vérifiable se
  mesure avant d'être appliquée. Un audit qui se trompe une fois sur quatre reste un très bon
  audit — à condition qu'on sache laquelle.
- **n°192** — un correctif posé contre un défaut que la page a déjà traité coûte plus cher que
  le défaut : il retire l'explication qui répondait à l'objection. Avant de corriger, lire ce
  que la page dit déjà.
- **n°193** — chercher un défaut empêche de voir une absence. Trois lecteurs ont calculé les
  durées de cinq pages sans remarquer qu'aucune ne les affichait.

---

## 2026-08-28 (correction) — Je comptais l'emoji, les espaces, et le signe

La PR #263 publiait une lecture vérifiée de trois audits du Thème 2, et reprochait à leurs
auteurs de mesurer des conventions d'écriture au lieu de mesurer des choses. **Trois de ses
propres verdicts étaient faux, et pour exactement cette raison.**

| Ce que j'avais écrit | Ce qui est vrai | Ce que je comptais |
|---|---|---|
| « le critère *9/9* n'existe pas » | la page écrit « **9 / 9** » | les espaces |
| « cinq séquences n'annoncent aucune durée » | **une** seule ; les quatre autres écrivent la phrase sans ⏱ devant | l'emoji |
| « `5e_C4.7` : 4 min d'activités pour 3 séances » | 144 min ; la page écrit « ⏱ **≈** 20 min » | le signe `≈` |

Le compte du document passe de « 17 exactes, 4 fausses » à **18 exactes, 3 fausses** : la
matrice D22 avait raison sur le critère de recopie. Et ma « découverte » — cinq pages sans
durée annoncée, qu'aucun des trois audits n'aurait vue — se réduit à une page, `4e_C6.2`,
c'est-à-dire au lot qui cumulait déjà tous les autres défauts. Elle n'apprenait rien.

C'est la règle n°184, pour la sixième fois cette semaine, et la première fois dans un document
qui la citait. Écrire la règle ne protège pas de la règle.

### Ce qui change, cette fois

Pas « faire attention ». `_outils/mesurer_temps_seances.py` **refuse de rendre son tableau**
si une seule séquence ressort sans aucune durée d'activité lue, et dit pourquoi : zéro n'est
presque jamais un résultat, c'est une panne de lecture. Les trois erreurs ci-dessus se seraient
signalées seules.

Passé immédiatement sur les trois thèmes, le contrôle a trouvé autre chose : **quatre pages du
Thème 1 sans aucune durée d'activité** — deux pointeurs de mutualisation (normal, ils ne
portent pas de séance) et **`4e_C1.4` et `3e_C1.5`**. Sixième indicateur indépendant à
désigner les deux lots héritage, après le budget de lecture, les aides repliées, le mode
essentiel, les QCM sans réfutation et l'absence de section « Activité ». Aucun des six n'a été
construit pour les trouver.

### Une question tranchée par le dépôt lui-même

Je demandais à Pascal s'il fallait réécrire les bandeaux « 55 min » en créneaux de 90.
La réponse était déjà dans le dépôt : les cinq pages du lot `3e_C9.2` (Thème 3, les plus
récentes) écrivent **« 4 séances de 90 min (1 h 30) »**. Le gabarit existe ; ce sont les seize
bandeaux du Thème 2 qui sont restés à l'ancienne convention. Reste la seule vraie décision
d'enseignant : un lot en 4 × 55 devient 3 × 90 ou 2 × 90 selon ce qu'on garde — et ça, ça se
décide devant une classe, pas devant un dépôt.

### La règle

- **n°194** — un outil de mesure se teste d'abord sur un cas dont on connaît déjà la réponse.
  Un résultat nul n'est pas une découverte, c'est la première chose à vérifier. *(Corollaire de
  la n°184 : la n°184 dit quelle erreur on commet ; la n°194 dit comment on l'attrape.)*

---

## 2026-08-28 — La fiche du jardin, et un statut regagné par la mesure

Le contrôle de la PR #263 avait retiré à `4e_C4.1` — le lot phare de la 4ᵉ, neuf codes en une
séquence — son statut « complet et validable », pour une seule pièce manquante : la fiche
pédagogique. Le lot portait tout le reste (séquence, QCM de 30 questions, matrice de 28 lignes,
deux synthèses, dix SVG originaux, rapport de tests 21/21). Il lui manquait le document qui dit
à un remplaçant ce qu'il tient entre les mains.

Elle est écrite, **d'après la séquence et non d'après une intention** : chaque durée, chaque
production, chaque critère y est recopié de la page. Le contrôle la voit, le statut revient. Il
n'a pas été rendu : il a été regagné. C'est exactement ce qu'on attend d'un statut qui se mesure
(n°190).

### Ce que la fiche dit et que la séquence ne disait pas

Une fiche honnête dit aussi ce que le lot ne porte pas. Cinq points, tous vérifiés :

1. **La version 🅰 est déclarée, pas outillée** — « le vrai jardin, ou une maquette capteur +
   pompe », sans liste de matériel, ni protocole, ni fiche de sécurité. Sans préparation
   d'atelier, la classe bascule en 🅱. *(C'est le défaut D02 des trois audits : celui-là tient.)*
2. **Deux boutons de QCM dans la page** au lieu d'un (règle n°4) : celui du lot, et
   `qcm_xxl_40_reseaux_ip_nfc_rfid_zigbee`, une ressource héritée. **Seule séquence des 17 du
   Thème 2 à enfreindre la règle.**
3. Aucun rôle de groupe, aucun lexique — comme les seize autres.
4. Neuf codes en quatre séances : la couverture est réelle, la maîtrise individuelle ne s'en
   déduit pas. Le lot gagne à être joué comme **vue système**.
5. **La séquence annonce « 30 questions dont 3 avec schémas ». Son QCM en porte quatre.** Elle a
   une image de retard sur son propre QCM.

### Une question tranchée par Pascal, contre mon avis

Je proposais d'aligner les seize bandeaux « 55 min » du Thème 2 sur le gabarit 90 min du lot
`3e_C9.2`, avec le calcul tout prêt : 52 séances de 55 min devenaient 41 créneaux de 90, chacun
avec 18 à 38 minutes de respiration. **Pascal garde les 55 min.** Le calage 1 h 30 restera un
document d'accompagnement, à côté des pages, sans toucher au HTML.

J'ai bien fait de demander : je m'apprêtais à réécrire seize bandeaux dans le mauvais sens sur
la foi d'un « ok on garde » que je lisais à l'envers. La formule était ambiguë, l'action ne
l'était pas — seize fichiers, et le découpage de son année.

- **n°195** — quand une consigne courte peut se lire dans les deux sens et que l'action, elle,
  n'est pas réversible à bon marché, on demande. Une question coûte une minute ; seize pages
  réécrites à l'envers coûtent une confiance.

---

## 2026-08-28 — « Il se refait » : j'avais jugé un lot sur son dossier, sans lire sa page

En annonçant la PR #265, j'ai écrit à Pascal que `4e_C6.2` « ne se répare pas avec une fiche :
il se refait ». **C'était faux.** Le lot manquait trois pièces dans son dossier — fiche, matrice,
synthèses — et j'en ai conclu à l'état de la séquence sans l'ouvrir.

Ouverte, elle porte : un **contrat de séquence** (règle n°18 — que je déclarais absent partout
dans le Thème 1), un référentiel avec **capacité observable** rédigée, huit activités minutées,
**deux verrous expérientiels** (éditeur exigé aux act. 3 et 5, banc 3/3 à l'act. 6), une grille
LSU à quatre niveaux, un bloc de différenciation avec pont explicite vers la 3ᵉ, un bonus à trois
défis, une fiche professeur intégrée, et un rapport de tests réels à **27/27**.

Elle porte même la démarche **prédire → exécuter → comparer** aux activités 5 et 6 — exactement
ce que l'audit ChatGPT réclamait pour la 3ᵉ, et qui est déjà là en 4ᵉ.

C'est la troisième fois cette semaine, et toujours la même faute : **mesurer l'enveloppe et
conclure sur le contenu.** L'emoji au lieu de la durée, les espaces au lieu du critère, et
maintenant le dossier au lieu de la page.

### Ce qui a été fait, à la bonne échelle

- **Bandeau posé** : `⏱ 3 séances de 55 min`, sur les trois « problèmes intermédiaires, un par
  séance » que la page énonce elle-même. Le Thème 2 passe de 16 à **17 séquences sur 17** qui
  annoncent leur durée. Test navigateur : zéro erreur JS, badge rendu.
- **Fiche pédagogique et matrice de couverture écrites**, d'après la page.
- **Le contrôle de statut corrigé** — il disait « manque : QCM » pour un lot qui porte un QCM de
  24 questions, simplement écrit à l'ancienne, sans banque. Il dit désormais « QCM **au gabarit
  maison** », et signale entre parenthèses le QCM hérité quand il y en a un. Il a immédiatement
  révélé le même cas en `4e_C4.4` (`qcm_ecall_chaine_information`).

### Ce que je n'ai pas fait, et pourquoi

`4e_C6.2` reste **« à vérifier »**, pour un seul motif : les synthèses ne sont pas des fichiers.
Le contenu existe — la page porte « Synthèse — à retenir » et une fiche professeur repliée — et
j'aurais pu l'extraire en deux fichiers ce soir pour faire repasser le statut au vert.

Je ne l'ai pas fait. Fabriquer un fichier dans le seul but de satisfaire un contrôle que j'ai
écrit moi-même, c'est transformer la mesure en décoration — exactement ce que la règle n°190
condamne. Les synthèses seront écrites parce qu'un élève absent en a besoin, ou ne le seront pas.

### La règle

- **n°196** — on ne juge pas un lot sur ce que son dossier ne contient pas : le dossier dit ce
  qui est rangé, la page dit ce qui est enseigné. Trois pièces manquantes ne font pas une
  séquence à refaire. *(Corollaire de la n°184 : ici l'enveloppe, ce n'est pas un mot ni un
  emoji, c'est une liste de fichiers.)*
- **n°197** — l'auteur d'un contrôle est le premier à devoir le respecter. Créer la pièce qui
  fait passer sa propre mesure au vert, sans que la pièce serve à quelqu'un, c'est truquer les
  deux.

---

## 2026-08-28 — Le QCM du lot 4e_C6.2, et un défaut que je répétais depuis trois jours

`4e_C6.2` avait trois fichiers `qcm_` dans son dossier et aucun bouton de QCM dans sa page :
l'élève n'y arrivait jamais. Des trois, l'un porte sur l'**éclairage** et code en vocabulaire
privé (CAP/PRG/SYS), l'autre est un **TP** dont le nom de fichier ment, et le troisième — 24
questions sur le bon sujet — était écrit à l'ancienne, avec **la bonne réponse en clair dans le
code de la page** (`value="v0"`).

Ces 24 questions sont devenues la matière première du QCM du lot : 20 reprises, 3 réécrites
(deux « coche les éléments » et une réponse libre, que le gabarit ne porte pas), 1 abandonnée
(elle demandait quel code du dépôt correspond à l'activité — une question sur notre
nomenclature, pas sur la technologie), et 10 nouvelles sur ce que la séquence enseigne et que
l'ancien QCM ne visitait pas : la conversion 0–1023, le cas frontière, la portée d'une preuve,
et ce que devient ce qu'on tape dans un éditeur en ligne.

Résultat : 30 questions, 90 réfutations, 30 notions nommées, cinq codes du programme, 8/7/7/8.
Un seul bouton dans la séquence — la règle n°4 est tenue.

### Le test qui a échoué est le plus utile de la série

Au premier passage, **24 questions sur 30 avaient la bonne réponse la plus longue**, avec 12,5
caractères d'avance en moyenne. C'est le défaut classique du QCM écrit à la main : on soigne la
bonne réponse et on expédie les distracteurs. Un élève qui coche la plus longue s'en tire sans
rien savoir.

Première correction : la bonne réponse n'était plus la plus longue que 3 fois sur 30 — mais la
plus **courte** 24 fois sur 30. **J'avais échangé le biais contre son miroir.** Le rang n'est
donc pas le bon critère : ce qui compte est l'écart **visible**. Après la deuxième passe, l'écart
moyen est de −1,6 caractère, et aucune bonne réponse ne se détache de plus de 8 caractères.

La correction a consisté à **allonger les distracteurs**, pas à raccourcir les bonnes réponses :
un distracteur détaillé et plausible est un meilleur piège qu'un distracteur bâclé — et il
correspond à une vraie erreur d'élève.

### Puis j'ai passé la mesure sur les 43 banques du dépôt

`_outils/controle_longueurs.py` mesure, pour chaque banque, la part de questions où la bonne
réponse se détache de plus de 8 caractères du peloton. Les QCM anciens de la maison sont entre
0 et 10 %. Trois dépassent le seuil de 15 % :

| QCM | détachées | écart moyen | auteur |
|---|---|---|---|
| `qcm_numerique_societe.html` (3e_C1.5) | **28 / 30** | **+34,9 car.** | moi, PR #261 |
| `qcm_cybersecurite_usage_raisonne.html` (4e_C1.4) | **20 / 30** | **+21,6 car.** | moi, PR #261 |
| `qcm_book-train.html` (4e_C4.1·C4.2·C4.4) | 5 / 30 | +7,9 car. | hérité |

Dans `qcm_numerique_societe`, **les 30 bonnes réponses sur 30 sont les plus longues.** Un élève
qui ne lit aucune question et coche systématiquement la réponse la plus longue obtient 30/30.
Ces deux QCM sont fusionnés depuis trois jours et je les ai annoncés « au gabarit ». Ils le
sont : le gabarit ne dit rien de la longueur des options. C'est un contrôle qui manquait.

Les deux sont dans le Thème 1 : ils seront corrigés sur une branche `theme-1`, pas ici.

### Les règles

- **n°198** — dans un QCM, la bonne réponse ne doit pas se reconnaître sans lire la question.
  Un distracteur bâclé est une réponse offerte. On corrige en étoffant les distracteurs, jamais
  en tronquant la bonne réponse.
- **n°199** — corriger un biais en l'inversant, ce n'est pas le corriger. Après « la plus
  longue », « la plus courte » se devine aussi bien. Ce qui doit disparaître, c'est l'écart
  visible, pas le rang.
- **n°200** — un contrôle qui n'existe pas laisse passer un défaut dans tout ce qu'on a produit
  entre-temps. Celui-ci a été écrit trois jours trop tard, et deux lots déjà fusionnés le paient.
