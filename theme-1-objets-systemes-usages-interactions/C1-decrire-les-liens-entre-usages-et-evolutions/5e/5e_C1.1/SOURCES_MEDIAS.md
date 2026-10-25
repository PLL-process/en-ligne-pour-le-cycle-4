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
| `Images/geste_activite2_trier_1_menu.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 13/09/2026 | activité 2, geste Trier — A1:E91 sélectionné, menu Données déroulé, « Trier… » surligné (fenêtre entière) | CC0 | 173 Ko |
| `Images/geste_activite2_trier_1b_boite.png` | capture d'écran réelle, boîte de dialogue LibreOffice Calc 26.2.5.2 (fr), mode sombre, 13/09/2026 | activité 2, geste Trier — la boîte « Trier » réglée : pm25_ug_m3, Croissant, étiquettes de colonne cochées (boîte seule) | CC0 | 44 Ko |
| `Images/geste_activite2_trier_2_resultat.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 13/09/2026 | activité 2, geste Trier — résultat : −4,2 en ligne 2, chaque relevé déplacé entier (fenêtre entière) | CC0 | 126 Ko |
| `Images/geste_activite2_trier_3_erreur_etendre.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 13/09/2026 | activité 2, geste Trier — erreur typique : C1:C91 seule sélectionnée, boîte « Trier la plage » (Étendre la sélection / Sélection active / Annuler) (fenêtre entière) | CC0 | 183 Ko |
| `Images/geste_activite2_formule_1_saisie.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 13/09/2026 | activité 2, geste Moyenne — =MOYENNE(C2:C91) en cours de saisie en C92, pas encore validée (fenêtre entière) | CC0 | 107 Ko |
| `Images/geste_activite2_formule_2_resultat.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 13/09/2026 | activité 2, geste Moyenne — résultat 27,363333333 dans C92, la formule encore dans la barre (fenêtre entière) | CC0 | 108 Ko |
| `Images/geste_activite2_formule_3_erreur_sans_egal.png` | capture d'écran réelle, LibreOffice Calc 26.2.5.2 (fr), mode sombre, 13/09/2026 | activité 2, geste Moyenne — erreur typique : MOYENNE(C2:C91) sans le =, affiché comme du texte en C93 (fenêtre entière) | CC0 | 108 Ko |

## L'animation des trois principes et sa voix (activité 1, ajoutée le 25/10/2026)

**L'animation** (bloc `#trois-principes-pas-a-pas` de la séquence) est une **création originale** : SVG et JavaScript écrits à la
main dans la page, sans bibliothèque, sans image externe, sans réseau. Auteur : écosystème Pascal/Claude (Fable), licence **CC0 1.0**,
comme les schémas du lot. À l'écran, elle remplace les trois schémas fixes de la planche ; ceux-ci restent dans la page et
**s'impriment** (rien ne change sur papier). Couleurs de la planche conservées : P1 bleu, P2 vert, P3 violet. Les nombres de
l'étape 7 (20 µg dans 2 m³, soit 10 µg/m³) sont ceux de l'encadré « D'abord, ce qu'on mesure », pour qu'il n'y ait qu'un exemple.

**La voix : synthèse neuronale, hors ligne. Aucune voix humaine enregistrée.** Les onze fichiers sont engendrés par
`_generation/voix_trois_principes/generer.py` à partir des onze phrases de l'animation, lues mot pour mot (le script refuse de
produire si une phrase de la page a changé). Les phrases des étapes ①②③ sont celles des cartes P1, P2, P3.

| Fichier | Nature |
|---|---|
| `Audio/trois-principes_scene1.ogg` · `.mp3` | Étape 1 : voix de synthèse, Opus mono 32 kb/s (36.2 Ko) et MP3 mono 48 kb/s de secours (52.7 Ko) |
| `Audio/trois-principes_scene2.ogg` · `.mp3` | Étape 2 : voix de synthèse, Opus mono 32 kb/s (18.7 Ko) et MP3 mono 48 kb/s de secours (27.1 Ko) |
| `Audio/trois-principes_scene3.ogg` · `.mp3` | Étape 3 : voix de synthèse, Opus mono 32 kb/s (12.2 Ko) et MP3 mono 48 kb/s de secours (17.1 Ko) |
| `Audio/trois-principes_scene4.ogg` · `.mp3` | Étape 4 : voix de synthèse, Opus mono 32 kb/s (37.9 Ko) et MP3 mono 48 kb/s de secours (55.6 Ko) |
| `Audio/trois-principes_scene5.ogg` · `.mp3` | Étape 5 : voix de synthèse, Opus mono 32 kb/s (14.2 Ko) et MP3 mono 48 kb/s de secours (19.9 Ko) |
| `Audio/trois-principes_scene6.ogg` · `.mp3` | Étape 6 : voix de synthèse, Opus mono 32 kb/s (8.8 Ko) et MP3 mono 48 kb/s de secours (12.7 Ko) |
| `Audio/trois-principes_scene7.ogg` · `.mp3` | Étape 7 : voix de synthèse, Opus mono 32 kb/s (18.3 Ko) et MP3 mono 48 kb/s de secours (26.2 Ko) |
| `Audio/trois-principes_scene8.ogg` · `.mp3` | Étape 8 : voix de synthèse, Opus mono 32 kb/s (22.3 Ko) et MP3 mono 48 kb/s de secours (31.7 Ko) |
| `Audio/trois-principes_scene9.ogg` · `.mp3` | Étape 9 : voix de synthèse, Opus mono 32 kb/s (8.8 Ko) et MP3 mono 48 kb/s de secours (12.1 Ko) |
| `Audio/trois-principes_scene10.ogg` · `.mp3` | Étape 10 : voix de synthèse, Opus mono 32 kb/s (36.3 Ko) et MP3 mono 48 kb/s de secours (52.3 Ko) |
| `Audio/trois-principes_scene11.ogg` · `.mp3` | Étape 11 : voix de synthèse, Opus mono 32 kb/s (41.5 Ko) et MP3 mono 48 kb/s de secours (59.7 Ko) |

