# -*- coding: utf-8 -*-
"""controle_unites.py — règle d'or n°312 : une unité se lit en toutes lettres.

LE CONSTAT
----------
Le 25/10/2026, Pascal, devant le tableau « Les chiffres pour choisir » de Chengdu (« Consommation : 1,2 W ·
0,4 W · 12 W ») : « beaucoup d'élèves ne pourront pas dire que ce sont des watts […] même s'il l'a vu en
physique, il ne s'en souvient pas toujours ». Un symbole qu'on ne sait pas lire oblige à deviner avant de
raisonner. Le premier comptage du même jour : environ 800 grandeurs dans 64 pages élèves, et 50 pages où au
moins une unité n'est jamais écrite en toutes lettres.

LA RÈGLE (décision de Pascal, 25/10/2026)
-----------------------------------------
À la première apparition d'une unité dans chaque activité, chaque tableau et chaque question de QCM, le
symbole est suivi de son nom en toutes lettres, au pluriel, entre parenthèses : « 1,2 W (watts) ». Dans un
tableau, le nom peut aussi être dans l'intitulé de la ligne ou de la colonne (« Consommation (en watts, W) »).
Les unités connues depuis l'école (m, cm, mm, km, g, kg, L, mL, s, min, h, °C, €, %, km/h, m², m³) n'ont
pas besoin d'être nommées.

Dans un choix (question de QCM, liste à choix, groupe de boutons), quand UNE SEULE option porte l'unité,
l'unité s'y écrit en toutes lettres, sans symbole ni parenthèse : « il ne manipule que du 5 volts ». Une
parenthèse distinguerait cette option des autres ; un rappel dans l'énoncé la désignerait. (Constaté le
25/10/2026 : 5 questions de QCM et 3 listes où la bonne réponse était la seule à porter « (volts) ».)

PÉRIMÈTRE (règle n°47 — un contrôle déclare ce qu'il regarde)
-------------------------------------------------------------
Pages lues : les pages qu'un élève lit, sous theme-* (séquences, QCM, synthèses élève, lexiques, ateliers,
TP, activités, entraînements, fiches de maths, mini-quiz, cahiers). Hors archive, hors dossiers « _… »,
hors synthèses professeur.

Zones (là où le nom doit apparaître) :
  - une activité : le texte compris entre deux titres h2, ou entre deux débuts d'activité (bloc
    « activite », titre h3 « Activité N », « REFAIRE », « Réinvestissement », « Bilan », « Bonus ») ;
  - un tableau : tout son texte, intitulés compris ;
  - une question de QCM : tous les textes de l'objet de la question (énoncé, options, explication, exemple,
    erreur classique, réfutations, à retenir), lus dans le tableau QUESTIONS du script ;
  - un schéma (depuis le 25/10/2026, phase 2) : chaque <svg> intégré à une page, et chaque fichier .svg sous
    theme-* (hors dossiers « _… » et « fichiers_drawio », qui gardent les sources d'édition). Son texte
    VISIBLE (<text>, <tspan>) doit nommer ses unités : la forme retenue est la ligne « Unités : V (volts) »
    sous le dessin, posée par `_outils/legende_unites.py`.

Mesuré : dans chaque zone, chaque unité écrite après un nombre (« 12 V », « 0,4 W », « 2 000 mAh ») doit
y voir son nom en toutes lettres au moins une fois (singulier ou pluriel, avec ou sans accent).
Mesuré aussi : aucun choix n'a une seule option portant un nom entre parenthèses (« (volts) »,
« (12 V, en volts) »). Choix lus : les options d'une question de QCM, une liste <select> dont la première
option est vide (« — je choisis — » : une question, pas un réglage de simulateur), les étiquettes d'un
<fieldset>.

NON mesuré, donc NON couvert, et à juger à l'œil :
  - que le nom suive bien la PREMIÈRE apparition (le contrôle accepte le nom n'importe où dans la zone) ;
  - le texte écrit par un script à l'exécution (simulateurs), les listings de code (<pre>, <code>) ;
  - le texte d'un schéma qui n'est que dans son <title> ou sa <desc> (l'œil ne le voit pas) : seuls <text> et
    <tspan> comptent ;
  - une unité écrite sans nombre devant (« en V ») ou séparée de son nombre par une balise de mise en forme
    (« <b>12</b> V ») — cette dernière est rattrapée : le texte est aplati avant la lecture.

Usage : python3 _outils/controle_unites.py [--muet] [--json] [--images] [chemin…]
Sortie : 0 rien à reprendre · 1 au moins une unité sans son nom, ou une option seule à porter le nom ·
2 rien pu lire (règle n°299).
"""
from __future__ import annotations

