# 🧰 SKILLS_AUDIT — skills locales de l'écosystème cycle 4

*Tenu à jour à chaque ajout/refus de skill. Règle : aucune skill externe n'est
installée si une skill locale suffit. Aucune skill ne contient de secret.*

**Dernier inventaire : 23/10/2026** (skill `inventaire-skills`) — 42 skills jugés
(7 du dépôt, 35 importés sur le compte claude.ai de Pascal), verdicts confrontés au
journal jusqu'à la règle d'or n°311. Détail par skill (raison, preuve, question) :
`inventaire_skills_2026-10-23.json`, remis à Pascal. Entrée du journal du 23/10/2026.
Depuis : `synthese-vulgarisee` (29/10, n°316) et quatre skills le 07/11/2026 (voir ci-dessous) ; le
dépôt compte douze skills, treize avec `texte-clair-et-aere` (08/11/2026).

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
| `synthese-vulgarisee` | 29/10/2026 (n°316) | 29/10/2026 | synthèse élève lisible par un élève de 6e, deux pages A4 | aucune | **UTILISÉE** — absente du registre jusqu'au 07/11/2026 |
| `situation-declenchante-ancree` | 07/11/2026 | 07/11/2026 | ouverture d'une séquence : personne, lieu nommé, mots glosés, image réaliste (05-06/11), hypothèse rappelée au bilan, problématique, prérequis sans « l'an dernier » (n°304) | aucune | **À EXERCER** sur le premier lot qui s'ouvre |
| `lexique-sequence` | 07/11/2026 | 07/11/2026 | remplir `vocabulaire_<lot>.json` (deux passes : technique + lisibilité, sources, mots APTE), puis `generer_lexique.py` et `poser_lien_lexique.py` | Python 3 stdlib (outils existants) | **À EXERCER** |
| `mutualisation-couverture` | 07/11/2026 | 07/11/2026 | revue qualitative de la matrice : COUVERT prouvé (activité vérifiée + 2 questions QCM), doublons → archivage n°12, mutualisation sur trois critères, manques triés par date de classeur ; rapport + décisions pour Pascal | `audit-couverture-cycle4` | **À EXERCER** |
| `differenciation-dans-la-page` | 07/11/2026 | 07/11/2026 | différenciation dans la page unique : aides à deux niveaux, Bonus unique, critères gradués sur les 4 niveaux LSU, versions 🅰/🅱/🅲 — refuse les « trois versions » séparées | `k12-lesson-differentiation` pour le fond | **À EXERCER** |
| `texte-clair-et-aere` | 08/11/2026 | 08/11/2026 | texte élève aéré : consigne et explication séparées, légendes en lignes, corrections réponse → pourquoi → refus un par ligne ; `audit_aeration.py`, `aerer_legendes.py` | Python 3 stdlib | **UTILISÉE** — pilote 5e_C3.1, passe des légendes sur tout le site |

