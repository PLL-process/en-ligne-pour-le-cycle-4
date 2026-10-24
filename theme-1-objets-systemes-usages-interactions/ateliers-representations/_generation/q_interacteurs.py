# -*- coding: utf-8 -*-
"""Les 30 questions du QCM de l'atelier « diagramme des interacteurs extérieurs » (diagramme pieuvre).

Toutes les bonnes réponses sont en position 0 ici : la répartition sur A/B/C/D
est faite ensuite par `_outils/fix_r.js`, de façon déterministe.

Répartition : 5e_C2.1 (10) · 5e_C2.2 (10) · 4e_C2.2 (10). Quatre questions illustrées.
"""
from qbanque import Banque

B = Banque()
q = B.q

IMG_SCENE = {"src": "Images/velo_cargo_la_scene.svg",
             "alt": "Dessin : Léa pédale sur un vélo-cargo dans une côte, sous la pluie ; deux enfants et des courses dans le bac ; "
                    "un téléphone au guidon affiche un trajet."}
IMG_A_COMPLETER = {"src": "Images/pieuvre_velo_cargo_a_completer.svg",
                   "alt": "Diagramme pieuvre du vélo-cargo : quatre bulles remplies (Léa, le téléphone, la pluie, l'itinéraire) et trois "
                          "bulles vides qui attendent un usager, un autre objet et un élément de l'environnement."}
IMG_CHOIX = {"src": "Images/velo_cargo_trois_choix.svg",
             "alt": "Le vélo-cargo avec trois repères : A sur le bac à rebords hauts, B sur la commande de vitesses du guidon, "
                    "C sur la chaîne près du pédalier."}
IMG_JARDIN = {"src": "Images/pieuvre_jardin_arrosage.svg",
              "alt": "Diagramme pieuvre du système d'arrosage : le trait 1 va de la gardienne aux plantes en passant par le système ; "
                     "les traits 2 à 6 relient le système à un seul interacteur chacun."}

# ═══════════════ 5e_C2.1 — Faire la liste des interacteurs extérieurs d'un OST (10) ═══════════════
C = "5e_C2.1"

q(C, "Ce qu'est un interacteur",
  "Un interacteur extérieur d'un objet, c'est…",
  ["ce qui est en dehors de l'objet et en relation avec lui",
   "une pièce de l'objet, qui bouge quand on l'utilise",
   "une personne qui utilise l'objet, et seulement une personne",
   "une action que l'on fait avec l'objet, comme rouler ou freiner"],
  "Deux conditions, ensemble : être <b>en dehors</b> de l'objet, et être <b>en relation</b> avec lui (le toucher, agir sur lui, "
  "ou subir son action). Ce peut être une personne, une chose, une information ou un élément de la nature.",
  "La pluie est en dehors du vélo-cargo et le mouille : c'est un interacteur, sans être une personne.",
  "Ne citer que des personnes, ou citer des pièces de l'objet.",
  ["",
   "Une pièce qui bouge, comme la pédale, est DANS l'objet : c'est un constituant, pas un interacteur.",
   "Les personnes ne sont qu'une famille sur quatre : la pluie, le téléphone ou l'itinéraire sont aussi des interacteurs.",
   "Rouler est un usage, une action : un interacteur est quelqu'un ou quelque chose."],
  "Interacteur = en dehors + en relation.")

q(C, "Les deux noms du schéma",
  "Le programme dit « diagramme des interacteurs extérieurs ». Sous quel autre nom ce schéma est-il très connu ?",
  ["le diagramme pieuvre",
   "la bête à cornes",
   "le diagramme de Gantt",
   "l'algorigramme"],
  "On l'appelle diagramme pieuvre parce que l'objet est au centre, comme la tête, et que les traits vers les interacteurs "
  "ressemblent à des tentacules. Les deux noms désignent le même schéma.",
  "Dans un manuel ou sur Internet, « diagramme pieuvre du vélo » et « diagramme des interacteurs du vélo » montrent le même dessin.",
  "Confondre les représentations entre elles parce qu'elles ont toutes un surnom.",
  ["",
   "La bête à cornes existe bien, mais elle exprime le besoin (à qui, sur quoi, dans quel but), pas la liste des interacteurs.",
   "Le diagramme de Gantt place des tâches dans le temps : il sert à organiser un projet.",
   "Un algorigramme montre l'ordre des opérations d'un programme, pas ce qui entoure un objet."],
  "Diagramme des interacteurs extérieurs = diagramme pieuvre.")

