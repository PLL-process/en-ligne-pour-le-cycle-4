# Rapport de tests — Thème 2 · LOT 01 « Station d'alerte cyclonique » (3e_C4.3 → C4.6)

Date : 2026-07-22 · Agent : Fable (Thème 2) · Environnement : Chromium headless (Playwright), viewport téléphone 390×844 + vérifications scriptées Python/Node.

## 1. Tests automatisés exécutés — 40/40 réussis (suite principale) + 10/10 (scénarios de notes)

### Séquence (`sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html`)

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS (hors police externe facultative) | ✅ |
| Table de données : 48 enregistrements rendus | ✅ |
| Simulateur CAN : N(943 hPa) = 512 ± 1 | ✅ |
| Activité 1 : validation des 8 réponses justes + justification → feedback « ok » | ✅ |
| Progression 1/7 mise à jour puis **restaurée après rechargement** (localStorage) | ✅ |
| Onglets de séances fonctionnels | ✅ |
| Zéro lien local cassé (SVG, CSV/ODS/XLSX, QCM) — vérification `fs` + parcours `href/src/data` de tous les HTML | ✅ |
| Lien d'évitement (skip-link) accessible au clavier | ✅ |

### QCM (`qcm_3e_C4.3-C4.6_station_alerte_cyclonique.html`)

| Test | Résultat |
|---|---|
| Chargement sans erreur JS · grille de 32 questions | ✅ |
| Réponse correcte comptée · correction complète affichée (bonne réponse en toutes lettres, explication, exemple, erreur fréquente, distracteurs expliqués, « À retenir », encouragement) | ✅ |
| Minuteur : démarrage auto à la 1re validation, pause fige le temps, reprise, option « sans minuteur » | ✅ |
| Bouton « Réessayer » : question réinitialisée et compteurs exacts | ✅ |
| Réponse fausse comptée · marquage 🔖 « à revoir » | ✅ |
| « Prochaine non répondue » | ✅ |
| **Sauvegarde/reprise après fermeture** : réponses, erreurs, marquages restaurés | ✅ |
| Mode « uniquement mes erreurs » (1 question) · mode « 10 questions » | ✅ |
| Écran final : note /20, %, temps, bilan par compétence (4 lignes), notions maîtrisées/à revoir | ✅ |
| Question non répondue correctement comptée | ✅ |

### Scénarios de notes (calculés à la main, puis vérifiés en machine)

| Scénario | Attendu | Obtenu |
|---|---|---|
| S1 : 32/32 correctes | 32 pts · 20,0/20 · 100 % | ✅ identique |
| S2 : 16 correctes + 16 incorrectes | 16 pts · 10,0/20 · 50 % | ✅ identique |
| S3 : 8 correctes + 8 incorrectes + 16 non répondues | 8 pts · 5,0/20 · 25 % · 16 NR | ✅ identique |

### Tableau de bord (`index.html` régénéré + badge NEW)

| Test | Résultat |
|---|---|
| Badge NEW sur le code `3e_C4.3`, sur la compétence C4, sur le thème 2 | ✅ |
| Badge NEW sur les liens séquence/QCM nouveaux | ✅ |
| Aucun badge sur le thème 1 (non concerné) | ✅ |
| Ancre directe `index.html#3e_C4.3` : ouvre la compétence, défile jusqu'au code, met la ligne en évidence | ✅ |
| Zéro erreur JS | ✅ |

## 2. Contrôles statiques

- **Syntaxe JavaScript** : `node --check` sur les scripts extraits de la séquence, du QCM et de l'index → OK.
- **Liens locaux** : parcours automatique de tous les `href/src/data` des HTML du lot → aucun lien cassé.
- **Poids des médias** : 5 SVG originaux entre 5 et 7 Ko, données 3-7 Ko → très en dessous du seuil de 300 Ko.
- **Matrice de couverture** : les 32 questions du QCM sont rattachées à une notion enseignée ; aucune question hors séquence ; aucune notion essentielle sans question (vérification scriptée de l'ensemble 1-32).
- **Aucun secret, aucune donnée personnelle envoyée** : sauvegardes en localStorage uniquement, aucune requête sortante indispensable (la police Google est décorative avec repli système ; tout fonctionne hors connexion après chargement).

## 3. Accessibilité et confort

- Navigation clavier (skip-link testé, focus visibles), `aria-label`/`role`/`aria-live` posés, `<title>/<desc>` dans chaque SVG.
- `prefers-reduced-motion` respecté (badge NEW, défilements, transitions).
- Contrastes de la palette commune du projet ; l'information ne repose jamais sur la seule couleur (étiquettes textuelles).
- Impression A4 : styles dédiés séquence, synthèse élève (1 page) et QCM.
- Minuteur désactivable (travail sans contrainte de temps).

## 4. Contrôles restant manuels (non exécutés — à faire par un humain)

- Test sur appareils réels (iOS/Android, tablette) — seul le viewport mobile a été émulé ;
- test du montage **version A** (Arduino UNO/R4 + Grove luminosité + LCD) au labo : compatibilité bibliothèque LCD ↔ UNO R4 Minima **À CONFIRMER — prévoir l'alternative VittaScience** ;
- relecture orthotypographique humaine ;
- vérification du rendu GitHub Pages après publication (ancre + badge sur l'URL publique).

## 5. Échecs

Aucun test exécuté en échec au moment de la remise.
