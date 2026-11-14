# Cahier des charges — représentations pédagogiques « ultra premium »

**Périmètre proposé :** séquence 3e_C9.1 pilote, puis déploiement sur les séquences, QCM, synthèses et lexiques du site. **Statut :** recommandations issues de l'audit du 12 novembre 2026 ; aucune nouvelle interface publiée.

L'identité bleu nuit et les situations concrètes peuvent être conservées. Le niveau de qualité visé se mesure à la compréhension, à la lisibilité, à la cohérence et à la fiabilité des interactions. Chaque figure doit aider l'élève à produire une réponse ou à comprendre un mécanisme.

## 1. Conventions communes

| Élément | Spécification proposée | Réception attendue |
|---|---|---|
| Texte de lecture | Base de 16 à 18 pixels CSS, interligne voisin de 1,6 ; alignement à gauche | Lecture confortable sur ordinateur et mobile, sans réduire le texte pour faire tenir un panneau |
| Largeur des explications | Environ 60 à 75 caractères par ligne ; l'espace de simulation peut être plus large | Les paragraphes longs ne traversent pas toute une grande fenêtre |
| Titres | Trois niveaux visuels nets ; titres d'activité orientés vers une action | L'élève distingue séance, tâche et détail sans lire tous les badges |
| Code | Police à chasse fixe, taille de lecture confortable ; guillemets, point et indentation bien distincts | `1.8`, `1,8`, `"3"` et `3` sont clairement différenciés |
| Couleurs | Bleu nuit de fond, surfaces légèrement plus claires, un accent principal cyan ; vert/orange/rouge pour les états | Une couleur ne porte jamais seule une information ; le violet reste un accent secondaire limité |
| Contraste | Au moins 4,5:1 pour le texte courant ; 3:1 pour les éléments concernés par les critères non textuels | Mesures contre le fond effectivement affiché, y compris crédits, commentaires et états désactivés selon leur statut |
| Espacement | Échelle commune de 4, 8, 12, 16, 24 et 32 pixels ; réserves autour des figures | Des tâches distinctes se distinguent d'abord par le rythme et l'espace |
| Encadrements | Deux niveaux de surface dans la zone de travail ; bordure réservée à un regroupement utile | Pas de succession de cinq rectangles autour d'une même instruction |
| Icônes | Une famille cohérente ; libellé visible pour toute commande pédagogique | Une personne qui ne reconnaît pas le pictogramme peut accomplir l'action |
| Animation | Courte et liée à une transformation ; arrêt ou réduction selon les préférences utilisateur | La version immobile conserve toutes les informations |
| Cibles tactiles | Viser au moins 44 × 44 pixels pour les commandes importantes | Manipulation possible sans toucher la commande voisine ; cible de confort, pas affirmation d'un seuil RGAA universel |
| Figure essentielle | Titre-question, représentation, une idée clé, consigne de lecture et alternative | Un élève sait ce qu'il doit observer et utiliser |
| Texte dans une figure | Cible interne de 14 pixels CSS ou plus à la taille réellement affichée | Aucune légende essentielle ne devient une annotation miniature |

Ces valeurs sont des objectifs de conception à éprouver avec les utilisateurs, sauf les seuils de contraste renvoyant au référentiel d'accessibilité. Elles ne remplacent pas une recette.

## 2. Les quatre représentations à reprendre en priorité

### A. Mémoire : rendre visible le changement d'état

**État actuel observé :** un schéma de synthèse juxtapose programme, boîtes et panneau ; un simulateur distinct permet six étapes. Le mécanisme pas à pas est pertinent, mais la figure et le simulateur ne doivent pas multiplier inutilement les explications équivalentes.

**Proposition :** une représentation synchronisée à trois zones : instruction active, noms et valeurs courantes, sortie du programme. Sur mobile, les trois zones se suivent verticalement. Mettre en avant l'expression calculée avant de remplacer la valeur. Une ancienne valeur peut être affichée temporairement comme état précédent, avec une légende explicite ; elle ne doit pas sembler encore stockée dans la variable.

**Commandes :** « Étape précédente », « Étape suivante », « Recommencer » ; repère « instruction 4 sur 6 ». Décrire verbalement le changement : « minutes : 4 devient 3 ». Annoncer cette information sans relire toute la page.

