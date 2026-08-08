# État des lieux — règles d'or n°23 à n°34 sur le Thème 2

Généré par `python _outils/verif_regles_audit.py theme-2-* --json` le 08/08/2026, **après le rétrofit C4**.
Ce document dit ce qui a été **mécaniquement mesuré**. Les règles n°24, n°25, n°27, n°28 et n°32 relèvent du
jugement pédagogique : elles apparaissent en fin de document comme points à relire, jamais comme verdicts.

> **Historique du compte.** 59 manquements annoncés au départ, puis 54 après correction d'un défaut du
> vérificateur lui-même, puis 50 après les rétrofits C5 et C6, et **33 après le rétrofit C4**. Les seize
> séquences du thème disposent désormais du mode essentiel, chacune vérifiée au navigateur.

## Tableau de bord

| Séquence | n°23 durée | n°26 diagnostic d'entrée | n°29 mode essentiel | n°30 tableau de bord | n°31 version étayée | n°33 aération | n°34 accessibilité |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| `3e_C4.1-C4.2_energie_station` | ? | ✘ | ✔ | ✘ | ✘ | ✔ | ✔ |
| `3e_C4.3-C4.6_station_alerte_cyclonique` | ? | · | ✔ | ✘ | ✘ | ✔ | ✔ |
| `3e_C4.7-C4.8_internet_sainte_luce` | ? | · | ✔ | ✘ | ✘ | ✔ | ✔ |
| `3e_C4.7-C4.8_pont_numerique_packet_tracer` | ✔ | ✔ | ✔ | ✘ | ✘ | ▲ | ✔ |
| `4e_C4.1-C4.9_jardin_connecte` | ? | ✘ | ✔ | ✘ | ✘ | ✔ | ✔ |
| `4e_C4.1-C4.2-C4.4_book-train` | ✔ | ✔ | ✔ | · | ✔ | ✔ | ✔ |
| `4e_C4.7-C4.9_sos_serre_packet_tracer` | ✔ | ✔ | ✔ | ✘ | ✔ | ▲ | ✔ |
| `5e_C4.1-C4.8_lampadaire_intelligent` | ? | ✘ | ✔ | ✘ | ✘ | ✔ | ✔ |
| `5e_C4.7-C4.8_reseau_local_packet_tracer` | ✔ | ✔ | ✔ | ✘ | ✘ | ▲ | ✔ |
| `3e_C5.1-C5.4_sos_station_reparer` | ? | · | ✔ | ✘ | ✘ | ✔ | ✔ |
| `4e_C5.1-C5.3_depanner_jardin` | ? | ✘ | ✔ | ✘ | ✘ | ✔ | ✔ |
| `5e_C5.1-C5.3_depanner_lampadaire` | ? | · | ✔ | ✘ | ✘ | ✔ | ✔ |
| `3e_C6.1-C6.3_programmer_alerte` | ? | · | ✔ | ✘ | ✘ | ✔ | ✔ |
| `algorigrammes_dnb` | ? | · | ✘ | · | · | ✔ | ✔ |
| `4e_C6.1-C6.3_ajuster_programme_jardin` | ? | · | ✔ | ✘ | ✘ | ✔ | ✔ |
| `5e_C6.1-C6.3_programmer_lampadaire` | ? | ✘ | ✔ | ✘ | ✘ | ✔ | ✔ |

Légende : ✔ conforme · ✘ manquement établi · ▲ à surveiller · · sans objet · ? non mesurable en l'état

## Règle par règle

- **n°23 durée** — 12 ?, 4 ✔
- **n°26 diagnostic d'entrée** — 7 ·, 5 ✘, 4 ✔
- **n°29 mode essentiel** — 15 ✔, 1 ✘
- **n°30 tableau de bord** — 14 ✘, 2 ·
- **n°31 version étayée** — 13 ✘, 2 ✔, 1 ·
- **n°33 aération** — 13 ✔, 3 ▲
- **n°34 accessibilité** — 16 ✔

## Points de jugement signalés pour relecture humaine

**sequence_3e_C4.1-C4.2_energie_station.html**
- n°27 : « mesures réelles » — préciser qu'il s'agit d'une simulation

**sequence_3e_C4.7-C4.8_pont_numerique_packet_tracer.html**
- n°27 : « mesures réelles » — préciser qu'il s'agit d'une simulation

**sequence_4e_C4.7-C4.9_sos_serre_packet_tracer.html**
- n°27 : « 0 % loss » sans bornage au test en cours

