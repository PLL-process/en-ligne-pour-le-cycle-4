# Rapport de tests — Lot 4e_C4.1 · C4.2 · C4.4 « Un Book Train pour la Schœlcher »

**Exécution réelle** le 08/08/2026, suite Playwright (Chromium headless) : **32/32 verts**.
Seuls des tests réellement exécutés sont déclarés ici (barre qualité du dépôt).

Ce lot **achève** une séquence qui existait seule depuis le 05/08/2026, sans QCM, sans synthèses, sans
fiche ni manifest — ce qui contredisait la règle du lot indivisible. La séquence elle-même n'a pas été
réécrite : elle a été complétée et mise aux règles d'or n°23 à n°34.

## Séquence (18 tests)

| Test | Vérifie | Résultat |
|---|---|---|
| SEQ-01 | chargement sans erreur JS | ✔ |
| SEQ-02 | titre conforme à la charte | ✔ |
| SEQ-03/04/05 | blocs règle n°4 : « 🧠 Prêt·e à t'entraîner ? », UN SEUL bouton QCM, « 🎁 Bonus » | ✔ |
| SEQ-06 | toutes les figures de la page se chargent (naturalWidth > 0) | ✔ |
| SEQ-07 | le lien QCM pointe un fichier réellement présent | ✔ |
| SEQ-08 | le nombre de questions annoncé correspond au QCM livré (30 dont 4 illustrées) | ✔ |
| SEQ-09 | sauvegarde locale : champ restauré après rechargement | ✔ |
| AUD-23 | durées annoncées par activité + badge « 3 séances de 55 min » (154 min pour 165) | ✔ |
| AUD-26 | billet d'entrée présent et annoncé **sans note** | ✔ |
| AUD-26b | le billet refuse les réponses vides **sans sanctionner** (« aucune note à la clé ») | ✔ |
| AUD-26c | 2 sur 3 → orientation vers la capsule de rattrapage | ✔ |
| AUD-26d | 3 sur 3 → l'élève est invité à poursuivre | ✔ |
| AUD-29 | bouton « mode essentiel » présent | ✔ |
| AUD-29b/c | activation : les corrections deviennent effectivement invisibles | ✔ |
| AUD-29d | retour au mode complet | ✔ |
| AUD-29e | choix du mode persistant après rechargement | ✔ |
| AUD-31 | une version étayée pour **chacune** des 3 productions écrites | ✔ |
| AUD-34 | **tout** select de la page porte une étiquette (`label for` ou `aria-label`) | ✔ |

## QCM (11 tests)

| Test | Vérifie | Résultat |
|---|---|---|
| QCM-01 | chargement sans erreur JS | ✔ |
| QCM-02 | 30 questions | ✔ |
| QCM-03 | répartition 10 / 10 / 10 sur C4.1, C4.2, C4.4 | ✔ |
| QCM-04 | bonnes réponses réparties sur A/B/C/D (8/7/8/7, `fix_r.js` graine 4127) | ✔ |
| QCM-05 | 4 questions illustrées | ✔ |
| QCM-06 | chaque distracteur réfuté + explication, exemple, erreur classique, à retenir | ✔ |
| QCM-07 | les images des questions existent sur le disque | ✔ |
| QCM-08/09 | correction détaillée affichée et tableau de bord mis à jour | ✔ |
| QCM-10 | sauvegarde locale restaurée après rechargement | ✔ |
| QCM-11 | navigation « ← Séquence » (règle n°11) | ✔ |

## Vérification des règles d'or n°23 à n°34

`python _outils/verif_regles_audit.py` sur ce lot : **n°23 ✔ · n°26 ✔ · n°29 ✔ · n°31 ✔ · n°33 ✔ · n°34 ✔**,
n°30 sans objet (les tâches de cette séquence ne passent pas par des vérificateurs numérotés).

## Environnement et limites (honnêteté)

- Tests exécutés hors ligne : l'appel aux polices Google échoue proprement (repli sur la police système),
  non bloquant, identique aux autres lots ; cet échec de ressource est journalisé mais non compté comme erreur.
- **Non testé automatiquement** : l'impression A4 (vérifiée visuellement), le rendu dans draw.io et dans
  LibreOffice Impress, et la lecture des SVG par un lecteur d'écran réel. Les deux SVG portent `role="img"`
  avec `title` et `desc` complets, ce qui est vérifiable dans le code mais ne remplace pas un essai avec NVDA
  ou VoiceOver.
- **Non testé non plus** : la règle n°30 (tableau de bord des tâches) n'est pas applicable en l'état à cette
  séquence, dont la progression repose sur des marqueurs de validation différents des `data-check` numérotés
  des autres lots. C'est un écart assumé et signalé, pas une conformité.
- Script de test : suite Playwright du lot (32 vérifications), rejouable.
