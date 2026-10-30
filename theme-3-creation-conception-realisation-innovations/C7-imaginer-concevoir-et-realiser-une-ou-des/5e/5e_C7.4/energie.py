# -*- coding: utf-8 -*-
"""Les données du banc d'énergie — calculées, pas choisies.

TOUT ce que les trois pages affichent se calcule ici. Mais aucun générateur ne
lit ce module : les pages, leurs corrections, leurs QCM, leurs synthèses, leurs
fiches, leurs rapports et leurs bancs RECOPIENT ces nombres. Tout changement ici
se reporte donc à la main dans chacun d'eux — et dans les trois copies de ce
fichier (3e_C7.4, 4e_C7.4, 5e_C7.4), qui restent identiques.

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

* L'ensoleillement dépend du **lieu de l'objet**, et chaque niveau prend celui
  du sien (`LIEUX`, plus bas) :
    - **Martinique** — le hall de 5e et la station de 3e : **5,3 kWh/m²/jour**
      en moyenne annuelle, soit 5,3 heures équivalent plein soleil ;
    - **New York** — le jardin de 4e, à Brooklyn : **4,5 heures** équivalent
      plein soleil par jour en moyenne annuelle, pour un panneau fixe incliné
      de 20° plein sud ; environ **2,4 heures en décembre**. Source : NREL,
      PVWatts v8 (base NSRDB), pour 40,71° N, 74,01° O, relevé par
      thegreenwatt.com (https://www.thegreenwatt.com/new-york-peak-sun-hours/).
      Recoupement à plat (rayonnement global horizontal) : 3,93 kWh/m²/jour en
      moyenne, 1,75 en décembre (NREL, via
      https://solarscope.io/solar-data/new-york/new-york-city).
  Le rendement de chaîne (orientation fixe, salissure, régulateur de charge,
  températures) est pris à **70 %** pour les deux lieux, valeur basse et
  volontairement prudente.

* Un total s'affiche arrondi au centième **« demi vers le haut »**, comme au
  collège : 2,775 Wh s'écrit 2,78 (un arrondi machine écrirait 2,77, parce que
  2,775 est rangé en mémoire comme 2,77499…). Les parts et les autonomies se
  calculent sur le total EXACT, jamais sur le total arrondi. La récolte d'un
  panneau suit la même règle, au dixième : 4,5 × 0,7 = 3,15 Wh s'écrit 3,2.
"""

from decimal import Decimal, ROUND_HALF_UP

# ── Les consommateurs ─────────────────────────────────────────────────────
#: nom → (courant moyen sous 5 V en mA, ce que c'est)
CONSOS = {
    "Carte Arduino UNO":            (45, "la carte elle-même, DEL d'alimentation et régulateur compris"),
    "Capteur d'humidité du sol":    (2,  "capteur analogique Grove, alimenté en permanence"),
    "Capteur de présence du sac":   (0.5, "un contact que le sac enfonce (bouton Grove) : 5 V à travers 10 kΩ, soit 0,5 mA quand il est appuyé"),
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
           None, "un panneau qui dure 20 ans, un accu à remplacer"),
]

#: € — le panneau 2 W crête que recommande la correction de l'activité 3 (4e).
#: Le prix du 1 W du banc n'est donné nulle part : les 15 € sont ceux du 2 W.
PRIX_PANNEAU_2W = 15.00

#: lieu → moyenne annuelle, en heures équivalent plein soleil par jour
ENSOLEILLEMENT = {
    "Martinique": 5.3,
    #: NREL, PVWatts v8 (base NSRDB), panneau fixe incliné de 20° plein sud ;
    #: décembre : environ 2,4 h (voir l'en-tête de ce fichier)
    "New York": 4.5,
}
#: lieu → comment l'écrire après « Panneau 1 W crête »
EN_LIEU = {"Martinique": "en Martinique", "New York": "à New York"}
#: niveau → lieu de son objet
LIEUX = {"5e": "Martinique", "4e": "New York", "3e": "Martinique"}
#: pertes de chaîne : orientation fixe, salissure, régulateur, température
RENDEMENT_SOLAIRE = 0.70


