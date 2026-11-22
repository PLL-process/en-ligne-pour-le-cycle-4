# Rapport de tests — lot 3e_C1.1 à C1.4 « Tsinghua »

**Date d'exécution** 9 août 2026 · **Suite** `tests_3e_C1.1-C1.4_tsinghua.py` · **Moteur** Chromium
via Playwright.

**41 contrôles exécutés, 41 verts, aucune erreur JavaScript.**

Ne sont déclarés ici que des tests **réellement exécutés**. Le détail exact figure dans le fichier
de tests, qui est livré avec le lot et rejouable en une commande.

## Séquence — 24 contrôles

| Ce qui est vérifié | Nombre |
|---|---|
| Les six verrous **refusent** une page vide | 6 |
| Les six verrous **s'ouvrent** sur une production complète | 6 |
| Progression : 5 / 5 activités après validation | 1 |
| Cible du bouton d'entraînement aux trois moments (règle n°45) | 2 |
| Sauvegarde locale restaurée après rechargement (texte + progression) | 2 |
| Blocs de la règle n°4 : entraînement, Bonus, **corrigé du Bonus** | 3 |
| Phrase éthique de l'activité 4 **visible et non repliée** (règle n°68) | 1 |
| Carte de référentiel : les quatre formulations | 1 |
| Les trois corrigés graphiques se chargent effectivement | 1 |
| Zéro erreur JavaScript | 1 |

## QCM — 17 contrôles

Titre affiché et sous-titre propres au lot (règle n°51) · aucune trace d'un autre lot ·
30 questions · bonnes réponses réparties sur A/B/C/D · 11 illustrées · chaque distracteur réfuté ·
réfutation vide pour la bonne réponse · explication, exemple, erreur classique et à-retenir sur
chaque question · formulation du référentiel recopiée · ouverture `#depart=court` sur 10 questions ·
bandeau de portée visible · 30 bonnes réponses acceptées · clé de sauvegarde propre au lot ·
les 11 images se chargent · lien de retour vers la séquence · zéro erreur JavaScript.

Vérifié en outre, hors suite : `#codes=C1.1,C1.4` ouvre bien les 15 questions correspondantes
(8 + 7), le filtre propose les quatre codes, et le mode passe à « cible ».

## Vérificateur de règles du dépôt

`python3 _outils/verif_regles_audit.py` sur le dossier du lot : **8 contrôles sur 8**, dont la
règle n°42 — les quatre formulations de la carte sont celles du référentiel — et la n°33, après
correction de deux pavés de plus de 110 mots dans la correction de l'activité 5.

## Ce qui n'a PAS été testé (règle n°47)

- L'exactitude pédagogique des corrigés et des explications : elle relève de la relecture.
- La justesse des chiffres publics cités : elle relève des sources, listées dans
  `SOURCES_DONNEES_IMPACTS_3e.md`. Les tests vérifient que la page les affiche, pas que le
  ministère de l'Intérieur a raison.
- Le rendu à l'impression et l'ergonomie réelle en classe.
- Le comportement sur un navigateur autre que Chromium.

## Défauts trouvés et corrigés pendant les tests

1. **Deux éléments portaient `id="s1"`.** La découpe du gabarit tombait à l'intérieur de la
   structure des séances : le haut se terminait par l'ouverture du panneau `s1`. Le gestionnaire
   d'onglets activait donc le panneau vide, et le vrai restait invisible. Trouvé parce qu'un bouton
   présent dans le DOM refusait d'être cliquable — un contrôle qui porte sur ce qui est **rendu**
   (n°49) voit ce qu'une lecture du source laisse passer.
2. **Deux pavés de 117 et 115 mots** dans la correction de l'activité 5 (n°33). Coupés aux
   frontières de sens, sans être raccourcis : c'est leur longueur qui montre à l'élève ce qu'on
   attend d'un argumentaire.
3. **La séquence annonçait 7 questions illustrées**, la banque en compte 11. Aligné sur le nombre
   calculé depuis la banque (n°54).

## Révision du 15/11/2026 (révision des trois thèmes, 55)

- `python3 tests_3e_C1.1-C1.4_tsinghua.py` : **50 / 50** ; le banc suit les quatre bonnes réponses raccourcies (be_1, a1_1, a1_2, a1_4).
- `node tests_regle_311_3e_C1.1.mjs` : **34 / 34**.
- `node _outils/mode_mission/banc_generique.mjs` : la page jouée écran par écran, aucun refus ; 84 pourquoi sur 84 mauvaises propositions, chacun avec son étape suivante (`enrichir.py --etapes` : 0 sans étape).
- `verif_regles_audit.py` : 0 ✘ ; `audit_aeration.py --strict` : 0 ; `controle_ordre_propositions.py`, `controle_unites.py` : verts.
- `mesurer_charge.mjs` : 1 259 · 756 · 461 · 564 · 1 000 mots visibles (séance 1 au-dessus du repère, écart dit au suivi).
- Non testé : la lecture par un élève en classe ; le rendu sur un autre navigateur que Chromium.

## 21/11/2026 — Une question se lit seule : le QCM relu question par question, et le billet de sortie

- **Question 5, une erreur de fond.** La bonne réponse marquée était « trois niveaux hiérarchiques du même service » — et le pourquoi de la proposition voisine disait « Aucune hiérarchie n'est en jeu ». Une proposition et son pourquoi avaient été inversés : l'élève qui répondait juste (trois savoir-faire différents) était corrigé. La bonne réponse est maintenant « trois savoir-faire bien différents », à la place 4, et chaque pourquoi parle de sa proposition.

- Question 16 : le leurre « sans rapport avec le sujet de la séquence » devient « économique : il fait baisser le coût des secours », avec son pourquoi. Question 23 : « un argumentaire de 3e sur l'incidence d'un OST » devient « … d'un objet technique » (sigle non expliqué). Question 32 : « dans son cahier » devient « sur une feuille » (les élèves n'ont pas de cahier).

- **Billet de sortie** (n°330), à la fin de la dernière séance, juste avant le Bonus : le GPS du téléphone. Deux réponses écrites, chacune sa version étayée ; une correction avec ses deux critères et ses contre-exemples ; aucun bouton. Le banc le vérifie.

Exécuté : Banc 51 / 51 ; n°311 34 / 34. `node _outils/balayer_questions_qcm.mjs --apres` sur les huit QCM de C1 : 247 questions jouées à 390 px, 741 écrans d'aide après une réponse fausse, 0 écart. `controle_question_seule.py --strict` : 0 refus ; le thème 1 n'a plus de chantier D1 ni P1. Mode mission joué (`banc_generique.mjs`) : aucun refus. La dernière séance compte maintenant 1216 mots visibles (repère : 1 200 ; `mesurer_charge.mjs`).

Non fait : les questions n'ont pas été essayées en classe.
