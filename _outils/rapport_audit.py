#!/usr/bin/env python3
"""rapport_audit.py — l'état des lieux des trois thèmes, en un fichier, rejouable.

POURQUOI (07/11/2026)
---------------------
Pascal : « il faudrait un audit des trois thèmes ainsi qu'une boucle d'améliorations
possible sur tous les plans ». Le dépôt a déjà les outils qui mesurent (matrice de
couverture, `verif_regles_audit.py`, les contrôles de `_outils/`, les bancs, les
générateurs) ; il n'avait pas la page qui les lit tous ensemble et dit, par priorité, ce
qui reste à faire. Ce script l'écrit. Il ne corrige rien : il mesure, classe, et laisse
les décisions à Pascal (liste à cocher en fin de rapport).

CE QU'IL LIT
------------
  1. Couverture : `audit_couverture.csv` (statut par code et par thème, anomalies notées,
     preuves manquantes).
  2. Règles d'or : `verif_regles_audit.py`, relancé ; les ✘ sont comptés par règle et par
     page. Un ✘ n'est pas forcément un défaut de la page : quand une règle tombe sur toute
     une famille de pages faites au même gabarit, c'est souvent le CONTRÔLE qui est en
     retard sur une règle plus récente (vu le 07/11 : la n°300 refuse les menus déroulants
     que la n°317 impose dans un cahier des charges). Le rapport le signale ; le crible
     « vrai défaut / contrôle périmé » reste un jugement, écrit à la main dans la section
     « Crible » quand quelqu'un l'a fait.
  3. Contrôles du site : les `controle_*.py` (rapides) et, avec `--complet`, les `.mjs`
     (Playwright, longs). Chaque contrôle : code de sortie, dernière ligne, non exécuté
     si absent ou en panne (règle n°299 : on ne déclare que ce qui a tourné).
  4. Preuves des codes COUVERT : chaque code « couvert par une séquence mutualisée »
     doit avoir, dans le QCM du lot principal, au moins deux questions marquées de son code
     (`c:"C2.2"`). Zéro question = couvert sans preuve.
  5. Dérive des générateurs (avec `--generateurs`) : le dépôt est copié hors de git, les
     générateurs sûrs y sont relancés, et les fichiers qui diffèrent du dépôt sont listés
     — une page engendrée corrigée à la main sera écrasée à la prochaine régénération
     (vu le 07/11 sur les panneaux de la bête à cornes). `build_qcms.py` n'est jamais
     relancé (skill `qcm-html-accessible`).

PRIORITÉS
---------
  P1  ce qui empêche un élève ou Pascal d'utiliser une page : lien mort, page qui ne se
      lit pas hors ligne, fabrique visible, champ qui fait zoomer, squelette cassé ;
      un code À VÉRIFIER ou ABSENT ; un COUVERT sans preuve.
  P2  un ✘ de règle d'or non criblé, un code EXISTANT À AMÉLIORER, une dérive de
      générateur, un autre contrôle rouge.
  P3  les anomalies notées dans la matrice (poids d'images, provenance, différenciation…).

    python3 _outils/rapport_audit.py                      # rapide (≈ 5 min)
    python3 _outils/rapport_audit.py --complet            # + contrôles Playwright
    python3 _outils/rapport_audit.py --generateurs        # + dérive des générateurs
    python3 _outils/rapport_audit.py --sortie <fichier.md>
Sortie par défaut : docs/audits/RAPPORT_AUDIT_<AAAA-MM-JJ>.md
"""
import collections
import csv
import datetime as dt
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

RACINE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
THEMES = {"1": "theme-1-objets-systemes-usages-interactions",
          "2": "theme-2-structure-fonctionnement-comportement",
          "3": "theme-3-creation-conception-realisation-innovations"}

CONTROLES_PY = ["controle_liens.py", "controle_regles_visibles.py", "controle_tactile.py",
                "controle_hierarchie.py", "controle_mode_essentiel.py", "controle_debordement.py",
                "controle_competences.py", "controle_formulations.py", "controle_impression_papier.py",
                "controle_boutons_vivants.py", "controle_longueurs.py", "controle_regle4.py",
                "controle_medias.py", "controle_sigles.py", "controle_unites.py",
                "controle_fichiers_telechargeables.py", "controle_atteignabilite.py",
                "controle_rapports_tests.py", "controle_blocs_dessines.py", "controle_schemas.mjs"]
CONTROLES_MJS = ["controle_squelette.mjs", "controle_hors_ligne.mjs", "controle_impression.mjs",
                 "controle_verrous.mjs", "controle_contraste_liens.mjs", "controle_code_colore.mjs"]
