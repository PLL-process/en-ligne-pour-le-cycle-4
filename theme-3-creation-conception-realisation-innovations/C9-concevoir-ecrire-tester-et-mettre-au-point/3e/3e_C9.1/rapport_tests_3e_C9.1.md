# Rapport de tests réels — Arc variables, marche 3e (3e_C9.1)

**Date : 2026-07-30 · Suite Playwright (Chromium réel, mobile 390×844) · RÉSULTAT : 30/30 PASS**

## Séquence (18 tests)
Titre et h1 conformes à la charte `Thème 3 · New York — 3e · Atelier : …` · nav ⌂ (règle n°11) ·
UN SEUL bouton QCM (règle n°4) · blocs 🧠/🎁 présents · 3 éditeurs Vittascience embarqués ·
verrou act1 FERMÉ avant l'exécution du simulateur puis validation après les 6 étapes (écran
« Q - 96 St 3 min » vérifié) · act2 validée · verrou act3 fermé avant ouverture de l'éditeur puis
validé · banc de tests : T1-T3 verts, T4 signale le cas limite ⚠, badge 🔓 · sauvegarde/restauration
après rechargement (hypothèse + progression).

## QCM (6 tests)
Titre charte · nav ⌂ + ← Séquence · 30 questions chargées · réponses réparties 8/7/7/8 (graine 47) ·
réfutation présente pour CHAQUE distracteur (et vide pour la bonne réponse) · familles VAR 8 / TYP 8 /
PRG 7 / MAP 7.

## Synthèses, stub, archive (5 tests) + JS (1)
Navigation 2 liens sur les 2 synthèses · stub de redirection en place, cible existante ·
ancienne version présente aux archives · **zéro erreur JS** sur tout le parcours
(erreurs réseau de l'iframe Vittascience exclues : hors ligne de test).

## Non testé (honnêteté)
Le contenu INTERNE de l'iframe Vittascience (service externe) : l'embarquement et le suivi
d'ouverture sont testés, pas l'exécution Python côté Vittascience.
