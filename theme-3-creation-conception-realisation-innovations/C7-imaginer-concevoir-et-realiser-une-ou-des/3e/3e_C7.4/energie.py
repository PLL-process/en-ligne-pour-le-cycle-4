# -*- coding: utf-8 -*-
"""Les données du banc d'énergie — calculées, pas choisies.

TOUT ce que les trois pages affichent sort d'ici. Aucune valeur n'est saisie à
la main dans le HTML : le générateur lit ce module et écrit les nombres.

Conventions
-----------
* Les consommations sont des **courants moyens sous 5 V**, valeurs constructeur
  usuelles des modules Grove et de la carte UNO. Chaque consommateur porte en
  plus une **durée de fonctionnement par jour** : c'est le produit des deux qui
  fait l'énergie, et c'est exactement ce que les élèves oublient.

* Le rendement d'un **régulateur linéaire** vaut Vsortie / Ventrée — ce n'est pas
  une valeur d'atelier, c'est de la physique : il dissipe la différence en
  chaleur. 9 V → 5 V jette 44 % de l'énergie avant d'alimenter quoi que ce soit.
  Le rendement d'un **convertisseur élévateur** (3,7 V → 5 V) est donné par le
  constructeur : 85 %.

* L'ensoleillement retenu pour la Martinique est de **5,3 kWh/m²/jour** en
  moyenne annuelle, soit 5,3 heures équivalent plein soleil. Le rendement de
  chaîne (orientation fixe, salissure, régulateur de charge, températures
  tropicales) est pris à **70 %**, valeur basse et volontairement prudente.
"""

# ── Les consommateurs ─────────────────────────────────────────────────────
#: nom → (courant moyen sous 5 V en mA, ce que c'est)
CONSOS = {
    "Carte Arduino UNO":            (45, "la carte elle-même, DEL d'alimentation et régulateur compris"),
    "Capteur d'humidité du sol":    (2,  "capteur analogique Grove, alimenté en permanence"),
    "Écran LCD RGB":                (40, "rétroéclairage allumé ; éteint, il ne consomme presque rien"),
    "Module relais":                (70, "seulement quand la bobine est excitée"),
    "Pompe immergée 5 V":           (300, "seulement quand elle tourne"),
    "DEL indicatrice":              (10, "une DEL Grove avec sa résistance"),
    "Buzzer d'alerte":              (30, "seulement quand il sonne"),
    "Anémomètre à impulsions":      (1,  "il ne consomme que pour compter des tours"),
    "Girouette":                    (1,  "une résistance lue par une entrée analogique"),
}

TENSION = 5.0  #: V — tout le montage est alimenté en 5 V


class Source:
    def __init__(self, nom, tension, capacite_mah, conversion, detail, prix, dechet):
        self.nom = nom
        self.tension = tension            # V
        self.capacite = capacite_mah      # mAh (None pour secteur et solaire)
        self.conversion = conversion      # rendement de la mise en 5 V
        self.detail = detail
        self.prix = prix                  # € l'unité, ordre de grandeur
        self.dechet = dechet              # ce qu'il en reste en fin de vie

    @property
    def brute(self):
        """énergie stockée, en Wh"""
        return None if self.capacite is None else self.capacite / 1000 * self.tension

    @property
    def utile(self):
        """énergie réellement disponible sous 5 V, en Wh"""
        return None if self.brute is None else round(self.brute * self.conversion, 1)


#: rendement d'un régulateur LINÉAIRE = Vsortie / Ventrée. C'est de la physique.
def lineaire(v_entree):
    return TENSION / v_entree


SOURCES = [
    Source("Pile 9 V alcaline", 9.0, 550, lineaire(9.0),
           "Une pile plate à deux boutons-pression. Régulateur linéaire 9 → 5 V : "
           "il dissipe 4 V sur 9 en chaleur, soit 44 % de l'énergie perdue avant "
           "d'alimenter quoi que ce soit.",
           3.50, "une pile à rapporter en bac de collecte"),
    Source("4 piles AA alcalines", 6.0, 2500, lineaire(6.0),
           "Quatre piles bâton en série. Régulateur linéaire 6 → 5 V : il ne dissipe "
           "qu'un volt sur six, donc il perd beaucoup moins.",
           4.00, "quatre piles à rapporter en bac de collecte"),
    Source("Accu Li-ion 18650 rechargeable", 3.7, 3000, 0.85,
           "Un accumulateur rechargeable et un convertisseur ÉLÉVATEUR 3,7 → 5 V, "
           "donné à 85 % par son constructeur. Il se recharge environ 500 fois.",
           8.00, "un accu rechargeable, 500 cycles avant recyclage"),
    Source("Secteur — adaptateur USB scellé", 5.0, None, 1.0,
           "Un bloc secteur fermé, jamais ouvert ni modifié par un élève : côté "
           "élève, il n'y a que du 5 V. Illimité — tant qu'il y a du réseau.",
           6.00, "un adaptateur qui dure des années"),
    Source("Panneau solaire 1 W crête + accu", 5.0, None, 0.70,
           "Un petit panneau et l'accu qu'il recharge. Ce n'est pas un réservoir : "
           "c'est un robinet, qui donne une certaine énergie CHAQUE JOUR.",
           15.00, "un panneau qui dure 20 ans, un accu à remplacer"),
]

