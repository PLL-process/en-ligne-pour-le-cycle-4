# Rapport de tests — 4e_C8 « Jardin connecté : valider » (4e_C8.1 · C8.2 · C8.3)

Date : 2026-08-26 (**harmonisation du lot** ; version antérieure : 2026-07-25, agent Grok) ·
Agent : Fable · Environnement : Chromium headless (Playwright 1.55),
viewport 1280×900 + émulation téléphone 390×844 · Suite : `tests_4e_C8.mjs`
(**committée dans ce dossier**, rejouable : `node tests_4e_C8.mjs .`).

> Règle d'or n°136 : chaque dispositif est vérifié par la **mesure de son effet** — un
> nombre —, jamais par la présence de ses commandes.

> **Mise à jour du 31/10/2026 — règle d'or n°317.** L'exercice incrusté de l'activité 2 (atelier des exigences, 4e,
> exercice 3) se complète maintenant dans le tableau du cahier des charges : 8 menus `ex_4e_e3__valid_<ligne>_3`
> (le test) et `_5` (le verdict), réincrusté depuis l'atelier. La grille « Conforme ? » de la page reçoit des menus
> nommés (« Ligne 1, … — conforme ? »), la décision globale sur sa dernière ligne, un retour écrit sous chaque case
> fausse ou vide après « Vérifier », et une correction ligne par ligne qui réfute chaque piège. La suite compte
> **53 / 53** (48 avant) : cinq contrôles ajoutés (les 5 menus de la grille dans leurs cases et nommés ; « ○ Sans
> réponse » à vide ; les 10 options fausses, chacune son retour ; les 8 menus de l'exercice et le retour d'un test
> faux exprès ; les 8 menus retrouvés au rechargement). À l'impression, la page retire la liste d'options que la
> fiche papier ajoute sous chaque menu du tableau incrusté.

## 1. Tests automatisés exécutés — 41/41 réussis

### Les dispositifs installés à l'harmonisation

| Règle | Vérification exécutée | Résultat |
|---|---|---|
| n°23 | cadre « 3 séances de 55 min » reconnaissable, 5 durées à la convention `~n min`, total 80 min pour 165 | ✅ |
| n°26 | billet d'entrée (acquis de 4e_C7), **hors progression** — la progression reste à 0 | ✅ |
| n°29 | le mode essentiel masque la carte de référentiel **et les corrections** ; un second clic rétablit | ✅ |
| n°30 | le tableau de bord liste les 6 activités, aucune cochée au départ | ✅ |
| n°31 | 4 versions étayées (hypothèse, diagnostic, améliorations, réinvestissement) | ✅ |
| n°34 | aucun champ sans étiquette (38 champs) | ✅ |
| n°42 | les 3 formulations de la carte sont celles du programme, au mot près | ✅ |
| n°122 · n°136 | choisir 🅲 masque **1 bloc 🅱 sur 1**, sans retirer aucun des 6 vérificateurs | ✅ |
| n°135 | aucun tableau visible sans séparation lisible | ✅ |

### Le parcours élève

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS | ✅ |
| Act. 0 : **refusée** tant que 3 tests n'ont pas été lancés au banc virtuel | ✅ |
| Act. 0 : le banc rend un verdict, puis l'activité se valide 2/2 | ✅ |
| Act. 1 : le raisonnement de validation validé 5/5 — et **refusé (4/5) sur un ordre faux** | ✅ |
| Progression 1/6 · tâche cochée au tableau de bord · barre à 17 % | ✅ |
| **Sauvegarde / restauration** après rechargement | ✅ |
| La page ne sort pas sur le réseau (hors connexion complet) | ✅ |
| Mobile 390 px : débord horizontal = **0**, zéro erreur JS | ✅ |
| Zéro lien local cassé (4 HTML parcourus) | ✅ |

### QCM

