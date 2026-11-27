# Fiche pédagogique — 4e_C7 Jardin connecté (conception)

**Codes** : 4e_C7.1 · C7.2 · C7.3  
**Ancrage** : New York — school garden / rooftop  
**Durée** : 6 × 55 min — 2 séances sur la page de la séquence (deux onglets), puis l'atelier de planification (1 séance) et le TP « Le dé sur sa pointe » (3 séances), liés en bas de la séance 2  
**Socle** : D2 · D3 · D4 · D5

## Intention
Imaginer, organiser et choisir une solution technique simple (support capteur, abri, indicateur) sous contraintes NY (gel, pluie, vent, réemploi).

## CRCN règle 7 (voir aussi `CRCN_regle7.md`)

| Compétence | Niveau | Action observable | Trace |
|---|---|---|---|
| 3.1 Documents textuels | 2 | Planning + choix justifié | Tableau tâches + paragraphe |
| 1.2 Gérer des données | 1–2 | Sauvegarder / reprendre identité & hypothèse | localStorage ou export |

**3.4 Programmer** → reporté volontairement en **4e_C9** (même objet-fil).

## Versions A/B/C
A maquette TBT · B simulation · C papier

## Sécurité
Très basse tension uniquement ; secteur 230 V interdit.

## Évaluation
Planning · 2 solutions · tableau matériaux · QCM · auto-positionnement

## Harmonisation du 26 août 2026

Le lot a reçu les dispositifs communs du dépôt : billet d'entrée hors progression, mode
essentiel, tableau de bord des six activités, versions étayées, durées à la convention,
carte de référentiel recopiant le programme au mot près, sélecteur de parcours 🅰/🅱/🅲
réellement agissant, et une barre de progression qui suit les validations. Contrôle
mécanisé : **cinq manquements → zéro**. Suite committée : **41 tests, tous verts**.

**Le défaut le plus grave n'était pas là.** Les 28 bonnes réponses du QCM étaient toutes
en position B : un élève qui clique la deuxième proposition à chaque question obtenait
28/28 sans rien savoir. Les propositions ont été redistribuées (7 par position) par
`repartir_qcm.mjs`, dont la suite de positions est écrite en clair — reproductible, pas
tirée au hasard. Le détail est dans le rapport de tests.

## Découpage en séances à onglets (04/11/2026, vague de la règle d'or n°311)

La page était d'un seul tenant ; elle a maintenant deux séances à onglets, sur le modèle du pilote 4e_C8.1 (même gabarit).
Les blocs sont déplacés, pas réécrits ; la durée annoncée sur la page (2 × 55 min) ne change pas.

| Séance | Question directrice | Contenu | Temps annoncé |
|---|---|---|---|
| 1 — Éprouver, dessiner la démarche, choisir | Qu'est-ce qui a tué les bacs, et comment passe-t-on d'un problème à une solution choisie avec des critères ? | Ouverture, activités 0, 1 (diagramme et planning) et 2 | ouverture + 10 + 15 + 25 min |
| 2 — Comparer les matériaux, refaire, conclure | Quel matériau, et la même démarche marche-t-elle ailleurs ? | Activité 3, réinvestissement (FAST incrusté, jardinière), billet de sortie, synthèse, Bonus (corrigé par défi), bilan, TP et atelier liés, QCM | 20 + 30 + 5 min + clôture |

**La durée, rendue cohérente (04/11/2026).** Les trois mentions ne parlaient pas de la même chose : l'étiquette de la page (« 2 séances de 55 min ») désigne la page seule — sa bulle disait déjà « + 3 séances sur le TP et 1 sur l'atelier, soit 6 au total » ; la fiche (« 4 × 55 min ») et l'activité 1 (« pendant 4 séances ») dataient du temps où le TP et l'atelier comptaient une séance chacun (entrée du journal d'août 2026) ; le TP annonce aujourd'hui trois séances et l'atelier une. La page garde ses deux onglets ; l'activité 1 parle des « six séances du projet », l'en-tête de la séance 2 dit que les séances 3 à 6 se font sur l'atelier et le TP, et cette fiche annonce 6 × 55 min. **À vérifier par Pascal :** l'ordre de l'atelier et du TP n'est écrit nulle part (l'atelier « se place au lancement du projet », le TP vient « avant de dessiner le boîtier »). Et la séance 1 porte l'ouverture et 50 min d'activités.

Dès la séance 2, l'ouverture (étiquettes, note du mode essentiel, « Avant de commencer », situation, problématique,
hypothèse, billet, contrat, trois façons) est repliée dans le volet « 📖 Rappel » ; à la séance 1, elle est complète, dans
l'ordre du squelette (le billet passe après l'hypothèse, comme au pilote). Restent dehors : la mission, l'identité, la barre
d'outils, le sélecteur de parcours et ses deux zones `role=status`, la progression et « 🗺 Où j'en suis », qui devient un
volet ouvert à la séance 1 et replié dès la séance 2 (son résumé, « 🗺 Où j'en suis — 2 / 6 activités validées », suit la
liste). Le banc météo ne sert qu'à la séance 1 : il reste dans l'activité 0. L'exercice FAST incrusté passe à la séance 2
avec le réinvestissement, ses marques d'incrustation intactes.

La clôture reçoit un corrigé replié par défi du Bonus (réemploi de quartier, critère de test chiffré, lieux de New York) ;
au bilan, le retour à l'hypothèse (le texte écrit au début se relit), « Comment j'ai travaillé » et « Je me positionne »
sur 4e_C7.1, C7.2 et C7.3 aux quatre niveaux du livret scolaire.

## Le billet de sortie et les documents du QCM (27/11/2026, règles d'or n°330 et n°345)

**Billet de sortie**, en fin de séance 2, juste avant le Bonus (environ 5 min, seul et sans aide ; la séance tient en
55 minutes). Un objet que la séquence n'a pas étudié : **l'abri à outils du jardin partagé**, à Brooklyn.
- Question 1 (4e_C7.1) : ranger quatre tâches données dans le désordre et repérer celles qui avancent en même temps.
  On regarde un ordre justifié par ce que chaque tâche attend, et au moins une paire de tâches indépendantes.
- Question 2 (4e_C7.3) : choisir le matériau du toit et nommer le critère qui élimine l'autre. On regarde le critère
  éliminatoire nommé et rattaché au lieu (la pluie, le gel).

**QCM** : neuf questions sur trente se lisent sur un document (trois l'étaient déjà). Deux documents neufs, dessinés
pour le téléphone et LUS dans la séquence par `documents_qcm.py` : « Les tâches du projet du jardin » (les quatre
tâches de l'activité 1b, dans le désordre, avec leur durée ; q1, q8) et « Trois matériaux pour le boîtier » (le
tableau de l'activité 3, rempli avec ses réponses attendues ; q24, q26, q27, q29). La q1 demandait « En 5e on suit…
qu'attend-on de toi en 4e ? » : elle évaluait la connaissance du programme, et supposait une 5e faite avec nous
(n°304). Elle fait maintenant organiser la liste. La q29 disait « notre tableau » : elle montre le tableau.