## Ce qui reste, et pourquoi

**33 manquements mécaniques.** Ils se concentrent désormais sur les trois règles qu'aucun script ne peut
traiter : le **diagnostic d'entrée** (n°26) demande d'écrire des questions justes sur les prérequis, le
**tableau de bord des tâches** (n°30) demande de nommer les tâches de chaque séance, et la **version étayée**
(n°31) demande de rédiger des amorces de phrases qui tiennent debout. Ce sont des travaux de rédaction.

La règle n°23 reste en « ? » sur les séquences-îlots : elles n'annoncent aucune durée par activité. Ce n'est
pas une conformité, c'est une **absence de donnée** — il faut connaître le contenu pour la produire.

Les quatre lots qui ont servi de terrain d'essai aux règles (les trois ateliers réseaux et le Book Train)
sont, eux, largement conformes — y compris sur la n°23, dont deux d'entre eux étaient en faute avant ce
rétrofit : le pont numérique annonçait 169 min pour 165 disponibles, et SOS serre comptait comme activité
une note destinée à l'enseignant.

Enfin, 3 points relèvent du jugement pédagogique et ne seront jamais tranchés par un script.

---

## Mise à jour du 08/08/2026 — lot 3e_C6.2 « L'auto-test de la station »

Le dépôt compte désormais **17 séquences analysées** au lieu de 16, et toujours **33 manquements**.
La séquence ajoutée n'en apporte aucun : elle a été écrite conforme aux règles n°23 à n°34 dès le
départ, et le vérificateur la donne **7 sur 7**. C'est la première fois qu'une séquence naît conforme
plutôt que d'être rétrofitée — et c'est nettement moins cher.

Un cas mérite d'être nommé pour éviter qu'on le prenne un jour pour un oubli :
`sequence_algorigrammes_dnb.html`, la banque d'entraînement héritée du dossier 3e_C6.2, reste en
échec sur la règle n°29. Elle n'est **pas** bâtie sur le gabarit maison — pas de barre d'outils, pas
de `restore()` — et l'outil de rétrofit a refusé de la traiter plutôt que d'y poser un mode essentiel
à moitié câblé. Son statut d'audit devient **ressource d'entraînement**, ce qui est sa nature réelle.
Ce manquement est donc **assumé**, pas en attente.

---

## Mise à jour du 08/08/2026 (2) — les versions étayées du Thème 2 (règle n°31)

**33 → 20 manquements.** Les treize séquences du Thème 2 qui exigeaient une production écrite
sans proposer de version étayée en ont désormais une pour **chacune** de leurs zones de rédaction :
**67 blocs**, écrits à la main, zone par zone.

Ce n'est pas un rétrofit mécanique. Les amorces sont dans `_outils/amorces_versions_etayees.py`,
rédigées une par une à partir de la consigne réelle ; `_outils/poser_versions_etayees.py` ne fait
que les installer, et **refuse d'écrire un fichier** dont toutes les amorces n'ont pas été écrites.
C'est la leçon du bandeau de tâches : mécaniser une règle de forme est facile, mécaniser une règle
de sens ne l'est pas.

Un cas mérite d'être noté. La séquence 3e_C6.1 contient un `textarea` qui n'est **pas** une zone de
rédaction : c'est l'éditeur de code Python (`clTa`). Y poser une version étayée aurait été absurde.
Le script l'a laissé de côté et l'a dit en clair dans son compte rendu — un outil doit annoncer ce
qu'il n'a pas traité, pas le passer sous silence.

### Ce qui reste : 20 manquements

- **n°26 diagnostic d'entrée** — les séquences qui s'appuient sur l'année précédente sans billet
  d'entrée sans note ;
- **n°30 tableau de bord des tâches** — les libellés doivent être écrits à la main, séance par
  séance ;
- **n°29 mode essentiel** — uniquement la banque d'entraînement DNB héritée, écart déjà assumé ;
- **n°23 durée** — reste en «&nbsp;?&nbsp;» sur les séquences-îlots, qui n'annoncent aucune durée
  par activité : c'est une absence de donnée, pas une conformité.

---

## Mise à jour du 08/08/2026 (3) — les tableaux de bord des tâches (règle n°30)

**20 → 6 manquements.** Les quatorze séquences du Thème 2 qui enchaînaient plusieurs tâches sans
situer l'élève ont désormais leur bandeau : **79 tâches**, dont le libellé est écrit à la main,
séance par séance.

