# Fiche papier — impression des séquences

**Demande de Pascal, 25/10/2026** : « imprimer en PDF : les consignes ne sont pas vues parce que la police et sa
couleur est trop claire. Cela fait beaucoup de pages » ; « rendre ces impressions en PDF ultra premium et moins
longues ». Prototype sur le jardin (4e_C8.1 : 16 pages → 7), jugé par Pascal : « la qualité d'impression que tu donnes
là est super, bravo ». Décisions : **1a** la fiche papier sur les 60 séquences, avec un contrôle qui refuse un texte trop
pâle sur le papier ; **2a** on imprime la fiche élève (ce qui ne sert qu'à l'écran disparaît) ; séquences à onglets :
**1a** on imprime **la séance affichée**. Branche transversale `fable/impression-papier`.


## Ce que fait la fiche papier

Rien ne change à l'écran (captures pleine page des 60 séquences, `main` contre la branche : identiques, aux tirages au
hasard près). À l'impression :

- **un en-tête** : « Technologie · niveau · code · séance (rang / nombre) », le titre, Nom / Prénom / Classe / Date ; au
  pied de chaque page, le titre et « page n / N » ;
- **l'encre foncée** : la palette du dépôt redéfinie pour le papier (aussi dans les ateliers incrustés, qui la
  redéfinissent sur eux-mêmes) ; les couleurs claires écrites dans la page (`style="color:…"`) reconnues au chargement et
  rendues dans la même teinte, foncée (`.pp-encre`) ; les grands fonds foncés changés en cadre blanc (`.pp-fond`) ;
- **le crayon** : un menu devient des cases à cocher, un champ de texte des lignes d'écriture (autant que de lignes à
  l'écran, plus une), un champ court un trait, une case ou un bouton radio un carré ou un rond ; les réponses d'une
  question s'alignent sur une ligne ; un simulateur devient un encadré « cette partie se fait sur la page en ligne » avec
  un tableau pour noter ce qu'on observe ;
- **ce qui ne sert qu'à l'écran disparaît** : barre d'outils, menus de navigation, boutons, scores, compteurs, billet
  d'entrée, « où j'en suis », référentiel, ce qui est replié (`details` fermé), un bloc qui ne porte que des boutons ;
  un bloc marqué `pp-ecran` par la page elle-même ;
- **une séance** : dans une séquence à onglets, la séance affichée, et elle seule ; l'ouverture s'imprime avec la
  première, la clôture avec la dernière ; la séance suit l'en-tête sur la même feuille ;
- les animations pas à pas : l'image et la liste des étapes, côte à côte.

Fichiers : `papier.css`, `papier.js` (la source), `poser.py` (la pose, avant `</head>`, ou avant `</body>` dans une page
qui omet `</head>`), `banc_papier.py` (le banc au navigateur). Contrôles : `_outils/controle_impression_papier.py` (le
bloc est là, une fois, à jour) et `_outils/controle_impression.mjs` (sur une page qui porte la fiche, un texte sous
4,5 : 1 est refusé). Le générateur des quatre pages de la station (3e_C9.2) pose la fiche par `poser.py`.

Pour une nouvelle séquence : `python3 _outils/impression_papier/poser.py <page>`, puis
`python3 _outils/impression_papier/banc_papier.py --filtre <dossier du lot> --pdf <dossier>`, et regarder les PDF.
Après une retouche de `papier.css` ou `papier.js` : reposer sur toutes les séquences (la liste :
`find . -name "sequence*.html" -not -path "*/_archive-anciennes-versions/*"`) et relancer le générateur de 3e_C9.2.

## Plan et avancement

- [x] 0. Branche et plan (ce fichier).
- [x] 1. Relevé de la structure des 60 séquences : 37 à onglets de séances (`role=tabpanel`), 23 sans (thème 3 surtout,
      et les quatre pages de la station 3e_C9.2) ; ce qui ne sert qu'à l'écran, reconnu à sa classe ou à son titre.
- [x] 2. Source unique : `papier.css`, `papier.js`, `poser.py` ; contrôle `_outils/controle_impression_papier.py` + tests.
- [x] 3. Pose sur les 60 séquences ; le générateur `3e_C9.2/generer_les_quatre_pages.py` pose la fiche.
- [x] 4. `controle_impression.mjs` : sur une page qui porte la fiche papier, un texte sous 4,5 : 1 sur fond clair est refusé.
- [x] 5. Banc au navigateur : pages avant / après, aucun champ d'écran imprimé, aucun texte pâle, aucun grand fond foncé,
      première page remplie, aucune erreur JavaScript, écran inchangé (captures comparées), planches des 128 fiches regardées.
- [x] 6. Journal, nouveautés, skills, audit et index, contrôles du dépôt contre `main`, PR.

Reste ouvert : « Mode essentiel : ON » par défaut (décision 3, non tranchée).
