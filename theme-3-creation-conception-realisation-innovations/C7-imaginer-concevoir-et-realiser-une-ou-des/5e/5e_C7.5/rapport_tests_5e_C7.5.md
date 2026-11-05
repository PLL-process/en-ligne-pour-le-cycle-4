# Rapport de tests — 5e_C7.5 « L'éclairage du préau »

Tests **réels**, joués dans un navigateur Chromium par Playwright, sur les fichiers du lot tels
qu'ils sont livrés. Cette page est la sortie de la dernière exécution, recopiée telle quelle —
les scripts et le jeu de réponses sont dans ce dossier, on peut tout rejouer.

```bash
node tests_5e_C7.5_sequence.mjs "$PWD/sequence_5e_C7.5_eclairage-du-preau.html" 5e reponses_5e_C7.5.json
node tests_5e_C7.5_qcm.mjs      "$PWD/qcm_5e_C7.5_eclairage-du-preau.html" 5e_C7.5 5e_C4.5 sequence_5e_C7.5_eclairage-du-preau.html
```

---

## 1. Séquence — **39 / 39**

```
✅ charge sans erreur JS
✅ aucune requête échouée
✅ aucune boîte modale
✅ aucun constituant monté au départ
✅ aucune fonction tenue au départ
✅ les quatre fonctions sont tenues — 4
✅ le courant demandé est celui attendu — Courant demandé : 68 mA sur 500 mA disponibles par l'USB
✅ le montage juste est accepté — ✔ Il fait sombre (le capteur lit 180) : la DEL s'allume. Il 
✅ le verdict décrit le comportement obtenu — ✔ Il fait sombre (le capteur lit 180) : la DEL s'allume. Il fait jour (820) : el
✅ « le capteur sur D4 » : le diagnostic est le bon — ✘ Capteur de luminosité Grove est sur D4, et il lui faut une entrée analogique (A0 à A3). 
✅ « le capteur sur D4 » : le verrou port_lum s’ouvre
✅ « le capteur sur A1 » : le diagnostic est le bon — ✘ Le programme lit A0, et Capteur de luminosité Grove est sur A1 : l'ordre et la mesure se
✅ « le capteur sur A1 » : le verrou attendu_lum s’ouvre
✅ « la DEL retirée » : le diagnostic est le bon — ✘ La fonction « Agir » n'est tenue par aucun constituant. Sans actionneur, la décision res
✅ « la DEL retirée » : le verrou fonction_agir s’ouvre
✅ « la carte retirée » : le diagnostic est le bon — ✘ Rien ne s'exécute : il n'y a pas de carte. Le programme n'a nulle part où tourner.
✅ « la carte retirée » : le verrou sans_carte s’ouvre
✅ le montage juste est de nouveau accepté — ✔ Il fait sombre (le capteur lit 180) : la DEL s'a
✅ verrou « monte » ouvert
✅ verrou « teste » ouvert
✅ verrou « ok » ouvert
✅ verrou « panne » ouvert
✅ verrou « retire » ouvert
✅ bandeau de durée présent — ⏱ 2 séances de 55 min
✅ un seul bouton QCM
✅ hypothèse d’entrée présente
✅ consigne de sécurité très basse tension présente
✅ le secteur est explicitement écarté
✅ les trois versions A/B/C sont annoncées
✅ aucun marqueur de gabarit non remplacé
✅ activité 0 validée (5/5) — 🎉 Activité validée — 5/5. Ouvre la correction pour comparer.
✅ activité 1 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 2 validée (4/4) — 🎉 Activité validée — 4/4. Ouvre la correction pour comparer.
✅ activité 3 validée (6/6) — 🎉 Activité validée — 6/6. Ouvre la correction pour comparer.
✅ activité 4 validée (1/1) — 🎉 Activité validée — 1/1. Ouvre la correction pour comparer.
✅ une réponse fausse est refusée — 🟡 5/6 — les encoches ✘ te montrent où regard
✅ les réponses survivent au rechargement — a1q1 = sa sortie varie continûment : une entrée numérique ne lirait que 0 ou 1
✅ le montage survit au rechargement — SOCLE
✅ les verrous survivent au rechargement
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
✅ 20 questions sur 5e_C7.5 — {"5e_C7.5":20,"5e_C4.5":10}
✅ 10 questions sur 5e_C4.5 — {"5e_C7.5":20,"5e_C4.5":10}
✅ les deux codes dépassent le seuil de 5 questions
✅ bonnes réponses réparties sur les 4 positions — 8/7/7/8
✅ aucune bonne réponse détachée par sa longueur — 0
✅ écart moyen de longueur sous 5 caractères — 3.3
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
✅ le lien vers la séquence pointe le bon fichier — sequence_5e_C7.5_eclairage-du-preau.html
✅ la progression survit au rechargement — 30
✅ aucune boîte modale sur tout le parcours
```

