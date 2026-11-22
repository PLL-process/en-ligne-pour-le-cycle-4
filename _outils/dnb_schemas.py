# -*- coding: utf-8 -*-
"""dnb_schemas.py — les algorigrammes de l'entraînement DNB « algorigrammes » (3e_C6.2), dessinés en SVG.

Pourquoi un module (audit du 21/11/2026) : la page montrait trois images extérieures, dont un algorigramme qui
dessinait les envois au gardien dans des rectangles alors que la planche du cours les range dans les entrées-sorties,
et dont le libellé « non » d'un losange était posé à droite d'une flèche qui descend. Chaque schéma est maintenant
décrit ici, une fois, avec les mêmes conventions partout :
  · terminal arrondi = DÉBUT / FIN ; rectangle = traitement interne (affectation, calcul) ;
  · losange = question à deux sorties étiquetées, chaque étiquette posée contre le segment qu'elle nomme ;
  · parallélogramme = donnée qui entre (lire un capteur) ou qui sort (envoyer, afficher, commander un actionneur) ;
  · une flèche qui rejoint le flux arrive sur un point de jonction, jamais sur le flanc d'un bloc.
Les SVG sont écrits dans la page (aucun fichier à côté : la page se copie seule sur un poste sans réseau) et n'utilisent
que des attributs de présentation — une feuille <style> dans un SVG en ligne s'appliquerait à toute la page.
Largeur 400 à 440 unités, texte de 16 unités : environ 13 px sur un téléphone de 390 px (le schéma y prend toute
la largeur de la carte), sans loupe ; la loupe l'agrandit.

  python3 _outils/dnb_schemas.py --fichiers   # réécrit Images/algorigramme_auto_test.svg (utilisé par le QCM du lot)
"""
from html import escape
import pathlib
import sys

FOND, CARTE = "#061330", "#0d2347"
TXT, SOUS = "#e8eefc", "#a9c1ec"
FL = "#8fb8ff"
OUI, NON, NOTE = "#8ff0ac", "#ffb3bc", "#ffd66b"
STY = {
    "term": ("#173666", "#7fb0ff"),
    "rect": ("#122a52", "#5b86d1"),
    "dec": ("#2b1a3f", "#b48ae6"),
    "io": ("#0d3320", "#5cc28a"),
    "slot": ("#2a2410", NOTE),
}
POLICE = "system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif"
LH = 20  # interligne du texte des blocs


def e(t):
    return escape(t, quote=True)


