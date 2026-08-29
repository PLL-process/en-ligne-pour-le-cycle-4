# -*- coding: utf-8 -*-
"""Les matériaux du lot C7.3 — les caractéristiques, et ce qu'on en calcule.

RÈGLE : aucun nombre affiché dans une page n'est recopié à la main. Les masses,
les prix et les durées de vie sont calculés ici, à partir des caractéristiques du
matériau et de la géométrie de l'objet, puis injectés dans les pages.

Ce que valent ces nombres
-------------------------
Ce sont des **ordres de grandeur d'usage pédagogique**, pas des valeurs de
fiche technique fournisseur. Ils viennent de plages courantes en construction et
en aménagement, et ils sont choisis pour que les comparaisons soient justes entre
elles — c'est le classement qui doit être vrai, pas la troisième décimale.

Deux d'entre eux sont propres au climat de la Martinique, et ils sont le cœur du
lot : **la tenue au rayonnement solaire** et **la tenue au brouillard salin**.
Un tableau générique retiendrait des matériaux que ces deux colonnes éliminent.

Usage : python3 materiaux.py    (affiche toutes les tables des trois lots)
"""

# ── caractéristiques par matériau ─────────────────────────────────────────
# rho    : masse volumique, kg/m³
# sigma  : contrainte admissible en flexion, MPa (ordre de grandeur)
# prix   : € par kilogramme de matière mise en œuvre
# uv     : années avant dégradation visible en plein soleil tropical
# sel    : tenue au brouillard salin, 0 (nulle) à 5 (excellente)
# eau    : tenue au contact permanent d'une terre humide, 0 à 5
# chaud  : température atteinte en plein soleil, °C (surface, 32 °C à l'ombre)
# recyc  : part réellement recyclable en filière courante, %
# formes : procédés de mise en forme praticables au collège
MATERIAUX = {
    "pin": dict(
        nom="Bois — pin non traité", rho=520, sigma=40, prix=2.20,
        uv=2, sel=2, eau=1, chaud=42, recyc=90,
        formes=["sciage", "perçage", "découpe laser (3 mm)"],
        note="Le moins cher, le plus facile à travailler — et le premier à souffrir."),
    "pin_autoclave": dict(
        nom="Bois — pin traité autoclave classe 4", rho=550, sigma=38, prix=3.80,
        uv=8, sel=3, eau=4, chaud=43, recyc=20,
        formes=["sciage", "perçage"],
        note="Traité pour le contact avec la terre. Le traitement ferme la filière de recyclage."),
    "teck": dict(
        nom="Bois — teck (ou bois exotique dense)", rho=650, sigma=75, prix=14.00,
        uv=15, sel=5, eau=5, chaud=44, recyc=85,
        formes=["sciage", "perçage"],
        note="Tient tout, et coûte six fois le pin traité. La provenance est une question."),
    "pvc": dict(
        nom="PVC rigide (stabilisé anti-UV)", rho=1400, sigma=45, prix=3.50,
        uv=8, sel=5, eau=5, chaud=58, recyc=45,
        formes=["sciage", "perçage", "découpe laser (interdite : vapeurs)", "thermoformage"],
        note="Imperméable et bon marché. Sa découpe laser dégage du chlorure d'hydrogène : interdite."),
    "pp_recycle": dict(
        nom="Polypropylène recyclé (plastique de récupération)", rho=950, sigma=30, prix=2.80,
        uv=6, sel=5, eau=5, chaud=55, recyc=95,
        formes=["sciage", "perçage", "moulage", "impression 3D"],
        note="Fait avec des déchets, et redevient un déchet utilisable. Il craint le soleil."),
    "pla": dict(
        nom="PLA (filament d'impression 3D courant)", rho=1240, sigma=50, prix=25.00,
        uv=1, sel=4, eau=3, chaud=52, recyc=15,
        formes=["impression 3D"],
        note="Parfait pour un prototype d'intérieur. Il se déforme dès 55 °C : il n'a rien à faire au soleil."),
    "petg": dict(
        nom="PETG (filament d'impression 3D technique)", rho=1270, sigma=53, prix=28.00,
        uv=5, sel=5, eau=5, chaud=54, recyc=30,
        formes=["impression 3D"],
        note="Tient l'eau, le sel et la chaleur bien mieux que le PLA, pour le même prix au kilo."),
    "acier_galva": dict(
        nom="Acier galvanisé", rho=7850, sigma=235, prix=1.90,
        uv=25, sel=3, eau=3, chaud=68, recyc=95,
        formes=["sciage", "perçage", "pliage"],
        note="Très résistant et très lourd. La galvanisation protège tant qu'elle n'est pas rayée."),
    "inox": dict(
        nom="Acier inoxydable 316 (dit « marine »)", rho=8000, sigma=250, prix=6.50,
        uv=30, sel=5, eau=5, chaud=59, recyc=95,
        formes=["sciage", "perçage", "pliage"],
        note="Le seul métal qui ne craint pas les embruns. Son prix est celui de cette tranquillité."),
    "alu": dict(
        nom="Aluminium anodisé", rho=2700, sigma=160, prix=5.20,
        uv=25, sel=4, eau=4, chaud=57, recyc=95,
        formes=["sciage", "perçage", "pliage"],
        note="Trois fois plus léger que l'acier, et il ne rouille pas — il se corrode autrement. "
             "Anodisé clair, il chauffe moins qu'un acier peint."),
    "beton": dict(
        nom="Béton préfabriqué", rho=2400, sigma=5, prix=0.35,
        uv=30, sel=4, eau=5, chaud=61, recyc=60,
        formes=["moulage"],
        note="Increvable et immobile. On ne le porte pas, on le pose une fois."),
}


