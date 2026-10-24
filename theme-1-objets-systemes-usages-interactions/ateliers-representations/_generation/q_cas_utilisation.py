# -*- coding: utf-8 -*-
"""Les 30 questions du QCM de l'atelier « diagramme de cas d'utilisation » (use case SysML).

Toutes les bonnes réponses sont en position 0 ici : la répartition sur A/B/C/D
est faite ensuite par `_outils/fix_r.js`, de façon déterministe.

Répartition : 5e_C2.1 (8) · 4e_C2.1 (12) · 3e_C2.1 (10). Huit questions illustrées.
"""
from qbanque import Banque

B = Banque()
q = B.q

IMG_STATION = {"src": "Images/station_velos_cas_utilisation_corrige.svg",
               "alt": "Diagramme de cas d'utilisation de la station de vélos : dans le cadre, Louer un vélo, Rendre un vélo, "
                      "Payer la location, Réparer une borne ; à gauche l'usager et le technicien de maintenance ; à droite le "
                      "serveur de paiement, relié à Payer la location."}
IMG_LAMPADAIRE = {"src": "Images/lampadaire_cas_utilisation.svg",
                  "alt": "Diagramme de cas d'utilisation du lampadaire solaire du parking : un cadre et quatre ellipses (Voir son "
                         "chemin la nuit, Régler les heures d'allumage, Suivre la charge de la batterie, Remplacer la lampe) ; "
                         "le piéton à gauche ; l'agent de la mairie et le technicien à droite, tous deux reliés à Suivre la "
                         "charge de la batterie."}
IMG_BORNE = {"src": "Images/borne_velos_cas_utilisation_corrige.svg",
             "alt": "Diagramme de cas d'utilisation de la borne : Louer un vélo, Rendre un vélo, Payer la location, Signaler "
                    "une panne, Réparer la borne ; l'usager et le technicien à gauche, le serveur de paiement à droite ; "
                    "Signaler une panne est relié à l'usager et au technicien."}
IMG_ERREURS = {"src": "Images/arrosage_cas_utilisation_avec_erreurs.svg",
               "alt": "Diagramme du système d'arrosage dessiné par Noah : la gardienne est dessinée dans le cadre ; ellipses "
                      "Programmer l'heure d'arrosage, La pompe, L'arrosage, Consulter le niveau de la cuve ; à droite, la "
                      "pluie reliée à L'arrosage, et le technicien relié à rien."}
IMG_CYCLONE = {"src": "Images/station_alerte_cas_utilisation_corrige.svg",
               "alt": "Diagramme de cas d'utilisation de la station d'alerte cyclonique : l'agent municipal relié à Déclencher "
                      "une alerte, le technicien à Tester la sirène, l'habitant à Recevoir une alerte, le service météo à "
                      "Envoyer un bulletin météo."}

# ═══════════════ 5e_C2.1 — Faire la liste des interacteurs extérieurs d'un OST (8) ═══════════════
C = "5e_C2.1"

q(C, "Ce qu'est un acteur",
  "Dans un diagramme de cas d'utilisation, un acteur est…",
  ["une personne ou un autre système, dehors, qui s'en sert avec un but",
   "tout ce qui touche le système, y compris la pluie et le soleil",
   "une pièce du système que l'usager manipule, comme l'écran",
   "seulement une personne qui paie pour se servir du système"],
  "Trois conditions ensemble : être une <b>personne</b> ou un <b>autre système</b>, être <b>en dehors</b> du système, et "
  "s'en servir <b>avec un but</b> (demander quelque chose, ou répondre).",
  "Le technicien de maintenance est un acteur de la station : il est dehors et vient réparer les bornes.",
  "Prendre pour acteur tout ce qui touche le système.",
  ["",
   "La pluie et le soleil touchent la station, mais sans but : ce sont des interacteurs, pas des acteurs.",
   "L'écran est une pièce, dedans : un acteur est toujours en dehors du système.",
   "Le technicien ne paie rien et c'est un acteur ; le serveur de paiement n'est pas une personne et en est un aussi."],
  "Acteur = dehors + avec un but (personne ou autre système).")

