# Fiche pédagogique / inspection — La station d'alerte cyclonique se programme

## Identification

| Champ | Valeur |
|---|---|
| Niveau | 3e (programme 2024) |
| Codes | **3e_C9.2** (dossier principal) · **3e_C8.3** (couvert, README pointeur) |
| Thème | Thème 3 — Création, conception, réalisation : des objets et des systèmes techniques à créer |
| Compétences parentes | C9 — Concevoir, écrire, tester et mettre au point un programme · C8 — Valider les solutions techniques par des essais et des tests |
| Référentiel | BO n°9 du 29/02/2024 |
| Domaines du socle | D1.3, D2, D3, D4, D5 |
| CRCN | 3.4 Programmer · 5.2 Évoluer dans un environnement numérique |
| Durée | 4 séances de 1 h 30 |
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
  vent, trois niveaux (veille / vigilance orange dès 100 km/h / alerte rouge dès
  150 km/h), alarme sonore acquittable par l'agent d'accueil, réaction < 1 s.
  Avant mise en service : **procès-verbal de recette** exigé.
- **Problématique** : *Comment écrire, puis mettre au point, un programme qui
  commande la station et dialogue avec un humain — et comment prouver à la mairie
  qu'il respecte le cahier des charges ?*
- **Honnêteté du dispositif** : seuils = cahier des charges pédagogique de la
  mairie (les vigilances réelles de Météo-France croisent d'autres critères) ;
  anémomètre **simulé par un potentiomètre**, dit explicitement aux élèves.

## Déroulé (4 × 1 h 30)

### S1 — « La mairie vous appelle » (C9.2)
Accroche (15 min) : courrier + hypothèses + billet d'entrée sans note.
Act. 1 (30 min) : exigences (comportement/performance), les deux chaînes, place
du bouton (règle n°6 : information en haut, énergie en bas, ordre qui descend).
Act. 2 (35 min) : algorithme en langage naturel puis algorigramme des 3 niveaux
(ordre des tests ; encart 🎓 DNB). Synthèse (10 min).

### S2 — Programmer la station en blocs (C9.2)
Act. 3 (70 min) : TP par **paliers** façon « dé de 5e » — 1. lire (A1, calibrer),
2. décider (SI/SINON, seuil haut d'abord), 3. afficher (LCD couleur, DEL) ;
chaque palier : geste → image du résultat attendu → rituel d'enregistrement.
Palier 4 en aperçu. Rotation îlot 🅰 pendant travail 🅱/🅲 au banc intégré.

### S3 — L'humain dans la boucle (C9.2)
Act. 4 (40 min) : acquittement — booléen-mémoire, événement (niveau ≠ précédent),
ré-armement ; chronogramme ; 2 expériences tracées au banc.
Act. 5 (35 min) : lecture guidée du C++ généré (const, map, else if, sous-programme
`afficherEtat()`) + diagnostic sur trace série (version 🅲 incluse).

### S4 — La recette (C8.3)
Act. 6 (40 min) : **rédiger** le protocole : nominaux, cas limites 99/100/149/150,
performance chronométrée, 2 essais d'interaction, règle de décision.
Act. 7 (35 min) : **exécuter** au banc (frontières et chrono tracés), tableau
essai/attendu/observé/verdict rempli PENDANT, **PV de recette** rédigé et signé.

## Versions 🅰🅱🅲

| Version | Dispositif |
|---|---|
| 🅰 Matériel réel | **Séance 2 (maquette)** : UNO + shield Grove 5 V, capteur rotatif A0, voyants D2 vert / D3 orange / D4 rouge, buzzer D5 — programme construit sur **Vittascience** (interface Arduino, mode BLOCS) et téléversé. **Séances 3-4 (station du labo)** : potentiomètre A1, bouton D2, DEL D3, buzzer D5, LCD I2C. TBT uniquement. |
| 🅱 Simulation | Banc d'essai intégré à la page : mêmes seuils, même logique (boucle 200 ms), verrous expérientiels `window.__exp`. |
| 🅲 Sans matériel | Banc intégré + traces d'exécution fournies (act. 5 et 7). Parcours complet, y compris à la maison. |

**Point de vigilance outil (refonte v2)** : la séance 2 se fait désormais sur
**Vittascience**, interface Arduino en mode **BLOCS**
(`fr.vittascience.com/arduino`). Motif : Vittascience **simule**, ArduBlock non —
or les tests aux **valeurs frontières** (39/40, 69/70), cœur de la compétence
C8.3, exigent de pouvoir rejouer une valeur exacte à volonté, sans carte et sans
attendre son tour. Conséquence à anticiper : Vittascience demande une
**connexion Internet** ; c'est le seul point de la séquence dans ce cas, et un
**repli hors-ligne** complet est prévu (lien direct + planches de blocs + banc
d'essai intégré), suffisant pour répondre à toutes les questions et valider
l'activité. Prévoir aussi l'**emplacement de l'iframe** Vittascience, à remplir
avec le code d'intégration officiel dès qu'il est disponible.

**ArduBlock Éducation 1.7** n'est pas abandonné : il devient un **bonus
facultatif — hors parcours obligatoire** de la séance 2, illustré par **deux
captures réelles** du logiciel (paliers 1 et 2, poste du labo — règle d'or
n°94). Ce bonus a une vraie valeur pédagogique : il montre le **même
raisonnement** dans deux logiciels et à deux échelles, ce qui prépare la question
« ce qu'un algorigramme ne dit pas » (act. 2 c).

Les planches de la séance 2 sont des **reconstitutions schématiques** de l'écran
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
- DNB : algorigrammes (encart 🎓 en S1, questions illustrées du QCM).
- EDD : culture du risque cyclonique, rôle des systèmes d'alerte en milieu insulaire.
- EPI possible : Physique-Chimie (pression, vent), Géographie (risques naturels).
