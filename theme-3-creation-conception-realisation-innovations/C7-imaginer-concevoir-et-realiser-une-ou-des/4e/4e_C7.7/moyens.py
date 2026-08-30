# -*- coding: utf-8 -*-
"""Les moyens de l'atelier, et ce qu'ils savent faire — lot C7.7.

RÈGLE : aucun nombre affiché dans une page n'est recopié à la main. Les temps,
les épaisseurs minimales et les verdicts de faisabilité sont calculés ici, à
partir du domaine de chaque moyen et de la géométrie de la pièce.

Ce que valent ces nombres
-------------------------
Ce sont des **ordres de grandeur d'atelier de collège**, pas des fiches
constructeur : imprimante à dépôt de fil (buse 0,4 mm, couche 0,2 mm),
découpeuse laser CO₂ de 40 à 60 W, petite fraiseuse 3 axes. Ce qui doit être
vrai, c'est **quel moyen sait faire quoi** — pas la seconde près.

Les deux idées que le module rend calculables
---------------------------------------------
**1. Un moyen n'a pas de qualité, il a un DOMAINE.** Hors de son domaine, il ne
fait pas « moins bien » : il fait *autre chose*, ou il ne fait pas. Une fraiseuse
ne rate pas un angle interne vif — elle le fait rond, parce qu'un outil rond ne
peut rien faire d'autre.

**2. Tout moyen DÉFORME le dessin, à sa manière, et toujours.** C'est le champ
`empreinte`. Le laser élargit de son trait de coupe, la fraiseuse arrondit les
angles internes, l'impression laisse un bourrelet de première couche. Le dessin
n'est pas la pièce : c'est ce qu'on a demandé, et chaque machine y répond avec
son accent.

Usage : python3 moyens.py    (affiche les tables des deux lots)
"""