q(C, "Un objet ou une donnée",
  "Dans quelle famille range-t-on l'itinéraire affiché sur le téléphone de Léa ?",
  ["une donnée",
   "un autre objet",
   "un usager",
   "un élément de l'environnement"],
  "L'itinéraire est une information : on la lit sur l'écran, on ne peut pas la toucher. Les informations forment la famille "
  "des <b>données</b>.",
  "La vitesse affichée sur un compteur, la température lue sur un thermomètre : des données.",
  "Mettre le téléphone et ce qu'il affiche dans la même famille.",
  ["",
   "L'objet, c'est le téléphone, qu'on touche ; l'itinéraire, lui, s'affiche dessus et ne se touche pas.",
   "Un usager est une personne ; l'itinéraire n'en est pas une.",
   "L'environnement, c'est le lieu et la nature : la route, la pluie. L'itinéraire est une information produite par un appareil."],
  "Ce qu'on touche : un objet. Ce qu'on lit : une donnée.")

q(C, "Une pièce n'est pas un interacteur",
  "Parmi ces éléments, lequel est une pièce du vélo-cargo, et non un interacteur extérieur ?",
  ["la chaîne",
   "la pluie",
   "les courses",
   "la route en pente"],
  "La chaîne est un <b>constituant</b> : elle fait partie du vélo-cargo. Un interacteur est toujours en dehors de l'objet.",
  "Le guidon, la selle, les roues et le bac sont aussi des constituants.",
  "Donner une bulle à une pièce parce qu'on la voit bien sur le dessin.",
  ["",
   "La pluie tombe sur le vélo-cargo depuis l'extérieur : c'est un interacteur (environnement).",
   "Les courses sont transportées dans le bac, mais ne sont pas une pièce du vélo : c'est un interacteur (autre objet).",
   "Les roues roulent sur la route, qui reste en dehors du vélo : c'est un interacteur (environnement)."],
  "Dedans : un constituant. Dehors : un interacteur.")

q(C, "Les familles sur un dessin",
  "Sur ce dessin, combien de familles différentes d'interacteurs extérieurs peut-on trouver ?",
  ["quatre",
   "deux",
   "sept",
   "une seule"],
  "Usagers (Léa, les enfants), données (l'itinéraire), autres objets (le téléphone, les courses), éléments de l'environnement "
  "(la pluie, la route en pente) : les quatre familles du programme sont là.",
  "Sept interacteurs, mais seulement quatre familles : plusieurs interacteurs appartiennent à la même famille.",
  "Confondre le nombre d'interacteurs et le nombre de familles.",
  ["",
   "Deux familles, ce serait par exemple les personnes et les objets ; on oublierait la pluie, la route et l'itinéraire.",
   "Sept, c'est le nombre d'interacteurs, pas de familles : Léa et les enfants sont de la même famille.",
   "Une seule famille, ce serait une liste de personnes seulement : c'est justement la liste à moitié faite."],
  "Quatre familles : usagers, données, autres objets, environnement.",
  img=IMG_SCENE)

q(C, "La liste à moitié faite",
  "Une liste d'interacteurs contient seulement : Léa, les enfants, un piéton. Que lui manque-t-il ?",
  ["les données, les autres objets et l'environnement",
   "rien : les personnes sont les seuls vrais interacteurs",
   "les pièces du vélo-cargo, comme la chaîne et la selle",
   "les usages, comme « aller au marché » ou « rentrer »"],
  "Les trois éléments sont des usagers ou des personnes. Il manque les objets (téléphone, courses), les données (itinéraire) "
  "et l'environnement (pluie, route).",
  "Une liste complète se vérifie famille par famille : au moins un interacteur dans chacune, quand il y en a.",
  "S'arrêter aux personnes, parce que ce sont elles qu'on remarque en premier.",
  ["",
   "La pluie ou la route agissent sur le vélo-cargo autant que Léa : ils ont leur place dans la liste.",
   "Les pièces sont dans l'objet : les ajouter rendrait la liste fausse, pas complète.",
   "Un usage est une action, pas quelqu'un ou quelque chose : il n'a pas de bulle."],
  "Une liste de personnes seulement est une liste à moitié faite.")

