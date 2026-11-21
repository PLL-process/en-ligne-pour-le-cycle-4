---
name: question-qui-se-lit-seule
description: Lire un QCM question par question pour trouver ce qu'aucun contrôle ne voit — une question qui renvoie à la séquence sans la montrer (« S1 », « du tableau », « dans notre travail »), une liste annoncée et tronquée (« les cinq étapes », quatre citées), un renvoi à une autre année, une notion affichée qui souffle la réponse, une question hors de sa compétence, un leurre d'une autre grandeur, un document qui donne la réponse — puis corriger, changer les questions de souvenir en questions sur document dessiné pour le téléphone, et fermer la séquence par un billet de sortie. À utiliser à chaque audit ou révision de QCM, après `propositions-sans-indice`, et en écrivant toute question neuve. Règles d'or n°343 (clé de voûte), n°344, n°345 ; n°304 et n°330 mesurées.
---

# Une question se lit seule

**Règle d'or n°343 (clé de voûte) — Une question se lit seule.** Pascal, le 21/11/2026 : « ce que les outils ne voient
pas, et que la lecture question par question trouve : il faut en faire des clés de voûte, des règles d'or et des
skills ». Ce skill est la méthode ; `_outils/controle_question_seule.py` est le contrôle de fin de lot.

Né de l'audit du thème 1 du 21/11/2026. Tous les contrôles du dépôt étaient verts sur les 22 QCM du thème. La lecture
des 671 questions a trouvé, entre autres : « Les cinq étapes » du cycle de vie avec quatre étapes dans la bonne
réponse — sous une figure qui en montrait cinq ; « Avec les quatre exigences du centre, combien de solutions
passent ? », sans les exigences ni les solutions ; « En 4e à Hangzhou… » ; la notion « La compétence CRCN 1.2 »
affichée au-dessus de la bonne réponse « CRCN 1.2 — Gérer des données » ; « au gramme près » pour des degrés. Et, en
remontant de la question à la séquence, deux erreurs de fond : « distance et masse vont dans le même sens » (faux pour
le troisième véhicule du tableau) et « F3 tombe sur trois exigences » (elle en rate quatre).

Le test qui résume tout : **l'élève ouvre le QCM trois semaines plus tard, au téléphone, sans la page de la séquence.
Peut-il répondre en raisonnant ?** Si la question demande un chiffre qu'il a vu en classe, elle mesure sa mémoire d'un
tableau, pas sa compétence.

## 0. Mesurer d'abord

```bash
python3 _outils/controle_question_seule.py --chantiers <lot ou thème>   # S1 à S4, E1 (refus) ; D1, P1 (chantiers)
node _outils/mesures_qcm.mjs ; python3 _outils/controle_longueurs.py     # place et longueur (n°137, n°144)
node _outils/controle_indices_qcm.mjs --muet                            # les mots qui désignent (n°341)
node _outils/balayer_questions_qcm.mjs --apres <lot ou thème>           # chaque question jouée à 390 px, avant et après une réponse fausse
```

| Mesure | Ce qu'elle voit | Règle |
|---|---|---|
| S1 | un code sans son nom, sans document : « S2 consomme 165 Wh/km » | n°343 |
| S2 | un renvoi sans document : « du tableau », « dans ce projet », « dans notre travail » | n°343 |
| S3 | une autre année : « en 4e à Hangzhou », « par rapport à la 5e », « au programme de » | n°304 |
| S4 | la notion affichée porte un nombre que seule la bonne réponse reprend | n°341, n°343 |
| E1 | la notion ou l'énoncé annonce N éléments, la bonne réponse en liste un autre nombre | n°344 |
| D1 | moins de six questions sur document dans le QCM d'une séquence | n°345 |
| P1 | une séquence sans billet de sortie | n°330 |
| B1 à B5 | au navigateur, à 390 px : une question ou son aide plus large que l'écran, une figure non décodée, sans description, un document trop petit, une erreur (`balayer_questions_qcm.mjs`) | n°343, n°345 |

Un outil qui ne lit rien est en panne, pas vert (n°299). Et zéro refus ne dit pas que le QCM est bon : la suite se lit.

## 1. Lire question par question — les sept lectures

Sortir la banque en clair, bonne réponse marquée, et la lire d'un trait, comme un élève puis comme un inspecteur.
Pour chaque question, sept vérifications ; la première qui échoue suffit à la reprendre.

