# 📓 Journal des décisions — écosystème cycle 4

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
