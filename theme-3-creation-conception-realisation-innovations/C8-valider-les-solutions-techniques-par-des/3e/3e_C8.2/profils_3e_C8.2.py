# -*- coding: utf-8 -*-
"""Les cinq candidats-mâts, et les valeurs du banc — calculées, pas inventées.

Mât encastré au pied, effort appliqué en tête, hauteur L = 2 000 mm.

  · charge de rupture en flexion   F = σ · I / (v · L)
  · flèche sous une charge F       f = F · L³ / (3 · E · I)
  · charge de rupture en traction  F = σ · A
  · allongement sous une charge F  Δ = F · L / (E · A)

Les résistances σ sont EXACTEMENT celles du banc de 5e (5e_C8.2) : bois 40 MPa,
PVC 52, aluminium 190, acier 400. C'est ce qui permet de dire à l'élève, sans
tricher : « même matière, même résistance, autre essai — et autre classement ».
"""

import math

L = 2000.0          #: hauteur du mât, en mm
CHARGE_ESSAI = 100  #: charge d'essai commune pour mesurer la flèche, en N
COEF = 3            #: coefficient de sécurité retenu par le bureau d'études
EXIGE = CHARGE_ESSAI * COEF   #: charge de rupture exigée, en N
FLECHE_MAX = 40     #: flèche admise sous la charge d'essai, en mm


def _tube(de, ep):
    di = de - 2 * ep
    return (math.pi * (de ** 2 - di ** 2) / 4,
            math.pi * (de ** 4 - di ** 4) / 64, de / 2)


def _plein(d):
    return math.pi * d ** 2 / 4, math.pi * d ** 4 / 64, d / 2


def _carre(c):
    return c * c, c ** 4 / 12, c / 2


#: (nom, géométrie, σ MPa, E MPa, masse volumique kg/m³, angle mort de l'essai)
BRUT = [
    ("Tube aluminium Ø50 × 3", _tube(50, 3), 190, 70000, 2700,
     "Le banc pousse une fois. Le vent fait vibrer le mât des milliers de fois : "
     "c'est la fatigue, et elle casse plus bas que l'essai."),
    ("Barre pleine acier Ø20", _plein(20), 400, 210000, 7850,
     "Presque 5 kg à hisser sur un toit et à fixer en haut d'une échelle : le banc, "
     "lui, ne pèse rien."),
    ("Tube PVC Ø50 × 3", _tube(50, 3), 52, 3000, 1400,
     "Sous le soleil des tropiques, le PVC vieillit et devient cassant : l'essai, "
     "lui, est fait sur un tube neuf."),
    ("Poutre bois 40 × 40", _carre(40), 40, 11000, 500,
     "L'humidité : une poutre qui a pris l'eau ne casse plus à la même charge, et "
     "le banc essaie du bois sec."),
    ("Tube acier galvanisé Ø33,7 × 2,6", _tube(33.7, 2.6), 400, 210000, 7850,
     "La galvanisation protège tant qu'on ne la perce pas : c'est le trou de "
     "fixation, non traité, qui rouille en premier."),
]


class Profil:
    def __init__(self, nom, geo, sigma, E, rho, angle):
        A, I, v = geo
        self.nom, self.A, self.I, self.v = nom, A, I, v
        self.sigma, self.E, self.rho, self.angle = sigma, E, rho, angle

    @property
    def flexion(self):
        """charge de rupture en flexion, en N, arrondie à l'entier"""
        return round(self.sigma * self.I / (self.v * L))

    @property
    def k_fleche(self):
        """flèche en mm par newton"""
        return L ** 3 / (3 * self.E * self.I)

    @property
    def fleche_essai(self):
        return round(self.k_fleche * CHARGE_ESSAI, 1)

    @property
    def traction(self):
        """charge de rupture en traction, en kN, arrondie au dixième"""
        return round(self.sigma * self.A / 1000, 1)

    @property
    def k_allong(self):
        """allongement en mm par kN"""
        return 1000 * L / (self.E * self.A)

    @property
    def masse(self):
        return round(self.A * 1e-6 * (L / 1000) * self.rho, 2)

    @property
    def passe_rupture(self):
        return self.flexion >= EXIGE

    @property
    def passe_fleche(self):
        return self.fleche_essai <= FLECHE_MAX


PROFILS = [Profil(*b) for b in BRUT]

if __name__ == "__main__":
    print("%-34s %8s %8s %10s %9s %8s" %
          ("profilé", "flexion", "flèche", "traction", "masse", "verdict"))
    for p in PROFILS:
        v = ("RETENU" if p.passe_rupture and p.passe_fleche else
             "flèche" if p.passe_rupture else "rupture")
        print("%-34s %6d N %6.1f mm %7.1f kN %6.2f kg  %s"
              % (p.nom, p.flexion, p.fleche_essai, p.traction, p.masse, v))
    print("\nexigé : rupture ≥ %d N · flèche ≤ %d mm sous %d N" % (EXIGE, FLECHE_MAX, CHARGE_ESSAI))
    print("rang traction :", " > ".join(p.nom for p in sorted(PROFILS, key=lambda x: -x.traction)))
    print("rang flexion  :", " > ".join(p.nom for p in sorted(PROFILS, key=lambda x: -x.flexion)))
