# Relais — en-ligne-pour-le-cycle-4

Mis à jour le 28/10/2026 23:24 (heure de la Martinique). Le journal des décisions fait foi ; ce relais dit où on en est.

## Où on en est
- Fusionnées ce soir : #537 (q.py de 5e_C2.1, 5e_C1.1, 5e_C1.2 reprennent les propositions publiées — n°144), #538 (carte des interacteurs Shenzhen refaite, premium).
- **#539** ouverte : règle d'or n°315 « tout schéma est premium » + `_outils/controle_schemas.mjs` (banc 10/10). Constat main : 448 schémas, 138 avec ✘ (T1 68, T2 48, T3 22).
- Décisions Pascal : contrôle + revue à l'œil ; revue thème par thème EN ENTIER ; outils installés sans demander, notés au journal ; « simple même pour un 6e ».
- Mesures et planches : `scratchpad/n315/theme-N.json`, `planche_theme-N/index.html`. Worktree règle : `scratchpad/wt_315`.
- Thème 1 : 3/4 des ✘ viennent du générateur `ateliers-representations` (cartes mentales : feuilles à 6 u ; pieuvres : étiquettes FP/FC collées aux bulles).
- Graphviz `dot` et elkjs disponibles.

_(écrit par Claude le 28/10/2026 23:24)_

## Branche et PR
- Branche : `fable/theme-2-regle-304` — dernier commit 5a5ededb4 Règle d'or n°304, vague du thème 2 : douze ouvertures ne disent plus le passé
- PR #539 ouverte (`fable/regle-315-schemas-premium`) — Règle d'or n°315 : tout schéma est premium — le contrôle des schémas — CI : in_progress

## Décisions en attente
_Aucune._

## Prochaine action
➡️ Thème 1 : corriger le générateur des ateliers de représentations, puis les SVG isolés, puis revue à l'œil des 283 schémas ; PR thème 1.

## Décisions prises récemment (messages de Pascal)
- 28/10/2026 23:09 — « un outil s'il donne un meilleur schéma ou une meilleur representation dans le sens vulgarisée, simple meme pour un 6e, et pédagogique »
- 28/10/2026 19:52 — « 1a »

_Résumés de compaction : `COMPACTIONS.md`, même branche._