# ── les moyens et leur domaine ────────────────────────────────────────────
# e_min      : épaisseur de paroi minimale réalisable, mm
# e_etanche  : épaisseur minimale quand la paroi doit être ÉTANCHE, mm
# r_int      : rayon imposé à tout angle interne, mm (0 = angle vif possible)
# surplomb   : angle maximal d'une surface en surplomb, ° (None = sans objet)
# res_z      : plus petit détail tenu dans l'épaisseur, mm
# tol        : tolérance courante sur une cote, mm
# min_piece  : temps machine par pièce, minutes
# prep       : temps de préparation, une fois pour tout le lot, minutes
# empreinte  : ce que le moyen change dans le dessin, toujours, sans le dire
MOYENS = {
    "impression": dict(
        nom="Impression 3D (dépôt de fil, buse 0,4 mm, couche 0,2 mm)",
        e_min=0.8, e_etanche=1.6, r_int=0.0, surplomb=45, res_z=0.4, tol=0.3,
        min_piece=40, prep=15,
        matieres=["PLA", "PETG", "PP recyclé"],
        traversant=True, borgne=True,
        empreinte="un bourrelet de première couche à la base, et des stries visibles "
                  "sur les faces inclinées",
        note="Le seul moyen qui fabrique une forme fermée, un volume creux, une "
             "contre-dépouille. Il paie cette liberté en temps : de loin le plus lent.",
        ne_sait_pas="une paroi étanche de moins de quatre passes de buse, ni un surplomb "
                    "au-delà de 45° sans support — et un support laisse une surface rugueuse"),
    "laser": dict(
        nom="Découpe laser CO₂ (plaque à plat)",
        e_min=1.0, e_etanche=1.0, r_int=0.0, surplomb=None, res_z=0.1, tol=0.2,
        min_piece=2, prep=10,
        matieres=["PMMA", "contreplaqué", "carton"],
        traversant=True, borgne=False,
        empreinte="un trait de coupe de 0,2 mm : toute ouverture sort 0,2 mm plus large "
                  "que dessinée, et le chant est légèrement conique",
        note="Très rapide, très précis, et il ne travaille qu'à plat. Angles internes "
             "parfaitement vifs : un faisceau n'a pas de rayon.",
        ne_sait_pas="un trou borgne, un relief, ni une épaisseur variable — et le PVC lui "
                    "est INTERDIT : chauffé, il dégage du chlorure d'hydrogène"),
    "fraiseuse": dict(
        nom="Fraiseuse numérique 3 axes (fraise Ø 3 mm)",
        e_min=1.5, e_etanche=1.5, r_int=1.5, surplomb=None, res_z=0.05, tol=0.05,
        min_piece=12, prep=25,
        matieres=["PMMA", "PVC", "contreplaqué", "aluminium"],
        traversant=True, borgne=True,
        empreinte="tout angle interne arrondi au rayon de la fraise, soit 1,5 mm — "
                  "ce n'est pas un défaut, c'est l'outil",
        note="La meilleure précision de l'atelier, et la seule qui usine le métal.",
        ne_sait_pas="un angle interne plus serré que le rayon de sa fraise"),
    "sciage": dict(
        nom="Sciage et perçage à la main",
        e_min=1.0, e_etanche=1.0, r_int=0.0, surplomb=None, res_z=0.5, tol=1.0,
        min_piece=18, prep=0,
        matieres=["PMMA", "PVC", "contreplaqué", "aluminium"],
        traversant=True, borgne=True,
        empreinte="une cote juste à 1 mm près, et deux pièces jamais tout à fait pareilles",
        note="Aucune préparation, aucune machine à réserver. Le seul moyen disponible "
             "quand tout le reste est pris.",
        ne_sait_pas="une fente étroite ni une cote au dixième — la main tremble à 1 mm près"),
    "thermoformage": dict(
        nom="Thermoformage sur moule",
        e_min=0.5, e_etanche=0.8, r_int=3.0, surplomb=None, res_z=1.0, tol=1.0,
        min_piece=4, prep=60,
        matieres=["PMMA", "PVC", "PETG"],
        traversant=False, borgne=False,
        empreinte="une paroi qui s'amincit dans les angles, d'autant plus que la forme "
                  "est profonde",
        note="Une heure pour faire le moule, puis quatre minutes par pièce. "
             "Il ne devient intéressant qu'en série.",
        ne_sait_pas="une contre-dépouille — la pièce ne sortirait pas du moule — ni un perçage"),
    "pliage": dict(
        nom="Pliage de tôle (plieuse d'établi)",
        e_min=0.5, e_etanche=0.5, r_int=2.0, surplomb=None, res_z=0.5, tol=0.5,
        min_piece=6, prep=20,
        matieres=["aluminium", "acier"],
        traversant=False, borgne=False,
        empreinte="un rayon de pliage imposé par la matrice, et la tôle qui s'allonge "
                  "un peu au pli",
        note="Rapide et solide, à condition que la pièce se déplie à plat.",
        ne_sait_pas="un perçage — les trous se percent avant, sur la tôle à plat"),
}

#: Le mot par lequel chaque moyen impose son rayon d'angle interne.
_POURQUOI_RAYON = {
    "fraiseuse": "sa fraise de 3 mm arrondit tout angle interne à 1,5 mm",
    "thermoformage": "la matière chaude ne descend pas dans un angle plus serré que 3 mm",
    "pliage": "le rayon de pliage est celui de la matrice, soit 2 mm",
}


# ── les pièces, décrites par leurs TRAITS ─────────────────────────────────
# Un trait = une exigence de forme que le moyen doit savoir produire.
PIECES = {
    "support": dict(
        nom="Le support du capteur d'humidité",
        contexte="Une plaque de 60 × 40 mm qui tient la sonde à 12 cm de profondeur "
                 "contre la paroi du bac, et qui se retire pour l'hivernage.",
        etanche=False, matiere="PMMA", moyen_vise=None,
        traits=[
            ("epaisseur", "Paroi de 3 mm", 3.0,
             "la plaque tient la sonde sans fléchir quand la terre pousse"),
            ("tol", "Tolérance de 0,3 mm sur la fente", 0.3,
             "trop large, la sonde bouge ; trop étroite, elle n'entre pas"),
            ("traversant", "Deux perçages traversants Ø 4 mm", True,
             "deux vis M4 traversent la paroi du bac et serrent le support"),
        ],
        quantites=[(4, "les quatre bacs du jardin"),
                   (30, "un support par élève, une classe entière")],
        temps_dispo=180),
    "boitier": dict(
        nom="Le boîtier de la station d'alerte",
        contexte="Celui choisi en 3e_C7.3 — PETG, imprimé au collège — et modélisé en "
                 "3e_C7.6. 200 × 150 × 90 mm, en tête d'un mât de 2 m.",
        etanche=True, matiere="PETG", moyen_vise="impression",
        traits=[
            ("epaisseur", "Paroi étanche de 2,9 mm", 2.9,
             "l'épaisseur calculée en 3e_C7.3 : e = 3,00 × racine(50 ÷ 53) pour le PETG"),
            ("surplomb", "Casquette anti-pluie inclinée à 70°", 70.0,
             "elle écarte l'eau du joint : c'est une fonction, pas une décoration"),
            ("res_z", "Rainure de joint de 0,3 mm de profondeur", 0.3,
             "le joint torique doit se loger et rester en place"),
            ("tol", "Jeu de 0,1 mm entre le couvercle et le fond", 0.1,
             "le couvercle doit fermer juste, sans forcer et sans jouer"),
            ("r_int", "Angles internes vifs au fond du boîtier", 0.0,
             "l'électronique se cale dans les coins"),
        ],
        quantites=[(1, "le prototype de la station"),
                   (12, "une station par bâtiment, en série")],
        temps_dispo=180),
}

