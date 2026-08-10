# -*- coding: utf-8 -*-
"""Les 30 questions du QCM de l'atelier de planification des tâches (C7.1).

Toutes les bonnes réponses sont en position 0 ici : la répartition sur A/B/C/D
est faite ensuite par `_outils/fix_r.js`, de façon déterministe.

Répartition : 5e — suivre (10) · 4e — organiser (10) · 3e — élaborer (10).
Cinq questions sont illustrées par les captures réelles du logiciel.

Les valeurs numériques citées (durées, marges, chemin le plus long) ne sont pas
saisies ici : elles sont importées du corrigé calculé par `_verifier_planning.py`
à partir du seul CSV (règle n°54).
"""
import json
import pathlib

_C = json.loads((pathlib.Path(__file__).resolve().parent.parent / "_corrige_calcule.json")
                .read_text(encoding="utf-8"))
P5, P4, P3 = _C["indicateur-rangement-hall"], _C["jardin-connecte-brooklyn"], _C["capteur-confort-ny"]

IMG_SAISIE = {
    "src": "Images/ganttproject_1_saisir_les_taches_et_les_durees.png",
    "alt": "Capture de GanttProject en français : le tableau des tâches du jardin connecté, "
           "avec les colonnes Nom, Date de début, Date de fin et Durée, et neuf lignes de A à I "
           "dont la dernière a une durée de zéro.",
}
IMG_PROPS = {
    "src": "Images/ganttproject_2_proprietes_duree_de_la_tache.png",
    "alt": "Capture de la boîte Propriétés d'une tâche dans GanttProject : onglets Général, "
           "Prédécesseurs, Ressources et Colonnes personnalisées ; champs Nom, case Jalon, "
           "Date de début, Date de fin grisée, Durée.",
}
IMG_PRED = {
    "src": "Images/ganttproject_3_declarer_les_predecesseurs.png",
    "alt": "Capture de l'onglet Prédécesseurs : un tableau ID, Nom de la tâche, Relation, Retard, "
           "Contrainte, avec deux lignes en relation Fin-Début et un retard de zéro.",
}
IMG_BARRES = {
    "src": "Images/ganttproject_4_les_barres_et_les_dates.png",
    "alt": "Capture du diagramme : neuf barres bleues en escalier reliées par des flèches, un "
           "losange final, et une échelle de temps en semaines.",
}
IMG_CRIT = {
    "src": "Images/ganttproject_5_afficher_le_chemin_critique.png",
    "alt": "Capture du même diagramme après activation du chemin critique : sept barres sont "
           "hachurées, deux restent unies.",
}

Q = []


def q(c, n, question, options, expl, ex, err, refs, ret, img=None):
    assert len(options) == 4 and len(refs) == 4, n
    assert refs[0] == "", n
    for r in refs[1:]:
        assert len(r) > 20, (n, r)
    o = {"c": c, "n": n, "q": question, "o": options, "r": 0,
         "expl": expl, "ex": ex, "err": err, "d": refs, "ret": ret}
    if img:
        o["img"] = img
    Q.append(o)


# ═══════════════ 5e — SUIVRE un processus avec des tâches identifiées (10) ═══════════════

q("5e", "Ce qui fait une tâche",
  "Parmi ces quatre lignes, laquelle est une vraie tâche ?",
  ["Câbler le capteur d'humidité sur la carte",
   "Travailler sur le capteur",
   "Avancer le projet",
   "Faire des recherches sur l'arrosage"],
  "Une tâche est une chose dont on peut dire, à un instant donné, si elle est terminée ou non. "
  "« Câbler le capteur sur la carte » a une fin observable : le fil est branché, ou il ne l'est pas.",
  "En fin de séance, le professeur passe et demande « c'est fini ? ». Sur une vraie tâche, la "
  "réponse est oui ou non, jamais « à peu près ».",
  "Écrire des intentions plutôt que des tâches, ce qui rend le planning invérifiable.",
  ["",
   "« Travailler sur » ne finit jamais : on peut travailler sur le capteur toute l'année sans que rien ne soit terminé.",
   "« Avancer le projet » décrit une direction, pas un état atteint : aucun jour ne permettra de dire que c'est fait.",
   "« Faire des recherches » n'a pas de fin définie non plus ; il faudrait dire ce qu'on cherche et à quel moment on s'arrête."],
  "Une tâche : on peut dire, à un instant donné, si elle est finie."),