| Test | Résultat |
|---|---|
| 28 questions, 4 propositions chacune, une explication sur chacune | ✅ |
| Bonnes réponses réparties **7/7/7/7** sur les quatre positions | ✅ |
| État déclaré : génération ancienne, sans réfutation par distracteur | ✅ |

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

## 5. Échecs

Aucun test en échec à la remise (41/41). Le défaut majeur trouvé — le QCM entièrement
concentré en position B — est décrit au §3 ; il touchait ce lot comme son jumeau 4e_C7.

## 6. 25/10/2026 — La situation animée « Une année sur le toit » et le banc animé (lecteur pas à pas commun)

Décisions de Pascal « 1a 2a 3b 4b » (journal du 25/10/2026). Commandes lancées comme on les lance, en sous-processus :

| Commande | Résultat |
|---|---|
| `node tests_4e_C8.mjs` | **48 / 48** — le banc attend la fin de chaque test animé et refuse un verdict dans la mesure (« réussi », « conforme », « au rendez-vous », « FISSURÉE ») |
| `python3 ../../../../_outils/lecteur_pas_a_pas/banc_lecteur.py` (depuis la racine : sans argument) | **vert** sur les 4 animations du dépôt, dont `#annee-sur-le-toit-pas-a-pas` (7 étapes) : 1280 et 390 px, mouvement réduit, 14 fichiers de voix présents, impression (7 étapes), lien direct |
| `python3 _generation/voix_situation/generer.py --verifier` | les 7 phrases de `phrases.json` sont celles de la page, mot pour mot |
| `python3 _outils/controle_lecteur_pas_a_pas.py` (racine) | sortie 0 |

Regardé à l'œil, captures dans `_generation/captures_animations/` : les sept étapes à 1280 px, trois étapes à 390 px,
les quatre postes du banc pendant puis à la fin du test. Aucune étape de la situation ne montre le résultat d'un test.

**Non exécuté** : l'écoute des sept prises (Pascal) ; Safari, iPad, téléphone réel.

## Reprise du 31/10/2026 — la séquence passe à onglets (pilote des 23 séquences sans onglets)

La page était d'un seul tenant : tout visible, pas de volet possible. Elle a maintenant trois séances à onglets (squelette
n°306) et le volet « 📖 Rappel » dès la séance 2 (n°311) : séance 1 = ouverture + activités 0 et 1 ; séance 2 = activité 2 ;
séance 3 = activité 3, réinvestissement, synthèse, Bonus, bilan, QCM. Chaque séance a sa question directrice et son bouton
vers la suivante (n°101) ; l'onglet en cours est mémorisé. La clôture est complétée : un corrigé replié par défi du Bonus
(n°86), le retour à l'hypothèse, « Comment j'ai travaillé » et « Je me positionne » sur 4e_C8.1 à C8.3 aux quatre niveaux
du livret (n°301). Le sélecteur de parcours tient sur deux lignes à 390 px.

- `node tests_regle_311_4e_C8.1.mjs` (relais du thème 3 → banc commun) : **34 / 34** — captures jointes à la PR.
- `node tests_4e_C8.mjs` : **53 / 53**, deux pas adaptés (les durées se lisent dans toute la page, pas seulement à l'écran ;
  l'activité 2 s'ouvre par son onglet).
- `controle_squelette.mjs` : 0 défaut (D1 à D6), aucun « à rédiger », aucun signalement.
- `verif_regles_audit.py` : 1 ✘ déjà présent avant (n°300 : 25 questions par liste déroulante) — hors périmètre de ce pilote.
- Verts : `controle_impression_papier` (3 fiches, 9 pages, une séance par fiche), `controle_impression` (0 page refusée),
  navigation des séances, hiérarchie, règles visibles, unités, sigles, compétences, liens, mode essentiel, verrous, hors ligne.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle. Non fait : le lexique par séance (le lexique du lot
n'a pas d'ancres `#seance-sN`) ; la conversion des listes déroulantes en boutons radio (n°300).
