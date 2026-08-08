# -*- coding: utf-8 -*-
"""Libellés du tableau de bord des tâches (règle d'or n°30), écrits à la main.

Un libellé dit ce que l'élève FAIT, à l'infinitif, en une ligne lisible d'un coup d'œil :
la barre de progression COMPTE, ce bandeau SITUE. Les titres d'activités des séquences ne
conviennent pas tels quels — ils annoncent un thème, pas une action ; c'est ce qui avait
fait échouer la mécanisation du 08/08/2026 au matin.

Structure : fichier → clé du panneau de séance (data-panel) → (titre affiché, [(n° de check, libellé)]).
"""

L = {}

L["sequence_3e_C4.1-C4.2_energie_station.html"] = {
 "s1": ("Séance 1 — Élaborer la chaîne d'énergie", [
   (1, "Élaborer le schéma-bloc de la chaîne d'énergie"),
   (2, "Dimensionner l'installation pour tenir 72 h au simulateur"),
   (6, "Appliquer la loi d'Ohm au circuit de la station")]),
 "s2": ("Séance 2 — Justifier les matériaux", [
   (3, "Lire les contraintes du site (vent, sel, UV)"),
   (4, "Choisir et justifier un matériau et un procédé, pièce par pièce"),
   (5, "Réinvestir la méthode sur la borne solaire du stade")]),
}

L["sequence_3e_C4.3-C4.6_station_alerte_cyclonique.html"] = {
 "s1": ("Séance 1 — Décoder la station", [
   (1, "Classer les huit organes dans les chaînes d'information et d'énergie"),
   (2, "Construire la chaîne d'information de la station")]),
 "s2": ("Séance 2 — Du signal au nombre", [
   (3, "Calculer la précision d'un CAN et convertir une mesure")]),
 "s3": ("Séance 3 — Typer et nommer les données", [
   (4, "Typer, nommer et coder les données de la station")]),
 "s4": ("Séance 4 — Enquêter dans les données", [
   (5, "Choisir le bon format de fichier pour chaque information"),
   (6, "Dépouiller le relevé de la nuit du cyclone"),
   (7, "Analyser la bouée houlographe de Sainte-Anne")]),
}

L["sequence_3e_C4.7-C4.8_internet_sainte_luce.html"] = {
 "s1": ("Séance 1 — Du réseau local au grand voyage", [
   (1, "Identifier les appareils du réseau local du collège"),
   (2, "Retracer le trajet Sainte-Luce → Paris et le noter au cahier")]),
 "s2": ("Séance 2 — Paquets et routage", [
   (3, "Découper, expédier et réassembler un message en paquets"),
   (4, "Jouer le routeur : appliquer une table de routage")]),
 "s3": ("Séance 3 — Éprouver la résistance du réseau", [
   (5, "Couper un câble au simulateur et observer le re-routage"),
   (6, "Suivre un mail pour Tokyo et justifier le rôle des protocoles")]),
}

L["sequence_3e_C4.7-C4.8_pont_numerique_packet_tracer.html"] = {
 "seance1": ("Séance 1 — Concevoir le pont", [
   (0, "Billet d'entrée : vérifier ses acquis de 4e (sans note)"),
   (1, "Comparer sa proposition au schéma de référence"),
   (2, "Jouer le routeur R-MQ sur les quatre enveloppes")]),
 "seance2": ("Séance 2 — Construire dans Packet Tracer", [
   (3, "Relever sur son écran les valeurs du réseau construit")]),
 "seance3": ("Séance 3 — Prouver le voyage", [
   (4, "Rapporter les preuves : ping, TTL et tracert"),
   (5, "Mener les deux expériences du poste-frontière")]),
}

L["sequence_4e_C4.1-C4.9_jardin_connecte.html"] = {
 "s1": ("Séance 1 — La chaîne d'énergie", [
   (1, "Suivre l'énergie du soleil jusqu'à l'eau")]),
 "s2": ("Séance 2 — La chaîne d'information", [
   (2, "Construire la chaîne d'information du jardin"),
   (3, "Suivre le voyage de la donnée jusqu'à la table")]),
 "s3": ("Séance 3 — Dépanner le réseau", [
   (4, "Résoudre les trois pannes du réseau")]),
 "s4": ("Séance 4 — Matériaux et procédés", [
   (5, "Enquêter sur quatre pièces du jardin")]),
}

L["sequence_4e_C4.7-C4.9_sos_serre_packet_tracer.html"] = {
 "seance1": ("Séance 1 — Concevoir le réseau de la serre", [
   (0, "Passeport réseau : vérifier ses acquis de 5e (sans note)"),
   (1, "Comparer sa proposition au plan de référence")]),
 "seance2": ("Séance 2 — Construire et valider", [
   (2, "Relever sur son écran les valeurs du réseau construit"),
   (3, "Apporter les preuves n°2 et 3 sur le reste du quartier")]),
 "seance3": ("Séance 3 — Diagnostiquer les pannes", [
   (4, "Mener les deux consultations de la clinique du réseau")]),
 "seance4": ("Séance 4 — Compléter la simulation", [
   (5, "Compléter la simulation fournie (contrat de 4e_C4.9)")]),
}