1. **Seule (n°343).** Cacher la séquence. Les objets sont-ils nommés ? Les nombres dont dépend la réponse sont-ils
   dans l'énoncé ou dans le document affiché ? « La solution la plus performante du tableau est aussi… » : quel
   tableau ?
2. **Entière (n°344).** « Les cinq étapes », « les six familles », « les trois piliers » : compter les éléments de
   la bonne réponse. Raccourcir une bonne réponse (n°144) raccourcit ses mots, jamais sa liste.
3. **Ici et maintenant (n°304).** Aucune question ne suppose une autre année, une autre séquence, une autre ville :
   les élèves de Pascal n'ont pas fait l'an dernier avec lui. « Dans une autre étude… » dit la même chose.
4. **De sa compétence.** La question évalue-t-elle le code qu'elle porte ? « Par rapport à la 5e, ce qui change… »
   évalue la connaissance du programme ; « ces mots viennent du monde professionnel » est une anecdote. Remplacer par
   une question qui fait faire ce que dit la compétence.
5. **Une seule réponse, conventions de la maison comprises.** Passer la porte A de `qcm-html-accessible` avec les
   conventions du site en tête : la batterie stocke en chimique et fournit en électrique ; « cinétique » pour ce qui
   est mis en mouvement ; les mots de la méthode APTE. Un leurre que la convention rend vrai fait deux bonnes réponses.
6. **La même grandeur.** Un leurre parle la grandeur de la question : pas de « au gramme près » pour une
   température. Et la notion affichée (`n`, écrite sur l'écran de la question) ne dit pas la réponse.
7. **Le document fait trouver.** Une figure sous une question de rappel ne montre pas ce qu'on demande (elle est
   muette, ou elle part). Une figure sous une question de lecture donne les données, jamais le verdict.

**Remonter à la séquence.** Une question qui cloche vient souvent d'une phrase de la séquence qui cloche : chercher
l'énoncé d'origine dans la page, et vérifier son nombre dans le fichier de données du lot. C'est ainsi qu'ont été
trouvés « le même sens » (Shanghai) et « trois exigences » (Hangzhou). Corriger alors la page, son vérificateur, son
banc, sa correction et les synthèses, ensemble (n°338).

## 2. Corriger

| Défaut | Geste |
|---|---|
| Code sans nom | écrire le nom : « la fourgonnette », ou « le vélo-cargo (S1) » si le code sert ailleurs |
| Donnée absente | la mettre dans l'énoncé, ou dans un document sous la question (§ 3) |
| Liste tronquée | citer la liste entière ; donner aux leurres le même nombre d'éléments |
| Autre année | « Dans une autre étude », « Ailleurs », ou retirer |
| Hors compétence | remplacer par une question sur document qui fait faire la compétence |
| Notion qui souffle | renommer la notion (et son piège dans `qcm_aides_<lot>.json`, puis `qcm_aides/poser.py`) |
| Texte sans espace qui pousse l'écran (chemin de fichier, adresse, formule) | `<wbr>` après chaque « / » dans la proposition, et, dans la page, `.option span{min-width:0;overflow-wrap:anywhere}` |

Outils :
- `node _outils/modifier_question_qcm.mjs <qcm.html> <retouches.json>` — réécrit les questions nommées, garde tous
  leurs champs et la forme du gabarit, refuse un énoncé inattendu, un `d` manquant, un `r` hors champ. Chaque
  mauvaise proposition garde son pourquoi, propre à cette proposition, avec l'étape suivante (n°339, n°341).
- Lot à générateur (`_generation/q.py`) : modifier `q.py` ET la page à l'identique, puis comparer les deux banques
  (mêmes énoncés, propositions, bonne réponse, pourquoi, images). Après une régénération, rejouer `document_qcm.py`.
- Garder la place de la bonne réponse (n°137) : réécrire les propositions à leur place, ne pas les déplacer.
- Une notion renommée : mettre à jour les pièges, reposer les aides, vérifier (`poser.py --verifier`).

## 3. D'une question de souvenir à une question sur document (n°345)

Au moins six questions sur document par QCM de séquence. Un document se lit pour répondre : un relevé, une fiche,
un cahier des charges, des barres, une capture réelle d'un logiciel.

1. **Choisir les questions** : d'abord celles que la lecture a trouvées non autonomes ; puis celles qui font
   comparer, calculer, filtrer, lire un seuil.
2. **Écrire les données** dans `documents_qcm_<lot>.json`, à partir du fichier de données du lot (jamais d'un nombre
   inventé à côté ; ce qui est simulé le dit). Blocs : `fiches`, `barres`, `tableau`, `intertitre`.
