# -*- coding: utf-8 -*-
"""4e_C1.1 — le corrigé de l'activité 2 « Estimer, et dire ce que l'estimation vaut », fait PAR LibreOffice Calc
(règles d'or n°332 et n°336, 16/11/2026).

1. `donnees_feux_impacts_4e_corrige.ods` : le fichier de l'élève (les données, feuille « donnees ») et la feuille
   « Estimation » — chaque étape du mode opératoire de la page dans sa cellule, le résultat calculé par Calc, la
   formule écrite à côté, et l'avertissement dans la cellule à côté du résultat.
2. `Images/capture_corrige_estimation_proxy.png` : la feuille « Estimation », telle que Calc l'imprime.

Rejouer : python3 _generation/corrige_tableur.py   (depuis le dossier du lot ; LibreOffice requis)
"""
import os
import sys

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ICI, "..", "..", "..", "..", "_outils"))
import tableur_corrige as T  # noqa: E402

CSV = os.path.join(ICI, "donnees_feux_impacts_4e.csv")
CORRIGE = os.path.join(ICI, "donnees_feux_impacts_4e_corrige.ods")
PNG = os.path.join(ICI, "Images", "capture_corrige_estimation_proxy.png")

# (étape, formule pour Calc, la formule telle que l'élève la lit dans Calc en français, format du résultat)
ETAPES = [
    ("Émissions des feux, UE 2023 (t de CO₂)", "=20*1000000", "=20*1000000", "# ##0"),
    ("Surface brûlée, UE 2023 (ha)", "=504002", "=504002", "# ##0"),
    ("Ratio : t de CO₂ par hectare", "=B4/B5", "=B4/B5", "0,00"),
    ("Surface brûlée, France 2026 (ha)", "=50000", "=50000", "# ##0"),
    ("Estimation : t de CO₂", "=B7*B6", "=B7*B6", "# ##0"),
    ("Arrondie à 3 chiffres significatifs", "=ROUND(B8;-4)", "=ARRONDI(B8;-4)", "# ##0"),
]
AVERTISSEMENT = ("Estimation par proxy européen 2023, non officielle pour la France 2026. Elle ne tient pas compte "
                 "du type de végétation, de l'humidité, de la sévérité du feu, de la biomasse réellement consumée, ni "
                 "du devenir du carbone après le feu. À ne pas présenter comme « les émissions des feux français "
                 "de 2026 » : c'est un ordre de grandeur.")

with T.Calc() as calc:
    doc = calc.ouvrir(CSV, separateur=";", decimale=",")
    T.en_francais(doc)
    d = doc.Sheets.getByIndex(0)
    d.setName("donnees")
    T.gras(d, "A1:H1")
    T.largeurs(d, {"A": 2.6, "B": 2.4, "C": 3.2, "D": 8.6, "E": 2.0, "F": 4.0, "G": 5.6, "H": 6.4})

    doc.Sheets.insertNewByName("Estimation", 1)
    e = doc.Sheets.getByName("Estimation")
    T.ecrire(e, "A1", "Estimer les émissions des feux français de 2026 — par un proxy européen")
    T.gras(e, "A1")
    for col, titre in zip("ABC", ("Étape", "Résultat", "La formule, dans Calc")):
        T.ecrire(e, "%s3" % col, titre)
    T.gras(e, "A3:C3")
    T.fond(e, "A3:C3", "#dfe7f7")
    for i, (etape, formule, lue, code) in enumerate(ETAPES):
        n = 4 + i
        T.ecrire(e, "A%d" % n, etape)
        T.ecrire(e, "B%d" % n, formule)
        e.getCellRangeByName("C%d" % n).setString(lue)
        T.format_fr(doc, e, "B%d" % n, code)
    T.fond(e, "B6", "#fff8d6")
    T.fond(e, "B8:B9", "#fff8d6")
    T.gras(e, "B6")
    T.gras(e, "B9")
    T.ecrire(e, "A11", "⚠ L'avertissement, à côté du résultat")
    T.gras(e, "A11")
    T.fond(e, "A11", "#ffe1c2")
    T.ecrire(e, "B11", AVERTISSEMENT)
    T.texte_long(e, "B11:C11")
    T.fond(e, "B11:C11", "#fff1e3")
    e.getCellRangeByName("A11").IsTextWrapped = True
    e.getCellRangeByName("A11").VertJustify = 1
    e.Rows.getByIndex(10).Height = 2600          # les quatre lignes de l'avertissement (cellules fusionnées)
    e.getCellRangeByName("C3:C9").ParaLeftMargin = 350   # un peu d'air entre le résultat et sa formule
    T.largeurs(e, {"A": 6.6, "B": 3.6, "C": 6.2})
    doc.Sheets.moveByName("Estimation", 0)
    calc.enregistrer(doc, CORRIGE)

    print("facteur voiture lu :", d.getCellRangeByName("E7").getValue(), "(0,142 attendu)")
    for n in range(4, 10):
        print(e.getCellRangeByName("A%d" % n).getString(), "→", e.getCellRangeByName("B%d" % n).getString())
    print("capture :", calc.capture(doc, "Estimation", PNG, plage="A1:C11"))
    doc.close(True)