q("5e", "Le jalon",
  "« L'indicateur est en service » figure dans le planning avec une durée de 0. Pourquoi ?",
  ["parce que ce n'est pas un travail à faire, mais un état atteint : c'est un jalon",
   "parce qu'on a oublié d'estimer sa durée",
   "parce que c'est la tâche la plus rapide du projet",
   "parce qu'elle est faite par toute la classe et pas par un binôme"],
  "Un jalon est un point de contrôle : il marque qu'on est arrivé quelque part. Il ne consomme "
  "aucun temps, donc sa durée est nulle, et le logiciel le dessine en losange.",
  "« Le cahier des charges est validé », « le prototype fonctionne » : des jalons, pas des tâches.",
  "Compter le jalon comme une tâche et ajouter une séance qui n'existe pas.",
  ["",
   "La durée n'a pas été oubliée : elle vaut zéro parce qu'il n'y a rien à faire, seulement quelque chose à constater.",
   "Ce n'est pas une question de rapidité : même la tâche la plus rapide dure au moins un peu, le jalon ne dure pas du tout.",
   "Qui réalise une tâche ne change rien à sa durée ; le jalon est à zéro par nature, quelle que soit la personne concernée."],
  "Un jalon ne dure pas : il constate qu'on est arrivé."),

q("5e", "Le mot du programme",
  "Le programme appelle ce dessin « diagramme de planification des tâches ». Dans les entreprises, on l'appelle…",
  ["diagramme de Gantt, du nom de l'ingénieur Henry Gantt",
   "diagramme de Pareto",
   "organigramme",
   "diagramme en bâtons"],
  "Le concept porte le nom du programme ; l'outil garde le nom du métier. Les deux désignent le "
  "même dessin, et savoir les deux évite d'être perdu devant un logiciel ou un sujet d'examen.",
  "Le logiciel utilisé en classe s'appelle GanttProject : le nom du métier est écrit sur la fenêtre.",
  "Croire que « Gantt » désigne autre chose que le diagramme de planification des tâches.",
  ["",
   "Le diagramme de Pareto classe des causes par importance : il ne place rien dans le temps.",
   "Un organigramme montre qui commande qui dans une organisation, pas ce qui doit attendre quoi.",
   "Un diagramme en bâtons compare des quantités ; il n'a pas d'axe du temps ni de contraintes entre barres."],
  "Diagramme de planification des tâches = diagramme de Gantt."),

q("5e", "Suivre, c'est dire la conséquence",
  "Suivre un planning, en 5e, c'est savoir dire à chaque séance :",
  ["ce qui est fini, ce qui est en retard, et ce que ce retard décale",
   "combien d'élèves ont travaillé",
   "quelle tâche était la plus difficile",
   "si le professeur est content du travail"],
  "Un suivi utile ne se contente pas de constater. Il relie le retard à sa conséquence : la date "
  "de fin bouge, ou elle ne bouge pas — et il faut pouvoir dire laquelle des deux.",
  "« C est en retard d'une séance, donc la mise en service recule d'une séance » : voilà un suivi.",
  "Dire « on a du retard » sans dire ce que ce retard décale.",
  ["",
   "Le nombre d'élèves qui ont travaillé ne dit rien de l'avancement : on peut être nombreux sur une tâche qui n'avance pas.",
   "La difficulté ressentie n'est pas une information de planning ; une tâche facile peut bloquer tout le projet.",
   "La satisfaction du professeur n'est pas un état du projet : le planning décrit des tâches, pas des appréciations."],
  "Suivre, c'est dire le retard ET ce qu'il décale."),

q("5e", "Un retard sur la chaîne",
  "Dans le planning de l'indicateur, la tâche C est sur la chaîne qui décide de la fin. "
  "Elle prend une séance de retard. La mise en service…",
  ["recule d'une séance",
   "ne bouge pas",
   "recule de deux séances",
   "avance d'une séance"],
  "Une tâche sans marge transmet intégralement son retard à tout ce qui suit : il n'y a, par "
  "définition, aucun jeu pour l'absorber.",
  "Le calcul du planning donne un chemin le plus long de " + " → ".join(P5["chemin"]) +
  ", et C en fait partie.",
  "Croire qu'une séance de retard « se rattrapera bien toute seule ».",
  ["",
   "Elle bouge : C n'a aucune marge, donc tout ce qui l'attend est décalé d'autant.",
   "Le retard n'est pas doublé en chemin : une séance de retard donne une séance de décalage, pas deux.",
   "Un retard ne fait jamais avancer la fin d'un projet ; au mieux il ne la décale pas."],
  "Retard sur la chaîne = retard sur tout le projet."),

q("5e", "Un retard sur une tâche à marge",
  "La tâche D possède une marge d'une séance. Elle prend une séance de retard. La mise en service…",
  ["ne bouge pas : la marge absorbe exactement ce retard",
   "recule d'une séance",
   "recule d'une demi-séance",
   "dépend du nombre d'élèves du groupe"],
  "La marge est précisément la quantité de retard qu'une tâche peut prendre sans rien décaler. "
  "Une séance de marge absorbe une séance de retard, et pas une de plus.",
  "Dans ce planning, la tâche qui a de la marge est : " + ", ".join(
      "%s (+%d séance)" % (i, m) for i, m in sorted(P5["marges"].items()) if m) + ".",
  "Traiter toutes les tâches comme également urgentes, et s'épuiser là où ça ne sert à rien.",
  ["",
   "Elle ne recule pas : c'est justement à cela que sert la marge, et c'est pour cela qu'on la calcule.",
   "Une marge se compte en séances entières ici : elle absorbe le retard, ou elle ne l'absorbe pas.",
   "Le nombre d'élèves ne change pas la structure du planning : la marge vient des contraintes, pas des effectifs."],
  "La marge, c'est le retard qu'on peut prendre sans rien décaler."),

