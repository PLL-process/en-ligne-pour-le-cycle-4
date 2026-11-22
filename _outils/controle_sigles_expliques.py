# -*- coding: utf-8 -*-
"""controle_sigles_expliques.py — règle d'or n°44, complétée le 22/11/2026 : aucun sigle ne reste nu, dans le texte aussi.

LE CONSTAT
----------
Pascal, 22/11/2026 : « Tous les sigles doivent être expliqués pour éviter les charges cognitives. » La n°44 (août 2026)
le disait pour l'interface (badges, codes, boutons) : une explication à portée immédiate, avec une mention en clair sur
la page, parce qu'une infobulle ne s'ouvre pas au doigt. Aucun outil ne le mesurait dans le texte lu par l'élève : un
« TTL » ou un « CDI » pouvait rester nu. La n°313, elle, ne regarde que les capitales (FAST, jamais fast).

LA RÈGLE MESURÉE
----------------
Sur chaque page, chaque sigle connu (liste SIGLES ci-dessous, avec son explication) est expliqué en clair au moins
une fois : « TTL (Time To Live, la durée de vie du paquet) », « le centre de documentation (CDI) », ou
`<abbr title="…">TTL</abbr>` accompagné de sa mention en clair. Mesuré :
  E  sigle jamais expliqué sur la page (défaut) ;
  P  sigle expliqué, mais plus bas que sa première apparition (signal : l'élève l'a déjà lu nu une fois).
Une page sans aucun sigle connu est lue, et comptée « rien à expliquer ».

PÉRIMÈTRE (n°47)
----------------
Pages : toutes les pages HTML sous theme-*, hors dossiers « _… ». Texte : le texte de la page hors <script>, <style>,
<pre>, <code> et <svg> (un listing ou un nom de variable n'est pas un sigle de la phrase). Les attributs title,
aria-label et alt comptent comme explication seulement avec une mention en clair dans le texte (n°44 : au doigt, une
infobulle ne s'affiche pas). Ne mesure pas : les schémas SVG séparés, les sigles absents de la liste (une liste qui ne
peut que grandir — un sigle nouveau s'y ajoute avec son explication).

    python3 _outils/controle_sigles_expliques.py                  (tout le site, résumé par thème et par sigle)
    python3 _outils/controle_sigles_expliques.py <page.html> …   (le détail des pages données)

Sortie : 0 aucun sigle nu · 1 au moins un sigle jamais expliqué · 2 rien n'a été lu (n°299).
"""
import html
import pathlib
import re
import sys
import unicodedata
from html.parser import HTMLParser

RACINE = pathlib.Path(__file__).resolve().parent.parent
THEMES = ("theme-1-objets-systemes-usages-interactions", "theme-2-structure-fonctionnement-comportement",
          "theme-3-creation-conception-realisation-innovations")