q(C, "La pluie et la borne",
  "La pluie mouille la borne de la station de vélos. Est-ce un acteur du diagramme de cas d'utilisation ?",
  ["Non : elle agit sur la borne, mais sans but",
   "Oui : elle agit sur la borne, donc c'est un acteur",
   "Oui : tout élément de l'environnement est un acteur",
   "Non : elle ne touche jamais la borne de la station"],
  "La pluie ne veut rien obtenir de la station : elle tombe, c'est tout. Elle reste un <b>interacteur</b> (l'environnement), "
  "à sa place dans le diagramme pieuvre et dans les exigences.",
  "Le soleil qui recharge un lampadaire solaire n'est pas un acteur non plus.",
  "Confondre « agir sur le système » et « s'en servir avec un but ».",
  ["",
   "Agir sur la borne ne suffit pas : il faut s'en servir avec un but, et la pluie ne veut rien.",
   "Les éléments de l'environnement sont des interacteurs ; aucun n'est un acteur, faute de but.",
   "La pluie touche bien la borne : ce n'est pas la raison. La raison, c'est qu'elle n'a pas de but."],
  "La nature agit sans but : ce n'est pas un acteur.")

q(C, "Un acteur qui n'est pas une personne",
  "Sur ce diagramme, le serveur de paiement est un acteur. Pourquoi, alors que ce n'est pas une personne ?",
  ["Il est dehors et répond à la borne : il accepte ou refuse la carte.",
   "Il est rangé dans la borne, juste derrière l'écran tactile.",
   "Tout ce qui est électrique est un acteur du système.",
   "Il coûte plus cher que tous les autres éléments de la station."],
  "Un acteur peut être un <b>autre système</b> : le serveur de paiement est en dehors de la station, et il échange avec elle "
  "avec un but (accepter ou refuser le paiement).",
  "Le service météo qui envoie ses bulletins à la station d'alerte cyclonique est aussi un acteur.",
  "Croire qu'un acteur est forcément une personne.",
  ["",
   "Le serveur de paiement est à la banque, loin de la station : s'il était dans la borne, ce serait une pièce.",
   "L'écran tactile est électrique, et c'est une pièce, pas un acteur : l'électricité ne décide de rien.",
   "Le prix ne dit rien du rôle d'un élément : seuls comptent « dehors » et « avec un but »."],
  "Un autre système peut être un acteur.",
  img=IMG_STATION)

q(C, "Une pièce de la borne",
  "Parmi ces éléments de la station de vélos, lequel est une pièce, donc pas un acteur ?",
  ["l'écran tactile de la borne",
   "le technicien de maintenance",
   "l'usager qui loue un vélo",
   "le serveur de paiement"],
  "L'écran tactile fait partie de la borne : c'est un <b>constituant</b>, dedans. Un acteur est toujours en dehors du système.",
  "Le cadenas, la batterie d'un lampadaire, la pompe d'un système d'arrosage sont aussi des pièces.",
  "Prendre pour acteur ce que l'usager touche.",
  ["",
   "Le technicien est une personne, dehors, qui vient réparer : c'est un acteur.",
   "L'usager est une personne, dehors, qui veut un vélo : c'est l'acteur principal.",
   "Le serveur de paiement est un autre système, dehors, qui répond à la borne : c'est un acteur."],
  "Dedans : une pièce. Dehors, avec un but : un acteur.")

q(C, "Le grand cadre",
  "Sur ce diagramme, comment s'appelle le grand cadre qui porte en haut le nom du lampadaire ?",
  ["la frontière du système",
   "l'ellipse principale",
   "le cadre des acteurs",
   "l'association du système"],
  "Le cadre sépare ce qui fait partie du système (dedans) de tout le reste (dehors) : c'est la <b>frontière du système</b>. "
  "Les ellipses sont dedans, les acteurs dehors.",
  "Sur le diagramme de la station de vélos, le cadre porte le nom « Station de vélos en libre-service ».",
  "Confondre les quatre éléments du diagramme.",
  ["",
   "Les ellipses sont les cas d'utilisation, dans le cadre ; le cadre, lui, n'est pas une ellipse.",
   "Les acteurs sont dessinés hors du cadre, pas dedans : le cadre ne leur appartient pas.",
   "Une association est un trait entre un acteur et une ellipse, pas un cadre."],
  "Le cadre = la frontière du système.",
  img=IMG_LAMPADAIRE)

q(C, "Suivre les traits",
  "Sur ce diagramme, quels acteurs sont reliés à « Suivre la charge de la batterie » ?",
  ["l'agent de la mairie et le technicien",
   "le piéton et l'agent de la mairie",
   "le technicien et le soleil, qui recharge",
   "le piéton, l'agent et le technicien"],
  "Deux traits arrivent à cette ellipse : l'un part de l'agent de la mairie, l'autre du technicien. Une ellipse peut avoir "
  "<b>deux acteurs</b>.",
  "« Payer la location » est reliée à l'usager et au serveur de paiement.",
  "Lire le diagramme sans suivre les traits.",
  ["",
   "Le seul trait du piéton va à « Voir son chemin la nuit », pas à la batterie.",
   "Le soleil n'est pas dessiné : il recharge la batterie sans but, ce n'est pas un acteur.",
   "Le piéton n'est pas relié à cette ellipse : seuls deux traits y arrivent."],
  "Un trait dit qui participe à quelle action.",
  img=IMG_LAMPADAIRE)

