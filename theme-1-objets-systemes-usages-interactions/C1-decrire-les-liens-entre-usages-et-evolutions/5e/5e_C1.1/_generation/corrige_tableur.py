# -*- coding: utf-8 -*-
"""5e_C1.1 — le corrigé de l'activité 2 « Collecter, trier, analyser », fait PAR LibreOffice Calc
(règles d'or n°332 et n°336, 16/11/2026).

1. `releves_air_chengdu_corrige.ods` : le fichier de l'élève, feuille « releves » — les quatre anomalies colorées et
   annotées dans une colonne « note » (on les écarte du calcul, on les GARDE dans le fichier), les formules de la page
   sous la colonne ; feuille « Corrigé » — les anomalies, et ce que le tableur en dit, formule par formule.
2. `Images/capture_corrige_anomalies_moyennes.png` : la feuille « Corrigé », telle que Calc l'imprime.

Rejouer : python3 _generation/corrige_tableur.py   (depuis le dossier du lot ; LibreOffice requis)
"""
import os
import sys

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ICI, "..", "..", "..", "..", "_outils"))
import tableur_corrige as T  # noqa: E402

CSV = os.path.join(ICI, "releves_air_chengdu_simules.csv")
CORRIGE = os.path.join(ICI, "releves_air_chengdu_corrige.ods")
PNG = os.path.join(ICI, "Images", "capture_corrige_anomalies_moyennes.png")
ROUGE, ORANGE, JAUNE = "#ffc9cc", "#ffdcb0", "#fff3b0"

