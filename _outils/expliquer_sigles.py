# -*- coding: utf-8 -*-
"""expliquer_sigles.py — pose l'explication d'un sigle à sa première apparition dans le texte d'une page (n°44,
complément du 22/11/2026 : « Tous les sigles doivent être expliqués pour éviter les charges cognitives »).

    python3 _outils/expliquer_sigles.py --sigle QCM [pages…]            (essai : dit ce qu'il ferait, n'écrit rien)
    python3 _outils/expliquer_sigles.py --sigle QCM --ecrire [pages…]   (écrit)
    Sans page : toutes les pages où `controle_sigles_expliques.py` voit ce sigle jamais expliqué (E).

Où l'explication se pose : après la première apparition du sigle dans un texte de la page — « le QCM
(questionnaire à choix multiples) de l'atelier ». Jamais dans : <title>, <h1>, la barre de navigation (`nav`,
`#navharm`), un lien, un bouton, une étiquette de badge ou d'étape, une option de liste, un script, un style, un listing
(<pre>, <code>), un schéma (<svg>), une zone de saisie. Au pluriel (« des QCM », « les QCM »), l'explication se met au
pluriel. Une page où le sigle n'apparaît que dans ces endroits est signalée « à poser à la main ».

Avec `--infobulle` (décision de Pascal du 22/11/2026, pour tous les sigles autres que QCM) : le sigle est entouré
d'une infobulle `<abbr class="sigle" title="…" tabindex="0">` à sa première apparition dans la page, puis à la
première de chaque séance, en préférant le texte courant à un lien ou un bouton (où elle se pose alors sans
tabindex, pour ne pas imbriquer deux éléments focalisables) ; rien de visible ne change, sauf un pointillé ; jamais
dans la navigation, un listing, un script, une option de liste. Le style commun (`#sigles-css`, posé
une fois par page) l'affiche au survol, à l'appui au doigt et à l'impression.

Un outil qui réécrit prouve d'abord qu'il sait ne rien changer (n°149) : lancé deux fois, il ne pose rien la seconde
fois (la page est alors « ok » pour `controle_sigles_expliques.py`).
Sortie : 0 · 1 au moins une page à poser à la main · 2 rien n'a été lu (n°299).
"""
import argparse
import html
import pathlib
import re
import sys
from html.parser import HTMLParser

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import controle_sigles_expliques as cse  # noqa: E402

PLURIEL = {"QCM": "questionnaires à choix multiples"}
EXCLUS = {"title", "h1", "nav", "a", "button", "option", "select", "script", "style", "pre", "code", "svg",
          "textarea", "summary"}
VIDES = {"br", "img", "input", "meta", "link", "hr", "source", "wbr", "col", "area", "base", "embed", "param", "track"}


class Premiere(HTMLParser):
    def __init__(self, src, sigle):
        super().__init__(convert_charrefs=False)
        self.src, self.sigle = src, sigle
        self.pile = []          # (tag, exclu)
        self.lignes = [0]
        for m in re.finditer("\n", src):
            self.lignes.append(m.end())
        self.trouve = None
        self.ailleurs = False

    def exclu(self):
        return any(e for _, e in self.pile)

    def handle_starttag(self, tag, attrs):
        if tag in VIDES:
            return
        a = dict(attrs)
        marque = (a.get("id") or "") + " " + (a.get("class") or "")
        ex = tag in EXCLUS or any(k in marque for k in ("navharm", "badge", "nav-", "etape", "chip", "pastille"))
        self.pile.append((tag, ex))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        for i in range(len(self.pile) - 1, -1, -1):
            if self.pile[i][0] == tag:
                del self.pile[i:]
                return

    def handle_data(self, d):
        if self.trouve is not None:
            return
        for m in re.finditer(r"(?<![\w./_-])" + re.escape(self.sigle) + r"(?![\w/_-])", d):
            if self.exclu():
                self.ailleurs = True
                return
            ligne, col = self.getpos()
            debut = self.lignes[ligne - 1] + col
            self.trouve = (debut + m.start(), debut + m.end(), d[max(0, m.start() - 12):m.start()])
            return


def poser(src, sigle):
    """Renvoie (nouveau source, contexte) ou (None, raison)."""
    p = Premiere(src, sigle)
    p.feed(src)
    if p.trouve is None:
        return None, "à poser à la main (le sigle n'apparaît que dans un titre, un lien, un bouton ou la navigation)" \
            if p.ailleurs else "sigle absent du texte"
    i, j, avant = p.trouve
    assert src[i:j] == sigle, (src[i - 10:j + 10], sigle)
    plur = re.search(r"(?:\b(?:des|les|aux|ces|mes|tes|nos|vos|deux|trois|quatre|plusieurs)\s*(?:&nbsp;)?)$", avant, re.I)
    expl = PLURIEL.get(sigle) if plur and sigle in PLURIEL else cse.SIGLES[sigle][0]
    ajout = f" ({expl})"
    if src[j:j + len(ajout)] == ajout:
        return None, "déjà posé"
    return src[:j] + ajout + src[j:], src[max(0, i - 50):j + 30].replace("\n", " ")


CSS_SIGLES = ('<style id="sigles-css">/* n°44, décision du 22/11/2026 : un sigle s\'explique au survol, à l\'appui et '
              'sur papier */abbr.sigle{text-decoration:underline dotted;text-underline-offset:2px;cursor:help}'
              'abbr.sigle:focus{outline:2px solid currentColor;outline-offset:1px}'
              'abbr.sigle:focus::after{content:" (" attr(title) ")"}'
              '@media print{abbr.sigle::after{content:" (" attr(title) ")"}}</style>')
EXCLUS_BULLE = {"title", "script", "style", "pre", "code", "svg", "textarea", "option", "select", "nav", "abbr"}


