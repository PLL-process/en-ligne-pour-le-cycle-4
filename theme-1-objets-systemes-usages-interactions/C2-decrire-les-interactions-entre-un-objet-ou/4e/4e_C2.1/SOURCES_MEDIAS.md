# Sources des médias — lot Hangzhou 4e_C2.1 · C2.2

**Règle d'or n°1** : chaque image est un document à lire, produite pour le dépôt, sous licence
libre, avec `<title>` et `<desc>` accessibles.

| Fichier | Nature | Auteur | Licence | Rôle pédagogique |
|---|---|---|---|---|
| `Images/du_verbatim_a_l_algorigramme.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | Le trajet imposé par le référentiel — langage naturel, schéma, graphique, algorithme — chacun avec ce qu'il apporte **et ce qu'il ne sait pas dire** |
| `Images/six_familles_d_exigences.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | Les six familles d'exigences **dans les mots du programme**, la question que chacune pose, et ce qu'elle donne sur la borne |
| `Images/notice_climatiseur_extrait.svg` | SVG original, écrit par `_generation/figures_qcm_fonctionnement_objet.py` (18/11/2026) | Fable, pour ce dépôt | CC0 1.0 | Image-objet du QCM complémentaire : un extrait de notice inventé (touches et pictogrammes, procédure en trois étapes, deux avertissements) que l'élève **lit** pour répondre (questions 3, 4, 5 et 27). Aucune marque, aucun modèle réel. |
| `Images/algorigramme_minuterie_climatiseur.svg` | SVG original, écrit par `_generation/figures_qcm_fonctionnement_objet.py` (18/11/2026) | Fable, pour ce dépôt | CC0 1.0 | Image-objet du QCM complémentaire : la minuterie du climatiseur en algorigramme (test, boucle, sortie OUI), lue aux questions 13 et 14. |
| `Images/corrige_temps_par_etape.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | **Corrigé** du graphique de l'activité 2 : moyenne et pire cas par étape, les 9 reprises sur 30 rendues visibles, et les deux lectures nommées |

## Pourquoi trois figures, et pas deux

Les deux premières sont des **documents à lire**, placés dans le fil de la page. La troisième est un
**corrigé** : elle n'apparaît que dans la correction repliée de l'activité 2, jamais avant.

C'est l'application de la **règle d'or n°43** : toute production demandée a son corrigé, et ce
corrigé arrive **après**. Le graphique est ce que l'élève doit produire — le montrer d'abord
donnerait la réponse ; ne jamais le montrer laisserait sans recours l'élève qui travaille seul. Le
repli du `<details>` est ce qui rend les deux exigences compatibles.

Un graphique se corrige par un **graphique**, pas par une phrase qui le décrit : un élève ne peut
pas comparer son tracé à un paragraphe. Le nom du fichier porte le mot `corrige` pour qu'on ne
puisse pas le glisser par erreur dans le fil de la page.

## Les données

Toutes **simulées**, construites pour l'exercice. Elles ne décrivent aucun service réellement
exploité.

`verbatims_usagers_hangzhou_simules.csv` — 12 usagers, en langage naturel, avec profil, étape
concernée et ressenti dominant. Deux particularités assumées, toutes deux pédagogiques :

- **V03 et V09 se contredisent** sur la liste des vélos : Wang la trouve décourageante, Ma la trouve
  pratique. Ce n'est pas une incohérence à corriger, c'est le résultat que l'activité 1 doit faire
  écrire — un même objet ne produit pas la même expérience selon qui l'utilise.
- **Les douze profils sont variés à dessein** : habitué, première fois, personne âgée, parent avec
  enfant, livreur, touriste. Une enquête qui n'interroge que des habitués ne trouve jamais de
  problème.

`donnees_parcours_borne_hangzhou_simulees.csv` — 30 retraits × 5 étapes, durées en secondes, plus
une colonne `reprise_necessaire`. Les valeurs sont construites pour qu'un **résultat
contre-intuitif** apparaisse tout seul :

- l'étape la plus longue en **moyenne** est « choisir » (40 s), et **aucun verbatim ne s'en plaint** ;
- l'étape dont parlent **trois verbatims sur douze** est « déverrouiller » (29 s de moyenne
  seulement), mais elle monte à **83 s** pour les **9 retraits sur 30** qui ont demandé une reprise.

Un élève qui n'aurait que le chronomètre corrigerait la mauvaise étape ; un élève qui n'aurait que
les témoignages ignorerait 40 secondes. C'est le croisement qui décide.

## Le QCM complémentaire

`qcm_fonctionnement_objet.html` a été réécrit le 18/11/2026 au gabarit commun (30 questions, C2.1
et C2.2 seulement). Ses deux figures sont dans le tableau ci-dessus. L'ancienne version (25
questions, sans image, qui débordait sur les codes C9 de l'ancien programme) est archivée dans
`_archive-anciennes-versions/C2-decrire-les-interactions-entre-un-objet-ou/4e_C2.1/`.

## Polices

**Aucune police distante** (règle d'or n°40). Séquence, QCM et synthèses utilisent une pile système.
La page entière fonctionne sans connexion, et aucune donnée n'est envoyée.

## Image générée par IA (Canva) pour la synthèse élève

Demande de Pascal du 29/10/2026 : « une capture d'écran ou une illustration permet d'avoir une vision plus synthétique
de l'objet » ; Canva autorisé « pour des images réalistes et autres ». Règles : skill `synthese-vulgarisee`, §4.

| Fichier | Ce qu'elle montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/synthese_borne_velos_hangzhou.png` | Une borne de vélos en libre-service sur un trottoir après la pluie, une rangée de vélos accrochés à côté. PNG 1 536 × 1 024, 2.8 Mo. | **Image générée par IA** avec Canva (génération d'image), compte de Pascal, 29/10/2026. Demande : « Realistic photo of a bike-sharing docking station on a wet city sidewalk after rain: a slim kiosk post with a small tilted screen and a card reader in the foreground, a row of identical shared bicycles locked into docks beside it, no people, no readable text, no logos, no brand colours » | Conditions Canva AI Product Terms : l'image appartient à Pascal, sans attribution exigée ; interdit de la présenter comme faite par un humain (légende « Image générée par IA (Canva) ») et d'en retirer les métadonnées de provenance (manifeste C2PA et XMP Canva gardés : **fichier non modifié**, d'où son poids). | Synthèse élève, carte « Ce que je dois retenir » ; et la situation déclenchante de la séquence (05/11/2026) |