**Origine des quatre skills du 07/11/2026** : une liste de quinze « skills » proposée par Grok à Pascal, par
curiosité. Onze ont été écartées — doublons de skills existants (`methode-fable`, `curriculum-assessment-cycle4`,
`questioning-discussion`, `livraison-depot-cycle4`…), QCM « 10 à 20 questions » contraire au choix du 23/10 (30
fixes), ou « progression spiralaire 5e → 4e → 3e » sans objet quand aucun élève n'a fait les séquences de l'année
précédente (n°304). Les quatre retenues ont été réécrites de zéro sur le journal (jusqu'à la n°318) ; aucun texte
de Grok n'y est repris.

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
| UI UX Pro Max — `nextlevelbuilder/ui-ux-pro-max-skill` (MIT, ~146 k★), skill + CLI `uipro` | 07/11/2026, sur le dépôt GitHub (SKILL.md non lu en détail : la page ne le montre pas) | **REFUSÉ.** Un catalogue (80 styles, 192 palettes, 74 paires de polices, 119 règles UX, 192 règles de « raisonnement ») présenté au modèle ; un CLI qui écrit dans `~/.claude/skills/` de tous les assistants (`--ai all`) ; une offre « premium ». Ses règles contredisent les règles d'or (« pas d'emoji comme icône » contre 📖 Rappel, 🎁 Bonus, 🧠). Sa liste avant livraison (contraste 4,5:1, focus visible, `prefers-reduced-motion`, reflux à 375 px) est déjà dans `_outils/` (`controle_tactile`, `controle_contraste_liens`, `controle_debordement`, n°34). `search.py` : Python stdlib, sans réseau — rien à craindre, rien à prendre. |
| Taste Skill — `Leonxlnx/taste-skill` (MIT, ~108 k★) | 07/11/2026, sur le dépôt GitHub | **REFUSÉ.** Fabrique des sites vitrine de A à Z (30-45 min, « quelques centaines de milliers de tokens »), s'installe par lien symbolique que `git pull` met à jour — le code que l'agent exécute change sans relecture ; pilote un vrai navigateur (`inspect.mjs`, Node 22 + Chrome) ; cherche des images sur Wikimedia Commons, Openverse et le Met ; liens d'affiliation, appli payante à côté. **Une idée reprise, réécrite de zéro** : sa boucle « capture → trois pires défauts → corriger, trois tours au plus » devient la « revue d'écran en trois tours » de `controle-qualite-lot` (07/11/2026). Son choix d'images libres avec crédit sur la page est déjà la règle n°1 et `licences-medias-education`. |
| Impeccable — `pbakaus/impeccable` (Apache 2.0, ~103 k★), parti de `frontend-design` d'Anthropic | 07/11/2026, sur le dépôt GitHub | **REFUSÉ.** Le plus proche du sujet, mais : hooks qui tournent même quand l'utilisateur refuse une commande ; binaire téléchargé dans `~/.impeccable/bin/` ; télémétrie activée par défaut ; mode « live » qui lance `claude` sans sandbox ni approbations ; extension Chrome qui lit toute page. Son détecteur de « slop » (62 règles sans LLM) vise des tics qui ne sont pas ceux du dépôt (Inter partout, dégradés violets, cartes imbriquées — les `section.card` dans un `details` sont voulues par la n°306). `frontend-design`, dont il est parti, est déjà sur le compte. |
| Ponytail — `DietrichGebert/ponytail` (MIT, ~186 k★) | 07/11/2026, sur le dépôt GitHub | **HORS SUJET, REFUSÉ comme plugin.** Qualité de code (« écrire moins », YAGNI), pas de design ni de pédagogie ; hooks de cycle de vie ; une « bande » qui lit les sessions Claude Code (`/ponytail band import`). Le dépôt tient déjà ses scripts courts et en stdlib ; rien à reprendre. |
| Classements « top 10 par étoiles » (Grok, 07/11/2026 ; deux images) : Superpowers, Matt Pocock, Karpathy, Addy Osmani, Graphify, Caveman, Understand Anything, Archify, Awesome Claude Skills | 07/11/2026, par leur description | **Non inspectés en détail : hors sujet.** Ateliers de développement logiciel (plan → TDD), bonnes pratiques de code, explorateurs de bases de code, mode télégraphique, ou simple liste de liens. Les étoiles mesurent la popularité chez les développeurs, pas l'utilité pour des ressources de technologie collège. Même famille qu'ECC, même verdict. `anthropics/skills` est déjà sur le compte (docx, pptx, xlsx, pdf). |
| Skills tiers importés sur le compte claude.ai (Trail of Bits, K-12, diagrammes, électronique…) | 23/10/2026, par l'inventaire | Jamais consignés jusqu'ici. Ceux qui touchent le dépôt : `webapp-testing` (à mettre à jour : forme `'file://' + chemin` interdite par la n°299), `drawio-skill` (à améliorer : texte `html=1` contraire à la n°310), `k12-lesson-planning` et `k12-lesson-differentiation` (cadre américain, sortie Word, sans technologie : **gardés par Pascal le 23/10**, le premier réservé aux demandes explicites de plans de séance en .docx). Les autres ne touchent pas le dépôt ; leurs verdicts sont dans l'inventaire du 23/10, et Pascal les a tous gardés (réponses du 23/10). |
| Veille du 08/11/2026 (demande de Pascal : « des skills pédagogiques et d'autres qui ordonnent et aèrent mieux certains paragraphes », puis « chercher et modifier en l'améliorant ces skills ») — dépôts clonés en lecture seule, aucun code exécuté | 08/11/2026 | **Aucun installé ; idées reprises, réécrites de zéro dans `texte-clair-et-aere`** : `francais-simple` (sachahjkl/skills, MIT — consigne/explication, 20/25 mots, condition avant l'action, table du remplissage ; le meilleur candidat, en français) · `refine-prose` et `clean-copy` (petekp/claude-skills, MIT — la réponse d'abord, couper la légende qui répète l'image ; ses consignes de voix « Pete » et sa chasse aux tics d'IA en anglais écartées) · `assessment-design` (savvides/idstack, MIT — la correction élaborée, le pourquoi ; **plugin refusé** : scripts `bin/`, extension Chrome, jeton Canvas, manifeste de cours) · `writing-clearly-and-concisely` (obra/the-elements-of-style, domaine public — Strunk ; déjà couvert par `synthese-vulgarisee`, une règle reprise : la phrase-repère en tête) · `practical-typography` (ckorhonen/claude-skills, MIT — 45 à 90 caractères par ligne ; le reste porte sur les polices, hors sujet). **Écartés** : `school-skills` (Jellypod, MIT, alpha ; cadre américain, installeur `npx` qui écrit dans `~/.claude/skills/`, doublonne `k12-lesson-planning` et `synthese-vulgarisee`) · `style-prose` (NeverSight, retours à la ligne sémantiques dans le **source**, rendu inchangé : hors sujet) · `skimmable` (ckorhonen, lisibilité du code) · `feedback-pedagogy` (claudskills.com, SKILL.md non lu : source non nommée). |
