# Rapport de tests — Lot 5e_C4.1 → C4.8 « Le lampadaire intelligent »

**Date** : 2026-07-23, **QCM rejoué le 2026-08-31** · **Agent** : Fable (Thème 2) ·
**Outil** : Playwright (Chromium headless), viewport mobile 390×844 ·
**Verdict global : 21 / 21 (séquence, tableau écrit) + 25 / 25 (QCM, rejouable) ✅**

> **Mise au point du 31/08/2026.** Ce rapport annonçait « 26 / 26 » et citait un script
> `tests_lot05.js` qui **n'a jamais été commité**. Vingt-six coches que personne ne
> pouvait relancer : c'est exactement ce que la règle d'or n°259 condamne. Le QCM — la
> partie modifiée ce jour-là, passée de 32 à 36 questions — a maintenant sa suite
> **livrée dans le dossier** : `tests_5e_C4.1-C4.8_qcm.mjs`, 25 contrôles, qui parcourt
> réellement les 36 questions et lit la note affichée.
>
> **Limite déclarée, et elle est réelle** : les 16 contrôles de la séquence restent un
> tableau écrit à la main. Ils n'ont pas été rejoués le 31/08 — la séquence n'a pas été
> modifiée ce jour-là, à un nombre près (« 36 questions » au lieu de « 32 »). Écrire
> leur suite est le prochain geste dû à ce lot.

## Séquence (16 tests)

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
| Progression 7/7 activités + coches des 5 séances | ✅ |
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