q("5e", "Une tâche qui en attend deux",
  "La tâche E doit attendre C et D. Elle peut commencer :",
  ["après la plus tardive des deux",
   "après la première des deux qui se termine",
   "en même temps que C",
   "dès le début du projet, puisqu'elle est longue"],
  "Attendre deux tâches, c'est les attendre toutes les deux. La contrainte la plus contraignante "
  "est celle qui finit le plus tard ; c'est elle qui fixe le départ.",
  "Si C finit à la séance 4 et D à la séance 3, E commence à la séance 5 — pas à la 4.",
  "Démarrer dès que la première condition est remplie, et devoir tout refaire.",
  ["",
   "Commencer après la première reviendrait à travailler sans ce que la seconde devait fournir.",
   "Commencer en même temps que C reviendrait à ignorer complètement la contrainte : C n'est pas finie.",
   "La longueur d'une tâche ne lui donne aucun droit de démarrer plus tôt ; seules les contraintes décident."],
  "Une tâche qui en attend plusieurs part après la plus tardive."),

q("5e", "Le tableau du logiciel",
  "Sur cette capture, quelle colonne dit combien de temps dure chaque tâche ?",
  ["la colonne Durée, à droite du tableau",
   "la colonne Nom",
   "la colonne Date de début",
   "la colonne Date de fin"],
  "Le tableau de gauche comporte quatre colonnes : Nom, Date de début, Date de fin et Durée. "
  "C'est la dernière qui porte le nombre de séances.",
  "Sur la dernière ligne, la valeur 0 signale le jalon : rien à faire, seulement un état atteint.",
  "Confondre la durée d'une tâche avec sa date de début.",
  ["",
   "La colonne Nom porte le libellé de la tâche : ce qu'il y a à faire, pas combien de temps cela prend.",
   "La date de début dit QUAND on commence, pas COMBIEN DE TEMPS on y passe.",
   "La date de fin est calculée à partir du début et de la durée : elle en découle, elle ne la donne pas."],
  "Nom, Date de début, Date de fin, Durée : quatre colonnes, quatre informations différentes.",
  img=IMG_SAISIE),

q("5e", "Estimer, ce n'est pas savoir",
  "On écrit « 2 séances » en face d'une tâche. Ce nombre est :",
  ["une estimation, qu'on comparera au réel à la fin du projet",
   "une mesure exacte, connue à l'avance",
   "une obligation : la tâche devra durer exactement 2 séances",
   "une valeur inutile tant que la tâche n'est pas faite"],
  "Personne ne connaît la durée d'une tâche avant de l'avoir faite. On l'estime, on l'écrit, et "
  "on la confronte ensuite à ce qui s'est passé : c'est ainsi qu'on estime mieux la fois suivante.",
  "En fin de projet, comparer durées estimées et durées réelles est l'exercice le plus formateur "
  "de toute la planification.",
  "Refuser d'écrire une durée « parce qu'on ne peut pas savoir », et se priver de tout planning.",
  ["",
   "Aucune durée de projet n'est connue exactement à l'avance : si elle l'était, il n'y aurait pas besoin de planifier.",
   "Le planning n'oblige pas la tâche à durer ce qu'on a écrit ; il annonce ce qu'on prévoit, et se corrige.",
   "Une estimation écrite sert immédiatement : c'est elle qui permet de calculer la date de fin prévue."],
  "Une durée s'estime. Et une estimation jamais comparée au réel ne s'améliore jamais."),

q("5e", "Ce qu'un planning sert vraiment",
  "À quoi sert d'abord un planning, dans un projet de classe ?",
  ["à savoir où il faut se dépêcher, et où c'est inutile",
   "à décorer le compte rendu de projet",
   "à prouver au professeur qu'on a travaillé",
   "à répartir les élèves en groupes de taille égale"],
  "La planification produit une information qu'aucune bonne volonté ne donne : quelles tâches "
  "commandent la date de fin, et lesquelles peuvent attendre sans conséquence.",
  "Deux groupes travaillent aussi dur ; celui qui sait où se dépêcher finit plus tôt.",
  "Faire un planning une fois au début, ne plus jamais le regarder, et le joindre au dossier.",
  ["",
   "Un planning qui ne sert qu'à illustrer un dossier n'a jamais fait gagner une seule séance.",
   "Prouver l'effort fourni n'est pas son objet : un planning décrit des tâches et des dates, pas du mérite.",
   "La taille des groupes ne se déduit pas du planning ; ce sont les contraintes entre tâches qui décident de ce qui peut avancer ensemble."],
  "Un planning dit OÙ il faut se dépêcher."),


