# Paquet de départ — activité 2 « Reconstruire une arborescence réutilisable »

## Pourquoi ce dossier existe

La séquence demandait à l'élève de « renommer et ranger **les six fichiers indiqués par le
professeur** ». Ces six fichiers n'existaient nulle part dans le lot : l'activité, telle qu'elle
était publiée, ne pouvait pas être menée sans que l'enseignant les invente lui-même — avec le
risque que chaque classe travaille sur un jeu différent.

Les voici. Ils sont **volontairement mal nommés** : espaces, accents, majuscules, parenthèses,
tiret cadratin, pas de date, pas de version. C'est ce désordre qui donne son sens à la règle de
nommage `AAAA-MM-JJ_type_contenu_version.ext`.

## Ce que contient le paquet

| Fichier tel qu'il arrive | Ce qu'il est | Destination attendue |
|---|---|---|
| `Données Vélos HANGZHOU (final) v2.csv` | l'extraction brute du 2 mars | `01_donnees_brutes` |
| `analyse stations — copie.csv` | un calcul fait à partir de l'extraction | `02_analyses` |
| `Rapport groupe.txt` | un texte destiné à être diffusé | `03_exports` |
| `plan station 12.svg` | un schéma qui accompagne le rapport | `03_exports` |
| `vieux fichier NE PAS EFFACER.csv` | l'extraction du 24 février | `99_archive` |
| `notes reunion 3 mars.txt` | des notes de travail, plus diffusées | `99_archive` |

## Correction du renommage

| Avant | Après |
|---|---|
| `Données Vélos HANGZHOU (final) v2.csv` | `2026-03-02_donnees_stations-hangzhou_v2.csv` |
| `analyse stations — copie.csv` | `2026-03-02_analyse_taux-occupation_v1.csv` |
| `Rapport groupe.txt` | `2026-03-02_rapport_stations-hangzhou_v1.txt` |
| `plan station 12.svg` | `2026-03-02_schema_station-12_v1.svg` |
| `vieux fichier NE PAS EFFACER.csv` | `2026-02-24_donnees_stations-hangzhou_v1.csv` |
| `notes reunion 3 mars.txt` | `2026-03-03_notes_reunion_v1.txt` |

Le nom d'origine du cinquième fichier — « NE PAS EFFACER » — mérite d'être discuté avec la classe :
c'est une consigne écrite dans un nom de fichier, faute d'un dossier `99_archive`. Ranger, c'est
justement ne plus avoir besoin d'écrire cela.

## Deux pièges volontaires, à exploiter

1. **`ST-05` n'a pas de valeur** dans l'extraction du 2 mars. Ce n'est pas un zéro : le capteur est
   muet. Une case vide et un zéro ne se rangent pas, ne se calculent pas et ne se racontent pas de
   la même façon.
2. **Deux fichiers portent des données de dates différentes.** L'élève qui range sans regarder la
   date met les deux au même endroit — et perd la possibilité de comparer.

## Si la salle informatique tombe

Imprimer les six noms sur des étiquettes et les quatre dossiers sur quatre feuilles A4 : l'activité
se fait sur une table, avec le même raisonnement et la même trace (photo au lieu de capture).
