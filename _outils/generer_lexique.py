#!/usr/bin/env python3
"""generer_lexique.py — le lexique qui manque à nos séquences est déjà écrit.

LE CONSTAT QUI A DONNÉ CETTE IDÉE
---------------------------------
Une mesure des 41 séquences du dépôt a montré qu'AUCUNE ne porte de lexique.
Et le même jour, une autre mesure a montré que nos 40 QCM portent 1 206
questions, dont 1 206 nomment une NOTION (`n`) et 1 176 portent un « à
retenir » d'une ligne (`ret`) — déjà rédigés, déjà relus, déjà mesurés.

    « La moyenne qui ne décrit personne » → « Une moyenne décrit un milieu,
    pas une personne. »

Ce lexique existe donc. Il est simplement enfermé dans les corrections d'un
QCM, que seul lit l'élève qui se trompe — et jamais celui qui révise.

CE QUE CE SCRIPT FAIT
---------------------
Il ouvre les QCM d'un lot, en extrait les couples (notion, à retenir), les
range par compétence, et écrit une page `lexique_<code>.html` autonome :
imprimable, hors ligne, sans compte, lisible en noir et blanc.

Il n'INVENTE rien. Chaque ligne vient d'un QCM du même lot, mot pour mot. Si
une notion n'a pas de « à retenir », elle est signalée comme telle plutôt que
comblée — un lexique qui bouche ses trous ment sur ce qu'il contient
(règle n°146).

USAGE
    python3 generer_lexique.py <dossier du lot> [autres…]
    python3 generer_lexique.py --tous theme-1-*      # tous les lots d'un thème
"""
import glob
import html
import os
import re
import sys
import unicodedata

CHAMP = lambda bloc, nom: (
    m.group(1) if (m := re.search(r'"?\b%s"?\s*:\s*"((?:[^"\\]|\\.)*)"' % nom, bloc)) else ""
)
DEBUTS = ["const QUESTIONS = [", "const QUESTIONS=[", "const Q = [", "const Q=["]


def blocs_questions(src):
    """Découpe la banque en blocs `{…}`, en ignorant les accolades des chaînes."""
    for motif in DEBUTS:
        i = src.find(motif)
        if i >= 0:
            deb = i + len(motif) - 1
            break
    else:
        return []
    prof, cur, dans_txt, ech, blocs = 0, "", False, False, []
    for k in range(deb, len(src)):
        ch = src[k]
        if dans_txt:
            cur += ch
            if ech: ech = False
            elif ch == "\\": ech = True
            elif ch == '"': dans_txt = False
            continue
        if ch == '"' and prof:
            dans_txt = True; cur += ch; continue
        if ch == "{": prof += 1
        if prof: cur += ch
        if ch == "}":
            prof -= 1
            if prof == 0:
                blocs.append(cur); cur = ""
        if ch == "]" and prof == 0 and blocs:
            break
    return blocs


