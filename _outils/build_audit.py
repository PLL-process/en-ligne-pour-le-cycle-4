# -*- coding: utf-8 -*-
"""
build_audit.py — Génère la matrice de couverture pédagogique des 114 codes.

Produit à la racine du dépôt :
  - audit_couverture.csv
  - audit_couverture.json

Sources :
  - _outils/data_competences.py  (référentiel C1-C9 × 3 niveaux, issu du classeur
    Référentiel_Technologie_Cycle4_2024.xlsx de Pascal — le classeur lui-même
    n'est PAS dans le dépôt, voir AUDIT_COUVERTURE_PEDAGOGIQUE.md §1.3)
  - le contenu réel des dossiers de codes (fichiers hors .gitkeep)
  - un dictionnaire d'observations qualitatives (OVERLAY) rempli lors de
    l'audit manuel de juillet 2026.

Usage : python3 _outils/build_audit.py
"""
import csv
import json
import os
import sys

# Import du référentiel embarqué dans le dépôt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_competences import COMP_BY_LEVEL, C_PARENT, THEME_TITLES  # noqa: E402
from controle_statut import verdict as controle_verdict  # noqa: E402

# NB : on NE réimporte PAS make_index (son import exécute la génération de
# l'index — effet de bord indésirable pendant un simple audit). Les fonctions
# de chemin sont recopiées à l'identique ci-dessous.
import re
import unicodedata

THEME_SLUG = {
    1: "theme-1-objets-systemes-usages-interactions",
    2: "theme-2-structure-fonctionnement-comportement",
    3: "theme-3-creation-conception-realisation-innovations",
}


def slugify(s, maxlen=45):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    parts, out, total = s.split("-"), [], 0
    for p in parts:
        if total + len(p) + 1 > maxlen and out:
            break
        out.append(p)
        total += len(p) + 1
    return "-".join(out)


def code_dir(cnum, niveau, code):
    text, _, theme = C_PARENT[cnum]
    return os.path.join(THEME_SLUG[theme], f"{cnum}-{slugify(text)}", niveau, f"{niveau}_{code}")

RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# ---------------------------------------------------------------------------
# Observations qualitatives issues de l'audit manuel (juillet 2026).
# Chaque clé = code préfixé. Les codes absents de ce dictionnaire et sans
# fichier réel reçoivent automatiquement le statut "À CRÉER".
# ---------------------------------------------------------------------------
OVERLAY = {
    "3e_C8.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le mât de la station — la simulation avant le banc » (Fable, 31/08/2026) — "
                "séquence 3 séances, simulateur à trois réglages (hauteur × cas de charge × "
                "limite), QCM 30 q (20 sur le code, 10 sur 3e_C3.4), 2 synthèses, fiche, matrice, "
                "lexique, modèle `mat_station.py` et suite de 62 + 32 tests exécutés et verts. "
                "Les DOUZE réglages possibles sont vérifiés un par un contre le modèle Python. "
                "Découverte centrale : le banc appliquait 200 N·m à tous, le vent en applique de "
                "128 à 298 selon la largeur et la forme de la section.",
        anomalies="La vitesse du vent n'est pas réglable dans le simulateur : c'est délibéré, et "
                  "c'est l'objet du réinvestissement (savoir ce qu'un outil ne permet pas). "
                  "Encastrement supposé parfait ; fatigue hors modèle — l'angle mort est nommé "
                  "dans la séquence, la synthèse et le QCM.",
        accessibilite="Vérifiée : labels sur les trois menus, title/desc sur le SVG du mât, "
                      "verdicts écrits en toutes lettres, hors ligne intégral.",
        medias="1 SVG original CC0 écrit pour le lot — le mât qui se courbe et les flèches de "
               "charge, réparties ou ponctuelles selon le cas choisi.",
    ),
    "5e_C8.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « La patère du hall — ce que la simulation voyait » (Fable, 31/08/2026) — "
                "séquence 2 séances avec simulateur intégré hors ligne, QCM 30 q (20 sur le code, "
                "10 sur 5e_C3.1), 2 synthèses, fiche, matrice, lexique, modèle de calcul "
                "`patere.py` et suite de 39 + 32 tests exécutés et verts. Le modèle reproduit "
                "EXACTEMENT les cinq charges de rupture relevées au banc de 5e_C8.2 (41, 51, 53, "
                "194, 408 kg), puis change de question et compare à la limite élastique : un seul "
                "matériau change de camp, le bois (3,4 sur la rupture, 2,1 sur l'élastique).",
        anomalies="Aucune manipulation d'objet réel sur le parcours 🅱 : le geste sur la matière "
                  "est celui de 5e_C8.2, dont ce lot est la suite. Fatigue et vieillissement hors "
                  "modèle — déclaré à l'élève dans la synthèse, pas tu.",
        accessibilite="Vérifiée : labels sur tous les champs, title/desc sur le SVG du crochet, "
                      "signalement non chromatique (mots « retenu »/« écarté »), hors ligne intégral.",
        medias="1 SVG original CC0 écrit pour le lot — le crochet vu de côté, avec la contrainte "
               "peinte en dégradé et sa valeur en clair.",
    ),
    "5e_C1.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Chengdu : le collège qui mesure son air » (Fable, 08/08/2026) — "
                "séquence 5 séances portant les SIX codes du C1, QCM 30 q dont 13 "
                "illustrées, 2 synthèses, fiche, matrice, 3 jeux de données simulés "
                "déterministes, 4 schémas CC0 dont 2 corrigés, suite de 43 tests "
                "exécutés et verts. Deux chemins d'accès à l'activité tableur "
                "(règle n°59). L'état antérieur est archivé avec le relevé de ce qui "
                "en a été repris.",
        anomalies="Aucune manipulation d'un objet réel (règle n°58) — geste manquant "
                  "identifié et déclaré dans la fiche, la synthèse professeur et le "
                  "README. La donnée est traitée, jamais produite.",
        accessibilite="Vérifiée : étiquettes, alternatives, signalement non chromatique, "
                      "title/desc sur les 4 SVG, hors ligne intégral.",
        medias="4 SVG originaux CC0 écrits pour le lot, title/desc de 1 360 à 1 509 car.",
    ),
    "5e_C1.2": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        pointeur_second_parcours="Le lot Chengdu (5e_C1.1) couvre aussi ce code, par une autre "
                                 "entrée : trois principes de MESURE, sans objet à manipuler. Voir "
                                 "le tableau comparatif du README de 5e_C1.2.",
        qualite="Lot « Sainte-Luce : quel frein pour les vélos du collège ? » (Fable, 09/08/2026), "
                "REFONTE au gabarit — 3 séances, QCM 30 q dont 8 illustrées, 2 synthèses, fiche, "
                "matrice, 2 jeux de données simulés et cohérents entre eux, 2 corrigés graphiques "
                "CC0, suite de 36 tests exécutés et verts. PREMIER LOT DU DÉPÔT à placer une "
                "manipulation d'objet réel au parcours obligatoire (règle n°58) : un vélo, cinq "
                "minutes, trois versions A/B/C validées par le même vérificateur.",
        anomalies="Les quinze mesures sont fournies, non relevées par les élèves. Le prix d'achat "
                  "est volontairement absent. L'état antérieur — page sans aucun champ de saisie "
                  "annonçant trois « productions attendues », et définition de la fonction "
                  "technique confondue avec la fonction d'usage — est archivé avec le relevé de "
                  "ce qui en a été repris.",
        accessibilite="Vérifiée : étiquettes, alternatives, signalement non chromatique, "
                      "title/desc sur les SVG, hors ligne intégral.",
        medias="2 SVG originaux CC0 écrits pour le lot (1 315 et 1 694 car. de description), "
               "2 SVG hérités conservés. Aucune photographie, aucune capture d'écran.",
    ),
    "5e_C1.3": dict(
        pointeur_second_parcours="Le lot Chengdu (5e_C1.1) couvre aussi ce code, par une autre entrée. Les deux ressources coexistent : voir le tableau comparatif du README de 5e_C1.1. La ressource décrite ci-dessus n'est pas modifiée.",
        statut="EXISTANT À AMÉLIORER",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence SI/gestion de données complète (couvre aussi 5e_C1.4) + QCM 24 q.",
        anomalies="8 images PNG de 1,1 à 1,9 Mo chacune (≈ 9,3 Mo au total) à compresser "
                  "(WebP/redimensionnement) ; pas de différenciation ; provenance/licence "
                  "des 8 images extraites non documentée (pas de SOURCES_MEDIAS.md).",
        accessibilite="À vérifier (textes alternatifs des 8 images).",
        medias="8 PNG extraits de l'ancien HTML base64 — origine à documenter.",
    ),
    "5e_C1.4": dict(
        pointeur_second_parcours="Le lot Chengdu (5e_C1.1) couvre aussi ce code, par une autre entrée. Les deux ressources coexistent : voir le tableau comparatif du README de 5e_C1.1. La ressource décrite ci-dessus n'est pas modifiée.",
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="5e_C1.3",
        qualite="README pointeur propre vers 5e_C1.3 (mutualisation justifiée : même "
                "support « SI / gestion de données »).",
        anomalies="Aucune.",
        accessibilite="s.o.",
        medias="s.o.",
    ),
    "5e_C1.5": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le compte du club » (5e_C1.5 + 5e_C1.6) : 3 seances de 55 min pour "
                "140 min d'activites, BANC DE PUBLICATION original integre a la page. On coche "
                "les elements d'une publication, et le banc affiche DEUX compteurs qui bougent "
                "separement : les indices qui menent encore a une personne reelle, et les regles "
                "enfreintes. Il rend visibles deux choses qu'aucun cours ne rend evidentes — "
                "une autorisation rend LICITE et ne rend pas ANONYME (le compteur d'indices ne "
                "bouge pas d'un seul), et ce n'est pas un element qui identifie mais leur "
                "COMBINAISON (retirer le visage fait passer de 7 indices a 6). La charniere "
                "entre les deux codes est l'activite 3 : un compte partage ne rend pas seulement "
                "le compte moins sur, il rend la responsabilite INDECIDABLE — et ce qui empeche "
                "d'attribuer une faute empeche aussi de s'en defendre. Sept verrous "
                "experientiels. QCM 30 q / 90 refutations (C1.5 x15, C1.6 x15), lexique 30 "
                "notions, deux syntheses, fiche, matrice de 30 notions engendree depuis la "
                "banque, tests reels 38/38 et 32/32, scripts livres.",
        anomalies="Aucune publication reelle : le banc simule avec des personnes inventees, et "
                  "la version A le fait avec le compte du college. Le droit est presente, pas "
                  "enseigne : droit a l'image, donnees personnelles et licences sont donnes au "
                  "niveau utile a une decision d'eleve. Le verificateur du reinvestissement "
                  "compte des caracteres, et la page le dit. La cyberviolence est abordee par un "
                  "cas, pas traitee : un eleve concerne a besoin d'un adulte, et la page donne "
                  "le 3018. Les deux pointeurs qui renvoyaient ces codes vers 4e_C1.4 sont "
                  "archives (la 5e vient avant la 4e ; le pointeur ecartait la propriete "
                  "intellectuelle que l'intitule de C1.5 nomme ; C1.6 n'etait pas couvert). "
                  "A noter : le QCM du lot Chengdu (5e_C1.1) porte deja 5 questions codees C1.5 "
                  "et 4 codees C1.6 ; les deux ressources coexistent, ce lot-ci est la seance, "
                  "celui-la un rappel dans un autre parcours.",
        accessibilite="Cases a cocher, listes deroulantes, corrections depliables, version C "
                      "entierement debranchee (affiche A3 et etiquettes qu'on decolle). AUCUNE "
                      "donnee reelle n'entre dans la page : personnes inventees, aucun champ "
                      "nom/photo/mot de passe, rien n'est envoye. Consigne explicite de ne "
                      "jamais taper un vrai mot de passe dans un exercice, et numero 3018 "
                      "indique. Aucune boite modale (regle n°188).",
        medias="Banc de publication original (HTML + JS, CC0). Aucun media tiers.",
    ),
    "5e_C1.6": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="5e_C1.5",
        qualite="README pointeur vers le lot « Le compte du club », range en 5e_C1.5. La "
                "mutualisation n'est pas de politesse : la moitie des activites (0, 1, 4 et "
                "REFAIRE) et 15 des 30 questions du QCM portent sur ce code. Les deux codes sont "
                "ensemble parce que la responsabilite suppose qu'on puisse dire QUI a agi — ce "
                "qu'un compte partage rend impossible.",
        anomalies="Aucune. Le pointeur qui renvoyait ce code vers 4e_C1.4 est archive le "
                  "30/08/2026.",
        accessibilite="s.o. (README pointeur).",
        medias="s.o.",
    ),
    "3e_C1.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Tsinghua : robots, drones et IA face aux feux » (Fable, 09/08/2026), "
                "REFONTE — 5 séances portant 3e_C1.1 à C1.4, QCM 30 q dont 11 illustrées, "
                "2 synthèses, fiche, matrice, 3 corrigés graphiques CC0, suite de 41 tests "
                "exécutés et verts. Données réelles et sourcées (Intérieur, JRC/EFFIS, ADEME, "
                "PNUE). La version antérieure annonçait 4 codes et n'en servait qu'un : elle est "
                "archivée, son contenu intégralement repris comme base factuelle.",
        anomalies="Aucune.",
        accessibilite="Étiquettes, alternatives textuelles longues sur les 3 SVG, signalement non "
                      "chromatique, mode essentiel, 7 versions étayées.",
        medias="3 SVG originaux CC0 produits pour ce lot.",
    ),
    # ── C8 : trois codes déclarés « À CRÉER » alors que le travail existe ────────
    # Mesure du 29/08/2026. Les dossiers 4e_C8.2, 4e_C8.3 et 5e_C8.3 sont vides, donc
    # l'audit les classait « À CRÉER ». Mais les séquences qui les portent le disent
    # elles-mêmes, dans leur tableau « Ce que dit le programme — recopié, pas
    # reformulé » : c'est le dossier qui était vide, pas le travail.
    # (Même défaut que 4e_C4.2 / 4e_C4.4 avec le Book Train — règle n°196.)
    "4e_C8.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C8.1",
        qualite="Porté par « Jardin connecté — valider une solution » (4e_C8.1), activités 1 "
                "et 2 : l'élève remet en ordre le raisonnement de validation (attendu écrit "
                "AVANT l'essai, exécution, comparaison, boucle de retest), puis juge la "
                "conformité des quatre tests et propose le test discriminant qui départagerait "
                "deux causes. Le tableau « Ce que dit le programme » de la séquence l'annonce "
                "explicitement.",
        anomalies="Aucune. Le dossier 4e_C8.2 reste un squelette, ce qui est normal pour un "
                  "code mutualisé — mais il gagnerait un README pointeur (règle n°205).",
        accessibilite="s.o.", medias="s.o.",
    ),
    "4e_C8.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C8.1",
        qualite="Porté par « Jardin connecté — valider une solution » (4e_C8.1), activités 2 "
                "et 3 et le réinvestissement : chaque amélioration proposée doit être "
                "rattachée à un résultat d'essai précis — « une amélioration qui ne cite aucun "
                "résultat d'essai est une idée, pas une correction » — et l'élève doit dire "
                "quels essais rejouer après modification.",
        anomalies="Aucune. Dossier squelette, README pointeur à écrire.",
        accessibilite="s.o.", medias="s.o.",
    ),
    "5e_C8.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="5e_C7.1",
        qualite="Porté par le mini-projet d'objet de 5e (5e_C7.1) : vérifier le comportement "
                "d'un objet en suivant un protocole fourni. Le README de 5e_C8.1 documente "
                "déjà cette mutualisation pour le code voisin.",
        anomalies="Aucune. Dossier squelette, README pointeur à écrire.",
        accessibilite="s.o.", medias="s.o.",
    ),
    "3e_C1.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C1.1",
        qualite="Travaillé en séance 1 du lot Tsinghua 3e : la découverte de l'infrarouge par "
                "Herschel en 1800, et les deux siècles qui la séparent du drone thermique. "
                "7 questions au QCM.",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "3e_C1.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C1.1",
        qualite="Travaillé en séance 5 du lot Tsinghua 3e : argumentaire court sur l'incidence de "
                "l'objet technique sur la société, appuyé sur les faits des séances 2 à 4. "
                "8 questions au QCM.",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "3e_C1.4": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C1.1",
        qualite="Travaillé en séances 4 et 5 du lot Tsinghua 3e : l'incommensurabilité de "
                "certaines grandeurs, puis l'argumentaire sur l'incidence des contraintes "
                "sociétales — trois natures exigées (règle, moyen, attente), chacune avec son "
                "effet concret sur l'objet. 7 questions au QCM.",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "4e_C1.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Tsinghua : concevoir avant de connecter » (Fable, 09/08/2026), REFONTE — "
                "4 séances portant 4e_C1.1 à C1.3, QCM 30 q dont 6 illustrées, 2 synthèses, fiche, "
                "matrice, 2 corrigés graphiques CC0, suite de 42 tests exécutés et verts. SEUL LOT "
                "DU DÉPÔT bâti sur des données réelles et sourcées (ministère de l'Intérieur, "
                "JRC/EFFIS, ADEME). Mesure de température au parcours obligatoire (règle n°58).",
        anomalies="Aucune donnée n'est produite par les élèves sauf la température. Les chiffres "
                  "sont datés de juillet 2026 et vieilliront — c'est déclaré, et posé comme un "
                  "prolongement possible plutôt que comme un défaut.",
        accessibilite="Vérifiée : étiquettes, alternatives, signalement non chromatique, "
                      "title/desc sur les SVG, hors ligne intégral.",
        medias="2 SVG originaux CC0 (1 874 et 1 529 car. de description). Aucune photographie.",
    ),
    "4e_C1.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C1.1",
        qualite="Travaillé en séance 3 du lot Tsinghua : quatre équivalences et leurs périmètres, "
                "puis les deux faces d'une évolution technique. 9 questions au QCM.",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "4e_C1.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C1.1",
        qualite="Travaillé en séance 4 du lot Tsinghua : cinq exigences vérifiables, sans nommer "
                "aucun composant, et la garde humaine comme exigence. 9 questions au QCM.",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "4e_C1.4": dict(
        statut="EXISTANT À AMÉLIORER",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=None, problematique=True,
        qualite="Séquence cybersécurité V16 (PWA, accessibilité, tests intégrés, 120 Ko) "
                "+ activité bonus 2FA + QCM 24 q + README de traçabilité soigné.",
        anomalies="L'activité bonus référence images/tab_key.png et "
                  "images/indentation_error.png : le premier est en fait dans "
                  "_ressources-communes/Images/Ressources transversales/"
                  "touche-tabulation.png, le second n'existe nulle part dans le "
                  "dépôt (lien cassé) ; pas de grille LSU ni de différenciation "
                  "formalisées ; pas de version professeur/inspection séparée.",
        accessibilite="Bonne (V16 annoncée accessible) — à contre-vérifier au clavier.",
        medias="Illustrations majoritairement inline ; sources non consignées.",
    ),
    "3e_C1.5": dict(
        statut="EXISTANT À AMÉLIORER",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence « Numérique, société, économie, environnement, santé » + QCM 24 q.",
        anomalies="Lien PDF cassé au format DOS 8.3 (DELAGR~1.PDF) — le fichier visé est "
                  "_ressources-communes/Ressources pédagogiques/Programme 2024/"
                  "affiche-ecologie-numerique-delagrave.pdf ; "
                  "cette affiche est un document éditeur (Delagrave) : licence de "
                  "rediffusion À VÉRIFIER ; pas de différenciation.",
        accessibilite="À vérifier.",
        medias="Affiche Delagrave : droit de rediffusion non établi.",
    ),
    "3e_C2.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Pékin — trois destinataires, trois représentations » (08/08/2026) : "
                "3 séances de 55 min, 4 activités + billet sans note, 40 observations, 8 verbatims "
                "et 3 incidents simulés, 4 SVG originaux dont DEUX corrigés, QCM de 30 questions "
                "dont 5 illustrées, 2 synthèses, fiche, matrice de 33 notions, 54 tests Playwright "
                "tous passés. TROISIÈME ET DERNIER LOT DU C2 : la compétence est désormais "
                "couverte sur les trois niveaux, et la marche complète est écrite À L'ÉLÈVE.",
        anomalies="Aucune : 8 règles mécanisables au vert. AMBIGUÏTÉ DU RÉFÉRENTIEL DÉCLARÉE : "
                  "« à l'aide de modes de représentation CHOISIS » ne dit pas par qui. La séquence "
                  "retient « par l'élève » et le dit comme une lecture, à l'élève comme au "
                  "professeur (règle n°42, troisième volet). Les six modes étant tous traités et "
                  "tous corrigés, la séquence fonctionne dans les deux lectures : la fiche décrit "
                  "la variante où l'enseignant impose le mode et garde la justification. "
                  "Données simulées annoncées comme telles, effectifs d'abandon fixés et non "
                  "tirés au sort.",
        accessibilite="Champs étiquetés, alternatives longues sur les quatre figures, 8 versions "
                      "étayées pour 8 productions écrites, infobulle sur chaque badge et chaque "
                      "bouton PLUS une légende en clair, vocabulaire des six modes travaillé avant "
                      "tout choix, aucune ressource distante (n°40). Non vérifiés donc non "
                      "déclarés conformes : impression A4, lecteur d'écran, zoom 200 %, mobile.",
        medias="4 SVG originaux CC0, dont DEUX corrigés présents seulement dans les corrections "
               "repliées : la séquence offre six modes de représentation, il fallait six corrigés "
               "(règle n°43 précisée le jour même — un choix offert engage un corrigé par option).",
    ),
    # ── Lot Thème 1 (Fable) : îlot 5e_C2 « Shenzhen, la station de vélos » ──
    "5e_C2.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Shenzhen — la station de vélos et tout ce qui l'entoure » (08/08/2026) : "
                "3 séances de 55 min, 3 activités + billet sans note + bilan, 2 SVG originaux "
                "lus comme des documents, QCM de 30 questions dont 4 illustrées, 2 synthèses, "
                "fiche, matrice de 25 notions, 45 tests Playwright tous passés. PREMIER LOT DU "
                "C2. Achève une séquence héritée qui n'était qu'un plan rédigé en HTML (7,4 ko) "
                "et RÉPARE un lien cassé connu du Thème 1 : la page pointait vers un QCM absent.",
        anomalies="CORRIGÉ EN v1.1 : la v1.0 nommait « esthétique » le troisième domaine de "
                  "conception, alors que le référentiel dit « ou en lien avec des objectifs de "
                  "développement durable ». Une dimension du programme avait été remplacée par une "
                  "dimension inventée, et enseignée comme canonique dans le QCM. Corrigé partout ; "
                  "l'esthétique reste nommée comme une vraie question de conception sans être "
                  "comptée comme l'un des trois domaines. — 7 règles mécanisables au vert. "
                  "FRONTIÈRE DE NIVEAU à tenir : "
                  "« décrire l'expérience de l'utilisateur » relève de la 4e, pas de la 5e. "
                  "Ici l'élève recense et repère ; c'est écrit à l'élève dans la carte du "
                  "référentiel, à la fiche, à la synthèse professeur, et le QCM y consacre sa "
                  "dernière question. Le relevé de l'activité 2 exige qu'au moins un des quatre "
                  "choix relève du développement durable. Données de la station simulées et annoncées comme telles "
                  "(règle n°27). Le fichier hérité solutions_station_shenzhen_simulees.csv "
                  "n'est pas utilisé : il évalue des variantes selon des critères, geste de la "
                  "compétence C3 — c'est dit au SOURCES_MEDIAS plutôt que masqué.",
        accessibilite="Champs étiquetés, alternatives longues sur les deux figures, 7 versions "
                      "étayées pour 7 productions écrites, mode essentiel, bandeau de tâches, "
                      "aucune ressource distante (n°40). Non vérifiés donc non déclarés "
                      "conformes : impression A4, lecteur d'écran, zoom 200 %, mobile réel.",
        medias="2 SVG originaux CC0 écrits pour ce dépôt. Aucune photographie de station "
               "réelle : elle donnerait les réponses de l'activité 1.",
    ),
    "5e_C2.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Traité par la séquence Shenzhen du dossier 5e_C2.1 (séances 2 et 3 — retrouver "
                "la décision derrière une forme, puis comparer deux stations et transposer). Les "
                "trois domaines travaillés sont ceux du référentiel : ergonomie, sécurité, "
                "développement durable. "
                "15 des 30 questions du QCM lui sont consacrées.",
        anomalies="Voir 5e_C2.1 : dossier principal du lot.",
    ),
    "4e_C2.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Hangzhou — ce que vit l'usager devant la borne » (08/08/2026) : 3 séances "
                "de 55 min, 4 activités + billet sans note, 12 verbatims et 150 relevés simulés, "
                "3 SVG originaux, QCM de 30 questions dont 5 illustrées, 2 synthèses, fiche, "
                "matrice de 31 notions, 60 tests Playwright tous passés. Le déroulé est dicté par "
                "le référentiel : 4e_C2.1 impose d'aller du langage naturel aux schémas, "
                "graphiques et algorithmes — la séquence fait parcourir ce trajet, elle ne le "
                "décrit pas.",
        anomalies="Aucune : 8 règles mécanisables au vert. PREMIÈRE APPLICATION des règles n°43 "
                  "étendue (le Bonus a son corrigé), n°44 (aucun sigle ni bouton nu) et n°45 "
                  "(l'entraînement s'ouvre sur ce qui a été fait). Le QCM hérité "
                  "qcm_fonctionnement_objet.html (25 questions, autre auteur) n'a pas été "
                  "modifié : il est référencé comme ressource complémentaire, avec sa portée "
                  "dite — il déborde sur les codes C9. Données simulées annoncées comme telles.",
        accessibilite="Champs étiquetés, alternatives longues sur les trois figures, 8 versions "
                      "étayées pour 8 productions écrites, infobulle sur chaque badge et chaque "
                      "bouton PLUS une légende en clair (une infobulle ne s'ouvre pas au doigt), "
                      "aucune ressource distante (n°40). Non vérifiés donc non déclarés "
                      "conformes : impression A4, lecteur d'écran, zoom 200 %, mobile réel.",
        medias="3 SVG originaux CC0. Le troisième est un CORRIGÉ, présent seulement dans la "
               "correction repliée de l'activité 2 : le graphique est ce que l'élève doit "
               "produire, mais celui qui travaille seul doit pouvoir se corriger (n°43).",
    ),
    "4e_C2.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Traité par la séquence Hangzhou du dossier 4e_C2.1 (séance 3 — écrire quatre "
                "exigences couvrant au moins trois des six familles du programme, chacune "
                "rattachée à un verbatim). 15 des 30 questions du QCM lui sont consacrées.",
        anomalies="Voir 4e_C2.1 : dossier principal du lot.",
    ),
    # ── LOT 09 (Fable) : îlot 4e_C4 « Le jardin connecté » ──
    "4e_C4.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence « Le jardin connecté » (4 séances) couvrant l'îlot "
                "4e_C4 entier (9 codes) : chaîne d'énergie et transformations "
                "(C4.1-C4.2), chaîne d'information, données téléversées et "
                "table structurée avec explorateur à verrou (C4.4-C4.6), "
                "réseau/IP fixe et simulateur de dépannage à verrou 3 pannes "
                "(C4.7-C4.9), forme et procédé (C4.3). QCM 30 q (7/10/10/3, "
                "3 illustrées, réponses réparties 7/7/8/8), synthèses, "
                "matrice, 3 SVG CC0, rapport 21/21. Règle n°4 appliquée. "
                "L'ancien QCM « automatisation premium » reste en ressource "
                "complémentaire dans le dossier.",
        anomalies="Aucune sur le lot. L'ancien QCM automatisation conserve son "
                  "gabarit ${q.img} non résolu (consolidation post-Conseil).",
        accessibilite="Clavier, aria/alt, listes déroulantes exclusivement "
                      "(DYS), reduced-motion, impression A4.",
        medias="3 SVG originaux CC0 image-objet — SOURCES_MEDIAS.md complet.",
    ),
    "4e_C4.2": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        mutualise_avec="4e_C4.1",
        qualite="ATELIER DÉDIÉ « Un Book Train pour la Schœlcher » "
                "(4e_C4.1·C4.2·C4.4, dossier 4e_C4.1_book-train) : analyse d'un "
                "système automatisé réel (New York Public Library) au service d'un "
                "projet martiniquais — diagramme fonctionnel, transformations "
                "d'énergie bloc par bloc, chaîne d'information, algorigramme "
                "normalisé construit dans draw.io, export justifié SVG/PNG et "
                "diaporama. QCM 30 q (10/10/10, 4 illustrées, réponses 8/7/8/7), "
                "synthèses élève/professeur, fiche, matrice, 2 SVG CC0 + sources "
                ".drawio modifiables, 32/32 tests. Lot ACHEVÉ le 08/08/2026 : la "
                "séquence existait seule depuis le 05/08, sans QCM ni synthèses. "
                "Aux règles d'or n°23 à n°34 (billet d'entrée sans note, mode "
                "essentiel, durées annoncées, versions étayées, étiquetage complet).",
        anomalies="Aucune. Règle n°30 (tableau de bord des tâches) non applicable "
                  "en l'état : écart assumé et signalé au rapport de tests. "
                  "Complète la séance 1 du Jardin connecté (4e_C4.1).",
        accessibilite="Clavier, tous les champs étiquetés (label ou aria-label), "
                      "SVG avec title/desc, listes déroulantes (DYS), mode essentiel, "
                      "impression A4.",
        medias="2 SVG originaux CC0 + sources .drawio + bibliothèque de formes ; "
               "schéma d'ensemble assumé comme généré par IA puis vérifié et corrigé "
               "par l'enseignant — SOURCES_MEDIAS.md complet.",
    ),
    "4e_C4.4": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        mutualise_avec="4e_C4.1",
        qualite="ATELIER DÉDIÉ « Un Book Train pour la Schœlcher » "
                "(4e_C4.1·C4.2·C4.4, dossier 4e_C4.1_book-train) : chaîne "
                "d'information du système (terminal, capteurs, destination "
                "programmée) puis traduction du traitement en algorigramme "
                "normalisé dans draw.io — 10 q de QCM dédiées, synthèses, fiche, "
                "matrice, 32/32 tests. Complète la séance 2 du Jardin connecté "
                "(4e_C4.1) ; le QCM eCall 40 q existant reste en entraînement "
                "complémentaire (rattachement confirmé le 21/07/2026).",
        anomalies="Aucune.",
        accessibilite="Clavier, tous les champs étiquetés, mode essentiel, "
                      "versions étayées des productions écrites, impression A4.",
        medias="2 SVG originaux CC0 + sources .drawio — SOURCES_MEDIAS.md complet.",
    ),
    "4e_C4.7": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="ATELIER DÉDIÉ « SOS serre » (C4.7·C4.8·C4.9, dossier principal), "
                "REFONTE v2 après audit pédagogique externe (08/08/2026) : "
                "4 séances de 55 min, passeport réseau d'entrée sans note, mode "
                "essentiel, conception du plan d'adressage par l'élève (règle n°22), "
                "adresse fixe passerelle comprise prouvée par le ping vers l'objet "
                "ajouté, clinique du réseau et intervention réelle sur TROIS fichiers "
                ".pkt en panne (adressage, liaison, masque) réellement fabriqués et "
                "vérifiés au ping, validation par simulation, défi sans tutoriel ; "
                "QCM 30 q (10/10/10), 14 SVG CC0 reconstitués de sessions Packet "
                "Tracer 8.2 réelles, 5 fichiers .pkt fournis (départ, maître, "
                "3 pannes), 54/54 tests Playwright ; complète la séance 3 du Jardin "
                "connecté (4e_C4.1) + QCM XXL réseaux conservé en entraînement.",
        anomalies="Héritées du QCM XXL existant : licences des images *_hd.jpg "
                  "non documentées — LICENCE À VÉRIFIER (consolidation "
                  "post-Conseil) ; doc3_schema_parcours.png (2,6 Mo) à trier.",
        accessibilite="Clavier, aria/alt, listes déroulantes exclusivement (DYS), "
                      "reduced-motion (clinique comprise), impression A4.",
        medias="14 SVG originaux CC0 + 5 fichiers .pkt — SOURCES_MEDIAS.md complet.",
    ),
    **{c: dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C4.1",
        qualite=f"README pointeur ({d}).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ) for c, d in {
        "4e_C4.3": "séance 4 : la forme d'une pièce raconte son procédé",
        "4e_C4.5": "séance 2 : transformation des données téléversées",
        "4e_C4.6": "séance 2 : structure de table, explorateur avec verrou",
    }.items()},
    **{c: dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=True, projet=False, synthese=False,
        evaluation=False, correction=True, situation=False, problematique=False,
        mutualise_avec="4e_C4.7",
        qualite=f"README pointeur double : atelier dédié « SOS serre » "
                f"(4e_C4.7, {d}) + séance 3 du Jardin connecté (4e_C4.1).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ) for c, d in {
        "4e_C4.8": "act. 2 et 4 + intervention réelle : banc d'essai, panne « mauvaise rue » et trois fichiers .pkt en panne à diagnostiquer",
        "4e_C4.9": "act. 5 et défi sans tutoriel : simulation fournie complétée, validée et test choisi par l'élève",
    }.items()},
    "4e_C6.2": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="SÉQUENCE MODÈLE « Jardin connecté » : situation déclenchante, "
                "problématique, mission, référentiel/socle/CRCN, 3 séances, simulation "
                "seuil/pompe, synthèse, grille LSU, différenciation, EDD, mode "
                "enseignant + 2 SVG originaux + 3 QCM (jardin connecté 24 q, "
                "algorigrammes domotique V12, éclairage automatique).",
        anomalies="Améliorations souhaitées (sans casser l'existant) : note chiffrée /20 "
                  "avec pondération paramétrable, exports PDF/CSV, sauvegarde locale de "
                  "la séquence, séparation élève/professeur/inspection, SOURCES_MEDIAS.md ; "
                  "les 2 QCM domotique/éclairage relèvent plutôt d'un autre sous-code — "
                  "rattachement à revoir.",
        accessibilite="Bonne base ; navigation clavier des onglets de séances à vérifier.",
        medias="2 SVG originaux (schema_chaines_arrosage, schema_eclairage_automatique).",
    ),
    "3e_C3.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Shenzhen — refroidir un local qui surchauffe » (08/08/2026) : 4 séances "
                "de 55 min, 5 activités + billet sans note, 6 solutions simulées à 15 colonnes, "
                "QCM de 30 questions, 2 synthèses, fiche, matrice de 31 notions, 28 tests "
                "Playwright tous passés. TROISIÈME ET DERNIER LOT DU C3 : la compétence est "
                "désormais couverte sur les onze codes des trois niveaux.",
        anomalies="Aucune : 7 règles mécanisables au vert. CONTRAINTE D'USAGE à respecter : le "
                  "tableau des six solutions ne se distribue pas en séance 1, sinon l'élève lit "
                  "une liste au lieu de l'établir et 3e_C3.1 n'est pas couvert. C'est écrit au "
                  "README, à la fiche et à la synthèse professeur. Données simulées annoncées, "
                  "et addition des effets présentée comme un ordre de grandeur (règle n°27).",
        accessibilite="Champs étiquetés, alternative longue sur la figure, aucun défilement "
                      "horizontal à 1280 ni à 390 px, 9 versions étayées pour 9 productions "
                      "écrites, aucune ressource distante (n°40). Non vérifiés donc non déclarés "
                      "conformes : impression A4, contraste mesuré, lecteur d'écran, zoom 200 %.",
        medias="1 SVG original CC0 — une seule figure, volontairement : la séquence demande de "
               "PRODUIRE la liste, une planche illustrée aurait donné les réponses.",
    ),
    "3e_C3.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Traité par la séquence Shenzhen du dossier 3e_C3.1 (séance 4 — choisir ou composer, et argumenter sur le cycle de vie et les trois piliers).",
        anomalies="Voir 3e_C3.1 : dossier principal du lot.",
    ),
    "3e_C3.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Traité par la séquence Shenzhen du dossier 3e_C3.1 (séance 2 — construire une grille pondérée et la défendre).",
        anomalies="Voir 3e_C3.1 : dossier principal du lot.",
    ),
    "3e_C3.4": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Traité par la séquence Shenzhen du dossier 3e_C3.1 (séance 3 — définir un protocole exécutable par un autre, puis le mettre en œuvre).",
        anomalies="Voir 3e_C3.1 : dossier principal du lot.",
    ),
    "4e_C3.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Hangzhou — quelle flotte de vélos pour la ville ? » (08/08/2026) : "
                "4 séances de 55 min, 5 activités + billet sans note, 4 flottes simulées à "
                "17 colonnes exploitées au tableur, QCM de 30 questions, 2 synthèses, fiche, "
                "matrice de 32 notions, 28 tests Playwright tous passés. Deuxième lot du C3, "
                "après Shanghai en 5e.",
        anomalies="Aucune : 7 règles mécanisables au vert. La marche depuis la 5e est explicite "
                  "et tenue : en 5e le cahier des charges et le protocole sont FOURNIS, en 4e "
                  "l'élève les ÉCRIT et choisit les appareils de mesure. Données simulées "
                  "annoncées comme telles, et bilan carbone présenté comme un ordre de grandeur "
                  "et non une valeur exacte (règle n°27).",
        accessibilite="Champs étiquetés, alternatives longues, aucun défilement horizontal à "
                      "1280 ni à 390 px, 9 versions étayées pour 9 productions écrites. Aucune "
                      "ressource distante (règle n°40). Non vérifiés donc non déclarés conformes : "
                      "impression A4, contraste mesuré, lecteur d'écran réel, zoom 200 %.",
        medias="2 SVG originaux CC0 (du besoin aux caractéristiques ; à chaque grandeur son appareil).",
    ),
    "4e_C3.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Traité par la séquence Hangzhou du dossier 4e_C3.1 (séance 2 — comparer les incidences en les rapportant au service rendu, qualitatif compris).",
        anomalies="Voir 4e_C3.1 : dossier principal du lot.",
    ),
    "4e_C3.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Traité par la séquence Hangzhou du dossier 4e_C3.1 (séance 3 — choisir les appareils de mesure et rédiger un protocole reproductible).",
        anomalies="Voir 4e_C3.1 : dossier principal du lot.",
    ),
    "5e_C3.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Shanghai — quel véhicule pour le dernier kilomètre ? » (08/08/2026) : "
                "4 séances de 55 min, 5 activités + billet d'entrée sans note, données simulées "
                "à 20 colonnes exploitées au tableur, QCM de 30 questions dont 3 illustrées, "
                "2 synthèses, fiche, matrice de 32 notions, 27 tests Playwright tous passés. "
                "Premier lot du C3, compétence qui n'avait aucune ressource sur les trois niveaux. "
                "L'ordre de traitement est C3.1, C3.2, C3.4 puis C3.3 : on ne choisit qu'après "
                "avoir caractérisé, situé dans le cycle de vie et mesuré.",
        anomalies="Aucune : les 7 règles mécanisables sont au vert. Les données du fichier CSV "
                  "sont ENTIÈREMENT SIMULÉES et annoncées comme telles dès la situation "
                  "déclenchante (règle n°27) — aucun véhicule commercialisé n'est décrit.",
        accessibilite="Champs étiquetés, alternatives longues (plus de 120 caractères) sur les "
                      "trois figures, aucun défilement horizontal à 1280 ni à 390 px, versions "
                      "étayées pour les 8 productions écrites. PREMIÈRE SÉQUENCE DU DÉPÔT SANS "
                      "AUCUNE RESSOURCE DISTANTE (règle n°40) : elle fonctionne à l'identique "
                      "derrière un filtrage de collège. Non vérifiés donc non déclarés conformes : "
                      "impression A4, contraste mesuré, lecteur d'écran réel, zoom 200 %.",
        medias="3 SVG originaux CC0 écrits à la main (planche comparative des trois solutions, "
               "cycle de vie avec les étapes influencées, protocole de mesure du freinage).",
    ),
    "5e_C3.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Traité par la séquence Shanghai du dossier 5e_C3.1 (séance 2 — les étapes du cycle de vie influencées par les choix de matériaux et d'énergie).",
        anomalies="Voir 5e_C3.1 : dossier principal du lot.",
    ),
    "5e_C3.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Traité par la séquence Shanghai du dossier 5e_C3.1 (séance 4 — filtrer selon un cahier des charges, puis choisir et argumenter).",
        anomalies="Voir 5e_C3.1 : dossier principal du lot.",
    ),
    "5e_C3.4": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Traité par la séquence Shanghai du dossier 5e_C3.1 (séance 3 — appliquer un protocole fourni et comparer des performances).",
        anomalies="Voir 5e_C3.1 : dossier principal du lot.",
    ),
    "3e_C6.2": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Atelier « L'auto-test de la station » (08/08/2026) : 3 séances de 55 min, "
                "5 activités + billet d'entrée sans note, banc d'essai intégré avec verrou "
                "expérientiel (deux exécutions exigées, dont un cas à plusieurs pannes), "
                "cas limite de la défaillance silencieuse, QCM maison de 30 questions dont "
                "3 illustrées, deux synthèses, fiche, matrice de 32 notions, suite de "
                "22 tests Playwright tous passés. Le libellé est pris au mot : l'élève "
                "ÉCRIT une fonctionnalité nouvelle, il ne lit pas et ne modifie pas.",
        anomalies="Aucune : les 7 règles mécanisables (n°23, 26, 29, 30, 31, 33, 34) sont "
                  "au vert sur la séquence. Le dossier propose en outre un ENTRAÎNEMENT DNB "
                  "réécrit au gabarit maison (30 exercices en 4 manches, 90 réfutations de "
                  "distracteurs, 60 aides, sauvegarde locale, mode essentiel, 21 tests "
                  "Playwright passés). La banque d'origine a été archivée le 08/08/2026 dans "
                  "_archive-anciennes-versions/ : elle reste consultable mais n'est plus "
                  "proposée aux élèves, ses corrections ne réfutant pas les distracteurs.",
        accessibilite="Tous les champs de saisie étiquetés, aucun défilement horizontal à "
                      "1280 px ni à 420 px, focus clavier conservé, réussite jamais "
                      "signalée par la seule couleur. Non vérifiés automatiquement, donc "
                      "non déclarés conformes : impression A4, contraste mesuré, lecteur "
                      "d'écran réel, zoom 200 %.",
        medias="3 SVG originaux CC0 écrits à la main (algorigramme de l'auto-test, planche "
               "des symboles normalisés, trace d'exécution au banc d'essai), avec title et "
               "desc accessibles de 585 à 700 caractères.",
    ),
    # ── Lot 5e_C8.2 « La patère du hall », 29/08/2026 ───────────────────────────
    "5e_C8.2": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « La patère du hall — éprouver un matériau » : 2 séances de 55 min, banc "
                "d'essai de traction ORIGINAL intégré à la page (cinq matériaux, éprouvette "
                "normalisée de 2 x 5 mm, charge par paliers, rupture), deux verrous "
                "expérientiels — le vérificateur de l'activité 2 compare les cinq relevés aux "
                "vraies valeurs du banc, donc un chiffre recopié ou inventé est refusé, ce qui "
                "est le coeur du code : en C8.2 on evalue la mise en oeuvre, pas le nombre. "
                "QCM 30 q / 90 refutations (C8.2 x20, C3.1 x10), lexique 30 notions, deux "
                "syntheses, fiche, matrice, rapport de tests reels 14/14 et 17/17.",
        anomalies="Aucun essai physique : le banc est une simulation, et la page le dit a l'eleve "
                  "(une question du QCM porte precisement la-dessus). La version A renvoie au "
                  "« laboratoire des materiaux » du Reseau National Technologie College "
                  "(eduscol STI, gratuit, sans compte, CC BY-NC-SA 3.0) sans en faire un prerequis.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement sans "
                      "ecran, figure du banc dotee de title et desc.",
        medias="Banc d'essai SVG original (CC0). Aucun media tiers.",
    ),
    # ── Lot 3e_C8.2 « Le mât de la station », 29/08/2026 ────────────────────────
    "3e_C8.2": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le mat de la station — proposer un protocole » : 2 seances de 90 min "
                "pour 160 min d'activites, banc d'essai ORIGINAL integre a la page avec DEUX "
                "sollicitations sur le meme mat (flexion et traction), trois verrous "
                "experientiels. Le pivot du lot est une mesure, pas une affirmation : les cinq "
                "candidats ne se classent pas dans le meme ordre selon l'essai — la barre "
                "pleine acier est 1re en traction (125,7 kN) et 4e en flexion (157 N). L'eleve "
                "applique donc le protocole de 5e, juste et correctement applique, et constate "
                "lui-meme qu'il designe le mauvais mat ; c'est de la qu'il tire la necessite "
                "d'en proposer un autre. Les dix releves de l'activite 3 sont compares aux "
                "vraies valeurs du banc a 0,05 pres : 41 au lieu de 41,1 est refuse. "
                "QCM 30 q / 90 refutations (C8.2 x20, C3.4 x10), lexique 30 notions, deux "
                "syntheses, fiche, matrice de 23 notions, tests reels 32/32 et 26/26, "
                "scripts de test et de calcul livres dans le dossier.",
        anomalies="Aucun essai physique : le banc est une simulation, calculee par "
                  "profils_3e_C8.2.py avec les formules de la poutre encastree et les "
                  "resistances deja utilisees par le banc de 5e — la page le dit a l'eleve a "
                  "trois endroits, dont une question de QCM. Le modele a un domaine : la "
                  "fleche de 723,8 mm du PVC en sort, la page l'ecrit. Le verificateur ne lit "
                  "pas le protocole redige — il compte des lignes — et c'est pour cela qu'une "
                  "grille de relecture croisee en binome (7 criteres) figure dans la page.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement sans "
                      "ecran, figure du banc dotee de title et desc detailles. Les trois "
                      "boites alert() du gabarit herite sont remplacees par un bandeau "
                      "aria-live (regle d'or n°188) — mesure au passage, hors archives : le "
                      "meme defaut subsiste dans 46 QCM sur 51 et 35 sequences sur 46, ce qui "
                      "demande une passe dediee et non un balayage glisse dans un lot.",
        medias="Banc d'essai SVG original (CC0). Aucun media tiers.",
    ),
    # ── Lot C7.4 « L'energie des trois objets », 29/08/2026 ─────────────────────
    "5e_C7.4": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « L'indicateur du hall : de quoi va-t-il vivre » : 2 seances de 55 min pour "
                "95 min d'activites, BANC D'ENERGIE original integre a la page (cinq sources, "
                "consommation calculee ligne par ligne, autonomie). Le pivot de la seance est un "
                "piege verifiable : le panneau solaire suffit SUR LE PAPIER (3,7 Wh recoltes pour "
                "2,85 consommes) et ne marche pas, parce qu'il n'y a pas de soleil dans un hall ; "
                "le REFAIRE deplace le meme objet sur le portail a velos et le panneau redevient "
                "le bon choix, sans qu'un seul chiffre change. Verrou experientiel sur les cinq "
                "sources, cinq releves compares aux vraies valeurs du banc. QCM 30 q / 90 "
                "refutations (C7.4 x20, C3.1 x10), lexique 30 notions, deux syntheses, fiche, "
                "matrice de 16 notions, tests reels 34/34 et 26/26 avec scripts livres.",
        anomalies="Aucune mesure reelle : courants constructeur usuels et capacites du commerce, la version A "
                  "(multimetre en serie) les remplace par des mesures et ce sont elles qui font foi. "
                  "Le banc ignore l'eclairement interieur, ce qui est exactement le ressort de "
                  "l'activite 3. Le vieillissement des piles n'est pas modelise.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement sans ecran, "
                      "encadre de securite TBT (5 V, adaptateur USB scelle jamais ouvert). Les trois "
                      "boites alert() du gabarit de QCM sont remplacees par un bandeau aria-live "
                      "(regle d'or n°188).",
        medias="Banc d'energie original (HTML + JS, CC0). Aucun media tiers.",
    ),
    "4e_C7.4": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « De quoi vit le jardin connecte » : 2 seances de 55 min pour 100 min "
                "d'activites, meme banc d'energie, chaque consommateur pouvant etre ETEINT. Deux "
                "decouvertes portent la seance et l'eleve les fait au banc : la pompe pese 0,4 % "
                "quand la carte pese 92 %, puis comparer les sources finit par obliger a regarder "
                "la CHARGE — avec une carte sobre le besoin tombe de 5,87 a 1,07 Wh et le panneau "
                "qui perdait tout devient le meilleur. Calcul du cout sur la duree : 131 piles 9 V "
                "pour les deux mois d'ete, soit 459 euros. Verrou experientiel exigeant d'avoir "
                "eteint la pompe ET la carte. QCM 30 q / 90 refutations (C7.4 x20, C3.1 x10), "
                "lexique 30 notions, deux syntheses, fiche, matrice de 17 notions, tests reels "
                "35/35 et 26/26 avec scripts livres.",
        anomalies="Aucune mesure reelle. Les 5 mA de la carte sobre sont une hypothese d'etude, et la "
                  "correction dit explicitement qu'une UNO complete ne descend pas sous 30 mA a "
                  "cause de sa DEL d'alimentation et de son composant USB : c'est la carte qu'il "
                  "faudrait changer, pas le programme. Les couts annuels sont des ordres de "
                  "grandeur. La grille ne pondere pas les criteres, volontairement : la "
                  "hierarchisation est le travail de l'activite 3.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement sans ecran, "
                      "encadre de securite (TBT, eau et electricite, boitier en hauteur et fils par "
                      "le dessous). Trois boites alert() du gabarit remplacees par un bandeau "
                      "aria-live.",
        medias="Banc d'energie original (HTML + JS, CC0). Aucun media tiers.",
    ),
    "3e_C7.4": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « La station doit tenir 72 heures sans secteur » : 2 seances de 90 min pour "
                "150 min d'activites, meme banc d'energie. Le reseau tombe au moment precis ou la "
                "station sert : la reponse attendue n'est pas UNE source mais une ARCHITECTURE — "
                "secteur en source normale, trois accus 18650 (28,2 Wh pour 18,12 exiges, 112 h) en "
                "reserve, panneau 2 W en recharge. Deux accus donneraient 18,8 Wh pour 18,12, soit "
                "3,8 % de marge : la page renvoie explicitement au bois qui cassait a 41 kg pour 40 "
                "en 5e_C8.2 et au mat recale pour 1,1 mm en 3e_C8.2 — tout juste n'est pas assez, "
                "trois fois, sur trois objets sans rapport. Le cycle de vie s'argumente avec un "
                "nombre : 787 piles 9 V par an pour une seule station. QCM 30 q / 90 refutations "
                "(C7.4 x20, C3.2 x10), lexique 30 notions, deux syntheses, fiche, matrice de 19 "
                "notions, tests reels 36/36 et 26/26 avec scripts livres.",
        anomalies="Aucune mesure reelle. « Moins d'un dixieme » de recolte solaire sous cyclone est un "
                  "ordre de grandeur, pas un releve, et la page ne le presente pas autrement. Le "
                  "vieillissement des accus est traite en un seul chiffre (environ 20 % apres "
                  "quelques centaines de cycles) alors qu'il depend de la temperature, de la "
                  "profondeur de decharge et du courant. La bascule secteur/accu n'est pas conçue "
                  "ici : le lot dit qu'elle existe et qu'elle se teste, et renvoie au defi bonus.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement sans ecran, "
                      "encadre de securite complet incluant l'emballement thermique des accus "
                      "Li-ion, qui ne sont pas des piles. Trois boites alert() du gabarit remplacees "
                      "par un bandeau aria-live.",
        medias="Banc d'energie original (HTML + JS, CC0). Aucun media tiers.",
    ),
    # ── Statuts remis a jour d'apres ce que les dossiers portent, 31/08/2026 ────
    # Le statut n'est pas calcule, il est DECLARE ici. Trois lots complets etaient
    # restes marques « a verifier » faute d'avoir ete declares ; deux le meritent
    # (leur couverture est demontree), le troisieme non — et c'est dit.
    "4e_C7.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le jardin connecte, conception » : sequence, QCM de 30 questions, fiche, "
                "lexique, deux syntheses, rapport de tests, script de tests livre, et un ATELIER "
                "DE PLANIFICATION des taches. Le lot etait complet sur le disque depuis "
                "longtemps et l'OVERLAY ne l'avait jamais declare : il restait affiche « a "
                "verifier par l'enseignant » alors qu'il porte ses six pieces. Sa MATRICE DE "
                "COUVERTURE relie chaque notion a un code (4e_C7.1, 4e_C7.2, 4e_C7.3), a une "
                "activite, a une production d'eleve et aux numeros de questions du QCM : c'est "
                "cette piece-la qui demontre la couverture, et c'est elle qui autorise le statut.",
        anomalies="Le QCM etiquette ses questions par MOT-CLE THEMATIQUE (ORG, SOL, MAT) et non "
                  "par code de competence : c'est une convention des premiers lots du depot. La "
                  "matrice porte le lien notion → code, et elle seule. Une harmonisation des "
                  "etiquettes rendrait le controle d'echantillonnage utilisable sur ce lot ; elle "
                  "n'est pas faite. Par ailleurs la matrice revendique 4e_C7.3, qui dispose "
                  "depuis le 31/08 de son propre lot (« Le bac du jardin ») : les deux se "
                  "completent, le lot C7.3 evalue le code, celui-ci le mobilise.",
        accessibilite="Corrections depliables, atelier de planification imprimable, syntheses "
                      "eleve et professeur separees. Aucune boite modale (verifie).",
        medias="Voir SOURCES_MEDIAS.md du dossier.",
    ),
    "4e_C7.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C7.1",
        qualite="Couvert par la sequence « Le jardin connecte, conception » du dossier 4e_C7.1. "
                "La PREUVE est dans la matrice de couverture de ce lot, qui porte la ligne : "
                "« Proposition de solutions techniques · 4e_C7.2 · Activite 2 · 2 solutions + "
                "justification · questions 3, 8, 9, 13 ». Le dossier recoit un README engendre "
                "par _outils/pointeurs_codes.py, avec la formulation officielle et un lien "
                "verifie vers la sequence.",
        anomalies="Le dossier ne porte aucune ressource propre, et c'est voulu : le geste est "
                  "travaille dans le lot voisin. Le README precedent disait « Voir le lot 01 dans "
                  "4e_C7.1 » — une reference interne que personne ne pouvait resoudre, et sans "
                  "lien cliquable.",
        accessibilite="README seul, lisible hors ligne, lien verifie sur le disque avant ecriture.",
        medias="Aucun.",
    ),
    "5e_C7.2": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=False, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        mutualise_avec="atelier CAO — TP nº1 bis « Le dé, en mieux »",
        qualite="Lot « Le dé, en mieux » (Fable, 30/08/2026) — TP de réinvestissement de "
                "40 min, QCM 30 questions toutes étiquetées 5e_C7.2, 2 synthèses, fiche, "
                "matrice de 11 groupes, lexique de 30 notions, modèle `calotte.py` et suite "
                "de 31 tests exécutés et verts. Le code n'était évalué NULLE PART, et il "
                "n'était pas vraiment enseigné non plus : le TP nº1 annonçait le geste sans "
                "l'écrire (« une calotte demanderait de soustraire une sphère, et ça, c'est "
                "un geste d'après »). L'élève reprend SON dé, garde la v1 comme témoin, "
                "remplace un creux à fond plat par une calotte creusée à la bille Ø20, "
                "mesure (Ø10,54 contre Ø10) et décide s'il généralise aux 21 points. Toutes "
                "les cotes des pages sont engendrées par le modèle.",
        anomalies="Les gestes Onshape (plan décalé, primitive Sphère en mode Retirer) sont "
                  "décrits d'après la documentation et NON constatés sur poste : à dérouler "
                  "une fois en salle avant de donner le TP. Cinq paliers sur huit n'ont pas "
                  "d'image de résultat (règle n°77) ; seul le dessin de coupe existe, et il "
                  "est original. Aucun parcours hors connexion pour le geste — exception "
                  "assumée à la règle de conception n°5, annoncée en tête du TP.",
        accessibilite="Vérifiée : aucune boîte modale, SVG avec title et desc, corrections "
                      "dépliables, deux synthèses séparées, lexique imprimable, hors ligne "
                      "intégral pour tout ce qui évalue.",
        medias="1 SVG original CC0 engendré par `calotte.py` — la coupe comparée des deux "
               "creux, avec la bille en pointillés et la hauteur de son centre.",
    ),
    "5e_C7.6": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=False, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        mutualise_avec="atelier CAO — TP nº1 « Le dé », mutualisé entre les trois niveaux",
        qualite="Lot « Le dé » (Fable, 30/08/2026) — QCM 30 questions toutes étiquetées "
                "5e_C7.6, 2 synthèses, fiche, matrice de 13 groupes, lexique de 30 notions, "
                "suite de 31 tests exécutés et verts. Le code n'était évalué NULLE PART dans le "
                "dépôt : il l'est maintenant. La séquence est le TP de l'atelier CAO, mutualisé "
                "entre les trois niveaux et non dupliqué ici — d'où le reclassement.",
        # Ce texte disait « en tête des trois TP » : un compte écrit en dur dans un
        # générateur, donc faux dans tous les fichiers qu'il produit le jour où
        # l'atelier en a reçu un quatrième (règles n°256 et n°261). On ne le corrige
        # pas en « quatre », on cesse de compter.
        anomalies="Aucun parcours hors connexion pour le geste de modélisation : Onshape n'a pas "
                  "de mode hors ligne. Exception assumée à la règle de conception n°5 (décision "
                  "du 30/08/2026, option a), désormais annoncée en tête de chaque TP de "
                  "l'atelier. Le QCM, les synthèses et le lexique, eux, fonctionnent hors ligne "
                  "et sans compte. Les images du TP ne sont pas toutes produites (limite "
                  "déclarée de l'atelier).",
        accessibilite="Vérifiée : aucune boîte modale, corrections dépliables, deux synthèses "
                      "séparées, lexique imprimable en noir et blanc, hors ligne intégral.",
        medias="Aucun média propre : le lot n'ajoute aucune image, il accompagne le TP.",
    ),
    "4e_C7.6": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=False, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        mutualise_avec="atelier CAO — TP nº2 « Le dé sur son socle », mutualisé entre les trois niveaux",
        qualite="Lot « Le dé sur son socle » (Fable, 30/08/2026) — QCM 30 questions toutes "
                "étiquetées 4e_C7.6, 2 synthèses, fiche, matrice de 13 groupes, lexique de 30 "
                "notions, suite de 31 tests exécutés et verts. Le code n'était évalué nulle part. "
                "Le partage des questions dit le point de bascule de la 4e : NEUF questions sur "
                "la contrainte (ce qu'elle est, comment on la vérifie, ce qu'elle survit) contre "
                "cinq sur la révolution, qui est pourtant le geste visible du TP.",
        anomalies="Aucun parcours hors connexion pour le geste de modélisation (voir 5e_C7.6). "
                  "Le lot ne dit rien de la TENUE réelle de l'assemblage — que le dé ne bascule "
                  "pas relève de C8 ; l'angle mort est nommé dans la synthèse.",
        accessibilite="Vérifiée : aucune boîte modale, corrections dépliables, deux synthèses "
                      "séparées, lexique imprimable, hors ligne intégral.",
        medias="Aucun média propre.",
    ),
    "3e_C7.6": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=False, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        mutualise_avec="atelier CAO — TP nº4 « Le boîtier étanche », mutualisé entre les trois niveaux",
        qualite="Lot « Le boîtier étanche » (Fable, 30/08/2026) — QCM 30 questions (20 sur "
                "3e_C7.6, 10 sur 3e_C7.2), 2 synthèses, fiche, matrice de 12 groupes, lexique de "
                "30 notions, suite de 32 tests exécutés et verts. Les DEUX codes étaient "
                "évalués nulle part ; ils dépassent maintenant le seuil d'évaluabilité de 5 "
                "questions. Contresens central traité de front : l'eau n'entre pas par la "
                "matière, elle entre par ce qu'on a ouvert exprès.",
        anomalies="Aucun parcours hors connexion pour le geste de modélisation (voir 5e_C7.6). "
                  "Aucun essai d'étanchéité n'est fourni ni chiffré : le lot dit qu'il faut le "
                  "faire, un protocole d'arrosage relèverait de C8.",
        accessibilite="Vérifiée : aucune boîte modale, corrections dépliables, deux synthèses "
                      "séparées, lexique imprimable, hors ligne intégral.",
        medias="Aucun média propre.",
    ),
    "3e_C7.2": dict(
        statut="À VÉRIFIER PAR L’ENSEIGNANT",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=True, correction=True, situation=False, problematique=False,
        qualite="Enseigné par la séquence « Le capteur de confort » de 3e_C7.1, et ÉVALUÉ depuis "
                "le 30/08/2026 par les dix dernières questions du QCM du lot 3e_C7.6 « Le "
                "boîtier étanche » — c'est là que la fabrication a lieu, le boîtier étant la "
                "seule pièce du parcours réellement imprimée. Enseigner et évaluer à deux "
                "endroits différents est permis (règle d'or n°81) ; le taire ne l'est pas, et le "
                "README du dossier le dit maintenant, mesure à l'appui.",
        anomalies="Le dossier ne porte aucune ressource propre : c'est un renvoi. Le statut reste "
                  "« à vérifier par l'enseignant » parce que le report d'un score évalué dans un "
                  "AUTRE lot est une décision d'enseignant, pas une conséquence mécanique.",
        accessibilite="README seul, lisible hors ligne, liens vérifiés sur le disque.",
        medias="Aucun.",
    ),
    "4e_C9.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le jardin connecte se programme » : 3 seances de 55 min, six activites, "
                "editeur embarque, algorigramme, jeu d'essais, et un defaut de CLIGNOTEMENT "
                "corrige par hysteresis. Le lot etait complet sur le disque et l'OVERLAY ne "
                "l'avait jamais declare. Sa banque de QCM est la seule des lots anciens a "
                "etiqueter ses questions par CODE DE COMPETENCE : 10 sur C9.1, 10 sur C9.2, 10 "
                "sur C9.3 — la couverture est demontree dans la banque elle-meme, question par "
                "question. Controle : 30 questions, repartition A/B/C/D 8/7/7/8, 4 options et 3 "
                "refutations partout, 30 notions distinctes, une seule bonne reponse detachee par "
                "sa longueur sur 30, ecart moyen +0,7 caractere, aucune erreur JS, aucune boite "
                "modale.",
        anomalies="L'execution est simulee dans l'editeur embarque : elle prouve la logique, pas "
                  "le montage. Le lot couvre trois codes a lui seul, ce qui est coherent avec la "
                  "sequence — six activites, dont trois consacrees a C9.3 — mais laisse peu de "
                  "place a chacun : 10 questions par code, soit le double du seuil "
                  "d'evaluabilite, sans plus.",
        accessibilite="Corrections depliables, journal chiffre exige par le verificateur (au "
                      "moins trois valeurs relevees, pour empecher le « ca marche » qui ne prouve "
                      "rien). Aucune boite modale.",
        medias="Voir SOURCES_MEDIAS.md du dossier.",
    ),
    "4e_C9.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C9.1",
        qualite="Couvert par la sequence « Le jardin connecte se programme » du dossier 4e_C9.1, "
                "activite 3 : l'algorigramme devient un programme, en blocs puis en Python. La "
                "PREUVE est dans la banque du lot, qui etiquette 10 de ses 30 questions par le "
                "code 4e_C9.2. README engendre, lien verifie.",
        anomalies="Le dossier ne porte aucune ressource propre, et c'est voulu.",
        accessibilite="README seul, lisible hors ligne, lien verifie.",
        medias="Aucun.",
    ),
    "4e_C9.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C9.1",
        qualite="Couvert par la sequence « Le jardin connecte se programme » du dossier 4e_C9.1, "
                "activites 4 a 6 : le jeu d'essais (nominaux, frontieres, exclusions, absurdes), "
                "le clignotement corrige par hysteresis, et le reinvestissement sans modele "
                "fourni. La PREUVE est dans la banque du lot, qui etiquette 10 de ses 30 "
                "questions par le code 4e_C9.3. README engendre, lien verifie.",
        anomalies="Le dossier ne porte aucune ressource propre, et c'est voulu.",
        accessibilite="README seul, lisible hors ligne, lien verifie.",
        medias="Aucun.",
    ),

    # ── 4e_C6.2 : les deux syntheses qui manquaient, 31/08/2026 ─────────────────
    "4e_C6.2": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le jardin connecte s'arrose » : 3 seances de 55 min, editeur embarque, "
                "banc de tests. Le verbe du code est COMPLETER, et le mot qui decide est "
                "FOURNI : le programme existe, il tourne, il lui manque une piece. Le moment qui "
                "porte la seance est le CAS FRONTIERE — l'essai exactement au seuil, le seul qui "
                "distingue < de <=, et celui que personne n'ecrit spontanement. La difficulte la "
                "plus interessante est ailleurs : UN MAUVAIS SEUIL NE CASSE RIEN. Le programme "
                "s'execute, la pompe tourne, et le jardin est mal arrose — defaut de reglage, pas "
                "de code, et il faut un banc de tests pour le voir. QCM 30 q / 90 refutations "
                "dont 16 sur C6.2, lexique, fiche, matrice, rapport de tests. Les DEUX SYNTHESES "
                "manquaient : elles sont ecrites, et engendrees par synthese_4e_C6.2.py livre "
                "dans le dossier — chaque encadre reprend un « a retenir » de la banque de QCM ou "
                "la trace ecrite de la sequence, rien n'y est ajoute.",
        anomalies="Le programme n'est pas ecrit de zero : il est fourni, remis en ordre puis "
                  "complete — ecrire un programme entier releve de 4e_C9.3, et la sequence le dit "
                  "a l'eleve. L'execution est SIMULEE dans l'editeur embarque : elle prouve la "
                  "logique, pas le montage. Le QCM deborde sur quatre autres codes (C4.1 3 q., "
                  "C4.4 5 q., C4.5 4 q., C1.4 2 q.) : sous le seuil d'evaluabilite, ils y sont "
                  "MOBILISES et non mesures — seul 4e_C6.2, avec 16 questions, est evaluable. Le "
                  "choix du seuil n'est pas tranche par la sequence, volontairement : l'eleve "
                  "doit l'argumenter.",
        accessibilite="Corrections depliables, trace ecrite depliable, trois facons de vivre "
                      "l'atelier dont une debranchee, differenciation explicite. Les deux "
                      "syntheses sont imprimables en noir et blanc et lisibles hors ligne. "
                      "Aucune boite modale (verifie par sans_modale.py).",
        medias="Aucun media tiers ajoute par cette livraison.",
    ),

    # ── Lot C7.7 « Choisir les moyens et produire la forme », 31/08/2026 ────────
    "4e_C7.7": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le support du capteur » : 2 seances de 55 min pour 95 min d'activites, "
                "ATELIER DES MOYENS original integre a la page. Il ne classe pas les machines du "
                "meilleur au pire : il dit lesquelles savent produire CETTE forme-la, et CE "
                "QU'ELLES EN FERONT. La phrase du programme est identique en 3e — ce n'est donc "
                "pas elle qui distingue les niveaux, c'est le geste : en 4e la forme est DONNEE "
                "et l'on choisit le moyen. Deux moyens savent produire le support, et aucun des "
                "deux ne rend le dessin : le laser elargit la fente de son trait de coupe "
                "(3,00 mm dessines sortent a 3,20), la fraiseuse arrondit ses extremites au rayon "
                "de sa fraise et le meplat de 20 mm ne trouve plus que 17 mm de droit. On corrige "
                "en dessinant des DEGAGEMENTS D'ANGLE. Puis la quantite decide : a 4 pieces les "
                "deux moyens tiennent dans les 3 h de machine disponibles, a 30 la fraiseuse sort "
                "du delai (6 h 25 contre 1 h 10) tout en restant parfaitement CAPABLE — deux "
                "jauges separees, parce qu'on confond les deux questions. Verrous experientiels "
                "sur l'evaluation et sur le changement de quantite. Toutes les valeurs calculees "
                "par moyens.py. QCM 30 q / 90 refutations (C7.7 x20, C4.3 x10), lexique 30 "
                "notions, deux syntheses, fiche, matrice associee par NOM, tests reels 38/38 et "
                "32/32, scripts livres.",
        anomalies="Les temps sont des ordres de grandeur d'atelier de college, pas des fiches "
                  "constructeur : ce qui doit etre vrai est QUEL MOYEN SAIT FAIRE QUOI, pas la "
                  "seconde pres. Aucune piece n'est reellement produite — la version A lance les "
                  "deux moyens sur une chute et mesure la fente au pied a coulisse, et c'est elle "
                  "qui fait foi. Les 3 h de machine disponibles sont une donnee du scenario, et le "
                  "bonus demande justement d'ou elles viennent. Le cout matiere n'entre pas dans "
                  "le lot : il ne departage pas ici, et l'ajouter aurait brouille la seule "
                  "question posee.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement "
                      "debranchee (cinq fiches cartonnees et le dessin cote au tableau), encadre "
                      "de securite atelier — PVC jamais au laser, piece bridee et AUCUN GANT a la "
                      "fraiseuse — verifie par un test. Aucune boite modale (regle d'or n°188).",
        medias="Atelier des moyens original (HTML + JS, CC0). Aucun media tiers.",
    ),
    "3e_C7.7": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Produire le boitier » : 2 seances de 90 min pour 160 min d'activites. "
                "Meme phrase de programme qu'en 4e, geste tout autre — ici le moyen est CHOISI "
                "DEPUIS LONGTEMPS (3e_C7.3 : PETG imprime au college) et la forme est MODELISEE "
                "(3e_C7.6). Tout est decide, et rien n'est fabricable : trois cotes sur cinq sont "
                "hors du domaine de la buse. Le geste est de faire remonter la contrainte de "
                "fabrication DANS LE DESSIN — et c'est un geste distinct de celui de C7.3, ou l'on "
                "rouvrait le CAHIER DES CHARGES en nommant qui paierait. Ici on n'y touche pas : "
                "ni matiere, ni encombrement, ni etancheite, ni masse admise. PERSONNE NE PAIE, et "
                "c'est ce qui rend ce geste preferable. Trois corrections au pas de la machine : "
                "casquette 70° → 45° (l'angle qu'une buse tient sans support), rainure 0,3 → "
                "0,6 mm (trois couches franches au lieu d'une couche et demie), jeu du couvercle "
                "0,1 → 0,4 mm (sous la tolerance, les deux pieces se soudent). Le piege est "
                "symetrique : DEUX COTES N'ONT BESOIN D'AUCUNE CORRECTION — la paroi de 2,9 mm "
                "calculee en C7.3 et les angles vifs que l'impression fait tres bien — et les "
                "toucher est compte sur une JAUGE A PART (regle d'or n°219). Enfin l'impression "
                "deportee supprime l'iteration : meme temps machine, un delai, UNE SEULE FOURNEE. "
                "QCM 30 q / 90 refutations (C7.7 x20, C8.1 x10), lexique 30 notions, deux "
                "syntheses, fiche, matrice, tests reels 52/52 et 32/32, scripts livres.",
        anomalies="Aucune piece n'est imprimee dans la version B : la version A imprime une "
                  "EPROUVETTE DE COIN — 15 mm de boitier, 8 min — ou les trois defauts se voient a "
                  "l'oeil nu, et c'est elle qui fait foi. Aucune simulation n'est lancee : "
                  "3e_C8.1 est mobilise, pas reenseigne — le lot travaille ce qu'une simulation "
                  "remplace et ce qu'elle IGNORE, notamment l'anisotropie d'une piece imprimee, "
                  "qui cede d'abord entre deux couches. Les valeurs de domaine sont des ordres de "
                  "grandeur (buse 0,4 mm, couche 0,2 mm, tolerance 0,3 mm) : une autre machine "
                  "deplacerait les trois seuils sans changer le raisonnement. Le scenario de "
                  "l'impression deportee est une hypothese de travail tiree d'une decision "
                  "d'etablissement.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement "
                      "debranchee (le dessin cote au tableau et cinq bandes de papier, une par "
                      "cote), encadre de securite atelier — local ventile, capot ferme, LUNETTES "
                      "pour retirer les supports — verifie par un test. Aucune boite modale.",
        medias="Atelier des moyens original (HTML + JS, CC0). Aucun media tiers.",
    ),

    # ── Lot C7.3 « Choisir un materiau », 31/08/2026 ────────────────────────────
    "5e_C7.3": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le banc de la cour » : 2 seances de 55 min pour 95 min d'activites, "
                "BANC DES MATERIAUX original integre a la page — il ne note pas, ne pondere pas "
                "et ne conseille pas : il ELIMINE, et il dit sur quel critere. Six candidats, "
                "cinq exigences, deux retenus. Le geste qui porte la seance est l'activite 2 : "
                "RETIRER une exigence et voir le nombre de retenus changer (regle d'or n°213) — "
                "sans « temperature au soleil », le PVC entre a cent euros de moins, et c'est "
                "exactement le critere qu'on n'a pas le droit de retirer. Deux verrous "
                "experientiels (evaluer, retirer un critere). Toutes les valeurs — masses, couts, "
                "verdicts — sont CALCULEES par materiaux.py, livre dans le dossier : aucun nombre "
                "recopie a la main. QCM 30 q / 90 refutations (C7.3 x20, C4.4 x10), lexique 30 "
                "notions, deux syntheses, fiche, matrice de 30 notions engendree depuis la banque "
                "et associee par NOM et non par position, tests reels 41/41 et 32/32, scripts livres.",
        anomalies="Les valeurs sont des ordres de grandeur d'usage pedagogique, tirees de plages "
                  "courantes en construction — c'est le CLASSEMENT qui doit etre juste, pas la "
                  "troisieme decimale, et la sequence le dit. Aucune mesure n'est faite par "
                  "l'eleve : la version A releve les temperatures au thermometre infrarouge sur "
                  "six chutes de materiau, et ce sont ces releves qui font foi. Le banc ne pondere "
                  "pas et ne note pas — c'est un choix, pas une limite technique. La provenance et "
                  "l'energie de fabrication n'ont pas de colonne : elles sont nommees dans la "
                  "correction de l'activite 3, sans etre chiffrees.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement "
                      "debranchee (six fiches cartonnees et cinq bandes d'exigences qu'on pose ou "
                      "qu'on retire), encadre climat verifie par un test. Aucune boite modale : "
                      "les messages passent par un bandeau aria-live (regle d'or n°188).",
        medias="Banc des materiaux original (HTML + JS, CC0). Aucun media tiers.",
    ),
    "4e_C7.3": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le bac du jardin » : 2 seances de 55 min pour 95 min d'activites, banc des "
                "materiaux muni d'un SELECTEUR DE DUREE. Le verbe du code est COMPARER, et "
                "l'expression a ouvrir est « le plus adapte » — adapte a quoi, et pour combien de "
                "temps. Trois materiaux tiennent le cahier des charges ; a l'achat PP recycle 90 € "
                "< PVC 167 € < teck 309 €, et sur quinze ans PP 271 € < TECK 309 € < PVC 333 € : "
                "le classement se retourne. Sur vingt ans il se retourne une SECONDE fois, le teck "
                "repassant dernier a 619 € parce qu'un deuxieme teck part a la benne avec dix ans "
                "de vie devant lui. Le classement n'appartient pas aux materiaux : il appartient a "
                "la duree qu'on a choisie, et cette duree est une decision qui s'ecrit. Verrou "
                "experientiel sur le changement de duree. QCM 30 q / 90 refutations (C7.3 x20, "
                "C3.2 x10), lexique 30 notions, deux syntheses, fiche, matrice de 30 notions, "
                "tests reels 44/44 et 32/32, scripts livres.",
        anomalies="Tout le raisonnement repose sur les durees de vie annoncees, et le bonus demande "
                  "justement a l'eleve d'ou elles viennent ; la version A les remplace par des "
                  "garanties de fournisseurs reels. Le banc ne compte que la matiere : ni l'energie "
                  "de fabrication, ni les kilometres, ni la pose — c'est ecrit dans la correction "
                  "de l'activite 3. Aucune analyse de cycle de vie complete n'est conduite : "
                  "4e_C3.2 est mobilise sur la comparaison chiffree et sur ce qu'elle laisse de "
                  "cote. Le pilier social du developpement durable est absent du cahier des "
                  "charges, et la sequence le dit plutot que de faire comme s'il y figurait. "
                  "Ce lot REMPLACE le README de deux lignes qui renvoyait a un lot inexistant.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement "
                      "debranchee (une frise de vingt ans au tableau et trois bandes de couleur "
                      "recollees a chaque remplacement), encadre de securite atelier — decoupe "
                      "laser du PVC interdite, sciure de pin autoclave — verifie par un test. "
                      "Aucune boite modale (regle d'or n°188).",
        medias="Banc des materiaux original (HTML + JS, CC0). Aucun media tiers.",
    ),
    "3e_C7.3": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le boitier de la station » : 2 seances de 90 min pour 160 min d'activites. "
                "Le mot du code est CONSTITUTIF, et le lot en tire deux consequences que les deux "
                "niveaux precedents n'avaient pas. (1) L'EPAISSEUR N'EST PAS DONNEE : elle se "
                "deduit du materiau par e = e0 x racine(s0/s), si bien que l'aluminium, presque "
                "deux fois plus dense que le PVC, donne un boitier de 0,557 kg contre 0,545 — "
                "douze grammes. (2) AUCUN des six candidats ne passe le cahier des charges tel "
                "qu'il est ecrit. Zero retenu n'est pas une panne : c'est la situation ordinaire "
                "d'un bureau d'etudes. Trois sorties existent, une par exigence relachee, et "
                "chacune envoie la facture ailleurs — le sel sur l'entretien, la masse sur celui "
                "qui pose en haut d'une echelle, la duree sur celui qui remontera dans cinq ans. "
                "Une contrainte relachee ne disparait pas : elle CHANGE DE PORTEUR. Deux verrous "
                "experientiels (evaluer, obtenir exactement un retenu). QCM 30 q / 90 refutations "
                "(C7.3 x20, C4.2 x10), lexique 30 notions, deux syntheses, fiche, matrice de 30 "
                "notions, tests reels 43/43 et 32/32, scripts livres.",
        anomalies="Aucune eprouvette n'est cassee : la loi en racine carree est admise, pas "
                  "mesuree — la version A imprime trois plaques a 1, 2 et 3 mm et les casse sur le "
                  "banc de flexion de 3e_C8.2. Cette loi est une simplification : paroi plane, "
                  "meme chargement, meme critere de ruine ; elle donne l'ordre de grandeur et le "
                  "bon classement, pas une cote de fabrication. Le lien avec le mat de 3e_C8.2 "
                  "n'est PAS recalcule : le seuil de 1,2 kg vient de la pose a une main, argument "
                  "deja employe dans ce lot-la contre la barre d'acier de 4,93 kg ; verifier "
                  "l'effet d'une tete plus lourde sur le mat resterait a faire, et la sequence le "
                  "dit. Le verificateur ne lit pas la justification de l'activite 3 : il compte "
                  "des caracteres.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement "
                      "debranchee (six fiches, cinq bandes d'exigences, un seul seuil deplacable "
                      "a la fois), encadre de securite atelier — PVC jamais au laser, impression "
                      "en local ventile, metaux perces piece bridee sans gants — verifie par un "
                      "test. Aucune boite modale (regle d'or n°188).",
        medias="Banc des materiaux original (HTML + JS, CC0). Aucun media tiers.",
    ),

    # ── Lot C7.5 « Assembler un prototype », 30/08/2026 ─────────────────────────
    "5e_C7.5": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « L'eclairage du preau » : 2 seances de 55 min pour 95 min d'activites, "
                "ETABLI GROVE original integre a la page — l'eleve place chaque constituant sur "
                "un port et l'etabli ne repond jamais « ca ne marche pas » : il repond POURQUOI, "
                "du plus grossier au plus fin, comme un depanneur. Le mot du code est FOURNIS : "
                "en 5e on ne choisit pas, on place. Le geste qui porte la seance est l'activite 2 "
                "— RETIRER un constituant d'un montage qui marchait et lire les quatre pannes "
                "differentes que cela produit (regle d'or n°213). Le cas le plus instructif est "
                "le capteur sur A1 quand le programme lit A0 : rien ne chauffe, rien ne fume, et "
                "rien ne marche. Cinq verrous experientiels. QCM 30 q / 90 refutations "
                "(C7.5 x20, C4.5 x10), lexique 30 notions, deux syntheses, fiche, matrice de 30 "
                "notions engendree depuis la banque, tests reels 39/39 et 32/32, scripts livres.",
        anomalies="Aucun assemblage reel : l'etabli simule, et la version A le fait avec la carte, "
                  "le Base Shield et deux modules Grove — c'est elle qui fait foi. Le programme "
                  "est donne, charge et lu, jamais modifie : le modifier releve de C6.2. Le "
                  "catalogue est reduit au strict necessaire ; choisir entre plusieurs "
                  "constituants est le travail de la 3e. Le budget de courant est affiche, pas "
                  "travaille — il devient une contrainte en 4e.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement "
                      "debranchee (quatre eleves tiennent les quatre fonctions), encadre de "
                      "securite TBT 5 V verifie par un test. Aucune boite modale : les messages "
                      "passent par un bandeau aria-live (regle d'or n°188).",
        medias="Etabli Grove original (HTML + JS, CC0). Aucun media tiers.",
    ),
    "4e_C7.5": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le jardin qui n'arrose pas encore » : 2 seances de 55 min pour 95 min "
                "d'activites. Trois prototypes livres, chacun incomplet d'une maniere "
                "DIFFERENTE, et chacun empruntant une branche differente du diagnostic : un "
                "constituant qui en exige un autre (la pompe sans relais), un budget de courant "
                "depasse (800 mA sur 500, donc un defaut INTERMITTENT qui ne se voit qu'a la "
                "mise en eau), et une fonction tenue par le mauvais capteur (une temperature "
                "comparee a un seuil d'humidite). Le point de depart n'est pas le montage mais "
                "le cahier des charges : un manque se compare, une panne se teste. QCM 30 q / 90 "
                "refutations (C7.5 x20, C4.4 x10), lexique 30 notions, deux syntheses, fiche, "
                "matrice de 30 notions, tests reels 39/39 et 32/32, scripts livres.",
        anomalies="Aucun montage reel : l'etabli charge les trois cas, et la version A les "
                  "prepare sur trois plateaux. Le programme n'est ni ecrit ni modifie — il est "
                  "correct dans les trois cas, ce qui est justement ce qui rend la recherche du "
                  "manque interessante. Le quatrieme cas du reinvestissement n'a PAS de solution "
                  "unique : deux causes restent possibles, et la correction le dit — le resultat "
                  "attendu est un essai qui tranche, pas une reponse.",
        accessibilite="Listes deroulantes, corrections depliables, version C debranchee (fiches "
                      "cartonnees et liste attendue), encadre de securite TBT avec la regle de "
                      "l'essai a sec avant toute mise en eau. Aucune boite modale (regle n°188).",
        medias="Etabli Grove original (HTML + JS, CC0). Aucun media tiers.",
    ),
    "3e_C7.5": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « La station qu'il faut equiper » : 2 seances de 90 min pour 150 min "
                "d'activites. Le catalogue contient dix constituants pour un cahier des charges "
                "a quatre exigences, et le lot ne porte pas sur le tri mais sur la PROPAGATION : "
                "l'exigence « visible depuis la cour » impose le bandeau de DEL, le bandeau "
                "impose 480 mA, 580 mA au total imposent la batterie, et la batterie remet en "
                "cause l'autonomie de 72 h qui etait tenue. Le bon choix cree le probleme "
                "suivant — c'est ce qu'un exercice de tri ne montre jamais. Quatre retraits "
                "produisent quatre refus de quatre NATURES : une grandeur, un usage, une preuve, "
                "une quantite d'energie. QCM 30 q / 90 refutations (C7.5 x20, C4.3 x10), lexique "
                "30 notions, deux syntheses, fiche, matrice de 30 notions, tests reels 42/42 et "
                "32/32, scripts livres.",
        anomalies="Aucune station reelle : l'etabli simule, la version A utilise le carton "
                  "complet et la contrainte de courant s'y mesure au multimetre. L'autonomie "
                  "n'est pas calculee ici — elle l'a ete en 3e_C7.4 ; ce lot montre seulement "
                  "que le choix du bandeau la remet en cause, et le dit. Le verificateur ne lit "
                  "pas la justification ecrite de l'activite 1 : il compte des caracteres, et la "
                  "correction donne les deux arguments attendus mot pour mot.",
        accessibilite="Listes deroulantes, corrections depliables, version C debranchee (dix "
                      "fiches cartonnees, cahier des charges lu a voix haute, budget calcule au "
                      "tableau), encadre de securite TBT avec l'avertissement thermique du "
                      "bandeau de 480 mA. Le reinvestissement porte sur une exigence "
                      "d'accessibilite. Aucune boite modale (regle n°188).",
        medias="Etabli Grove original (HTML + JS, CC0). Aucun media tiers.",
    ),
    # ── Lot C7.8 « Interfacer », 29/08/2026 ─────────────────────────────────────
    "4e_C7.8": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Le jardin publie sa mesure » : 2 seances de 55 min pour 95 min "
                "d'activites, BANC DE LIAISON original integre a la page — l'eleve compose le "
                "message case par case et le banc lui dit, ligne par ligne, ce que le "
                "destinataire peut ou ne peut pas en faire. L'adressage n'est PAS refait : il "
                "est traite par l'atelier SOS serre (4e_C4.7), et la premiere section de la "
                "sequence le dit. Ce qui se decide ici est du cote de l'objet — ce qu'il envoie, "
                "quand, a qui, et ce qu'il fait quand plus personne n'ecoute. Le geste qui porte "
                "la seance est le bouton COUPER LE LIEN : le champ d'horodatage, coche a "
                "l'activite 1 sans qu'on voie bien pourquoi, trouve sa raison d'etre deux "
                "activites plus tard, quand douze mesures liberees d'un coup seraient toutes "
                "datees de la meme minute. Trois verrous experientiels. QCM 30 q / 90 "
                "refutations (C7.8 x20, C1.4 x10), lexique 30 notions, deux syntheses, fiche, "
                "matrice de 17 notions, tests reels 35/35 et 26/26 avec scripts livres.",
        anomalies="Aucune liaison reelle : le banc simule l'echange, et la version A le fait avec "
                  "deux cartes et le moniteur serie — ce sont alors les trames observees qui font "
                  "foi. Le format JSON est impose par le banc ; le choix d'un format est traite "
                  "en question de QCM et en defi bonus, pas en activite. Le verificateur ne lit "
                  "pas la phrase redigee de l'activite 3 : il compte des caracteres, et la page "
                  "le dit a l'eleve.",
        accessibilite="Listes deroulantes, corrections depliables, version C entierement "
                      "debranchee (deux eleves jouent les deux objets, une feuille pliee fait le "
                      "message), encadre de securite sur les donnees personnelles et les secrets. "
                      "Les trois boites alert() du gabarit de QCM sont remplacees par un bandeau "
                      "aria-live (regle d'or n°188).",
        medias="Banc de liaison original (HTML + JS, CC0). Aucun media tiers.",
    ),
    "3e_C7.8": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Lot « Deux stations qui se parlent » : 2 seances de 90 min pour 150 min "
                "d'activites, meme banc de liaison. Deux objets, et personne pour arbitrer : "
                "tout ce qu'un humain compensait sans y penser doit devenir un champ, une regle "
                "ou un delai. Le ressort de la seance est que la regle de la mairie — la sirene "
                "ne part que si les deux stations sont d'accord — cree aussitot un defaut PIRE "
                "que celui qu'elle corrige : si Sainte-Anne est detruite par le grain qui arrive "
                "sur Le Robert, il n'y a plus d'alerte du tout. Defaillance dangereuse. La bonne "
                "reponse n'est pas un compromis mais un troisieme terme : on declenche ET on "
                "ecrit qu'on etait seule. Regle d'accord a trois morceaux (sur quoi, quelle "
                "tolerance, quel delai), delai de silence justifie (trois periodes d'emission), "
                "et six essais dont la moitie portent sur des pannes. QCM 30 q / 90 refutations "
                "(C7.8 x20, C8.3 x10), lexique 30 notions, deux syntheses, fiche, matrice de 17 "
                "notions, tests reels 34/34 et 26/26 avec scripts livres.",
        anomalies="Aucune liaison reelle : le banc simule. Le routage et l'adressage ne sont ni "
                  "travailles ni evalues ici — ils le sont par 3e_C4.7 et 3e_C4.8, et le lot "
                  "s'appuie dessus sans les refaire. La synchronisation des horloges est laissee "
                  "en defi bonus : la regle de fraicheur suppose deux horloges a peu pres justes, "
                  "le lot le dit et n'entre pas dans le mecanisme. L'accuse de reception n'est "
                  "traite qu'en defi : un lot complet sur la fiabilite de transport serait un "
                  "autre lot.",
        accessibilite="Listes deroulantes, corrections depliables, version C debranchee, encadre "
                      "de securite (aucun secret, aucune donnee personnelle, un secours se teste). "
                      "Trois boites alert() du gabarit remplacees par un bandeau aria-live.",
        medias="Banc de liaison original (HTML + JS, CC0). Aucun media tiers.",
    ),
    "3e_C9.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Atelier « Variables, types et systèmes » (Arc variables, Thème 3 · "
                "New York) : refonte complète de la ressource Vittascience héritée — "
                "4 séances, 5 activités, simulateur de mémoire pas-à-pas (verrou 6 "
                "étapes), motif prédire→tester→reporter sur l'éditeur Vittascience "
                "EMBARQUÉ (3 iframes mode mixte), chasse aux 3 bugs du panneau MTA, "
                "banc de mise au point 4 tests avec cas limite, QCM 30 q (8/8/7/7, "
                "3 illustrées), synthèses, 3 SVG originaux CC0, TP mBot2 conservé "
                "en prolongement 🅰.",
        anomalies="Ancienne ressource archivée (règle n°12) avec stub de redirection "
                  "sur l'URL historique ; qcm_python_variables.html (24 q) hérité "
                  "encore en place — remplacement possible par le QCM 30 q ; l'iframe "
                  "Vittascience exige une connexion (versions 🅲 hors ligne prévues).",
    ),
    # ── Thème 3 · Station d'alerte cyclonique : programmation + recette (Fable, 2026-08-19) ──
    "3e_C9.2": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence « La station d'alerte cyclonique se programme » (objet-fil "
                "3e, commande de la mairie avec exigence de PV de recette) : 4 séances "
                "de 1 h 30, 7 activités, banc d'essai de la station INTÉGRÉ (curseur de "
                "vent, LCD, DEL, buzzer, bouton d'acquittement, chrono, boucle 200 ms) "
                "avec verrous expérientiels sur les activités 3, 4 et 7 ; programmation "
                "ArduBlock par paliers façon « dé de 5e » (image du résultat attendu et "
                "rituel d'enregistrement à chaque palier), acquittement et détection "
                "d'événement (IHM du libellé prise au mot), lecture guidée du C++ généré, "
                "diagnostic sur trace série ; QCM 30 q (15/15, 4 illustrées, 8/7/7/8), "
                "2 synthèses, fiche, matrice 23 notions, 9 SVG originaux CC0, programme "
                "C++ de référence commenté (compilation arduino:avr:uno vérifiée : "
                "6 764 o) + banc Docker enseignant. Suite Playwright de 51 tests, tous "
                "passés, qui SIMULE la séquence comme un élève avec 32 captures d'écran.",
        anomalies="Planches ArduBlock = reconstitutions schématiques étiquetées (pas de "
                  "captures : site DuinoEdu inaccessible le 19/08/2026, version 1.7 à "
                  "revalider en début d'année) ; banc Docker non exécuté en session "
                  "(réservé au poste enseignant). Aucun corrigé sommatif publié.",
        accessibilite="Navigation clavier + skip-link, aria complets, loupe sur toutes "
                      "les images (règle n°92), mode essentiel, étayages 11/11, "
                      "prefers-reduced-motion, mobile 390 px sans défilement horizontal "
                      "(vérifié), impression A4. Non vérifiés automatiquement : "
                      "contraste mesuré, lecteur d'écran réel, zoom 200 %.",
        medias="9 SVG originaux CC0 écrits à la main (title/desc de 504 à 1 188 "
               "caractères) — SOURCES_MEDIAS.md complet.",
    ),
    "3e_C8.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Proposer un protocole de test : séance 4 entière de la séquence "
                "« La station d'alerte cyclonique se programme » (3e_C9.2) — l'élève "
                "RÉDIGE son protocole (act. 6 : nominaux, frontières 99/100/149/150, "
                "performance chronométrée, interaction) puis l'EXÉCUTE au banc et signe "
                "le PV (act. 7, verrous sur les frontières et le chrono). 15 questions "
                "de QCM dédiées. README pointeur en place.",
        anomalies="",
    ),
    # ── Thème 3 · Arc variables, marche 5e (Fable, 2026-07-30) ──
    "5e_C9.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Atelier « La boîte étiquetée » (Arc variables, marche 5e — le "
                "compteur du Cyclone de Coney Island) : 3 séances / 5 activités, "
                "simulateur de mémoire (verrou 4 étapes), prédire→tester→reporter "
                "sur éditeur Vittascience EMBARQUÉ, banc de tests du programme "
                "FOURNI (bug des descendus), modification ciblée + barrière "
                "commandée (banc 3 tests, cas limite zéro), QCM 30 q (10/10/10, "
                "3 illustrées), synthèses, fiche, matrice, 2 SVG CC0, photo Coney "
                "mutualisée avec l'atelier 3e.",
        anomalies="",
    ),
    "5e_C9.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        qualite="Modifier le programme fourni : séance 3 (activité 5 ①) de "
                "l'atelier « La boîte étiquetée » — README pointeur.",
    ),
    "5e_C9.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        qualite="Réaliser et mettre au point la barrière commandée : séance 3 "
                "(activité 5 ②) de l'atelier « La boîte étiquetée » — README "
                "pointeur.",
    ),
    # ── Thème 2 · LOT 01 (Fable, 2026-07-22) : Station d'alerte cyclonique ──
    "3e_C4.3": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence-projet « Station d'alerte cyclonique connectée » (4 séances, "
                "contexte Martinique) couvrant 3e_C4.3→C4.6 : 6 activités interactives "
                "+ réinvestissement, simulateur de CAN intégré, versions A (Arduino/"
                "Grove) / B (VittaScience) / C (sans matériel), QCM séparé 32 q avec "
                "corrections exhaustives et bilan par compétence, synthèses élève (A4) "
                "et professeur, fiche pédagogique/inspection, matrice de couverture, "
                "5 SVG originaux CC0, jeu de données 48 h simulé (CSV/ODS/XLSX), "
                "rapport de tests automatisés (Playwright, 40/40 + scénarios de notes).",
        anomalies="Compatibilité LCD Grove ↔ UNO R4 Minima non testée au labo "
                  "(MATÉRIEL À CONFIRMER — alternative VittaScience prévue). "
                  "Évaluation sommative laissée à l'enseignant (non publiée, conforme).",
        accessibilite="Navigation clavier + skip-link, aria/alt complets, "
                      "prefers-reduced-motion, minuteur désactivable, impression A4.",
        medias="5 SVG originaux (CC0) + données simulées — SOURCES_MEDIAS.md complet.",
    ),
    "3e_C4.4": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C4.3",
        qualite="README pointeur vers la séquence mutualisée 3e_C4.3 (activité 3 : "
                "CAN et simulateur ; 8 questions dédiées au QCM).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "3e_C4.5": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C4.3",
        qualite="README pointeur vers la séquence mutualisée 3e_C4.3 (activité 4 : "
                "types, descripteurs, codage binaire ; 8 questions dédiées au QCM).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "3e_C4.6": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C4.3",
        qualite="README pointeur vers la séquence mutualisée 3e_C4.3 (activités 5-6 : "
                "formats, transmission, stockage, exploitation de données ; "
                "8 questions dédiées au QCM).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "3e_C4.7": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence-projet « Internet jusqu'à Sainte-Luce » (3 séances) couvrant "
                "3e_C4.7+C4.8 : 5 activités + réinvestissement, 3 simulateurs HTML "
                "intégrés (paquets, jeu du routeur, panne/résilience), activité "
                "débranchée, versions A (Filius) / B (Packet Tracer à confirmer) / C, "
                "QCM séparé 30 q, synthèses élève/professeur, fiche pédagogique, "
                "matrice de couverture, 4 SVG originaux CC0, rapport de tests ; "
                "approfondie par l'atelier routage dédié « Le pont numérique "
                "Martinique → New York » (3e_C4.8) — README pointeur croisé.",
        anomalies="Packet Tracer 8.2 CONFIRMÉ en conditions réelles (session du "
                  "07/08/2026, atelier 3e_C4.8) — version B débloquée. Évaluation "
                  "sommative laissée à l'enseignant.",
        accessibilite="Clavier + skip-link, aria/alt, prefers-reduced-motion, "
                      "impression A4, minuteur désactivable.",
        medias="4 SVG originaux CC0 — SOURCES_MEDIAS.md complet.",
    ),
    "3e_C4.8": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="ATELIER DÉDIÉ « Le pont numérique Martinique → New York » "
                "(C4.7·C4.8, dossier principal) : conception du schéma à deux "
                "réseaux par l'élève (règle n°22), jeu du poste-frontière avec "
                "table DONNÉE (activité débranchée — conformité au libellé), "
                "montage réel à 2 routeurs 1941 (routes statiques miroir), preuves "
                "mesurées (ping TTL=126, tracert 3 sauts, Event List Successful) + "
                "contre-épreuve « route effacée » à verrou ; QCM 30 q (12/18), "
                "7 SVG CC0 reconstitués de la session Packet Tracer 8.2 réelle, "
                "fichier .pkt fourni, 37/37 tests Playwright ; complète la "
                "séquence-îlot « Internet jusqu'à Sainte-Luce » (3e_C4.7). "
                "RÉTROFIT AUDIT (08/08/2026) : billet d'entrée sans note sur les "
                "acquis de 4e + capsule de révision, mode essentiel persistant, "
                "domaine 1 du socle explicité, CRCN 2.3 ajouté, version 🅰 en "
                "réseau ISOLÉ (la preuve par le manque) — 25/25 tests dédiés.",
        anomalies="Aucune. Évaluation sommative laissée à l'enseignant.",
        accessibilite="Clavier, aria/alt, listes déroulantes exclusivement (DYS), "
                      "reduced-motion (simulateur compris), impression A4.",
        medias="7 SVG originaux CC0 + fichier .pkt — SOURCES_MEDIAS.md complet.",
    ),
    # ── Thème 2 · LOT 03 (Fable, 2026-07-22) : SOS station, réparer plutôt que jeter ──
    "3e_C5.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence-projet « SOS station : réparer plutôt que jeter » (4 séances) "
                "couvrant 3e_C5.1→C5.4 : 5 activités + réinvestissement, simulateur de "
                "dépannage à 2 pannes scriptées (compteur de mesures, verrou "
                "pédagogique), arbre de diagnostic, plan coté, versions A/B/C, QCM 32 q "
                "dont 10 illustrées (règle images v2), synthèses, fiche, matrice, 5 SVG "
                "originaux CC0, rapport de tests.",
        anomalies="Multimètres et imprimante 3D : MATÉRIEL À CONFIRMER (alternatives "
                  "simulation/gabarit prévues). Évaluation sommative à l'enseignant.",
        accessibilite="Clavier, aria/alt, reduced-motion, impression A4, minuteur "
                      "désactivable.",
        medias="5 SVG originaux CC0 image-objet — SOURCES_MEDIAS.md complet.",
    ),
    "3e_C5.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C5.1",
        qualite="README pointeur (activité 3 : rédaction du protocole ; 8 questions).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "3e_C5.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C5.1",
        qualite="README pointeur (activité 4 : simulateur de dépannage ; 8 questions).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "3e_C5.4": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C5.1",
        qualite="README pointeur (activité 5 : plan coté, procédé, matériau ; 8 questions).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    # ── Thème 2 · LOT 04 (Fable, 2026-07-23) : Programmer l'alerte ──
    "3e_C6.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence-projet « Programmer l'alerte » (3 séances) couvrant "
                "3e_C6.1+C6.3 : éditeur CodeLab Techno complet (première "
                "implémentation du composant commun), programme Python réel, "
                "vérification du code effectivement écrit par l'élève (act. 3-4), "
                "plan de tests aux frontières, versions A/B/C, QCM 30 q dont 6 "
                "illustrées, synthèses, fiche, matrice, 3 SVG CC0, rapport de tests. "
                "3e_C6.2 volontairement non traité (couvert par la séquence "
                "Algorigrammes DNB existante, non modifiée).",
        anomalies="Aucune. Exécution Python réelle proposée en bonus uniquement.",
        accessibilite="Clavier, aria/alt, A−/A+ et retour à la ligne dans CodeLab, "
                      "reduced-motion, impression A4, minuteur désactivable.",
        medias="3 SVG originaux CC0 image-objet — SOURCES_MEDIAS.md complet.",
    ),
    "3e_C6.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C6.1",
        qualite="README pointeur (activités 3-5 : modification, implémentation, "
                "plan de tests ; 15 questions dédiées).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    # ── LOT 07 (Fable) : îlot 5e_C6 « Programmer le lampadaire » ──
    "5e_C6.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence « Programmer le lampadaire » (3 séances) couvrant "
                "l'îlot 5e_C6 sur l'objet-fil du LOT 05 : carte d'identité du "
                "programme par blocs (données utilisées/produites/paramètres), "
                "traduction en algorithme en langage naturel (ordre + SI/ET/"
                "SINON), simulateur PARAMÉTRABLE avec mission mairie et verrou "
                "expérientiel (réglage d'origine testé puis réglage modifié "
                "vérifié). Versions A/B/C, QCM 30 q (10/10/10, 2 illustrées, "
                "réponses réparties), synthèses, fiche, matrice, 2 SVG CC0, "
                "rapport de tests. C4 et C6 de 5e désormais complets.",
        anomalies="Aucune. Version A en très basse tension uniquement.",
        accessibilite="Clavier, aria/alt, listes déroulantes exclusivement "
                      "(DYS), reduced-motion, impression A4.",
        medias="2 SVG originaux CC0 image-objet — SOURCES_MEDIAS.md complet.",
    ),
    **{c: dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="5e_C6.1",
        qualite=f"README pointeur ({d} ; 10 questions dédiées).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ) for c, d in {
        "5e_C6.2": "activité 2 : traduction en algorithme en langage naturel",
        "5e_C6.3": "activité 3 : paramètres, mission mairie, effets évalués",
    }.items()},
    # ── LOT 08 (Fable) : îlot 5e_C5 « Dépanner le lampadaire » ──
    "5e_C5.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence « Dépanner le lampadaire » (3 séances) clôturant "
                "l'îlot 5e du Thème 2 sur l'objet-fil des LOTs 05/07 : "
                "inspection visuelle interactive (6 zones, verrou 6/6, "
                "symptôme vs cause, fausse piste du panneau sale), réparation "
                "au protocole fourni (simulateur pas à pas avec remise à zéro "
                "pédagogique, verrou : test final exigé), atelier de "
                "fabrication (4 postes, familles additif/enlèvement, sécurité "
                "atelier), réinvestissement vélo. Versions A/B/C, QCM 30 q "
                "(10/10/10, 3 illustrées, réponses réparties 8/7/7/8), "
                "synthèses, fiche, matrice, 3 SVG CC0, rapport 22/22. "
                "Règles d'or n°4 (blocs élève) appliquée. C4+C5+C6 de 5e "
                "complets : la 5e du Thème 2 est bouclée.",
        anomalies="Aucune. Version A en très basse tension uniquement — "
                  "le secteur est explicitement interdit.",
        accessibilite="Clavier, aria/alt, listes déroulantes exclusivement "
                      "(DYS), reduced-motion, impression A4.",
        medias="3 SVG originaux CC0 image-objet — SOURCES_MEDIAS.md complet.",
    ),
    **{c: dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="5e_C5.1",
        qualite=f"README pointeur ({d} ; 10 questions dédiées).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ) for c, d in {
        "5e_C5.2": "séance 2 : réparation au protocole, simulateur avec verrou",
        "5e_C5.3": "séance 3 : atelier de fabrication, procédés et sécurité",
    }.items()},
    # ── LOT 06 (Fable) : l'énergie de la station (3e_C4.1 + C4.2) ──
    "3e_C4.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence « L'énergie de la station » (2 séances) clôturant la "
                "compétence C4 de 3e : élaboration du schéma-bloc (palette avec "
                "intrus, natures), dimensionnement (Wh, Ah, marge raisonnée) "
                "vérifié au simulateur d'autonomie 72 h (verrou expérientiel : "
                "essai insuffisant ET suffisant exigés), contraintes du site, "
                "choix justifiés matériau/procédé (abaque), réinvestissement "
                "borne du stade. Versions A/B/C, QCM 30 q (15/15, 3 illustrées, "
                "réponses réparties), synthèses, fiche, matrice, 3 SVG CC0, "
                "rapport de tests. Comble le manque détecté par l'audit.",
        anomalies="Aucune. Version A en très basse tension uniquement.",
        accessibilite="Clavier, aria/alt, listes déroulantes (DYS), "
                      "reduced-motion, impression A4, minuteur désactivable.",
        medias="3 SVG originaux CC0 image-objet — SOURCES_MEDIAS.md complet.",
    ),
    "3e_C4.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C4.1",
        qualite="README pointeur (activités 3-4 : contraintes du site, choix "
                "justifiés matériau/procédé ; 15 questions dédiées).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    # ── LOT 05 (Fable) : îlot 5e complet de la compétence C4 ──
    "5e_C4.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence-îlot « Le lampadaire intelligent » (5 séances) couvrant "
                "les 8 codes 5e de la compétence C4 sur un objet-fil unique : "
                "fonctions/solutions + matériaux, chaîne d'énergie et natures, "
                "chaîne d'information avec simulateur interactif (verrou "
                "expérientiel : jour/nuit/nuit+passage), descripteurs et données "
                "(table des 6 lampadaires), réseau local et jeu du courrier "
                "débranché (prescription C4.8), réinvestissement sonnette "
                "connectée. Versions A/B/C, QCM 32 q (4 par code) dont 6 "
                "illustrées, synthèses, fiche, matrice, 3 SVG CC0, rapport de "
                "tests. Première entrée 5e du Thème 2, langue calibrée 12 ans.",
        anomalies="Aucune.",
        accessibilite="Clavier, aria/alt, listes déroulantes (DYS), "
                      "reduced-motion, impression A4, minuteur désactivable.",
        medias="3 SVG originaux CC0 image-objet — SOURCES_MEDIAS.md complet.",
    ),
    **{f"5e_C4.{i}": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="5e_C4.1",
        qualite=f"README pointeur ({detail} ; 4 questions dédiées).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ) for i, detail in {
        2: "activité 2 : chaîne d'énergie fournie à compléter",
        3: "activité 2 : natures des énergies à chaque étape",
        4: "activité 1 : matériaux et critères de choix",
        5: "activité 3 : chaîne d'information + simulateur",
        6: "activité 4 : descripteurs, types, formats",
    }.items()},
    "5e_C4.7": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Atelier dédié « Le réseau de la salle techno » (3 séances) couvrant "
                "5e_C4.7+C4.8 avec Cisco Packet Tracer 8.2 embarqué en pratique "
                "guidée : jeu du facteur débranché, lecture de topologie, "
                "construction complète du réseau (guide inclusif A→H, règle n°20, "
                "figures reconstituées d'après le vrai logiciel — 24 ports, "
                "triangles, SSID, module WPC300N), adressage IP par l'analogie de "
                "la rue, preuves ping/Simulation, panne du doublon, mini-simulateur "
                "d'enveloppe à verrou expérientiel, tablette et smartphone dans le "
                "montage. QCM 30 q (16/14, 6 illustrées, réponses 8/7/7/8), "
                "synthèses élève/professeur, fiche, matrice, 7 SVG CC0, fichier "
                ".pkt maître, cartouche CRCN 5.1 (règle n°7), rapport de tests. "
                "Approfondit les act. 5-6 du lampadaire (5e_C4.1) ; vocabulaire "
                "strictement 5e (masque/passerelle/routage exclus, réservés 4e/3e). "
                "RÉTROFIT AUDIT (08/08/2026) : billet d'entrée sans note + capsule "
                "de rattrapage, mode essentiel persistant, domaine 1 du socle "
                "explicité, CRCN 2.3 ajouté, encadré « premier ping : ne panique "
                "pas », valeurs dites réellement observées, version 🅰 en réseau "
                "ISOLÉ (TP 2 PC + commutateur dédié) — 24/24 tests dédiés.",
        anomalies="Aucune.",
        accessibilite="Clavier + skip-link, aria/alt, listes déroulantes (DYS), "
                      "reduced-motion (mini-simulateur compris), impression A4, "
                      "minuteur QCM désactivable.",
        medias="7 SVG originaux CC0 (reconstitutions fidèles Packet Tracer 8.2) "
               "+ fichier .pkt maître — SOURCES_MEDIAS.md complet.",
    ),
    "5e_C4.8": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="5e_C4.7",
        qualite="README pointeur vers l'atelier réseau mutualisé 5e_C4.7 "
                "(act. 1, 4, 5 : jeu du facteur, adressage, preuves par "
                "simulation ; 14 questions dédiées) ; l'activité 6 du lampadaire "
                "(5e_C4.1) reste la première rencontre.",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "4e_C5.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence « SOS jardin connecté » (3 séances) ouvrant l'îlot C5 de 4e sur "
                "l'objet-fil du LOT 09 : le protocole de diagnostic est PROPOSÉ par l'élève "
                "(6 tests ordonnés puis exécutés au poste de diagnostic, verrou 6/6, capteur "
                "menteur démasqué par le test discriminant mesure/réalité), remplacement en "
                "autonomie SANS protocole affiché (vignettes non numérotées, simulateur à "
                "verrou, photo + comparaison + test final à l'eau), choix multicritère du "
                "procédé (impression 3D PETG, gamme, jeu fonctionnel 10,2/10,0), "
                "réinvestissement lampe du CDI (frontière TBT/secteur). Versions A/B/C, "
                "QCM 30 q (10/10/10, 3 illustrées, réponses réparties 8/7/7/8, graine 42), "
                "synthèses, fiche, matrice, 3 SVG CC0, rapport 23/23. Règles d'or n°4 "
                "appliquée ; _outils/fix_r.js recréé et commité. La panne « capteur qui "
                "ment » prépare le LOT C6 (corriger le programme).",
        anomalies="Aucune. Version A en très basse tension uniquement — le secteur est "
                  "explicitement interdit (y compris au réinvestissement).",
        accessibilite="Clavier, aria/alt, listes déroulantes exclusivement (DYS), "
                      "reduced-motion, impression A4.",
        medias="3 SVG originaux CC0 image-objet — SOURCES_MEDIAS.md complet.",
    ),
    "4e_C5.2": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C5.1",
        qualite="README pointeur (séance 2 : remplacement en autonomie sans protocole "
                "affiché, simulateur avec verrou ; 10 questions dédiées).",
        anomalies="Aucune.",
        accessibilite="s.o.",
        medias="s.o.",
    ),
    "4e_C5.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C5.1",
        qualite="README pointeur (séance 3 : choix multicritère des procédés, gamme, jeu "
                "fonctionnel, sécurité atelier ; 10 questions dédiées).",
        anomalies="Aucune.",
        accessibilite="s.o.",
        medias="s.o.",
    ),
    "4e_C6.1": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence « Ajuster le programme du jardin » (2 séances) clôturant l'arc "
                "4e de l'objet-fil (C4 structure → C6.2 programme → C5 dépannage → ce "
                "lot) : analyse des relevés USB (pompe qui bat 47 fois autour du seuil "
                "unique, arrosage à 13 h, cas normal de contrôle), spécification de "
                "l'hystérésis 35/45 (écart > vibration) et de la plage horaire (ET sur "
                "le démarrage seulement), banc de test à 4 scénarios en ordre libre "
                "(verrou __exp.scen), méthode de validation en 5 étapes (sauvegarde, "
                "simulation, plant témoin, non-régression, rollback), transfert "
                "lampadaire (hystérésis 20/40 lux). Versions A/B/C, QCM 30 q (15+15, "
                "3 illustrées, réponses réparties 8/7/7/8, graine 57), synthèses, fiche, "
                "matrice, 3 SVG CC0, rapport 23/23 (Playwright réel). Règle d'or n°4 "
                "appliquée. 4e_C6.2 volontairement non traité (séquence modèle existante, "
                "non modifiée, référencée au bilan) : la compétence C6 de 4e est complète.",
        anomalies="Aucune. Version A en très basse tension uniquement — le secteur est "
                  "explicitement interdit.",
        accessibilite="Clavier, aria/alt, listes déroulantes exclusivement (DYS), "
                      "reduced-motion, impression A4.",
        medias="3 SVG originaux CC0 (2 image-objet + 1 image-explication) — "
               "SOURCES_MEDIAS.md complet.",
    ),
    "4e_C6.3": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C6.1",
        qualite="README pointeur (séance 2 : méthode de validation en 5 étapes, banc de "
                "test à scénarios avec verrou ; 15 questions dédiées).",
        anomalies="Aucune.",
        accessibilite="s.o.",
        medias="s.o.",
    ),
}

