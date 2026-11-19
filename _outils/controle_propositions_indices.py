# -*- coding: utf-8 -*-
"""controle_propositions_indices.py — une question de séquence ne souffle pas sa réponse (audit de `3e_C4.1`, 17/11/2026).

LE CONSTAT
----------
L'audit externe de `3e_C4.1` du 17/11/2026 relève, dans les questions à boutons radio et les calculs de la séquence :
  · une bonne réponse qui porte sa propre justification — « moulage par injection (la série rentabilise le moule) »,
    face à « sculpture à la main » : l'élève reconnaît la phrase qui explique, il ne raisonne pas ;
  · des intrus qu'on élimine sans réfléchir (« carton compressé » pour un poteau en bord de mer) ;
  · une question qui affiche le résultat de la précédente : « 432 Wh ÷ 12 V = … Ah » sous la question qui demande
    les 432 Wh ;
  · une échelle d'auto-positionnement dans le désordre (fragile, en cours, expert, solide), sans dire ce que veut
    dire chaque niveau.
Le skill `propositions-sans-indice` en tire la méthode ; cet outil mesure ce qui se lit dans le source. `controle_longueurs.py`
et `controle_ordre_propositions.py` jugent déjà la longueur et la place de la bonne réponse ; `controle_indices_qcm.mjs`,
les mots des QCM.

CE QU'IL MESURE (pages élèves hors QCM et synthèses)
-----------------------------------------------------
  I1 ⚠  la bonne réponse est seule à porter une justification : une parenthèse de quatre mots ou plus, un « — » suivi
        d'une explication, un « car », « parce que », « puisque », « donc » ; quand toutes les propositions portent
        la leur (« 20 Ah — moins chère, ça devrait passer »), le choix porte sur l'argument : rien à signaler ;
        (19/11/2026) « parce que » et « puisqu' » sont lus comme justification : seuls « parce qu' » et « puisque » l'étaient,
        si bien qu'une bonne réponse en « parce qu'… » parmi des intrus en « parce que… » passait pour seule justifiée.
  I3 ⚠  le résultat attendu d'un calcul (`num("d2_1")===432`) se lit dans une étiquette ou une légende de la page,
        hors aides et corrections. Un champ dont la valeur se recopie d'un document de la page — un seuil du cahier des
        charges, une valeur lue dans le programme — n'est pas un calcul : il porte `data-donnee="cahier des charges"`
        (ou « programme »…) et I3 ne le lit pas (19/11/2026, `3e_C9.2` et `5e_C6.1`) ;
  I4 ✘  une échelle d'auto-positionnement (`positionnement`, ou un groupe `auto…` ou `pos1`, `pos2`… — ces derniers
         vus depuis le 19/11/2026 : 24 échelles de 10 pages étaient mélangées sans que l'outil les lise) dont les niveaux ne sont pas dans
        l'ordre ;
  I4 ⚠  une échelle dont les niveaux ne disent pas ce qu'ils veulent dire (aucun « — » après le niveau).

Les intrus trop faciles (I2) ne se mesurent pas : ils se lisent à voix haute, comme un élève qui n'a pas encore appris
(skill, étape 2).

  python3 _outils/controle_propositions_indices.py [page.html | dossier …] [--detail]

Sortie : 0 aucun ✘ · 1 une échelle dans le désordre (I4 ✘) · 2 aucune page lue (n°299).
"""
from __future__ import annotations

import html as H
import os
import re
import sys

OUT = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(OUT)
sys.path.insert(0, OUT)
import controle_ordre_propositions as COP  # noqa: E402

VALEUR_JS = re.compile(r"""\$\(\s*["'](\w+)["']\s*\)\.value\s*===?\s*"((?:[^"\\]|\\.)*)\"""")
JUSTIF = re.compile(r"\((?:[^()]*?\s){3,}[^()]*\)|\s[—–]\s+\S+(?:\s+\S+){2,}|\b(?:car|parce que?|puisque?|donc)\b", re.I)
NOMBRE_ATTENDU = [
    re.compile(r"""num\(\s*["'](\w+)["']\s*\)\s*===?\s*(\d+(?:[.,]\d+)?)\b"""),
    re.compile(r"""Math\.abs\(\s*num\(\s*["'](\w+)["']\s*\)\s*-\s*(\d+(?:[.,]\d+)?)\s*\)"""),
]
ETIQUETTE = re.compile(r"<(label|legend)\b[^>]*>(.*?)</\1>", re.S)
OPTION_ID = re.compile(r'<input type="radio"[^>]*\bid="([^"]+)__(\d+)"')


