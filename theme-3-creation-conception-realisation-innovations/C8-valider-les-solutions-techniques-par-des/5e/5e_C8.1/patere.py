# -*- coding: utf-8 -*-
"""Le crochet du hall, et ce que la simulation en dit — calculé, pas inventé.

Crochet encastré dans le mur, charge suspendue au bout du bras.

    contrainte de flexion   σ = F · L / (I/v)
    charge qui déforme      F_e = σ_e · (I/v) / L
    charge qui casse        F_r = σ_r · (I/v) / L
    coefficient de sécurité k = σ_e / σ_service

Les charges de RUPTURE calculées ici sont EXACTEMENT celles que le banc de
5e_C8.2 a relevées : bois 41 kg, PLA 51, PVC 53, aluminium 194, acier 408. Ce
n'est pas une coïncidence, c'est une vérification — la simulation et le banc
décrivent le même objet, et doivent tomber d'accord là où ils mesurent la même
chose (règle d'or n°234).

Là où ils ne tombent PAS d'accord est tout l'objet de la séquence. Le banc a
mesuré quand le crochet CASSE. Le gestionnaire, lui, a décrit un crochet qui
PLIE : « accroché d'un coup sec, et le crochet plie ». Ce ne sont pas les mêmes
chiffres, et pour le bois ce ne sont pas les mêmes conclusions.
"""

#: bras du crochet, en mm (du mur au point d'accrochage)
L = 60.0
#: section rectangulaire du bras, en mm
LARGEUR, EPAISSEUR = 25.0, 12.0
#: module de flexion I/v, en mm³
MODULE = LARGEUR * EPAISSEUR ** 2 / 6
#: pesanteur, en N/kg
G = 9.81

#: cahier des charges du gestionnaire
CHARGE_SERVICE = 12      #: un sac de cours trempé, en kg
COEF_EXIGE = 3           #: coefficient de sécurité exigé
NOMBRE = 40              #: patères à remplacer dans le hall

#: (nom, σ_e limite élastique MPa, σ_r rupture MPa, E module MPa,
#:  prix unitaire €, minutes de fabrication, tenue à l'humidité du hall)
BRUT = [
    ("Bois (pin)", 25, 40, 11000, 1.20, 12,
     "Gonfle et se fend si l'eau reste ; le hall reçoit la pluie de midi."),
    ("PLA imprimé en 3D", 45, 50, 3500, 0.60, 45,
     "Insensible à l'eau, mais ramollit vers 55 °C — pas au soleil direct."),
    ("PVC rigide", 45, 52, 3000, 2.10, 10,
     "Insensible à l'eau. Devient cassant après quelques années de UV."),
    ("Aluminium", 140, 190, 70000, 4.80, 15,
     "Ne rouille pas : sa couche d'oxyde le protège toute seule."),
    ("Acier doux", 235, 400, 210000, 3.90, 15,
     "Rouille dans un hall humide s'il n'est pas galvanisé (+ 1,60 €)."),
]