q(C, "Compléter une bulle",
  "Quel mot met-on dans la bulle ③, qui attend un élément de l'environnement ?",
  ["la route en pente",
   "les courses",
   "la pédale du vélo-cargo",
   "les enfants"],
  "L'environnement, c'est le lieu et la nature. La route en pente est le sol sur lequel roule le vélo-cargo.",
  "Le sable d'une plage, le vent, le soleil seraient aussi des éléments de l'environnement.",
  "Prendre le premier mot de la banque sans vérifier la famille annoncée dans la bulle.",
  ["",
   "Les courses sont une chose que l'on touche : elles vont dans la bulle ②, « un autre objet ».",
   "La pédale est une pièce du vélo-cargo : elle n'a aucune bulle.",
   "Les enfants sont des personnes que le vélo-cargo transporte : ils vont dans la bulle ①, « un usager »."],
  "Bulle ③ : la route en pente.",
  img=IMG_A_COMPLETER)

q(C, "Fixé, mais pas une pièce",
  "Le téléphone est fixé au guidon. Pourquoi est-il quand même un interacteur extérieur du vélo-cargo ?",
  ["Parce qu'on l'enlève et le vélo roule toujours : ce n'est pas une pièce.",
   "Parce qu'il est électrique, et que tout ce qui est électrique est extérieur.",
   "Parce qu'il coûte plus cher que le guidon sur lequel il est fixé.",
   "Parce que tout ce qui est fixé à un vélo devient un interacteur."],
  "Être attaché à l'objet ne suffit pas à en faire une pièce. Le téléphone n'est pas nécessaire au vélo-cargo : c'est un "
  "autre objet, en relation avec lui.",
  "Un porte-bidon fait partie du vélo ; la gourde qu'on y glisse est un autre objet.",
  "Confondre « fixé à l'objet » et « pièce de l'objet ».",
  ["",
   "Une batterie de vélo électrique est électrique, et c'est pourtant une pièce du vélo : l'électricité ne décide de rien.",
   "Le prix ne dit rien de la place d'un élément, dedans ou dehors.",
   "Le guidon est fixé au vélo, et c'est une pièce : être fixé ne suffit pas."],
  "Pièce ou non : peut-on l'enlever sans que l'objet cesse d'être lui-même ?")

q(C, "Ce que relie un trait",
  "Dans un diagramme pieuvre, que relie chaque trait ?",
  ["l'objet, au centre, à un de ses interacteurs",
   "deux pièces de l'objet entre elles",
   "deux étapes de l'utilisation, dans l'ordre",
   "une fonction à la solution qui la réalise"],
  "Le diagramme pieuvre dit avec qui ou quoi l'objet est en relation : chaque trait part de l'objet et va vers un interacteur.",
  "Le trait entre le vélo-cargo et la pluie dit : la pluie agit sur le vélo-cargo.",
  "Croire que les traits montrent un ordre ou un fonctionnement interne.",
  ["",
   "Les pièces de l'objet n'apparaissent pas dans ce diagramme : il regarde l'objet du dehors.",
   "Un ordre d'étapes se montre avec un algorigramme ou un storyboard, pas avec une pieuvre.",
   "Relier une fonction à sa solution, c'est le rôle d'un autre schéma, le diagramme FAST."],
  "Un trait = une relation entre l'objet et un interacteur.")

q(C, "Une règle n'est pas un interacteur",
  "La ville impose que tous les vélos-cargos aient un éclairage. Cette règle est-elle un interacteur extérieur ?",
  ["Non : c'est une exigence imposée à ceux qui conçoivent le vélo.",
   "Oui : c'est un élément de l'environnement, comme la pluie et le vent.",
   "Oui : c'est un usager, puisque la ville est faite de personnes.",
   "Non : seulement parce qu'elle n'est pas dessinée sur l'image."],
  "Une règle, une norme, une loi ne touchent pas l'objet et n'échangent rien avec lui : elles s'imposent à ceux qui le "
  "conçoivent. Ce sont des <b>exigences</b>.",
  "« Les freins doivent arrêter le vélo en moins de 5 m » : c'est une exigence, pas un interacteur.",
  "Mettre les règles et les normes dans les bulles du diagramme.",
  ["",
   "La pluie touche le vélo-cargo ; une règle de la ville ne touche rien : elle s'impose au concepteur.",
   "La règle n'est pas une personne qui utilise le vélo : les habitants ne pédalent pas parce qu'une règle existe.",
   "Dessinée ou non, une règle reste une exigence : le dessin ne décide pas de la famille."],
  "Une règle ou une norme est une exigence, pas un interacteur.")

