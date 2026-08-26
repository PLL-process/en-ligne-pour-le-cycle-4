# Sources des médias — Lot 4e_C9 « Le jardin connecté se programme »

Tous les médias de ce lot sont des **créations originales** réalisées pour le projet
(SVG écrits à la main). Aucune image extraite d'un manuel, de Google Images ou d'un
site tiers. Aucun hotlinking. **Aucune capture d'écran** dans ce lot : les planches
sont des schémas, et elles ne se présentent jamais comme des captures (règle d'or
n°94 — on ne fait pas passer une reconstitution pour une capture).

| Fichier | Type | Source / auteur | Licence | Rôle pédagogique (image à LIRE) | Poids |
|---|---|---|---|---|---|
| `Images/chaines_jardin_connecte.svg` | SVG original | Création Fable pour ce projet | CC0 (domaine public) | Image-objet : les deux chaînes selon la convention du dépôt (info en haut, énergie en bas, ordre qui descend) — et la flèche d'ORDRE qui s'arrête sur le **relais**, act. 1 et QCM (q. illustrée) | ~9 Ko |
| `Images/algorigramme_arrosage.svg` | SVG original | Création Fable pour ce projet | CC0 | Image-objet : algorigramme normalisé à cinq blocs numérotés, avec la bulle de commentaire sur le ET et la boucle sans bloc FIN — act. 2 et QCM (q. illustrée) | ~7 Ko |
| `Images/jeu_de_tests_anatomie.svg` | SVG original | Création Fable pour ce projet | CC0 | Image-objet : les quatre familles d'essais placées sur la droite de l'humidité, le tableau attendu/observé, et l'avertissement sur le cas absurde — act. 4 et QCM (q. illustrée) | ~8 Ko |
| `Images/hysteresis_chronogramme.svg` | SVG original | Création Fable pour ce projet | CC0 | Image-objet : **la figure centrale du lot** — la même mesure d'humidité traitée à un seuil (six basculements) puis à deux seuils (un seul), avec la bande morte tramée — act. 5 et QCM (q. illustrée) | ~8 Ko |

Autres fichiers non graphiques du lot :

| Fichier | Nature | Licence |
|---|---|---|
| `tests_4e_C9.mjs` | Suite de tests Playwright du lot (création originale) | CC0 |
| Trace d'exécution de l'activité 5 | **Données SIMULÉES**, écrites pour l'exercice et signalées comme telles dans la page (« trace enregistrée ») | CC0 |
| Banc d'essai du jardin (JavaScript intégré à la séquence) | Création originale ; le « tremblement » est une suite de valeurs **figée dans le code**, non un tirage aléatoire, pour que la comparaison entre les deux règles soit reproductible | CC0 |

## Notes de conformité

- chaque image est un **document à lire** — aucune image décorative ;
- **lisibilité en niveaux de gris** : l'information ne repose jamais sur la seule
  couleur. Sur le chronogramme, la bande morte est **tramée** en plus d'être
  colorée, les deux états de la pompe sont **écrits** (ON / OFF), et les six
  basculements sont **comptés en toutes lettres** dans la légende (règle n°119) ;
- **textes alternatifs** : `alt` long dans la page (plus de 120 caractères chacun,
  vérifié par la suite de tests) + `<title>` et `<desc>` internes à chaque SVG, et
  une **description dépliable** sous chaque figure (règle n°117). Toutes les images
  s'agrandissent à la loupe (règle n°92) ;
- **aucune donnée personnelle**, aucun identifiant, aucun nom de compte ;
- **l'éditeur Vittascience** est appelé par `iframe` depuis `fr.vittascience.com` :
  c'est le seul élément du lot qui demande une connexion, et un repli hors-ligne
  complet est prévu (le banc d'essai fonctionne sans réseau) ;
- **valeurs pédagogiques** : le seuil de 40 % d'humidité, la plage 6 h - 10 h et les
  seuils 35/45 sont des **valeurs de départ proposées par le professeur**, dites
  comme telles dans la situation déclenchante. Ce ne sont pas des données
  agronomiques : la séquence le précise, et l'activité 6 demande justement de
  justifier un choix de seuils plutôt que de le recopier (règle n°111).