q(C, "Acteurs et interacteurs",
  "Quelle phrase est juste ?",
  ["Tout acteur est un interacteur ; tout interacteur n'est pas un acteur.",
   "Tout interacteur est un acteur ; tout acteur n'est pas un interacteur.",
   "Un acteur et un interacteur sont deux noms pour la même chose.",
   "Un acteur est toujours dans le système, un interacteur toujours dehors."],
  "Les interacteurs sont tout ce qui entoure le système (personnes, objets, données, nature). Les acteurs n'en gardent qu'une "
  "partie : ceux qui s'en servent <b>avec un but</b>.",
  "La pluie et le vélo sont des interacteurs de la station, mais pas des acteurs ; l'usager est les deux.",
  "Mettre dans le diagramme de cas d'utilisation tous les interacteurs du diagramme pieuvre.",
  ["",
   "C'est l'inverse : la pluie est un interacteur, et ce n'est pas un acteur.",
   "Ce ne sont pas des synonymes : le vélo est un interacteur de la station, pas un acteur.",
   "Un acteur est toujours dehors, comme un interacteur : aucun des deux n'est dans le système."],
  "Acteurs ⊂ interacteurs : ceux qui ont un but.")

q(C, "Le nom anglais",
  "Le diagramme de cas d'utilisation est souvent appelé par son nom anglais. Lequel ?",
  ["use case",
   "flowchart",
   "storyboard",
   "mind map"],
  "En anglais, « cas d'utilisation » se dit <b>use case</b>. Ce diagramme vient du langage SysML (<i>Systems Modeling "
  "Language</i>, le langage de modélisation des systèmes).",
  "Dans un logiciel de modélisation, le menu « Use case diagram » ouvre ce diagramme.",
  "Confondre les noms anglais des représentations.",
  ["",
   "« Flowchart » désigne l'algorigramme, qui montre l'ordre des actions et les tests.",
   "Un storyboard est une suite d'images, comme une bande dessinée : ce n'est pas ce diagramme.",
   "« Mind map » désigne la carte mentale, qui organise des idées autour d'un mot central."],
  "Cas d'utilisation = use case.")

# ═══════════════ 4e_C2.1 — Du langage naturel aux schémas (12) ═══════════════
C = "4e_C2.1"

q(C, "Un verbatim",
  "Qu'appelle-t-on un verbatim ?",
  ["ce qu'une personne a dit, recopié mot pour mot",
   "le résumé, en une ligne, de ce qu'ont dit les usagers",
   "le nom du système, écrit en haut du cadre du diagramme",
   "une action écrite avec un verbe à l'infinitif"],
  "Un <b>verbatim</b> est une phrase d'usager recopiée telle quelle, sans la résumer : c'est du langage naturel, le point de "
  "départ pour aller vers le schéma.",
  "« Je ne trouve jamais où poser ma carte » : un verbatim d'usager de la borne.",
  "Résumer les phrases des usagers avant de les lire.",
  ["",
   "Un résumé n'est plus un verbatim : on y perd les mots de l'usager, donc une partie de son ressenti.",
   "Le nom du système, en haut du cadre, n'a rien à voir : un verbatim vient d'un usager.",
   "Une action avec un verbe à l'infinitif, c'est un cas d'utilisation : on l'obtient à partir du verbatim."],
  "Verbatim = mot pour mot.")

q(C, "De la phrase au cas",
  "« Je pose ma carte, j'attends le bip, et je pars avec le vélo. » Quel cas d'utilisation cette phrase décrit-elle ?",
  ["Louer un vélo",
   "Rendre un vélo",
   "Signaler une panne",
   "Payer la location"],
  "L'usager repart avec un vélo : l'action faite avec la borne est <b>Louer un vélo</b>. Le cas s'écrit verbe à l'infinitif + "
  "complément.",
  "« Le soir, je remets le vélo dans un emplacement libre » → Rendre un vélo.",
  "S'arrêter au premier geste (poser sa carte) au lieu de chercher l'action entière.",
  ["",
   "Rendre un vélo, c'est le remettre à sa place ; ici, l'usager part avec.",
   "Aucun problème n'est signalé dans la phrase : tout se passe bien.",
   "Poser sa carte sert ici à prendre le vélo ; la phrase ne parle ni de code ni de paiement."],
  "Chercher l'action faite avec le système.")

