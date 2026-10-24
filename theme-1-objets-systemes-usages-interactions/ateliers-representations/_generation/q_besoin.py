# -*- coding: utf-8 -*-
"""Les 30 questions du QCM de l'atelier « Le besoin » (bête à cornes).

Toutes les bonnes réponses sont en position 0 ici : la répartition sur A/B/C/D
est faite ensuite par `_outils/fix_r.js`, de façon déterministe.

Répartition : 5e_C3.3 (10) · 4e_C1.3 (5) · 4e_C3.1 (5) · 3e_C3.1 (10). Six questions illustrées.
"""
from qbanque import Banque

B = Banque()
q = B.q

IMG_VELO = {"src": "Images/bete_a_cornes_velo_cargo.svg",
            "alt": "Bête à cornes du vélo-cargo : à qui le produit rend-il service ? Léa. Sur quoi agit-il ? ses deux enfants "
                   "et ses courses. Dans quel but ? transporter ses deux enfants et ses courses en ville."}
IMG_LAMPE = {"src": "Images/bete_a_cornes_lampadaire_a_completer.svg",
             "alt": "Bête à cornes du lampadaire intelligent, à compléter : les cases « À qui le produit rend-il service ? », "
                    "« Sur quoi le produit agit-il ? » et « Dans quel but ? » sont vides."}
IMG_BESOIN = {"src": "Images/bete_a_cornes_besoin_de_lea.svg",
              "alt": "Bête à cornes du besoin de Léa : à qui ? Léa. Sur quoi ? ses deux enfants et ses courses. Au centre : quel "
                     "objet ? Dans quel but ? transporter ses deux enfants et ses courses en ville, sans voiture."}
IMG_ARROSAGE = {"src": "Images/bete_a_cornes_arrosage_connecte.svg",
                "alt": "Bête à cornes du système d'arrosage connecté : à qui ? la gardienne du jardin. Sur quoi ? les plantes du "
                       "jardin. Dans quel but ? arroser les plantes du jardin, même en l'absence de la gardienne, sans gaspiller l'eau."}
IMG_ALERTE = {"src": "Images/bete_a_cornes_alerte_cyclonique.svg",
              "alt": "Bête à cornes du projet d'alerte : à qui ? les habitants du quartier. Sur quoi ? les habitants du quartier. "
                     "Au centre : quel objet ? Dans quel but ? prévenir les habitants du quartier de l'arrivée d'un cyclone."}
IMG_MAL = {"src": "Images/bete_a_cornes_alerte_mal_formulee.svg",
           "alt": "Bête à cornes d'une autre équipe : à qui ? les habitants du quartier. Sur quoi ? la sécurité du quartier. "
                  "Au centre : quel objet ? Dans quel but ? envoyer un SMS aux habitants."}

# ═══════════════ 5e_C3.3 — Choisir un OST parmi plusieurs propositions en vue de répondre à un besoin (10) ═══════════════
C = "5e_C3.3"

q(C, "Les trois questions",
  "La bête à cornes exprime le besoin avec trois questions. Lesquelles ?",
  ["À qui ? Sur quoi ? Dans quel but ?",
   "Quoi ? Où ? Quand ? Pendant combien de temps ?",
   "Avec quelles pièces ? Comment ? Combien ?",
   "Pour qui ? Contre quoi ? Avec quel moteur ?"],
  "Les trois questions du besoin : <b>à qui</b> le produit rend-il service ? <b>sur quoi</b> agit-il ? <b>dans quel but</b> "
  "existe-t-il ? Elles disent à quoi sert l'objet, sans parler de ses pièces.",
  "Le vélo-cargo : à qui ? Léa ; sur quoi ? ses enfants et ses courses ; dans quel but ? les transporter en ville.",
  "Mélanger les questions du besoin avec celles de la fabrication (les pièces, le prix).",
  ["",
   "Le lieu et la durée peuvent préciser un usage, mais la bête à cornes ne les demande pas : elle demande à qui, sur quoi, dans quel but.",
   "Les pièces et le « comment » sont des solutions : la bête à cornes les laisse de côté, elle exprime le besoin.",
   "Le moteur est une solution ; et « contre quoi » n'est pas une de ses cases : ce que l'objet doit respecter vient avec le diagramme des interacteurs."],
  "À qui ? Sur quoi ? Dans quel but ?")

