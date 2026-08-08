# Sources des médias — 3e_C6.2 « L'auto-test de la station »

**Règle d'or n°1 du dépôt** : chaque image est un document à lire, produite pour le dépôt,
sous licence libre, avec `<title>` et `<desc>` accessibles. Aucune capture de logiciel
propriétaire, aucune image trouvée sur un moteur de recherche, aucun hotlinking.

## Les trois figures de ce lot

| Fichier | Nature | Auteur | Licence | Rôle pédagogique |
|---|---|---|---|---|
| `Images/algorigramme_auto_test.svg` | SVG original, écrit à la main | Fable (agent Thème 2), pour ce dépôt | CC0 1.0 (domaine public) | L'algorigramme complet de la fonctionnalité : compteur avant la boucle, boucle sur les quatre organes, décision unique après la boucle |
| `Images/symboles_algorigramme.svg` | SVG original, écrit à la main | Fable (agent Thème 2), pour ce dépôt | CC0 1.0 (domaine public) | La planche des cinq symboles normalisés et de ce que chacun promet (une flèche entre, deux sortent…) |
| `Images/trace_banc_essai.svg` | SVG original, écrit à la main | Fable (agent Thème 2), pour ce dépôt | CC0 1.0 (domaine public) | La trace d'une exécution ligne à ligne, avec le compteur qui ne redescend pas et le cas de la défaillance silencieuse |

Les trois fichiers sont du SVG écrit directement (pas d'export d'un logiciel), sans police
embarquée, sans image tramée incluse, sans référence réseau. Ils s'affichent hors ligne.

## Accessibilité des figures

Chaque SVG porte un `<title>` court et un `<desc>` long qui **décrit le contenu, pas
l'apparence** : un élève qui n'accède qu'au texte alternatif doit pouvoir répondre à la
question posée. Les trois descriptions font de 585 à 700 caractères. Dans le QCM, l'attribut
`alt` reprend la même information sous forme condensée.

Aucune information n'est portée par la seule couleur : les branches d'un losange sont
étiquetées en toutes lettres (« oui », « non »), et dans la trace les réponses sont écrites
« vrai » et « FAUX » en plus d'être colorées.

## Les fichiers hérités du dossier

`sequence_algorigrammes_dnb.html` et `qcm_algorigrammes_dnb.html` contiennent leurs propres
SVG **inline** (13 schémas), produits avec la banque d'entraînement DNB avant ce lot. Ils ne
sont pas modifiés ici : ils restent la propriété éditoriale de leur auteur d'origine et sont
référencés comme ressource d'appui. Aucun de leurs médias n'a été copié dans les figures
ci-dessus.

## Polices

`Poppins` et `Fira Code` sont appelées depuis Google Fonts par la séquence et le QCM, comme
dans tout le dépôt (SIL Open Font License 1.1). En l'absence de réseau, la page bascule sur
la police système : aucune information n'est perdue.

## Réemploi dans l'entraînement DNB

La page `entrainement_dnb_algorigrammes.html` réutilise les **trois mêmes SVG**, sans en produire
de nouveaux : la planche des symboles illustre l'exercice sur le losange et le rappel de cours,
l'algorigramme de l'auto-test illustre l'exercice sur l'initialisation du compteur, et la trace
d'exécution illustre celui sur le compteur qui ne redescend pas.

Un média produit une fois et lu trois fois vaut mieux que trois médias décoratifs.
