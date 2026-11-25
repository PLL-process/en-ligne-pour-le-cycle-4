# -*- coding: utf-8 -*-
"""controle_verification_execute.py — une vérification de programme juge ce qu'il FAIT, pas ce qu'il ÉCRIT
(règle d'or n°333, mesurée sur tout le site le 22/11/2026).

LE CONSTAT
----------
« Programmer l'alerte » (3e_C6.1), audit externe du 21/11/2026 : le bouton « Vérifier » de l'activité 4 cherchait
sept motifs dans le TEXTE du programme. La version 2 juste, écrite avec des apostrophes au lieu des guillemets,
obtenait 5 / 7 et un message qui disait « branches incomplètes » ; la même version avec `>=` au seuil de 118 — fausse
précisément à la frontière que la séquence apprend à tester — obtenait 7 / 7. La règle d'or n°333 (14/11/2026) disait
déjà « on compare le comportement, pas le texte du programme » ; aucun outil ne la mesurait hors des bancs de lot, et la
séquence, antérieure à la règle, n'avait jamais été remise à l'aune.

LA RÈGLE MESURÉE
----------------
Dans une page qui donne à l'élève un éditeur de code (CodeLab `#clTa`, éditeur Python intégré `.editeur-py`), les
vérifications (`const CHECKS = {…}`) qui lisent le programme de l'élève l'EXÉCUTENT (`EditeurPython.executer`,
`BancPython.executer`, ou une fonction de la page qui les appelle) et comparent ses sorties. Chercher un motif dans le
texte (`.test(code)`, `code.includes(…)`, `code.indexOf(…)`, `code.match(…)`, `code.search(…)`) n'est permis que pour
un conseil de forme annoncé comme tel, dans une fonction dont le nom commence par `conseil` (« il ne compte pas »).

Classement de chaque page à éditeur :
  ✔ X  les vérifications exécutent le programme, sans motif dans son texte (hors conseil de forme) ;
  ⚠ M  elles exécutent ET cherchent des motifs dans le texte (à relire : le motif décide-t-il du verdict ?) ;
  ✘ T  elles cherchent des motifs dans le texte sans jamais l'exécuter (défaut n°333) ;
  ○ N  l'éditeur existe, mais aucune vérification ne lit le programme (rien à juger ici).

CE QU'IL VOIT AUSSI DEPUIS LE 25/11/2026 (mesure de départ du 22/11 : 3 X · 4 N)
---------------------------------------------------------------------------
Les quatre pages ○ N ne l'étaient pas pour la même raison. Deux juges y exécutaient le programme sans que le contrôle
les voie : un écouteur `editeur-py:fin` qui range le résultat (`window.__lamp = e.detail`, 4e_C9.1) ou qui fait
rejouer le programme par une fonction qui exécute (le banc-eleve). Ailleurs, le verrou s'ouvrait sur N'IMPORTE QUELLE
sortie : `print("x")` validait l'activité 3b de 3e_C7.1 et de 5e_C7.1. Et l'éditeur de l'activité 3 de 4e_C9.1, où
l'élève écrit sa décision, n'était nommé par aucune vérification. Le contrôle dit donc maintenant, page par page :
  ⚠ verrou à relire  une sortie non vide (`.trim()`, `/./`) ou une exécution sans erreur suffit à l'ouvrir ;
  ○ éditeur qu'aucune vérification ne juge  un éditeur d'activité que ni CHECKS, ni un écouteur, ni BANC_ELEVE ne
                     nomme (les éditeurs d'échauffement, `.editeur-py-essai`, ne comptent pas) ;
  · éditeur du Bonus sans banc  compté à part : un Bonus est facultatif, un corrigé suffit (avec --detail).
Mesure du 25/11/2026, après le lot : 7 X · 0 verrou faible · 0 éditeur d'activité sans jugement · 2 Bonus sans banc.

CE QU'IL NE SAIT PAS VOIR (n°47, n°146)
---------------------------------------
Une vérification écrite hors de `const CHECKS` ; un éditeur sans identifiant connu ; un motif caché derrière deux
fonctions ; si un motif sert seulement à un message et pas au verdict (classé M, à juger à la main) ; la justesse de ce
que compare l'exécution (un verrou à motif fixe sur la sortie, comme « Humidité du sol », n'est pas signalé : il peut
convenir à un programme DONNÉ qu'on exécute seulement). Il ne lit ni les scripts communs (`_ressources-communes`, `_outils`), ni les archives.

RÉFÉRENCE (n°273) : mesure de départ du 22/11/2026, écrite au journal ; la liste peut rétrécir, jamais grandir.

Sortie : 0 aucune page ✘ T (ou mesure sans --strict) · 1 au moins une page ✘ T avec --strict · 2 EN PANNE (aucune
page à éditeur lue, n°299).
Usage : python3 _outils/controle_verification_execute.py [chemins…] [--detail] [--strict]
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THEMES = ("theme-1-objets-systemes-usages-interactions", "theme-2-structure-fonctionnement-comportement",
          "theme-3-creation-conception-realisation-innovations")
IGNORES = {".git", "node_modules", "_archive-anciennes-versions"}

EXECUTEURS = re.compile(r"\b(?:EditeurPython\s*\.\s*executer|BancPython\s*\.\s*executer|Sk\s*\.\s*importMainWithBody|"
                        r"pyodide\s*\.\s*runPython)\s*\(")
# blocs posés depuis une source unique : on ne les lit pas comme du code de la page
BLOCS_POSES = re.compile(r"<!--\s*([a-z0-9-]+) v[\d.]+ : début.*?<!--\s*\1 v[\d.]+ : fin\s*-->", re.S)


def editeurs(html):
    """Les identifiants des zones de code données à l'élève."""
    ids = set()
    if re.search(r'id\s*=\s*"clTa"', html):
        ids.add("clTa")
    for m in re.finditer(r'<textarea[^>]*class\s*=\s*"[^"]*editeur-py-code[^"]*"[^>]*>', html):
        i = re.search(r'id\s*=\s*"([^"]+)"', m.group(0))
        if i:
            ids.add(i.group(1))
    for m in re.finditer(r'<textarea[^>]*id\s*=\s*"([^"]+)"[^>]*class\s*=\s*"[^"]*editeur-py-code', html):
        ids.add(m.group(1))
    return ids


