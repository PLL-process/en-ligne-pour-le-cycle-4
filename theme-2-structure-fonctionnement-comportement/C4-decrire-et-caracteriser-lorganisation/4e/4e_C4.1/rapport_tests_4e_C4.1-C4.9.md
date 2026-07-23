# Rapport de tests — Lot 4e_C4.1 → C4.9 « Le jardin connecté »

**Environnement réel d'exécution** : Chromium (Playwright), viewport mobile 390×844,
pages en `file://` (hors ligne — polices distantes filtrées comme attendu).
Suite : `tests_lot09.js` — 21 tests, **tous réellement exécutés** le 24/07/2026.

**Résultat : 21 / 21 réussis · aucune erreur JavaScript sur les deux pages.**

## Séquence (15 tests)

| # | Test | Résultat |
|---|---|---|
| 1 | Titre + sous-titre en tête (règle d'or n°4 §1) | ✅ |
| 2 | 4 onglets de séances, bascule fonctionnelle | ✅ |
| 3 | Act. 1 (énergie) : 9/9 | ✅ |
| 4 | Act. 2 (chaîne d'information) : 4/4 | ✅ |
| 5 | Explorateur de table : 3 bacs filtrés → verrou `__exp.table` | ✅ |
| 6 | Act. 3 (données) : 6/6 avec verrou actif | ✅ |
| 7 | Simulateur réseau : mauvais diagnostic → refus explicite | ✅ |
| 8 | Simulateur réseau : 3 pannes résolues → verrou `__exp.reseau` | ✅ |
| 9 | Act. 4 (réseau) : 4/4 avec verrou | ✅ |
| 10 | Act. 5 (forme/procédé) : 6/6 | ✅ |
| 11 | Progression 5/5 activités | ✅ |
| 12 | Sauvegarde localStorage + rechargement : état restauré, verrous compris | ✅ |
| 13 | Blocs règle n°4 (Prêt·e / Bonus) après le bilan, avant le pied de page | ✅ |
| 14 | Liens internes valides (y compris vers les ressources existantes C4.7 et C6.2) | ✅ |
| 15 | Bouton QCM du bilan sans débordement (correctif gabarit hérité) | ✅ |

## QCM (6 tests)

| # | Test | Résultat |
|---|---|---|
| 16 | Chargement, titre, 30 questions | ✅ |
| 17 | Familles : 7 EN + 10 ID + 10 RES + 3 PRO | ✅ |
| 18 | Répartition A/B/C/D = 7/7/8/8, `d[r]` vide partout | ✅ |
| 19 | 3 questions illustrées (fichiers présents) + qualité de banque (4 options, expl, ret, 3 distracteurs expliqués) | ✅ |
| 20 | Une partie se joue réellement | ✅ |
| 21 | Clé localStorage correcte + lien retour séquence | ✅ |

## Limites

Tests exécutés uniquement en Chromium/Playwright — aucune compatibilité non testée
n'est revendiquée. La version 🅰 (jardin réel) relève de l'enseignant.
