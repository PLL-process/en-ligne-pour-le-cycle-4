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
creux (« Ce n'est pas la bonne réponse », « Il mesure une tension. ») fait un mauvais indice : le réécrire d'abord, en
disant pourquoi CETTE proposition ne répond pas à CETTE question (skill `qcm-html-accessible`).

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

Un lot qui a un générateur (`_generation/build_qcm.py`) repose les aides juste avant d'écrire sa page, sinon une
régénération les effacerait : `s = _poser_aides(s, sortie)` (`poser.poser_si_donnees`, qui trouve le
`qcm_aides_*.json` du dossier dont « qcm » est la page), importé en tête du générateur — modèle :
`3e_C1.1/_generation/build_qcm.py` (17/11/2026). Le pilote `5e_C2.1` passe par `apports_audit.py`.

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
