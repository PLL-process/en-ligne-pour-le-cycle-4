# -*- coding: utf-8 -*-
"""legende_unites.py — règle d'or n°312 dans les schémas : la ligne « Unités : … » sous le dessin.

Un schéma est une zone à part entière, comme un tableau. Son texte se lit souvent seul (agrandi par la loupe,
ouvert comme image, repris dans un QCM), et ses étiquettes n'ont pas la place d'un nom entre parenthèses :
« batterie 12 V (volts) » déborde d'un bloc dessiné pour « batterie 12 V ». La forme retenue pour un schéma
est donc une ligne de légende, ajoutée sous le dessin, dans sa police et ses couleurs :

    Unités : V (volts) · mA (milliampères)

Seules y figurent les unités que le texte VISIBLE du dessin (<text>, <tspan>) écrit après un nombre sans
jamais les nommer. Le titre et la description (<title>, <desc>) ne comptent pas : l'œil ne les voit pas.

Ce que l'outil fait au dessin, et seulement cela :
  - il agrandit le viewBox vers le bas d'une bande (2,2 fois la taille de police médiane du dessin) ;
  - il allonge d'autant le rectangle de fond qui couvre tout le dessin, s'il y en a un (même couleur, même
    dégradé, mêmes coins arrondis) ;
  - il met à l'échelle l'attribut height du <svg> s'il est chiffré ;
  - il écrit la ligne, centrée, marquée data-legende-unites ; il ajoute la même phrase à la fin de <desc>.
Il est idempotent : une ligne déjà posée est retirée puis recalculée.

Usage :
    python3 _outils/legende_unites.py fichier.svg page.html…     pose ou met à jour
    python3 _outils/legende_unites.py --verifier fichier.svg…   dit ce qui changerait (sortie 1 si écart)
Dans une page HTML, chaque <svg> intégré est traité à part. Importé, `poser(svg)` rend le dessin modifié
(le générateur des ateliers de représentation l'appelle sur chacune de ses figures).
"""
from __future__ import annotations

import html
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_unites as CU  # noqa: E402

MARQUE = "data-legende-unites"
_RACINE = re.compile(r"<svg\b[^>]*>", re.S)
_LEGENDE = re.compile(r'<text\b[^>]*%s="ligne"[^>]*>.*?</text>' % MARQUE, re.S)


def texte_visible(svg):
    """Le texte que l'œil lit dans le dessin : <text> et <tspan>, chacun séparé de son voisin."""
    s = re.sub(r"<(title|desc|style|script|metadata)\b.*?</\1>", " ", svg, flags=re.S)
    s = _LEGENDE.sub(" ", s)
    morceaux = re.findall(r"<text\b[^>]*>(.*?)</text>", s, flags=re.S)
    return CU.plat(" ¦ ".join(html.unescape(re.sub(r"<[^>]+>", " ", m)) for m in morceaux))


def unites_sans_nom(svg):
    """[(symbole, nom)] : les unités écrites dans le dessin sans leur nom, dans leur ordre d'apparition."""
    return [(s, CU.NOMS[s][1]) for s, _ in CU.manques(texte_visible(svg))]


def phrase(unites):
    return "Unités : " + " · ".join("%s (%s)" % (s, n) for s, n in unites)


def _attr(balise, nom):
    m = re.search(r'\s%s\s*=\s*"([^"]*)"' % re.escape(nom), balise)
    return m.group(1) if m else None


def _remplacer_attr(balise, nom, valeur):
    if _attr(balise, nom) is None:
        return balise
    return re.sub(r'(\s%s\s*=\s*")[^"]*(")' % re.escape(nom), lambda m: m.group(1) + valeur + m.group(2), balise, count=1)


def _clair(couleur):
    """Vrai si la couleur (#rgb, #rrggbb) est claire ; None si on ne sait pas la lire."""
    m = re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", (couleur or "").strip())
    if not m:
        return None
    h = m.group(1)
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) > 140


