# -*- coding: utf-8 -*-
"""nommer_competences.py — écrit chaque compétence du CRCN en toutes lettres dans une page (règle d'or n°314).

    python3 _outils/nommer_competences.py <page.html> [<page.html> …]      # réécrit les pages
    python3 _outils/nommer_competences.py --voir <page.html> […]          # montre ce qu'il ferait, sans écrire

Ce qu'il fait, et rien d'autre :
  1. après chaque code CRCN montré sans son intitulé (« CRCN 1.3 », « CRCN : 1.2 · 1.3 »), il écrit l'intitulé
     officiel : « CRCN 1.3 Traiter des données », « CRCN : 1.2 Gérer des données · 1.3 Traiter des données » ;
  2. il donne à chaque étiquette (`<span class="badge …">`) qui nomme des compétences du CRCN une bulle (`title`) à
     trois étages par compétence : « CRCN 1.3 Traiter des données — niveau 2. », « Le cadre : « … » » (la description
     officielle), et le « Ici : … » que la bulle avait déjà — il ne l'invente jamais : s'il manque, le contrôle le
     réclame, et il s'écrit à la main, page par page ; aux étiquettes de domaines du socle, une infobulle qui donne
     chaque domaine en toutes lettres ;
  3. il sépare en deux étiquettes une étiquette qui mêlait domaines du socle et CRCN.
Il ne touche ni aux commentaires (HTML, CSS, JavaScript), ni aux <style>, ni aux codes de rangement (4e_C8.1…). Les intitulés s'écrivent avec
l'apostrophe typographique (’) : ils ne cassent ni une chaîne JavaScript, ni un attribut. Ce qu'il ne sait pas faire
(un code coupé par une balise, « CRCN <b>1.3</b> ») reste signalé par `controle_competences.py` : à reprendre à la main.
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from controle_competences import CADRE, CRCN, SOCLE, SOCLE_CLE, chaine, etages_manquants, norme, segments  # noqa: E402
from controle_regles_visibles import masque  # noqa: E402

TYPO = {c: t.replace("'", "’") for c, t in CRCN.items()}
CADRE_TYPO = {c: t.replace("'", "’") for c, t in CADRE.items()}
SOCLE_TYPO = {d: t.replace("'", "’") for d, t in SOCLE.items()}
SEP_RAW = re.compile(r"(?:\s|&nbsp;|&#160;|&#x?a0;|&middot;|&#183;|·|•|,|;|/|\+|&amp;|\bet\b|\bou\b|:)+", re.I)
CODE_RAW = re.compile(r"(?<![\d.])([1-5]\.[1-4])(?![\d.]*\d)")
APRES_RAW = re.compile(r"(?:\s|&nbsp;|&#160;)*(?:(?:—|–|-|:|&mdash;|&ndash;)(?:\s|&nbsp;|&#160;)*)?")
NIVEAU_RAW = re.compile(r"(?:\s|&nbsp;)*\(?\s*(?:niv(?:eau)?\.?\s*|N\s?)\d(?:\s*(?:[-–→/]|&rarr;|à)\s*\d)?\s*\)?", re.I)
PAREN_RAW = re.compile(r"(?:\s|&nbsp;)*\((?:programme|visé|extension|compl[ée]mentaire)[^)]*\)", re.I)


def _fin_intitule(src, j, intitule):
    """Si l'intitulé suit (au séparateur près), la position où il finit dans le source ; sinon None."""
    m = APRES_RAW.match(src, j)
    k = m.end() if m else j
    cible = norme(intitule)
    fen = src[k:k + 400]
    if not norme(html.unescape(fen)).startswith(cible):
        return None
    for n in range(len(cible), len(fen) + 1):          # le plus court préfixe du source qui contient l'intitulé
        if norme(html.unescape(fen[:n])) .startswith(cible):
            return k + n
    return None


