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

## Reprise du 04/11/2026 — « 🗺 Où j'en suis » se replie à partir de la séance 2

La liste des activités poussait les onglets hors du premier écran dès la séance 2. Le bloc est maintenant un `<details>` :
ouvert à la séance 1 (rien ne change), replié dès la séance 2 derrière une ligne de 44 px qui garde le compte
(« 🗺 Où j'en suis — 2 / 6 activités validées », mis à jour avec la liste). Un clic ou le clavier le rouvre ; il reste ouvert
pendant la séance et se replie au changement de séance. Sans JavaScript, il est ouvert. La barre de progression ne change pas.
À la séance 2, en haut de page : onglets à 538 px et titre de la séance à 627 px à 1280 px (écran de 900 px) ; à 390 px,
les onglets commencent à 866 px pour un écran de 844 px (avant : 1400 px).

- `node tests_regle_311_4e_C8.1.mjs` : **34 / 34** ; `node tests_4e_C8.mjs .` : **54 / 54** (53 / 53 avant, un test ajouté : ouvert à la séance 1, replié
  à la séance 2, même compte que la progression).
- `controle_squelette` : 0 défaut, aucun « à rédiger ». Verts : `controle_impression`, `controle_verrous`, `controle_impression_papier`, fiche papier
  (`banc_papier.py`), `controle_hors_ligne`, `controle_contraste_liens`, `controle_unites`, `controle_hierarchie`, `controle_sigles`.

## Révision du 15/11/2026 (ligne 46 du suivi) — boutons radio, replis, aération, mode mission

Les 16 listes déroulantes qui posaient une question sont des groupes de boutons radio (règle d'or n°300), la grille
« Conforme ? » comprise ; `save()` garde le groupe, pas ses boutons. Les 8 menus du tableau de l'exercice incrusté restent des
menus (n°317) : l'incrustation est rétablie depuis sa source. Le rappel du cahier des charges et le Bonus sont repliés ;
l'aération passe de 22 écarts à 0 ; le mode mission reçoit 34 pourquoi (`mission_4e_C8.1.json`).

Le banc garde ses questions : un shim `_groupesRadio(page)` coche le bouton de la valeur demandée, un choix par rang (billet
d'entrée) suit l'ordre d'origine (`ORIGINE`) ; la lecture de la grille « Conforme ? » prend les valeurs de ses boutons et son
nom dans sa légende.

- `node tests_4e_C8.mjs .` : **54 / 54**.
- `node tests_regle_311_4e_C8.1.mjs` : **34 / 34**.
- `node _outils/mode_mission/banc_generique.mjs` : la page jouée écran par écran, aucun refus.
- `python3 _outils/tests_verif_regles_audit.py` : **68 / 68** (après la reconnaissance des menus `…__valid_…`).
- `verif_regles_audit.py` : 0 ✘. `audit_aeration.py --strict` : 0. `controle_impression_papier.py` : à jour.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.


## Reprise du 25/11/2026 — trois questions du QCM sur l'essai réel de la console

Questions 17 à 19 remplacées (« Après le dernier palier », « Le critère d'un essai de tenue », « La flèche grandit comme
la charge ») ; nouveau piège « L'essai d'une vraie pièce ». Commandes lancées depuis la racine :

| Commande | Résultat |
|---|---|
| `python3 _outils/qcm_aides/poser.py <qcm> qcm_aides_4e_C8.1.json` | posé, sortie 0 |
| `python3 _outils/poser_entrainement_melange.py --verifier` | sortie 0 |
| `node _outils/verif_qcm_coherence.mjs <qcm>` | 30 q, positions 8 / 7 / 7 / 8, réfutations alignées |
| `node _outils/balayer_questions_qcm.mjs --apres <lot>` | 30 questions jouées à 390 px, 90 écrans d'aide, 0 écart |
| `node _outils/qcm_aides/banc_aides.mjs <qcm>` | 30 questions dans un piège, 8 pièges au bilan, 0 refus |
| trois parcours joués au navigateur (clic sur les options, « Valider », « Terminer ») | tout juste 20,0 /20 · tout faux 0,0 /20 · les trois nouvelles seules justes 2,0 /20 |
| `controle_longueurs`, `controle_indices_qcm.mjs --muet`, `controle_unites --muet`, `controle_effectifs_qcm`, `controle_banque_qcm`, `controle_entete_qcm`, `controle_sigles` | sans écart pour ce QCM |
| `python3 _outils/controle_question_seule.py --strict` | 0 refus dans ce QCM (1 sur `main` : « En 3e, ce protocole deviendra… », n°304) |

Regardé à 390 px : les trois questions et leur indice après une réponse fausse.

Non exécuté : un vrai téléphone, Firefox, Safari. Reste : 3 questions sur document dessiné, pour 6 attendues (n°345).

## Reprise du 25/11/2026 (soir) — six questions du QCM sur document dessiné pour le téléphone (n°345)

Trois documents dessinés par `_outils/document_qcm.py` depuis `documents_qcm_4e_C8.1.json` : « Les quatre essais du
support » (questions 2 et 15), un extrait du protocole de l'essai de la console (question 18), le relevé de la flèche
(question 19). L'ancienne planche de la question 2 (`protocole_quatre_tests.svg`, 940 unités de large) donnait le verdict :
retirée. Le schéma du banc de l'activité 2 ter : les deux sacs étaient à 6 unités l'un de l'autre (✘ contact de
`controle_schemas.mjs`) ; ils sont séparés de 16 unités, reliés par la corde, page régénérée par `console_jardiniere.py`.

| Commande | Résultat |
|---|---|
| `python3 _outils/document_qcm.py documents_qcm_4e_C8.1.json --verifier` | 3 documents, 0 écart |
| `node _outils/controle_schemas.mjs <lot>` | 0 ✘ (1 ✘ sur `main` : les deux sacs du banc), 8 ⚠ sur les planches anciennes, aucun sur un `doc_…` |
| `python3 _outils/controle_question_seule.py --chantiers` | le QCM sort de D1 (6 questions sur document) ; reste P1, pas de billet de sortie |
| `node _outils/balayer_questions_qcm.mjs --apres <lot>` | 30 questions, 6 illustrées, 90 écrans d'aide, 0 écart |
| `node _outils/qcm_aides/banc_aides.mjs <qcm>` | 0 refus |
| `node tests_protocole_4e_C8.1.mjs` · `tests_4e_C8.mjs .` · `tests_simulation_4e_C8.1.mjs` · `tests_regle_311_4e_C8.1.mjs` | 18 / 18 · 54 / 54 · 13 / 13 · 34 / 34 |
| `controle_unites`, `controle_indices_qcm`, `verif_qcm_coherence`, `controle_entete_qcm`, `controle_banque_qcm`, `controle_effectifs_qcm`, `poser.py --verifier` | sans écart |

Regardé à 312 px (les trois documents seuls) et à 390 px dans le QCM (questions 2, 15, 18, 19) : texte lisible sans loupe,
0 erreur JavaScript.

Non exécuté : un vrai téléphone, Firefox, Safari.

## Reprise du 25/11/2026 (fin de journée) — le billet de sortie (n°330)

À la fin de la séance 4, juste avant le Bonus : `<section class="card" id="billetSortie">`, environ 5 minutes, seul et sans
aide, sur le crochet à cartable (un objet que la séquence n'a pas étudié). Deux réponses écrites (4e_C8.2 : l'essai de
tenue ; 4e_C8.3 : l'étape qui teste le comportement), deux versions étayées, une correction complète avec le critère de
chaque question et deux contre-exemples. Aucun bouton. En chemin : les corrections des activités 2 bis et 2 ter
(écrites par `console_jardiniere.py`) cousaient leurs idées par des « ; » ; chaque idée a maintenant sa ligne.

| Commande | Résultat |
|---|---|
| `node tests_4e_C8.mjs .` | **56 / 56** — deux tests ajoutés : la forme du billet (deux zones, deux versions étayées, deux critères, dernière séance, avant le Bonus, aucun bouton) ; la réponse écrite survit au rechargement. Le compte des durées passe à 8 (le billet a la sienne). |
| `node tests_regle_311_4e_C8.1.mjs` · `tests_protocole_4e_C8.1.mjs` · `tests_simulation_4e_C8.1.mjs` | 34 / 34 · 18 / 18 · 13 / 13 |
| `python3 _generation/console_jardiniere.py` | la page et les attendus sont à jour |
| `python3 _outils/audit_aeration.py --strict` (séquence, synthèses élève et professeur) | 0 écart (sur `main` : C1 1, C2 5 dans les corrections 2 bis et 2 ter) |
| `python3 _outils/controle_question_seule.py --chantiers` | la séquence sort de P1 |
| `node _outils/controle_squelette.mjs`, `banc_generique.mjs` (mode mission), `banc_papier.py` (4 fiches, 15 pages) | verts |
| `controle_unites`, `controle_hierarchie`, `controle_sigles`, `controle_liens`, `controle_impression_papier`, `controle_impression.mjs`, `verif_regles_audit` | sans écart |

Regardé à 390 px : le billet, ses versions étayées et sa correction ouvertes ; pas de défilement de côté, 0 erreur
JavaScript.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.

## 26/11/2026 — Plus rien d'une année précédente (n°304)

En traitant `3e_C8.2`, une recherche sur les lots C8 a trouvé trois phrases de cette séquence qui affirmaient la 5e :
« Rappel de 5e : avec la patère du hall, tu suivais un protocole fourni », la proposition « … comme en 5e » de l'activité
2 ter (et son pourquoi, page et `mission_4e_C8.1.json`), et la correction « c'est le protocole de 5e ». Elles disent
maintenant « Ce qui change : un essai de traction suit un protocole fourni… », « comme un essai de traction », « le
protocole d'un essai de traction ». Le banc de l'activité 2 ter cherchait « 5e » dans le pourquoi : il cherche « essai de
traction ».

Exécuté, dans le dossier du lot : `tests_protocole_4e_C8.1.mjs` **18 / 18** · `tests_4e_C8.mjs .` **56 / 56** ·
`tests_simulation_4e_C8.1.mjs` **13 / 13** · `tests_regle_311_4e_C8.1.mjs` **34 / 34**. À la racine :
`audit_aeration.py --strict`, `enrichir.py --verifier-tout`, `mode_mission/banc_generique.mjs`, `verif_regles_audit.py`,
`controle_squelette.mjs`, `controle_liens.py` : verts.