# ═══════════════ 4e — ORGANISER un processus avec des tâches identifiées (10) ═══════════════

q("4e", "La contrainte d'antériorité",
  "Écrire « C ne peut commencer qu'après B », c'est poser :",
  ["une contrainte d'antériorité",
   "une durée",
   "un jalon",
   "une marge"],
  "Le programme nomme trois choses : les tâches, leur durée, et les contraintes entre tâches. "
  "L'antériorité est la contrainte de base : elle dit ce qui doit attendre quoi.",
  "« Assembler » attend « fabriquer le support » : sans support, il n'y a rien à assembler.",
  "Confondre l'ordre dans lequel on a écrit les tâches avec l'ordre dans lequel elles doivent se faire.",
  ["",
   "Une durée dit combien de temps une tâche prend, pas ce qu'elle doit attendre.",
   "Un jalon est un point de contrôle sans durée ; ce n'est pas une relation entre deux tâches.",
   "Une marge est un résultat de calcul : elle se déduit des contraintes, elle ne se pose pas."],
  "Une contrainte d'antériorité : B attend A."),

q("4e", "Le parallélisme",
  "Deux tâches entre lesquelles il n'existe aucune contrainte :",
  ["peuvent être menées en même temps",
   "doivent quand même être faites l'une après l'autre",
   "sont forcément sur le chemin le plus long",
   "doivent être fusionnées en une seule tâche"],
  "L'absence de contrainte est une information, pas un oubli : elle autorise le travail simultané. "
  "C'est le seul endroit où un groupe gagne réellement du temps en se répartissant le travail.",
  "Dans le jardin connecté, câbler le capteur et fabriquer le support n'ont rien à s'échanger : "
  "les deux peuvent avancer ensemble.",
  "Faire les tâches dans l'ordre alphabétique du tableau, et perdre tout le parallélisme.",
  ["",
   "Rien n'oblige à les enchaîner : si aucune n'attend l'autre, les enchaîner ne fait que perdre du temps.",
   "Deux tâches parallèles peuvent parfaitement être hors du chemin le plus long ; le parallélisme ne dit rien de la criticité.",
   "Fusionner deux tâches indépendantes ferait disparaître l'information la plus utile : qu'elles peuvent avancer ensemble."],
  "Pas de contrainte = travail en même temps."),

q("4e", "La date au plus tôt",
  "La date au plus tôt d'une tâche, c'est :",
  ["le moment le plus précoce où elle peut commencer, compte tenu de ce qu'elle attend",
   "le moment où elle doit obligatoirement commencer",
   "le moment où elle se termine",
   "la date choisie par le professeur"],
  "C'est une limite basse, pas un ordre. On ne peut pas commencer avant ; on peut commencer après, "
  "dans la limite de la marge.",
  "Une tâche dont la date au plus tôt est la séance 5 ne peut pas démarrer en séance 4, même si "
  "le groupe est disponible.",
  "Lire une date au plus tôt comme une convocation, et croire qu'on est en retard dès qu'on ne "
  "démarre pas ce jour-là.",
  ["",
   "Rien n'oblige à commencer exactement à cette date : les tâches à marge peuvent démarrer plus tard sans conséquence.",
   "La date de fin s'obtient en ajoutant la durée à la date de début ; ce n'est pas la même information.",
   "Elle n'est pas choisie : elle est calculée à partir des durées et des contraintes, et personne ne peut la décider."],
  "Date au plus tôt : une limite basse, calculée, pas un ordre."),

q("4e", "Le calcul, de proche en proche",
  "Comment trouve-t-on la date au plus tôt d'une tâche, sans logiciel ?",
  ["en prenant la fin la plus tardive parmi les tâches qu'elle attend",
   "en additionnant les durées de toutes les tâches précédentes du tableau",
   "en divisant la durée totale par le nombre de tâches",
   "en la plaçant au milieu du projet"],
  "On part du début et on descend : pour chaque tâche, on regarde toutes celles qu'elle attend, "
  "on garde celle qui finit le plus tard, et on commence juste après. Le logiciel ne fait rien "
  "d'autre — il le fait seulement plus vite.",
  "Une tâche qui attend C (fin en séance 4) et E (fin en séance 5) commence en séance 6.",
  "Additionner toutes les durées et croire qu'on obtient la durée du projet.",
  ["",
   "Additionner tout le tableau ignore le parallélisme : plusieurs tâches avancent en même temps, leurs durées ne s'ajoutent pas.",
   "Une moyenne n'a aucun sens ici : les tâches n'ont ni la même durée ni les mêmes contraintes.",
   "Placer une tâche « au milieu » revient à inventer une date que rien ne justifie."],
  "Chaque tâche part après la PLUS TARDIVE de celles qu'elle attend."),

