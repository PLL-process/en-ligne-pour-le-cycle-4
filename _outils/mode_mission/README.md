# Mode mission — un exercice à la fois

Décision de Pascal du 11/11/2026 (voir `docs/mode-mission/PLAN.md` et le journal).

Le mode mission est une **seconde vue de la même page**. Il n'invente aucun exercice : il montre ceux de la
séquence, un écran à la fois, avec une barre d'étapes et trois boutons — Précédent · Vérifier · Suivant.

## Ce que le bloc fait

- **Découpe** chaque séance en écrans : la séance (et la situation de départ) ; pour chaque activité l'atelier
  incrusté, le départ (objectif, ressources, consigne), puis **une question par écran**, puis « je retiens »
  (correction, erreurs fréquentes, à retenir, critère) ; enfin chaque autre carte (synthèse, Bonus, bilan, QCM).
- **Habille** une grille de boutons radio (`.qcm-cles` + `fieldset.qcm-grille`) en **étiquettes à poser** : on
  touche l'étiquette puis sa case, on la glisse, ou on fait les deux au clavier. Poser une étiquette coche le
  bouton radio de la page : la sauvegarde, la vérification et l'impression de la page ne voient aucune différence.
- **Vérifie** chaque écran avec les réponses que la page porte déjà (`const att = {…}` dans ses vérifications) :
  les réponses justes restent, les étiquettes fausses retournent dans la réserve. La dernière question d'une
  activité lance la vérification de la page : c'est elle qui valide l'activité (verrous, justification écrite,
  atelier réussi).
- **Décourage le tâtonnement** : les erreurs se comptent réponse par réponse et font les étoiles (3 sans erreur ;
  2 avec une erreur, deux sur un jeu de trois réponses ou plus ; 1 au-delà) ; après une erreur, « Vérifier » souffle
  deux secondes ; au deuxième essai manqué sur le même écran, le coup de pouce de l'activité (`details.aide1`,
  ou le premier `details.aide`) s'ouvre sous le message, au quatrième le second. Ouvrir une aide ne retire rien.
- **Garde** sur l'appareil le mode, l'écran en cours, les erreurs et les étoiles (`localStorage`, clé
  `mission:<page>`) ; « Effacer ma sauvegarde » les efface aussi. La barre affiche les étoiles de la séance, le
  bilan celles de la séquence et les erreurs corrigées en route.

## Ce qu'il ne fait pas

- Rien tant que l'élève n'a pas appuyé sur « 🎮 Mode mission » (dans le cadre « Ma progression ») : la page s'ouvre
  comme avant, et son contenu n'est pas touché. « 📄 Page complète », dans la barre de la mission, y ramène.
  Les contrôles et les bancs du dépôt mesurent et jouent donc la page qui défile.
- Rien à l'impression : tout ce qui cache est sous `@media screen`. La fiche papier sort entière.
- Il ne bloque jamais « Suivant », ne chronomètre rien, ne classe personne.

## Fichiers

| Fichier | Rôle |
|---|---|
| `mission.css`, `mission.js` | la source unique |
| `poser.py` | pose ou met à jour le bloc dans une page (`--verifier` : ne rien écrire) |
| `banc_mission.mjs` | joue le pilote comme un élève, à 390 px et à 1 180 px (22 tests par largeur) |
| `../controle_mode_mission.py` | le bloc d'une page est celui de la source, une fois |

## Poser le mode mission sur une séquence

```bash
python3 _outils/mode_mission/poser.py <sequence.html>
node _outils/mode_mission/banc_mission.mjs          # le pilote
python3 _outils/controle_mode_mission.py
```

Avant de le poser ailleurs que sur le pilote : ouvrir la page en mode mission et parcourir chaque séance. Le
découpage suit le gabarit commun (`.seance-panel > section.card > .activite > .exo`, parties en `h4`) ; une page
d'un autre gabarit reste telle quelle (le bouton n'apparaît pas). Sans table `const att`, les écrans ne se
vérifient pas un à un : seule la vérification de la page joue, à la dernière question de l'activité.

## Limites connues (pilote)

- Les séries de numéros à ordonner et les textes à trous ne sont pas encore habillés (ils restent des boutons radio).
- Un lien vers une ancre (`#act3`) ouvre la bonne séance, pas le bon écran.
- Non essayé sur une vraie tablette : le glisser au doigt n'a été joué qu'en simulation. Au doigt, une étiquette
  se glisse depuis la réserve ; une case ne se glisse pas (la page défile) : on la touche pour reprendre l'étiquette.
- Pas d'étiquettes leurres ni de « pourquoi » par mauvaise réponse : c'est du contenu, à écrire séquence par
  séquence (voir `docs/mode-mission/PLAN.md`, « Ce que dit la recherche »).
