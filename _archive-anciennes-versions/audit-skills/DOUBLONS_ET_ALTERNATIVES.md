# Doublons et alternatives

La règle retenue est un composant principal par fonction, avec un secondaire uniquement lorsqu'il ajoute une capacité distincte.

| Famille | Principal déjà installé | Propositions du classeur | Alternative actuelle | Décision |
|---|---|---|---|---|
| PDF | plugin `pdf` officiel | Anthropic PDF, Stirling-PDF, Pandoc | conserver `pdf` | doublons refusés |
| DOCX | plugin `documents` officiel | Anthropic DOCX, LibreOffice, Pandoc | conserver `documents` | doublons refusés |
| Présentations | plugin `presentations` officiel | Anthropic PPTX, Canva | conserver `presentations`; Canva pour le design | pas d'ajout |
| Tableurs | plugin `spreadsheets` officiel | Anthropic XLSX | conserver `spreadsheets` | doublon refusé |
| GitHub | plugin GitHub officiel | GitHub MCP, Aider, Claude Code, Continue, Cody | GitHub en lecture; Codex seul écrivain | aucun MCP GitHub supplémentaire |
| Navigateur | Browser + Chrome officiels | Playwright MCP, browser-use | conserver les plugins intégrés | doublons refusés |
| Sécurité | Codex Security officiel | Trail of Bits, Promptfoo | Codex Security principal | collection Trail of Bits refusée |
| Web/HTML | build-web-apps + Browser | Vercel/Cloudflare skills | conserver l'officiel | pas d'ajout |
| Accessibilité | Browser/build-web-apps | wshobson accessibility-compliance | sous-plugin distinct, instructions seules | B à valider |
| Hugging Face | aucun plugin HF installé | huggingface/skills | plugin officiel `hugging-face` 1.0.3 | B à valider |
| Arduino/EEA | skills personnels Arduino, EEA, Proteus | dépôts Arduino/ESP32/RTOS | garder les skills ciblés | les bibliothèques ne sont pas des skills |
| Diagrammes | eea-diagram-designer + visualize | outils divers | conserver les deux rôles distincts | pas d'ajout |
| CAO/3D | cad, implicit-cad, gcode, bambu-labs | FreeCAD, OpenSCAD, Blender, CadQuery | conserver les skills spécialisés | applications séparées |
| QCM/éducation | workflows génériques et HTML | H5P, Moodle, LMS | utiliser au besoin comme applications | aucune installation Codex |
| Audio/vidéo | aucune collection globale | Whisper, FFmpeg, OBS, Kdenlive | installer une application seulement sur demande | hors audit skill |
| Documentation | documents/PDF + OpenAI Docs | MarkItDown, Pandoc, Docusaurus, MkDocs | outils de projet seulement | pas de skill supplémentaire |
| Modèles locaux | Ollama 0.31.1 | llama.cpp, LocalAI, Open WebUI | Ollama reste principal | applications séparées |
| Gestion de projet | Notion installé | n8n, Activepieces, Flowise | Notion/automations ciblées | pas d'installation en bloc |
| Veille web | Browser/recherche web | Firecrawl, Jina Reader, Context7 | outils intégrés d'abord | MCP externe seulement sur besoin |
| Citations | aucun plugin Zotero | zotero/zotero | plugin officiel Zotero 0.1.2 | non prioritaire, B si demandé |

Doublons explicites comptés dans le CSV : 4. Les familles contiennent davantage de recouvrements fonctionnels, mais ce nombre ne double-compte pas toutes les applications similaires.