# ═══════════════ 5e_C2.2 — Repérer et expliquer les choix de conception (10) ═══════════════
C = "5e_C2.2"

q(C, "Pour qui, les rebords hauts",
  "Les rebords hauts du bac du vélo-cargo répondent surtout à quel interacteur ?",
  ["les enfants",
   "la pluie",
   "la route en pente",
   "l'itinéraire"],
  "Les enfants sont assis dans le bac : des rebords hauts les empêchent de tomber dans un virage ou un freinage.",
  "Une barrière de lit d'enfant a la même raison d'être : retenir celui qui est dedans.",
  "Chercher la réponse dans l'objet au lieu de chercher qui ou quoi le choix protège.",
  ["",
   "Contre la pluie, on ajoute une housse ou des garde-boue : les rebords ne protègent pas de l'eau qui tombe.",
   "Pour la pente, on ajoute des vitesses : la hauteur du bac ne change pas l'effort.",
   "L'itinéraire est une information sur un écran : il n'a aucun lien avec la hauteur du bac."],
  "Un choix de conception répond à un interacteur.")

q(C, "Le domaine des ceintures",
  "Dans quel domaine range-t-on les ceintures des enfants dans le bac ?",
  ["la sécurité",
   "l'ergonomie",
   "le développement durable",
   "l'esthétique"],
  "Une ceinture évite qu'un enfant soit éjecté ou blessé : c'est un choix pour la <b>sécurité</b>.",
  "La ceinture d'une voiture, le casque d'un cycliste : des choix de sécurité.",
  "Confondre le confort (ergonomie) et la protection contre une blessure (sécurité).",
  ["",
   "L'ergonomie rend l'objet confortable et facile ; une ceinture peut être confortable, mais elle est là d'abord pour éviter une blessure.",
   "Le développement durable cherche à préserver la planète ; une ceinture ne réduit ni les déchets ni l'énergie.",
   "L'esthétique concerne la beauté de l'objet ; une ceinture n'est pas là pour faire joli."],
  "Éviter une blessure : sécurité.")

q(C, "Le repère B",
  "Sur ce dessin, le détail B (une commande de huit vitesses) relève surtout de…",
  ["l'ergonomie : moins d'effort dans la montée",
   "la sécurité : ne pas tomber en descente",
   "le développement durable : moins de pièces",
   "aucun domaine : c'est seulement décoratif"],
  "Changer de vitesse permet de pédaler avec moins de force quand la route monte : le vélo-cargo est plus facile à utiliser. "
  "C'est l'<b>ergonomie</b>.",
  "Un ouvre-boîte à long manche, un sac à dos rembourré : des choix d'ergonomie.",
  "Ranger toute aide à l'utilisateur dans la sécurité.",
  ["",
   "En descente, c'est le frein qui empêche de tomber ; les vitesses servent surtout à diminuer l'effort en montée.",
   "Huit vitesses ajoutent des pièces au lieu d'en enlever : ce n'est pas l'argument du développement durable ici.",
   "Une commande de vitesses a un rôle précis dans l'effort : elle n'est pas décorative."],
  "Diminuer l'effort, rendre l'usage facile : ergonomie.",
  img=IMG_CHOIX)

q(C, "Ce que veut dire ergonomie",
  "Rendre un objet ergonomique, c'est…",
  ["le rendre confortable et facile à utiliser",
   "le rendre moins cher à fabriquer",
   "le rendre moins nuisible pour la planète",
   "le rendre plus beau à regarder"],
  "L'ergonomie adapte l'objet à la personne qui s'en sert : moins d'effort, moins de fatigue, des gestes simples.",
  "Une poignée de forme ronde qui tient bien dans la main est un choix d'ergonomie.",
  "Confondre ergonomie et esthétique.",
  ["",
   "Le prix de fabrication est une question de coût, pas de confort d'utilisation.",
   "Préserver la planète relève du développement durable.",
   "La beauté d'un objet relève de l'esthétique ; un bel objet peut être pénible à utiliser."],
  "Ergonomie = confort et facilité d'usage.")

