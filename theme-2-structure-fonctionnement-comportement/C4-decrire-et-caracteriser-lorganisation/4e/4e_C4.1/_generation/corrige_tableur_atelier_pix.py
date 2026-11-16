# -*- coding: utf-8 -*-
"""4e_C4.1 — atelier Pix, « Le tableau qui dit la vérité » : le corrigé fait PAR LibreOffice Calc
(règles d'or n°332 et n°336, 16/11/2026).

Les huit relevés de la page (Doc 1, `DONNEES` dans son script), tels qu'un élève les saisit dans Calc : l'heure en A,
l'humidité en B, la pompe en C, les titres en ligne 1, donc les valeurs d'humidité en B2:B9. Puis ce que l'atelier fait
faire : le tri par humidité croissante, et la moyenne de la journée.

Produit :
1. `atelier_pix_releves_corrige.ods` — les relevés triés, la moyenne par =MOYENNE(B2:B9) ;
2. `Images/capture_corrige_atelier_pix_tri.png` — la feuille, telle que Calc l'imprime.

Rejouer : python3 _generation/corrige_tableur_atelier_pix.py   (depuis le dossier du lot ; LibreOffice requis)
"""
import os
import re
import sys

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ICI, "..", "..", "..", "..", "_outils"))
import tableur_corrige as T  # noqa: E402

PAGE = os.path.join(ICI, "atelier_pix_crcn_jardin.html")
CORRIGE = os.path.join(ICI, "atelier_pix_releves_corrige.ods")
PNG = os.path.join(ICI, "Images", "capture_corrige_atelier_pix_tri.png")

# les relevés, lus dans la page elle-même : le corrigé ne peut pas diverger de l'exercice
src = open(PAGE, encoding="utf-8").read()
brut = re.search(r"const DONNEES = (\[\[.*?\]\]);", src).group(1)
DONNEES = [(h, int(v), p) for h, v, p in re.findall(r'\["([^"]+)",(\d+),"([^"]+)"\]', brut)]
assert len(DONNEES) == 8, DONNEES

with T.Calc() as calc:
    doc = calc.nouveau()
    T.en_francais(doc)
    f = doc.Sheets.getByIndex(0)
    f.setName("releves")
    for col, titre in zip("ABC", ("Heure", "Humidité (%)", "Pompe")):
        T.ecrire(f, "%s1" % col, titre)
    for i, (h, v, p) in enumerate(DONNEES):
        f.getCellRangeByName("A%d" % (2 + i)).setString(h)
        T.ecrire(f, "B%d" % (2 + i), v)
        T.ecrire(f, "C%d" % (2 + i), p)
    T.gras(f, "A1:C1")
    T.fond(f, "A1:C1", "#dfe7f7")
    f.getCellRangeByName("C1:C9").HoriJustify = 2                 # centré
    T.trier(f, "A1:C9", 1, croissant=True)                         # le tri de l'atelier : humidité croissante
    for r in range(2, 10):
        if f.getCellRangeByName("C%d" % r).getString() == "ON":
            T.fond(f, "A%d:C%d" % (r, r), "#fff3b0")
    T.ecrire(f, "A11", "Moyenne")
    T.gras(f, "A11")
    T.ecrire(f, "B11", "=AVERAGE(B2:B9)")
    T.format_fr(doc, f, "B11", "0,00")
    T.gras(f, "B11")
    T.fond(f, "B11", "#fff8d6")
    f.getCellRangeByName("C11").setString("=MOYENNE(B2:B9)")
    f.getCellRangeByName("C11").ParaLeftMargin = 300
    T.largeurs(f, {"A": 2.4, "B": 3.2, "C": 4.4})
    calc.enregistrer(doc, CORRIGE)
    print("ordre :", [f.getCellRangeByName("A%d" % r).getString() for r in range(2, 10)],
          "· moyenne :", f.getCellRangeByName("B11").getValue())
    print("capture :", calc.capture(doc, "releves", PNG, plage="A1:C11"))
    doc.close(True)
