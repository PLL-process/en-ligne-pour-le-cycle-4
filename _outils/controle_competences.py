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
porte une bulle (`title`) à trois étages pour chacune de ses compétences — « Traiter des données, c'est vaste » (Pascal) :
  1. le code, l'intitulé et le niveau : « CRCN 1.3 Traiter des données — niveau 2. » ;
  2. ce que la compétence recouvre, mot pour mot dans le cadre de référence : « Le cadre : « Appliquer des traitements à
     des données pour les analyser et les interpréter. » » (le CRCN n'a pas de sous-compétences officielles : c'est
     cette description qui précise l'intitulé) ;
  3. ce que l'élève en fait dans cette séquence : « Ici : tu ranges les résultats de tes tests dans un tableau… ».
Le troisième étage s'écrit à la main, page par page : aucun outil ne sait ce que fait l'élève. Les domaines du socle gardent leur code dans la
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
  · une étiquette CRCN dont la bulle, pour l'une de ses compétences, ne donne pas l'intitulé, la description du cadre
    ou « Ici : » (ou qui n'a pas de bulle) ;
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
#: Ce que chaque compétence recouvre, mot pour mot : la première proposition de sa description dans le cadre de
#: référence (décret n° 2019-919, BO n°37 du 10/10/2019, annexe, relevé le 26/10/2026), sans la parenthèse d'exemples
#: d'outils qui la suit. C'est le deuxième étage de la bulle (« Le cadre : « … » »).
CADRE = {
    "1.1": "Mener une recherche et une veille d'information pour répondre à un besoin d'information et se tenir au courant "
           "de l'actualité d'un sujet tout en étant en mesure de vérifier les sources et la fiabilité de l'information",
    "1.2": "Stocker et organiser des données pour les retrouver, les conserver et en faciliter l'accès et la gestion",
    "1.3": "Appliquer des traitements à des données pour les analyser et les interpréter",
    "2.1": "Interagir avec des individus et des petits groupes pour échanger dans divers contextes liés à la vie privée ou "
           "à une activité professionnelle, de façon ponctuelle et récurrente",
    "2.2": "Partager et publier des informations et des contenus pour communiquer ses propres productions ou opinions, "
           "relayer celles des autres en contexte de communication publique en apportant un regard critique sur la nature "
           "du contenu",
    "2.3": "Collaborer dans un groupe pour réaliser un projet, co-produire des ressources, des connaissances, des données, "
           "et pour apprendre",
    "2.4": "Maîtriser les enjeux de la présence en ligne, développer des stratégies et des pratiques autonomes en respectant "
           "les règles, les droits et les valeurs qui leur sont liés, pour se positionner en tant qu'acteur social, "
           "économique et citoyen dans le monde numérique",
    "3.1": "Produire des documents à contenu majoritairement textuel pour communiquer des idées, rendre compte et valoriser "
           "ses travaux",
    "3.2": "Développer des documents à contenu multimédia pour créer ses propres productions multimédia, enrichir ses "
           "créations textuelles",
    "3.3": "Adapter des documents de tous types en fonction de l'usage envisagé et maîtriser l'usage des licences pour "
           "permettre, faciliter et encadrer l'utilisation dans divers contextes",
    "3.4": "Écrire des programmes et des algorithmes pour répondre à un besoin",
    "4.1": "Sécuriser les équipements, les communications et les données pour se prémunir contre les attaques, pièges, "
           "désagréments et incidents susceptibles de nuire au bon fonctionnement des matériels, logiciels, sites internet, "
           "et de compromettre les transactions et les données",
    "4.2": "Maîtriser ses traces et gérer les données personnelles pour protéger sa vie privée et celle des autres, et "
           "adopter une pratique éclairée",
    "4.3": "Prévenir et limiter les risques générés par le numérique sur la santé, le bien-être et l'environnement mais "
           "aussi tirer parti de ses potentialités pour favoriser le développement personnel, le soin, l'inclusion dans la "
           "société et la qualité des conditions de vie, pour soi et pour les autres",
    "5.1": "Résoudre des problèmes techniques pour garantir et rétablir le bon fonctionnement d'un environnement informatique",
    "5.2": "Installer, configurer et enrichir un environnement numérique (matériels, outils, services) pour disposer d'un "
           "cadre adapté aux activités menées, à leur contexte d'exercice ou à des valeurs",
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


ICI = re.compile(r"\bIci\s*:\s*\S.{19,}", re.S)


def segments(title):
    """{code: partie de l'infobulle} — de « CRCN x.y » jusqu'à la compétence suivante. Une bulle à trois étages parle
    de chaque compétence dans son propre paragraphe : « CRCN 1.3 Traiter des données — niveau 2. / Le cadre : « … » /
    Ici : … »."""
    out = {}
    ms = list(re.finditer(r"\bCRCN\s+([1-5]\.[1-4])\b", title))
    for k, m in enumerate(ms):
        out.setdefault(m.group(1), title[m.start():ms[k + 1].start() if k + 1 < len(ms) else len(title)])
    return out


def etages_manquants(code, segment):
    """Ce qui manque à la bulle d'une compétence : l'intitulé, le cadre officiel, « Ici : » (ce que l'élève fait)."""
    manque = []
    if norme(CRCN.get(code, "§§§")) not in norme(segment):
        manque.append("l'intitulé")
    if norme(CADRE.get(code, "§§§")) not in norme(segment):
        manque.append("ce que dit le cadre")
    if not ICI.search(segment):
        manque.append("« Ici : » ce que l'élève fait")
    return manque


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
            segs = segments(title)
            for c in codes:
                manque = etages_manquants(c, segs.get(c, ""))
                if manque:
                    trouves.append((n, "étiquette CRCN : la bulle de %s (%s) ne donne pas %s"
                                    % (c, CRCN.get(c, "?"), ", ".join(manque)), t[:80]))
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
        print("\n     Écris « CRCN 1.3 Traiter des données ». Pour la bulle : `nommer_competences.py` écrit l'intitulé, le niveau"
              " et le cadre ;\n     « Ici : » (ce que l'élève fait dans la séquence) s'écrit à la main.")
        return 1
    print("\n✅ chaque compétence du CRCN se lit en toutes lettres, et chaque étiquette la détaille au survol — intitulé,"
          " cadre, « Ici : » (règle d'or n°314)")
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--muet"]
    sys.exit(main("--muet" in sys.argv, args[0] if args else None))
