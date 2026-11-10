#!/usr/bin/env python3
"""aerer_corrections.py — une correction d'un seul tenant passe à la ligne entre ses phrases (08/11/2026).

Skill `texte-clair-et-aere`, passe complète d'une séquence (skill `revision-sequence`). `audit_aeration.py` signale
dans les corrections deux défauts :
  C1  un bloc de plus de 45 mots d'un seul tenant ;
  C2  un bloc où deux « ; » ou plus cousent des idées.
Pour un bloc C1, l'outil pose un retour à la ligne (<br>) à la fin d'une phrase, en gardant ensemble les phrases
courtes : une ligne fait au moins 12 mots avant qu'un retour soit posé, sauf une phrase courte en tête de bloc
(un repère : « Erreurs fréquentes. ») quand au moins 25 mots la suivent. Pour un bloc C2, il passe à la ligne après
chaque « ; » (la forme de liste française : chaque item finit par « ; », le dernier par « . »).

Il NE CHANGE AUCUN MOT. Il ne touche que le texte des blocs de correction (classes correction, correction-bloc,
corrige-bonus, feedback), jamais une incrustation des ateliers (son texte vient du générateur), jamais l'intérieur d'un <code>, <kbd>, <pre>, <script>, <style>, <summary>, d'un titre, d'un
champ ou d'un bouton. Une phrase seule de plus de 45 mots reste à réécrire à la main : l'outil la signale.

Usage : python3 _outils/aerer_corrections.py <page.html>… [--ecrire]       (sans --ecrire : ce qui changerait)
        python3 _outils/aerer_corrections.py <page.html>… --partout [--ecrire]

--partout (08/11/2026, révision des trois thèmes) : la même passe, hors des corrections, sur les paragraphes, les items
de liste et les définitions (<p>, <li>, <dd>) que l'élève lit d'un seul tenant, au-delà de 30 mots, et sur les légendes
(<figcaption>) au-delà de 35 (le seuil L1 de l'audit) : une consigne,
une annonce, une définition passent à la ligne entre leurs phrases. Jamais dans une incrustation des ateliers (le texte
y vient du générateur : il se corrige à sa source), ni dans un script, un style ou un schéma.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_aeration as A  # noqa: E402

MIN_LIGNE = 12
INTERDITS = {"code", "kbd", "pre", "script", "style", "summary", "h1", "h2", "h3", "h4", "h5", "h6", "textarea",
             "select", "option", "button", "label", "legend", "svg"}
FRONTIERE = re.compile(r"^<\s*(/?)\s*(br|p|li|td|th|tr|h[1-6]|div|ul|ol|dl|dt|dd|table|summary|details|figure|section)\b",
                       re.I)
# une fin de phrase : . ! ? ou … (éventuellement suivie de » ou d'une parenthèse), une espace, puis une majuscule,
# un guillemet ou un chiffre. « p. ex. », « 1. » en tête de liste et les nombres décimaux ne sont pas des fins.
FIN = re.compile(r"(?<!\bp)(?<!\bex)(?<!\bcf)(?<!\bn°)(?<=[a-zà-ÿ0-9)»\]%])([.!?…]+[»)]?)(\s|&nbsp;)+(?=[A-ZÀ-ÖØ-Ý«0-9])")
PV = re.compile(r"(&nbsp;| |\s)?;(\s|&nbsp;)+")


DELIM = re.compile(r"(<br\s*/?>|</?(?:p|li|td|th|tr|h[1-6]|div|ul|ol|dl|dt|dd|table|summary|details|figure|section)\b[^>]*>)",
                   re.I)
DEBUT_MAJ = re.compile(r"(?:\s|&nbsp;)*(?=[A-ZÀ-ÖØ-Ý«0-9])")
POINT_EN_TETE = re.compile(r"^([.!?…]+[»)]?)(?:\s|&nbsp;)+(?=[A-ZÀ-ÖØ-Ý«0-9])")


def mots_texte(fragment):
    return len(A.texte(fragment).split())


def reflow_segment(seg, pile, seuil=None):
    """un segment entre deux frontières : (segment aéré, retours posés)"""
    total = mots_texte(seg)
    c1 = total > (seuil or A.SEUIL_CORRECTION)
    c2 = A.texte(seg).count(";") >= 2
    toks = re.findall(r"<[^>]*>|[^<]+", seg, re.S)
    if not (c1 or c2):
        for t in toks:   # tenir la pile des balises interdites à jour
            m = re.match(r"<\s*(/?)\s*([a-zA-Z0-9]+)", t)
            if m and m.group(2).lower() in INTERDITS:
                if m.group(1):
                    if pile and pile[-1] == m.group(2).lower():
                        pile.pop()
                elif not t.endswith("/>"):
                    pile.append(m.group(2).lower())
        return seg, 0
    sortie, poses, consommes, ligne, fin_avant, espace_avant = [], 0, 0, 0, False, False
    for t in toks:
        if t.startswith("<"):
            m = re.match(r"<\s*(/?)\s*([a-zA-Z0-9]+)", t)
            if m and m.group(2).lower() in INTERDITS:
                if m.group(1):
                    if pile and pile[-1] == m.group(2).lower():
                        pile.pop()
                elif not t.endswith("/>"):
                    pile.append(m.group(2).lower())
            sortie.append(t)
            continue
        n_t = len(t.split())
        if pile:
            sortie.append(t)
            consommes += n_t
            ligne += n_t
            fin_avant = False
            continue
        coupes = []   # (texte gardé jusqu'à, reprise à, genre)
        if fin_avant:
            md = DEBUT_MAJ.match(t)
            if md and (md.end() > 0 or espace_avant):
                coupes.append((0, md.end(), "fin"))
        mp = POINT_EN_TETE.match(t)
        if mp and ligne > 0:
            coupes.append((mp.end(1), mp.end(), "fin"))
        for m in FIN.finditer(t):
            coupes.append((m.end(1), m.end(), "fin"))
        if c2:
            for m in PV.finditer(t):
                coupes.append((m.start() + len(m.group(1) or "") + 1, m.end(), "pv"))   # « ; » reste en fin de ligne
        coupes.sort()
        morceaux, pos = [], 0
        for garde, reprise, genre in coupes:
            if garde < pos:
                continue
            mots_avant = ligne + len(t[pos:garde].split())
            reste = total - (consommes + len(t[:reprise].split()))
            # une phrase courte en tête (« Erreurs fréquentes. ») ouvre sa ligne quand un long texte la suit ;
            # sinon les phrases courtes restent ensemble
            if (genre == "pv" and mots_avant >= 4) or (genre == "fin" and c1 and
                                                        (mots_avant >= MIN_LIGNE or (mots_avant >= 3 and reste >= 25))):
                morceaux.append(t[pos:garde] + (" <br>" if garde else "<br>"))
                poses += 1
                pos = reprise
                ligne = 0
        reste_t = t[pos:]
        morceaux.append(reste_t)
        ligne += len(reste_t.split())
        consommes += n_t
        fin_avant = bool(re.search(r"[a-zà-ÿ0-9)»\]%][.!?…]+[»)]?(?:\s|&nbsp;)*$", t))
        espace_avant = bool(re.search(r"(?:\s|&nbsp;)$", t))
        sortie.append("".join(morceaux))
    return "".join(sortie), poses


def reflow(fragment, seuil=None):
    """retourne (fragment avec <br>, nombre de retours posés, blocs encore trop longs)"""
    pile, sortie, poses = [], [], 0
    for seg in DELIM.split(fragment):
        if DELIM.fullmatch(seg or ""):
            sortie.append(seg)
            continue
        neuf, n = reflow_segment(seg, pile, seuil)
        sortie.append(neuf)
        poses += n
    neuf = "".join(sortie)
    # un retour posé juste après l'ouverture d'un gras ou d'un italique passe devant lui (« <b><br>Puis » → « <br><b>Puis »)
    neuf = BR_DANS_BALISE.sub(r"<br>\1", neuf)
    longues = [b[:80] for b in A.blocs(neuf) if A.mots(b) > (seuil or A.SEUIL_CORRECTION)]
    return neuf, poses, longues


BR_DANS_BALISE = re.compile(r"((?:<(?:b|i|em|strong|u)>)+)<br>")
SEUIL_PARTOUT = 30
INCRUSTATION = re.compile(r"<!-- ateliers-representations:debut (\S+) -->.*?<!-- ateliers-representations:fin \1 -->", re.S)
EXCLUS = re.compile(r"<!-- ateliers-representations:debut (\S+) -->.*?<!-- ateliers-representations:fin \1 -->|"
                    r"<(script|style|svg|template|h[1-6]|summary)\b.*?</\2\s*>|"
                    r"<(?:p|footer)\b[^>]*class=\"[^\"]*licence-cc[^>]*>.*?</(?:p|footer)>", re.S | re.I)


def zones_exclues(s):
    z = [(m.start(), m.end()) for m in EXCLUS.finditer(s)]
    for m in re.finditer(r"<(div|p|section|details|aside)\b[^>]*%s[^>]*>" % A.CLASSES_CORRECTION.pattern, s):
        contenu = A.element(s, m.start())
        z.append((m.start(), s.index(contenu, m.start()) + len(contenu) if contenu else m.end()))
    return sorted(z)


def partout(s):
    """les <p>, <li>, <dd> hors corrections et hors incrustations : (page aérée, retours posés, blocs restés longs)"""
    zones = zones_exclues(s)

    def exclu(a, b):
        return any(x < b and a < y for x, y in zones)
    morceaux, pos, total, longues = [], 0, 0, []
    for m in re.finditer(r"<(p|li|dd|figcaption)\b[^>]*>", s):
        if m.start() < pos:
            continue
        contenu = A.element(s, m.start())
        deb = s.index(">", m.start()) + 1
        fin = deb + len(contenu)
        # une légende : le seuil de l'audit (L1, 35 mots), une phrase par ligne au-delà
        seuil = A.SEUIL_LEGENDE if m.group(1) == "figcaption" else SEUIL_PARTOUT
        if exclu(m.start(), fin) or A.mots(A.texte(contenu)) <= seuil:
            continue
        # un <li> qui porte une sous-liste ou une figure : on n'aère que son texte, segment par segment (DELIM)
        neuf, n, lg = reflow(contenu, seuil)
        if n:
            morceaux.append(s[pos:deb])
            morceaux.append(neuf)
            pos = fin
            total += n
        longues += lg
    morceaux.append(s[pos:])
    return "".join(morceaux), total, longues


def aerer(s, tout=False):
    """la passe sur un texte HTML : (texte aéré, retours posés, blocs restés longs). `incrustations.py` l'appelle sur
    chaque incrustation qu'il engendre (10/11/2026) : c'est ainsi que le texte des ateliers s'aère « à sa source »."""
    morceaux, pos, total, longues = [], 0, 0, []
    # une incrustation des ateliers vient du générateur : son texte s'aère à sa source, pas ici
    incrustations = [(x.start(), x.end()) for x in INCRUSTATION.finditer(s)]
    for m in re.finditer(r"<(div|p|section|details|aside)\b[^>]*%s[^>]*>" % A.CLASSES_CORRECTION.pattern, s):
        if m.start() < pos or any(x <= m.start() < y for x, y in incrustations):
            continue
        contenu = A.element(s, m.start())
        deb = s.index(contenu, m.start()) if contenu else m.end()
        fin = deb + len(contenu)
        neuf, n, lg = reflow(contenu)
        morceaux.append(s[pos:deb])
        morceaux.append(neuf)
        pos = fin
        total += n
        longues += lg
    morceaux.append(s[pos:])
    neuf = "".join(morceaux)
    if tout:
        neuf, n, lg = partout(neuf)
        total += n
        longues += lg
    return neuf, total, longues


def traiter(chemin, ecrire, tout=False):
    s = open(chemin, encoding="utf-8").read()
    neuf, total, longues = aerer(s, tout)
    if ecrire and neuf != s:
        open(chemin, "w", encoding="utf-8").write(neuf)
    return total, longues


def main():
    args = sys.argv[1:]
    ecrire = "--ecrire" in args
    pages = [a for a in args if not a.startswith("--")]
    if not pages:
        print(__doc__)
        return 2
    somme = 0
    for p in pages:
        n, longues = traiter(p, ecrire, "--partout" in args)
        somme += n
        if n or longues:
            print(("✎ " if ecrire else "· ") + p + " : %d retour(s) à la ligne" % n)
        for l in longues:
            print("   ⚠ reste d'un seul tenant (phrase à réécrire à la main) : « %s… »" % l)
    print("%d page(s) lues, %d retour(s) à la ligne %s" % (len(pages), somme, "posés" if ecrire else "à poser"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
