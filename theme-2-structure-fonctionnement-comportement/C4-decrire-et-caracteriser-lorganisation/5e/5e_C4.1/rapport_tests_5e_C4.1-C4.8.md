# Rapport de tests — Lot 5e_C4.1 → C4.8 « Le lampadaire intelligent »

**Date** : 2026-07-23 · **Agent** : Fable (Thème 2) · **Outil** : Playwright
(Chromium headless), viewport mobile 390×844 · **Verdict global : 26 / 26 ✅**

Conformément au prompt maître : tous les tests listés ont été **réellement
exécutés** (script `tests_lot05.js`) ; aucun résultat n'est déclaré sans
exécution. Les suites des LOTS 03 et 04 ont été **rejouées** après le correctif
de répartition des réponses (30/30 et 22/22 ✅).

## Séquence (16 tests)

| Test | Résultat |
|---|---|
| Chargement sans erreur JS (console + pageerror filtrés hors réseau sandbox) | ✅ |
| Rappel d'hypothèse affiché après saisie | ✅ |
| Act. 1 fonctions/solutions + matériaux : validation 9/9 | ✅ |
| Act. 2 chaîne d'énergie + natures : validation 9/9 (chaîne fléchée exigée) | ✅ |
| **Verrou expérientiel** : refus de valider l'act. 3 sans expériences réelles | ✅ |
| Simulateur : jour → éteint · nuit → veille 30 % · nuit + passage → pleine puissance | ✅ |
| Act. 3 validée 10/10 après les 3 observations réelles | ✅ |
| Act. 4 descripteurs (batterie_pct, L5, L3, 2 posés 2025) : validation 7/7 | ✅ |
| Act. 5 réseau local : validation 6/6 | ✅ |
| Act. 6 jeu du courrier (conflit de noms, sans destinataire) : validation 5/5 | ✅ |
| Act. 7 réinvestissement sonnette connectée : validée | ✅ |
| Progression 7/7 activités + coches des 5 séances | ✅ |
| Reprise après rechargement : réponses restaurées | ✅ |
| Reprise : validations ET traces d'expériences (__exp) restaurées | ✅ |
| Zéro lien local cassé (SVG, QCM, synthèses, pointeurs) | ✅ |
| Zéro erreur JS après l'ensemble des interactions | ✅ |

## QCM (5 tests)

| Test | Résultat |
|---|---|
| Chargement sans erreur JS · 32 questions dans la grille | ✅ |
| Bonnes réponses réparties A/B/C/D = 8/8/8/8 (règle issue du correctif LOT 03/04) | ✅ |
| 6 questions illustrées, fichiers SVG présents sur le disque | ✅ |
| Parcours complet 32/32 bonnes réponses → note 20,0/20 · bilan par 8 codes | ✅ |
| Zéro erreur JS après le scénario complet | ✅ |

## Synthèses (2 tests)

Synthèse élève et synthèse professeur : chargement sans erreur, tous les
schémas SVG référencés présents. ✅

## Index / badge NEW (3 tests)

| Test | Résultat |
|---|---|
| Badge NEW sur 5e_C4.1 + badge unique sur la compétence C4 | ✅ |
| Ancre `#5e_C4.1` : auto-ouverture du dépliant C4 + ciblage visuel | ✅ |
| Pointeurs 5e_C4.2 → C4.8 badgés NEW | ✅ |

## Limites connues

- Google Fonts inaccessible dans le bac à sable de test : erreurs réseau
  filtrées (la page utilise des polices de repli système, sans incidence).
- Tests exécutés en local (`file://`) ; le comportement GitHub Pages est
  identique (aucune requête serveur, liens relatifs).
- La version 🅰 (sortie parking + maquette Grove) n'est pas testable en
  sandbox : la page l'annonce comme option matérielle sans en dépendre.