#: Les corrections possibles du DESSIN — trait → (nouvelle valeur, geste, effet).
#: Aucune ne touche au cahier des charges : ni ce que l'objet doit faire, ni son
#: encombrement, ni sa matière. Et l'une des quatre n'a rien à corriger.
CORRECTIONS = {
    "surplomb": (45.0, "ramener la casquette à 45°, l'angle que la buse tient sans support",
                 "elle écarte toujours l'eau : c'est la pente qui compte, pas l'angle exact"),
    "res_z": (0.6, "creuser la rainure à 0,6 mm, soit trois couches de 0,2 mm",
              "le joint torique se loge mieux, et rien d'autre ne bouge"),
    "tol": (0.4, "dessiner 0,4 mm de jeu entre le couvercle et le fond",
            "le couvercle ferme, et le joint fait l'étanchéité — c'est son travail, pas celui du jeu"),
    "epaisseur": (2.9, "ne rien changer : 2,9 mm ont été calculés en 3e_C7.3",
                  "quatre passes de buse suffisent à l'étanchéité, on en a sept"),
    "r_int": (0.0, "ne rien changer : l'impression sait faire un angle interne vif",
              "c'est la fraiseuse qui ne saurait pas — et on n'imprime pas à la fraiseuse"),
}

#: Les traits qu'il ne faut PAS toucher. Un contrôle qui ne distingue pas ce
#: qu'il a réparé de ce qu'il n'a jamais touché apprend à tout changer
#: (règle d'or n°219).
SANS_CORRECTION = ("epaisseur", "r_int")

MOYENS_PAR_PIECE = {
    "support": ["laser", "fraiseuse", "impression", "sciage", "thermoformage"],
    "boitier": ["impression", "thermoformage", "fraiseuse", "laser", "sciage"],
}


def vg(x, dec=1):
    if isinstance(x, bool):
        return "oui" if x else "non"
    return ("%.*f" % (dec, x)).replace(".", ",")


def tient_trait(cle_moyen, cle, valeur, etanche=False):
    """Le moyen sait-il produire ce trait ? → (ok, motif du refus)"""
    m = MOYENS[cle_moyen]
    if cle == "epaisseur":
        seuil = m["e_etanche"] if etanche else m["e_min"]
        return (valeur >= seuil,
                "il ne fait pas une paroi %sde moins de %s mm"
                % ("étanche " if etanche else "", vg(seuil, 1)))
    if cle == "r_int":
        return (valeur >= m["r_int"],
                _POURQUOI_RAYON.get(cle_moyen, "il impose un rayon de %s mm aux angles internes"
                                    % vg(m["r_int"], 1)))
    if cle == "surplomb":
        if m["surplomb"] is None:
            return (True, "")
        return (valeur <= m["surplomb"],
                "au-delà de %d° il faut un support, et le support laisse une surface rugueuse"
                % m["surplomb"])
    if cle == "res_z":
        return (valeur >= m["res_z"],
                "il ne tient pas un détail de moins de %s mm dans l'épaisseur" % vg(m["res_z"], 2))
    if cle == "tol":
        return (valeur >= m["tol"], "sa tolérance courante est de %s mm" % vg(m["tol"], 2))
    if cle == "traversant":
        return (m["traversant"] or not valeur, "il ne perce pas")
    if cle == "borgne":
        return (m["borgne"] or not valeur, "il ne fait pas de trou borgne")
    raise KeyError(cle)


