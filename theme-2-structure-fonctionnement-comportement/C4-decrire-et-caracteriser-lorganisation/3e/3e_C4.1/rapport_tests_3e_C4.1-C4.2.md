# Rapport de tests — Lot 3e_C4.1 + C4.2 « L'énergie de la station »

**Date** : 2026-07-23 · **Agent** : Fable (Thème 2) · **Outil** : Playwright
(Chromium headless), viewport mobile 390×844 · **Verdict global : 23 / 23 ✅**


> **Correction du 31/08/2026 — le verrou expérientiel s'ouvrait en partie tout seul.**
> `_outils/controle_verrous.mjs`, écrit ce jour-là, ouvre chaque séquence du dépôt dans un
> navigateur neuf et lit `window.__exp` juste après le chargement. Cette page en portait déjà
> la clé `suffisant` **avant tout geste** : la fonction d'affichage du simulateur était appelée à
> l'initialisation et enregistrait l'état affiché comme une observation. Le verrou de
> l'activité concernée s'ouvrait donc en partie sans que l'élève ait rien manœuvré, ce que la
> règle d'or n°226 interdit. La fonction ne trace plus que sur un geste ; vérifié : `__exp`
> est vide à l'ouverture, et se remplit dès le premier mouvement de curseur.
Conformément au prompt maître : tous les tests listés ont été **réellement
exécutés** (script `tests_lot06.js`). Un défaut réel a été détecté par la
suite (lien inter-dossiers vers la séquence station) et corrigé avant livraison ;
la suite complète a été rejouée après correction.

## Séquence (13 tests)

| Test | Résultat |
|---|---|
| Chargement sans erreur JS | ✅ |
| Rappel d'hypothèse affiché | ✅ |
| Act. 1 élaboration (5 blocs + 4 natures + 2 intrus) : 11/11 | ✅ |
| **Verrou expérientiel** : refus de valider sans l'essai insuffisant | ✅ |
| Simulateur : 20 Ah → ❌ 40 h · 40 Ah → ✅ 72 h tenus | ✅ |
| Act. 2 validée (432 Wh, 36 Ah, choix 40 Ah + 2 essais réels) | ✅ |
| Act. 3 contraintes du site : 5/5 | ✅ |
| Act. 4 matériaux/procédés (8 choix + justification à 2 contraintes) | ✅ |
| Act. 5 réinvestissement borne du stade | ✅ |
| Progression 5/5 + coches des 2 séances | ✅ |
| Reprise après rechargement (réponses, validations, essais __exp) | ✅ |
| Zéro lien local cassé (défaut détecté puis corrigé, suite rejouée) | ✅ |
| Zéro erreur JS après l'ensemble des interactions | ✅ |

## QCM (5 tests)

| Test | Résultat |
|---|---|
| Chargement sans erreur JS · 30 questions | ✅ |
| Bonnes réponses réparties A/B/C/D = 8/8/7/7 | ✅ |
| 3 questions illustrées, SVG présents sur le disque | ✅ |
| Parcours 30/30 → 20,0/20 · bilan par 2 codes | ✅ |
| Zéro erreur JS après le scénario complet | ✅ |

## Synthèses (2) et index (3)

Synthèses élève/professeur : chargement sans erreur, schémas présents ✅.
Index : badge NEW sur 3e_C4.1 + compétence C4, ancre auto-ouverte/ciblée,
pointeur 3e_C4.2 badgé ✅.

## Limites connues

- Google Fonts inaccessible dans le bac à sable (polices de repli, sans incidence).
- Version 🅰 (panneau + batterie + multimètre réels) non testable en sandbox :
  annoncée comme option, très basse tension uniquement.

## Complément (v2, demande Pascal)

Activité bonus « Loi d'Ohm » ajoutée (I = P÷U, U = R×I, choix du fusible —
hors barre de progression) et correctif d'affichage du bouton QCM du bilan
(débordement multi-lignes, corrigé aussi sur les séquences 5e au même gabarit).
Tests rejoués : bonus validé 3/3, progression inchangée (5 activités), zéro
erreur JS, display:block confirmé sur le bouton.
