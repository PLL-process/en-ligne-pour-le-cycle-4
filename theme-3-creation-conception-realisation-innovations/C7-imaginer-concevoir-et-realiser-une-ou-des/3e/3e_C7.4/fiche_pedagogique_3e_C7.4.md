# Fiche pédagogique — 3e_C7.4 « La station doit tenir 72 heures sans secteur »

> **Choisir une source d'énergie pour un OST.**
> Programme 2024 · cycle 4 · thème 3 · socle D1.3 · D2 · D3 · D4 · D5

| | |
|---|---|
| **Niveau** | 3e |
| **Code principal** | 3e_C7.4 — 20 questions de QCM |
| **Code d'appui** | 3e_C3.2 — *Choisir un OST et argumenter ce choix en prenant en compte son cycle de vie et les trois piliers du développement durable.* — 10 questions |
| **Durée** | 2 séances de 90 min (1 h 30) — 150 min d'activités obligatoires |
| **Matériel** | un navigateur, hors ligne. Aucune installation, aucun compte. |
| **Version A** | montage réel + multimètre en série ; les mesures remplacent alors le banc |

---

## 1. Le pari didactique

Le verbe du code est **choisir une source pour un OST** — sans liste fermée, sans
grille fournie. Le lot pose donc un objet réel, une contrainte réelle, et un avis à signer.

**Le pivot :** la station est alimentée par le secteur, et le réseau tombe exactement au
moment où elle sert. La réponse attendue n'est pas UNE source, c'est une **architecture** :
qui alimente d'habitude, qui prend le relais, qui recharge.

**La contre-intuition à faire vivre :** « un panneau solaire, c'est autonome ». Sous un
cyclone, un panneau récolte moins d'un dixième de sa production — et une plaque plate à 180 km/h
s'arrache. Le panneau ne *tient* pas : il *recharge*.

**Et la spirale se referme :** deux accus donnent 18,8 Wh pour 18,12 exigés, soit 3,8 % de
marge. C'est le bois qui cassait à 41 kg pour 40 en 5ᵉ et le mât recalé pour 1,1 mm en
3ᵉ. **Tout juste n'est pas assez**, trois fois, sur trois objets sans rapport.


## 2. Déroulé

| # | Activité | Durée | Réponses attendues | Verrou expérientiel |
|---|---|---|---|---|
| 0 | FAIRE d'abord : quel jour faut-il dimensionner | ~20 min | 3 | srcAll |
| 1 | Le besoin sur 72 heures, et ce qu'il faut de réserve | ~25 min | 5 | — |
| 2 | Pourquoi le panneau ne fait pas l'autonomie | ~25 min | 4 | — |
| 3 | Le cycle de vie, pas seulement l'autonomie | ~30 min | 6 | — |
| 4 | L'avis à la mairie | ~30 min | 4 | — |
| — | REFAIRE | ~20 min | 1 | — |

## 3. Ce que le montage consomme

| Ce qui consomme | Courant | Par jour | Énergie | Part |
|---|---|---|---|---|
| Carte Arduino UNO | 45 mA | 24 h | 5,400 Wh | 89,4 % |
| Buzzer d'alerte | 30 mA | 2 h | 0,300 Wh | 5,0 % |
| Anémomètre à impulsions | 1 mA | 24 h | 0,120 Wh | 2,0 % |
| Girouette | 1 mA | 24 h | 0,120 Wh | 2,0 % |
| DEL indicatrice | 10 mA | 2 h | 0,100 Wh | 1,7 % |
| **Total** | | | **6,04 Wh** | 100 % |

## 4. Ce que les sources donnent

| Source | Énergie disponible | Face à 6,04 Wh/jour |
|---|---|---|
| Pile 9 V alcaline | 2,8 Wh | 11 heures |
| 4 piles AA alcalines | 12,5 Wh | 2,1 jours |
| Accu Li-ion 18650 rechargeable | 9,4 Wh | 37 heures |
| Secteur — adaptateur USB scellé | illimitée | tant qu'il y a du réseau |
| Panneau solaire 1 W crête + accu | 3,7 Wh/jour | **ne suffit pas** (−2,34 Wh/jour) |

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

* **Aucune mesure réelle.** Consommations et capacités sont des ordres de grandeur du commerce ; la version 🅰 les remplace par des mesures au multimètre.
* **« Moins d'un dixième » sous cyclone est un ordre de grandeur**, pas une mesure : l'éclairement sous couche épaisse tombe à quelques pour cent, ce qui suffit largement à la conclusion mais ne doit pas être présenté comme un relevé.
* **Le vieillissement des accus est traité en un seul chiffre** (≈ 20 % après quelques centaines de cycles). La réalité dépend de la température, de la profondeur de décharge et du courant — la chaleur martiniquaise mérite d'être discutée, et le défi bonus s'en charge.
* **La bascule secteur/accu n'est pas conçue ici.** Le lot dit qu'elle existe, qu'elle se teste, et renvoie au défi bonus. Ce serait un lot C7.5 à part entière.

## 8. Prolongements


  **⚡ Défi bascule :** cherche comment on fait basculer automatiquement une alimentation
  du secteur vers une batterie sans que l'appareil s'éteigne une seule milliseconde. Écris le
  nom du composant et ce qu'il faudrait tester pour être sûr qu'il marche.
  **🌡 Défi température :** un accu Li-ion perd de la capacité au froid — mais en
  Martinique, c'est la **chaleur** qui l'use. Cherche à partir de quelle température un accu
  vieillit vite, et dis où tu ne placerais surtout pas le boîtier sur un toit-terrasse.
  **🔌 Défi Martinique :** l'électricité du réseau martiniquais vient encore largement de
  centrales thermiques. Cherche la part des énergies renouvelables dans le mix de l'île, et dis
  ce que ça change à l'argument « le secteur, c'est plus écologique que des accus ».


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
3e_C7.4/
├── sequence_3e_C7.4_energie-de-la-station.html
├── qcm_3e_C7.4_energie-de-la-station.html
├── lexique_3e_C7.4.html
├── synthese_eleve_3e_C7.4.html
├── synthese_professeur_3e_C7.4.html
├── fiche_pedagogique_3e_C7.4.md
├── matrice_couverture_3e_C7.4.csv
├── rapport_tests_3e_C7.4.md
├── tests_3e_C7.4_sequence.mjs · tests_3e_C7.4_qcm.mjs · reponses_3e_C7.4.json
└── energie.py
```
