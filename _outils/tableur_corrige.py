# -*- coding: utf-8 -*-
"""tableur_corrige.py — fabriquer le corrigé d'une activité de tableur AVEC LibreOffice Calc, et sa capture.

POURQUOI
--------
Règles d'or n°332 (15/11/2026) et n°336 (16/11/2026) : la correction d'une production faite avec un outil la montre
« telle que l'outil la rend », et donne son fichier. Pour le tableur, l'outil est LibreOffice Calc : ce module le pilote
sans écran (`soffice --headless`, par UNO), ouvre le fichier de l'élève, y fait ce que l'élève devait faire (formules,
tri, filtre, couleurs, graphique), enregistre le fichier corrigé (.ods) et exporte une feuille en PDF, puis en PNG
rogné : la capture est celle de Calc, pas un dessin qui lui ressemble.

UTILISATION (dans le générateur du lot, `_generation/corrige_tableur.py`)
-------------------------------------------------------------------------
    import sys; sys.path.insert(0, "<racine>/_outils"); import tableur_corrige as T
    with T.Calc() as calc:
        doc = calc.ouvrir("donnees/mesures.csv", separateur=";")      # ou un .ods / .xlsx
        f = doc.Sheets.getByIndex(0)
        T.ecrire(f, "H2", "=MIN(E2:E49)") ; T.fond(f, "A33:G33", "#ffd66b") ; T.gras(f, "A1:G1")
        calc.enregistrer(doc, "donnees/mesures_corrige.ods")
        calc.capture(doc, "Corrigé", "Images/capture_corrige.png", plage="A1:D12")
Le PNG est rogné à son contenu, à 2× (lisible au téléphone, zoomable).

Dépend de : LibreOffice (soffice, python3-uno), pdftoppm, Pillow.
"""
from __future__ import annotations

import os
import shutil
import socket
import subprocess
import tempfile
import time

import uno  # noqa: F401  (python3-uno, fourni avec LibreOffice)
from com.sun.star.beans import PropertyValue  # type: ignore
from com.sun.star.table import CellRangeAddress  # type: ignore
from com.sun.star.awt import Rectangle  # type: ignore


def pv(nom, valeur):
    p = PropertyValue()
    p.Name, p.Value = nom, valeur
    return p


def couleur(hexa: str) -> int:
    return int(hexa.lstrip("#"), 16)


def ecrire(feuille, ref: str, valeur):
    c = feuille.getCellRangeByName(ref)
    if isinstance(valeur, str) and valeur.startswith("="):
        c.setFormula(valeur)
    elif isinstance(valeur, (int, float)):
        c.setValue(valeur)
    else:
        c.setString(str(valeur))
    return c


def fond(feuille, plage: str, hexa: str):
    feuille.getCellRangeByName(plage).CellBackColor = couleur(hexa)


def gras(feuille, plage: str):
    feuille.getCellRangeByName(plage).CharWeight = 150.0          # com.sun.star.awt.FontWeight.BOLD


def largeurs(feuille, cm: dict):
    """{'A': 4.2, …} en centimètres."""
    cols = feuille.Columns
    for lettre, l in cm.items():
        cols.getByName(lettre).Width = int(l * 1000)


def en_francais(doc):
    """Le document en français : virgule décimale, dates à la française, comme sur l'ordinateur d'un élève."""
    from com.sun.star.lang import Locale  # type: ignore
    try:
        doc.CharLocale = Locale("fr", "FR", "")
    except Exception:
        pass


def mise_en_page(doc, feuille, paysage=True):
    """Pour la capture : ni en-tête ni pied de page, la plage tient sur une page en largeur."""
    st = doc.StyleFamilies.getByName("PageStyles").getByName(feuille.PageStyle)
    st.HeaderIsOn = False
    st.FooterIsOn = False
    if paysage and not st.IsLandscape:
        w, h = st.Width, st.Height
        st.IsLandscape = True
        st.Width, st.Height = h, w
    try:
        st.ScaleToPagesX = 1
        st.ScaleToPagesY = 0
    except Exception:
        pass


def adresse(feuille, plage: str) -> CellRangeAddress:
    return feuille.getCellRangeByName(plage).RangeAddress


