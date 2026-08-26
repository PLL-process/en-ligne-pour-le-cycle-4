# Rapport de tests — 4e_C7 « Jardin connecté : concevoir » (4e_C7.1 · C7.2 · C7.3)

Date : 2026-08-26 (**harmonisation du lot** ; versions antérieures : 2026-07, agent Grok) ·
Agent : Fable · Environnement : Chromium headless (Playwright 1.55),
viewport 1280×900 + émulation téléphone 390×844 · Suite : `tests_4e_C7.mjs`
(**committée dans ce dossier**, rejouable : `node tests_4e_C7.mjs .`).

> Règle d'or n°136 : chaque dispositif est vérifié par la **mesure de son effet** — un
> nombre —, jamais par la présence de ses commandes.

## 1. Tests automatisés exécutés — 41/41 réussis

### Les dispositifs installés à l'harmonisation

| Règle | Vérification exécutée | Résultat |
|---|---|---|
| n°23 | cadre « 2 séances de 55 min » reconnaissable, 5 durées à la convention `~n min`, total 85 min pour 110 | ✅ |
| n°26 | billet d'entrée (acquis de 5e), **hors progression** — la progression reste à 0 | ✅ |
| n°29 | le mode essentiel masque la carte de référentiel **et les 6 corrections** ; un second clic rétablit | ✅ |
| n°30 | le tableau de bord liste les 6 activités, aucune cochée au départ | ✅ |
| n°31 | 3 versions étayées (hypothèse, choix de solution, réinvestissement) | ✅ |
| n°34 | aucun champ sans étiquette (38 champs) | ✅ |
| n°42 | les 3 formulations de la carte sont celles du programme, au mot près | ✅ |
| n°122 · n°136 | choisir 🅲 masque **1 bloc 🅱 sur 1**, sans retirer aucun des 6 vérificateurs | ✅ |
| n°135 | aucun des 4 tableaux visibles sans séparation lisible | ✅ |

### Le parcours élève

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS | ✅ |
| Act. 0 : **refusée** tant que 3 combinaisons n'ont pas été soumises au banc météo | ✅ |
| Act. 0 : le banc rend un verdict pour l'essai joué, puis l'activité se valide 2/2 | ✅ |
| Act. 1 : diagramme validé 5/5 dans le bon ordre — et **refusé (4/5) sur un ordre faux** | ✅ |
| Progression 1/6 · tâche cochée au tableau de bord · barre à 17 % | ✅ |
| **Sauvegarde / restauration** après rechargement | ✅ |
| La page ne sort pas sur le réseau (hors connexion complet) | ✅ |
| Mobile 390 px : débord horizontal = **0**, zéro erreur JS | ✅ |
| Zéro lien local cassé (5 HTML parcourus) | ✅ |

### QCM

| Test | Résultat |
|---|---|
| 28 questions, 4 propositions chacune, une explication sur chacune | ✅ |
| Bonnes réponses réparties **7/7/7/7** sur les quatre positions | ✅ |
| État déclaré : génération ancienne, sans réfutation par distracteur | ✅ (0 réfutation, conforme à ce qui est déclaré) |

## 2. Contrôles statiques

- **Règles d'or mécanisées** (`python3 _outils/verif_regles_audit.py …`) : **0 manquement**.
  Avant l'harmonisation : cinq — n°23, n°26, n°29, n°30, n°31 et n°34.
- **Aucun envoi réseau** : la page fonctionne entièrement hors connexion, sauvegarde
  `localStorage` comprise. La suite le vérifie en écoutant les requêtes sortantes.

## 3. Ce que la campagne a trouvé — le défaut le plus grave du lot

**Les 28 bonnes réponses du QCM étaient toutes en position B.**

Un élève qui clique la deuxième proposition à chaque question obtenait **28/28** sans
rien savoir. Le QCM ne mesurait plus rien : il récompensait la découverte d'un motif,
pas la connaissance. Et cela ne se voyait ni à l'écran, ni à l'usage — il faut
**compter les positions** pour que ça saute aux yeux.

Corrigé : les propositions de chaque question ont été **tournées** (l'ordre relatif des
distracteurs est conservé) pour amener la bonne réponse sur une position voulue. La
suite de positions est écrite en clair dans l'outil `repartir_qcm.mjs` : équilibrée
(7 par lettre), sans cycle apparent, et **reproductible** — ce n'est pas un tirage au
hasard qui donnerait un fichier différent à chaque exécution. L'outil vérifie après
rotation que `opts[nouvelle position]` est bien le texte de l'ancienne bonne réponse ;
sans cette assertion, une erreur de rotation aurait faussé silencieusement tout le QCM.

> **Le balayage qui a suivi.** Le même contrôle passé sur les 40 QCM du dépôt a trouvé
> **deux autres cas dans le Thème 3** (5e_C7 : 24 questions toutes en B ; 3e_C7 :
> 26 questions toutes en B) — corrigés au passage — et **trois cas dans le Thème 2**,
> hors de mon périmètre, signalés à Pascal sans y toucher.

## 4. Ce qui reste à faire (déclaré, pas caché)

- **Le QCM est de la génération ancienne du dépôt** : 28 questions au lieu de 30, format
  `{q, opts, ok, exp}`, et **aucune réfutation par distracteur**. Le standard actuel
  (voir les lots C9) explique pourquoi chaque mauvaise réponse est fausse. La mise à
  niveau n'est pas faite ici — la dire est plus utile que de la laisser croire.
- Relecture orthotypographique humaine ; rendu à l'impression ; appareils réels.

## 5. Une décision à valider par Pascal

La page annonçait « **4 × 55 min** » pour **85 minutes** d'activités. Les deux séances
manquantes ne sont pas perdues : elles se passent **ailleurs**, sur le TP « Le dé sur son
socle » (modélisation Onshape) et sur l'atelier de planification, tous deux liés en bas de
page. L'en-tête dit désormais « **2 séances de 55 min sur cette page** (+ 2 séances sur le
TP et l'atelier) — soit 4 au total pour le lot ».

C'est une formulation, pas un changement de contenu. Mais elle engage la lecture du lot :
si le découpage réel est différent, c'est à corriger d'un mot.

## 6. Échecs

Aucun test en échec à la remise (41/41). Trois échecs rencontrés en cours de campagne :
le QCM concentré en position B (corrigé, §3), trois champs de bilan sans étiquette
(corrigés), et deux critères de la suite elle-même mal calibrés — elle attendait
six durées là où l'activité 1 en porte deux vérificateurs sous une seule durée annoncée,
et elle exigeait un tableau `QUESTIONS` alors que ces QCM le nomment `questions`.
