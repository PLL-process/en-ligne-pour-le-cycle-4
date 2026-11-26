# -*- coding: utf-8 -*-
"""controle_bonus_corrige.py — chaque défi du Bonus a son corrigé, et le titre annonce le bon nombre de défis.

LA RÈGLE
--------
Règle d'or n°4 (bloc élève obligatoire) et n°301 : le Bonus porte ses champs de réponse **et son corrigé**.
Demande de Pascal du 25/11/2026 : « assure-toi […] qu'il y ait la correction ».

Mesure du 25/11/2026, avant correction (86 pages closes par un Bonus) : 14 n'avaient aucun corrigé (B1), 3 autres
laissaient sept défis sans le leur (B2), et 25 titres repliés annonçaient un nombre de défis faux (B3 : « Les 4 défis
du Bonus » pour trois, « Le défi du Bonus » pour quatre) — `replier_bonus.py` comptait les lignes de la version
étayée, ou les champs de réponse, pas les défis. Après correction : 0, 0, 0.

CE QU'IL MESURE
---------------
  B1  le Bonus porte au moins un corrigé (`<details class="correction…">`, ou un volet dont le titre dit « Corrigé »
      ou « Correction ») ;
  B2  quand les défis sont nommés (« Défi carte : », « 1. », « Citoyen : »…), chacun est suivi de son corrigé avant
      le défi suivant — ou le Bonus porte un corrigé d'ensemble (« Corrigé du Bonus ») ;
  B3  le titre replié « Les N défis du Bonus » annonce le nombre de défis nommés ; « Le défi du Bonus » n'en couvre
      qu'un.

CE QU'IL NE LIT PAS
-------------------
Que le corrigé soit juste, complet et aéré : cela se lit (skill `texte-clair-et-aere`, `controle_correction_complete`).
Un défi d'évaluation, volontairement sans corrigé public, se déclare par `data-sans-corrige="<raison>"` sur son bloc.

Sortie : 0 conforme · 1 écart(s) · 2 rien lu (règle n°299).
Usage : python3 _outils/controle_bonus_corrige.py [--detail] [pages…]
Banc  : python3 _outils/tests_controle_bonus_corrige.py        (27 / 27 au 25/11/2026)
Titre : python3 _outils/replier_bonus.py --titres <pages…> --ecrire   recompte et réécrit un titre faux
"""
import glob
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TITRE = re.compile(r"<h([23])\b[^>]*>(?:(?!</h\1>).)*?Bonus(?:(?!</h\1>).)*?facultatif(?:(?!</h\1>).)*?</h\1>", re.S | re.I)
VOLET = re.compile(r"<details\b([^>]*)>\s*<summary\b[^>]*>(.*?)</summary>", re.S | re.I)
NU = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h).replace("&nbsp;", " ")).strip()
# le début d'un défi : un paragraphe, un item ou un intertitre qui s'ouvre sur un libellé en gras
LIBELLE = re.compile(
    r"<(p|li|h3|h4)\b[^>]*>\s*(?:[^\w<&]{0,8}\s*)?(?:<(b|strong)\b[^>]*>\s*(?:[^\w<&]{0,8}\s*)?)?"
    r"(D[ée]fi\b[^<:.]{0,60}|\d{1,2}\s*\.|Citoyen|Technique|New\s*York|Ancrage\b[^<:.]{0,40}|CRCN\b[^<:]{0,40})"
    r"\s*(?:&nbsp;|\s)*[:.—-]?", re.I)


def fin_bloc(s, debut, balise):
    """la fin du bloc <balise> ouvert en `debut` (les blocs s'emboîtent)"""
    n = 0
    for m in re.finditer(r"<(/?)%s\b[^>]*>" % balise, s[debut:], re.I):
        n += -1 if m.group(1) else 1
        if n == 0:
            return debut + m.end()
    return -1


