# Fiche pédagogique — 4e_C7.4 « De quoi vit le jardin connecté »

> **Comparer différentes sources d'énergie pour choisir la plus adaptée.**
> Programme 2024 · cycle 4 · thème 3 · socle D1.3 · D2 · D4 · D5

| | |
|---|---|
| **Niveau** | 4e |
| **Code principal** | 4e_C7.4 — 20 questions de QCM |
| **Code d'appui** | 4e_C3.1 — *Identifier les caractéristiques à prendre en compte dans le choix d'un OST en vue de répondre à un besoin.* — 10 questions |
| **Durée** | 2 séances de 55 min — 100 min d'activités obligatoires |
| **Matériel** | un navigateur, hors ligne. Aucune installation, aucun compte. |
| **Version A** | montage réel + multimètre en série ; les mesures remplacent alors le banc |

---

## 1. Le pari didactique

Le verbe du code est **comparer**. Faire choisir sans grille n'évalue rien : tous
les élèves désignent le secteur, et personne n'a comparé. Le lot rend donc la comparaison
**nécessaire** en installant deux surprises que seul le banc peut lever.

**Première surprise :** la pompe, gros consommateur évident, pèse **0,4 %** ; la carte,
qui ne fait rien 99 % du temps, pèse **92 %**. L'intuition est démentie en trois clics.

**Seconde surprise, activité 4 :** comparer les sources finit par obliger à regarder la
**charge**. Avec une carte sobre, le besoin tombe de 5,87 à 1,07 Wh et le panneau qui perdait
toutes les comparaisons devient le meilleur. On croyait choisir une source ; on a changé le
problème.


## 2. Déroulé

| # | Activité | Durée | Réponses attendues | Verrou expérientiel |
|---|---|---|---|---|
| 0 | FAIRE d'abord : qui vide vraiment la source | ~15 min | 3 | compare |
| 1 | Écrire les critères AVANT de comparer | ~20 min | 9 | — |
| 2 | Remplir la grille de comparaison | ~20 min | 6 | srcAll |
| 3 | Trancher, et assumer ce qu'on écarte | ~20 min | 4 | — |
| 4 | Et si on changeait la charge plutôt que la source | ~15 min | 3 | — |
| — | REFAIRE | ~10 min | 1 | — |

## 3. Ce que le montage consomme

| Ce qui consomme | Courant | Par jour | Énergie | Part |
|---|---|---|---|---|
| Carte Arduino UNO | 45 mA | 24 h | 5,400 Wh | 92,0 % |
| Capteur d'humidité du sol | 2 mA | 24 h | 0,240 Wh | 4,1 % |
| Écran LCD RGB | 40 mA | 1 h | 0,200 Wh | 3,4 % |
| Pompe immergée 5 V | 300 mA | 60 s | 0,025 Wh | 0,4 % |
| Module relais | 70 mA | 60 s | 0,006 Wh | 0,1 % |
| **Total** | | | **5,87 Wh** | 100 % |

## 4. Ce que les sources donnent

| Source | Énergie disponible | Face à 5,87 Wh/jour |
|---|---|---|
| Pile 9 V alcaline | 2,8 Wh | 11 heures |
| 4 piles AA alcalines | 12,5 Wh | 2,1 jours |
| Accu Li-ion 18650 rechargeable | 9,4 Wh | 38 heures |
| Secteur — adaptateur USB scellé | illimitée | tant qu'il y a du réseau |
| Panneau solaire 1 W crête + accu | 3,2 Wh/jour | **ne suffit pas** (−2,67 Wh/jour) |