def _num(v):
    try:
        return float(re.match(r"[\d.]+", v).group(0))
    except (TypeError, AttributeError, ValueError):
        return None


def retirer(svg):
    """Le dessin sans sa ligne de légende (ni la bande, ni la phrase dans <desc>), viewBox rendu."""
    racine = _RACINE.search(svg)
    if not racine or MARQUE not in svg:
        return svg
    bande = _attr(racine.group(0), MARQUE)
    s = _LEGENDE.sub("", svg)
    s = re.sub(r"\s*Unités : [^<]*(</desc>)", r"\1", s, count=1)
    if bande:
        b = float(bande)
        r = _RACINE.search(s).group(0)
        vb = [float(x) for x in _attr(r, "viewBox").split()]
        r2 = _remplacer_attr(r, "viewBox", "%g %g %g %g" % (vb[0], vb[1], vb[2], vb[3] - b))
        h = _attr(r, "height")
        if _num(h) and re.fullmatch(r"[\d.]+(px)?", h):
            r2 = _remplacer_attr(r2, "height", "%g" % round(float(_num(h)) * (vb[3] - b) / vb[3], 2))
        r2 = re.sub(r'\s%s="[^"]*"' % MARQUE, "", r2)
        s = s.replace(r, r2, 1)
        s = re.sub(r'(<rect\b[^>]*?)\s%s-fond="([\d.]+)"' % MARQUE, lambda m: _rendre_fond(m), s, count=1)
    return s


def _rendre_fond(m):
    balise, h = m.group(1), m.group(2)
    return _remplacer_attr(balise, "height", h)