INTERACTIFS = {"a", "button", "summary", "label"}


class Bulles(HTMLParser):
    """Relève chaque apparition du sigle : sa position, sa séance (onglet), et si elle est dans un élément qu'on
    clique (lien, bouton, étiquette de choix, titre de volet)."""
    def __init__(self, src, sigle):
        super().__init__(convert_charrefs=False)
        self.sigle, self.pile, self.occ = sigle, [], []
        self.lignes = [0] + [m.end() for m in re.finditer("\n", src)]

    def handle_starttag(self, tag, attrs):
        if tag in VIDES:
            return
        a = dict(attrs)
        marque = (a.get("id") or "") + " " + (a.get("class") or "")
        ex = tag in EXCLUS_BULLE or "navharm" in marque
        seance = a.get("id") if "seance-panel" in (a.get("class") or "") else None
        inter = tag in INTERACTIFS or a.get("role") in ("tab", "button", "link")
        self.pile.append((tag, ex, seance, inter))

    def handle_endtag(self, tag):
        for i in range(len(self.pile) - 1, -1, -1):
            if self.pile[i][0] == tag:
                del self.pile[i:]
                return

    def handle_data(self, d):
        if any(e for _, e, _, _ in self.pile):
            return
        seance = next((s for _, _, s, _ in reversed(self.pile) if s), None)
        inter = any(i for _, _, _, i in self.pile)
        for m in re.finditer(r"(?<![\w./_-])" + re.escape(self.sigle) + r"(?![\w/_-])", d):
            ligne, col = self.getpos()
            self.occ.append((self.lignes[ligne - 1] + col + m.start(), seance, inter))

    def choisir(self):
        """La première apparition de la page, puis la première de chaque séance qui n'en a pas encore ; dans chaque
        groupe, une apparition dans le texte passe avant une apparition dans un élément qu'on clique."""
        groupes = [self.occ] + [[o for o in self.occ if o[1] == s]
                                for s in dict.fromkeys(o[1] for o in self.occ if o[1])]
        choisis = []
        for g in groupes:
            if not g or any(o in choisis for o in g):
                continue
            choisis.append(next((o for o in g if not o[2]), g[0]))
        return choisis


def poser_infobulle(src, sigle):
    if re.search(r'<abbr class="sigle"[^>]*>' + re.escape(sigle) + "</abbr>", src):
        return None, "déjà posé"
    p = Bulles(src, sigle)
    p.feed(src)
    choisis = p.choisir()
    if not choisis:
        return None, "sigle absent du texte (ou seulement dans la navigation, un listing, un titre d'onglet)"
    titre = html.escape(cse.SIGLES[sigle][0], quote=True)
    neuf = src
    for i, _, inter in sorted(choisis, reverse=True):
        assert neuf[i:i + len(sigle)] == sigle
        # Dans un lien ou un bouton, pas de tabindex : un élément focalisable dans un élément focalisable gêne le
        # clavier et les lecteurs d'écran ; l'infobulle reste au survol et à l'impression.
        foc = "" if inter else ' tabindex="0"'
        neuf = neuf[:i] + f'<abbr class="sigle" title="{titre}"{foc}>{sigle}</abbr>' + neuf[i + len(sigle):]
    if 'id="sigles-css"' not in neuf and "</head>" in neuf:
        neuf = neuf.replace("</head>", CSS_SIGLES + "\n</head>", 1)
    return neuf, f"{len(choisis)} infobulle(s)"


def infobuller(src):
    """Explique dans ce source tous les sigles que `controle_sigles_expliques.py` voit non expliqués (E) ou expliqués trop
    bas (P), et le rend : QCM jamais expliqué s'écrit en clair (`poser`) quand il est dans le texte, tout le reste reçoit
    son infobulle. Pour un générateur : `page = infobuller(page)` avant d'écrire, et la page régénérée garde ses
    explications (n°283)."""
    for sigle, etat in cse.mesurer_source(src).items():
        if etat == "ok":
            continue
        neuf = poser(src, sigle)[0] if (sigle == "QCM" and etat == "E") else None
        neuf = neuf or poser_infobulle(src, sigle)[0]
        if neuf:
            src = neuf
    return src


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--sigle", required=True)
    ap.add_argument("--ecrire", action="store_true")
    ap.add_argument("--infobulle", action="store_true", help="une infobulle <abbr> au lieu d'une explication en clair")
    ap.add_argument("pages", nargs="*")
    a = ap.parse_args(argv)
    if a.sigle not in cse.SIGLES:
        print(f"✘ {a.sigle} n'est pas dans la liste de controle_sigles_expliques.py : l'ajouter d'abord, avec son explication")
        return 2
    pages = [pathlib.Path(x) for x in a.pages] or [p for p in cse.pages_tout() if cse.mesurer(p).get(a.sigle) == "E"]
    if not pages:
        print("Rien à lire.")
        return 2
    poses, main_ = 0, []
    for page in pages:
        src = page.read_text(encoding="utf-8")
        neuf, info = poser_infobulle(src, a.sigle) if a.infobulle else poser(src, a.sigle)
        rel = page.resolve().relative_to(cse.RACINE) if cse.RACINE in page.resolve().parents else page
        if neuf is None:
            if info.startswith("à poser") or (a.infobulle and info.startswith("sigle absent")):
                main_.append(str(rel))
            print(f"○ {rel} — {info}")
            continue
        poses += 1
        print(f"{'✎' if a.ecrire else '→'} {rel}\n    … {info} …")
        if a.ecrire:
            page.write_text(neuf, encoding="utf-8")
    print(f"\n{poses} explication(s) {'posée(s)' if a.ecrire else 'à poser'} · {len(main_)} page(s) à poser à la main")
    return 1 if main_ else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
