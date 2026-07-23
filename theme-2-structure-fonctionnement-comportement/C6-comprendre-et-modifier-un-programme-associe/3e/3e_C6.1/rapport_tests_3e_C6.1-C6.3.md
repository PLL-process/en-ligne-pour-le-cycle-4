# Rapport de tests — Thème 2 · LOT 04 « Programmer l'alerte » (3e_C6.1 + C6.3)

Date : 2026-07-23 · Agent : Fable (Thème 2) · Chromium headless (Playwright), viewport téléphone 390×844.

## 1. Tests automatisés — 22/22 réussis

### CodeLab Techno (composant commun, première implémentation)
| Test | Résultat |
|---|---|
| Programme initial chargé (24 lignes, compteur exact) | ✅ |
| Coloration syntaxique Python active | ✅ |
| Surlignage de lignes piloté par les consignes (6-7) | ✅ |
| A+ change la taille de police | ✅ |
| Comparaison : 1 ligne modifiée détectée après édition | ✅ |
| Sauvegarde/reprise : le code de l'élève (v2) est restauré après rechargement | ✅ |

### Séquence
| Test | Résultat |
|---|---|
| Chargement sans erreur JS | ✅ |
| Activité 1 (entrées/sorties + lignes) : 8/8 | ✅ |
| Activité 3 : le vérificateur contrôle le CODE RÉEL (SEUIL_ORANGE = 60 exigé dans l'éditeur) | ✅ |
| Activité 4 incomplète → message listant précisément les ajouts manquants | ✅ |
| Activité 4 complète (v2 avec gyrophare) : 7/7 contrôles de code passés | ✅ |
| Activité 5 (plan de tests) : 7/7 | ✅ |
| Reprise des réponses · zéro lien cassé · zéro erreur JS après interactions | ✅ |

### QCM et tableau de bord
| Test | Résultat |
|---|---|
| 30 questions (15/15) · 6 illustrées, images présentes · zéro erreur JS | ✅ |
| Scénario 30/30 → note exacte 20,0/20 · bilan 2 compétences | ✅ |
| Badge NEW sur 3e_C6.1 et compétence C6 · ancre #3e_C6.1 fonctionnelle | ✅ |
| **3e_C6.2 existant : listé, intact, SANS badge** (aucune modification) | ✅ |

## 2. Contrôles statiques
`node --check` OK (séquence + QCM) · 3 SVG de 5-6 Ko · matrice : 30/30 questions rattachées, aucune manquante · programme Python original (aucune exécution requise, fonctions fictives explicites) · aucun secret, aucune donnée envoyée.

## 3. Conformité règles du dépôt
Images v2 : 3 SVG image-objet, 6 questions illustrées, zéro décoratif. En-tête QCM standard. A/B/C : encadré présent (matériel confirmé uniquement). CodeLab conforme à la spécification du prompt maître (fonctions obligatoires implémentées ; console d'exécution volontairement absente : non indispensable, prévue comme amélioration éventuelle).

## 4. Contrôles restant manuels
Version 🅰 sur maquette réelle ; import de fichier .py (testé unitairement via FileReader, à confirmer sur appareil réel) ; mode plein écran sur iOS (API fullscreen limitée : le bouton reste sans effet sur iPhone — comportement dégradé acceptable) ; relecture humaine ; GitHub Pages après fusion.

## 5. Échecs
Aucun test exécuté en échec au moment de la remise.
