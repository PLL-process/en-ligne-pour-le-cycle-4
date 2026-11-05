# Rapport de tests — 5e_C7.1 « Mini-projet : le voyant du hall » (5e_C7.1 · C8.3 · C9.3)

Date : 2026-08-26 (**harmonisation du lot**) · Agent : Fable ·
Environnement : Chromium headless (Playwright 1.55), viewport 1280×900 +
émulation téléphone 390×844 · Suite : `tests_5e_C7.mjs` (**committée dans ce dossier**,
rejouable : `node tests_5e_C7.mjs .`).

> Règle d'or n°136 : chaque dispositif est vérifié par la **mesure de son effet** —
> un nombre —, jamais par la présence de ses commandes.

> **Mise à jour du 31/10/2026 — règle d'or n°317.** La grille de validation de l'activité 2 se complète dans le
> tableau : menus nommés (« Ligne 1, poser le sac — résultat attendu »), décision globale sur sa dernière ligne (elle
> était sous le tableau), un retour écrit sous chaque case fausse ou vide après « Vérifier », et une correction
> ligne par ligne qui réfute chaque piège. La suite compte **46 / 46** (42 avant) : les 6 menus dans leurs cases et
> nommés ; « ○ Sans réponse » à vide ; les 7 options fausses, chacune son retour ; la grille juste validée 6/6, sans
> retour restant.

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
| 30 questions, 4 propositions `o` chacune (bonne réponse `r` de 0 à 3), une explication `expl` sur chacune | ✅ |
| Bonnes réponses réparties **8/7/7/8** sur les quatre positions | ✅ |
| État déclaré : chaque mauvaise réponse a sa réfutation (`d` : 4 entrées, vide sur la bonne) — 30 sur 30 | ✅ |

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

- **Le QCM est au standard actuel** : 30 questions, format `{q, o, r, expl, d}`, une
  réfutation par mauvaise réponse. Le banc le lit dans ce format, sans repli sur l'ancien
  (`opts`, `ok`, `exp`) : la mise à niveau n'est plus à faire (5 octobre 2026).
- **Le verrou expérientiel de l'activité 0 n'existe pas dans ce lot** : la suite le dit
  explicitement (« contrôle NON applicable, donc NON exécuté ») plutôt que de compter
  un succès qu'elle n'a pas obtenu.
- Relecture orthotypographique humaine ; rendu à l'impression ; appareils réels.

## 5. Échecs

Aucun test en échec à la remise (37/37).

## 6. Rejouée le 05/10/2026 (encart des gestes sans compte, mode mixte conservé, version 🅰 retirée)

La suite a été **rejouée après le lot du 05/10/2026** : **42 tests, 39 réussis** — les 5 contrôles ajoutés, préfixés « gestes », passent : les liens-boutons gardent l'éditeur
en `?mode=mixed` ; plus de version 🅰 (ni bouton, ni carte, ni « Avec le matériel ») ; l'activité 3 limite le volet Python et demande de nommer puis télécharger le projet (geste 4) ; les
11 captures de l'encart se chargent avec un texte alternatif ; un ancien choix « a » mémorisé retombe sur « tous ». **Les 3 échecs restants sont ceux du QCM**
(« chaque question a 4 propositions », « chaque question porte une explication », « état déclaré ») : la suite attend encore l'ancien format du QCM ; ils étaient déjà là sur `main`
(34 / 37), ne viennent pas de ce lot, et sont traités dans un lot « bancs » dédié. Ce que la fiche de remise annonçait (« 37 / 37 ») n'était donc plus exact avant ce lot.

Le contenu de Vittascience (blocs, Python, réouverture du fichier) a été mesuré à la main avec les programmes exacts de l'activité 3b et n'est pas rejoué ici : service externe.

## 7. Reprise du 04/11/2026 — la séquence passe à onglets (vague n°311, sur le modèle du pilote 4e_C8.1)

La page était d'un seul tenant. Elle a maintenant trois séances à onglets (squelette n°306) et le volet « 📖 Rappel » dès la
séance 2 (n°311) : séance 1 = ouverture + activités 0 et 1 ; séance 2 = activité 2, les gestes de Vittascience, activité 3 ;
séance 3 = réinvestissement, synthèse, Bonus, bilan, TP « Le dé », atelier de planification, QCM. Le billet d'entrée rejoint
sa place du squelette (après l'idée de départ). Le simulateur de place sert aux séances 1 et 2 : un seul nœud, rangé dans la
séance ouverte, sous son en-tête. La clôture est complétée : un corrigé replié par défi du Bonus, le retour à l'idée de départ,
« Comment j'ai travaillé » et « Je me positionne » sur 5e_C7.1, C8.3 et C9.3 aux quatre niveaux du livret. La page ne portait
ni la chaîne `rappel-ouverture` ni d'exercice incrusté des ateliers.

- `node tests_regle_311_5e_C7.1.mjs` (relais du thème 3 → banc commun) : **34 / 34**.
- `node tests_5e_C7.mjs .` : **47 / 47** (46 avant) — les durées se lisent dans toute la page, pas seulement à l'écran ;
  l'activité 3 et la grille s'ouvrent par l'onglet de la séance 2 ; un test ajouté (trois séances, le volet, le simulateur
  dans la séance ouverte).
- `controle_squelette.mjs` : 0 défaut (D1 à D6), aucun « à rédiger », aucun signalement.
- Verts : `controle_impression.mjs`, `controle_verrous.mjs`, `controle_hors_ligne.mjs`, `controle_contraste_liens.mjs`,
  `controle_impression_papier.py`, `controle_regles_visibles.py`, `controle_liens.py`, `controle_hierarchie.py`,
  `controle_unites.py`, `controle_sigles.py`, `controle_navigation_seances.py`, `controle_mode_essentiel.py`,
  `controle_competences.py`. Fiche papier (`banc_papier.py`) : une fiche par séance, sans champ d'écran ni texte pâle.
- `verif_regles_audit.py` : les mêmes ✘ qu'avant la reprise (vérifié sur `main`), hors périmètre de cette vague.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.

## Reprise du 04/11/2026 — « 🗺 Où j'en suis » se replie à partir de la séance 2

La liste des activités poussait les onglets hors du premier écran dès la séance 2. Le bloc est maintenant un `<details>` :
ouvert à la séance 1 (rien ne change), replié dès la séance 2 derrière une ligne de 44 px qui garde le compte
(« 🗺 Où j'en suis — 2 / 6 activités validées », mis à jour avec la liste). Un clic ou le clavier le rouvre ; il reste ouvert
pendant la séance et se replie au changement de séance. Sans JavaScript, il est ouvert. La barre de progression ne change pas.
À la séance 2, en haut de page : onglets à 513 px et titre de la séance à 604 px à 1280 px (écran de 900 px) ; à 390 px,
les onglets commencent à 866 px pour un écran de 844 px (avant : 1377 px).

- `node tests_regle_311_5e_C7.1.mjs` : **34 / 34** ; `node tests_5e_C7.mjs .` : **48 / 48** (47 / 47 avant, un test ajouté : ouvert à la séance 1, replié
  à la séance 2, même compte que la progression).
- `controle_squelette` : 0 défaut, aucun « à rédiger ». Verts : `controle_impression`, `controle_verrous`, `controle_impression_papier`, fiche papier
  (`banc_papier.py`), `controle_hors_ligne`, `controle_contraste_liens`, `controle_unites`, `controle_hierarchie`, `controle_sigles`.
