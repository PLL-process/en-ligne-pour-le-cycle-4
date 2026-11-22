# -*- coding: utf-8 -*-
"""Les 30 exercices de l'entraînement DNB « algorigrammes » (3e_C6.2), réécrits après l'audit du 21/11/2026.

Ce que l'audit a mesuré sur la version du 08/08/2026, et ce que cette banque change :
  · la bonne réponse revenait selon le motif 2-1-4-3, et elle était strictement la plus longue dans 23 exercices sur
    30 (les 8 de la manche 4) : on validait la manche en choisissant la phrase la plus longue. Ici, les quatre
    propositions d'un exercice ont la même forme et des longueurs voisines ; la justification n'est plus dans la
    bonne réponse, elle est dans la correction (« ✍️ Sur ta copie »), écrite comme on l'écrirait au brevet ;
  · la place de la bonne réponse suit une suite fixe, équilibrée et sans motif (dnb_build.py, PLACES) ;
  · les corrections citent les propositions par leur texte, jamais par une lettre ;
  · chaque proposition fausse garde son « pourquoi » : c'est lui que l'élève lit dans « 🔎 Revoir mon erreur »,
    il dit ce qui cloche sans donner la bonne réponse ;
  · la manche 4 présente des algorigrammes à parcourir (serre, lampadaire, tri, porte) ; l'épreuve écrite de
    l'abri à vélos, sans propositions, est dans le gabarit (dnb_gabarit.html).

Champs : m (manche), t (titre), q (énoncé, dans la <legend>), bonne, copie (justification modèle), intrus
[(texte, pourquoi) × 3], a1, a2 (aides), ret (à retenir), cle (True : 🔑 indispensable, False : 🔁 révision, None :
sans marque), doc (document à lire : svg, pre ou html), pred (prédire avant de voir les propositions), icones
(forme dessinée devant chaque proposition), corr (document de la correction), apres (paragraphe final de la
correction).
"""

E = []


def ex(m, t, q, bonne, copie, intrus, a1, a2, ret, cle=None, doc=None, pred=False, icones=None, corr=None,
       apres=None):
    assert len(intrus) == 3, t
    E.append(dict(m=m, t=t, q=q, bonne=bonne, copie=copie, intrus=intrus, a1=a1, a2=a2, ret=ret, cle=cle,
                  doc=doc, pred=pred, icones=icones, corr=corr, apres=apres))


def tableau(entetes, lignes, legende=None, classe="trace"):
    th = "".join(f"<th scope=\"col\">{h}</th>" for h in entetes)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in l) + "</tr>" for l in lignes)
    cap = f"<caption>{legende}</caption>" if legende else ""
    return f'<div class="tableau-defile"><table class="{classe}">{cap}<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


FORMES = {"un rectangle aux bords arrondis": "terminal", "un rectangle aux angles droits": "rectangle",
          "un rectangle": "rectangle", "un losange": "losange", "un parallélogramme": "parallelogramme"}

# ══════════ Manche 1 — Symboles ══════════
ex(1, "Ce qu'est un algorithme",
   "Quelle définition décrit un algorithme ?",
   "une suite ordonnée d'instructions qui résout un problème",
   "Un algorithme est une suite d'instructions précises, rangées dans un ordre, qui mène à la solution d'un "
   "problème. Il existe avant tout langage : on peut l'écrire en français.",
   [("un programme écrit dans un langage informatique comme Python",
     "Un langage sert à traduire l'idée pour la machine. L'idée elle-même existe avant tout langage : elle peut "
     "s'écrire en français."),
    ("un schéma qui montre les pièces d'un objet technique",
     "Un tel schéma décrit l'objet dans l'espace, pièce par pièce. Cherche une définition qui parle d'actions qui "
     "s'enchaînent dans le temps."),
    ("une liste de composants à brancher sur une carte",
     "Des composants sont du matériel. La définition cherchée parle d'une méthode, pas d'objets à brancher.")],
   "Pense à une recette de cuisine : qu'est-ce qui permet à n'importe qui de la suivre ?",
   "Une recette donne des étapes précises, dans un ordre, pour arriver à un résultat. Cherche la définition qui dit "
   "la même chose, sans parler ni d'un langage, ni de matériel.",
   "Algorithme = des instructions, dans un ordre, pour résoudre un problème.", cle=False)

ex(1, "Suivre un losange",
   "La température mesurée vaut 28 °C. Quelle action le système exécute-t-il ?",
   "il éteint le ventilateur",
   "28 n'est pas strictement supérieur à 30 : la réponse à la question « T > 30 ? » est « non ». Je suis la "
   "branche « non », qui mène à « éteindre le ventilateur ».",
   [("il allume le ventilateur",
     "C'est l'action au bout de la branche « oui ». Remplace T par 28 dans la question du losange : la réponse "
     "est-elle « oui » ?"),
    ("il allume, puis éteint le ventilateur",
     "À chaque passage dans un losange, on ne suit qu'une seule branche : les deux actions ne peuvent pas "
     "s'enchaîner."),
    ("il n'exécute aucune des deux actions",
     "Un losange a toujours une réponse, « oui » ou « non » : l'une des deux branches est forcément suivie.")],
   "Remplace T par 28 dans la question écrite dans le losange : la réponse est « oui » ou « non » ?",
   "« 28 > 30 » est faux, donc la réponse est « non ». Pose ton doigt sur la flèche étiquetée « non » et suis-la "
   "jusqu'au bloc où elle arrive.",
   "Au losange, on calcule la réponse, puis on suit une seule branche.", cle=True,
   doc=dict(svg="ventilateur", legende="L'algorigramme du ventilateur"))