#: Martinique — moyenne annuelle, en heures équivalent plein soleil par jour
ENSOLEILLEMENT = 5.3
#: pertes de chaîne : orientation fixe, salissure, régulateur, température
RENDEMENT_SOLAIRE = 0.70


def solaire(watt_crete):
    """énergie réellement récoltée par jour, en Wh/jour"""
    return round(watt_crete * ENSOLEILLEMENT * RENDEMENT_SOLAIRE, 1)


# ── Les trois montages, un par niveau ─────────────────────────────────────
#: niveau → [(consommateur, heures de fonctionnement par jour)]
MONTAGES = {
    "5e": [("Carte Arduino UNO", 10.0),
           ("Capteur d'humidité du sol", 10.0),
           ("DEL indicatrice", 10.0)],
    "4e": [("Carte Arduino UNO", 24.0),
           ("Capteur d'humidité du sol", 24.0),
           ("Écran LCD RGB", 1.0),
           ("Module relais", 60 / 3600),
           ("Pompe immergée 5 V", 60 / 3600)],
    "3e": [("Carte Arduino UNO", 24.0),
           ("Anémomètre à impulsions", 24.0),
           ("Girouette", 24.0),
           ("Buzzer d'alerte", 2.0),
           ("DEL indicatrice", 2.0)],
}


def energie_jour(montage):
    """Wh consommés par jour, et le détail par consommateur."""
    detail = []
    for nom, heures in montage:
        ma = CONSOS[nom][0]
        wh = ma / 1000 * TENSION * heures
        detail.append((nom, ma, heures, round(wh, 3)))
    return round(sum(d[3] for d in detail), 2), detail


def autonomie(source, wh_jour, watt_crete=1.0):
    """En jours. None = illimité (secteur). 0 = la source ne suffit même pas au jour."""
    if source.capacite is None and source.nom.startswith("Secteur"):
        return None
    if source.capacite is None:                      # solaire : un robinet
        recolte = solaire(watt_crete)
        return float("inf") if recolte >= wh_jour else 0.0
    return round(source.utile / wh_jour, 2)


if __name__ == "__main__":
    print("Sources — énergie réellement utile sous 5 V")
    print("%-34s %8s %8s %9s" % ("source", "brute", "rendem.", "utile"))
    for s in SOURCES:
        b = "%.2f Wh" % s.brute if s.brute else "—"
        u = "%.1f Wh" % s.utile if s.utile else "—"
        print("%-34s %8s %7.0f %% %9s" % (s.nom, b, s.conversion * 100, u))
    print("\nPanneau 1 W crête en Martinique : %.1f Wh/jour "
          "(%.1f h équivalent plein soleil × %.0f %%)"
          % (solaire(1), ENSOLEILLEMENT, RENDEMENT_SOLAIRE * 100))
    print("Panneau 2 W crête : %.1f Wh/jour" % solaire(2))

    for niv, m in MONTAGES.items():
        tot, det = energie_jour(m)
        print("\n── %s ── %.2f Wh/jour" % (niv, tot))
        for nom, ma, h, wh in sorted(det, key=lambda d: -d[3]):
            print("   %-30s %4d mA × %6s h = %6.3f Wh  (%4.1f %%)"
                  % (nom, ma, ("%.4f" % h).rstrip("0").rstrip("."), wh, 100 * wh / tot))
        print("   autonomies :")
        for s in SOURCES:
            a = autonomie(s, tot)
            if a is None:
                txt = "illimitée tant qu'il y a du réseau"
            elif a == float("inf"):
                txt = "suffit chaque jour (%.1f Wh récoltés pour %.2f consommés)" % (solaire(1), tot)
            elif a == 0.0:
                txt = "NE SUFFIT PAS (%.1f Wh récoltés pour %.2f consommés)" % (solaire(1), tot)
            else:
                txt = "%.2f jour(s) = %.0f h" % (a, a * 24)
            print("      %-34s %s" % (s.nom, txt))