q(C, "Léa ou ses enfants",
  "Sur cette bête à cornes, pourquoi Léa est-elle dans la case « à qui ? », et pas ses enfants ?",
  ["Parce que c'est elle qui se sert du vélo-cargo ; les enfants, il les transporte.",
   "Parce que les enfants sont trop jeunes pour avoir le droit d'être dans une case.",
   "Parce que Léa est la seule personne de la famille à avoir payé le vélo-cargo.",
   "Parce qu'une bête à cornes ne peut jamais montrer plus d'une seule personne."],
  "La case « à qui ? » nomme la personne que l'objet aide, celle qui s'en sert. Les enfants changent de place grâce au "
  "vélo-cargo : ils sont dans la case « sur quoi ? ».",
  "Pour une poussette : à qui ? le parent qui la pousse ; sur quoi ? le bébé.",
  "Mettre dans « à qui ? » tout ce que l'objet transporte.",
  ["",
   "L'âge ne décide de rien : les enfants sont bien dans le schéma, dans la case « sur quoi ? ».",
   "Payer ne décide pas de la case : celui qui paie n'est pas toujours celui à qui l'objet rend service.",
   "Les cases du haut peuvent nommer plusieurs personnes ; ici, les enfants sont dans la case « sur quoi ? »."],
  "À qui ? → la personne que l'objet aide.",
  img=IMG_VELO)

q(C, "Un but bien écrit",
  "Lequel de ces buts est bien écrit pour un lampadaire de parking ?",
  ["Éclairer le parking la nuit pour les piétons",
   "Allumer une ampoule quand un capteur voit quelqu'un",
   "Le lampadaire intelligent du parking de la plage",
   "Une lumière forte et blanche, au bout d'un mât"],
  "Un but commence par un <b>verbe à l'infinitif</b> et ne nomme <b>aucune solution</b> : il dit pourquoi l'objet existe, "
  "pas comment il est fait.",
  "Pour un arrosoir : « arroser les plantes du jardin ».",
  "Écrire comment l'objet marche au lieu de dire pourquoi il existe.",
  ["",
   "L'ampoule et le capteur sont des solutions : ils disent comment le lampadaire marche, pas pourquoi il existe.",
   "C'est le nom de l'objet, déjà écrit au centre du schéma : un but commence par un verbe.",
   "C'est une description de l'objet, sans verbe : on ne sait pas à quoi il sert."],
  "But = verbe à l'infinitif, sans solution.")

q(C, "Celui qui paie",
  "La mairie a commandé et payé le lampadaire du parking. Dans sa bête à cornes, à qui rend-il service ?",
  ["aux piétons qui traversent le parking la nuit",
   "à la mairie, puisque c'est elle qui l'a commandé",
   "à l'entreprise qui a fabriqué le lampadaire",
   "à l'ampoule, qui s'allume quand il fait nuit"],
  "La case « à qui ? » nomme la personne que l'objet aide quand il fonctionne. La mairie décide et paie, mais ce sont les "
  "piétons qui profitent de la lumière.",
  "Un parent qui offre un vélo à son enfant le paie ; c'est pourtant à l'enfant que le vélo rend service.",
  "Confondre celui qui commande l'objet et celui qui s'en sert.",
  ["",
   "La mairie commande et paie, mais elle ne marche pas sur le parking la nuit : celui qui paie n'est pas celui que l'objet aide.",
   "Le fabricant vend le lampadaire ; une fois installé, il n'en profite pas.",
   "L'ampoule est une pièce du lampadaire, une solution : elle n'a aucune case dans la bête à cornes."],
  "Celui qui paie n'est pas toujours celui à qui l'objet rend service.")

q(C, "La case « sur quoi ? » du lampadaire",
  "Sur cette bête à cornes à compléter, quel mot va dans la case « Sur quoi le produit agit-il ? » ?",
  ["la rue du parking",
   "la nuit, quand il fait noir",
   "l'ampoule du lampadaire",
   "la mairie de Sainte-Luce"],
  "La case « sur quoi ? » nomme ce que l'objet touche ou change : la lumière du lampadaire éclaire la rue du parking.",
  "Pour un arrosoir : sur quoi agit-il ? sur les plantes, qu'il mouille.",
  "Choisir la nuit, parce que le lampadaire « agit contre elle ».",
  ["",
   "La nuit est le moment où le lampadaire travaille ; la lumière ne la change pas : elle éclaire la rue.",
   "L'ampoule est une pièce du lampadaire, une solution : elle n'a pas de case.",
   "La mairie a commandé le lampadaire : elle n'est ni la personne servie, ni ce sur quoi il agit."],
  "Sur quoi ? → ce que l'objet touche ou change.",
  img=IMG_LAMPE)

