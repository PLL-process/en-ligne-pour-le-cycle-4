# 3e_C8.3 — Proposer un protocole de test (couvert par une séquence mutualisée)

> Proposer un protocole de test pour valider le comportement et les performances
> d'un objet technique.

Ce code est **entièrement travaillé par la séquence « La station d'alerte
cyclonique se programme »**, dont le dossier principal est
[`3e_C9.2`](../../../C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2/README.md) :

➡ **[Ouvrir la séquence](../../../C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2/sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html)** —
la **séance 4** y est consacrée à 3e_C8.3 :

* **Activité 6 — Rédiger le protocole de recette** : l'élève *propose* (verbe du
  code) son protocole AVANT toute exécution — 4 essais nominaux, **6 cas limites**
  aux frontières des trois seuils (62/63, 117/118 et 177/178 km/h), performance
  chronométrée (< 1 s), deux essais d'interaction humain-machine, règle de
  décision. Soit **13 essais**, dont la moitié aux frontières : c'est là que
  vivent les pannes, et c'est là que se joue le « ≥ ».
* **Activité 7 — Exécuter la recette et signer le PV** : exécution au banc d'essai
  intégré (les six frontières et le chrono tracés par verrous expérientiels — la
  page refuse de valider sans elles), tableau essai / attendu / observé / verdict
  rempli PENDANT les essais, procès-verbal de recette rédigé et signé. La
  correction déplie **six captures réelles du simulateur Vittascience**, une par
  frontière : entre 177 et 178 km/h, la mesure brute passe de 725 à 729 et le
  niveau bascule — le « ≥ » cesse d'être une convention d'écriture.

Le QCM du lot consacre **15 questions à 3e_C8.3** (dont une illustrée sur
l'anatomie du protocole), et la synthèse élève récapitule la démarche complète
(protocole rédigé avant, frontières, performance mesurée, non-régression, PV).

*Contexte : la mairie commande la station et exige un procès-verbal de recette
avant mise en service — la validation par les tests n'est pas un exercice ajouté,
c'est la condition de livraison du projet.*

## Où travailler, page par page

La séquence existe aussi **découpée en quatre pages**, une par séance. Pour 3e_C8.3,
tout se passe sur la quatrième :
[`..._station_4_recette.html`](../../../C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2/sequence_3e_C9.2-C8.3_station_4_recette.html).
Les cinq fichiers partagent le même enregistrement : un élève qui a travaillé sur la
page complète retrouve ses réponses ici, et réciproquement.
