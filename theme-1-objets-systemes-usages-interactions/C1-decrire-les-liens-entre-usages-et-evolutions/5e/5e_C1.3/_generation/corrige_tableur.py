# -*- coding: utf-8 -*-
"""5e_C1.3 — le corrigé de l'activité 3 « Exploiter un jeu de données simulées », fait PAR LibreOffice Calc
(règles d'or n°332 et n°336, 16/11/2026). Chaque consigne de la page, faite dans Calc, dans l'ordre :

  colonne statut_maintenance → « prioritaire » si incidents ≥ 3 OU autonomie < 35 % → tri par incidents décroissant →
  filtre sur « prioritaire » → export PDF.

Produit, à côté du CSV de l'élève :
1. `donnees_velos_hangzhou_corrige.ods` : le tableur transformé (statut saisi, trié, filtré — le filtre se retire par
   Données → Plus de filtres → Réinitialiser le filtre, et les huit vélos reviennent : rien n'a été supprimé) ;
2. `velos_prioritaires_corrige.pdf` : le PDF filtré, tel que Calc l'exporte ;
3. `Images/capture_corrige_velos_tries.png` (les huit vélos, statut saisi, triés) et
   `Images/capture_corrige_velos_pdf_filtre.png` (la page du PDF : les quatre vélos prioritaires).

Rejouer : python3 _generation/corrige_tableur.py   (depuis le dossier du lot ; LibreOffice requis)
"""
import os
import sys

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ICI, "..", "..", "..", "..", "_outils"))
import tableur_corrige as T  # noqa: E402

CSV = os.path.join(ICI, "donnees_velos_hangzhou_simulees.csv")
CORRIGE = os.path.join(ICI, "donnees_velos_hangzhou_corrige.ods")
PDF = os.path.join(ICI, "velos_prioritaires_corrige.pdf")
PNG_TRI = os.path.join(ICI, "Images", "capture_corrige_velos_tries.png")
PNG_PDF = os.path.join(ICI, "Images", "capture_corrige_velos_pdf_filtre.png")

with T.Calc() as calc:
    doc = calc.ouvrir(CSV, separateur=";")
    T.en_francais(doc)
    f = doc.Sheets.getByIndex(0)
    f.setName("velos")
    n = 1
    while f.getCellRangeByName("A%d" % (n + 1)).getString():
        n += 1                                                   # n : la dernière ligne (titres en ligne 1)
    plage = "A1:G%d" % n
    T.format_fr(doc, f, "F2:F%d" % n, "AAAA-MM-JJ")

    # ③ ④ la colonne statut_maintenance (déjà titrée dans le fichier) : « prioritaire » selon le critère
    prioritaires = []
    for r in range(2, n + 1):
        incidents = f.getCellRangeByName("D%d" % r).getValue()
        autonomie = f.getCellRangeByName("E%d" % r).getValue()
        if incidents >= 3 or autonomie < 35:
            T.ecrire(f, "G%d" % r, "prioritaire")
            prioritaires.append(f.getCellRangeByName("A%d" % r).getString())
    T.gras(f, "A1:G1")
    T.fond(f, "A1:G1", "#dfe7f7")
    T.largeurs(f, {"A": 1.9, "B": 3.8, "C": 3.9, "D": 3.7, "E": 5.0, "F": 4.9, "G": 4.5})
    f.getCellRangeByName("G1:G%d" % n).ParaLeftMargin = 300     # de l'air entre la date et le statut

    # ⑤ le tri : incidents décroissants (colonne D, la 4e)
    T.trier(f, plage, 3, croissant=False)
    ordre = [f.getCellRangeByName("A%d" % r).getString() for r in range(2, n + 1)]
    print("prioritaires :", prioritaires, "· ordre après tri :", ordre)
    print("capture triée :", calc.capture(doc, "velos", PNG_TRI, plage=plage))

    # ⑥ le filtre : seulement les lignes « prioritaire » (colonne G, la 7e) — masquées, pas supprimées
    T.filtrer_egal(f, plage, 6, "prioritaire")
    visibles = [f.getCellRangeByName("A%d" % r).getString() for r in range(2, n + 1)
                if f.Rows.getByIndex(r - 1).IsVisible]
    print("visibles après filtre :", visibles)
    calc.enregistrer(doc, CORRIGE)

    # ⑦ l'export PDF, et sa capture
    calc.exporter_pdf(doc, "velos", PDF, plage=plage)
    print("capture du PDF :", calc.capture(doc, "velos", PNG_PDF, plage=plage))
    doc.close(True)
