# -*- coding: utf-8 -*-
"""Amorces de la règle d'or n°31, écrites à la main, zone par zone.

Le niveau scientifique attendu est IDENTIQUE à celui de la consigne autonome :
on retire l'obstacle de la rédaction, jamais l'exigence. Chaque amorce doit donc
pouvoir être complétée par une réponse juste et complète — et par elle seule.
"""

def bilan(objet, savoirs, gestes, revoir):
    """Le quatuor de fin de séquence, décliné avec le vocabulaire de la séquence."""
    return {
        "hyp_retour": [
            "Au départ je pensais que ____.",
            "Maintenant je sais que ____, parce que ____ me l'a montré.",
            "Ce qui a changé mon avis, c'est ____.",
        ],
        "bilan1": ["J'ai appris que " + s + " ____." for s in savoirs],
        "bilan2": ["Je sais maintenant " + g + " ____." for g in gestes],
        "bilan3": [
            "Je dois encore revoir ____, parce que ____.",
            "Ce que je n'arrive pas encore à faire seul·e : ____.",
            "Pour progresser, la prochaine fois je ____.",
        ],
    }

A = {}

# ══════════════════════════════════════════════════════════════════════════
A["sequence_3e_C4.1-C4.2_energie_station.html"] = {
 "hyp1": [
   "Pour produire son énergie, la station aura besoin de ____.",
   "Pour la stocker jusqu'à la nuit et pendant les 72 h de cyclone, il faudra ____.",
   "Au bord de la mer, je pense que ____ résistera bien, alors que ____ s'abîmera, parce que ____.",
 ],
 "j4": [
   "Pour le mât, je choisis ____ parce qu'il doit d'abord résister à ____.",
   "Il doit aussi supporter ____ : c'est la deuxième contrainte, et elle écarte ____.",
   "Le procédé retenu est ____, parce que la pièce est ____ (nombre d'exemplaires, forme, dimensions).",
 ],
}

# ══════════════════════════════════════════════════════════════════════════
S = "sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html"
A[S] = {
 "hyp1": [
   "Quand le vent souffle sur l'anémomètre, celui-ci ____.",
   "Ensuite, ce que le capteur produit est transformé par ____.",
   "Pour finir, le nombre « 132 km/h » s'affiche parce que ____.",
 ],
 "hyp2": [
   "Je m'appuie sur ____ (objet déjà vu, expérience, cours précédent).",
   "Ce qui me fait penser cela, c'est que ____.",
   "Ce dont je ne suis pas sûr·e, c'est ____.",
 ],
 "a1_just": [
   "Le panneau solaire ne fait pas partie de la chaîne d'information, parce qu'il ____.",
   "Son rôle est de ____, ce qui correspond à la fonction ____.",
   "La chaîne d'information, elle, sert à ____ — et le panneau n'y participe pas puisque ____.",
 ],
 "a3_exp": [
   "La grandeur réelle (la pression) est continue : entre deux valeurs, il existe ____.",
   "Le CAN, lui, ne peut distinguer que ____ paliers : il est obligé de ____.",
   "La donnée numérique est donc une approximation, parce que ____.",
 ],
 "a6_conc": [
   "Quand le vent monte, la pression ____.",
   "Les deux mesures ensemble rendent l'alerte plus fiable parce qu'une seule pourrait ____.",
   "Si les deux capteurs disent la même chose, alors ____ ; s'ils se contredisent, ____.",
 ],
 "a7_just": [
   "La bouée stocke aussi ses mesures en interne parce que la transmission par satellite peut ____.",
   "Si la liaison est coupée, les mesures ____ — alors qu'avec la carte mémoire, ____.",
   "Ce double enregistrement sert aussi à ____ après la tempête.",
 ],
 **bilan("la station",
   ["une grandeur physique devient une donnée numérique en", "le nombre de paliers d'un CAN dépend de", "un fichier .csv sert à"],
   ["calculer la précision d'un capteur à partir de", "lire un relevé horaire et y repérer", "expliquer pourquoi une mesure numérique est"],
   "les CAN"),
}

