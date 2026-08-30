# Ce que les banques évaluent vraiment — relevé, et proposition non appliquée

**État : proposition. Rien n'a été renommé.** Ce fichier existe pour qu'une
décision pédagogique soit prise en la voyant, pas en la subissant.

## 1. Pourquoi ce relevé

`controle_statut.py` compte les pièces d'un lot. Six pièces présentes, statut
tenu. Mais six pièces peuvent parler d'autre chose que du code sous lequel
elles sont rangées : le dossier serait plein, la matrice verte, et la preuve de
couverture nulle part.

`controle_couverture.py` pose la seule question qui manquait : **le lot
nomme-t-il le code qu'il prétend couvrir, et où ?** Il répond par un fait, pas
par un verdict.

```
python3 _outils/controle_couverture.py            # 114 codes, un par ligne
python3 _outils/controle_couverture.py --muets    # les cas sans preuve
```

Au 30/08/2026 :

| état | codes | ce que cela veut dire |
|---|---:|---|
| ÉVALUÉ | 45 | au moins 5 questions du QCM du lot portent ce code |
| CITÉ | 15 | le code est écrit dans une séquence, une fiche, une matrice ou une synthèse, mais aucune question ne le porte en nombre suffisant |
| RENVOI | 43 | le code n'apparaît que dans un README, un manifeste ou un lexique — le lot dit où aller, il ne montre rien |
| VIDE | 11 | dossier sans fichier |

Les 43 « RENVOI » ne sont pas une alerte : ils sont, à deux exceptions près,
tenus pour « couverts par une séquence mutualisée », et c'est exactement ce
qu'un renvoi doit être. L'outil lit le statut **tenu** après contrôle de
pièces, pas le statut déclaré dans l'OVERLAY : `4e_C4.2` et `4e_C4.4` sont déjà
reclassés par `controle_statut.py`, et il serait faux de les compter deux fois.

Restent **cinq codes tenus pour complets dont la couverture n'est pas mesurable
dans leur propre lot** :

```
3e_C9.1   CITÉ   0 question  ·  4e_C4.1   CITÉ   0 question
4e_C7.1   CITÉ   0 question  ·  5e_C9.1   CITÉ   0 question
5e_C4.1   CITÉ   4 questions
```

et **une famille de banques** qui explique les cinq, plus trois lots non encore
déclarés.

## 2. La cause : huit banques qui n'étiquettent pas par code

Sept banques étiquettent leurs questions par un mot de thème (`ELA`, `SIM`,
`SEU`…) plutôt que par le code travaillé. Une huitième étiquette par code, mais
répartit 32 questions sur 8 codes — quatre chacun, un de moins que le seuil.

| banque | lot | étiquettes |
|---|---|---|
| `qcm_3e_C7_capteur-confort-ny.html` | 3e_C7.1 | ELA:10 SIM:10 SEU:10 |
| `qcm_5e_C7_mini-projet.html` | 5e_C7.1 | CON:10 VAL:10 PRG:10 |
| `qcm_4e_C7_jardin-conception.html` | 4e_C7.1 | ORG:10 SOL:10 MAT:10 |
| `qcm_4e_C8_jardin-validation.html` | 4e_C8.1 | PAR:10 PRO:10 PER:10 |
| `qcm_4e_C4.1-C4.9_jardin_connecte.html` | 4e_C4.1 | EN:7 ID:10 RES:10 PRO:3 |
| `qcm_3e_C9.1_variables_types_systemes.html` | 3e_C9.1 | VAR:8 TYP:8 PRG:7 MAP:7 |
| `qcm_5e_C9.1-C9.3_boite_etiquetee.html` | 5e_C9.1 | BOI:10 LIR:10 MOD:10 |
| `qcm_5e_C4.1-C4.8_lampadaire_intelligent.html` | 5e_C4.1 | C4.2:4 … C4.8:4 (+ C4.1:4) |

## 3. La proposition, groupe par groupe