q(C, "Faire durer",
  "Des pièces traitées contre la rouille font durer le vélo-cargo plus longtemps sous la pluie. Quel domaine ?",
  ["le développement durable",
   "l'ergonomie et le confort",
   "la sécurité des personnes",
   "l'esthétique de l'objet"],
  "Un vélo qui dure plus longtemps, c'est moins de pièces à fabriquer, à transporter et à jeter : c'est un objectif de "
  "<b>développement durable</b>.",
  "Pouvoir remplacer une seule pièce au lieu de jeter tout l'objet : développement durable aussi.",
  "Croire que le développement durable ne concerne que l'énergie.",
  ["",
   "La rouille ne rend pas l'usage plus pénible tout de suite : elle use l'objet avec le temps.",
   "Une chaîne rouillée peut casser, c'est vrai, mais le but premier ici est de faire durer l'objet.",
   "Le traitement contre la rouille ne se voit presque pas : il n'est pas là pour rendre l'objet plus beau."],
  "Faire durer l'objet : développement durable.")

q(C, "La bonne question",
  "Pour expliquer un choix de conception, quelle question est la plus utile ?",
  ["« Pour qui ou contre quoi cette forme est-elle là ? »",
   "« Combien coûte cette pièce dans le magasin ? »",
   "« De quelle couleur cette pièce est-elle peinte ? »",
   "« Dans quelle usine l'objet a-t-il été fabriqué ? »"],
  "Un choix de conception répond presque toujours à un interacteur : le chercher, c'est trouver la raison du choix.",
  "« Pourquoi le bac a-t-il des rebords hauts ? → pour les enfants, qui pourraient tomber. »",
  "Décrire le détail sans chercher sa raison.",
  ["",
   "Le prix renseigne sur le coût, pas sur la raison de la forme.",
   "La couleur est rarement la raison d'une forme ; elle peut compter pour être vu, mais ce n'est pas la question de départ.",
   "Le lieu de fabrication ne dit rien de la raison d'un choix de forme."],
  "Pour qui, contre quoi ?")

q(C, "Expliquer, pas décrire",
  "Laquelle de ces phrases EXPLIQUE un choix de conception ?",
  ["« Le bac a des rebords hauts pour retenir les enfants. »",
   "« Le bac a des rebords hauts, et il est peint en vert. »",
   "« Le bac du vélo-cargo est placé devant le guidon. »",
   "« Le bac mesure environ un mètre de long. »"],
  "Expliquer, c'est donner la raison : « pour… », « parce que… ». Les autres phrases décrivent, sans dire pourquoi.",
  "« La poignée est ronde pour tenir dans la main » explique ; « la poignée est ronde » décrit.",
  "S'arrêter à la description.",
  ["",
   "Ajouter un deuxième détail (la couleur) décrit davantage, mais n'explique toujours rien.",
   "Dire où est le bac le décrit ; on ne sait pas pourquoi il est là.",
   "Une mesure est une description précise, pas une raison."],
  "Expliquer : « pour… », « parce que… ».")

q(C, "Changer de lieu",
  "Léa roule sur la route du bord de mer. Quel nouvel interacteur pourrait expliquer des pièces traitées contre la rouille ?",
  ["l'air salé de la mer",
   "l'itinéraire du téléphone",
   "les enfants dans le bac",
   "la selle du vélo-cargo"],
  "Le sel de la mer fait rouiller le métal très vite : c'est un élément de l'environnement qui explique le traitement contre la rouille.",
  "Les bancs du bord de mer sont souvent en matériaux qui ne rouillent pas, pour la même raison.",
  "Oublier qu'un changement de lieu apporte de nouveaux interacteurs.",
  ["",
   "L'itinéraire est une donnée affichée : il n'abîme pas le métal.",
   "Les enfants ne font pas rouiller les pièces ; ils expliquent plutôt les rebords et les ceintures.",
   "La selle est une pièce du vélo-cargo : ce n'est pas un interacteur."],
  "Changer de lieu, c'est changer d'interacteurs.")