q(C, "Que devient le ressenti",
  "« Il y a trois logos sur la borne, je ne sais jamais où poser ma carte. » Que devient l'agacement de cet usager ?",
  ["Il se garde à côté du diagramme, pour une exigence",
   "Il devient une ellipse « Être agacé » dans le cadre",
   "Il devient un nouvel acteur : l'usager agacé",
   "Il est effacé : seul compte ce qui fonctionne"],
  "Le diagramme garde l'action (Louer un vélo). Le <b>ressenti</b> ne s'y dessine pas : on le garde à côté, et il deviendra "
  "une exigence (« le lecteur de carte se repère du premier coup »).",
  "Tom trouve l'écran illisible en plein soleil → exigence : « l'écran reste lisible en plein soleil ».",
  "Vouloir tout mettre dans le même schéma.",
  ["",
   "« Être agacé » n'est pas une action faite avec la borne : ce n'est pas un cas d'utilisation.",
   "Un acteur est un rôle (l'usager), pas une émotion : content ou agacé, c'est le même acteur.",
   "Le ressenti ne s'efface pas : c'est lui qui dit ce qu'il faut améliorer."],
  "Le ressenti se garde à côté, pour les exigences.")

q(C, "Une phrase sans action",
  "« Le bleu de la borne est joli, il va bien avec la mer. » Quel cas d'utilisation cette phrase donne-t-elle ?",
  ["aucun : la phrase ne décrit aucune action",
   "Admirer la borne, puisqu'on regarde sa couleur",
   "Consulter les vélos disponibles sur la borne",
   "Peindre la borne en bleu, une fois par an"],
  "La phrase donne un avis sur la couleur : l'usagère ne fait rien avec la borne. Elle ne donne <b>aucun</b> cas "
  "d'utilisation (elle peut servir plus tard pour une exigence de forme).",
  "« Ce boîtier vert est discret derrière les plantes » : aucun cas non plus.",
  "Créer un cas d'utilisation pour chaque phrase.",
  ["",
   "Regarder une couleur n'est pas un service que la borne rend : ce n'est pas une action faite avec elle.",
   "Consulter les vélos disponibles est un vrai cas, mais la phrase ne parle pas des vélos.",
   "Personne ne peint la borne dans cette phrase : ce serait inventer une action."],
  "Un avis n'est pas une action.")

q(C, "Un libellé bien écrit",
  "Quel libellé est un cas d'utilisation bien écrit ?",
  ["Payer la location",
   "Le paiement",
   "L'écran tactile",
   "La borne encaisse l'argent"],
  "Un cas d'utilisation s'écrit avec un <b>verbe à l'infinitif + un complément</b>, du point de vue de l'acteur : ce qu'il "
  "fait avec le système.",
  "« Rendre un vélo », « Signaler une panne », « Consulter les vélos disponibles ».",
  "Écrire un nom, une pièce, ou ce que fait le système à l'intérieur.",
  ["",
   "« Le paiement » n'a pas de verbe : on ne sait pas qui fait quoi.",
   "L'écran tactile est une pièce de la borne, pas une action.",
   "C'est une phrase conjuguée, qui dit ce que fait la borne à l'intérieur, pas ce que l'usager fait avec elle."],
  "Verbe à l'infinitif + complément.")

q(C, "L'écran, intrus",
  "Sur ce diagramme de la borne, pourquoi « l'écran tactile » n'a-t-il ni ellipse ni bonhomme ?",
  ["C'est une pièce de la borne : ni action, ni acteur",
   "Il est déjà dessiné sur la borne, à côté du cadenas",
   "Il ne sert qu'au technicien, jamais à l'usager",
   "Il faudrait le dessiner en bonhomme, hors du cadre"],
  "L'écran est un <b>constituant</b> : on s'en sert pour louer, payer ou consulter, mais c'est un moyen, pas une action ; et "
  "il est dedans, donc ce n'est pas un acteur.",
  "Le cadenas, le lecteur de carte, le bouton rouge : des pièces, absentes du diagramme.",
  "Écrire dans une ellipse ce que l'usager touche.",
  ["",
   "Le diagramme ne dessine pas les pièces de la borne : il n'y a ni écran ni cadenas sur le schéma.",
   "L'usager se sert de l'écran pour louer : la raison n'est pas l'utilisateur, c'est que c'est une pièce.",
   "Un bonhomme est un acteur, dehors, avec un but : l'écran est dedans et n'a pas de but."],
  "Une pièce n'est ni une ellipse ni un bonhomme.",
  img=IMG_BORNE)