q(C, "L'objet qui répond",
  "Voici le besoin de Léa, avant d'acheter. Quel objet remplit les trois branches ?",
  ["un vélo-cargo avec un grand bac",
   "une voiture familiale à cinq places",
   "un vélo avec un siège enfant à l'arrière",
   "une trottinette électrique pliable"],
  "Le vélo-cargo sert à Léa, porte deux enfants et des courses dans son bac, en ville et sans voiture : les trois branches "
  "sont remplies.",
  "Un parent qui doit porter un seul enfant, sans courses, pourrait choisir le vélo à siège enfant : son besoin est différent.",
  "Garder l'objet qui fait « presque tout ».",
  ["",
   "La voiture transporte tout le monde, mais le but dit « sans voiture » : une branche échoue.",
   "Un siège enfant ne porte qu'un enfant, et il ne reste pas de place pour les courses.",
   "Une trottinette ne porte que la personne debout dessus : ni enfants, ni courses."],
  "Un objet répond au besoin s'il remplit les trois branches.",
  img=IMG_BESOIN)

q(C, "La branche qui échoue",
  "Un sac à dos sert bien à Léa. Quelle branche de son besoin (deux enfants et des courses, en ville, sans voiture) échoue ?",
  ["« sur quoi ? » : il porte les courses, pas les enfants",
   "« à qui ? » : un sac à dos n'est fait pour personne",
   "« dans quel but ? » : on ne va pas en ville à pied",
   "aucune : un sac à dos répond aux trois branches à la fois"],
  "Le sac à dos sert à Léa (à qui ✔), mais il ne porte que les courses : deux enfants n'y entrent pas. La branche « sur "
  "quoi ? » échoue, et l'objet est écarté.",
  "Une trottinette échoue au même endroit : elle ne porte que la personne debout dessus.",
  "Écarter un objet sans dire quelle branche échoue.",
  ["",
   "Le sac à dos sert bien à Léa : la branche « à qui ? » est remplie.",
   "On peut aller en ville à pied ; le problème est ailleurs : le sac ne porte pas deux enfants.",
   "Il suffit d'une branche qui échoue : deux enfants n'entrent pas dans un sac à dos."],
  "Une seule branche qui échoue suffit à écarter un objet.")

q(C, "Ce que la bête à cornes ne fait pas",
  "Parmi ces phrases sur la bête à cornes, laquelle est FAUSSE ?",
  ["Elle liste tout ce que l'objet doit respecter (la pluie…).",
   "Elle peut être écrite avant de savoir quel objet on choisira.",
   "Elle se lit comme une phrase : à qui, sur quoi, pour quoi.",
   "Son but s'écrit avec un verbe à l'infinitif, sans solution."],
  "La bête à cornes exprime le besoin, en trois cases. Ce que l'objet doit respecter (résister à la pluie, monter les "
  "côtes…) vient ensuite, avec le diagramme des interacteurs extérieurs.",
  "« Résister à la pluie » est une contrainte du vélo-cargo : elle n'a pas de case dans sa bête à cornes.",
  "Demander à la bête à cornes de tout dire de l'objet.",
  ["",
   "C'est vrai : on exprime le besoin avant de choisir l'objet ; le produit peut rester un point d'interrogation.",
   "C'est vrai : « le vélo-cargo rend service à Léa, en agissant sur ses enfants et ses courses, pour les transporter ».",
   "C'est vrai : un verbe à l'infinitif, et aucune solution."],
  "La bête à cornes exprime le besoin ; les contraintes viennent après.")

q(C, "Reconnaître le schéma",
  "Un schéma a deux cases en haut (à qui ? sur quoi ?), l'objet au milieu et le but en bas. Comment l'appelle-t-on souvent ?",
  ["la bête à cornes",
   "le diagramme pieuvre",
   "le diagramme de Gantt",
   "la chaîne d'énergie"],
  "Ce schéma exprime le besoin ; on l'appelle souvent la bête à cornes, à cause de la courbe qui part des deux cases et passe "
  "sous l'objet, comme des cornes.",
  "Le diagramme pieuvre, lui, met l'objet au centre et tous ses interacteurs autour.",
  "Confondre les représentations parce qu'elles placent toutes l'objet quelque part.",
  ["",
   "Le diagramme pieuvre place l'objet au centre et, autour, tous ses interacteurs : il ne pose pas les trois questions du besoin.",
   "Le diagramme de Gantt place des tâches dans le temps : il sert à organiser un projet.",
   "La chaîne d'énergie suit l'énergie dans l'objet : alimenter, distribuer, convertir, transmettre."],
  "Le besoin → la bête à cornes.")

q(C, "Le but devient…",
  "Le but écrit dans la bête à cornes devient…",
  ["la fonction d'usage de l'objet",
   "la liste des pièces à acheter",
   "le prix de vente de l'objet en magasin",
   "le nom de l'objet, écrit au centre"],
  "Le but dit à quoi sert l'objet : c'est sa <b>fonction d'usage</b>. Elle sert ensuite de point de départ aux autres "
  "schémas de l'objet.",
  "Le vélo-cargo → fonction d'usage : transporter des enfants et des courses en ville.",
  "Croire que le but est une phrase qui décore le schéma.",
  ["",
   "Les pièces sont des solutions : la bête à cornes n'en parle pas.",
   "Le prix ne figure pas dans la bête à cornes : elle dit à quoi sert l'objet.",
   "Le nom de l'objet est au centre ; le but, en bas, dit à quoi il sert."],
  "But = fonction d'usage.")

