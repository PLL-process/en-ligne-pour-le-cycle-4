---
name: banc-essai-programme
description: Vérifier une activité où l'élève modifie ou écrit un programme dans la page (CodeLab, éditeur Python intégré, banc-eleve) en EXÉCUTANT son programme sur des entrées choisies et en comparant ses sorties au cahier des charges — jamais en cherchant des mots dans son texte ; la version du programme toujours dite ; la prévision écrite avant l'essai ; un essai périmé dès que le code change ; une limite de l'outil jamais présentée comme une erreur de l'élève. Règles d'or n°333 (mesurée par `controle_verification_execute.py`), n°373 et n°374 (en essai). À utiliser sur toute séquence C6, C9 ou C8 qui fait programmer dans la page, à chaque audit d'une telle séquence, et avant d'écrire un nouvel exécuteur.
---

# Un banc d'essai juge ce que fait le programme

Né le 22/11/2026 des deux audits de « Programmer l'alerte » (`3e_C6.1`). Le bouton « Vérifier » de l'activité 4
cherchait sept motifs dans le texte du programme : la version juste écrite avec des apostrophes obtenait 5 / 7 et le
message « branches incomplètes » ; la même avec `>=` au seuil de 118, fausse précisément à la frontière que la séquence
apprend à tester, obtenait 7 / 7. L'activité 5 donnait « maîtrisé » à sept prévisions justes sur la version 2 alors que
la version 1 était restée dans l'éditeur. Les documents mélangeaient les versions (un algorigramme à 50 après la
consigne qui fixe 60). Rien de tout cela n'était nouveau dans les règles : la n°333 le disait depuis le 14/11. La page
était antérieure à la règle, et aucun outil ne la mesurait.

## 0. Avant d'écrire quoi que ce soit : chercher l'outil du dépôt

- **L'éditeur Python commun** (`_ressources-communes/editeur-python/`, Skulpt 1.2.0, depuis le 04/11/2026) exécute un
  vrai Python, hors ligne : `EditeurPython.executer(code, {simulation, entrees})` → `Promise<{sortie, erreur, arret}>`,
  et l'événement `editeur-py:fin` après chaque ▶. C'est l'outil par défaut pour juger un programme (modèles : 5e_C9.1,
  `jugerBarr` ; 3e_C9.1, la preuve rangée dans `window.__exp`).
- **Le banc-python** (`_outils/banc_python/`, posé par `poser.py`) : un sous-ensemble du Python du collège, synchrone,
  qui rend la trace des tests évalués (« 118 > 118 → faux ») pour un chemin suivi pas à pas. Il a été écrit pour
  `3e_C6.1` sans avoir consulté l'éditeur commun d'abord — erreur de méthode, dite au journal. **Décision du
  22/11/2026** (carte blanche de Pascal) : on garde les deux, l'éditeur commun par défaut, le banc-python seulement pour
  le pas à pas ou la vérification instantanée du Python du collège ; garde-fou : le banc et CPython donnent les mêmes
  sorties sur les programmes du lot (`tests_banc_python.mjs`, test 20). Détail : `_outils/banc_python/LISEZMOI.md`.
- **Le banc-eleve** (`_outils/banc_eleve/`, 25/11/2026) : le chemin le plus court quand l'élève ÉCRIT dans l'éditeur
  commun. La page déclare une table `BANC_ELEVE` (les essais, leurs attendus, comment lire la sortie) ; le cœur, recopié
  à l'identique depuis la source (`poser.py --verifier-tout`), rejoue le programme après chaque ▶, écrit le premier
  écart sous l'éditeur, garde l'empreinte, retire la validation à la frappe. Dans `CHECKS` : `exp: beOk("vs1"),
  expMsg: beMsg("vs1")`. Modèles : `3e_C7.1` (une variable remplacée), `4e_C6.2` (une carte simulée par essai, un
  programme `while True` arrêté par la fin des mesures). Détail : `_outils/banc_eleve/LISEZMOI.md`.
