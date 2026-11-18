---
name: qcm-aides-et-pieges
description: Poser sur un QCM du gabarit maison les aides progressives (indice, règle, puis correction complète) et la révision par pièges (règle d'or n°339), avec sa carte « Avant de commencer » (n°337) — définir les pièges du lot à partir de ses confusions fréquentes, écrire `qcm_aides_<lot>.json`, poser avec `_outils/qcm_aides/poser.py`, vérifier dans le navigateur. À utiliser pour chaque QCM (généralisation décidée le 17/11/2026) et pour tout QCM neuf.
---

# Un QCM qui aide avant de corriger

Audit « double regard » du QCM de Shenzhen, transmis par Pascal le 17/11/2026 : « des aides progressives : lorsqu'un
élève se trompe, il devrait pouvoir consulter un premier indice, puis une explication plus détaillée, sans voir
immédiatement la bonne réponse » ; « une révision fondée sur les difficultés : si l'élève confond régulièrement un
interacteur et une exigence, le système devrait lui proposer plusieurs questions supplémentaires sur cette
distinction ». Règle d'or n°339. Pilote : `5e_C2.1` (#762). Les 72 QCM du gabarit maison acceptent le moteur tel quel.

## Ce que voit l'élève

- **Juste, ou non répondue** : la correction complète, comme avant (n°96 : exhaustive même après un sans-faute).
- **Fausse** : 💡 « tu as choisi C. » + le pourquoi de CETTE proposition (champ `d` de la question) ; boutons
  « 🔁 Réessayer avec cet indice », « 💡💡 Un indice de plus » (la règle à appliquer : le champ `ret`, « À retenir »),
  « 📖 Voir la correction complète ». La bonne réponse n'est ni dite ni marquée en vert avant ce dernier clic.
- **Le piège** : sous l'indice, « 🎯 C'est le piège « … » — Réviser ce piège : N questions » ; le mode `piege` ne garde
  que ses questions, celles pas encore réussies d'abord. Après deux erreurs sur un même piège : « tu t'y es déjà
  trompé·e N fois ».
- **Le bilan** : « 🎯 Tes pièges, du plus fréquent au moins fréquent », chacun avec son bouton de révision.
- **Avant de commencer** : la carte en trois lignes (n°337, skill `avant-de-commencer-trois-lignes`).

Aucun champ neuf dans les questions : le moteur se sert de `d` et de `ret`, que chaque QCM porte déjà. Un `d` vide ou
creux (« Ce n'est pas la bonne réponse », « Il mesure une tension. ») fait un mauvais indice, et un `d` réduit à « ! »
trahit un intrus-plaisanterie : les réécrire d'abord — `node _outils/qcm_aides/indices_creux.mjs <qcm> --liste`, puis
`corriger_question.py` (skill `propositions-sans-indice`, § 4).

## Définir les pièges

Un piège est une **confusion fréquente** de la séquence, pas un chapitre. On les trouve dans :
- les « Erreur fréquente » (`err`) et les « Piège classique » des activités ;
- les distracteurs qui reviennent d'une question à l'autre ;
- les « À retenir » qui opposent deux notions (« Un interacteur échange. Une exigence impose. ») ;
- les remarques de Pascal et des audits (« confond un interacteur et une exigence »).

Règles :
- **au moins trois questions** par piège (sinon, une révision n'en est pas une) ; si une confusion importante n'en a
  que deux, écrire une question jumelle, sans changer le nombre de questions du QCM sans le dire (n°338) ;
- une question dans **un seul** piège ; toutes les questions dans un piège, sauf une question d'ouverture (« ce qu'on
  fera l'an prochain ») ;
- le **libellé** est la question que l'élève doit se poser, dans ses mots : « Interacteur ou pas ? Une règle (une
  exigence), une pièce de l'objet, sa couleur » ; « Quel domaine : ergonomie, sécurité ou développement durable ? » ;
- 4 à 8 pièges pour 30 questions.

Le plan s'écrit par **numéros de questions**, lus sur `indices_creux.mjs <qcm> --liste` ; `fabriquer.py` recopie les
notions mot pour mot, refuse une question hors piège ou en double, un piège de moins de trois questions, et met les
espaces insécables avant « ? » et « : » (sinon « ? » passe seul à la ligne sur téléphone) :

```bash
python3 _outils/qcm_aides/fabriquer.py <qcm> plan.json     # écrit qcm_aides_<lot>.json à côté du QCM
#   {"lot": "…" (si le dossier a plusieurs QCM), "avant_de_commencer": {"revoir": […], "savoir_faire": […],
#    "reussir": ["…", "@std"]}, "pieges": {"cle": ["Libellé ?", [1, 4, 7]], …}}
```

## Les données, l'outil

```json
// qcm_aides_<lot>.json, dans le dossier du lot ; un lot à plusieurs QCM : qcm_aides_<lot>_<sujet>.json
// (4e_C6.2 : _arrosage, _eclairage), « qcm » dit à quelle page il va
{"qcm": "qcm_….html",
 "avant_de_commencer": {"revoir": ["…"], "savoir_faire": ["…"], "reussir": ["…"]},
 "pieges": {"dedans": {"libelle": "Interacteur ou pas ? …", "notions": ["Définition", "Ce qui contraint", "…"]}},
 "bilan_remarquable": "Remarquable ! <les notions de CE QCM> n’ont plus de secret pour toi — …"}
```

- `notions` : la notion `n` exacte de chaque question (l'outil refuse une notion inconnue, en double, ou un piège de
  moins de trois questions).
- `bilan_remarquable` : quand le premier message du bilan est celui du gabarit (n°338 ; `controle_memes_nombres.py`,
  N3, en compte 5 recopiés dans 60 QCM le 17/11/2026).

```bash
python3 _outils/qcm_aides/poser.py <qcm> <lot>/qcm_aides_<lot>.json            # pose ou met à jour
python3 _outils/qcm_aides/poser.py <qcm> <lot>/qcm_aides_<lot>.json --verifier  # 0 à jour · 1 à reposer
python3 _outils/qcm_aides/poser.py --etat [--strict]                            # le dépôt
```

État au 17/11/2026 : **72 QCM sur 72** portent la carte, les aides et les pièges (lot 3, vagues 1 à 6). Un QCM neuf
les reçoit avant sa livraison : `poser.py --etat --strict` sort à 1 sinon.

Un lot qui a un générateur (`_generation/build_qcm.py`) repose les aides juste avant d'écrire sa page, sinon une
régénération les effacerait : `s = _poser_aides(s, sortie)` (`poser.poser_si_donnees`, qui trouve le
`qcm_aides_*.json` du dossier dont « qcm » est la page), importé en tête du générateur — modèle :
`3e_C1.1/_generation/build_qcm.py` (17/11/2026). Le pilote `5e_C2.1` passe par `apports_audit.py`.

Avant de brancher un générateur, le rejouer sur l'arbre propre et lire `git diff` : vide, il est à jour ; sinon, la
régénération perdrait ce que les outils du site ont posé depuis sur la page (vague 6 : les sept ateliers du thème 1
perdaient le contraste du minuteur, la licence, les correctifs de la loupe). On le branche quand même, on ne le relance
pas, et on le signale ; puis on remet son gabarit à jour (18/11/2026 : les ateliers du thème 1 se régénèrent de nouveau
à l'identique, et `build_qcm.py --verifier`, lancé par `banc_ateliers.py`, le redit à chaque banc). Un générateur qui recopie un autre QCM comme gabarit (l'atelier de planification part du QCM de
Shenzhen) pose les aides AVANT ses contrôles de restes : elles remplacent la carte et les pièges du gabarit. Mettre
`bilan_remarquable` dans le JSON fait aussi survivre le bilan propre au QCM (n°338).

## Vérifier

- `node _outils/qcm_aides/banc_aides.mjs [qcm…]` (sans argument : chaque QCM qui porte les aides) joue chaque
  question fausse à 390 px — A1 indice sans la réponse, A2 la règle, A3 la correction complète, A4 « Réviser ce
  piège », A5 le bilan et le mode piège, A6 le compte sauvegardé, A7 la carte et zéro erreur JavaScript. Ce qu'il
  vérifie, à la main, sur un QCM au moins par vague :
- Dans Chromium, toutes les questions : réponse fausse → indice sans la bonne réponse (ni dite, ni en vert) → indice 2
  → correction complète ; un piège sous chaque indice (sauf la question d'ouverture) ; le bilan liste les pièges ; le
  bouton ouvre le mode piège ; la sauvegarde garde le compte des erreurs par piège ; aucune erreur JavaScript.
- `verif_qcm_coherence.mjs`, `controle_indices_qcm.mjs`, `controle_entete_qcm.py`, `controle_effectifs_qcm.py`,
  `controle_banque_qcm.py`, `controle_sauvegarde_locale.py` (il lit le script : le moteur n'imbrique aucun gabarit
  `${…`…`}`), `controle_boutons_vivants.py`, puis l'export Éléa (`export_moodle_xml.mjs`).