import json
import os
import re
import sys

import warnings

from bs4 import BeautifulSoup, Comment, NavigableString, Tag, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)
MOTIFS = ("sequence_", "sequence-", "sequence.html", "qcm_", "qcm-", "synthese_eleve", "lexique", "atelier",
          "tp_", "activite", "entrainement", "fiche_maths", "vittascience", "miniquiz", "mini_quiz", "cahier")

V = "[eéèê]"
A = "[aàâ]"
# symbole → motif du nom en toutes lettres (singulier ou pluriel), et nom à écrire (au pluriel)
UNITES = [
    ("kWh", r"kilo-?watts?[- ]?heures?", "kilowattheures"),
    ("mWh", r"milli-?watts?[- ]?heures?", "milliwattheures"),
    ("Wh", r"(?<![a-zé])watts?[- ]?heures?", "wattheures"),
    ("kW", r"kilo-?watts?\b(?![- ]?heure)", "kilowatts"),
    ("mW", r"milli-?watts?\b(?![- ]?heure)", "milliwatts"),
    ("W", r"(?<![a-zé])watts?\b(?![- ]?heure)", "watts"),
    ("mAh", r"milli-?amp" + V + r"res?[- ]?heures?", "milliampères-heures"),
    ("Ah", r"(?<![a-zé])amp" + V + r"res?[- ]?heures?", "ampères-heures"),
    ("µA", r"micro-?amp" + V + r"res?", "microampères"),
    ("mA", r"milli-?amp" + V + r"res?\b(?![- ]?heure)", "milliampères"),
    ("A", r"(?<![a-zé])amp" + V + r"res?\b(?![- ]?heure)", "ampères"),
    ("kV", r"kilo-?volts?", "kilovolts"),
    ("mV", r"milli-?volts?", "millivolts"),
    ("V", r"(?<![a-zé])volts?\b", "volts"),
    ("kΩ", r"kilo-?ohms?", "kiloohms"),
    ("MΩ", r"m" + V + r"ga-?ohms?", "mégaohms"),
    ("Ω", r"(?<![a-zé])ohms?\b", "ohms"),
    ("GHz", r"giga-?hertz", "gigahertz"),
    ("MHz", r"m" + V + r"ga-?hertz", "mégahertz"),
    ("kHz", r"kilo-?hertz", "kilohertz"),
    ("Hz", r"(?<![a-zé])hertz", "hertz"),
    ("N·m", r"newtons?[- ]m" + V + r"tres?", "newtons-mètres"),
    ("N.m", r"newtons?[- ]m" + V + r"tres?", "newtons-mètres"),
    ("kN", r"kilo-?newtons?", "kilonewtons"),
    ("N", r"(?<![a-zé])newtons?\b(?![- ]m)", "newtons"),
    ("GPa", r"giga-?pascals?", "gigapascals"),
    ("MPa", r"m" + V + r"ga-?pascals?", "mégapascals"),
    ("kPa", r"kilo-?pascals?", "kilopascals"),
    ("hPa", r"hecto-?pascals?", "hectopascals"),
    ("Pa", r"(?<![a-zé])pascals?\b", "pascals"),
    ("MJ", r"m" + V + r"ga-?joules?", "mégajoules"),
    ("kJ", r"kilo-?joules?", "kilojoules"),
    ("dB", r"d" + V + r"cibels?", "décibels"),
    ("lx", r"\blux\b", "lux"),
    ("lm", r"\blumens?\b", "lumens"),
    ("ppm", r"parties? par million", "parties par million"),
    ("µg/m³", r"microgrammes? par m" + V + r"tre cube", "microgrammes par mètre cube"),
    ("kgCO₂e", r"kilogrammes? " + V + r"quivalent", "kilogrammes équivalent CO₂"),
    ("kg CO₂e", r"kilogrammes? " + V + r"quivalent", "kilogrammes équivalent CO₂"),
    ("gCO₂e", r"(?<![a-zé])grammes? " + V + r"quivalent", "grammes équivalent CO₂"),
    ("tCO₂e", r"tonnes? " + V + r"quivalent", "tonnes équivalent CO₂"),
    ("To", r"t" + V + r"ra-?octets?", "téraoctets"),
    ("Go", r"giga-?octets?", "gigaoctets"),
    ("Mo", r"m" + V + r"ga-?octets?", "mégaoctets"),
    ("ko", r"kilo-?octets?", "kilooctets"),
    ("Gbit/s", r"gigabits? par seconde", "gigabits par seconde"),
    ("Mbit/s", r"m" + V + r"gabits? par seconde", "mégabits par seconde"),
    ("kbit/s", r"kilobits? par seconde", "kilobits par seconde"),
    ("bit/s", r"(?<![a-zé])bits? par seconde", "bits par seconde"),
    ("tr/min", r"tours? par minute", "tours par minute"),
    ("m/s", r"m" + V + r"tres? par seconde", "mètres par seconde"),
    ("ms", r"millisecondes?", "millisecondes"),
    ("µs", r"microsecondes?", "microsecondes"),
]
NOMS = {s: (re.compile(m, re.I), n) for s, m, n in UNITES}
# un nom entre parenthèses : « (volts) », « (en volts) », « (12 V, en volts) », « (45 MPa, en mégapascals) »
NOM_PAR = re.compile(r"\((?:[^()]*?,\s*)?(?:en\s+)?(?:" + "|".join("(?:%s)" % m for _, m, _ in UNITES)
                     + r")\s*(?:,[^()]*)?\)", re.I)
