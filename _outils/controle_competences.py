# -*- coding: utf-8 -*-
"""controle_competences.py — une compétence numérique se lit en toutes lettres (règle d'or n°314).

LE CONSTAT
----------
Le 26/10/2026, Pascal ouvre au hasard le jardin de New York (4e_C8.1) : sous le titre, une étiquette « CRCN », et rien
d'autre ; plus bas, une carte « 🎯 CRCN mobilisés » vide (le mode essentiel en masquait le contenu). « On ne sait pas
quelles compétences. » Le relevé des 60 séquences, le même jour : 61 codes CRCN montrés sans leur intitulé, sur
25 pages — « CRCN : 1.2 · 1.3 · 3.4 · 5.2 », « D1.3 · D2 · D3 · D4 · D5 · CRCN 1.3 niv. 3 », « (CRCN 3.4) » dans un
titre d'activité. Le survol ne donnait la compétence en toutes lettres que sur quatre pages ; et le survol n'existe ni
au doigt (tablette, téléphone), ni sur le papier.

LA RÈGLE (n°314, décisions de Pascal du 26/10/2026)
-------------------------------------------------
Toute compétence du CRCN montrée à l'élève — étiquette, titre d'activité, consigne, cartouche — porte son code ET son
intitulé officiel, visibles sans survol : « CRCN 1.3 Traiter des données », jamais « CRCN 1.3 » seul. Une étiquette CRCN
redonne aussi, au survol (`title`), chaque compétence en toutes lettres. Les domaines du socle gardent leur code dans la
ligne d'étiquettes (règle n°298), mais leur infobulle donne chaque domaine en toutes lettres. Les codes de rangement des
séquences (4e_C8.1…) ne sont pas des compétences : la règle ne les vise pas.

CE QU'IL LIT
------------
Comme `controle_regles_visibles.py` : chaque .html et .svg suivi par Git, hors `_archive-anciennes-versions`, `_outils`,
`_generation`, `captures`, hors synthèses professeur, fiches et rapports de tests ; le texte que l'élève peut lire —
corps, chaînes de JavaScript qui s'affichent (banques de QCM), attributs `title`, `aria-label`, `alt` — sans les
commentaires ni les <style>.

CE QU'IL REFUSE
  · un code CRCN (« 1.3 » dans « CRCN 1.3 », « CRCN : 1.2 · 1.3 ») que ne suit pas son intitulé officiel ;
  · une étiquette (`.badge`, ou élément de `.badges`) qui dit « CRCN » sans nommer de compétence ;
  · une étiquette CRCN dont l'infobulle ne redonne pas chaque compétence en toutes lettres (ou qui n'en a pas) ;
  · une étiquette de domaines du socle (D1 à D5) dont l'infobulle ne donne pas chaque domaine en toutes lettres.
Ce qu'il laisse : « le CRCN », « compétences du CRCN » (le cadre, pas une compétence) ; les niveaux (« niv. 2 »,
« N3 ») ; les domaines du socle écrits dans le texte, hors étiquettes (la n°298 les a déjà retirés de la page élève).

NON LU : une compétence nommée sans son code (« traiter des données ») — elle se lit déjà en toutes lettres ; un
intitulé juste mais mal placé ; le texte porté par les pixels d'une capture ; ce qu'un script n'écrit qu'après un clic,
s'il ne figure pas en clair dans la page.

Usage :
    python3 _outils/controle_competences.py           # rapport complet
    python3 _outils/controle_competences.py --muet    # seulement les refus
Sortie : 0 si chaque compétence se lit en toutes lettres, 1 sinon, 2 si rien n'a pu être lu (règle d'or n°299).
"""
import html
import os
import re
import sys
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import panne  # noqa: E402
from controle_regles_visibles import DEPOT, PROFESSEUR, MODELES, fichiers, masque  # noqa: E402