Chaque ligne s'appuie sur le texte des questions du groupe, pas sur son nom.
`✓` = atteint le seuil de 5 questions ; `✗` = en dessous.

### 3.1 `qcm_3e_C7_capteur-confort-ny.html` — lot 3e_C7.1

| questions | ce qu'elles travaillent | code proposé | n |
|---|---|---|---:|
| ELA 1–6 | verbe de la 3e, besoin de Mme Reyes, deux critères, estimer une durée, chemin le plus long | **3e_C7.1** | 6 ✓ |
| ELA 7–9 | coque, point faible à l'eau, vue en coupe | 3e_C7.6 | 3 ✗ |
| ELA 10 | formulation d'une compétence CRCN | *hors référentiel* | 1 |
| SIM 11–16 | simuler pour éliminer, seuil, cas frontière, prédire, quatre scénarios, décision | 3e_C8.3 | 6 ✓ |
| SIM 17–19 | clignotement, hystérésis, test discriminant | 3e_C9.1 | 3 |
| SIM 20 | la trace | *hors référentiel* | 1 |
| SEU 21–29 | seuil, algorigramme, losange, condition Python, if/elif/else, boucle, mise au point | 3e_C9.1 | 9 |
| SEU 30 | îlot de chaleur | *sciences* | 1 |

**Bilan** : 3e_C7.1 → 6 ✓ · 3e_C9.1 → 12 ✓ · 3e_C8.3 → 6 ✓ · 3e_C7.6 → 3 ✗.

À noter : la question 11 recopie le verbe de **3e_C8.1** (« mettre en œuvre une
simulation pour valider »), mais 3e_C8.1 porte sur la *tenue mécanique d'un
matériau* — rien dans ce groupe ne concerne la résistance d'un matériau. La
question est étiquetée par sa formulation, pas par son objet.

### 3.2 `qcm_5e_C7_mini-projet.html` — lot 5e_C7.1

| questions | ce qu'elles travaillent | code proposé | n |
|---|---|---|---:|
| CON 1–8 | besoin, preuve chiffrée, deux solutions, critère, planning suivi, retard, ordre des étapes | **5e_C7.1** | 8 ✓ |
| CON 9 | enregistrement et versions dans Onshape | 5e_C1.4 | 1 ✗ |
| CON 10 | export STL en millimètres | 5e_C7.6 | 1 ✗ |
| VAL 11–16 | attendu d'abord, protocole fourni, test qui échoue, trois décisions, comportement/performance, prédire | 5e_C8.3 | 6 ✓ |
| VAL 17–19 | capteur, actionneur, ordre de la chaîne | 5e_C4.5 | 3 ✗ |
| VAL 20 | très basse tension | *sécurité* | 1 |
| PRG 21–30 | règle SI, losange, terminal, boucle, cas oublié, Python, sans LED, mise au point, réinvestissement | 5e_C9.3 | 10 ✓ |

**Bilan** : 5e_C7.1 → 8 ✓ · 5e_C9.3 → 10 ✓ · 5e_C8.3 → 6 ✓.

À noter : la rétention de CON 4 dit « **Organiser**, puis plusieurs idées » —
« organiser » est le verbe de la 4e. En 5e on **suit** un processus. Un mot à
corriger, quelle que soit la décision sur les étiquettes.

### 3.3 `qcm_4e_C7_jardin-conception.html` — lot 4e_C7.1

| questions | ce qu'elles travaillent | code proposé | n |
|---|---|---|---:|
| ORG 1,2,5,6,7,8 + SOL 19 | verbe de la 4e, condition d'Ortiz, diagramme de la démarche, flèche de retour, vraie tâche, tâches parallèles, ce qu'on évalue | **4e_C7.1** | 7 ✓ |
| ORG 3,4 | sonde inutilisable dehors, indice de protection | 4e_C3.1 | 2 ✗ |
| ORG 9,10 | révolution, contrainte d'assemblage | 4e_C7.6 | 2 ✗ |
| SOL 11–18, 20 | deux solutions distinctes, filtre des critères, fonction contradictoire, ouverture, choc, contrainte ou critère, croquis coté, transfert | 4e_C7.2 | 9 ✓ |
| MAT 21–30 | banc météo, trois critères, réemploi, contrainte fatale, le banc contre l'intuition | 4e_C7.3 | 10 ✓ |

