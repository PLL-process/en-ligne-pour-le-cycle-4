# Suivi de la révision des trois thèmes

Décision de Pascal du 08/11/2026 : « une révision des 3 thèmes s'impose » ; « depuis longtemps cela me paraissait une
charge cognitive » ; « 1. Oui [la passe complète par séquence] 2. Ordre : c'est urgent, donc tu as carte blanche pour tous
les thèmes de toutes les séquences ». Méthode : skill `revision-sequence`. Une ligne par séquence, dans l'ordre de passage
(les classeurs de progression : ce qui passe en classe le plus tôt d'abord, les trois niveaux entrelacés).

**Les colonnes.**
- **Séance la plus lourde** : les mots que l'élève voit à l'ouverture de sa séance la plus chargée, sans rien déplier, à
  390 px (`node _outils/mesurer_charge.mjs`). Repère : 1 200 mots, soit 10 minutes de lecture seule.
- **✘ règles** : `verif_regles_audit.py` sur la page. **Menus** : questions encore posées par une liste déroulante (n°300).
- **Aération** : écarts de `audit_aeration.py` (légendes et corrections d'un seul tenant).
- Avant → après quand la passe est faite. La dernière colonne est lue par `_outils/bilan_revision.py`.

**État de départ, 08/11/2026** (56 séquences, 188 séances) : médiane 1 134 mots visibles par séance ; **86 séances au-delà
de 1 200** ; le mode essentiel retire 2 % du texte ; 87 ✘ de règles, 995 questions en listes déroulantes et 897 écarts d’aération sur les pages de séquence (914 comptés d'abord : l'audit lisait aussi la description des schémas SVG, corrigé le jour même) ; **1 séquence propre** (5e_C3.1).

| N° | Séquence | Séance la plus lourde (mots) | ✘ règles | Menus | Aération | État |
|---|---|---|---|---|---|---|
| 1 | `5e_C1.5` | 1549 → 1322 | 4 → 0 | 27 → 0 | 18 → 0 | livrée #619 |
| 2 | `5e_C1.3` | 1050 → 1043 | 0 | 0 | 5 → 0 | livrée #620 |
| 3 | `4e_C1.1` | 3570 → 2911 | 0 | 0 | 22 → 0 | livrée #620 — séance 5 : décision de Pascal |
| 4 | `4e_C1.4` | 1291 → 1172 | 0 | 0 | 9 → 0 | livrée #PRNUM |
| 5 | `3e_C1.5` | 2017 | 0 | 0 | 19 | à faire |
| 6 | `3e_C2.1` | 1861 | 0 | 0 | 6 | à faire |
| 7 | `5e_C1.1` | 1629 | 0 | 0 | 26 | à faire |
| 8 | `5e_C1.2` | 2117 | 0 | 0 | 26 | à faire |
| 9 | `5e_C3.1` | 2912 | 0 | 0 | 0 | à faire |
| 10 | `4e_C2.1` | 2625 | 1 | 0 | 24 | à faire |
| 11 | `4e_C3.1` | 1850 | 0 | 0 | 10 | à faire |
| 12 | `3e_C4.1` | 1444 | 1 | 33 | 6 | à faire |
| 13 | `3e_C4.3` | 1928 | 2 | 33 | 8 | à faire |
| 14 | `5e_C2.1` | 2272 | 0 | 0 | 20 | à faire |
| 15 | `4e_C4.1` | 2394 | 1 | 39 | 11 | à faire |
| 16 | `4e_C4.1_book-train` | 2752 | 0 | 0 | 14 | à faire |
| 17 | `3e_C4.7` | 1169 | 1 | 28 | 8 | à faire |
| 18 | `3e_C4.8` | 2076 | 1 | 30 | 9 | à faire |
| 19 | `3e_C5.1` | 1238 | 1 | 30 | 5 | à faire |
| 20 | `3e_C6.1` | 1135 | 1 | 23 | 9 | à faire |
| 21 | `3e_C6.2` | 1285 | 1 | 32 | 5 | à faire |
| 22 | `5e_C4.1` | 2663 | 1 | 64 | 17 | à faire |
| 23 | `5e_C6.1` | 1023 | 1 | 30 | 5 | à faire |
| 24 | `4e_C5.1` | 1316 | 1 | 30 | 4 | à faire |
| 25 | `4e_C6.1` | 1460 | 1 | 28 | 6 | à faire |
| 26 | `4e_C6.2` | 1990 | 6 | 25 | 18 | à faire |
| 27 | `3e_C9.1` | 1597 | 1 | 33 | 11 | à faire |
| 28 | `3e_C7.1` | 3512 | 1 | 20 | 12 | à faire |
| 29 | `5e_C5.1` | 1109 | 1 | 30 | 4 | à faire |
| 30 | `4e_C4.7` | 2022 | 1 | 40 | 7 | à faire |
| 31 | `5e_C4.7` | 1807 | 1 | 35 | 6 | à faire |
| 32 | `3e_C7.3` | 1796 | 0 | 0 | 29 | à faire |
| 33 | `3e_C7.4` | 1220 | 0 | 0 | 27 | à faire |
| 34 | `3e_C7.5` | 1439 | 0 | 0 | 26 | à faire |
| 35 | `3e_C7.7` | 1959 | 0 | 0 | 24 | à faire |
| 36 | `3e_C7.8` | 1530 | 0 | 0 | 21 | à faire |
| 37 | `3e_C8.1` | 1888 | 0 | 0 | 23 | à faire |
| 38 | `3e_C8.2` | 1414 | 0 | 0 | 28 | à faire |
| 39 | `3e_C9.2` | 2597 | 2 | 62 | 48 | à faire |
| 40 | `4e_C7.1` | 1780 | 2 | 22 | 28 | à faire |
| 41 | `4e_C7.3` | 1866 | 5 | 13 | 27 | à faire |
| 42 | `4e_C7.4` | 1582 | 5 | 22 | 23 | à faire |
| 43 | `4e_C7.5` | 2077 | 5 | 23 | 25 | à faire |
| 44 | `4e_C7.7` | 1831 | 5 | 16 | 19 | à faire |
| 45 | `4e_C7.8` | 1880 | 5 | 19 | 15 | à faire |
| 46 | `4e_C8.1` | 1975 | 1 | 25 | 22 | à faire |
| 47 | `4e_C9.1` | 2909 | 1 | 54 | 34 | à faire |
| 48 | `5e_C7.1` | 1685 | 1 | 17 | 17 | à faire |
| 49 | `5e_C7.3` | 1694 | 5 | 15 | 15 | à faire |
| 50 | `5e_C7.4` | 1607 | 5 | 18 | 16 | à faire |
| 51 | `5e_C7.5` | 1528 | 5 | 22 | 8 | à faire |
| 52 | `5e_C8.1` | 1421 | 5 | 17 | 13 | à faire |
| 53 | `5e_C8.2` | 1412 | 5 | 16 | 12 | à faire |
| 54 | `5e_C9.1` | 1761 | 1 | 24 | 5 | à faire |
| 55 | `3e_C1.1` | 1451 | 0 | 0 | 23 | à faire |
| 56 | `3e_C3.1` | 1939 | 0 | 0 | 19 | à faire |

## Notes par séquence

- **5e_C1.5** (le compte du club), 08/11/2026 : ancien gabarit → gabarit commun (`migrer_gabarit_306.py`, 25 listes →
  groupes, 4 versions étayées) ; trois **grilles** (`grilles_radio.py`) : 14 questions qui partageaient leurs réponses
  les lisent une fois, lettrées ; 40 retours à la ligne dans les corrections (`aerer_corrections.py`) ; 13 consignes et
  annonces de plus de 25 mots coupées en lignes. Séance 3 : 1 549 → 1 322 mots, au-dessus du repère : c'est la séance
  de clôture (synthèse, banc de publication pour le Bonus, Bonus facultatif, bilan) ; sans le Bonus et son banc, elle
  passe sous 1 000.
- **5e_C1.3** (les vélos de Hangzhou), 08/11/2026 : déjà sous le repère (1 050 / 217 / 718 mots). 14 retours à la ligne
  dans les corrections, 5 hors corrections (`aerer_corrections.py --partout`) ; les trois « Au programme », la consigne
  de l'activité 2, le transfert et le bilan en lignes ;
  l'incrustation de l'atelier « carte mentale » allégée (la définition de « donnée » y était dite trois fois, l'intro ne
  la redit plus ; la consigne passe en ① ② ⚠), corrigée à l'identique dans sa source (`donnees_carte_mentale.py`,
  `incrustations_lots/donnees_et_validation.py`), l'atelier de 5e et le cahier de 5e — le générateur, rejoué à part,
  produit le même texte.
- **4e_C1.1** (Tsinghua, les feux), 08/11/2026 :
  - séance 1 : 1 641 → 921 mots. Les 15 captures des quatre gestes du tableur se déplient à la demande
    (`replier_captures.py`) : chaque geste reste écrit en toutes lettres, ses images et leurs légendes sont à un clic ;
  - séance 5 : 3 570 → 2 911 mots. La piqûre de rappel de la bête à cornes est repliée (option `replie` des
    incrustations) ; les introductions des deux blocs d'exercices et de l'activité 5 ne redisent plus l'objectif ;
  - 75 retours à la ligne (corrections, consignes, définitions, légendes) ; trois légendes réécrites ; six corrections
    des ateliers aérées à leur source (`donnees_besoin.py`, `donnees_carte_mentale.py`), dans les ateliers, les cahiers
    et les séquences qui les portent ;
  - **la séance 5 reste au-dessus du repère** : trois exercices d'atelier de 12 à 15 minutes (séance voulue par Pascal
    le 24/10/2026), dont le texte visible vient des exercices eux-mêmes. Deux pistes, à trancher par Pascal : la
    scinder en deux séances, ou rendre l'exercice 3 (« Corriger une carte mentale mal faite ») facultatif.
