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
