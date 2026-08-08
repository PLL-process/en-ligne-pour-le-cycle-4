# Rapport de tests — lot 5e_C1.1 à C1.6 « Chengdu »

**Exécuté le 8 août 2026** · Chromium via Playwright · `python3 tests_5e_C1.1_chengdu.py`
**Résultat : 43 contrôles, 43 verts, aucune erreur JavaScript.**

Ne figurent ici que des tests **réellement exécutés**. La suite est livrée avec le lot : elle se
rejoue en une commande.

## Périmètre déclaré (règle n°47)

**Ce que cette suite vérifie** — les six verrous de la séquence, fermés sur une page vide et ouverts
sur une production complète ; la progression ; la sauvegarde et sa restauration après rechargement ;
la cible du bouton d'entraînement aux trois moments prévus ; la présence des deux blocs de la
règle n°4, corrigé du Bonus compris ; pour le QCM : le titre **affiché** et son sous-titre, le
nombre de questions, la répartition des bonnes réponses, la réfutation de chaque distracteur, le
filtre par compétence, l'ouverture ciblée, le chargement effectif des images, l'absence d'erreur JS.

**Ce qu'elle ne vérifie pas, et qui reste à l'œil** — l'exactitude pédagogique des corrigés et des
explications ; le rendu à l'impression ; l'ergonomie réelle en classe. La conformité des
formulations du référentiel est couverte ailleurs, par `_outils/verif_regles_audit.py` (règle n°42).

## Séquence — 22 contrôles

| Contrôle | Résultat |
|---|---|
| Les six verrous refusent une page vide (checks 0 à 5) | ✅ 6/6 |
| Les six verrous s'ouvrent sur une production complète | ✅ 6/6 |
| La progression atteint 5 / 5 activités validées | ✅ |
| Le bouton QCM à zéro validation ouvre le parcours court | ✅ |
| Le bouton QCM à mi-parcours ouvre `#codes=C1.2,C1.1` | ✅ |
| Le bouton QCM en fin ouvre le parcours complet | ✅ |
| Les zones de rédaction survivent à un rechargement | ✅ |
| La progression survit à un rechargement | ✅ |
| Bloc « Prêt·e à t'entraîner ? » présent (règle n°4) | ✅ |
| Bloc « Bonus » présent (règle n°4) | ✅ |
| Corrigé du Bonus présent — lu par `textContent` | ✅ |
| Zéro erreur JavaScript | ✅ |

> Le corrigé du Bonus se lit par `textContent` et non par `inner_text` : un `<details>` replié ne
> rend que son `<summary>`. C'est la cinquième fois que ce piège se présente dans le dépôt ; le
> commentaire est dans le fichier de tests.

## QCM — 21 contrôles

| Contrôle | Résultat |
|---|---|
| Titre **affiché** et sous-titre propres au lot (règle n°51) | ✅ |
| Aucune trace du lot d'origine du gabarit dans la page | ✅ |
| 30 questions, 13 illustrées | ✅ |
| Bonnes réponses réparties A/B/C/D — 8/7/7/8, graine 512 | ✅ |
| Chaque distracteur porte une réfutation de plus de 20 caractères | ✅ 90/90 |
| La réfutation de la bonne réponse est vide | ✅ 30/30 |
| Les six codes présents, filtre par compétence complet | ✅ |
| `#codes=C1.2,C1.1` ouvre 11 questions, mode « cible », bandeau visible | ✅ |
| `#depart=court` ouvre 10 questions | ✅ |
| Un code inconnu est ignoré, le QCM reste complet, bandeau caché | ✅ |
| La progression enregistrée survit au retour depuis la séquence | ✅ |
| Les 13 images se chargent réellement | ✅ |
| Clé de sauvegarde propre au lot | ✅ |
| Zéro erreur JavaScript | ✅ |

## Vérificateur de règles

`python3 _outils/verif_regles_audit.py` sur le dossier du lot : **8 contrôles sur 8 verts** pour la
séquence — n°23 (durée), n°26 (diagnostic), n°29 (mode essentiel), n°30 (tableau de bord), n°31
(versions étayées : 10 pour 13 zones), n°33 (aération), n°34 (accessibilité), n°42 (les six
formulations du référentiel sont celles du texte officiel).

## Trois contrôles ont été rouges — les trois fois, c'était le contrôle

Consigné parce que la règle n°50 s'est appliquée trois fois dans la même journée.

1. **`#codes=` semblait sans effet.** Changer seulement le fragment d'une adresse **ne recharge pas
   la page** : le code d'ouverture ne rejouait pas. Le test appelle désormais `reload()`.
2. **Le cas du code inconnu échouait.** Il mesurait en réalité la restauration de l'essai précédent,
   faute d'avoir vidé la sauvegarde. Corrigé — et le piège a produit un contrôle de plus, celui qui
   vérifie qu'un élève qui revient ne perd pas ce qu'il avait commencé.
3. **Les schémas des synthèses semblaient introuvables.** `fetch()` est bloqué sur `file://`, et
   `contentDocument` est nul d'une origine à l'autre. Les SVG se chargeaient parfaitement : on mesure
   maintenant la hauteur rendue et l'étiquette accessible, qui sont observables depuis la page hôte.

Un seul défaut réel a été trouvé et corrigé pendant cette phase : le générateur du QCM appelait
`rendre()`, qui n'existe pas — la fonction s'appelle `rendreTout()`.