ex(1, "Les bornes d'un traitement qui se termine",
   "L'auto-test du matin commence, puis se termine. Quelle forme ont ses bornes DÉBUT et FIN ?",
   "un rectangle aux bords arrondis",
   "DÉBUT et FIN s'écrivent dans un terminal, un rectangle aux bords arrondis : c'est la forme réservée aux bornes "
   "d'un traitement qui se termine.",
   [("un rectangle aux angles droits",
     "Cette forme porte un traitement, au milieu du parcours : une flèche y entre et une flèche en sort."),
    ("un losange",
     "Cette forme pose une question, et deux flèches en sortent. DÉBUT n'a qu'une flèche qui sort, FIN n'a qu'une "
     "flèche qui entre."),
    ("un parallélogramme",
     "Cette forme fait entrer ou sortir une donnée (lire un capteur, envoyer un message) : elle ne marque ni le "
     "départ ni l'arrivée.")],
   "Cherche la forme qui n'a qu'une seule flèche : une qui sort pour DÉBUT, une qui entre pour FIN.",
   "Le terminal se reconnaît à ses bords arrondis. Relis la planche des cinq repères, dans le rappel de cours.",
   "Bords arrondis = DÉBUT ou FIN d'un traitement qui se termine.", cle=False, icones=True)

ex(1, "La donnée qui quitte le système",
   "La station envoie la vitesse du vent au téléphone du gardien. Dans quelle forme dessine-t-on "
   "« envoyer la vitesse du vent au gardien » ?",
   "un parallélogramme",
   "La vitesse du vent quitte la station pour aller chez le gardien : c'est une sortie de donnée. Une entrée ou "
   "une sortie de donnée se dessine dans un parallélogramme.",
   [("un rectangle",
     "Le rectangle porte un traitement qui reste à l'intérieur du système : un calcul, un compteur. Ici, une donnée "
     "part vers l'extérieur."),
    ("un losange",
     "Aucune question n'est posée : la station ne choisit rien, elle transmet une valeur."),
    ("un rectangle aux bords arrondis",
     "Cette forme est réservée à DÉBUT et FIN. L'envoi se fait au milieu du parcours.")],
   "Quelle donnée quitte le système, et vers qui va-t-elle ?",
   "La vitesse du vent sort de la station et arrive chez le gardien : elle franchit la frontière du système. Une "
   "seule forme sert à faire entrer ou sortir une donnée.",
   "Une donnée qui entre ou qui sort = un parallélogramme.", cle=True, icones=True)

ex(1, "La flèche d'affectation",
   "Dans l'instruction « defauts ← defauts + 1 », que fait la machine ?",
   "elle ajoute 1 au contenu de la variable defauts",
   "La flèche ← se lit « reçoit ». La machine calcule d'abord la partie droite avec l'ancienne valeur, defauts + "
   "1, puis range le résultat dans defauts : le contenu augmente de 1.",
   [("elle vérifie si defauts est égal à defauts + 1",
     "Vérifier une égalité, c'est comparer, avec le signe =. La flèche ← ne compare rien : elle range une valeur "
     "dans une variable."),
    ("elle crée une variable nommée « defauts + 1 »",
     "« defauts + 1 » n'est pas un nom : c'est un calcul. Un nom de variable ne contient pas de signe d'opération."),
    ("elle affiche la valeur de defauts suivie de + 1",
     "Rien ne s'affiche : afficher est une sortie, écrite AFFICHER et dessinée dans un parallélogramme.")],
   "Lis la flèche ← comme le mot « reçoit » : que reçoit defauts ?",
   "Avec defauts = 3 : la partie droite vaut 3 + 1 = 4, puis defauts reçoit 4. Le contenu de la case a changé ; "
   "aucune comparaison n'a eu lieu.",
   "← range une valeur (affectation) ; = compare deux valeurs.", cle=True)

ex(1, "Une surveillance qui ne s'arrête pas",
   "La station lit son capteur de vent chaque minute, jour et nuit, sans jamais s'arrêter. Dans son algorigramme, "
   "après « envoyer la mesure », où mène la flèche ?",
   "elle remonte vers « lire le capteur de vent »",
   "Un système qui surveille en continu n'atteint jamais FIN : après l'envoi, une flèche de retour remonte vers la "
   "lecture du capteur, et le parcours recommence.",
   [("elle descend jusqu'au terminal FIN, tout en bas",
     "Atteindre FIN arrêterait la surveillance après une seule mesure. Or la station doit mesurer jour et nuit."),
    ("elle s'arrête sans mener nulle part",
     "Une flèche mène toujours quelque part : sans pointe d'arrivée, le lecteur ne sait pas quoi exécuter ensuite."),
    ("elle mène à une copie de « lire le capteur »",
     "Recopier les mêmes blocs une infinité de fois serait impossible à dessiner : une répétition se montre par une "
     "flèche qui revient.")],
   "Si la flèche menait à FIN, combien de mesures la station ferait-elle ?",
   "Une seule mesure, puis plus rien. Pour recommencer sans fin, une flèche doit revenir vers un bloc déjà "
   "traversé.",
   "Un système qui surveille en continu revient lire son capteur : son parcours n'atteint pas FIN.", cle=False)

ex(1, "Le mot-clé de la répétition",
   "En pseudo-code, quel mot-clé annonce qu'un bloc d'instructions va se répéter ?",
   "TANT QUE … FAIRE",
   "TANT QUE … FAIRE fait revenir au test après chaque passage dans le bloc : le bloc se répète tant que la "
   "condition est vraie.",
   [("SI … ALORS … SINON",
     "SI choisit un chemin une seule fois : après le bloc, on continue sans revenir au test. Dans un algorigramme, "
     "c'est un losange sans flèche de retour."),
    ("DÉBUT … FIN",
     "Ces deux mots encadrent tout l'algorithme : ils ne font rien répéter."),
    ("AFFICHER",
     "AFFICHER envoie une donnée vers l'écran : c'est une sortie, pas une répétition.")],
   "Cherche le mot-clé qui oblige à revenir en arrière.",
   "Dans un algorigramme, la répétition se voit à une flèche de retour qui remonte vers un losange. En "
   "pseudo-code, un seul de ces mots-clés produit ce retour.",
   "TANT QUE = on revient au test ; SI = on choisit une fois.", cle=False)

