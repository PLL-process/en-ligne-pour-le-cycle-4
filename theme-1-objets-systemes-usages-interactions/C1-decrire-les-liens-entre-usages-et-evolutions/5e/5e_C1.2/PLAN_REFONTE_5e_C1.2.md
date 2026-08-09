# Plan de refonte — 5e_C1.2 « Sainte-Luce : quel frein pour les vélos du collège ? »

Écrit **après lecture intégrale** de l'existant (règle n°46) : la séquence de 10 ko, le QCM de
10 questions, les deux synthèses, la fiche, le manifeste, les données et les deux SVG.

## Pourquoi une refonte et non une réparation

Pascal a signalé la séquence ; l'audit du 8 août l'a confirmée en défaut sur trois règles, et la
lecture en montre davantage. **Aucun champ de saisie** : ni `textarea`, ni `select`, ni `input`, ni
`button` — alors que la page annonce trois fois une « production attendue ». Le QCM ne compte que
**10 questions** et n'emploie pas le moteur du dépôt. Les deux synthèses portent la définition
fausse. La réparation aurait touché tous les fichiers : autant reconstruire au gabarit.

## Ce qui est repris — et c'est beaucoup (règle n°12)

| Repris | Pourquoi |
|---|---|
| **La situation de Sainte-Luce** | Des vélos de prêt, des descentes, la pluie, les embruns. C'est le **seul ancrage martiniquais** du C1, et il est excellent. On le garde entier. |
| **Le cas du freinage** | Une fonction limpide — *arrêter un vélo en mouvement* — et trois principes réellement différents. Meilleur support de C1.2 que n'importe quel objet inventé. |
| **Le jeu de données `donnees_simulees_freinage_5e_C1.2.csv`** | Trois solutions × six critères chiffrés. **Plus riche que ce que la séquence en faisait** : elle n'en comparait que deux, et qualitativement (« Moyenne », « Bonne »). On exploite les trois et les chiffres. |
| **L'opposition fonction / principe / solution** | L'intention pédagogique était juste. C'est sa formulation qui était fausse. |
| **L'activité CRCN sur les données de freinage** | Réintégrée dans la séance 2 comme chemin autonome (règle n°59). |
| **Le second exemple « éclairer une salle »** | LED contre filament : deux principes pour une fonction, hors du vélo. Sert de transfert. |

## Ce qui ne peut pas être repris

- **La définition de la fonction technique.** « La fonction répond à : *à quoi cela sert-il ?* » et
  l'en-tête de tableau « Fonction : à quoi sert-il ? » définissent la **fonction d'usage**. Corrigé
  au gabarit de la règle n°53 : la fonction technique dit **ce que l'objet doit faire**, sans dire
  par quel moyen. La formulation fautive se retrouve à l'identique dans les deux synthèses.
- **Les tableaux statiques.** Cellules à « … » qu'aucun élève ne peut remplir.
- **`sequence.mhtml`** (180 ko) : une archive de navigateur qui se télécharge au lieu de s'afficher,
  et dont l'en-tête interne nomme un fichier `sequence_C1.2_4e_dark.html` — donc peut-être une
  séquence de 4e rangée en 5e. Archivée sans être reprise.
- **Le QCM de 10 questions**, hors moteur du dépôt : refait à 30, sur le gabarit.

## La séquence refondue

Trois séances de 55 min. **145 min annoncés pour 165 disponibles.**

| Séance | Titre | Ce que l'élève produit |
|---|---|---|
| Billet | Trois mots à ne pas confondre — sans note | 3 réponses + aiguillage |
| 1 | **Une fonction, trois principes** (~45 min) | La fonction technique écrite correctement, les trois principes décrits, et le piège de la solution évité |
| 2 | **Comparer avec des chiffres** (~50 min) | Le tableau des six critères exploité, et **ce que chaque critère ne dit pas** |
| 3 | **Choisir pour Sainte-Luce** (~40 min) | Le principe retenu, deux raisons chiffrées, **et ce qu'on accepte de perdre** |
| Bilan | Retour sur l'hypothèse, métacognition, auto-positionnement | ~10 min |

### Le geste propre à ce lot

En 5e, comparer n'est pas classer. La séquence installe **le critère qui tranche** : à Sainte-Luce,
la résistance à la corrosion (embruns) et la distance d'arrêt sous la pluie (descentes) pèsent plus
que la masse ou le prix. Le même tableau, lu pour un collège de montagne sèche, donnerait un autre
gagnant — et c'est **la leçon**, pas un détail.

### Règle n°58 — le réel n'est pas un bonus

Ce lot est le premier à porter une **manipulation obligatoire**, et elle ne coûte rien : un vélo,
n'importe lequel, présent dans le collège ou apporté.

| Version | Matériel | Ce que l'élève fait |
|---|---|---|
| **🅰 Réel** | un vélo, une clé Allen | Actionner le levier, **voir** ce qui serre quoi, mesurer l'écart patin/jante, sentir la différence de force |
| **🅱 Photos** | les deux SVG du lot | Suivre le trajet de l'effort sur un schéma coté |
| **🅲 Sans matériel** | rien | Le récit d'observation est fourni, l'élève l'analyse |

## Les productions attendues, et leur corrigé (règle n°43)

Chaque activité a son champ, son vérificateur, sa correction repliée. Deux corrigés graphiques sont
à produire : **le trajet de l'effort dans les trois principes**, et **le tableau comparatif renseigné
avec le critère qui tranche mis en évidence**.

## Deux routes pour le code 5e_C1.2

Le lot **Chengdu** (5e_C1.1) couvre déjà C1.2 par son activité 1 — trois principes de mesure des
poussières. Les deux coexistent, et le README dira en quoi elles diffèrent (n°66 amendée) :
Chengdu compare des principes **de mesure** dans une chaîne de données ; Sainte-Luce compare des
principes **mécaniques** sur un objet qu'on peut toucher, en contexte martiniquais.