#: Les 16 compétences du CRCN, intitulés officiels (décret n° 2019-919 ; note de service du 23/01/2026, BO n°6 du
#: 05/02/2026 ; relevés dans le skill CRCN, revérifié en ligne le 24/10/2026).
CRCN = {
    "1.1": "Mener une recherche et une veille d'information",
    "1.2": "Gérer des données",
    "1.3": "Traiter des données",
    "2.1": "Interagir",
    "2.2": "Partager et publier",
    "2.3": "Collaborer",
    "2.4": "S'insérer dans le monde numérique",
    "3.1": "Développer des documents textuels",
    "3.2": "Développer des documents multimédia",
    "3.3": "Adapter les documents à leur finalité",
    "3.4": "Programmer",
    "4.1": "Sécuriser l'environnement numérique",
    "4.2": "Protéger les données personnelles et la vie privée",
    "4.3": "Protéger la santé, le bien-être et l'environnement",
    "5.1": "Résoudre des problèmes techniques",
    "5.2": "Évoluer dans un environnement numérique",
}
#: Les domaines du socle commun (décret n° 2015-372 du 31 mars 2015 modifié ; texte d'éduscol relevé le 26/10/2026).
SOCLE = {
    "D1": "Les langages pour penser et communiquer",
    "D1.1": "Comprendre, s'exprimer en utilisant la langue française à l'oral et à l'écrit",
    "D1.2": "Comprendre, s'exprimer en utilisant une langue étrangère et, le cas échéant, une langue régionale",
    "D1.3": "Comprendre, s'exprimer en utilisant les langages mathématiques, scientifiques et informatiques",
    "D1.4": "Comprendre, s'exprimer en utilisant les langages des arts et du corps",
    "D2": "Les méthodes et outils pour apprendre",
    "D3": "La formation de la personne et du citoyen",
    "D4": "Les systèmes naturels et les systèmes techniques",
    "D5": "Les représentations du monde et l'activité humaine",
}
#: Ce qu'un domaine doit laisser lire dans l'infobulle (le cœur de l'intitulé : l'article initial et l'ordre « oral /
#: écrit » varient d'un texte officiel à l'autre).
SOCLE_CLE = {
    "D1": "langages pour penser et communiquer", "D1.1": "langue française", "D1.2": "langue étrangère",
    "D1.3": "langages mathématiques, scientifiques et informatiques", "D1.4": "langages des arts et du corps",
    "D2": "méthodes et outils pour apprendre", "D3": "formation de la personne et du citoyen",
    "D4": "systèmes naturels et les systèmes techniques", "D5": "représentations du monde et l'activité humaine",
}


def norme(t):
    return re.sub(r"\s+", " ", t.replace("’", "'").replace(" ", " ").replace(" ", " ")).strip().lower()


CODE = re.compile(r"(?<![\d.])([1-5]\.[1-4])(?![\d.]*\d)")
SEP = re.compile(r"(?:\s|[·•,;/+&]|\bet\b|\bou\b)+", re.I)
NIVEAU = re.compile(r"\(?\s*(?:niv(?:eau)?\.?\s*|N\s?)\d(?:\s*(?:[-–→/]|à)\s*\d)?\s*\)?(?:\s*\((?:visé|extension)[^)]*\))?", re.I)
PAREN = re.compile(r"\((?:programme|visé|extension|compl[ée]mentaire)[^)]*\)", re.I)


def chaine(texte, i):
    """Les codes de la liste qui suit « CRCN » à la position i : [(code, position, intitulé présent ?)]."""
    out, j = [], i
    while True:
        m = SEP.match(texte, j)
        if m:
            j = m.end()
        if texte.startswith(":", j):
            j += 1
            continue
        c = CODE.match(texte, j)
        if not c:
            return out
        code, j = c.group(1), c.end()
        reste = texte[j:j + 160]
        m = re.match(r"\s*(?:[—–:-]\s*)?", reste)
        present = norme(reste[m.end():]).startswith(norme(CRCN.get(code, "§§§")))
        if present:
            j += m.end() + len(CRCN[code])
        out.append((code, c.start(), present))
        for motif in (NIVEAU, PAREN, NIVEAU):
            m = re.compile(r"\s*(?:[—–:-]\s*)?").match(texte, j)
            k = m.end() if m else j
            n = motif.match(texte, k)
            if n and n.group(0).strip():
                j = n.end()