Tout est recalculé par [`energie.py`](energie.py), livré dans le dossier. Le rendement d'un
régulateur linéaire y vaut V<sub>sortie</sub> ÷ V<sub>entrée</sub> — c'est de la physique, pas
un réglage : il dissipe la différence en chaleur. Ensoleillement retenu pour New York (le jardin
est à Brooklyn) : 4,5 heures équivalent plein soleil par jour en moyenne annuelle, panneau fixe
incliné de 20° plein sud, avec 30 % de pertes de chaîne. Le panneau 2 W de la correction récolte
donc 6,3 Wh par jour : il tient les 5,87 Wh, de peu. Source : NREL, PVWatts v8 (base NSRDB), pour
40,71° N, 74,01° O, relevé par [thegreenwatt.com](https://www.thegreenwatt.com/new-york-peak-sun-hours/) ;
recoupement à plat, 3,93 kWh/m²/jour en moyenne (NREL, via
[solarscope.io](https://solarscope.io/solar-data/new-york/new-york-city)).

## 5. Sécurité

Très basse tension **5 V** partout. Le « secteur » de la liste est un **adaptateur USB fermé** :
on ne l'ouvre pas, on ne le modifie pas, on ne coupe pas son câble. Côté élève, il n'y a que du
5 V. Piles et accus : jamais de court-circuit, jamais percés, jamais chauffés ; bac de collecte
en fin de vie.

## 6. Différenciation

* **🅰 avec le matériel** — montage réel, multimètre en série. Les valeurs mesurées remplacent
  celles du banc, et ce sont elles qui font foi.
* **🅱 avec le banc de la page** — hors ligne, sans installation. Seule voie qui permette
  d'éteindre un consommateur pour voir ce qu'il pesait.
* **🅲 sans écran** — les tableaux s'impriment, toutes les valeurs sont dans les corrections.

## 7. Ce que ce lot ne fait pas

* **Aucune mesure réelle.** Les 45 mA de la carte sont une valeur usuelle : une UNO réelle mesurée au multimètre peut en donner 35 ou 60. Le défi bonus « mesure » demande justement l'écart.
* **Les 5 mA de la carte sobre sont une hypothèse d'étude.** La correction dit explicitement qu'une UNO complète ne descend pas sous 30 mA à cause de sa DEL d'alimentation et de son composant USB : c'est la carte qu'il faudrait changer.
* **Le coût annuel est un ordre de grandeur.** Prix indicatifs, hors remises et hors transport.
* **La grille ne pondère pas les critères.** C'est volontaire : la hiérarchisation est le travail de l'activité 3, et une question de QCM y est consacrée.

## 8. Prolongements


  **💰 Défi coût réel :** compare, sur **quatre années scolaires**, le coût total des
  quatre piles AA (4,00 € le jeu, 2,1 jours d'autonomie) et celui du panneau 2 W (15 €, plus un
  accu à 8 € tous les trois ans). À partir de quel mois le panneau devient-il moins cher ?
  **🔍 Défi mesure :** avec un multimètre en série, mesure le courant réel de ta carte au
  repos. Est-il de 45 mA ? Écris l'écart, et une raison possible.
  **❄ Défi hiver :** le banc compte 4,5 heures d'équivalent plein soleil en moyenne
  annuelle. Cherche ce que devient ce chiffre en décembre à New York, et dis de combien il
  faudrait grossir l'accu ou le panneau pour passer une semaine de décembre.
  *Corrigé, pour le professeur :* en décembre, environ **2,4 heures** sur un panneau incliné,
  **1,75** à plat (kWh/m²/jour) : deux fois et demie moins qu'en juillet sur le panneau incliné
  (6,15 heures), plus de trois fois moins à plat (5,85). Le
  panneau 2 W ne récolte plus que 2 × 2,4 × 0,7 ≈ 3,4 Wh par jour pour 5,87 : il manque
  environ 2,5 Wh chaque jour, soit 17,6 Wh sur la semaine — deux accus 18650 de plus
  (9,4 Wh utiles chacun). Ou un panneau d'au moins 5,87 ÷ (2,4 × 0,7) ≈ 3,5 W crête.


## 9. La skill `arduino-grove-college`, et ce qui est sans objet ici

Cette skill impose **20 éléments** à toute séquence mettant en jeu une carte, un capteur ou un
actionneur. Ce lot met bien une carte en jeu — mais **rien n'y est programmé** : on choisit une
source d'énergie, on ne code pas. Plutôt que d'ignorer la skill en silence, voici la lecture
retenue, ligne par ligne.

| Élément de la skill | Ici |
|---|---|
| Rôle de chaque composant | **tenu** — chaque ligne du banc nomme le composant et son courant |
| Chaîne d'énergie | **tenue** — c'est l'objet même de la séquence |
| Versions A / B / C étiquetées | **tenues** — matériel réel, banc de la page, sans écran |
| Solution sans matériel | **tenue** — la version 🅲 se fait entièrement sur papier |
| Sécurité TBT, EPI, gestes interdits, arrêt | **tenue** — encadré dédié, jamais de secteur manipulé |
| QCM | **tenu** — 30 questions, 90 réfutations |
| Grille d'évaluation | **tenue** — repères LSU dans la synthèse professeur |
| Approfondissement | **tenu** — trois défis bonus |
| Photo / SVG du matériel | **partiel** — le banc figure les consommateurs, pas les modules |
| Tableau des broches, niveaux logiques, type des signaux | **sans objet** — aucun câblage n'est demandé |
| Algorithme, algorigramme, programme par blocs, C++ ligne par ligne | **sans objet** — rien n'est programmé |
| Moniteur série, test progressif, dépannage | **sans objet** — il n'y a pas de programme à mettre au point |
| Chaîne d'information | **sans objet** — la séquence porte sur la chaîne d'énergie |

Autrement dit : **les éléments matériels et de sécurité sont tenus, les éléments de programmation
sont sans objet.** Cette liste est écrite ici pour qu'on puisse la contester — pas pour clore le
sujet.

## 10. Fichiers du lot

```
4e_C7.4/
├── sequence_4e_C7.4_energie-du-jardin.html
├── qcm_4e_C7.4_energie-du-jardin.html
├── lexique_4e_C7.4.html
├── synthese_eleve_4e_C7.4.html
├── synthese_professeur_4e_C7.4.html
├── fiche_pedagogique_4e_C7.4.md
├── matrice_couverture_4e_C7.4.csv
├── rapport_tests_4e_C7.4.md
├── tests_4e_C7.4_sequence.mjs · tests_4e_C7.4_qcm.mjs · reponses_4e_C7.4.json · tests_regle_311_4e_C7.4.mjs
└── energie.py
```

## Découpage en séances à onglets (04/11/2026, vague de la règle d'or n°311)

La page était d'un seul tenant ; elle a maintenant deux séances à onglets, sur le modèle du pilote 4e_C8.1 et de la vague C8. Les blocs sont déplacés, pas réécrits ; le nombre de séances annoncé (2 × 55 min) ne change pas.

| Séance | Question directrice | Contenu | Temps annoncé |
|---|---|---|---|
| 1 — Mesurer, écrire les critères, comparer | Qu'est-ce qui vide vraiment la source, et comment comparer cinq sources avec les mêmes critères ? | Ouverture, activités 0, 1 et 2 | ouverture + 15 + 20 + 20 min |
| 2 — Trancher, changer la charge, conclure | Laquelle choisir — et faut-il changer la source, ou la charge ? | Activités 3 et 4, réinvestissement, synthèse, Bonus (corrigé par défi), bilan, QCM | 20 + 15 + 10 min + clôture |

**À trancher par Pascal :** la séance 1 porte l'ouverture et 55 min d'activités (l'autre coupe, après l'activité 1, laissait 65 min à la séance 2).

Dès la séance 2, l'ouverture (étiquettes, « Avant de commencer », situation, problématique et idée de départ, sécurité, trois façons, billet d'entrée) est repliée dans le volet « 📖 Rappel » ; elle est complète à la séance 1. L'en-tête de la séance 2 rappelle en une ligne la consigne de sécurité de la carte, et renvoie au volet. Restent visibles à chaque séance : le titre, la mission (elle remplace le sous-titre « Thème 3 · 4e — … », comme au pilote), la barre d'outils (🖨 Imprimer / PDF, que la page n'avait pas) et **le banc d'énergie**, qui sert aux deux séances : un seul bloc ; à la séance 1, il reste à sa place, dans l'activité 0 ; dès la séance 2, le script des onglets le place juste après l'en-tête de la séance ouverte. Sans JavaScript, toutes les séances s'affichent à la suite, l'outil à sa place.

La clôture reçoit un corrigé replié par défi (coût réel sur quatre ans : 2 784 € de piles contre 31 €, le panneau moins cher dès le onzième jour ; défi mesure ; défi hiver : 2,4 h en décembre, 17,6 Wh manquants sur une semaine, deux accus ou un panneau de 3,5 W) ; au bilan, « Comment j'ai travaillé » et « Je me positionne » aux quatre niveaux du livret scolaire, sur `4e_C7.4` et `4e_C3.1` (appui).
