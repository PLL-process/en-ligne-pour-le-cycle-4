# -*- coding: utf-8 -*-
"""Le mât de la station, et la simulation qu'on met en œuvre — calculé, pas inventé.

Mât encastré au pied, hauteur réglable, chargé de deux façons :

    · POUSSÉE DU BANC — 100 N appliqués en tête, quel que soit le profilé.
      C'est ce que le banc de 3e_C8.2 fait, et ce que la simulation doit
      reproduire pour qu'on puisse lui faire confiance ensuite.

    · VENT DE CYCLONE — une pression q = ½ · ρ · V² répartie sur la surface
      que le mât offre au vent, plus le boîtier de la station en tête.
      Ici, la charge dépend de la LARGEUR du profilé : un mât fin prend moins
      de vent. Le banc, lui, poussait pareil sur tout le monde.

Moments au pied, en N·mm :

    banc     M = F · L
    vent     M = w · L² / 2  +  F_boîtier · L      avec w = q · Cd · largeur

Flèche en tête, en mm :

    banc     f = F · L³ / (3 E I)
    vent     f = w · L⁴ / (8 E I)  +  F_boîtier · L³ / (3 E I)

Les cinq profilés sont EXACTEMENT ceux du banc de 3e_C8.2, avec les mêmes
résistances à la rupture (règle d'or n°234). Ce qui est nouveau ici, c'est la
LIMITE ÉLASTIQUE : la valeur à partir de laquelle le mât plie pour de bon,
bien avant de casser. Un mât tordu ne casse pas ; il ne mesure plus rien.
"""

import math

RHO_AIR = 1.225          #: masse volumique de l'air, kg/m³
G = 9.81
AIRE_BOITIER = 0.030     #: surface au vent du boîtier de la station, m² (200 × 150 mm)

#: hauteurs proposées par la simulation, en mm
HAUTEURS = (1200, 1500, 2000)
#: hauteur minimale pour que l'anémomètre lise le vrai vent au-dessus du toit
HAUTEUR_MESURE = 2000
#: vitesse de référence du cahier des charges, en km/h (cyclone catégorie 1)
VENT_REFERENCE = 150
#: charge du banc de 3e_C8.2, en N
POUSSEE_BANC = 100
#: coefficient de sécurité exigé par le bureau d'études
COEF_EXIGE = 3
#: flèche admise en tête, en mm — au-delà, l'anémomètre ne vise plus juste
FLECHE_MAX = 40


def _tube(de, ep):
    di = de - 2 * ep
    return (math.pi * (de ** 4 - di ** 4) / 64, de / 2, de, 1.2)


def _plein(d):
    return math.pi * d ** 4 / 64, d / 2, d, 1.2


def _carre(c):
    return c ** 4 / 12, c / 2, c, 2.0


#: (nom, géométrie, σ_e MPa, σ_r MPa, E MPa, angle mort commun aux deux instruments)
BRUT = [
    ("Tube aluminium Ø50 × 3", _tube(50, 3), 140, 190, 70000,
     "Le vent fait vibrer le mât des milliers de fois : c'est la fatigue. "
     "Ni le banc ni la simulation ne la voient — ils chargent une seule fois."),
    ("Barre pleine acier Ø20", _plein(20), 235, 400, 210000,
     "Presque 5 kg à hisser sur un toit : ni le banc ni la simulation ne pèsent "
     "le mât avant de le monter."),
    ("Tube PVC Ø50 × 3", _tube(50, 3), 45, 52, 3000,
     "Sous le soleil des tropiques le PVC vieillit et devient cassant. Les deux "
     "instruments travaillent sur un tube neuf."),
    ("Poutre bois 40 × 40", _carre(40), 25, 40, 11000,
     "Une poutre qui a pris l'eau ne tient plus la même charge, et sa section "
     "carrée prend presque deux fois plus de vent qu'un tube rond."),
    ("Tube acier galvanisé Ø33,7 × 2,6", _tube(33.7, 2.6), 235, 400, 210000,
     "La galvanisation protège tant qu'on ne la perce pas : c'est le trou de "
     "fixation, non traité, qui rouille en premier."),
]


def pression(v_kmh=VENT_REFERENCE):
    """Pression dynamique du vent, en Pa."""
    v = v_kmh / 3.6
    return 0.5 * RHO_AIR * v * v


