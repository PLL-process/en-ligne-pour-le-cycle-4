# Rapport de tests — Lot 5e_C4.1 → C4.8 « Le lampadaire intelligent »

**Date** : 2026-07-23, **QCM rejoué le 2026-08-31** · **Agent** : Fable (Thème 2) ·
**Outil** : Playwright (Chromium headless), viewport mobile 390×844 ·
**Verdict global : 55 / 55 (séquence) + 25 / 25 (QCM) + 34 / 34 (règle n°311) — rejouables ✅** (au 30/10/2026, six séances, les deux chaînes animées)

> **Complément du 30/10/2026 — les deux chaînes s'animent (séance 2).** Le schéma fixe des deux chaînes laisse sa place, à l'écran, à une animation pas à pas (bloc `#chaines-lampadaire-pas-a-pas`, 9 étapes, lecteur commun `_outils/lecteur_pas_a_pas/`, moteur `_generation/chaine_pas_a_pas/`, voix `_generation/voix_chaines/`) ; le schéma fixe reste dessous, replié, et c'est lui qui s'imprime. Quatre contrôles de plus dans `tests_5e_C4.1-C4.8_sequence.mjs` (**55 / 55**) : **41** l'animation est en séance 2 avant l'activité 2, « Étape 1 / 9 », huit blocs, en colonne à 390 px sans défilement de côté, schéma fixe replié, neuf prises de voix (.ogg et .mp3) ; **42** la prédiction de l'étape 4 propose trois réponses, en choisir une mène à l'étape 5 avec son retour ; **43** « Regarder » s'arrête à l'étape 4 tant que l'élève n'a pas répondu, puis reprend (« Suivant » ne bloque pas : le banc commun du lecteur doit parcourir toutes les étapes) ; **44** « À toi » mène à l'activité 2, le schéma fixe se déplie, et à l'impression c'est lui qui sort, pas l'animation. Les six onglets portent maintenant `aria-controls` : le banc commun ouvre ainsi la séance 2. Hors suite : `banc_lecteur.py` vert sur les cinq animations du dépôt ; la mesure n°315 (`controle_schemas.mjs`) passée sur chacune des 9 étapes, à 1 280 et 390 px, en image fixe : 0 ✘, 0 ⚠.

> **Complément du 24/10/2026 — clôture.** Le Bonus a maintenant, pour chacun de ses trois défis (maquette, maison, Filius), un champ, une version étayée et un corrigé replié : ce qu'il faut observer, pourquoi, les erreurs classiques. Le bilan a son « Je me positionne » : un groupe de quatre boutons radio par code, les huit, enregistré avec le travail. `controle_squelette.mjs --json` ne signale plus rien à rédiger. La suite de la séquence passe à **51 contrôles, 51 / 51** (contrôles 36 à 40 : corrigés du Bonus, positionnement, reprise).

