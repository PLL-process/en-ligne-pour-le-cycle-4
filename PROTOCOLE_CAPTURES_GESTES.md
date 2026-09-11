# Prendre les captures de gestes sur le poste, sans exposer le poste

> **Ce fichier a changé de méthode le 11/09/2026.** Sa première version proposait de créer un
> compte Windows `Eleve` en thème clair. Pascal l'a écartée, et pour une raison qui prime :
> **les élèves ont exactement l'affichage de ce poste** — thème sombre, boîtes de dialogue
> Windows par défaut. Une capture prise dans un décor plus propre que la réalité n'aide pas
> l'élève à retrouver son geste : elle lui montre un écran qu'il n'aura jamais. On capture donc
> le poste tel qu'il est, et on protège la vie privée **par le cadrage**, pas par un décor.

Le protocole ci-dessous est celui qui a produit les quinze captures du lot `4e_C1.1`. Il vaut
pour les quatorze pages suivantes : seule la liste des captures change.

---

## 1. Les deux interdits

Ils se vérifient **image par image, avant intégration**, jamais après.

1. **Aucune capture ne montre le nom du compte.**
2. **Aucune capture ne montre le contenu du dossier `Documents`** du poste.

Le reste — barre des tâches, second écran, bureau — ne pose pas de problème : `capwin.ps1` ne
capture qu'une fenêtre.

## 2. Ce que les boîtes Windows donnent gratuitement

Le fil d'Ariane des boîtes de dialogue de Windows **ne nomme pas le compte** : il écrit
« › Documents › », puis « › Documents › 4E3 » une fois dans le dossier de classe. Le premier
interdit est donc tenu sans rien faire pour toutes les boîtes de dialogue.

**L'Explorateur de fichiers, lui, déroule le chemin complet** — « Utilisateurs › <compte> ›
Documents › 4E3 ». Il faut **rétrécir la fenêtre** jusqu'à ce que le fil d'Ariane se replie en
« … › Documents › 4E3 ». Autour de 1500 px de large, c'est fait.

## 3. Ce qu'il faut faire pour le second interdit

Trois gestes, tous de cadrage :

- **Masquer le volet de navigation.** Il liste OneDrive, Dropbox, les dossiers de travail, et il
  déplie `Documents`. Dans une boîte de dialogue : **Organiser → Disposition → Volet de
  navigation**. Dans l'Explorateur : **Afficher → Afficher → Volet de navigation**. À remettre
  après la séance de captures.
- **Recadrer au bandeau du haut** les vues qui ouvrent sur `Documents` : fil d'Ariane et barre
  d'outils, rien en dessous. C'est ce dont l'élève a besoin — vérifier le chemin, trouver le
  bouton — et rien de plus.
- **Rétrécir la boîte à une seule ligne de liste** pour les captures qui suivent la création du
  dossier. Windows garde à l'écran la ligne en cours d'édition : elle devient la seule visible.
  Autour de 1440 px de haut sur ce poste.

Ce ne sont pas des retouches : l'image n'est pas modifiée, c'est le cadre qui est choisi. La
distinction est celle de la règle des médias du dépôt, et elle doit rester lisible dans
`SOURCES_MEDIAS.md`, où chaque ligne dit si la capture est entière ou recadrée.

## 4. Les outils

Tout est dans `_outils/captures-gestes/`.