class Schema:
    def __init__(self, ident, w, titre, desc):
        self.id, self.w, self.titre, self.desc = ident, w, titre, desc
        self.fonds, self.traits, self.blocs, self.textes = [], [], [], []
        self.h = 0

    # ── textes ──────────────────────────────────────────────────────────
    def texte(self, x, y, t, taille=16, anchor="middle", couleur=TXT, gras=False, halo=False):
        lignes = t.split("\n")
        y0 = y - (len(lignes) - 1) * LH / 2
        attrs = (f'x="{x:g}" font-size="{taille}" text-anchor="{anchor}" fill="{couleur}"'
                 + (' font-weight="700"' if gras else "")
                 + (f' stroke="{FOND}" stroke-width="5" stroke-linejoin="round" paint-order="stroke"' if halo else ""))
        for i, l in enumerate(lignes):
            self.textes.append(f'<text {attrs} y="{y0 + i * LH + taille * 0.35:g}">{e(l)}</text>')

    def lbl(self, x, y, t, sorte="oui", anchor="middle"):
        couleur = {"oui": OUI, "non": NON, "note": NOTE, "sous": SOUS}[sorte]
        taille = 15 if sorte in ("oui", "non") else 14
        self.texte(x, y, t, taille, anchor, couleur, gras=sorte in ("oui", "non"), halo=True)

    # ── blocs ───────────────────────────────────────────────────────────
    def _bloc(self, forme, sorte, cx, cy, t, taille=16, pointille=False):
        f, s = STY[sorte]
        tirets = ' stroke-dasharray="6 5"' if pointille else ""
        self.blocs.append(forme.format(f=f, s=s, d=tirets))
        if t:
            self.texte(cx, cy, t, taille, couleur=NOTE if sorte == "slot" else TXT)

    def term(self, cx, y, w, h, t):
        self._bloc(f'<rect x="{cx - w / 2:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{h / 2:g}" '
                   'fill="{f}" stroke="{s}" stroke-width="2"/>', "term", cx, y + h / 2, t)
        return dict(cx=cx, top=y, bot=y + h, l=cx - w / 2, r=cx + w / 2, cy=y + h / 2)

    def rect(self, cx, y, w, h, t):
        self._bloc(f'<rect x="{cx - w / 2:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="6" '
                   'fill="{f}" stroke="{s}" stroke-width="2"/>', "rect", cx, y + h / 2, t)
        return dict(cx=cx, top=y, bot=y + h, l=cx - w / 2, r=cx + w / 2, cy=y + h / 2)

    def io(self, cx, y, w, h, t, k=14):
        x0, x1 = cx - w / 2, cx + w / 2
        pts = f"{x0 + k:g},{y:g} {x1:g},{y:g} {x1 - k:g},{y + h:g} {x0:g},{y + h:g}"
        self._bloc(f'<polygon points="{pts}" fill="{{f}}" stroke="{{s}}" stroke-width="2"/>', "io", cx, y + h / 2, t)
        return dict(cx=cx, top=y, bot=y + h, l=x0 + k / 2, r=x1 - k / 2, cy=y + h / 2)

    def dec(self, cx, top, hw, hh, t):
        cy = top + hh
        pts = f"{cx:g},{top:g} {cx + hw:g},{cy:g} {cx:g},{top + 2 * hh:g} {cx - hw:g},{cy:g}"
        self._bloc(f'<polygon points="{pts}" fill="{{f}}" stroke="{{s}}" stroke-width="2"/>', "dec", cx, cy, t)
        return dict(cx=cx, top=top, bot=top + 2 * hh, l=cx - hw, r=cx + hw, cy=cy)

    def slot(self, cx, y, w, h, t):
        self._bloc(f'<rect x="{cx - w / 2:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="8" '
                   'fill="{f}" stroke="{s}" stroke-width="2"{d}/>', "slot", cx, y + h / 2, t, 16, pointille=True)
        return dict(cx=cx, top=y, bot=y + h, l=cx - w / 2, r=cx + w / 2, cy=y + h / 2)

    def zone(self, x, y, w, h):
        self.fonds.append(f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="14" fill="none" '
                          f'stroke="#4a6fae" stroke-width="1.5" stroke-dasharray="7 6"/>')

    # ── traits ──────────────────────────────────────────────────────────
    def fl(self, *pts, pointe=True):
        d = "M" + " L".join(f"{x:g} {y:g}" for x, y in pts)
        m = f' marker-end="url(#{self.id}-p)"' if pointe else ""
        self.traits.append(f'<path d="{d}" fill="none" stroke="{FL}" stroke-width="2.2" '
                           f'stroke-linejoin="round"{m}/>')

    def point(self, x, y):
        self.traits.append(f'<circle cx="{x:g}" cy="{y:g}" r="4.5" fill="{FL}"/>')

    # ── rendu ───────────────────────────────────────────────────────────
    def svg(self, fichier=False):
        ns = ' xmlns="http://www.w3.org/2000/svg"' if fichier else ""
        haut = " haut" if self.h > 1.6 * self.w else ""
        tete = (f'<svg{ns} class="algo-svg{haut}" viewBox="0 0 {self.w:g} {self.h:g}" role="img" '
                f'aria-labelledby="{self.id}-t {self.id}-d" font-family="{POLICE}">'
                f'<title id="{self.id}-t">{e(self.titre)}</title><desc id="{self.id}-d">{e(self.desc)}</desc>'
                f'<defs><marker id="{self.id}-p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" '
                f'markerHeight="11" markerUnits="userSpaceOnUse" orient="auto">'
                f'<path d="M0 0 L10 5 L0 10 z" fill="{FL}"/></marker></defs>'
                f'<rect width="{self.w:g}" height="{self.h:g}" rx="14" fill="{FOND}"/>')
        return tete + "".join(self.fonds + self.traits + self.blocs + self.textes) + "</svg>"


