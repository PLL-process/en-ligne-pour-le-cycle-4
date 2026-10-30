# Fiche pédagogique / inspection — La station d'alerte cyclonique se programme

## Identification

| Champ | Valeur |
|---|---|
| Niveau | 3e (programme 2024) |
| Codes | **3e_C9.2** (dossier principal) · **3e_C8.3** (couvert, README pointeur) |
| Thème | Thème 3 — Création, conception, réalisation, innovations : des objets à concevoir et à réaliser |
| Compétences parentes | C9 — Concevoir, écrire, tester et mettre au point un programme · C8 — Valider les solutions techniques par des essais et des tests |
| Référentiel | BO n°9 du 29/02/2024 |
| Domaines du socle | D1.3, D2, D3, D4, D5 |
| CRCN | 3.4 Programmer · 5.2 Évoluer dans un environnement numérique |
| Durée | 8 séances de 55 min (285 min d'activités annoncées) |
| Objet-fil 3e | La station d'alerte cyclonique (décrite en 3e_C4.3, programmée ici, auto-testée en 3e_C6.2) |

## Sous-compétences travaillées (formulations officielles)

| Code | Intitulé | Activités |
|---|---|---|
| 3e_C9.2 | Réaliser et mettre au point un programme commandant un système réel incluant une interaction entre un humain et une machine. | 1, 2, 3, 4, 5 |
| 3e_C8.3 | Proposer un protocole de test pour valider le comportement et les performances d'un objet technique. | 6, 7 |

**Verbe pris au mot (C8.3)** : l'élève *propose* — il rédige son protocole (act. 6)
avant de l'exécuter (act. 7). La production probante est le protocole rédigé + le
PV de recette, pas le QCM (qui consolide).

## Situation déclenchante et problématique

- **Situation** : la mairie commande au club techno un prototype de station
  d'alerte cyclonique pour la cour (courrier de commande dans la page) : mesure du
  vent, quatre niveaux repris de l'échelle de Saffir-Simpson (veille /
  tempête tropicale dès 63 km/h / ouragan dès 118 / ouragan majeur dès 178),
  un seul voyant allumé à la fois et qui pulse à partir du jaune, alarme sonore
  en ouragan majeur seulement, acquittable par l'agent, réaction < 1 s.
  Avant mise en service : **procès-verbal de recette** exigé.
- **Problématique** : *Comment écrire, puis mettre au point, un programme qui
  commande la station et dialogue avec un humain — et comment prouver à la mairie
  qu'il respecte le cahier des charges ?*
- **Honnêteté du dispositif** : seuils = cahier des charges pédagogique de la
  mairie, qui les reprend de l'échelle de Saffir-Simpson ; une VIGILANCE
  (Météo-France) et une ALERTE (préfecture) sont d'une autre nature — la
  séquence distingue explicitement mesure, vigilance et alerte ;
  anémomètre **simulé par un potentiomètre**, dit explicitement aux élèves.

## Déroulé (8 × 55 min)

Une heure de cours par semaine et par classe (décision de Pascal du 24/10/2026) :
la séquence, écrite d'abord en quatre séances de 1 h 30, passe à **huit séances de
55 min**, sans rien retirer. Chaque séance garde 15 à 25 min hors activités annoncées
pour le lancement, l'échauffement logiciel, les transitions et le bilan (règle n°23).
La seule activité de plus de 55 min (act. 3, ~70 min) est coupée en deux parties
nommées, à la frontière palier 2 / palier 3.