class Profile:
    def __init__(self, nom, geo, sigma_e, sigma_r, E, angle):
        self.I, self.v, self.largeur, self.cd = geo
        self.nom, self.sigma_e, self.sigma_r, self.E = nom, sigma_e, sigma_r, E
        self.angle = angle

    # ── les deux cas de charge ──────────────────────────────────────────
    def moment(self, hauteur, cas, v_kmh=VENT_REFERENCE):
        """Moment de flexion au pied, en N·mm."""
        if cas == "banc":
            return POUSSEE_BANC * hauteur
        q = pression(v_kmh)
        L = hauteur / 1000.0
        w = q * self.cd * (self.largeur / 1000.0)      # N/m
        return (w * L * L / 2 + q * self.cd * AIRE_BOITIER * L) * 1000

    def fleche(self, hauteur, cas, v_kmh=VENT_REFERENCE):
        """Flèche en tête, en mm."""
        EI = self.E * self.I
        if cas == "banc":
            return POUSSEE_BANC * hauteur ** 3 / (3 * EI)
        q = pression(v_kmh)
        w = q * self.cd * (self.largeur / 1000.0) / 1000.0   # N/mm
        f_b = q * self.cd * AIRE_BOITIER
        return w * hauteur ** 4 / (8 * EI) + f_b * hauteur ** 3 / (3 * EI)

    def contrainte(self, hauteur, cas, v_kmh=VENT_REFERENCE):
        """Contrainte maximale au pied, en MPa."""
        return self.moment(hauteur, cas, v_kmh) * self.v / self.I

    def coefficient(self, hauteur, cas, critere="elastique", v_kmh=VENT_REFERENCE):
        limite = self.sigma_e if critere == "elastique" else self.sigma_r
        return limite / self.contrainte(hauteur, cas, v_kmh)

    # ── le verdict ──────────────────────────────────────────────────────
    def tient(self, hauteur, cas, critere="elastique", v_kmh=VENT_REFERENCE):
        return (self.coefficient(hauteur, cas, critere, v_kmh) >= COEF_EXIGE
                and self.fleche(hauteur, cas, v_kmh) <= FLECHE_MAX)

    def pourquoi(self, hauteur, cas, critere="elastique", v_kmh=VENT_REFERENCE):
        """La raison du refus, ou une chaîne vide s'il n'y en a pas."""
        k = self.coefficient(hauteur, cas, critere, v_kmh)
        f = self.fleche(hauteur, cas, v_kmh)
        if k < COEF_EXIGE and f > FLECHE_MAX:
            return "coefficient %.1f et flèche %.0f mm" % (k, f)
        if k < COEF_EXIGE:
            return "coefficient %.1f < %d" % (k, COEF_EXIGE)
        if f > FLECHE_MAX:
            return "flèche %.0f mm > %d mm" % (f, FLECHE_MAX)
        return ""


PROFILES = [Profile(*b) for b in BRUT]
PAR_NOM = {p.nom: p for p in PROFILES}


def retenus(hauteur, cas, critere="elastique", v_kmh=VENT_REFERENCE):
    return [p for p in PROFILES if p.tient(hauteur, cas, critere, v_kmh)]


if __name__ == "__main__":
    print("Pression à %d km/h : %.0f Pa · boîtier %.3f m² en tête\n"
          % (VENT_REFERENCE, pression(), AIRE_BOITIER))

    for cas in ("banc", "vent"):
        for critere in ("rupture", "elastique"):
            print("=" * 84)
            print("cas « %s » · critère « %s » · hauteur %d mm"
                  % (cas, critere, HAUTEUR_MESURE))
            for p in PROFILES:
                print("  %-34s M %6.0f N·m  σ %5.0f MPa  k %5.1f  f %5.0f mm  %s"
                      % (p.nom, p.moment(HAUTEUR_MESURE, cas) / 1000,
                         p.contrainte(HAUTEUR_MESURE, cas),
                         p.coefficient(HAUTEUR_MESURE, cas, critere),
                         p.fleche(HAUTEUR_MESURE, cas),
                         "RETENU" if p.tient(HAUTEUR_MESURE, cas, critere)
                         else p.pourquoi(HAUTEUR_MESURE, cas, critere)))

    print("=" * 84)
    print("Nombre de profilés retenus selon le réglage (hauteur × cas × critère) :")
    print("%-8s %-8s %-11s %s" % ("hauteur", "cas", "critère", "retenus"))
    for h in HAUTEURS:
        for cas in ("banc", "vent"):
            for critere in ("rupture", "elastique"):
                r = retenus(h, cas, critere)
                print("%-8d %-8s %-11s %d  %s"
                      % (h, cas, critere, len(r),
                         ", ".join(x.nom.split()[1] for x in r)))