# ═══════════════════════════════════════════════════════════════════════
# Les schémas
# ═══════════════════════════════════════════════════════════════════════

def ventilateur():
    """Exercice 2 — un losange, deux branches, une valeur à suivre."""
    s = Schema("sv-ventilo", 400, "Algorigramme du ventilateur commandé par la température",
               "DÉBUT. Parallélogramme : lire la température T. Losange : T > 30 ? Branche « oui », à droite, qui "
               "descend vers le parallélogramme « allumer le ventilateur ». Branche « non », à gauche, qui descend vers "
               "le parallélogramme « éteindre le ventilateur ». Les deux chemins se rejoignent, puis FIN.")
    cx = 200
    d = s.term(cx, 18, 130, 40, "DÉBUT")
    s.fl((cx, d["bot"]), (cx, 88))
    l = s.io(cx, 88, 250, 46, "lire la température T")
    s.fl((cx, l["bot"]), (cx, 162))
    q = s.dec(cx, 162, 100, 52, "T > 30 ?")
    r = s.io(300, 318, 170, 58, "allumer le\nventilateur")
    g = s.io(100, 318, 170, 58, "éteindre le\nventilateur")
    s.fl((q["r"], q["cy"]), (300, 318))
    s.fl((q["l"], q["cy"]), (100, 318))
    s.lbl(312, 270, "oui", "oui", "start")
    s.lbl(88, 270, "non", "non", "end")
    j = 404
    s.fl((100, g["bot"]), (100, j), (cx - 6, j))
    s.fl((300, r["bot"]), (300, j), (cx + 6, j))
    s.point(cx, j)
    s.fl((cx, j), (cx, 432))
    f = s.term(cx, 432, 130, 40, "FIN")
    s.h = f["bot"] + 18
    return s.svg()


def boucle_retour():
    """Exercice 8 — une flèche qui remonte."""
    s = Schema("sv-remonte", 380, "Algorigramme d'un compteur qui compte jusqu'à 3",
               "DÉBUT. Rectangle : c ← 0. La flèche descend jusqu'à un point de jonction, puis vers le rectangle "
               "c ← c + 1, puis vers le losange : c < 3 ? La branche « oui » part à gauche du losange, remonte le long "
               "du bord gauche et rejoint le point de jonction placé juste au-dessus du rectangle c ← c + 1. La "
               "branche « non » descend vers le parallélogramme « afficher c », puis FIN.")
    cx = 220
    d = s.term(cx, 18, 130, 40, "DÉBUT")
    s.fl((cx, d["bot"]), (cx, 86))
    a = s.rect(cx, 86, 150, 44, "c ← 0")
    j = 168
    s.fl((cx, a["bot"]), (cx, j), pointe=False)
    s.point(cx, j)
    s.fl((cx, j), (cx, 196))
    b = s.rect(cx, 196, 170, 44, "c ← c + 1")
    s.fl((cx, b["bot"]), (cx, 270))
    q = s.dec(cx, 270, 92, 50, "c < 3 ?")
    s.fl((q["l"], q["cy"]), (56, q["cy"]), (56, j), (cx - 6, j))
    s.lbl(92, q["cy"] - 15, "oui", "oui")
    s.fl((cx, q["bot"]), (cx, 404))
    s.lbl(cx + 13, 386, "non", "non", "start")
    o = s.io(cx, 404, 180, 44, "afficher c")
    s.fl((cx, o["bot"]), (cx, 476))
    f = s.term(cx, 476, 130, 40, "FIN")
    s.h = f["bot"] + 18
    return s.svg()


