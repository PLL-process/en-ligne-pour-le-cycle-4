# -*- coding: utf-8 -*-
"""Les exercices des ateliers, incrustés dans les séquences des codes qu'ils servent.

Chaque incrustation est une section `.atelier-incruste`, posée dans une séance entre deux
marqueurs HTML :

    <!-- ateliers-representations:debut <id> --> … <!-- ateliers-representations:fin <id> -->

La première fois, elle prend la place d'un passage désigné (ou se pose avant une phrase
repère) ; ensuite, on ne réécrit QUE ce qui est entre les marqueurs. Le moteur des exercices
et sa feuille de style (limitée à la section incrustée) sont posés une seule fois par page,
juste avant </body>, entre leurs propres marqueurs.

Les exercices gardent la MÊME clé de sauvegarde que dans leur atelier et dans le cahier du
niveau : ce que l'élève fait dans sa séquence se retrouve dans l'atelier, et inversement.

    python3 incrustations.py            # pose ou met à jour toutes les incrustations
    python3 incrustations.py --verifier # dit seulement ce qui changerait (sortie 1 si écart)
"""
import importlib
import json
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import build  # noqa: E402
import moteur  # noqa: E402

DEPOT = moteur.DEPOT
KIT = ("<!-- ateliers-representations:moteur -->", "<!-- /ateliers-representations:moteur -->")
GARDER = re.compile(r"^(\.(?:card|meta|consigne|note|btn|figure|schema-vivant|defile|retour|encoche|option|options|demo|retenir|piege|critere|"
                    r"croquis|verif|lsu|champ)|fieldset|textarea|input|table|th|td|details|label|a)")


def css_incruste():
    """La feuille du kit, limitée à .atelier-incruste (rien ne déborde sur la séquence)."""
    src = re.sub(r"/\*.*?\*/", "", moteur.KIT_CSS, flags=re.S)
    variables = re.search(r":root\{(.*?)\}", src, re.S).group(1)
    sortie = [".atelier-incruste{%s}" % variables.strip()]

    def portee(bloc):
        out = []
        for regle in re.finditer(r"([^{}@]+)\{([^{}]*)\}", bloc):
            sels = [x.strip() for x in regle.group(1).split(",")]
            gardes = []
            for sel in sels:
                tete = sel.lstrip(".") if False else sel
                if GARDER.match(sel) or sel.startswith("body.essentiel"):
                    if sel.startswith("body.essentiel"):
                        gardes.append("body.essentiel .atelier-incruste " + sel[len("body.essentiel"):].strip())
                    else:
                        gardes.append(".atelier-incruste " + sel)
            if gardes:
                out.append("%s{%s}" % (",".join(gardes), regle.group(2).strip()))
        return out

    # règles hors @media
    hors = re.sub(r"@media[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}", "", src)
    sortie += portee(hors)
    for m in re.finditer(r"(@media[^{]*)\{((?:[^{}]*\{[^{}]*\})*[^{}]*)\}", src):
        regles = portee(m.group(2))
        if regles:
            sortie.append("%s{%s}" % (m.group(1).strip(), "".join(regles)))
    sortie.append(".atelier-incruste{border-left:5px solid var(--head);}")
    sortie.append(".atelier-incruste .card.exercice{background:rgba(10,27,61,.6)}")
    sortie.append(".atelier-incruste>h3,.atelier-incruste>h4{color:var(--head);font-size:1.08em;margin:4px 0 8px}")
    sortie.append(".atelier-incruste .card.exercice>h4,.atelier-incruste .card.exercice>h5{color:var(--hl);font-size:1.02em;margin:4px 0 8px}")
    sortie.append("@media print{.atelier-incruste,.atelier-incruste .card.exercice{background:#fff!important;color:#111}"
                  ".atelier-incruste>h3,.atelier-incruste>h4,.atelier-incruste .card.exercice>h4,.atelier-incruste .card.exercice>h5{color:#111}}")
    return "\n".join(sortie)


#: Le moteur, posé une fois par page : feuille limitée à la section, et script commun.
def bloc_moteur():
    return "%s\n<style>\n%s\n</style>\n<script>\n%s</script>\n%s\n" % (KIT[0], css_incruste(), moteur.KIT_JS, KIT[1])


