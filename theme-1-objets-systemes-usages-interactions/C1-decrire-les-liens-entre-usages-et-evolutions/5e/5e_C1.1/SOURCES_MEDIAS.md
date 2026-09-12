# Sources et licences des médias — lot 5e_C1.1 à C1.6 (Chengdu)

## Principe (règle d'or n°1)

Aucune image de ce lot ne vient d'une recherche d'images, d'un scan, ni d'un site tiers. **Les
quatre schémas sont des SVG originaux**, écrits à la main pour cette séquence, placés sous **CC0**
(domaine public), et portant chacun un `<title>` et un `<desc>` accessibles — un lecteur d'écran
restitue l'intégralité du document, pas une étiquette.

Chaque image est un **document à lire**, pas une décoration : si on la retire, une information
disparaît de la séquence.

## Les quatre schémas

| Fichier | Ce qu'il donne à lire | `desc` |
|---|---|---|
| `Images/trois_principes_de_mesure.svg` | Les trois principes de mesure des poussières, chacun avec un schéma en trois étapes, une comparaison familière (le rayon de soleil, le sac d'aspirateur, la lampe derrière un rideau), son délai, sa précision, son prix et ce qu'il exige. Redessiné le 09/09/2026 pour des élèves de 5e ; la séquence en porte la version détaillée (cartes, tableau des chiffres, lecture du µg/m³). Sans lui, le QCM et la synthèse n'ont pas de document. | 1 387 car. |
| `Images/corrige_arborescence.svg` | **Corrigé** (règle n°43) : les quatorze entrées mal nommées à gauche, l'arborescence rangée à droite, et les quatre règles de nommage. | 1 384 car. |
| `Images/corrige_systeme_information.svg` | **Corrigé** : les quatre étages du système d'information, et pour chacun qui a le droit d'y écrire. | 1 360 car. |
| `Images/la_donnee_qui_designe.svg` | Les trois publications du même fait vrai — nommer l'agent, taire la cause, désigner l'organisation. C'est le document central de la séance 5. | 1 476 car. |

Auteur : **Fable**, agent de production du dépôt, pour ce lot. Licence **CC0 1.0**.
Aucune police externe n'est appelée : les schémas utilisent la pile système
(`Segoe UI, system-ui, sans-serif`), et la page fonctionne **entièrement hors ligne** (règle n°40).

## Les jeux de données

Tous **simulés**, et la séquence le dit à l'élève en toutes lettres. Ils sont **déterministes**
(règle n°48) : les valeurs sur lesquelles s'appuie un corrigé sont fixées, pas tirées au sort — un
corrigé qui dépendrait d'un tirage serait faux à la régénération suivante.

| Fichier | Contenu | Ce qui y est planté |
|---|---|---|
| `releves_air_chengdu_simules.csv` | 90 relevés horaires — 7 jours × 13 h, moins une ligne ; séparateur `;`, **virgule décimale** depuis le 12/09/2026 | les quatre anomalies, et le pic du mardi et jeudi 7 h |
| `principes_mesure_poussieres_simules.csv` | Les trois principes et leurs cinq critères | rien — ce sont des ordres de grandeur réalistes |
| `arborescence_actuelle_simulee.csv` | 14 entrées mal nommées | les six défauts de nommage travaillés en séance 3 |

**Aucune donnée réelle, aucune personne réelle.** L'agent d'entretien de la séquence est une
construction ; la fiche pédagogique prévient qu'un élève pourra malgré tout nommer une personne de
son collège, et ce qu'il faut en faire.

Les ordres de grandeur des trois principes de mesure (temps de réponse, incertitude, prix,
consommation) sont **plausibles et arrondis**, à usage pédagogique : ils permettent de comparer, ils
ne valent pas fiche technique.

## Les quinze captures de gestes

Les **captures de gestes** sont des captures d'écran réelles, prises sur le poste en suivant
l'encart « Avant de commencer (échauffement) » geste par geste (règles d'or n°94, 70, 121, 127,
75). Sept montrent LibreOffice Calc, sept les **boîtes de dialogue de Windows** — celles que
LibreOffice utilise par défaut, donc celles que l'élève verra —, une l'Explorateur de fichiers.
Toutes sont en **mode sombre**, le thème du poste : l'élève voit une seule interface d'un bout
à l'autre de l'encart.

