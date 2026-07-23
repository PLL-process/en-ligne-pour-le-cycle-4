#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script autonome v3 — Remplissage des onglets S7 (Thème 3) des progressions 5e et 4e.
Corrigé après banc d'essai Fable v2 (23/07/2026).
Préserve le préfixe « ■ Séance n — semaine Sxx ».

Usage (depuis la racine du dépôt) :
    python _progressions/remplir_S7_theme3.py
"""

from openpyxl import load_workbook
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent.parent
CONTENU_JSON = Path(__file__).resolve().parent / "contenu_S7_theme3.json"

def charger_contenu():
    with open(CONTENU_JSON, encoding="utf-8") as f:
        return json.load(f)

def ecrire_si_possible(ws, cell, value):
    """Écrit uniquement si la cellule n'est pas une MergedCell en lecture seule."""
    try:
        ws[cell] = value
    except AttributeError:
        print(f"  [ignoré] {cell} est une cellule fusionnée")

def remplir_identification(ws, data):
    mapping = {
        "B5": data.get("situation_declenchante"),
        "B6": data.get("prerequis"),
        "B7": data.get("objectifs_synthese"),
        "B11": data.get("versions"),
        "B12": data.get("liens_epi"),
        "B14": data.get("ressources_en_ligne"),
    }
    for cell, value in mapping.items():
        if value:
            ecrire_si_possible(ws, cell, value)

def remplir_colonne_D_competences(ws, mapping_codes, start_row, end_row):
    for row in range(start_row, end_row + 1):
        code = ws.cell(row=row, column=1).value
        if code and code in mapping_codes:
            ecrire_si_possible(ws, f"D{row}", mapping_codes[code])

def remplir_seance(ws, start_row, seance):
    """Remplit un bloc de séance de 9 lignes à partir de start_row.
    Préserve le préfixe « ■ Séance n — semaine Sxx »."""
    if seance.get("titre_seance"):
        actuel = str(ws[f"A{start_row}"].value or "")
        prefixe = actuel.split("— — —")[0].rstrip()  # « ■ Séance n — semaine Sxx »
        brut = seance["titre_seance"]
        titre = brut.split("—", 1)[-1].strip() if "—" in brut else brut
        ecrire_si_possible(ws, f"A{start_row}", f"{prefixe} — — — {titre}")

    ecrire_si_possible(ws, f"B{start_row + 1}", seance.get("question_directrice", ""))
    ecrire_si_possible(ws, f"B{start_row + 2}", seance.get("activites_supports", ""))
    ecrire_si_possible(ws, f"B{start_row + 3}", seance.get("demarche", ""))
    ecrire_si_possible(ws, f"B{start_row + 4}", seance.get("bilan_trace", ""))
    ecrire_si_possible(ws, f"B{start_row + 5}", seance.get("cahier_texte_contenu", ""))
    ecrire_si_possible(ws, f"B{start_row + 6}", seance.get("cahier_texte_travail", ""))
    # Ligne start_row+7 = Suivi enseignant → NE PAS ÉCRIRE

def traiter_classeur(path, niveau, data_niveau):
    if not path.exists():
        print(f"Fichier non trouvé : {path}")
        return False

    wb = load_workbook(path)
    if "S7" not in wb.sheetnames:
        print(f"ATTENTION : onglet S7 introuvable dans {path.name}")
        return False

    ws = wb["S7"]

    # Garde-fou structure
    a18 = ws["A18"].value
    expected = f"{niveau}_C7.1"
    if a18 != expected:
        print(f"GARDE-FOU : A18 = '{a18}' (attendu '{expected}'). Structure changée → abandon sans sauvegarde.")
        return False

    print(f"Remplissage S7 ({niveau})...")

    remplir_identification(ws, data_niveau)

    if niveau == "5e":
        remplir_colonne_D_competences(ws, data_niveau.get("codes_seances", {}), 18, 29)
        seances_rows = [32, 41, 50, 59, 68, 77]
    else:
        remplir_colonne_D_competences(ws, data_niveau.get("codes_seances", {}), 18, 31)
        seances_rows = [34, 43, 52, 61, 70, 79]

    seances = data_niveau.get("seances", [])
    for i, start_row in enumerate(seances_rows):
        if i < len(seances):
            remplir_seance(ws, start_row, seances[i])

    wb.save(path)
    print(f"  → S7 {niveau} sauvegardé.")
    return True

def main():
    contenu = charger_contenu()

    ok5 = traiter_classeur(
        ROOT / "_progressions" / "5e" / "Progression_Techno_5e_2026-2027_Martinique.xlsx",
        "5e",
        contenu["5e"]["S7"]
    )
    ok4 = traiter_classeur(
        ROOT / "_progressions" / "4e" / "Progression_Techno_4e_2026-2027_Martinique.xlsx",
        "4e",
        contenu["4e"]["S7"]
    )

    if ok5 and ok4:
        print("\nTerminé avec succès. Vérifier les onglets S7 puis recalculer si besoin.")
    else:
        print("\nTerminé avec des alertes. Vérifier les messages ci-dessus.")
        sys.exit(1)

if __name__ == "__main__":
    main()