# ═══════════════ 4e_C1.3 — Justifier l'évolution d'un OST pour répondre à l'évolution des besoins (5) ═══════════════
C = "4e_C1.3"

q(C, "Ce qui a changé",
  "Voici la bête à cornes du système d'arrosage connecté. Celle de l'arrosoir disait : la gardienne ; les plantes du jardin ; "
  "arroser les plantes du jardin. Qu'est-ce qui a changé ?",
  ["le but : arroser même sans la gardienne, sans gaspiller l'eau",
   "la case « à qui ? » : le système rend maintenant service aux plantes",
   "la case « sur quoi ? » : le système agit sur le smartphone",
   "rien : seul l'objet a changé, le besoin est exactement le même"],
  "À qui ? la gardienne, dans les deux. Sur quoi ? les plantes, dans les deux. C'est le <b>but</b> qui s'est enrichi : les "
  "vacances et le carême ont changé le besoin.",
  "Un cartable remplacé par un sac à roulettes : le but devient « transporter ses affaires sans se faire mal au dos ».",
  "Chercher le changement dans l'objet seulement, sans regarder le besoin.",
  ["",
   "Les plantes reçoivent l'eau : elles sont dans la case « sur quoi ? ». C'est toujours à la gardienne que le système rend service.",
   "Le smartphone est un autre objet avec lequel le système échange ; le système agit toujours sur les plantes.",
   "Si le besoin était le même, l'arrosoir suffirait encore : c'est parce que le but a changé que l'objet a changé."],
  "On justifie une évolution en comparant les buts.",
  img=IMG_ARROSAGE)

q(C, "Justifier une évolution",
  "Laquelle de ces phrases JUSTIFIE le passage de l'arrosoir au système d'arrosage connecté ?",
  ["Pendant les vacances, personne ne peut arroser : le besoin a changé.",
   "Le système connecté est plus récent, donc il est forcément meilleur que l'arrosoir.",
   "L'arrosoir est un objet ancien que plus personne n'utilise.",
   "Le système connecté a un écran, des voyants et une application."],
  "Justifier une évolution, c'est montrer que le <b>besoin</b> a changé : les vacances demandent d'arroser sans la "
  "gardienne, le carême demande d'économiser l'eau.",
  "La lampe solaire remplace la lampe à pétrole parce qu'on veut s'éclairer même pendant une coupure, sans fumée.",
  "Justifier par la nouveauté ou par les options de l'objet.",
  ["",
   "Plus récent ne veut pas dire mieux adapté : sans les vacances et le carême, l'arrosoir répondrait encore.",
   "L'arrosoir sert encore dans bien des jardins ; ce qui a changé, c'est le besoin de celui-ci.",
   "L'écran et l'application sont des solutions : ils décrivent l'objet, ils ne disent pas pourquoi il a fallu en changer."],
  "Un objet évolue parce que le besoin évolue.")

q(C, "Le carême",
  "En carême, l'eau de la cuve devient rare. Qu'est-ce qui fait évoluer le besoin du jardin, ici ?",
  ["le développement durable : économiser une ressource rare",
   "la mode des objets connectés, que tout le monde veut avoir",
   "la couleur du nouveau système, plus jolie que l'ancien",
   "le prix de l'arrosoir, devenu bien trop cher dans les magasins"],
  "Économiser l'eau, une ressource rare, c'est une préoccupation de <b>développement durable</b> : elle ajoute « sans "
  "gaspiller l'eau » au but.",
  "Une lampe qui consomme moins d'énergie répond aussi à un besoin nouveau de développement durable.",
  "Croire qu'un besoin n'évolue que lorsqu'on invente un nouvel objet.",
  ["",
   "La mode ne change pas ce qu'on demande à l'objet : le carême, lui, ajoute « sans gaspiller l'eau ».",
   "La couleur ne répond à aucune partie du besoin.",
   "Le prix de l'arrosoir n'est pas en cause : c'est le manque d'eau qui change le but."],
  "Développement durable, inventions, innovations, façons de vivre : ce qui fait évoluer un besoin.")