- La leçon générale : un audit qui propose un outil (« Skulpt, à prototyper ») propose parfois ce que le dépôt a déjà.
  Chercher dans `_outils/`, `_ressources-communes/` et le journal (`grep -n "<outil>" JOURNAL_DES_DECISIONS.md`) avant
  de construire, et avant de numéroter une règle (`python3 _outils/registre_regles.py --prochain`, puis lire les
  règles voisines : la n°333 couvrait déjà deux des trois règles qu'on allait écrire).

## 1. Une spécification par version (n°373)

1. Nommer chaque version du programme que la séquence fait vivre : « version 1 d'origine », « version 1 recalibrée »,
   « version 2 ». Les écrire une fois, en tête de la séance qui les introduit.
2. Une seule table par version (le cahier des charges : entrée → message, actionneurs) nourrit **tout** : le schéma
   (algorigramme, plan de tests), les attendus du banc (`SPECS` dans la page), le code de la correction, le QCM.
3. Chaque document dit sa version dans son titre ou sa légende ; un plan de tests « de la v1 » ne commande que ce que
   la v1 commande.
4. Les lectures d'une version précise (« à quelle ligne… ») se font sur cette version **figée** (un listing qui ne
   bouge pas), jamais dans l'éditeur que l'élève modifie : un commentaire ajouté en tête ne décale plus la réponse.
5. L'éditeur dit en permanence la version qu'il contient, reconnue par son comportement : on l'essaie sur les vents du
   banc contre chaque spécification (`versionDe`, `3e_C6.1`) ; sinon « ta version modifiée ».

## 2. Exécuter, comparer, nommer le premier écart (n°333)

1. Choisir les entrées : sous, à et au-dessus de chaque seuil (n°351), entiers si la grandeur l'est (dire la
   résolution : « vent mesuré en km/h entiers »). `3e_C6.1` : 55, 59, 60, 61, 89, 90, 91, 117, 118, 119.
2. Simuler les fonctions de la maquette (capteurs, envoi, actionneurs) et relever les sorties : message, chaque
   actionneur. Chaque essai part du repos.
3. Comparer à la spécification ; verdict = tous conformes. Le message dit le nombre (« 9 / 10 vents conformes ») et le
   **premier écart en clair** : « 118 km/h · niveau : rouge attendu, violette obtenu · gyrophare : arrêté attendu, actif
   obtenu ». Jamais la ligne à corriger : un lien « 🔎 voir le chemin suivi à ce vent ».
4. Un paramètre se lit par sa **valeur** dans le programme exécuté (`60.5` n'est pas 60 ; `"60"` est un texte), puis
   son effet s'essaie (55 et 61 km/h).
5. Un motif dans le texte n'est permis que pour un **conseil de forme** annoncé comme tel, dans une fonction dont le
   nom commence par `conseil` (« 💡 Conseil de forme, il ne compte pas : un test écrit 118 au lieu de SEUIL_… »).
6. Une erreur de Python se dit avec son nom et sa ligne (`IndentationError`, `NameError` d'une variable sans valeur au
   repos), et la version se dit « contient une erreur ».

## 3. Prévoir avant d'essayer (n°374)

1. Trois cases, dans l'ordre : **prévision** (écrite avant, d'après le cahier des charges), **observation** (le
   programme ACTUEL exécuté), **conclusion** (conforme, ou l'écart).
2. Le bouton du banc reste fermé tant que les prévisions manquent (`banc5Verrou`).
3. Trois comptes séparés : « Mes prévisions : 6 / 6 », « Diagnostic : 2 / 2 », « Essais de ma version : à exécuter »
   puis « 10 / 10 conformes ». Une prévision juste ne valide jamais un programme.
4. Le journal d'essai garde chaque essai avec sa version ; le bilan peut en citer une ligne (« 118 km/h · attendu
   rouge · obtenu violette »).

## 4. Un code modifié périme l'essai (n°333)

Chaque vérification réussie mémorise l'empreinte du programme (`BancPython.empreinte(code)`, 8 caractères). Une frappe
qui change l'empreinte retire la validation et le dit (« à rejouer : ton programme a changé depuis l'essai »). La
barre de progression suit.

## 5. Dire les limites de l'outil (n°340, n°146)

- Une écriture Python juste que l'outil ne lit pas n'est **jamais** une « SyntaxError » : « limite du banc, pas
  forcément une erreur de ton programme », et un chemin (« essaie-le dans Python sur ordinateur : le Bonus donne le
  fichier `.py` », ou « écris cette ligne avec les écritures du cours »).