class Materiau:
    def __init__(self, nom, sigma_e, sigma_r, E, prix, minutes, humidite):
        self.nom, self.sigma_e, self.sigma_r = nom, sigma_e, sigma_r
        self.E, self.prix, self.minutes, self.humidite = E, prix, minutes, humidite

    # ── ce que la simulation calcule ────────────────────────────────────
    def contrainte(self, masse_kg):
        """Contrainte de flexion dans le bras, en MPa, sous une masse donnée."""
        return masse_kg * G * L / MODULE

    def coefficient(self, masse_kg=None):
        """σ_e / σ_service — combien de fois la charge de service tient."""
        m = CHARGE_SERVICE if masse_kg is None else masse_kg
        return self.sigma_e / self.contrainte(m)

    @property
    def charge_deforme(self):
        """Charge à partir de laquelle le crochet plie POUR TOUJOURS, en kg."""
        return self.sigma_e * MODULE / (L * G)

    @property
    def charge_casse(self):
        """Charge à laquelle le crochet casse, en kg — ce que le banc a mesuré."""
        return self.sigma_r * MODULE / (L * G)

    # ── la décision ─────────────────────────────────────────────────────
    @property
    def retenu(self):
        """Le seul verdict qui compte : k ≥ 3 sur la LIMITE ÉLASTIQUE."""
        return self.coefficient() >= COEF_EXIGE

    @property
    def retenu_au_banc(self):
        """Ce que le banc de 5e_C8.2 aurait conclu — sur la rupture."""
        return self.charge_casse / CHARGE_SERVICE >= COEF_EXIGE

    @property
    def cout_total(self):
        """Prix des 40 patères, galvanisation comprise si le hall l'exige."""
        supplement = 1.60 if "galvanis" in self.humidite else 0.0
        return (self.prix + supplement) * NOMBRE

    @property
    def heures_total(self):
        """Temps machine pour les 40 patères, en heures."""
        return self.minutes * NOMBRE / 60.0


MATERIAUX = [Materiau(*b) for b in BRUT]
PAR_NOM = {m.nom: m for m in MATERIAUX}


def desaccords():
    """Les matériaux sur lesquels le banc et la simulation ne disent PAS pareil."""
    return [m for m in MATERIAUX if m.retenu != m.retenu_au_banc]


if __name__ == "__main__":
    print("Crochet %g × %g mm, bras %g mm → module I/v = %g mm³"
          % (LARGEUR, EPAISSEUR, L, MODULE))
    print("Cahier des charges : %d kg de service, coefficient ≥ %d\n"
          % (CHARGE_SERVICE, COEF_EXIGE))
    print("%-20s %8s %8s %9s %8s %7s  %s" %
          ("matériau", "σ_e", "plie à", "casse à", "σ_serv", "k", "verdict"))
    for m in MATERIAUX:
        print("%-20s %5d MPa %5.0f kg %6.0f kg %6.1f MPa %6.1f  %s"
              % (m.nom, m.sigma_e, m.charge_deforme, m.charge_casse,
                 m.contrainte(CHARGE_SERVICE), m.coefficient(),
                 "RETENU" if m.retenu else "écarté"))

    print("\nCe que le banc (rupture) aurait conclu :")
    for m in MATERIAUX:
        print("  %-20s casse à %3.0f kg → k = %4.1f  %s"
              % (m.nom, m.charge_casse, m.charge_casse / CHARGE_SERVICE,
                 "retenu" if m.retenu_au_banc else "écarté"))

    d = desaccords()
    print("\nDésaccord banc / simulation : %s"
          % (", ".join(m.nom for m in d) if d else "aucun"))

    egaux = [m.nom for m in MATERIAUX if m.sigma_e == 45]
    print("Même limite élastique, classement du banc pourtant différent : %s"
          % " et ".join(egaux))

    print("Contrainte de service identique pour tous : %.1f MPa — la contrainte "
          "ne dépend que de la forme et de la charge." % MATERIAUX[0].contrainte(CHARGE_SERVICE))

    print("\nCoût et temps des %d patères, parmi les retenus :" % NOMBRE)
    for m in sorted((m for m in MATERIAUX if m.retenu), key=lambda m: m.cout_total):
        print("  %-20s %7.2f €  %5.1f h d'atelier   %s"
              % (m.nom, m.cout_total, m.heures_total, m.humidite))
    moins_cher = min((m for m in MATERIAUX if m.retenu), key=lambda m: m.cout_total)
    plus_rapide = min((m for m in MATERIAUX if m.retenu), key=lambda m: m.heures_total)
    print("\nle moins cher : %s (%.0f h) · le plus rapide : %s (%.2f €)"
          % (moins_cher.nom, moins_cher.heures_total,
             plus_rapide.nom, plus_rapide.cout_total))