# ── objets, et ce qu'on en calcule ────────────────────────────────────────
# Chaque objet est décrit par un VOLUME DE MATIÈRE (m³), déduit de sa géométrie.
OBJETS = {
    "banc": dict(
        nom="L'assise du banc de la cour",
        # planche 1,60 m × 0,40 m × 35 mm
        volume=1.60 * 0.40 * 0.035,
        exigences=dict(sigma=25, uv=8, sel=3, chaud=55, masse_max=35),
        pourquoi=dict(
            sigma="trois élèves assis au milieu, soit 2 000 N sur 1,60 m",
            uv="la cour est en plein soleil ; on ne remplace pas un banc tous les deux ans",
            sel="le collège est à 900 m de la mer : l'air porte du sel toute l'année",
            chaud="au-delà de 55 °C, on ne peut pas s'asseoir à midi sans se brûler",
            masse_max="deux agents doivent pouvoir le déplacer à deux pour laver le sol")),
    "bac": dict(
        nom="Le bac du jardin connecté",
        # caisse 1,00 × 0,50 × 0,40 m, parois 20 mm, fond compris
        volume=(2 * (1.00 * 0.40) + 2 * (0.50 * 0.40) + 1.00 * 0.50) * 0.020,
        exigences=dict(sigma=20, uv=5, sel=3, eau=4, recyc=40, masse_max=60),
        pourquoi=dict(
            sigma="la terre humide pousse sur les parois : 1,5 kN sur le grand côté",
            uv="dehors toute l'année, sans abri — cinq ans, c'est un cycle de collégiens",
            sel="900 m de la mer, alizés permanents",
            eau="la terre reste humide en permanence, c'est le principe d'un jardin arrosé",
            recyc="le collège s'est engagé à ne pas installer ce qu'il ne saura pas jeter",
            masse_max="il doit pouvoir être déplacé plein par quatre élèves et un adulte")),
    "boitier": dict(
        nom="Le boîtier de la station d'alerte",
        # boîte 200 × 150 × 90 mm, six faces. L'ÉPAISSEUR N'EST PAS DONNÉE :
        # elle se déduit du matériau, car la rigidité d'une paroi varie comme
        # le carré de son épaisseur. e = e_ref × racine(sigma_ref / sigma).
        surface=2 * (0.200 * 0.090) + 2 * (0.150 * 0.090) + 2 * (0.200 * 0.150),
        e_ref=0.003, sigma_ref=50,
        exigences=dict(sigma=30, uv=10, sel=5, chaud=60, masse_max=1.2),
        pourquoi=dict(
            sigma="il tient sur un mât de 2 m par vent de 150 km/h",
            uv="en haut d'un mât, sans ombre, toute l'année",
            sel="en cyclone, les embruns remontent à plusieurs kilomètres dans les terres",
            chaud="l'électronique à l'intérieur ne doit pas dépasser sa température de service",
            masse_max="un agent le fixe en tête de mât, en haut d'une échelle, d'une seule main")),
}

CRITERES = [
    ("sigma", "Résistance", "MPa", "au moins"),
    ("uv", "Tenue au soleil", "ans", "au moins"),
    ("sel", "Tenue au sel", "/5", "au moins"),
    ("eau", "Tenue à l'eau", "/5", "au moins"),
    ("chaud", "Température au soleil", "°C", "au plus"),
    ("recyc", "Recyclabilité", "%", "au moins"),
    ("masse_max", "Masse de la pièce", "kg", "au plus"),
]


def epaisseur(cle_mat, cle_obj):
    """Épaisseur de paroi nécessaire, en m — pour les objets dont la géométrie
    s'adapte au matériau. La rigidité d'une paroi en flexion varie comme le carré
    de son épaisseur : un matériau deux fois plus résistant se contente d'une
    paroi 1,41 fois plus fine."""
    o = OBJETS[cle_obj]
    if "e_ref" not in o:
        return None
    return o["e_ref"] * (o["sigma_ref"] / MATERIAUX[cle_mat]["sigma"]) ** 0.5