def solaire(watt_crete, lieu):
    """énergie réellement récoltée par jour, en Wh/jour, arrondie au dixième
    « demi vers le haut » : 4,5 × 0,7 = 3,15 donne 3,2 (round() donnerait 3,1,
    parce que 3,15 est rangé en mémoire comme 3,1499…)."""
    return float(wh_txt(watt_crete * ENSOLEILLEMENT[lieu] * RENDEMENT_SOLAIRE, 1))


# ── Les trois montages, un par niveau ─────────────────────────────────────
#: niveau → [(consommateur, heures de fonctionnement par jour)]
MONTAGES = {
    "5e": [("Carte Arduino UNO", 10.0),
           ("Capteur de présence du sac", 10.0),
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
    """Wh consommés par jour (total EXACT, à afficher avec `wh_txt`), et le détail."""
    detail = []
    for nom, heures in montage:
        ma = CONSOS[nom][0]
        wh = ma / 1000 * TENSION * heures
        detail.append((nom, ma, heures, round(wh, 3)))
    return sum(d[3] for d in detail), detail


def wh_txt(wh, dec=2):
    """Arrondi « demi vers le haut » pour l'affichage seulement : 2,775 → « 2.78 »."""
    exact = Decimal(repr(round(wh, 6)))      # efface le bruit de la virgule flottante
    return str(exact.quantize(Decimal(1).scaleb(-dec), rounding=ROUND_HALF_UP))


def autonomie(source, wh_jour, lieu, watt_crete=1.0):
    """En jours. None = illimité (secteur). 0 = la source ne suffit même pas au jour."""
    if source.capacite is None and source.nom.startswith("Secteur"):
        return None
    if source.capacite is None:                      # solaire : un robinet
        recolte = solaire(watt_crete, lieu)
        return float("inf") if recolte >= wh_jour else 0.0
    return round(source.utile / wh_jour, 2)


if __name__ == "__main__":
    print("Sources — énergie réellement utile sous 5 V")
    print("%-34s %8s %8s %9s" % ("source", "brute", "rendem.", "utile"))
    for s in SOURCES:
        b = "%.2f Wh" % s.brute if s.brute else "—"
        u = "%.1f Wh" % s.utile if s.utile else "—"
        print("%-34s %8s %7.0f %% %9s" % (s.nom, b, s.conversion * 100, u))
    print()
    for lieu in ENSOLEILLEMENT:
        print("Panneau 1 W crête %s : %.1f Wh/jour "
              "(%.1f h équivalent plein soleil × %.0f %%)"
              % (EN_LIEU[lieu], solaire(1, lieu), ENSOLEILLEMENT[lieu], RENDEMENT_SOLAIRE * 100))
    print("Panneau 2 W crête %s : %.1f Wh/jour, %.0f €"
          % (EN_LIEU[LIEUX["4e"]], solaire(2, LIEUX["4e"]), PRIX_PANNEAU_2W))

    for niv, m in MONTAGES.items():
        lieu = LIEUX[niv]
        tot, det = energie_jour(m)
        print("\n── %s ── %s Wh/jour" % (niv, wh_txt(tot)))
        for nom, ma, h, wh in sorted(det, key=lambda d: -d[3]):
            # %g et non %d : un courant de 0,5 mA s'écrirait « 0 mA » ; 45 reste « 45 »
            print("   %-30s %4s mA × %6s h = %6.3f Wh  (%4.1f %%)"
                  % (nom, "%g" % ma, ("%.4f" % h).rstrip("0").rstrip("."), wh, 100 * wh / tot))
        print("   autonomies :")
        for s in SOURCES:
            a = autonomie(s, tot, lieu)
            if a is None:
                txt = "illimitée tant qu'il y a du réseau"
            elif a == float("inf"):
                txt = "suffit chaque jour (%.1f Wh récoltés pour %s consommés)" % (solaire(1, lieu), wh_txt(tot))
            elif a == 0.0:
                txt = "NE SUFFIT PAS (%.1f Wh récoltés pour %s consommés)" % (solaire(1, lieu), wh_txt(tot))
            else:
                # les heures se calculent sur le rapport exact, pas sur les jours arrondis :
                # 2,8 ÷ 5,87 × 24 = 11,4 h (0,48 × 24 donnerait 12)
                txt = "%.2f jour(s) = %.0f h" % (a, s.utile / tot * 24)
            print("      %-34s %s" % (s.nom, txt))
