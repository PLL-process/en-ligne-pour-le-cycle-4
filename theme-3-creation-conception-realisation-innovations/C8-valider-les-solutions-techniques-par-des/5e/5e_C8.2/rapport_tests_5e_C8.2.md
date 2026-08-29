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
