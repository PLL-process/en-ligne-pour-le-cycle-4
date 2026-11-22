---
name: cadrage-cles-de-voute
description: Cadrer une séquence du dépôt en-ligne-pour-le-cycle-4 avant de l'écrire, puis l'auditer avant de la valider, avec les sept clés de voûte (n°306, 87/311, 337, 343, 346, 347, 348), une checklist de seize questions à réponse vérifiable et une grille sur 100 points où un zéro aux critères 1 ou 2 bloque. À utiliser au début de tout lot, à chaque révision, et pour noter une page après un audit externe.
---

# Cadrer, puis auditer, avec sept clés de voûte

Décision de Pascal du 21/11/2026, sur l'audit de l'entraînement DNB de `3e_C6.2` : 360 règles ne se lisent plus ; sept
principes cadrent une séquence, et les autres règles se rangent sous eux. Grille reprise en tête de `_outils/METHODE.md`.

## 1. Au début du lot : cadrer (dix minutes)

Écrire, avant toute page, une ligne par clé de voûte :

1. **Squelette (n°306)** : combien de séances de 55 min, où vont Bonus, Bilan, QCM.
2. **Rappel (n°87, n°311)** : quels prérequis, quel exemple guidé, quel cas neuf. Pascal change de collège chaque année :
   aucun élève n'a fait sa séquence précédente (n°304).
3. **Trois lignes (n°337)** : ce que l'élève apprend, sait faire, et le seuil chiffré de réussite.
4. **Question seule (n°343)** : quels nombres et quel état de départ chaque question devra donner (n°350).
5. **Preuve écrite (n°346)** : le document inédit et ses quatre questions rédigées (skill `tache-finale-redigee`).
6. **Retour (n°347)** : comment l'élève saura quoi reprendre après « Vérifier ».
7. **Langue du cours (n°348)** : la planche de référence des formes, des mots et des nombres.

Ajouter le critère de recette demandé par Pascal (« avec 6 justes et 2 blancs, la page affiche… »). Sans critère, on
ne sait pas quand c'est fini.

## 2. Avant de valider : seize questions

Chacune se répond par un nombre ou un oui/non constaté.

1. Où l'élève rédige-t-il une réponse, sans propositions, sur un document jamais vu ?
2. Combien d'activités `eleve_qui_ne_lit_pas.py` valide-t-il ? (attendu : 0, skill `eleve-qui-ne-lit-pas`)
3. Avec des cases vides, la tâche « répondre à tous » reste-t-elle non cochée ?
4. Après une erreur, le message cite-t-il le numéro sans la bonne réponse ?
5. Chaque symbole des documents a-t-il la forme de la planche du rappel ?
6. Un document d'exercice, ou sa description, contient-il la réponse ?
7. Chaque énoncé donne-t-il état de départ, unité, type de nombre, capteur ?
8. Chaque seuil est-il joué sous la valeur, à la valeur et au-dessus (n°351) ?
9. Fiche, trois lignes et code portent-ils les mêmes seuils (`controle_memes_nombres.py`) ?
10. À partir de la séance 2, le rappel est-il replié, avec exemple guidé et cas neuf ?
11. La page s'ouvre-t-elle seule, dans un dossier vide, réseau coupé, sans erreur ?
12. À 390 px : défilement horizontal ? texte des schémas d'au moins 13 px à l'écran ?
13. Combien de pages A4 pour la partie ouverte ? un schéma séparé de sa question ?
14. Chaque lien de l'accès rapide ouvre-t-il l'onglet qu'il nomme (n°359) ?
15. Le rapport de tests écrit-il ce qui n'a pas été vérifié ?
16. Chaque chiffre du journal, de la fiche et du rapport a-t-il été recalculé ?

## 3. Noter sur 100

Paliers seulement — zéro, la moitié ou le plein — pour ne pas inventer une précision. **Un zéro aux critères 1 ou 2
bloque la séquence**, quel que soit le total.

| Critère | Points | Plein si… | Zéro si… |
|---|---|---|---|
| 1. Preuve de compétence | 15 | réponse rédigée sur document inédit, avec grille | tout se coche |
| 2. Questions qui ne soufflent pas | 15 | n°360 à 0, places réparties, documents sans réponse | la plus longue ou une place fixe valide |
| 3. Retour qui dit quoi reprendre | 12 | numéros à revoir, indice avant corrigé, corrections exhaustives | un score seul |
| 4. Cohérence cours, document, énoncé | 12 | mêmes formes, mots, nombres ; aucune hypothèse tue | un document contredit le rappel |
| 5. Rappel et progression | 10 | prérequis rappelés, exemple guidé, cas neuf, transfert | rien n'est rappelé |
| 6. Lisibilité au téléphone | 10 | 390 px sans défilement, schémas lisibles, mots par manche comptés | illisible au téléphone |
| 7. Accessibilité | 8 | axe-core sans défaut, contour ≥ 3:1, mode allégé complet (n°29) | le clavier est bloqué |
| 8. Usage de classe | 8 | 55 min tenues, impression courte, hors ligne, sauvegarde qui avertit | dépend du réseau |
| 9. Vérification déclarée | 5 | bancs rejouables, revue d'écran, non-vérifié écrit | aucun test rejouable |
| 10. Preuve en classe | 5 | durée mesurée, trois copies comparées | aucun passage en classe |

Lecture : 85 et plus, publiable ; 70 à 84, publiable avec la liste des corrections ; 50 à 69, à reprendre avant la
classe ; moins de 50, à refaire. Étalonnage (21/11/2026) : l'ancienne page de l'entraînement DNB était bloquée (zéro
aux critères 1 et 2) ; la nouvelle obtient environ 86, faute de mesure en classe.

## 4. Les anti-patterns à reconnaître

La bonne réponse « bien expliquée » (plus longue) · le schéma généreusement annoté · le rappel qui donne une partie
pour le tout · le score global flatteur · le bandeau tout coché · ajouter des questions avant de corriger · vingt
contrôles verts sans regarder · mélanger les réponses au hasard · la durée écrite au jugé · le mode allégé qui retire
les corrections · imprimer toute la page · « le brevet se joue dans les distracteurs » · la règle d'or du soir sans
contrôle · le « premium » sans critère.
