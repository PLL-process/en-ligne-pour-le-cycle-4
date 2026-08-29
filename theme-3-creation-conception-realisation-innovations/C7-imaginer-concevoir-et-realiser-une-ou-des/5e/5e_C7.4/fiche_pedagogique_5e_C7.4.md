# Fiche pédagogique — 5e_C7.4 « L'indicateur du hall »

> **Choisir une source d'énergie parmi plusieurs proposées et une forme d'énergie possible.**
> Programme 2024 · cycle 4 · thème 3 · socle D1.3 · D4 · D5

| | |
|---|---|
| **Niveau** | 5e |
| **Code principal** | 5e_C7.4 — 20 questions de QCM |
| **Code d'appui** | 5e_C3.1 — *Repérer pour un OST les matériaux, les sources et les formes d'énergies, le traitement de l'information.* — 10 questions |
| **Durée** | 2 séances de 55 min — 95 min d'activités obligatoires |
| **Matériel** | un navigateur, hors ligne. Aucune installation, aucun compte. |
| **Version A** | montage réel + multimètre en série ; les mesures remplacent alors le banc |

---

## 1. Le pari didactique

Le verbe du code est **choisir parmi plusieurs sources proposées**. Le piège que
la séquence installe est le meilleur outil pour l'évaluer : **le panneau solaire suffit sur le
papier** — 3,7 Wh récoltés pour 2,85 consommés — **et ne marche pas**, parce qu'il n'y a pas
de soleil dans un hall.

L'élève qui décide au seul vu du banc se trompe. L'élève qui a compris que le lieu fait partie
du choix ne se trompe pas. Le REFAIRE ferme la démonstration : le même objet, posé sur le portail
à vélos, retrouve le panneau — **sans qu'un seul chiffre change**.


## 2. Déroulé

| # | Activité | Durée | Réponses attendues | Verrou expérientiel |
|---|---|---|---|---|
| 0 | FAIRE d'abord : brancher les cinq sources | ~15 min | 2 | srcAll |
| 1 | D'où vient l'énergie, et sous quelle forme | ~20 min | 6 | — |
| 2 | Relever ce que chaque source donne vraiment | ~20 min | 5 | srcAll |
| 3 | Choisir, et le dire | ~20 min | 4 | — |
| 4 | Ce que le banc ne compte pas | ~10 min | 4 | — |
| — | REFAIRE | ~10 min | 1 | — |

## 3. Ce que le montage consomme

| Ce qui consomme | Courant | Par jour | Énergie | Part |
|---|---|---|---|---|
| Carte Arduino UNO | 45 mA | 10 h | 2,250 Wh | 78,9 % |
| DEL indicatrice | 10 mA | 10 h | 0,500 Wh | 17,5 % |
| Capteur d'humidité du sol | 2 mA | 10 h | 0,100 Wh | 3,5 % |
| **Total** | | | **2,85 Wh** | 100 % |

## 4. Ce que les sources donnent

| Source | Énergie disponible | Face à 2,85 Wh/jour |
|---|---|---|
| Pile 9 V alcaline | 2,8 Wh | 24 heures |
| 4 piles AA alcalines | 12,5 Wh | 4,4 jours |
| Accu Li-ion 18650 rechargeable | 9,4 Wh | 3,3 jours |
| Secteur — adaptateur USB scellé | illimitée | tant qu'il y a du réseau |
| Panneau solaire 1 W crête + accu | 3,7 Wh/jour | suffit (30 % de marge) |

Tout est recalculé par [`energie.py`](energie.py), livré dans le dossier. Le rendement d'un
régulateur linéaire y vaut V<sub>sortie</sub> ÷ V<sub>entrée</sub> — c'est de la physique, pas
un réglage : il dissipe la différence en chaleur. Ensoleillement retenu pour la Martinique :
5,3 heures équivalent plein soleil par jour, avec 30 % de pertes de chaîne.

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

* **Aucune mesure réelle.** Les courants sont des valeurs constructeur usuelles, les capacités des ordres de grandeur du commerce. La version 🅰 (multimètre en série) remplace ces valeurs par des mesures, et ce sont elles qui font foi.
* **Le banc ignore l'éclairement intérieur.** Il compte l'ensoleillement extérieur de la Martinique. C'est exactement ce qui rend l'activité 3 intéressante — mais un élève qui lit vite peut croire le panneau bon partout, et il faut le reprendre.
* **Le vieillissement n'est pas modélisé.** Une pile alcaline stockée deux ans a déjà perdu une partie de sa charge.

## 8. Prolongements


  **🔋 Défi pile :** une pile 9 V coûte 3,50 € et tient 24 h. Combien coûterait une année
  scolaire d'indicateur alimenté ainsi ? Compare au prix de l'adaptateur, une fois pour toutes.
  **☀ Défi Martinique :** le banc compte 5,3 heures d'équivalent plein soleil par jour, en
  moyenne annuelle. Cherche ce que devient ce chiffre en saison des pluies, et dis ce que ça
  change pour le panneau du portail.
  **🔦 Défi dynamo :** une sixième source existe et n'était pas dans la liste : la dynamo,
  qui transforme un mouvement en électricité. Où faudrait-il installer l'indicateur pour qu'elle
  soit un bon choix ?


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
5e_C7.4/
├── sequence_5e_C7.4_indicateur-du-hall.html
├── qcm_5e_C7.4_indicateur-du-hall.html
├── lexique_5e_C7.4.html
├── synthese_eleve_5e_C7.4.html
├── synthese_professeur_5e_C7.4.html
├── fiche_pedagogique_5e_C7.4.md
├── matrice_couverture_5e_C7.4.csv
├── rapport_tests_5e_C7.4.md
├── tests_5e_C7.4_sequence.mjs · tests_5e_C7.4_qcm.mjs · reponses_5e_C7.4.json
└── energie.py
```