**Bilan** : 4e_C7.1 → 7 ✓ · 4e_C7.2 → 9 ✓ · 4e_C7.3 → 10 ✓.

À noter : 4e_C7.3 possède depuis le 30/08 son propre lot (« Écarter, classer,
rouvrir »). Les dix questions MAT en couvriraient donc le code une seconde
fois, par une autre entrée — un doublon utile, pas une erreur.

### 3.4 `qcm_4e_C8_jardin-validation.html` — lot 4e_C8.1

| questions | ce qu'elles travaillent | code proposé | n |
|---|---|---|---:|
| PAR 1–10 | paramétrer la simulation fournie, test raté par le support, attendu tranchable, conformité, trace | **4e_C8.1** | 10 ✓ |
| PRO 11–14, 17–19 | ce qu'est un protocole, exécutable par un autre, écrit avant, étape trop vague, test discriminant, amélioration recevable | 4e_C8.3 | 7 |
| PRO 15,16,20 | le gel qui échoue, l'attache cassée par le froid, rejouer après remplacement | 4e_C8.2 | 3 ✗ |
| PER 21–30 | comportement/performance, attendu en plein soleil, vent, généraliser, hypothèse d'entrée | 4e_C8.3 | 10 |

**Bilan** : 4e_C8.1 → 10 ✓ · 4e_C8.3 → 17 ✓ · **4e_C8.2 → 3 ✗**.

Correction d'un dire antérieur : j'avais écrit que 4e_C8.2 n'était « pas
couvert du tout ». C'est faux — il l'est par trois questions. Trois, c'est en
dessous du seuil ; ce n'est pas rien.

### 3.5 `qcm_4e_C4.1-C4.9_jardin_connecte.html` — lot 4e_C4.1

C'est le cas le plus lourd : neuf codes, trente questions.

| questions | ce qu'elles travaillent | code proposé | n |
|---|---|---|---:|
| EN 1,2,7 | fonction du panneau, de la batterie, pont entre les deux chaînes | 4e_C4.1 | 3 ✗ |
| EN 3,4,5,6 | transformation dans la pompe, trajet des natures, stocker ≠ transformer, trois flux | 4e_C4.2 | 4 ✗ |
| ID 8 | ordre de la chaîne d'information | 4e_C4.4 | 1 ✗ |
| ID 9,10,15,17 | mesure brute, horodatage, téléverser, donnée douteuse | 4e_C4.5 | 4 ✗ |
| ID 11,12,13,14 | une ligne, la colonne capteur, lire un arrosage, trier/filtrer/tracer | 4e_C4.6 | 4 ✗ |
| ID 16 | ce qui fait un objet connecté | *transversal* | 1 |
| RES 18,19,24 | adresse IP, pourquoi fixe, en choisir une sans panne | 4e_C4.7 | 3 ✗ |
| RES 20,21,22,23,25,27 | DHCP, conflit, passerelle, borne débranchée, diagnostic, local ≠ internet | **4e_C4.8** | 6 ✓ |
| RES 26 | s'entraîner sur une simulation | 4e_C4.9 | 1 ✗ |
| PRO 28,29,30 | stries d'impression, ligne de joint, forme + quantité | 4e_C4.3 | 3 ✗ |

**Bilan** : un seul code atteint le seuil — 4e_C4.8. Le lot est pourtant déclaré
« complet et validable » pour 4e_C4.1.

### 3.6 `qcm_3e_C9.1_variables_types_systemes.html` — lot 3e_C9.1