def bonus_etendue(s):
    """(début, fin) du bloc Bonus de l'élève dans la page, ou None : la <section> qui s'ouvre sur le titre
    « 🎁 Bonus (facultatif…) » — jamais un aparté du professeur, jamais un titre repris dans un <summary>"""
    for t in TITRE.finditer(s):
        k = s.rfind("<section", 0, t.start())
        if k < 0 or s[k:t.start()].count("<details") > s[k:t.start()].count("</details"):
            continue
        fin = fin_bloc(s, k, "section")
        if fin > 0:
            return t.end(), fin
    return None


def bonus(s):
    e = bonus_etendue(s)
    return s[e[0]:e[1]] if e else None


def sans_accent(t):
    return (t.lower().replace("é", "e").replace("è", "e").replace("ê", "e").replace("à", "a").replace("ç", "c")
            .replace("ô", "o").replace("î", "i").replace("û", "u"))


def cle(nom):
    """le mot qui distingue un défi : « Défi carte » → carte ; « Citoyen » → citoyen ; « 2. » → 2"""
    n = re.match(r"\s*(\d{1,2})\s*\.", nom)
    if n:
        return n.group(1)
    mots = [m for m in re.findall(r"[\w'’-]+", sans_accent(re.sub(r"^\s*d[ée]fi\b", "", nom, flags=re.I))) if len(m) > 2]
    return mots[0] if mots else sans_accent(nom)


def lire(bloc):
    """(défis, corrigés d'ensemble, corrigés en tout, nombre annoncé ou None, dispensé)
    défis : [(libellé, a son corrigé)] dans l'ordre de la page"""
    dispense = 'data-sans-corrige="' in bloc
    annonce = None
    m = re.search(r"<summary\b[^>]*>([^<]*d[ée]fis?\s+du\s+Bonus[^<]*)</summary>", bloc, re.I)
    if m:
        n = re.search(r"Les\s+(\d+)\s+d[ée]fis", m.group(1), re.I)
        annonce = int(n.group(1)) if n else (1 if re.search(r"\bLe\s+d[ée]fi\s+du\s+Bonus\s*—", m.group(1), re.I) else None)
        bloc = bloc[:m.start()] + bloc[m.end():]
    # les volets : un corrigé laisse une marque à sa place, les autres (aides, version étayée) s'effacent
    ensemble = 0
    titres = []                                           # les titres des corrigés qui nomment leur défi
    sortie, i = [], 0
    while True:
        v = VOLET.search(bloc, i)
        if not v:
            sortie.append(bloc[i:])
            break
        fin = fin_bloc(bloc, v.start(), "details")
        if fin < 0:
            sortie.append(bloc[i:])
            break
        attrs, titre = v.group(1), NU(v.group(2))
        sortie.append(bloc[i:v.start()])
        if "bonus-replie" in attrs:                      # le volet replié du Bonus : on lit dedans
            i = v.end()
            continue
        if re.search(r'class="[^"]*\bcorr', attrs, re.I) or re.search(r"\bcorrig|\bcorrection|exemple de r[ée]ponse|bonne r[ée]ponse", titre, re.I):
            if re.search(r"\bBonus\b|\bdes\s+(?:\w+\s+)?d[ée]fis\b|exemple de r[ée]ponse|bonne r[ée]ponse", titre, re.I) \
                    and not re.search(r"\bdu\s+d[ée]fi\b", titre, re.I):
                ensemble += 1
                sortie.append("⟦ENSEMBLE⟧")
            else:
                titres.append(sans_accent(titre))
                sortie.append("⟦CORR⟧")
        i = fin
    net = "".join(sortie).replace("</details>", "")
    # un corrigé peut aussi être un bloc que la vérification découvre (<div class="correction-box" hidden>)
    net, n_blocs = re.subn(r'<(?:div|section|aside)\b[^>]*class="[^"]*\bcorr[^"]*"[^>]*>', "⟦CORR⟧", net)
    total = ensemble + len(titres) + n_blocs
    departs = [(m.start(), NU(m.group(3))) for m in LIBELLE.finditer(net)]
    if not departs:                                       # des défis en liste, sans libellé (TP, 5e_C1.3)
        liste = re.search(r"<(ol|ul)\b[^>]*>(.*?)</\1>", net, re.S | re.I)
        if liste:
            departs = [(liste.start(2) + m.start(), "%d." % (k + 1))
                       for k, m in enumerate(re.finditer(r"<li\b", liste.group(2)))]
    if not departs:                                       # des défis que seuls leurs corrigés numérotent (5e_C1.5)
        nums = sorted({int(x) for t in titres for x in re.findall(r"\bdefi\s+(\d)\b", t)})
        if len(nums) > 1:
            return [("%d." % k, True) for k in nums], ensemble, total, annonce, dispense
    defis = []
    for n, (pos, nom) in enumerate(departs):
        fin = departs[n + 1][0] if n + 1 < len(departs) else len(net)
        k = cle(nom)
        nomme = any(re.search(r"\bdefi\s+%d\b" % (n + 1), t) or (not k.isdigit() and re.search(r"\b%s" % re.escape(k), t))
                    for t in titres)
        defis.append((nom, "⟦CORR⟧" in net[pos:fin] or nomme))
    return defis, ensemble, total, annonce, dispense


