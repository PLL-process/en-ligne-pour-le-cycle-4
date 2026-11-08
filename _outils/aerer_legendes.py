#!/usr/bin/env python3
"""aerer_legendes.py — chaque partie d'une légende ouvre sa ligne (08/11/2026, skill `texte-clair-et-aere`).

Pascal, le 08/11/2026 : « quant aux textes au-dessous des images, bien souvent un retour à la ligne est nécessaire ».
Les légendes du dépôt ont une anatomie stable : « Ce que tu dois voir : … », « Puis : … », une note en italique en
fin de légende, parfois des repères ① ② ③, et la mention « Image générée par IA (Canva) ». L'outil pose un <br>
devant chacune de ces parties quand du texte la précède sur la même ligne. Il ne réécrit aucun mot : une légende
encore trop longue après lui (L1 de `audit_aeration.py`) se réécrit à la main, selon le skill.

Usage : python3 _outils/aerer_legendes.py <page.html>… [--ecrire]     (sans --ecrire : ce qui changerait)
"""
import re
import sys

PUIS = re.compile(r"(?=<b>\s*Puis(?:&nbsp;|\s)*:)")
# un repère ouvre une ligne s'il annonce un point (« ① La conversion… ») ; « les repères ①②③ » les cite, sans liste
REPERE = re.compile(r"(?<![①②③④⑤⑥⑦⑧⑨])(?=[①②③④⑤⑥⑦⑧⑨](?:&nbsp;|\s)*[A-Za-zÀ-ÿ«(<])")
NOTE_FINALE = re.compile(r"(?=<i\b[^>]*>(?:(?!</?i\b).)*</i>\s*$)", re.S)


def texte_avant(cap, pos):
    avant = cap[:pos]
    dernier = avant.rfind("<br")
    debut = avant[dernier:] if dernier >= 0 else avant
    return re.sub(r"<[^>]+>|&nbsp;|\s", "", debut) != ""


def aerer(cap):
    positions = set()
    for m in PUIS.finditer(cap):
        positions.add(m.start())
    reperes = [m.start() for m in REPERE.finditer(cap)]
    if len(reperes) >= 2:
        positions.update(reperes)
    m = NOTE_FINALE.search(cap.rstrip())
    if m:
        positions.add(m.start())
    sortie, pris = cap, 0
    for pos in sorted(positions, reverse=True):
        if texte_avant(cap, pos):
            # l'espace d'avant reste : sans lui, une lecture vocale ou un copier-coller lirait « colonnes.Puis »
            avant = sortie[:pos]
            sortie = avant + ("" if avant[-1:].isspace() else " ") + "<br>" + sortie[pos:]
            pris += 1
    return sortie, pris


def traiter(chemin, ecrire):
    s = open(chemin, encoding="utf-8").read()
    total = 0

    def remplace(m):
        nonlocal total
        neuf, n = aerer(m.group(2))
        total += n
        return m.group(1) + neuf + m.group(3)

    neuf = re.sub(r"(<figcaption\b[^>]*>)(.*?)(</figcaption>)", remplace, s, flags=re.S | re.I)
    if ecrire and neuf != s:
        open(chemin, "w", encoding="utf-8").write(neuf)
    return total


def main():
    args = sys.argv[1:]
    ecrire = "--ecrire" in args
    pages = [a for a in args if not a.startswith("--")]
    if not pages:
        print(__doc__)
        return 2
    somme = 0
    for p in pages:
        n = traiter(p, ecrire)
        somme += n
        if n:
            print(("✎ " if ecrire else "· ") + p + " : %d retour(s) à la ligne" % n)
    print("%d page(s) lues, %d retour(s) à la ligne %s" % (len(pages), somme, "posés" if ecrire else "à poser"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