q(C, "Le nouveau but",
  "Quel nouveau but est bien formulé pour le système d'arrosage ?",
  ["Arroser les plantes même sans la gardienne, sans gaspiller l'eau",
   "Commander une pompe et une électrovanne depuis un smartphone",
   "Mesurer l'humidité de la terre avec un capteur planté au sol",
   "Le système d'arrosage connecté installé au jardin partagé du collège"],
  "Un verbe à l'infinitif, les plantes, l'absence de la gardienne, l'économie d'eau — et aucune solution.",
  "« Prévenir les habitants de l'arrivée d'un cyclone » : même forme, pour un projet d'alerte.",
  "Écrire dans le but les pièces du système.",
  ["",
   "La pompe, l'électrovanne et le smartphone sont des solutions : elles disent comment, pas pourquoi.",
   "Le capteur est une solution, et mesurer l'humidité est une fonction technique : ce n'est pas le but.",
   "C'est le nom de l'objet, sans verbe : il va au centre du schéma, pas dans le but."],
  "Le nouveau but : un verbe, sans solution.")

q(C, "Ce qui reste pareil",
  "Dans les deux bêtes à cornes, la case « sur quoi ? » dit « les plantes du jardin ». Qu'est-ce que cela montre ?",
  ["Le système agit toujours sur les mêmes plantes : c'est le but qui change.",
   "Le dessinateur a oublié de mettre à jour la case « sur quoi ? ».",
   "Les plantes du jardin ont besoin d'un objet plus moderne qu'avant pour pousser.",
   "La case « sur quoi ? » ne change jamais, quel que soit l'objet."],
  "Comparer, c'est aussi voir ce qui reste pareil : la gardienne et les plantes n'ont pas bougé. Seul le but s'est enrichi.",
  "Cartable et sac à roulettes : l'élève et ses affaires ne changent pas ; le but, si.",
  "Croire que tout change quand l'objet change.",
  ["",
   "Ce n'est pas un oubli : le système arrose bien les mêmes plantes.",
   "Les plantes poussent de la même façon ; ce qui change, c'est qu'il faut les arroser sans la gardienne.",
   "Elle change souvent d'un objet à l'autre : un vélo-cargo agit sur des enfants, un arrosoir sur des plantes."],
  "Comparer, c'est voir ce qui change et ce qui reste.")

# ═══════════════ 4e_C3.1 — Identifier les caractéristiques à prendre en compte dans le choix d'un OST (5) ═══════════════
C = "4e_C3.1"

q(C, "L'absence de la gardienne",
  "Besoin : arroser les plantes même en l'absence de la gardienne. Quelle caractéristique sert cette partie du besoin ?",
  ["l'autonomie, en nombre de jours sans intervention",
   "la couleur du boîtier, assortie aux plantes du jardin",
   "le nombre de boutons sur le boîtier",
   "la marque du fabricant, connue de tous"],
  "« Même en l'absence de la gardienne » se mesure en jours : combien de temps le système arrose-t-il seul ? C'est son "
  "<b>autonomie</b>.",
  "Pour une lampe de secours après un cyclone : l'autonomie, en heures.",
  "Choisir une caractéristique qui se voit au lieu de celle qui sert le besoin.",
  ["",
   "La couleur ne fait pas arroser plus longtemps.",
   "Le nombre de boutons ne dit pas combien de jours le système tient seul.",
   "Une marque connue ne dit rien de l'autonomie d'un modèle."],
  "Absence → autonomie.")

q(C, "Sans gaspiller l'eau",
  "« Sans gaspiller l'eau » : quelle caractéristique faut-il comparer entre deux modèles ?",
  ["la consommation d'eau par jour, en litres",
   "la longueur du tuyau livré avec le système",
   "la vitesse à laquelle l'eau sort du tuyau",
   "le volume du carton d'emballage, en litres"],
  "Ne pas gaspiller, cela se mesure : combien de litres le système utilise-t-il par jour ? On compare cette "
  "<b>consommation</b> d'un modèle à l'autre.",
  "Pour un lave-linge, on compare aussi la consommation d'eau par lavage.",
  "Choisir une grandeur qui parle d'eau, mais qui ne dit rien du gaspillage.",
  ["",
   "Un tuyau plus long ne dit pas si l'eau est gaspillée.",
   "La vitesse de sortie parle bien de l'eau, mais pas de la quantité utilisée chaque jour : un jet rapide et court peut gaspiller moins qu'un jet lent et continu.",
   "Le carton n'a rien à voir avec l'eau des plantes, même s'il se mesure aussi en litres."],
  "Sans gaspiller → consommation d'eau.")

