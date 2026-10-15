# Archive — vittascience_variables.html (règle d'or n°12)

Ressource héritée « Vittascience – Créer des variables, manipuler les types et programmer des
systèmes » (enquête Vittascience adaptée P. Gouacide, donnée aux trois niveaux), **remplacée le
2026-07-30** par l'atelier refondu :

➡ `theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/sequence_3e_C9.1_variables_types_systemes.html`

L'URL historique porte un stub de redirection. Les captures PNG dédiées sont archivées ici (Images/).

## Version blocs 5e – 4e et son évaluation notée

- `vittascience_variables_blocs.html` — la séance d'entraînement en blocs (5e – 4e), utilisée en classe.
- `evaluation_vittascience_blocs.html` — **évaluation notée** (09/10/2026) tirée des trois exercices les plus
  exigeants de cette séance : Ex. 10 « Arrosage automatique », Bonus 9 « Triangle coloré », Bonus 10 « Spirale ».
  16 questions, 30 points ramenés sur 20 ; indice gratuit, coup de pouce à −¼ des points de la question
  (`COUT_COUP_DE_POUCE`), correction par exercice qui verrouille les réponses (question sans réponse = 0).
  Les réponses et corrections sont encodées dans la page (`decoderCle()`) ; code enseignant : celui de la séance.


## Évaluations A et B — repères gratuits (15/10/2026)

À la demande de Pascal, la version A est enrichie de repères de navigation et une version B parallèle est créée pour une passation ultérieure. Les deux fichiers sont publiés ici sur sa demande explicite. Les réponses et corrections restent encodées dans chaque page, selon le fonctionnement de la version initiale ; cet encodage ne constitue pas une protection d'accès.

- [Version A](evaluation_vittascience_blocs.html) : arrosage automatique, triangle et spirale.
- [Version B](evaluation_vittascience_blocs_B.html) : ventilation de salle (simulation et seuils pédagogiques), hexagone et nouvelle spirale.
- 3 exercices, 16 questions, 10 points par exercice, 30 points convertis sur 20, 50 min (tiers temps 67 min).
- Trois tableaux « Où trouver les blocs ? », un guide général et la capture fournie par Pascal, intégrée à chaque fichier. Consultation gratuite, sans pénalité ; règles des autres aides conservées.
- Noms des fichiers et sauvegardes différents : une copie A ne se recharge pas dans B. Les réponses B, programmes, indices, corrections et exports sont adaptés.
- Niveau affiché : 3e ; rattachement partiel à C9.1 (variables, conditions, boucles, tests et mise au point). Ces exercices ne couvrent pas à eux seuls la compétence complète de conception d'un programme structuré avec sous-programmes.

### Équivalence et couverture des deux sujets

| Questions A / B | Notion et opération évaluées | Exercice A → B | Rattachement | Exigence |
|---|---|---|---|---|
| 1.1–1.2 | Exécuter quatre comparaisons strictes reliées par ET | Arrosage → ventilation | 3e C9.1, partiel | Analyse / test |
| 1.3 | Adapter un seuil de durée | 24 h → 20 min | 3e C9.1, partiel | Application |
| 1.4 | Introduire une exception avec OU | Sol très sec → CO₂ élevé | 3e C9.1, partiel | Transfert |
| 1.5 | Expliquer un résultat au seuil exact | Humidité → bruit | 3e C9.1, partiel | Analyse |
| 2.1–2.2 | Compter les répétitions et la longueur totale | Triangle → hexagone | 3e C9.1, partiel | Compréhension / application |
| 2.3–2.4 | Distinguer angle intérieur et rotation ; adapter un polygone | Triangle vers hexagone → transfert inverse | 3e C9.1, partiel | Analyse / transfert |
| 2.5 | Calculer la valeur d'une variable pour un périmètre imposé | 450 / 3 → 540 / 6 | 3e C9.1, partiel | Application |
| 2.6 | Diagnostiquer une rotation hors de la boucle | Triangle → hexagone | 3e C9.1, partiel | Mise au point |
| 3.1–3.3 | Suivre une variable avant et après la mise à jour | Départ 10, +10, 20 tours → départ 15, +5, 16 tours | 3e C9.1, partiel | Analyse |
| 3.4–3.5 | Étudier une mise à jour supprimée ou inversée ; rester positif | Deux spirales de paramètres distincts | 3e C9.1, partiel | Analyse / transfert |

Socle : D1.3, D2, D4 ; CRCN : 3.4 Programmer. Difficulté visée équivalente par structure, opérations et barème ; équivalence non étalonnée sur une cohorte.

### Vérification de cette livraison

48 assertions exécutées avec jsdom : structure, barème, rendu des blocs dans le DOM, démarrage avec identité obligatoire, notes vide et parfaite, pénalité d'aide, score intermédiaire, verrouillage et affichage des corrections, restauration des réponses, absence d'erreur JavaScript, séparation des sauvegardes. Calcul indépendant des valeurs numériques B (relevés, polygones, spirale). Pas de contrôle graphique ni d'exécution des programmes dans l'éditeur Vittascience externe pour cette livraison.