| script | à quoi il sert |
| --- | --- |
| `capwin.ps1` | capture **une fenêtre seule** (jamais l'écran), par son titre et sa classe |
| `ecran.ps1` | capture une zone d'écran — seul moyen de voir un **menu déroulant**, qui n'appartient pas à la fenêtre |
| `getrect.ps1` | donne le cadre visible d'une fenêtre, en pixels physiques |
| `uia.ps1` | pose, redimensionne, lit et clique par UI Automation ; `-Action poser` est le seul moyen fiable de dimensionner une fenêtre LibreOffice |
| `posewin.ps1` | pose une fenêtre ordinaire, même maximisée ou ancrée |
| `restaurer.ps1` | sort une fenêtre de l'état maximisé et la ramène devant |
| `clic.ps1` | clic gauche, droit ou double, en pixels physiques, **avec vérification** que le curseur est bien arrivé où on le voulait |
| `survol.ps1` | pose le curseur sans cliquer, pour capturer un bouton surligné |
| `frappe.ps1` | envoie des touches **seulement si** la fenêtre attendue a le focus |
| `serie_frappes.ps1` | enchaîne des frappes en revérifiant le focus **avant chacune** |
| `menu_choisir.ps1` | ouvre un menu, y descend au clavier jusqu'à l'entrée voulue, la valide |
| `attendre_fenetre.ps1` | attend qu'une fenêtre soit au premier plan |
| `reduire.py` | 1400 px de large, 256 couleurs, PNG optimisé |
| `inserer_captures.py` | insère les captures dans la page |

## 5. Les six pièges, et leur remède

Chacun a coûté une panne réelle le 10 et le 11/09/2026.

1. **La mise à l'échelle.** Les écrans sont à 175 %. Un PowerShell ordinaire n'est pas conscient
   du DPI : une largeur demandée revient divisée par 1,75 dès qu'une fenêtre change d'écran. Tous
   les outils appellent `SetThreadDpiAwarenessContext(-4)` — conscience **par moniteur v2** — avant
   toute chose. `clic.ps1` relit la position du curseur et refuse d'agir si elle a été mise à
   l'échelle.
2. **LibreOffice réimpose sa taille.** `SetWindowPos` et `SetWindowPlacement` sont ignorés : la
   fenêtre revient à la hauteur de l'écran. Seul `TransformPattern` d'UI Automation
   (`uia.ps1 -Action poser`) obtient la taille voulue. La taille minimale d'une boîte reste
   imposée par son contenu : sur ce poste, 1665 px de haut pour « Import de texte ».
3. **Le titre ne suffit pas à désigner une fenêtre.** La fenêtre de Claude porte dans son titre le
   texte de la conversation : elle a été capturée à la place de l'Explorateur. Toujours passer
   `-Classe` : `CabinetWClass` pour l'Explorateur, `SALFRAME` pour LibreOffice, `#32770` pour une
   boîte de dialogue Windows.
4. **Une frappe égarée agit.** Envoyée à la mauvaise fenêtre, elle ouvre le menu Démarrer,
   enregistre un fichier, ou lance un installeur. **Ne jamais taper sans vérifier le focus** —
   c'est ce que font `frappe.ps1` et `serie_frappes.ps1`. Et **ne pas piloter au clavier un poste
   où PRONOTE, ou tout logiciel qui écrit des données, est ouvert.**
5. **Les menus.** Un clic simulé n'active pas les entrées des menus de l'Explorateur : il faut
   descendre au clavier en relisant, à chaque flèche, quelle entrée porte le focus. Et les
   coordonnées UIA d'un menu déroulant ne sont pas toujours celles de l'écran : `menu_choisir.ps1`
   ne garde que les entrées situées **sous** le point d'ouverture.
6. **Pas d'infobulle** sous un curseur simulé : on capture le bouton surligné, pas sa bulle.

## 6. La marche à suivre, dans l'ordre

1. Fermer tout ce qui n'est pas nécessaire. Un bureau vide, c'est zéro vol de focus.
2. Copier le fichier de départ du lot dans `Téléchargements`.
3. Faire les gestes dans l'ordre de l'encart, en capturant au moment du geste **et** au résultat.
4. Masquer le volet de navigation à la première boîte de dialogue ouverte ; il le reste ensuite.
5. Réduire : `python _outils\captures-gestes\reduire.py brutes finales`.
6. **Relire les images une par une**, contre les deux interdits. C'est ce contrôle qui a manqué au
   lot pilote : une légende annonçait « des dossiers de classes » quand l'image montrait une
   trentaine de dossiers personnels.
7. Intégrer, réécrire `alt` et légendes, mettre à jour `SOURCES_MEDIAS.md` — **poids et dates
   réels**, et la mention du recadrage quand il y en a un.
8. Contrôles du lot, puis navigateur à 1280 px et 390 px.
9. Remettre le poste en état : supprimer le dossier de classe et la copie du fichier de départ,
   réafficher les volets de l'Explorateur, fermer le logiciel.

## 7. Ce qu'on ne touche pas

**Le profil LibreOffice.** Le lot pilote y avait forcé l'apparence claire et les boîtes de
dialogue LibreOffice ; les deux réglages sont abandonnés. Les boîtes Windows par défaut sont
celles que l'élève verra, et le thème sombre est celui de son poste.