_SYMS = sorted({s for s, _, _ in UNITES}, key=len, reverse=True)
NOMBRE = r"(?<![\w.,/:])(?<!niveau )[\u2212-]?\d+(?:[ \u00a0\u202f]\d{3})*(?:[.,]\d+)?"
OCC = re.compile(NOMBRE + r"[ \u00a0\u202f]?(" + "|".join(re.escape(s) for s in _SYMS) + r")(?![\w\u00c0-\u00ff\u00b2\u00b3:'\u2019]|[/\u00b7.][A-Za-z\u00b5])")

BLOCS = ["td", "th", "li", "p", "div", "dt", "dd", "br", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "caption",
         "figcaption", "legend", "label", "option", "button", "section", "article", "header", "summary", "blockquote"]
DEBUT_ACT = re.compile(r"^\W*(?:Activit[ée]\s*\d|REFAIRE|R[ée]investissement|Bilan|Bonus|Billet d|Transfert|Mon bilan)", re.I)


def ouvrir(chemin):
    with open(chemin, encoding="utf-8", errors="replace") as f:
        return f.read()


def pages(racines):
    vues = set()
    for racine in racines:
        if os.path.isfile(racine):
            vues.add(os.path.abspath(racine))
            continue
        for dossier, _, fichiers in os.walk(racine):
            d = dossier.replace(os.sep, "/")
            if any(e in d for e in ECARTES) or "/." in d or "/_" in d:
                continue
            rel = os.path.relpath(dossier, DEPOT).replace(os.sep, "/")
            if not rel.startswith("theme-"):
                continue
            for f in fichiers:
                if f.endswith(".html") and f.startswith(MOTIFS) and "professeur" not in f:
                    vues.add(os.path.join(dossier, f))
                elif f.endswith(".svg") and "fichiers_drawio" not in d:
                    vues.add(os.path.join(dossier, f))
    return sorted(vues)


def plat(t):
    t = re.sub(r"\s+", " ", t.replace("\u00a0", " ").replace("\u202f", " "))
    return re.sub(r"(?: ¦ ?)+", " ¦ ", t).strip(" ¦")


# ── les questions de QCM, lues dans le script ────────────────────────────────
def objets_js(src, debut):
    """Découpe le tableau littéral qui commence à `debut` (sur le « [ ») en objets de premier niveau."""
    i, n = debut + 1, len(src)
    prof, cour, objets, quote = 0, None, [], None
    while i < n:
        c = src[i]
        if quote:
            if c == "\\":
                i += 2
                continue
            if c == quote:
                quote = None
        elif c in "\"'`":
            quote = c
        elif src.startswith("/*", i):
            j = src.find("*/", i + 2)
            i = n if j < 0 else j + 2
            continue
        elif src.startswith("//", i) and (i == 0 or src[i - 1] in " \t\n,[{"):
            j = src.find("\n", i)
            i = n if j < 0 else j
            continue
        elif c in "{[(":
            if prof == 0 and c == "{":
                cour = i
            prof += 1
        elif c in "}])":
            if prof == 0:
                break
            prof -= 1
            if prof == 0 and c == "}" and cour is not None:
                objets.append(src[cour:i + 1])
                cour = None
        i += 1
    return objets