- Jouer l'outil sur des variantes justes avant de livrer : apostrophes, `== True` / `is True`, f-string, `a if c else
  b`, `;`, `print` de débogage, tabulations, parenthèses autour du test. Banc : `tests_banc_python.mjs` 17 à 19.
- Une simulation le dit : « 🧪 Simulation scolaire : vents inventés, seuils du club, aucun vrai capteur ».

## 6. Le chemin suivi, pas à pas

Après un écart (ou à la demande), montrer la trace : chaque test avec ses valeurs (« ligne 12 · if vent_kmh >
SEUIL_OURAGAN → 118 > 118 → faux : on passe à la suite »), puis les affectations et les appels. Boutons ⏮ ◀ « Pas
suivant ▶ » « Tout » ; rien d'essentiel ne repose sur le mouvement seul (n°178, n°119). Les affectations de constantes en tête se
sautent.

## 7. Le banc du lot rejoue les critères de recette

Recopier dans `tests_<lot>.mjs` les phrases de l'audit, au mot près : apostrophes → même verdict ; `>=` au seuil →
refus avec l'écart exact ; la v1 dans l'éditeur + prévisions justes → « à exécuter », puis « 3 / 10 », puis « à
rejouer » ; `60.5` refusé ; lignes lues sur la version figée même avec un commentaire inséré ; une écriture hors de
l'outil → « limite du banc », jamais « SyntaxError » ; le fichier `.py` du Bonus passe le banc 10 / 10.
Modèle : `3e_C6.1`, tests 6 à 21 bis (57 / 57 au 22/11/2026).

## 8. Mesurer sur tout le site

```bash
python3 _outils/controle_verification_execute.py --detail     # ✔ X · ⚠ M · ✘ T · ○ N, puis verrous faibles et éditeurs non jugés
python3 _outils/tests_controle_verification_execute.py       # 23 / 23, dont les pages d'avant l'audit et d'avant le 25/11
python3 _outils/banc_python/poser.py --verifier-tout          # chaque page porte la version de la source
python3 _outils/banc_eleve/poser.py --verifier-tout           # idem pour le banc-eleve (4 pages au 25/11/2026)
```

Mesure de départ (22/11/2026, 410 pages) : 7 pages à éditeur ; 3 exécutent, 0 juge par le texte seul, 4 éditeurs sans
vérification du programme. Un ⚠ M se relit à la main : le motif décide-t-il du verdict ?

Mesure du 25/11/2026, après le lot du banc-eleve : **7 ✔ X · 0 verrou faible · 0 éditeur d'activité sans jugement**
(2 éditeurs de Bonus sans banc, des défis ouverts : un corrigé suffit). Les « 4 ○ N » du 22/11 cachaient trois choses
différentes, que le contrôle dit maintenant :
- **un verrou d'exécution n'est pas un jugement** : « la console affiche quelque chose » (`print("x")`) ou « une ligne
  [pompe] » ne dit pas que le programme fait ce qu'on attend — `⚠ verrou à relire` ;
- **un éditeur qu'aucune vérification ne nomme** : l'élève y écrit, rien ne lit (`4e_C9.1`, activité 3) — `○ éditeur
  qu'aucune vérification ne juge` ;
- **un juge que le contrôle ne voyait pas** : un écouteur qui range `e.detail` (`window.__lamp`, relu par `lampJuger`).

Trois pièges vus dans ce lot :
- **Le lien Vittascience ne prouve rien** quand l'élève écrit : la page ne lit pas le programme écrit là-bas. Le
  geste d'ouvrir le lien ne vaut preuve que pour un programme DONNÉ qu'on exécute seulement (`4e_C6.2`, activité 3).
- **Un même mot pour deux choses** : le banc disait `"arret"` pour « programme arrêté par le banc », la page `4e_C6.2`
  pour « pompe à l'arrêt ». Un état du système et un état de l'outil ne partagent jamais un nom.
- **L'éditeur sauvegarde 500 ms après la dernière frappe** (un `change`) : le retrait commun de validation (« tu as
  changé une réponse ») s'y déclenche. Un banc de lot qui vérifie dans la foulée d'une frappe voit une validation
  disparaître ; il attend 0,7 s, comme un élève.

## Réponse à Pascal

Format `reponses-actionnables`. Les décisions qui lui reviennent (🔶) : un seuil de
tolérance ; une écriture que l'outil devrait apprendre à lire.