def texte(s: str) -> str:
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def sans_aides(src: str) -> str:
    """La page sans scripts, styles, aides ni corrections : ce que l'élève lit en répondant."""
    s = re.sub(r"<(script|style)\b.*?</\1>", "", src, flags=re.S)
    for _ in range(3):
        s = re.sub(r'<details class="(?:aide|correction|corrige)[^"]*"[^>]*>(?:(?!<details).)*?</details>', "", s, flags=re.S)
    return s


def attendus(src: str) -> dict:
    att = COP.attendus(src)
    for k, v in VALEUR_JS.findall(src):
        att.setdefault(k, v.replace('\\"', '"'))
    return att


def analyser(src: str):
    out = []
    att, grp = attendus(src), COP.groupes(src)
    # I1 — la bonne réponse seule à porter sa justification
    for k, v in att.items():
        if k not in grp or v not in grp[k] or len(grp[k]) < 3:
            continue
        bonne = COP.longueur(v) and texte(v)
        autres = [texte(x) for x in grp[k] if x != v]
        if JUSTIF.search(bonne) and not any(JUSTIF.search(a) for a in autres):
            out.append(("⚠", "I1", "%s : « %s » est seule à porter sa justification" % (k, bonne[:70])))
    # I3 — le résultat attendu se lit dans une étiquette
    lu = sans_aides(src)
    etiquettes = [texte(m.group(2)) for m in ETIQUETTE.finditer(lu)]
    vus = set()
    for rx in NOMBRE_ATTENDU:
        for k, n in rx.findall(src):
            if len(n.replace(",", "").replace(".", "")) < 2 or (k, n) in vus:
                continue
            vus.add((k, n))
            # une donnée à recopier d'un document de la page (un seuil du cahier des charges, une valeur du
            # programme) n'est pas un résultat à calculer : son champ le dit par data-donnee="…"
            if re.search(r'<input\b[^>]*\bid="%s"[^>]*\bdata-donnee="' % re.escape(k), src):
                continue
            # une page découpée garde le script entier : un champ absent de la page ne s'y remplit pas
            if not re.search(r'\bid="%s"' % re.escape(k), src):
                continue
            motif = re.compile(r"(?<![\d,.])%s(?![\d,])" % re.escape(n.replace(".", ",")) + "|" + r"(?<![\d,.])%s(?![\d.])" % re.escape(n))
            for e in etiquettes:
                if motif.search(e):
                    out.append(("⚠", "I3", "le résultat attendu de %s (%s) se lit dans « %s »" % (k, n, e[:80])))
                    break
    # I4 — l'échelle d'auto-positionnement
    for m in COP.FIELDSET.finditer(src):
        classes, fid, corps = m.group(1), m.group(2), m.group(4)
        if "positionnement" not in classes and not fid.startswith("auto") and not re.match(r"pos\d", fid):
            continue
        rangs = [int(r) for i, r in OPTION_ID.findall(corps) if i == fid]
        if rangs and rangs != sorted(rangs):
            out.append(("✘", "I4", "%s : les niveaux sont dans le désordre (%s)" % (fid, ", ".join(map(str, rangs)))))
        libelles = [texte(x) for x in re.findall(r"<label[^>]*>(.*?)</label>", corps, re.S)]
        if libelles and not any(re.search(r"\s[—–]\s", x) for x in libelles):
            out.append(("⚠", "I4", "%s : les niveaux ne disent pas ce qu'ils veulent dire" % fid))
    return out


def main(argv):
    detail = "--detail" in argv
    chemins = [a for a in argv if not a.startswith("--")]
    ps = []
    for c in chemins or [os.path.join(DEPOT, t) for t in sorted(os.listdir(DEPOT)) if t.startswith("theme-")]:
        ps += [c] if os.path.isfile(c) else list(COP.pages_html(c))
    if not ps:
        print("✘ aucune page lue : rien n'a été vérifié")
        return 2
    compte, refus, avec = {}, 0, 0
    for p in sorted(ps):
        src = open(p, encoding="utf-8").read()
        res = analyser(src)
        if res:
            avec += 1
        for g, code, msg in res:
            compte[(g, code)] = compte.get((g, code), 0) + 1
            refus += g == "✘"
            if g == "✘" or detail:
                print("  %s %s %s — %s" % (g, code, os.path.relpath(p, DEPOT), msg))
    resume = " · ".join("%s %s : %d" % (g, c, k) for (g, c), k in sorted(compte.items()))
    print("%d page(s) lues · %d page(s) à revoir · %s" % (len(ps), avec, resume or "rien à signaler"))
    if not detail and any(g == "⚠" for g, _ in compte):
        print("  (⚠ : une mesure ; --detail les nomme page par page)")
    return 1 if refus else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
