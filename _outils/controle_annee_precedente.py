# -*- coding: utf-8 -*-
"""Règle d'or n°304, sur toute la page : aucune phrase n'affirme ce que l'élève a fait une année précédente.

Pascal change de collège chaque année : il n'hérite jamais d'une classe qui a suivi ses séquences. « Tu as vu en 5e »,
« Rappel de 5e », « comme en 4e », « le lampadaire de 5e » sont donc faux pour presque tous ses élèves — et quand c'est
vrai, l'affirmation met en défaut celui qui ne l'a pas fait (Pascal, 21/09/2026 : l'élève « peut se sentir dévalorisé
ou stressé »).

`verif_regles_audit.py` (n°304) ne lit que le BLOC D'OUVERTURE, et `controle_question_seule.py` (S3) que l'énoncé et la
bonne réponse d'un QCM. Le 26/11/2026, en traitant 3e_C8.2, la page disait encore « Tu as déjà éprouvé des matériaux en
5e », « le protocole de 5e », « comme en 5e » — hors de l'ouverture, dans une proposition, dans un pourquoi. Ce
contrôle lit TOUT ce que l'élève lit.

PÉRIMÈTRE (règle n°47 — un contrôle déclare ce qu'il regarde)
-------------------------------------------------------------
Les pages lues par l'élève, hors archive, exports et générateurs : `sequence*.html`, `qcm*.html`,
`synthese_eleve*.html`, `atelier*.html`, `tp_*.html`, `entrainement*.html`, `miniquiz*.html`. Le niveau de la page
(5e, 4e, 3e) se lit dans son chemin ; une page sans niveau n'est pas lue (un atelier commun à trois niveaux ne peut pas
parler d'une année « précédente »). Le texte lu : le texte visible (sans `<script>`, `<style>`, commentaires), les
pourquoi des propositions (`data-pourquoi`), et les chaînes de la banque d'un QCM (`const QUESTIONS`).

CE QUI EST MESURÉ — une phrase qui nomme une année antérieure au niveau de la page (« 5e » sur une page de 4e ou de
3e ; « 6e » sur une page de 5e), ou « l'an dernier », et qui :
  A  s'adresse à l'élève au passé — « tu as vu », « tu avais », « tu recensais », « t'a appris », « tu connais déjà »,
     « souviens-toi » ;
  B  renvoie à cette année comme à un souvenir commun — « comme en 5e », « Rappel de 5e », « vu en 5e », « l'an
     dernier » ;
  C  donne un objet ou une séquence de cette année comme connu — « le lampadaire de 5e », « la serre de 4e », « la
     séquence de 4e », « le protocole de 5e ».

CE QUI EST PERMIS, et n'est pas compté (n°304, point 3) :
  · la forme prudente, dans la même phrase — « Tu as PEUT-ÊTRE déjà vu… ; SINON, le voici », « SI tu as déjà fait… » ;
  · une année nommée sans rien affirmer de l'élève — « En 5e on suit, en 4e on organise, en 3e on élabore », « au
    programme de 5e », un tableau de progression écrit au présent ;
  · un lien de rattrapage vers une ressource d'un autre niveau — « l'atelier de 4e « Le diagramme des interacteurs » »
    (point 4 : chaque compétence nommée offre un moyen de la rattraper) ;
  · un code de compétence (« 5e_C8.2 »), qui n'est pas une année.

NON LU, à relire : une affirmation sans année ni « tu » (« la classe a déjà construit… ») ; une séquence de la MÊME
année donnée comme faite (« comme en 3e_C9.1 ») — permise au conditionnel, elle se juge à la lecture ; la pertinence
du moyen de rattrapage.

Usage : python3 _outils/controle_annee_precedente.py [--muet] [chemin…]
Sortie : 0 aucune phrase en défaut · 1 au moins une · 2 rien lu (n°299 : un outil qui ne lit rien est en panne).
"""
from __future__ import annotations

import html
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = re.compile(r"^(?:sequence|qcm|synthese_eleve|atelier|cahier|tp_|entrainement|miniquiz)[^/]*\.html$")
NIVEAU = re.compile(r"(?:^|[/_])([345])e(?:[/_]|$)")

