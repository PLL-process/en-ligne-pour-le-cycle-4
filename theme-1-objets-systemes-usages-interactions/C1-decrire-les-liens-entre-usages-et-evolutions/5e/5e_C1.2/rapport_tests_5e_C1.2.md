# Rapport de tests — lot 5e_C1.2 « Sainte-Luce »

**Exécuté le 9 août 2026** · Chromium via Playwright · `python3 tests_5e_C1.2_sainte_luce.py`
**Résultat : 36 contrôles, 36 verts, aucune erreur JavaScript.**

Ne figurent ici que des tests **réellement exécutés**. La suite est livrée avec le lot.

## Périmètre déclaré (règle n°47)

**Vérifié** — les quatre verrous, fermés sur une page vide et ouverts sur une production complète ;
le **refus argumenté** du frein à patins en séance 3 ; la progression, la sauvegarde et sa
restauration ; la cible du bouton d'entraînement avant et après la séquence ; les deux blocs de la
règle n°4, corrigé du Bonus compris ; la mention de la manipulation obligatoire ; pour le QCM, le
titre **affiché** et son sous-titre, le nombre de questions et d'illustrées, la répartition des
bonnes réponses, la réfutation de chaque distracteur, la formulation du référentiel, l'ouverture
ciblée, le chargement effectif des images et le lien de retour.

**Non vérifié** — l'exactitude pédagogique des corrigés, le rendu à l'impression, l'ergonomie en
classe, et **la faisabilité de la manipulation sur le vélo**, qui se vérifie devant un vélo.

## Séquence — 19 contrôles

| Contrôle | Résultat |
|---|---|
| Les quatre verrous refusent une page vide | ✅ 4/4 |
| Les quatre verrous s'ouvrent sur une production complète | ✅ 4/4 |
| Le bouton QCM à zéro validation ouvre le parcours court | ✅ |
| **Le choix du frein à patins est refusé, et la raison chiffrée est donnée** | ✅ |
| La progression atteint 3 / 3 après remise d'une défense valable | ✅ |
| Le bouton QCM en fin ouvre le parcours complet | ✅ |
| Les zones de rédaction survivent à un rechargement | ✅ |
| La progression survit à un rechargement | ✅ |
| Bloc « Prêt·e à t'entraîner ? » présent (règle n°4) | ✅ |
| Bloc « Bonus » présent, et son corrigé | ✅ |
| La manipulation est annoncée comme obligatoire (règle n°58) | ✅ |
| Zéro erreur JavaScript | ✅ |

> Le contrôle du **refus argumenté** est nouveau dans le dépôt. Il ne vérifie pas seulement qu'une
> mauvaise réponse est rejetée, mais que le message **cite le chiffre** qui la disqualifie —
> « 8,9 m sous la pluie » — et renvoie au Bonus où le même choix devient le bon. Un refus qui
> n'aide pas l'élève à repartir n'est pas un vérificateur, c'est un mur.

## QCM — 17 contrôles

| Contrôle | Résultat |
|---|---|
| Titre **affiché** et sous-titre propres au lot (règle n°51) | ✅ |
| Aucune trace du lot d'origine du gabarit | ✅ |
| 30 questions, 8 illustrées | ✅ |
| Bonnes réponses réparties A/B/C/D — 8/7/7/8, graine 218 | ✅ |
| Chaque distracteur porte une réfutation de plus de 20 caractères | ✅ 90/90 |
| La réfutation de la bonne réponse est vide | ✅ 30/30 |
| Chaque question a explication, exemple, erreur classique et à-retenir | ✅ 30/30 |
| La formulation du référentiel est celle du texte officiel (règle n°42) | ✅ |
| `#depart=court` ouvre 10 questions, bandeau visible | ✅ |
| Les 8 images se chargent réellement | ✅ |
| Le lien de retour vers la séquence est présent et exact | ✅ |
| Clé de sauvegarde propre au lot | ✅ |
| Zéro erreur JavaScript | ✅ |

## Vérificateur de règles

`python3 _outils/verif_regles_audit.py` sur le dossier : **8 sur 8** — n°23 (150 min pour 165),
n°26, n°29 (mode essentiel), n°30 (tableau de bord), n°31 (4 versions étayées pour 9 zones),
n°33 (aération), n°34 (accessibilité), n°42 (formulation du référentiel).

**La règle n°67 est levée** : la page comptait **zéro** champ de saisie et annonçait trois fois une
production attendue. Elle en compte désormais **18 listes déroulantes et 9 zones de rédaction**.

## Deux incidents de production, sans conséquence sur le lot

Consignés parce qu'ils se répètent et qu'il faudra en tirer une règle.

1. **La banque de questions s'est d'abord écrite hors du dépôt**, un `cd` résiduel ayant déplacé le
   répertoire courant entre deux commandes. Récupérée et remise en place, pas réécrite. C'est la
   deuxième occurrence de la journée — la première concernait une entrée de journal.
2. **Le premier générateur a refusé d'écrire** en signalant des restes « 3e_C3 » : c'était le
   garde-fou de la règle n°51 qui faisait son travail, sur le titre affiché du gabarit que nous
   avions nous-mêmes corrigé la veille. Le contrôle avait raison.