ex(1, "Une flèche qui remonte",
   "On vient de passer dans le losange, et la réponse est « oui ». Quel bloc exécute-t-on ensuite ?",
   "le rectangle « c ← c + 1 », plus haut",
   "La branche « oui » part sur le côté, puis remonte : sa pointe rejoint le trait juste au-dessus de "
   "« c ← c + 1 ». On exécute donc ce rectangle une nouvelle fois, puis on revient au losange.",
   [("le parallélogramme « afficher c », plus bas",
     "C'est la suite de la branche « non ». Suis la pointe de la flèche « oui » : elle ne descend pas."),
    ("le terminal FIN, tout en bas",
     "Pour arriver à FIN, il faut passer par « afficher c », au bout de la branche « non »."),
    ("le rectangle « c ← 0 », tout en haut",
     "La flèche « oui » rejoint le trait sous ce rectangle : regarde où se trouve le point d'arrivée.")],
   "Pose ton doigt sur la flèche « oui » et suis-la jusqu'à sa pointe, même si elle monte.",
   "Un algorigramme ne se lit pas toujours de haut en bas : on suit le sens des pointes. La flèche « oui » remonte "
   "et rejoint le trait au-dessus d'un rectangle.",
   "On suit la pointe des flèches, pas le haut et le bas de la feuille.", cle=True,
   doc=dict(svg="remonte", legende="Un compteur qui compte jusqu'à 3"))

# ══════════ Manche 2 — Déroulement ══════════
ex(2, "Lire et calculer",
   "On saisit A = 4, puis B = 9. Qu'affiche cet algorithme ?",
   "13",
   "S reçoit A + B, c'est-à-dire 4 + 9 = 13. L'instruction « Afficher S » affiche donc 13.",
   [("36", "36 serait le résultat de A × B. Relis le signe écrit dans la ligne du calcul."),
    ("9", "9 est la valeur de B, le plus grand des deux nombres. Aucune comparaison n'est écrite dans cet "
          "algorithme."),
    ("49", "« 49 » met les deux chiffres bout à bout. Le signe + additionne des nombres.")],
   "Lis la ligne « S ← A + B » et remplace A et B par leurs valeurs.",
   "Trois temps : deux entrées (Lire A, Lire B), un calcul (S ← A + B), une sortie (Afficher S).",
   "Entrées, traitement, sortie : on remplace chaque variable par sa valeur.", pred=True,
   doc=dict(pre="DÉBUT\n  Lire A\n  Lire B\n  S ← A + B\n  Afficher S\nFIN"))

ex(2, "Le seuil, essayé trois fois",
   "On exécute ces lignes trois fois : avec x = 9, puis x = 10, puis x = 11. Quels affichages obtient-on, dans "
   "l'ordre ?",
   "Petit, Petit, Grand",
   "« 9 > 10 » est faux : Petit. « 10 > 10 » est faux, car 10 n'est pas strictement plus grand que 10 : Petit. "
   "« 11 > 10 » est vrai : Grand.",
   [("Petit, Grand, Grand", "Regarde la valeur qui tombe pile sur 10 : le signe écrit est >, pas ≥."),
    ("Grand, Grand, Petit", "Les deux branches sont inversées : relis ce qui suit ALORS et ce qui suit SINON."),
    ("Grand, Petit, Petit", "Le signe > se lit « strictement plus grand que » : 9 est-il plus grand que 10 ?")],
   "Fais un petit tableau sur ta feuille de brouillon : x, « x > 10 » (vrai ou faux), affichage.",
   "Le cas qui piège est x = 10 : « 10 > 10 » se lit « 10 est strictement plus grand que 10 », et c'est faux. "
   "Avec ≥, ce serait vrai.",
   "Essaie toujours trois valeurs : sous le seuil, pile sur le seuil, au-dessus.", pred=True,
   doc=dict(pre="SI x > 10 ALORS\n  Afficher « Grand »\nSINON\n  Afficher « Petit »\nFIN SI"),
   corr=dict(html=tableau(["x", "x > 10", "Affichage"],
                          [["9", "faux", "Petit"], ["10", "faux", "Petit"], ["11", "vrai", "Grand"]],
                          "Le tableau qui tranche : une ligne par essai")))

ex(2, "La valeur finale",
   "Que vaut A après ces deux lignes ?",
   "12",
   "Ligne 1 : A reçoit 5. Ligne 2 : on calcule la partie droite avec l'ancienne valeur, 5 + 7 = 12, puis A "
   "reçoit 12.",
   [("5", "5 est la valeur de départ : la deuxième ligne la remplace."),
    ("7", "7 est le nombre ajouté, pas le résultat du calcul."),
    ("57", "Le signe + additionne deux nombres ; il ne met pas les chiffres bout à bout.")],
   "Remplace A par sa valeur du moment dans la partie droite de la ligne 2.",
   "On calcule toujours la partie droite d'abord (5 + 7), puis on range le résultat à gauche, dans A.",
   "A ← A + 7 : on calcule à droite avec l'ancienne valeur, on range à gauche.", pred=True,
   doc=dict(pre="A ← 5\nA ← A + 7"))

