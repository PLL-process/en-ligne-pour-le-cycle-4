# Fiche pédagogique — 3e Capteur de confort scolaire (NY)

**Codes** : 3e_C7.1 (COMPLET) · 3e_C8.1 (COUVERT) · 3e_C7.2 (ENSEIGNÉ en séance 3 ; évalué par le QCM de 3e_C7.6)  
**Ancrage** : New York — îlot de chaleur / salle scolaire  
**Durée** : 3 × 55 min sur la page de la séquence (145 min d'activités annoncées) ; le projet se prolonge par le TP « Le boîtier étanche » et l'atelier de planification (une séance)  
**Socle** : D2 · D4 · D5

## Déroulé en trois séances (depuis le 24/10/2026)

| Séance | Activités | Minutes annoncées |
|---|---|---|
| 1 — Faire, concevoir, valider | activité 0 (simulateur, 10) · activité 1 (concevoir, 20) · activité 2 (valider par des essais, 25) | 55 / 55 |
| 2 — L'algorigramme, puis le code | gestes Vittascience · activité 3 (algorigramme, code, mise au point, 30) · REFAIRE (15) | 45 / 55 |
| 3 — Représenter les solutions | activité 6 (contrôler un FAST, 13) · activité 7 (trois croquis, puis choisir la représentation, 25) · synthèse, Bonus facultatif, bilan (7), renvoi au QCM | 45 / 55 |

La page défile d'un seul tenant (pas d'onglets) : chaque séance s'ouvre par un en-tête « 🗓 Séance N », et se ferme par un
bouton vers la suivante. La clôture (synthèse → Bonus → bilan → QCM) vient après la séance 3.

**Pourquoi une séance 3.** Demande du professeur (24/10/2026) : aucune des deux séances n'avait le temps d'accueillir un
exercice des ateliers des représentations (séance 1 pleine, séance 2 à 45 min pour des exercices de 12 à 13 min). La
séance 3 est faite de trois exercices des ateliers, au service de 3e_C7.2 : « Trouver les erreurs d'un FAST » (atelier
FAST, 3e), « Trois croquis rapides pour fixer la sirène » et « Du croquis au schéma ou à la modélisation » (atelier croquis,
3e). Ils portent sur la **station d'alerte cyclonique**, système voisin du capteur (mesurer → comparer à un seuil →
prévenir) ; l'introduction de chaque bloc le dit, et l'« À retenir » de chaque activité ramène au capteur de confort. Les
exercices gardent leur clé de sauvegarde d'atelier (`rep_fast_3e_e6`, `rep_croquis_3e_e4`, `rep_croquis_3e_e6`) : le
travail fait ici se retrouve dans l'atelier et dans le cahier de 3e. Les vérificateurs des activités 6 et 7 exigent leur
réussite.

**Bilan complété** : retour à l'hypothèse de départ, une question sur la démarche (« où as-tu hésité… »), « Je me
positionne » sur 3e_C7.1, 3e_C8.1 et 3e_C7.2 (boutons radio) ; le Bonus a désormais son corrigé replié.

## CRCN règle 7

| Compétence | Niveau | Repère (verbatim orienté PIX/CRCN) | Action observable | Trace |
|---|---|---|---|---|
| 3.4 Programmer | 2–3 | Réaliser / mettre au point un programme simple | Pseudo-code SI + correction hystérésis | Texte algo + tests |
| 1.3 Traiter des données | 2 | Saisir et exploiter des données | 4 lignes de protocole | Tableau renseigné |
| 5.1 Résoudre des problèmes techniques | 2 | Résoudre un dysfonctionnement simple | Cause + test discriminant | Fiche diagnostic |

## Versions B/C
B simulation · C papier.

La version 🅰 (maquette TBT) a été **retirée le 05/10/2026** : l'éditeur Python ne pilote aucune carte. Elle pourra revenir avec la future version carte réelle, en interface Arduino (voir `JOURNAL_DES_DECISIONS.md`).

## Sécurité
TBT uniquement.

## Harmonisation du 26 août 2026

Dispositifs communs du dépôt installés — billet d'entrée hors progression, mode essentiel,
tableau de bord des six activités, versions étayées, durées à la convention, sélecteur de
parcours 🅱/🅲 réellement agissant, barre de progression reliée aux validations.
Contrôle mécanisé : **quatre manquements → zéro**. Suite committée : **37 tests, tous verts**
(`node tests_3e_C7.mjs .`).

**Le QCM avait ses 26 bonnes réponses toutes en position B** : cliquer la deuxième
proposition à chaque question donnait 26/26 sans rien savoir. Elles sont redistribuées sur
les quatre positions (outil `repartir_qcm.mjs`, dans `4e/4e_C7.1/`). Le QCM reste de la
génération ancienne — 26 questions, sans réfutation par distracteur : la mise à niveau au
standard des lots C9 n'est pas faite, et c'est dit plutôt que sous-entendu.
