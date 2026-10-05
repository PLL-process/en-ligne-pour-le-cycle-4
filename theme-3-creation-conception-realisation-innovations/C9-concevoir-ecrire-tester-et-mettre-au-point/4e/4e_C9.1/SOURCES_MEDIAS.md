# Sources des médias — Lot 4e_C9 « Le jardin connecté se programme »

Tous les médias de ce lot sont des **créations originales** réalisées pour le projet
(SVG écrits à la main). Aucune image extraite d'un manuel, de Google Images ou d'un
site tiers. Aucun hotlinking. **Les planches sont des schémas**, et elles ne se présentent jamais
comme des captures (règle d'or n°94 — on ne fait pas passer une reconstitution pour une capture) ;
**les douze captures d'écran de l'encart des gestes** sont décrites à la fin de ce fichier.

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
- **l'éditeur Vittascience** s'ouvre par un lien, dans un nouvel onglet, sur `fr.vittascience.com` (le site refuse d'être encadré) :
  c'est le seul élément du lot qui demande une connexion, et un repli hors-ligne
  complet est prévu (le banc d'essai fonctionne sans réseau) ;
- **valeurs pédagogiques** : le seuil de 40 % d'humidité, la plage 6 h - 10 h et les
  seuils 35/45 sont des **valeurs de départ proposées par le professeur**, dites
  comme telles dans la situation déclenchante. Ce ne sont pas des données
  agronomiques : la séquence le précise, et l'activité 6 demande justement de
  justifier un choix de seuils plutôt que de le recopier (règle n°111).

## Captures d'écran des gestes de Vittascience (05/10/2026)

L'encart « Avant de commencer (échauffement) » porte douze captures. **Il se fait sans compte, et l'éditeur reste en mode mixte** : la
séance 2 va des blocs au Python, et le programme de l'activité 3 revient en blocs à la réouverture (mesuré le 05/10/2026). Aucune capture
ne montre une session connectée. Les captures de Vittascience ont été prises dans un **profil de navigateur temporaire, neuf et jamais
connecté** : aucun identifiant, aucun mot de passe enregistré, aucune extension. Les captures de l'Explorateur sont des **fenêtres seules**,
sans nom de compte Windows, sans autre fichier (`PROTOCOLE_CAPTURES_GESTES.md`). Les noms `4e-JARDIN-DUPONT` et `4E3` sont des **exemples**,
dits comme tels dans les légendes. Il n'y a pas de capture du menu « Ouvrir avec » ni du Bloc-notes : ce lot ne les utilise pas.

| Fichier | Nature | Origine | Licence | Usage | Poids |
|---|---|---|---|---|---|
| `Images/geste_vitta_1_ouvrir_bouton.png` | **Capture d'écran réelle** (règle n°94) | La séquence 4e_C9.1 elle-même (servie en local), Chrome 154 piloté par Playwright, profil temporaire neuf, échelle 1, 05/10/2026 — fenêtre de 1400 × 875, non recadrée | CC0 | Geste 1 — Ouvrir : le bouton de l'activité 3, avec la consigne « Nomme ton projet… » | 40 Ko |
| `Images/geste_vitta_1c_ouvrir_editeur.png` | **Capture d'écran réelle** (règle n°94) | Vittascience (page seule), Chrome 154 piloté par Playwright, **profil temporaire neuf**, **sans compte**, mode mixte, thème sombre, échelle 1, poste de Pascal, 05/10/2026 | CC0 | Geste 1 — Ouvrir : l'éditeur en mode mixte, avec le bloc « afficher Bonjour » | 29 Ko |
| `Images/geste_vitta_2_nommer_fenetre.png` | **Capture d'écran réelle** (règle n°94) | Vittascience (page seule), Chrome 154 piloté par Playwright, **profil temporaire neuf**, **sans compte**, mode mixte, thème sombre, échelle 1, poste de Pascal, 05/10/2026 | CC0 | Geste 2 — Nommer : la fenêtre « Modifier les informations du projet » | 34 Ko |
| `Images/geste_vitta_2b_nommer_resultat.png` | **Capture d'écran réelle** (règle n°94) | Vittascience (page seule), Chrome 154 piloté par Playwright, **profil temporaire neuf**, **sans compte**, mode mixte, thème sombre, échelle 1, poste de Pascal, 05/10/2026 | CC0 | Geste 2 — Nommer : le nom du projet en haut à gauche | 29 Ko |
| `Images/geste_vitta_3_retrouver_ouvrir.png` | **Capture d'écran réelle** (règle n°94) | Vittascience (page seule), Chrome 154 piloté par Playwright, **profil temporaire neuf**, **sans compte**, mode mixte, thème sombre, échelle 1, poste de Pascal, 05/10/2026 | CC0 | Geste 3 — Retrouver : « Ouvrir un projet », onglet « Depuis votre appareil » | 33 Ko |
| `Images/geste_vitta_3b_retrouver_confirmer.png` | **Capture d'écran réelle** (règle n°94) | Vittascience (page seule), Chrome 154 piloté par Playwright, **profil temporaire neuf**, **sans compte**, mode mixte, thème sombre, échelle 1, poste de Pascal, 05/10/2026 — l'avertissement « Est-ce que vous êtes sûr de vouloir importer ce fichier… ? » vu après le choix du fichier | CC0 | Geste 3 — Retrouver : la confirmation, boutons Oui et Non | 33 Ko |
| `Images/geste_vitta_3c_retrouver_resultat.png` | **Capture d'écran réelle** (règle n°94) | Vittascience (page seule), Chrome 154 piloté par Playwright, **profil temporaire neuf**, **sans compte**, mode mixte, thème sombre, échelle 1, poste de Pascal, 05/10/2026 — le fichier est celui téléchargé au geste 4 (4e-JARDIN-DUPONT_202695_3431.py), choisi par le pilote de test ; programme de l'activité 3, exécuté, console POMPE ON | CC0 | Geste 3 — Retrouver : le programme revenu en blocs et en Python, avec son nom | 44 Ko |
| `Images/geste_vitta_4_sortir_telecharger.png` | **Capture d'écran réelle** (règle n°94) | Vittascience (page seule), Chrome 154 piloté par Playwright, **profil temporaire neuf**, **sans compte**, mode mixte, thème sombre, échelle 1, poste de Pascal, 05/10/2026 — fenêtre « Sauvegarder le projet » **sans compte** : « Je me connecte », « Je m'inscris ! », puis « Télécharger » | CC0 | Geste 4 — Sortir : la disquette, puis le bouton Télécharger | 32 Ko |
| `Images/geste_vitta_4b_sortir_telechargements.png` | **Capture d'écran réelle** (règle n°94) | Explorateur de fichiers Windows (fenêtre seule, rétrécie à une ligne), poste de Pascal, 05/10/2026 — recadrée de 8 px sur chaque bord (bord transparent de la fenêtre) ; la fenêtre est rétrécie pour que le fil d'Ariane se replie et qu'aucun autre élément ne soit montré | CC0 | Geste 4 — Sortir : le fichier .py dans Téléchargements | 51 Ko |
| `Images/geste_vitta_4c_sortir_nouveau_dossier.png` | **Capture d'écran réelle** (règle n°94) | **Reprise octet pour octet** de `4e_C6.2/Images/geste_vitta_4c_sortir_nouveau_dossier.png` (Explorateur de fichiers, fenêtre seule, rétrécie à une ligne, poste de Pascal, 04/10/2026) : aucun nom de fichier ni de classe visible | CC0 | Geste 4 — Sortir : Documents, nouveau dossier à renommer | 48 Ko |
| `Images/geste_vitta_4d_sortir_nom_de_classe.png` | **Capture d'écran réelle** (règle n°94) | **Reprise octet pour octet** de `4e_C6.2/Images/geste_vitta_4d_sortir_nom_de_classe.png` (même fenêtre, 04/10/2026) : le nom de classe 4E3 saisi | CC0 | Geste 4 — Sortir : le nom 4E3 saisi | 46 Ko |
| `Images/geste_vitta_4e_sortir_resultat.png` | **Capture d'écran réelle** (règle n°94) | Explorateur de fichiers Windows (fenêtre seule, rétrécie à une ligne), poste de Pascal, 05/10/2026 — recadrée de 8 px sur chaque bord (bord transparent de la fenêtre) ; le fil d'Ariane se replie en « Documents › 4E3 » | CC0 | Geste 4 — Sortir : Documents › 4E3 contient le fichier | 51 Ko |