def boucle_jamais():
    """Exercice 14 — la boucle qui ne tourne pas : tracer le chemin et la sortie."""
    s = Schema("sv-jamais", 400, "Algorigramme d'une boucle qui commence avec i = 10",
               "DÉBUT. Rectangle : i ← 10. La flèche descend jusqu'à un point de jonction, puis vers le losange : "
               "i < 5 ? La branche « oui » descend vers le parallélogramme « afficher i », puis vers le rectangle "
               "i ← i + 1, puis repart à gauche, remonte et rejoint le point de jonction au-dessus du losange. La "
               "branche « non » part à droite du losange et descend jusqu'au terminal FIN, en bas à droite.")
    cx = 190
    d = s.term(cx, 18, 130, 40, "DÉBUT")
    s.fl((cx, d["bot"]), (cx, 86))
    a = s.rect(cx, 86, 150, 44, "i ← 10")
    j = 160
    s.fl((cx, a["bot"]), (cx, j), pointe=False)
    s.point(cx, j)
    s.fl((cx, j), (cx, 184))
    q = s.dec(cx, 184, 88, 50, "i < 5 ?")
    s.fl((cx, q["bot"]), (cx, 318))
    s.lbl(cx + 13, 302, "oui", "oui", "start")
    o = s.io(cx, 318, 170, 44, "afficher i")
    s.fl((cx, o["bot"]), (cx, 390))
    b = s.rect(cx, 390, 160, 44, "i ← i + 1")
    s.fl((cx, b["bot"]), (cx, 462), (36, 462), (36, j), (cx - 6, j))
    s.fl((q["r"], q["cy"]), (340, q["cy"]), (340, 484))
    s.lbl(310, q["cy"] - 15, "non", "non")
    f = s.term(340, 484, 96, 40, "FIN")
    s.h = f["bot"] + 18
    return s.svg()


