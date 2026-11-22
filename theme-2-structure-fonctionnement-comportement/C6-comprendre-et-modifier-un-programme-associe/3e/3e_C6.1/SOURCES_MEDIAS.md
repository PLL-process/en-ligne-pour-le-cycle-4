# Sources des médias — Lot 3e_C6.1 + C6.3 « Programmer l'alerte »

Tous les médias sont des **créations originales** (règle images v2 : image-objet).
Aucune image de manuel, de Google Images ou de site tiers ; aucun hotlinking.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/programme_entrees_sorties.svg` | SVG original (Fable) | image-objet : entrées/sorties à identifier (act. 1, QCM) — mots corrigés le 22/11/2026 (audit) : mesure, paramètre, état, décision ; le message est « Vigilance violette » comme dans le programme (il disait « ALERTE… ») ; `True` (il disait « vrai ») ; l'extrait de code en Python | CC0 | ~7 Ko |
| `Images/programme_entrees_sorties_muet.svg` | SVG original (Fable) | image-objet : entrées/sorties à identifier (act. 1, QCM) | CC0 | version **muette** de `programme_entrees_sorties.svg` (les six données en « ? »), affichée avec les questions de l'activité 1 — règle d'or n°331, 15/11/2026 ; la version complète est dans la correction |
| `Images/algorigramme_alerte_graduee.svg` | SVG original (Fable) | image-objet : LA spécification de la **version 2** à implémenter (act. 4, QCM) — redessinée le 22/11/2026 (audit) : seuil orange **60** (il testait encore 50), états exacts du programme (« verte », plus « verte/jaune »), lecture et envoi en parallélogrammes (n°348), textes à 12 px au moins | CC0 | ~9 Ko |
| `Images/plan_de_tests_jeux_essai.svg` | SVG original (Fable) | image-objet : plan de tests à lire, bug à diagnostiquer (act. 5, QCM) — refait le 22/11/2026 (audit) : un plan **authentique de la version 1 d'origine** (seuils 50 · 90 · 118, aucun gyrophare), six essais 49/50/51/117/118/119, essayé sur une copie fautive nommée « copie B » (`>=` à 118). Avant, il annonçait « orange + gyrophare » à 51 pour une v1 qui n'a pas de gyrophare | CC0 | ~9 Ko |
| `Images/plan_de_tests_jeux_essai_muet.svg` | SVG original (Fable) | image-objet : plan de tests à analyser (act. 5) | CC0 | version **muette** de `plan_de_tests_jeux_essai.svg` (l'encart ne dit plus pourquoi ces valeurs ni la cause du bug : il pose les deux questions), affichée avec les questions de l'activité 5 ; la version complète est dans sa correction (règle d'or n°331, 15/11/2026) ; refaite avec elle le 22/11/2026 · ~9 Ko |

Le code source affiché (programme v1/v2, programme de la bouée) est une création
originale du lot, en Python réel, avec fonctions fictives explicites
(lire_capteur, envoyer, activer_*). Alt/desc dans chaque SVG ; symboles
d'algorigramme conformes à ceux de
`_ressources-communes/Images/Ressources transversales/algorigramme-symbole-*.svg`.

## Image reprise d'un lot voisin pour la situation déclenchante (05/11/2026)

Copie, octet pour octet, de `theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation/3e/3e_C4.3/Images/synthese_station_alerte.png` (même provenance, mêmes droits) : elle montre le même objet, sans donner la réponse de la séquence. Demande de Pascal du 05/11/2026 : « il manque aussi des images réalistes ».

| Fichier | Ce qu'elle montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/synthese_station_alerte.png` | La station d'alerte cyclonique sur le toit d'un collège : mât, anémomètre, girouette, panneau solaire, sirène, gyrophare, boîtier ; la mer au loin. PNG 1 536 × 1 024, 2.0 Mo. | **Image générée par IA** avec Canva (génération d'image), compte de Pascal, 29/10/2026. Demande : « Realistic photo of a small autonomous cyclone warning station on a galvanized steel mast on the flat roof of a school in Martinique: cup anemometer and wind vane at the top, a small solar panel on a side arm, a white weatherproof electronics box, a horn siren and a small orange beacon light mounted on the mast, a short radio antenna, the sea in the distance, cloudy sky, no people, no text, no logos, the whole mast visible » | Conditions Canva AI Product Terms : l'image appartient à Pascal, sans attribution exigée ; interdit de la présenter comme faite par un humain (légende « Image générée par IA (Canva) ») et d'en retirer les métadonnées de provenance (manifeste C2PA et XMP Canva gardés : **fichier non modifié**, d'où son poids). | Séquence, situation déclenchante (05/11/2026) |

## Poids de l'image de la situation (audit du 21/11/2026 ; décision du 22/11/2026)

L'audit proposait une variante légère de `synthese_station_alerte.png` (2 022 508 octets).

**Décision du 22/11/2026** (carte blanche de Pascal) : **on garde le fichier d'origine, non modifié.**
- Les conditions Canva AI rappelées ci-dessus interdisent d'en retirer les métadonnées de provenance (C2PA, XMP), et
  un redimensionnement fait hors de Canva les retire. La seule version légère permise est un nouvel export depuis
  Canva. Il a été fait le 22/11/2026 (création `DAHaEhWWmSY`, JPG, 1 536 px de large, qualité 82), mais le serveur
  d'export de Canva est hors de la liste des sites que l'atelier de Claude peut joindre : le fichier n'a pas pu entrer
  dans le dépôt.
- Le dépôt garde ce poids une seule fois : les huit copies de l'image (3e_C4.3, 3e_C4.7, 3e_C5.1, 3e_C6.1, 3e_C6.2,
  3e_C7.4, 3e_C7.5, 3e_C7.8) sont identiques octet pour octet, et git ne stocke qu'un seul objet pour un même contenu.
- Dans les six séquences, l'image est chargée en différé (`loading="lazy"`) ; les cinq synthèses, faites pour
  l'impression, la chargent tout de suite, pour qu'elle soit sur la feuille. Sa légende dit « Image générée par IA (Canva) : ce n'est pas
  une photographie ».
- À reprendre si une page met trop longtemps à s'ouvrir en classe : exporter la création depuis Canva en JPG
  (1 536 px, qualité 80), puis remplacer les huit copies et leurs liens dans le même commit.