def sans_balises(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip()


def cle_tri(t):
    """Tri alphabétique qui ignore les accents et l'article initial."""
    t = re.sub(r"^(l'|la |le |les |un |une |des |d')", "", t.lower())
    return "".join(c for c in unicodedata.normalize("NFD", t)
                   if unicodedata.category(c) != "Mn")


#: le bouton « ouvrir le QCM » d'une séquence — un <a class="btn …"> vers un qcm_*.html
BOUTON_QCM = re.compile(r'<a\b[^>]*class="[^"]*\bbtn\b[^"]*"[^>]*href="([^"]*qcm[^"]*\.html)"'
                        r'|<a\b[^>]*href="([^"]*qcm[^"]*\.html)"[^>]*class="[^"]*\bbtn\b', re.I)


def qcm_du_lot(dossier):
    """Les QCM du lot, tels que ses séquences les DÉSIGNENT.

    Première version : tous les `qcm_*.html` du dossier. Sur le Thème 2, le lot
    `4e_C4.7` en porte quatre — le sien plus trois ressources d'entraînement — et
    produisait un lexique de 120 notions. Un lexique de 120 entrées n'est pas un
    outil de révision, c'est un annuaire.

    On suit donc le BOUTON de la séquence : « un seul bouton QCM » est déjà la
    règle d'or n°4, et c'est un fait écrit dans la page, pas une convention de
    nommage à deviner. Les renvois « pour aller plus loin » du bilan, qui ne sont
    pas des boutons, ne comptent pas.

    Repli : s'il n'y a aucune séquence ou aucun bouton, on reprend tous les QCM
    du dossier — mieux vaut un lexique trop large que pas de lexique.
    """
    vises = []
    for s in sorted(glob.glob(os.path.join(dossier, "sequence*.html"))):
        src = open(s, encoding="utf-8", errors="ignore").read()
        for m in BOUTON_QCM.finditer(src):
            cible = m.group(1) or m.group(2)
            chemin = os.path.normpath(os.path.join(dossier, cible))
            if os.path.isfile(chemin) and chemin not in vises:
                vises.append(chemin)
    return vises or sorted(glob.glob(os.path.join(dossier, "qcm_*.html")))


def lire_lot(dossier):
    """Rend {competence: [(notion, a_retenir, fichier), …]} pour un dossier."""
    par_comp = {}
    for f in qcm_du_lot(dossier):
        src = open(f, encoding="utf-8", errors="ignore").read()
        for b in blocs_questions(src):
            n = sans_balises(CHAMP(b, "n"))
            if not n:
                continue
            comp = sans_balises(CHAMP(b, "c")) or "—"
            ret = sans_balises(CHAMP(b, "ret") or CHAMP(b, "t"))
            par_comp.setdefault(comp, []).append((n, ret, os.path.basename(f)))
    return par_comp


GABARIT = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lexique — {titre}</title>
<style>
  :root{{ --bg:#050f24; --panel:#0d2347; --border:#274a8a; --title:#81aaff;
          --sub:#9bbefc; --head:#c68ef2; --text:#e4eaf5; --hl:#61dafb; }}
  *{{box-sizing:border-box}}
  body{{background:var(--bg);color:var(--text);margin:0;padding:0 16px 60px;line-height:1.55;
       font-family:system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif}}
  h1{{font-size:1.45em;text-align:center;margin:22px 0 4px;color:var(--title)}}
  .sub{{text-align:center;color:var(--sub);margin-bottom:14px;font-size:.95em}}
  main{{max-width:880px;margin:0 auto}}
  section{{background:var(--panel);border:1px solid var(--border);border-radius:14px;
           padding:14px 20px;margin-bottom:16px}}
  h2{{color:var(--head);font-size:1.05em;margin:.2em 0 .6em}}
  dl{{margin:0}}
  dt{{font-weight:700;color:var(--hl);margin-top:.7em}}
  dd{{margin:.15em 0 0 0}}
  dd.vide{{color:var(--sub);font-style:italic}}
  .compte{{color:var(--sub);font-size:.85em}}
  nav a{{color:var(--hl)}}
  footer{{max-width:880px;margin:20px auto 0;color:var(--sub);font-size:.85em;text-align:center}}
  @media print{{
    body{{background:#fff;color:#000;padding:0}}
    section{{background:#fff;border:1px solid #666;break-inside:avoid}}
    h1,h2,dt{{color:#000}} dd.vide{{color:#444}} nav,footer{{display:none}}
  }}
</style>
</head>
<body>
<nav style="padding-top:12px"><a href="{retour}">← Revenir à la séquence</a></nav>
<h1>📖 Lexique — {titre}</h1>
<p class="sub">{compte} notions, tirées mot pour mot des QCM du lot · imprimable · fonctionne hors ligne</p>
<main>
{corps}
</main>
<footer>
  Chaque ligne provient d'une question de {sources}. Rien n'a été réécrit ici :
  ce lexique rassemble ce que les corrections disaient déjà, une par une.
</footer>
</body>
</html>
"""


def ecrire_lexique(dossier, titre, retour):
    par_comp = lire_lot(dossier)
    total = sum(len(v) for v in par_comp.values())
    if not total:
        return None
    corps, sources = [], set()
    for comp in sorted(par_comp):
        vus, lignes = set(), []
        for n, ret, f in sorted(par_comp[comp], key=lambda x: cle_tri(x[0])):
            if n in vus:
                continue
            vus.add(n); sources.add(f)
            if ret:
                lignes.append("  <dt>%s</dt>\n  <dd>%s</dd>"
                              % (html.escape(n), html.escape(ret)))
            else:
                lignes.append("  <dt>%s</dt>\n  <dd class=\"vide\">"
                              "(cette question ne porte pas de « à retenir » — à écrire)</dd>"
                              % html.escape(n))
        corps.append("<section>\n <h2>%s <span class=\"compte\">· %d notions</span></h2>\n"
                     " <dl>\n%s\n </dl>\n</section>"
                     % (html.escape(comp), len(vus), "\n".join(lignes)))
    page = GABARIT.format(titre=html.escape(titre), compte=total, retour=html.escape(retour),
                          corps="\n".join(corps), sources=", ".join(sorted(sources)))
    code = re.sub(r"[^A-Za-z0-9._-]", "_", titre)[:60]
    sortie = os.path.join(dossier, "lexique_%s.html" % code)
    open(sortie, "w", encoding="utf-8").write(page)
    return sortie, total


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    tous = "--tous" in sys.argv
    dossiers = []
    for a in args:
        if tous:
            dossiers += sorted({os.path.dirname(f)
                                for f in glob.glob(a + "/**/sequence*.html", recursive=True)})
        else:
            dossiers.append(a)
    for d in dossiers:
        seqs = sorted(glob.glob(os.path.join(d, "sequence*.html")))
        if not seqs:
            continue
        titre = os.path.basename(d)
        r = ecrire_lexique(d, titre, os.path.basename(seqs[0]))
        if r:
            print("%-58s %3d notions → %s" % (titre[:56], r[1], os.path.basename(r[0])))
        else:
            print("%-58s  aucun QCM lisible dans ce dossier — NON GÉNÉRÉ" % titre[:56])
