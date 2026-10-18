# Sources des médias — archive 3e_C9.1 (séance « Vittascience en blocs » 5e – 4e et son évaluation notée)

Les captures `Images/capture-*.png` et `Images/install-manager-*.png` viennent de la ressource héritée,
archivée avec elle (voir `README.md`).

## Captures des programmes en blocs (règle d'or n°308, lot 1 — 18/10/2026)

Un bloc ne se dessine pas, il se capture. Chaque programme a été **construit dans Vittascience Python,
exécuté, puis capturé** : Chrome 155 piloté par Playwright, **profil de navigateur temporaire, neuf et jamais
connecté** (aucun compte, aucun mot de passe, aucune extension), thème par défaut de ce profil (clair),
**zoom par défaut de l'éditeur (0,9)**, échelle 1, poste de Pascal. Le Python du programme est tapé dans le volet
du mode mixte ; les blocs que Vittascience en tire sont relus un à un ; le programme est réassemblé et exécuté en
**mode blocs**, à partir du Python que Vittascience génère depuis les blocs. Le cadre est la boîte des blocs seuls,
plus 12 px de fond d'espace de travail : ni boîte à outils, ni volet de code, ni corbeille, ni bouton de zoom,
aucun bloc sélectionné. Réduction en 256 couleurs (`reduire.py` du thème 1) : les couleurs des catégories
survivent à ±2 par canal, vérifié pixel par pixel sur les captures brutes, gardées hors du dépôt.

| Fichier | Nature | Origine | Licence | Usage | Poids |
|---|---|---|---|---|---|
| `Images/bloc_vitta_B01.png` | **Capture d'écran réelle** (règles n°94, n°308) | Vittascience Python, 18/10/2026, poste de Pascal, recadrée sur les blocs, 270 × 76 | CC0 | Séance, « Rappel rapide » : le bloc « affecter à x la valeur 14 ». Console : rien (aucun bloc afficher). | 3 Ko |
| `Images/bloc_vitta_B18.png` | **Capture d'écran réelle** (règles n°94, n°308) | Vittascience Python, 18/10/2026, poste de Pascal, recadrée sur les blocs, 684 × 630. Les trois blocs « et » sont en **« Entrées externes »** (clic droit sur le bloc, rendu réel de Vittascience) : en entrées en ligne, le programme mesure 1 357 px de large | CC0 | Séance, Ex. 10 · évaluation, Ex. 1 (programme fourni) : l'arrosage. Console : `1`, comme la page l'attend. | 25 Ko |
| `Images/bloc_vitta_B31.png` | **Capture d'écran réelle** (règles n°94, n°308) | Vittascience Python, 18/10/2026, poste de Pascal, recadrée sur les blocs, 366 × 277. Vittascience n'a **pas** de bloc « couleur du stylo » : le premier bloc est « définir le tracé de couleur ● largeur 5 » de la catégorie Turtle, couleur rouge (#ff0000), largeur laissée à sa valeur de boîte à outils | CC0 | Séance, Bonus 9 · évaluation, Ex. 2 (programme fourni) : le triangle. Exécution : un triangle rouge, aucune ligne en console. | 8 Ko |