def juger(s):
    """[(code, message)] pour une page ; None si la page n'a pas de Bonus"""
    bloc = bonus(s)
    if bloc is None:
        return None
    defis, ensemble, total, annonce, dispense = lire(bloc)
    ecarts = []
    if not total and not dispense:
        ecarts.append(("B1", "le Bonus n'a aucun corrigé"))
    elif len(defis) > 1 and not ensemble and not dispense:
        sans = [nom for nom, ok in defis if not ok]
        if sans:
            ecarts.append(("B2", "sans corrigé : " + " · ".join(sans)))
    if annonce is not None and len(defis) > 1 and annonce != len(defis):
        ecarts.append(("B3", "le titre annonce %d défi(s), la page en nomme %d" % (annonce, len(defis))))
    if annonce is not None and annonce > 1 and len(defis) <= 1 and LIBELLE.search(bloc) is None:
        ecarts.append(("B3", "le titre annonce %d défis, la page n'en nomme aucun : compter à la main" % annonce))
    return ecarts


def pages():
    out = []
    for f in sorted(glob.glob(os.path.join(RACINE, "theme-*", "**", "*.html"), recursive=True)):
        if "_archive" in f or "/_generation/" in f or "/_modele/" in f or os.path.getsize(f) < 6000:
            continue
        out.append(f)
    return out


def main(argv):
    detail = "--detail" in argv
    choisies = [a for a in argv if not a.startswith("--")] or pages()
    lues = avec = 0
    ecarts = []
    for f in choisies:
        try:
            s = open(f, encoding="utf-8").read()
        except OSError:
            continue
        lues += 1
        r = juger(s)
        if r is None:
            continue
        avec += 1
        for code, msg in r:
            ecarts.append((os.path.relpath(f, RACINE), code, msg))
        if detail and not r:
            print("✔ %s" % os.path.basename(f))
    if not avec:
        print("⚠ aucune page avec un Bonus n'a été lue (%d page(s) ouvertes) : le contrôle n'a rien vérifié" % lues)
        return 2
    for f, code, msg in ecarts:
        print("✘ %s  %s\n     %s" % (code, f, msg))
    par = {c: sum(1 for e in ecarts if e[1] == c) for c in ("B1", "B2", "B3")}
    print("\n%d page(s) avec un Bonus · B1 sans corrigé : %d · B2 défi sans son corrigé : %d · B3 titre faux : %d"
          % (avec, par["B1"], par["B2"], par["B3"]))
    if ecarts:
        return 1
    print("✅ chaque Bonus a son corrigé, chaque défi nommé le sien, et le titre annonce le bon nombre")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
