# Rapport de tests — 3e_C7.8 « Deux stations qui se parlent »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle —
les scripts et le jeu de réponses sont dans ce dossier, on peut tout rejouer.

> **Découpage du 24/10/2026 — trois séances de 55 min au lieu de deux de 90.** La séquence se fait
> désormais en une heure de cours par semaine : séance 1 = activités 0 et 1 (45 min), séance 2 =
> activités 2 et 3 (55 min), séance 3 = activité 4 et REFAIRE (50 min), puis la clôture. Aucune
> activité n'est coupée ni raccourcie. Le banc de la séquence le vérifie (bandeau, trois en-têtes
> dans l'ordre, minutes par séance, clôture à la seule séance 3, boutons et liens de séance,
> 390 px sans défilement horizontal) et recharge la page sur une sauvegarde écrite au format de
> l'ancienne page : chaque réponse revient à sa place. Le QCM n'a pas changé ; son banc a été rejoué.

> **Clé de sauvegarde propre, 24/10/2026.** Jusque-là, la page enregistrait sous la clé de
> 3e_C7.4 (`seq_3e_C7_4`) : les deux séquences mélangeaient le travail de l'élève dans un même
> navigateur. Elle enregistre désormais sous `seq_3e_C7_8`. À la première ouverture, si cette clé
> n'existe pas et que `seq_3e_C7_4` existe, elle en fait une copie (sans rien effacer), puis ne la
> relit plus jamais. Le banc vérifie la clé, la migration, la copie sans effacement, qu'écrire
> dans 3e_C7.8 ne touche plus `seq_3e_C7_4`, et que la migration ne se rejoue pas.

```bash
node tests_3e_C7.8_sequence.mjs "$PWD/sequence_3e_C7.8_deux-stations.html" 3e reponses_3e_C7.8.json
node tests_3e_C7.8_qcm.mjs      "$PWD/qcm_3e_C7.8_deux-stations.html" 3e_C7.8 3e_C8.3 sequence_3e_C7.8_deux-stations.html
```

---

