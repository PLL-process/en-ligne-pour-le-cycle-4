# État des lieux — règles d'or n°23 à n°34 sur le Thème 2

Généré par `python _outils/verif_regles_audit.py theme-2-* --json` le 08/08/2026, **avant le rétrofit**.
Ce document dit ce qui a été **mécaniquement mesuré**. Les règles n°24, n°25, n°27, n°28 et n°32 relèvent du
jugement pédagogique : elles apparaissent en fin de document comme points à relire, jamais comme verdicts.

## Tableau de bord

| Séquence | n°23 durée | n°26 diagnostic d'entrée | n°29 mode essentiel | n°30 tableau de bord | n°31 version étayée | n°33 aération | n°34 accessibilité |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| `3e_C4.1-C4.2_energie_station` | ? | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ |
| `3e_C4.3-C4.6_station_alerte_cyclonique` | ? | · | ✘ | ✘ | ✘ | ✔ | ✔ |
| `3e_C4.7-C4.8_internet_sainte_luce` | ? | · | ✘ | ✘ | ✘ | ✔ | ✔ |
| `3e_C4.7-C4.8_pont_numerique_packet_tracer` | ✘ | ✔ | ✔ | ✘ | ✘ | ▲ | ✘ |
| `4e_C4.1-C4.9_jardin_connecte` | ? | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ |
| `4e_C4.1-C4.2-C4.4_book-train` | ? | ✘ | ✘ | · | ✘ | ▲ | ✘ |
| `4e_C4.7-C4.9_sos_serre_packet_tracer` | ✘ | ✔ | ✔ | ✘ | ✔ | ✘ | ✘ |
| `5e_C4.1-C4.8_lampadaire_intelligent` | ? | ✘ | ✘ | ✘ | ✘ | ✔ | ✘ |
| `5e_C4.7-C4.8_reseau_local_packet_tracer` | ✔ | ✔ | ✔ | ✘ | ✘ | ▲ | ✘ |
| `3e_C5.1-C5.4_sos_station_reparer` | ? | · | ✘ | ✘ | ✘ | ✔ | ✘ |
| `4e_C5.1-C5.3_depanner_jardin` | ? | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ |
| `5e_C5.1-C5.3_depanner_lampadaire` | ? | · | ✘ | ✘ | ✘ | ✔ | ✔ |
| `3e_C6.1-C6.3_programmer_alerte` | ? | · | ✘ | ✘ | ✘ | ✔ | ✘ |
| `algorigrammes_dnb` | ? | · | ✘ | · | · | ✔ | ✔ |
| `4e_C6.1-C6.3_ajuster_programme_jardin` | ? | · | ✘ | ✘ | ✘ | ✔ | ✘ |
| `5e_C6.1-C6.3_programmer_lampadaire` | ? | ✘ | ✘ | ✘ | ✘ | ✔ | ✔ |

Légende : ✔ conforme · ✘ manquement établi · ▲ à surveiller · · sans objet · ? non mesurable en l'état

## Règle par règle

- **n°23 durée** — 13 ?, 2 ✘, 1 ✔
- **n°26 diagnostic d'entrée** — 7 ·, 6 ✘, 3 ✔
- **n°29 mode essentiel** — 13 ✘, 3 ✔
- **n°30 tableau de bord** — 14 ✘, 2 ·
- **n°31 version étayée** — 14 ✘, 1 ✔, 1 ·
- **n°33 aération** — 12 ✔, 3 ▲, 1 ✘
- **n°34 accessibilité** — 9 ✘, 7 ✔

## Points de jugement signalés pour relecture humaine

**sequence_3e_C4.1-C4.2_energie_station.html**
- n°27 : « mesures réelles » — préciser qu'il s'agit d'une simulation

**sequence_3e_C4.7-C4.8_pont_numerique_packet_tracer.html**
- n°27 : « mesures réelles » — préciser qu'il s'agit d'une simulation

**sequence_4e_C4.7-C4.9_sos_serre_packet_tracer.html**
- n°27 : « 0 % loss » sans bornage au test en cours

## Lecture honnête de ce tableau

**59 manquements mécaniques** sur 16 séquences. Ce chiffre ne dit pas que le Thème 2 est mauvais : il dit
que douze règles écrites aujourd'hui n'existaient pas quand ces lots ont été produits. Trois d'entre elles —
n°29 mode essentiel, n°30 tableau de bord, n°31 version étayée — concentrent la majorité des lignes rouges,
et sont mécanisables : le rétrofit sera long mais peu risqué.

La règle n°23 sort majoritairement en « ? » : la plupart des séquences n'annoncent pas de durée par activité.
Ce n'est pas une conformité, c'est une **absence de donnée** — il faudra la produire lot par lot, à la main,
en connaissant le contenu. C'est le poste le plus coûteux du chantier.

Les trois lots réseaux (5e, 4e, 3e) sont déjà partiellement conformes : ils viennent d'être repris après
l'audit. C'est visible dans le tableau, et c'est normal — ils ont servi de terrain d'essai aux règles.

Enfin, 3 points relèvent du jugement pédagogique et ne seront jamais tranchés par un script.
