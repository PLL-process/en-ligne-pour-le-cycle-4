# Audit du 16/11/2026 — la barre d'étapes du mode mission et le retour en mission, dans les trois thèmes

Demande de Pascal, 16/11/2026, sur `4e_C9.1` (le jardin connecté se programme) :

> La progression de l'élève n'était pas suivie constamment […] un espèce de chenillard qui montre la progression de
> l'élève : certaines leds n'étaient pas allumées à un certain moment alors que l'élève avait fait le parcours. […]
> Quand l'élève quitte ce mode, il a du mal à revenir à cet affichage : il n'y a aucun bouton apparent.

puis : « L'existence de ces défauts potentiels doit être vérifiée, de façon générale, dans les 3 thèmes, afin d'y
remédier. »

## Ce qui causait les deux défauts

Le « chenillard » est la **barre d'étapes du mode mission** (un trait par écran de la séance). Le mode mission est un
outil commun (`_outils/mode_mission/`), posé à l'identique dans **les 60 pages** de séquence des trois thèmes (les 57
`sequence_*.html` et trois pages `sequence-…`) : un défaut de l'outil est donc dans toutes.

- **B1 — revenir en arrière éteint des écrans déjà faits.** Un écran sans question (la séance, le départ d'une
  activité, « je retiens ») ne s'allumait que s'il était **avant l'écran en cours**. L'élève qui revenait en arrière
  voyait s'éteindre tout ce qui suivait ; en avançant de nouveau, les traits se rallumaient. C'est le « pas suivi
  constamment, puis ça reprenait en compte ».
- **B2 — un écrit ne s'allumait jamais.** Un écran où l'on écrit (une justification, un pseudo-code), sans rien à
  vérifier ici, ne s'allumait qu'après « Vérifier » — un bouton qu'il n'a pas. Écrit et dépassé, il restait éteint.
- **B2 bis — ce qui est fait en page complète ne comptait pas.** Une question réussie en page complète restait éteinte
  en mission. Et une question répondue mais pas vérifiée ressemblait à une question pas faite.
- **B3 — pas de bouton pour revenir.** « 📄 Page complète » fait sortir du mode ; le seul bouton pour y revenir est en
  haut de la page, dans le cadre « Ma progression ». Dès que l'élève défile, il n'en voit plus aucun.

## Mesure, page par page

`_outils/mode_mission/banc_barre.mjs` (nouveau) joue chaque page comme un élève, à 1 280 px : il entre en mission,
parcourt la séance 1 par « Suivant » (il écrit sur les écrans à écrire, ne répond à aucune question à choix), revient
au deuxième écran, sort du mode, défile, cherche un bouton visible pour revenir et l'utilise. Lancé sur `main` (avant)
puis sur la branche (après) :

| Thème | Pages | B1 sur `main` | B2 sur `main` | B3 sur `main` | Après le correctif |
|---|---|---|---|---|---|
| 1 · Objets, systèmes, usages | 14 | 11 | 3 | 14 | 14 / 14 sans défaut |
| 2 · Structure, fonctionnement | 17 | 15 | 4 | 17 | 17 / 17 sans défaut |
| 3 · Création, conception | 29 | 24 | 5 | 27 | 29 / 29 sans défaut |
| **Total** | **60** | **50** | **12** | **58** | **60 / 60 sans défaut** |

Lecture : sur `main`, **aucune page n'est sans défaut**. B1 n'apparaît pas sur les 10 pages dont la séance 1 n'a pas
d'écran sans question au-delà du deuxième ; B2, seulement sur les 12 pages dont la séance 1 a un écrit sans
vérification ; B3 manque sur 2 pages courtes (`3e_C7.5`, `3e_C8.1`) où le bouton du haut reste à l'écran. Le banc
ne joue que la séance 1 : la cause étant dans l'outil commun, les autres séances avaient les mêmes défauts. Aucune
erreur de script, avant comme après.

## Ce qui est corrigé (dans l'outil commun, reposé dans les 60 pages)

- Un écran sans question s'allume une fois dépassé, **et le reste** : le mode garde, par séance, l'écran le plus loin
  atteint (`M.loin`, dans la sauvegarde de la mission) ; le dernier écran compte comme dépassé quand on passe à la
  séance suivante.