def chaines_js(obj):
    out = []
    for m in re.finditer(r'"((?:[^"\\]|\\.)*)"|\'((?:[^\'\\]|\\.)*)\'|`((?:[^`\\]|\\.)*)`', obj, re.S):
        s = next(g for g in m.groups() if g is not None)
        out.append(s.replace('\\"', '"').replace("\\'", "'").replace("\\n", " "))
    return " ".join(out)


def questions(src):
    zones = []
    for m in re.finditer(r"\b(?:const|let|var)\s+(?:QUESTIONS|questions)\s*=\s*\[", src):
        for k, obj in enumerate(objets_js(src, m.end() - 1), 1):
            texte = BeautifulSoup(chaines_js(obj), "html.parser").get_text(" ")
            zones.append(("question %d" % k, plat(texte)))
    return zones


def choix(src):
    """[(libellé, [textes des options])] : les questions de QCM, les listes-questions, les fieldsets."""
    res = []
    for m in re.finditer(r"\b(?:const|let|var)\s+(?:QUESTIONS|questions)\s*=\s*\[", src):
        for k, obj in enumerate(objets_js(src, m.end() - 1), 1):
            mo = re.search(r'\bo\s*:\s*\[((?:\s*(?:"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')\s*,?)+)\s*\]', obj)
            if mo:
                res.append(("question %d" % k, [BeautifulSoup(chaines_js(x.group(0)), "html.parser").get_text(" ")
                                                for x in re.finditer(r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'', mo.group(1))]))
    soup = BeautifulSoup(src, "html.parser")
    for t in soup(["script", "style", "template"]):
        t.decompose()
    for sel in soup.find_all("select"):
        opts = sel.find_all("option")
        if opts and opts[0].get("value") == "" and len(opts) > 2:
            res.append(("liste %s" % (sel.get("id") or "?"), [o.get_text(" ") for o in opts[1:]]))
    for fs in soup.find_all("fieldset"):
        leg = fs.find("legend")
        res.append(("choix « %s »" % (plat(leg.get_text(" "))[:40] if leg else "?"), [l.get_text(" ") for l in fs.find_all("label")]))
    return res


def options_seules(src):
    """[(libellé, option)] : choix dont UNE SEULE option porte un nom entre parenthèses."""
    out = []
    for lib, opts in choix(src):
        avec = [o for o in opts if NOM_PAR.search(plat(o))]
        if len(opts) >= 2 and len(avec) == 1:
            out.append((lib, plat(avec[0])[:90]))
    return out


# ── les zones de la page ─────────────────────────────────────────────────────
def zones(src):
    """[(libellé, texte)] et le texte des schémas intégrés (compté à part)."""
    qz = questions(src)
    soup = BeautifulSoup(src, "html.parser")
    for t in soup(["style", "script", "template", "noscript", "pre", "code"]):
        t.decompose()
    for c in soup.find_all(string=lambda x: isinstance(x, Comment)):
        c.extract()
    # une case de tableau, un item, un paragraphe : une frontière. « <td>2</td><td>A</td> » (une durée, puis une
    # tâche) ne doit pas se lire « 2 A », deux ampères.
    for t in soup.find_all(BLOCS):
        t.insert(0, NavigableString(" ¦ "))
        t.append(NavigableString(" ¦ "))
    images = []
    res = []
    for k, s in enumerate(soup.find_all("svg"), 1):
        t = schema_visible(s)
        images.append(t)
        res.append(("schéma %d" % k, t))
        s.decompose()
    for k, tab in enumerate(soup.find_all("table"), 1):
        titre = tab.find_previous(["h2", "h3", "h4"])
        res.append(("tableau %d%s" % (k, (" — " + plat(titre.get_text(" "))[:50]) if titre else ""), plat(tab.get_text(" "))))
        tab.decompose()
    corps = soup.body or soup
    cour_lib, cour = "début de page", []
    for el in corps.descendants:
        if isinstance(el, Tag):
            nouveau = False
            if el.name == "h2":
                nouveau = True
            elif el.name in ("h3", "h4", "header", "summary") and DEBUT_ACT.match(plat(el.get_text(" "))):
                nouveau = True
            elif el.name in ("div", "section", "article") and (
                    "activite" in " ".join(el.get("class") or []) or re.match(r"act\d", el.get("id") or "")):
                nouveau = True
            if nouveau:
                if cour:
                    res.append((cour_lib, plat(" ".join(cour))))
                cour_lib, cour = plat(el.get_text(" "))[:60] or el.name, []
        elif isinstance(el, NavigableString) and not isinstance(el, Comment):
            cour.append(str(el))
    if cour:
        res.append((cour_lib, plat(" ".join(cour))))
    return res + qz, images


