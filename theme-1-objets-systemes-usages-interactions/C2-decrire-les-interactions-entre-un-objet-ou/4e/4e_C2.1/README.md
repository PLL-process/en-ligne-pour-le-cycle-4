# 4e_C2.1 · C2.2 — Hangzhou : ce que vit l'usager devant la borne

Deuxième lot du **C2**. Il prend la suite du 5e — où l'élève recensait les interacteurs — et fait
ce que le programme de 4e impose : **partir de ce que les gens disent pour aboutir aux schémas, aux
graphiques et aux algorithmes**, puis remonter aux exigences.

➡ **[Séquence complète](sequence_4e_C2_hangzhou_borne.html)** — 3 séances de 55 min. Une
réclamation : « vos bornes sont trop lentes ». Une réponse : « aucune n'est en panne ». **Les deux
ont raison, et personne n'avance.**

➡ **[QCM d'entraînement](qcm_4e_C2_hangzhou_borne.html)** — 30 questions, dont 5 illustrées, chaque
distracteur réfuté. Il s'ouvre sur **ce que l'élève a déjà travaillé** (règle n°45).

➡ Synthèses : [élève](Synthèses/synthese_eleve_4e_C2.1-C2.2.html) ·
[professeur](Synthèses/synthese_professeur_4e_C2.1-C2.2.html)

➡ [Fiche pédagogique](fiche_pedagogique_4e_C2.1-C2.2.md) ·
[Matrice](matrice_couverture_4e_C2.1-C2.2.csv) · [Rapport de tests](rapport_tests_4e_C2.1-C2.2.md) ·
[Sources des médias](SOURCES_MEDIAS.md) · [Plan du lot](PLAN_LOT_C2_4e.md)

➡ Données **simulées** :
[`verbatims_usagers_hangzhou_simules.csv`](verbatims_usagers_hangzhou_simules.csv) (12 usagers) ·
[`donnees_parcours_borne_hangzhou_simulees.csv`](donnees_parcours_borne_hangzhou_simulees.csv)
(30 retraits × 5 étapes)

➡ [`_generation/`](_generation/) — les 30 questions du QCM (`q.py`) et le générateur qui les injecte
dans le gabarit maison (`build_qcm.py`). Une seule source de vérité, un seul générateur.

## Le résultat que les données produisent toutes seules

L'étape la plus longue en **moyenne** est « choisir » — **40 s** — et **personne ne s'en plaint**.
L'étape dont parlent trois verbatims sur douze est « déverrouiller » : **29 s** de moyenne, mais
**83 s** pour les **9 retraits sur 30** qui ont demandé une reprise.

Un élève qui n'aurait que le chronomètre corrigerait la mauvaise étape. Un élève qui n'aurait que
les témoignages ignorerait 40 secondes. **C'est le croisement qui décide.**

## ⚠️ À lire avant d'utiliser le lot en classe

**Le tableau de données ne dispense pas des verbatims, et l'inverse non plus.** Si vous sautez
l'activité 1 pour aller au graphique, la séquence perd son sujet : elle devient un exercice de
tableur.

**Codes de classement.** `4e_C2.1` et `4e_C2.2` sont des codes **internes à ce dépôt**. La référence
normative est le programme de technologie du cycle 4, BO n°9 du 29 février 2024 — et les
formulations de la carte du référentiel en sont recopiées, non reformulées (règle n°42).

## Ce qui est nouveau dans ce lot

Trois règles du dépôt s'y appliquent pour la première fois, toutes nées de remarques de Pascal le
jour même :

- **n°43 étendue** — le **Bonus a son corrigé**, entièrement traité sur le distributeur de boissons
  du hall : les mots exacts de trois personnes, dix chronométrages, et l'écart moyenne / pire cas
  qui rejoue en petit ce que l'élève a découvert sur la borne.
- **n°44** — chaque badge et chaque bouton porte une infobulle, **et** une légende en clair. Une
  infobulle ne s'ouvre pas au doigt : sur tablette, `title` ne s'affiche jamais.
- **n°45** — le bouton du QCM ouvre sur **ce que l'élève a validé**. Après la seule séance 1, il
  propose 15 questions et non 30. Le parcours complet reste à un clic.

Conséquence : **un élève absent ou en reprise à la maison peut faire cette séquence seul**, du début
à la fin. Tout ce qui lui est demandé a son corrigé.

## Ressource complémentaire, héritée

[`qcm_fonctionnement_objet.html`](qcm_fonctionnement_objet.html) (25 questions) était présent dans
ce dossier avant cette séquence. Il est d'un **autre auteur** et n'a pas été modifié. Il aborde les
notices et les contraintes, et **déborde sur la programmation** (codes C9). Il ne remplace pas le
QCM du lot.

## Ce que l'élève doit savoir dire à la fin

Qu'un **ressenti n'est pas une mesure**, et qu'il faut les deux. Qu'une **moyenne décrit le milieu**,
et que personne ne vit le milieu. Qu'un **test a deux sorties**, et qu'une reprise sans sortie
d'échec est une boucle. Qu'une **exigence dit ce qu'il faut obtenir**, pas comment. Et que **la
donnée la plus grosse n'est pas toujours le problème**.

## Les codes voisins

- **4e_C2.2** est couvert par cette même séquence (séance 3) — voir le README pointeur du dossier
  `4e_C2.2`.
- **3e_C2.1** (décrire l'expérience de l'utilisateur à l'aide de modes de représentation choisis)
  reste à créer : l'algorigramme travaillé ici en pose le geste, qui est aussi un geste du **DNB**.

*Lot Thème 1 · 4e — on ne se plaint pas de la moyenne, on se plaint de ce qu'on a vécu.*