def blocs(html):
    """(bloc, champ) de chaque éditeur Python intégré d'activité ; l'éditeur d'échauffement (.editeur-py-essai), qui
    n'exerce que les gestes, n'est pas compté."""
    out = []
    for m in re.finditer(r'<div[^>]*class\s*=\s*"editeur-py(?:\s[^"]*)?"[^>]*>', html):
        if "editeur-py-essai" in m.group(0):
            continue
        b = re.search(r'id\s*=\s*"([^"]+)"', m.group(0))
        t = re.search(r'<textarea[^>]*class\s*=\s*"[^"]*editeur-py-code[^"]*"[^>]*>', html[m.end():m.end() + 6000])
        c = re.search(r'id\s*=\s*"([^"]+)"', t.group(0)) if t else None
        f = re.search(r'data-fichier\s*=\s*"([^"]*)"', m.group(0))
        sec = re.findall(r"<section\b[^>]*>", html[:m.start()])
        bonus = bool(f and "bonus" in f.group(1).lower()) or bool(sec and "bonus" in sec[-1].lower())
        out.append((b.group(1) if b else None, c.group(1) if c else None, bonus))
    return out


def scripts(html):
    html = BLOCS_POSES.sub("", html)
    return "\n".join(m.group(1) for m in re.finditer(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html, re.S))


def bloc_accolades(js, debut):
    """Le texte entre l'accolade ouvrante qui suit `debut` et sa fermante (chaînes et commentaires sautés)."""
    i = js.find("{", debut)
    if i < 0:
        return ""
    prof, j, n = 0, i, len(js)
    while j < n:
        c = js[j]
        if c in "\"'`":
            q, j = c, j + 1
            while j < n and js[j] != q:
                j += 2 if js[j] == "\\" else 1
        elif js.startswith("//", j):
            j = js.find("\n", j)
            if j < 0:
                break
        elif js.startswith("/*", j):
            j = js.find("*/", j)
            if j < 0:
                break
            j += 1
        elif c == "{":
            prof += 1
        elif c == "}":
            prof -= 1
            if prof == 0:
                return js[i:j + 1]
        j += 1
    return js[i:]