- **4e_C1.4** (cybersécurité), 08/11/2026 : séance 3 (traces, propriété intellectuelle et clôture) 1 291 → 1 172 mots : les
  trois défis du Bonus et les exemples de 5.b se déplient à la demande, les mises en situation passent en lignes (une
  phrase par ligne, « la bonne attitude » en ①②③), l'exemple de 5.b qui répétait la liste tombe. Corrections aérées
  (`aerer_corrections.py --partout`, puis les deux blocs de plus de 45 mots à la main) ; vouvoiements restants passés au tu.
  **Lu comme un élève, à 390 px** : (1) neuf zones de réponse sur dix-huit gardaient la taille par défaut du navigateur
  (~180 px) → pleine largeur partout ; (2) le jeu des licences 6.c ne pouvait pas se jouer — chaque zone ne gardait qu'une
  étiquette alors qu'une licence va dans plusieurs catégories, et les infobulles n'existaient qu'au survol → les zones
  reçoivent une copie, la licence reste dans la réserve, double-clic pour retirer, légende des sigles repliée, infobulles
  au toucher (focus) et jamais plus larges que l'écran ; les étiquettes et les cas de 6.b se lisent sans survol ;
  (3) la barre de score collante prenait 178 px sur 844 à chaque écran → elle défile avec la page sur téléphone ; le
  bloc Python élargissait la page à 718 px → le code défile dans son cadre. Au passage : 6.a compte dans le score de la
  section (il annonçait 2 points sans être lu), 6.b dit « non noté », 5.c dit ses 7 questions, aide et correction de la
  section 6 réécrites avec les mots du jeu, dépôt au clavier réparé (zones focalisables, `dragstart` synthétique sans
  `dataTransfer`). Hors parcours Python inchangé sur le fond (686 mots).

