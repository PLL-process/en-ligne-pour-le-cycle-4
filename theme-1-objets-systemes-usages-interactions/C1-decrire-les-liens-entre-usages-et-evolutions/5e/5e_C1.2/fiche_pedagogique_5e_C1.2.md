# Fiche pédagogique — 5e_C1.2 « Sainte-Luce : quel frein pour les vélos du collège ? »

**Niveau** 5e · **Thème 1** · **Durée** 4 séances de 55 min (185 min annoncés pour 220 : séance 1 5 + 40,
séance 2 50, séance 3 40, séance 4 15 + 25 + 10)
**Matériel** un **vélo** (manipulation obligatoire, séance 1) et une clé Allen · un tableur, utile
mais **pas nécessaire** en séance 2

> **24/10/2026 — une séance 4 de 55 min, faite d'exercices** (demande du professeur). La clôture
> (Bonus → Bilan → QCM) y passe ; la séance 3 garde l'activité 3 seule (40 min). La séance 4
> accueille l'exercice de l'atelier FAST de 5e « Deux principes pour une même fonction » (activité 4)
> et une activité écrite pour la séquence, « Léa dans la grande descente » (activité 5).

## Où ce lot se situe sur la chaîne d'analyse (règle n°64)

Sur le versant **analyse externe**, juste avant le cahier des charges : on compare des principes
pour une fonction déjà énoncée. Ce qui vient après — décomposer en fonctions techniques avec un
FAST — relève du Thème 2. La séance 4 en **lit** seulement un extrait, pour voir deux principes
d'une même fonction écrits dans deux cases reliées par « ou » ; le construire reste au Thème 2.

## Le référentiel

`5e_C1.2` — *Comparer des principes techniques pour une même fonction technique.*
**Socle** : D1.3 (lire et exploiter un tableau de mesures) · D4 · D5.
**CRCN 1.3** — traiter des données. **La trace est le classeur `comparatif_freinage_groupeXX`
produit dans l'activité CRCN du lot** (`activite_crcn_donnees_freinage_5e_C1.2.html`, atteinte depuis
l'index) : une colonne insérée, des priorités saisies, un tri, un filtre — des transformations
visibles dans un fichier conservé (règle n°60). Le relevé écrit de l'activité 2 atteste la
lecture du tableau, pas le traitement numérique : seul, il ne suffit pas à cocher CRCN 1.3
(audit externe du 08/09, point A17).

Le mot difficile du référentiel n'est pas « principe » : c'est **« comparer »**. Comparer n'est ni
préférer, ni classer, ni compter les colonnes gagnées — c'est **hiérarchiser des critères selon un
contexte**, et assumer ce qu'on perd.

## Le verbe du niveau (règle n°65)

| | Le geste |
|---|---|
| **5e — ici** | **comparer** des principes, et justifier un choix par le contexte |
| 4e | **formuler** des exigences vérifiables, avec critères et niveaux |
| 3e | **arbitrer** entre des exigences incompatibles |

## Le déroulé

| Séance | Titre | Durée | Production évaluée |
|---|---|---|---|
| Billet | Trois mots à ne pas confondre — **sans note** | 5 min | aiguillage seul |
| 1 | **Une fonction, trois principes** | 40 min | un relevé d'observation en trois lignes + 5 appariements |
| 2 | **Comparer avec des chiffres** | 50 min | six critères, meilleur et moins bon, **et ce que le tableau ne dit pas** |
| 3 | **Choisir pour Sainte-Luce** | 40 min | un principe, **deux raisons chiffrées**, et **une perte assumée** |
| 4 | **Conseiller** — act. 4 : le vélo-cargo de Léa, deux principes dans un FAST (exercice de l'atelier FAST 5e) | 15 min | cinq propriétés rangées, un choix, une phrase (vérifié par l'exercice, clé `rep_fast_5e_e3`) |
| 4 | act. 5 : **Léa dans la grande descente** — conseiller avec des chiffres | 25 min | un frein, **deux chiffres**, **une perte**, et ce qui distingue Léa du collège |
| Bilan | (séance 4) Retour sur l'hypothèse, métacognition, auto-positionnement | 10 min | — |

## 🔧 La manipulation — au parcours obligatoire (règle n°58)

C'est la première du dépôt à ne pas être un bonus. Elle demande un vélo, cinq minutes, et rien
d'autre. Le vélo reste **à l'arrêt**, tenu par un camarade ; **on ne démonte rien**.

| Version | Matériel | Ce que l'élève fait |
|---|---|---|
| **🅰 Réel** | un vélo, une clé Allen | actionne le levier, observe ce qui serre quoi, mesure l'écart au repos |
| **🅱 Photos** | les schémas de la page | suit le trajet de l'effort sur le schéma |
| **🅲 Sans matériel** | rien | analyse un relevé d'observation fourni |

Les trois mènent à la même production et sont validées par le **même** vérificateur.

**Ce qu'elle apporte et qu'aucun schéma ne remplace** : l'élève voit que la surface qui frotte, sur
un frein à patins, est **la roue elle-même** — celle qui roule dans les flaques. Il en déduit seul
la faiblesse sous la pluie, **avant** d'ouvrir le tableau. Le chiffre confirme alors une intuition
au lieu d'être appris.

## Les données