## Documents du QCM (21/11/2026, règle d'or n°345)

Des documents à lire pour répondre, dessinés pour le téléphone (350 unités de large, texte de 15 px et plus).
Pour les redessiner : `python3 _outils/document_qcm.py documents_qcm_4e_C2.1.json`.

| Fichier | Ce qu'il montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/doc_six_familles_questions.svg` | Six fiches, une par famille d'exigences, avec la question que chacune pose. Sécurité : quelqu'un peut-il se blesser ou être mis en danger ? Incidences environnementales : que coûte l'objet en matière et en énergie, sur sa durée de vie ? Formes et fonctions : la forme sert-elle ce que l'objet doit faire ? Ergonomie : le corps et les gestes sont-ils respectés ? Qualité : l'objet fait-il toujours ce qu'il annonce ? Fiabilité : combien de fois sur cent l'objet échoue-t-il ? | SVG original, dessiné par `_outils/document_qcm.py` à partir de `documents_qcm_4e_C2.1.json` — Claude (Fable 5.2), pour ce dépôt, 21/11/2026. Les nombres sont ceux du fichier de données simulées du lot. | CC0 1.0 | QCM, questions 19, 20, 22 et 23 |
| `Images/doc_parcours_cinq_etapes.svg` | Cinq fiches, dans l'ordre du parcours. 1. Arriver : s'approcher de la borne et lire l'écran. 2. Identifier : présenter sa carte ou son téléphone. 3. Choisir : parcourir la liste des vélos disponibles. 4. Déverrouiller : attendre le déverrouillage du point d'ancrage. 5. Partir : sortir le vélo de son ancrage. | SVG original, dessiné par `_outils/document_qcm.py` à partir de `documents_qcm_4e_C2.1.json` — Claude (Fable 5.2), pour ce dépôt, 21/11/2026. Les libellés des étapes sont ceux de `donnees_parcours_borne_hangzhou_simulees.csv`. | CC0 1.0 | QCM, question 1 |