ex(2, "Une ligne qui ne change rien",
   "Que vaut n après ces trois lignes, et laquelle ne change pas sa valeur ?",
   "6 ; la 3ᵉ ligne ne change rien",
   "Après la 1ʳᵉ ligne, n vaut 3. Après la 2ᵉ, n vaut 3 × 2 = 6. La 3ᵉ ligne calcule 6 − 0 = 6 : elle range dans n "
   "la valeur qu'il avait déjà.",
   [("6 ; la 2ᵉ ligne ne change rien", "La 2ᵉ ligne fait passer n de 3 à 6 : elle change bien sa valeur."),
    ("9 ; la 3ᵉ ligne ne change rien", "Refais la 2ᵉ ligne : l'opération écrite est une multiplication par 2."),
    ("0 ; la 3ᵉ ligne remet n à 0", "« n − 0 » retire zéro : ce n'est pas « n ← 0 ».")],
   "Note la valeur de n après chaque ligne, sur ta feuille de brouillon.",
   "2ᵉ ligne : 3 × 2. 3ᵉ ligne : retirer 0 à un nombre le laisse identique.",
   "Un tableau de suivi, une ligne par instruction, évite les erreurs.", pred=True,
   doc=dict(pre="n ← 3\nn ← n × 2\nn ← n − 0"))

ex(2, "Compter les tours",
   "Quand la boucle s'arrête, combien de nombres ont été affichés, et que vaut i ?",
   "5 nombres ; i vaut 6",
   "La boucle affiche 1, 2, 3, 4 et 5 : cinq nombres. Après l'affichage de 5, i reçoit 6 ; le test « 6 ≤ 5 » est "
   "faux, on sort. Le test a donc été évalué six fois, et i vaut 6.",
   [("5 nombres ; i vaut 5",
     "Après l'affichage de 5, il reste une instruction dans le bloc, « i ← i + 1 » : elle s'exécute avant le "
     "dernier test."),
    ("6 nombres ; i vaut 6",
     "Le test est évalué six fois, mais la sixième fois il est faux : le bloc, et donc l'affichage, ne s'exécute "
     "pas."),
    ("4 nombres ; i vaut 5", "Ce serait le cas avec « i < 5 ». Le signe écrit est ≤ : la valeur 5 passe le test.")],
   "Fais un tableau : valeur de i, résultat du test « i ≤ 5 », nombre affiché. Continue jusqu'à ce que le test "
   "soit faux.",
   "Distingue trois nombres : les affichages (le bloc exécuté), les tests évalués (un de plus : le dernier est "
   "faux) et la valeur finale de i.",
   "Une boucle TANT QUE évalue son test une fois de plus qu'elle ne tourne.", pred=True,
   doc=dict(pre="i ← 1\nTANT QUE i ≤ 5 FAIRE\n  Afficher i\n  i ← i + 1\nFIN TANT QUE"),
   corr=dict(html=tableau(["i au test", "i ≤ 5", "Affiché", "i après le tour"],
                          [["1", "vrai", "1", "2"], ["2", "vrai", "2", "3"], ["3", "vrai", "3", "4"],
                           ["4", "vrai", "4", "5"], ["5", "vrai", "5", "6"], ["6", "faux", "rien : on sort", "6"]],
                          "Six tests, cinq affichages, i vaut 6 à la fin")))

ex(2, "Suivre le chemin dans le schéma",
   "Pose ton doigt sur DÉBUT et suis les flèches. Par quelle branche sors-tu du losange la première fois, et "
   "qu'affiche l'algorithme ?",
   "par « non » ; rien ne s'affiche",
   "Au premier passage, i vaut 10 : « 10 < 5 » est faux. Je sors par la branche « non », qui mène directement à "
   "FIN. Le bloc n'est jamais exécuté : aucune sortie.",
   [("par « oui » ; 10 s'affiche une fois",
     "Le test se fait AVANT d'entrer dans le bloc : remplace i par 10 dans « i < 5 »."),
    ("par « oui » ; 10 à 14 s'affichent",
     "Cinq tours supposent un test vrai cinq fois. Le premier test est-il vrai avec i = 10 ?"),
    ("par « non » ; 10 s'affiche une fois",
     "La branche « non » mène directement à FIN : « afficher i » n'est pas sur ce chemin.")],
   "Avant tout, remplace i par sa valeur de départ dans la question du losange.",
   "Le losange est placé AVANT le bloc répété : si la réponse est « non » dès le départ, le bloc ne s'exécute "
   "pas une seule fois. Ce n'est pas un bogue.",
   "Une boucle TANT QUE peut tourner zéro fois : la trace dit alors « aucune sortie ».",
   doc=dict(svg="jamais", legende="Une boucle qui commence avec i = 10"))

ex(2, "Réparer une boucle sans fin",
   "Cette boucle ne s'arrête jamais. Quelle ligne faut-il écrire à la place de ▢ pour qu'elle affiche 1, 2, 3, 4, "
   "5 puis s'arrête ?",
   "i ← i + 1",
   "Rien ne faisait avancer i vers la sortie. Avec « i ← i + 1 » : 1er tour, on affiche 1 et i devient 2 ; "
   "2e tour, on affiche 2 et i devient 3… Au 5e tour, i devient 6 : « 6 ≤ 5 » est faux, la boucle s'arrête.",
   [("i ← i − 1",
     "Fais les deux premiers tours : i passe de 1 à 0, puis à −1. Il s'éloigne de 5 : le test reste vrai pour "
     "toujours."),
    ("i ← 1", "i reçoit 1 à chaque tour : il garde la même valeur, et le test reste vrai pour toujours."),
    ("i ← 5",
     "Fais les deux premiers tours : on affiche 1, puis 5, puis encore 5… i reste à 5 et « 5 ≤ 5 » est toujours "
     "vrai.")],
   "Une boucle a besoin de trois choses : une valeur de départ, un test, une instruction qui rapproche la variable "
   "de la sortie. Laquelle manque ?",
   "Essaie chaque ligne sur les deux premiers tours : quelles valeurs prend i ? Une seule fait passer i de 1 à 2, "
   "puis de 2 à 3.",
   "Toute boucle a besoin d'une progression vers sa sortie.", pred=True,
   doc=dict(pre="i ← 1\nTANT QUE i ≤ 5 FAIRE\n  Afficher i\n  ▢\nFIN TANT QUE"))

