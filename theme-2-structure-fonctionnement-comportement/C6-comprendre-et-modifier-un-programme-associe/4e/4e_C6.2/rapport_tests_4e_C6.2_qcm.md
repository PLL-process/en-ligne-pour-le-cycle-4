# Rapport de tests — QCM 4e_C6.2 « Le jardin connecté : arrosage automatique »

**Environnement réel d'exécution** : Chromium (Playwright), page ouverte en `file://`, hors ligne.
Suite : `tests.mjs` — 16 tests, **tous réellement exécutés** le 28/08/2026.

**Résultat : 16 / 16 réussis · aucune erreur JavaScript · aucune requête échouée.**

| # | Test | Résultat | Mesure |
|---|---|---|---|
| 1 | La page charge sans erreur JS | ✅ | 0 erreur |
| 2 | Aucune requête échouée | ✅ | 0 |
| 3 | Aucune boîte modale (règle n°188) | ✅ | 0 |
| 4 | 30 questions | ✅ | 30 |
| 5 | 30 notions nommées, toutes distinctes | ✅ | 30 |
| 6 | 90 réfutations, une par distracteur | ✅ | 90 |
| 7 | Aucune réfutation posée sur la bonne réponse | ✅ | `d[r]` vide partout |
| 8 | Répartition A/B/C/D équilibrée | ✅ | 8 / 7 / 7 / 8 (graine 62) |
| 9 | Cinq codes du programme, aucun code inventé | ✅ | C6.2 ×16, C4.4 ×5, C4.5 ×4, C4.1 ×3, C1.4 ×2 |
| 10 | Tous les champs du gabarit renseignés | ✅ | `c n q o r expl ex err d ret` |
| 11 | Aucune option dupliquée | ✅ | 30/30 |
| 12 | Aucune bonne réponse détachée par sa longueur | ✅ | 0 / 30 (seuil : 8 caractères) |
| 13 | Écart moyen bonne / distracteurs sous 5 caractères | ✅ | **−1,6** caractère |
| 14 | Aucune réponse exposée dans le HTML rendu | ✅ | plus de `value="v0"` |
| 15 | Titre à la charte | ✅ | porte `4e_C6.2` |
| 16 | Retour vers la séquence du lot | ✅ | `sequence-jardin-connecte-arrosage-automatique.html` |

## Le test n°12 a d'abord échoué, et c'est le plus utile de la série

Première exécution : **24 questions sur 30** avaient la bonne réponse la plus longue, avec
**12,5 caractères d'avance** en moyenne. Défaut classique du QCM rédigé à la main — on soigne la
bonne réponse et on expédie les distracteurs. Un élève qui coche systématiquement la plus longue
obtenait un score honorable sans rien savoir.

Deux passes de correction ont été nécessaires, et la première s'est trompée :

| État | bonne = la plus longue | bonne = la plus courte | écart moyen |
|---|---|---|---|
| version initiale | 24 / 30 | 3 / 30 | **+12,5** car. |
| après 1ʳᵉ passe | 3 / 30 | 24 / 30 | **−6,7** car. |
| après 2ᵉ passe | 6 / 30 | 15 / 30 | **−1,6** car. |

La première passe avait **échangé le biais contre son miroir** : « coche la plus courte » marchait
aussi bien. Le rang seul n'est donc pas un bon critère — ce qui compte est l'écart **visible**.
Quand la bonne réponse est la plus courte, elle l'est aujourd'hui de 2 caractères en médiane, et
de 7 au maximum : personne ne peut le voir dans une liste.

La correction a consisté à **allonger les distracteurs**, pas à tronquer les bonnes réponses : un
distracteur détaillé et plausible est un meilleur piège qu'un distracteur bâclé, et il correspond
à une vraie erreur d'élève.

## Ce que ce rapport ne prouve pas

Que les 30 questions sont pédagogiquement justes pour des élèves de 4ᵉ. Aucun test automatique ne
le dira : cela se voit en classe. Le rapport prouve que la banque est conforme au gabarit, que la
page fonctionne, et que la bonne réponse ne se devine pas sans lire la question.
