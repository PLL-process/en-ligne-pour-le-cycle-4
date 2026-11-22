---
name: validations-qui-disent-vrai
description: Vérifier et corriger les validations automatiques d'une séquence (boutons « Vérifier », `const CHECKS`, simulateurs) pour qu'une activité affichée « réussie » le soit vraiment — seuil codé = seuil annoncé, ordre exigé vérifié, réponse changée = validation retirée, justification écrite jamais validée aux mots-clés, simulateur qui dit ses hypothèses (règles d'or n°333 et n°338). À utiliser à chaque révision ou audit de séquence, et sur toute activité neuve qui se vérifie. Règle d'or n°340.
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

## 3. Rejouer chaque constat en test de banc

Un défaut de validation se corrige avec le test qui l'aurait vu (n°333 : le code modifié se reteste). Dans le banc du
lot (`tests_<lot>.mjs`), un cas par défaut corrigé — modèle `3e_C4.1`, tests 10 bis et 10 ter :

- la bonne réponse complète valide ; la même moins une réponse ne valide pas (le seuil) ;
- l'essai réussi avant l'échec ne valide pas (l'ordre) ;
- « vent sel vent sel… » ne valide pas ; la phrase qui nomme matériau et procédé valide (la réponse écrite) ;
- valider, changer une réponse : l'activité n'est plus validée, le message le dit (le retrait).

Lancer le banc du lot et `tests_regle_311_<lot>.mjs` ; le mode mission : `node _outils/mode_mission/banc_generique.mjs <page>`.

## 3 bis. La simulation et le bilan disent vrai aussi (n°347, n°348, 21/11/2026)

Nés de l'audit en 12 axes du TP `4e_C6.2` (PR #841) :

- **Une simulation joue le travail de l'élève** (n°347). Celle du TP testait une règle fixe (« < 50 lux → la lampe
  s'allume ») quelles que soient les sorties que l'élève avait choisies : elle ne pouvait ni le contredire ni l'aider.
  Elle lit maintenant ses choix : sans choix, elle les demande ; avec un choix faux, elle dit ce que fait la lampe et
  pourquoi ce n'est pas le besoin. Si une simulation ne peut que montrer un modèle, elle le dit (« voici le modèle »).
  Test de banc : choix faux → message d'erreur ; choix juste → réussite, aux deux bords du seuil.
- **Le bilan imprimé est une preuve** (n°348). Il montre ce que l'élève a construit et répondu (ordre des blocs,
  sorties, cases, réponses, mini-projet), le nombre d'essais ratés par exercice, et un code de validation calculé sur
  TOUT ce qu'il affiche (nom, classe, score, date). Le code du TP ne lisait que les sept premières lettres du nom :
  identique à 0 / 20 et à 20 / 20. Test de banc : le vrai code est reconnu, une note retouchée est refusée.
- **La date du bilan est celle du poste** (n°350, `controle_date_locale.py`).

## 4. Généraliser et dire

- Mesurer tout le site (`controle_validations.py`, sans chemin) et écrire le compte dans le journal, même si on ne
  corrige qu'une page (n°293).
- Un ✘ V1 se corrige dans la même PR (le code suit l'annonce) ; les ⚠ se reprennent séquence par séquence à la
  révision, avec le banc du lot.
- Réponse à Pascal : format `reponses-actionnables` ; une tolérance à garder ou un seuil à baisser est sa décision (🔶).