q("4e", "La somme n'est pas la durée",
  "Dans le projet du jardin connecté, la somme des durées vaut " +
  str(sum(P4["duree_tache"].values())) + " séances, et le projet en dure " +
  str(P4["duree_totale"]) + ". Pourquoi cet écart ?",
  ["parce que certaines tâches avancent en même temps",
   "parce qu'on a oublié des tâches",
   "parce que le jalon ne compte pas",
   "parce qu'une séance ne fait pas une heure entière"],
  "L'écart mesure exactement le parallélisme du projet. Plus il est grand, plus le projet permet "
  "de travailler simultanément.",
  "Écrire le programme pendant que d'autres câblent : deux durées qui s'écoulent en même temps, "
  "donc une seule qui compte.",
  "Annoncer aux familles une durée égale à la somme des tâches, et se tromper du simple au double.",
  ["",
   "Aucune tâche ne manque : l'écart vient de la structure du planning, pas d'un oubli de saisie.",
   "Le jalon dure zéro : le retirer ou l'ajouter ne change strictement rien à la somme.",
   "La longueur d'une séance ne change pas le rapport entre la somme et la durée du projet : on compte en séances des deux côtés."],
  "La durée d'un projet n'est pas la somme des durées de ses tâches."),

q("4e", "Fin-Début",
  "Sur cette capture, la relation « Fin-Début » signifie :",
  ["la fin de la tâche attendue commande le début de celle-ci",
   "les deux tâches finissent le même jour",
   "les deux tâches commencent le même jour",
   "la tâche se termine dès qu'elle commence"],
  "C'est exactement la contrainte d'antériorité du programme, dite avec le vocabulaire du "
  "logiciel. C'est la seule relation dont on ait besoin au collège.",
  "F attend C et E : deux lignes Fin-Début, retard 0, dans l'onglet Prédécesseurs.",
  "Créer un lien par glisser-déposer sans jamais vérifier quelles tâches ont été reliées.",
  ["",
   "Finir ensemble serait une relation « Fin-Fin » : ce n'est pas ce qui est écrit ici.",
   "Commencer ensemble serait une relation « Début-Début », qui ne correspond pas à une antériorité.",
   "Une tâche qui se terminerait dès son début aurait une durée nulle : ce serait un jalon, pas une relation."],
  "Fin-Début : la fin de l'une commande le début de l'autre.",
  img=IMG_PRED),

q("4e", "Lire le parallélisme sur le dessin",
  "Sur ce diagramme, deux barres qui se chevauchent verticalement montrent :",
  ["deux tâches qui avancent en même temps",
   "deux tâches qui se contredisent",
   "une erreur de saisie",
   "deux tâches faites par la même personne"],
  "C'est le service principal du dessin : le parallélisme se voit d'un coup d'œil, alors qu'il est "
  "invisible dans une simple liste de tâches.",
  "Câbler le capteur et fabriquer le support occupent les mêmes journées : leurs barres se "
  "superposent dans le temps.",
  "Vouloir « aligner proprement » les barres et détruire l'information qu'elles portaient.",
  ["",
   "Deux tâches simultanées ne se contredisent pas : rien dans le planning n'interdit de travailler à deux endroits à la fois.",
   "Ce n'est pas une erreur : c'est au contraire le résultat que l'on cherche en organisant un projet.",
   "Le diagramme ne dit rien de qui réalise les tâches ; les ressources sont un autre onglet du logiciel."],
  "Barres qui se chevauchent = tâches simultanées.",
  img=IMG_BARRES),

q("4e", "La preuve qu'un planning existe",
  "Un diagramme sans aucune flèche entre les barres signifie :",
  ["qu'aucune contrainte n'a été déclarée : ce n'est pas encore un planning",
   "que le projet est particulièrement simple",
   "que toutes les tâches sont critiques",
   "que le logiciel n'a pas fini de calculer"],
  "Sans contrainte, le logiciel place tout au premier jour. Le dessin est net, et il ne prouve "
  "rien : les flèches sont la trace visible du travail de planification.",
  "Un élève qui saisit dix tâches sans lien obtient dix barres alignées à gauche, toutes "
  "commençant le même jour.",
  "Rendre un diagramme joli mais vide, et croire le travail fait.",
  ["",
   "Un projet réel comporte presque toujours des dépendances : leur absence signale un oubli, pas une simplicité.",
   "Sans contrainte, aucune tâche n'est critique au sens du planning : il n'y a même pas de chaîne.",
   "Le calcul du logiciel est instantané ; il n'y a pas d'attente qui expliquerait des flèches manquantes."],
  "Pas de flèche, pas de planning."),

