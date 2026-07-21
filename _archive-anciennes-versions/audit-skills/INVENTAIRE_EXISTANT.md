# Inventaire existant

Audit en lecture seule réalisé le 15 juillet 2026. Aucun secret n'a été lu ni affiché.

## Codex et configuration

- Application Codex Windows : `26.707.3748.0`.
- Codex CLI : `0.137.0`.
- Dossiers de configuration : `C:\Users\PhaseLockedLoop\.codex` et `C:\Users\PhaseLockedLoop\.agents`.
- Skills système : imagegen, openai-docs, plugin-creator, skill-creator, skill-installer.
- Skills personnels : 26 dossiers détectés, dont Arduino/Grove, EEA, Proteus, CAO, G-code, URDF/SDF/SRDF, impression 3D et identité visuelle technique.
- Aucun skill personnel supplémentaire dans `~/.codex/skills` hors `.system`.
- Plugins activés : GitHub, documents, spreadsheets, presentations, PDF, browser, Chrome, computer-use, build-web-apps, codex-security, openai-developers, Canva, Figma, Gmail, Outlook Email, Notion, template-creator et visualize.
- Plusieurs anciennes révisions restent dans le cache des plugins. Elles ne sont pas désinstallées conformément à la consigne.

## MCP et connecteurs

- MCP configurés localement : `node_repl` et `GitKraken`.
- GitHub est connecté par le plugin officiel. Le compte a des droits complets sur `PLL-process/synthese-app`; l'audit l'a utilisé uniquement en lecture.
- Aucun manifeste `.mcp.json`, `.codex-plugin/plugin.json` ou `SKILL.md` n'est présent dans le sous-projet courant.

## Outils Windows

| Outil | État |
|---|---|
| Git | 2.55.0.windows.2 |
| Python | 3.14.5 |
| Node.js | 22.22.3 |
| npm | 10.9.8 |
| Docker CLI | absent |
| Ollama | 0.31.1 |
| PowerShell | 7.5.5 |
| GitHub CLI | 2.95.0, non authentifié |

L'inspection passive des applications a confirmé Excel et Ollama installés.

## Dépôts locaux et état Git

- Dépôts détectés sous `Documents\GitHub` : `en-ligne-pour-le-cycle-4`, `math-6e`, `sequences-arduino`.
- Dépôt courant : `en-ligne-pour-le-cycle-4`.
- Branche présente avant l'audit : `codex/jumeau-numerique-v1`.
- 43 chemins modifiés/non suivis existaient avant l'audit. Ils appartiennent à l'utilisateur et n'ont pas été modifiés.

## Secrets et permissions

- Variables connues `OPENAI_API_KEY`, `GITHUB_TOKEN`, `GH_TOKEN`, `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, `AZURE_OPENAI_API_KEY`, `NPM_TOKEN`, `PYPI_TOKEN`, `DOCKER_PASSWORD` : absentes de l'environnement du processus.
- Fichiers potentiellement sensibles contrôlés sans lecture du contenu (`.git-credentials`, `.npmrc`, `.config\gh\hosts.yml`, `.codex\.env`) : absents.
- L'authentification des connecteurs gérés par l'application n'est pas écrite dans le dépôt.
- Aucune permission excessive n'a été détectée sur les fichiers sensibles vérifiés, puisqu'ils sont absents.

## Point de vigilance local

`desktop.git-always-force-push = true` est configuré dans Codex. Cette option est incompatible avec la politique prudente du dépôt principal. Elle n'a pas été modifiée, car la demande interdit les changements de configuration non validés. Recommandation : la désactiver après accord explicite.

## Sources de référence

- Manuel Codex actuel : https://developers.openai.com/codex/codex-manual.md
- Plugins officiels : https://github.com/openai/plugins (commit audité `11c74d6ba24d3a6d48f54a194cd00ef3beea18f9`, 13 juillet 2026)