q(C, "Le garde-boue",
  "Un garde-boue évite que Léa soit éclaboussée. Quel interacteur sert-il, et dans quel domaine ?",
  ["l'eau de la route — l'ergonomie, le confort",
   "les courses — la sécurité des enfants",
   "le téléphone — le développement durable",
   "aucun interacteur — il est décoratif"],
  "Le garde-boue arrête l'eau projetée par la roue : Léa reste sèche. C'est une question de confort, donc d'<b>ergonomie</b>.",
  "Un parapluie sert aussi le confort de la personne qui le tient.",
  "Ranger en sécurité tout ce qui protège.",
  ["",
   "Le garde-boue n'est pas près des courses, et une éclaboussure ne blesse personne.",
   "Le téléphone n'est pas concerné par l'eau projetée par la roue arrière, et le garde-boue ne fait pas durer l'objet.",
   "Un garde-boue a une fonction précise : arrêter les projections d'eau."],
  "Protéger du désagrément : ergonomie ; d'une blessure : sécurité.")

q(C, "Deux interacteurs à la fois",
  "Un même choix de conception peut-il répondre à deux interacteurs ?",
  ["Oui : le bac à rebords retient à la fois les enfants et les courses.",
   "Non : chaque choix de conception sert un seul interacteur.",
   "Non : seuls les usagers peuvent expliquer un choix de conception.",
   "Oui, mais seulement si les deux sont de la même famille."],
  "Un choix peut servir plusieurs interacteurs, de familles différentes : le bac retient les enfants (usagers) et les courses (autres objets).",
  "Un toit de station de vélos protège les usagers de la pluie et les vélos du soleil.",
  "Croire qu'à chaque forme correspond un seul interacteur.",
  ["",
   "Dans ce cas, le bac sert bien deux interacteurs : les enfants et les courses.",
   "Les courses ne sont pas des usagers, et elles expliquent aussi la forme du bac.",
   "Les enfants (usagers) et les courses (autres objets) sont de familles différentes, et le même bac les sert."],
  "Un choix peut répondre à plusieurs interacteurs.")

# ═══════════════ 4e_C2.2 — Repérer et expliquer les contraintes, exigences (10) ═══════════════
C = "4e_C2.2"

q(C, "Le trait qui passe par l'objet",
  "Sur ce diagramme, le trait 1 va de la gardienne aux plantes en passant par le système. C'est…",
  ["une fonction principale : le service rendu",
   "une fonction contrainte : une condition",
   "une solution technique : un composant",
   "une erreur de dessin à corriger"],
  "Un trait qui relie <b>deux</b> interacteurs en passant par l'objet montre ce que l'objet fait pour eux : c'est la "
  "fonction principale (FP).",
  "« Permettre à la gardienne d'arroser les plantes sans être là » : la FP du système d'arrosage.",
  "Prendre toute courbe pour une contrainte.",
  ["",
   "Une fonction contrainte ne touche qu'un seul interacteur ; le trait 1 en touche deux.",
   "Le diagramme pieuvre ne montre pas de composants : il regarde l'objet du dehors.",
   "La courbe qui passe par l'objet est la forme normale d'une fonction principale."],
  "Deux interacteurs reliés par l'objet : FP.",
  img=IMG_JARDIN)

q(C, "Ce que relie une FC",
  "Une fonction contrainte (FC) relie l'objet…",
  ["à un seul interacteur, dont il doit tenir compte",
   "à deux interacteurs, en passant par lui-même",
   "à ses propres pièces, à l'intérieur de l'objet",
   "à la solution technique qu'on choisira ensuite"],
  "Une FC dit une condition que l'objet doit respecter pour s'adapter à <b>un</b> interacteur : résister à la pluie, ne pas "
  "gaspiller l'eau de la cuve…",
  "FC : « le système doit résister à la pluie et au soleil ».",
  "Confondre la FC avec le service rendu.",
  ["",
   "Relier deux interacteurs en passant par l'objet, c'est la fonction principale.",
   "Les pièces sont dans l'objet : le diagramme pieuvre ne les montre pas.",
   "Les solutions techniques viennent plus tard, avec d'autres schémas comme le FAST."],
  "FC : l'objet et un interacteur.")