#: une année du collège, « 5e », « 5ᵉ », « 5ème », « 5<sup>e</sup> » (rendu « 5e ») ; pas un code (« 5e_C8.2 »)
ANNEE = re.compile(r"(?<![\w/.])([3-6])(?:e|ᵉ|ème)(?![\w_])(?!\s+(?:[Aa]venue|[Rr]ue|arrondissement|étage)\b)")
#: une personne de ce niveau n'est pas une année vécue (« un camarade de 6e », « les 4e de l'an dernier »)
PERSONNE = re.compile(r"(?:camarades?|élèves?|un|une|les|des|aux)\s+(?:de\s+)?$", re.I)
AN_DERNIER = re.compile(r"l['’]an(?:née)?\s+derni(?:er|ère)|l['’]an\s+passé", re.I)
#: « l'an dernier » ne fait défaut que si la phrase parle de l'élève : « le club a réparé la station l'an dernier »
#: raconte l'histoire de l'objet ; « l'an dernier tu recensais », « votre avis de l'an dernier » racontent l'élève
A_L_ELEVE = re.compile(r"\b(?:tu|te|t['’]|toi|ton|ta|tes|vous|votre|vos)\b", re.I)

PRUDENT = re.compile(r"\bpeut[- ]être\b|\bsi\s+tu\b|\bs['’]il\b|\bsinon\b|\bau cas où\b|\bsi\s+ta\s+classe\b", re.I)
#: A — l'élève, au passé ou dans un souvenir
A_TOI = re.compile(
    r"\btu\s+(?:as|avais)\s+(?:déjà\s+|bien\s+|tous?\s+)?[a-zà-ÿ]+|\btu\s+[a-zà-ÿ]{2,}(?:ais|ait)\b|"
    r"\bt['’](?:a|avait)\s+[a-zà-ÿ]+|\btu\s+(?:connais|sais)\s+déjà\b|\bsouviens[- ]toi\b|\btu\s+te\s+souviens\b|"
    r"\b(?:ton|ta|tes)\s+[a-zà-ÿ]+\s+(?:de|en)\s+[3-6](?:e|ᵉ|ème)\b", re.I)
#: B — l'année comme souvenir commun
B_SOUVENIR = re.compile(r"\bcomme\s+en\s+[3-6](?:e|ᵉ|ème)\b|\b[Rr]appel\s+(?:de\s+(?:la\s+)?)?[3-6](?:e|ᵉ|ème)\b|"
                        r"\b(?:vu|vue|vus|appris|fait|faite|rencontré)\s+en\s+(?:classe\s+de\s+)?[3-6](?:e|ᵉ|ème)\b",
                        re.I)
#: C — un objet ou une séquence de cette année, donné comme connu (« le lampadaire de 5e »)
C_OBJET = re.compile(r"\b(?:le|la|les|l['’]|du|des|au|aux|ce|cette|même)\s*([a-zà-ÿ'’-]+(?:\s+[a-zà-ÿ'’-]+)?)\s+de\s+"
                     r"(?:la\s+)?[3-6](?:e|ᵉ|ème)\b", re.I)
#: ce que C ne compte pas : le programme, un niveau, un moyen de rattrapage
C_PERMIS = re.compile(r"(?:^|\s)(?:programme|programmes|niveau|niveaux|classe|classes|cycle|atelier|ateliers|version|"
                      r"versions|parcours|progression|palier|élèves?|compétences?|attendus?|codes?|année|années|"
                      r"collège|fin|début|cours|professeur|carte|fiche|fiches|lexique|synthèse|capsule|"
                      r"exercices?|questions?|notion|notions|vocabulaire|repères?|spirale|TP|geste|gestes|verbe)$", re.I)


def niveau_de(rel: str):
    m = NIVEAU.search(rel.replace(os.sep, "/"))
    return int(m.group(1)) if m else None


def fichiers(chemins):
    for c in chemins or [DEPOT]:
        if os.path.isfile(c):
            yield c
            continue
        for d, _, fs in os.walk(c):
            dd = d.replace(os.sep, "/")
            if any(x in dd for x in ("_archive", "/.", "node_modules", "_exports", "_generation")):
                continue
            for f in sorted(fs):
                if PAGES.match(f):
                    yield os.path.join(d, f)