Les libellés sont dans `_outils/libelles_bandeaux_taches.py` ; `_outils/poser_bandeaux_taches.py`
ne fait que les installer, et **refuse d'écrire un fichier** dont la liste des tâches ne recouvre
pas exactement les boutons `data-check` réellement présents, ou dont une clé de séance n'existe
pas dans la page. C'est la garde née de l'échec du matin : l'extraction automatique des titres
avait produit des tâches trompeuses.

### Ce qui reste : 6 manquements

- **n°26 diagnostic d'entrée** — 5 séquences invoquent l'année précédente sans billet d'entrée
  sans note ;
- **n°29 mode essentiel** — la seule banque d'entraînement DNB héritée, écart déjà assumé.

La règle n°23 reste en «&nbsp;?&nbsp;» sur les séquences-îlots, qui n'annoncent aucune durée par
activité : c'est une absence de donnée, pas un manquement — et elle demande un jugement
d'enseignant, pas un script.

---

## Mise à jour du 08/08/2026 (4) — les diagnostics d'entrée (règle n°26)

**6 → 1 manquement.** Et sur les cinq signalements, **un seul** était réel.

Le vérificateur cherchait «&nbsp;en 5e&nbsp;», «&nbsp;en 4e&nbsp;», «&nbsp;l'an dernier&nbsp;»
n'importe où dans la page. Il comptait donc comme invocation d'un prérequis&nbsp;:

- un **distracteur** de liste déroulante («&nbsp;…parce que plier est interdit en 4e&nbsp;») ;
- une **correction repliée** qui raconte la progression («&nbsp;en 5e la chaîne était fournie, en
  3e tu l'as élaborée&nbsp;») ;
- une **annonce de la suite** («&nbsp;tu la verras de près en 4e et en 3e&nbsp;», dans une
  séquence de 5e) ;
- le **niveau de la séquence elle-même** («&nbsp;en 4e, on ne reçoit plus le protocole&nbsp;»,
  dans une séquence de 4e).

`regle_26` ne lit désormais que le texte de consigne — hors `option`, hors correction repliée — et
ne retient qu'un niveau **antérieur** à celui de la séquence, déduit de son nom de fichier.

Une seule séquence invoquait réellement l'année précédente sans filet&nbsp;:
`sequence_4e_C4.1-C4.9_jardin_connecte.html` («&nbsp;En 5e vous avez appris à lire UN objet
simple&nbsp;»). Elle a reçu son billet d'entrée sans note, avec capsule de rattrapage de 5e.

### Ce qui reste : 1 manquement

Le mode essentiel de `sequence_algorigrammes_dnb.html`, la banque d'entraînement héritée — écart
assumé et documenté depuis le lot 3e_C6.2.

La règle n°23 reste en «&nbsp;?&nbsp;» sur les séquences-îlots&nbsp;: absence de donnée, et
jugement d'enseignant.

---

## Mise à jour du 08/08/2026 (5) — archivage de la banque DNB d'origine

**1 → 0 manquement.** Le Thème 2 ne compte plus aucun manquement mécanique.

Le dernier n'était pas un défaut à corriger mais une **décision à prendre**&nbsp;: la banque
d'entraînement d'origine, remplacée le matin même, restait dans le dossier actif à côté de son
remplaçant. Elle est désormais dans
`_archive-anciennes-versions/C6-comprendre-et-modifier-un-programme-associe/3e_C6.2-banque-dnb-v1/`,
contenu **non modifié**, avec un README qui explique ce qu'elle est et pourquoi elle a été
remplacée.

Le vérificateur analyse 16 séquences au lieu de 17&nbsp;: c'est la séquence archivée qui sort du
champ, pas un fichier perdu.

### Le compte de la journée

| Étape | Manquements |
|---|---|
| au réveil, avant l'audit externe | 61 |
| après le correctif du vérificateur (aria-label) | 54 |
| après les rétrofits mode essentiel | 33 |
| après les 67 versions étayées (n°31) | 20 |
| après les 79 bandeaux de tâches (n°30) | 6 |
| après les diagnostics d'entrée (n°26) | 1 |
| après l'archivage de la banque d'origine | **0** |

La règle n°23 reste en «&nbsp;?&nbsp;» sur les séquences-îlots&nbsp;: absence de donnée, et
jugement d'enseignant. Les règles n°24, 25, 27, 28 et 32 relèvent du jugement par construction.
