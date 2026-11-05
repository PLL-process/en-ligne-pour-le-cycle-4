# Rapport de tests — 5e_C1.5 + 5e_C1.6 « Le compte du club »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle.


> **Correction du 31/08/2026 — deux verrous expérientiels s'ouvraient au chargement.**
> `_outils/controle_verrous.mjs` ouvre chaque séquence du dépôt dans un navigateur **neuf** et
> lit `window.__exp` juste après le chargement. Cette page en portait **deux** avant tout
> geste : `anonyme` (un profil vide n'a aucun indice, donc la condition « zéro indice » était
> vraie d'emblée) et `regarde` (la fonction qui affiche ce que le profil laisse voir était
> appelée à l'initialisation). Les activités qui exigent « j'ai regardé ce que mon profil
> laisse voir » et « j'ai composé un profil anonyme » étaient donc déverrouillées avant que
> l'élève ait coché une seule case. `majPubli` et `regarder` prennent désormais un `tracer` et
> n'enregistrent que sur un geste ; l'initialisation passe `false`. Vérifié : `__exp` est
> **vide** à l'ouverture, et vaut `{anonyme, compose, regarde}` dès la première case cochée
> (règles d'or n°226 et n°265).
```bash
node tests_5e_C1.5-C1.6_sequence.mjs "$PWD/sequence_5e_C1.5-C1.6_le-compte-du-club.html" 5e reponses_5e_C1.5-C1.6.json
node tests_5e_C1.5-C1.6_qcm.mjs      "$PWD/qcm_5e_C1.5-C1.6_le-compte-du-club.html" 5e_C1.5 5e_C1.6 sequence_5e_C1.5-C1.6_le-compte-du-club.html 15 15
```

---

## 1. Séquence — **38 / 38**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ le banc part vide — [0,0]
✅ la publication du club compte 7 indices — [7,3]
✅ elle enfreint 3 règle(s) — [7,3]
✅ le banc énumère 9 constats — 9
✅ publier est refusé, et le banc dit pourquoi — Refusé — Droit à l'image : publier le visage d'une personne reconnaissable demande son acc
✅ « on retire le visage » → 6 indice(s) / 2 règle(s) — [6,2]
✅ « accord écrit des responsables légaux » → 6 indice(s) / 1 règle(s) — [6,1]
✅ « image sous licence CC BY, auteur cité » → 6 indice(s) / 0 règle(s) — [6,0]
✅ « on retire le nom et la classe » → 4 indice(s) / 0 règle(s) — [4,0]
✅ « on retire la rue, l'heure, le collège et la géolocalisation » → 0 indice(s) / 0 règle(s) — [0,0]
✅ la publication corrigée est acceptée — Publié. La photo montre le jardin connecté et rien d'autre :
✅ verrou « charge » ouvert
✅ verrou « regarde » ouvert
✅ verrou « compose » ouvert
✅ verrou « refuse » ouvert
✅ verrou « anonyme » ouvert
✅ verrou « legal » ouvert
✅ verrou « publie » ouvert
✅ bandeau de durée présent — ⏱ 3 séances de 55 min
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ encadré de règle de la séquence présent
✅ le numéro national est indiqué
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ activité 0 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 1 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 2 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 3 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 4 validée (7/7) — 🎉 Activité validée — 7/7. Ouvre la correction pour comparer.
✅ activité 5 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ une réponse fausse est refusée — 🟡 4/5 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a1q1 = son nom, sa classe et son collège le désignent toujours
✅ la publication survit au rechargement — jardin coché
✅ les verrous survivent au rechargement
```

## 2. QCM — **34 / 34**

> **Ce qui a changé le 02/09/2026.** La suite exigeait *« aucune image héritée du lot
> voisin »* — et le vérifiait en refusant **toute** image. Elle datait du jour où le
> commentaire du fichier annonçait « 3 illustrees » alors qu'il n'en portait aucune : la
> garde visait des images arrivées par copie du gabarit. Ce lot porte maintenant **une**
> image, la sienne, et la ligne dit enfin ce qu'elle voulait dire : une image, s'il y en a
> une, **vient du lot lui-même** (`Images/…`), porte un `alt` de plus de soixante caractères
> qui transcrit ce qui est visible, et **se charge réellement** (`naturalWidth > 0`).
> Deux contrôles de plus, et une garde qui n'interdit plus ce qu'elle devait seulement
> localiser : 32 → 34.

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ 30 questions — 30
✅ 4 options par question
✅ 3 réfutations par question
✅ la bonne réponse n’a pas de réfutation
✅ tous les champs du gabarit remplis
✅ aucune image héritée d’un autre lot — Images/licences_symboles.svg
✅ chaque image porte un alt qui transcrit ce qui est visible — 292 car.
✅ chaque image se charge réellement (naturalWidth > 0) — Images/licences_symboles.svg 660×240
✅ 30 notions distinctes — 30
✅ 15 questions sur 5e_C1.5 — {"5e_C1.5":15,"5e_C1.6":15}
✅ 15 questions sur 5e_C1.6 — {"5e_C1.5":15,"5e_C1.6":15}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 1.5
✅ une bonne réponse est déclarée correcte
✅ la correction déplie les trois réfutations
✅ la correction porte un « À retenir »
✅ une mauvaise réponse est déclarée incorrecte
✅ valider sans réponse n’ouvre aucune boîte modale
✅ valider sans réponse annonce et ne valide pas encore — Tu n'as choisi aucune réponse : elle comptera comme non répondue. — clique une seconde fois pour confirmer.
✅ le second clic valide bien
✅ « recommencer » n’ouvre aucune boîte modale
✅ « recommencer » demande confirmation sans rien effacer — 30
✅ le second clic remet bien à zéro — 0
✅ le mode « marquées » vide n’ouvre aucune boîte modale
✅ il affiche un bandeau à la place — Aucune question marquée « à revoir ». Utilise le bouton 🔖 sur une question.
✅ 30 bonnes réponses donnent 100 % — 100 %
✅ la note affichée est 20/20 — 20,0 /20
✅ le lien vers la séquence pointe le bon fichier — sequence_5e_C1.5-C1.6_le-compte-du-club.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours

34 / 34
```

## 3. Ce que ces tests vérifient de particulier

Cinq d'entre eux suivent **le compteur d'indices pas à pas**, et c'est là tout l'intérêt :

* la publication du club en compte **7**, et enfreint **3** règles ;
* retirer le visage : **6 indices** — un seul de moins, alors que c'est l'élément le plus visible ;
* obtenir l'accord écrit : **6 indices**, **1 règle**. *Le compteur d'indices ne bouge pas :*
  une autorisation rend licite, elle ne rend pas anonyme ;
* citer l'auteur de l'image sous CC BY : **0 règle** ;
* tout retirer sauf la photo du jardin : **0 indice**, et la publication est acceptée.

Un test qui se contenterait de vérifier « la publication est refusée » puis « la publication est
acceptée » passerait tout aussi bien — et ne prouverait rien du raisonnement que la séquence
demande. Ce sont les **valeurs intermédiaires** qui font la preuve.

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur une publication réelle** : le banc simule, avec des personnes
  inventées. La version 🅰 le fait avec le compte du collège, et c'est elle qui engage.
* Ils ne prouvent rien sur la **qualité du texte rédigé** au réinvestissement : le vérificateur
  compte des caractères, et la page le dit à l'élève.
* Ils ne prouvent rien sur ce qui se passe **en classe** — et cette séquence-là touche à des
  situations que des élèves vivent. Un test vert ne dit rien de cela.

## 5. Reprise du 04/11/2026 — la séquence passe à onglets (vague des séquences sans onglets)

La page était d'un seul tenant. Elle a maintenant trois séances à onglets (squelette n°306), le volet « 📖 Rappel » dès la
séance 2 (n°311) : séance 1 = ouverture + activités 0 et 1 ; séance 2 = activités 2 et 3 ; séance 3 = activité 4,
réinvestissement, synthèse, Bonus, bilan, QCM. Chaque séance a sa question directrice, son programme et son bouton vers la
suivante (n°101) ; l'onglet en cours est mémorisé. Le banc de publication reste **un seul** banc, hors du volet, qui suit
la séance ouverte et garde ce qui est coché. Le bilan reçoit « Comment j'ai travaillé » (seul manque relevé par
`controle_squelette`) ; la barre d'outils reçoit « 🖨 Imprimer / PDF ».

```bash
node tests_regle_311_5e_C1.5.mjs [--captures <dossier>]
```

```
✅ 1280 px : au chargement, le banc de publication (un seul nœud) est à sa place, dans l'activité 0 de la séance 1
✅ 1280 px : le sous-titre est visible hors du volet, à la séance 1 et à la séance 2
✅ 1280 px : un outil n'est pas du décor — .toolbar, #etabli hors du volet, visibles aux séances 1 et 2
✅ 1280 px : à la séance 2, le banc est juste après l'en-tête de la séance, avant l'activité 2
✅ 1280 px : déplacé, le banc garde son état (7 · une image trouvée sur un site, sans licence indiquée · 6 · 2 · 1)
✅ 1280 px : séance 2, le banc hors de sa carte ne déborde pas (0)
✅ 1280 px : à la séance 2, les onglets et l'en-tête de la séance sont dans le premier écran
✅ 1280 px : à la séance 3, le banc est juste avant le Bonus, avec son état
✅ 1280 px : retour à la séance 1, le banc retrouve sa place dans l'activité 0
✅ 1280 px : après rechargement (séance 2 mémorisée), le banc est de nouveau dans la séance 2 (séance s2, banc en s2)
✅ 1280 px : aucune erreur JS 
✅ 390 px : au chargement, le banc de publication (un seul nœud) est à sa place, dans l'activité 0 de la séance 1
✅ 390 px : le sous-titre est visible hors du volet, à la séance 1 et à la séance 2
✅ 390 px : un outil n'est pas du décor — .toolbar, #etabli hors du volet, visibles aux séances 1 et 2
✅ 390 px : à la séance 2, le banc est juste après l'en-tête de la séance, avant l'activité 2
✅ 390 px : déplacé, le banc garde son état (7 · une image trouvée sur un site, sans licence indiquée · 6 · 2 · 1)
✅ 390 px : séance 2, le banc hors de sa carte ne déborde pas (0)
✅ 390 px : à la séance 3, le banc est juste avant le Bonus, avec son état
✅ 390 px : retour à la séance 1, le banc retrouve sa place dans l'activité 0
✅ 390 px : après rechargement (séance 2 mémorisée), le banc est de nouveau dans la séance 2 (séance s2, banc en s2)
✅ 390 px : aucune erreur JS 
✅ sans JavaScript : la page reste d'un seul tenant (les trois séances à la suite, ni onglets ni boutons de séance), le banc dans l'activité 0
✅ lien direct #act4 : page chargée, volet replié, la cible à l'écran
✅ 1280 px : séance 1 = ouverture complète (6/6 titres, barre d'outils), sans volet
✅ 1280 px : séance 2 (s2) = volet « Rappel » replié, ouverture masquée
✅ 1280 px : séance 2 = titre, barre d'outils visible, badges masqués
✅ 1280 px : séance 2 sans défilement horizontal (0)
✅ 1280 px : séance dernière (s3) = volet « Rappel » replié, ouverture masquée
✅ 1280 px : séance dernière = titre, barre d'outils visible, badges masqués
✅ 1280 px : séance dernière sans défilement horizontal (0)
✅ 1280 px : clavier — Entrée sur le volet l'ouvre (ouverture et badges de nouveau visibles)
✅ 1280 px : ce qui a été saisi dans l'ouverture est conservé et visible dans le volet
✅ 1280 px : clavier — Espace referme le volet
✅ 1280 px : retour à la séance 1 : ouverture complète
✅ 1280 px : après rechargement (séance s3), le volet suit la séance
✅ 1280 px : la sauvegarde survit au rechargement
✅ 1280 px : aucune erreur JS 
✅ 390 px : séance 1 = ouverture complète (6/6 titres, barre d'outils), sans volet
✅ 390 px : séance 2 (s2) = volet « Rappel » replié, ouverture masquée
✅ 390 px : séance 2 = titre, barre d'outils visible, badges masqués
✅ 390 px : séance 2 sans défilement horizontal (0)
✅ 390 px : séance dernière (s3) = volet « Rappel » replié, ouverture masquée
✅ 390 px : séance dernière = titre, barre d'outils visible, badges masqués
✅ 390 px : séance dernière sans défilement horizontal (0)
✅ 390 px : clavier — Entrée sur le volet l'ouvre (ouverture et badges de nouveau visibles)
✅ 390 px : ce qui a été saisi dans l'ouverture est conservé et visible dans le volet
✅ 390 px : clavier — Espace referme le volet
✅ 390 px : retour à la séance 1 : ouverture complète
✅ 390 px : après rechargement (séance s3), le volet suit la séance
✅ 390 px : la sauvegarde survit au rechargement
✅ 390 px : aucune erreur JS 
✅ lien direct #act4 : ouvre s3, ouverture repliée
✅ lien direct #act0 : séance 1, ouverture complète
✅ sans JavaScript : ouverture et badges affichés, sans volet
✅ impression depuis s3 (fiche papier) : la séance seule, sans l'ouverture ni le bouton du volet
✅ après l'impression : le volet est replié de nouveau
✅ impression depuis la séance 1 (fiche papier) : l'ouverture, et l'en-tête qui porte Niveau 5e et 5e_C1.5

══ 5e_C1.5 : 34 / 34 tests réussis ══
```

- `tests_5e_C1.5-C1.6_sequence.mjs` : **38 / 38**, les mêmes lignes qu'avant. Un pas adapté : avant de remplir les champs
  d'une activité, le banc ouvre la séance qui la porte, comme l'élève.
- `tests_5e_C1.5-C1.6_qcm.mjs` : **34 / 34**, identique (le QCM n'a pas changé).
- `controle_squelette.mjs` : 0 défaut (D1 à D6), aucun « à rédiger », aucun signalement.
- Avant et après, mêmes verdicts (0 refus) : `controle_hors_ligne`, `controle_contraste_liens`, `controle_hierarchie`,
  `controle_unites`, `controle_sigles`, `controle_impression_papier`, `controle_regles_visibles`, `controle_liens`,
  `controle_verrous`, `controle_impression` ; `verif_regles_audit.py` : 5 ✘ avant, 4 après, tous déjà là (n°29, 30, 34, 300). Le n°31 n'est plus
  relevé parce que la nouvelle zone « Comment j'ai travaillé » a sa version étayée ; les cinq zones d'avant n'en ont
  toujours pas.

- Fiche papier (`banc_papier.py`, PDF A4 de Chromium) : **3 fiches, une par séance, 10 pages en tout** ; aucun texte pâle,
  aucun champ d'écran imprimé, aucun grand fond foncé, aucune première page vide.

**Retouches du même jour.** Le `<title>` disait « Thème 3 » : il dit « Thème 1 ». La page a sa mission en une phrase sous
le titre (« 🎯 Ta mission : … », tirée de la situation et de la problématique), la ligne « Thème 1 · 5e — … » reste en
plus petit ; le banc n°311 la vérifie hors du volet aux séances 1 et 2. Le Bonus a un corrigé replié **par défi** : le
corrigé commun est réparti entre les deux, et chacun reçoit ses attendus et ses erreurs fréquentes (les chiffres cités
ont été relus sur les compteurs du banc : géolocalisation seule 1 indice, image non choisie 0 règle et publication
refusée, accord oral 7 indices et 2 règles). Après les retouches : n°311 **57 / 57**, séquence **38 / 38**, QCM
**34 / 34**, `controle_squelette` 0 défaut, aucun « à rédiger ».

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.
