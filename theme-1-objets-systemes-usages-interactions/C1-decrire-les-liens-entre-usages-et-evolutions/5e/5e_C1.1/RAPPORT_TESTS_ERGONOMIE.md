# Rapport de tests — ergonomie 5e_C1.1

Date d’exécution : 24/07/2026
Branche : `codex/theme-1/5e-c1-1-ergonomie-v3`
Fichier testé : `sequence_5e_C1.1_donnees_tableur_2026.html`

## Contrôle statique réellement exécuté

Analyse du document avec BeautifulSoup :

- un seul `h1` : réussi ;
- une mission d’ouverture : réussi ;
- trois activités principales : réussi ;
- un seul bloc « 🧠 Prêt·e à t’entraîner ? » : réussi ;
- un seul bouton « 🚀 Ouvrir le QCM d’entraînement » : réussi ;
- un bloc Bonus hors parcours avec trois défis : réussi ;
- quatre images avec un texte alternatif non vide : réussi ;
- ordre final Bilan → QCM → Bonus : réussi.

## Tests navigateur réellement exécutés

Moteur : Chromium système piloté avec Playwright Python.
Le contenu HTML a été chargé avec `page.set_content()` ; le chargement réseau des médias et des liens relatifs n’a donc pas été testé.

### Bureau — 1440 × 900

- page chargée sans erreur JavaScript : réussi ;
- bouton QCM unique, visible et accessible au focus : réussi ;
- trois couleurs d’activité distinctes : réussi ;
- aucun débordement horizontal : réussi ;
- ordre final Bilan → QCM → Bonus : réussi.

### Mobile — 390 × 844

Un débordement horizontal causé par l’URL Pronote et les noms de fichiers a été détecté lors du premier passage. La règle CSS `overflow-wrap:anywhere` a été ajoutée, puis le test a été relancé.

Après correction :

- page chargée sans erreur JavaScript : réussi ;
- bouton QCM unique, visible et accessible au focus : réussi ;
- trois couleurs d’activité distinctes : réussi ;
- aucun débordement horizontal : réussi ;
- ordre final Bilan → QCM → Bonus : réussi.

## Contrôles non déclarés réussis

- chargement réel des quatre SVG depuis GitHub Pages ;
- ouverture effective du QCM et de la synthèse ;
- impression physique ;
- test tactile sur appareil réel ;
- exécution des générateurs partagés sur la branche finale.
