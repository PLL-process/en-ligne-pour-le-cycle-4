# Rapport de tests — lot Shenzhen 5e_C2.1 · C2.2

**Date** 8 août 2026 · **Suite** `tests_5e_C2.1-C2.2_shenzhen.py` (Playwright, Chromium 1280×900)
**Résultat** **45 / 45 tests passés** (v1.1)


> **Correction du 31/08/2026 — la suite de ce lot était rouge, et c'est le test qui avait tort.**
> Réexécutée ce jour-là (personne ne l'avait relancée depuis sa livraison), elle échouait sur
> « séquence : hors ligne, aucune ressource distante (n°40) ». La cause n'était pas dans la
> page : le contrôle cherchait la chaîne `http://` dans le HTML sérialisé, où **chaque SVG en
> ligne porte son `xmlns="http://www.w3.org/2000/svg"** — un identifiant d'espace de noms, que
> nul navigateur ne va chercher. Le contrôle regarde désormais ce que la page **irait charger**
> (`src`, `link href`, `object data`, `iframe`, `use`), sans les hyperliens, qui ont le droit
> d'être distants. Vérifié dans les deux sens : la suite passe, et elle redevient rouge si l'on
> injecte une vraie ressource distante dans la page.
>
> ```
> 47 / 47 tests passés
> ```
Ce rapport ne mentionne que des tests **réellement exécutés**. La suite est livrée avec le lot :
elle se relance depuis le dossier du lot par `python3 tests_5e_C2.1-C2.2_shenzhen.py`.

## La séquence (27 tests)

| Ce qui a été vérifié | Résultat |
|---|---|
| Aucune erreur JavaScript au chargement ni pendant le parcours | ✔ |
| Hors ligne intégral : aucune ressource distante (n°40) | ✔ |
| Lien d'accueil résolu sur le fichier réel (n°11) | ✔ |
| Bandeau de tâches affiché et mis à jour par séance (n°30) | ✔ |
| 7 zones de rédaction, 7 versions étayées (n°31) | ✔ |
| Chaque champ porte une étiquette ou un `aria-label` (n°34) | ✔ |
| Les deux figures sont chargées, avec une alternative longue (n°1) | ✔ |
| Le compteur annonce 3 activités et en compte 3 (n°39) | ✔ |
| Billet d'entrée : oriente sans note, ne compte pas dans la progression (n°26) | ✔ |
| Activité 1 : une liste de six **personnes** est refusée | ✔ |
| Activité 1 : validée seulement quand les quatre familles sont nommées | ✔ |
| Activité 2 : le relevé de quatre choix est exigé avant validation | ✔ |
| Activité 2 : un relevé **sans développement durable** est refusé | ✔ |
| Activité 3 : le transfert martiniquais (trois interacteurs) est exigé | ✔ |
| Mode essentiel : bascule et `aria-pressed` cohérent (n°29) | ✔ |
| L'hypothèse de départ est rappelée au bilan | ✔ |
| Sauvegarde locale restaurée après rechargement (textes et progression) | ✔ |
| Blocs « Prêt·e à t'entraîner » et « Bonus » présents, **un seul** bouton QCM (n°4) | ✔ |

Les trois verrous de production ont été testés **dans les deux sens** : refus quand la production
manque ou reste incomplète, validation quand elle est là. C'est le point qui distingue une activité
d'un questionnaire déguisé.

## Le QCM (12 tests)

| Ce qui a été vérifié | Résultat |
|---|---|
| Aucune erreur JavaScript | ✔ |
| 30 questions, 15 par code | ✔ |
| Les trois domaines du code sont ceux du référentiel : ergonomie, sécurité, **développement durable** | ✔ |
| Bonnes réponses réparties A/B/C/D = **8 / 7 / 7 / 8** (graine 502) | ✔ |
| 4 questions illustrées | ✔ |
| Aucune réfutation de distracteur de 20 caractères ou moins ; `d[r]` vide partout | ✔ |
| Chaque question porte explication, exemple, erreur classique et à-retenir | ✔ |
| Parcours complet des 30 questions : les 30 bonnes réponses sont acceptées | ✔ |
| Bilan par compétence affiché avec les deux codes | ✔ |
| Sauvegarde restaurée après rechargement (30 questions validées) | ✔ |
| Une mauvaise réponse affiche la réfutation **du distracteur choisi** | ✔ |

La répartition des bonnes réponses n'a pas été jugée à la lecture, elle a été **comptée** : c'est le
seul moyen de la voir. Le contrôle de longueur des réfutations relève du même principe — trois lots
de suite, des réfutations trop courtes s'étaient glissées là où l'auteur trouvait la réponse fausse
évidente, c'est-à-dire précisément là où l'élève a besoin d'une explication.

## Les synthèses (6 tests)

Élève et professeur : aucune erreur JavaScript, figures référencées au bon nombre, et **tous les
liens de navigation résolus sur des fichiers existants**.

## Ce que ces tests n'auraient pas attrapé

La v1.0 de ce lot enseignait « ergonomie, sécurité, **esthétique** » là où le référentiel dit
« ergonomie et sécurité, ou en lien avec des objectifs de **développement durable** ». Les 43 tests
passaient tous. Aucun ne comparait le contenu enseigné au **texte du référentiel** — ils
vérifiaient la mécanique, la cohérence interne et l'accessibilité, c'est-à-dire tout sauf la seule
chose qui était fausse.

Un test a été ajouté en v1.1 : il lit la bonne réponse de la question « Trois domaines » du QCM et
la compare à la formulation attendue. C'est peu, mais c'est le premier test de ce dépôt qui
contrôle un **contenu institutionnel** plutôt qu'un comportement.

## Ce qui n'a pas été testé

- L'impression A4 (rendu papier) : les feuilles `@media print` sont reprises du gabarit maison, mais
  aucune sortie papier n'a été produite ni relue.
- Le comportement sur un vrai lecteur d'écran : les `aria-label`, `title`/`desc` SVG et le
  signalement non chromatique sont en place et vérifiés dans le DOM, mais aucun test avec NVDA ou
  VoiceOver n'a été mené.
- La séquence sur mobile réel : seule la fenêtre 1280×900 a été utilisée.
