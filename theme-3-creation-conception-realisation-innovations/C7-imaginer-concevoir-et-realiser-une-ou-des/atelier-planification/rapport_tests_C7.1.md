# Rapport de contrôles — Atelier de planification des tâches (C7.1)

Ce rapport ne liste **que des contrôles réellement exécutés** (règle d'or n°43). Chaque ligne
correspond à une assertion qui est passée. La commande, reproductible :

```
python3 tests_atelier_C7.1.py
python3 _verifier_planning.py
node _outils/fix_r.js qcm_C7.1_planification_taches.html 617
```

## 1. Les trois pages de l'atelier (5e, 4e, 3e) — 48 contrôles Playwright

Le banc boucle sur les trois pages. Les onglets attendus sont déclarés page par page (5e : p5, gp, pm ; 4e : p4, gp, pm ; 3e : p3, gp, pm) : un onglet disparu ou en trop fait échouer le banc. Les contrôles propres à un niveau (dates au plus tôt en 4e, chemin le plus long en 3e) ne tournent que sur sa page.

```
── page 5e
  ✔ les cinq captures sont référencées ET présentes sur le disque
  ✔ chaque image porte une alternative textuelle qui la DÉCRIT (règle n°1)
  ✔ un seul bouton QCM dans toute la page (règle n°4)
  ✔ la barre de navigation pointe aussi vers le QCM (un lien, hors bouton)
  ✔ le bloc Bonus est présent, annoncé hors parcours obligatoire
  ✔ l'ordre bilan → entraînement → bonus ferme la page (règle n°4)
  ✔ aucune mention du secteur : l'activité est en papier et en logiciel
  ✔ aucun appel réseau : la page fonctionne hors ligne (règle n°40)
  ✔ aucune erreur JavaScript au chargement
  ✔ 5e : les onglets p5, gp, pm sont les seuls présents et s'ouvrent
  ✔ le verrou expérientiel tient : sans les bandes découpées, rien n'est validé
  ✔ une fois les bandes déclarées faites, l'activité 1 se valide
  ✔ les réponses et les validations reviennent après rechargement
  ✔ le mode essentiel masque bien le référentiel et les corrections
  ✔ à l'impression, aucun panneau n'est caché
── page 4e
  ✔ les cinq captures sont référencées ET présentes sur le disque
  ✔ chaque image porte une alternative textuelle qui la DÉCRIT (règle n°1)
  ✔ un seul bouton QCM dans toute la page (règle n°4)
  ✔ la barre de navigation pointe aussi vers le QCM (un lien, hors bouton)
  ✔ le bloc Bonus est présent, annoncé hors parcours obligatoire
  ✔ l'ordre bilan → entraînement → bonus ferme la page (règle n°4)
  ✔ aucune mention du secteur : l'activité est en papier et en logiciel
  ✔ aucun appel réseau : la page fonctionne hors ligne (règle n°40)
  ✔ aucune erreur JavaScript au chargement
  ✔ 4e : les onglets p4, gp, pm sont les seuls présents et s'ouvrent
  ✔ le verrou expérientiel tient : sans les bandes découpées, rien n'est validé
  ✔ une fois les bandes déclarées faites, l'activité 1 se valide
  ✔ les dates au plus tôt du corrigé calculé sont bien celles que la page accepte
  ✔ une date fausse est refusée — le vérificateur vérifie vraiment
  ✔ les réponses et les validations reviennent après rechargement
  ✔ le mode essentiel masque bien le référentiel et les corrections
  ✔ à l'impression, aucun panneau n'est caché
── page 3e
  ✔ les cinq captures sont référencées ET présentes sur le disque
  ✔ chaque image porte une alternative textuelle qui la DÉCRIT (règle n°1)
  ✔ un seul bouton QCM dans toute la page (règle n°4)
  ✔ la barre de navigation pointe aussi vers le QCM (un lien, hors bouton)
  ✔ le bloc Bonus est présent, annoncé hors parcours obligatoire
  ✔ l'ordre bilan → entraînement → bonus ferme la page (règle n°4)
  ✔ aucune mention du secteur : l'activité est en papier et en logiciel
  ✔ aucun appel réseau : la page fonctionne hors ligne (règle n°40)
  ✔ aucune erreur JavaScript au chargement
  ✔ 3e : les onglets p3, gp, pm sont les seuls présents et s'ouvrent
  ✔ le verrou expérientiel tient : sans les bandes découpées, rien n'est validé
  ✔ une fois les bandes déclarées faites, l'activité 1 se valide
  ✔ le chemin le plus long offert en réponse est exactement celui du calcul
  ✔ les réponses et les validations reviennent après rechargement
  ✔ le mode essentiel masque bien le référentiel et les corrections
  ✔ à l'impression, aucun panneau n'est caché

48 contrôles exécutés, 48 réussis.
```

## 2. Le calcul des plannings

`_verifier_planning.py` recalcule les trois projets à partir du seul CSV, vérifie à chaque
exécution l'invariant **« le chemin le plus long est exactement l'ensemble des tâches de marge
nulle »**, n'écrit le corrigé que si les trois projets passent, puis **relit le fichier écrit** et
contrôle qu'il redonne bien marge nulle exactement sur le chemin. Sortie de la dernière exécution :
les trois projets sont cohérents.

## 3. Le QCM

Contrôles exécutés :

- les cinq images référencées dans `img:{src:…}` existent sur le disque ;
- aucune erreur JavaScript au chargement ;
- 30 questions chargées, réparties 10 / 10 / 10 sur les trois niveaux ;
- bonnes réponses réparties **8 / 7 / 7 / 8** sur A / B / C / D (graine 617) ;
- `d[r]` vide pour les 30 questions : aucune « réfutation » de la bonne réponse ;
- une question illustrée affiche bien son image (`naturalWidth > 0`) ;
- le générateur refuse d'écrire s'il reste une trace du gabarit d'origine (règle n°51) : titre
  affiché, sous-titre, badges et libellés de compétences sont contrôlés motif par motif.

## 4. Les liens depuis les trois séquences C7.1

Les trois chemins relatifs insérés dans `5e_C7.1`, `4e_C7.1` et `3e_C7.1` ont été **résolus sur le
disque**, pas seulement écrits. Chaque séquence conserve un unique bouton de QCM.

## Ce qui n'a PAS été testé

- Le rendu sur un vrai poste du collège (résolution, navigateur installé, version de GanttProject
  différente). Les captures ont été prises sur un poste Windows en GanttProject 3.3 ; une autre
  version peut déplacer un bouton — c'est écrit dans `SOURCES_MEDIAS.md`, et l'atelier ne fait
  jamais dépendre une consigne d'une couleur.
- Le comportement avec un lecteur d'écran réel. Les attributs `aria` et les alternatives textuelles
  sont présents et contrôlés automatiquement, mais aucune écoute n'a été faite.
- L'usage en classe. L'atelier n'a pas encore été mené devant des élèves.

## 5. Les douze règles mécanisées — appliquées à la main ici

`_outils/verif_regles_audit.py` n'analyse que les fichiers nommés `sequence_*.html`. Cette
ressource s'appelle `atelier_*.html` : **elle échappe donc au contrôle automatique**, et c'est une
dette à corriger côté outillage (le fichier vit dans le périmètre du Thème 2, il ne peut pas être
modifié depuis une branche de Thème 3).

Les contrôles ont donc été rejoués à la main sur la page, et voici ce qu'ils donnent :

| Règle | Résultat |
|---|---|
| n°23 durée annoncée | ✔ « 1 séance de 55 min », et un temps par étape |
| n°29 mode essentiel | ✔ bouton présent, masque référentiel et corrections (vérifié par Playwright) |
| n°30 tableau de bord | ✔ barre de progression + bandeau « Dans cette étape » |
| n°34 accessibilité | ✔ **40 champs, 0 sans étiquette** (`<label for>` ou `aria-label`) |
| n°42 formulation du référentiel | ✔ le texte du programme est cité mot pour mot, pas résumé |
| n°51 titre affiché | ✔ le `<h1>` et le `<title>` parlent bien de C7.1 et du cycle 4 |
| n°54 nombre annoncé ailleurs | ✔ « 5 illustrées » annoncées, 5 images dans le QCM |
| n°67 consigne sans champ | ✔ 6 zones de rédaction pour les 6 productions annoncées |
| n°31 version étayée | ⚑ **manquante** — reconnue, et assumée pour l'instant : la voie B (papier) joue déjà ce rôle pour l'activité du logiciel, mais pas pour les parcours de calcul |

**Le seul manquement connu est la n°31**, et il est écrit ici plutôt que passé sous silence.
