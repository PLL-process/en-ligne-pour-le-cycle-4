# 🧰 SKILLS_AUDIT — skills locales de l'écosystème cycle 4

*Tenu à jour à chaque ajout/refus de skill. Règle : aucune skill externe n'est
installée si une skill locale suffit. Aucune skill ne contient de secret.*

## Skills locales créées (lot 0 — 21 juillet 2026)

| Nom | Origine | Version | Licence | Utilité | Dépendances | Risques | Décision |
|---|---|---|---|---|---|---|---|
| `audit-couverture-cycle4` | locale (Claude, lot 0) | 1.0 | même licence que le dépôt | resynchroniser la matrice des 114 codes via `_outils/build_audit.py` | Python 3 stdlib | aucun | **UTILISÉE** |
| `sequence-pedagogique-engageante` | locale (Claude, lot 0) | 1.0 | idem | gabarit de séquence (modèle Jardin connecté amélioré) | aucune | aucun | **UTILISÉE** |
| `qcm-html-accessible` | locale (Claude, lot 0) | 1.0 | idem | spécification QCM entraînement/sommatif + réutilisation `qcm_generator.py` | Python 3 stdlib | aucun | **UTILISÉE** |
| `controle-qualite-lot` | locale (Claude, lot 0) | 1.0 | idem | contrôle qualité bloquant avant remise à ChatGPT | Python 3 stdlib | aucun | **UTILISÉE** |
| `arduino-grove-college` | locale (Claude, lot 0) | 1.0 | idem | règles Arduino UNO/R4 + Grove, 20 éléments, versions A/B/C, sécurité TBT | aucune | aucun | **UTILISÉE** |
| `licences-medias-education` | locale (Claude, lot 0) | 1.0 | idem | ordre de préférence des licences + tenue de SOURCES_MEDIAS.md | aucune | aucun | **UTILISÉE** |

## Skills prévues (créées au moment où un lot en aura besoin, pas avant)

`referentiel-technologie-2024` (source confirmée : `_outils/data_competences.py`) ·
`svg-pedagogique` · `projet-technologique-note` · `preparation-lot-chatgpt`
(pour l'instant couverte par `controle-qualite-lot`) · `robotique-mbot2-mblock` ·
`vittascience-blocs-code` · `reseaux-filius` · `reseaux-packet-tracer` ·
`proteus-arduino` · `cao-college` · `sweethome3d-habitat` ·
`blender-visualisation-pedagogique` · `tableur-donnees-capteurs` ·
`compatibilite-materiel-logiciel` (couverte par la matrice CSV) ·
`alternative-sans-materiel` (couverte par `arduino-grove-college` §versions).

Créer 20 skills d'avance diluerait leur qualité ; chacune naîtra avec le premier
lot qui l'exerce, avec exemples tirés de ce lot.

## Skills externes

Aucune skill externe n'a été recherchée, téléchargée ni installée pour ce lot.
Toute future skill externe passera par l'inspection complète (SKILL.md, scripts,
dépendances, réseau, permissions, réputation) avant décision, consignée ici.
