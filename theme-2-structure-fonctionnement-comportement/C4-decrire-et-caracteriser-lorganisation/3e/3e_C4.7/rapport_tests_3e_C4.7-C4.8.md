# Rapport de tests — Thème 2 · LOT 02 « Internet jusqu'à Sainte-Luce » (3e_C4.7 → C4.8)

Date : 2026-07-22 · Agent : Fable (Thème 2) · Environnement : Chromium headless (Playwright), viewport téléphone 390×844 + vérifications scriptées Python/Node.

## 1. Tests automatisés — 24/24 réussis

### Séquence (`sequence_3e_C4.7-C4.8_internet_sainte_luce.html`)

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS (hors police externe facultative) | ✅ |
| Activité 1 : 6 réponses justes → feedback « ok » | ✅ |
| Simulateur de paquets : découpage en 3 paquets, remise en ordre, réassemblage | ✅ |
| Activité 3 : verrou d'expérience (le simulateur doit avoir été utilisé) + 3 réponses | ✅ |
| Simulateur de panne : chemin initial le plus court R1→R3→R5 | ✅ |
| Re-routage automatique après coupure de R3-R5 (chemin par R4) | ✅ |
| Isolement de R5 (R3-R5 + R4-R5 coupées) → « livraison impossible » | ✅ |
| Sauvegarde/reprise : réponses ET liaisons coupées restaurées après rechargement | ✅ |
| Zéro lien local cassé (SVG, QCM) | ✅ |

### QCM (`qcm_3e_C4.7-C4.8_internet_sainte_luce.html`)

| Test | Résultat |
|---|---|
| Chargement sans erreur JS · grille de 30 questions · 2 compétences au bilan | ✅ |
| Scénario complet 30/30 correctes → note exacte 20,0/20 | ✅ |
| Bilan par compétence : 2 lignes (C4.7, C4.8) | ✅ |
| Moteur identique au LOT 01, déjà éprouvé (minuteur, modes, filtres, reprise, réessayer ; scénarios de notes 20,0 · 10,0 · 5,0/20 vérifiés au LOT 01) | ✅ |

### Tableau de bord (`index.html` régénéré, `nouveautes.json` unifié)

| Test | Résultat |
|---|---|
| Badge NEW sur `3e_C4.7` ET sur `4e_C7.1` (entrée du Thème 3 préservée après unification) | ✅ |
| Badges NEW simultanés sur le thème 2 et le thème 3 | ✅ |
| Ancre `index.html#3e_C4.7` : ouvre C4, cible la ligne | ✅ |
| Zéro erreur JS | ✅ |

## 2. Contrôles statiques

- `node --check` sur les scripts extraits (séquence, QCM, index) → OK.
- Poids des médias : 4 SVG originaux de 5 à 7 Ko (seuil 300 Ko).
- Matrice de couverture : les 30 questions rattachées à une notion enseignée (vérification scriptée 1-30, aucune manquante) ; aucune question hors séquence.
- Adresses IP des exemples : plages réservées à la documentation (192.168/198.51.100/203.0.113/172.16).
- Aucun secret, aucune donnée envoyée (localStorage uniquement, hors connexion après chargement).

## 3. Accessibilité

Navigation clavier (liaisons du simulateur focusables : `tabindex` + Entrée/Espace, `role=button`, `aria-label`), skip-link, `aria-live` sur les résultats, alt/desc sur tous les SVG, `prefers-reduced-motion`, impression A4, minuteur désactivable.

## 4. Anomalie détectée ET corrigée par les tests

La correction de l'activité 5 annonçait un chemin initial erroné (R1→R2→R4→R5) ; le simulateur calcule le vrai plus court chemin (R1→R3→R5). **Texte pédagogique corrigé** avant remise — exemple concret de l'intérêt des tests bloquants.

## 5. Contrôles restant manuels

Appareils réels iOS/Android ; séance Filius version A au labo ; comptes Packet Tracer (version B) **À CONFIRMER** ; relecture orthotypographique humaine ; vérification GitHub Pages après fusion.

## 6. Échecs

Aucun test exécuté en échec au moment de la remise.