q("4e", "Organiser, c'est décider",
  "Après avoir repéré deux tâches parallèles, que fait un groupe qui organise vraiment ?",
  ["il décide qui travaille sur l'une pendant que d'autres travaillent sur l'autre",
   "il choisit celle qui a l'air la plus intéressante et fait l'autre plus tard",
   "il fusionne les deux tâches pour aller plus vite",
   "il attend l'avis du professeur avant de commencer"],
  "Le parallélisme n'est utile que s'il devient une décision d'équipe. Sinon, l'information reste "
  "sur le papier et le projet avance comme avant.",
  "« Léa et Sam câblent, Inès et Tom fabriquent le support » : voilà la décision que permet le "
  "planning.",
  "Repérer le parallélisme, le noter, et continuer à travailler tous sur la même tâche.",
  ["",
   "Choisir la plus intéressante et remettre l'autre revient à renoncer au gain de temps qu'on venait de découvrir.",
   "Fusionner deux tâches indépendantes ne les rend pas plus rapides : elles restent deux travaux distincts.",
   "Le planning est justement fait pour décider sans attendre : il donne l'information nécessaire au groupe."],
  "Organiser, c'est transformer le parallélisme en décision d'équipe."),

q("4e", "La marge",
  "Une tâche possède une marge de 3 séances. Cela signifie :",
  ["qu'elle peut prendre jusqu'à 3 séances de retard sans décaler la fin du projet",
   "qu'elle dure 3 séances de plus que prévu",
   "qu'elle doit être finie 3 séances avant la fin du projet",
   "qu'elle est trois fois moins importante que les autres"],
  "La marge est la quantité de retard tolérable. Elle se calcule à partir des contraintes : "
  "elle existe parce que ce qui suit la tâche attend aussi autre chose, plus tardif.",
  "Dans le jardin connecté, les tâches à marge sont : " + ", ".join(
      "%s (+%d)" % (i, m) for i, m in sorted(P4["marges"].items()) if m) + ".",
  "Confondre marge et importance, et négliger une tâche à marge jusqu'à ce qu'elle devienne critique.",
  ["",
   "La marge ne modifie pas la durée de la tâche : celle-ci reste exactement ce qui a été estimé.",
   "Rien n'impose de la finir en avance : la marge autorise du retard, elle n'exige pas de l'avance.",
   "L'importance d'une tâche est une autre question : une tâche à marge peut être indispensable au projet."],
  "La marge : le retard qu'on peut prendre sans rien décaler."),


# ═══════════════ 3e — ÉLABORER un processus avec des tâches identifiées (10) ═══════════════

q("3e", "Le chemin le plus long",
  "Le chemin le plus long d'un projet, c'est :",
  ["la suite de tâches enchaînées la plus longue, du début au jalon final",
   "la suite des tâches qui durent le plus longtemps",
   "la suite des tâches les plus difficiles",
   "la liste de toutes les tâches, dans l'ordre du tableau"],
  "Ce qui compte, c'est l'enchaînement : chaque tâche de la chaîne attend la précédente. C'est "
  "cette chaîne, et elle seule, qui fixe la date de fin du projet.",
  "Dans le capteur de confort, ce chemin est " + " → ".join(P3["chemin"]) +
  ", pour " + str(P3["duree_totale"]) + " séances.",
  "Prendre les tâches longues une par une, sans regarder si elles s'enchaînent.",
  ["",
   "Une tâche longue qui n'attend personne et que personne n'attend ne fait partie d'aucune chaîne.",
   "La difficulté ne joue aucun rôle : une tâche critique peut être la plus facile du projet.",
   "L'ordre du tableau est un ordre d'écriture ; il ne dit rien des contraintes réelles."],
  "Le chemin le plus long : la suite ENCHAÎNÉE la plus longue."),

q("3e", "Raccourcir hors du chemin",
  "On raccourcit d'une séance une tâche qui n'est pas sur le chemin le plus long. Le projet gagne :",
  ["aucune séance",
   "une séance",
   "une demi-séance",
   "cela dépend du nombre d'élèves mobilisés"],
  "Une tâche hors chemin possède de la marge : ce qui la suit attend de toute façon autre chose, "
  "plus tardif. L'accélérer n'avance donc rien du tout.",
  "Dans le capteur de confort, les tâches hors chemin sont " + ", ".join(
      "%s (+%d)" % (i, m) for i, m in sorted(P3["marges"].items()) if m) +
  " : les accélérer ne change pas la date de fin.",
  "Mobiliser tout le groupe sur une tâche à marge et s'étonner que le projet n'avance pas.",
  ["",
   "Le gain serait d'une séance seulement si la tâche appartenait à la chaîne qui commande la fin.",
   "Il n'y a pas de gain partiel : hors du chemin, le gain est exactement nul.",
   "Le nombre d'élèves ne change pas la structure : la marge vient des contraintes, pas des effectifs."],
  "Accélérer hors du chemin ne fait rien gagner."),