q(C, "Une exigence vérifiable",
  "Laquelle de ces phrases est une exigence que l'on peut vérifier ?",
  ["« Le boîtier doit résister aux projections d'eau : IPX4 au moins. »",
   "« Le boîtier doit être solide, très bien fait et durer longtemps. »",
   "« Le boîtier doit plaire beaucoup à la gardienne et au jardinier. »",
   "« Le boîtier doit être de la meilleure qualité possible sur le marché. »"],
  "Une exigence vérifiable a un <b>critère</b> (la résistance à l'eau, mesurée par l'indice IP) et un <b>niveau</b> (IPX4 "
  "au moins) : on peut tester et dire « réussi » ou « raté ».",
  "« Au plus 10 L d'eau par jour » : critère, le volume ; niveau, 10 L.",
  "Écrire des mots qui ne se mesurent pas : solide, bien, beau.",
  ["",
   "« Solide », « bien fait », « longtemps » ne disent ni ce qu'on mesure ni la valeur à atteindre.",
   "Plaire est un avis, qui change d'une personne à l'autre : aucun test ne peut le trancher.",
   "« La meilleure qualité » ne fixe aucun niveau : meilleure que quoi, mesurée comment ?"],
  "Exigence vérifiable = critère + niveau.")

q(C, "Critère et niveau",
  "Dans « le volume d'eau utilisé par jour : au plus 10 L », que sont les deux parties ?",
  ["le critère, puis le niveau",
   "le niveau, puis le critère",
   "deux contraintes différentes",
   "deux interacteurs du système"],
  "Le <b>critère</b> dit ce qu'on mesure (le volume d'eau par jour) ; le <b>niveau</b> dit la valeur à atteindre (au plus 10 L).",
  "« Le niveau sonore : au plus 35 dB » : critère, le niveau sonore ; niveau, 35 dB.",
  "Inverser les deux mots parce que « niveau » sonne comme une mesure.",
  ["",
   "Le niveau est la valeur (10 L) ; ce qui vient en premier est ce qu'on mesure, le critère.",
   "C'est une seule contrainte (ne pas gaspiller), précisée par son critère et son niveau.",
   "Un volume d'eau et une valeur ne sont ni des personnes ni des choses autour de l'objet."],
  "Critère : ce qu'on mesure. Niveau : la valeur à atteindre.")

q(C, "D'où vient IPX4",
  "Le code IPX4 veut dire la même chose chez tous les fabricants parce qu'il vient…",
  ["d'une norme",
   "d'un label",
   "d'un cahier des charges",
   "d'une publicité"],
  "Une <b>norme</b> est un texte officiel qui fixe les mêmes règles pour tous ; les codes IP de résistance à l'eau et à la "
  "poussière sont fixés par une norme internationale.",
  "Les tailles des prises électriques sont aussi fixées par des normes.",
  "Confondre norme et label.",
  ["",
   "Un label garantit une qualité (économiser l'eau, l'énergie) ; il ne définit pas les codes de résistance à l'eau.",
   "Un cahier des charges peut DEMANDER IPX4, mais il ne définit pas ce que veut dire IPX4 : c'est la norme qui le fait.",
   "Une publicité n'a pas le pouvoir de fixer une règle commune à tous les fabricants."],
  "Le code IP vient d'une norme.")

q(C, "Très basse tension",
  "« Le boîtier fonctionne en très basse tension (12 V). » Dans quelle catégorie range-t-on cette exigence ?",
  ["la sécurité",
   "l'ergonomie",
   "les incidences environnementales",
   "la fiabilité"],
  "Une très basse tension n'est pas dangereuse au toucher, même sous la pluie ; le 230 V de la maison, lui, peut tuer. C'est "
  "une exigence de <b>sécurité</b>.",
  "Les jouets électriques fonctionnent tous en très basse tension, pour la même raison.",
  "Ranger les exigences électriques dans la fiabilité.",
  ["",
   "La tension ne rend pas l'objet plus facile à utiliser : elle le rend moins dangereux.",
   "La tension ne dit rien de l'eau ou de l'énergie gaspillées.",
   "La fiabilité concerne les pannes ; ici, c'est un danger pour les personnes qui est évité."],
  "Éviter qu'une personne soit blessée : sécurité.")

