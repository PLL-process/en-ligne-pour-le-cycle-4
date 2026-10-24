# -*- coding: utf-8 -*-
"""Insère (ou remet à jour) le volet « Pour aller plus loin : le pont en H » dans les deux pages de 3e_C9.2 qui portent la planche des trois cas :
la page tout-en-un et la page 1 (le générateur des quatre pages est en panne sur main : elles se maintiennent à la main, donc ici).

    python3 inserer.py        (depuis n'importe où)

Les trois fragments voisins — pont_en_h.fragment (le volet : un morceau de page, pas une page), pont_en_h.css, pont_en_h.js (balise <script> comprise) — sont la source ; la page ne
se modifie qu'entre les marqueurs « pont_en_h : début / fin ». Relancé, le script redonne les pages à l'octet près."""
import pathlib

ICI = pathlib.Path(__file__).resolve().parent
LOT = ICI.parents[1]
PAGES = ["sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html", "sequence_3e_C9.2-C8.3_station_1_besoin-et-algorithme.html"]
HTML = (ICI / "pont_en_h.fragment").read_text(encoding="utf-8").rstrip("\n")
CSS = (ICI / "pont_en_h.css").read_text(encoding="utf-8").rstrip("\n")
JS = (ICI / "pont_en_h.js").read_text(encoding="utf-8").rstrip("\n")

M_HTML = ("<!-- pont_en_h : début -->", "<!-- pont_en_h : fin -->")
M_CSS = ("/* pont_en_h (style) : début */", "/* pont_en_h (style) : fin */")
ANCRE_HTML = '    <details class="approfondissement" style="margin:1rem 0">\n      <summary>🔎 Un même composant peut appartenir aux deux analyses</summary>'
ANCRE_CSS = "  /* Règle d'or n°29 — mode essentiel */"


def remplace_ou_insere(t, marques, corps, ancre):
    d, f = marques
    bloc = d + "\n" + corps + "\n" + f + "\n"
    if d in t:
        i = t.index(d)
        j = t.index(f, i) + len(f)
        if t[j:j + 1] == "\n":
            j += 1
        return t[:i] + bloc + t[j:]
    assert t.count(ancre) == 1, ("ancre introuvable ou multiple", ancre[:60])
    return t.replace(ancre, bloc + ancre)


for nom in PAGES:
    p = LOT / nom
    brut = p.read_bytes().decode("utf-8")
    eol = "\r\n" if "\r\n" in brut else "\n"
    t = brut.replace("\r\n", "\n")
    t = remplace_ou_insere(t, M_CSS, CSS, ANCRE_CSS)
    t = remplace_ou_insere(t, M_HTML, HTML + "\n" + JS, ANCRE_HTML)
    p.write_bytes(t.replace("\n", eol).encode("utf-8"))
    print("ok", nom)
