# Rapport de tests — lot 5e_C1.2

Date de validation : 25 juillet 2026

Branche : `codex/theme-1/finaliser-5e-c1-2`

## Résultat global

- QCM : **44 contrôles fonctionnels sur 44 réussis dans Chromium headless**.
- Nouvelle activité CRCN : **16 contrôles sur 16 réussis après correction du débordement mobile**.
- Jeu CSV : **3 lignes de données, 8 colonnes, structure décodée sans erreur**.

Le QCM testé correspond au blob GitHub `e379d30dc93b50d36b3d6c99d56d2e1d25531c16`. L’activité CRCN et le CSV ont été reconstruits localement avec le contenu exact envoyé sur la branche, puis contrôlés avant et après correction.

## Contrôles statiques de la séquence

- titre avec emoji et mission immédiatement lisible ;
- situation déclenchante à Sainte-Luce et problématique présentes ;
- trois activités distinctes et progressives ;
- productions attendues, aides, corrections, exemples et erreurs fréquentes ;
- bilan placé avant les blocs de fin ;
- un seul bouton « Ouvrir le QCM d’entraînement » ;
- ordre conforme `Bilan → QCM → Bonus → pied de page` ;
- deux SVG locaux avec textes alternatifs ;
- liens relatifs vers les images, le QCM et les synthèses vérifiés statiquement.

## Contrôles du QCM réellement exécutés dans Chromium

### Structure et chargement

- chargement sans erreur JavaScript ;
- banque de 24 questions ;
- quatre champs d’identité ;
- sept compteurs permanents ;
- cinq modes visibles : parcours complet, 10 questions, révision ciblée, erreurs et questions marquées ;
- grille de 24 boutons de navigation ;
- barre de progression ARIA initialisée à 0 ;
- corrections détaillées contenant explication, exemple, erreur fréquente et « À retenir ».

### Scénarios de notation

- **tout juste** : 24/24, note affichée `20.0 /20` ;
- **tout faux** : 0/24, note affichée `0.0 /20` ;
- **mixte connu** : 12/24, note affichée `10.0 /20` ;
- compteurs corrects dans les trois scénarios ;
- bilan final par notion généré sans erreur.

### Sauvegarde et reprise

- identité enregistrée et restaurée ;
- réponse validée restaurée ;
- question marquée restaurée ;
- reprise du code applicatif validée avec un stockage local simulé par le banc d’essai.

La politique de sécurité du conteneur interdit toute navigation Chromium vers `file://`, `localhost` ou une origine interceptée (`ERR_BLOCKED_BY_ADMINISTRATOR`). Le banc a donc exécuté la page avec `page.set_content()` et une implémentation compatible de `localStorage`. Cette limite valide la logique de sérialisation et de reprise, mais ne remplace pas un essai manuel du stockage natif dans Edge après publication.

### Minuteur, clavier, responsive et impression

- démarrage, pause et reprise du minuteur ;
- modes 10 questions, révision ciblée, erreurs et marquées ;
- saisie de l’identité, sélection et validation au clavier ;
- focus visible et absence d’erreur JavaScript ;
- aucun débordement horizontal à 320, 768 et 1440 px ;
- commandes masquées en média d’impression ;
- PDF A4 généré avec succès.

## Activité CRCN originale ajoutée

Fichiers contrôlés :

- `activite_crcn_donnees_freinage_5e_C1.2.html` ;
- `donnees_simulees_freinage_5e_C1.2.csv`.

### Vérification de la règle d’or n°7

Les cinq informations obligatoires sont présentes et visibles :

1. compétence exacte : `CRCN 1.3 — Traiter des données` ;
2. niveau visé : niveau 2 ;
3. repère pour enseigner verbatim ;
4. action observable ;
5. trace produite.

Le principe « utiliser un ordinateur n’est pas une compétence » est présent. Le CRCN repose sur des actions vérifiables : enregistrement au format tableur, insertion d’une colonne, saisie, tri, filtre et production d’un PDF argumenté.

### Premier passage Chromium

Résultat : **15/16**. Un débordement horizontal de 17 px a été détecté à 320 px, provoqué par le nom long du fichier de trace.

Correction appliquée : ajout de règles CSS d’enveloppement et de césure sur les éléments `code`, les listes et les cartes.

### Second passage Chromium

Résultat : **16/16** :

- titre correct ;
- cinq preuves CRCN présentes ;
- avertissement anti-CRCN décoratif présent ;
- lien relatif vers le CSV correct ;
- CSV présent ;
- tableau et correction dépliable présents ;
- aucun débordement à 320, 768 et 1440 px ;
- PDF A4 généré, 3 pages, 91 806 octets ;
- aucune erreur console.

### Validation du CSV

- séparateur : point-virgule ;
- 8 descripteurs ;
- 3 solutions ;
- toutes les lignes possèdent 8 valeurs ;
- valeurs et scénario signalés comme entièrement simulés ;
- aucune donnée personnelle.

## Contrôle du périmètre GitHub

Les **onze fichiers** actuellement modifiés appartiennent exclusivement au dossier :

`theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.2/`

Aucun contenu des Thèmes 2 et 3, aucun fichier de `.github/` et aucun script de `_outils/` n’est modifié.

Une nouvelle exécution de la garde de périmètre est attendue automatiquement sur le commit final.

## Contrôles volontairement non déclarés comme réussis

- essai tactile sur appareil physique ;
- essai du stockage local natif dans Edge ou Firefox sur une origine normale ;
- ouverture réelle du CSV dans LibreOffice Calc et Excel ;
- impression sur imprimante physique ;
- validation des liens sur GitHub Pages après fusion dans `main`.

## Conclusion

Le paquet `5e_C1.2` respecte désormais la règle d’or CRCN observable, tracé et justifié. Il pourra être déclaré prêt pour revue après synchronisation finale du manifeste, du journal et réussite de la garde de périmètre.