# Codes couverts par mutualisation déclarée dans le dépôt (README pointeurs)
# et croisements signalés par les README.
CROISEMENTS = {
    "5e_C1.4": "Mutualisé avec 5e_C1.3 (README pointeur en place).",
    "5e_C1.5": "Croisement déclaré avec 4e_C1.4 (cybersécurité V16) — pointeur manquant.",
    "5e_C1.6": "Croisement déclaré avec 4e_C1.4 (cybersécurité V16) — pointeur manquant.",
}


def fichiers_reels(rel_dir):
    """Liste (relative) des fichiers réels du dossier code, .gitkeep exclu."""
    full = os.path.join(RACINE, rel_dir)
    out = []
    if not os.path.isdir(full):
        return out
    for base, _dirs, files in os.walk(full):
        for f in files:
            if f == ".gitkeep":
                continue
            # normalisation "/" : sous Windows, relpath produit des "\" qui
            # pollueraient audit_couverture.json (chemins non portables)
            out.append(os.path.relpath(os.path.join(base, f), full).replace(os.sep, "/"))
    return sorted(out)


def construire():
    lignes = []
    for niveau in ("5e", "4e", "3e"):
        for cnum, items in COMP_BY_LEVEL[niveau].items():
            texte_parent, socle_parent, theme = C_PARENT[cnum]
            for code, texte, socle in items:
                code_pref = f"{niveau}_{code}"
                rel = code_dir(cnum, niveau, code)
                fichiers = fichiers_reels(rel)
                o = OVERLAY.get(code_pref, {})
                statut = o.get("statut", "À CRÉER" if not fichiers else "À VÉRIFIER PAR L’ENSEIGNANT")
                # Un statut « complet et validable » ne se déclare pas : il se
                # vérifie sur pièces (règle d'or n°190). Voir controle_statut.py.
                statut, manquantes, motif = controle_verdict(
                    statut, os.path.join(RACINE, rel), o.get("mutualise_avec", ""))
                if motif:
                    o = dict(o)
                    o["anomalies"] = (motif + " " + o.get("anomalies", "")).strip()
                ligne = {
                    "code": code_pref,
                    "niveau": niveau,
                    "competence": cnum,
                    "competence_officielle": texte_parent,
                    "theme": theme,
                    "theme_titre": THEME_TITLES[theme],
                    "formulation": texte,
                    "socle": socle,
                    "chemin": rel.replace(os.sep, "/"),
                    "nb_fichiers": len(fichiers),
                    "fichiers": fichiers,
                    "sequence": o.get("sequence", False),
                    "qcm": o.get("qcm", False),
                    "projet": o.get("projet", False),
                    "synthese": o.get("synthese", False),
                    "evaluation": o.get("evaluation", False),
                    "correction": o.get("correction", False),
                    "situation_declenchante": o.get("situation", False),
                    "problematique": o.get("problematique", False),
                    "qualite": o.get("qualite", "" if fichiers else "Dossier vide (squelette Images/ + Synthèses/)."),
                    "anomalies": o.get("anomalies", ""),
                    "accessibilite": o.get("accessibilite", ""),
                    "medias_licences": o.get("medias", ""),
                    "croisement": CROISEMENTS.get(code_pref, o.get("mutualise_avec", "")),
                    "statut": statut,
                    "preuves_manquantes": ", ".join(manquantes),
                }
                lignes.append(ligne)
    return lignes


