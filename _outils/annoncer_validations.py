# -*- coding: utf-8 -*-
"""annoncer_validations.py — l'élève lit ce que la vérification accepte (règle d'or n°340, V1 et V4).

LE CONSTAT
----------
`controle_validations.py` a mesuré, le 17/11/2026, 59 activités dont le code valide avec une tolérance que la page ne
dit pas (« 5 / 6 » codé, rien d'écrit), et 99 réponses écrites validées par des mots-clés sans que l'élève sache que
son professeur la relira. Pascal, le 18/11/2026 : annoncer chaque tolérance, dire la relecture (n°340).

CE QUE FAIT L'OUTIL
-------------------
Pour chaque activité qu'il signale, juste avant son bouton « Vérifier » (`data-check`), sans toucher au code :
  · V1, pas de critère : un critère qui dit le seuil réel — « 🎯 Critère de réussite : au moins 5 réponses justes
    sur 6 » ; si la vérification demande autre chose encore (`valide: ok>=5 && …`), « et ce que le message de
    « Vérifier » te demande encore » ;
  · V1, un critère qui tait la tolérance : la phrase « Au moins 5 réponses justes sur 6 suffisent à valider. » à la
    fin de ce critère ;
  · V4 : « ✍ Ta réponse écrite sera relue par ton professeur : « Vérifier » regarde si l'essentiel y est, pas si
    tout est juste. »
Un exercice incrusté (atelier) n'est pas touché : il a sa vérification. L'outil se rejoue sans rien changer.

  python3 _outils/annoncer_validations.py [--ecrire] [page.html | dossier …]   (sans chemin : les trois thèmes)

Sortie : 0 rien à annoncer, ou tout écrit (--ecrire) · 1 il reste à annoncer · 2 rien lu (n°299).
"""
from __future__ import annotations

import os
import re
import sys

OUT = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(OUT)
sys.path.insert(0, OUT)
import controle_validations as V  # noqa: E402

STYLE = 'style="font-size:.9em;color:var(--sub)"'
RELU_HTML = ('<p class="note-relue" %s>✍ Ta réponse écrite sera relue par ton professeur&nbsp;: «&nbsp;Vérifier&nbsp;» '
             'regarde si l\'essentiel y est, pas si tout est juste.</p>' % STYLE)
V1_MSG = re.compile(r"activité (\S+) : le code valide à (\d+) / (\d+), la page ne l'annonce pas \(critère : « (.*) »\)$")
V4_MSG = re.compile(r"activité (\S+) : une réponse écrite")


def bouton(src: str, n: str):
    """La position de la balise <button … data-check="n"> de l'activité (hors scripts et exercices incrustés)."""
    interdits = [(m.start(), m.end()) for m in re.finditer(r"<script\b.*?</script>", src, re.S)]
    for m in V.INCRUSTE.finditer(src):
        prof, fin = 0, len(src)
        for t in V.SECTION.finditer(src, m.start()):
            prof += 1 if t.group(0) == "<section" else -1
            if prof == 0:
                fin = t.end()
                break
        interdits.append((m.start(), fin))
    for m in re.finditer(r'<button\b[^>]*\bdata-check="%s"[^>]*>' % re.escape(n), src):
        if not any(a <= m.start() < b for a, b in interdits):
            return m.start()
    return None


def avant_bouton(src: str, pos: int, html: str) -> str:
    debut = src.rfind("\n", 0, pos) + 1
    retrait = re.match(r"[ \t]*", src[debut:pos]).group(0) if src[debut:pos].strip() == "" else ""
    if retrait or src[debut:pos] == "":
        return src[:debut] + retrait + html + "\n" + src[debut:]
    return src[:pos] + html + src[pos:]


def annoncer(src: str):
    """(page annoncée, [ce qui a été écrit])."""
    faits = []
    corps = V.entrees(src)
    for g, code, msg in V.analyser(src):
        m = V1_MSG.match(msg) if code == "V1" and g == "⚠" else None
        if m:
            n, k, t, crit = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
            pos = bouton(src, n)
            if pos is None:
                continue
            if crit == "aucun":
                plus = ""
                seuil = V.SEUIL.search(corps.get(n, ""))
                if seuil and "&&" in seuil.group(1):
                    plus = ", et ce que le message de «&nbsp;Vérifier&nbsp;» te demande encore"
                html = ('<p class="critere" %s>🎯 <b>Critère de réussite&nbsp;:</b> au moins %d réponses justes sur %d%s.</p>'
                        % (STYLE, k, t, plus))
                src = avant_bouton(src, pos, html)
                faits.append("V1 activité %s : critère écrit (%d / %d)" % (n, k, t))
            else:
                z, b = V.zone(src, n)
                cs = [(abs(c.start() - b), c) for c in re.finditer(r'class="critere[^"]*"[^>]*>(.*?)</(div|p)>', z, re.S)]
                c = min(cs, key=lambda x: x[0])[1]
                vieux = z[c.start():c.end()]
                fin = vieux.rfind("</")
                neuf = vieux[:fin].rstrip()
                neuf = neuf + ("" if neuf.endswith((".", "!", "?")) else ".") + \
                    " Au moins %d réponses justes sur %d suffisent à valider.%s" % (k, t, vieux[fin:])
                assert src.count(vieux) == 1, (n, vieux[:80])
                src = src.replace(vieux, neuf)
                faits.append("V1 activité %s : tolérance ajoutée au critère (%d / %d)" % (n, k, t))
        m4 = V4_MSG.match(msg) if code == "V4" else None
        if m4:
            n = m4.group(1)
            pos = bouton(src, n)
            if pos is None:
                continue
            src = avant_bouton(src, pos, RELU_HTML)
            faits.append("V4 activité %s : relecture annoncée" % n)
    return src, faits


def main(argv):
    ecrire = "--ecrire" in argv
    ps = V.pages([a for a in argv if not a.startswith("--")])
    if not ps:
        print("✘ aucune page lue : rien n'a été vérifié")
        return 2
    total = 0
    for p in ps:
        s = open(p, encoding="utf-8").read()
        u, faits = annoncer(s)
        if not faits:
            continue
        total += len(faits)
        print("  %s %s" % ("✍" if ecrire else "⚠", os.path.relpath(p, DEPOT)))
        for f in faits:
            print("      " + f)
        if ecrire:
            open(p, "w", encoding="utf-8").write(u)
    print("%d page(s) lues · %d annonce(s) %s" % (len(ps), total, "écrite(s)" if ecrire else "à écrire"))
    return 1 if (total and not ecrire) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