## 1. Séquence — **58 / 58**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ message vide au départ — {}
✅ rien n’est lisible avec un message vide
✅ le message partiel est celui attendu — {"id":"robert","v":124,"u":"km/h"}
✅ certaines lectures restent impossibles — 5 non
✅ le message complet est celui attendu — {"id":"robert","v":124,"u":"km/h","t":"14:07","niv":2,"seq":417}
✅ tout devient lisible
✅ verrou du message valide ouvert
✅ un champ de trop est signalé au lieu d’être ignoré — 1
✅ le canal passe en coupé
✅ « ne déclenche jamais sans l'accord … » : le journal dit « AUCUNE alerte » — pé14:10  ✘ AUCUNE alerte — 124 km/h mesurés, et la sirène reste muette
✅ « déclenche seule, sans rien signale… » : le journal dit « déclenchée seule » —  déclenchée seule — et personne ne sait qu'elle n'était pas corroborée
✅ « déclenche seule, et signale qu'ell… » : le journal dit « NON CORROBORÉE » — lenchée, marquée « NON CORROBORÉE — Sainte-Anne muette depuis 15 min »
✅ verrou « coupe » ouvert
✅ verrou « degrade » ouvert
✅ lien rétabli : le message est reçu — ":"robert","v":124,"u":"km/h","t":"14:07","niv":2,"seq":417}
✅ bandeau de durée présent — ⏱ 3 séances de 55 min
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ encadré de sécurité présent
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ bandeau : 3 séances de 55 min — ⏱ 3 séances de 55 min
✅ le bandeau de durée a un title et un aria-label
✅ trois en-têtes de séance, dans l’ordre — seance-1,seance-2,seance-3
✅ seance-1 : 45 min d’activités annoncées, au plus 55 — 45 min — 🖐️ Activité 0 + 📋 Activité 1
✅ seance-2 : 55 min d’activités annoncées, au plus 55 — 55 min — 🤝 Activité 2 + 🔇 Activité 3
✅ seance-3 : 50 min d’activités annoncées, au plus 55 — 50 min — 🧪 Activité 4 + 🔄 REFAIRE
✅ aucune activité avant la séance 1, et 150 min en tout
✅ clôture à la dernière séance seulement : Bonus → Bilan → QCM — Bonus → Bilan → QCM
✅ un bouton vers la séance suivante au bas des séances 1 et 2 — #seance-2,#seance-3
✅ des liens vers les trois séances sous le titre — #seance-1,#seance-2,#seance-3
✅ chaque lien « banc » mène à un banc qui existe
✅ à 390 px, le bouton ➡ mène à la séance 2 — haut à 60 px
✅ à 390 px, le bouton ➡ mène à la séance 3 — haut à 60 px
✅ à 390 px, aucun défilement horizontal — 390
✅ activité 0 validée (3/3) — 🎉 Activité validée — 3/3. Ouvre la correction pour comparer.
✅ activité 1 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 2 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 3 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 4 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 5 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ une réponse fausse est refusée — 🟡 4/5 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a1msg = {"id":"robert","v":124,"u":"km/h","t":"14:07","niv":2,"seq":417}
✅ les verrous survivent au rechargement
✅ les champs cochés survivent au rechargement
✅ la page enregistre sous sa propre clé — seq_3e_C7_8
✅ première ouverture : la clé propre est créée, rien sous seq_3e_C7_4
✅ migration : la page se recharge sans erreur JS
✅ migration : chaque réponse de seq_3e_C7_4 apparaît à sa place, séance 3 comprise — hyp=Si l’une des d · hors=déclenche seul · a2regle=La sirène part · a3ph=Quand l’autre  · reinv=À trois, on vo
✅ migration : l’idée de départ est rappelée au bilan
✅ migration : les verrous sont conservés
✅ migration : copie sans effacer — seq_3e_C7_4 est intacte
✅ écrire dans 3e_C7.8 ne modifie plus seq_3e_C7_4
✅ … et ce qui est écrit va sous seq_3e_C7_8
✅ migration une seule fois : 3e_C7.8 ne relit plus seq_3e_C7_4 — Nouvelle idée, écrite dans 3e_C7.8.
```

## 2. QCM — **32 / 32**

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
✅ 20 questions sur 3e_C7.8 — {"3e_C7.8":20,"3e_C8.3":10}
✅ 10 questions sur 3e_C8.3 — {"3e_C7.8":20,"3e_C8.3":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 3.8
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
✅ le lien vers la séquence pointe le bon fichier — sequence_3e_C7.8_deux-stations.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Six de ces tests existent parce qu'une règle avait été mal appliquée

La règle d'or n°188 — *une page d'élève ne s'arrête pas pour parler* — avait été appliquée au
seul mot `alert`. Le gabarit de QCM maison ouvre aussi **deux boîtes de confirmation** : valider
une question sans avoir choisi de réponse, et « Recommencer ». Personne ne les avait comptées, et
le test qui affirmait « aucune boîte modale sur tout le parcours » **ne passait par aucun de ces
deux chemins** : il était vert sans rien prouver.

Six tests l'accompagnent maintenant, qui les empruntent : `valider sans réponse n'ouvre aucune
boîte modale` / `annonce et ne valide pas encore` / `le second clic valide bien`, puis les trois
mêmes pour « recommencer », dont `demande confirmation sans rien effacer` — celui-là vérifie que
les 30 réponses sont **toujours là** après le premier clic.

Une confirmation ne se supprime pas : elle pose une question dont la réponse change ce qui arrive.
`_outils/sans_modale.py` la remplace par une confirmation **en deux temps** (premier clic : le
bandeau `aria-live` annonce ; second clic dans les six secondes : l'action s'exécute) et refuse
tout motif qu'il ne reconnaît pas plutôt que de deviner.

*Règle d'or n°216 : un test qui affirme qu'il ne se passe rien doit passer par les chemins où
quelque chose pourrait se passer. Sinon il mesure son propre silence.*

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur une liaison réelle** : le banc simule l'échange. La version 🅰 le
  fait avec deux cartes, et ce sont les trames observées qui font foi.
* Ils ne prouvent rien sur la **qualité des phrases rédigées** : le vérificateur compte des
  caractères et des lignes. C'est écrit dans la page, à l'élève.
* Ils ne prouvent rien sur ce qui se passe **en classe**. Un test vert dit que la page fait ce
  qu'elle annonce, pas qu'un élève apprend.
