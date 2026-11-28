# Sources des médias — 3e_C6.2 « L'auto-test de la station »

**Règle d'or n°1 du dépôt** : chaque image est un document à lire, produite pour le dépôt,
sous licence libre, avec `<title>` et `<desc>` accessibles. Aucune capture de logiciel
propriétaire, aucune image trouvée sur un moteur de recherche, aucun hotlinking.

## Les trois figures de ce lot

| Fichier | Nature | Auteur | Licence | Rôle pédagogique |
|---|---|---|---|---|
| `Images/algorigramme_auto_test.svg` | SVG original, écrit à la main | Fable (agent Thème 2), pour ce dépôt | CC0 1.0 (domaine public) | L'algorigramme complet de la fonctionnalité : compteur avant la boucle, boucle sur les quatre organes, décision unique après la boucle |
| `Images/symboles_algorigramme.svg` | SVG original, écrit à la main | Fable (agent Thème 2), pour ce dépôt | CC0 1.0 (domaine public) | La planche des cinq symboles normalisés et de ce que chacun promet (une flèche entre, deux sortent…) |
| `Images/trace_banc_essai.svg` | SVG original, écrit à la main | Fable (agent Thème 2), pour ce dépôt | CC0 1.0 (domaine public) | La trace d'une exécution ligne à ligne, avec le compteur qui ne redescend pas et le cas de la défaillance silencieuse |

Les trois fichiers sont du SVG écrit directement (pas d'export d'un logiciel), sans police
embarquée, sans image tramée incluse, sans référence réseau. Ils s'affichent hors ligne.

## Accessibilité des figures

Chaque SVG porte un `<title>` court et un `<desc>` long qui **décrit le contenu, pas
l'apparence** : un élève qui n'accède qu'au texte alternatif doit pouvoir répondre à la
question posée. Les trois descriptions font de 585 à 700 caractères. Dans le QCM, l'attribut
`alt` reprend la même information sous forme condensée.

Aucune information n'est portée par la seule couleur : les branches d'un losange sont
étiquetées en toutes lettres (« oui », « non »), et dans la trace les réponses sont écrites
« vrai » et « FAUX » en plus d'être colorées.

## Les fichiers hérités du dossier

`sequence_algorigrammes_dnb.html` et `qcm_algorigrammes_dnb.html` contiennent leurs propres
SVG **inline** (13 schémas), produits avec la banque d'entraînement DNB avant ce lot. Ils ne
sont pas modifiés ici : ils restent la propriété éditoriale de leur auteur d'origine et sont
référencés comme ressource d'appui. Aucun de leurs médias n'a été copié dans les figures
ci-dessus.

## Polices

`Poppins` et `Fira Code` sont appelées depuis Google Fonts par la séquence et le QCM, comme
dans tout le dépôt (SIL Open Font License 1.1). En l'absence de réseau, la page bascule sur
la police système : aucune information n'est perdue.

## L'entraînement DNB : douze algorigrammes écrits dans la page (révision du 21/11/2026)

Depuis la révision qui suit l'audit du 21/11/2026, `entrainement_dnb_algorigrammes.html` ne charge plus aucune image :
ses **douze algorigrammes** sont des SVG originaux, **CC0 1.0**, écrits dans la page par `_outils/dnb_schemas.py`
(Fable, agent Thème 2) — ventilateur, compteur qui remonte, boucle qui ne tourne pas, auto-test à trois emplacements,
auto-test complet, auto-test annoté (correction), deux voyants du Lamentin (rappel), serre à deux seuils, lampadaire,
tri des déchets, porte automatique, abri à vélos (épreuve). Mêmes conventions partout : parallélogramme pour lire,
envoyer, afficher ou commander ; étiquette « oui » / « non » contre le segment qu'elle nomme. Chacun porte un `<title>`
et un `<desc>` qui décrivent le contenu, et la page affiche la même description en étapes (« 📝 Le schéma, en texte »).

Deux fichiers du lot ont changé avec lui, parce que le QCM s'en sert aussi :
- `Images/algorigramme_auto_test.svg` est **régénéré** par `dnb_schemas.py --fichiers` (le même dessin que l'exemple
  guidé de la correction) : les envois au gardien sont des parallélogrammes, le libellé « non » est contre la flèche
  qui descend, et la description ne dit plus que le message nomme les organes (un compteur ne retient qu'un nombre) ;
- `Images/symboles_algorigramme.svg` : ses textes disent « cinq repères… il en existe d'autres », et les bornes
  « d'un traitement qui se termine ».

`Images/trace_banc_essai.svg` n'est plus utilisé par l'entraînement ; le QCM le garde (son message cite les organes,
comme l'algorithme de l'atelier, qui les mémorise dans une liste).

## Image générée par IA (Canva) pour la synthèse élève

Demande de Pascal du 29/10/2026 : « une capture d'écran ou une illustration permet d'avoir une vision plus synthétique
de l'objet » ; Canva autorisé « pour des images réalistes et autres ». Règles : skill `synthese-vulgarisee`, §4.

| Fichier | Ce qu'elle montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/synthese_station_alerte.png` | La station d'alerte cyclonique sur le toit d'un collège : mât, anémomètre, girouette, panneau solaire, sirène, gyrophare, boîtier ; la mer au loin. PNG 1 536 × 1 024, 2.0 Mo. | **Image générée par IA** avec Canva (génération d'image), compte de Pascal, 29/10/2026. Demande : « Realistic photo of a small autonomous cyclone warning station on a galvanized steel mast on the flat roof of a school in Martinique: cup anemometer and wind vane at the top, a small solar panel on a side arm, a white weatherproof electronics box, a horn siren and a small orange beacon light mounted on the mast, a short radio antenna, the sea in the distance, cloudy sky, no people, no text, no logos, the whole mast visible » | Conditions Canva AI Product Terms : l'image appartient à Pascal, sans attribution exigée ; interdit de la présenter comme faite par un humain (légende « Image générée par IA (Canva) ») et d'en retirer les métadonnées de provenance (manifeste C2PA et XMP Canva gardés : **fichier non modifié**, d'où son poids). | Synthèse élève, carte « Ce que je dois retenir » ; et la situation déclenchante de la séquence (05/11/2026) |

## Document du QCM (28/11/2026, n°345)

| Fichier | Ce qu'il montre | Provenance | Droits | Où |
|---|---|---|---|---|
| `Images/doc_programme_auto_test.svg` | Le programme de l'auto-test, indenté, sans dire ce qu'il produit dans un cas donné. | SVG original, dessiné par `_outils/document_qcm.py` depuis `documents_qcm_3e_C6.2.json`, lui-même LU dans la correction de l'activité 3 (« 1. » à « 8. », et l'instruction manquante) par `documents_qcm.py`. | CC0, comme les images du dépôt | QCM, q7, q17, q18, q19 |

