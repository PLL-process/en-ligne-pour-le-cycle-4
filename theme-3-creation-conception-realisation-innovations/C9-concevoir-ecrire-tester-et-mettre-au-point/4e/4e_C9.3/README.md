# 4e_C9.3 — Réaliser et mettre au point un programme (couvert par une séquence mutualisée)

> Réaliser et mettre au point un programme commandant un système réel incluant
> éventuellement une interaction entre un humain et une machine.

Ce code est **entièrement travaillé par la séquence « Le jardin connecté se
programme »**, dont le dossier principal est
[`4e_C9.1`](../4e_C9.1/README.md) :

➡ **[Ouvrir la séquence](../4e_C9.1/sequence_4e_C9_jardin-programme.html)** —
trois activités lui sont consacrées.

* **Activité 4 — Tester : construire le jeu d'essais qui prouve.** Quatre familles
  d'essais — nominaux, **frontières**, exclusions, **absurdes** —, et la règle qui
  fait tout : la colonne ATTENDU se remplit **avant** l'exécution. L'essai à 40 %
  pile est le seul qui distingue `<` de `<=` ; l'essai à 250 % (capteur débranché)
  montre qu'un programme peut se tromper **en silence**.
* **Activité 5 — Le clignotement.** La pompe s'allume et s'éteint six fois par
  minute, et **il n'y a aucun bug** : chaque décision est juste, c'est la règle qui
  est mal choisie. On diagnostique, on corrige par **hystérésis** (deux seuils, une
  bande morte, une mémoire d'état), puis on **re-teste dans les mêmes conditions**
  — au banc, avec exactement le même tremblement de mesure.
* **Activité 6 — Réinvestir.** Le même squelette sur un lampadaire, écrit **sans
  aucun modèle fourni** (règle d'or n°114), avec une justification chiffrée de
  l'écart entre les deux seuils.

Le QCM du lot consacre **10 questions à 4e_C9.3**, dont deux illustrées :
l'anatomie d'un jeu de tests, et le chronogramme qui compare un seuil à deux
seuils sur la même mesure.

*L'idée qui reste quand tout le reste est oublié : **un programme peut être
parfaitement juste et parfaitement inutilisable**.*
