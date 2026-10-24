# Rapport de tests — atelier « La carte mentale »

Écrit le 2026-10-24 par `_generation/gouvernance.py`, **à partir des exécutions faites à l'instant** : rien n'y est déclaré qui n'ait tourné (règle d'or n°299 : un contrôle qui n'a rien vérifié est en panne).

## Banc de l'atelier (`banc_ateliers.py carte_mentale`, Chromium, 390 px)

Code de sortie : **0** — 43 / 43 tests passés

- ✔ carte-mentale 5e : aucune erreur JavaScript au chargement
- ✔ carte-mentale 5e : aucun défilement horizontal à 390 px
- ✔ carte-mentale 5e : un onglet par exercice, plus la clôture (3)
- ✔ carte-mentale 5e · e1 : « Vérifier » à vide donne un retour à reprendre
- ✔ carte-mentale 5e · e1 : rempli juste, « Tout est juste »
- ✔ carte-mentale 5e · e2 : « Vérifier » à vide donne un retour à reprendre
- ✔ carte-mentale 5e · e2 : rempli juste, « Tout est juste »
- ✔ carte-mentale 5e : la sauvegarde locale du premier exercice existe
- ✔ carte-mentale 5e : le premier exercice est noté réussi après rechargement
- ✔ carte-mentale 5e : aucune erreur JavaScript pendant le parcours
- ✔ carte-mentale 4e : aucune erreur JavaScript au chargement
- ✔ carte-mentale 4e : aucun défilement horizontal à 390 px
- ✔ carte-mentale 4e : un onglet par exercice, plus la clôture (3)
- ✔ carte-mentale 4e · e3 : « Vérifier » à vide donne un retour à reprendre
- ✔ carte-mentale 4e · e3 : rempli juste, « Tout est juste »
- ✔ carte-mentale 4e · e4 : « Vérifier » à vide donne un retour à reprendre
- ✔ carte-mentale 4e · e4 : rempli juste, « Tout est juste »
- ✔ carte-mentale 4e : la sauvegarde locale du premier exercice existe
- ✔ carte-mentale 4e : le premier exercice est noté réussi après rechargement
- ✔ carte-mentale 4e : aucune erreur JavaScript pendant le parcours
- ✔ carte-mentale 3e : aucune erreur JavaScript au chargement
- ✔ carte-mentale 3e : aucun défilement horizontal à 390 px
- ✔ carte-mentale 3e : un onglet par exercice, plus la clôture (3)
- ✔ carte-mentale 3e · e5 : « Vérifier » à vide donne un retour à reprendre
- ✔ carte-mentale 3e · e5 : rempli juste, « Tout est juste »
- ✔ carte-mentale 3e · e6 : « Vérifier » à vide donne un retour à reprendre
- ✔ carte-mentale 3e · e6 : rempli juste, « Tout est juste »
- ✔ carte-mentale 3e : la sauvegarde locale du premier exercice existe
- ✔ carte-mentale 3e : le premier exercice est noté réussi après rechargement
- ✔ carte-mentale 3e : aucune erreur JavaScript pendant le parcours
- ✔ carte-mentale QCM (390 px) : aucune erreur JavaScript
- ✔ carte-mentale QCM (390 px) : aucun défilement horizontal
- ✔ carte-mentale QCM : 30 questions
- ✔ carte-mentale QCM (1280 px) : aucune erreur JavaScript
- ✔ carte-mentale QCM (1280 px) : aucun défilement horizontal
- ✔ carte-mentale synthèse élève (390 px) : aucune erreur JavaScript
- ✔ carte-mentale synthèse élève (390 px) : aucun défilement horizontal
- ✔ carte-mentale synthèse élève (1280 px) : aucune erreur JavaScript
- ✔ carte-mentale synthèse élève (1280 px) : aucun défilement horizontal
- ✔ carte-mentale synthèse professeur (390 px) : aucune erreur JavaScript
- ✔ carte-mentale synthèse professeur (390 px) : aucun défilement horizontal
- ✔ carte-mentale synthèse professeur (1280 px) : aucune erreur JavaScript
- ✔ carte-mentale synthèse professeur (1280 px) : aucun défilement horizontal

## Contrôles du dépôt

| Contrôle | Code | Dernière ligne |
|---|---|---|
| `controle_longueurs.py` | 0 | Aucune banque signalée. |
| `controle_hierarchie.py` | 0 | 4 page(s) lues · ✅ aucune énumération en ligne, aucun mur sans repère, aucun paragraphe tout en gras, aucune cellule-pavé, aucun item-pavé, aucun pavé hors séquence |
| `controle_regles_visibles.py` | 0 | ✅ aucune page lue par un élève ne laisse voir la fabrique (règle d'or n°309) |
| `controle_medias.py` | 0 | ✅ chaque image du dépôt a une provenance écrite, et aucune n'est promise en vain |
| `controle_liens.py` | 0 | ✅ aucun lien mort, aucune ancre introuvable dans le périmètre regardé |
| `verif_qcm_coherence.mjs` | 0 | ✅ qcm_carte-mentale.html · 30 q · positions {"0":8,"1":7,"2":7,"3":8} · réfutations alignées |

## Non exécuté ici

- La relecture humaine des dessins (captures PNG regardées à la production, non rejouées par ce script).
- Les bancs des séquences qui accueillent des exercices insérés : ils se lancent dans le dossier de chaque séquence.