def autotest(variante="complet", ident=None, objet="organe", nb=4, final="bilan"):
    """L'auto-test de la station (exercices 17 et 19, correction) et sa version du rappel (deux voyants).

    variante : « trous » (emplacements ①②③ à choisir, sans la mise à zéro), « complet » (sans annotation),
    « annote » (exemple guidé de la correction, avec deux repères écrits).
    final : « bilan » (décision après la boucle, deux envois au gardien) ou « afficher » (un seul affichage)."""
    W, cx = 440, 220
    trous, annote = variante == "trous", variante == "annote"
    pluriel = "organes" if objet == "organe" else "voyants"
    if final == "bilan":
        titre = ("Algorigramme de l'auto-test du matin, à compléter" if trous
                 else "Algorigramme de l'auto-test du matin de la station")
    else:
        titre = "Algorigramme d'une station qui teste ses deux voyants"
    s = Schema(ident or f"sv-auto-{variante}", W, titre, "")
    desc = []
    y = 16
    d = s.term(cx, y, 190, 40, "DÉBUT — 7 h 00" if final == "bilan" else "DÉBUT")
    desc.append("DÉBUT à 7 h 00." if final == "bilan" else "DÉBUT.")
    y = d["bot"] + 28
    s.fl((cx, d["bot"]), (cx, y))
    if trous:
        z1 = s.slot(cx, y, 190, 44, "①")
        desc.append("Emplacement ① : un cadre vide en pointillés, entre DÉBUT et le début de la boucle.")
    else:
        z1 = s.rect(cx, y, 190, 44, "defauts ← 0")
        desc.append("Rectangle : defauts ← 0, avant la boucle.")
        if annote:
            s.lbl(cx + 104, y + 22, "une seule fois,\navant la boucle", "note", "start")
    y = z1["bot"]
    zone_haut = y + 22
    j1 = zone_haut + 28
    s.fl((cx, y), (cx, j1), pointe=False)
    s.point(cx, j1)
    y = j1 + 26
    s.fl((cx, j1), (cx, y))
    if trous:
        z2 = s.slot(cx, y, 190, 44, "②")
        desc.append(f"La boucle commence. Emplacement ② : un cadre vide en pointillés, au début de chaque tour, "
                    f"juste avant « {objet} suivant de la liste ».")
        y = z2["bot"] + 26
        s.fl((cx, z2["bot"]), (cx, y))
    nxt = s.rect(cx, y, 220, 52, f"{objet} suivant\nde la liste")
    if not trous:
        desc.append(f"La boucle commence. Rectangle : {objet} suivant de la liste.")
    y = nxt["bot"] + 28
    s.fl((cx, nxt["bot"]), (cx, y))
    question = f"l'{objet} répond-il\ncorrectement ?" if objet == "organe" else f"le {objet}\nfonctionne-t-il ?"
    q1 = s.dec(cx, y, 118, 56, question)
    y = q1["bot"] + 32
    s.fl((cx, q1["bot"]), (cx, y))
    s.lbl(cx + 13, q1["bot"] + 16, "non", "non", "start")
    inc = s.rect(cx, y, 230, 44, "defauts ← defauts + 1")
    j2 = inc["bot"] + 30
    s.fl((cx, inc["bot"]), (cx, j2), pointe=False)
    s.fl((q1["r"], q1["cy"]), (414, q1["cy"]), (414, j2), (cx + 6, j2))
    s.lbl(376, q1["cy"] - 15, "oui", "oui")
    s.point(cx, j2)
    desc.append(f"Losange : {question.replace(chr(10), ' ')} Branche « non », vers le bas : rectangle "
                f"defauts ← defauts + 1. Branche « oui », à droite : elle contourne ce rectangle sans rien compter. "
                f"Les deux chemins se rejoignent en un point.")
    y = j2 + 28
    s.fl((cx, j2), (cx, y))
    q2 = s.dec(cx, y, 104, 52, f"reste-t-il\nun {objet} ?")
    s.fl((q2["l"], q2["cy"]), (24, q2["cy"]), (24, j1), (cx - 6, j1))
    s.lbl(70, q2["cy"] - 15, "oui", "oui")
    zone_bas = q2["bot"] + 18
    s.zone(12, zone_haut, W - 24, zone_bas - zone_haut)
    s.lbl(20, zone_haut - 9, "↻ la boucle", "sous", "start")
    desc.append(f"Losange : reste-t-il un {objet} ? Branche « oui », à gauche : elle remonte et rejoint le point "
                f"placé en haut de la boucle. Branche « non », vers le bas : on sort de la boucle, cadre en "
                f"pointillés qui entoure toute la partie répétée, une fois pour chacun des {nb} {pluriel}.")
    y = zone_bas + 30
    s.fl((cx, q2["bot"]), (cx, y))
    s.lbl(cx + 13, q2["bot"] + 16, "non", "non", "start")
    if trous:
        z3 = s.slot(cx, y, 190, 44, "③")
        desc.append("Emplacement ③ : un cadre vide en pointillés, après la boucle, avant la décision finale.")
        y = z3["bot"] + 26
        s.fl((cx, z3["bot"]), (cx, y))
    if final == "bilan":
        q3 = s.dec(cx, y, 108, 46, "defauts = 0 ?")
        if annote:
            s.lbl(16, q3["top"] + 6, "une décision,\naprès la boucle", "note", "start")
        yb = q3["cy"] + 64
        ok = s.io(328, yb, 196, 72, "envoyer au gardien\n« station\nopérationnelle »")
        ko = s.io(112, yb, 196, 72, "envoyer au gardien\n« défaut sur\nN organe(s) »")
        s.fl((q3["r"], q3["cy"]), (328, yb))
        s.fl((q3["l"], q3["cy"]), (112, yb))
        s.lbl(341, q3["cy"] + 30, "oui", "oui", "start")
        s.lbl(99, q3["cy"] + 30, "non", "non", "end")
        j3 = ok["bot"] + 26
        s.fl((112, ko["bot"]), (112, j3), (cx - 6, j3))
        s.fl((328, ok["bot"]), (328, j3), (cx + 6, j3))
        s.point(cx, j3)
        y = j3 + 26
        s.fl((cx, j3), (cx, y))
        desc.append("Après la boucle, losange : defauts = 0 ? Branche « oui », à droite : parallélogramme « envoyer au "
                    "gardien : station opérationnelle ». Branche « non », à gauche : parallélogramme « envoyer au "
                    "gardien : défaut sur N organe(s) ». Les deux chemins se rejoignent, puis FIN.")
    else:
        o = s.io(cx, y, 220, 46, "afficher defauts")
        y = o["bot"] + 28
        s.fl((cx, o["bot"]), (cx, y))
        desc.append("Après la boucle, parallélogramme : afficher defauts. Puis FIN.")
    f = s.term(cx, y, 130, 40, "FIN")
    s.h = f["bot"] + 18
    if annote:
        desc.append("Deux repères sont écrits sur le schéma : « une seule fois, avant la boucle » à côté de "
                    "defauts ← 0, et « une décision, après la boucle » à côté du dernier losange.")
    s.desc = " ".join(desc)
    return s