**Version papier :** programme court, table de suivi vierge et exemple de première ligne ; les lignes suivantes restent à produire par l'élève.

**Critères de réception :** l'élève identifie la valeur utilisée pour le calcul, la valeur remplacée et la nouvelle valeur. Le focus reste visible. Les six étapes restent compréhensibles sans animation ni couleur.

### B. Types : remplacer la planche réduite par des cartes adaptatives

**État actuel observé :** quatre cartes et deux exemples sont intégrés dans un SVG de 940 unités ; sa largeur descend à environ 240 pixels dans la page sur mobile.

**Proposition :** quatre cartes composées de vrais textes, disposées en quatre colonnes quand l'espace le permet, puis deux, puis une. Chaque carte conserve les mêmes rubriques : nom du type, sens, exemples, opération et piège.

| Type | Sens | Exemple | Opération à essayer |
|---|---|---|---|
| `int` | Nombre entier | `4`, `-2` | `4 + 1` donne `5` |
| `float` | Nombre flottant | `3.5` | `3 + 4.5` donne `7.5` |
| `str` | Chaîne de caractères | `"Q"`, `"34"` | `"3" + "4"` donne `"34"` |
| `bool` | Valeur logique | `True`, `False` | `4 > 3` donne `True` |

**En dessous :** deux expériences alignées « code → type du résultat → valeur », puis une question de prédiction. Les formes et mots donnent le sens ; les couleurs facilitent le repérage.

**Version papier :** les mêmes quatre cartes et deux exemples, avec du texte vectoriel sélectionnable et une taille lisible à 100 % sur une feuille A4.

**Critères de réception :** les guillemets sont visibles sur téléphone ; l'élève distingue valeur affichée et type ; l'addition de deux types numériques n'est pas interdite par une règle trop générale.

### C. Panneau bugué : organiser une investigation

**État actuel observé :** les choix de réponses et le code se succèdent ; la correction d'une cause supprime plusieurs symptômes.

**Proposition :** organiser le poste de travail autour de trois colonnes sur grand écran, trois étapes sur mobile : « Je prédis », « J'exécute », « J'explique ». Le code garde ses numéros de ligne ; l'erreur observée renvoie à la ligne pertinente ; une fiche de diagnostic relie cause, type/valeur et conséquence.

**Structure de trace :** « Ligne repérée », « Valeur et type observés », « Conséquence », « Modification », « Nouveau résultat ». Un état « corrigé » indique le résultat d'un vrai essai et reste distinct d'une réponse correcte au questionnaire.

**Version papier :** petit listing et tableau causal ; la sortie réelle peut être fournie après la prédiction pour maintenir l'intérêt de l'investigation.

**Critères de réception :** aucun badge ne repose seulement sur l'ouverture d'un éditeur ; les minuscules différences de syntaxe restent visibles ; une solution équivalente correcte est acceptée.

### D. Ventilation : montrer la chaîne complète et la preuve

**État actuel observé :** la figure réunit besoin, algorithme, fonction et tests ; le tableau interactif calcule une fonction prédéfinie, tandis que l'éditeur personnel est séparé.

**Proposition :** quatre étapes visuellement reliées : besoin explicite, algorithme produit, fonction de l'élève, tests de cette fonction. Chaque paramètre est nommé et illustré par une valeur d'exemple. Le schéma exprime la priorité de la pollution sur l'arrivée du train.

**Tableau de résultat :** identifiant du test, entrées, attendu, obtenu, verdict écrit. Un bouton « Tester ma fonction » agit sur la dernière version de la fonction et met à jour toutes les lignes. En cas de modification ultérieure, le statut devient « à retester ».

**Progression :** « Besoin compris », « Fonction écrite », « Tests proposés réussis », « Explication individuelle ». Ne pas confondre ces quatre traces avec une garantie générale du programme.

**Version papier :** besoin, algorithme ou fonction à compléter, banc de tests et justification du cas limite. Un petit tableau doit tenir ensemble ; éviter une ligne de test coupée entre deux pages.

**Critères de réception :** `return 0` ne valide pas la production ; un programme imprimant seulement les valeurs attendues ne passe pas un contrôle de fonction ; la priorité des conditions est testée.