q(C, "L'intrus",
  "Pour choisir un système d'arrosage qui réponde au besoin du jardin, laquelle de ces caractéristiques est à écarter ?",
  ["la couleur du boîtier",
   "la résistance à la pluie",
   "la capacité de la cuve",
   "la facilité de réglage"],
  "Si on change la couleur, le système arrose tout aussi bien, sans la gardienne et sans gaspiller : elle ne sert pas ce besoin.",
  "Pour choisir une glacière de plage, la couleur ne compte pas ; le nombre d'heures au frais, si.",
  "Écarter une caractéristique utile parce qu'elle n'est pas écrite mot pour mot dans le but.",
  ["",
   "Le système vit dehors : en panne après une averse, il n'arroserait plus en l'absence de la gardienne.",
   "Pendant les vacances, la cuve doit contenir assez d'eau pour tous les jours d'absence.",
   "C'est la gardienne qui règle le système : la branche « à qui ? » le demande."],
  "On écarte ce qui ne sert pas le besoin.")

q(C, "Le point de départ",
  "Pour savoir quelles caractéristiques comparer avant de choisir un objet, on part…",
  ["du besoin : chaque partie appelle une caractéristique",
   "de la publicité, qui dit ce qui compte le plus",
   "du modèle le plus cher, qui est forcément le plus complet",
   "de la couleur préférée de la personne qui achète"],
  "La bête à cornes dit ce qu'on attend de l'objet ; chaque partie indique ce qu'il faut mesurer et comparer.",
  "« Même en l'absence » → l'autonomie ; « sans gaspiller l'eau » → la consommation.",
  "Comparer des modèles sur ce qu'ils mettent en avant, au lieu de ce dont on a besoin.",
  ["",
   "La publicité met en avant ce qui fait vendre, pas forcément ce qui répond à ce besoin-là.",
   "Le plus cher peut avoir des options inutiles pour ce besoin, et manquer de l'essentiel.",
   "La couleur ne répond à aucune partie du besoin du jardin."],
  "Le besoin d'abord, les caractéristiques ensuite.")

q(C, "Un critère du programme",
  "Le programme cite des critères de choix valables pour presque tous les objets. Lequel en fait partie ?",
  ["l'efficacité énergétique",
   "la couleur la plus à la mode",
   "le nombre de boutons",
   "la marque la plus connue"],
  "Le programme cite la qualité, l'efficacité énergétique, la durabilité et la recyclabilité : des critères qui se "
  "mesurent et qui comptent aussi pour la planète.",
  "Deux systèmes d'arrosage qui arrosent aussi bien : on préfère celui qui consomme le moins d'énergie.",
  "Confondre un critère de choix avec un goût personnel.",
  ["",
   "La mode change d'une année à l'autre : ce n'est pas un critère de choix technique.",
   "Le nombre de boutons ne dit ni la qualité, ni la consommation, ni la durée de vie.",
   "Une marque connue ne garantit aucune caractéristique mesurée."],
  "Qualité, efficacité énergétique, durabilité, recyclabilité.")

# ═══════════════ 3e_C3.1 — Établir une liste d'OST possibles en vue de répondre à un besoin (10) ═══════════════
C = "3e_C3.1"

q(C, "Ce qu'est un OST",
  "Lequel de ces éléments est un OST (un objet ou système technique) qui pourrait prévenir les habitants d'un cyclone ?",
  ["une sirène installée sur le toit de la mairie",
   "la mairie de Sainte-Luce, qui décide de donner l'alerte",
   "évacuer le quartier avant l'arrivée du vent",
   "le vent violent qui annonce le cyclone"],
  "Un OST est un objet fabriqué, ou plusieurs objets qui travaillent ensemble. La sirène en est un ; une personne, une "
  "action ou le danger lui-même n'en sont pas.",
  "La radio locale est un système : un émetteur, et des postes chez les habitants.",
  "Mettre dans la liste celui qui décide, ou ce qu'on fait.",
  ["",
   "La mairie est un service : elle choisit l'OST, elle n'en est pas un.",
   "Évacuer est une action : on la fait une fois prévenu.",
   "Le vent est le danger lui-même : il annonce le cyclone, mais personne ne l'a fabriqué."],
  "OST = un objet ou un système fabriqué.")

q(C, "La liste de départ",
  "Avec ce besoin, quelle liste de départ est la plus utile ? (Un SMS est un texto ; un OST, un objet ou système technique.)",
  ["sirène, SMS, radio locale, haut-parleur, panneau lumineux",
   "le SMS seulement, puisque presque tout le monde a un téléphone",
   "la mairie, les pompiers, les voisins, la gendarmerie",
   "fermer les volets, rentrer le linge, remplir des bidons"],
  "La liste utile est large et faite d'OST de familles différentes : un son, un téléphone, la radio, une voix, une lumière.",
  "Si le réseau téléphonique est coupé, la sirène et la radio prennent le relais.",
  "Arrêter la liste à la première idée.",
  ["",
   "Une seule idée ferme la liste : sans réseau, ou sans téléphone, des habitants ne seraient pas prévenus.",
   "Ce sont des personnes et des services : ils utiliseront des OST, ils n'en sont pas.",
   "Ce sont des actions pour se protéger, une fois prévenu : aucune ne prévient les habitants."],
  "Une liste large, d'OST de familles différentes.",
  img=IMG_ALERTE)

