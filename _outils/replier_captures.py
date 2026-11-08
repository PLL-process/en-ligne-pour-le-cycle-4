#!/usr/bin/env python3
"""replier_captures.py — les captures d'un geste se déplient à la demande (08/11/2026).

Révision des trois thèmes (skill `revision-sequence`) : Pascal, le 08/11/2026, « depuis longtemps cela me paraissait
une charge cognitive ». Les encarts de gestes (règle d'or n°93) montrent, sous chaque geste, deux ou trois captures
d'écran avec leur légende en trois temps (« Ce que tu dois voir », « Comment savoir que c'est fait », « Si tu vois
ceci »). Posées « visibles d'emblée » (journal du 10/09/2026), elles font l'essentiel du texte de la séance : sur
4e_C1.1, l'échauffement des quatre gestes du tableur comptait 1 007 mots visibles, la séance entière 1 641.

L'outil garde chaque geste écrit en toutes lettres, visible, et range ses captures dans un `<details>` placé au même
endroit : « 🖼 Le voir en images — 3 captures : ce que tu dois voir, et que faire si ça ne marche pas ». Rien n'est
retiré : les images, leur `alt`, leurs légendes restent sur la page, à un clic. Un élève qui sait faire lit le
geste et passe ; un élève qui hésite ouvre les images.

Une suite de captures est repliée quand elle compte au moins une `<figure class="geste-capture">` (seules ou à la
suite, séparées par des blancs). Une capture déjà dans un `<details>` n'est pas touchée. Rejouable.

Usage : python3 _outils/replier_captures.py <page.html>… [--ecrire]      (sans --ecrire : ce qui changerait)
"""
import re
import sys

FIGURE = re.compile(r'<figure class="geste-capture"[^>]*>.*?</figure>', re.S)
CSS = """<style id="css-geste-images">
/* replier_captures.py (08/11/2026) : les captures d'un geste se déplient à la demande */
details.geste-images{margin:8px 0;border:1px dashed var(--border,#274a8a);border-radius:10px;padding:4px 10px}
details.geste-images>summary{cursor:pointer;font-weight:600;padding:4px 0;min-height:24px}
details.geste-images[open]>summary{margin-bottom:6px}
@media print{details.geste-images{border-color:#999!important}}
</style>
"""


def dans_details(s, pos):
    """la position est-elle à l'intérieur d'un <details> ouvert plus haut et pas encore fermé ?"""
    avant = s[:pos]
    return len(re.findall(r"<details\b", avant)) > len(re.findall(r"</details\s*>", avant))


def resume(figures):
    n = len(figures)
    erreur = any("Si tu vois ceci" in f for f in figures)
    return ("🖼 Le voir en images — %d capture%s : ce que tu dois voir%s"
            % (n, "s" if n > 1 else "", ", et que faire si ça ne marche pas" if erreur else ""))


def traiter(chemin, ecrire):
    s = open(chemin, encoding="utf-8").read()
    figs = [m for m in FIGURE.finditer(s) if not dans_details(s, m.start())]
    suites, courante = [], []
    for m in figs:
        if courante and s[courante[-1].end():m.start()].strip() == "":
            courante.append(m)
        else:
            if courante:
                suites.append(courante)
            courante = [m]
    if courante:
        suites.append(courante)
    if not suites:
        return 0, 0
    sortie, pos = [], 0
    for suite in suites:
        deb, fin = suite[0].start(), suite[-1].end()
        bloc = s[deb:fin]
        sortie.append(s[pos:deb])
        sortie.append('<details class="geste-images"><summary>%s</summary>\n%s\n</details>'
                      % (resume([m.group(0) for m in suite]), bloc))
        pos = fin
    sortie.append(s[pos:])
    neuf = "".join(sortie)
    if 'id="css-geste-images"' not in neuf:
        k = neuf.lower().rfind("</head>")
        neuf = neuf[:k] + CSS + neuf[k:]
    if ecrire:
        open(chemin, "w", encoding="utf-8").write(neuf)
    return len(suites), sum(len(x) for x in suites)


def main():
    args = sys.argv[1:]
    ecrire = "--ecrire" in args
    pages = [a for a in args if not a.startswith("--")]
    if not pages:
        print(__doc__)
        return 2
    tg = tf = 0
    for p in pages:
        g, f = traiter(p, ecrire)
        tg += g
        tf += f
        if g:
            print(("✎ " if ecrire else "· ") + p + " : %d geste(s), %d capture(s) repliées" % (g, f))
    print("%d page(s) lues, %d suite(s) de captures %s (%d captures)" % (len(pages), tg, "repliées" if ecrire else "à replier", tf))
    return 0


if __name__ == "__main__":
    sys.exit(main())