def boucle_choix(ident, titre, lecture, question, oui, non, desc):
    """Lampadaire (24), porte (28), abri à vélos (épreuve) : on lit, on décide, on commande, on recommence."""
    s = Schema(ident, 440, titre, desc)
    cx = 230
    d = s.term(cx, 16, 130, 40, "DÉBUT")
    j = 84
    s.fl((cx, d["bot"]), (cx, j), pointe=False)
    s.point(cx, j)
    s.fl((cx, j), (cx, 108))
    nl = lecture.count("\n") + 1
    l = s.io(cx, 108, 300, 30 + LH * nl, lecture)
    s.fl((cx, l["bot"]), (cx, l["bot"] + 28))
    q = s.dec(cx, l["bot"] + 28, 114, 56, question)
    yb = q["cy"] + 74
    r = s.io(340, yb, 168, 58, oui)
    g = s.io(120, yb, 168, 58, non)
    s.fl((q["r"], q["cy"]), (340, yb))
    s.fl((q["l"], q["cy"]), (120, yb))
    s.lbl(353, q["cy"] + 36, "oui", "oui", "start")
    s.lbl(107, q["cy"] + 36, "non", "non", "end")
    j2 = r["bot"] + 26
    s.fl((120, g["bot"]), (120, j2), (cx - 6, j2))
    s.fl((340, r["bot"]), (340, j2), (cx + 6, j2))
    s.point(cx, j2)
    yr = j2 + 30
    s.fl((cx, j2), (cx, yr), (16, yr), (16, j), (cx - 6, j))
    s.lbl(28, yr - 14, "on recommence", "sous", "start")
    s.h = yr + 20
    return s.svg()