# ══════════════════════════════════════════════════════════════════════════
S = "sequence_3e_C4.7-C4.8_internet_sainte_luce.html"
A[S] = {
 "hyp1": [
   "D'après moi, le message part d'abord vers ____.",
   "Ensuite il traverse ____ pour franchir l'océan.",
   "Je pense qu'il utilise plutôt ____ que ____, parce que ____.",
 ],
 "hyp2": [
   "Je m'appuie sur ____.",
   "Ce qui me le fait penser, c'est que ____.",
   "Ce dont je doute, c'est ____.",
 ],
 "b2_cahier": [
   "Le message part de ____ et rejoint d'abord ____.",
   "Il passe ensuite par ____, puis franchit l'Atlantique par ____.",
   "Il arrive enfin à ____ après être passé par le centre d'échange n°____.",
 ],
 "b4_just": [
   "Un protocole de routage commun est nécessaire parce que les routeurs doivent ____.",
   "Sans règles identiques pour tous, un routeur fabriqué par une entreprise ne pourrait pas ____.",
   "C'est comparable à ____ : si chacun utilisait ses propres règles, ____.",
 ],
 "b5_exp": [
   "Internet a été conçu avec plusieurs chemins possibles pour que ____.",
   "Les tables de routage sont mises à jour en permanence afin de ____.",
   "En revanche, aucun protocole ne peut ____ : si toutes les routes physiques sont coupées, ____.",
 ],
 "b6_just": [
   "Ce voyage n'est possible que parce que tous les réseaux traversés ____.",
   "Chaque appareil du trajet sait quoi faire du paquet parce qu'il ____.",
   "Si un seul maillon n'appliquait pas les mêmes règles, alors ____.",
 ],
 **bilan("Internet",
   ["un paquet voyage de réseau en réseau grâce à", "une table de routage sert à", "l'essentiel du trafic intercontinental passe par"],
   ["suivre le trajet d'un message de la Martinique à", "expliquer pourquoi un message arrive même quand", "justifier la nécessité d'un protocole commun en"],
   "le routage"),
}

# ══════════════════════════════════════════════════════════════════════════
S = "sequence_3e_C4.7-C4.8_pont_numerique_packet_tracer.html"
A[S] = {
 "hyp1": [
   "À la frontière entre deux réseaux, je pense qu'un appareil ____.",
   "Pour choisir la direction, il doit d'abord regarder ____ dans le message.",
   "Ce qui lui permet de décider, c'est probablement ____.",
 ],
 "e1c_prod": [
   "Depuis PC-MQ, le message entre d'abord dans ____, dont le rôle est de ____.",
   "Il atteint ensuite ____, qui marque la frontière parce qu'il ____.",
   "La rue-pont relie ____ à ____ ; de l'autre côté, ____ distribue jusqu'au serveur de New York.",
   "Les deux rues sont ____ et ____.",
 ],
 "e2_just": [
   "Avec deux réseaux seulement, on peut écrire les routes à la main parce que ____.",
   "Avec des centaines de milliers de réseaux, ce n'est plus possible car ____.",
   "Un protocole de routage devient donc nécessaire pour que les routeurs ____ sans intervention humaine.",
 ],
 **bilan("le pont numérique",
   ["un routeur se distingue d'un commutateur parce qu'il", "une table de routage indique", "le TTL sert à"],
   ["appliquer une table de routage pour dire", "lire une trace saut par saut et y repérer", "justifier pourquoi un protocole de routage est"],
   "les tables de routage"),
}

# ══════════════════════════════════════════════════════════════════════════
A["sequence_4e_C4.1-C4.9_jardin_connecte.html"] = {
 "hyp1": [
   "La mesure part du capteur planté dans la terre, qui transforme ____ en ____.",
   "Elle est ensuite traitée par ____, dont le rôle est de ____.",
   "Elle est enfin transmise par ____ jusqu'à la tablette, où elle devient ____.",
 ],
}