def inserer_intitules(src):
    """Le source, avec l'intitulé écrit après chaque code CRCN qui ne l'avait pas. Rend (source, [(code, extrait)])."""
    vu = masque(src)                                       # commentaires (HTML, CSS, JS) et <style> : intouchables
    dans_mort = lambda i: vu[i] != src[i]
    ajouts = []
    for m in re.finditer(r"\bCRCN\b", src):
        if dans_mort(m.start()):
            continue
        j = m.end()
        while True:
            s = SEP_RAW.match(src, j)
            if s:
                j = s.end()
            c = CODE_RAW.match(src, j)
            if not c:
                break
            code, j = c.group(1), c.end()
            fin = _fin_intitule(src, j, CRCN.get(code, "§§§"))
            if fin is not None:
                j = fin
            elif code in TYPO:
                ajouts.append((j, " " + TYPO[code], code))
            for motif in (NIVEAU_RAW, PAREN_RAW, NIVEAU_RAW):
                n = motif.match(src, j)
                if n and n.group(0).strip():
                    j = n.end()
    for pos, texte, code in sorted(ajouts, reverse=True):
        src = src[:pos] + texte + src[pos:]
    return src, [(code, None) for _, _, code in ajouts]


def _texte(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]*>", "", fragment))).strip()


NIV = re.compile(r"(?:\bniv(?:eau)?\.?|\bN)\s?(\d)(?:\s*([-–→/]|à)\s*(\d))?", re.I)


def niveaux(texte):
    """{code: « niveau 2 », « niveaux 2 à 3 », « niveau 2, vers le 3 »} : le niveau que l'étiquette écrit après chaque
    code (« (Niv. 2) », « niv. 3 », « — Niv. 2 », « (niv. 2→3) »)."""
    m = re.search(r"\bCRCN\b", texte)
    pos = [(c, p) for c, p, _ in chaine(texte, m.end())] if m else []
    out = {}
    for k, (c, p) in enumerate(pos):
        n = NIV.search(texte, p + len(c), pos[k + 1][1] if k + 1 < len(pos) else len(texte))
        if n:
            a, sep, b = n.groups()
            out[c] = ("niveau %s" % a if not b else
                      "niveau %s, vers le %s" % (a, b) if sep == "→" else "niveaux %s à %s" % (a, b))
    return out


def titre_crcn(codes, niv=None, ici=None):
    """La bulle à trois étages (règle n°314) : pour chaque compétence, « CRCN 1.3 Traiter des données — niveau 2. »,
    puis « Le cadre : « … » » (la description officielle, mot pour mot), puis « Ici : … » si on le connaît — sinon le
    contrôle le réclamera : il s'écrit à la main."""
    niv, ici = niv or {}, ici or {}
    blocs = []
    for c in codes:
        if c not in TYPO:
            continue
        lignes = ["CRCN %s %s%s." % (c, TYPO[c], " — " + niv[c] if niv.get(c) else ""), "Le cadre : « %s. »" % CADRE_TYPO[c]]
        if ici.get(c):
            t = ici[c].strip()
            lignes.append("Ici : " + t + ("" if t[-1] in ".!?…" else "."))
        blocs.append("\n".join(lignes))
    return "\n\n".join(blocs)


def ici_de(ancien, codes):
    """Les « Ici : » déjà écrits dans une bulle, par compétence. Une infobulle de l'ancienne forme (« … — l'élève exploite
    un tableau de mesures ») donne son complément comme « Ici : » quand elle ne parle que d'une compétence."""
    segs = segments(ancien)
    out = {}
    for c in codes:
        m = re.search(r"\bIci\s*:\s*(.+)", segs.get(c, ""), re.S)
        if m:
            out[c] = re.sub(r"\s+", " ", m.group(1)).strip()
    if not segs and len(codes) == 1 and " — " in ancien:
        reste = ancien.split(" — ", 1)[1].strip()
        if reste:
            out[codes[0]] = reste[0].upper() + reste[1:]
    return out


def _titre_socle(doms):
    return "Domaines du socle commun travaillés : " + " · ".join("%s %s" % (d, SOCLE_TYPO[d]) for d in doms if d in SOCLE_TYPO) + "."


