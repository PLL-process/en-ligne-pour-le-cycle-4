# -*- coding: utf-8 -*-
"""controle_blocs_dessines.py — règle d'or n°308 : un bloc ne se dessine pas, il se capture.

LE CONSTAT
----------
Mesuré le 16/10/2026 sur main (add91c2) : 56 dessins de blocs dans 8 pages. Deux pages de
l'archive 3e_C9.1 imitent Vittascience en CSS (35 programmes `data-blocs`, le schéma qui
suit les curseurs, 8 programmes `data-programme`, le schéma décoratif du haut de
l'évaluation) ; trois stations de 3e_C9.2 montrent quatre SVG « reconstitution
schématique » des paliers ; trois pages de 5e_C6.1 montrent un SVG aux blocs inventés
(« quand le lampadaire démarre »), qu'aucun logiciel ne possède. Chacun de ces dessins dit
à l'élève « voilà ce que tu verras à l'écran », et l'écran dit autre chose : couleurs,
libellés, forme des blocs d'opération.

CE QUE LE CONTRÔLE COMPTE
-------------------------
D1  un dessin HTML : une balise portant `data-blocs`, `data-programme`, ou la classe
    `vb-prog` ou `programme-heros` ;
D2  un dessin SVG : chaque référence, dans une page, à un fichier `.svg` dont le nom
    contient « bloc » (balise, <object>, ou chaîne d'un script de QCM) ;
D3  une capture mal déclarée : une image `class="bloc-capture"` dont le nom n'est pas
    `bloc_vitta_*.png`, qui manque, qui pèse plus de 300 Ko, dont le texte `alt` est vide
    ou trop court, ou qu'aucune ligne « Capture d'écran réelle » d'un SOURCES_MEDIAS.md
    du dossier (ou d'un dossier parent) ne déclare.

Un algorigramme, du pseudo-code ou du code en texte ne sont pas des blocs (règle n°308) :
le contrôle ne les regarde pas. L'archive est lue : ses deux pages servent en classe.

LE REGISTRE EN_ATTENTE
----------------------
Chaque page qui porte encore des dessins y figure avec leur nombre exact. Une page
dessinée hors registre est refusée (un nouveau dessin) ; une page dont le compte a bougé
est refusée aussi (registre périmé) : le lot qui remplace ses dessins retire sa ligne
dans le même commit. Le travail est fini quand EN_ATTENTE = {}.

Usage : python3 _outils/controle_blocs_dessines.py [--muet] [--json]
Sortie : 0 rien à refuser (dessins en attente compris) · 1 refus · 2 rien n'a pu être lu
(règle n°299).
"""
import glob, html, json, os, re, sys

import panne

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = (".git", "node_modules", "_site")

T3 = ("theme-3-creation-conception-realisation-innovations/"
      "C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2/")
T2 = ("theme-2-structure-fonctionnement-comportement/"
      "C6-comprendre-et-modifier-un-programme-associe/5e/5e_C6.1/")
ARCH = "_archive-anciennes-versions/C7_C9_Creation-conception-realisation-innovations/3e_C9.1/"

# Page → nombre de dessins qu'elle porte encore. Relevé du 16/10/2026 (56 dans 8 pages) ; le lot 1
# (archive 3e_C9.1, 45 dessins dans 2 pages) est terminé le 18/10/2026 : ses deux lignes sont retirées.
EN_ATTENTE = {
    # Lot 2 — thème 3 · 3e_C9.2 (Vittascience Arduino, blocs)
    T3 + "sequence_3e_C9.2-C8.3_station_2_programmer.html": 3,
    T3 + "sequence_3e_C9.2-C8.3_station_3_interaction.html": 1,
    T3 + "sequence_3e_C9.2-C8.3_station_alerte_cyclonique.html": 4,
    # Lot 3 — thème 2 · 5e_C6.1 (le lampadaire)
    T2 + "sequence_5e_C6.1-C6.3_programmer_lampadaire.html": 1,
    T2 + "qcm_5e_C6.1-C6.3_programmer_lampadaire.html": 1,
    T2 + "Synthèses/synthese_eleve_5e_C6.1-C6.3.html": 1,
}

POIDS_MAX = 300 * 1024
ALT_MIN = 20
COMMENTAIRE = re.compile(r"<!--.*?-->", re.S)
BALISE = re.compile(r"<[a-zA-Z][\w-]*\b[^<>]*>")
CLASSE = re.compile(r"""\bclass\s*=\s*(["'])(.*?)\1""", re.S | re.I)
ATTR_DESSIN = re.compile(r"""\sdata-(blocs|programme)\s*=""", re.I)
CLASSES_DESSIN = {"vb-prog", "programme-heros"}
SVG_BLOC = re.compile(r"""[\w./%-]*bloc[\w%-]*\.svg\b""", re.I)
IMG = re.compile(r"<img\b[^<>]*>", re.I)
CAPTURE = re.compile(r"^bloc_vitta_[\w-]+\.png$")


def attr(balise, nom):
    m = re.search(r"""\s%s\s*=\s*(["'])(.*?)\1""" % nom, balise, re.S | re.I)
    return html.unescape(m.group(2)) if m else None


def pages(racine):
    return [f for f in sorted(glob.glob(os.path.join(racine, "**", "*.html"), recursive=True))
            if not any(os.sep + e + os.sep in os.sep + os.path.relpath(f, racine) + os.sep
                       for e in ECARTES)]


def rel(f, racine):
    return os.path.relpath(f, racine).replace(os.sep, "/")


def sans_commentaires(texte):
    """Efface les commentaires en gardant les fins de ligne, pour que les numéros de
    ligne restent justes."""
    return COMMENTAIRE.sub(lambda m: "\n" * m.group(0).count("\n"), texte)