3. **Dessiner** : `python3 _outils/document_qcm.py <lot>/documents_qcm_<lot>.json`. 350 unités de large, texte de
   15 px et plus — environ 14 px sur un téléphone de 390 px, sans loupe ; fond et couleurs de la charte ; des cadres
   à 16 unités l'un de l'autre ; aucun « ? » ni mot seul en bout de ligne ou de titre ; `<title>` et `<desc>` ; un
   style posé une fois dans le QCM (400 px au plus sur grand écran). Puis `node _outils/controle_schemas.mjs <lot>` :
   aucun ✘, aucun ⚠ sur un `doc_…` (n°315), et chaque document regardé à la taille du téléphone.
4. **Le document donne les données, pas le verdict** : ni coche, ni croix, ni barre mise en évidence. Une case vide
   se montre vide.
5. **Réécrire la question** : elle nomme ce qu'on cherche ; les leurres sont des lectures fausses du document (une
   ligne pour une autre, le nombre au lieu du taux, le prix d'achat au lieu du coût sur dix ans, le cas pile sur le
   seuil compté comme raté) ; chaque pourquoi renvoie à la ligne à relire.
6. **L'`alt`** dit tout ce que montre le document, nombres compris : il permet de répondre sans voir.
7. **Une capture réelle** (tableur, Vittascience, Windows) se prend sur le poste de Pascal, selon
   `PROTOCOLE_CAPTURES_GESTES.md` ; pour un QCM, on la recadre sur ce qu'il faut lire (deux extraits l'un sous
   l'autre restent des extraits : aucun pixel n'est retouché), on nomme le fichier `doc_…`, et `SOURCES_MEDIAS.md` dit
   « capture réelle recadrée » et sa source.
8. **Mettre à jour ce qui annonce le nombre** (n°338) : l'étiquette du QCM, la ligne « Banque », le README, le
   manifeste, la phrase de la séquence, le banc du lot, `q.py` et `build_qcm.py` s'il y en a.

## 4. Fermer la séquence : le billet de sortie (n°330)

Le QCM entraîne ; il ne prouve pas seul (n°28, n°202). La preuve : une production faite seul, sans aide, sur un objet
que la séquence n'a pas étudié. Modèle : `5e_C2.1` (l'abribus), puis les cinq billets du 21/11/2026.

- `<section class="card" id="billetSortie">`, à la fin de la dernière séance, juste avant le Bonus ; environ 5 min,
  à faire tenir dans les 55 minutes de la séance (n°17).
- Un objet proche de l'élève, en Martinique quand c'est possible : la fontaine à eau de la cour, la borne du self, la
  lampe du kit cyclone, le ventilateur de la salle, le bruit à la cantine.
- Deux questions écrites, une par compétence de la séquence ; pour chacune une version étayée (n°31).
- Une correction complète : une réponse possible, le **critère** de chaque question, un ou deux contre-exemples (✘).
- Aucun bouton : il ne valide rien (n°333). Le banc du lot le vérifie (deux zones sauvegardées, deux versions
  étayées, deux critères, avant le Bonus) ; la fiche pédagogique dit ce qu'on y regarde.

## 5. Vérifier, livrer

- `controle_question_seule.py` : zéro refus sur le lot ; D1 et P1 dits dans le journal s'ils restent.
- Les contrôles des QCM (`qcm-html-accessible`), les bancs du lot, le mode mission joué (`banc_generique.mjs`).
- `node _outils/balayer_questions_qcm.mjs --apres <lot>` : chaque question jouée à 390 px, avant de répondre et sur
  les trois écrans de l'aide après une réponse fausse — rien ne dépasse, chaque figure est décodée et décrite.
- Chaque question sur document regardée à 390 px dans le QCM : le texte lisible, sans loupe.
- Le journal (ce qui a été lu, ce qui a été trouvé, la mesure avant et après), le rapport de tests du lot, la PR
  (`livraison-depot-cycle4`).

## Ce que ce skill ne fait pas

Il ne juge ni la longueur ni la place des propositions (`propositions-sans-indice`, n°341), ni les aides et les
pièges (`qcm-aides-et-pieges`, n°339), ni le niveau de lecture (`texte-clair-et-aere`). Il ne remplace pas la lecture
par l'outil : S1 à S4 et E1 à zéro, c'est le début de la lecture, pas sa fin.
