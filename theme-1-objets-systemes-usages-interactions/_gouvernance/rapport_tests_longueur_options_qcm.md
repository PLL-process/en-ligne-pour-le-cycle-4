# Rapport de tests — la longueur des options ne doit pas trahir la bonne réponse

**Date** : 28/08/2026 · **Environnement réel** : Chromium (Playwright), pages en `file://`, hors ligne.
**Mesure** : `_outils/controle_longueurs.py` sur les 43 banques de questions du dépôt.

## Le défaut

Dans un QCM écrit à la main, on soigne la bonne réponse — nuancée, complète, précise — et on
expédie les distracteurs en quatre mots. L'élève qui ne sait rien coche la plus longue et s'en
tire très bien. Le QCM mesure alors l'habileté au QCM, pas la technologie.

Le critère retenu est l'écart **visible** : une bonne réponse qui se détache de plus de
8 caractères du peloton des distracteurs. Être la plus courte de deux caractères ne se remarque
pas ; le rang seul n'est donc pas un critère utilisable.

## Ce que la mesure a trouvé

Les QCM anciens de la maison sont entre 0 et 10 % de questions détachées. Trois banques
dépassaient le seuil de 15 % — **et les deux pires étaient les deux QCM écrits le 25/08/2026
(PR #261)** :

| Banque | avant | écart moyen | après | écart moyen |
|---|---|---|---|---|
| `qcm_numerique_societe.html` (3e_C1.5) | **28 / 30** | **+34,9 car.** | **0 / 30** | −1,0 car. |
| `qcm_cybersecurite_usage_raisonne.html` (4e_C1.4) | **20 / 30** | **+21,6 car.** | **0 / 30** | +1,5 car. |
| `qcm_book-train.html` (Thème 2, hérité) | 5 / 30 | +7,9 car. | *hors périmètre de cette branche* | |

Dans `qcm_numerique_societe`, **les 30 bonnes réponses sur 30 étaient les plus longues de leur
question**. Un élève qui ne lisait aucune question et cochait systématiquement la réponse la
plus longue obtenait 30/30.

## Ce qui a été changé, et ce qui ne l'a pas été

**Changé** : le texte de 48 bonnes réponses (28 + 20), raccourci — et une, allongée
(« un délit, puni par la loi », qui était au contraire trop brève parmi ses distracteurs).

**Pas changé** : le sens des réponses, l'ordre des options, l'index de la bonne réponse, les
90 réfutations de chaque banque, les champs `expl`, `ex`, `err`, `ret`. La répartition A/B/C/D
reste 8/7/7/8 dans les deux banques.

Le remède a été de **raccourcir la bonne réponse**, pas d'allonger les distracteurs : les bonnes
réponses étaient des phrases d'explication là où les distracteurs étaient des affirmations nues.
L'explication a déjà sa place dans le champ `expl`, qui s'affiche à la correction — la garder
aussi dans l'option, c'était la donner deux fois, et la donner d'avance.

*(Sur le QCM `4e_C6.2`, écrit le même jour, le remède inverse a été employé : là, allonger les
distracteurs était le bon geste. Ce n'est pas une recette, c'est un diagnostic à faire banque
par banque.)*

## Suite de tests, 17 tests par banque

| # | Test | 3e_C1.5 | 4e_C1.4 |
|---|---|---|---|
| 1 | La page charge sans erreur JS | ✅ | ✅ |
| 2 | Aucune requête échouée | ✅ | ✅ |
| 3 | Aucune boîte modale (règle n°188) | ✅ | ✅ |
| 4 | 30 questions | ✅ | ✅ |
| 5 | 30 notions nommées, toutes distinctes | ✅ | ✅ |
| 6 | 90 réfutations, une par distracteur | ✅ | ✅ |
| 7 | Aucune réfutation sur la bonne réponse | ✅ | ✅ |
| 8 | Répartition A/B/C/D équilibrée | ✅ 8/7/7/8 | ✅ 8/7/7/8 |
| 9 | Codes du programme bien formés | ✅ C1.3·C1.4·C1.5 | ✅ C1.4·C1.5·C1.6 |
| 10 | Codes assez échantillonnés (≥ 5 q.) | ✅ 10 chacun | ✅ 10 chacun |
| 11 | Tous les champs du gabarit renseignés | ✅ | ✅ |
| 12 | Aucune option dupliquée | ✅ | ✅ |
| 13 | Aucune bonne réponse détachée (> 8 car.) | ✅ 0/30 | ✅ 0/30 |
| 14 | Écart moyen sous 5 caractères | ✅ −1,0 | ✅ +1,5 |
| 15 | Aucune réponse exposée dans le HTML | ✅ | ✅ |
| 16 | Titre portant un code du programme | ✅ | ✅ |
| 17 | Retour vers la séquence du lot | ✅ | ✅ |

**17 / 17 sur les deux banques.**

## Ce que ce rapport ne prouve pas

Que les questions sont pédagogiquement justes. Aucun test automatique ne le dira. Il prouve que
la bonne réponse ne se devine plus sans lire la question — ce qui n'était pas le cas il y a
trois jours, dans deux lots que j'avais annoncés « au gabarit ». Ils l'étaient : le gabarit ne
disait rien de la longueur des options. C'est le contrôle qui manquait.
