# Rapport de tests — 5e_C1.3–C1.4

Date : 25 juillet 2026

Branche : `codex/theme-1/conformite-5e-c1-3-c1-4`

## Séquence testée

`sequence_C1.3-C1.4_SI_gestion_donnees.html`

## Résultat

**23 contrôles sur 23 réussis** sur la version autonome reconstruite.

## Contrôles réellement exécutés

- chargement de la page sans dépendance `_assets` ;
- absence des six références cassées signalées par l’audit ;
- titre avec ancrage Chine et mission immédiatement lisible ;
- situation déclenchante, problématique et trois activités progressives ;
- productions attendues, aides, corrections, exemples et erreurs fréquentes ;
- deux blocs CRCN contenant chacun : compétence exacte, niveau visé, repère, action observable et trace ;
- présence de la phrase « utiliser un ordinateur n’est pas une compétence » ;
- lien vers le CSV local ;
- présence du fichier CSV et cohérence des colonnes ;
- deux SVG locaux accessibles ;
- un seul bouton QCM ;
- ordre `Bilan → QCM → Bonus → pied de page` ;
- sauvegarde locale des champs de réponse de la séquence ;
- affichage sans débordement horizontal à 320 px ;
- affichage sans débordement horizontal à 768 px ;
- affichage sans débordement horizontal à 1440 px ;
- génération d’un PDF A4 ;
- aucun appel obligatoire à une police, une image ou un script distant.

## Données contrôlées

Le fichier `donnees_velos_hangzhou_simulees.csv` contient uniquement des données inventées pour l’apprentissage. Aucune donnée personnelle n’est présente.

## Contrôles non déclarés comme réussis

- ouverture du CSV dans Excel sur Windows ;
- ouverture du CSV dans LibreOffice Calc sur les postes du collège ;
- essai tactile sur appareil physique ;
- impression sur imprimante physique ;
- validation des liens après publication sur GitHub Pages ;
- tests du QCM modernisé, qui sera traité séparément dans ce lot avant passage en revue.

## Conclusion provisoire

La nouvelle séquence et ses ressources locales sont conformes. Le lot reste en cours tant que le QCM commun, les synthèses, le manifeste et les fichiers d’intégration ne sont pas tous contrôlés.
