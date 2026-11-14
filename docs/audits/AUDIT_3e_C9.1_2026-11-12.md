# Audit pédagogique, fonctionnel et visuel — Variables, types et systèmes

> **Copie déposée dans le dépôt le 14/11/2026**, à la demande de Pascal, avec le cahier des charges qui l'accompagne (`CAHIER_DES_CHARGES_ULTRA_PREMIUM_2026-11-12.md`). Les dix captures et le journal des ressources qu'elle cite ne sont pas joints : leurs liens sont devenus du texte. Rien d'autre n'est changé. Les règles d'or tirées de cet audit (n°322 à n°330) sont au journal des décisions, entrée du 14/11/2026.

**Date : 12 novembre 2026. Public vérifié : troisième, cycle 4.**

**Objet :** audit approfondi de la séquence 3e_C9.1 et examen transversal d'un échantillon du site, avec un cahier des charges pour des représentations « ultra premium ».

[Séquence examinée](https://pll-process.github.io/en-ligne-pour-le-cycle-4/theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/sequence_3e_C9.1_variables_types_systemes.html).

Les constats portent sur la version effectivement affichée et téléchargée le jour de l'audit. La copie indexée par le moteur de recherche était antérieure : elle mentionnait notamment un éditeur Vittascience embarqué. La page actuelle utilise un éditeur Python intégré ; Vittascience est facultatif. Les défauts anciens corrigés dans la version actuelle ne sont donc pas repris comme problèmes présents.

## 1. Synthèse exécutive

**Appréciation globale : une ressource pédagogique riche et déjà soignée, dont la finition haut de gamme doit d'abord renforcer la lisibilité des représentations et la fiabilité des preuves de réussite.**

La progression est intelligible : suivre une variable, comprendre les types, déboguer, puis utiliser une fonction et des tests. Les prédictions, aides graduées, retours explicatifs, rôles de binôme et retour sur l'hypothèse initiale soutiennent des apprentissages actifs. L'éditeur intégré limite les changements d'outil et le recours aux comptes externes. Le QCM propose une remédiation particulièrement détaillée.

Trois interventions sont prioritaires :

1. **Fiabiliser la validation de l'activité 5.** L'audit a obtenu le statut « activité validée » sans modifier ni exécuter la fonction Python de l'élève. La fonction contenait encore `return 0`. Les quatre boutons du tableau exécutent une fonction JavaScript prédéfinie, indépendante du code saisi. La réussite affichée ne prouve donc pas la production annoncée.
2. **Reconcevoir les schémas pour les petits écrans.** Sur une fenêtre de 390 pixels, le document sur les types n'occupe qu'environ 240 pixels de largeur. Certaines annotations de 10,5 unités dans un dessin de 940 unités reviennent à environ 2,7 pixels CSS. Le dessin reste net au sens vectoriel, mais ses textes sont pratiquement illisibles.
3. **Simplifier la hiérarchie de présentation.** Les encadrements imbriqués, nombreux accents colorés, badges et commandes donnent beaucoup d'éléments de même importance visuelle. Une réalisation premium doit rendre évidents l'action à accomplir, le document utile et la preuve attendue.

| Domaine | Appréciation qualitative |
|---|---|
| Progression et accompagnement | Solides ; autonomie de conception encore à renforcer |
| Évaluation | Retours riches ; validation finale à corriger en priorité |
| Ergonomie | Repères nombreux ; démarrage chargé et modes à clarifier |
| Représentations visuelles | Identité cohérente ; adaptation mobile insuffisante |
| Accessibilité | Bonnes fondations ; obstacles et tests complémentaires identifiés |
| Technique | Fonctionnement de base observé ; promesse hors ligne à préciser |
| Données et droits | Informations utiles présentes ; portée des affirmations à préciser |
| Maintenance | Mutualisation commencée ; accumulation de correctifs locaux visible |

Aucune note chiffrée ni conformité générale au RGAA n'est attribuée.

## 2. Périmètre, méthode et limites

### Pages et documents examinés

- **Séquence 3e_C9.1 :** lecture des quatre séances, des corrections et du fonctionnement de validation ; essais interactifs ciblés.
- **[Accueil du site](https://pll-process.github.io/en-ligne-pour-le-cycle-4/index.html) :** examen visuel et structurel du catalogue et des accès rapides.
- **[QCM associé, 30 questions](https://pll-process.github.io/en-ligne-pour-le-cycle-4/theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/qcm_3e_C9.1_variables_types_systemes.html) :** inspection du contenu et essai d'une réponse incorrecte avec correction.
- **[Lexique associé](https://pll-process.github.io/en-ligne-pour-le-cycle-4/theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.1/lexique_3e_C9.1.html) :** lecture et examen visuel.
- **[Synthèse élève de quatrième liée aux prérequis](https://pll-process.github.io/en-ligne-pour-le-cycle-4/theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.1/Synth%C3%A8ses/synthese_eleve_4e_C9.html) :** lecture, structure et capture.
- **Sources complémentaires :** quatre schémas SVG, scripts et styles de la séquence et de l'éditeur ; vérification de disponibilité des liens vers le TP mBot2 et le jardin connecté. Ces deux TP n'ont pas fait l'objet d'une exécution complète.
- **Références officielles :** BO du 29 février 2024, annexe du programme, accompagnement éduscol et critères RGAA 4.1.2.

Il s'agit d'un **audit approfondi d'une séquence et d'un audit transversal par échantillonnage du site**. Les conclusions transversales indiquent une direction de travail ; elles ne certifient pas toutes les pages du catalogue.

### Essais réellement effectués

| Étape | Essai | Résultat et état |
|---|---|---|
| 1 | Ouverture et navigation entre les séances | Fonctionnelles ; entrée dense |
| 2 | Six étapes du simulateur de mémoire | Valeurs et écran final cohérents ; badge obtenu |
| 3 | Exécution des trois expériences Python préremplies | Console : `7`, `34`, `Train Q 3 min` ; fonctionnement observé |
| 4 | Quatre boutons du banc et sept réponses de l'activité 5, sans toucher au programme | Validation obtenue malgré `return 0` et console non exécutée : défaut confirmé |
| 5 | Rechargement après cet essai | Progression conservée : `1 / 5` ; fonction toujours inchangée |
| 6 | Fenêtres 1440 × 1000, 1280 × 900, 768 × 1024 et 390 × 844 | Recomposition générale ; forte réduction des textes intégrés aux SVG |
| 7 | Flèche droite depuis l'onglet de séance 2 | L'onglet sélectionné reste la séance 2 ; navigation attendue d'un composant à onglets à compléter |
| 8 | Première question du QCM, réponse incorrecte puis validation | Explication, réfutation des distracteurs et possibilité de réessai présentes |
| 9 | Requêtes vers les ressources locales liées | 27 requêtes réussies, représentant 21 adresses distinctes sans les fragments ; toutes HTTP 200 |
| 10 | Activation de l'impression | Essai non concluant dans le navigateur disponible ; aucun PDF imprimé validé |

Les dimensions sont des **fenêtres de navigateur**, pas des essais sur appareils physiques. Les calculs complémentaires Python ont été effectués séparément avec l'interpréteur local ; ils ne constituent pas une certification de compatibilité complète du moteur intégré.

### Statut des preuves

**O — Observé :** affichage, contenu, mesure ou comportement effectivement lu ou essayé. **I — Inféré :** conséquence probable pour les utilisateurs, à confirmer en situation. **NV — Non vérifié :** contrôle restant à effectuer.

**NV :** lecteurs d'écran NVDA/VoiceOver, utilisateurs DYS, navigateurs multiples, vrais appareils tactiles, zoom utilisateur à 200 % et 400 %, performances sur réseau contraint, session réellement déconnectée, export/import complet des fichiers, impression A4, comportement du robot et ensemble des traitements opérés par l'hébergeur ou Vittascience. Aucun compte personnel ni renseignement d'élève n'a été utilisé. Le site publié n'a pas été modifié.

### Captures de référence

Les captures représentent le site pendant l'audit, pas des propositions de nouvelle interface.

1. Entrée sur ordinateur (capture `01-entree-ordinateur.jpg`, non jointe) — fonctionnement correct, hiérarchie chargée.
2. Simulateur après six étapes (capture `02-simulateur.jpg`, non jointe) — fonctionnement correct, représentation utile.
3. Console des expériences (capture `03-python-types.jpg`, non jointe) — exécution correcte.
4. Validation sans programme exécuté (capture `04-validation-sans-programme.jpg`, non jointe) — défaut confirmé.
5. Schéma sur smartphone (capture `05-schema-mobile.jpg`, non jointe) — lisibilité insuffisante.
6. Schéma sur tablette (capture `06-schema-tablette.jpg`, non jointe) — réduction toujours sensible.
7. Accueil (capture `07-accueil.jpg`, non jointe) — catalogue cohérent, entrée surtout orientée classement pédagogique.
8. Lexique (capture `08-lexique.jpg`, non jointe) — contenu lisible, consultation longue.
9. Retour du QCM (capture `09-qcm-retroaction.jpg`, non jointe) — remédiation riche, plusieurs niveaux d'encadrement.
10. Synthèse liée (capture `10-synthese.jpg`, non jointe) — carte de questions intéressante à réutiliser.

Le journal des ressources est conservé dans `resource-checks.json` (non joint). Les sources téléchargées permettent de localiser les constats à la date de l'audit.

## 3. Présentation de la séquence

| Élément | Caractérisation vérifiée |
|---|---|
| Public | Troisième ; inscription explicite dans le thème 3 du cycle 4 |
| Prérequis | Variable et affectation, lecture d'algorigrammes, traduction et tests ; rappels de cinquième et quatrième |
| Objectif central | Comprendre les variables et les types pour lire, corriger et tester un programme structuré |
| Notions | Affectation, trace d'exécution, `int`, `float`, `str`, `bool`, concaténation, erreur de type, fonction, conditions, cas limite et non-régression |
| Organisation | Cinq activités sur quatre séances : mémoire ; suivi ; types ; débogage du panneau ; fonction de ventilation et tests |
| Durée annoncée | Quatre séances de 55 minutes. Activités : environ 25 + 25 + 45 + 45 + 45 minutes, soit 185 minutes ; 35 minutes restent pour l'ensemble des autres temps |
| Supports | Contexte du métro new-yorkais, photographies créditées, quatre documents SVG, simulateur, éditeur Python intégré, lexique et QCM |
| Modalités | Travail individuel et binôme avec alternance pilote/vérificateur ; simulation et parcours de suivi sur papier |
| Évaluation | Diagnostic d'entrée non noté, vérifications d'activité, critères de réussite, bilan réflexif et QCM d'entraînement |

**I :** le temps est tendu en séance 1 : deux activités de 25 minutes laissent cinq minutes pour le démarrage, le diagnostic, la situation et le bilan. Le temps de quatre gestes de gestion de fichiers peut également absorber la marge de séance 2. Cette estimation doit être confrontée à un groupe réel.

### Cohérence avec le programme applicable

Au 12 novembre 2026, le programme publié en 2024 s'applique à la troisième depuis la rentrée 2026-2027, selon l'article 2 de l'[arrêté du 9 février 2024, BO n°9 du 29 février 2024](https://www.education.gouv.fr/bo/2024/Hebdo9/MENE2402802A). Cette entrée en vigueur est également présentée par [éduscol](https://eduscol.education.gouv.fr/5745/ressources-d-accompagnement-du-programme-de-technologie-au-cycle-4).

La séquence contribue bien à la conception algorithmique, aux fonctions et à la mise au point. Cependant, compléter un programme fourni ne suffit pas à démontrer une conception autonome. L'[annexe officielle, page 16 du PDF](https://www.education.gouv.fr/sites/default/files/ensel802_annexe.pdf) comporte aussi la programmation d'un système réel avec interaction humain-machine. Le lien mBot2 peut prolonger ce travail ; son seul affichage ne démontre pas que cet attendu est effectivement réalisé. L'accueil précise utilement que les codes tels que `3e_C9.1` sont une codification locale, à préserver.

## 4. Audit détaillé par axe

### A. Qualité pédagogique et didactique

**Forces observées.** L'enchaînement des activités fait passer d'une représentation concrète à la lecture du code, puis aux tests. Les prédictions précédant l'exécution rendent visibles les conceptions initiales. Les aides en deux niveaux et les distracteurs commentés rendent l'erreur exploitable. La réflexion finale revient sur l'hypothèse de départ. La répartition des rôles, avec échange à mi-parcours, répond à un enjeu réel d'équité dans l'accès au clavier.

**A1 — Conception encore trop guidée — O/I.** L'activité 5 annonce l'élaboration d'un algorithme, mais fournit déjà la règle, le schéma et la structure de fonction ; l'élève choisit des éléments. Cela prépare la compétence, sans prouver qu'il sait concevoir une solution. **Amélioration :** prévoir un court transfert individuel avec un nouveau besoin, un algorithme rédigé par l'élève et une fonction sans squelette ; garder le squelette comme aide facultative.

**A2 — Couverture inégale des types — O/I.** Les expériences centrales de la séance 2 mobilisent surtout les entiers et les chaînes. Le flottant intervient ensuite et le booléen devient un paramètre en séance 4. **Impact :** reconnaître quatre noms peut être confondu avec savoir les utiliser. **Amélioration :** ajouter une expérience courte associant `3.5`, une comparaison et `type(...)`, avec une interprétation en phrase.

**A3 — Une généralisation technique incorrecte — O.** Le lexique, repris du QCM, affirme que `+` exige le même type. `3 + 4.5` donne pourtant `7.5`. **Amélioration :** limiter la règle aux cas étudiés : deux chaînes se concatènent ; les nombres entiers et flottants peuvent s'additionner ; une chaîne et un nombre ne s'additionnent pas directement. Voir la [documentation officielle des types Python](https://docs.python.org/3/library/stdtypes.html).

**A4 — Deux causes et une conséquence présentées comme trois bogues indépendants — O/I.** Dans l'activité 4, le texte initial de `minutes` produit une concaténation, puis rend la soustraction impossible. Corriger l'initialisation supprime aussi cette erreur de type. **Amélioration :** conserver l'exercice mais demander de relier « cause → valeur/type → conséquence » ; parler de deux défauts à corriger et d'une conséquence à expliquer, ou introduire un troisième défaut réellement indépendant.

**Point positif de justesse :** la version actuelle explique correctement que `/ 1,8` peut produire un tuple plutôt qu'une erreur de syntaxe. Le calcul local de contrôle donne `(45.0, 8)` ; avec `1.8`, il donne `25.0`. Ne pas remplacer cette explication juste par l'ancienne formulation indexée. Le rôle de la virgule dans une expression d'affectation est documenté dans la [référence Python](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements).

**A5 — Frontière du modèle de la boîte — O/I.** La métaphore convient à l'initiation. Dire que l'ancien contenu est perdu devient trop général si un autre nom le conserve. **Amélioration :** écrire « cette variable ne permet plus de retrouver l'ancienne valeur, sauf si on l'a conservée ailleurs ». Éviter de transformer la métaphore en description physique universelle de la mémoire.

**A6 — Passage du panneau à la ventilation — O/I.** Le changement de sous-système renouvelle l'activité mais ajoute un indice de pollution, un booléen et une règle de priorité. **Amélioration :** introduire une transition de deux phrases et nommer l'indice comme une donnée simplifiée de simulation. Faire apparaître les entrées, le traitement et la sortie du système.

**A7 — Besoin initial puis besoin précisé — O/I.** La règle commence avec `> 100`, puis la commande précise que 100 doit aussi déclencher la vitesse 3. **Amélioration :** rendre explicite que l'on clarifie ou modifie une exigence. Selon le besoin initial littéral, `>` était correct ; le test révèle ici une frontière à préciser, pas nécessairement une faute de traduction.

### B. Évaluation des apprentissages

**Forces observées.** Le diagnostic distingue les prérequis de la progression notée par les badges. Les critères sont formulés en actions. Dans le QCM essayé, l'explication ne se limite pas à donner la bonne lettre : elle reprend la notion, fournit un exemple et explique chaque distracteur. Les modes « erreurs », « à revoir » et « 10 questions » permettent une remédiation ciblée ; un mode sans minuteur est présent.

**B1 — Validation finale dissociée du programme — O, priorité critique.** Essai reproductible : laisser la fonction à `return 0`, sélectionner les sept réponses attendues, cliquer les quatre boutons du tableau, puis vérifier. Le statut validé est obtenu. La fonction `fnVentil` du code de page calcule les résultats indépendamment de la zone Python. Le vérificateur de l'activité 5 contrôle le questionnaire et les quatre clics ; il ne contrôle pas l'exécution du programme corrigé. **Impact :** le bilan peut déclarer acquis ce qui n'a pas été réalisé.

*Capture de l'audit, non jointe au dépôt : Essai observé : activité 5 validée avec une console restée vide (`04-validation-sans-programme.jpg`).*

**Correction attendue :** appeler la fonction de l'élève avec des entrées de test et comparer les valeurs renvoyées, après sa dernière modification. Ne pas se contenter d'un texte imprimé dans la console : `print(3, 2, 1, 3)` ne prouve pas l'existence d'une fonction correcte. Un programme inchangé à `return 0` doit rester « production à terminer ». Le tableau de démonstration peut subsister avec un nom explicite, distinct du banc personnel.

**B2 — Preuves d'exécution trop faibles dans les autres activités — O du code, I du risque.** Pour les activités 3 et 4, une exécution sans erreur dans le bloc suffit à ouvrir le verrou ; un clic sur le lien Vittascience le fait également. Cela ne prouve ni les trois expériences, ni la correction attendue. Ce contournement n'a pas été rejoué dans l'interface. **Amélioration :** distinguer « outil ouvert », « programme exécuté » et « résultat vérifié » ; comparer les productions pertinentes sans imposer un texte source unique.

**B3 — Mesure de compréhension à individualiser — I.** Après une réussite de binôme, faire répondre chaque élève à une petite variante sans correction immédiatement visible. La note sur 20 du QCM reste un indicateur d'entraînement ; elle ne doit pas suffire à conclure à la maîtrise de la conception.

**B4 — Élargir le banc — recommandation.** Ajouter des valeurs juste au-dessous et au-dessus de la frontière, ainsi qu'un cas combinant pollution et arrivée du train. Exemple : `(150, True)` doit renvoyer 3 si la pollution est prioritaire. Exiger une justification de ce choix. Aucun petit banc fini ne constitue, à lui seul, une preuve générale pour toutes les entrées possibles.

### C. Ergonomie et expérience utilisateur

**Forces observées.** Les séances sont repérées, la progression est lisible et le rappel d'ouverture se replie lors du passage aux séances suivantes. Les liens vers le lexique restent contextualisés. Le mode mission et le mode essentiel montrent que la réduction de charge a déjà été prise en compte ; ils ne sont pas absents.

**C1 — Beaucoup de décisions avant la première action — O/I.** L'entrée juxtapose outils de sauvegarde, parcours, rappels, identité, diagnostic et contexte. **Amélioration :** un résumé initial comprenant « ce que tu vas réussir », durée et bouton « Commencer le diagnostic ». Ranger les outils secondaires dans un espace clairement nommé, tout en gardant visible le statut de sauvegarde.

**C2 — Parcours aux intitulés ambigus — O/I.** « En simulation » et « Sans matériel » peuvent tous deux désigner l'absence de robot. **Amélioration :** utiliser « Sur ordinateur » et « Sur papier », préciser les productions de chaque parcours et prévoir une validation équivalente par l'enseignant pour les traces papier. Le parcours papier ne doit pas se réduire à recopier un corrigé.

**C3 — Lexique abondant, accès local perfectible — O/I.** Il annonce 55 mots et 30 notions ; les sources documentaires prennent de la place entre les définitions. **Amélioration :** recherche simple, sommaire des séances, termes liés depuis les consignes et références bibliographiques repliables. Conserver l'accès complet à ces sources.

**C4 — Catalogue surtout conçu pour classer — O/I.** L'accueil expose thèmes, compétences et statuts avant le travail du jour. Aucun champ de recherche ou de filtre n'a été trouvé dans la version inspectée. **Amélioration :** conserver cette entrée documentaire pour l'enseignant et proposer aux élèves une entrée par niveau et activité. Les accès rapides présentent un QCM de 24 questions, différent de celui de 30 questions lié depuis la séquence : préciser leur rôle et leur articulation ; ne pas supposer qu'il s'agit d'un lien erroné.

### D. Qualité esthétique et représentations « ultra premium »

**Forces à préserver.** L'accueil, la séquence, le lexique et le QCM partagent un fond bleu nuit, des textes clairs et des accents cyan/violet. Les photographies documentaires ancrent le scénario. Les SVG sont légers et accompagnés de descriptions. La synthèse liée organise la mémorisation autour de questions : c'est une bonne piste pour structurer le reste du site.

**D1 — Le dessin réduit reste une page miniature — O.** Les quatre SVG utilisent une largeur de référence de 940 unités et juxtaposent plusieurs panneaux. Les textes internes sont souvent petits même sur ordinateur ; sur mobile, ils deviennent minuscules. **Correction :** cartes HTML adaptatives pour les types, lecture en étapes pour la mémoire, présentation verticale pour « besoin → algorithme → fonction → tests ». Réserver le SVG aux relations qui doivent réellement être dessinées. La transcription d'une règle doit rester du texte lisible et sélectionnable.

*Capture de l'audit, non jointe au dépôt : Document des types affiché dans une fenêtre de smartphone (`05-schema-mobile.jpg`).*

**D2 — L'agrandisseur ne couvre pas ces objets — O du code et de l'essai ciblé.** L'agrandisseur arme les images et les SVG intégrés directement, mais pas les quatre SVG chargés par `<object>`. Un clic sur le document des types n'a pas ouvert de vue agrandie pendant l'essai. **Correction :** fournir un bouton explicite « Agrandir le schéma », une vue navigable au clavier et une alternative textuelle structurée. Le zoom complète la version mobile, il ne remplace pas son adaptation.

**D3 — Trop de cadres concurrents — O/I.** Plusieurs couches de carte, activité, consigne, exercice et aide entourent une même tâche. **Correction :** deux niveaux de surface au maximum dans la zone de travail, une action principale évidente et des séparations par espacement. Conserver des couleurs réservées aux états et aux informations utiles.

**D4 — Typographie et signes à unifier — O/I.** Les documents SVG utilisent Verdana ; la page emploie une police système ; les nombreux émojis varient selon l'appareil. **Correction :** conserver une famille sobre pour le texte et une police à chasse fixe pour le code ; employer un jeu d'icônes homogène avec des libellés. Réduire les capitales insistantes à quelques mots réellement structurants.

**D5 — Représenter un raisonnement, pas seulement une décoration — recommandation.** Dans le simulateur, relier visuellement l'expression calculée, la valeur courante et l'affectation. Dans le banc, aligner clairement entrée, attendu, obtenu et verdict. Dans les types, juxtaposer le code, le type et la valeur. Ces correspondances ont davantage de valeur pédagogique qu'une animation décorative.

Le [cahier des charges visuel joint](CAHIER_DES_CHARGES_ULTRA_PREMIUM_2026-11-12.md) donne les spécifications et les critères de réception.

### E. Accessibilité et inclusion

**Fondations observées.** Langue française déclarée, lien d'évitement, titres structurés, groupes de réponses avec légendes, étiquettes des champs et plusieurs zones de statut. Les photographies ont des alternatives descriptives. Les SVG possèdent des titres et descriptions internes. La réduction des animations selon les préférences utilisateur est prévue. Ces éléments ne suffisent pas à conclure à une conformité complète.

**E1 — Contraste insuffisant de certains crédits — O.** Pour les crédits des photos MTA : texte calculé `#5b7bb8`, fond effectif de la carte `#0d2347`, taille 13,6 pixels. Le ratio calculé est **3,69:1**, inférieur au seuil de 4,5:1 applicable au texte courant. Le texte principal sur ce fond atteint environ 12,89:1 : le problème est localisé. **Correction :** éclaircir les crédits et vérifier leur état imprimé et visité. Référence : [RGAA 4.1.2, critère 3.2](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/).

**E2 — Schémas et petites tailles — O/I.** Le problème mobile décrit plus haut touche directement la compréhension. **Correction :** textes recomposables, zoom explicite et équivalent textuel. Contrôler notamment les critères RGAA 1.1/1.6 et 10.4/10.11. L'existence d'un `<desc>` dans le SVG ne démontre pas que l'ensemble de son contenu est correctement restitué par chaque lecteur d'écran.

**E3 — Commandes peu explicites hors contexte — O.** Les quatre boutons du banc s'appellent seulement « ▶ » ; l'autoévaluation propose des boutons nommés par des émojis. **Correction :** « Exécuter le test T1 », etc., et « Pas encore / Avec aide / Seul / Je peux expliquer », avec état sélectionné annoncé. Vérifier les critères RGAA 7.1 et 7.3.

**E4 — Onglets à compléter — O de l'essai ciblé.** La flèche droite n'a pas déplacé la sélection depuis la séance 2. **Correction :** adopter un comportement cohérent avec les rôles annoncés : flèches, Home/End, gestion du focus et relations entre onglets et panneaux. Vérifier l'ensemble au clavier ; ne pas présenter l'essai effectué comme un audit clavier exhaustif.

**E5 — Profils DYS — I/NV.** La segmentation, les aides et la police système sont favorables. La longueur de l'entrée, les capitales et les petits textes intégrés aux images sont des risques. **Correction :** consignes brèves, alignement à gauche, interligne confortable, largeur de lecture limitée et présentation stable. Aucune police dite DYS ne garantit à elle seule l'accessibilité : faire essayer le parcours par les élèves concernés.

Les numéros de critères renvoient au [référentiel officiel consulté](https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/). Il ne s'agit ni d'une déclaration de conformité ni d'une qualification juridique du site.

### F. Qualité technique et compatibilité

**F1 — Fonctionnement principal satisfaisant — O.** Navigation des séances, simulateur et première exécution Python fonctionnent dans le navigateur utilisé. La console a produit les trois sorties prévues. Les 21 adresses distinctes contrôlées répondent HTTP 200 ; cela ne vérifie ni chaque lien du site ni le comportement de chaque ressource.

**F2 — « Page unique hors-ligne » à préciser — O du code, NV du scénario réel.** Le HTML dépend de styles, scripts et SVG séparés. L'éditeur charge aussi son moteur Skulpt au premier lancement. Enregistrer uniquement le fichier HTML ne garantit donc pas le fonctionnement hors ligne. **Correction :** proposer un dossier ou une archive complète, avec mode d'ouverture testé ; annoncer « fonctionne hors connexion avec le dossier complet téléchargé ». Un premier chargement réussi sur Internet n'est pas un test hors ligne.

**F3 — Sauvegarde : informations plutôt claires, robustesse à renforcer — O/I.** L'avertissement sur les postes partagés est pertinent et la progression a été restaurée après rechargement. Dans le code, une erreur d'écriture du stockage peut toutefois être ignorée avant l'affichage du message de réussite. Ce cas n'a pas été provoqué. **Correction :** afficher un succès uniquement après une écriture réussie et proposer une sortie de secours. Tester la suppression de toutes les traces, y compris les programmes et états gardés par les composants mutualisés.

**F4 — Compatibilité et papier — NV.** La mise en page générale s'est recomposée aux largeurs essayées, sans débordement global constaté sur la séance 2 ; cela ne résout pas la taille des textes du schéma. Le code comporte de nombreuses règles d'impression et de transformation des réponses : l'intention est forte, mais aucun PDF final n'a été inspecté. **Réception nécessaire :** A4 avec réponses longues, aides ouvertes/fermées, schémas complets, noir et blanc et sauts de page stables.

### G. Données, droits et confiance

**Forces observées.** Auteur, année et licence de la ressource sont indiqués. Les photographies possèdent des crédits séparés. Les SVG sont annoncés CC0. Le recours facultatif à Vittascience est expliqué et la page avertit des risques d'un ordinateur partagé.

**G1 — Portée de l'absence d'envoi — O/I.** Le code principal inspecté conserve les réponses localement et aucun envoi de réponse vers un serveur n'a été trouvé dans ces scripts. Cela ne signifie pas qu'une visite du site ne génère aucun échange réseau : l'hébergement reçoit des requêtes et un lien externe conduit à un autre service. **Correction :** préciser « les réponses saisies sont enregistrées dans ce navigateur ; elles ne sont pas transmises par les fonctions de cet atelier ». Documenter séparément l'hébergement et les services facultatifs. Aucun constat de non-conformité juridique n'est établi.

**G2 — Identité et effacement — recommandation.** Si l'identité complète n'est utile que sur une impression, autoriser un identifiant de classe ou un pseudonyme pendant l'entraînement. Vérifier que « effacer » couvre effectivement toutes les traces de l'atelier et prévoir une indication compréhensible de fin de session.

**G3 — Contexte fictif et formulations d'autorité — O/I.** Le défi entre classes et le programme de la MTA servent de narration ; leur réalité n'a pas été vérifiée. L'affirmation sur « 9 collégiens sur 10 » n'est pas accompagnée d'une source visible. **Correction :** présenter clairement la mission comme un scénario pédagogique et remplacer le chiffre par « une notion qui réserve encore des surprises ». Distinguer la photo documentaire du programme simulé que l'élève corrige.

**G4 — Réutilisation des médias — recommandation.** Maintenir un inventaire des licences par fichier. La licence générale de la page ne remplace pas celles des photographies. La présence des crédits a été vérifiée ; les chaînes complètes de droits et conditions des services tiers ne l'ont pas été.

### H. Maintenance et réutilisation

**H1 — Mutualisation utile — O.** L'éditeur et la coloration du code sont externalisés dans des ressources communes. Cette base permet d'harmoniser plusieurs pages sans réécrire chaque activité.

**H2 — Complexité accumulée — O/I.** Le HTML de séquence téléchargé pèse environ 254 ko non compressés, comporte 13 blocs de style et 7 éléments de script. Il contient notamment une couche de mode mission qui examine les scripts pour retrouver les réponses. Ce sont des indices de couplage et de fragilité lors des modifications ; ils ne constituent pas à eux seuls une mesure de lenteur. **Correction :** une définition explicite des activités et des critères, des composants communs et une feuille de style centrale.

**H3 — Variantes de représentations — recommandation.** Donner à chaque schéma un identifiant, un objectif, une version mobile et papier, son texte alternatif et sa source modifiable. Ajouter une date de révision visible et une courte fiche enseignant : temps réels, productions, matériel, solutions et variantes de groupe.

**H4 — Audit du dépôt limité — NV.** Les sources publiques ont été inspectées, mais pas un dépôt de conception complet ni ses procédures de publication. Aucun jugement n'est porté sur des tests ou une organisation de fichiers qui n'auraient pas été vus.

## 5. Tableau des recommandations

Priorités : **critique** = preuve de réussite fausse ; **élevée** = compréhension ou accès fortement affectés ; **moyenne** = amélioration importante de l'usage ; **faible** = finition secondaire. Les efforts sont relatifs, sans chiffrage contractuel : faible = correction ciblée ; moyen = composant ou activité ; important = architecture ou harmonisation transversale.

| Constat et preuve | Impact | Recommandation concrète | Priorité | Effort estimé |
|---|---|---|---|---|
| B1 : activité 5 validée avec `return 0`, console vierge | Réussite non démontrée | Tester les valeurs renvoyées par la fonction réellement écrite | Critique | Moyen |
| B2 : verrous 3/4 fondés sur ouverture ou exécution sans erreur | Trace d'activité trop faible | Séparer ouverture, exécution et résultat correct | Élevée | Moyen |
| D1 : schéma des types ≈240 px sur fenêtre 390 px | Contenu essentiel illisible | Cartes adaptatives avec vrais textes et version verticale | Élevée | Moyen |
| D2 : objets SVG non couverts par l'agrandisseur | Pas de lecture confortable à la demande | Bouton d'agrandissement et alternative structurée | Élevée | Faible à moyen |
| A3 : `+` présenté comme exigeant le même type | Règle scientifique erronée | Corriger QCM et lexique, ajouter `3 + 4.5` | Élevée | Faible |
| E1 : crédits à 3,69:1 | Texte secondaire difficile à lire | Ajuster la couleur et vérifier le contraste effectif | Élevée | Faible |
| A1 : conception annoncée mais squelette fourni | Maîtrise autonome inconnue | Petit transfert individuel sans squelette par défaut | Élevée | Moyen |
| E3 : boutons « ▶ » et émojis seuls | Commandes peu explicites à l'écoute | Libellés contextuels et états annoncés | Élevée | Faible |
| F2 : ressources externes au HTML et moteur chargé au clic | Hors ligne incertain | Archive complète et test réellement déconnecté | Élevée | Moyen |
| C1/D3 : entrée dense et encadrements multiples | Démarrage plus coûteux, attention dispersée | Une action principale, outils secondaires regroupés | Moyenne | Moyen |
| A4 : cause de typage et conséquence comptées séparément | Diagnostic mécanique | Faire construire une chaîne causale explicite | Moyenne | Faible |
| A7 : seuil précisé en cours d'activité | Confusion entre nouveau besoin et bogue | Nommer la clarification de spécification | Moyenne | Faible |
| B4 : manque de cas combiné et de voisinage du seuil | Priorité des branches peu vérifiée | Ajouter 99, 101 et `(150, True)` | Moyenne | Faible |
| C2 : « sans matériel » ambigu | Choix de parcours difficile | « Sur ordinateur » / « Sur papier », productions équivalentes | Moyenne | Faible |
| E4 : flèches d'onglets inactives lors de l'essai | Interaction clavier incohérente | Comportement complet du composant à onglets | Moyenne | Faible à moyen |
| C3 : 85 entrées/notions et références développées | Recherche lente dans le lexique | Sommaire, recherche, références repliables | Moyenne | Moyen |
| C4 : entrée du catalogue par compétences, sans recherche observée | Repérage élève difficile | Entrée par niveau/activité, recherche et filtres | Moyenne | Moyen |
| F3 : erreurs de stockage ignorées dans le code | Sauvegarde annoncée à tort dans certains cas | Statut de sauvegarde conditionné au succès réel | Moyenne | Faible |
| G1 : formulation absolue d'absence d'envoi | Portée de l'information mal comprise | Distinguer réponses, hébergement et services externes | Moyenne | Faible |
| H2 : couches de styles et logique de correction couplées | Risque de régression | Composants partagés et données d'activité explicites | Moyenne | Important |
| G3 : statistique sans source et fiction peu signalée | Confiance documentaire affaiblie | Scénario annoncé, chiffre retiré ou sourcé | Faible | Faible |
| D4 : icônes et capitales hétérogènes | Finition visuelle irrégulière | Jeu d'icônes et hiérarchie typographique communs | Faible | Moyen |

## 6. Plan d'action priorisé et angles morts

### Corrections rapides — avant la prochaine utilisation

Corriger la règle sur `+`, les libellés des tests et le contraste des crédits. Renommer le banc actuel « démonstration du programme fourni ». Tant que le programme de l'élève n'est pas contrôlé, remplacer la validation globale par « questionnaire réussi — programme à vérifier ». Clarifier le scénario, le parcours papier et la portée du hors ligne.

**Réception :** un programme à `return 0` n'obtient plus un statut qui annonce une production validée ; les élèves peuvent identifier l'action et le résultat attendu sans interpréter un pictogramme seul.

### Moyen terme — une séquence pilote complète

Relier l'évaluation à la fonction saisie. Refaire les quatre représentations avec une version mobile et une vue agrandie accessible. Ajouter le transfert individuel, la frise de progression et une synthèse courte de troisième. Revoir le temps des séances après un essai en classe. Vérifier le dossier hors ligne et les exports papier.

**Réception :** les tests comparent de vraies valeurs retournées, les étiquettes des schémas sont lisibles à 390 pixels, et l'enseignant obtient une trace individuelle compréhensible.

### Long terme — généralisation au site

Déployer la charte validée sur l'accueil, les séquences, synthèses, lexiques et QCM. Centraliser les composants ; inventorier et revoir les figures ; prévoir un contrôle automatique des liens, contrastes courants et cas fonctionnels sensibles. Faire une recette avec élèves et enseignants, puis un audit d'accessibilité adapté.

**Réception :** mêmes conventions de lecture et de navigation entre les pages, sans réduire la précision des contenus.

### Angles morts à traiter

- **Preuve individuelle :** un binôme performant peut masquer une difficulté ; conserver une trace courte par élève.
- **Égalité des parcours :** un parcours papier doit viser les mêmes apprentissages, avec un autre mode de preuve, pas seulement afficher moins de contenu.
- **Temps de reprise :** retrouver son travail après une semaine et sur un autre poste est un scénario distinct du simple rechargement ; le tester.
- **Information du système :** distinguer une mesure d'air, sa représentation numérique et la commande de ventilation ; expliciter le rôle des unités ou d'un indice fictif.
- **Usage au vidéoprojecteur :** vérifier les figures depuis le fond de la salle ; une capture sur écran individuel ne permet pas de conclure.
- **Version élève/enseignant :** prévoir une fiche de conduite et des corrigés séparables pour que l'autocorrection reste une modalité choisie.
- **Périmètre de maîtrise :** la simulation développe une partie de la compétence ; vérifier où sont réellement travaillées l'interaction avec un objet et la conception autonome.

## 7. Cinq propositions prêtes à l'emploi

### 1 — Consigne de mise au point et critère de réussite

> Écris la fonction `vitesse_ventilation(air, train_arrive)`. L'indice d'air est une donnée de simulation : à partir de 100, la fonction renvoie 3, même si un train arrive. En dessous de 100, elle renvoie 2 si un train arrive et 1 sinon. Prévois les résultats avant d'exécuter. Teste ta fonction avec les entrées du tableau, puis avec une nouvelle entrée de ton choix.
>
> J'ai réussi si ma fonction renvoie les valeurs attendues, si je justifie le cas exactement égal à 100 et si je sais expliquer la priorité entre pollution et arrivée d'un train.

### 2 — Tableau de tests à réutiliser

| Test | Indice d'air | Train arrive | Attendu avant exécution | Obtenu par ma fonction | Conclusion |
|---|---:|---|---:|---|---|
| T1 | 150 | False | 3 | À renseigner | À comparer |
| T2 | 60 | True | 2 | À renseigner | À comparer |
| T3 | 40 | False | 1 | À renseigner | À comparer |
| T4 | 100 | False | 3 | À renseigner | Frontière |
| T5 | 99 | False | 1 | À renseigner | Juste en dessous |
| T6 | 101 | False | 3 | À renseigner | Juste au-dessus |
| T7 | 150 | True | 3 | À renseigner | Deux conditions vraies |

Rejouer le tableau après une correction. Expliquer toute différence entre attendu et obtenu. Ces cas couvrent des situations choisies ; ils ne garantissent pas toutes les utilisations possibles.

### 3 — Synthèse courte sur les types

> Une variable associe un nom à une valeur. Une affectation change la valeur associée à ce nom. `int` désigne notamment les entiers, `float` les nombres flottants, `str` les chaînes de caractères et `bool` les valeurs `True` ou `False`. Les entiers et flottants peuvent s'additionner : `3 + 4.5` donne `7.5`. Deux chaînes se concatènent : `"3" + "4"` donne `"34"`. Une chaîne et un nombre ne s'additionnent pas directement. En cas de doute, j'affiche `type(ma_variable)`.

### 4 — Billet de sortie individuel, sans aide

```python
attente = 4
copie = attente
attente = attente - 1
texte = "Train " + "Q"
```

Questions : que valent `attente`, `copie` et `texte` ? Pourquoi la modification d'`attente` ne change-t-elle pas `copie` dans cet exemple ? Quelle différence entre `"4" + "1"` et `4 + 1` ?

**Réponses enseignant :** `3`, `4`, `"Train Q"` ; la deuxième affectation a conservé la valeur entière initiale sous un autre nom ; concaténation `"41"` contre addition `5`. Réussite : valeurs justes et explication du rôle des guillemets, sans se limiter à une lettre de QCM.

### 5 — Textes d'interface de validation

**Questionnaire seul réussi :** « Tes réponses sont justes. Il reste à exécuter et vérifier ta fonction. »

**Programme exécuté mais résultat incorrect :** « Le programme s'exécute. Le test T4 attend 3 et obtient 1 : compare le besoin et la condition à la frontière 100. »

**Programme modifié après validation :** « Ton code a changé depuis le dernier test. Relance le banc pour vérifier cette version. »

**Production et tests réussis :** « Ta fonction passe les tests proposés. Explique maintenant ton choix pour 100 et pour le cas où les deux conditions sont vraies. »

## 8. Questions à poser au concepteur ou à l'enseignant

1. L'activité doit-elle attester une compréhension guidée ou une conception autonome ? Quel travail individuel complète le binôme ?
2. Les quatre séances incluent-elles le diagnostic, les manipulations de fichiers, la synthèse et le QCM ? Quels temps ont été mesurés en classe ?
3. Le parcours papier vise-t-il toute la séquence ? Quelle trace et quelle validation lui sont associées ?
4. Où les élèves programment-ils effectivement un système réel avec une interaction humain-machine ? Le TP mBot2 est-il réalisé par tous ?
5. Quels postes, tailles d'écran et navigateurs dominent ? Les mobiles servent-ils surtout à réviser ou à programmer ?
6. Quel scénario hors ligne est promis : page déjà chargée, dossier complet, réseau local ou archive distribuée ?
7. Quel est le rôle respectif du QCM de 24 questions accessible depuis l'accueil et du QCM de 30 questions associé à la séquence ?
8. L'effacement supprime-t-il toutes les données des éditeurs et du mode mission ? Comment sont gérées les sessions partagées ?
9. Les SVG disposent-ils de sources facilement modifiables et d'une procédure de validation mobile/papier ?
10. Qui assure les révisions pédagogiques, les tests après publication et la mise à jour des droits des médias ?

**Première décision recommandée : faire de 3e_C9.1 la séquence pilote, corriger sa preuve de réussite puis valider ses quatre représentations sur mobile, ordinateur et papier avant de généraliser la charte au catalogue.**