q(C, "Une ellipse, deux acteurs",
  "Sur ce diagramme de la borne, quelle ellipse est reliée à l'usager ET au technicien ?",
  ["Signaler une panne",
   "Réparer la borne",
   "Payer la location",
   "Louer un vélo"],
  "Deux traits arrivent à « Signaler une panne » : l'usager prévient, le technicien est averti. Une ellipse peut avoir deux "
  "acteurs.",
  "« Payer la location » a aussi deux acteurs : l'usager et le serveur de paiement.",
  "Lire une ellipse sans compter les traits qui y arrivent.",
  ["",
   "« Réparer la borne » n'est reliée qu'au technicien.",
   "« Payer la location » est reliée à l'usager et au serveur de paiement, pas au technicien.",
   "« Louer un vélo » n'est reliée qu'à l'usager."],
  "Compter les traits qui arrivent à l'ellipse.",
  img=IMG_BORNE)

q(C, "Un acteur dans le cadre",
  "Sur le diagramme de Noah, qu'est-ce qui ne va pas pour la gardienne ?",
  ["Elle est dessinée dans le cadre : un acteur est dehors",
   "Elle a trois traits, alors qu'un acteur n'en a qu'un seul",
   "Elle devrait être à droite, avec les autres acteurs",
   "Une personne ne peut pas être un acteur du système"],
  "Un acteur est toujours <b>en dehors</b> du système : la gardienne doit être dessinée hors du cadre, à gauche ou à droite.",
  "Sur le diagramme de la station, l'usager et le technicien sont dessinés hors du cadre.",
  "Dessiner l'usager principal dans le système, parce qu'il s'en sert beaucoup.",
  ["",
   "Un acteur peut avoir plusieurs traits : la gardienne programme et consulte, c'est juste.",
   "Le côté ne compte pas : un acteur peut être à gauche ou à droite, du moment qu'il est dehors.",
   "Les personnes sont justement les acteurs les plus fréquents : la gardienne en est un."],
  "Un acteur est toujours hors du cadre.",
  img=IMG_ERREURS)

q(C, "Une ellipse sans verbe",
  "Sur le diagramme de Noah, pourquoi « L'arrosage » est-il une erreur ?",
  ["Il n'a pas de verbe : on ne sait pas qui fait quoi",
   "Il est trop long pour tenir dans une ellipse du schéma",
   "Un système d'arrosage n'arrose jamais lui-même",
   "L'arrosage est une pièce : c'est le tuyau d'eau"],
  "Un cas d'utilisation commence par un <b>verbe à l'infinitif</b> : « Arroser les plantes du potager », « Lancer un "
  "arrosage ».",
  "« Le paiement » → « Payer la location ».",
  "Écrire un nom au lieu d'une action.",
  ["",
   "La longueur ne compte pas : « L'arrosage » est même très court. Il lui manque un verbe.",
   "Le système arrose bien les plantes : le problème est la façon d'écrire le cas, pas ce qu'il fait.",
   "« L'arrosage » n'est pas une pièce, c'est une action écrite comme un nom : il faut un verbe."],
  "Pas de verbe, pas de cas d'utilisation.",
  img=IMG_ERREURS)

q(C, "Un acteur sans trait",
  "Dans un diagramme, un acteur n'est relié à aucune ellipse. Que faut-il faire ?",
  ["Le relier au cas auquel il participe, ou l'enlever",
   "Le laisser : un acteur sans trait est un spectateur",
   "Le dessiner dans le cadre, plus près des ellipses",
   "Le transformer en ellipse portant son nom"],
  "Un acteur sans trait ne fait rien avec le système : soit on a oublié son cas (le technicien → « Entretenir le système »), "
  "soit il n'a rien à faire dans le diagramme.",
  "Le technicien du diagramme de Noah : on le relie à « Entretenir le système ».",
  "Laisser des bonshommes isolés « pour décorer ».",
  ["",
   "Il n'y a pas de spectateur dans ce diagramme : chaque acteur fait quelque chose avec le système.",
   "Un acteur n'est jamais dans le cadre, relié ou non.",
   "Une ellipse contient une action, pas le nom d'une personne."],
  "Chaque acteur a au moins un trait.")