L["sequence_5e_C4.1-C4.8_lampadaire_intelligent.html"] = {
 "s1": ("Séance 1 — Fonctions et matériaux", [
   (1, "Associer fonctions, solutions et matériaux")]),
 "s2": ("Séance 2 — La chaîne d'énergie", [
   (2, "Remonter la chaîne d'énergie du lampadaire")]),
 "s3": ("Séance 3 — La chaîne d'information", [
   (3, "Suivre la chaîne d'information en direct")]),
 "s4": ("Séance 4 — Les données du parc", [
   (4, "Lire et exploiter la table des lampadaires")]),
 "s5": ("Séance 5 — Le réseau local", [
   (5, "Identifier les habitants du réseau local"),
   (6, "Jouer le jeu du courrier et en tirer la règle de l'adresse unique"),
   (7, "Analyser la sonnette connectée du portail")]),
}

L["sequence_5e_C4.7-C4.8_reseau_local_packet_tracer.html"] = {
 "seance1": ("Séance 1 — Comprendre et concevoir", [
   (0, "Vérifier ses bagages avant de partir (sans note)"),
   (1, "Jouer le facteur du réseau avant d'apprendre"),
   (2, "Concevoir son schéma de la salle, puis nommer les appareils")]),
 "seance2": ("Séance 2 — Construire le réseau", [
   (3, "Construire le réseau dans Packet Tracer, étape par étape")]),
 "seance3": ("Séance 3 — Adresser et prouver", [
   (4, "Attribuer une adresse unique à chaque appareil"),
   (5, "Prouver la livraison au ping et provoquer la panne du doublon")]),
}

L["sequence_3e_C5.1-C5.4_sos_station_reparer.html"] = {
 "s1": ("Séance 1 — Localiser la panne", [
   (1, "Lire les symptômes et formuler les causes possibles"),
   (2, "Parcourir l'arbre de diagnostic jusqu'à la conclusion")]),
 "s2": ("Séance 2 — Écrire le protocole", [
   (3, "Rédiger un protocole de dépannage en 3 ou 4 étapes")]),
 "s3": ("Séance 3 — Réparer", [
   (4, "Mener la réparation de la sirène à la clinique")]),
 "s4": ("Séance 4 — Refabriquer et décider", [
   (5, "Passer du plan coté à la pièce refabriquée"),
   (6, "Décider de réparer ou remplacer le ventilateur du CDI")]),
}

L["sequence_4e_C5.1-C5.3_depanner_jardin.html"] = {
 "s1": ("Séance 1 — Du symptôme au protocole", [
   (1, "Construire sa méthode : du symptôme au protocole")]),
 "s2": ("Séance 2 — Remplacer en autonomie", [
   (2, "Remplacer la pièce et apporter les preuves")]),
 "s3": ("Séance 3 — Refabriquer", [
   (3, "Choisir le procédé pour refaire le clip-support"),
   (4, "Réinvestir la méthode sur la lampe du CDI")]),
}

L["sequence_5e_C5.1-C5.3_depanner_lampadaire.html"] = {
 "s1": ("Séance 1 — Inspecter", [
   (1, "Mener l'inspection visuelle du lampadaire n°3")]),
 "s2": ("Séance 2 — Réparer", [
   (2, "Suivre le protocole de réparation, étape par étape")]),
 "s3": ("Séance 3 — Refabriquer", [
   (3, "Visiter l'atelier de fabrication et nommer les procédés"),
   (4, "Réinvestir la méthode sur le vélo du collège")]),
}

L["sequence_3e_C6.1-C6.3_programmer_alerte.html"] = {
 "s1": ("Séance 1 — Lire le programme", [
   (1, "Établir la carte d'identité du programme (données d'entrée et de sortie)"),
   (2, "Tracer l'exécution à la main")]),
 "s2": ("Séance 2 — Modifier", [
   (3, "Modifier un paramètre et en mesurer l'effet"),
   (4, "Programmer la nouvelle fonctionnalité : le gyrophare gradué")]),
 "s3": ("Séance 3 — Tester", [
   (5, "Dérouler le plan de tests et vérifier la non-régression"),
   (6, "Refaire la démarche seul·e sur le programme de la bouée")]),
}

L["sequence_4e_C6.1-C6.3_ajuster_programme_jardin.html"] = {
 "s1": ("Séance 1 — Lire et déduire", [
   (1, "Lire les relevés et y repérer le défaut"),
   (5, "Tracer l'algorigramme de la correction"),
   (2, "Déduire les deux seuils et la plage horaire")]),
 "s2": ("Séance 2 — Tester et réinvestir", [
   (3, "Éprouver la correction sur les quatre scénarios du banc de test"),
   (4, "Réinvestir sur le lampadaire qui clignote au crépuscule")]),
}

L["sequence_5e_C6.1-C6.3_programmer_lampadaire.html"] = {
 "s1": ("Séance 1 — Lire le programme", [
   (1, "Établir la carte d'identité du programme")]),
 "s2": ("Séance 2 — Traduire en algorithme", [
   (5, "Reconnaître les formes de l'algorigramme"),
   (2, "Écrire l'algorithme en langage naturel")]),
 "s3": ("Séance 3 — Régler et réinvestir", [
   (3, "Régler les paramètres au simulateur et observer l'effet"),
   (4, "Réinvestir sur l'arrosage du jardin pédagogique")]),
}
