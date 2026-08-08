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