ex(2, "Ce qui doit venir avant",
   "La station doit lire la vitesse du vent, la comparer à 90 km/h, et déclencher la sirène si elle dépasse ce "
   "seuil. Quel enchaînement est correct ?",
   "lire le vent → tester « vent > 90 » → déclencher la sirène",
   "On ne peut décider qu'à partir d'une mesure déjà lue : la lecture du vent vient avant le test, et le test "
   "vient avant la sirène, qui n'est déclenchée que si la réponse est « oui ».",
   [("tester « vent > 90 » → lire le vent → déclencher la sirène",
     "Au moment du test, aucune vitesse n'a encore été lue : à quoi compare-t-on 90 ?"),
    ("lire le vent → déclencher la sirène → tester « vent > 90 »",
     "La sirène sonnerait avant que l'on sache si le vent dépasse 90 km/h."),
    ("déclencher la sirène → lire le vent → tester « vent > 90 »",
     "La sirène sonnerait à chaque fois, quel que soit le vent : le test arrive trop tard pour l'empêcher.")],
   "Pour chaque étape, demande-toi ce qui doit déjà exister avant de pouvoir la faire.",
   "Un test a besoin d'une valeur ; une action décidée par un test a besoin de sa réponse. Range les étapes selon "
   "ces deux dépendances.",
   "On lit une mesure avant de décider à partir de cette mesure.")

# ══════════ Manche 3 — Auto-test ══════════
ex(3, "Où mettre le compteur à zéro",
   "Où écrire l'instruction « defauts ← 0 » pour que la station compte tous les défauts du matin ?",
   "à l'emplacement ①",
   "Le compteur doit valoir 0 avant le premier tour, puis garder ce qu'il compte d'un tour à l'autre : on le met à "
   "zéro une seule fois, à l'emplacement ①, avant la boucle.",
   [("à l'emplacement ②",
     "② est dans la boucle : le compteur repartirait de zéro à chaque organe. Fais le calcul avec deux organes en "
     "panne : que vaut-il à la fin ?"),
    ("à l'emplacement ③",
     "③ est après la boucle : le compteur vaudrait 0 au moment de décider, quels que soient les défauts trouvés."),
    ("aux emplacements ① et ②",
     "La mise à zéro en ② effacerait, à chaque tour, ce qui a été compté aux tours précédents.")],
   "Imagine que l'instruction est répétée à chaque tour : que deviendrait un défaut compté au tour d'avant ?",
   "Un compteur se met à zéro une seule fois, avant le premier tour, et ne doit plus être effacé ensuite. Cherche "
   "l'emplacement traversé une seule fois, avant le point où revient la flèche de retour.",
   "Un compteur se met à zéro AVANT la boucle.",
   doc=dict(svg="auto_trous", legende="L'auto-test du matin, avec trois emplacements possibles"),
   corr=dict(svg="auto_annote", legende="L'algorigramme complet, annoté : un exemple guidé à garder"))

ex(3, "Dérouler un nouveau matin",
   "Ce matin, l'anémomètre et la sirène sont en panne ; le gyrophare et la liaison radio fonctionnent. Que vaut "
   "defauts juste après le 3ᵉ tour ?",
   "2",
   "Avant la boucle, defauts vaut 0. 1er tour : l'anémomètre est en panne, defauts passe à 1. 2e tour : le "
   "gyrophare fonctionne, defauts reste à 1. 3e tour : la sirène est en panne, defauts passe à 2.",
   [("1", "1 est la valeur après le 1er ou le 2e tour. Le 3e organe testé fonctionne-t-il ?"),
    ("3", "3 compterait le gyrophare, qui fonctionne : un organe en état n'ajoute rien au compteur."),
    ("0", "0 est la valeur avant la boucle : deux organes en panne ont déjà été testés.")],
   "Complète la trace ligne par ligne : un organe en panne ajoute 1, un organe qui fonctionne n'ajoute rien.",
   "Le compteur ne redescend jamais : il garde ce qu'il a compté. Après le 2e tour, il vaut toujours ce qu'il "
   "valait après le 1er.",
   "Une trace se remplit ligne par ligne : la valeur avant, ce qui se passe, la valeur après.",
   doc=dict(trace=True, legende="Ma trace du matin — à compléter (facultatif, ce n'est pas noté)"),
   corr=dict(html=tableau(["Tour", "Organe testé", "Résultat du test", "defauts après ce tour"],
                          [["—", "avant la boucle", "—", "0"], ["1", "anémomètre", "en panne", "1"],
                           ["2", "gyrophare", "fonctionne", "1"], ["3", "sirène", "en panne", "2"],
                           ["4", "liaison radio", "fonctionne", "2"]],
                          "La trace complète de ce matin")))

ex(3, "Le moment de l'envoi",
   "Toujours ce matin-là (anémomètre et sirène en panne), quand le bilan part-il, et que dit-il ?",
   "une fois, après le 4ᵉ tour : « défaut sur 2 organe(s) »",
   "La décision « defauts = 0 ? » est placée après la boucle : on ne la prend qu'une fois les quatre organes "
   "testés. defauts vaut alors 2, la réponse est « non », et un seul message part : « défaut sur 2 organe(s) ».",
   [("deux fois, aux tours 1 et 3 : « défaut sur 1 organe(s) »",
     "Ce serait le cas avec un envoi à l'intérieur de la boucle, dans la branche « en panne ». Où la décision "
     "est-elle placée sur le schéma ?"),
    ("quatre fois : un message à la fin de chaque tour",
     "Un message par tour supposerait un envoi dans la boucle : le gardien recevrait quatre messages chaque "
     "matin."),
    ("une fois, après le 4ᵉ tour : « défaut sur 4 organe(s) »",
     "4 compterait tous les organes testés. Le compteur n'augmente que pour un organe en panne.")],
   "Sur le schéma, la décision « defauts = 0 ? » est-elle dans la boucle ou après ?",
   "Après la boucle : une seule décision, donc un seul message. Reste à savoir ce que vaut defauts à ce moment-là "
   "— c'est la dernière ligne de ta trace.",
   "On teste dans la boucle ; on décide après, une seule fois.",
   doc=dict(svg="auto_complet", legende="L'auto-test du matin"),
   apres="Le message dit <b>combien</b> d'organes sont en panne, pas <b>lesquels</b> : un compteur ne retient qu'un "
         "nombre. Pour citer les organes, la station doit aussi les mémoriser, dans une liste des organes en panne "
         "— c'est l'instruction « ajouter organe à pannes » de l'atelier 3e_C6.2, séance 2.")