class Calc:
    """LibreOffice sans écran, le temps d'un `with`."""

    def __init__(self):
        self.proc = None
        self.profil = tempfile.mkdtemp(prefix="lo-profil-")

    def __enter__(self):
        s = socket.socket()
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
        s.close()
        self.proc = subprocess.Popen(
            ["soffice", "--headless", "--invisible", "--norestore", "--nologo", "--nodefault",
             "-env:UserInstallation=file://" + self.profil,
             "--accept=socket,host=127.0.0.1,port=%d;urp;" % port],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        local = uno.getComponentContext()
        resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
        for _ in range(120):
            try:
                ctx = resolver.resolve("uno:socket,host=127.0.0.1,port=%d;urp;StarOffice.ComponentContext" % port)
                break
            except Exception:
                time.sleep(0.25)
        else:
            raise RuntimeError("LibreOffice ne répond pas")
        self.ctx = ctx
        self.desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        return self

    def __exit__(self, *exc):
        try:
            self.desktop.terminate()
        except Exception:
            pass
        if self.proc:
            try:
                self.proc.wait(timeout=20)
            except Exception:
                self.proc.kill()
        shutil.rmtree(self.profil, ignore_errors=True)

    def ouvrir(self, chemin: str, separateur: str = None):
        args = [pv("Hidden", True)]
        if chemin.lower().endswith(".csv"):
            # séparateur, guillemets, UTF-8 (76), première ligne 1 ; les nombres « 1011.5 » lus en anglais (en-US)
            sep = str(ord(separateur or ";"))
            args += [pv("FilterName", "Text - txt - csv (StarCalc)"),
                     pv("FilterOptions", "%s,34,76,1,,1033,false,true" % sep)]
        return self.desktop.loadComponentFromURL(uno.systemPathToFileUrl(os.path.abspath(chemin)), "_blank", 0, tuple(args))

    def nouveau(self):
        return self.desktop.loadComponentFromURL("private:factory/scalc", "_blank", 0, (pv("Hidden", True),))

    def enregistrer(self, doc, chemin: str):
        filtre = {".ods": "calc8", ".xlsx": "Calc MS Excel 2007 XML"}[os.path.splitext(chemin)[1].lower()]
        doc.storeToURL(uno.systemPathToFileUrl(os.path.abspath(chemin)), (pv("FilterName", filtre),))

    def capture_graphique(self, doc, feuille: str, png: str, largeur_px: int = 1400, index: int = 0):
        """Le graphique de la feuille, exporté en image par LibreOffice lui-même (le rendu de Calc)."""
        f = doc.Sheets.getByName(feuille)
        forme = f.DrawPage.getByIndex(index)
        gef = self.ctx.ServiceManager.createInstanceWithContext("com.sun.star.drawing.GraphicExportFilter", self.ctx)
        gef.setSourceDocument(forme)
        taille = forme.Size
        hauteur_px = int(largeur_px * taille.Height / taille.Width)
        donnees = uno.Any("[]com.sun.star.beans.PropertyValue", (pv("PixelWidth", largeur_px), pv("PixelHeight", hauteur_px)))
        os.makedirs(os.path.dirname(os.path.abspath(png)), exist_ok=True)
        uno.invoke(gef, "filter", ((pv("URL", uno.systemPathToFileUrl(os.path.abspath(png))), pv("MediaType", "image/png"),
                                    pv("FilterData", donnees)),))
        return (largeur_px, hauteur_px)

    def capture(self, doc, feuille: str, png: str, plage: str = None, dpi: int = 160):
        """La feuille (ou sa plage) exportée en PDF par Calc, puis en PNG rogné à son contenu."""
        from PIL import Image, ImageChops
        f = doc.Sheets.getByName(feuille)
        mise_en_page(doc, f)
        donnees = []
        if plage:
            donnees.append(pv("Selection", f.getCellRangeByName(plage)))
        else:
            donnees.append(pv("Selection", f))
        tmp = tempfile.mkdtemp(prefix="cap-")
        pdf = os.path.join(tmp, "c.pdf")
        filtre = uno.Any("[]com.sun.star.beans.PropertyValue", tuple(donnees))
        uno.invoke(doc, "storeToURL", (uno.systemPathToFileUrl(pdf),
                                        (pv("FilterName", "calc_pdf_Export"), pv("FilterData", filtre))))
        subprocess.run(["pdftoppm", "-png", "-r", str(dpi), "-f", "1", "-l", "1", pdf, os.path.join(tmp, "p")], check=True)
        brut = [x for x in os.listdir(tmp) if x.startswith("p") and x.endswith(".png")][0]
        im = Image.open(os.path.join(tmp, brut)).convert("RGB")
        fondb = Image.new("RGB", im.size, (255, 255, 255))
        boite = ImageChops.difference(im, fondb).getbbox()
        if boite:
            m = 18
            im = im.crop((max(0, boite[0] - m), max(0, boite[1] - m), min(im.width, boite[2] + m), min(im.height, boite[3] + m)))
        os.makedirs(os.path.dirname(os.path.abspath(png)), exist_ok=True)
        im.save(png, optimize=True)
        shutil.rmtree(tmp, ignore_errors=True)
        return im.size

    def graphique_lignes(self, doc, feuille: str, nom: str, plages: list, rect_cm: tuple, titre: str = "",
                         axe_secondaire: int = None, titres_axes: tuple = ("", "", "")):
        """Un graphique en lignes sur la feuille. plages : ['A1:A49', 'C1:C49', …] (la 1re = les abscisses).
        axe_secondaire : l'indice (1-based, parmi les séries) de la série portée par l'axe Y de droite."""
        f = doc.Sheets.getByName(feuille)
        x, y, l, h = rect_cm
        r = Rectangle()
        r.X, r.Y, r.Width, r.Height = int(x * 1000), int(y * 1000), int(l * 1000), int(h * 1000)
        adrs = tuple(adresse(f, p) for p in plages)
        f.Charts.addNewByName(nom, r, adrs, True, True)
        ch = f.Charts.getByName(nom).getEmbeddedObject()
        ch.setDiagram(ch.createInstance("com.sun.star.chart.LineDiagram"))
        if titre:
            ch.HasMainTitle = True
            ch.Title.String = titre
        d = ch.getDiagram()
        if titres_axes[0]:
            d.HasXAxisTitle = True
            d.XAxisTitle.String = titres_axes[0]
        if titres_axes[1]:
            d.HasYAxisTitle = True
            d.YAxisTitle.String = titres_axes[1]
        if axe_secondaire:
            d.HasSecondaryYAxis = True
            d.getDataRowProperties(axe_secondaire - 1).Axis = 4      # com.sun.star.chart.ChartAxisAssign.SECONDARY_Y
            if titres_axes[2]:
                d.HasSecondaryYAxisTitle = True
                d.SecondYAxisTitle.String = titres_axes[2]
        return ch
