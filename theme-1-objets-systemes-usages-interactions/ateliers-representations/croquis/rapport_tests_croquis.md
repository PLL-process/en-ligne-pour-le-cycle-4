# Rapport de tests — atelier « Le croquis »

Écrit le 2026-10-24 par `_generation/gouvernance.py`, **à partir des exécutions faites à l'instant** : rien n'y est déclaré qui n'ait tourné (règle d'or n°299 : un contrôle qui n'a rien vérifié est en panne).

## Banc de l'atelier (`banc_ateliers.py croquis`, Chromium, 390 px)

Code de sortie : **0** — 37 / 37 tests passés

- ✔ croquis 4e : aucune erreur JavaScript au chargement
- ✔ croquis 4e : aucun défilement horizontal à 390 px
- ✔ croquis 4e : un onglet par exercice, plus la clôture (4)
- ✔ croquis 4e · e1 : « Vérifier » à vide donne un retour à reprendre
- ✔ croquis 4e · e1 : rempli juste, « Tout est juste »
- ✔ croquis 4e · e2 : « Vérifier » à vide donne un retour à reprendre
- ✔ croquis 4e · e2 : rempli juste, « Tout est juste »
- ✔ croquis 4e · e3 : « Vérifier » à vide donne un retour à reprendre
- ✔ croquis 4e · e3 : rempli juste, « Tout est juste »
- ✔ croquis 4e : la sauvegarde locale du premier exercice existe
- ✔ croquis 4e : le premier exercice est noté réussi après rechargement
- ✔ croquis 4e : aucune erreur JavaScript pendant le parcours
- ✔ croquis 3e : aucune erreur JavaScript au chargement
- ✔ croquis 3e : aucun défilement horizontal à 390 px
- ✔ croquis 3e : un onglet par exercice, plus la clôture (4)
- ✔ croquis 3e · e4 : « Vérifier » à vide donne un retour à reprendre
- ✔ croquis 3e · e4 : rempli juste, « Tout est juste »
- ✔ croquis 3e · e5 : « Vérifier » à vide donne un retour à reprendre
- ✔ croquis 3e · e5 : rempli juste, « Tout est juste »
- ✔ croquis 3e · e6 : « Vérifier » à vide donne un retour à reprendre
- ✔ croquis 3e · e6 : rempli juste, « Tout est juste »
- ✔ croquis 3e : la sauvegarde locale du premier exercice existe
- ✔ croquis 3e : le premier exercice est noté réussi après rechargement
- ✔ croquis 3e : aucune erreur JavaScript pendant le parcours
- ✔ croquis QCM (390 px) : aucune erreur JavaScript
- ✔ croquis QCM (390 px) : aucun défilement horizontal
- ✔ croquis QCM : 30 questions
- ✔ croquis QCM (1280 px) : aucune erreur JavaScript
- ✔ croquis QCM (1280 px) : aucun défilement horizontal
- ✔ croquis synthèse élève (390 px) : aucune erreur JavaScript
- ✔ croquis synthèse élève (390 px) : aucun défilement horizontal
- ✔ croquis synthèse élève (1280 px) : aucune erreur JavaScript
- ✔ croquis synthèse élève (1280 px) : aucun défilement horizontal
- ✔ croquis synthèse professeur (390 px) : aucune erreur JavaScript
- ✔ croquis synthèse professeur (390 px) : aucun défilement horizontal
- ✔ croquis synthèse professeur (1280 px) : aucune erreur JavaScript
- ✔ croquis synthèse professeur (1280 px) : aucun défilement horizontal

## Contrôles du dépôt

| Contrôle | Code | Dernière ligne |
|---|---|---|
| `controle_longueurs.py` | 0 | Aucune banque signalée. |
| `controle_hierarchie.py` | 0 | 3 page(s) lues · ✅ aucune énumération en ligne, aucun mur sans repère, aucun paragraphe tout en gras, aucune cellule-pavé, aucun item-pavé, aucun pavé hors séquence |
| `controle_regles_visibles.py` | 0 | ✅ aucune page lue par un élève ne laisse voir la fabrique (règle d'or n°309) |
| `controle_medias.py` | 0 | ✅ chaque image du dépôt a une provenance écrite, et aucune n'est promise en vain |
| `controle_liens.py` | 0 | ✅ aucun lien mort, aucune ancre introuvable dans le périmètre regardé |
| `verif_qcm_coherence.mjs` | 0 | ✅ qcm_croquis.html · 30 q · positions {"0":8,"1":7,"2":7,"3":8} · réfutations alignées |

## Non exécuté ici

- La relecture humaine des dessins (captures PNG regardées à la production, non rejouées par ce script).
- Les bancs des séquences qui accueillent des exercices insérés : ils se lancent dans le dossier de chaque séquence.