def section(inc):
    at = importlib.import_module("donnees_" + inc["module"])
    niv = inc["niveau"]
    N = at.NIVEAUX[niv]
    seq = DEPOT / inc["sequence"]
    d = seq.parent
    defs = {}
    h = ['<section class="card atelier-incruste" id="incruste-%s" aria-labelledby="incruste-%s-titre">' % (inc["id"], inc["id"]),
         '<%s id="incruste-%s-titre">%s</%s>' % (inc["balise"], inc["id"], inc["titre"], inc["balise"]),
         '<p>%s</p>' % inc["intro"]]
    numeros = {ex["id"]: i + 1 for i, ex in enumerate(N["exercices"])}
    for exo in inc["exos"]:
        ex = next(x for x in N["exercices"] if x["id"] == exo)
        uid = "%s_%s_%s" % (at.COURT, niv, ex["id"])
        cle = "rep_%s_%s_%s" % (at.SLUG, niv, ex["id"])
        # Les minutes de l'exercice sont déjà comptées dans celles de l'activité qui l'accueille :
        # elles s'écrivent dans la ligne « Durée », pas dans le titre.
        html, df = moteur.exercice(ex, numeros[exo], uid, cle, balise=inc["balise_exo"], duree_au_titre=False)
        h.append(html)
        defs[uid] = df
    page = build.page_niveau(at, niv)
    h.append('<p class="note">%s Ces exercices viennent de <a href="%s">l\'atelier de %s « %s »</a>&nbsp;: '
             'ce que tu fais ici s\'y retrouve, avec %s.</p>'
             % (at.EMOJI, moteur.rel(d, page), niv, at.TITRE, inc.get("suite", "les autres exercices et le QCM")))
    h.append('<script type="application/json">%s</script>' % json.dumps({"exercices": defs}, ensure_ascii=False).replace("</", "<\\/"))
    h.append("</section>")
    return "".join(h)


def marqueurs(ident):
    return ("<!-- ateliers-representations:debut %s -->" % ident, "<!-- ateliers-representations:fin %s -->" % ident)


def poser(inc, texte):
    debut, fin = marqueurs(inc["id"])
    bloc = "%s\n%s\n%s" % (debut, section(inc), fin)
    if debut in texte:
        i, j = texte.index(debut), texte.index(fin) + len(fin)
        texte = texte[:i] + bloc + texte[j:]
    elif "remplacer" in inc:
        a, b = inc["remplacer"]
        i = texte.index(a)
        j = texte.index(b, i) + len(b)
        texte = texte[:i] + bloc + "\n" + texte[j:]
    elif "avant" in inc:
        if texte.count(inc["avant"]) != 1:
            raise SystemExit("Repère absent ou ambigu dans %s : %r" % (inc["sequence"], inc["avant"][:60]))
        i = texte.index(inc["avant"])
        texte = texte[:i] + bloc + "\n" + texte[i:]
    else:
        raise SystemExit("Incrustation sans point de pose : %s" % inc["id"])
    # le moteur, une fois par page
    m = bloc_moteur()
    if KIT[0] in texte:
        i, j = texte.index(KIT[0]), texte.index(KIT[1]) + len(KIT[1]) + 1
        texte = texte[:i] + m + texte[j:]
    else:
        i = texte.rindex("</body>")
        texte = texte[:i] + m + texte[i:]
    return texte


def main(argv):
    verifier = "--verifier" in argv
    import incrustations_table as table
    ecarts = 0
    par_page = {}
    for inc in table.INCRUSTATIONS:
        par_page.setdefault(inc["sequence"], []).append(inc)
    for seq, incs in par_page.items():
        p = DEPOT / seq
        avant = p.read_text(encoding="utf-8")
        texte = avant
        for inc in incs:
            texte = poser(inc, texte)
        if texte != avant:
            ecarts += 1
            print(("À METTRE À JOUR : " if verifier else "écrit : ") + seq)
            if not verifier:
                p.write_text(texte, encoding="utf-8")
        else:
            print("à jour : " + seq)
    return 1 if (verifier and ecarts) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