| Fichier | Contenu | Ce qu'il apporte |
|---|---|---|
| `donnees_freinage_sainte_luce_simulees.csv` | 3 solutions × 6 critères | le tableau de comparaison |
| `releves_essai_college_sainte_luce_simules.csv` | 15 freinages chronométrés | **la fiche en est la moyenne exacte** — donc vérifiable |

Toutes **simulées** et **déterministes** (règle n°48). L'écart sec/pluie vaut **+3,1 m** pour les
patins, **+1,0 m** pour le disque, **+0,8 m** pour le tambour : c'est là que le choix se joue.

**Séance 4 — le tableau du vendeur de Léa**, écrit dans la page (pas de fichier) et déclaré simulé à
l'élève : vélo-cargo chargé à environ 150 kg, lancé à 18 km/h comme les vélos du collège.

| Frein | Sec | Pluie | Freins chauds (bas de la grande descente, sec) | Masse | Entretien |
|---|---|---|---|---|---|
| Patins | 7,5 m | 11,6 m | 8,2 m | 320 g | 18 €/an |
| Disque | 7,0 m | 8,3 m | 7,5 m | 510 g | 34 €/an |
| Tambour | 7,9 m | 9,1 m | 10,4 m | 760 g | 27 €/an |

Construit pour rester cohérent avec le collège : masses et entretien inchangés (ce sont des
propriétés du frein), distances plus longues avec la charge, écarts sec/pluie plus grands
(+4,1 / +1,3 / +1,2 m), et l'essai 15 du collège (« chauffe en fin de descente ») qui devient ici un
critère. Seul l'ordre des grandeurs physiques est affirmé : l'énergie à dissiper est proportionnelle
à la masse (cinétique ½mv², de position mgh), d'où le facteur 150 ÷ 60 = 2,5 ; un frein dont la
chaleur reste enfermée perd de son efficacité quand il chauffe (l'« évanouissement » du freinage).

## Où ça résiste

**Séance 1** — la distinction fonction / principe / solution se dit en trois minutes et se perd en
trois jours. Le test qui la fixe : *si la phrase reste vraie pour les trois freins, c'est une
fonction ; si elle n'est vraie que pour un type, c'est un principe ; si elle désigne un article de
catalogue, c'est une solution.* Le vérificateur exige **les deux** pièces qui frottent — beaucoup
écrivent « le patin frotte » et s'arrêtent.

**Séance 2** — deux difficultés distinctes. Savoir dans quel sens se lit chaque colonne (mécanique).
Et comprendre que le tableau donne les **faits**, pas leur **importance** (conceptuel, et beaucoup
plus dur). C'est la dernière phrase attendue, et c'est elle qui bloque.

**Séance 3** — le vérificateur **refuse** le frein à patins et lui dit pourquoi, en chiffres, en
renvoyant au Bonus 1 où ce même choix devient le bon.

**Séance 4** — difficulté attendue (pas encore observée en classe) : recopier le choix de la
séance 3. Pour Léa, le vérificateur **refuse le
tambour** (10,4 m freins chauds, presque 3 m de plus que le disque) et les patins (11,6 m sous la
pluie). Ici une seule réponse tient — le disque — et c'est voulu : le contraste avec les deux
réponses défendables du collège porte la leçon (« le même raisonnement, un autre usage, une autre
réponse »). Le calcul 150 ÷ 60 = 2,5 est de la proportionnalité de 5e ; la masse du frein
(440 g sur 150 kg) montre qu'un critère peut presque disparaître quand l'usage change.
L'activité 4 ne se valide qu'une fois l'exercice inséré réussi : sa sauvegarde est celle de
l'atelier FAST, partagée avec lui et avec le cahier de 5e ; « Effacer ma sauvegarde » de la
séquence ne l'efface pas.

## ⚠️ Deux précautions

**Ne tranchez pas entre le disque et le tambour.** Les deux sont défendables. Si la classe attend
« la » bonne réponse, l'objectif est manqué : ce qui s'évalue est la qualité de la défense.

**Le Bonus 1 n'est pas un supplément** — c'est lui qui achève la leçon. Le même tableau, à
Fort-de-France, désigne les patins. Si le temps manque, faites-le **à l'oral en deux minutes**
plutôt que de le sauter.

## Deux routes vers ce code

Le lot **Chengdu** (5e_C1.1) couvre aussi C1.2, par son activité 1 : trois principes **de mesure**
des poussières, sans objet à toucher, dans une séquence de six codes. **Sainte-Luce** compare des
principes **mécaniques**, sur un objet qu'on manipule, en contexte martiniquais. Si vous ne faites
qu'une seule des deux, Sainte-Luce est la plus complète sur ce code.

## Ce que ce lot ne fait pas (règle n°47)

- **Les mesures sont fournies, pas relevées par les élèves.** Un prolongement naturel : refaire deux
  ou trois freinages dans la cour, au décamètre.
- **Le prix d'achat n'apparaît pas**, seulement le coût d'entretien — volontairement : il aurait
  écrasé la discussion.
- **Le QCM n'a pas changé** avec la séance 4 : ce qu'elle mobilise y est déjà (l'énergie devient
  chaleur, le revers du tambour fermé, la pente change tout, le même tableau ailleurs). Elle n'y
  ajoute pas de question sur le diagramme FAST, qui a son propre QCM dans l'atelier.
