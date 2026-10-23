# 🧰 SKILLS_AUDIT — skills locales de l'écosystème cycle 4

*Tenu à jour à chaque ajout/refus de skill. Règle : aucune skill externe n'est
installée si une skill locale suffit. Aucune skill ne contient de secret.*

**Dernier inventaire : 23/10/2026** (skill `inventaire-skills`) — 42 skills jugés
(7 du dépôt, 35 importés sur le compte claude.ai de Pascal), verdicts confrontés au
journal jusqu'à la règle d'or n°311. Détail par skill (raison, preuve, question) :
`inventaire_skills_2026-10-23.json`, remis à Pascal. Entrée du journal du 23/10/2026.

## Skills du dépôt (`.claude/skills/`)

| Nom | Créée | Mise à jour | Utilité | Dépendances | Décision |
|---|---|---|---|---|---|
| `audit-couverture-cycle4` | 21/07/2026 (lot 0) | 23/10/2026 | matrice des 114 codes : `build_audit.py`, `controle_statut.py`, `controle_couverture.py` | Python 3 stdlib | **UTILISÉE** |
| `sequence-pedagogique-engageante` | 21/07/2026 (lot 0) | 23/10/2026 | squelette de séquence (n°306) et règles de forme de la page élève | aucune | **UTILISÉE** |
| `qcm-html-accessible` | 21/07/2026 (lot 0) | 23/10/2026 | QCM d'entraînement : en-tête standard, distracteurs, contrôles des QCM | Python 3 stdlib, Node | **UTILISÉE** — ne plus relancer `build_qcms.py` |
| `controle-qualite-lot` | 21/07/2026 (lot 0) | 23/10/2026 | revue de fin de lot : les contrôles de `_outils/`, livraison par `livraison-depot-cycle4` | Python 3 stdlib, Node, Playwright | **UTILISÉE** |
| `arduino-grove-college` | 21/07/2026 (lot 0) | 23/10/2026 | activités carte/capteurs, versions A/B/C, très basse tension | aucune | **UTILISÉE** |
| `licences-medias-education` | 21/07/2026 (lot 0) | 23/10/2026 | provenance des médias, SOURCES_MEDIAS.md, documents d'éditeur | Python 3 stdlib | **UTILISÉE** |
| `chaine-energie-fonctionnelle` | 21/10/2026 (n°310) | 23/10/2026 | schémas des chaînes d'énergie, représentation fonctionnelle | Python 3 stdlib | **UTILISÉE** |

Questions pédagogiques posées à Pascal le 23/10/2026, **tranchées le même jour** et
écrites dans ces skills : QCM à **30 questions fixes**, sans tirage aléatoire ; séquence
modèle **5e_C3.1** ; fonction absente d'une chaîne **en pointillés grisés avec sa raison**
(n°131 ; générateur et page 3e_C9.2 à mettre en conformité) ; Arduino : **C++ commenté et
compilation Arduino CLI gardés**, l'élève programmant en blocs Vittascience.

## Skills du compte claude.ai de Pascal qui parlent du dépôt

Ils ne sont pas versionnés ici : Pascal les remplace lui-même sur claude.ai. État au 23/10/2026.

| Nom | Verdict du 23/10 | Suite |
|---|---|---|
| `methode-fable` | Mettre à jour | copie de `_outils/METHODE.md` du 23/07 ; METHODE.md corrigé ce jour, le skill est à réaligner |
| `livraison-depot-cycle4` | Améliorer | tester d'abord le droit de pousser (n°5 amendée), le colis reste le plan B |
| `curriculum-assessment-cycle4`, `explicit-instruction`, `self-regulated-learning`, `gantt-pedagogique`, `skill-crcn-2026`, `dnb-technologie`, `manuels-2024-mecaniques` | Mettre à jour | contredits par les n°202, 300, 301, 304, 305, 306 ou par des faits datés |
| `questioning-discussion`, `reponses-actionnables` | Améliorer | compléments (n°139, 144, 148 ; ordre de fin de réponse) |
| `inventaire-skills`, `balayage-navigateur` | Améliorer → **corrigés le 23/10** | voir « Skills externes » |

## Skills prévues (créées au moment où un lot en aura besoin, pas avant)

`referentiel-technologie-2024` (source confirmée : `_outils/data_competences.py`) ·
`svg-pedagogique` (les chaînes d'énergie sont couvertes par `chaine-energie-fonctionnelle`) ·
`projet-technologique-note` · `robotique-mbot2-mblock` ·
`vittascience-blocs-code` · `reseaux-filius` · `reseaux-packet-tracer` ·
`proteus-arduino` · `cao-college` · `sweethome3d-habitat` ·
`blender-visualisation-pedagogique` · `tableur-donnees-capteurs` ·
`compatibilite-materiel-logiciel` (couverte par la matrice CSV) ·
`alternative-sans-materiel` (couverte par `arduino-grove-college` §versions).
`preparation-lot-chatgpt` est sans objet depuis la n°5 amendée (Fable pousse et ouvre ses PR).

Créer 20 skills d'avance diluerait leur qualité ; chacune naîtra avec le premier
lot qui l'exerce, avec exemples tirés de ce lot.

## Skills externes

Toute skill externe passe par l'inspection complète (SKILL.md, scripts,
dépendances, réseau, permissions, réputation) avant décision, consignée ici.

| Source | Inspectée | Décision |
|---|---|---|
| ECC — `affaan-m/ECC` (licence MIT), plugin Claude Code | 23/10/2026 | **Plugin REFUSÉ** : conçu pour le développement logiciel (tests d'abord, couverture de 80 %, build), il présente tout son catalogue (311 skills, 71 agents) au modèle à chaque session, ses hooks exécutent des scripts à chaque action, et sa mémoire et son « apprentissage continu » doublonnent la gouvernance par le journal. **Deux idées adaptées, réécrites de zéro** (aucun code tiers exécuté) : `inventaire-skills` (d'après `skill-stocktake`) et `balayage-navigateur` (d'après `e2e-testing`), skills du compte claude.ai, Python 3 stdlib + Playwright. |
| Skills tiers importés sur le compte claude.ai (Trail of Bits, K-12, diagrammes, électronique…) | 23/10/2026, par l'inventaire | Jamais consignés jusqu'ici. Ceux qui touchent le dépôt : `webapp-testing` (à mettre à jour : forme `'file://' + chemin` interdite par la n°299), `drawio-skill` (à améliorer : texte `html=1` contraire à la n°310), `k12-lesson-planning` et `k12-lesson-differentiation` (cadre américain, sortie Word, sans technologie : **gardés par Pascal le 23/10**, le premier réservé aux demandes explicites de plans de séance en .docx). Les autres ne touchent pas le dépôt ; leurs verdicts sont dans l'inventaire du 23/10, et Pascal les a tous gardés (réponses du 23/10). |