def main():
    lignes = construire()
    assert len(lignes) == 114, f"Attendu 114 codes, obtenu {len(lignes)}"

    champs = ["code", "niveau", "competence", "theme", "formulation", "socle",
              "chemin", "nb_fichiers", "sequence", "qcm", "projet", "synthese",
              "evaluation", "correction", "situation_declenchante", "problematique",
              "qualite", "anomalies", "accessibilite", "medias_licences",
              "croisement", "statut", "preuves_manquantes"]

    csv_path = os.path.join(RACINE, "audit_couverture.csv")
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=champs, extrasaction="ignore", delimiter=";")
        w.writeheader()
        for l in lignes:
            l2 = dict(l)
            for k in ("sequence", "qcm", "projet", "synthese", "evaluation",
                      "correction", "situation_declenchante", "problematique"):
                v = l2[k]
                l2[k] = "oui" if v else ("?" if v is None else "non")
            w.writerow(l2)

    json_path = os.path.join(RACINE, "audit_couverture.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"genere_le": "2026-07-21",
                   "total_codes": len(lignes),
                   "codes": lignes}, f, ensure_ascii=False, indent=2)

    # Récapitulatif par statut
    from collections import Counter
    stats = Counter(l["statut"] for l in lignes)
    print(f"{len(lignes)} codes écrits dans audit_couverture.csv / .json")
    for s, n in stats.most_common():
        print(f"  {n:3d}  {s}")

    recales = [l for l in lignes if l["preuves_manquantes"]]
    if recales:
        print(f"\n  Contrôle de statut — {len(recales)} code(s) recalé(s) faute de pièces :")
        for l in recales:
            print(f"    {l['code']:<10} → {l['statut']}  (manque : {l['preuves_manquantes']})")


if __name__ == "__main__":
    main()
