# Rapport de tests — lot 5e_C8.2 « La patère du hall »

**Environnement réel d'exécution** : Chromium (Playwright), pages ouvertes en `file://`, hors ligne.
Tests **réellement exécutés** le 29/08/2026, puis rejoués et complétés le 30/08/2026.

**Résultat : séquence 24/24 · QCM 17/17 · zéro erreur JavaScript sur les deux pages.**
Les deux suites sont dans ce dossier et se relancent&nbsp;: `tests_5e_C8.2_sequence.mjs` et
`tests_5e_C8.2_qcm.mjs`.

## Séquence — `tests_5e_C8.2_sequence.mjs` (24 tests)

    node tests_5e_C8.2_sequence.mjs sequence_5e_C8.2_patere-du-hall.html

**24 / 24**, sous Chromium (Playwright), le 30/08/2026.

> **Ce que ce bloc remplace.** Il portait un tableau de **quatorze lignes écrites à la main**,
> quatorze coches vertes, et rien pour les rejouer. Le QCM avait reçu son script le 29/08 ; la
> séquence était restée avec sa liste de bonnes intentions. Un tableau qu'on ne peut pas
> relancer ne dit pas « ça marche », il dit « ça marchait le jour où quelqu'un a regardé ».

La suite **conduit le banc pour de vrai** : elle choisit un matériau, clique sur les paliers de
charge jusqu'à la rupture, remet une éprouvette neuve, et recommence cinq fois. Les verrous ne
sont donc pas forcés dans le code — ils s'ouvrent par le geste, comme pour un élève.

Les quatorze affirmations d'origine sont toutes rejouées. S'y ajoutent dix contrôles que le
tableau ne faisait pas :

- **aucun verrou expérientiel ouvert à l'ouverture de la page** (règle d'or n°226) ;
- une éprouvette déjà cassée refuse une charge de plus, et le dit ;
- les cinq charges de rupture sont lues sur la page, une par une (41 · 51 · 53 · 194 · 408 kg) ;
- la **formulation officielle du code** est comparée à `_outils/data_competences.py` — le test la
  lit dans le référentiel plutôt que de la recopier, sinon il cesserait de tester la citation ;
- aucun identifiant HTML en double ;
- relevés, verrous et hypothèse survivent au rechargement.

### Le contrôle qui a trouvé quelque chose

**La séquence ne portait aucune consigne de sécurité.** Son voisin `5e_C8.1` écrit pourtant
« aucune manipulation électrique dans cette séquence : ni très basse tension, ni secteur ».
Celui-ci, qui décrit un banc de traction où une masse est suspendue, ne disait rien du tout.

La consigne est ajoutée au palier du banc : le banc de la page est un **simulateur**, il n'y a
pas de secteur — et si le professeur monte un banc réel, la charge se pose et se retire à
l'arrêt, personne ne reste sous la masse, et c'est lui qui l'installe.

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