def fonctions(js):
    """{nom: corps} des fonctions déclarées dans la page (function nom(…){…} et const nom = (…) => {…})."""
    out = {}
    for m in re.finditer(r"\bfunction\s+([A-Za-z_$][\w$]*)\s*\(", js):
        out[m.group(1)] = bloc_accolades(js, m.end())
    for m in re.finditer(r"\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*(?:function\b[^(]*)?\([^)]*\)\s*(?:=>)?\s*\{", js):
        out.setdefault(m.group(1), bloc_accolades(js, m.end() - 1))
    return out


def lecture_de(ident):
    """Lire la valeur d'une zone : $("id").value, ($("id") || {}).value, getElementById, querySelector("#id")."""
    q = re.escape(ident)
    return (r"""(?:\$|document\s*\.\s*getElementById)\(\s*["']%s["']\s*\)(?:\s*\|\|\s*\{\s*\}\s*\))?\s*\.\s*value|"""
            r"""document\s*\.\s*querySelector\(\s*["']#%s["']\s*\)\s*\.\s*value""" % (q, q))


def appels(corps, noms):
    return {n for n in noms if re.search(r"(?<![\w$.])%s\s*\(" % re.escape(n), corps)}


def motifs(corps, lecture, lecteurs):
    """Les motifs cherchés dans le texte du programme : sur une lecture directe, ou sur une variable qui la reçoit
    (directement, ou par une fonction de la page qui lit l'éditeur)."""
    source = lecture + ("|" + "|".join(r"(?<![\w$.])%s\s*\([^()]*\)" % re.escape(n) for n in lecteurs) if lecteurs else "")
    noms = set(re.findall(r"\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*\(?\s*(?:%s)" % source, corps))
    noms |= set(re.findall(r"[,{]\s*([A-Za-z_$][\w$]*)\s*=\s*\(?\s*(?:%s)" % source, corps))
    cibles = [lecture] + [r"\b%s\b" % re.escape(n) for n in noms]
    vus = []
    for c in cibles:
        for m in re.finditer(r"(?:%s)\s*\.\s*(?:includes|indexOf|match|search|startsWith|endsWith)\s*\(" % c, corps):
            vus.append(m.group(0)[:60])
        for m in re.finditer(r"\.test\(\s*(?:%s)\s*\)" % c, corps):
            vus.append(m.group(0)[:60])
    return vus