ex(3, "Deux écritures pour « au moins un »",
   "Le compteur defauts est un nombre entier : 0, 1, 2, 3… Quelle paire de tests veut dire, l'un comme l'autre, "
   "« au moins un défaut » ?",
   "defauts > 0 et defauts ≥ 1",
   "« Au moins un » veut dire 1, 2, 3… mais pas 0. Sur des entiers, « defauts > 0 » et « defauts ≥ 1 » sont vrais "
   "exactement pour les mêmes valeurs : 1, 2, 3…",
   [("defauts > 1 et defauts ≥ 1",
     "Essaie defauts = 1 : « 1 > 1 » est faux. Le premier test oublie le cas d'un seul défaut."),
    ("defauts > 0 et defauts = 1",
     "Essaie defauts = 2 : « 2 = 1 » est faux. Ce test ne reconnaît qu'un défaut, exactement."),
    ("defauts ≥ 0 et defauts > 0",
     "Essaie defauts = 0 : « 0 ≥ 0 » est vrai. Ce test annonce un défaut alors qu'il n'y en a aucun.")],
   "Essaie chaque test avec trois valeurs : 0, 1 et 2.",
   "Un bon test est faux pour 0 et vrai pour 1, 2, 3… Cherche la paire où les deux tests réussissent cet essai.",
   "Sur des entiers, « > 0 » et « ≥ 1 » disent la même chose. Avec des nombres à virgule, ce ne serait plus vrai.")

ex(3, "Le bloc répété",
   "Combien de fois s'exécute « n ← n + 1 », puis combien de fois « Envoyer defauts au gardien » ?",
   "4 fois, puis 1 fois",
   "« n ← n + 1 » est décalée entre TANT QUE et FIN TANT QUE : elle fait partie du bloc répété, exécuté pour n = "
   "1, 2, 3 et 4. « Envoyer » est écrite après FIN TANT QUE, sans décalage : elle s'exécute une fois, après la "
   "boucle.",
   [("4 fois, puis 4 fois",
     "« Envoyer » est écrite après FIN TANT QUE, au même niveau que TANT QUE : fait-elle partie du bloc répété ?"),
    ("1 fois, puis 1 fois",
     "« n ← n + 1 » est décalée entre TANT QUE et FIN TANT QUE : elle fait partie du bloc répété."),
    ("5 fois, puis 1 fois",
     "Le test est évalué 5 fois (la 5e fois, n vaut 5 et le test est faux), mais le bloc ne s'exécute que si le "
     "test est vrai.")],
   "Encadre, sur ta feuille de brouillon, les lignes comprises entre TANT QUE et FIN TANT QUE.",
   "Le décalage (l'indentation) et les mots TANT QUE … FIN TANT QUE délimitent le bloc répété. Ce qui est dedans "
   "s'exécute à chaque tour ; ce qui est après, une seule fois.",
   "Les délimiteurs et l'indentation montrent ce qui se répète.",
   doc=dict(pre="defauts ← 0\nn ← 1\nTANT QUE n ≤ 4 FAIRE\n  SI l'organe n est en panne ALORS\n"
                "    defauts ← defauts + 1\n  FIN SI\n  n ← n + 1\nFIN TANT QUE\nEnvoyer defauts au gardien"))

ex(3, "Le silence du matin",
   "Ce matin, la liaison radio, celle qui transmet le bilan, est en panne. À 7 h 10, le gardien n'a reçu aucun "
   "message. Que peut-il conclure avec cette seule observation ?",
   "qu'il manque le bilan, sans savoir quel organe est en cause",
   "Le gardien constate seulement que le bilan n'est pas arrivé. À distance, il ne peut pas savoir ce qui est en "
   "panne : la radio, l'alimentation de la station ou autre chose. L'absence de message est elle-même un signal "
   "d'alerte : il doit aller voir.",
   [("que la liaison radio est en panne, et aucun autre organe",
     "Rien n'arrive au gardien : il ne peut savoir ni quels organes ont été testés, ni lesquels sont en panne."),
    ("que la station va bien : pas de message, donc pas de défaut",
     "Un matin sans défaut envoie quand même un message, « station opérationnelle ». Le silence n'est donc pas "
     "une bonne nouvelle."),
    ("que la station a trouvé ses quatre organes en panne",
     "Aucun nombre n'est arrivé jusqu'au gardien : il n'a aucune information sur le nombre de défauts.")],
   "Par quel chemin physique le bilan doit-il passer pour arriver jusqu'au gardien ?",
   "Le bilan est calculé, mais le canal qui devait le porter est en panne. Le gardien ne reçoit rien : que sait-il "
   "vraiment, sans aller voir la station ?",
   "Un auto-test ne peut pas signaler la panne de son propre moyen de signalement : c'est l'absence de bilan qui "
   "doit alerter.")

