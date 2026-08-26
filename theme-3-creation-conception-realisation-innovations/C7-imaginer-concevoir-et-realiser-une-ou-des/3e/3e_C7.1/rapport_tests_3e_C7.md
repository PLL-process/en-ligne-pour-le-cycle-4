# Rapport de tests — 3e_C7.1 « Capteur de confort — New York » (3e_C7.1 · 3e_C8.1)

Date : 2026-08-26 (**harmonisation du lot**) · Agent : Fable ·
Environnement : Chromium headless (Playwright 1.55), viewport 1280×900 +
émulation téléphone 390×844 · Suite : `tests_3e_C7.mjs` (**committée dans ce dossier**,
rejouable : `node tests_3e_C7.mjs .`).

> Règle d'or n°136 : chaque dispositif est vérifié par la **mesure de son effet** —
> un nombre —, jamais par la présence de ses commandes.

## 1. Tests automatisés exécutés — 37/37 réussis

### Les dispositifs installés à l'harmonisation

| Règle | Vérification exécutée | Résultat |
|---|---|---|
| n°23 | cadre « 2 séances de 55 min » reconnaissable, durées à la convention `~n min` | ✅ |
| n°26 | billet d'entrée, **hors progression** — la progression reste à 0 | ✅ |
| n°29 | le mode essentiel masque la carte de référentiel **et toutes les corrections** ; un second clic rétablit | ✅ |
| n°30 | le tableau de bord liste les 6 activités, aucune cochée au départ | ✅ |
| n°31 | 4 versions étayées sur les rédactions qui comptent | ✅ |
| n°34 | aucun champ sans étiquette | ✅ |
| n°42 | les formulations de la carte sont celles du programme, au mot près | ✅ |
| n°122 · n°136 | choisir 🅲 masque **1 bloc 🅱 sur 1**, sans retirer aucun des 6 vérificateurs | ✅ |
| n°135 | aucun tableau visible sans séparation lisible | ✅ |

### Le parcours élève

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS | ✅ |
| Act. 3 : l'algorigramme validé 5/5 dans le bon ordre — et **refusé (4/5) sur un ordre faux** | ✅ |
| Tableau de bord complet, progression à 0 au départ | ✅ |
| **Sauvegarde / restauration** après rechargement | ✅ |
| La page ne sort pas sur le réseau (hors connexion complet) | ✅ |
| Mobile 390 px : débord horizontal = **0**, zéro erreur JS | ✅ |
| Zéro lien local cassé | ✅ |

### QCM

| Test | Résultat |
|---|---|
| 26 questions, 4 propositions chacune, une explication sur chacune | ✅ |
| Bonnes réponses réparties **7/7/6/6** sur les quatre positions | ✅ |
| État déclaré : génération ancienne, sans réfutation par distracteur | ✅ |

## 2. Contrôles statiques

- **Règles d'or mécanisées** : **0 manquement** (quatre avant l'harmonisation).
- **Aucun envoi réseau** : la page fonctionne entièrement hors connexion.

## 3. Ce que la campagne a trouvé

**Les 26 bonnes réponses du QCM étaient toutes en position B.** Un élève qui clique la
deuxième proposition à chaque question obtenait 26/26 sans rien savoir. Ce défaut n'existe
qu'au niveau de la **collection** : chaque question, prise seule, est irréprochable.
Aucune relecture question par question ne peut le voir — il faut compter. C'est la
règle d'or n°137, et la correction est faite par rotation des propositions (l'ordre
relatif des distracteurs est conservé), vers une suite de positions écrite en clair
dans `4e_C7.1/repartir_qcm.mjs` : reproductible, relisible, vérifiée après coup.

Le balayage des 40 QCM du dépôt, déclenché par cette découverte, a trouvé le même défaut
dans quatre autres fichiers — deux dans le Thème 3 (corrigés), trois dans le Thème 2
(signalés à Pascal, hors de mon périmètre).

## 4. Ce qui reste à faire (déclaré, pas caché)

- **Le QCM est de la génération ancienne** : 26 questions, format `{q, opts, ok, exp}`,
  **aucune réfutation par distracteur**. Le standard actuel du dépôt (lots C9) explique
  pourquoi chaque mauvaise réponse est fausse. La mise à niveau n'est pas faite ici.
- **Le verrou expérientiel de l'activité 0 n'existe pas dans ce lot** : la suite le dit
  explicitement (« contrôle NON applicable, donc NON exécuté ») plutôt que de compter
  un succès qu'elle n'a pas obtenu.
- Relecture orthotypographique humaine ; rendu à l'impression ; appareils réels.

## 5. Échecs

Aucun test en échec à la remise (37/37).
