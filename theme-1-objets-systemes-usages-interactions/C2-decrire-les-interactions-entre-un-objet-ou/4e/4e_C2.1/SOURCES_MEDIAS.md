# Sources des médias — lot Hangzhou 4e_C2.1 · C2.2

**Règle d'or n°1** : chaque image est un document à lire, produite pour le dépôt, sous licence
libre, avec `<title>` et `<desc>` accessibles.

| Fichier | Nature | Auteur | Licence | Rôle pédagogique |
|---|---|---|---|---|
| `Images/du_verbatim_a_l_algorigramme.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | Le trajet imposé par le référentiel — langage naturel, schéma, graphique, algorithme — chacun avec ce qu'il apporte **et ce qu'il ne sait pas dire** |
| `Images/six_familles_d_exigences.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | Les six familles d'exigences **dans les mots du programme**, la question que chacune pose, et ce qu'elle donne sur la borne |
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

## Ressource héritée, non modifiée

`qcm_fonctionnement_objet.html` (50 Ko, 25 questions, « Comment expliquer le fonctionnement d'un
objet ? ») était présent dans ce dossier **avant** cette séquence. Il est d'un **autre auteur** et
n'a pas été modifié — pas une balise.

Il est référencé depuis le bloc Bonus comme **ressource complémentaire**, avec sa portée dite
honnêtement : il annonce lui-même couvrir `C2.1`, `C2.2` **et `C9.1` à `C9.3`**, c'est-à-dire qu'il
déborde sur la programmation. Il ne remplace pas le QCM du lot.

## Polices

**Aucune police distante** (règle d'or n°40). Séquence, QCM et synthèses utilisent une pile système.
La page entière fonctionne sans connexion, et aucune donnée n'est envoyée.