q(C, "Pomper l'eau",
  "Un élève propose l'ellipse « Pomper l'eau » pour le système d'arrosage de la gardienne. Est-ce un bon cas d'utilisation ?",
  ["Non : c'est ce que fait une pièce, pas la gardienne",
   "Oui : il commence bien par un verbe à l'infinitif",
   "Oui : la pompe est la pièce la plus importante",
   "Non : un cas d'utilisation n'a jamais de verbe"],
  "Le verbe ne suffit pas : un cas dit ce que l'<b>acteur</b> fait avec le système. « Pomper l'eau » est ce que fait la "
  "pompe à l'intérieur ; la gardienne, elle, veut « Arroser les plantes ».",
  "« Ouvrir le cadenas » est ce que fait la borne ; l'usager, lui, veut « Louer un vélo ».",
  "Donner un verbe à une pièce et croire que c'est un cas d'utilisation.",
  ["",
   "Le verbe à l'infinitif est nécessaire, mais il faut aussi que ce soit l'action de l'acteur, pas celle d'une pièce.",
   "Ce diagramme regarde le système du dehors : ses pièces n'y figurent pas, même les plus importantes.",
   "C'est le contraire : un cas d'utilisation commence toujours par un verbe."],
  "Un cas : l'action de l'acteur, pas celle d'une pièce.")

q(C, "La pluie en bonhomme",
  "Sur un diagramme de cas d'utilisation, on voit un bonhomme « la pluie ». Où la pluie devrait-elle être ?",
  ["Dans le diagramme pieuvre et dans les exigences",
   "Dans une ellipse « La pluie », dans le cadre",
   "Sous le même bonhomme, mais à gauche du cadre",
   "Nulle part : la pluie ne compte pas pour le concepteur"],
  "La pluie agit sans but : c'est un <b>interacteur</b> (l'environnement). Elle a sa bulle dans le diagramme pieuvre et elle "
  "donne une exigence : « résister à la pluie ».",
  "Le vent de la station d'alerte cyclonique : pas un acteur, mais une exigence « résister au vent ».",
  "Mettre la météo parmi les acteurs parce qu'elle agit sur le système.",
  ["",
   "« La pluie » n'a pas de verbe et n'est pas une action faite avec le système.",
   "Changer de côté ne change rien : la pluie n'a pas de but, ce n'est pas un acteur.",
   "Le concepteur doit en tenir compte, mais dans les exigences, pas comme acteur."],
  "La nature : dans la pieuvre et les exigences.")

# ═══════════════ 3e_C2.1 — Modes de représentation choisis (10) ═══════════════
C = "3e_C2.1"

q(C, "Qui fait quoi",
  "« Qui se sert de la borne, et pour faire quoi ? » Quel mode de représentation répond à cette question ?",
  ["le diagramme de cas d'utilisation",
   "un graphique des locations par jour",
   "l'algorigramme de la location",
   "le storyboard d'une location"],
  "« Qui » et « pour faire quoi » : c'est exactement ce que montre le <b>diagramme de cas d'utilisation</b> — des acteurs "
  "reliés à leurs actions.",
  "« Qui reçoit l'alerte, et qui la déclenche ? » → le diagramme de cas d'utilisation de la station d'alerte.",
  "Choisir le mode qu'on préfère au lieu de celui qui répond à la question.",
  ["",
   "Un graphique compte des locations, mais il ne dit pas qui fait quoi avec la borne.",
   "L'algorigramme montre l'ordre des actions et les tests, pas la liste des acteurs.",
   "Le storyboard suit un usager, étape par étape ; il ne montre pas le technicien ni la banque."],
  "Qui fait quoi → cas d'utilisation.")

q(C, "Combien",
  "« Combien d'usagers abandonnent, chaque jour de la semaine ? » Quel mode choisir ?",
  ["un graphique, une barre par jour",
   "le diagramme de cas d'utilisation",
   "l'algorigramme de la location",
   "le diagramme des interacteurs"],
  "« Combien », jour par jour : on compare des <b>quantités</b>. Un graphique en barres le montre d'un coup d'œil.",
  "Le nombre d'alertes déclenchées chaque mois de la saison cyclonique → un graphique.",
  "Répondre à une question de quantité avec un schéma qui n'a pas de nombres.",
  ["",
   "Le diagramme de cas d'utilisation ne contient aucun nombre : il dit qui fait quoi.",
   "L'algorigramme montre où l'usager peut abandonner, pas combien abandonnent.",
   "Le diagramme des interacteurs montre ce qui entoure la borne, pas des quantités."],
  "Combien → graphique.")

