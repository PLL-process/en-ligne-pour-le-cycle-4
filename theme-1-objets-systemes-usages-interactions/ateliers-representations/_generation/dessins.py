# -*- coding: utf-8 -*-
"""Les scènes dessinées des ateliers (SVG originaux, CC0).

Une scène ne nomme rien de ce que l'élève doit trouver : elle montre.
Les repères numérotés (A, B, C…) ne sont posés que lorsque l'exercice les cite.
"""
from figures import e, texte, svg, ENCRE, GRIS, fleche_def

PEAU = "#c98d5f"
PEAU2 = "#8a5a3c"


def _pluie(largeur, hauteur, pas=46, decal=0):
    traits = []
    k = 0
    for y in range(10, hauteur - 120, 38):
        for x in range(10 + (k % 2) * 23 + decal, largeur, pas):
            traits.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#6f9bd1" stroke-width="2" stroke-linecap="round" opacity=".75"/>'
                          % (x, y, x - 7, y + 16))
        k += 1
    return "".join(traits)


def velo_cargo(ident, titre, desc, reperes=None, pluie=True, largeur=800, hauteur=470):
    """Léa sur son vélo-cargo (biporteur), deux enfants et des courses dans le bac,
    une route qui monte, la pluie, un téléphone au guidon qui affiche un trajet.
    reperes : liste de (lettre, x, y, x_cible, y_cible) pour montrer un détail."""
    c = [fleche_def(ident + "-pt", "#b3261e")]
    # ciel et nuage
    c.append('<rect x="0" y="0" width="%d" height="%d" fill="#e9eef7"/>' % (largeur, hauteur))
    c.append('<g fill="#c7d0de"><ellipse cx="140" cy="60" rx="90" ry="34"/><ellipse cx="210" cy="48" rx="70" ry="30"/>'
             '<ellipse cx="560" cy="52" rx="80" ry="28"/><ellipse cx="625" cy="66" rx="64" ry="26"/></g>')
    if pluie:
        c.append(_pluie(largeur, hauteur))
    # la route qui monte (vers la droite)
    c.append('<polygon points="0,440 %d,330 %d,%d 0,%d" fill="#8b929c"/>' % (largeur, largeur, hauteur, hauteur))
    c.append('<line x1="0" y1="440" x2="%d" y2="330" stroke="#5f6670" stroke-width="4"/>' % largeur)
    c.append('<line x1="40" y1="452" x2="760" y2="353" stroke="#f4f4f4" stroke-width="4" stroke-dasharray="34 26"/>')
    # le vélo-cargo, incliné avec la pente
    g = ['<g transform="rotate(-7.8 420 380)">']
    # roues
    for (x, y, r) in ((235, 372, 50), (640, 380, 40)):
        g.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="7"/>' % (x, y, r, ENCRE))
        g.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="#7d8597" stroke-width="1.5"/>' % (x, y, r - 9))
        g.append('<circle cx="%d" cy="%d" r="5" fill="%s"/>' % (x, y, ENCRE))
    # cadre
    g.append('<path d="M235,372 L305,262 L345,358 Z" fill="none" stroke="#2c6e9e" stroke-width="7" stroke-linejoin="round"/>')
    g.append('<path d="M345,358 L405,358 L405,300 L380,250" fill="none" stroke="#2c6e9e" stroke-width="7" stroke-linejoin="round"/>')
    g.append('<path d="M405,358 L585,362 L640,380" fill="none" stroke="#2c6e9e" stroke-width="7" stroke-linejoin="round"/>')
    # selle, pédalier, chaîne
    g.append('<rect x="283" y="250" width="44" height="9" rx="4" fill="%s"/>' % ENCRE)
    g.append('<circle cx="345" cy="358" r="13" fill="none" stroke="%s" stroke-width="4"/>' % ENCRE)
    # la chaîne, enfermée dans un carter (une coque grise)
    g.append('<path d="M236,360 L345,346 Q360,352 345,370 L236,384 Q222,372 236,360 Z" fill="#9aa3ad" stroke="#5f6670" stroke-width="2.4"/>')
    # guidon et téléphone
    g.append('<path d="M380,250 L372,224 L395,220" fill="none" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % ENCRE)
    # la commande de vitesses, une petite molette sur la poignée
    g.append('<rect x="370" y="227" width="14" height="9" rx="3" fill="#e0b000" stroke="%s" stroke-width="1.5"/>' % ENCRE)
    g.append('<rect x="392" y="196" width="20" height="34" rx="3" fill="#111a2c" stroke="#111a2c" transform="rotate(12 402 213)"/>')
    g.append('<path d="M397,224 L401,215 L406,212 L404,204" fill="none" stroke="#7fe0ff" stroke-width="2" transform="rotate(12 402 213)"/>')
    # le bac, devant
    g.append('<path d="M412,286 L600,286 L590,352 L420,352 Z" fill="#3c8d5a" stroke="#235638" stroke-width="3"/>')
    # deux enfants dans le bac
    for (x, h) in ((462, 248), (520, 254)):
        g.append('<rect x="%d" y="%d" width="34" height="%d" rx="12" fill="#e2a33b"/>' % (x - 17, h + 22, 290 - h - 6))
        g.append('<circle cx="%d" cy="%d" r="17" fill="%s"/>' % (x, h + 6, PEAU))
        g.append('<path d="M%d,%d q17,-16 34,0" fill="%s"/>' % (x - 17, h + 2, PEAU2))
    # les courses (un sac et un poireau)
    g.append('<rect x="556" y="252" width="34" height="40" rx="4" fill="#f2e3c6" stroke="#a6875a" stroke-width="2"/>')
    g.append('<line x1="566" y1="252" x2="560" y2="226" stroke="#4a9a3a" stroke-width="6" stroke-linecap="round"/>')
    g.append('<line x1="580" y1="252" x2="588" y2="232" stroke="#d9a441" stroke-width="7" stroke-linecap="round"/>')
    # Léa
    g.append('<path d="M302,252 L330,178" stroke="#b03a57" stroke-width="22" stroke-linecap="round"/>')
    g.append('<path d="M330,190 L376,226" stroke="#b03a57" stroke-width="9" stroke-linecap="round"/>')
    g.append('<circle cx="338" cy="158" r="19" fill="%s"/>' % PEAU)
    g.append('<path d="M318,152 q20,-30 42,-4 q-6,-10 -20,-12 z" fill="#2a1a12"/>')
    g.append('<path d="M306,256 L352,300 L345,358" fill="none" stroke="#2b3a67" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>')
    g.append('</g>')
    c.append("".join(g))
    for (lettre, x, y, xc, yc) in (reperes or []):
        c.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#b3261e" stroke-width="2.4" marker-end="url(#%s-pt)"/>'
                 % (x, y, xc, yc, ident))
        c.append('<circle cx="%d" cy="%d" r="17" fill="#b3261e"/>' % (x, y))
        c.append(texte(x, y, lettre, taille=17, gras=True, couleur="#ffffff", car=3))
    return svg(largeur, hauteur, titre, desc, "".join(c), ident=ident)