- Une question s'allume une fois vérifiée ; **répondue mais pas vérifiée, son trait se cercle** (« répondu, pas encore
  vérifié » pour un lecteur d'écran) : l'élève voit ce qu'il lui reste à vérifier.
- Un écrit s'allume une fois écrit.
- Ce qui a été réussi en page complète (toutes les réponses justes, ou la vérification de la page passée) s'allume à
  l'entrée dans le mode. Lu à l'entrée seulement : **pendant la mission, la barre ne dit jamais si une réponse est
  juste** (pas de tâtonnement possible par la barre).
- En page complète, dès que le bouton du haut sort de l'écran, **un petit « 🎮 Mode mission » reste en bas à droite** ;
  il ramène à l'écran où l'élève en était. Jamais imprimé. Si la page a déjà un bouton fixé dans ce coin (« ⬆ » de
  Book Train), il se pose au-dessus, sans le toucher (`controle_axe`, cible tactile). Dans la page, il est rangé à côté
  du bouton du haut, avant les onglets : `controle_squelette` (D5) ne le compte pas comme un contenu hors séance.

## Le banc du pilote, remis à jour

`banc_mission.mjs` échouait déjà sur `main` (46 / 50) : la page pilote (le lampadaire, `5e_C4.1`) a changé depuis
qu'il a été écrit. Sa séance 3 compte 7 écrans (9 avant) ; et ses questions de la séance 3 sont cachées par la page
elle-même, qui les remplace par ses cartes à classer. Le test 15 mesure désormais ce que **la mission** cache encore
après la sortie (rien), et non ce que la page cache d'elle-même. 50 / 50.

## Le détail, page par page

