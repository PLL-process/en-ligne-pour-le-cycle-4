# Rapport de tests — 5e_C7.1 « Mini-projet : le voyant du hall » (5e_C7.1 · C8.3 · C9.3)

Date : 2026-08-26 (**harmonisation du lot**) · Agent : Fable ·
Environnement : Chromium headless (Playwright 1.55), viewport 1280×900 +
émulation téléphone 390×844 · Suite : `tests_5e_C7.mjs` (**committée dans ce dossier**,
rejouable : `node tests_5e_C7.mjs .`).

> Règle d'or n°136 : chaque dispositif est vérifié par la **mesure de son effet** —
> un nombre —, jamais par la présence de ses commandes.

## 1. Tests automatisés exécutés — 37/37 réussis

### Les dispositifs installés à l'harmonisation

| Règle | Vérification exécutée | Résultat |
|---|---|---|
| n°23 | cadre « 3 séances de 55 min » reconnaissable, durées à la convention `~n min` | ✅ |
| n°26 | billet d'entrée, **hors progression** — la progression reste à 0 | ✅ |
| n°29 | le mode essentiel masque la carte de référentiel **et toutes les corrections** ; un second clic rétablit | ✅ |
| n°30 | le tableau de bord liste les 6 activités, aucune cochée au départ | ✅ |
| n°31 | 2 versions étayées sur les rédactions qui comptent | ✅ |
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
| 24 questions, 4 propositions chacune, une explication sur chacune | ✅ |
| Bonnes réponses réparties **6/6/6/6** sur les quatre positions | ✅ |
| État déclaré : génération ancienne, sans réfutation par distracteur | ✅ |

## 2. Contrôles statiques

- **Règles d'or mécanisées** : **0 manquement** (quatre avant l'harmonisation).
- **Aucun envoi réseau** : la page fonctionne entièrement hors connexion.

## 3. Ce que la campagne a trouvé

**Les 24 bonnes réponses du QCM étaient toutes en position B.** Un élève qui clique la
deuxième proposition à chaque question obtenait 24/24 sans rien savoir. Ce défaut n'existe
qu'au niveau de la **collection** : chaque question, prise seule, est irréprochable.
Aucune relecture question par question ne peut le voir — il faut compter. C'est la
règle d'or n°137, et la correction est faite par rotation des propositions (l'ordre
relatif des distracteurs est conservé), vers une suite de positions écrite en clair
dans `4e_C7.1/repartir_qcm.mjs` : reproductible, relisible, vérifiée après coup.

**Et une carte de référentiel en double.** Le lot en possédait déjà une, mieux écrite que
celle que j'allais poser : elle porte l'histoire de la correction des codes (« cette séquence
annonçait auparavant C7 · C8 · C9, c'est-à-dire douze compétences pour en servir trois »).
J'ai retiré la mienne et gardé la sienne — en déplaçant ses codes de `<th>` vers `<td>` pour
que le contrôle n°42 puisse les lire, et en la remontant avant l'en-tête pédagogique.

> **Pourquoi la remonter ?** Le contrôle n°42 cherche `referentiel-card`, puis le **premier
> `</table>` qui suit**. Comme le mot apparaît d'abord dans la feuille de style, c'est le
> premier tableau de la page qui était lu — pas la carte. Le raccourci est signalé à Pascal ;
> en attendant, la carte est placée avant tout autre tableau, ce qui est de toute façon sa
> place logique.

## 4. Ce qui reste à faire (déclaré, pas caché)

- **Le QCM est de la génération ancienne** : 24 questions, format `{q, opts, ok, exp}`,
  **aucune réfutation par distracteur**. Le standard actuel du dépôt (lots C9) explique
  pourquoi chaque mauvaise réponse est fausse. La mise à niveau n'est pas faite ici.
- **Le verrou expérientiel de l'activité 0 n'existe pas dans ce lot** : la suite le dit
  explicitement (« contrôle NON applicable, donc NON exécuté ») plutôt que de compter
  un succès qu'elle n'a pas obtenu.
- Relecture orthotypographique humaine ; rendu à l'impression ; appareils réels.

## 5. Échecs

Aucun test en échec à la remise (37/37).