# ══════════ Manche 4 — Transfert ══════════
ex(4, "La serre et ses deux seuils",
   "Entre 18 °C et 22 °C, le chauffage garde son état. Il est arrêté au départ, puis le capteur mesure 17 °C, "
   "20 °C et 23 °C. Dans quel état est le chauffage après chacune des trois mesures ?",
   "en marche, en marche, arrêté",
   "17 < 18 : on allume, le chauffage est en marche. 20 °C n'est ni sous 18 ni au-dessus de 22 : aucune commande, "
   "il garde son état, en marche. 23 > 22 : on éteint, il est arrêté.",
   [("en marche, arrêté, arrêté",
     "À 20 °C, les deux tests sont faux : quelle commande le chauffage reçoit-il ? Suis la branche « non » du "
     "second losange."),
    ("arrêté, en marche, arrêté",
     "À 17 °C, le premier test « T < 18 ? » est vrai : relis l'action au bout de sa branche « oui »."),
    ("en marche, en marche, en marche",
     "À 23 °C, le second test « T > 22 ? » est vrai : relis l'action au bout de sa branche « oui ».")],
   "Traite les mesures une par une, en notant l'état du chauffage après chacune. Que se passe-t-il quand les deux "
   "tests sont faux ?",
   "Entre 18 et 22 °C, la branche « non » du second losange revient à la lecture sans aucune commande : le "
   "chauffage garde l'état qu'il avait juste avant.",
   "Deux seuils créent une zone neutre : entre les deux, le système garde son état.",
   doc=dict(svg="serre", legende="L'algorigramme du chauffage de la serre"),
   apres="<b>Et en partant de l'arrêt, avec 20 °C ?</b> Les deux tests sont faux : le chauffage garde son état, il "
         "reste arrêté. À 20 °C, l'état dépend donc de ce qui s'est passé avant. C'est voulu : avec un seul seuil, "
         "le chauffage s'allumerait et s'éteindrait sans arrêt autour d'une seule valeur.")

ex(4, "ET : les deux conditions",
   "La commande est recalculée à chaque mesure. Parmi quatre situations — jour sans présence, jour avec présence, "
   "nuit sans présence, nuit avec présence —, dans combien la lampe est-elle allumée ?",
   "dans 1 situation sur 4",
   "Avec ET, la lampe ne s'allume que si les deux conditions sont vraies en même temps : la nuit, avec une "
   "présence. Dans les trois autres situations, la branche « non » commande l'extinction.",
   [("dans 2 situations sur 4",
     "Deux situations, ce serait le cas si une seule condition comptait, la nuit ou la présence. Relis le mot qui "
     "les relie."),
    ("dans 3 situations sur 4", "Trois situations, c'est le comportement de OU : au moins une condition vraie. "
                                "Le losange dit ET."),
    ("dans les 4 situations",
     "Le jour sans présence, aucune des deux conditions n'est vraie : la branche « non » commande l'extinction.")],
   "Fais un tableau de quatre lignes : nuit (oui ou non), présence (oui ou non), « nuit ET présence » (vrai ou "
   "faux).",
   "« A ET B » n'est vrai que si A est vrai et B est vrai. Compte les lignes où les deux valent « oui ».",
   "ET : les deux conditions. OU : au moins une.",
   doc=dict(svg="lampadaire", legende="L'algorigramme du lampadaire"),
   corr=dict(html=tableau(["Il fait nuit ?", "Présence ?", "nuit ET présence", "La lampe"],
                          [["non", "non", "faux", "éteinte"], ["non", "oui", "faux", "éteinte"],
                           ["oui", "non", "faux", "éteinte"], ["oui", "oui", "vrai", "allumée"]],
                          "Les quatre situations, essayées une à une")),
   apres="<b>Pour aller plus loin :</b> avec « nuit OU présence », la lampe serait allumée dans trois situations "
         "sur quatre ; avec « NON nuit », elle ne s'allumerait que le jour.")

ex(4, "Justifier le cas limite",
   "Un algorithme affiche « admis » si la moyenne est supérieure ou égale à 10. Un élève a exactement 10, et "
   "l'algorithme affiche « admis ». Quelle justification est correcte ?",
   "le test « moyenne ≥ 10 » est vrai pour une moyenne de 10",
   "Le signe ≥ se lit « supérieur ou égal » : il inclut l'égalité. Avec une moyenne de 10, « 10 ≥ 10 » est vrai, "
   "donc l'algorithme suit la branche qui affiche « admis ».",
   [("le test « moyenne ≥ 10 » arrondit la moyenne à l'unité au-dessus",
     "Un test compare la valeur telle qu'elle est : il n'arrondit rien. Et 10 n'a pas besoin d'être arrondi."),
    ("10 est strictement plus grand que 10, donc c'est vrai",
     "« 10 > 10 » est faux : 10 n'est pas strictement plus grand que lui-même. Ce n'est d'ailleurs pas le signe "
     "écrit ici."),
    ("le test est faux, mais l'algorithme admet par défaut",
     "Relis le signe écrit. Et un algorithme n'admet rien « par défaut » : il suit la branche que donne le test.")],
   "Lis le signe ≥ à voix haute, en entier.",
   "« Supérieur ou égal » : le cas « égal » fait partie du test. Cherche la justification qui le dit, sans inventer "
   "d'arrondi ni de règle cachée.",
   "≥ inclut l'égalité ; > l'exclut. Le cas limite s'essaie toujours.")

ex(4, "La branche oubliée",
   "Le besoin dit : un objet qui n'est ni métallique, ni en plastique, ni en verre doit être écarté dans le bac "
   "« refus ». Que faut-il écrire dans le cadre « ? », au bout de la dernière branche « non » ?",
   "diriger l'objet vers le bac « refus »",
   "Toute suite de tests doit prévoir le cas « aucun des précédents ». Ici, le besoin le dit : l'objet qui n'est "
   "reconnu par aucun test part dans le bac « refus ». Sans cette branche, il resterait sans décision.",
   [("diriger l'objet vers le bac « plastique »",
     "Le deuxième losange a déjà répondu « non » : l'objet n'est pas en plastique. Il polluerait ce bac."),
    ("arrêter le convoyeur jusqu'au soir",
     "Le besoin ne demande pas d'arrêt : un seul objet inconnu bloquerait toute la chaîne de tri."),
    ("remonter au premier test, « métal ? »",
     "Le même objet repasserait par les mêmes tests et recevrait les mêmes réponses : il tournerait en rond.")],
   "Relis le besoin : il dit précisément ce qui arrive à un objet non reconnu.",
   "La dernière branche « non » rassemble les objets qui ne sont ni métal, ni plastique, ni verre. Le besoin leur "
   "donne une destination.",
   "Toujours prévoir la branche « aucun des cas précédents ».",
   doc=dict(svg="tri", legende="L'algorigramme du tri, à compléter"))