q("3e", "Raccourcir sur le chemin",
  "On raccourcit d'une séance une tâche du chemin le plus long. Le projet gagne :",
  ["une séance, tant qu'aucun autre chemin ne devient le plus long à son tour",
   "une séance, définitivement",
   "aucune séance",
   "autant de séances qu'il y a de tâches après elle"],
  "Le chemin le plus long est le résultat d'un calcul sur les durées du moment. Dès qu'on modifie "
  "une durée, il faut recalculer : un autre chemin, jusque-là plus court, peut devenir le plus long.",
  "Raccourcir une tâche de 3 à 1 séance peut ne faire gagner qu'une séance, si une autre chaîne "
  "prend le relais.",
  "Croire qu'on peut raccourcir indéfiniment un projet en accélérant toujours la même chaîne.",
  ["",
   "Le gain n'est pas définitivement acquis : au-delà d'un certain point, une autre chaîne devient contraignante.",
   "Le gain n'est pas nul : sur le chemin, chaque séance économisée se répercute sur la date de fin.",
   "Le gain ne se multiplie pas par le nombre de tâches suivantes : elles sont simplement décalées d'autant, une seule fois."],
  "Sur le chemin, on gagne — jusqu'à ce qu'un autre chemin prenne le relais."),

q("3e", "Le nom du métier",
  "Le chemin le plus long s'appelle, dans les entreprises, le chemin critique. « Critique » veut dire ici :",
  ["sans aucune marge",
   "difficile",
   "important",
   "risqué"],
  "Le mot ne décrit ni la difficulté, ni l'enjeu : il décrit une propriété calculée. Une tâche "
  "critique est une tâche dont le moindre retard décale la fin.",
  "Dans le capteur de confort, les tâches critiques sont " + ", ".join(P3["chemin"]) +
  " : leur marge est nulle.",
  "Traiter les tâches « critiques » comme les plus difficiles, et les confier aux plus rapides.",
  ["",
   "Une tâche critique peut être très facile : coller une étiquette peut être critique si tout attend cette étiquette.",
   "Toutes les tâches d'un projet sont importantes ; la criticité est une propriété du planning, pas du contenu.",
   "Le risque est une autre notion : une tâche risquée peut avoir beaucoup de marge, et une tâche sûre n'en avoir aucune."],
  "Critique = sans marge. Ni difficile, ni important."),

q("3e", "Ce que montre la capture",
  "Sur cette capture, la commande a été activée et sept barres sont hachurées. Les deux barres restées unies sont :",
  ["les deux tâches qui possèdent de la marge",
   "les deux tâches les plus longues",
   "les deux tâches non commencées",
   "les deux tâches qui n'ont pas de responsable"],
  "L'affichage du chemin critique met en évidence les tâches de marge nulle. Celles qui restent "
  "unies sont donc, exactement, celles qui peuvent prendre du retard sans conséquence.",
  "Ici, ce sont C (câbler) et D (écrire le programme) : leurs marges valent respectivement " +
  str(P4["marges"]["C"]) + " et " + str(P4["marges"]["D"]) + " séances.",
  "Dire « les barres rouges », alors que la mise en évidence change d'aspect selon les versions.",
  ["",
   "La longueur des barres n'a rien à voir : la tâche la plus longue de ce projet est justement sur le chemin critique.",
   "L'avancement se règle ailleurs, dans le champ Avancement des propriétés : le chemin critique ne le regarde pas.",
   "Les responsables se déclarent dans l'onglet Ressources ; le chemin critique se calcule sans eux."],
  "Les tâches mises en évidence sont celles de marge nulle.",
  img=IMG_CRIT),

q("3e", "La date de fin est calculée",
  "Dans les propriétés d'une tâche, le champ « Date de fin » est grisé. Pourquoi ?",
  ["parce qu'elle est calculée à partir du début et de la durée",
   "parce que le logiciel est en version limitée",
   "parce qu'il faut enregistrer le fichier avant de la modifier",
   "parce qu'une tâche n'a pas de fin tant qu'elle n'est pas faite"],
  "Un planning ne doit pas pouvoir se contredire. Si l'on pouvait imposer le début, la durée et "
  "la fin, on pourrait écrire quelque chose de faux : le logiciel l'interdit en calculant la fin.",
  "Début en séance 5, durée 3 séances : la fin tombe en séance 7, et aucun autre choix n'est "
  "possible.",
  "Chercher à taper une date de fin, ne pas y arriver, et croire à un dysfonctionnement.",
  ["",
   "Le grisé n'a rien à voir avec la licence : GanttProject est un logiciel libre, complet et sans version bridée.",
   "L'enregistrement ne débloque rien : le champ restera calculé quel que soit l'état du fichier.",
   "Une tâche non commencée a bien une date de fin PRÉVUE : c'est justement l'objet du planning."],
  "Début + durée = fin. La fin ne se saisit pas, elle se calcule.",
  img=IMG_PROPS),