q(C, "Si la carte est refusée",
  "« Si la carte est refusée, la borne la redemande-t-elle ? » Quel mode montre cela ?",
  ["l'algorigramme, avec un test dans un losange",
   "le diagramme de cas d'utilisation, avec une ellipse",
   "un graphique du nombre de cartes refusées",
   "le diagramme des interacteurs de la borne"],
  "« Si… » : c'est un <b>test</b>, avec deux suites possibles. L'algorigramme le dessine dans un losange, avec une sortie "
  "« oui » et une sortie « non ».",
  "« Si le vent dépasse le seuil, la station prévient l'agent » → un algorigramme.",
  "Croire que le diagramme de cas d'utilisation montre ce qui se passe en cas d'échec.",
  ["",
   "Une ellipse dit une action (Payer la location), pas ce qui se passe si elle échoue.",
   "Un graphique peut compter les refus, mais pas dire ce que fait la borne après un refus.",
   "Le diagramme des interacteurs montre ce qui entoure la borne : il n'a ni ordre ni test."],
  "Si… alors… → algorigramme.")

q(C, "Pour un touriste",
  "Pour montrer à un touriste qui ne lit pas le français comment louer un vélo, quel mode choisir ?",
  ["un storyboard : des images, étape par étape",
   "un algorigramme, avec ses losanges et ses tests",
   "le diagramme de cas d'utilisation de la borne",
   "un tableau qui compare les bornes de la ville"],
  "Le <b>storyboard</b> se comprend sans lire : une suite d'images montre chaque geste, dans l'ordre.",
  "Un nouvel habitant qui doit savoir quoi faire quand il reçoit l'alerte cyclonique → un storyboard.",
  "Choisir le mode le plus complet au lieu de celui que le destinataire peut lire.",
  ["",
   "Un algorigramme est fait de mots et de formes à apprendre : illisible pour qui ne lit pas le français.",
   "Le diagramme de cas d'utilisation dit qui fait quoi, mais pas comment faire, geste après geste.",
   "Un tableau se lit lentement, avec des mots : le touriste ne le comprendrait pas."],
  "Pour qui ne lit pas → des images.")

q(C, "Ce que le diagramme ne montre pas",
  "Que ne montre PAS un diagramme de cas d'utilisation ?",
  ["l'ordre dans lequel l'usager fait ses actions",
   "les acteurs qui se servent du système",
   "les actions faites avec le système",
   "les liens entre les acteurs et les actions"],
  "Le diagramme de cas d'utilisation montre les acteurs, les actions et leurs liens, mais <b>pas l'ordre</b> : ses ellipses "
  "ne sont pas rangées dans le temps. Il ne montre pas non plus les quantités ni le ressenti.",
  "Pour l'ordre des gestes de location → l'algorigramme ou le storyboard.",
  "Lire les ellipses de haut en bas comme une suite d'étapes.",
  ["",
   "Les acteurs sont justement les bonshommes : le diagramme les montre.",
   "Les actions sont les ellipses : le diagramme les montre.",
   "Les liens sont les traits (les associations) : le diagramme les montre."],
  "Pas d'ordre dans un diagramme de cas d'utilisation.")

q(C, "Le service météo",
  "Sur ce diagramme, le service météo est un acteur. Pourquoi, alors que ce n'est pas une personne ?",
  ["C'est un autre système, dehors, qui envoie ses bulletins",
   "Il est installé sur le mât, à côté de l'anémomètre",
   "Tout ce qui parle de la météo est un acteur",
   "Il compte plus que l'habitant pour la station"],
  "Un acteur peut être un <b>autre système</b> : le service météo est en dehors de la station et il échange avec elle avec "
  "un but (envoyer ses bulletins).",
  "Le serveur de paiement d'une banque est un acteur de la station de vélos, pour la même raison.",
  "Croire qu'un acteur est forcément une personne.",
  ["",
   "Le service météo n'est pas sur le mât : s'il y était, ce serait une pièce de la station, pas un acteur.",
   "Le vent parle aussi de météo, et ce n'est pas un acteur : il agit sans but.",
   "L'importance ne compte pas : l'habitant et le service météo sont des acteurs tous les deux."],
  "Un autre système, dehors, avec un but : un acteur.",
  img=IMG_CYCLONE)