def texte_eleve(src: str) -> str:
    """Le texte que l'élève lit : la page sans scripts, les pourquoi, et la banque d'un QCM."""
    banque = ""
    i = src.find("const QUESTIONS")
    if i >= 0:
        j = src.find("];", i)
        banque = " ".join(m.group(1) for m in re.finditer(r'"((?:[^"\\]|\\.)*)"', src[i:j if j > 0 else None]))
        banque = re.sub(r"<sup>\s*(e|ème|ᵉ)\s*</sup>", r"\1", banque.replace('\\"', '"'))
        banque = re.sub(r"<[^>]+>", " ", banque)
    s = re.sub(r"<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->", " ", src, flags=re.S | re.I)
    pourquoi = " ".join(m.group(1) for m in re.finditer(r'data-pourquoi="([^"]*)"', s))
    s = re.sub(r"<sup>\s*(e|ème|ᵉ)\s*</sup>", r"\1", s)
    # une ligne de tableau se lit d'un trait (« 5e · Shenzhen · tu recensais… ») : ses cellules ne coupent pas la phrase
    s = re.sub(r"<tr\b.*?</tr>", lambda m: re.sub(r"<br\s*/?>", " ", m.group(0), flags=re.I), s, flags=re.S | re.I)
    s = re.sub(r"<(?:td|th)\b[^>]*>", " · ", s, flags=re.I)
    s = re.sub(r"<(?:br|p|li|h[1-6]|tr|div|section|summary|legend|label|figcaption)\b[^>]*>", " . ", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    t = html.unescape(s + " . " + pourquoi + " . " + banque)
    return re.sub(r"\s+", " ", t.replace(" ", " ").replace(" ", " "))


def phrases(t: str):
    return [p.strip() for p in re.split(r"(?<=[.!?;:])\s+(?=[A-ZÀ-Ý«\"“0-9✘•·①-⑩—-])|\s\.\s", t) if p.strip()]


def juger(phrase: str, niveau: int):
    """La raison du refus (A, B ou C, et le passage), ou None."""
    anterieure = [m for m in ANNEE.finditer(phrase)
                  if int(m.group(1)) > niveau and not PERSONNE.search(phrase[max(0, m.start() - 16):m.start()])]
    dernier = AN_DERNIER.search(phrase)
    if dernier and not A_L_ELEVE.search(phrase):
        dernier = None
    if not anterieure and not dernier:
        return None
    if PRUDENT.search(phrase):
        return None
    if dernier:
        return "B", dernier.group(0)
    m = B_SOUVENIR.search(phrase)
    if m and int(re.search(r"\d", m.group(0)).group(0)) > niveau:
        return "B", m.group(0)
    m = A_TOI.search(phrase)
    if m:
        return "A", m.group(0)
    for m in C_OBJET.finditer(phrase):
        an = int(re.search(r"(\d)(?:e|ᵉ|ème)\b", m.group(0)).group(1))
        if an <= niveau or C_PERMIS.search(m.group(1).strip()):
            continue
        return "C", m.group(0)
    return None


def lire(p: str):
    rel = os.path.relpath(p, DEPOT)
    niveau = niveau_de(rel)
    if not niveau:
        return rel, None, []
    t = texte_eleve(open(p, encoding="utf-8", errors="replace").read())
    vus, out = set(), []
    for ph in phrases(t):
        j = juger(ph, niveau)
        if j and ph not in vus:
            vus.add(ph)
            out.append((j[0], j[1], ph[:220]))
    return rel, niveau, out


def main(argv) -> int:
    muet = "--muet" in argv
    chemins = [a for a in argv if not a.startswith("--")]
    lues, defauts = 0, []
    for p in fichiers(chemins):
        rel, niveau, out = lire(p)
        if niveau is None:
            continue
        lues += 1
        defauts += [(rel, *o) for o in out]
    if not lues:
        print("✘ rien n'a été lu : aucune page d'élève de 5e, de 4e ou de 3e dans le périmètre")
        return 2
    if not muet:
        for rel, code, passage, ph in defauts:
            print("  ✘ %s %s\n      « %s » — %s" % (code, rel, passage, ph))
    if defauts:
        print("⛔ %d phrase(s) affirment une année que l'élève n'a peut-être pas faite (n°304), sur %d page(s) lue(s) · "
              "A au passé : %d · B souvenir commun : %d · C objet donné comme connu : %d"
              % (len(defauts), lues, *[sum(1 for d in defauts if d[1] == c) for c in "ABC"]))
        return 1
    print("✅ %d page(s) d'élève lue(s) : aucune phrase n'affirme une année que l'élève n'a peut-être pas faite (n°304)"
          % lues)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
