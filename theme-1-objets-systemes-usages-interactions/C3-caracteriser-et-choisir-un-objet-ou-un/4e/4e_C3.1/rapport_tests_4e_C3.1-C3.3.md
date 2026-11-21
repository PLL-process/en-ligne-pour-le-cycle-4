# Rapport de tests — lot Hangzhou 4e_C3.1 à C3.3

**Date** 08/08/2026 · **Agent** Fable · **Branche** `fable/theme-1/lot-hangzhou-4e-C3`


> **Correction du 31/08/2026 — la suite de ce lot était rouge, et c'est le test qui avait tort.**
> Réexécutée ce jour-là (personne ne l'avait relancée depuis sa livraison), elle échouait sur
> « séquence : hors ligne, aucune ressource distante (n°40) ». La cause n'était pas dans la
> page : le contrôle cherchait la chaîne `http://` dans le HTML sérialisé, où **chaque SVG en
> ligne porte son `xmlns="http://www.w3.org/2000/svg"** — un identifiant d'espace de noms, que
> nul navigateur ne va chercher. Le contrôle regarde désormais ce que la page **irait charger**
> (`src`, `link href`, `object data`, `iframe`, `use`), sans les hyperliens, qui ont le droit
> d'être distants. Vérifié dans les deux sens : la suite passe, et elle redevient rouge si l'on
> injecte une vraie ressource distante dans la page.
>
> ```
> 28 / 28 tests passés
> ```
```
python3 tests_4e_C3.1-C3.3_hangzhou.py     # depuis ce dossier, Playwright + Chromium
```

## Résultat : 28 / 28 tests passés

**Séquence** — aucune erreur JavaScript · aucune ressource distante (n°40) · bandeau de tâches
(n°30) · 9 zones de rédaction pour 9 versions étayées (n°31) · chaque champ étiqueté (n°34) ·
alternatives longues sur les deux figures · billet d'entrée sans note (n°26) · **verrou du cahier
des charges** : l'activité 1 exige quatre exigences écrites contenant au moins quatre chiffres, et
se valide une fois rédigées · **verrou de l'analyse** en activité 2 · mode essentiel qui masque
référentiel et corrections en laissant les versions étayées visibles · sauvegarde et restauration ·
blocs de la règle n°4 · un seul bouton QCM · aucun défilement horizontal à 1280 ni à 390 px.

**QCM** — aucune erreur JavaScript · aucune ressource distante · 30 questions · 2 illustrées avec
alternative longue · réponses réparties 8/7/7/8 · aucune réfutation en face de la bonne réponse ·
chaque distracteur réfuté · les trois codes couverts · les cinq champs de correction remplis.

## Vérificateur des règles d'or

**7 règles sur 7 au vert** — n°23 (145 min annoncés plus 10 de marge pour 220 disponibles), n°26,
n°29, n°30, n°31, n°33, n°34.

## Un défaut trouvé par les tests

Quatre réfutations de distracteurs étaient **trop courtes** — « Aucun rapport. », « Une seule
suffit. » Le test qui exige plus de vingt caractères par réfutation les a rejetées, et il avait
raison : une réfutation de trois mots n'enseigne rien. Elles ont été réécrites pour dire *pourquoi*
la réponse est fausse, ce qui est tout l'intérêt de la réfutation.

C'est un test que j'avais écrit pour le lot précédent et qui a servi ici sans que j'y pense : un
contrôle utile survit à son lot d'origine.

## Ce que la suite ne couvre pas

Impression A4, contraste mesuré, lecteur d'écran réel, zoom 200 % : **non vérifiés**, donc **non
déclarés conformes**. Le travail au tableur de l'activité 2 se fait hors de la page et n'est pas
testable automatiquement ; la trace attendue est décrite dans la séquence.

## Ajout du 21/11/2026 — audit du thème 1 : le QCM se lit seul, la séquence se ferme par un billet de sortie

Règles d'or n°343 (une question se lit seule), n°344 (ce qui est annoncé est cité en entier), n°345 (un QCM fait
lire des documents) et n°330 (la preuve faite seul).

- **QCM.** 5 questions retouchées : « Par rapport à la 5e… » (une question sur le programme, n°304) devient une lecture de fiche (« qu'ils durent » → quelle donnée ?) ; « Qu'on puisse les réparer » n'a plus deux réponses défendables ; le CO₂ par kilomètre se calcule et se compare sur document. 2 → 6 questions sur document. Dans la séquence : F3 rate les QUATRE exigences, pas trois (son antivol est à 3 pour 4 exigé) — question, vérificateur, correction et synthèse élève corrigés ; la légende de a1_6 s'accorde de nouveau avec ses propositions ; 72 « pourquoi » écrits (`mission_4e_C3.1.json`) : 9 → 81 sur 81.
- **Billet de sortie** (fin de la dernière séance, ~5 min, avant le Bonus) : le ventilateur des salles de classe (deux modèles). Deux réponses écrites, chacune
  avec sa version étayée ; une correction complète avec ses critères. Il ne valide rien.

Exécuté le 21/11/2026 :
- `python3 tests_4e_C3.1-C3.3_hangzhou.py` : **33 / 33** — dont le test du billet (deux zones sauvegardées, deux versions étayées,
  deux critères, avant le Bonus, aucun bouton) et le nouveau compte des questions sur document ;
- `node _outils/mode_mission/banc_generique.mjs` : la séquence jouée écran par écran à 390 px, aucun refus, le billet
  est un écran de la dernière séance ;
- `python3 _outils/controle_question_seule.py` : aucun refus sur le QCM (S1 à S4, E1) ;
- `python3 _outils/document_qcm.py documents_qcm_4e_C3.1.json --verifier` : les documents sont ceux des données ;
- les questions sur document regardées à 390 px dans le QCM (aucun débordement, l'image se charge).

Non testé : que le billet soit fait seul et sans aide — cela se voit en classe ; la lecture des réponses écrites
revient au professeur.
