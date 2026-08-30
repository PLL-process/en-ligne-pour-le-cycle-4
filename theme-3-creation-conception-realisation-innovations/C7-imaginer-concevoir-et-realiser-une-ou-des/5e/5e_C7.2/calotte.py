#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""calotte.py — la géométrie du creux que laisse une bille.

LE MODÈLE, ET POURQUOI IL EXISTE
--------------------------------
Le TP « Le dé » creuse les points du dé au cylindre : un fond plat, une arête
vive. Il le dit lui-même, au palier 4 :

    « Sur un dé du commerce, les points sont des CALOTTES : le fond est arrondi,
    comme le creux d'une cuillère. Nous faisons plus simple […] parce qu'une
    calotte demanderait de soustraire une sphère, et ça, c'est un geste
    d'après. »

Ce fichier calcule ce geste d'après. Il ne décore pas le TP : c'est lui qui
donne les cotes, et la suite de tests compare la page à ces valeurs. Une cote
écrite à la main dans une page finit par ne plus correspondre au modèle ; une
cote engendrée ne le peut pas (règle d'or n°246).

LA GÉOMÉTRIE, EN UNE PHRASE
---------------------------
Une bille de rayon R dont le centre est à la distance c au-dessus de la face
s'enfonce de h = R - c dans la matière, et laisse un creux circulaire de rayon
a = racine(R² - c²).

C'est le théorème de Pythagore, et rien d'autre : le rayon de la bille est
l'hypoténuse, la hauteur du centre et le rayon du creux sont les deux côtés.

LE FAIT QUI COMMANDE LE TP
--------------------------
Une bille de Ø20 posée de façon à s'enfoncer de 1,5 mm laisse un creux de
Ø10,5 — presque exactement l'empreinte des Ø10 actuels. Le dé garde donc son
allure : il ne gagne QUE la douceur du fond. C'est ce qui rend l'amélioration
honnête à évaluer — on ne change pas l'objet, on change une seule de ses
qualités.

CE QUE CE MODÈLE NE DIT PAS
---------------------------
Rien sur l'impression : une calotte de 1,5 mm de profondeur s'imprime comme un
creux de 1,5 mm, mais l'état de surface d'une paroi inclinée en dépôt de fil
dépend de la hauteur de couche, qui n'est pas ici. Rien non plus sur le
toucher, qui est le vrai critère et qui se juge la pièce en main.

Usage : python3 calotte.py
"""
import json
import math
import sys

#: le dé du TP nº1, tel qu'il est construit — ces cotes viennent du scénario
COTE_DE = 50.0          # mm, l'arête du cube
DIAMETRE_CREUX = 10.0   # mm, le cercle esquissé pour chaque point
PROFONDEUR = 1.5        # mm, l'enlèvement de matière (« Retraité de 1.5 »)
POINTS = 21             # le total sur les six faces : 1+2+3+4+5+6

#: les billes qu'on peut essayer, à enfoncement égal
BILLES = [10.0, 20.0, 30.0]
BILLE_RETENUE = 20.0


def creux(diametre_bille, profondeur=PROFONDEUR):
    """Le creux laissé par une bille enfoncée de `profondeur`.

    Renvoie (hauteur du centre au-dessus de la face, diamètre du creux).
    """
    R = diametre_bille / 2.0
    if profondeur <= 0 or profondeur >= 2 * R:
        raise ValueError("un enfoncement se situe entre 0 et le diamètre de la bille")
    centre = R - profondeur                      # au-dessus de la face
    rayon_creux = math.sqrt(R * R - centre * centre)
    return centre, 2 * rayon_creux


def volume_calotte(diametre_bille, profondeur=PROFONDEUR):
    """Le volume de matière retirée par une calotte, en mm³."""
    R = diametre_bille / 2.0
    return math.pi * profondeur ** 2 * (R - profondeur / 3.0)


def volume_cylindre(diametre=DIAMETRE_CREUX, profondeur=PROFONDEUR):
    return math.pi * (diametre / 2.0) ** 2 * profondeur


def table():
    """Ce que donnent les trois billes, à enfoncement égal."""
    lignes = []
    for d in BILLES:
        centre, creux_d = creux(d)
        lignes.append(dict(bille=d, centre=centre, creux=creux_d,
                           volume=volume_calotte(d)))
    return lignes


def profil(diametre_bille, pas=0.25, profondeur=PROFONDEUR):
    """La largeur du creux à chaque quart de millimètre de profondeur.

    Une calotte est LARGE en haut et se referme vers le bas : c'est exactement
    l'inverse d'un cylindre, large pareil du haut jusqu'au fond.
    """
    R = diametre_bille / 2.0
    centre = R - profondeur
    points, d = [], 0.0
    while d <= profondeur + 1e-9:
        # à la profondeur d sous la face, le plan de coupe est à (centre + d)
        # du centre de la bille
        y = centre + d
        largeur = 2 * math.sqrt(max(R * R - y * y, 0.0))
        points.append((round(d, 3), round(largeur, 3)))
        d += pas
    return points


def profondeur_de_croisement(diametre_bille, diametre_cylindre=DIAMETRE_CREUX,
                             profondeur=PROFONDEUR):
    """À quelle profondeur le cylindre devient-il plus large que la calotte ?

    Question qui commande tout le TP : peut-on poser la calotte PAR-DESSUS
    l'ancien creux cylindrique, sans rien retirer ?

    Réponse mesurée, pas devinée. La calotte est plus large que le cylindre
    seulement dans les premiers dixièmes de millimètre ; plus bas, c'est le
    cylindre qui déborde, et la bille ne touche plus rien. Poser la calotte
    sans retirer l'ancien creux ne ferait donc qu'ébrécher le bord.

    Renvoie None si la calotte reste plus large sur toute la profondeur.
    """
    R = diametre_bille / 2.0
    centre = R - profondeur
    # largeur de la calotte = diamètre du cylindre  ⇔  R² - (centre+d)² = (D/2)²
    reste = R * R - (diametre_cylindre / 2.0) ** 2
    if reste < 0:
        return 0.0                      # la bille est plus étroite dès la surface
    d = math.sqrt(reste) - centre
    if d <= 0:
        return 0.0
    return None if d >= profondeur else d


def mesures():
    """Tout ce que les pages du lot ont le droit de citer."""
    centre, creux_d = creux(BILLE_RETENUE)
    return dict(
        cote_de=COTE_DE,
        diametre_creux_cylindrique=DIAMETRE_CREUX,
        profondeur=PROFONDEUR,
        points=POINTS,
        bille=BILLE_RETENUE,
        centre_au_dessus=round(centre, 2),
        diametre_calotte=round(creux_d, 2),
        elargissement=round(creux_d - DIAMETRE_CREUX, 2),
        volume_cylindre=round(volume_cylindre(), 1),
        volume_calotte=round(volume_calotte(BILLE_RETENUE), 1),
        croisement=round(profondeur_de_croisement(BILLE_RETENUE), 2),
        table=[dict(bille=l["bille"], centre=round(l["centre"], 2),
                    creux=round(l["creux"], 2), volume=round(l["volume"], 1))
               for l in table()],
    )


def main():
    m = mesures()
    print("Le dé : arête %g mm · %d points · creux cylindriques Ø%g, profondeur %g mm"
          % (m["cote_de"], m["points"], m["diametre_creux_cylindrique"], m["profondeur"]))
    print()
    print("À enfoncement égal (%g mm), trois billes :" % m["profondeur"])
    print("   bille     centre au-dessus     creux obtenu     matière retirée")
    for l in m["table"]:
        print("   Ø%-6g   %6.2f mm            Ø%-6.2f        %6.1f mm³"
              % (l["bille"], l["centre"], l["creux"], l["volume"]))
    print()
    print("Retenue : Ø%g → creux de Ø%g, soit %+g mm sur les Ø%g d'aujourd'hui."
          % (m["bille"], m["diametre_calotte"], m["elargissement"],
             m["diametre_creux_cylindrique"]))
    print("Le dé garde donc son allure : il ne gagne que la douceur du fond.")
    print()
    print("Matière retirée par point : cylindre %.1f mm³ · calotte %.1f mm³ "
          "(la calotte en retire %.0f %% de moins)"
          % (m["volume_cylindre"], m["volume_calotte"],
             100 * (1 - m["volume_calotte"] / m["volume_cylindre"])))
    print()
    print("Largeur du creux, quart de millimètre par quart de millimètre (bille Ø%g) :"
          % m["bille"])
    for d, largeur in profil(BILLE_RETENUE):
        print("   à %.2f mm sous la face : %5.2f mm de large" % (d, largeur))
    print()
    print("Peut-on poser la calotte PAR-DESSUS l'ancien creux, sans rien retirer ?")
    print("   Non : dès %.2f mm sous la face, le cylindre Ø%g est déjà plus large que"
          % (m["croisement"], m["diametre_creux_cylindrique"]))
    print("   la calotte, qui se referme en descendant. La bille ne toucherait plus")
    print("   rien : elle ébrécherait le bord, et le fond plat resterait plat.")
    print("   → il faut RETIRER ce qu'on remplace avant de poser l'amélioration.")
    if "--json" in sys.argv:
        print(json.dumps(m, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


# ── le dessin : une coupe, deux creux, et la bille qui explique le second ────
SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {H}" role="img"
     aria-labelledby="t d" font-family="system-ui,sans-serif">
<title id="t">Coupe du dé : à gauche le creux cylindrique, à droite la calotte</title>
<desc id="d">Une coupe de la face du dé. À gauche, le creux actuel : un cylindre de
{Dcyl} millimètres de large, {p} millimètre de profondeur, à fond plat et à arête vive.
À droite, la calotte : une bille de {Db} millimètres de diamètre, dont le centre est
{c} millimètres au-dessus de la face, s'enfonce de {p} millimètre et laisse un creux
arrondi de {Dcal} millimètres de large. Les deux creux ont la même profondeur ; la
calotte est à peine plus large, et son fond est rond.</desc>
<rect width="{L}" height="{H}" fill="#f7f9fc"/>
{corps}
</svg>
"""


def dessin_coupe(chemin=None):
    """Écrit (ou renvoie) la coupe comparée — cotée depuis le modèle, pas à la main."""
    m = mesures()
    k, x0, y0 = 11.0, 74.0, 232.0            # px par mm, origine du plan de la face
    L, H = 620, 400

    def X(mm):
        return x0 + mm * k

    def Y(mm):                                # mm positifs vers le BAS (dans la matière)
        return y0 + mm * k

    R = m["bille"] / 2.0
    c = m["centre_au_dessus"]
    a = m["diametre_calotte"] / 2.0
    dc = m["diametre_creux_cylindrique"] / 2.0
    gauche, droite = 9.0, 33.0               # abscisses des deux centres, en mm
    p = m["profondeur"]

    parties = []
    A = parties.append
    # la matière : un profil qui contourne les deux creux
    A('<path d="M {x1} {y0} L {a1} {y0} L {a1} {y1} L {a2} {y1} L {a2} {y0} '
      'L {b1} {y0} A {ra} {ra} 0 0 0 {b2} {y0} L {x2} {y0} L {x2} {yb} L {x1} {yb} Z" '
      'fill="#dfe7f3" stroke="#1d4e89" stroke-width="2"/>'.format(
          x1=X(-4), x2=X(46), y0=Y(0), yb=Y(9),
          a1=X(gauche - dc), a2=X(gauche + dc), y1=Y(p),
          b1=X(droite - a), b2=X(droite + a), ra=R * k))
    # la bille, en pointillés
    A('<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#b8860b" '
      'stroke-width="1.6" stroke-dasharray="6 4"/>'.format(
          cx=X(droite), cy=Y(-c), r=R * k))
    A('<circle cx="{cx}" cy="{cy}" r="3" fill="#b8860b"/>'.format(cx=X(droite), cy=Y(-c)))
    # la cote du centre au-dessus de la face
    A('<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="#b8860b" stroke-width="1.4"/>'
      .format(x=X(droite), y1=Y(-c), y2=Y(0)))
    A('<text x="{x}" y="{y}" font-size="15" fill="#8a6508">{v} mm</text>'.format(
        x=X(droite) + 8, y=Y(-c / 2), v=("%g" % c).replace(".", ",")))
    # la largeur des deux creux
    for cx, largeur, couleur in ((gauche, m["diametre_creux_cylindrique"], "#1d4e89"),
                                 (droite, m["diametre_calotte"], "#1d4e89")):
        A('<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{co}" stroke-width="1.4"/>'
          .format(x1=X(cx - largeur / 2), x2=X(cx + largeur / 2), y=Y(-1.4), co=couleur))
        A('<text x="{x}" y="{y}" font-size="15" fill="{co}" text-anchor="middle">'
          'Ø{v}</text>'.format(x=X(cx), y=Y(-2.2), co=couleur,
                               v=("%g" % largeur).replace(".", ",")))
    # la profondeur, commune aux deux : une ligne de niveau entre les deux creux
    A('<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#1d4e89" stroke-width="1" '
      'stroke-dasharray="5 4"/>'.format(x1=X(gauche + dc + 0.5), x2=X(droite - a - 0.5),
                                        y=Y(p)))
    A('<text x="{x}" y="{y}" font-size="15" fill="#1d4e89" text-anchor="middle">'
      'même profondeur : {v} mm</text>'.format(
          x=X((gauche + droite) / 2), y=Y(p + 2.4), v=("%g" % p).replace(".", ",")))
    # les deux légendes
    A('<text x="{x}" y="{y}" font-size="16" fill="#1d4e89" text-anchor="middle" '
      'font-weight="700">aujourd\'hui : fond plat</text>'.format(x=X(gauche), y=Y(11.4)))
    A('<text x="{x}" y="{y}" font-size="16" fill="#8a6508" text-anchor="middle" '
      'font-weight="700">la calotte : fond rond</text>'.format(x=X(droite), y=Y(11.4)))
    svg = SVG.format(L=L, H=H, corps="\n".join(parties),
                     Dcyl=("%g" % m["diametre_creux_cylindrique"]).replace(".", ","),
                     Db=("%g" % m["bille"]).replace(".", ","),
                     Dcal=("%g" % m["diametre_calotte"]).replace(".", ","),
                     c=("%g" % c).replace(".", ","),
                     p=("%g" % m["profondeur"]).replace(".", ","))
    if chemin:
        open(chemin, "w", encoding="utf-8").write(svg)
    return svg
