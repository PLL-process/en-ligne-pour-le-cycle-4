# Sources des médias — lot Shenzhen 3e_C3.1 à C3.4

**Règle d'or n°1** : chaque image est un document à lire, produite pour le dépôt, sous licence
libre, avec `<title>` et `<desc>` accessibles.

| Fichier | Nature | Auteur | Licence | Rôle pédagogique |
|---|---|---|---|---|
| `Images/familles_de_solutions.svg` | SVG original écrit à la main | Fable, pour ce dépôt | CC0 1.0 | Les trois familles — passives, actives, organisationnelles — présentées comme également légitimes, avec la règle de la liste |

Une seule figure, et c'est volontaire : cette séquence demande aux élèves de **produire** la liste,
pas de la lire. Une planche de solutions illustrées aurait donné les réponses de l'activité 1.

## Les données

`donnees_local_technique_shenzhen_simulees.csv` — **entièrement simulées**, produites pour ce lot :
six solutions, quinze colonnes. Réalistes et cohérentes, elles ne décrivent aucun matériel
commercialisé.

Deux particularités assumées du tableau, toutes deux pédagogiques :

- **S6 porte des valeurs négatives** (coût annuel −450 €, consommation −900 kWh). Ce n'est pas une
  erreur : réduire le nombre de machines fait baisser la facture et la chaleur produite. C'est la
  seule ligne qui agit sur la cause, et le tableau doit le montrer plutôt que le dire.
- **S5 et S6 n'ont ni durée de vie ni indice de réparabilité.** Ces cases sont vides parce que la
  question n'a pas d'objet — elles n'installent aucun matériel. Savoir distinguer une case sans
  objet d'une donnée manquante fait partie de ce que la séance 2 travaille.

Le tableau **n'est pas distribué en séance 1** : il arriverait avant que les élèves aient établi
leur propre liste, et viderait la compétence 3e_C3.1 de son sens.

## Polices

**Aucune police distante** (règle d'or n°40). Séquence, QCM et synthèses utilisent une pile système.

## Image générée par IA (Canva) pour la synthèse élève

Demande de Pascal du 29/10/2026 : « une capture d'écran ou une illustration permet d'avoir une vision plus synthétique
de l'objet » ; Canva autorisé « pour des images réalistes et autres ». Règles : skill `synthese-vulgarisee`, §4.

| Fichier | Ce qu'elle montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/synthese_local_serveurs.png` | Un petit local sans fenêtre : deux armoires de serveurs, des câbles, un thermomètre et une bouche d'aération au mur. PNG 1 536 × 1 024, 2.2 Mo. | **Image générée par IA** avec Canva (génération d'image), compte de Pascal, 29/10/2026. Demande : « Realistic photo of a small windowless server room in a school: two black server racks with small status lights and tidy cables, a wall thermometer, a small wall air vent, warm light, eye-level view, no people, no text, no logos » | Conditions Canva AI Product Terms : l'image appartient à Pascal, sans attribution exigée ; interdit de la présenter comme faite par un humain (légende « Image générée par IA (Canva) ») et d'en retirer les métadonnées de provenance (manifeste C2PA et XMP Canva gardés : **fichier non modifié**, d'où son poids). | Synthèse élève, carte « Ce que je dois retenir » ; et la situation déclenchante de la séquence (05/11/2026) |

## Documents du QCM (21/11/2026, règle d'or n°345)

Des documents à lire pour répondre, dessinés pour le téléphone (350 unités de large, texte de 15 px et plus).
Pour les redessiner : `python3 _outils/document_qcm.py documents_qcm_3e_C3.1.json`.

| Fichier | Ce qu'il montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/doc_cout_deux_solutions.svg` | Deux fiches. Climatiseur : installation 2 400 euros, fonctionnement 340 euros par an, durée de vie 10 ans. Refroidissement par eau : installation 3 100 euros, fonctionnement 210 euros par an, durée de vie 15 ans. | SVG original, dessiné par `_outils/document_qcm.py` à partir de `documents_qcm_3e_C3.1.json` — Claude (Fable 5.2), pour ce dépôt, 21/11/2026. Les nombres sont ceux du fichier de données simulées du lot. | CC0 1.0 | QCM, question 11 |
| `Images/doc_cases_vides.svg` | Deux fiches. Climatiseur : installation 2 400 euros, baisse de température 9 degrés, durée de vie 10 ans, réparabilité 5 sur 10. Réduire le nombre de machines : installation 0 euro, baisse de température 5 degrés, durée de vie : case vide, réparabilité : case vide. | SVG original, dessiné par `_outils/document_qcm.py` à partir de `documents_qcm_3e_C3.1.json` — Claude (Fable 5.2), pour ce dépôt, 21/11/2026. Les nombres sont ceux du fichier de données simulées du lot. | CC0 1.0 | QCM, question 12 |
| `Images/doc_trois_solutions_actives.svg` | Trois fiches. Extracteur d'air : baisse de température 4 degrés, consommation 310 kilowattheures par an, durée de vie 12 ans, réparabilité 8 sur 10. Climatiseur : baisse 9 degrés, consommation 1 850 kilowattheures par an, durée de vie 10 ans, réparabilité 5 sur 10. Refroidissement par eau : baisse 7 degrés, consommation 540 kilowattheures par an, durée de vie 15 ans, réparabilité 6 sur 10. | SVG original, dessiné par `_outils/document_qcm.py` à partir de `documents_qcm_3e_C3.1.json` — Claude (Fable 5.2), pour ce dépôt, 21/11/2026. Les nombres sont ceux du fichier de données simulées du lot. | CC0 1.0 | QCM, question 15 |
| `Images/doc_releves_journee_juin.svg` | Cinq barres, une par relevé. À 8 heures : 29 degrés. À 11 heures : 33 degrés. À 14 heures : 38 degrés. À 17 heures : 41 degrés. À 20 heures : 35 degrés. | SVG original, dessiné par `_outils/document_qcm.py` à partir de `documents_qcm_3e_C3.1.json` — Claude (Fable 5.2), pour ce dépôt, 21/11/2026. Les nombres sont ceux du fichier de données simulées du lot. | CC0 1.0 | QCM, question 20 |
| `Images/doc_trois_baisses.svg` | Quatre fiches. À combler : il faut gagner 9 degrés au moment le plus chaud. Ventilation naturelle, seule : baisse de 2,5 degrés. Extracteur d'air, seul : baisse de 4 degrés. Réduire le nombre de machines, seule : baisse de 5 degrés. | SVG original, dessiné par `_outils/document_qcm.py` à partir de `documents_qcm_3e_C3.1.json` — Claude (Fable 5.2), pour ce dépôt, 21/11/2026. Les nombres sont ceux du fichier de données simulées du lot. | CC0 1.0 | QCM, question 27 |
