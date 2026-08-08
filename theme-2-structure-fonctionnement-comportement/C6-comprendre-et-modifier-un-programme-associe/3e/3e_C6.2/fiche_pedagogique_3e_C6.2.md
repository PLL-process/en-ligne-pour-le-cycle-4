# Fiche pédagogique — 3e_C6.2 « L'auto-test de la station »

**Niveau** 3e · **Thème 2** Structure, fonctionnement et comportement des objets et systèmes
**Code visé** 3e_C6.2 — *Programmer un algorithme lié à une nouvelle fonctionnalité*
**Durée** 3 séances de 55 min (144 min d'activités annoncées pour 165 disponibles)
**Objet-fil du niveau** la station d'alerte cyclonique de Sainte-Luce

## Pourquoi cet atelier existe

Le libellé officiel du code dit **programmer**, et il dit **nouvelle fonctionnalité**. Ni lire,
ni modifier. C'est ce qui le sépare de ses deux voisins :

- **3e_C6.1** — déterminer les données utilisées et produites : l'élève *lit* un programme ;
- **3e_C6.2** — cet atelier : l'élève *écrit*, à partir d'un besoin exprimé en français ;
- **3e_C6.3** — modifier et tester : l'élève *retouche* un programme existant.

Le dossier contenait jusqu'ici une excellente banque d'entraînement DNB (30 exercices,
13 schémas) qui fait *lire* des algorigrammes. Elle est conservée telle quelle et devient la
ressource d'appui de la séance 1 ; elle ne couvre pas, à elle seule, le verbe du libellé.

## La situation déclenchante

Après le passage d'un cyclone, la mairie constate que la station a bien alerté — mais que
personne ne savait, la veille, si elle fonctionnait encore. Le gardien demande une
fonctionnalité nouvelle : **un auto-test quotidien**. Chaque matin à 7 h, la station teste ses
quatre organes (anémomètre, gyrophare, sirène, liaison radio), compte les défauts et envoie
**un seul** message.

C'est un besoin réel, formulé par une personne, et il est impossible à satisfaire sans un
compteur, une boucle et une décision — exactement les notions du code.

## Problématique

> Comment écrire, de zéro, l'algorithme d'une fonctionnalité qui n'existe pas encore ?

## Déroulé

### Séance 1 — Comprendre la demande et concevoir (55 min)

| Temps | Activité | Production |
|---|---|---|
| 4 min | **Billet d'entrée sans note** — variable, test, boucle (acquis de 4e) | 3 réponses + aiguillage automatique vers les rappels |
| ~20 min | **Activité 1** — de quoi l'auto-test a-t-il besoin ? | Classement entrées / sorties, et désignation de la *sortie utile* |
| ~30 min | **Activité 2** — CONCEVOIR l'algorigramme, **avant toute référence** (règle n°22) | Algorigramme au brouillon, relu et annoté par le binôme |

### Séance 2 — Écrire l'algorithme (55 min)

| Temps | Activité | Production |
|---|---|---|
| ~30 min | **Activité 3** — remettre 8 instructions dans l'ordre, et écrire celle qui manque | Algorithme complet et indenté |
| ~25 min | **Activité 4** — le banc d'essai, face à la panne (**verrou expérientiel : 2 essais exigés**) | Deux exécutions tracées, dont une sans panne et une à deux pannes |

### Séance 3 — Éprouver et valider (55 min)

| Temps | Activité | Production |
|---|---|---|
| ~35 min | **Activité 5** — cas limites et message utile à un humain | Tableau de suivi déroulé, analyse du cas radio, message rédigé |
| reste | Synthèse, bilan avec auto-positionnement, QCM d'entraînement | 30 questions, 3 illustrées |

## Les trois obstacles, dans l'ordre où ils tombent

1. **Le compteur placé dans la boucle.** Il finit toujours à 0 ou 1. Ne pas prévenir : le banc
   d'essai le montre mieux qu'une explication.
2. **Le message envoyé dans la boucle.** Le gardien en reçoit quatre. Question qui débloque :
   « à quel moment sais-tu combien il y a de défauts ? ».
3. **La panne qui arrête tout.** Sortir de la boucle au premier défaut, c'est ignorer les
   organes suivants — un auto-test partiel rassure à tort.

## Le cas limite, qui n'est pas un bonus

La liaison radio est **à la fois** un organe testé et le canal du message. Si elle tombe, le
message est calculé correctement et ne part jamais : le système est en panne **et** muet. Le
remède ne s'écrit pas dans la boucle — c'est le gardien qui doit s'inquiéter de *l'absence* de
message. La classe découvre là que tout système d'alerte doit prouver qu'il est vivant.

## Évaluation

Conformément à la **règle d'or n°28**, la compétence se prouve **en situation** : la preuve
retenue est l'algorigramme conçu par l'élève avant toute référence, puis éprouvé sur deux jeux
d'essai qu'il choisit. Le QCM de 30 questions est un **entraînement**, jamais la mesure.

Indicateurs de réussite :

- le compteur est initialisé **avant** la boucle ;
- la boucle couvre les quatre organes et ne s'interrompt pas au premier défaut ;
- la décision est **unique** et postérieure à la boucle ;
- le message nomme les organes en défaut ;
- l'élève sait dire ce que son test **ne prouve pas**.

## Socle et CRCN

**Socle** : D1.3 (langages scientifiques et techniques), D2 (méthodes et outils pour
apprendre), D4 (systèmes naturels et techniques).

**CRCN réellement travaillé par l'activité** — et non collectionné en étiquettes (règle n°7) :

- **3.4 Programmer**, niveau 3 : l'élève écrit un algorithme comportant une boucle et une
  condition, l'éprouve sur des jeux d'essai et corrige à partir du résultat observé ;
- **2.3 Collaborer**, niveau 2 : la relecture de l'algorigramme par le binôme, en séance 1,
  est une étape obligatoire du parcours, pas un ajout décoratif.

## Différenciation

- **Mode essentiel** (n°29) : masque référentiel, corrections et compléments, à tout moment.
- **Versions étayées** (n°31) : les cinq productions écrites existent en phrases à compléter,
  à exigence scientifique identique.
- **Bandeau de tâches** (n°30) : libellés écrits à la main, séance par séance.
- **Billet d'entrée sans note** (n°26) : il oriente, il ne sanctionne pas — et la page le dit.
- **Pour les plus rapides** : ajouter un cinquième organe sans réécrire la boucle ; proposer
  une fréquence d'auto-test et la justifier ; concevoir le journal des auto-tests.

## Matériel

Aucun. L'atelier se mène sur la page, hors ligne, sans compte et sans envoi de données. Le
banc d'essai est intégré à la séquence. Le papier et le crayon restent l'outil de la séance 1 :
l'algorigramme se conçoit à la main.
