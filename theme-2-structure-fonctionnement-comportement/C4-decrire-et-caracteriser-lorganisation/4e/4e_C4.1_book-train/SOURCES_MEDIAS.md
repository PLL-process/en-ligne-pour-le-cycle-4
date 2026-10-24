# Sources des médias — Lot 4e_C4.1 · C4.2 · C4.4 « Un Book Train pour la Schœlcher »

Tous les médias de ce lot sont des **productions du lot** (règle images v2 : chaque image est un document
à lire, jamais une décoration). Aucune image de manuel, aucune image issue d'une recherche en ligne,
aucun hotlinking.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/chaine_energie_book-train.svg` | SVG original (draw.io, production du lot) | image-objet : le diagramme fonctionnel de la chaîne d'énergie en quatre blocs — ALIMENTER, DISTRIBUER, CONVERTIR, TRANSMETTRE — dont les flèches portent les quatre visages de l'énergie (act. 2.1, QCM q. illustrées C4.2) | CC0 | ~16 Ko |
| `Images/chaine_information_book-train.svg` | SVG original (draw.io, production du lot) | image-objet : le diagramme fonctionnel de la chaîne d'information — ACQUÉRIR, TRAITER, COMMUNIQUER — avec la flèche d'ordre qui descend vers la chaîne d'énergie (act. 1.2, QCM q. illustrées C4.4) | CC0 | ~15 Ko |
| `fichiers_drawio/chaine_energie_book-train.drawio` | Source draw.io | fichier modifiable du diagramme d'énergie — l'enseignant peut l'adapter à un autre système | CC0 | ~5 Ko |
| `fichiers_drawio/chaine_energie_a_completer.drawio` | Source draw.io | version à trous distribuée aux élèves | CC0 | ~8 Ko |
| `fichiers_drawio/chaine_information_a_completer.drawio` | Source draw.io | version à trous de la chaîne d'information (act. 2.3 : ajouter les capteurs) | CC0 | ~5 Ko |
| `fichiers_drawio/chaine_information_correction.drawio` | Source draw.io | corrigé enseignant de l'act. 2.3 | CC0 | ~5 Ko |
| `fichiers_drawio/bibliotheque_chaines_book-train.xml` | Bibliothèque de formes draw.io, écrite par `_outils/generer_bibliotheque_chaines.py` | 34 formes des chaînes d'information et d'énergie (fonctions, composant dessous, formes d'énergie, fonction absente, flèche d'ordre), réutilisables pour tout autre système étudié | CC0 | ~26 Ko |
| `fichiers_drawio/schema_ensemble_book-train.jpg` | Image d'étude | schéma en coupe du parcours (tunnel, montée verticale, stations) — **généré avec une IA à partir de sources documentaires, puis vérifié et corrigé par l'enseignant** | production du lot | ~249 Ko |

## Deux points d'honnêteté

**Le schéma d'ensemble est assumé comme tel.** Il a été produit avec l'aide d'une IA puis relu et corrigé par
l'enseignant, et la page le dit sous la figure. Mieux : la séquence en fait un objet d'apprentissage. Trois
points y restent volontairement à préciser — l'énergie qui entre dans ALIMENTER, le trajet exact des ordres,
les retours d'information — et ce sont les élèves qui les précisent au fil des activités. « L'IA propose, on
audite » est ici une compétence travaillée, pas une excuse.

**Le système décrit est réel.** Le Book Train dessert les Milstein Stacks de la New York Public Library, sous
Bryant Park. Relu le 24/10/2026 contre le [communiqué de la bibliothèque du 21/09/2016](https://www.nypl.org/press/press-release/september-21-2016/new-york-public-library-installs-new-state-art-conveyor) :
24 wagonnets de 30 lb (13,6 kg), 950 pieds de rail (≈ 290 m), 75 pieds par minute, environ 5 minutes et 375 pieds
(11 niveaux) des réserves à la salle de lecture, 24 V continu, deux points de livraison, 2,6 millions de dollars.
**Le 480 V alternatif n'y figure pas** : la séquence le présente comme la tension habituelle des grands bâtiments
américains, et non comme une donnée publiée. La nacelle qui pivote pour rester horizontale et l'espacement entre
wagonnets viennent de la presse technique de l'époque (Hackaday, 05/10/2016) ; l'ancien système (fiches de
demande, convoyeur, monte-charge) du blog de la bibliothèque (21/12/2010), les tubes pneumatiques d'Atlas Obscura. La bibliothèque Schœlcher de Fort-de-France, dessinée par Pierre-Henri
Picq et présentée à Paris en 1889 avant d'être remontée en Martinique, est le commanditaire fictif de la
mission — le besoin est plausible, le projet ne l'est pas.

Les deux SVG portent `role="img"` avec `title` et `desc` complets : leur contenu est intégralement accessible
à un lecteur d'écran, y compris la description des flux entre les blocs.

## Correction des chaînes — 21/10/2026

`Images/chaine_energie_book-train.svg` : schéma fonctionnel corrigé, production originale CC0. Fonctions dans les blocs, composants en dessous, formes d’énergie sur les flèches ; « Énergie chimique stockée » sous les batteries. Les descriptions accessibles suivent le dessin.

Génération déterministe : `python _outils/regenerer_chaines_energie.py` depuis la racine. Source draw.io modifiable dans `_generation/chaines_energie/` (Book Train : `fichiers_drawio/`). Le SVG contient aussi cette source et utilise des textes SVG natifs, sans ressource distante.

La figure incorporée dans la séquence, le SVG autonome, les fichiers draw.io complet et à compléter et les téléchargements incorporés dans `FICHIERS` sont synchronisés. Le modèle reste fonctionnel ; les tensions, le secours et la réalisation de l’entraînement se précisent d’après la documentation du système étudié.

## Vidéo et figure 5 — 24/10/2026

**Vidéo du Book Train (onglet Départ).** Ce n'est pas un média du dépôt : la page porte un **lien** vers YouTube
(`https://www.youtube.com/watch?v=4IOv1O6SULY`, Tech Insider, 29/09/2016, 1 min 44 s, vidéo relayée par la revue
Poets & Writers) et son QR code.
Rien n'est intégré ni téléchargé : la page reste lisible sans Internet, avec un repli écrit. Le bloc est posé par
`theme-3-…/C7-…/poser_ressource.py` depuis le registre `ressources_externes.json` (entrée `res-4e-C4-1-book-train`),
où sont notés ce qui a été vérifié et comment. **Licence lue le 24/10/2026** : licence YouTube standard (la
description dépliée ne porte aucune ligne « Licence », que YouTube n'affiche que pour une vidéo Creative Commons) ;
lien, QR code et intégration permis, téléchargement, découpage et réhébergement non. Le QR code est un SVG
produit localement par `segno`, sans service distant.

**Traduction de la vidéo (24/10/2026).** La vidéo a été regardée de bout en bout avec l'outil vidIQ branché par Pascal
(métadonnées YouTube et lecture image par image) : aucune voix, 18 phrases incrustées en anglais. Les sous-titres
automatiques de YouTube ne traduisent pas un texte écrit dans l'image : la page donne donc, sous le lien, chaque phrase
minutée avec sa traduction. La traduction est une production originale du lot (CC0) ; les phrases anglaises, une centaine
de mots au total, sont reprises en courte citation, à des fins d'enseignement, avec leur source, pour que l'élève
reconnaisse à l'écran ce qu'il lit en français.

**Figure 5 (chaîne d'information, incorporée dans la page).** Production originale CC0, retouchée à la main : le rappel
de la chaîne d'énergie dit « Alimenter (480 V ~ → 24 V ⎓) » au lieu de « 13,2 kV AC », comme la page et le fichier
`Images/chaine_information_book-train.svg` ; la légende passe à gauche, l'étiquette ORDRE ne la recouvre plus ; les
mots « signaux » et « décisions » ne sont plus cachés par les blocs. Les pointes de flèche ne changent pas.

**Figure 1 (schéma en coupe, incorporé dans la page).** Production originale CC0, retouchée à la main : le sous-sol
était peint après trois étiquettes (les toilettes du parc, le perron côté parc) et les cachait ; deux autres
(le perron monumental et ses lions) sortaient du cadre. Le fond du sous-sol est désormais peint en premier, les
étiquettes sont replacées sous ce qu'elles nomment ; « nacelle horizontale » et « comptoir de distribution » ne
chevauchent plus le rail ni le comptoir. Rien n'est ajouté au dessin.
