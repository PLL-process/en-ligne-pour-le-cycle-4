# -*- coding: utf-8 -*-
"""3e_C4.3 — les fichiers de tableur de l'enquête « la nuit du cyclone », faits PAR LibreOffice Calc (règles n°332, n°336).

1. `donnees/mesures_station_48h_simulees.ods` : refait depuis le CSV. Le fichier d'avant gardait chaque nombre en TEXTE
   (« 1011.5 » écrit, pas compté) : MIN et MAX, que la correction conseille, y rendaient 0. Désormais : des nombres,
   des dates-heures.
2. `donnees/mesures_station_48h_corrige.ods` : le corrigé — les lignes colorées selon la vigilance, les réponses par
   formules (MIN, MAX, INDEX/EQUIV), et le graphique vent/pression du défi du Bonus.
3. Deux captures de Calc : `Images/capture_corrige_enquete_donnees.png`, `Images/capture_corrige_graphique_vent_pression.png`.

Rejouer : python3 _generation/corrige_tableur.py   (depuis le dossier du lot ; LibreOffice requis)
"""
import os
import sys

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ICI, "..", "..", "..", "..", "_outils"))
import tableur_corrige as T  # noqa: E402

CSV = os.path.join(ICI, "donnees", "mesures_station_48h_simulees.csv")
ODS = os.path.join(ICI, "donnees", "mesures_station_48h_simulees.ods")
CORRIGE = os.path.join(ICI, "donnees", "mesures_station_48h_corrige.ods")
COULEURS = {"verte": "#d9f7e0", "jaune": "#fff3b0", "orange": "#ffd2a6", "rouge": "#ffb3b8", "violette": "#e3ccff"}


def nombre_fr(doc, feuille, plage):
    """Une décimale, à la française : 966,8."""
    from com.sun.star.lang import Locale  # type: ignore
    loc = Locale("fr", "FR", "")
    nf = doc.NumberFormats
    cle = nf.queryKey("0,0", loc, False)
    if cle == -1:
        cle = nf.addNew("0,0", loc)
    feuille.getCellRangeByName(plage).NumberFormat = cle


def format_date(doc, feuille, plage):
    from com.sun.star.lang import Locale  # type: ignore
    loc = Locale("fr", "FR", "")
    nf = doc.NumberFormats
    cle = nf.queryKey("AAAA-MM-JJ HH:MM", loc, False)
    if cle == -1:
        cle = nf.addNew("AAAA-MM-JJ HH:MM", loc)
    feuille.getCellRangeByName(plage).NumberFormat = cle


