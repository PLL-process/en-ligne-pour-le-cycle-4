# 3e_C2.1 — Pékin : trois destinataires, trois représentations

Troisième et dernier lot du **C2**. Avec lui, la compétence est couverte sur les **trois niveaux**
du cycle.

➡ **[Séquence complète](sequence_3e_C2_pekin_borne.html)** — 3 séances de 55 min. Un rapport tient
en une ligne : « un usager sur cinq abandonne devant la borne ». Le chiffre est exact — et il ne dit
à **personne** ce qu'il faudrait faire, parce qu'il n'a été mis en forme **pour personne**.

➡ **[QCM d'entraînement](qcm_3e_C2_pekin_borne.html)** — 30 questions, dont 5 illustrées, chaque
distracteur réfuté. Il s'ouvre sur un parcours court tant que la séquence n'est pas finie (n°45).

➡ Synthèses : [élève](Synthèses/synthese_eleve_3e_C2.1.html) ·
[professeur](Synthèses/synthese_professeur_3e_C2.1.html)

➡ [Fiche pédagogique](fiche_pedagogique_3e_C2.1.md) ·
[Matrice](matrice_couverture_3e_C2.1.csv) · [Rapport de tests](rapport_tests_3e_C2.1.md) ·
[Sources des médias](SOURCES_MEDIAS.md) · [Plan du lot](PLAN_LOT_C2_3e.md)

➡ Données **simulées** :
[`observations_borne_pekin_simulees.csv`](observations_borne_pekin_simulees.csv) (40 usagers) ·
[`verbatims_usagers_pekin_simules.csv`](verbatims_usagers_pekin_simules.csv) (8 verbatims) ·
[`incidents_maintenance_pekin_simules.csv`](incidents_maintenance_pekin_simules.csv) (3 incidents)

➡ [`_generation/`](_generation/) — les 30 questions du QCM (`q.py`) et le générateur qui les injecte
dans le gabarit maison (`build_qcm.py`).

## ⚙️ Deux façons de conduire cette séquence

Le référentiel écrit « à l'aide de modes de représentation **choisis** » — **sans dire par qui**.
Les deux lectures sont recevables : modes choisis *par l'élève*, ou *sélectionnés* par l'enseignant.

La séquence retient la première et **le dit à l'élève**. Mais les six modes étant tous traités et
tous corrigés, **vous pouvez conduire l'autre** : imposez l'appariement en début d'activité 2, et
gardez la justification et la défense. Le geste difficile n'a jamais été de choisir — il a toujours
été de **justifier**.

## Le résultat que les données produisent seules

« Un usager sur cinq abandonne » : exact — 8 sur 40. En détaillant :

| habitués | occasionnels | poussette | touristes | personnes âgées |
|---|---|---|---|---|
| **0 %** | 11 % | 25 % | **43 %** | **50 %** |

Ce ne sont pas 20 % des gens qui échouent au hasard : ce sont **toujours les mêmes**. Et la durée
moyenne — 77 s — ne décrit personne : l'habitué met 41 s, la personne âgée 123 s.

La phrase qui reste : **ceux qui décident sont presque toujours des habitués, et les habitués
réussissent.**

## ⚠️ À lire avant d'utiliser le lot en classe

**Ne sautez pas le vocabulaire.** Six modes, dont *storyboard* et *carte d'empathie*, qui ne sont
pas des mots de collège. L'activité 2 s'ouvre sur six appariements, et le vérificateur refuse
d'aller plus loin tant qu'ils ne sont pas tenus : un élève qui ignore ce qu'est une carte d'empathie
ne la choisira jamais, et son « choix » se réduira à ce qu'il connaissait déjà.

**Codes de classement.** `3e_C2.1` est un code **interne à ce dépôt**. La référence normative est le
programme de technologie du cycle 4, BO n°9 du 29 février 2024 — et la formulation de la carte du
référentiel en est recopiée, non reformulée (règle n°42).

## La marche du C2, écrite à l'élève

| | Ce que l'élève faisait | Ce qui changeait |
|---|---|---|
| [5e — Shenzhen](../../5e/5e_C2.1/README.md) | il recensait les interacteurs, repérait les choix | il regardait l'objet **du dehors** |
| [4e — Hangzhou](../../4e/4e_C2.1/README.md) | il décrivait un vécu et le traduisait | l'itinéraire lui était **donné** |
| **3e — ici** | il décrit un vécu et **choisit** la forme | il **décide**, et il **défend** |

C'est le premier lot du dépôt qui achève une compétence dont les deux autres niveaux existent déjà.
La marche est donc écrite **à l'élève**, dans la séquence — pas seulement dans la fiche du
professeur.

## Ce que l'élève doit savoir dire à la fin

Qu'un **chiffre agrégé peut être exact et inutilisable**. Qu'une moyenne sur un groupe varié
**décrit une personne qui n'existe pas**. Qu'un **mode n'est jamais bon en soi — il est bon pour
quelqu'un**. Qu'on le justifie par son **angle mort**, pas par son point fort. Qu'un **défaut
d'ordre** ne se voit que sur un algorigramme. Et que **représenter, c'est choisir ce qu'on montre,
donc aussi ce qu'on cache**.

## 🎓 Lien DNB

L'activité 3 fait produire un algorigramme et y repérer un **test mal placé** : c'est un geste
attendu à l'épreuve de sciences et technologie. Il est ici l'outil qui convient au technicien, pas
un exercice de bachotage.

*Lot Thème 1 · 3e — un mode n'est jamais bon en soi, il est bon pour quelqu'un.*
