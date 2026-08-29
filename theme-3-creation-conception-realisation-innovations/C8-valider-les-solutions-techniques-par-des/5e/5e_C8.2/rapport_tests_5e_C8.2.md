# Rapport de tests — lot 5e_C8.2 « La patère du hall »

**Environnement réel d'exécution** : Chromium (Playwright), pages ouvertes en `file://`, hors ligne.
Tests **réellement exécutés** le 29/08/2026.

**Résultat : séquence 14/14 · QCM 17/17 · zéro erreur JavaScript sur les deux pages.**

## Séquence (14 tests)

| # | Test | Résultat |
|---|---|---|
| 1 | La page charge sans erreur JS | ✅ |
| 2 | Aucune requête échouée (hors ligne) | ✅ |
| 3 | Aucune boîte modale (règle n°188) | ✅ |
| 4 | Le bois casse au 5ᵉ palier de 10 kg | ✅ |
| 5 | La rupture annonce la bonne charge (41 kg) | ✅ |
| 6 | Le verrou tient tant que 3 éprouvettes ne sont pas cassées | ✅ |
| 7 | Verrou « 3 éprouvettes » ouvert après 3 ruptures | ✅ |
| 8 | Verrou « 5 éprouvettes » ouvert après 5 ruptures | ✅ |
| 9 | Activité 2 validée avec les cinq bons relevés (5/5) | ✅ |
| 10 | **Un relevé faux (40 au lieu de 41) est refusé** (4/5) | ✅ |
| 11 | Activité 3 validée (4/4) | ✅ |
| 12 | Bandeau de durée présent | ✅ |
| 13 | Un seul bouton QCM (règle n°4) | ✅ |
| 14 | Hypothèse d'entrée présente | ✅ |

Le test n°10 est celui qui compte : il vérifie qu'on **ne peut pas valider l'activité 2 avec un
chiffre approché**. En 5e_C8.2, c'est la mise en œuvre qui est évaluée ; un relevé recopié sur le
voisin ne passe pas.

## QCM (17 tests)

30 questions · 30 notions distinctes · 90 réfutations · `d[r]` vide partout · répartition
A/B/C/D **8/7/7/8** (graine 82) · codes C8.2 ×20 et C3.1 ×10, tous deux au-dessus du seuil de
cinq questions · aucune réponse exposée dans le HTML rendu.

**Longueur des options** : aucune bonne réponse ne se détache de plus de 8 caractères du peloton,
écart moyen **+2,1 caractères**. Surveillé dès l'écriture cette fois, et non après coup — trois
jeux d'options ont été resserrés avant la première génération (règles n°198 et n°199).

## Ce que ce rapport ne prouve pas

Que la séquence fonctionne avec des élèves de 5ᵉ. Aucun test automatique ne le dira. Il prouve que
les pages tournent, que les verrous verrouillent, qu'un relevé inventé est refusé, et que la bonne
réponse du QCM ne se devine pas sans lire la question.

---

## Contrôle du 29/08/2026 — les deux boîtes que personne n'avait comptées

Ce rapport affirmait, ligne 3 de son tableau de séquence, « Aucune boîte modale (règle n°188) ✅ ».
C'était vrai des `alert()`, et **faux du reste** : le gabarit de QCM maison ouvre aussi deux boîtes
de confirmation — valider une question sans réponse, et « Recommencer ». Elles n'avaient jamais été
comptées, parce que la règle n°188 avait été appliquée au seul mot `alert`.

Deux corrections, faites le 29/08 :

* la page ne les ouvre plus. `_outils/sans_modale.py` les remplace par une confirmation **en deux
  temps** — premier clic : le bandeau `#savedNote` (`role="status"`, `aria-live="polite"`) annonce ;
  second clic dans les six secondes : l'action s'exécute. Une confirmation ne se supprime pas :
  elle pose une question dont la réponse change ce qui arrive ;
* **le lot reçoit enfin un script de test rejouable pour son QCM.** Il n'en avait aucun : le
  tableau « QCM (17 tests) » ci-dessus était une liste écrite à la main, que personne ne pouvait
  rejouer. `tests_5e_C8.2_qcm.mjs` est livré dans le dossier, et six de ses tests empruntent
  précisément les deux chemins qui ouvraient une boîte.

```
node tests_5e_C8.2_qcm.mjs "$PWD/qcm_5e_C8.2_patere-du-hall.html" C8.2 C3.1 sequence_5e_C8.2_patere-du-hall.html
```

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ 30 questions — 30
✅ 4 options par question
✅ 3 réfutations par question
✅ la bonne réponse n’a pas de réfutation
✅ tous les champs du gabarit remplis
✅ aucune image héritée du lot voisin
✅ 30 notions distinctes — 30
✅ 20 questions sur C8.2 — {"C8.2":20,"C3.1":10}
✅ 10 questions sur C3.1 — {"C8.2":20,"C3.1":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 2.1
✅ une bonne réponse est déclarée correcte
✅ la correction déplie les trois réfutations
✅ la correction porte un « À retenir »
✅ une mauvaise réponse est déclarée incorrecte
✅ valider sans réponse n’ouvre aucune boîte modale
✅ valider sans réponse annonce et ne valide pas encore — Tu n'as choisi aucune réponse : elle comptera comme non répondue. — clique une seconde fois pour confirmer.
✅ le second clic valide bien
✅ « recommencer » n’ouvre aucune boîte modale
✅ « recommencer » demande confirmation sans rien effacer — 30
✅ le second clic remet bien à zéro — 0
✅ le mode « marquées » vide n’ouvre aucune boîte modale
✅ il affiche un bandeau à la place — Aucune question marquée « à revoir ». Utilise le bouton 🔖 sur une question.
✅ 30 bonnes réponses donnent 100 % — 100 %
✅ la note affichée est 20/20 — 20,0 /20
✅ le lien vers la séquence pointe le bon fichier — sequence_5e_C8.2_patere-du-hall.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours

32 / 32
```

*Règle d'or n°216 : un test qui affirme qu'il ne se passe rien doit passer par les chemins où
quelque chose pourrait se passer. Sinon il mesure son propre silence.*

*La séquence de ce lot n'a toujours pas de script rejouable ; son tableau de 14 tests reste une
liste écrite à la main. C'est écrit ici pour que ce soit repris, pas pour que ce soit oublié.*
