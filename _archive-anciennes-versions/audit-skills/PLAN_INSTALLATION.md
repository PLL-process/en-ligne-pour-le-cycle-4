# Plan d'installation

## Résumé des 200 lignes

- ABANDONNE: 13
- APPLICATION: 92
- BIBLIOTHEQUE: 74
- COLLECTION_DE_SKILLS: 7
- DOCUMENTATION: 2
- NON_PERTINENT: 2
- PLUGIN_CODEX: 1
- RISQUE: 1
- SERVEUR_MCP: 7
- SKILL_CODEX: 1

- Dépôts analysés : 200.
- Dépôts GitHub valides : 198.
- Structures de skills/collections détectées : 8.
- Lignes classées plugin Codex : 1; 149 manifests Codex ont aussi été observés dans deux grands agrégateurs.
- Serveurs MCP : 7.
- Applications : 92.
- Doublons explicitement refusés : 4.
- Projets abandonnés/archivés : 13.
- Lignes refusées ou non installables comme skill : 195.
- Actions automatiques recommandées : 1 mise à jour, aucune nouvelle installation.

## Lot A — exécution automatique autorisée

1. Sauvegarder `~/.agents/skills/find-skills` hors des dossiers scannés comme skills.
2. Installer uniquement `skills/find-skills` depuis `vercel-labs/skills`, commit `5527c09adc367612b0bffd9c80e3bc28a6b01b6d`.
3. Vérifier le frontmatter, l'égalité avec la source épinglée et l'absence de scripts.
4. Tester la présence du skill et documenter le retour arrière.

## Lot B — validation humaine obligatoire

- Plugin officiel `hugging-face@openai-curated` 1.0.3. Motif : accès au Hub utile, mais manifest déclaré `Read` et `Write`, authentification à l'installation, commandes de dépôt/job possibles.
- Sous-plugin `accessibility-compliance` 1.2.3 depuis `wshobson/agents`, commit épinglé. Motif : utile pour HTML/QCM accessibles et sans code exécutable, mais source communautaire.

Aucun B n'est installé pendant cet audit.

## Lots C et D

Aucune installation. Les collections Trail of Bits et wshobson complètes nécessitent un bac à sable; l'agrégateur sickn33 est refusé.

## Retour arrière A

La copie précédente est déplacée vers `~/.codex/backups/skills`. Le rollback consiste à mettre la nouvelle copie en quarantaine puis à restaurer le dossier sauvegardé; aucune suppression massive n'est utilisée.