class Etiquettes(HTMLParser):
    """Les étiquettes de la page : (texte, title, ligne) des éléments `.badge` et des enfants de `.badges`."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pile, self.trouvees, self.attributs = [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        parent_badges = bool(self.pile) and "badges" in self.pile[-1]["classes"]
        etiquette = "badge" in classes or (parent_badges and tag in ("span", "a", "li"))
        for nom in ("title", "aria-label", "alt"):
            if a.get(nom):
                self.attributs.append((a[nom], self.getpos()[0]))
        if tag in ("br", "img", "input", "meta", "link", "hr", "source", "wbr"):
            return
        self.pile.append({"tag": tag, "classes": classes, "etiquette": etiquette, "title": a.get("title") or "",
                          "texte": [], "ligne": self.getpos()[0]})

    def handle_endtag(self, tag):
        while self.pile:
            e = self.pile.pop()
            if e["etiquette"]:
                self.trouvees.append(("".join(e["texte"]), e["title"], e["ligne"]))
            if self.pile:
                self.pile[-1]["texte"].extend(e["texte"])
            if e["tag"] == tag:
                break

    def handle_data(self, data):
        if self.pile and self.pile[-1]["tag"] not in ("script", "style"):
            self.pile[-1]["texte"].append(data)


def griefs(texte):
    """[(ligne, grief, extrait)] — vide si chaque compétence se lit en toutes lettres."""
    visible = masque(texte)
    trouves = []
    # 1. le texte lu (balises effacées, ligne par ligne) et les attributs lus
    sans_balises = re.sub(r"<[^>]*>", lambda m: re.sub(r"[^\n]", " ", m.group(0)), visible)
    lignes = [(n + 1, html.unescape(l)) for n, l in enumerate(sans_balises.split("\n"))]
    p = Etiquettes()
    try:
        p.feed(re.sub(r"<script\b.*?</script>", lambda m: "\n" * m.group(0).count("\n"), visible, flags=re.S | re.I))
    except Exception:  # une page mal formée : on garde ce qui a été lu
        pass
    lignes += [(n, html.unescape(t)) for t, n in p.attributs]
    for n, l in lignes:
        for m in re.finditer(r"\bCRCN\b", l):
            for code, pos, present in chaine(l, m.end()):
                if not present:
                    extrait = re.sub(r"\s+", " ", l[max(0, m.start() - 30):pos + 50]).strip()
                    trouves.append((n, "« CRCN %s » sans son intitulé (« %s »)" % (code, CRCN.get(code, "?")), extrait))
    # 2. les étiquettes et leur infobulle
    for t, title, n in p.trouvees:
        t = re.sub(r"\s+", " ", html.unescape(t)).strip()
        if re.search(r"\bCRCN\b", t):
            codes = [c for c, _, _ in chaine(t, re.search(r"\bCRCN\b", t).end())]
            if not codes:
                trouves.append((n, "une étiquette « CRCN » qui ne nomme aucune compétence", t[:80]))
            manque = [c for c in codes if norme(CRCN.get(c, "§§§")) not in norme(title)]
            if codes and manque:
                trouves.append((n, "étiquette CRCN dont le survol ne redonne pas %s en toutes lettres"
                                % ", ".join("%s (%s)" % (c, CRCN.get(c, "?")) for c in manque), t[:80]))
        doms = re.findall(r"(?<![\w.])(D[1-5](?:\.[1-4])?)(?![\w.]*\d)", t)
        if doms and re.fullmatch(r"(?:Socle\s*:?\s*)?(?:D[1-5](?:\.[1-4])?\s*[·•,/]?\s*)+.*", t):
            manque = [d for d in doms if norme(SOCLE_CLE.get(d, "§§§")) not in norme(title)]
            if manque:
                trouves.append((n, "étiquette du socle dont le survol ne donne pas %s en toutes lettres"
                                % ", ".join(manque), t[:80]))
    return sorted(set(trouves))


def main(muet=False, racine=None):
    racine = racine or DEPOT
    lus, refuses, total = 0, [], 0
    for chemin in fichiers(racine):
        nom = os.path.basename(chemin)
        if PROFESSEUR.match(nom) or nom in MODELES:
            continue
        try:
            texte = open(chemin, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        lus += 1
        g = griefs(texte)
        if g:
            refuses.append((os.path.relpath(chemin, racine).replace(os.sep, "/"), g))
            total += len(g)
    if not lus:
        return panne.rien_vu("aucun .html ni .svg lisible sous %s" % racine)
    if not muet:
        print("%d page(s) et SVG lus · %d compétence(s) qui ne se lisent pas en toutes lettres · %d fichier(s) en refus"
              % (lus, total, len(refuses)))
        print("     NON LU : une compétence nommée sans code, la justesse d'un intitulé mal placé, le texte d'une capture,\n"
              "     ce qu'un script n'écrit qu'après un clic. Les codes de rangement (4e_C8.1…) ne sont pas des compétences.")
    if refuses:
        print("\n⛔ %d fichier(s) montrent une compétence sans la nommer (règle d'or n°314 : une compétence numérique se lit"
              " en toutes lettres) :" % len(refuses))
        for rel, g in refuses:
            print("  %s" % rel)
            for ligne, nom, extrait in g:
                print("     ligne %d · %s : … %s …" % (ligne, nom, extrait))
        print("\n     Écris « CRCN 1.3 Traiter des données », et donne au survol de l'étiquette chaque compétence en toutes lettres.")
        return 1
    print("\n✅ chaque compétence du CRCN se lit en toutes lettres, et chaque étiquette le redit au survol (règle d'or n°314)")
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--muet"]
    sys.exit(main("--muet" in sys.argv, args[0] if args else None))