| questions | ce qu'elles travaillent | code proposé | n |
|---|---|---|---:|
| VAR 1–8 · TYP 9–16 | variable, affectation, écrasement, compteur, échange, table de suivi, quatre types, conversions, TypeError | **3e_C9.1** *(prérequis)* | 16 |
| PRG 17–23 | prédire, une correction à la fois, lire l'erreur, ordre des lignes, = ou ==, trace, motifs | **3e_C9.1** | 7 ✓ |
| MAP 24–29 | pourquoi une fonction, élaborer avant de taper, banc de tests, cas limite, non-régression, « fini » | **3e_C9.1** | 6 ✓ |
| MAP 30 | la variable devient commande d'un système réel | 3e_C9.2 | 1 ✗ |

**Bilan** : 3e_C9.1 → 29 ✓. Seule question ouverte : les 16 questions VAR + TYP
sont des *prérequis* (au niveau de 5e_C9.1) et non le geste de 3e_C9.1, qui est
d'élaborer un algorithme et de le traduire en programme structuré. Les compter
gonfle la couverture sans la prouver.

### 3.7 `qcm_5e_C9.1-C9.3_boite_etiquetee.html` — lot 5e_C9.1

| questions | ce qu'elles travaillent | code proposé | n |
|---|---|---|---:|
| BOI 1–10 | variable, =, écrasement, compteur, nommer, afficher ≠ ranger | **5e_C9.1** *(prérequis)* | 10 |
| LIR 11–20 | prédire, tester = comparer attendu et obtenu, plusieurs cas, répondre au besoin | **5e_C9.1** | 10 ✓ |
| MOD 21–26, 28, 29 | la bonne ligne, retester après, condition, test frontière, > ou >=, une ligne = un réglage | 5e_C9.2 | 8 ✓ |
| MOD 27, 30 | commander le réel, la démarche complète | 5e_C9.3 | 2 ✗ |

**Bilan** : le nom du fichier annonce `C9.1-C9.3`. C9.3 est effleuré par deux
questions. Le fichier promet plus qu'il ne tient.

### 3.8 `qcm_5e_C4.1-C4.8_lampadaire_intelligent.html` — lot 5e_C4.1

Cette banque est déjà étiquetée par codes réels, honnêtement : huit codes,
trente-deux questions, **quatre chacun**. Aucun n'atteint le seuil de cinq.

Ce n'est pas une négligence, c'est une conséquence arithmétique : un lot
mutualisé qui couvre huit codes avec une banque de trente questions ne *peut
pas* donner cinq questions à chacun. Le seuil et la mutualisation se
contredisent.

## 4. Ce qu'il faut arbitrer

Trois décisions, et elles ne se déduisent d'aucun contrôle.

1. **Le seuil face aux lots mutualisés.** Cinq questions par code est le seuil
   d'évaluabilité de `controle_echantillonnage.py`. Un lot qui couvre huit
   codes ne peut pas le tenir. Faut-il un seuil qui dépend du nombre de codes
   portés par le lot (par exemple `min(5, 30 // nombre_de_codes)`), ou faut-il
   accepter qu'un code mutualisé ne soit pas « évaluable seul » et le dire ?

2. **Les prérequis.** VAR, TYP, BOI — 26 questions au total — enseignent ce
   sans quoi le geste du code est impossible, mais ne sont pas ce geste.
   Les étiqueter du code du lot gonfle la couverture ; les étiqueter d'un code
   d'un autre niveau ment sur le niveau. Une troisième voie serait une
   étiquette explicite `3e_C9.1:prérequis`, comptée à part.

3. **Les codes sous le seuil après relabellisation.** 4e_C8.2 (3), 3e_C7.6 (3),
   5e_C4.5 (3), 4e_C4.3 (3), 4e_C4.7 (3), 4e_C4.1 (3), 4e_C4.2 (4),
   4e_C4.5 (4), 4e_C4.6 (4). Deux issues par code : écrire les questions qui
   manquent, ou retirer la revendication.

Tant que ces trois points ne sont pas tranchés, **rien n'est renommé**. Une
étiquette fausse rendrait l'audit faussement sûr de lui, ce qui est pire que
l'imprécision actuelle, qui au moins se voit.
