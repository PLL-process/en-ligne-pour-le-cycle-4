# Rapport de tests — Thème 2 · LOT 03 « SOS station : réparer plutôt que jeter » (3e_C5.1 → C5.4)

Date : 2026-07-22 · Agent : Fable (Thème 2) · Chromium headless (Playwright), viewport téléphone 390×844 + contrôles scriptés.

## 1. Tests automatisés — 30/30 réussis

### Séquence
| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS | ✅ |
| Activité 1 (symptômes/hypothèses) : 7/7 → feedback « ok » | ✅ |
| Simulateur de dépannage : symptôme constaté, relevés T1→T4 affichés | ✅ |
| Mauvaise pièce remplacée → réfutation explicite (« cet élément était sain ») | ✅ |
| Panne 1 (câble) résolue → panne 2 activée automatiquement | ✅ |
| Panne 2 (fusible) localisée en 2 mesures et résolue | ✅ |
| Retest final : « sirène opérationnelle » | ✅ |
| Activité 4 : verrou pédagogique (2 pannes exigées) + 2 questions | ✅ |
| Activité 5 (plan coté) : 8/8 | ✅ |
| Sauvegarde/reprise : réponses ET état du simulateur persistés | ✅ |
| Zéro lien local cassé | ✅ |

### QCM (moteur étendu : images)
| Test | Résultat |
|---|---|
| 32 questions · 4 compétences au bilan · zéro erreur JS | ✅ |
| Question sans image : zone figure masquée | ✅ |
| Question illustrée : figure visible, image chargée, alt renseigné | ✅ |
| 10 questions illustrées, toutes les images existent sur disque | ✅ |
| Scénario 32/32 → note exacte 20,0/20 · bilan 4 lignes | ✅ |

### Tableau de bord
| Test | Résultat |
|---|---|
| Badge NEW sur `3e_C5.1` et sur la compétence C5 | ✅ |
| Ancre `#3e_C5.1` : ouvre C5, cible la ligne | ✅ |

## 2. Contrôles statiques
`node --check` OK (séquence, QCM) · 5 SVG de 5-6 Ko (seuil 300 Ko) · matrice : 32/32 questions rattachées, aucune manquante · valeurs électriques cohérentes (TBT 12 V) · aucun secret, aucune donnée envoyée.

## 3. Conformité règle images v2
Chaque image répond OUI au critère de contrôle : les 5 SVG sont des documents à LIRE (constats, arbre, points de test, plan coté, comparatif) ; 10 questions illustrées sur 32 ; aucune image décorative.

## 4. Contrôles restant manuels
Appareils réels ; atelier version 🅰 (multimètres **MATÉRIEL À CONFIRMER**) ; impression 3D (**À CONFIRMER**) ; relecture humaine ; GitHub Pages après fusion (ajuster `date_publication` si fusion après le 22/07).

## 5. Échecs
Aucun test exécuté en échec au moment de la remise.