def schema_visible(svg):
    """Le texte que l'œil lit dans un schéma (un Tag <svg>) : chaque <text> séparé de son voisin, sans <title>
    ni <desc>."""
    for t in svg.find_all(["title", "desc", "style", "script", "metadata"]):
        t.decompose()
    return plat(" ¦ ".join(t.get_text(" ") for t in svg.find_all("text")))


def manques(texte):
    """[(symbole, extrait)] : unités écrites après un nombre dont le nom n'apparaît pas dans le texte."""
    vus = {}
    for m in OCC.finditer(texte):
        s = m.group(1)
        if s not in vus:
            vus[s] = texte[max(0, m.start() - 30):m.end() + 15]
    return [(s, ex) for s, ex in vus.items() if not NOMS[s][0].search(texte)]


def lire_page(chemin):
    src = ouvrir(chemin)
    if chemin.endswith(".svg"):
        racine = BeautifulSoup(src, "html.parser").find("svg")
        texte = schema_visible(racine) if racine else ""
        ecarts = [dict(zone="schéma", unite=s, nom=NOMS[s][1], extrait=ex) for s, ex in manques(texte)]
        n = sum(1 for _ in OCC.finditer(texte))
        return dict(zones=1, occurrences=n, ecarts=ecarts, images=n)
    zs, images = zones(src)
    ecarts, occurrences = [], 0
    for lib, texte in zs:
        occurrences += sum(1 for _ in OCC.finditer(texte))
        for s, ex in manques(texte):
            ecarts.append(dict(zone=lib, unite=s, nom=NOMS[s][1], extrait=ex))
    for lib, opt in options_seules(src):
        ecarts.append(dict(zone=lib, unite="option seule", nom="", extrait=opt))
    img = sum(1 for t in images for _ in OCC.finditer(t))
    return dict(zones=len(zs), occurrences=occurrences, ecarts=ecarts, images=img)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    muet, en_json, voir_images = "--muet" in argv, "--json" in argv, "--images" in argv
    cibles = [a for a in argv if not a.startswith("--")] or [DEPOT]
    liste = pages(cibles)
    if not liste:
        print("⛔ PANNE — aucune page élève lue sous %s : un contrôle qui n'a rien lu n'est pas vert (règle d'or n°299)."
              % ", ".join(cibles), file=sys.stderr)
        return 2
    bilan, zones_lues, occ, img, n_ecarts = {}, 0, 0, 0, 0
    for p in liste:
        r = lire_page(p)
        zones_lues += r["zones"]; occ += r["occurrences"]; img += r["images"]
        if r["ecarts"] or (voir_images and r["images"]):
            bilan[os.path.relpath(p, DEPOT)] = r
        n_ecarts += len(r["ecarts"])
    if zones_lues == 0:
        print("⛔ PANNE — %d page(s) ouvertes, aucune zone lue (règle d'or n°299)." % len(liste), file=sys.stderr)
        return 2
    if en_json:
        print(json.dumps(dict(pages=len(liste), zones=zones_lues, occurrences=occ, images=img, ecarts=n_ecarts,
                              detail=bilan), ensure_ascii=False, indent=1))
    else:
        if not muet:
            for p, r in bilan.items():
                if not r["ecarts"]:
                    continue
                print("✘ %s" % p)
                for e in r["ecarts"]:
                    if e["unite"] == "option seule":
                        print("    [%s] seule option à porter le nom : l'écrire en toutes lettres — « %s »"
                              % (e["zone"][:45], e["extrait"]))
                    else:
                        print("    [%s] %s sans « %s » — …%s…" % (e["zone"][:45], e["unite"], e["nom"], e["extrait"]))
        pages_ko = sum(1 for r in bilan.values() if r["ecarts"])
        print("%d page(s) et schéma(s) lus · %d zones · %d grandeurs avec unité, dont %d dans des schémas"
              % (len(liste), zones_lues, occ, img))
        if n_ecarts:
            print("✘ %d écart(s) — unité sans son nom, ou option seule à le porter — dans %d page(s) (règle d'or n°312)"
                  % (n_ecarts, pages_ko))
        else:
            print("✅ chaque unité est nommée en toutes lettres dans son activité, son tableau, sa question ou son schéma (règle d'or n°312)")
    return 1 if n_ecarts else 0


if __name__ == "__main__":
    sys.exit(main())
