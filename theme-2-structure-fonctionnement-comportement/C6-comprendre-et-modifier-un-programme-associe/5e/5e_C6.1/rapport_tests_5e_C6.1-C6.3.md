# Rapport de tests — Lot 5e_C6.1 → C6.3 « Programmer le lampadaire »

**Date** : 2026-07-23 · **Agent** : Fable (Thème 2) · **Outil** : Playwright
(Chromium headless), viewport mobile 390×844 · **Verdict global : 23 / 23 ✅**

Conformément au prompt maître : tous les tests listés ont été **réellement
exécutés** (script `tests_lot07.js`) ; aucun résultat n'est déclaré sans exécution.

## Séquence (13 tests)

| Test | Résultat |
|---|---|
| Chargement sans erreur JS | ✅ |
| Rappel d'hypothèse affiché | ✅ |
| Act. 1 carte d'identité du programme (6 classements + seuil + états) : 8/8 | ✅ |
| Act. 2 algorithme en langage naturel (6 étapes + SI/ET/SINON) : 9/9 | ✅ |
| **Verrou expérientiel** : refus de valider sans la mission au simulateur | ✅ |
| Mission mairie vérifiée (seuil 50, luminosité 45 → veille, réglage d'origine testé aussi) | ✅ |
| État simulé cohérent (veille à 45 % avec seuil 50) | ✅ |
| Act. 3 validée (3 prédictions + mission réelle) | ✅ |
| Act. 4 réinvestissement arrosage : 4/4 | ✅ |
| Progression 4/4 + coches des 3 séances | ✅ |
| Reprise après rechargement (réponses, validations, mission __exp) | ✅ |
| Zéro lien local cassé (SVG, QCM, synthèses, lien vers l'îlot 5e_C4) | ✅ |
| Zéro erreur JS après l'ensemble des interactions | ✅ |

## QCM (5 tests)

Chargement · 30 questions ✅ · réponses réparties A/B/C/D = 7/7/8/8 ✅ ·
2 questions illustrées (SVG présents) ✅ · parcours 30/30 → 20,0/20 avec
bilan par 3 codes ✅ · zéro erreur JS ✅.

## Synthèses (2) et index (3)

Synthèses élève/professeur sans erreur, schémas présents ✅. Index : badge NEW
sur 5e_C6.1 + compétence C6, ancre auto-ouverte/ciblée, pointeur 5e_C6.3 badgé ✅.

## Limites connues

- Google Fonts inaccessible en sandbox (polices de repli, sans incidence).
- Version 🅰 (maquette + VittaScience) non testable en sandbox : annoncée comme
  option, très basse tension uniquement.