def volume(cle_mat, cle_obj):
    """Volume de matière, en m³ — fixe, ou déduit du matériau."""
    o = OBJETS[cle_obj]
    if "e_ref" in o:
        return o["surface"] * epaisseur(cle_mat, cle_obj)
    return o["volume"]


def masse(cle_mat, cle_obj):
    """Masse de la pièce, en kg — calculée, jamais recopiée."""
    return MATERIAUX[cle_mat]["rho"] * volume(cle_mat, cle_obj)


def cout(cle_mat, cle_obj):
    """Coût de la matière, en euros."""
    return masse(cle_mat, cle_obj) * MATERIAUX[cle_mat]["prix"]


def cout_sur(cle_mat, cle_obj, annees):
    """Coût sur une durée : on remplace la pièce chaque fois qu'elle est usée.
    Comparer des prix d'achat sans comparer des durées de vie n'apprend rien."""
    import math
    n = max(1, math.ceil(annees / MATERIAUX[cle_mat]["uv"]))
    return cout(cle_mat, cle_obj) * n, n


def valeur(cle_mat, cle_obj, critere):
    if critere == "masse_max":
        return masse(cle_mat, cle_obj)
    return MATERIAUX[cle_mat][critere]


def tient(cle_mat, cle_obj, critere):
    """Le matériau tient-il ce seuil pour cet objet ?"""
    seuil = OBJETS[cle_obj]["exigences"].get(critere)
    if seuil is None:
        return True
    v = valeur(cle_mat, cle_obj, critere)
    return v <= seuil if critere in ("chaud", "masse_max") else v >= seuil


def verdict(cle_mat, cle_obj):
    """(retenu ?, liste des critères qui échouent)"""
    rates = [c for c in OBJETS[cle_obj]["exigences"] if not tient(cle_mat, cle_obj, c)]
    return (not rates), rates


def table(cle_obj, candidats):
    """Le tableau complet, prêt à être affiché ou vérifié."""
    lignes = []
    for m in candidats:
        ok, rates = verdict(m, cle_obj)
        lignes.append(dict(
            cle=m, nom=MATERIAUX[m]["nom"],
            masse=masse(m, cle_obj), cout=cout(m, cle_obj),
            valeurs={c: valeur(m, cle_obj, c) for c, _, _, _ in CRITERES
                     if c in OBJETS[cle_obj]["exigences"]},
            retenu=ok, rates=rates, note=MATERIAUX[m]["note"],
            formes=MATERIAUX[m]["formes"]))
    return lignes


CANDIDATS = {
    "banc": ["pin", "pin_autoclave", "teck", "pvc", "acier_galva", "beton"],
    "bac": ["pin", "pin_autoclave", "pvc", "pp_recycle", "acier_galva", "teck"],
    "boitier": ["pla", "petg", "pvc", "alu", "inox", "pp_recycle"],
}


def vg(x, dec=1):
    return ("%.*f" % (dec, x)).replace(".", ",")


def main():
    for obj in ("banc", "bac", "boitier"):
        o = OBJETS[obj]
        print("═" * 92)
        if "e_ref" in o:
            print("%s — surface %s m², épaisseur déduite du matériau"
                  % (o["nom"], vg(o["surface"], 3)))
        else:
            print("%s — volume de matière %s L" % (o["nom"], vg(o["volume"] * 1000, 2)))
        ex = o["exigences"]
        print("exigences : " + " · ".join(
            "%s %s %s %s" % (lib, sens, ex[c], u)
            for c, lib, u, sens in CRITERES if c in ex))
        print("-" * 92)
        entetes = [lib for c, lib, u, s in CRITERES if c in ex]
        print("%-42s %8s %9s  %s" % ("matériau", "masse", "coût", " ".join(
            "%8s" % e[:8] for e in entetes)))
        for l in table(obj, CANDIDATS[obj]):
            vals = " ".join("%8s" % vg(l["valeurs"][c], 0 if c != "masse_max" else 1)
                            for c, lib, u, s in CRITERES if c in ex)
            print("%-42s %6s kg %7s €  %s  %s"
                  % (l["nom"][:42], vg(l["masse"], 1), vg(l["cout"], 2), vals,
                     "RETENU" if l["retenu"] else "recalé : " + ", ".join(l["rates"])))
        retenus = [l["nom"] for l in table(obj, CANDIDATS[obj]) if l["retenu"]]
        print("→ %d matériau(x) retenu(s) : %s" % (len(retenus), ", ".join(retenus) or "aucun"))
        print()


if __name__ == "__main__":
    main()
