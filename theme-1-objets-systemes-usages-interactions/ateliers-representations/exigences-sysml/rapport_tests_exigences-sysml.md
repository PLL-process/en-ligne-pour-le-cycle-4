# Rapport de tests — atelier « Le diagramme des exigences »

Écrit le 2026-10-24 par `_generation/gouvernance.py`, **à partir des exécutions faites à l'instant** : rien n'y est déclaré qui n'ait tourné (règle d'or n°299 : un contrôle qui n'a rien vérifié est en panne).

## Banc de l'atelier (`banc_ateliers.py exigences`, Chromium, 390 px)

Code de sortie : **0** — 37 / 37 tests passés

- ✔ exigences-sysml 4e : aucune erreur JavaScript au chargement
- ✔ exigences-sysml 4e : aucun défilement horizontal à 390 px
- ✔ exigences-sysml 4e : un onglet par exercice, plus la clôture (4)
- ✔ exigences-sysml 4e · e1 : « Vérifier » à vide donne un retour à reprendre
- ✔ exigences-sysml 4e · e1 : rempli juste, « Tout est juste »
- ✔ exigences-sysml 4e · e2 : « Vérifier » à vide donne un retour à reprendre
- ✔ exigences-sysml 4e · e2 : rempli juste, « Tout est juste »
- ✔ exigences-sysml 4e · e3 : « Vérifier » à vide donne un retour à reprendre
- ✔ exigences-sysml 4e · e3 : rempli juste, « Tout est juste »
- ✔ exigences-sysml 4e : la sauvegarde locale du premier exercice existe
- ✔ exigences-sysml 4e : le premier exercice est noté réussi après rechargement
- ✔ exigences-sysml 4e : aucune erreur JavaScript pendant le parcours
- ✔ exigences-sysml 3e : aucune erreur JavaScript au chargement
- ✔ exigences-sysml 3e : aucun défilement horizontal à 390 px
- ✔ exigences-sysml 3e : un onglet par exercice, plus la clôture (4)
- ✔ exigences-sysml 3e · e4 : « Vérifier » à vide donne un retour à reprendre
- ✔ exigences-sysml 3e · e4 : rempli juste, « Tout est juste »
- ✔ exigences-sysml 3e · e5 : « Vérifier » à vide donne un retour à reprendre
- ✔ exigences-sysml 3e · e5 : rempli juste, « Tout est juste »
- ✔ exigences-sysml 3e · e6 : « Vérifier » à vide donne un retour à reprendre
- ✔ exigences-sysml 3e · e6 : rempli juste, « Tout est juste »
- ✔ exigences-sysml 3e : la sauvegarde locale du premier exercice existe
- ✔ exigences-sysml 3e : le premier exercice est noté réussi après rechargement
- ✔ exigences-sysml 3e : aucune erreur JavaScript pendant le parcours
- ✔ exigences-sysml QCM (390 px) : aucune erreur JavaScript
- ✔ exigences-sysml QCM (390 px) : aucun défilement horizontal
- ✔ exigences-sysml QCM : 30 questions
- ✔ exigences-sysml QCM (1280 px) : aucune erreur JavaScript
- ✔ exigences-sysml QCM (1280 px) : aucun défilement horizontal
- ✔ exigences-sysml synthèse élève (390 px) : aucune erreur JavaScript
- ✔ exigences-sysml synthèse élève (390 px) : aucun défilement horizontal
- ✔ exigences-sysml synthèse élève (1280 px) : aucune erreur JavaScript
- ✔ exigences-sysml synthèse élève (1280 px) : aucun défilement horizontal
- ✔ exigences-sysml synthèse professeur (390 px) : aucune erreur JavaScript
- ✔ exigences-sysml synthèse professeur (390 px) : aucun défilement horizontal
- ✔ exigences-sysml synthèse professeur (1280 px) : aucune erreur JavaScript
- ✔ exigences-sysml synthèse professeur (1280 px) : aucun défilement horizontal

## Contrôles du dépôt

| Contrôle | Code | Dernière ligne |
|---|---|---|
| `controle_longueurs.py` | 0 | Aucune banque signalée. |
| `controle_hierarchie.py` | 0 | 3 page(s) lues · ✅ aucune énumération en ligne, aucun mur sans repère, aucun paragraphe tout en gras, aucune cellule-pavé, aucun item-pavé, aucun pavé hors séquence |
| `controle_regles_visibles.py` | 0 | ✅ aucune page lue par un élève ne laisse voir la fabrique (règle d'or n°309) |
| `controle_medias.py` | 0 | ✅ chaque image du dépôt a une provenance écrite, et aucune n'est promise en vain |
| `controle_liens.py` | 1 |        → atelier_3e_C7.1_planification_taches.html |
| `verif_qcm_coherence.mjs` | 0 | ✅ qcm_exigences-sysml.html · 30 q · positions {"0":8,"1":7,"2":7,"3":8} · réfutations alignées |

## Non exécuté ici

- La relecture humaine des dessins (captures PNG regardées à la production, non rejouées par ce script).
- Les bancs des séquences qui accueillent des exercices insérés : ils se lancent dans le dossier de chaque séquence.
