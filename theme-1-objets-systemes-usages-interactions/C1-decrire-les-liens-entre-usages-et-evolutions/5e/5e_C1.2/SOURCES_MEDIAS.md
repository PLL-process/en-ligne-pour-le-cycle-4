# Sources et licences des médias — lot 5e_C1.2 (Sainte-Luce)

## Principe (règle d'or n°1)

Aucune image de ce lot ne vient d'une recherche d'images, d'un scan ni d'un site tiers. Les
**quatre SVG** sont des originaux écrits à la main, sous **CC0** (domaine public), avec `<title>`
et `<desc>` accessibles — un lecteur d'écran restitue l'intégralité du document, pas une étiquette.

| Fichier | Ce qu'il donne à lire | `desc` | Origine |
|---|---|---|---|
| `Images/corrige_trois_principes_de_freinage.svg` | **Corrigé** : ce qui serre quoi dans les trois principes, et la distinction fonction / principe / solution | 1 315 car. | écrit pour ce lot (Fable, 09/08/2026) |
| `Images/corrige_le_critere_qui_tranche.svg` | **Corrigé** : le tableau renseigné, le meilleur et le moins bon de chaque colonne, et le piège du décompte | 1 694 car. | écrit pour ce lot (Fable, 09/08/2026) |
| `Images/comparer_freins_velo.svg` | schéma de comparaison hérité du lot précédent | — | hérité, conservé |
| `Images/eclairer_principes.svg` | trois principes d'éclairage, sert le Bonus 2 | — | hérité, conservé |

Aucune police externe n'est appelée : pile système, et la page fonctionne **hors ligne**
(règle n°40).

## Les jeux de données

Tous **simulés** et **déterministes** (règle n°48), et la séquence le dit à l'élève.

| Fichier | Contenu | Cohérence |
|---|---|---|
| `donnees_freinage_sainte_luce_simulees.csv` | 3 solutions × 6 critères | — |
| `releves_essai_college_sainte_luce_simules.csv` | 15 freinages, avec pente et état de chaussée | **la fiche est la moyenne exacte des essais** — l'élève peut la retrouver |

Les ordres de grandeur (distances d'arrêt, masses, coûts d'entretien) sont **plausibles et
arrondis**, à usage pédagogique. Ils ne valent pas fiche technique de fournisseur, et aucun
fournisseur réel n'est nommé.

## Ce que le lot ne contient pas

- aucune photographie, aucune capture d'écran de logiciel — les modes opératoires tableur sont
  **écrits**, pour LibreOffice Calc et Excel ;
- aucun appel réseau, aucune police distante, aucun script tiers ;
- aucune marque de fabricant.

## Le matériel réel

La manipulation de la séance 1 demande **un vélo**, quel qu'il soit, et une clé Allen. Aucun
matériel n'est à acheter, rien n'est démonté, et la très basse tension n'entre pas en jeu — il n'y a
pas d'électricité dans ce lot.

## Deux SVG présents mais employés par aucune page (relevé du 31/08/2026)

Ces deux fichiers sont, comme les autres, des **créations originales (Fable, CC0)**, du SVG écrit
à la main, sans raster embarqué ni référence distante. Ils sont documentés ici pour que leur
licence ne dépende de personne. Mais **aucune page du lot ne les affiche** :

| Fichier | Titre porté par le SVG | Poids |
|---|---|---|
| `Images/comparer_freins_velo.svg` | Comparer deux principes de freinage | ~2 Ko |
| `Images/eclairer_principes.svg` | Deux principes pour éclairer | ~2 Ko |

À trancher, pas à deviner : schémas devenus sans emploi et à retirer, ou images-objets dont le
câblage dans la séquence a été oublié. `_outils/controle_medias.py` les compte et les nomme sans
les refuser : un fichier inemployé est une dette, pas un mensonge.
