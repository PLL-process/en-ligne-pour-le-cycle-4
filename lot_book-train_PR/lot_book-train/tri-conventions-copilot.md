# Tri des conventions Copilot (01/08/2026) — quoi verser aux règles d'or

> Principe de gouvernance du dépôt : une règle d'or est PEU NOMBREUSE,
> NUMÉROTÉE et VÉRIFIÉE dans chaque lot. Une liste affichée non vérifiée
> est de la décoration. D'où ce tri en trois colonnes.

## ✅ À ADOPTER (nouveau)

**Clause « consigne » pour la règle n°6 (chaînes)** — née de la remarque
de Pascal, confirmée par l'usage :
> Communiquer = transmettre la CONSIGNE qui pilote la chaîne d'énergie
> (ajuster puissance, vitesse, état). C'est ce que matérialise la flèche
> ORDRE. Ne JAMAIS renommer le bloc en « Transmettre » : ce verbe est
> réservé, comme titre de bloc, à la chaîne d'énergie (transmettre le
> mouvement). Même verbe, deux flux — information vs mouvement — et cette
> distinction est un piège enseigné, pas évité.

Exemple de classe validé : ventilateur automatique (capteur température →
comparaison au seuil → consigne au moteur → vitesse ajustée). Le Book Train
en est la version spectaculaire (capteurs de station → PLC → consigne au
variateur 24 V).

## 🟰 DÉJÀ COUVERT (ne pas dupliquer)

| Item Copilot | Chez nous |
|---|---|
| Verbe à l'infinitif partout (fonctions, blocs, actions) | Règle n°19 (candidate) + encadré canonique séquence |
| Chaînes info/énergie à blocs infinitifs | Règle n°6 (info en haut, énergie en bas, ordre descend) |
| Flux représentés par des flèches, orientation entrée→sortie | Règles n°6 + n°18 (affluents, jonctions, sens) |
| Couleurs fonctionnelles, pas décoratives | Bloc « finition premium » (3 couleurs max, rouge = ORDRE) |
| Pièces et actions nommées clairement | Règle n°18 clause libellés + premium |
| Indentation / mots-clés des algos, variables explicites | Mécaniques Parsons / Python à trous (règles 16/17) |
| Tester, mesurer, conclure | Vérificateurs + verrous __exp (règle 14) |

## ❌ À ÉCARTER (avec raison)

- **SADT / FAST** : outillage lycée SI ; hors cible cycle 4 programme 2024.
  À garder en réserve pour une passerelle 3e → 2de, pas en règle d'or.
- **« Jamais de paragraphes, toujours des listes »** : contredit la méthode
  du dépôt — le récit des situations déclenchantes est de la prose VOULUE.
  La vraie règle est : document TECHNIQUE = nominal/listes ; document
  NARRATIF ou RÉFLEXIF = prose légitime.
- **« Pas de je, pas de subjectif »** : casserait les auto-positionnements
  (« j'y arrive seul·e ») et les bilans d'hypothèse. Même distinction
  technique/réflexif que ci-dessus.
- **Les « 10 clefs de voûte » en affiche** : séduisant mais non vérifiable
  en l'état. Si affiche il y a, elle DÉRIVE des règles numérotées du dépôt
  (6, 14, 16, 17, 18, 19 + clause consigne), pas l'inverse.

## Vérification dans les lots (à ajouter aux check-lists)

☐ Le bloc Communiquer n'est jamais renommé « Transmettre »
☐ La flèche ORDRE est légendée comme consigne pilotant l'énergie
☐ Le piège « les deux Transmettre » figure dans toute séquence chaînes
