---
name: validations-qui-disent-vrai
description: Vérifier et corriger les validations automatiques d'une séquence (boutons « Vérifier », `const CHECKS`, simulateurs) pour qu'une activité affichée « réussie » le soit vraiment — seuil codé = seuil annoncé, ordre exigé vérifié, réponse changée = validation retirée, justification écrite jamais validée aux mots-clés, simulateur qui dit ses hypothèses (règles d'or n°333 et n°338). À utiliser à chaque révision ou audit de séquence, et sur toute activité neuve qui se vérifie. Règles d'or n°340, n°347, n°362 et n°363 ; pour un programme écrit dans la page, n°333 mesurée et skill `banc-essai-programme`.
---

# Une validation dit la vérité

**Règle d'or n°340 — Une validation dit vrai** (Pascal, 18/11/2026, sur l'audit de `3e_C4.1` : « oui, deux règles d'or »). Ce skill en est la méthode ; ses outils en sont le contrôle de fin de lot.

Né le 17/11/2026 de l'audit externe de `3e_C4.1` (l'énergie de la station). L'auditeur n'a rien cliqué : il a lu les
fonctions `CHECKS` et `majSim`, et chaque constat s'est vérifié au navigateur. L'activité 1 annonçait 11 / 11 et
validait à 10 ; l'activité 4 annonçait 8 / 8 et validait à 7, avec une justification acceptée sur sa longueur
(« vent sel vent sel vent sel… » passait) ; la consigne exigeait « une configuration insuffisante, PUIS ta solution »
et le code acceptait l'ordre inverse ; une réponse changée après la vérification laissait l'activité validée ; le
simulateur donnait 80 h pour 40 Ah sans dire qu'il ignorait les pertes. Mesuré le même jour sur le site :
**14 seuils** codés sous le seuil annoncé, dans 9 séquences du thème 2 ; **63 pages sur 64** sans retrait de la
validation.

Règles : n°333 (une réussite affichée prouve la production réelle), n°338 (un même attendu se dit avec les mêmes
nombres partout : la consigne et le code compris), n°336 (chaque exercice a sa correction).

## 1. Mesurer

```bash
python3 _outils/controle_validations.py --detail <dossier du lot>
```

| Code | Ce qu'il voit | Gravité |
|---|---|---|
| V1 | « 🎯 Critère de réussite : 6 / 6 » et `valide: ok>=5` | ✘ — sortie 1 |
| V1 | `valide: ok>=5` sur `total:6`, sans « 5 / 6 » écrit nulle part | ⚠ |
| V3 | aucun `__valid[…] = false` : une réponse changée garde la validation | ⚠ |
| V4 | une réponse écrite validée par la machine (longueur, `mots.size`, mots-clés) sans « relue par ton professeur » | ⚠ |
| V5 | un curseur `type="range"` sans « modèle simplifié » dans la page | ⚠ |

Ce que l'outil ne lit pas se fait à la main, activité par activité (étape 2).

