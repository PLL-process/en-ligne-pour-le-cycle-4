---
name: reprise-espacee
description: Poser en tête de chaque séance, à partir de la deuxième, une « 🔁 Reprise » de deux ou trois questions que l'élève résout DE MÉMOIRE sur les acquis 🔑 des séances précédentes, avant tout rappel déplié ; faire dire au bilan ce qui reste flou et quand on le reprend ; proposer au QCM un « 🔀 Entraînement mélangé ». Règles d'or n°369 (clé de voûte), n°371 et n°372, en essai. À utiliser en écrivant ou en révisant une séquence de plus d'une séance, et en posant les aides d'un QCM.
---

# Ce qui compte revient

Décision de Pascal du 22/11/2026 (« ils seront à installer automatiquement ensuite »), sur la veille de l'audit du
même jour (PR #867). Règles **en essai** (n°147) : elles s'adoptent après mesure sur l'ensemble.

## Pourquoi

Le volet « 📖 Rappel » (n°311) **réexplique**. Réexpliquer donne à l'élève l'impression de savoir (on reconnaît ce
qu'on relit) ; **retrouver de mémoire**, quelques jours plus tard, fait tenir l'acquis. C'est l'un des résultats les
plus solides de la recherche sur l'apprentissage : l'effet de test (Roediger et Karpicke, 2006), l'espacement
(Cepeda et al., 2006), et leur méta-analyse en classe (Adesope et al., 2017). On distingue la **force de restitution**
(je retrouve tout de suite après la leçon) de la **force de stockage** (je retrouve trois semaines après) : seule la
seconde compte, et c'est la difficulté de retrouver qui la construit (Bjork).

Mesure de départ (22/11/2026) : sur 113 séances n°2 et suivantes, 8 au plus s'ouvrent sur une question de mémoire.

Ce n'est pas contraire à la n°304 : Pascal change de collège chaque année, la reprise se fait **dans l'année**, entre
les séances d'une séquence et entre séquences d'un même niveau.

## 1. La reprise en tête de séance (n°369)

Dans chaque panneau de séance `id="s2"`, `id="s3"`…, **avant** le volet « 📖 Rappel » :

```html
<section class="card reprise" data-reprise>
  <h3>🔁 Reprise : sans regarder, retrouve</h3>
  <p class="consigne">1. Réponds de mémoire, sans ouvrir le rappel.<br>2. Vérifie.<br>3. Si tu t'es trompé·e, ouvre le rappel juste en dessous.</p>
  <fieldset>…question 1…</fieldset>
  <fieldset>…question 2…</fieldset>
</section>
```

- **Deux ou trois questions**, pas plus : la reprise dure trois à cinq minutes, **comptées** dans les 55 minutes
  (n°23 — l'audit du 22/11 a vu trois séquences dépasser après des ajouts non comptés).
- Elles portent sur les acquis **🔑 (n°353)** d'une séance **précédente**, pas sur celle du jour. Une sur la séance
  d'avant, une sur une séance plus ancienne quand il y en a une (c'est l'espacement).
- **Une question qui se lit seule** (n°343) : objet, nombres, état de départ sous les yeux. Pas de « comme en S1 ».
- **On prédit avant les propositions** (n°349) quand c'est possible : une réponse courte à écrire, puis les
  propositions. Sinon, des boutons radio (n°300), bonnes réponses à des places mélangées (n°323), sans indice de
  longueur (n°341).
- La correction d'une erreur **renvoie au rappel** : « Ouvre le 📖 Rappel juste en dessous : la ligne 2 dit … ».
  Le rappel reste (n°311) : il vient après, pour ceux qui n'ont pas retrouvé.
- Dans la page, la reprise **ne valide pas** l'activité : elle se coche « faite », pas « réussie » (n°340).
- Les mots de la fabrique ne vont pas sur la page (n°309) : jamais « récupération », « effet de test » ; on écrit
  le geste : « sans regarder, retrouve ».

## 2. La maîtrise se confirme plus tard

Un acquis 🔑 réussi le jour même n'est pas « maîtrisé » : il l'est quand la reprise d'une séance suivante le
retrouve. Au bilan et au positionnement, « ✔ réussi aujourd'hui » et « ✔ retrouvé plus tard » se distinguent quand la
page sait les deux (sauvegarde locale, n°322).

## 3. Le bilan dit ce qui reste flou et quand on le reprend (n°372)

Dans le bilan (n°301), un champ `data-flou` :

```html
<label for="flou">Ce qui reste flou pour moi, et quand je le reprends (la séance, ou le QCM) :</label>
<textarea id="flou" data-flou></textarea>
```

Une phrase-modèle aide : « Je ne sais pas encore … ; je le reprends à la séance … / dans le QCM, mode « Mes erreurs » ».

## 4. Le QCM entrelace (n°371)

Mesure de départ (22/11/2026) : **69 QCM sur 70** posent leurs questions **par blocs de compétence**. Mélanger des
compétences voisines aide à les **distinguer** (Rohrer et Taylor, 2007 ; Brunmair et Richter, 2019 : effet net quand
les notions se ressemblent — chaîne d'énergie et d'information, formes d'énergie ; plus faible ailleurs).

- On **garde** le parcours complet tel qu'il est (son ordre est parfois voulu).
- On **ajoute** un bouton `data-mode="melange"` « 🔀 Entraînement mélangé » dont la liste est l'ordre de
  `python3 _outils/mesurer_entrelacement.py --ordre <qcm.html>` : un tour par compétence, **déterministe**, sans
  hasard (même ordre pour deux voisins et pour l'enseignant).
- À poser dans le moteur du gabarit (`setMode`), comme les autres modes ; le banc du QCM le joue.

## 5. Mesurer

```bash
python3 _outils/controle_reprise_espacee.py            # n°369, n°372 : séances sans reprise, bilans sans « flou »
python3 _outils/controle_reprise_espacee.py --strict   # refuse (pour une séquence révisée)
python3 _outils/mesurer_entrelacement.py               # n°371 : banques par blocs, modes mélangés présents
python3 _outils/tests_controle_reprise_espacee.py      # le banc des deux outils
```

Ce que les outils ne voient pas : que la reprise porte sur une séance **précédente** et sur un acquis **qui
compte**. Relire chaque reprise avec la liste des 🔑 de la séquence.

## Pilote proposé

Une séquence de trois séances au moins, qui passe bientôt en classe, et dont les acquis 🔑 sont déjà marqués (n°353 :
six pages en portent au 22/11). Poser la reprise des séances 2 et 3, le champ `data-flou`, rejouer
`controle_reprise_espacee.py --strict` sur la page, le banc de la séquence, la revue d'écran à 390 px. Puis
généraliser par vagues, comme les trois lignes « Avant de commencer » (n°337).