Elles montrent le fichier de **ce lot**, `releves_air_chengdu_simules.csv`, et son classeur
`5E-AIR-DUPONT.ods` : treize des quinze portent ce nom, ou celui de la classe. Elles ne sont
donc pas reprises du lot pilote `4e_C1.1` — un élève de 5e doit voir un fichier de 5e.

Aucune retouche : le geste est désigné dans la légende, pas sur l'image ; seuls le cadrage,
la réduction à 1400 px de large et la quantification à 256 couleurs ont été appliqués. Le
cadrage suit deux règles, tenues image par image avant intégration : **aucune capture ne
montre le nom du compte** — les fenêtres ont été rétrécies jusqu'à ce que le fil d'Ariane se
replie en « … › Documents › 5E1 » — et **aucune ne montre le contenu du dossier Documents**
du poste : les deux vues qui l'ouvrent sont recadrées au bandeau du haut, fil d'Ariane et
barre d'outils, et les deux qui suivent la création du dossier n'affichent que la ligne de
ce dossier. Le volet de navigation, qui listait des dossiers personnels, est masqué partout.

| Fichier | Type | Usage pédagogique (règle v2) | Licence | Poids |
|---|---|---|---|---|
| `Images/geste_tableur_1_ouvrir_import_csv.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 11/09/2026 | geste 1 Ouvrir — la boîte « Import de texte » pour `releves_air_chengdu_simules.csv`, Point-virgule seul coché, aperçu en cinq colonnes où pm25_ug_m3 montre 24,3 à la virgule (encart d'échauffement de la séquence) | CC0 | 126 Ko |
| `Images/geste_tableur_1b_ouvrir_resultat.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 11/09/2026 | geste 1 Ouvrir — résultat attendu : cinq colonnes A à E, et les valeurs alignées à droite, donc reconnues comme des nombres (encart d'échauffement de la séquence) | CC0 | 126 Ko |
| `Images/geste_tableur_1c_ouvrir_erreur_separateur.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 11/09/2026 | geste 1 Ouvrir — contre-exemple : séparateur Virgule, la ligne de titres tassée dans la colonne A et chaque relevé coupé en quatre au milieu de ses nombres (encart d'échauffement de la séquence) | CC0 | 133 Ko |
| `Images/geste_tableur_2_nommer_documents.png` | capture d'écran réelle, boîte de dialogue Windows 11 (fr), mode sombre, recadrée au bandeau du haut, 11/09/2026 | geste 2 Nommer — « Enregistrer sous » ouverte sur Documents : fil d'Ariane et barre d'outils seuls, aucun dossier du poste visible (encart d'échauffement de la séquence) | CC0 | 13 Ko |
| `Images/geste_tableur_2b_nommer_bouton_nouveau_dossier.png` | capture d'écran réelle, boîte de dialogue Windows 11 (fr), mode sombre, recadrée au bandeau du haut, 11/09/2026 | geste 2 Nommer — le bouton « Nouveau dossier » de la boîte Windows, surligné au survol, dans le même bandeau (encart d'échauffement de la séquence) | CC0 | 13 Ko |
| `Images/geste_tableur_2c_nommer_nom_du_dossier.png` | capture d'écran réelle, boîte de dialogue Windows 11 (fr), mode sombre, recadrée au bandeau du haut, 11/09/2026 | geste 2 Nommer — la ligne de saisie du nouveau dossier, 5E1 en cours de frappe, seule ligne de la liste affichée (encart d'échauffement de la séquence) | CC0 | 23 Ko |
| `Images/geste_tableur_2d_nommer_dossier_cree.png` | capture d'écran réelle, boîte de dialogue Windows 11 (fr), mode sombre, recadrée au bandeau du haut, 11/09/2026 | geste 2 Nommer — la même ligne après validation : 5E1 créé, type Dossier (encart d'échauffement de la séquence) | CC0 | 23 Ko |
| `Images/geste_tableur_2e_nommer_enregistrer_sous.png` | capture d'écran réelle, boîte de dialogue Windows 11 (fr), mode sombre, 11/09/2026 | geste 2 Nommer — dans Documents › 5E1 : nom d'exemple 5E-AIR-DUPONT, type Classeur ODF (*.ods) ; le dossier de classe est vide (encart d'échauffement de la séquence) | CC0 | 61 Ko |
| `Images/geste_tableur_2f_nommer_resultat.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 11/09/2026 | geste 2 Nommer — résultat attendu : la barre de titre en .ods (encart d'échauffement de la séquence) | CC0 | 125 Ko |
| `Images/geste_tableur_2g_nommer_explorateur.png` | capture d'écran réelle, Explorateur de fichiers de Windows 11 (fr), mode sombre, 11/09/2026 | geste 2 Nommer — résultat sur le disque : le fil d'Ariane replié en … › Documents › 5E1, un seul fichier dans le dossier (encart d'échauffement de la séquence) | CC0 | 51 Ko |
| `Images/geste_tableur_3_retrouver_avant_ctrl_s.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 11/09/2026 | geste 3 Retrouver — avant Ctrl+S : « moyenne » tapé en A92, sous la dernière ligne de relevés, et l'icône rouge de la barre d'état (non enregistré) (encart d'échauffement de la séquence) | CC0 | 104 Ko |
| `Images/geste_tableur_3b_retrouver_apres_ctrl_s.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 11/09/2026 | geste 3 Retrouver — après Ctrl+S : la même icône redevenue grise (encart d'échauffement de la séquence) | CC0 | 104 Ko |
| `Images/geste_tableur_3c_retrouver_rouvrir.png` | capture d'écran réelle, boîte de dialogue Windows 11 (fr), mode sombre, 11/09/2026 | geste 3 Retrouver — « Ouvrir » dans Documents › 5E1, le .ods sélectionné et son nom complet dans le champ du bas (encart d'échauffement de la séquence) | CC0 | 52 Ko |
| `Images/geste_tableur_4_sortir_clic_droit_graphique.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 11/09/2026 | geste 4 Sortir — le graphique des douze relevés du lundi sélectionné, clic droit ouvert sur Copier et Exporter comme image (encart d'échauffement de la séquence) | CC0 | 144 Ko |
| `Images/geste_tableur_4b_sortir_enregistrer_image.png` | capture d'écran réelle, boîte de dialogue Windows 11 (fr), mode sombre, 11/09/2026 | geste 4 Sortir — « Enregistrer en tant qu'image » dans Documents › 5E1, type PNG (encart d'échauffement de la séquence) | CC0 | 59 Ko |

## Ce que le lot ne contient pas

- aucune photographie ;
- aucun appel réseau, aucune police distante, aucun script tiers.

## Quatre SVG présents mais employés par aucune page (relevé du 31/08/2026)

Ces quatre fichiers sont, comme les autres, des **créations originales (Fable, CC0)**, du SVG
écrit à la main, sans raster embarqué ni référence distante. Ils sont documentés ici pour que
leur licence ne dépende de personne. Mais **aucune page du lot ne les affiche** :

| Fichier | Titre porté par le SVG | Poids |
|---|---|---|
| `Images/collecte_temperature_salles.svg` | Collecte de températures dans quatre salles | ~2 Ko |
| `Images/donnee_information_tableur.svg` | De la donnée à l'information | ~1 Ko |
| `Images/tri_filtre_moyenne.svg` | Trier, filtrer et calculer dans un tableur | ~2 Ko |
| `Images/choisir_graphique.svg` | Choisir un graphique adapté | ~2 Ko |

Deux lectures possibles, et c'est à trancher, pas à deviner : ou bien ces schémas ont été
dessinés pour des activités qui ont changé de forme et n'ont plus de place — alors ils sont à
retirer ; ou bien ils devaient illustrer la séquence et le câblage a été oublié — alors ce sont
quatre images-objets qui manquent à l'élève. `_outils/controle_medias.py` les compte et les
nomme sans les refuser : un fichier inemployé est une dette, pas un mensonge.
