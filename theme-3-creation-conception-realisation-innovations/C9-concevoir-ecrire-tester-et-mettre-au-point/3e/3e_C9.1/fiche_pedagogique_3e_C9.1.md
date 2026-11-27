# Fiche pédagogique — Atelier « Variables, types et systèmes » (3e_C9.1)

**Thème 3 · New York · Arc variables (marche 3e)** — refonte de la ressource « Vittascience :
variables » (enquête Vittascience adaptée P. Gouacide), archivée selon la règle d'or n°12.

## Compétence officielle
**3e_C9.1** — Élaborer ou concevoir un algorithme permettant de répondre au besoin visé, puis le
traduire en un programme structuré (appel de sous-programmes ou de fonctions), le tester et le
mettre au point. **Socle : D1.3, D2, D4 · CRCN 3.4 Programmer (Niv. 3, règle n°7 : action = expériences
exécutées dans l'éditeur Vittascience + programme corrigé ; trace = réponses/badges sauvegardés).**

## Pourquoi cet atelier (le vrai besoin)
Constat de terrain (Pascal, tous niveaux) : les élèves programment par blocs depuis la 6e **sans avoir
conceptualisé la variable**. L'atelier attaque ce mur frontalement : boîte étiquetée → types →
lecture de programme → mise au point, sur un fil narratif New York (le panneau bugué du quai 96 St).

## Déroulé (4 séances de 55 min)
| Séance | Activités | Verrou expérientiel |
|---|---|---|
| 1 La boîte étiquetée | 1. Simulateur de mémoire pas-à-pas · 2. Table de suivi | 6 étapes déroulées |
| 2 Les types | 3. Prédire → tester → reporter (piège des guillemets) | la console a montré les 3 résultats + reports exacts |
| 3 Le panneau bugué | 4. Chasse aux 3 bugs + preuve par la console | le programme affiche la bonne ligne, et la recalcule avec 95 °F |
| 4 Mise au point | 5. Algorithme → fonction → banc de 4 tests + cas limite → la fonction de l'élève testée par la page (7 appels) | banc de démonstration joué + la fonction de l'élève renvoie les 7 valeurs attendues |

## Versions (règle n°3)
🅱 éditeur Vittascience dans un nouvel onglet (parcours principal) · 🅲 simulateur + tables au cahier (hors ligne). La version 🅰 (éditeur → carte réelle) est retirée le
20/10/2026 : l'éditeur Python ne pilote aucune carte ; le TP mBot2 reste le prolongement sur robot réel, au collège.

## Évaluation
Formative : vérificateurs + QCM 30 q (VAR/TYP/PRG/MAP → positionnement par famille).
Depuis le 27/11/2026, six questions de chaque QCM se lisent sur un document dessiné pour le téléphone (n°345) : au
QCM de la séquence, « Le banc de la ventilation » (q26 à q28 : pourquoi un test T4, ce qu'il renvoie, la
non-régression) ; au QCM du TP, « Les quatre familles de valeurs » (q8 à q11) et « Six commandes du robot mBot2 »
(q29, q30 : reconnaître le capteur et l'actionneur dans les commandes). Regarder si l'élève relit le document avant de
répondre, ou répond de mémoire.
Sommative : à construire par l'enseignant, corrigé jamais publié dans le dépôt.

## Différenciation
DYS : listes déroulantes exclusivement, phrases courtes, aides à 2 niveaux. Rapides : défis bonus
(banc de tests AVANT les fonctions, cas limites MetroCard), TP mBot2.

## Dispositifs de classe (harmonisation du 26 août 2026)
**Billet d'entrée** (3 questions, corrigé immédiat, **hors progression** — il sert à savoir
d'où part la classe, pas à noter) · **mode essentiel** (masque référentiel, corrections et
compléments : il ne reste que les consignes) · **tableau de bord** des 5 activités, coché au
fur et à mesure · **deux versions étayées** pour les zones de rédaction · **durées annoncées**
(185 min d'activités pour 220 disponibles — la marge est voulue) · **sélecteur de parcours**
🅱/🅲 qui masque ce qui ne concerne pas l'élève **sans retirer aucune question**.

> Les barres 🧪 des éditeurs restent visibles dans les trois parcours : ce sont elles qui
> portent le verrou d'expérience des activités 3 et 4. En 🅲, une consigne dédiée dit quoi
> faire au cahier.

## Le TP « Programmer le robot mBot2 en Python » (refonte des 26 et 27/11/2026)

**Compétences officielles.** **3e_C9.2** — Réaliser et mettre au point un programme commandant un système réel
incluant une interaction entre un humain et une machine (le robot, sa manette et ses boutons). **3e_C9.1** — Élaborer
ou concevoir un algorithme […], le traduire en un programme structuré, le tester et le mettre au point.
**Socle : D1.3, D2, D4 · CRCN 3.4 Programmer (niveau 3).**

| Séance (55 min) | Ce que fait l'élève | Exercices |
|---|---|---|
| 1 — Les premiers ordres au robot | les six gestes de mBlock ; six programmes à remettre en ordre : écran, lumières, attente d'un geste, pause, moteurs, rotation | A1 à A6 (12 points) |
| 2 — Le robot qui évite les obstacles | le programme à dix trous (capteur de distance, `if / elif / else`), le robot simulé, les couleurs, les commandes | A7 (4 points), E1 à E8 (19 points) |
| 3 — Les boucles | vingt petits programmes à une ligne manquante (`for`, `while`, `range`, `break`…) : l'élève écrit la ligne, la page exécute le programme et montre ce qu'il affiche ; puis le bilan | B1 à B20 (20 points) |

**Versions (règle n°3).** 🅰 robot réel : chaque programme juste se téléverse avec mBlock (très basse tension, robot au
sol). 🅱 robot simulé : le bouton « ▶ Essayer sur le robot simulé » exécute le programme construit, et la console
raconte ce que ferait le robot ; un bac à sable accepte tout programme. 🅲 sans matériel : les exercices E et B, et le
robot simulé, se font sur téléphone, à la maison (20 min par semaine au plus).

**Vers le vrai robot : mBlock, ou Vittascience (27/11/2026).** Sous chaque activité, « 🚀 Envoyer ton programme au
vrai robot » ouvre l'éditeur de la page sur le programme de l'élève (il peut le modifier, l'essayer, le télécharger),
le copie, et mène à l'interface mBot2 de Vittascience (https://fr.vittascience.com/cyberpi/, il faut Internet).
L'échauffement donne les deux chemins : les six gestes de mBlock, et cinq gestes pour Vittascience. Le Bonus a son
éditeur. **À faire avant la première séance :** un essai de Vittascience avec un vrai mBot2 (mode Python, collage,
téléversement) ; ensuite, les gestes se mettent en captures.

**Ce que le robot simulé suppose, et dit à l'élève :** il compte le temps sans l'attendre ; un tour de roue = 20 cm
(valeur arrondie) ; un obstacle à 60 cm ; la touche demandée est pressée au troisième regard ; l'essai s'arrête après
30 s comptées ou trois virages. Il ne remplace pas l'essai sur le robot.

**Comment B1 à B20 sont vérifiés.** La ligne du corrigé est reconnue aux espaces et aux guillemets près. Toute autre
ligne est jugée en exécutant le programme : elle est juste si le programme fait le même travail (`while d > 14:` pour
`while d >= 15:`, `s = i + s`, `while 1:`…). Sinon, l'élève voit côte à côte ce que son programme affiche et ce qu'il
doit afficher. Pour B1, B8, B12 et B15, la page fait un second essai en changeant un nombre du programme : une ligne
qui ne convient qu'aux nombres montrés (`s = 10`) est refusée. B9 et B16 se jouent sur le robot simulé, bouton par
bouton. Si le moteur Python ne se charge pas, la page le dit et ne compte pas l'essai.

**Points.** 55 points, ramenés sur 20. Réussi sans ouvrir la correction : tous les points jusqu'au 3e essai, la moitié
ensuite (question à choix : tout, la moitié, puis rien). Correction ouverte avant la réussite : 0 point. Le suivi sépare
« réussis », « à reprendre » (avec leurs numéros) et « pas encore faits ». La fiche imprimée (2 pages) se rend en PDF.

**À vérifier sur vos robots avant la première séance** (non vérifiable sans mBot2) : le mot-clé `run_time` de
`forward` et `backward` en mode Téléverser (c'est l'écriture du manuel Python du mBot2 de Makeblock, relu le 27/11/2026 ;
l'aide en ligne de Makeblock et la bibliothèque du mode En direct écrivent `t` — si un robot refuse `run_time`, écrire
les deux nombres sans mot-clé, `forward(50, 1)`, convient aux deux), et les libellés exacts des boutons de votre version de mBlock dans l'encart des six gestes.
