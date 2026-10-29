# Relais — en-ligne-pour-le-cycle-4

Mis à jour le 29/10/2026 00:06 (heure de la Martinique). Le journal des décisions fait foi ; ce relais dit où on en est.

## Où on en est
- Fusionnées : #537 (q.py ← propositions publiées, 3 QCM thème 1), #538 (carte Shenzhen premium), #539 (règle n°315 + controle_schemas.mjs).
- Ouvertes : **#540** (complément n°315 : pastille ≠ contact, 128 schémas avec ✘) ; **#541** (règle n°316 « une synthèse se lit par un élève de 6e » + skill `.claude/skills/synthese-vulgarisee/`).
- Modèles lus (navigateur de Pascal) : Toulouse fiches de synthèse 2024 (1 page « Ce que je dois retenir », carte centrale + blocs) et fiches de connaissances CF-2024 (FC4-1, FC16). Pujades et Bordeaux : sites en panne ce soir. Limoges : pas regardé.
- Campagne décidée par Pascal : thème par thème EN ENTIER (schémas n°315, et synthèses n°316 proposées avec). Pilote synthèse : 5e_C1.1. Thème 1 : 59 schémas avec ✘, 3/4 dans le générateur `ateliers-representations/_generation/figures.py` (carte_mentale : pas 46→56 ; pieuvre : étiquettes FC au milieu du segment visible).
- Mesures : `scratchpad/n315/`.

_(écrit par Claude le 29/10/2026 00:03)_

## Branche et PR
- Branche : `fable/theme-2-regle-304` — dernier commit 5a5ededb4 Règle d'or n°304, vague du thème 2 : douze ouvertures ne disent plus le passé
- PR #541 ouverte (`fable/regle-316-syntheses-vulgarisees`) — Règle d'or n°316 : une synthèse élève se lit par un élève de 6e — skill synthese-vulgarise — CI : success
- PR #540 ouverte (`fable/regle-315-pastilles`) — Règle n°315 (complément) : une pastille posée sur un cadre n'est pas un contact — CI : success

## Décisions en attente
_Aucune._

## Prochaine action
➡️ Fusionne #540 (complément de la règle sur les schémas) et #541. Ensuite j'attaque le thème 1 : le générateur des ateliers de représentations (les trois quarts des défauts de schémas), puis la synthèse de `5e_C1.1` réécrite en pilote.

## Décisions prises récemment (messages de Pascal)
- 28/10/2026 23:09 — « un outil s'il donne un meilleur schéma ou une meilleur representation dans le sens vulgarisée, simple meme pour un 6e, et pédagogique »
- 28/10/2026 19:52 — « 1a »

_Résumés de compaction : `COMPACTIONS.md`, même branche._