def poser(svg, taille=None):
    """Le dessin avec sa ligne « Unités : … » (ou sans, si rien ne manque). `taille` : la taille de police que
    la feuille de style de la page donne au texte du dessin, quand elle l'impose (sinon : la médiane des
    tailles écrites dans le dessin)."""
    svg = retirer(svg)
    unites = unites_sans_nom(svg)
    racine = _RACINE.search(svg)
    if not unites or not racine:
        return svg
    r = racine.group(0)
    vb_txt = _attr(r, "viewBox")
    if not vb_txt:
        return svg
    x0, y0, w, h = (float(v) for v in vb_txt.replace(",", " ").split())
    tailles = [float(t) for t in re.findall(r'font-size\s*[=:]\s*"?\s*([\d.]+)', svg)]
    fs = taille or (round(statistics.median(tailles), 1) if tailles else 16)  # 16 : la taille par défaut d'un SVG
    bande = round(fs * 2.2, 1)
    # le fond qui couvre tout le dessin : on l'allonge
    corps = svg[racine.end():]
    fond = None
    for m in re.finditer(r"<rect\b[^>]*>", corps):
        b = m.group(0)
        bw, bh = _attr(b, "width"), _attr(b, "height")
        bx, by = _num(_attr(b, "x") or "0") or 0, _num(_attr(b, "y") or "0") or 0
        if bx == x0 and by == y0 and bw and bh and (bw == "100%" or _num(bw) == w) and (bh == "100%" or _num(bh) == h):
            fond = m
        break
    couleur_fond = _attr(fond.group(0), "fill") if fond else None
    clair = _clair(couleur_fond)
    if clair is None and couleur_fond and couleur_fond.startswith("url("):  # un dégradé : sa première couleur
        ident = re.search(r"url\(#([^)]+)\)", couleur_fond)
        grad = re.search(r'<(?:linear|radial)Gradient\b[^>]*id="%s".*?stop-color\s*[=:]\s*"?(#[0-9a-fA-F]{3,6})' % re.escape(ident.group(1)), svg, re.S) if ident else None
        clair = _clair(grad.group(1)) if grad else None
    if clair is None:
        clair = True
    # l'encre du dessin lui-même (la plus fréquente parmi celles qui se lisent sur ce fond) : la ligne suit ainsi
    # les règles d'impression du dessin, quand il en a (« text[fill=…]{fill:…} » pour le papier blanc)
    encres = [c for c in re.findall(r'<text\b[^>]*\sfill="(#[0-9a-fA-F]{3,6})"', svg) if _clair(c) is (not clair)]
    encre = max(sorted(set(encres)), key=encres.count) if encres else ("#3d4b66" if clair else "#c7d2e6")
    police = re.search(r"font-family\s*[=:]\s*(\"[^\"]*\"|'[^']*'|[^;\"'>]+)", svg)
    attr_police = ""
    if police:
        v = police.group(1).strip().strip('"')
        attr_police = ' font-family="%s"' % v.replace('"', "'")
    ligne = ('<text %s="ligne" x="%g" y="%g" text-anchor="middle" font-size="%g" fill="%s"%s>%s</text>'
             % (MARQUE, x0 + w / 2, round(y0 + h + bande * 0.62, 1), fs, encre, attr_police, html.escape(phrase(unites))))
    nouveau_corps = corps
    if fond:
        b = fond.group(0)
        if _attr(b, "height") == "100%":
            b2 = b
        else:
            b2 = _remplacer_attr(b, "height", "%g" % (h + bande))
            b2 = b2[:-2] + ' %s-fond="%g"/>' % (MARQUE, h) if b2.endswith("/>") else b2[:-1] + ' %s-fond="%g">' % (MARQUE, h)
        nouveau_corps = corps[:fond.start()] + b2 + corps[fond.end():]
    fin = nouveau_corps.rfind("</svg>")
    nouveau_corps = nouveau_corps[:fin] + ligne + nouveau_corps[fin:]
    r2 = _remplacer_attr(r, "viewBox", "%g %g %g %g" % (x0, y0, w, h + bande))
    hh = _attr(r, "height")
    if hh and re.fullmatch(r"[\d.]+(px)?", hh):
        r2 = _remplacer_attr(r2, "height", "%g" % round(_num(hh) * (h + bande) / h, 2))
    r2 = r2[:-1].rstrip("/") + ' %s="%g">' % (MARQUE, bande) if not r2.endswith("/>") else r2
    s = svg[:racine.start()] + r2 + nouveau_corps
    # la même phrase pour qui écoute le dessin
    s = re.sub(r"(<desc\b[^>]*>)(.*?)(</desc>)", lambda m: m.group(1) + m.group(2).rstrip() + " " + html.escape(phrase(unites)) + "." + m.group(3), s, count=1, flags=re.S)
    return s


def _taille_css(src, svg):
    """La taille que la feuille de style de la page impose au texte de ce dessin (« .classe text{font-size:17px} »)."""
    classes = (_attr(_RACINE.search(svg).group(0), "class") or "").split()
    for c in classes:
        m = re.search(r"\.%s\s+text\s*\{[^}]*font-size\s*:\s*([\d.]+)px" % re.escape(c), src)
        if m:
            return float(m.group(1))
    return None


def traiter_page(src):
    """Chaque <svg> intégré d'une page HTML, traité à part."""
    return re.sub(r"<svg\b.*?</svg>", lambda m: poser(m.group(0), _taille_css(src, m.group(0))), src, flags=re.S)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    verifier = "--verifier" in argv
    fichiers = [a for a in argv if not a.startswith("--")]
    if not fichiers:
        print(__doc__)
        return 2
    ecarts = 0
    for f in fichiers:
        src = open(f, encoding="utf-8").read()
        nouveau = poser(src) if f.endswith(".svg") else traiter_page(src)
        if nouveau != src:
            ecarts += 1
            if verifier:
                print("À METTRE À JOUR : %s" % f)
            else:
                open(f, "w", encoding="utf-8").write(nouveau)
                print("écrit : %s" % f)
    return 1 if (verifier and ecarts) else 0


if __name__ == "__main__":
    sys.exit(main())
