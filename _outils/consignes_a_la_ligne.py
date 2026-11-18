#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Règle d'or n°342 : met à la ligne, dans une page, les consignes qui donnent plusieurs actions sur une ligne.

Le contrôle est `controle_consignes_a_la_ligne.py` ; cet outil fait la passe mécanique de la vague, ligne par ligne :
  N1 (étapes numérotées sur une ligne) : un retour avant chaque repère (②, ③… ou b), c)…) et avant le premier s'il suit
     une phrase de contexte ; le « ; » qui les cousait disparaît, l'étape finit par un point et commence par une capitale.
  N2 (actions enchaînées) : chaque action va sur sa ligne et se numérote (①, ②…) ; le « ; », le « , puis »,
     l'« ensuite » qui les cousaient disparaissent (le numéro dit l'ordre) ; la phrase de contexte reste en tête, sur sa
     ligne ; ce qui suit une action sans en être une (une précision, un exemple) reste avec elle.
Aucun autre mot ne change. Une ligne qu'il ne sait pas couper sans risque est NOMMÉE, à reprendre à la main :
  - la coupure tomberait dans un gras, un lien, du code ;
  - la ligne porte déjà un numéro (« ② Lance l'essai, puis choisis… ») : la numérotation est à repenser.
Il ne lit que les pages qu'on lui donne, et n'écrit qu'avec --ecrire. Une page engendrée se corrige dans sa source.

Usage :
  python3 _outils/consignes_a_la_ligne.py <page.html>…            # ce qui serait changé, ligne par ligne
  python3 _outils/consignes_a_la_ligne.py <page.html>… --ecrire   # l'écrit
Sortie 0 ; 2 si aucune page n'a pu être lue (n°299).
"""
import html as H
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_consignes_a_la_ligne as C  # noqa: E402

NUMEROS = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
INLINE = {"b", "strong", "i", "em", "a", "span", "code", "mark", "u", "sup", "sub", "kbd", "abbr", "small", "q", "label"}
VIDES = {"br", "img", "input", "wbr", "hr"}
FIN = ".!?…:"
CONNECTEUR = re.compile(r"^(?:puis|ensuite|enfin|et\s+ensuite)\s*,?\s+", re.I)


def masquer(s):
    """les scripts, styles et modèles remplacés par des blancs de même longueur : les positions restent justes"""
    return re.sub(r"<(script|style|template)\b.*?</\1\s*>", lambda m: " " * len(m.group(0)), s, flags=re.S | re.I)


def zones_consignes(s):
    """(début, fin) du CONTENU de chaque consigne de la page, sans consigne imbriquée"""
    m = masquer(s)
    debuts = []
    for x in C.CLASSE_CONSIGNE.finditer(m):
        if any(re.fullmatch(r"(?:[a-z]+-)*consigne(?:-[a-z]+)*", j) for j in x.group(2).split()):
            debuts.append(x.start())
    debuts += [x.start() for x in C.PARAGRAPHE_CONSIGNE.finditer(m)]
    zones = []
    for d in sorted(set(debuts)):
        if any(a <= d < b for a, b in zones):
            continue
        contenu = C.element(m, d)
        a = m.index(">", d) + 1
        zones.append((a, a + len(contenu)))
    return zones


def lignes_html(s, a, b):
    """(début, fin) de chaque ligne entre deux frontières, dans s[a:b] ; un <pre> n'est jamais coupé"""
    bornes, i = [a], a
    frag = s[a:b]
    pre = [(x.start() + a, x.end() + a) for x in re.finditer(r"<pre\b.*?</pre\s*>", frag, re.S | re.I)]
    for x in C.FRONTIERE.finditer(frag):
        p = x.start() + a
        if any(u <= p < v for u, v in pre):
            continue
        bornes += [p, x.end() + a]
    bornes.append(b)
    return [(bornes[k], bornes[k + 1]) for k in range(0, len(bornes) - 1, 2) if bornes[k] < bornes[k + 1]]


def lire(s, a, b):
    """le texte de s[a:b], avec pour chaque caractère sa place dans s et sa profondeur dans les balises en ligne"""
    txt, pos, prof, dans_code = [], [], [], []
    pile, i = [], a
    while i < b:
        c = s[i]
        if c == "<":
            j = s.find(">", i)
            j = b if j < 0 else j + 1
            t = re.match(r"<(/?)([a-zA-Z0-9]+)", s[i:j])
            if t:
                nom = t.group(2).lower()
                if t.group(1):
                    if nom in pile:
                        while pile and pile.pop() != nom:
                            pass
                elif nom in INLINE and not s[i:j].endswith("/>"):
                    pile.append(nom)
                elif nom not in VIDES:
                    pile.append(nom)
            i = j
            continue
        if c == "&":
            e = re.match(r"&(?:#\d+|#x[0-9a-fA-F]+|[a-zA-Z]+);", s[i:b])
            if e:
                txt.append(H.unescape(e.group(0)))
                pos.append((i, i + len(e.group(0))))
                prof.append(len(pile))
                dans_code.append("code" in pile or "pre" in pile)
                i += len(e.group(0))
                continue
        txt.append(c)
        pos.append((i, i + 1))
        prof.append(len(pile))
        dans_code.append("code" in pile or "pre" in pile)
        i += 1
    return "".join(txt).replace(" ", " "), pos, prof, dans_code


def capitale(s, pos, k):
    """(place, lettre) pour mettre en capitale la première lettre à partir de k"""
    while k < len(s) and not s[k].isalpha():
        k += 1
    if k < len(s) and s[k].islower():
        return [(pos[k][0], pos[k][1], s[k].upper())]
    return []


def coupures_ligne(s, a, b):
    """les remplacements [(début, fin, texte)] qui mettent la ligne s[a:b] à la ligne, ou (None, raison)"""
    t, pos, prof, code = lire(s, a, b)
    if not t.strip():
        return [], None
    codes = [c for c, _ in C.ecarts_ligne(t)]
    if not any(c in ("N1", "N2") for c in codes):
        return [], None
    base = min(prof) if prof else 0
    # le texte de l'étiquette « Consigne : » en tête
    lab = re.match(r"^\s*(?:[^\w\s]+\s*)?(?:consigne[^:.—–-]{0,40}?\s*[:.—–-]\s*)?", t, re.I)
    debut_utile = lab.end() if lab else 0
    rep = []
    derniere = [-1]

    def couper(k, g=None, numero="", efface=0, cap=None):
        """une nouvelle ligne commence en k : efface t[g:k] (par défaut les blancs, « ; » et virgules qui précèdent)
        et le connecteur t[k:k+efface] ; finit la ligne d'avant par un point ; ajoute le numéro ; met la capitale"""
        if g is None:
            g = k
            while g > 0 and (t[g - 1].isspace() or t[g - 1] in ";,"):
                g -= 1
        while g > 0 and t[g - 1].isspace():
            g -= 1
        if g > 1 and t[g - 1] in "—–" and t[g - 2].isspace():
            g -= 1
            while g > 0 and t[g - 1].isspace():
                g -= 1
        if g <= derniere[0]:
            raise ValueError("deux coupures se chevauchent")
        derniere[0] = k
        ins = pos[k][0]
        if k < len(t) and prof[k] != base:
            # l'action commence au premier mot d'un gras (« , puis <b>écris</b> ») : la coupure va avant la balise
            if not code[k] and k > 0 and prof[k - 1] == base and all(prof[x] == prof[k] for x in range(k, k + efface)):
                ins = pos[k - 1][1]
            else:
                raise ValueError("la coupure tombe dans une balise en ligne")
        for x in list(range(g, k)):
            if prof[x] != base or code[x]:
                raise ValueError("la coupure tombe dans une balise en ligne")
        if k < len(t) and code[k]:
            raise ValueError("la coupure tombe dans du code")
        for x in list(range(g, k)) + list(range(k, k + efface)):
            rep.append((pos[x][0], pos[x][1], ""))
        avant_ligne = t[:g].strip() != ""
        point = "." if avant_ligne and g > debut_utile and t[g - 1] not in FIN else ""
        rep.append((ins, ins, point + ("<br>" if avant_ligne else "") + (numero + " " if numero else "")))
        rep.extend(capitale(t, pos, k + efface if cap is None else cap))

    def fin_repere(k):
        return k + (1 if t[k] in NUMEROS else len(re.match(r"\(?[a-h]\)", t[k:]).group(0)))

    try:
        marques = [m.start() for m in re.finditer("[%s]" % NUMEROS, t) if not code[m.start()]]
        lettres = [m.start(1) for m in re.finditer(r"(?:^|\s)(\(?[a-h]\))\s", t) if not code[m.start(1)]]
        if "N1" in codes:
            ks = marques if len(marques) >= 2 else lettres
            for n, k in enumerate(ks):
                if n == 0 and not t[debut_utile:k].strip() and not t[:debut_utile].strip():
                    rep.extend(capitale(t, pos, fin_repere(k)))
                    continue
                couper(k, cap=fin_repere(k))
            return rep, None
        if re.match(r"^\s*(?:[%s]|\(?[a-h]\)|\(?[1-9][0-9]?[.)])" % NUMEROS, t[debut_utile:]):
            return None, "la ligne porte déjà un numéro : la numérotation est à repenser"
        if marques or lettres:
            return None, "la ligne mêle un repère numéroté et des actions enchaînées"
        # N2 : les segments (début, fin) et le début du séparateur qui les précède
        segs, k, sep = [], 0, 0
        for m in C.SEPARATEUR.finditer(t):
            if any(code[x] for x in range(m.start(), m.end())):
                continue
            segs.append((k, m.start(), sep))
            k, sep = m.end(), m.start()
        segs.append((k, len(t), sep))
        actions = [(u, v, g) for u, v, g in segs if t[u:v].strip() and C.est_action(t[u:v])]
        if len(actions) < 2:
            return [], None
        if len(actions) > 3:
            return None, "%d actions sur une ligne : la consigne est à réécrire" % len(actions)
        for n, (u, v, g) in enumerate(actions):
            while u < v and t[u].isspace():
                u += 1
            if n == 0 and u < debut_utile and t[:debut_utile].strip():
                u = debut_utile
            i, avant = verbe_pos(t[u:v])
            if i is not None and avant.rstrip().endswith("("):
                raise ValueError("une action entre parenthèses")
            if i is not None and avant.rstrip().endswith(":"):
                # une étiquette (« Consigne : », « 📌 Avant de commencer : ») : l'action commence au verbe
                u = u + i
                g = None
            elif n == 0:
                g = None
            cn = CONNECTEUR.match(t[u:v])
            lg = cn.end() if cn else 0
            if n == 0 and not t[:u].strip():
                tete = a
                while tete < len(s) and s[tete].isspace():
                    tete += 1
                rep.append((tete, tete, NUMEROS[0] + " "))
                for x in range(u, u + lg):
                    rep.append((pos[x][0], pos[x][1], ""))
                rep.extend(capitale(t, pos, u + lg))
                continue
            couper(u, g=g if n else None, numero=NUMEROS[n], efface=lg)
        return rep, None
    except ValueError as e:
        return None, str(e)


def verbe_pos(seg):
    """(place du verbe dans le segment, texte qui le précède) ; (None, "") s'il n'y en a pas"""
    for m in re.finditer(C.MOT, seg[:90], re.I):
        avant = seg[:m.start()]
        a = avant.strip()
        if not C.verbe(m.group(1)):
            continue
        if not a or a[-1] in ",:(" or re.search(r"(?:^|\s)(?:puis|ensuite|enfin)$", a, re.I) or not re.search(r"\w", a):
            return m.start(), avant
    return None, ""


def appliquer(s, rep):
    for d, f, x in sorted(rep, key=lambda r: (r[0], r[1]), reverse=True):
        s = s[:d] + x + s[f:]
    return s


def traiter(chemin, ecrire):
    s = open(chemin, encoding="utf-8").read()
    toutes, manuelles = [], []
    for a, b in zones_consignes(s):
        for u, v in lignes_html(s, a, b):
            rep, raison = coupures_ligne(s, u, v)
            texte = C.texte(s[u:v])
            if raison:
                manuelles.append((texte, raison))
            elif rep:
                toutes.append((u, v, rep, texte))
    for u, v, rep, texte in toutes:
        delta = sum(len(x) - (f - d) for d, f, x in rep)
        apres = appliquer(s, rep)[u:v + delta]
        print("  ✎ « %s »\n    → %s" % (texte[:150], re.sub(r"\s+", " ", apres)[:400]))
    nouveau = appliquer(s, [r for _, _, rep, _ in toutes for r in rep])
    for texte, raison in manuelles:
        print("  ✋ à la main (%s) : « %s »" % (raison, texte[:150]))
    if ecrire and nouveau != s:
        open(chemin, "w", encoding="utf-8").write(nouveau)
    return len(toutes), len(manuelles)


def main():
    args = sys.argv[1:]
    ecrire = "--ecrire" in args
    pages = [a for a in args if not a.startswith("--")]
    lues = 0
    for p in pages:
        if not os.path.exists(p):
            print("✘ introuvable : " + p)
            continue
        lues += 1
        print("── " + p)
        n, m = traiter(p, ecrire)
        print("   %d ligne(s) mise(s) à la ligne%s · %d à reprendre à la main" % (n, "" if ecrire else " (à écrire)", m))
    if not lues:
        print("✘ aucune page lue")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