| Séance | Contenu | Activités annoncées | Page découpée |
|---|---|---|---|
| S1 | Accroche (courrier, hypothèses, billet d'entrée) + act. 1 | 30 min | page 1 |
| S2 | Act. 2 | 35 min | page 1 |
| S3 | Échauffement Vittascience (cinq gestes) + act. 3, première partie | 35 min | page 2 |
| S4 | Act. 3, suite (reprise, palier 3, journal, vérificateur) | 35 min | page 2 |
| S5 | Act. 4 | 40 min | page 3 |
| S6 | Act. 5 | 35 min | page 3 |
| S7 | Act. 6 | 40 min | page 4 |
| S8 | Act. 7 + clôture (synthèse, Bonus, bilan, QCM) | 35 min | page 4 |

Avant / après : S1 90 min (act. 1 + 2 = 65) → S1 + S2 ; S2 (act. 3 = 70) → S3 + S4 ;
S3 (act. 4 + 5 = 75) → S5 + S6 ; S4 (act. 6 + 7 = 75, clôture) → S7 + S8.

### S1 — « La mairie vous appelle » : du besoin aux deux chaînes (C9.2)
Accroche (15 min) : courrier + hypothèses + billet d'entrée sans note.
Act. 1 (30 min) : exigences (comportement/performance), les deux chaînes, place
du bouton (règle n°6 : information en haut, énergie en bas, ordre qui descend).

### S2 — Du besoin à l'algorithme (C9.2)
Act. 2 (35 min) : algorithme en langage naturel puis algorigramme des 4 niveaux
(ordre des tests ; encart 🎓 DNB). Synthèse (10 min).

### S3 — Programmer la station en blocs : lire et décider (C9.2)
Échauffement : les cinq gestes de Vittascience (ouvrir, catégories, nommer,
simuler, sortir).
Act. 3, première partie (35 min) : TP par **paliers** façon « dé de 5e » —
1. lire (A1, convertir), 2. décider (SI/SINON, seuil haut d'abord) ; chaque palier :
geste → image du résultat attendu → rituel d'enregistrement. Fin de partie :
programme du palier 2 enregistré et rangé dans le dossier de la classe.

### S4 — Programmer la station en blocs : alerter, puis vérifier (C9.2)
Act. 3, suite (35 min) : reprise (rouvrir le programme du palier 2, ou le
reconstruire avec les planches), 3. alerter (sous-programmes de mode, LCD
couleur, DEL), palier 4 en aperçu, captures réelles du programme de référence,
journal de paliers et vérificateur (verrous du banc). Rotation îlot 🅰 pendant
travail 🅱/🅲 au banc intégré.

### S5 — L'humain dans la boucle (C9.2)
Act. 4 (40 min) : acquittement — booléen-mémoire, événement (niveau ≠ précédent),
ré-armement ; chronogramme ; 2 expériences tracées au banc.

### S6 — Sous le capot : lire le C++ (C9.2)
Act. 5 (35 min) : lecture guidée du C++ généré (const, map, else if, sous-programme
`afficherEtat()`) + diagnostic sur trace série (version 🅲 incluse).

### S7 — Prouver (1) : le protocole (C8.3)
Act. 6 (40 min) : **rédiger** le protocole : nominaux, cas limites aux six frontières 62/63, 117/118, 177/178,
performance chronométrée, 2 essais d'interaction, règle de décision.

### S8 — Prouver (2) : la recette (C8.3)
Act. 7 (35 min) : **exécuter** au banc (frontières et chrono tracés), tableau
essai/attendu/observé/verdict rempli PENDANT, **PV de recette** rédigé et signé.
Puis la clôture : synthèse, Bonus facultatif, bilan (retour à l'hypothèse,
positionnement), renvoi au QCM.

## Versions 🅰🅱🅲

| Version | Dispositif |
|---|---|
| 🅰 Matériel réel | **Un seul montage, des séances 3 à 8** : UNO + shield Grove 5 V, potentiomètre A1 (anémomètre simulé, 0-250 km/h), bouton D2, voyants D6 vert / D7 jaune / D3 orange / D4 rouge, buzzer D5, LCD RGB I2C — programme construit sur **Vittascience** (interface Arduino, mode BLOCS) et téléversé. TBT uniquement. |
| 🅱 Simulation | Banc d'essai intégré à la page : mêmes seuils, même logique (boucle 200 ms), verrous expérientiels `window.__exp`. |
| 🅲 Sans matériel | Banc intégré + traces d'exécution fournies (act. 5 et 7). Parcours complet, y compris à la maison. |

**Point de vigilance outil (refonte v2)** : les séances 3 et 4 se font sur
**Vittascience**, interface Arduino en mode **BLOCS**
(`fr.vittascience.com/arduino`). Motif : Vittascience **simule**, ArduBlock non —
or les tests aux **six valeurs frontières** (62/63, 117/118, 177/178), cœur de la compétence
C8.3, exigent de pouvoir rejouer une valeur exacte à volonté, sans carte et sans
attendre son tour. Conséquence à anticiper : Vittascience demande une
**connexion Internet** ; c'est le seul point de la séquence dans ce cas, et un
**repli hors-ligne** complet est prévu (planches de blocs + banc d'essai intégré),
suffisant pour répondre à toutes les questions et valider l'activité. L'éditeur
s'ouvre par un **lien-bouton vers le programme partagé, dans un nouvel onglet** :
le code d'intégration officiel (embed=1) répond X-Frame-Options: SAMEORIGIN
(mesuré le 13/09/2026), aucun cadre ne s'affiche.

**ArduBlock Éducation 1.7** n'est pas abandonné : il devient un **bonus
facultatif — hors parcours obligatoire** de la séance 4, illustré par **deux
captures réelles** du logiciel (paliers 1 et 2, poste du labo — règle d'or
n°94). Ce bonus a une vraie valeur pédagogique : il montre le **même
raisonnement** dans deux logiciels et à deux échelles, ce qui prépare la question
« ce qu'un algorigramme ne dit pas » (act. 2 c).

Les planches des séances 3 et 4 sont des **reconstitutions schématiques** de l'écran
Vittascience, étiquetées comme telles (pas des captures) : à remplacer par des
captures du poste réel dès que les programmes de la classe existent
(règles n°70/73/94).

**Banc Docker (enseignant uniquement)** : `banc-docker/` — vérifie la compilation
`arduino:avr:uno` du programme de référence (compte Docker personnel requis).
Compilation déjà vérifiée hors Docker le 19/08/2026 : 6 764 o flash / 569 o RAM.

## Différenciation, inclusion, accessibilité

- Exercices fermés en **listes déroulantes** (DYS), aides à 2 niveaux, corrections
  complètes repliées, versions étayées 🪜 sur chaque zone de rédaction.
- **Mode essentiel** 🎯 (allège la page), navigation clavier + skip-link, aria,
  `prefers-reduced-motion`, images agrandissables (loupe), impression A4.
- **Verrous expérientiels** : les activités 3, 4 et 7 exigent les manipulations
  réelles au banc (traces locales `window.__exp`) — pas de validation « de tête ».
- Bonus pour élèves rapides : 3 défis ouverts **avec corrigés repliés**.

## Évaluation

- **Formative** : vérificateurs par activité, progression visible, bilan avec
  auto-positionnement par code.
- **Entraînement** : QCM séparé 30 questions (15 par code, 4 illustrées),
  corrections exhaustives (réfutation de chaque distracteur), bilan par
  compétence, /20 indicatif.
- **Sommative** : à construire par l'enseignant depuis la matrice de couverture —
  aucune évaluation sommative ni corrigé publiés dans le dépôt public.
- **LSU** (indicatif) : ≥ 75 % des items du code = maîtrisé · 50-74 % = en cours ·
  < 50 % = fragile — à croiser avec les productions (protocole rédigé, PV).

## Sécurité

Très basse tension 5 V uniquement ; le secteur 230 V est **interdit** aux élèves ;
câblage validé par l'enseignant avant branchement USB ; jamais de connexion ou
déconnexion de module sous tension.

## Prolongements

- 3e_C6.2 « L'auto-test de la station » (non-régression outillée) — même objet-fil.
- 3e_C8.1 / C8.2 (essais, mesures, comparaison aux performances attendues).
- DNB : algorigrammes (encart 🎓 en S2, questions illustrées du QCM).
- EDD : culture du risque cyclonique, rôle des systèmes d'alerte en milieu insulaire.
- EPI possible : Physique-Chimie (pression, vent), Géographie (risques naturels).