def traits_de(cle_piece):
    return {c: v for c, _, v, _ in PIECES[cle_piece]["traits"]}


def verdict(cle_moyen, cle_piece, traits=None):
    """(retenu ?, [motifs de refus]) — matière comprise."""
    p = PIECES[cle_piece]
    traits = traits_de(cle_piece) if traits is None else traits
    rates = []
    if p["matiere"] not in MOYENS[cle_moyen]["matieres"]:
        rates.append("il n'accepte pas le %s" % p["matiere"])
    for cle, valeur in traits.items():
        ok, motif = tient_trait(cle_moyen, cle, valeur, p["etanche"])
        if not ok:
            rates.append(motif)
    return (not rates), rates


def temps(cle_moyen, n):
    """Temps total pour n pièces : préparation + n × temps machine, en minutes."""
    m = MOYENS[cle_moyen]
    return m["prep"] + n * m["min_piece"]


def duree_txt(minutes):
    minutes = int(round(minutes))
    if minutes < 60:
        return "%d min" % minutes
    h, m = divmod(minutes, 60)
    return "%d h" % h if m == 0 else "%d h %02d" % (h, m)


def table(cle_piece, traits=None):
    p = PIECES[cle_piece]
    lignes = []
    for cle in MOYENS_PAR_PIECE[cle_piece]:
        ok, rates = verdict(cle, cle_piece, traits)
        lignes.append(dict(
            cle=cle, nom=MOYENS[cle]["nom"], retenu=ok, rates=rates,
            note=MOYENS[cle]["note"], empreinte=MOYENS[cle]["empreinte"],
            ne_sait_pas=MOYENS[cle]["ne_sait_pas"],
            temps={n: temps(cle, n) for n, _ in p["quantites"]},
            tient_delai={n: temps(cle, n) <= p["temps_dispo"] for n, _ in p["quantites"]}))
    return lignes


def corrige(cle_piece):
    """Les traits du dessin, une fois les corrections appliquées."""
    tr = traits_de(cle_piece)
    for cle, (nouvelle, _, _) in CORRECTIONS.items():
        if cle in tr:
            tr[cle] = nouvelle
    return tr


def main():
    for cle_piece in ("support", "boitier"):
        p = PIECES[cle_piece]
        print("═" * 104)
        print("%s — %s%s" % (p["nom"], p["matiere"], " · paroi étanche" if p["etanche"] else ""))
        print("traits : " + " · ".join("%s = %s" % (lib, vg(v, 1)) for _, lib, v, _ in p["traits"]))
        print("temps machine disponible : %s" % duree_txt(p["temps_dispo"]))
        print("-" * 104)
        for l in table(cle_piece):
            t = " · ".join("%d p. %s%s" % (n, duree_txt(l["temps"][n]),
                                           "" if l["tient_delai"][n] else " ✗")
                           for n, _ in p["quantites"])
            print("%-52s %-8s %-30s %s"
                  % (l["nom"][:52], "RETENU" if l["retenu"] else "recalé", t,
                     "" if l["retenu"] else "; ".join(l["rates"])[:60]))
        r = [l["nom"] for l in table(cle_piece) if l["retenu"]]
        print("→ %d moyen(s) : %s" % (len(r), ", ".join(r) or "aucun"))
        print()

    print("═" * 104)
    print("BOÎTIER — après correction du DESSIN (le cahier des charges ne bouge pas)")
    tr = corrige("boitier")
    print("traits corrigés : " + " · ".join("%s=%s" % (k, vg(v, 1)) for k, v in tr.items()))
    for l in table("boitier", tr):
        print("%-52s %-8s %s" % (l["nom"][:52], "RETENU" if l["retenu"] else "recalé",
                                 "" if l["retenu"] else "; ".join(l["rates"])[:60]))
    r = [l["nom"] for l in table("boitier", tr) if l["retenu"]]
    print("→ %d moyen(s) : %s" % (len(r), ", ".join(r) or "aucun"))


if __name__ == "__main__":
    main()