## 3. Ce que ces tests ont attrapé pendant la fabrication

Deux défauts, trouvés par les tests et non par relecture :

* **l'établi était écrit deux fois.** Il figurait dans chaque activité qui l'utilise, si bien que
  la page portait deux jeux d'éléments avec les mêmes identifiants. La sauvegarde n'en retenait
  qu'un — le montage de l'élève était perdu au rechargement. L'établi n'est plus écrit qu'une
  fois, et les activités suivantes y renvoient ;
* **l'établi écrasait sa propre sauvegarde.** Il appelait sa mise à jour au chargement de la
  page, donc *avant* la restauration : chaque ouverture remplaçait la sauvegarde par un établi
  vide. C'est le squelette qui restaure d'abord et met à jour ensuite.

Les deux défauts avaient le même symptôme et deux causes différentes ; aucun ne se voit à la
lecture du code.

## 4. Ce que ces tests ne prouvent pas

* Ils ne prouvent **rien sur un montage réel** : l'établi simule. La version 🅰 le fait avec la
  carte et les modules, et ce sont les branchements observés qui font foi.
* Ils ne prouvent rien sur la **qualité des phrases rédigées** : le vérificateur compte des
  caractères. C'est écrit dans la page, à l'élève.
* Ils ne prouvent rien sur ce qui se passe **en classe**. Un test vert dit que la page fait ce
  qu'elle annonce, pas qu'un élève apprend.

## 5. Reprise du 04/11/2026 — la séquence passe à onglets (vague n°311, sur le modèle du pilote 4e_C8.1)

Deux séances à onglets : séance 1 = ouverture + activités 0 et 1 ; séance 2 = activités 2 et 3, réinvestissement, synthèse,
Bonus, bilan, QCM. L'ouverture, dont l'encadré Sécurité, est repliée dans le volet « 📖 Rappel » dès la séance 2 ; l'en-tête de
la séance 2 rappelle qu'en 🅰 on rebranche hors tension. L'établi sert aux deux séances : un seul nœud (`#etabli`), rangé dans
la séance ouverte, sous son en-tête. Une barre d'outils (« 🖨 Imprimer / PDF ») est posée. La clôture est complétée : le corrigé
replié du Bonus (la phrase exacte de l'établi pour le capteur sur A1, relue sur la page), « Comment j'ai travaillé », et
« Je me positionne » aux quatre niveaux du livret sur 5e_C7.5 et 5e_C4.5.

- `node tests_regle_311_5e_C7.5.mjs` (relais du thème 3 → banc commun) : **34 / 34**.
- `node tests_5e_C7.5_sequence.mjs …` : **40 / 40** (39 avant) — les activités de la séance 2 s'ouvrent par leur onglet ; un
  test ajouté (deux séances, le volet). `node tests_5e_C7.5_qcm.mjs …` : **32 / 32** (inchangé).
- `controle_squelette.mjs` : 0 défaut (D1 à D6), aucun « à rédiger », aucun signalement.
- Verts : `controle_impression.mjs`, `controle_verrous.mjs`, `controle_hors_ligne.mjs`, `controle_contraste_liens.mjs`,
  `controle_impression_papier.py`, `controle_regles_visibles.py`, `controle_liens.py`, `controle_hierarchie.py`,
  `controle_unites.py`, `controle_sigles.py`, `controle_navigation_seances.py`, `controle_mode_essentiel.py`,
  `controle_competences.py`. Fiche papier (`banc_papier.py`) : une fiche par séance, sans champ d'écran ni texte pâle.
- `verif_regles_audit.py` : les mêmes ✘ qu'avant la reprise (vérifié sur `main`), hors périmètre de cette vague.

Non exécuté : un vrai téléphone, Firefox, Safari, une impression réelle.