def _avec_titre(attrs, titre):
    titre = (titre.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")
             .replace("\n", "&#10;"))
    if re.search(r'\btitle="[^"]*"', attrs):
        return re.sub(r'\btitle="[^"]*"', 'title="%s"' % titre, attrs, count=1)
    return attrs + ' title="%s"' % titre


DOMAINES = re.compile(r"(?<![\w.])(D[1-5](?:\.[1-4])?)(?![\w.]*\d)")


def etiquettes(src):
    """Les étiquettes CRCN et socle avec leur infobulle en toutes lettres ; une étiquette mixte devient deux."""
    changees = []

    def une(m):
        tag, attrs, contenu = m.group(1), m.group(2), m.group(3)
        if not re.search(r'\bclass="[^"]*\bbadge\b', attrs):
            return m.group(0)
        texte = _texte(contenu)
        ancien = html.unescape((re.search(r'\btitle="([^"]*)"', attrs) or [None, ""])[1])
        a_crcn = re.search(r"\bCRCN\b", texte)
        doms = DOMAINES.findall(texte[:a_crcn.start()] if a_crcn else texte)
        socle = bool(doms) and re.match(r"(?:Socle\s*:?\s*)?D[1-5]", texte)
        if a_crcn and socle:                              # étiquette mixte : on sépare
            i = contenu.find("CRCN")
            gauche = re.sub(r"(?:\s|&nbsp;|·|&middot;|,|;)+$", "", contenu[:i])
            droite = contenu[i:]
            codes = [c for c, _, _ in chaine(_texte(droite), 4)]
            attrs_sans_id = re.sub(r'\s+id="[^"]*"', "", attrs)
            changees.append(texte)
            return ('<%s%s>%s</%s> <%s%s>%s</%s>' % (tag, _avec_titre(attrs, _titre_socle(doms)), gauche, tag,
                                                      tag, _avec_titre(attrs_sans_id, titre_crcn(codes, niveaux(_texte(droite)))),
                                                      droite, tag))
        if a_crcn:
            codes = [c for c, _, _ in chaine(texte, a_crcn.end())]
            if not codes:
                return m.group(0)                        # « CRCN » seul : à écrire à la main, avec ses compétences
            segs = segments(ancien)
            if all(not etages_manquants(c, segs.get(c, "")) for c in codes if c in CRCN):
                return m.group(0)                        # la bulle a ses trois étages : on n'y touche pas
            titre = titre_crcn(codes, niveaux(texte), ici_de(ancien, codes))
        elif socle:
            if all(norme(SOCLE_CLE.get(d, "§§§")) in norme(ancien) for d in doms):
                return m.group(0)
            titre = _titre_socle(doms)
        else:
            return m.group(0)
        if norme(titre) == norme(ancien):
            return m.group(0)
        changees.append(texte)
        return "<%s%s>%s</%s>" % (tag, _avec_titre(attrs, titre), contenu, tag)

    src = re.sub(r'<(span|a|li)(\s(?:[^>"]|"[^"]*")*)>(.*?)</\1>', une, src, flags=re.S)   # un « > » dans un attribut ne coupe pas la balise
    return src, changees


def nommer(src):
    src, ajouts = inserer_intitules(src)
    src, changees = etiquettes(src)
    return src, ajouts, changees


def main(args):
    voir = "--voir" in args
    pages = [a for a in args if a != "--voir"]
    if not pages:
        print(__doc__)
        return 2
    for chemin in pages:
        avant = open(chemin, encoding="utf-8").read()
        apres, ajouts, changees = nommer(avant)
        if apres == avant:
            print("  · %s — rien à écrire" % chemin)
            continue
        print("  %s %s — %d intitulé(s) écrit(s), %d étiquette(s) rendue(s) lisibles au survol"
              % ("👁" if voir else "✔", chemin, len(ajouts), len(changees)))
        if not voir:
            open(chemin, "w", encoding="utf-8").write(apres)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