def ligne(texte, pos):
    return texte.count("\n", 0, pos) + 1


def dessins(texte):
    """[(type, ligne, quoi)] — les dessins de blocs D1 et D2 d'une page."""
    t = sans_commentaires(texte)
    trouves = []
    for m in BALISE.finditer(t):
        b = m.group(0)
        c = CLASSE.search(b)
        classes = set(c.group(2).split()) if c else set()
        if ATTR_DESSIN.search(b) or classes & CLASSES_DESSIN:
            trouves.append(("D1", ligne(t, m.start()), b[:90]))
    for m in SVG_BLOC.finditer(t):
        trouves.append(("D2", ligne(t, m.start()), m.group(0).rsplit("/", 1)[-1]))
    return trouves


def declarations(dossier, racine):
    """Le texte des SOURCES_MEDIAS.md du dossier de la page et de ses parents."""
    textes, d = [], os.path.abspath(dossier)
    racine = os.path.abspath(racine)
    while True:
        p = os.path.join(d, "SOURCES_MEDIAS.md")
        if os.path.isfile(p):
            textes.append(open(p, encoding="utf-8", errors="replace").read())
        if d == racine or os.path.dirname(d) == d:
            return textes
        d = os.path.dirname(d)


def captures_fautives(f, texte, racine):
    """[(ligne, raison)] — les captures de blocs mal faites ou mal déclarées (D3)."""
    t = sans_commentaires(texte)
    fautes, sources = [], None
    for m in IMG.finditer(t):
        b = m.group(0)
        c = CLASSE.search(b)
        src = attr(b, "src") or ""
        nom = src.split("?")[0].rsplit("/", 1)[-1]
        est_capture = (c and "bloc-capture" in c.group(2).split()) or nom.startswith("bloc_vitta_")
        if not est_capture:
            continue
        n = ligne(t, m.start())
        if not CAPTURE.match(nom):
            fautes.append((n, "« %s » : une capture de blocs se nomme bloc_vitta_*.png" % nom))
            continue
        chemin = os.path.normpath(os.path.join(os.path.dirname(f), src.split("?")[0]))
        if not os.path.isfile(chemin):
            fautes.append((n, "« %s » : fichier introuvable" % src))
        elif os.path.getsize(chemin) > POIDS_MAX:
            fautes.append((n, "« %s » : %d Ko, plus de 300 Ko" % (nom, os.path.getsize(chemin) // 1024)))
        alt = attr(b, "alt")
        if not alt or len(alt.strip()) < ALT_MIN:
            fautes.append((n, "« %s » : texte alt absent ou trop court — il dit le programme en mots" % nom))
        if sources is None:
            sources = declarations(os.path.dirname(f), racine)
        if not any(nom in l and "Capture d'écran réelle" in l.replace("’", "'")
                   for s in sources for l in s.splitlines()):
            fautes.append((n, "« %s » : aucune ligne « Capture d'écran réelle » ne la déclare "
                              "dans un SOURCES_MEDIAS.md (règles n°94, n°308)" % nom))
    return fautes


def releve(racine, registre):
    lues = pages(racine)
    attente, refus, vus = {}, [], set()
    for f in lues:
        texte = open(f, encoding="utf-8", errors="replace").read()
        r = rel(f, racine)
        d = dessins(texte)
        for n, raison in captures_fautives(f, texte, racine):
            refus.append({"page": r, "ligne": n, "raison": "D3 " + raison})
        if r in registre:
            vus.add(r)
            if len(d) != registre[r]:
                refus.append({"page": r, "ligne": 0, "raison":
                              "registre périmé : EN_ATTENTE dit %d dessin(s), la page en porte %d — "
                              "mets la ligne à jour (ou retire-la si 0)" % (registre[r], len(d))})
            elif d:
                attente[r] = d
        elif d:
            refus.append({"page": r, "ligne": d[0][1], "raison":
                          "%d dessin(s) de blocs hors registre (premier : %s %s) — un bloc ne se "
                          "dessine pas, il se capture (règle n°308)" % (len(d), d[0][0], d[0][2])})
    for r in sorted(set(registre) - vus):
        refus.append({"page": r, "ligne": 0, "raison":
                      "registre périmé : la page n'existe plus — retire sa ligne d'EN_ATTENTE"})
    return lues, attente, refus


def main(muet=False, en_json=False, registre=None):
    registre = EN_ATTENTE if registre is None else registre
    lues, attente, refus = releve(DEPOT, registre)
    if not lues:
        return panne.rien_vu("aucune page .html sous %s" % DEPOT)
    total = sum(len(d) for d in attente.values())
    if en_json:
        print(json.dumps({
            "pages_lues": len(lues),
            "dessins_en_attente": total,
            "en_attente": {p: {"compte": len(d), "dessins": [
                {"type": t, "ligne": n, "quoi": q} for t, n, q in d]} for p, d in attente.items()},
            "refus": refus,
        }, ensure_ascii=False, indent=1))
        return 1 if refus else 0
    if refus:
        print("⛔ %d refus (règle d'or n°308 — un bloc ne se dessine pas, il se capture) :" % len(refus))
        for x in refus:
            print("  %s%s  %s" % (x["page"], ":%d" % x["ligne"] if x["ligne"] else "", x["raison"]))
    if not muet or refus:
        if attente:
            print("⏳ %d dessin(s) en attente dans %d page(s) du registre EN_ATTENTE :" % (total, len(attente)))
            for p, d in attente.items():
                print("  %3d  %s" % (len(d), p))
        print("%d page(s) lues · %d dessin(s) en attente%s" % (
            len(lues), total, "" if refus else " · ✅ aucun dessin de blocs hors registre"))
    return 1 if refus else 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv, "--json" in sys.argv))
