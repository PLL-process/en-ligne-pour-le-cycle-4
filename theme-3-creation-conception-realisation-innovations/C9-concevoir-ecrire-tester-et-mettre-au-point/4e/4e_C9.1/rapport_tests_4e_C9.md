# Rapport de tests — Lot 4e_C9 « Le jardin connecté se programme »

Date : 2026-08-26 (**réécriture complète** ; v1 : 2026-07-25, agent Grok) ·
Agent : Fable · Environnement : Chromium headless (Playwright 1.55),
viewport 1280×900 + émulation téléphone 390×844 · Suite : `tests_4e_C9.mjs`
(committée dans ce dossier, rejouable : `node tests_4e_C9.mjs .`).

> **Mise à jour du 31/10/2026 — règle d'or n°311 : à partir de la séance 2, l'élève voit sa séance, pas le décor.**
> À la séance 1, l'ouverture est complète (la barre d'outils passe juste sous la mission, la progression juste après l'ouverture).
> À partir de la séance 2 : titre, mission, barre d'outils, sélecteur de parcours, puis le volet replié « 📖 Rappel : la situation
> et ton hypothèse » (étiquettes, « Avant de commencer », billet d'entrée, identité, note du mode essentiel, situation, problématique,
> hypothèse, façons de vivre la séquence). Restent dehors, parce que ce sont des outils des séances 2 et 3 : la progression,
> « 🗺 Où en suis-je ? » et « 🧪 Le banc d'essai du jardin ». Le lien direct `#pompe-pas-a-pas` ouvre toujours la séance 3.
> Banc `tests_regle_311_4e_C9.1.mjs` (relais du thème 3, puis banc commun du thème 1) : **9 / 9 + 34 / 34**.
> Suite du lot rejouée après le volet : `node tests_4e_C9.mjs .` → **77 / 77**, comme avant.


> **Correction du 31/08/2026 — le verrou expérientiel s'ouvrait en partie au chargement.**
> `_outils/controle_verrous.mjs`, écrit ce jour-là, ouvre chaque séquence du dépôt dans un
> navigateur **neuf** et lit `window.__exp` juste après le chargement. Cette page en portait
> déjà `vuSec` **avant tout geste** : la fonction d'affichage du banc était appelée à
> l'initialisation, et elle enregistrait ce qu'elle affichait. Le verrou « j'ai fait varier l'humidité » exige d'avoir vu la pompe des DEUX côtés du seuil : il n'en attendait plus qu'un. La fonction ne trace plus que
> sur un geste ; vérifié après correction : `__exp` est **vide** à l'ouverture, et le verrou
> s'ouvre normalement dès les manipulations réelles (règles d'or n°226 et n°265).
La suite **simule la séquence comme un élève** et prend une capture d'écran à
chaque action (23 captures). Elle ne déclare que ce qu'elle exécute.

## 1. Tests automatisés exécutés — 60/60 réussis

### La démonstration centrale : un seuil contre deux seuils

C'est le test dont dépend toute la séance 3. Il exécute la démonstration **comme
un élève la fera**, avec le même tremblement de mesure dans les deux modes.

| Test | Résultat |
|---|---|
| Banc : en **UN seuil**, la mesure qui tremble affole la pompe | ✅ 8 basculements |
| Banc : en **DEUX seuils**, le **même** tremblement n'affole plus la pompe | ✅ 0 basculement |
| La démonstration est probante (au moins 4 basculements évités) | ✅ 8 → 0 |

> Le tremblement est une suite de valeurs **figée dans le code**
> (41, 39, 41, 40, 39, 40, 39, 41, 40, 39, 41, 40), pas un tirage aléatoire.
> Sans cela, la comparaison entre les deux modes ne prouverait rien : on
> comparerait deux mesures différentes. C'est aussi ce qui rend la démonstration
> **reproductible d'un poste à l'autre** — un élève qui la rejoue obtient
> exactement les mêmes nombres, et peut donc les inscrire dans son compte rendu.

### Le banc d'essai — le comportement, valeur par valeur