# sigle : (explication à écrire en clair, mots dont la présence près du sigle vaut explication)
SIGLES = {
    "TTL": ("Time To Live, la durée de vie du paquet", ["time to live", "duree de vie"]),
    "CDI": ("centre de documentation et d'information", ["centre de documentation"]),
    "DNB": ("diplôme national du brevet", ["diplome national du brevet"]),
    "QCM": ("questionnaire à choix multiples", ["questionnaire a choix", "questions a choix"]),
    "CRCN": ("cadre de référence des compétences numériques", ["cadre de reference des competences numeriques"]),
    "FAST": ("Function Analysis System Technique, le diagramme des fonctions techniques",
             ["function analysis system technique", "fonctions techniques"]),
    "SysML": ("Systems Modeling Language, langage de modélisation des systèmes", ["systems modeling language", "langage de modelisation"]),
    "SADT": ("Structured Analysis and Design Technique", ["structured analysis"]),
    "UML": ("Unified Modeling Language", ["unified modeling language"]),
    "NFC": ("Near Field Communication, communication en champ proche", ["near field communication", "champ proche"]),
    "RFID": ("identification par radiofréquence", ["radio frequency identification", "radiofrequence", "radio-frequence"]),
    "CAO": ("conception assistée par ordinateur", ["conception assistee par ordinateur"]),
    "DAO": ("dessin assisté par ordinateur", ["dessin assiste par ordinateur"]),
    "TBT": ("très basse tension", ["tres basse tension"]),
    "LCD": ("écran à cristaux liquides", ["cristaux liquides", "liquid crystal"]),
    "GPS": ("Global Positioning System, positionnement par satellites", ["global positioning system", "positionnement par satellite", "geolocalisation par satellite"]),
    "USB": ("Universal Serial Bus, la prise et le câble universels", ["universal serial bus"]),
    "LED": ("Light-Emitting Diode, diode électroluminescente", ["diode electroluminescente", "light-emitting diode", "light emitting diode"]),
    "DEL": ("diode électroluminescente", ["diode electroluminescente"]),
    "IP": ("Internet Protocol, l'adresse d'une machine sur le réseau", ["internet protocol"]),
    "DNS": ("Domain Name System, l'annuaire qui traduit un nom en adresse", ["domain name system", "annuaire"]),
    "LAN": ("réseau local", ["reseau local", "local area network"]),
    "WAN": ("réseau étendu", ["reseau etendu", "wide area network"]),
    "URL": ("adresse d'une page web", ["uniform resource locator", "adresse d'une page", "adresse de la page", "adresse web"]),
    "HTTP": ("HyperText Transfer Protocol, le protocole du web", ["hypertext transfer protocol", "protocole du web"]),
    "MAC": ("Media Access Control, l'adresse physique d'une carte réseau", ["media access control", "adresse physique"]),
    "ARP": ("Address Resolution Protocol", ["address resolution protocol"]),
    "DHCP": ("Dynamic Host Configuration Protocol", ["dynamic host configuration protocol"]),
    "RGPD": ("règlement général sur la protection des données", ["reglement general sur la protection des donnees"]),
    "CNIL": ("Commission nationale de l'informatique et des libertés", ["commission nationale de l'informatique"]),
    "ENT": ("espace numérique de travail", ["espace numerique de travail"]),
    "EPI": ("enseignement pratique interdisciplinaire", ["enseignement pratique interdisciplinaire"]),
    "LSU": ("livret scolaire unique", ["livret scolaire unique"]),
    # « un OST » est écrit tel quel dans les formulations du programme (n°105 : on ne les reformule pas) : l'explication
    # se pose à côté de la formulation, jamais dedans
    "OST": ("objet ou système technique", ["objet ou systeme technique", "objets ou systemes techniques",
                                           "objets et systemes techniques", "objet et systeme technique"]),
    "CPU": ("processeur", ["central processing unit", "processeur"]),
    "RAM": ("mémoire vive", ["memoire vive", "random access memory"]),
    "PLA": ("acide polylactique, le plastique des imprimantes 3D", ["acide polylactique", "polylactique"]),
    "PVC": ("polychlorure de vinyle", ["polychlorure de vinyle"]),
    "IDE": ("environnement de développement", ["environnement de developpement", "integrated development environment"]),
    "PIR": ("détecteur infrarouge passif", ["infrarouge passif", "passive infrared"]),
    "LDR": ("photorésistance", ["photoresistance", "light dependent resistor"]),
    "IA": ("intelligence artificielle", ["intelligence artificielle"]),
}
MAJ = {k.upper(): k for k in SIGLES}


def plat(t):
    t = unicodedata.normalize("NFD", t.lower())
    return "".join(c for c in t if unicodedata.category(c) != "Mn").replace("’", "'")