with T.Calc() as calc:
    doc = calc.ouvrir(CSV, separateur=";", decimale=",")
    T.en_francais(doc)
    r = doc.Sheets.getByIndex(0)
    r.setName("releves")
    T.gras(r, "A1:F1")
    T.ecrire(r, "F1", "note")
    # le numéro de ligne de chaque relevé, lu dans le CSV lui-même (Calc a fait de « 11:00 » une heure)
    with open(CSV, encoding="utf-8") as fic:
        lignes = {tuple(l.split(";")[:2]): n for n, l in enumerate(fic.read().splitlines()[1:], start=2)}
    T.format_fr(doc, r, "B2:B91", "HH:MM")
    T.format_fr(doc, r, "C2:E91", "0,0")

    # les quatre anomalies : repérées dans le fichier, colorées, annotées — jamais effacées
    def ligne(jour, heure):
        return lignes[(jour, heure)]
    n = ligne("mercredi", "11:00")
    T.fond(r, "A%d:F%d" % (n, n), ROUGE)
    T.ecrire(r, "F%d" % n, "impossible : une concentration n'est jamais négative — écartée du calcul")
    figees = [ligne("vendredi", "%02d:00" % h) for h in range(9, 15)]
    for n in figees:
        T.fond(r, "A%d:F%d" % (n, n), ORANGE)
    T.ecrire(r, "F%d" % figees[0], "capteur figé ? 23,7 six heures de suite — à signaler, vérifier l'appareil")
    n = ligne("lundi", "13:00")
    T.fond(r, "A%d:F%d" % (n, n), JAUNE)
    T.ecrire(r, "F%d" % n, "le relevé de 14 h manque (12 lignes ce jour-là) — on n'invente pas de mesure")
    n = ligne("dimanche", "16:00")
    T.fond(r, "A%d:F%d" % (n, n), ROUGE)
    T.ecrire(r, "F%d" % n, "virgule décalée : 25,1 devenu 251 — écartée du calcul")
    T.largeurs(r, {"A": 2.4, "B": 1.6, "C": 2.6, "D": 3.0, "E": 2.8, "F": 13.5})

    # les formules de la page, sous la colonne pm25_ug_m3
    # dans l'ordre de la page : la moyenne en C92 (« la cellule sous la colonne pm25_ug_m3 (ici C92) »), puis les autres
    FORMULES = [
        ("Moyenne, toutes les valeurs", "=AVERAGE(C2:C91)", "=MOYENNE(C2:C91)", "0,0"),
        ("Moyenne sans les valeurs fausses", '=AVERAGEIFS(C2:C91;C2:C91;">0";C2:C91;"<200")',
         '=MOYENNE.SI.ENS(C2:C91;C2:C91;">0";C2:C91;"<200")', "0,0"),
        ("Écart entre les deux moyennes", "=C92-C93", "=C92-C93", "0,0"),
        ("Maximum", "=MAX(C2:C91)", "=MAX(C2:C91)", "0,0"),
        ("Nombre de relevés", "=COUNT(C2:C91)", "=NB(C2:C91)", "0"),
        ("Lignes du lundi (13 attendues)", '=COUNTIF(A2:A91;"lundi")', '=NB.SI(A2:A91;"lundi")', "0"),
    ]
    for i, (titre, formule, lue, code) in enumerate(FORMULES):
        n = 92 + i
        T.ecrire(r, "B%d" % n, titre)
        r.getCellRangeByName("B%d" % n).HoriJustify = 3          # à droite, collé au résultat
        T.ecrire(r, "C%d" % n, formule)
        T.format_fr(doc, r, "C%d" % n, code)
        r.getCellRangeByName("D%d" % n).setString(lue)
    T.gras(r, "C92:C97")
    T.fond(r, "C92:C97", "#fff8d6")

    # la feuille de la capture : les anomalies, puis ce que le tableur en dit
    doc.Sheets.insertNewByName("Corrigé", 0)
    c = doc.Sheets.getByName("Corrigé")
    T.ecrire(c, "A1", "Les quatre anomalies du fichier, puis les deux moyennes")
    T.gras(c, "A1")
    for col, titre in zip("ABCD", ("jour", "heure", "pm25 (µg/m³)", "Ce qui ne va pas")):
        T.ecrire(c, "%s3" % col, titre)
    T.gras(c, "A3:D3")
    T.fond(c, "A3:D3", "#dfe7f7")
    n = ligne("mercredi", "11:00")
    ANOM = [("mercredi", "11:00", "=$releves.C%d" % n, "impossible : une concentration n'est jamais négative", ROUGE),
            ("vendredi", "09:00 → 14:00", "=$releves.C%d" % figees[0],
             "la même valeur six heures de suite : capteur figé, à vérifier", ORANGE),
            ("lundi", "14:00", "(aucune ligne)", "relevé manquant : on le signale, on n'invente rien", JAUNE),
            ("dimanche", "16:00", "=$releves.C%d" % ligne("dimanche", "16:00"),
             "virgule décalée : 25,1 devenu 251", ROUGE)]
    for i, (jour, heure, val, quoi, coul) in enumerate(ANOM):
        k = 4 + i
        T.ecrire(c, "A%d" % k, jour)
        c.getCellRangeByName("B%d" % k).setString(heure)
        T.ecrire(c, "C%d" % k, val)
        T.ecrire(c, "D%d" % k, quoi)
        T.fond(c, "A%d:D%d" % (k, k), coul)
    T.format_fr(doc, c, "C4:C7", "0,0")
    c.getCellRangeByName("C4:C7").HoriJustify = 3
    for col, titre in zip("ABCD", ("Ce que le tableur calcule", "", "Résultat", "La formule, dans Calc")):
        T.ecrire(c, "%s9" % col, titre)
    T.gras(c, "A9:D9")
    T.fond(c, "A9:D9", "#dfe7f7")
    for i, (titre, _f, lue, code) in enumerate(FORMULES):
        k = 10 + i
        T.ecrire(c, "A%d" % k, titre)
        c.getCellRangeByName("A%d:B%d" % (k, k)).merge(True)
        T.ecrire(c, "C%d" % k, "=$releves.C%d" % (92 + i))
        T.format_fr(doc, c, "C%d" % k, code)
        c.getCellRangeByName("D%d" % k).setString(lue)
    T.gras(c, "C10:C15")
    T.fond(c, "C10:C11", "#fff8d6")
    c.getCellRangeByName("D4:D15").ParaLeftMargin = 300
    T.largeurs(c, {"A": 2.6, "B": 3.0, "C": 2.8, "D": 11.8})
    calc.enregistrer(doc, CORRIGE)

    for k in range(10, 16):
        print(c.getCellRangeByName("A%d" % k).getString(), "→", c.getCellRangeByName("C%d" % k).getValue())
    print("capture :", calc.capture(doc, "Corrigé", PNG, plage="A1:D15"))
    doc.close(True)