q(C, "La panne après l'orage",
  "« Après chaque orage, le boîtier tombe en panne. » Quelle catégorie de contrainte a été oubliée ?",
  ["la fiabilité",
   "l'ergonomie",
   "les formes et fonctions",
   "la qualité"],
  "Un objet qui cesse de fonctionner avec le temps ou sous la pluie manque de <b>fiabilité</b> : la contrainte « résister à la "
  "pluie » n'a pas été écrite.",
  "Un vélo dont la chaîne casse après deux semaines manque de fiabilité.",
  "Dire « qualité » pour tout ce qui ne va pas.",
  ["",
   "L'ergonomie parle de facilité d'usage ; la panne n'est pas une gêne d'utilisation, c'est un arrêt.",
   "Les formes et fonctions concernent ce que l'objet doit faire et sa forme ; ici il le faisait, jusqu'à l'orage.",
   "La qualité est un mot large ; la catégorie précise d'une panne qui arrive avec le temps ou la météo est la fiabilité."],
  "Tenir sans panne, longtemps : fiabilité.")

q(C, "Pourquoi commencer par la pieuvre",
  "Pourquoi tracer toutes les bulles du diagramme pieuvre AVANT d'écrire les exigences ?",
  ["pour ne pas oublier un interacteur, donc une contrainte",
   "pour que le cahier des charges ait une jolie image",
   "parce que le programme interdit d'écrire d'abord",
   "pour connaître le prix de vente de l'objet"],
  "Chaque interacteur pose la question « quelle contrainte m'impose-t-il ? ». Un interacteur oublié, c'est une contrainte que "
  "personne n'écrira — et une plainte plus tard.",
  "Oublier la pluie dans le diagramme, c'est oublier d'écrire « résister à la pluie ».",
  "Écrire les exigences de mémoire, sans faire le tour des interacteurs.",
  ["",
   "Le diagramme n'est pas une décoration : il sert à ne rien oublier.",
   "Rien n'interdit d'écrire avant de dessiner ; dessiner d'abord aide simplement à ne rien oublier.",
   "Le diagramme pieuvre ne contient aucun prix."],
  "Le diagramme pieuvre sert à ne rien oublier.")

q(C, "Le critère du réglage",
  "« Le système doit se régler sans outil. » Quel critère permet de le vérifier ?",
  ["le nombre d'outils nécessaires, avec le niveau 0",
   "la couleur du bouton qui sert au réglage",
   "le volume d'eau contenu dans la cuve pleine",
   "l'avis du vendeur qui a installé le système d'arrosage"],
  "Pour vérifier « sans outil », on compte les outils nécessaires au réglage : le niveau à atteindre est zéro.",
  "« Changer l'heure en moins d'une minute » : critère, le temps ; niveau, 1 min.",
  "Choisir un critère qui ne se rapporte pas à la contrainte.",
  ["",
   "La couleur peut aider à trouver le bouton, mais elle ne dit pas si un outil est nécessaire.",
   "Le volume de la cuve concerne l'eau disponible, pas le réglage.",
   "L'avis d'une personne ne se mesure pas : ce n'est pas un critère."],
  "Un critère se mesure ou se compte.")

q(C, "Dans la FP et dans une FC",
  "La gardienne apparaît dans la fonction principale et dans une fonction contrainte. Est-ce une erreur ?",
  ["Non : l'objet la sert, et elle lui impose aussi une condition.",
   "Oui : un interacteur ne peut avoir qu'un seul trait.",
   "Oui : une personne ne peut jamais être dans une FC.",
   "Non : mais seulement parce qu'elle est la plus importante."],
  "Le système rend service à la gardienne (FP) et doit aussi s'adapter à elle : se régler sans outil (FC). Un même interacteur "
  "peut avoir plusieurs traits.",
  "Léa est servie par le vélo-cargo, et la selle doit aussi être réglable pour elle.",
  "Croire qu'un interacteur n'a qu'un trait.",
  ["",
   "Dans ce diagramme, la gardienne a bien deux traits, et c'est juste : elle est servie et elle impose une condition.",
   "Une FC peut concerner une personne : « se régler sans outil » concerne la gardienne.",
   "L'importance n'est pas la raison : c'est parce qu'elle a deux relations différentes avec l'objet."],
  "Un interacteur peut avoir plusieurs traits.")

Q = B.fin(30, {"5e_C2.1": 10, "5e_C2.2": 10, "4e_C2.2": 10})