## 3. Architecture des pages du site

| Surface | Organisation proposée | Éléments à préserver |
|---|---|---|
| Accueil | Entrée « Mon niveau », recherche, activités disponibles ; accès aux thèmes/compétences pour les enseignants | Classement par programme et distinction des codes locaux |
| Séquence | Mission en quelques lignes, diagnostic, séance courante, production attendue et action principale | Contexte concret, aides graduées et statut de sauvegarde |
| QCM | Question et document au centre ; navigation et statistiques secondaires ; mode court facilement accessible | Explication des distracteurs, réessai, révision des erreurs, choix sans minuteur |
| Lexique | Recherche, sommaire par séance, définitions courtes ; sources accessibles à la demande | Définitions contextualisées et traçabilité documentaire |
| Synthèse | Une question structurante par bloc, relation claire entre représentation et règle | Carte de questions et transfert vers une autre situation |
| Fiche enseignant | Objectifs, prérequis, chronométrage, productions, critères, variantes et corrections | Possibilité de réutiliser la ressource dans un autre groupe |

Le parcours de lecture doit rester stable entre les pages : même emplacement pour retour, titre, progression et outil de lecture des figures. Une ouverture externe est annoncée dans le libellé ou son voisinage immédiat.

## 4. Agrandissement et alternatives

Chaque schéma utile possède un bouton visible « Agrandir ». La vue conserve son titre et sa légende, s'ouvre au clavier, se ferme avec Échap et rend le focus à la commande initiale. Une version textuelle structurée expose les mêmes relations. L'alternative doit permettre d'accomplir l'exercice ; un simple titre général ne suffit pas pour une figure complexe.

Les figures essentielles sont adaptées au mobile avant le zoom. Les photos documentaires peuvent être agrandies, mais elles ne doivent pas monopoliser l'espace où l'élève attend une consigne. Le document, son commentaire et la question associée restent proches.

## 5. Version imprimée et hors connexion

Prévoir une version claire pour l'impression, avec titres, numéros d'activités et légendes autonomes. Éviter les fonds sombres pleins. Les couleurs sont doublées par des libellés ou des motifs compréhensibles en noir et blanc. Fixer les sauts de page selon les unités de sens ; contrôler les réponses longues et les tableaux complets. Le nombre de pages n'est annoncé qu'après vérification du document final.

Le paquet hors connexion comprend le HTML, les styles, les images, les scripts et le moteur Python nécessaires. La procédure de distribution précise comment ouvrir et conserver le dossier. Le scénario est essayé en étant réellement déconnecté, y compris lors du premier lancement de Python dans ce contexte.

## 6. Grille de réception avant généralisation

- [ ] Chaque représentation a un objectif pédagogique identifiable et une question de lecture.
- [ ] Tous les textes essentiels restent lisibles dans une fenêtre de 390 pixels ; pas de simple planche entière miniaturisée.
- [ ] La version tablette à 768 pixels et la version ordinateur ont été inspectées.
- [ ] Les zooms utilisateur, la réduction d'animation et l'utilisation au clavier ont été essayés.
- [ ] Un lecteur d'écran peut comprendre les commandes et accéder à une alternative exploitable aux figures.
- [ ] Les contrastes sont mesurés, y compris légendes, commentaires de code et crédits.
- [ ] Les touches, commandes et statuts possèdent des noms compréhensibles hors de leur position visuelle.
- [ ] La réussite du programme est contrôlée sur les valeurs renvoyées par la production réelle.
- [ ] Une modification du programme rend visible la nécessité de retester.
- [ ] Le parcours papier vise les mêmes apprentissages avec une trace adaptée.
- [ ] La sauvegarde, la reprise sur un autre poste et l'effacement ont été vérifiés avec des données d'essai.
- [ ] Le paquet fonctionne dans le scénario hors connexion promis.
- [ ] La sortie A4 et le noir et blanc ont été inspectés à 100 %.
- [ ] Les photographies, figures originales et contenus tiers possèdent leurs crédits et licences propres.
- [ ] Un petit groupe d'élèves et un autre enseignant ont essayé la séquence pilote.

**Ordre de réalisation recommandé :** fiabilité des validations, lisibilité des quatre représentations, unification des composants, puis déploiement progressif sur le site.
