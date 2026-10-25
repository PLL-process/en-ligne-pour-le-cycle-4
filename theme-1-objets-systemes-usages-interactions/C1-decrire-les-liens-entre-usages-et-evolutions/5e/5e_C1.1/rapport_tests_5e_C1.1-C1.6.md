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

---

## 25/10/2026 — L'animation des trois principes (activité 1)

**Exécuté le 25 octobre 2026** · Chromium via Playwright (Python et Node) · espace de travail cloud.
Ne figurent ici que des tests réellement exécutés.

### Banc de l'animation — `python3 tests_animation_trois_principes.py` : **50 / 50**

| Contrôle | Résultat |
|---|---|
| Les 22 fichiers audio (11 Opus, 11 MP3) existent, de bonne forme, moins de 100 Ko | ✅ 11/11 |
| Les phrases dites (`phrases.json`) sont celles de la page, mot pour mot | ✅ |
| À l'écran : animation affichée, 3 schémas et 3 « À repérer » masqués, étapes des cartes visibles | ✅ 3/3 |
| À l'impression : animation masquée, schémas affichés | ✅ |
| À l'ouverture : aucun fichier audio demandé ni joué ; « Écouter » proposé | ✅ 2/2 |
| Onze étapes, chacune avec sa phrase ; description du dessin pour les étapes 1 à 10 ; boutons désactivés aux bornes ; finale | ✅ 4/4 |
| Les cinq chapitres mènent à leur étape et se marquent (`aria-current`) | ✅ |
| « Écouter » (étape 2), « Regarder » (étape 1 puis 2 à la fin de l'audio), « Pause » | ✅ 4/4 |
| Bouton « lentille » absent à l'étape 3 ; compteur qui monte à l'étape 4 ; lentille sale : il monte plus vite, la note s'affiche | ✅ 3/3 |
| Étape 5 : horloge de 0 h à 24 h, puis arrêt ; étape 6 : balance « après » à 100 020 µg ; étape 10 : jauge de « beaucoup » à « peu » | ✅ 3/3 |
| Finale : l'horloge tourne seule ; remise à 0 h ; P1 immédiat, P3 à l'heure, P2 à la journée (scénarios ci-dessous) | ✅ 7/7 |
| Mouvement réduit : grains immobiles avec un éclat montré ; horloge en attente d'un geste ; zéro erreur JS | ✅ 3/3 |
| 390 px : aucune des onze étapes ne fait défiler la page en largeur | ✅ |
| Lien direct `#trois-principes-pas-a-pas` depuis la séance 3 : séance 1 ouverte, animation à l'écran | ✅ |
| Sans Opus : le MP3 ; fichier refusé : la voix locale dit la phrase ; ni l'un ni l'autre : « lis les phrases » | ✅ 4/4 |
| Aucune ressource distante, zéro erreur JavaScript | ✅ |

**Scénarios de la finale, calculés à la main** (horloge en pause, bouton « + 1 h ») :
- curseur 40 → P1 = 40 µg/m³ tout de suite ; après 1 h, P3 = 40, P2 sans résultat ;
- 40 pendant 1 h, 20 pendant 11 h, 60 pendant 12 h → à 24 h : P2 = (40 + 220 + 720) / 24 = 40,8 → **41**, P3 = **60** ;
- puis 80 pendant 1 h → P3 = **80**, P2 garde **41** (moyenne de la veille).

**Ce que ce banc ne vérifie pas** : la qualité de la voix et sa prononciation (cela s'écoute) ; la clarté de l'animation pour
un élève (cela se voit en classe) ; Safari, iPad, téléphone réel.

### Bancs existants, rejoués

- `python3 tests_5e_C1.1_chengdu.py` : **43 / 43** (sortie 0).
- `node tests_regle_311_5e_C1.1.mjs` : **33 / 33** (sortie 0).

### Contrôles de `_outils/` (lancés depuis la racine, sur la branche)

| Outil | Sortie | Périmètre, remarque |
|---|---|---|
| `controle_atteignabilite.py`, `controle_banque_qcm.py`, `controle_blocs_dessines.py`, `controle_boutons_vivants.py`, `controle_cadres.py`, `controle_couverture.py`, `controle_echantillonnage.py`, `controle_effectifs_qcm.py`, `controle_entete_qcm.py`, `controle_fichiers_telechargeables.py`, `controle_formulations.py`, `controle_gestes_outil.py`, `controle_hierarchie.py`, `controle_longueurs.py`, `controle_marqueurs.py`, `controle_navigation_seances.py`, `controle_rapports_tests.py` | 0 | dépôt entier |
| `controle_liens.py` | 0 | aucun lien mort, aucune ancre introuvable (le lien du README vers `#trois-principes-pas-a-pas` compris) |
| `controle_medias.py` | 0 | provenance de chaque image, captures de la PR comprises |
| `controle_regles_visibles.py` | 0 | n°309 : aucune trace de fabrique dans ce que lit l'élève |
| `controle_debordement.py` | 0 | 194 pages lues |
| `controle_regle4.py` | 1 | **préexistant** : 18 ateliers des représentations refusés ; sortie identique sur `main` (comparée ligne à ligne) |
| `verif_regles_audit.py` (dossier du lot) | 0 | 1 ✘ n°298 (référentiel en toutes lettres) : **préexistant**, même résultat sur `main` |
| `controle_contraste_liens.mjs`, `controle_hors_ligne.mjs`, `controle_impression.mjs`, `controle_squelette.mjs` | 0 | dépôt entier |
| `controle_verrous.mjs` | 0 | 118 pages à verrous ouvertes dans un contexte neuf ; l'animation ne pose aucun verrou |

**Non exécutés** : validation HTML (aucun outil du dépôt) ; parcours au clavier seul rejoué touche par touche (les commandes
sont des boutons natifs) ; écoute des prises.
