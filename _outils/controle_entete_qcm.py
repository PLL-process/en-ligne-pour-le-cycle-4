# -*- coding: utf-8 -*-
"""controle_entete_qcm.py — ce qu'un QCM affiche de lui-même est vrai.

LE CONSTAT
----------
L'audit externe du thème 1 (08/09/2026, point A15) a montré trois QCM dont le sous-titre,
le menu « Compétence à réviser » et le pied de page venaient du lot de freinage de 5e. En
mesurant tout le dépôt le 09/09 : **31 QCM sur 68 avaient un menu « Compétence à réviser »
copié d'un autre lot** — le mode « cible » y rendait une liste vide, sans un mot — et
**24 en-têtes ou pieds de page nommaient un autre lot** (« 4e_C8.1 · C8.2 · C8.3 · New
York » en pied de vingt QCM de C7/C8, « 5e_C1.2 » en pied et sous-titre de trois QCM
de C1). Les tableaux de correspondance JavaScript, eux, étaient justes : seul le HTML
statique avait été copié.

CE QU'IL MESURE
---------------
Pour chaque QCM rangé dans un dossier de lot (`5e_C1.3`, `3e_C7.3`…) :

  · les zones que l'élève lit sur lui — `<title>`, `<h1>`, sous-titre (`.sub`/`.subtitle`),
    badges de code, `<footer>`, options du menu — ne nomment aucun code d'un AUTRE NIVEAU ;
  · le pied de page nomme le code du lot lui-même (ou l'un des codes des questions) ;
  · les `<option>` du menu « Compétence à réviser » correspondent exactement aux
    valeurs `c` des questions — sinon le mode « cible » ne rend rien.

CE QU'IL NE FAIT PAS
--------------------
Il ne juge pas le texte des questions : un code d'un autre niveau y est souvent un
distracteur légitime (« quel code correspond à… »). Il ne juge pas non plus le libellé
d'une option — seulement qu'elle désigne une compétence que le QCM contient.

Usage :
    python3 _outils/controle_entete_qcm.py           # rapport complet
    python3 _outils/controle_entete_qcm.py --muet    # seulement les refus
Sortie : 0 si chaque QCM dit vrai sur lui-même, 1 sinon.
"""

import glob
import html
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ECARTES = ("_archive-anciennes-versions",)

LOT = re.compile(r"^([345]e)_(C\d\.\d)")
CODE = re.compile(r"\b([345]e)_(C\d\.\d)\b")


def pages(racine):
    return sorted(f for f in glob.glob(os.path.join(racine, "**", "qcm*.html"), recursive=True)
                  if not any(e in f for e in ECARTES))


def _texte(fragment):
    return html.unescape(re.sub(r"<[^>]+>", " ", fragment or ""))


def _zone(texte, motif):
    m = re.search(motif, texte, re.S | re.I)
    return _texte(m.group(1)) if m else ""


def norm(c):
    return re.sub(r"^[345]e_", "", c)


def juger(chemin):
    """None si le QCM n'est pas dans un dossier de lot ; sinon la liste des écarts."""
    lot = os.path.basename(os.path.dirname(chemin))
    m = LOT.match(lot)
    if not m:
        return None
    niveau, code_lot = m.groups()
    t = open(chemin, encoding="utf-8", errors="replace").read()
    zones = {
        "title": _zone(t, r"<title>(.*?)</title>"),
        "h1": _zone(t, r"<h1[^>]*>(.*?)</h1>"),
        "sous-titre": _zone(t, r'<p class="(?:sub|subtitle)"[^>]*>(.*?)</p>'),
        "badges": _zone(t, r'<div class="badges">(.*?)</div>'),
        "pied": _zone(t, r"<footer[^>]*>(.*?)</footer>"),
        "menu": _zone(t, r'<select id="selComp"[^>]*>(.*?)</select>'),
    }
    questions = re.findall(r'\{\s*c\s*:\s*"([^"]+)"', t)
    codes_q = {norm(c) for c in questions}
    # un code d'un autre niveau est toléré s'il est VRAIMENT celui de questions du QCM : le
    # QCM de 4e_C1.4 revisite 5e_C1.5 et 5e_C1.6, et le dit dans son titre. On le sait par
    # les valeurs `c` complètes ou par le tableau de correspondance (« 5e_C1.5 — … »).
    carte = re.search(r"const (?:COMP_LABELS|COMP)\s*=\s*\{(.*?)\};", t, re.S)
    complets = {"%s_%s" % nc for nc in CODE.findall(" ".join(questions) + " " + (carte.group(1) if carte else ""))}
    ecarts = []
    for nom, z in zones.items():
        etrangers = sorted({"%s_%s" % (n, c) for n, c in CODE.findall(z)
                            if n != niveau and "%s_%s" % (n, c) not in complets})
        if etrangers:
            ecarts.append("%s nomme un autre niveau : %s" % (nom, ", ".join(etrangers)))
    if zones["pied"] and questions:
        pied_codes = {c for _n, c in CODE.findall(zones["pied"])} | set(re.findall(r"\bC\d\.\d\b", zones["pied"]))
        if code_lot not in pied_codes and not (codes_q & pied_codes):
            ecarts.append("le pied de page ne nomme ni %s ni un code des questions (%s)"
                          % (code_lot, ", ".join(sorted(pied_codes)) or "aucun code"))
    sel = re.search(r'<select id="selComp"[^>]*>(.*?)</select>', t, re.S)
    if sel and questions:
        options = {norm(o) for o in re.findall(r'<option value="([^"]+)"', sel.group(1))}
        if options != codes_q:
            ecarts.append("menu « Compétence à réviser » : propose %s, les questions portent %s "
                          "— le mode « cible » ne rend rien"
                          % (", ".join(sorted(options)) or "rien", ", ".join(sorted(codes_q))))
    return ecarts


def main(muet=False):
    lus, fautifs = 0, []
    for f in pages(DEPOT):
        r = juger(f)
        if r is None:
            continue
        lus += 1
        if r:
            fautifs.append((os.path.relpath(f, DEPOT).replace(os.sep, "/"), r))
    if not muet:
        print("%d QCM lus · %d disent faux sur eux-mêmes" % (lus, len(fautifs)))
        print("     NON LU : le texte des questions (un code d'un autre niveau y est souvent un\n"
              "     distracteur légitime), et le libellé des options du menu.")
    if fautifs:
        print("\n⛔ %d QCM affichent un en-tête, un pied ou un menu venus d'un autre lot :" % len(fautifs))
        for rel, es in fautifs:
            print("  %s" % rel)
            for e in es:
                print("     · %s" % e)
        return 1
    print("\n✅ chaque QCM dit vrai sur lui-même : titre, sous-titre, badges, pied, menu")
    return 0


if __name__ == "__main__":
    sys.exit(main("--muet" in sys.argv))