ex(4, "Compter des pièces, pas des tours",
   "Une machine doit s'arrêter après la 500ᵉ pièce terminée. À chaque tour, elle tente une fabrication, et un "
   "capteur de sortie confirme si la pièce est vraiment terminée. Où placer « pieces ← pieces + 1 » ?",
   "dans la branche « oui » de « pièce confirmée ? »",
   "Un tour de boucle n'est pas forcément une pièce réussie. On ne compte une pièce que lorsque le capteur la "
   "confirme : dans la branche « oui » du test « pièce confirmée ? ».",
   [("au début de chaque tour, avant même la fabrication",
     "Au début du tour, la pièce n'existe pas encore : une fabrication ratée serait comptée comme une pièce."),
    ("après la boucle, quand la machine s'arrête",
     "Après la boucle, plus rien n'est compté pendant la fabrication : le compteur ne pourrait jamais atteindre "
     "500."),
    ("avant la boucle, juste après « pieces ← 0 »",
     "Avant la boucle, l'instruction ne s'exécute qu'une fois : le compteur vaudrait 1, quelles que soient les "
     "pièces fabriquées.")],
   "Qu'est-ce qui prouve qu'une pièce est vraiment terminée ?",
   "Le compteur doit augmenter exactement une fois par pièce confirmée : ni pour une fabrication ratée, ni une "
   "seule fois en tout.",
   "On compte ce que l'on veut mesurer : ici, les pièces confirmées, pas les tours.")

ex(4, "La porte qui relit la présence",
   "Une personne était dans le passage, puis elle en sort. Que fait la porte au tour suivant ?",
   "elle relit « absent », puis se ferme",
   "À chaque tour, la flèche de retour ramène au parallélogramme « lire la présence » : la nouvelle valeur, "
   "« absent », est lue. Au losange, la réponse est « non », et la porte se ferme.",
   [("elle reste ouverte jusqu'au soir",
     "Rien n'est écrit sur l'heure : la porte suit la présence, relue à chaque tour."),
    ("elle se ferme, puis ne lit plus la présence",
     "Après « fermer la porte », la flèche de retour remonte : la lecture continue, prête pour la personne "
     "suivante."),
    ("elle garde la présence lue avant",
     "La présence n'est pas gardée d'un tour à l'autre : elle est relue au début de chaque tour.")],
   "Pose ton doigt sur le bloc où la présence est lue, puis suis la flèche de retour jusqu'à lui.",
   "La présence est relue à chaque tour, dans le parallélogramme. Avec la valeur « absent », quelle branche du "
   "losange prends-tu ?",
   "Une condition surveillée en continu se relit à chaque tour de boucle.",
   doc=dict(svg="porte", legende="L'algorigramme de la porte automatique"))

ex(4, "Ce que mesure la sonde",
   "Un four équipé d'une sonde à cœur coupe la chauffe quand le centre du plat atteint 75 °C. Quelle donnée la "
   "sonde envoie-t-elle à l'algorithme ?",
   "la température au cœur du plat",
   "La sonde est un capteur : elle mesure la température au centre du plat et l'envoie à l'algorithme, qui la "
   "compare à 75 °C pour décider de couper la chauffe.",
   [("le temps écoulé depuis le départ",
     "Le temps se mesure avec une minuterie, pas avec une sonde plantée dans le plat."),
    ("la puissance de la résistance",
     "La puissance est une caractéristique de la résistance qui chauffe : la sonde, plantée dans le plat, ne la "
     "mesure pas."),
    ("l'ordre de couper la chauffe",
     "Un ordre est une décision : l'algorithme la prend, l'actionneur l'exécute. La sonde, elle, informe.")],
   "Une sonde plantée dans un plat : que peut-elle mesurer, là où elle se trouve ?",
   "Le capteur informe, l'algorithme décide, l'actionneur agit. Cherche la donnée mesurée, pas la décision.",
   "Le capteur informe, l'algorithme décide, l'actionneur agit.")

ex(4, "Le stock, essayé trois fois",
   "Un magasin commande un nouveau lot quand le test « stock < 15 » est vrai. On essaie l'algorithme avec un stock "
   "de 14, puis de 15, puis de 16. Pour quelles valeurs commande-t-il ?",
   "pour 14 seulement",
   "« 14 < 15 » est vrai : commande. « 15 < 15 » est faux, car 15 n'est pas strictement inférieur à 15 : pas de "
   "commande. « 16 < 15 » est faux : pas de commande.",
   [("pour 14 et pour 15", "À 15, le test « 15 < 15 » est-il vrai ? Le signe écrit est <, pas ≤."),
    ("pour 15 et pour 16", "Le signe < veut dire « strictement inférieur » : 16 est-il plus petit que 15 ?"),
    ("pour aucune des trois", "Essaie 14 : « 14 < 15 » est vrai, donc au moins une valeur déclenche la commande.")],
   "Essaie les trois valeurs une par une : sous le seuil, pile sur le seuil, au-dessus.",
   "Seule la valeur pile sur le seuil demande de l'attention : « < » exclut l'égalité.",
   "Le seuil s'essaie avec sa valeur exacte.",
   apres="<b>Défi :</b> si le stock reste à 14 pendant une semaine, l'algorithme commanderait à chaque mesure. Une "
         "variable « commande_en_cours », mise à vrai quand on commande et remise à faux à la livraison, éviterait "
         "les commandes en double : le test devient « stock < 15 ET NON commande_en_cours ».")
