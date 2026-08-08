# Fiche pédagogique — 5e_C1.1 à C1.6 « Chengdu : le collège qui mesure son air »

**Niveau** 5e · **Thème 1** · **Durée** 5 séances de 55 min (215 min annoncés pour 275)
**Matériel** aucun — page autonome hors ligne ; un tableur utile en séance 2, **mais pas nécessaire**
**Ce lot couvre les six codes du C1 en 5e dans une seule séquence.**

## Où ce lot se situe sur la chaîne d'analyse (règle n°64)

Il n'est pas sur la chaîne de l'analyse fonctionnelle — il est **en amont de tout** : il porte sur la
**donnée elle-même**, celle dont l'analyse se nourrira ensuite. Un cahier des charges qui s'appuie
sur des mesures sales est un cahier des charges faux. C'est la place du C1 : ce qui rend le reste
possible, et qu'on saute d'habitude.

## Pourquoi six codes dans un seul lot

Ce n'est pas une commodité de découpage, c'est la thèse de la séquence. **Une même donnée** — le
relevé du capteur de la cour — les traverse tous les six :

| Code | Formulation du référentiel (recopiée, règle n°42) | Séance | Le verbe (n°65) |
|---|---|---|---|
| **C1.2** | Comparer des principes techniques pour une même fonction technique. | 1 | comparer, puis **renoncer** |
| **C1.1** | Collecter, trier et analyser des données. | 2 | **nettoyer** avant de calculer |
| **C1.4** | Recenser des données, les identifier, les classer, les représenter, les stocker, les retrouver dans une arborescence. | 3 | **renommer**, pas seulement ranger |
| **C1.3** | Décrire le rôle des systèmes d'information dans le partage d'information. | 4 | décrire un chemin **et ses droits** |
| **C1.5** | Identifier des règles permettant de sécuriser un environnement numérique (bases de la cybersécurité) et des règles de respect de la propriété intellectuelle. | 5 | dire ce que chaque mesure **empêche** |
| **C1.6** | Appréhender la responsabilité de chacun dans les dérives (cyberviolence, atteinte à la vie privée, aux données personnelles, usurpation d'identité). | 5 | **arbitrer** ce qu'on publie |

Traités séparément, ces six codes donnent six leçons sans rapport. Tenus par un seul objet, ils
disent une chose que les élèves ne soupçonnent pas : **entre le capteur et la décision, il n'y a que
des choix humains** — et chacun peut se tromper.

**Socle** : D1.3 (tableau, graphique, schéma), D2 (organiser, retrouver, sauvegarder),
D3 (responsabilité, vie privée). Déclarés seulement là où une production le prouve (règle n°60) :
le relevé écrit, l'arborescence proposée, la publication rédigée.

## Le déroulé

| Séance | Titre | Durée | Production évaluée |
|---|---|---|---|
| Billet | Vérifier ses trois outils — **sans note** | 5 min | aiguillage seul |
| 1 | Une fonction, trois principes | 40 min | principe retenu, deux raisons chiffrées, **et ce qu'on accepte de perdre** |
| 2 | Collecter, trier, analyser | 45 min | les quatre anomalies **et** les deux moyennes |
| 3 | Ranger, et retrouver | 35 min | arborescence renommée **et** trois règles de nommage |
| 4 | Le chemin de la donnée | 35 min | les quatre étages **et** qui écrit à chacun |
| 5 | Protéger, puis répondre | 45 min | trois mesures, puis la publication et **ce qu'elle écarte** |
| Bilan | Retour sur l'hypothèse, métacognition, auto-positionnement | 10 min | — |

## ⚙️ Le tableur est un outil, pas la compétence (règle n°59)

L'activité 2 offre **deux chemins vers la même exigence** :

| | Ce que l'élève fait | Ce qui reste identique |
|---|---|---|
| **🔵 Autonome** | ouvre le CSV, trie, calcule les deux moyennes | les quatre anomalies, les deux moyennes, le raisonnement |
| **🟢 Guidé** | lit un extrait déjà sorti du fichier, moyennes fournies | **exactement les mêmes** |

Le chemin guidé retire le calcul, pas le raisonnement — le vérificateur exige la même chose des
deux. C'est aussi le repli le jour où la salle informatique tombe.

Les modes opératoires sont donnés pour **LibreOffice Calc et Excel** : les formules sont les mêmes,
seuls les menus changent. C'est vrai de presque tout le tableur, et la page le dit à l'élève.

## Les quatre anomalies plantées dans le fichier

Elles ne sont pas là pour piéger : chacune enseigne une famille d'erreur différente.

| Anomalie | Ce qu'elle apprend |
|---|---|
| **−4,2** mercredi 11 h | une valeur **hors du domaine physique** n'est pas une mesure |
| **23,7 six fois** vendredi | la valeur est plausible, c'est sa **répétition** qui ne l'est pas |
| **lundi 14 h manquant** | une case vide **se signale**, elle ne se remplit pas |
| **251,0** dimanche | l'erreur de **saisie** : virgule décalée, 25,1 devenu 251 |

Moyenne avec : **27,4**. Sans : **25,2**. Moins de 5 % des lignes déplacent le résultat de 9 %.

Et un fait pédagogique qui n'est pas une anomalie : mardi et jeudi à 7 h, **66,8 et 68,8** contre
26-28 les autres jours. C'est le pic qui sert la séance 5.

## Où ça résiste

**Séance 1** — les élèves cherchent « le meilleur » principe et refusent qu'il dépende de l'usage.
Insister sur le délai (la gravimétrie est la plus précise et la plus inutile ici) et sur le critère
qui **élimine** au lieu de peser (la source radioactive).

**Séance 2** — trois anomalies sortent au tri. La quatrième résiste : on ne cherche pas une valeur
bizarre, on cherche un **comportement** bizarre.

**Séance 3** — beaucoup d'élèves déplacent « truc.csv » dans un beau dossier et s'arrêtent là. Le
vérificateur refuse : un fichier mieux placé mais toujours nommé « final » reste introuvable.

**Séance 4** — les quatre étages viennent seuls ; les **droits** ne viennent pas du tout. C'est la
moitié de la consigne, et celle qu'on oublie.

**Séance 5** — les élèves voient vite que la publication A est inacceptable. Beaucoup moins que la B,
prudente, ne sert à rien. Et presque aucun ne voit que **retirer le nom ne suffit pas**.

## ⚠️ Deux précautions de conduite

**L'agent d'entretien n'existe pas** — toutes les données sont simulées, et le dossier le dit. Mais
dans votre collège il y a une personne réelle qui passe la balayeuse. Si un élève la nomme, c'est
**exactement le moment de la séquence** : ne le reprenez pas, demandez-lui de relire la publication A.

**Ne transformez pas la séance 5 en leçon de morale** — les trois publications sont **toutes vraies**.
Si la classe conclut « il ne faut rien publier », la publication B a gagné et l'objectif est manqué.

## Ce que ce lot ne fait pas encore (règle n°47)

- **Aucune manipulation d'un objet réel** — le programme la recommande, la règle n°58 l'exige
  désormais. Geste manquant identifié : relever une semaine avec un capteur du collège, ou à défaut
  un thermomètre, et confronter le réel au fichier simulé.
- **La donnée est traitée, jamais produite** — l'élève nettoie un fichier rempli par quelqu'un
  d'autre. Cohérent avec C1.1, et une marche de moins que ce que la discipline vaut.