| Page | Écrans (séance 1) | B1 sur `main` | B2 sur `main` | B3 sur `main` | Après le correctif |
|---|---|---|---|---|---|
| T1 · 3e/3e_C1.1 | 15 | 1 | 1 | ✘ | ✅ |
| T1 · 3e/3e_C1.5 | 5 | — | — | ✘ | ✅ |
| T1 · 4e/4e_C1.1 | 6 | 1 | — | ✘ | ✅ |
| T1 · 4e/4e_C1.4 | 9 | — | — | ✘ | ✅ |
| T1 · 5e/5e_C1.1 | 15 | 1 | — | ✘ | ✅ |
| T1 · 5e/5e_C1.2 | 5 | — | — | ✘ | ✅ |
| T1 · 5e/5e_C1.3 | 6 | 1 | — | ✘ | ✅ |
| T1 · 5e/5e_C1.5 | 9 | 1 | 1 | ✘ | ✅ |
| T1 · 3e/3e_C2.1 | 11 | 1 | — | ✘ | ✅ |
| T1 · 4e/4e_C2.1 | 14 | 1 | 1 | ✘ | ✅ |
| T1 · 5e/5e_C2.1 | 12 | 1 | — | ✘ | ✅ |
| T1 · 3e/3e_C3.1 | 15 | 2 | — | ✘ | ✅ |
| T1 · 4e/4e_C3.1 | 15 | 2 | — | ✘ | ✅ |
| T1 · 5e/5e_C3.1 | 15 | 1 | — | ✘ | ✅ |
| T2 · 3e/3e_C4.1 | 14 | 4 | — | ✘ | ✅ |
| T2 · 3e/3e_C4.3 | 11 | 3 | — | ✘ | ✅ |
| T2 · 3e/3e_C4.7 | 15 | 3 | — | ✘ | ✅ |
| T2 · 3e/3e_C4.8 | 18 | 3 | 1 | ✘ | ✅ |
| T2 · 4e/4e_C4.1 | 11 | 2 | — | ✘ | ✅ |
| T2 · 4e/4e_C4.1_book-train | 10 | 5 | — | ✘ | ✅ |
| T2 · 4e/4e_C4.7 | 19 | 2 | 1 | ✘ | ✅ |
| T2 · 5e/5e_C4.1 | 11 | 1 | — | ✘ | ✅ |
| T2 · 5e/5e_C4.7 | 25 | 3 | 1 | ✘ | ✅ |
| T2 · 3e/3e_C5.1 | 15 | 3 | — | ✘ | ✅ |
| T2 · 4e/4e_C5.1 | 8 | 1 | — | ✘ | ✅ |
| T2 · 5e/5e_C5.1 | 7 | — | — | ✘ | ✅ |
| T2 · 3e/3e_C6.1 | 12 | 3 | — | ✘ | ✅ |
| T2 · 3e/3e_C6.2 | 17 | 2 | 1 | ✘ | ✅ |
| T2 · 4e/4e_C6.1 | 17 | 3 | — | ✘ | ✅ |
| T2 · 4e/4e_C6.2 | 17 | 7 | — | ✘ | ✅ |
| T2 · 5e/5e_C6.1 | 11 | — | — | ✘ | ✅ |
| T3 · 3e/3e_C7.1 | 11 | 2 | 1 | ✘ | ✅ |
| T3 · 3e/3e_C7.3 | 8 | 2 | 1 | ✘ | ✅ |
| T3 · 3e/3e_C7.4 | 10 | 1 | 1 | ✘ | ✅ |
| T3 · 3e/3e_C7.5 | 6 | 1 | — | — | ✅ |
| T3 · 3e/3e_C7.7 | 7 | 1 | — | ✘ | ✅ |
| T3 · 3e/3e_C7.8 | 13 | 1 | — | ✘ | ✅ |
| T3 · 4e/4e_C7.1 | 15 | 3 | — | ✘ | ✅ |
| T3 · 4e/4e_C7.3 | 7 | 2 | — | ✘ | ✅ |
| T3 · 4e/4e_C7.4 | 18 | 2 | — | ✘ | ✅ |
| T3 · 4e/4e_C7.5 | 8 | 2 | — | ✘ | ✅ |
| T3 · 4e/4e_C7.7 | 7 | 1 | — | ✘ | ✅ |
| T3 · 4e/4e_C7.8 | 12 | 1 | — | ✘ | ✅ |
| T3 · 5e/5e_C7.1 | 8 | 2 | 1 | ✘ | ✅ |
| T3 · 5e/5e_C7.3 | 7 | 2 | — | ✘ | ✅ |
| T3 · 5e/5e_C7.4 | 7 | 2 | — | ✘ | ✅ |
| T3 · 5e/5e_C7.5 | 6 | 2 | — | ✘ | ✅ |
| T3 · 3e/3e_C8.1 | 5 | 1 | — | — | ✅ |
| T3 · 3e/3e_C8.2 | 12 | 2 | 1 | ✘ | ✅ |
| T3 · 4e/4e_C8.1 | 12 | 1 | — | ✘ | ✅ |
| T3 · 5e/5e_C8.1 | 10 | 2 | — | ✘ | ✅ |
| T3 · 5e/5e_C8.2 | 13 | 2 | — | ✘ | ✅ |
| T3 · 3e/3e_C9.1 | 12 | 2 | — | ✘ | ✅ |
| T3 · 3e/3e_C9.2 | 13 | — | — | ✘ | ✅ |
| T3 · 3e/3e_C9.2 | 3 | — | — | ✘ | ✅ |
| T3 · 3e/3e_C9.2 | 8 | — | — | ✘ | ✅ |
| T3 · 3e/3e_C9.2 | 9 | — | — | ✘ | ✅ |
| T3 · 3e/3e_C9.2 | 13 | — | — | ✘ | ✅ |
| T3 · 4e/4e_C9.1 | 24 | 2 | — | ✘ | ✅ |
| T3 · 5e/5e_C9.1 | 12 | 2 | — | ✘ | ✅ |

B1 et B2 : le nombre d'écrans touchés dans la séance 1. Détail brut : `node _outils/mode_mission/banc_barre.mjs --json <fichier>`.

## Ce que l'audit ne couvre pas

- Le compteur de chaque page (« 2 / 6 activités validées », « Où en suis-je ? ») : il se met à jour à la vérification
  de chaque activité, page par page ; il n'est pas joué par ce banc.
- Un vrai téléphone, Firefox, Safari.