> **Mise à jour du 24/10/2026 — six séances.** La séance 5 annonçait 25 + 25 + 25 = 75 min pour 55. Elle garde le réseau local (act. 5) et le jeu du courrier (act. 6) : 50 min. Une **séance 6** « Défi final et bilan » reçoit l'activité 7 « Le FAST du lampadaire, complet » (exercice 2 de l'atelier FAST, 10 min, inséré par `incrustations_lots/lampadaire_s6.py`), le réinvestissement de la sonnette (25 min) et la clôture (synthèse, Bonus, bilan, QCM) : 35 min d'activités annoncées. Minutes par séance : 50 · 40 · 40 · 40 · 50 · 35. La suite de la séquence compte **46 contrôles, 46 / 46** : en plus des précédents, l'activité 7 refusée tant que l'exercice inséré n'est pas réussi, l'exercice vérifié à vide puis rempli juste, ses choix écrits dans le schéma, ses 5 réponses retrouvées au rechargement, la sauvegarde de la page qui ne capte plus les champs des exercices insérés, six onglets et le bandeau « 6 séances de 55 min », chaque séance à 55 min au plus, le bouton de fin de séance 5 qui ouvre la séance 6, la clôture en séance 6 seulement, et la relecture d'une sauvegarde faite avec la version à cinq séances (7 / 8, séance 5 cochée). Banc n°311 : **33 / 33** (lien direct vers l'activité 7, séance 6). QCM inchangé : **25 / 25**.

> **Mise à jour du 24/10/2026.** L'exercice « Lire le FAST du lampadaire » (atelier FAST, 5e) est inséré en tête de l'activité 1, qui passe à 50 min et exige sa réussite. La suite de la séquence compte désormais **34 contrôles, 34 / 34** : l'activité 1 refusée sans l'exercice, l'exercice vérifié à vide puis rempli juste, et ses réponses retrouvées au rechargement.

> **Mise au point du 31/08/2026.** Ce rapport annonçait « 26 / 26 » et citait un script
> `tests_lot05.js` qui **n'a jamais été commité**. Vingt-six coches que personne ne
> pouvait relancer : c'est exactement ce que la règle d'or n°259 condamne. Le QCM — la
> partie modifiée ce jour-là, passée de 32 à 36 questions — a maintenant sa suite
> **livrée dans le dossier** : `tests_5e_C4.1-C4.8_qcm.mjs`, 25 contrôles, qui parcourt
> réellement les 36 questions et lit la note affichée.
>
> **Suite du même jour.** La séquence a reçu la sienne : `tests_5e_C4.1-C4.8_sequence.mjs`,
> **30 contrôles**, qui remplit les sept activités, manœuvre le simulateur et provoque un
> passage devant le détecteur. Les bonnes réponses n'y sont pas recopiées : elles sont
> extraites des fonctions `CHECKS` de la page.
>
> **Ce qu'elle a trouvé en naissant.** `window.__exp` valait `{"jour":"eteint"}` **dès
> l'ouverture de la page** : la fonction d'affichage du simulateur était appelée à
> l'initialisation et enregistrait l'état affiché comme une expérience observée. Le verrou
> de l'activité 3 en exige trois — il s'ouvrait donc **d'un tiers tout seul**, avant que
> l'élève ait touché le curseur. La ligne « refus de valider l'act. 3 sans expériences
> réelles » de ce tableau était donc **partiellement fausse depuis l'origine**. Corrigé.

## Séquence — suite rejouable `tests_5e_C4.1-C4.8_sequence.mjs` (30 contrôles)

```
node tests_5e_C4.1-C4.8_sequence.mjs
```

Les seize lignes d'origine, plus quatorze que le tableau ne faisait pas : aucun
verrou ouvert au chargement (n°226), les réponses lues dans la page et non
recopiées, le simulateur conduit situation par situation, les liens locaux et les
identifiants en double.

| Test | Résultat |
|---|---|
| Chargement sans erreur JS (console + pageerror filtrés hors réseau sandbox) | ✅ |
| Rappel d'hypothèse affiché après saisie | ✅ |
| Act. 1 fonctions/solutions + matériaux : validation 9/9 | ✅ |
| Act. 2 chaîne d'énergie + natures : validation 9/9 (chaîne fléchée exigée) | ✅ |
| **Verrou expérientiel** : refus de valider l'act. 3 sans expériences réelles | ✅ |
| Simulateur : jour → éteint · nuit → veille 30 % · nuit + passage → pleine puissance | ✅ |
| Act. 3 validée 10/10 après les 3 observations réelles | ✅ |
| Act. 4 descripteurs (batterie_pct, L5, L3, 2 posés 2025) : validation 7/7 | ✅ |
| Act. 5 réseau local : validation 6/6 | ✅ |
| Act. 6 jeu du courrier (conflit de noms, sans destinataire) : validation 5/5 | ✅ |
| Act. 7 réinvestissement sonnette connectée : validée | ✅ |
| Activité 7 de la séance 6 (FAST complété, exercice d'atelier inséré) : refusée puis validée 5/5 | ✅ |
| Six séances : temps ≤ 55 min chacune, bouton s5 → s6, clôture en s6, ancienne sauvegarde relue | ✅ |
| Bonus : un champ et un corrigé replié par défi ; bilan : positionnement sur les huit codes, sauvegardé | ✅ |
| Progression 8/8 activités + coches des 6 séances (24/10/2026) | ✅ |
| Reprise après rechargement : réponses restaurées | ✅ |
| Reprise : validations ET traces d'expériences (__exp) restaurées | ✅ |
| Zéro lien local cassé (SVG, QCM, synthèses, pointeurs) | ✅ |
| Zéro erreur JS après l'ensemble des interactions | ✅ |

## QCM — suite rejouable `tests_5e_C4.1-C4.8_qcm.mjs` (25 contrôles)

```
node tests_5e_C4.1-C4.8_qcm.mjs
```

| Test | Résultat |
|---|---|
| Chargement sans erreur JS, aucune requête locale échouée | ✅ |
| La banque porte 36 questions — **nombre lu dans le manifeste**, pas recopié | ✅ |
| Chaque code porte le nombre de questions que le manifeste annonce | ✅ |
| Tout code sous le seuil de 5 dans cette banque est **renforcé ailleurs**, et le manifeste dit où (n°250) | ✅ |
| Chaque banque de renfort nommée par le manifeste existe sur le disque | ✅ |
| Gabarit maison : 4 propositions, `d[r]` vide, 4 réfutations, noms uniques, « à retenir » partout | ✅ |
| Bonnes réponses réparties A/B/C/D = 9/9/9/9 (écart max 1) | ✅ |
| Aucune bonne réponse détachée de plus de 8 caractères des autres | ✅ |
| 6 questions illustrées, fichiers SVG présents sur le disque, nombre conforme au manifeste | ✅ |
| Les cinq nombres que la page affiche sur elle-même valent 36 | ✅ |
| Aucun verrou expérientiel ouvert au chargement (n°226) | ✅ |
| Parcours complet 36/36 bonnes réponses → note 20,0/20 · bilan par 8 codes | ✅ |
| Aucune boîte modale, zéro erreur JS après le scénario complet | ✅ |

## Synthèses (2 tests)

Synthèse élève et synthèse professeur : chargement sans erreur, tous les
schémas SVG référencés présents. ✅

## Index / badge NEW (3 tests)

| Test | Résultat |
|---|---|
| Badge NEW sur 5e_C4.1 + badge unique sur la compétence C4 | ✅ |
| Ancre `#5e_C4.1` : auto-ouverture du dépliant C4 + ciblage visuel | ✅ |
| Pointeurs 5e_C4.2 → C4.8 badgés NEW | ✅ |

## Limites connues

- Google Fonts inaccessible dans le bac à sable de test : erreurs réseau
  filtrées (la page utilise des polices de repli système, sans incidence).
- Tests exécutés en local (`file://`) ; le comportement GitHub Pages est
  identique (aucune requête serveur, liens relatifs).
- La version 🅰 (sortie parking + maquette Grove) n'est pas testable en
  sandbox : la page l'annonce comme option matérielle sans en dépendre.