with T.Calc() as calc:
    # 1. le fichier de l'élève, avec de vrais nombres
    doc = calc.ouvrir(CSV, separateur=";")
    T.en_francais(doc)
    f = doc.Sheets.getByIndex(0)
    f.setName("Mesures")
    format_date(doc, f, "A3:A50")
    T.gras(f, "A2:G2")
    T.largeurs(f, {"A": 4.2, "B": 2.8, "C": 2.2, "D": 2.4, "E": 2.8, "F": 2.2, "G": 2.4})
    calc.enregistrer(doc, ODS)

    # 2. le corrigé : les lignes de la vigilance, les réponses en formules
    for r in range(3, 51):
        v = f.getCellRangeByName("G%d" % r).getString()
        if v in COULEURS:
            T.fond(f, "A%d:G%d" % (r, r), COULEURS[v])
    lignes = [("Question", "Formule (dans Calc)", "Réponse"),
              ("1. Premier « rouge »", '=INDEX(A3:A50;MATCH("rouge";G3:G50;0))', None),
              ("2. Pression minimale (hPa)", "=MIN(E3:E50)", None),
              ("3. Rafale maximale (km/h)", "=MAX(D3:D50)", None),
              ("4a. Premier « orange »", '=INDEX(A3:A50;MATCH("orange";G3:G50;0))', None),
              ("4b. Premier « violette »", '=INDEX(A3:A50;MATCH("violette";G3:G50;0))', None),
              ("4. Écart (heures)", "=(K7-K6)*24", None)]
    for i, (q, formule, _) in enumerate(lignes):
        n = 2 + i
        T.ecrire(f, "I%d" % n, q)
        if i == 0:
            T.ecrire(f, "J%d" % n, formule)
            T.ecrire(f, "K%d" % n, "Réponse")
            continue
        f.getCellRangeByName("J%d" % n).setString(formule.replace(";", " ; ").replace("MATCH", "EQUIV"))
        T.ecrire(f, "K%d" % n, formule)
    format_date(doc, f, "K3")
    format_date(doc, f, "K6:K7")
    T.gras(f, "I2:K2")
    T.fond(f, "I2:K2", "#dfe7f7")
    T.fond(f, "K3:K8", "#fff8d6")
    T.gras(f, "K3:K8")
    T.largeurs(f, {"H": 0.6, "I": 5.2, "J": 9.4, "K": 3.8})

    # la feuille de la capture : les réponses et les lignes qui les portent, sans les 48 h entières
    doc.Sheets.insertNewByName("Corrigé", 1)
    c = doc.Sheets.getByName("Corrigé")
    T.ecrire(c, "A1", "Les réponses, lues par le tableur")
    T.gras(c, "A1")
    T.ecrire(c, "A3", "Question"); T.ecrire(c, "B3", "Réponse"); T.ecrire(c, "C3", "La formule, dans Calc")
    for i in range(1, 7):
        c.getCellRangeByName("A%d" % (3 + i)).setString(f.getCellRangeByName("I%d" % (2 + i)).getString())
        c.getCellRangeByName("B%d" % (3 + i)).setFormula("=$Mesures.K%d" % (2 + i))
        c.getCellRangeByName("C%d" % (3 + i)).setString(f.getCellRangeByName("J%d" % (2 + i)).getString())
    format_date(doc, c, "B4"); format_date(doc, c, "B7:B8")
    nombre_fr(doc, c, "B5")
    T.gras(c, "A3:E3"); T.fond(c, "A3:E3", "#dfe7f7")
    T.fond(c, "B4:B9", "#fff8d6"); T.gras(c, "B4:B9")
    T.ecrire(c, "A11", "Les lignes qui portent ces réponses")
    T.gras(c, "A11")
    for j, h in enumerate(["horodatage", "vent_kmh", "rafale_kmh", "pression_hpa", "vigilance"]):
        T.ecrire(c, "%s12" % "ABCDE"[j], h)
    T.gras(c, "A12:E12"); T.fond(c, "A12:E12", "#dfe7f7")
    cibles, deja = [], set()
    for v in ("orange", "rouge", "violette"):
        for r in range(3, 51):
            if f.getCellRangeByName("G%d" % r).getString() == v:
                cibles.append(r)
                break
    pmin = min(range(3, 51), key=lambda r: f.getCellRangeByName("E%d" % r).getValue())
    rmax = max(range(3, 51), key=lambda r: f.getCellRangeByName("D%d" % r).getValue())
    for r in sorted(set(cibles + [pmin, rmax])):
        n = 13 + len(deja)
        deja.add(r)
        for j, col in enumerate("ACDEG"):
            c.getCellRangeByName("%s%d" % ("ABCDE"[j], n)).setFormula("=$Mesures.%s%d" % (col, r))
        T.fond(c, "A%d:E%d" % (n, n), COULEURS[f.getCellRangeByName("G%d" % r).getString()])
    format_date(doc, c, "A13:A%d" % (12 + len(deja)))
    nombre_fr(doc, c, "D13:D%d" % (12 + len(deja)))
    T.largeurs(c, {"A": 5.4, "B": 4.4, "C": 3.0, "D": 3.4, "E": 6.2})

    # le graphique du défi du Bonus : le vent monte, la pression chute — la « pince ». Ses données sont un bloc d'un
    # seul tenant sur sa feuille (l'heure, le vent, la pression, lus dans « Mesures ») : chaque colonne, une courbe.
    doc.Sheets.insertNewByName("Graphique", 2)
    g = doc.Sheets.getByName("Graphique")
    for j, h in enumerate(("heure", "vent (km/h)", "pression (hPa)")):
        T.ecrire(g, "%s1" % "ABC"[j], h)
    for i in range(48):
        r = 3 + i
        g.getCellRangeByName("A%d" % (2 + i)).setFormula('=TEXT($Mesures.A%d;"DD"" août, ""HH""h""")' % r)
        g.getCellRangeByName("B%d" % (2 + i)).setFormula("=$Mesures.C%d" % r)
        g.getCellRangeByName("C%d" % (2 + i)).setFormula("=$Mesures.E%d" % r)
    from com.sun.star.awt import Rectangle  # type: ignore
    rect = Rectangle(); rect.X, rect.Y, rect.Width, rect.Height = 5500, 300, 24000, 13500
    g.Charts.addNewByName("VentPression", rect, (T.adresse(g, "A1:C49"),), True, True)
    ch = g.Charts.getByName("VentPression").getEmbeddedObject()
    ch.setDiagram(ch.createInstance("com.sun.star.chart.LineDiagram"))
    ch.HasMainTitle = True
    ch.Title.String = "48 h de mesures : le vent monte, la pression chute"
    ch.HasLegend = True
    d = ch.getDiagram()
    d.HasXAxisTitle = True; d.XAxisTitle.String = "jour et heure (28 et 29 août)"
    d.HasYAxisTitle = True; d.YAxisTitle.String = "vent (km/h)"
    d.HasSecondaryYAxis = True
    d.getDataRowProperties(1).Axis = 4
    d.HasSecondaryYAxisTitle = True; d.SecondYAxisTitle.String = "pression (hPa)"
    calc.enregistrer(doc, CORRIGE)

    # 3. les captures, telles que Calc les rend
    nombre_fr(doc, f, "E3:E50")
    nombre_fr(doc, f, "K4")
    print("capture enquête :", calc.capture(doc, "Corrigé", os.path.join(ICI, "Images", "capture_corrige_enquete_donnees.png"), plage="A1:E%d" % (12 + len(deja))))
    print("capture graphique :", calc.capture_graphique(doc, "Graphique", os.path.join(ICI, "Images", "capture_corrige_graphique_vent_pression.png"), largeur_px=1400))
    doc.close(True)