| Entrées | Attendu | Résultat |
|---|---|---|
| H = 25 %, 8 h | POMPE ON | ✅ |
| H = 55 %, 8 h | POMPE OFF | ✅ |
| H = 25 %, **23 h** | POMPE OFF — le ET exige les deux conditions | ✅ |
| H = **39 %**, 7 h | POMPE ON (frontière basse) | ✅ |
| H = **40 %** pile, 7 h | POMPE OFF — `40 < 40` est **faux** | ✅ |

### Les verrous : la page refuse de valider ce qui n'a pas été fait

| Test | Résultat |
|---|---|
| Act. 1 refusée tant que la justification écrite manque | ✅ |
| Act. 3 refusée tant que le journal ne cite pas de **valeurs** (3 nombres exigés) | ✅ |
| Act. 3 refusée tant que les essais au banc ne sont pas faits | ✅ |
| Act. 4 refusée tant que les deux frontières ne sont pas exécutées au banc | ✅ |
| Act. 5 refusée tant que la démonstration au banc n'est pas jouée dans les deux modes | ✅ |
| Act. 6 refusée tant que le programme du lampadaire n'a pas **deux seuils distincts** | ✅ |

### Le parcours élève, de bout en bout

| Test | Résultat |
|---|---|
| Chargement `file://` sans erreur JS (début et fin de parcours) | ✅ |
| Billet d'entrée : feedback affiché, **déclaré hors progression**, et la progression reste à 0 | ✅ |
| Tableau de bord : les 6 activités listées, puis les 6 cochées en fin de parcours | ✅ |
| Activités 1 à 6 validées avec leurs vérificateurs exacts | ✅ |
| Progression 6/6 · les 3 séances cochées ✔ | ✅ |
| Rappel de l'hypothèse de départ affiché au bilan | ✅ |
| **Sauvegarde / restauration** après rechargement : progression, réponses, verrous du banc | ✅ |
| Zéro lien local cassé | ✅ |
| Mobile 390 px : aucun défilement horizontal (débord = 0), zéro erreur JS | ✅ |

### Les règles d'or vérifiables à l'écran

| Règle | Vérification | Résultat |
|---|---|---|
| n°4 | un **seul** bouton QCM dans la séquence | ✅ |
| n°29 | le mode essentiel masque réellement le référentiel | ✅ |
| n°92 | la loupe ouvre l'image en grand, Échap referme | ✅ |
| n°101 | 2 boutons « séance suivante », et le clic bascule vraiment | ✅ |
| n°117 | chaque figure a un `alt` ≥ 120 caractères **et** une description dépliable rattachée par `aria-describedby` | ✅ |
| n°122 | sélecteur de parcours actif ; choisir 🅲 masque les blocs 🅱 **sans retirer aucune question** | ✅ |

### QCM

| Test | Résultat |
|---|---|
| 30 questions · **10 par code** (C9.1 / C9.2 / C9.3) · 4 illustrées | ✅ |
| Bonnes réponses réparties A/B/C/D = **8/7/7/8** | ✅ |
| `d[r]` vide et 3 réfutations non vides sur **chacune** des 30 questions | ✅ |
| Chaque question porte explication, exemple, erreur fréquente et à-retenir | ✅ |
| Correction complète affichée · question illustrée · marquage 🔖 | ✅ |
| Révision ciblée 4e_C9.3 = 10 questions · mode « mes erreurs » = 1 | ✅ |
| Scénario 30/30 → **20,0 /20 · 100 %** · bilan à 3 lignes maîtrisées | ✅ |
| Scénario 15 justes / 15 fausses → **10,0 /20 · 50 %** | ✅ |
| Scénario 6 justes, 6 fausses, 18 non répondues → **4,0 /20 · 18 NR** | ✅ |
| Zéro erreur JS sur tout le parcours | ✅ |

## 2. Contrôles statiques

