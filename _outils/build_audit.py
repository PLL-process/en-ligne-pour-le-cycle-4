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
    "5e_C1.1": dict(
        statut="EXISTANT À AMÉLIORER",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="Séquence tableur/données interactive + QCM 24 q + 2 fichiers xlsx + 1 csv.",
        anomalies="Lien cassé vers C11_exo_tableur_debut.xlsx (le fichier s'appelle "
                  "exo_tableur_debut.xlsx) ; gabarits non résolus {{sensor_icon}}, "
                  "{{sort_icon}}, {{analysis_icon}} dans des src d'images ; pas de "
                  "différenciation ; pas de découpage explicite en séances.",
        accessibilite="Correcte (réparée lors de la migration) — contraste à revérifier.",
        medias="Fichiers tableur maison, pas de média externe.",
    ),
    "5e_C1.2": dict(
        statut="À CORRIGER",
        sequence=True, qcm=True, projet=False, synthese=False,
        evaluation=False, correction=False, situation=None, problematique=None,
        qualite="QCM 24 q correct ; la « séquence » est un fichier .mhtml (archive "
                "navigateur) de 176 Ko.",
        anomalies="Le .mhtml ne s'affiche pas comme une page sur GitHub Pages (il se "
                  "télécharge) ; l'en-tête interne indique un fichier d'origine nommé "
                  "sequence_C1.2_4e_dark.html : le contenu est peut-être une séquence "
                  "de 4e rangée en 5e — À VÉRIFIER PAR L'ENSEIGNANT. À reconvertir en "
                  ".html propre.",
        accessibilite="Non évaluable tant que le .mhtml n'est pas converti.",
        medias="Inconnus (encapsulés dans le .mhtml).",
    ),
    "5e_C1.3": dict(
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
        statut="À CRÉER",
        qualite="Aucune ressource dans le dossier. La séquence cybersécurité V16 rangée "
                "en 4e_C1.4 couvre ce code « en croisement » d'après son README, mais "
                "aucun README pointeur n'existe côté 5e.",
        anomalies="Créer au minimum un README pointeur vers 4e_C1.4 ou une déclinaison 5e.",
    ),
    "5e_C1.6": dict(
        statut="À CRÉER",
        qualite="Aucune ressource. Même situation que 5e_C1.5 (matériau réutilisable "
                "dans la séquence cybersécurité 4e_C1.4 : cyberviolence, vie privée).",
        anomalies="Créer au minimum un README pointeur vers 4e_C1.4 ou une déclinaison 5e.",
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
    "4e_C2.1": dict(
        statut="PARTIEL",
        sequence=False, qcm=True, projet=False, synthese=False,
        evaluation=False, correction=True, situation=False, problematique=False,
        qualite="Un seul QCM (qcm_fonctionnement_objet, 50 Ko) — reclassé depuis C1 "
                "lors de la migration.",
        anomalies="Pas de séquence, pas de synthèse, pas de projet. Un QCM isolé ne "
                  "constitue pas une séquence.",
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
    "4e_C4.4": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=True, projet=False, synthese=False,
        evaluation=False, correction=True, situation=False, problematique=False,
        mutualise_avec="4e_C4.1",
        qualite="README pointeur (séance 2 : chaîne d'information du jardin) "
                "+ QCM eCall 40 q existant conservé en entraînement "
                "complémentaire (rattachement confirmé le 21/07/2026).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ),
    "4e_C4.7": dict(
        statut="COMPLET ET VALIDABLE",
        sequence=True, qcm=True, projet=False, synthese=True,
        evaluation=True, correction=True, situation=True, problematique=True,
        qualite="ATELIER DÉDIÉ « SOS serre » (C4.7·C4.8·C4.9, dossier principal) : "
                "conception du plan d'adressage par l'élève (règle n°22), adresse "
                "fixe passerelle comprise, clinique du réseau (2 pannes réelles), "
                "validation par simulation ; QCM 30 q (10/10/10), 9 SVG CC0 "
                "reconstitués de sessions Packet Tracer 8.2 réelles, fichier .pkt "
                "fourni, 36/36 tests Playwright ; complète la séance 3 du Jardin "
                "connecté (4e_C4.1) + QCM XXL réseaux conservé en entraînement.",
        anomalies="Héritées du QCM XXL existant : licences des images *_hd.jpg "
                  "non documentées — LICENCE À VÉRIFIER (consolidation "
                  "post-Conseil) ; doc3_schema_parcours.png (2,6 Mo) à trier.",
        accessibilite="Clavier, aria/alt, listes déroulantes exclusivement (DYS), "
                      "reduced-motion (clinique comprise), impression A4.",
        medias="9 SVG originaux CC0 + fichier .pkt — SOURCES_MEDIAS.md complet.",
    ),
    **{c: dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="4e_C4.1",
        qualite=f"README pointeur ({d}).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
    ) for c, d in {
        "4e_C4.2": "séance 1 : transformations et flux d'énergie",
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
        "4e_C4.8": "act. 2 et 4 : banc d'essai + panne « mauvaise rue »",
        "4e_C4.9": "act. 5 : simulation fournie complétée et validée",
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
    "3e_C6.2": dict(
        statut="EXISTANT À AMÉLIORER",
        sequence=True, qcm=True, projet=False, synthese=False,
        evaluation=True, correction=True, situation=False, problematique=False,
        qualite="Séquence algorigrammes DNB (68 Ko, mode enseignant) + QCM 24 q — bonne "
                "banque d'exercices type brevet.",
        anomalies="Pas de situation déclenchante, pas de problématique, pas de mission, "
                  "pas de synthèse ni de référentiel affiché : c'est une banque "
                  "d'entraînement plus qu'une séquence au sens du gabarit Jardin connecté.",
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
                "matrice de couverture, 4 SVG originaux CC0, rapport de tests.",
        anomalies="Packet Tracer : comptes À CONFIRMER (version B non bloquante, "
                  "Filius confirmé). Évaluation sommative laissée à l'enseignant.",
        accessibilite="Clavier + skip-link, aria/alt, prefers-reduced-motion, "
                      "impression A4, minuteur désactivable.",
        medias="4 SVG originaux CC0 — SOURCES_MEDIAS.md complet.",
    ),
    "3e_C4.8": dict(
        statut="COUVERT PAR UNE SÉQUENCE MUTUALISÉE",
        sequence=False, qcm=False, projet=False, synthese=False,
        evaluation=False, correction=False, situation=False, problematique=False,
        mutualise_avec="3e_C4.7",
        qualite="README pointeur vers la séquence mutualisée 3e_C4.7 (activités 4-5 : "
                "jeu du routeur débranché, simulateur de panne ; 15 questions dédiées).",
        anomalies="Aucune.", accessibilite="s.o.", medias="s.o.",
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
                "strictement 5e (masque/passerelle/routage exclus, réservés 4e/3e).",
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
              "croisement", "statut"]

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


if __name__ == "__main__":
    main()