q(C, "Pourquoi une liste longue",
  "Pourquoi établir une longue liste d'OST (objets ou systèmes techniques) plutôt que garder la première idée ?",
  ["parce que chaque OST a ses faiblesses, qu'un autre peut compenser",
   "parce qu'il faudra ensuite acheter et installer tous les OST de la liste",
   "parce que la première idée est toujours la plus mauvaise",
   "parce qu'une longue liste montre qu'on a beaucoup travaillé"],
  "Le SMS (le texto) a besoin du réseau, que le cyclone peut couper ; la sirène s'entend mal dans une maison fermée. Une liste longue "
  "garde des possibilités pour choisir ensuite.",
  "Pour la fin de la récréation : sonnerie, cloche, haut-parleur… si la sonnerie tombe en panne, une autre idée existe.",
  "Confondre établir une liste et décider d'acheter.",
  ["",
   "Établir n'est pas acheter : on choisira ensuite, avec des critères.",
   "La première idée peut être la meilleure ; la liste sert à le vérifier.",
   "Le travail fourni ne dit rien de la qualité du choix."],
  "Élargir avant de choisir.")

q(C, "Utile, mais hors du besoin",
  "Des volets anticycloniques sont des objets utiles. Pourquoi ne sont-ils pas sur la liste de ce besoin (prévenir les habitants) ?",
  ["parce qu'ils protègent les maisons, mais ne préviennent personne",
   "parce que ce ne sont pas des objets techniques fabriqués",
   "parce qu'ils coûtent trop cher pour les habitants du quartier",
   "parce qu'on ne peut pas les installer dans un quartier proche de la mer"],
  "Le but est de prévenir les habitants. Les volets répondent à un autre but : protéger les maisons. Ce sont de vrais objets, "
  "mais hors du besoin.",
  "Une lampe torche est utile après un cyclone, mais elle ne prévient personne de son arrivée.",
  "Mettre dans la liste tout ce qui est utile pendant un cyclone.",
  ["",
   "Les volets sont bien des objets fabriqués : le problème est leur but, pas leur nature.",
   "Le coût viendra au moment de choisir ; ici, ils ne répondent pas au but.",
   "On en pose justement près de la mer : ils protègent, mais ne préviennent pas."],
  "Un objet de la liste répond au but écrit.")

q(C, "La case qui nomme une solution",
  "Sur cette bête à cornes, quelle case nomme déjà une solution ?",
  ["la case « dans quel but ? »",
   "la case « à qui ? »",
   "la case « sur quoi ? »",
   "aucune case : tout est juste"],
  "« Envoyer un SMS » (un texto) est un moyen : une solution. Le but devrait dire ce qu'il faut obtenir — prévenir les habitants de "
  "l'arrivée d'un cyclone.",
  "« Installer un écran qui affiche le menu » nomme aussi une solution ; « informer les élèves du menu » n'en nomme aucune.",
  "Croire qu'un but très précis est forcément meilleur.",
  ["",
   "« Les habitants du quartier » : c'est bien eux que l'objet aidera. Cette case est juste.",
   "« La sécurité du quartier » est une erreur, mais d'un autre genre : c'est une idée, pas une solution.",
   "Le but nomme une solution, le SMS, et la case « sur quoi ? » contient une idée : il y a deux erreurs."],
  "Un but ne nomme pas de solution.",
  img=IMG_MAL)

q(C, "Une idée n'est pas une chose",
  "Pourquoi « la sécurité du quartier » ne va-t-elle pas dans la case « sur quoi ? » ?",
  ["c'est une idée : l'objet agit sur les habitants, pas sur elle",
   "c'est une solution technique, qu'il faut garder pour la liste",
   "le mot « sécurité » est trop long pour tenir dans la case",
   "la sécurité n'a rien à voir avec un cyclone qui arrive"],
  "La case « sur quoi ? » nomme une personne ou une chose que l'objet touche, déplace ou prévient. La sécurité est ce qu'on "
  "veut obtenir : elle se dit dans le but.",
  "Pour un lampadaire : « sur quoi ? » la rue — pas « la sécurité des piétons ».",
  "Mettre dans « sur quoi ? » ce qu'on espère, au lieu de ce sur quoi l'objet agit.",
  ["",
   "La sécurité n'est pas une solution : c'est un résultat qu'on espère.",
   "La longueur du mot ne compte pas : « ses deux enfants et ses courses » est plus long, et juste.",
   "Au contraire, la sécurité est tout l'enjeu ; mais c'est ce qu'on veut obtenir, pas ce sur quoi l'objet agit."],
  "Sur quoi ? → une personne ou une chose.")