# ══════════════════════════════════════════════════════════════════════════
S = "sequence_5e_C4.1-C4.8_lampadaire_intelligent.html"
A[S] = {
 "hyp1": [
   "Je pense que le lampadaire sait qu'il doit s'allumer grâce à ____.",
   "Ce qu'il mesure, c'est ____.",
   "Il s'allume quand ____ devient ____.",
 ],
 "hyp2": [
   "La nuit, son énergie vient de ____.",
   "Cette énergie a été mise de côté pendant ____.",
   "Sans cela, le lampadaire ____.",
 ],
 "e1_just": [
   "Pour le mât, on choisit de l'acier galvanisé parce qu'en Martinique il doit résister à ____.",
   "L'acier seul poserait le problème de ____.",
   "La galvanisation ajoute ____, ce qui ____.",
 ],
 "e2_cahier": [
   "La chaîne d'énergie commence par ____, qui capte ____.",
   "Elle continue par ____, qui stocke l'énergie sous forme ____.",
   "Elle se termine par ____, qui transforme ____ en ____.",
 ],
 "e6_just": [
   "Chaque terminal doit avoir un nom unique parce que sinon ____.",
   "C'est comme ____ : deux ____ identiques rendraient la livraison ____.",
 ],
 **bilan("le lampadaire",
   ["un capteur sert à", "une batterie stocke l'énergie sous forme", "un matériau se choisit d'abord en fonction de"],
   ["retrouver les trois fonctions de la chaîne d'énergie dans", "expliquer comment le lampadaire décide", "justifier qu'un terminal doit porter"],
   "la chaîne d'énergie"),
}

# ══════════════════════════════════════════════════════════════════════════
S = "sequence_5e_C4.7-C4.8_reseau_local_packet_tracer.html"
A[S] = {
 "hyp1": [
   "Un message peut arriver au mauvais appareil si ____.",
   "Cela se produirait par exemple quand ____.",
   "Pour l'éviter, il faudrait que chaque appareil ____.",
 ],
 "e1_just": [
   "La règle du jeu : chaque appareil du réseau doit porter ____ unique, sinon ____.",
   "Le boîtier central, lui, ____ ; il ne décide pas de ____.",
 ],
 "e2c_prod": [
   "Au centre de mon schéma, j'ai placé ____.",
   "J'ai tracé ____ traits pleins, qui représentent ____.",
   "J'ai tracé ____ traits en pointillés, qui représentent ____.",
   "La forme obtenue s'appelle ____.",
 ],
 "e4_just": [
   "Deux appareils ne peuvent pas porter le même dernier nombre parce que ____.",
   "Le facteur, lui, ne saurait pas ____ ; sur le réseau, le message ____.",
 ],
 **bilan("le réseau de la salle",
   ["un commutateur sert à", "une adresse IP identifie", "un doublon d'adresse provoque"],
   ["construire un réseau en étoile en plaçant", "attribuer une adresse à un terminal dans", "vérifier qu'une livraison a réussi en"],
   "l'adressage"),
}