q(C, "Le vent et l'anémomètre",
  "Le vent fait tourner l'anémomètre de la station. Pourquoi n'a-t-il pas de bonhomme ?",
  ["Il agit sur la station sans but : c'est un interacteur",
   "Il est mesuré, donc il fait partie de la station",
   "On ne peut pas dessiner le vent dans un schéma",
   "Il est déjà dans l'ellipse « Recevoir une alerte »"],
  "Le vent ne veut rien obtenir de la station : c'est un <b>interacteur</b> (l'environnement). Il donne des exigences : "
  "résister au vent, le mesurer.",
  "La pluie sur la borne de vélos : un interacteur, pas un acteur.",
  "Dessiner en bonhomme ce que le système mesure.",
  ["",
   "Être mesuré ne fait pas entrer le vent dans la station : l'anémomètre est une pièce, le vent reste dehors.",
   "On le dessine très bien, dans le diagramme pieuvre : simplement, ce n'est pas un acteur.",
   "« Recevoir une alerte » est l'action de l'habitant ; le vent n'y figure pas."],
  "Être mesuré n'est pas se servir du système.")

q(C, "Une phrase, un acteur, un cas",
  "« Chaque matin, le technicien teste la sirène. » Que donne cette phrase dans le diagramme ?",
  ["un acteur, le technicien, et un cas « Tester la sirène »",
   "un acteur, la sirène, et un cas « Chaque matin »",
   "deux acteurs : le technicien et la sirène",
   "une ellipse « Le technicien » et un bonhomme « la sirène »"],
  "Celui qui agit avec un but → un <b>acteur</b> (le technicien). Ce qu'il fait avec la station → un <b>cas d'utilisation</b>, "
  "verbe à l'infinitif + complément (Tester la sirène).",
  "« L'agent municipal déclenche l'alerte » → l'agent municipal, et « Déclencher une alerte ».",
  "Prendre une pièce (la sirène) pour un acteur.",
  ["",
   "La sirène est une pièce de la station ; « Chaque matin » dit quand, pas quoi : ni l'un ni l'autre ne convient.",
   "La sirène est une pièce, dedans : ce n'est pas un acteur.",
   "C'est inversé : le technicien est un bonhomme, et la sirène n'est ni l'un ni l'autre."],
  "Qui agit → bonhomme ; ce qu'il fait → ellipse.")

q(C, "Un acteur de plus",
  "La station prévient aussi le centre de secours des pompiers, en même temps que les habitants. Que faut-il ajouter au diagramme ?",
  ["un acteur, relié à « Recevoir une alerte »",
   "une ellipse « Prévenir les pompiers », sans acteur",
   "rien : les pompiers sont des habitants comme les autres",
   "un bonhomme « la sirène », relié aux pompiers"],
  "Le centre de secours est un autre système, dehors, qui reçoit l'alerte : c'est un <b>acteur</b>, relié à l'ellipse "
  "existante. L'action ne change pas : « Recevoir une alerte » a maintenant deux acteurs.",
  "« Payer la location » est reliée à deux acteurs : l'usager et le serveur de paiement.",
  "Ajouter une ellipse chaque fois qu'on ajoute un acteur.",
  ["",
   "Une ellipse sans acteur ne sert à rien, et l'action « recevoir l'alerte » existe déjà.",
   "Le centre de secours n'est pas un habitant : c'est un autre système, qui a son propre trait.",
   "La sirène est une pièce de la station : elle n'a pas de bonhomme."],
  "Un acteur de plus ne veut pas dire une ellipse de plus.")

q(C, "Une bonne justification",
  "Quelle justification du choix d'un mode de représentation est la meilleure ?",
  ["« L'algorigramme montre le test : ce que fait la borne si la carte est refusée. »",
   "« J'ai choisi le graphique parce que c'est plus visuel et plus clair pour tout le monde. »",
   "« J'ai pris l'algorigramme parce que je sais bien le faire et qu'il fait sérieux. »",
   "« Le storyboard est le plus joli des modes, et ses couleurs attirent l'œil. »"],
  "Une bonne justification relie le mode à <b>la question</b> posée : ce que ce mode montre, et que les autres ne montrent pas.",
  "« Le graphique compare le nombre d'abandons jour par jour : c'est ce que demande la mairie. »",
  "Justifier par son goût ou par ce qu'on sait faire.",
  ["",
   "« Plus visuel », « plus clair » : cela vaudrait pour n'importe quelle question, donc cela ne justifie rien.",
   "Savoir faire un mode ne dit pas s'il répond à la question posée.",
   "La beauté ne répond à aucune question ; et une couleur seule ne se lit pas par tous."],
  "On justifie un mode par la question à laquelle il répond.")

Q = B.fin(30, {"5e_C2.1": 8, "4e_C2.1": 12, "3e_C2.1": 10})