q("3e", "Élaborer, c'est d'abord découper",
  "Élaborer un processus de réalisation commence par :",
  ["identifier les tâches, c'est-à-dire découper le projet en choses qu'on peut déclarer finies",
   "ouvrir le logiciel et créer un fichier",
   "estimer la durée totale du projet",
   "répartir les élèves dans les groupes"],
  "Le découpage est le vrai travail intellectuel : c'est là qu'on décide de quoi le projet est "
  "fait. Tout le reste — durées, contraintes, calcul — s'appuie dessus.",
  "Un découpage trop grossier (« fabriquer l'objet ») rend le planning inutile : on ne saura "
  "jamais où on en est.",
  "Ouvrir le logiciel d'abord, et découvrir qu'on ne sait pas quoi y saisir.",
  ["",
   "Le logiciel ne peut rien faire tant qu'aucune tâche n'existe : il vient après, pas avant.",
   "La durée totale est un RÉSULTAT du calcul ; l'estimer d'avance revient à décider la réponse avant l'exercice.",
   "La répartition des élèves dépend de ce qui peut avancer en parallèle, donc du planning : elle vient après."],
  "Élaborer commence par découper en tâches déclarables finies."),

q("3e", "Ajouter des personnes",
  "Une tâche critique dure 3 séances. On y met deux fois plus d'élèves. Que peut-on affirmer ?",
  ["rien : certaines tâches se divisent, d'autres non",
   "elle durera 1,5 séance",
   "elle durera toujours 3 séances",
   "le chemin critique disparaîtra"],
  "Le planning dit où il vaudrait la peine d'essayer d'accélérer ; il ne dit pas si c'est "
  "possible. Câbler quatre capteurs se divise ; attendre la fin d'une impression 3D ne se divise pas.",
  "Imprimer un boîtier prend le temps que prend l'imprimante, quel que soit le nombre d'élèves "
  "autour.",
  "Croire qu'ajouter des personnes raccourcit mécaniquement une tâche.",
  ["",
   "La division par deux ne vaut que pour les tâches réellement divisibles, et encore : la coordination coûte du temps.",
   "Affirmer qu'elle durera toujours 3 séances est tout aussi faux : beaucoup de tâches se partagent très bien.",
   "Un chemin critique existe toujours : même raccourci, un projet garde une chaîne qui commande sa date de fin."],
  "Le planning dit OÙ essayer d'accélérer, pas si c'est possible."),

q("3e", "Recalculer après chaque changement",
  "On modifie la durée d'une tâche. Que faut-il faire du chemin critique établi la veille ?",
  ["le recalculer : il peut avoir changé",
   "le garder tel quel, il est établi une fois pour toutes",
   "l'effacer, il ne sert plus à rien",
   "le recopier dans le compte rendu"],
  "Le chemin critique n'est pas une propriété permanente du projet : c'est le résultat d'un calcul "
  "sur les durées et les contraintes du moment. Changer une durée peut le déplacer entièrement.",
  "C'est précisément le service que rend un logiciel : recalculer instantanément après chaque "
  "modification.",
  "Planifier une fois au début et suivre un chemin critique devenu faux depuis des semaines.",
  ["",
   "Le garder tel quel revient à travailler sur une information périmée, et à se dépêcher au mauvais endroit.",
   "L'effacer priverait le projet de la seule information qui dit où le retard coûte cher.",
   "Le recopier dans un dossier ne le met pas à jour : ce qu'il faut, c'est refaire le calcul."],
  "Le chemin critique se recalcule à chaque changement de durée."),

q("3e", "Ce que le programme demande vraiment",
  "Le programme de cycle 4 nomme trois choses à propos de ce diagramme. Lesquelles ?",
  ["les tâches, leur durée, et les contraintes entre tâches",
   "les tâches, les responsables, et le budget",
   "les durées, les coûts, et les risques",
   "les tâches, les jalons, et le chemin critique"],
  "Le texte est court et précis : « le diagramme de planification des tâches : notion de tâches, "
  "durée et contraintes entre tâches ». Tout le reste — marges, chemin le plus long, jalons — "
  "se déduit de ces trois notions.",
  "C'est pour cela que l'atelier commence par les trois mots, et seulement ensuite par le calcul.",
  "Ajouter au programme des notions de gestion de projet qui n'y figurent pas, et alourdir "
  "inutilement la séance.",
  ["",
   "Les responsables et le budget relèvent de la conduite de projet, pas de ce point du programme.",
   "Les coûts et les risques ne sont pas nommés ici : les confondre avec le programme égare l'élève.",
   "Les jalons et le chemin critique sont utiles, mais ils se DÉDUISENT des trois notions nommées ; ils ne les remplacent pas."],
  "Tâches, durée, contraintes entre tâches : les trois mots du programme."),
