# Rapport de tests réels — Arc variables, marche 5e (5e_C9.1 → C9.3)

**Date : 2026-07-30 · Suite Playwright (Chromium réel, mobile 390×844) · RÉSULTAT : 27/27 PASS**

## Séquence (17)
Titre/h1 charte · nav ⌂ (règle n°11) · UN bouton QCM (règle n°4) · blocs 🧠/🎁 · 2 éditeurs Vittascience
embarqués · photo Coney MUTUALISÉE (référence + cible vérifiées) · verrou act1 fermé avant simulateur puis
validé après les 4 étapes (écran « 21 » vérifié) · banc de lecture : T1-T2 verts, T3 démasque le bug
(19 ✘ attendu 23), badge 🔓 · banc barrière : B3 cas limite FERMÉE ✔, badge 🔓 · sauvegarde/restauration.

## QCM (7)
Titre charte · nav ⌂ + ← Séquence · 30 questions · réponses 8/7/7/8 (graine 53) · familles BOI/LIR/MOD
10/10/10 · réfutation de CHAQUE distracteur (vide sur la bonne) · 3 illustrées.

## Synthèses (2) + JS (1)
Navigation 2 liens sur les 2 synthèses · zéro erreur JS (réseau iframe exclu, hors ligne de test).

## Non testé (honnêteté)
Le contenu interne de l'iframe Vittascience (service externe) : l'embarquement et le verrou d'ouverture
sont testés, pas l'exécution Python côté Vittascience.