# ══════════════════════════════════════════════════════════════════════════
S = "sequence_3e_C5.1-C5.4_sos_station_reparer.html"
A[S] = {
 "hyp1": [
   "Les causes possibles sont ____, ____ et ____.",
   "Je commencerais par ____, parce que c'est ____ à vérifier.",
   "Si ce n'est pas cela, je passerais ensuite à ____.",
 ],
 "hyp2": [
   "Je m'appuie sur ____.",
   "Ce qui me le fait penser, c'est que ____.",
   "Ce dont je ne suis pas sûr·e, c'est ____.",
 ],
 "c2_just": [
   "L'arbre pose la question de la LED en premier parce qu'elle permet de savoir si ____.",
   "Tant qu'on ne sait pas cela, on ne peut pas distinguer une panne de ____ d'une panne de ____.",
   "On ne change qu'une chose à la fois parce que sinon ____.",
 ],
 "c3_prot": [
   "Étape 1 : je vérifie d'abord ____, parce que ____.",
   "Étape 2 : si c'est correct, je contrôle ____ et j'attends de trouver ____.",
   "Étape 3 : je ne modifie que ____, puis je ____ pour vérifier l'effet.",
   "Étape 4 : je note ____, pour que le suivant puisse ____.",
 ],
 "c6_dec": [
   "Je choisis de ____, parce que la pièce coûte ____ contre ____ pour un appareil neuf.",
   "Réparer évite en plus ____.",
   "Le temps passé, lui, représente ____ — mais il m'apporte ____.",
 ],
 **bilan("la station en panne",
   ["une panne se localise en", "un arbre de diagnostic sert à", "on ne mesure jamais sur"],
   ["suivre un protocole de dépannage sans", "décider s'il faut réparer ou remplacer en comparant", "écrire un protocole en 3 ou 4 étapes qui"],
   "le diagnostic"),
}

# ══════════════════════════════════════════════════════════════════════════
A["sequence_4e_C5.1-C5.3_depanner_jardin.html"] = {
 "hyp1": [
   "La cause la plus probable est ____, parce que l'écran dit ____ alors que la terre ____.",
   "Mon premier test serait ____.",
   "S'il montre ____, alors je saurai que ____.",
 ],
}

# ══════════════════════════════════════════════════════════════════════════
A["sequence_5e_C5.1-C5.3_depanner_lampadaire.html"] = {
 "hyp1": [
   "Après l'orage, la cause la plus probable est ____, parce que ____.",
   "Je chercherais d'abord du côté de ____.",
   "Ce que je m'attends à y voir, c'est ____.",
 ],
}

# ══════════════════════════════════════════════════════════════════════════
S = "sequence_3e_C6.1-C6.3_programmer_alerte.html"
A[S] = {
 "hyp1": [
   "Avant de modifier un programme, il faut connaître ____.",
   "Il faut aussi savoir ____, sinon on risque de ____.",
   "Le plus dangereux serait de ____ sans avoir compris ____.",
 ],
 "hyp2": [
   "Pour être sûr·e de n'avoir rien cassé, je ____.",
   "Je referais surtout les essais qui ____.",
   "Si un ancien essai ne donne plus le même résultat, cela signifie ____.",
 ],
 "d2_just": [
   "Dans la situation B, la valeur 118 est exactement ____.",
   "L'opérateur de comparaison de la ligne 12 est ____, ce qui veut dire que ____.",
   "Le résultat est donc ____, alors qu'avec ____ on aurait obtenu ____.",
 ],
 **bilan("le programme de la station",
   ["une donnée d'entrée se distingue d'une sortie parce qu'elle", "un seuil sert à", "un jeu d'essai permet de"],
   ["repérer dans un programme les données qu'il", "modifier un seuil sans", "prouver qu'une modification n'a rien cassé en"],
   "les jeux d'essai"),
}

# ══════════════════════════════════════════════════════════════════════════
A["sequence_4e_C6.1-C6.3_ajuster_programme_jardin.html"] = {
 "hyp1": [
   "Le « clignotement » vient du fait que la mesure ____ autour du seuil de 40 %.",
   "Comme le programme ne compare qu'à ____, la pompe ____ dès que ____.",
   "Pour l'éviter, je proposerais de ____.",
 ],
}

# ══════════════════════════════════════════════════════════════════════════
A["sequence_5e_C6.1-C6.3_programmer_lampadaire.html"] = {
 "hyp1": [
   "Pour que le lampadaire s'allume plus tôt, il faut changer ____ dans le programme.",
   "Cette valeur sert à ____.",
   "Si je l'augmente, alors ____ ; si je la diminue, alors ____.",
 ],
}