class Texte(HTMLParser):
    IGNORE = {"script", "style", "pre", "code", "svg", "textarea"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.prof, self.morceaux, self.abbr = 0, [], set()

    def handle_starttag(self, tag, attrs):
        if tag in self.IGNORE:
            self.prof += 1
        if tag == "abbr":
            self._abbr = dict(attrs).get("title")
        if tag in ("p", "li", "div", "br", "h1", "h2", "h3", "h4", "td", "th", "label", "legend", "summary", "section"):
            self.morceaux.append("\n")

    def handle_endtag(self, tag):
        if tag in self.IGNORE and self.prof:
            self.prof -= 1

    def handle_data(self, d):
        if not self.prof:
            self.morceaux.append(d)
            if getattr(self, "_abbr", None) and d.strip():
                self.abbr.add(d.strip())
                self._abbr = None


def lire(page):
    p = Texte()
    p.feed(page.read_text(encoding="utf-8", errors="ignore"))
    return re.sub(r"[ \t  ]+", " ", "".join(p.morceaux)), p.abbr


def mesurer(page):
    """{sigle: 'ok' | 'P' | 'E'} pour les sigles connus présents dans la page."""
    texte, _ = lire(page)
    t_plat = plat(texte)
    res = {}
    for m in re.finditer(r"(?<![\w./_-])([A-Z][A-Za-z]{1,5})(?![\w/_-])", texte):
        mot = m.group(1)
        cle = MAJ.get(mot.upper())
        if not cle or (mot != cle and mot != cle.upper()) or cle in res:
            continue
        # première apparition : explication collée (parenthèse juste après ou juste avant), ou mots d'explication proches
        occ = [x.start() for x in re.finditer(r"(?<![\w./_-])" + re.escape(mot) + r"(?![\w/_-])", texte)]
        def explique_a(i):
            apres, avant = texte[i + len(mot):i + len(mot) + 4], texte[max(0, i - 3):i]
            fen = plat(texte[max(0, i - 160):i + len(mot) + 160])
            return apres.lstrip().startswith("(") or avant.rstrip().endswith("(") or any(e in fen for e in SIGLES[cle][1])
        if explique_a(occ[0]):
            res[cle] = "ok"
        elif any(explique_a(i) for i in occ[1:]) or any(e in t_plat for e in SIGLES[cle][1]):
            res[cle] = "P"
        else:
            res[cle] = "E"
    return res


def pages_tout():
    for th in THEMES:
        for p in sorted((RACINE / th).rglob("*.html")):
            if not any(part.startswith("_") for part in p.relative_to(RACINE).parts):
                yield p


def main(argv):
    detail = bool(argv)
    pages = [pathlib.Path(a) for a in argv] if argv else list(pages_tout())
    lues, nus, tard = 0, {}, {}
    par_theme = {}
    for page in pages:
        try:
            r = mesurer(page)
        except OSError:
            continue
        lues += 1
        rel = page.resolve().relative_to(RACINE) if RACINE in page.resolve().parents else page
        th = str(rel).split("/")[0][:7]
        e = sorted(k for k, v in r.items() if v == "E")
        pp = sorted(k for k, v in r.items() if v == "P")
        for k in e:
            nus.setdefault(k, []).append(str(rel))
        for k in pp:
            tard.setdefault(k, []).append(str(rel))
        if e:
            par_theme[th] = par_theme.get(th, 0) + 1
        if detail:
            if e or pp:
                print(f"{'✘' if e else '○'} {rel}")
                for k in e:
                    print(f"   E {k} jamais expliqué — à écrire : {k} ({SIGLES[k][0]})")
                for k in pp:
                    print(f"   P {k} expliqué plus bas que sa première apparition")
            else:
                print(f"✔ {rel} — {len(r)} sigle(s) connu(s), tous expliqués" if r else f"✔ {rel} — aucun sigle connu")
    if not lues:
        print("Rien n'a été lu : ce contrôle n'a rien vérifié (n°299).")
        return 2
    n_e = len({p for v in nus.values() for p in v})
    if not detail:
        print(f"{lues} page(s) lues · {n_e} page(s) avec au moins un sigle jamais expliqué · "
              f"{len({p for v in tard.values() for p in v})} page(s) avec un sigle expliqué trop bas")
        for th, n in sorted(par_theme.items()):
            print(f"   {th} : {n} page(s)")
        for k, v in sorted(nus.items(), key=lambda x: -len(x[1])):
            print(f"   E {k:5} : {len(v):3} page(s) — à écrire : {k} ({SIGLES[k][0]})")
    if n_e == 0:
        print("✅ aucun sigle connu ne reste nu (règle d'or n°44)")
    return 1 if n_e else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