def chaine(ident, titre, desc, lecture, tests, dernier=None, boucle=True, note_dernier=None):
    """Serre (23) et tri (26) : des tests en cascade ; chaque « oui » commande une action à droite."""
    s = Schema(ident, 440, titre, desc)
    cx, xb = 150, 426
    d = s.term(cx, 16, 130, 40, "DÉBUT")
    j = 84
    if boucle:
        s.fl((cx, d["bot"]), (cx, j), pointe=False)
        s.point(cx, j)
        s.fl((cx, j), (cx, 108))
        y = 108
    else:
        y = 84
        s.fl((cx, d["bot"]), (cx, y))
    nl = lecture.count("\n") + 1
    l = s.io(cx, y, 236, 30 + LH * nl, lecture)
    y = l["bot"] + 28
    s.fl((cx, l["bot"]), (cx, y))
    bus = None
    for i, (question, action) in enumerate(tests):
        q = s.dec(cx, y, 88, 48, question)
        nl = action.count("\n") + 1
        h = 30 + LH * nl
        a = s.io(338, q["cy"] - h / 2, 160, h, action)
        s.fl((q["r"], q["cy"]), (a["l"] - 4, q["cy"]))
        s.lbl((q["r"] + a["l"]) / 2 - 2, q["cy"] - 15, "oui", "oui")
        if bus is None:
            s.fl((a["r"] + 4, q["cy"]), (xb, q["cy"]), pointe=False)
            bus = q["cy"]
        else:
            s.fl((a["r"] + 4, q["cy"]), (xb - 6, q["cy"]))
            s.point(xb, q["cy"])
        y = q["bot"] + 34
        s.lbl(cx + 13, q["bot"] + 17, "non", "non", "start")
        if i < len(tests) - 1:
            s.fl((cx, q["bot"]), (cx, y))
        else:
            dernier_bas = q["bot"]
    if dernier:
        s.fl((cx, dernier_bas), (cx, y))
        z = s.slot(cx, y, 200, 48, dernier)
        jb = z["bot"] + 28
        s.fl((cx, z["bot"]), (cx, jb), pointe=False)
    else:
        jb = dernier_bas + (104 if note_dernier else 40)
        s.fl((cx, dernier_bas), (cx, jb), pointe=False)
        if note_dernier:
            s.lbl(cx + 12, dernier_bas + 62, note_dernier, "note", "start")
    s.fl((xb, bus), (xb, jb), (cx + 6, jb))
    s.point(cx, jb)
    if boucle:
        yr = jb + 30
        s.fl((cx, jb), (cx, yr), (18, yr), (18, j), (cx - 6, j))
        s.lbl(30, yr - 14, "on recommence", "sous", "start")
        s.h = yr + 20
    else:
        s.fl((cx, jb), (cx, jb + 26))
        f = s.term(cx, jb + 26, 130, 40, "FIN")
        s.h = f["bot"] + 18
    return s.svg()


# ── les schémas de la manche 4 et de l'épreuve ──────────────────────────
def lampadaire():
    return boucle_choix(
        "sv-lampe", "Algorigramme d'un lampadaire commandé par la nuit et la présence",
        "lire : fait-il nuit ?\nune présence est-elle détectée ?", "nuit ET\nprésence ?",
        "allumer\nla lampe", "éteindre\nla lampe",
        "DÉBUT. Point de jonction. Parallélogramme : lire s'il fait nuit et si une présence est détectée. Losange : "
        "nuit ET présence ? Branche « oui », à droite : parallélogramme « allumer la lampe ». Branche « non », à "
        "gauche : parallélogramme « éteindre la lampe ». Les deux chemins se rejoignent, puis une flèche repart à "
        "gauche, remonte et rejoint le point placé avant la lecture : on recommence à chaque mesure.")


def porte():
    return boucle_choix(
        "sv-porte", "Algorigramme d'une porte automatique",
        "lire la présence\ndans le passage", "présence ?",
        "ouvrir\nla porte", "fermer\nla porte",
        "DÉBUT. Point de jonction. Parallélogramme : lire la présence dans le passage. Losange : présence ? Branche "
        "« oui », à droite : parallélogramme « ouvrir la porte ». Branche « non », à gauche : parallélogramme « fermer "
        "la porte ». Les deux chemins se rejoignent, puis une flèche repart à gauche, remonte et rejoint le point "
        "placé avant la lecture : la présence est relue à chaque tour.")


def abri():
    return boucle_choix(
        "sv-abri", "Algorigramme de l'éclairage de l'abri à vélos",
        "lire la luminosité L (en lux)\net la présence d'un usager", "L < 80 ET\nprésence ?",
        "allumer\nla lampe", "éteindre\nla lampe",
        "DÉBUT. Point de jonction. Parallélogramme : lire la luminosité L, en lux, et la présence d'un usager. "
        "Losange : L < 80 ET présence ? Branche « oui », à droite : parallélogramme « allumer la lampe ». Branche "
        "« non », à gauche : parallélogramme « éteindre la lampe ». Les deux chemins se rejoignent, puis une flèche "
        "repart à gauche, remonte et rejoint le point placé avant la lecture : le contrôleur recommence une mesure "
        "chaque seconde.")