Une page où l'élève écrit un programme se mesure en plus avec `python3 _outils/controle_verification_execute.py
--detail` (n°333 : ✘ T si une vérification juge le programme par des motifs dans son texte, sans l'exécuter).

## 2. Lire chaque vérification comme l'auditeur

Ouvrir `const CHECKS = {` et, pour chaque activité, mettre côte à côte ce que la page **annonce** (consigne, critère
de réussite, message de réussite) et ce que le code **exige** :

1. **Le seuil (V1).** Le nombre codé est celui que lit l'élève. Par défaut, le code suit l'annonce
   (`ok===6` pour « 6 / 6 ») : c'est la décision prise pour `3e_C4.1` et les 14 seuils du 17/11. Une tolérance voulue
   (« 5 sur 6 suffisent ») s'écrit dans le critère, en toutes lettres.
2. **L'ordre (V2).** Une consigne qui dit « d'abord…, puis… » se vérifie dans cet ordre : on enregistre l'essai
   réussi seulement s'il suit l'échec (`if (ok && __exp.insuffisant !== undefined) __exp.apres_echec = …`), et le
   message dit ce qui manque (« fais d'abord un essai qui échoue »).
3. **Le retrait (V3).** Une réponse changée après la vérification retire la validation de l'activité, le dit
   (« ✏️ Tu as changé une réponse après la vérification : vérifie de nouveau ») et la barre de progression suit.
   Le modèle, posé sur `3e_C4.1` : un écouteur `input`/`change` sur la plus grande zone qui ne contient qu'un bouton
   `[data-check]` (pas la séance entière : trois boutons y vivent), qui ignore les curseurs du simulateur. Le
   généraliser demande de connaître l'état de chaque gabarit (`window.__valid`, `save`, `majProgress`) : une PR par
   gabarit, jamais à l'aveugle.
4. **La réponse écrite (V4).** Une machine ne juge pas un raisonnement. Elle peut exiger ce qui se nomme (le
   matériau, le procédé, la grandeur et son unité) et refuser le bourrage (au moins huit mots différents) ; le message
   de réussite ajoute « Ta justification sera relue par ton professeur ». Jamais « Acquis » sur un texte libre.
5. **Le simulateur (V5).** Un modèle idéal le dit sous le simulateur (« ⚠️ Modèle simplifié : … sans aucune perte. En
   vrai… : c'est une raison de plus pour prendre une marge »). Un chiffre qui sert à décider (tenir 72 h) ne se donne
   pas sans ses hypothèses.
6. **La question qui souffle (I3).** Une question ne montre pas le résultat de la précédente (« 432 Wh ÷ 12 V = … »
   sous la question qui demande les 432 Wh) : `python3 _outils/controle_propositions_indices.py` (skill
   `propositions-sans-indice`).

## 2 bis. Un score dit quoi reprendre (n°347, 21/11/2026)

Une validation juste ne suffit pas : l'élève doit savoir quoi refaire. Né de l'audit de l'entraînement DNB de
`3e_C6.2` : avec 7 / 8, l'élève ne savait pas quel exercice revoir ; avec 6 justes et 2 blancs, la page cochait
« répondre aux 8 exercices ». Modèle en place : `_outils/dnb_gabarit.html` (fonctions `corriger`, `poserEtat`,
`message`, `majTaches`).

1. **Trois comptes séparés** : renseignés, justes, seuil. « 6 / 8 renseignés · seuil atteint · exercices 15 et 16 à
   faire ». Une `CHECKS[n]()` renvoie aussi `vides` et `detail` (l'état de chaque exercice).
2. **Une marque par exercice** après « Vérifier » : ✔ juste, ✘ à revoir, ○ à faire — en mots, pas en couleur seule
   (n°119).
3. **Le message cite les numéros**, jamais la bonne réponse : « À revoir : exercice 17 ».
4. **« 🔎 Revoir mon erreur »** dit ce qui cloche dans le choix de l'élève (le `data-pourquoi` de sa proposition),
   puis ouvre l'aide 1 : l'indice ciblé avant le corrigé (n°339).
5. **Le bandeau des tâches** sépare « répondre à tous » (non cochée tant qu'une case est vide) et « atteindre le
   seuil ».
6. **Après rechargement**, les marques et le bilan « Où en suis-je ? » reviennent.

Critères de banc : 6 justes + 2 blancs → le message exact ci-dessus et la tâche « répondre à tous » non cochée ; une
erreur en 17 → « À revoir : exercice 17 », sans la bonne réponse dans le message.

## 2 ter. Un programme se juge en l'exécutant (n°333 ; n°373, n°374 en essai — 22/11/2026)

Né des audits de « Programmer l'alerte » (`3e_C6.1`) : sept motifs cherchés dans le texte refusaient un programme
juste écrit avec des apostrophes et acceptaient un programme faux à 118 km/h ; des prévisions justes validaient une
version jamais essayée. Méthode complète : skill `banc-essai-programme`. En bref :

1. **Exécuter** le programme de l'élève sur les entrées du cahier des charges (sous, à, au-dessus de chaque seuil) et
   comparer ses sorties ; le message nomme le premier écart, jamais la ligne à corriger.
2. **La version se dit** (n°373) : l'éditeur affiche la version qu'il contient ; chaque document dit la sienne ; les
   lectures se font sur la version figée.
3. **Prévoir avant d'essayer** (n°374) : prévisions, diagnostic et essais comptés à part ; une prévision juste ne
   valide jamais un programme.
4. **Un code modifié périme l'essai** (n°333) : l'empreinte du programme essayé est gardée ; une frappe la change → « à
   rejouer ».
5. **Une limite de l'outil n'est pas une erreur de l'élève** (n°340, la simplification dite) : « limite du banc, pas
   forcément une erreur de ton programme », jamais « SyntaxError » pour du Python juste.

## 3. Rejouer chaque constat en test de banc

Un défaut de validation se corrige avec le test qui l'aurait vu (n°333 : le code modifié se reteste). Dans le banc du
lot (`tests_<lot>.mjs`), un cas par défaut corrigé — modèle `3e_C4.1`, tests 10 bis et 10 ter :

- la bonne réponse complète valide ; la même moins une réponse ne valide pas (le seuil) ;
- l'essai réussi avant l'échec ne valide pas (l'ordre) ;
- « vent sel vent sel… » ne valide pas ; la phrase qui nomme matériau et procédé valide (la réponse écrite) ;
- valider, changer une réponse : l'activité n'est plus validée, le message le dit (le retrait).

Lancer le banc du lot et `tests_regle_311_<lot>.mjs` ; le mode mission : `node _outils/mode_mission/banc_generique.mjs <page>`.

## 3 bis. La simulation et le bilan disent vrai aussi (n°362, n°363, 21/11/2026)

Nés de l'audit en 12 axes du TP `4e_C6.2` (PR #841) :

- **Une simulation joue le travail de l'élève** (n°362). Celle du TP testait une règle fixe (« < 50 lux → la lampe
  s'allume ») quelles que soient les sorties que l'élève avait choisies : elle ne pouvait ni le contredire ni l'aider.
  Elle lit maintenant ses choix : sans choix, elle les demande ; avec un choix faux, elle dit ce que fait la lampe et
  pourquoi ce n'est pas le besoin. Si une simulation ne peut que montrer un modèle, elle le dit (« voici le modèle »).
  Test de banc : choix faux → message d'erreur ; choix juste → réussite, aux deux bords du seuil.
- **Le bilan imprimé est une preuve** (n°363). Il montre ce que l'élève a construit et répondu (ordre des blocs,
  sorties, cases, réponses, mini-projet), le nombre d'essais ratés par exercice, et un code de validation calculé sur
  TOUT ce qu'il affiche (nom, classe, score, date). Le code du TP ne lisait que les sept premières lettres du nom :
  identique à 0 / 20 et à 20 / 20. Test de banc : le vrai code est reconnu, une note retouchée est refusée.
- **La date du bilan est celle du poste** (n°365, `controle_date_locale.py`).

## 4. Généraliser et dire

- Mesurer tout le site (`controle_validations.py`, sans chemin) et écrire le compte dans le journal, même si on ne
  corrige qu'une page (n°293).
- Un ✘ V1 se corrige dans la même PR (le code suit l'annonce) ; les ⚠ se reprennent séquence par séquence à la
  révision, avec le banc du lot.
- Réponse à Pascal : format `reponses-actionnables` ; une tolérance à garder ou un seuil à baisser est sa décision (🔶).