def juger(html):
    ids = editeurs(html)
    if not ids:
        return None
    js = scripts(html)
    lecture = "|".join(lecture_de(i) for i in sorted(ids))
    fx = fonctions(js)
    noms = set(fx)
    lit = {n: {i for i in ids if re.search(lecture_de(i), c)} for n, c in fx.items()}
    appelle = {n: appels(c, noms - {n}) for n, c in fx.items()}
    executeur = {n for n, c in fx.items() if EXECUTEURS.search(c)}
    for _ in range(4):   # transitivité : qui lit (par une autre fonction), qui exécute (par une autre fonction)
        for n in fx:
            for g in appelle[n]:
                lit[n] |= lit[g]
                if g in executeur:
                    executeur.add(n)
    m = re.search(r"\bconst\s+CHECKS\s*=\s*", js)
    checks = bloc_accolades(js, m.end()) if m else ""
    appeles = appels(checks, noms)
    for _ in range(4):
        appeles |= {g for n in list(appeles) for g in appelle[n]}
    lus = {i for i in ids if re.search(lecture_de(i), checks)} | {i for n in appeles for i in lit[n]}
    # l'éditeur Python intégré prévient par l'événement « editeur-py:fin » APRÈS une exécution : une preuve qu'un
    # écouteur range dans window.__exp, puis que CHECKS relit, est une preuve d'exécution
    evt_vus, evt, faibles = [], False, []
    # tout ce que lisent les vérifications : CHECKS et les fonctions qu'il appelle (transitivement)
    lu_par_checks = checks + "\n".join(fx[n] for n in sorted(appeles))
    for mm in re.finditer(r"""addEventListener\(\s*["']editeur-py:fin["']""", js):
        corps = bloc_accolades(js, mm.end())
        cles = set(re.findall(r"__exp\s*\.\s*([\w$]+)\s*=(?!=)", corps))
        # (25/11/2026) une clé calculée, « __exp[d.bloc] = … » : les blocs sont ceux que l'écouteur nomme entre guillemets
        if re.search(r"__exp\s*\[[^\]]+\]\s*=(?!=)", corps):
            cles |= set(re.findall(r"""["']([\w$-]+)["']""", corps)) | set(re.findall(r"[{,]\s*([\w$]+)\s*:", corps))
        relu = checks and any(re.search(r"__exp\s*\.\s*%s\b" % re.escape(k), lu_par_checks) for k in cles)
        # (25/11/2026) l'écouteur range le résultat de l'exécution (e.detail) dans une variable que les vérifications
        # relisent — 4e_C9.1, « window.__lamp = e.detail », jugé par lampJuger(window.__lamp)
        ranges = set(re.findall(r"(?:window\s*\.\s*)?([\w$]+)\s*=(?!=)\s*e\s*\.\s*detail\b", corps)) - {"d", "r"}
        relu = relu or (checks and any(re.search(r"\b%s\b" % re.escape(k), lu_par_checks) for k in ranges))
        # (25/11/2026) l'écouteur fait REJOUER le programme par une fonction de la page qui l'exécute (banc-eleve) et
        # range son verdict dans __exp, que les vérifications relisent
        rejoue = bool(appels(corps, executeur) or EXECUTEURS.search(corps))
        relu = relu or (checks and rejoue and "__exp" in lu_par_checks)
        if relu:
            evt = True
            # à relire : un verrou que suffit à ouvrir une sortie non vide, ou une exécution sans erreur
            if not rejoue and (cles or "__exp" in corps) and not ranges and (
                    "sortie" not in corps or re.search(r"sortie[^;]*\.\s*trim\(\)", corps) or "/./" in corps):
                faibles.append(re.sub(r"\s+", " ", corps)[:90])
            for c2 in re.finditer(r"(?:\b[\w$]+\.(?:detail\.)?code)\s*\.\s*(?:includes|indexOf|match|search|startsWith|endsWith)\s*\(|\.test\(\s*\b[\w$]+\.(?:detail\.)?code\s*\)", corps):
                evt_vus.append("écouteur editeur-py:fin : " + c2.group(0)[:50])
    # (25/11/2026) chaque éditeur d'activité est-il nommé par ce qui juge ? (CHECKS et ses fonctions, les écouteurs
    # editeur-py:fin, la table BANC_ELEVE) — 4e_C9.1 : l'éditeur de l'activité 3 n'était nommé nulle part
    juge_txt = lu_par_checks + "\n".join(bloc_accolades(js, mm.end()) for mm in re.finditer(r"""addEventListener\(\s*["']editeur-py:fin["']""", js))
    mb = re.search(r"\bBANC_ELEVE\s*=\s*", js)
    if mb:
        juge_txt += "\n" + bloc_accolades(js, mb.end())
    nomme = lambda x: bool(x) and re.search(r"(?<![\w-])%s(?![\w-])" % re.escape(x), juge_txt)
    sans = ["%s (%s)" % (b, c) for b, c, bonus in blocs(html) if not bonus and not (nomme(b) or nomme(c))]
    bonus_libres = ["%s (%s)" % (b, c) for b, c, bonus in blocs(html) if bonus and not (nomme(b) or nomme(c))]
    if evt and not lus:
        classe = "M" if evt_vus else "X"
        return {"classe": classe, "editeurs": sorted(ids), "motifs": evt_vus, "execute": True, "faibles": faibles, "sans_jugement": sans, "bonus_libres": bonus_libres}
    if not checks or not lus:
        return {"classe": "N", "editeurs": sorted(ids), "motifs": [], "execute": False, "faibles": faibles, "sans_jugement": sans, "bonus_libres": bonus_libres}
    lecteurs = {n for n in fx if lit[n] and not n.startswith("conseil")}
    # chaque vérification à part : une variable « e » de l'activité 5 n'est pas celle de l'activité 4
    membres = [bloc_accolades(checks, mm.end() - 1) for mm in
               re.finditer(r"(?:^|[,{])\s*[\w$\"']+\s*(?::\s*(?:function\s*)?\([^)]*\)\s*(?:=>\s*)?|\([^)]*\)\s*)\{", checks[1:])]
    vus = [x for corps in (membres or [checks]) for x in motifs(corps, lecture, lecteurs)]
    for nom in sorted(appeles):
        if nom.startswith("conseil"):
            continue
        vus += ["%s() : %s" % (nom, x) for x in motifs(fx[nom], lecture, lecteurs - {nom})]
    # exécuté : CHECKS exécute, ou la page exécute ailleurs le programme d'un éditeur que CHECKS lit
    executes = set(lus) if (EXECUTEURS.search(checks) or appeles & executeur) else set()
    for n in executeur:
        executes |= lit[n]
    execute = bool(lus & executes) or evt
    vus += evt_vus
    classe = "X" if execute and not vus else "M" if execute else "T" if vus else "N"
    return {"classe": classe, "editeurs": sorted(ids), "motifs": vus, "execute": execute, "faibles": faibles, "sans_jugement": sans, "bonus_libres": bonus_libres}