q(C, "Le but qui rouvre la liste",
  "Quel but rouvre la liste des OST (objets ou systèmes techniques) possibles ?",
  ["Prévenir les habitants du quartier de l'arrivée d'un cyclone",
   "Envoyer un texto et une notification à chaque habitant du quartier",
   "Faire sonner une sirène sur le toit de la mairie de Sainte-Luce",
   "Les habitants du quartier, menacés par les cyclones chaque année"],
  "Un verbe, qui (les habitants), de quoi (le cyclone), et aucune solution : la sirène, le texto, la radio peuvent tous entrer "
  "dans la liste.",
  "« Informer les élèves du menu du jour » rouvre la liste : écran, affiche, annonce…",
  "Remplacer une solution par une autre dans le but.",
  ["",
   "Le texto et la notification sont des solutions : ce but ferme encore la liste.",
   "La sirène est une solution : on a changé d'idée, mais la liste reste fermée.",
   "Il n'y a pas de verbe : c'est une description des habitants, pas un but."],
  "Un but sans solution ouvre la liste.")

q(C, "Le SMS n'est pas interdit",
  "Le but réécrit ne parle plus du SMS (le texto). Le SMS est-il interdit pour autant ?",
  ["Non : il reste une solution possible, dans la liste à comparer.",
   "Oui : une solution écrite une fois dans le but est toujours mauvaise.",
   "Oui : le téléphone ne marche jamais pendant un cyclone.",
   "Non : mais il doit être obligatoirement choisi à la fin."],
  "Le SMS n'avait rien de mauvais ; il n'était pas à sa place. Dans la liste, il sera comparé aux autres objets possibles.",
  "La sirène, la radio et le SMS seront ensuite comparés : fonctionnent-ils sans électricité ? sans réseau ?",
  "Croire qu'une solution mal placée est une mauvaise solution.",
  ["",
   "Le problème était sa place, pas sa valeur : dans la liste, le SMS reste une bonne idée.",
   "Le réseau peut être coupé, mais pas toujours : avant l'arrivée du cyclone, le SMS fonctionne souvent très bien.",
   "Rien n'oblige à le choisir : c'est la comparaison, avec des critères, qui décidera."],
  "Une solution a sa place dans la liste, pas dans le but.")

q(C, "Les mêmes dans les deux cases",
  "Dans la bête à cornes du projet d'alerte, « les habitants du quartier » sont dans les deux cases du haut. Est-ce une erreur ?",
  ["Non : l'objet rend service aux habitants en agissant sur eux.",
   "Oui : une même personne ne peut jamais apparaître dans deux cases.",
   "Oui : il faut mettre la commune dans la case « à qui ? ».",
   "Non : mais seulement parce que le schéma n'est pas terminé."],
  "L'objet prévient les habitants : il agit sur eux, et c'est à eux qu'il rend service. Les deux cases portent alors le même nom.",
  "Un réveil rend service à l'élève et agit sur l'élève : il le réveille.",
  "Croire que les deux cases du haut doivent toujours être différentes.",
  ["",
   "Un réveil rend service à l'élève en agissant sur lui : la même personne est dans les deux cases, et c'est juste.",
   "La commune commande et paie, mais c'est aux habitants que l'objet rend service.",
   "Le schéma est terminé : les deux cases portent le même nom parce que l'objet agit sur ceux qu'il sert."],
  "La même personne peut être servie par l'objet et agie par lui.")

q(C, "Après la liste",
  "Une fois la liste des OST (objets ou systèmes techniques) possibles établie, que fait-on ensuite ?",
  ["On compare les OST selon des critères, puis on choisit.",
   "On installe le premier OST de la liste, le plus simple.",
   "On recommence la bête à cornes avec un nouvel objet.",
   "On tire au sort l'OST qui sera fabriqué par la commune."],
  "Établir la liste, c'est élargir ; choisir, c'est comparer avec des critères (fonctionner sans électricité, coût, "
  "entretien…) et argumenter.",
  "Une sirène sur batterie fonctionne même quand le courant est coupé : un critère qui compte pendant un cyclone.",
  "Choisir sans comparer.",
  ["",
   "Le premier de la liste n'a aucune raison d'être le meilleur : on compare d'abord.",
   "Le besoin ne change pas : on garde la même bête à cornes pour comparer les OST.",
   "Le hasard ne répond pas au besoin : on choisit avec des critères, et on argumente."],
  "Élargir, puis choisir avec des critères.")

Q = B.fin(30, {"5e_C3.3": 10, "4e_C1.3": 5, "4e_C3.1": 5, "3e_C3.1": 10})
