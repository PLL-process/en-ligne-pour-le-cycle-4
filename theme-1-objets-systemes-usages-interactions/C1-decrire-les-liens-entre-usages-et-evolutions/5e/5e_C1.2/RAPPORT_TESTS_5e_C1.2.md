# Rapport de tests — lot 5e_C1.2

Date de validation : 25 juillet 2026

Branche : `codex/theme-1/finaliser-5e-c1-2`

## Résultat global

**44 contrôles fonctionnels sur 44 réussis dans Chromium headless.**

Le fichier testé correspond au QCM présent dans la branche GitHub, blob `e379d30dc93b50d36b3d6c99d56d2e1d25531c16` au moment de la reconstruction du banc d’essai.

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

La politique de sécurité du conteneur interdit toute navigation Chromium vers `file://`, `localhost` ou une origine interceptée (`ERR_BLOCKED_BY_ADMINISTRATOR`). Le banc a donc exécuté la page avec `page.set_content()` et une implémentation compatible de `localStorage`. Cette limite est explicitement consignée : elle valide la logique de sérialisation et de reprise du QCM, mais ne remplace pas un essai manuel du stockage natif dans Edge après publication.

### Minuteur et modes

- démarrage du minuteur ;
- pause sans progression du temps ;
- reprise du minuteur ;
- mode 10 questions ;
- révision ciblée avec le nombre de questions attendu ;
- gestion correcte des modes « erreurs » et « marquées » lorsqu’aucune question n’est disponible.

### Clavier et accessibilité fonctionnelle

- saisie de l’identité au clavier ;
- sélection et validation d’une réponse avec la touche Entrée ;
- présence d’éléments focalisables dans les zones identité, minuteur, modes, navigation et question ;
- focus visible défini dans la feuille de style ;
- aucune erreur JavaScript pendant le parcours clavier.

### Responsive et impression

- aucune barre de défilement horizontale à 320 px ;
- aucune barre de défilement horizontale à 768 px ;
- aucune barre de défilement horizontale à 1440 px ;
- question visible dans les trois largeurs ;
- commandes masquées en média d’impression ;
- PDF A4 généré avec succès par Chromium.

## Contrôle du périmètre GitHub

Les neuf fichiers actuellement modifiés appartiennent exclusivement au dossier :

`theme-1-objets-systemes-usages-interactions/C1-decrire-les-liens-entre-usages-et-evolutions/5e/5e_C1.2/`

Aucun contenu des Thèmes 2 et 3, aucun fichier de `.github/` et aucun script de `_outils/` n’est modifié.

Le workflow GitHub **Garde-périmètre des thèmes** a déjà réussi sur un commit antérieur de cette branche. Une nouvelle exécution est attendue automatiquement sur le commit final.

## Contrôles volontairement non déclarés comme réussis

- essai tactile sur appareil physique ;
- essai du stockage local natif dans Edge ou Firefox sur une origine normale ;
- impression sur imprimante physique ;
- validation des liens sur GitHub Pages après fusion dans `main`.

Ces contrôles post-publication ne bloquent pas la revue du code : aucune affirmation de réussite n’est faite à leur sujet.

## Conclusion

Le paquet `5e_C1.2` est **prêt pour revue et fusion**, sous réserve de la garde de périmètre finale et de la fusion manuelle prévue par la gouvernance du dépôt.