- **Moteur** : Piper (`piper-tts` 1.8.0), sous GPL-3. Il n'est pas dans le dépôt, et un fichier audio qu'il produit n'est pas une œuvre dérivée du moteur.
- **Modèle** : `fr_FR-siwis-medium`, la voix choisie par Pascal le 21/10/2026 pour le vélo-cargo (5e_C3.1), entraînée sur la base **SIWIS**
  de l'Université d'Édimbourg (datashare.is.ed.ac.uk/handle/10283/2353). Le fichier du modèle a été pris le 25/10/2026 dans la redistribution
  GitHub de `k2-fsa/sherpa-onnx` (version `tts-models`, archive `vits-piper-fr_FR-siwis-medium.tar.bz2`), le dépôt d'origine
  (`rhasspy/piper-voices`, Hugging Face) n'étant pas joignable ; empreintes et mesures de comparaison avec les prises du vélo-cargo dans
  `_generation/voix_trois_principes/voix.json`.
- **Licence** : **CC BY 4.0** (fiche `MODEL_CARD` livrée avec le modèle). La licence de la base d'entraînement est celle que la fiche
  déclare ; l'origine des enregistrements n'a pas été vérifiée plus loin.
- **Attribution exigée** : « Voix de synthèse Piper « fr_FR-siwis-medium », entraînée sur la base SIWIS (Université d'Édimbourg), CC BY 4.0. »
  Elle figure ici, dans `voix.json` et, en version courte (« Voix de synthèse : SIWIS (CC BY 4.0) »), sous l'animation.
- **Chaîne audio** : celle du vélo-cargo — silences du début et de la fin coupés (−45 dB), volume normalisé à −16 LUFS (mesuré : −16,9 à −15,6
  sur quatre fichiers), crête −1,5 dB, mono.
- **Texte envoyé à la voix** : celui de la page, sauf aux étapes 2 (parenthèses dites entre virgules), 5 (« 24 h » dit « vingt-quatre heures »)
  et 11 (« µg/m³ » dit « microgrammes par mètre cube ») ; phonèmes corrigés aux étapes 4, 5, 6 et 8 (liaisons fausses d'espeak-ng).
  Détail dans `phrases.json`.
- **Prises NON ÉCOUTÉES** au 25/10/2026 : produites, mesurées (durée, volume), pas validées à l'oreille. **L'écoute de Pascal valide, ou
  demande une correction** ; la trace s'écrit dans `voix.json` (clé `prises`). Reproductibilité à l'octet : non (Piper tire du bruit à chaque prise).
- **Dans la page** : rien n'est chargé depuis le réseau ; les fichiers ne se lisent qu'après un geste de l'élève (« Écouter » ou
  « Regarder ») ; si un fichier ne se lit pas, la voix française locale du navigateur prend le relais, sinon l'élève lit la phrase.

**Les captures de comparaison** de la PR, dans `_generation/animation_trois_principes/captures/` : `avant-390-planche.png`
(la planche telle que `main` l'affichait, schémas fixes) et `apres-390-planche.png` (la même position, avec l'animation),
à 390 px ; `apres-1280-onze-etapes.png` (les onze étapes, à 1280 px, réduites). Captures du navigateur de ce lot (Chromium),
25/10/2026, quantifiées à 256 couleurs, CC0. Elles ne sont affichées par aucune page élève.

## Ce que le lot ne contient pas

- aucune photographie ;
- aucun appel réseau, aucune police distante, aucun script tiers ;
- aucune voix humaine enregistrée (la voix de l'animation est une synthèse, ci-dessus).

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