#: un rouge ici empêche d'utiliser la page : P1
BLOQUANTS = {"controle_liens.py", "controle_regles_visibles.py", "controle_tactile.py",
             "controle_squelette.mjs", "controle_hors_ligne.mjs", "controle_medias.py"}

#: générateurs relancés sans danger dans une COPIE (jamais build_qcms.py)
GENERATEURS = [
    ("theme-1-objets-systemes-usages-interactions/ateliers-representations/_generation", "build.py"),
    ("theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-planification/_generation", "build_atelier.py"),
    ("theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-cao/_generation", "build_tp.py ../scenarios/tp_5e_de_onshape.json"),
    ("theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-cao/_generation", "build_tp.py ../scenarios/tp_5e_de_calottes.json"),
    ("theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-cao/_generation", "build_tp.py ../scenarios/tp_4e_socle_assemblage.json"),
    ("theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/atelier-cao/_generation", "build_tp.py ../scenarios/tp_3e_boitier_etanche.json"),
    ("theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2", "generer_les_quatre_pages.py"),
    (".", "_outils/generer_lexique.py --tous theme-1-objets-systemes-usages-interactions theme-2-structure-fonctionnement-comportement theme-3-creation-conception-realisation-innovations"),
]


def lancer(cmd, cwd=RACINE, timeout=1800):
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout,
                           env={**os.environ, "PLAYWRIGHT_BROWSERS_PATH": os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")})
        return p.returncode, (p.stdout + p.stderr)
    except subprocess.TimeoutExpired:
        return -1, "délai dépassé (%d s)" % timeout
    except FileNotFoundError as e:
        return -2, str(e)


# ── 1. couverture ───────────────────────────────────────────────────────────
def couverture():
    rows = list(csv.DictReader(open(os.path.join(RACINE, "audit_couverture.csv"), encoding="utf-8-sig"), delimiter=";"))
    par_theme = collections.defaultdict(collections.Counter)
    for r in rows:
        par_theme[r["theme"]][r["statut"]] += 1
    non_complets = [r for r in rows if not r["statut"].startswith("COMPLET")]
    anomalies = [r for r in rows if r.get("anomalies", "").strip()]
    return rows, par_theme, non_complets, anomalies


# ── 2. règles d'or ──────────────────────────────────────────────────────────
def regles_or():
    code, out = lancer([sys.executable, "_outils/verif_regles_audit.py"], timeout=1800)
    page = None
    par_regle = collections.defaultdict(list)       # règle -> [(page, message)]
    par_page = collections.defaultdict(set)
    for l in out.split("\n"):
        if ".html" in l and not l.strip().startswith(("✔", "✘", "·")):
            m = re.search(r"(theme-\S+?\.html)", l)
            if m:
                page = m.group(1)
        m = re.search(r"✘\s*(n°\d+)\s*([^ ].*?)\s{2,}(.*)$", l) or re.search(r"✘\s*(n°\d+)\s*(\S.*)$", l)
        if m and page:
            regle = m.group(1)
            msg = (m.group(3) if m.lastindex == 3 else m.group(2)).strip()
            par_regle[regle].append((page, msg))
            par_page[page].add(regle)
    return code, par_regle, par_page


# ── 3. contrôles du site ────────────────────────────────────────────────────
def controles(complet):
    res = []
    liste = CONTROLES_PY + (CONTROLES_MJS if complet else [])
    for c in liste:
        chemin = os.path.join(RACINE, "_outils", c)
        if not os.path.exists(chemin):
            res.append((c, None, "absent"))
            continue
        cmd = ["node", chemin] if c.endswith(".mjs") else [sys.executable, chemin]
        code, out = lancer(cmd, timeout=3600 if c.endswith(".mjs") else 900)
        lignes = [l for l in out.strip().split("\n") if l.strip() and not l.strip().startswith("at ")]
        res.append((c, code, (lignes[-1] if lignes else "")[:220]))
    return res


# ── 4. preuves des COUVERT ──────────────────────────────────────────────────
def preuves_couverts(rows):
    sortie = []
    for r in rows:
        if not r["statut"].startswith("COUVERT"):
            continue
        code = r["code"]                     # 5e_C2.2
        suffixe = code.split("_", 1)[1]      # C2.2
        dossier = os.path.join(RACINE, r["chemin"])
        readme = os.path.join(dossier, "README.md")
        cible = None
        if os.path.exists(readme):
            t = open(readme, encoding="utf-8").read()
            m = re.search(r"\]\((\.\./[^)]+?/)(?:sequence[^)]*\.html|[^)]*\.html)\)", t) or re.search(r"\*\*(\d[a-z]_C\d\.\d+)\*\*", t)
            if m:
                g = m.group(1)
                cible = os.path.normpath(os.path.join(dossier, g)) if g.startswith("..") else os.path.join(os.path.dirname(dossier), g)
        # La mesure n'a de sens que si le QCM du lot marque ses questions par code (`c:"C2.2"`,
        # convention des lots du thème 1). Un QCM qui marque autrement (`c:"EN"`, `c:"ID"`) ou pas du
        # tout, ou un lot sans QCM à sa racine, ne dit rien : le rapport l'écrit, il n'invente pas un zéro.
        n_q, marque, trouve = 0, False, False
        if cible and os.path.isdir(cible):
            for f in sorted(os.listdir(cible)):
                if f.startswith("qcm") and f.endswith(".html"):
                    trouve = True
                    src = open(os.path.join(cible, f), encoding="utf-8").read()
                    if re.search(r'\bc:"C\d\.\d+"', src):
                        marque = True
                    n_q += len(re.findall(r'\bc:"%s"' % re.escape(suffixe), src))
        if not trouve:
            n_q = "pas de QCM à la racine du lot"
        elif not marque:
            n_q = "QCM non marqué par code"
        sortie.append((code, r["theme"], os.path.relpath(cible, RACINE) if cible else "—", n_q, r["croisement"][:80]))
    return sortie


# ── 5. dérive des générateurs ───────────────────────────────────────────────
def empreintes(racine):
    e = {}
    for d, _, fs in os.walk(racine):
        if "/.git" in d or "/_archive" in d or "node_modules" in d:
            continue
        for f in fs:
            if f.endswith((".html", ".json", ".csv", ".svg", ".md")):
                p = os.path.join(d, f)
                e[os.path.relpath(p, racine)] = hashlib.sha256(open(p, "rb").read()).hexdigest()
    return e


def derive_generateurs():
    tmp = tempfile.mkdtemp(prefix="audit_copie_")
    copie = os.path.join(tmp, "depot")
    shutil.copytree(RACINE, copie, ignore=shutil.ignore_patterns(".git", "node_modules", "_archive-anciennes-versions", "__pycache__"))
    avant = empreintes(copie)
    rapports = []
    for dossier, cmd in GENERATEURS:
        parties = cmd.split()
        code, out = lancer([sys.executable] + parties, cwd=os.path.join(copie, dossier), timeout=900)
        rapports.append((dossier, cmd, code, out.strip().split("\n")[-1][:160] if out.strip() else ""))
    apres = empreintes(copie)
    changes = sorted(p for p in apres if avant.get(p) != apres[p])
    shutil.rmtree(tmp, ignore_errors=True)
    return rapports, changes


# ── le rapport ──────────────────────────────────────────────────────────────
def theme_de(chemin):
    for n, d in THEMES.items():
        if chemin.startswith(d):
            return n
    return "?"


def ecrire(sortie, complet, generateurs):
    jour = dt.date.today().isoformat()
    rows, par_theme, non_complets, anomalies = couverture()
    code_vra, par_regle, par_page = regles_or()
    ctrl = controles(complet)
    preuves = preuves_couverts(rows)
    gen = derive_generateurs() if generateurs else None

    L = []
    L.append("# Rapport d'audit des trois thèmes — %s" % jour)
    L.append("")
    L.append("*Écrit par `_outils/rapport_audit.py` (%s). Il mesure et classe ; il ne corrige rien. Les décisions sont à la fin.*" %
             ("complet" if complet else "rapide" + (", avec générateurs" if generateurs else "")))
    L.append("")
    # Résumé
    p1 = [c for c, code, _ in ctrl if c in BLOQUANTS and code not in (0, None)]
    sans_preuve = [p for p in preuves if p[3] == 0]
    non_mesurables = [p for p in preuves if isinstance(p[3], str)]
    a_verifier = [r for r in non_complets if not r["statut"].startswith("COUVERT") and not r["statut"].startswith("EXISTANT")]
    n_x = sum(len(v) for v in par_regle.values())
    L.append("## Résumé")
    L.append("")
    L.append("| | Compte | Priorité |")
    L.append("|---|---|---|")
    L.append("| Contrôles bloquants rouges | %d (%s) | P1 |" % (len(p1), ", ".join(p1) or "aucun"))
    L.append("| Codes À VÉRIFIER / ABSENT | %d | P1 |" % len(a_verifier))
    L.append("| Codes COUVERT sans preuve au QCM (0 question marquée, QCM marqué par code) | %d sur %d | P1 |" % (len(sans_preuve), len(preuves)))
    L.append("| Codes COUVERT dont la preuve n'est pas mesurable (QCM non marqué par code, ou absent de la racine) | %d sur %d | décision |" % (len(non_mesurables), len(preuves)))
    L.append("| ✘ de règles d'or (à cribler) | %d sur %d pages | P2 |" % (n_x, len(par_page)))
    L.append("| Codes EXISTANT À AMÉLIORER | %d | P2 |" % sum(1 for r in non_complets if r["statut"].startswith("EXISTANT")))
    if gen:
        L.append("| Fichiers qu'une régénération changerait | %d | P2 |" % len(gen[1]))
    L.append("| Anomalies notées dans la matrice | %d codes | P3 |" % len(anomalies))
    L.append("")

    # Couverture
    L.append("## 1. Couverture (pédagogie) — 114 codes")
    L.append("")
    L.append("| Thème | " + " | ".join(sorted({s for c in par_theme.values() for s in c})) + " |")
    statuts = sorted({s for c in par_theme.values() for s in c})
    L.append("|---|" + "---|" * len(statuts))
    for t in ("1", "2", "3"):
        L.append("| %s | " % t + " | ".join(str(par_theme[t].get(s, 0)) for s in statuts) + " |")
    L.append("")
    L.append("### Codes non complets")
    L.append("")
    L.append("| Code | Statut | Priorité | Ce que dit la matrice |")
    L.append("|---|---|---|---|")
    for r in non_complets:
        if r["statut"].startswith("COUVERT"):
            continue
        prio = "P2" if r["statut"].startswith("EXISTANT") else "P1"
        L.append("| %s | %s | %s | %s |" % (r["code"], r["statut"], prio, (r.get("anomalies") or r.get("preuves_manquantes") or "").replace("|", "/")[:160]))
    L.append("")
    L.append("### Codes COUVERT par mutualisation : la preuve au QCM")
    L.append("")
    L.append("Preuve retenue : au moins deux questions du QCM du lot principal marquées du code (`c:\"Cx.y\"`). Zéro = couvert sans preuve (P1). "
             "La mesure ne vaut que pour les QCM qui marquent leurs questions par code (convention des lots du thème 1) ; "
             "ailleurs elle dit « non marqué » — ce qui est une décision à prendre, pas un défaut.")
    L.append("")
    L.append("| Code | Thème | Lot principal | Questions marquées | Note de la matrice |")
    L.append("|---|---|---|---|---|")
    for code, t, cible, n, note in sorted(preuves, key=lambda x: ((0 if x[3] == 0 else 1 if isinstance(x[3], str) else 2), x[0])):
        libelle = ("**0 — sans preuve**" if n == 0 else ("1 — faible" if n == 1 else (("*%s*" % n) if isinstance(n, str) else str(n))))
        L.append("| %s | %s | %s | %s | %s |" % (code, t, cible.split("/")[-1] if cible != "—" else "—", libelle, note.replace("|", "/")))
    L.append("")

    # Règles d'or
    L.append("## 2. Règles d'or (`verif_regles_audit.py`, sortie %s)" % code_vra)
    L.append("")
    L.append("| Règle | ✘ | Pages | Thèmes | Exemple de message | Lecture |")
    L.append("|---|---|---|---|---|---|")
    for regle, items in sorted(par_regle.items(), key=lambda kv: -len(kv[1])):
        pages = sorted({p for p, _ in items})
        themes = collections.Counter(theme_de(p) for p in pages)
        lecture = ("toute une famille de pages : vérifier le CONTRÔLE avant les pages" if len(pages) >= 10 else "à lire page par page")
        L.append("| %s | %d | %d | %s | %s | %s |" % (regle, len(items), len(pages),
                 " ".join("T%s:%d" % kv for kv in sorted(themes.items())), items[0][1].replace("|", "/")[:120], lecture))
    L.append("")
    L.append("### Par page")
    L.append("")
    L.append("| Page | Thème | Règles en ✘ |")
    L.append("|---|---|---|")
    for p, rs in sorted(par_page.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        L.append("| %s | %s | %s |" % (p.split("/")[-2] + "/" + p.split("/")[-1], theme_de(p), " ".join(sorted(rs, key=lambda s: int(s[2:])))))
    L.append("")
    L.append("### Crible (à remplir à la main : vrai défaut / contrôle périmé)")
    L.append("")
    L.append("*Vide tant que personne ne l'a fait. Un contrôle périmé se corrige dans `verif_regles_audit.py` (une PR) ; un vrai défaut se corrige par vague.*")
    L.append("")

    # Contrôles
    L.append("## 3. Contrôles du site (technique)")
    L.append("")
    L.append("| Contrôle | Sortie | Dernière ligne | Priorité si rouge |")
    L.append("|---|---|---|---|")
    for c, code, ligne in ctrl:
        etat = "non exécuté" if code is None else ("✅ 0" if code == 0 else "✘ %s" % code)
        L.append("| `%s` | %s | %s | %s |" % (c, etat, ligne.replace("|", "/"), "P1" if c in BLOQUANTS else "P2"))
    if not complet:
        L.append("| %s | non exécutés (lancer `--complet`) | | |" % ", ".join("`%s`" % c for c in CONTROLES_MJS))
    L.append("")

    # Générateurs
    L.append("## 4. Dérive des générateurs")
    L.append("")
    if gen:
        rapports, changes = gen
        L.append("| Générateur | Sortie | Dernière ligne |")
        L.append("|---|---|---|")
        for d, cmd, code, ligne in rapports:
            L.append("| `%s` | %s | %s |" % (cmd.replace("../scenarios/", ""), ("✅ 0" if code == 0 else "✘ %s" % code), ligne.replace("|", "/")))
        L.append("")
        L.append("Fichiers qu'une régénération changerait (%d) — une retouche faite à la main sur ces pages sera écrasée :" % len(changes))
        L.append("")
        for p in changes[:200]:
            L.append("- `%s`" % p)
        if len(changes) > 200:
            L.append("- … et %d autres" % (len(changes) - 200))
    else:
        L.append("*Non mesurée (lancer `--generateurs`).*")
    L.append("")

    # Anomalies de la matrice
    L.append("## 5. Anomalies notées dans la matrice (pratique de classe, médias, différenciation) — P3")
    L.append("")
    mots = collections.Counter()
    for r in anomalies:
        a = r["anomalies"].lower()
        for k, lib in (("compress", "images lourdes"), ("sources_medias", "provenance des médias"), ("différenciation", "différenciation"),
                       ("n°58", "manipulation réelle (n°58)"), ("alternatif", "textes alternatifs"), ("qcm", "QCM"), ("licence", "licence")):
            if k in a:
                mots[lib] += 1
    L.append("| Famille | Codes concernés |")
    L.append("|---|---|")
    for k, v in mots.most_common():
        L.append("| %s | %d |" % (k, v))
    L.append("")
    L.append("<details><summary>Le détail, code par code (%d)</summary>" % len(anomalies))
    L.append("")
    L.append("| Code | Statut | Anomalie |")
    L.append("|---|---|---|")
    for r in anomalies:
        L.append("| %s | %s | %s |" % (r["code"], r["statut"], r["anomalies"].replace("|", "/").replace("\n", " ")[:260]))
    L.append("")
    L.append("</details>")
    L.append("")

    # Décisions
    L.append("## 6. Décisions pour Pascal")
    L.append("")
    L.append("- [ ] Ordre des vagues : P1 d'abord, puis une règle d'or par vague (la plus nombreuse en premier), puis les P3 ?")
    L.append("- [ ] Pour chaque règle qui tombe sur toute une famille : corriger le contrôle, ou les pages ?")
    L.append("- [ ] Les codes COUVERT sans preuve : ajouter deux questions au QCM du lot principal, ou retirer la mutualisation ?")
    L.append("- [ ] Les QCM non marqués par code : adopter la convention `c:\"Cx.y\"` partout (règle d'or candidate), pour que la preuve se mesure ?")
    L.append("- [ ] Les codes À VÉRIFIER (thème 3) : qui regarde, et quand ?")
    L.append("")
    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    open(sortie, "w", encoding="utf-8").write("\n".join(L) + "\n")
    return sortie


if __name__ == "__main__":
    complet = "--complet" in sys.argv
    generateurs = "--generateurs" in sys.argv
    sortie = None
    if "--sortie" in sys.argv:
        sortie = sys.argv[sys.argv.index("--sortie") + 1]
    sortie = sortie or os.path.join(RACINE, "docs", "audits", "RAPPORT_AUDIT_%s.md" % dt.date.today().isoformat())
    print("écrit :", os.path.relpath(ecrire(sortie, complet, generateurs), RACINE))