def serre():
    return chaine(
        "sv-serre", "Algorigramme du chauffage d'une serre à deux seuils",
        "DÉBUT. Point de jonction. Parallélogramme : lire la température T. Premier losange : T < 18 ? Branche "
        "« oui », à droite : parallélogramme « allumer le chauffage ». Branche « non », vers le bas : second losange, "
        "T > 22 ? Branche « oui », à droite : parallélogramme « éteindre le chauffage ». Branche « non », vers le bas : "
        "aucune commande, une note dit que le chauffage garde son état. Tous les chemins se rejoignent en bas, puis une "
        "flèche repart à gauche, remonte et rejoint le point placé avant la lecture : on recommence.",
        "lire la\ntempérature T", [("T < 18 ?", "allumer le\nchauffage"), ("T > 22 ?", "éteindre le\nchauffage")],
        note_dernier="aucune commande :\nle chauffage garde\nson état")


def tri():
    return chaine(
        "sv-tri", "Algorigramme du tri des déchets, à compléter",
        "DÉBUT. Parallélogramme : lire la matière de l'objet. Premier losange : métal ? « oui », à droite : "
        "parallélogramme « vers le bac métal ». « non », vers le bas : second losange, plastique ? « oui », à droite : "
        "« vers le bac plastique ». « non », vers le bas : troisième losange, verre ? « oui », à droite : « vers le "
        "bac verre ». « non », vers le bas : un cadre vide en pointillés marqué « ? », à compléter. Tous les chemins "
        "se rejoignent en bas, puis FIN.",
        "lire la matière\nde l'objet",
        [("métal ?", "vers le bac\n« métal »"), ("plastique ?", "vers le bac\n« plastique »"),
         ("verre ?", "vers le bac\n« verre »")],
        dernier="?", boucle=False)


def icone(forme):
    """Petite forme pour les propositions des exercices 3 et 4 (décorative : le texte la nomme)."""
    f, s_ = {"terminal": STY["term"], "rectangle": STY["rect"], "losange": STY["dec"],
             "parallelogramme": STY["io"]}[forme]
    corps = {
        "terminal": f'<rect x="3" y="5" width="46" height="22" rx="11" fill="{f}" stroke="{s_}" stroke-width="2"/>',
        "rectangle": f'<rect x="3" y="5" width="46" height="22" rx="2" fill="{f}" stroke="{s_}" stroke-width="2"/>',
        "losange": f'<polygon points="26,2 50,16 26,30 2,16" fill="{f}" stroke="{s_}" stroke-width="2"/>',
        "parallelogramme": f'<polygon points="12,5 50,5 40,27 2,27" fill="{f}" stroke="{s_}" stroke-width="2"/>',
    }[forme]
    return (f'<svg class="icone-forme" viewBox="0 0 52 32" width="52" height="32" aria-hidden="true" '
            f'focusable="false" data-loupe="non">{corps}</svg>')


SCHEMAS = {
    "ventilateur": ventilateur,
    "remonte": boucle_retour,
    "jamais": boucle_jamais,
    "auto_trous": lambda: autotest("trous").svg(),
    "auto_complet": lambda: autotest("complet", ident="sv-auto-complet").svg(),
    "auto_annote": lambda: autotest("annote", ident="sv-auto-annote").svg(),
    "voyants": lambda: autotest("complet", ident="sv-voyants", objet="voyant", nb=2, final="afficher").svg(),
    "lampadaire": lampadaire,
    "porte": porte,
    "abri": abri,
    "serre": serre,
    "tri": tri,
}


def ecrire_fichiers():
    """L'algorigramme de l'auto-test sert aussi au QCM du lot (question « La flèche de retour ») : son fichier est le
    même dessin que l'exemple guidé de la page."""
    lot = (pathlib.Path(__file__).resolve().parents[1] / "theme-2-structure-fonctionnement-comportement"
           / "C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.2/Images")
    s = autotest("annote", ident="auto")
    (lot / "algorigramme_auto_test.svg").write_text(s.svg(fichier=True) + "\n", encoding="utf-8")
    print("Images/algorigramme_auto_test.svg réécrit")


if __name__ == "__main__":
    if "--fichiers" in sys.argv:
        ecrire_fichiers()
    else:
        print(__doc__)
