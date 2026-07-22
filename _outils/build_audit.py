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
                  "_ressources-communes/Images/, le second n'existe nulle part dans le "
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
                  "_ressources-communes/delagrave_affiche_l_ecologie_du_numerique_college.pdf ; "
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
    "4e_C4.1": dict(
        statut="PARTIEL",
        sequence=False, qcm=True, projet=False, synthese=False,
        evaluation=False, correction=True, situation=False, problematique=False,
        qualite="QCM « automatisation premium » (5,5 Ko seulement).",
        anomalies="Gabarit ${q.img} présent dans le code (images de questions non "
                  "résolues) ; très léger : à étoffer ou fusionner dans une vraie séquence.",
    ),
    "4e_C4.4": dict(
        statut="PARTIEL",
        sequence=False, qcm=True, projet=False, synthese=False,
        evaluation=False, correction=True, situation=False, problematique=False,
        qualite="QCM eCall 40 questions (chaîne d'information d'une voiture) — bon support, "
                "correctement rattaché : 4e_C4.4 = « Identifier les constituants de la chaîne "
                "d'information d'un objet réel et les associer à leur fonction » "
                "(rattachement confirmé par la gouvernance le 21/07/2026).",
        anomalies="Pas de séquence d'accueil autour du QCM (situation déclenchante, "
                  "synthèse, projet à créer).",
    ),
    "4e_C4.7": dict(
        statut="PARTIEL",
        sequence=False, qcm=True, projet=False, synthese=False,
        evaluation=False, correction=True, situation=False, problematique=False,
        qualite="QCM XXL réseaux 77 questions (fusion) + 9 images réseau.",
        anomalies="Pas de séquence ni d'activité Filius alors que le code porte sur les "
                  "composants d'un réseau local ; licences des images *_hd.jpg "
                  "(bluetooth_projecteur, rfid_tag_portique, zigbee_mesh…) non "
                  "documentées — LICENCE À VÉRIFIER ; doc3_schema_parcours.png (2,6 Mo) "
                  "placé ici « faute de certitude » d'après le rapport de migration.",
    ),
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
        statut="À CORRIGER",
        sequence=True, qcm=True, projet=True, synthese=True,
        evaluation=True, correction=True, situation=False, problematique=False,
        qualite="Riche : vittascience_variables.html (97 Ko, évaluation interactive "
                "Python/Vittascience), TP mBot2 Python (114 Ko), QCM 24 q, 15 images, "
                "README complet.",
        anomalies="17 liens d'images cassés dans vittascience_variables.html : le HTML "
                  "référence assets/… alors que les fichiers sont dans Images/ "
                  "(correction en une passe de remplacement) ; capture-06, capture-07 et "
                  "capture-02→05 partiellement non référencées à revérifier après "
                  "correction ; pas de situation déclenchante ni de problématique ; "
                  "vidéo YouTube intégrée (dépendance externe + RGPD à évaluer).",
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
            out.append(os.path.relpath(os.path.join(base, f), full))
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