- **Règles d'or mécanisées** (`python3 _outils/verif_regles_audit.py …/4e_C9.1/`) :
  **0 manquement**, et **aucune alerte**. La v1 en comptait **cinq** — n°23 (aucune
  durée annoncée), n°26 (pas de diagnostic d'entrée), n°29 (pas de mode essentiel),
  n°30 (5 tâches sans tableau de bord), n°31 (6 zones de rédaction, aucune version
  étayée), n°34 (16 champs sans étiquette).
- **n°42 — formulations du référentiel** : les 3 formulations de la carte sont
  celles du programme, **au mot près**. C'est ce contrôle qui a révélé l'erreur de
  fond du lot (voir §4).
- **Poids des médias** : 4 SVG originaux de 7 à 9 Ko. `<title>` et `<desc>`
  accessibles dans chacun.
- **Matrice de couverture** : 31 lignes, 8 colonnes normalisées ; les 30 questions
  du QCM sont rattachées à une notion enseignée.
- **Aucun envoi réseau** : sauvegardes localStorage uniquement
  (`seq_4e_C9_jardin-connecte` / `qcm_4eC9_jardin-connecte`). Seul l'`iframe`
  Vittascience sort, et son absence est prévue.

## 3. Contrôles restant manuels (non exécutés — à faire par un humain)

- la version 🅰 (matériel réel, téléversement) n'existe plus depuis le 05/10/2026 : plus
  de test au labo à prévoir ;
- **accès réseau** : vérifier que `fr.vittascience.com` n'est pas filtré par le
  réseau du collège avant la séance 2 (sinon, le banc d'essai prend le relais) ;
- test sur appareils réels (tablette, téléphone) — seul le viewport a été émulé ;
- relecture orthotypographique humaine ; rendu GitHub Pages après publication.

## 4. Ce que la campagne a trouvé

**Une erreur de fond, héritée de la v1 : les mauvais verbes en face des codes.**
Le lot annonçait « concevoir » pour 4e_C9.1 et « réinvestir » pour 4e_C9.3. Le
programme 2024 dit **modifier**, **traduire**, **réaliser et mettre au point** — et
« concevoir » est un verbe de **3e**. Ce n'est pas un détail de rédaction : cela
change ce qu'on demande à l'élève. « Modifier » interdit la page blanche, et
impose de fournir l'algorithme amputé d'une exigence.

Ce défaut est resté invisible pendant un mois parce qu'il ne se voit ni à l'écran,
ni à l'exécution : la page fonctionnait parfaitement. Il a fallu un contrôle qui
compare **mot à mot** la carte de référentiel au texte officiel (règle n°42) pour
qu'il apparaisse.

**Deux défauts de lisibilité**, trouvés en cours de campagne :

1. Le verrou « avoir fait varier l'humidité » comptait le **nombre de valeurs
   touchées** (six distinctes). Un élève qui saisit directement 25 puis 55 dans le
   champ de valeur exacte n'en touchait que deux, et restait bloqué sans comprendre
   pourquoi. Remplacé par une exigence qui a du sens : **avoir vu la pompe des deux
   côtés du seuil**.
2. Dans l'encadré des trois niveaux (lot 3e, corrigé au passage), les trois bords
   colorés sortaient tous de la même couleur : `.trois-niveaux .niv` (deux classes)
   l'emportait sur `.niv-mesure` (une seule). Invisible à l'œil sur fond sombre ;
   trouvé par un test qui **compare les trois couleurs entre elles**.

## 5. Échecs

Aucun test exécuté en échec au moment de la remise (60/60). La suite complète a été
rejouée intégralement, pas seulement les tests ajoutés.

## 6. Rejouée le 05/10/2026 (lot des gestes, mode mixte conservé)

La suite a été **rejouée après le lot du 05/10/2026** : **66 / 66** (61 avant le lot). Le contrôle « sélecteur de parcours » compte
désormais **trois** boutons (🅱, 🅲, tout afficher) au lieu de quatre, et **cinq contrôles** sont ajoutés, préfixés « gestes » : l'unique
lien-bouton garde l'éditeur en `?mode=mixed` ; plus de version 🅰 (ni bouton, ni carte, ni « matériel réel ») ; la consigne de l'activité 3
dit « Nomme ton projet 4e-JARDIN-TON NOM, puis télécharge-le (geste 4) » ; les douze captures de l'encart se chargent avec un texte
alternatif ; un ancien choix « a » mémorisé retombe sur « tous ». Le contenu de Vittascience (blocs, Python, réouverture du fichier)
a été mesuré à la main avec le programme exact de l'activité 3 et n'est pas rejoué ici : service externe.

## 7. Rejouée le 05/10/2026 (phrase ajoutée à l'activité 3)

La consigne de l'activité 3 porte maintenant « Dans le volet Python, change seulement ce que la consigne demande. Le reste, fais-le avec les blocs. » : elle limite ce qu'on tape dans le volet Python, pour que le programme reste traduisible en blocs. Un contrôle ajouté : **67 / 67** (66 avant).


## 8. Rejouée le 19/10/2026 (relecture pour le distanciel)

**Ce que la relecture a trouvé, et que la suite ne voyait pas.** La suite choisissait les bonnes réponses par leur **rang**
(`{ index: 1 }`) : elle passait parce que la bonne réponse était **toujours la première** — 23 menus vérifiés sur 23, et 22 fois la
plus longue. Elle validait aussi l'activité 6 avec « le sens », la réponse attendue par la page, alors que l'aide de niveau 2 et la
correction disaient que le sens ne s'inverse pas.

**Ce qui change dans la suite.** Les réponses sont choisies par leur **texte** (table `BONNE`), et trois contrôles sont ajoutés :
chaque bonne réponse existe dans son menu ; elle n'est en tête que dans moins d'un tiers des menus (5 / 22) ; aucune n'est détachée
par sa longueur de plus de 8 caractères (même seuil que `controle_longueurs.py`, règle n°198). **Résultat : 70 / 70** (67 avant).

**Mutation, elle mord** : la bonne réponse de `a5_q4` remise à sa formulation d'avant (« RIEN : la pompe garde son état précédent, et
c'est exactement ce qui supprime le clignotement ») → le contrôle de longueur échoue et nomme `a5_q4` (exécuté sur une copie du lot).

Non rejoué ici : le lexique régénéré (48 mots par séance) est vérifié par `generer_lexique.py` lui-même (formes présentes dans leur
panneau, sources présentes, aucun conflit avec un « à retenir ») et par le banc de l'outil, dans le dossier des outils du dépôt (28 / 28).

## 9. Rejouée le 30/10/2026 (l'animation « la pompe qui s'affole »)

L'activité 5 b) porte une animation pas à pas (bloc `#pompe-pas-a-pas`, neuf étapes) à la place du chronogramme fixe, qui reste
dans un volet replié dessous et s'imprime à sa place. **Résultat : 77 / 77** (70 avant) : `node tests_4e_C9.mjs . <dossier_captures>`.
Les sept contrôles ajoutés, préfixés « animation » :

| Test | Résultat |
|---|---|
| 9 étapes, et ses 18 fichiers de voix (`Audio/pompe_etape1…9`, .ogg et .mp3) | ✅ |
| « Regarder » s'arrête à la prédiction (étape 6) tant que l'élève n'a pas répondu (voix remplacée par un fichier qui finit tout de suite) | ✅ |
| La réponse mène à l'étape 7, qui rappelle la prédiction | ✅ |
| Un seul seuil : 6 basculements, et la console finit sur « 10:32:12  H=41  POMPE OFF », la dernière ligne de la trace (étape 3) | ✅ |
| Deux seuils : 0 basculement sur la même trace (étape 7), puis 1 quand le sol passe sous 35, console « 10:32:42  H=34  POMPE ON » (étape 8) | ✅ |
| À l'impression, l'animation se retire et le chronogramme fixe s'imprime (son volet s'ouvre) | ✅ |
| Zéro erreur JavaScript | ✅ |

**Mutation, elle mord** : sur une copie du lot où la prédiction n'arrête plus « Regarder », le contrôle de la prédiction échoue
(« Étape 9 / 9 » au lieu de « Étape 6 / 9 »).

**Le reste n'est pas propre à ce lot** et tourne ailleurs : le banc commun `_outils/lecteur_pas_a_pas/banc_lecteur.py` parcourt
l'animation à 1280 et 390 px et sous « mouvement réduit », vérifie la voix sur le disque, l'impression et le lien direct
`#pompe-pas-a-pas` (vert, 5 animations) ; `_outils/controle_lecteur_pas_a_pas.py` vérifie que le lecteur posé est celui de la source.
**Non vérifié** : l'écoute des neuf prises (à faire par Pascal) ; Safari, iPad, téléphone réel.

