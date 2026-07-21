# Audit de sécurité

## Méthode

- Vérification GitHub de 198 dépôts valides; deux lignes pointent vers des organisations et non des dépôts.
- Dernier commit récupéré par le connecteur GitHub; seuil d'abandon potentiel fixé au 15 janvier 2025.
- Clonage temporaire, sans installation, des dix dépôts ressemblant à des skills.
- Inspection des `SKILL.md`, manifests, scripts, dépendances et workflows.
- Recherche heuristique de `eval/exec`, commandes destructives, sous-processus/téléchargements, accès aux secrets et mécanismes admin/persistance. Un motif est un signal de revue, pas une preuve de malveillance.
- Recherche des issues et PR ouvertes étiquetées `security` ou `critical` : aucune détectée sur les dix candidats; l'absence d'étiquette ne prouve pas l'absence de vulnérabilité.

## Candidats réels

| Dépôt | Structure | Contributeurs historiques | Licence | Risque | Décision |
|---|---:|---:|---|---|---|
| openai/skills | 44 skills, 62 scripts | 35 | Apache-2.0 par skill | A pour skills officiels ciblés | ne pas réinstaller les composants déjà fournis |
| anthropics/skills | 18 skills, 75 scripts | 15 | Apache-2.0 par skill | B | refusé: doublons bureautiques |
| huggingface/skills | 26 skills, 58 scripts, 1 MCP | 45 | Apache-2.0 | B | préférer le plugin officiel HF |
| microsoft/skills | 191 skills, 113 scripts, 2 MCP | 36 | MIT | B/C | collection refusée |
| google/skills | 76 skills, 34 scripts | 5 | Apache-2.0 | B | collection refusée |
| cloudflare/skills | 11 skills, 5 scripts, 1 MCP | 29 | Apache-2.0 | B | préférer le plugin officiel ciblé |
| vercel-labs/skills | 1 skill; CLI du dépôt séparée | 116 | MIT | A pour `skills/find-skills` seul | mise à jour avec sauvegarde |
| trailofbits/skills | 75 skills, 85 scripts, 2 MCP | 36 | CC-BY-SA-4.0 | C | refusé: redondant et scripts puissants |
| wshobson/agents | 90 plugins Codex, 175 skills | 76 | MIT | C dépôt entier; B sous-plugin a11y | validation manuelle ciblée |
| sickn33/agentic-awesome-skills | 59 plugins, 6195 skills, 2868 scripts | 311 | MIT + licences hétérogènes | D | refusé |

## Signaux principaux

- `sickn33/agentic-awesome-skills` est trop vaste pour garantir la provenance de chaque composant; les motifs statiques incluent de nombreuses suppressions, installations et opérations privilégiées.
- `trailofbits/skills` contient des hooks de nettoyage, des scripts d'installation et des outils de sécurité à exécuter uniquement en environnement isolé.
- `cloudflare/skills` contient des scripts réseau et de récupération de secret dans un scénario Turnstile; aucun de ces scripts n'est retenu.
- `huggingface/skills` contient des téléchargements de modèles, créations de rôles cloud, déploiements et suppressions de ressources. Le sous-skill local-models est instructionnel, mais le plugin officiel actuel déclare des capacités Read/Write.
- `wshobson/agents/plugins/accessibility-compliance` possède un manifeste Codex valide (1.2.3), deux `SKILL.md`, une référence et aucun script, hook ou MCP. Le risque restant est la source communautaire et la possible obsolescence de certaines statistiques.
- Le skill `find-skills` retenu ne contient qu'un `SKILL.md`; aucun script n'est installé avec lui.

## Politique GitHub appliquée

- Le plugin GitHub connecté possède des droits administrateur et push sur `PLL-process/synthese-app`.
- Aucun outil tiers supplémentaire n'obtient de jeton ou de droit GitHub.
- Aucun push, merge, PR, modification de paramètres ou accès aux secrets GitHub Actions n'a été effectué.
- La configuration locale `git-always-force-push=true` est signalée comme mal alignée avec la politique; aucun changement automatique n'est effectué.