def pages(chemins):
    if not chemins:
        chemins = [os.path.join(RACINE, t) for t in THEMES]
    for c in chemins:
        if os.path.isfile(c) and c.endswith(".html"):
            yield c
            continue
        for d, sous, fichiers in os.walk(c):
            sous[:] = [s for s in sous if s not in IGNORES and not s.startswith("_")]
            for f in sorted(fichiers):
                if f.endswith(".html"):
                    yield os.path.join(d, f)


def main(argv):
    detail, strict = "--detail" in argv, "--strict" in argv
    chemins = [a for a in argv if not a.startswith("--")]
    lues, res = 0, []
    for p in pages(chemins):
        try:
            html = open(p, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            continue
        lues += 1
        j = juger(html)
        if j:
            res.append((os.path.relpath(p, RACINE), j))
    print("Vérifier un programme, c'est l'exécuter (règle d'or n°333) — %d page(s) lues, %d avec un éditeur de code" % (lues, len(res)))
    if not res:
        print("✘ EN PANNE : aucune page à éditeur de code lue — ce contrôle n'a rien vérifié (n°299).")
        return 2
    signes = {"X": "✔ X", "M": "⚠ M", "T": "✘ T", "N": "○ N"}
    compte = {k: 0 for k in signes}
    for chemin, j in res:
        compte[j["classe"]] += 1
        if detail or j["classe"] in ("T", "M") or j["faibles"] or j["sans_jugement"]:
            print("  %s %s" % (signes[j["classe"]], chemin))
            for v in j["motifs"][:6]:
                print("        motif dans le texte : %s" % v)
            for v in j["sans_jugement"]:
                print("        ○ éditeur qu'aucune vérification ne juge : %s" % v)
            for v in (j["bonus_libres"] if detail else []):
                print("        · éditeur du Bonus sans banc (facultatif : un corrigé suffit) : %s" % v)
            for v in j["faibles"][:3]:
                print("        ⚠ verrou à relire — une sortie non vide ou une exécution sans erreur l'ouvre : %s…" % v)
    print("\n%d ✔ X exécutent · %d ⚠ M exécutent et cherchent des motifs · %d ✘ T motifs seuls · %d ○ N sans vérification du code"
          % (compte["X"], compte["M"], compte["T"], compte["N"]))
    ns = sum(len(j["sans_jugement"]) for _, j in res)
    nb = sum(len(j["bonus_libres"]) for _, j in res)
    print("%d éditeur(s) d'activité qu'aucune vérification ne juge · %d éditeur(s) de Bonus sans banc (facultatifs ; "
          "les éditeurs d'échauffement ne comptent pas)" % (ns, nb))
    nf = sum(1 for _, j in res if j["faibles"])
    print("%d page(s) à verrou faible : l'exécution est exigée, mais rien ne compare ses sorties au cahier des charges" % nf)
    if compte["T"] == 0:
        print("✅ aucune vérification ne juge un programme par son seul texte")
    print("NON LU : une vérification hors de `const CHECKS`, un motif qui ne décide pas du verdict (M : à juger à la main).")
    return 1 if (strict and compte["T"]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
