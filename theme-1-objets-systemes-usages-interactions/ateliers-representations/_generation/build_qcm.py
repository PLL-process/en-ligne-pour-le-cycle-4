# -*- coding: utf-8 -*-
"""Assemble le QCM d'un atelier à partir du gabarit maison et de sa banque `q_<module>.py`.

Le moteur du QCM (barème, minuteur, modes, sauvegarde) n'est pas réécrit : il est
repris tel quel du gabarit (copie figée du QCM de l'atelier de planification,
`gabarit_qcm.tpl`) ; seuls le bloc `const QUESTIONS`, la clé, les libellés et la
navigation sont remplacés. Le générateur REFUSE d'écrire s'il reste une trace du
gabarit d'origine.

    python3 build_qcm.py interacteurs      puis      node ../../../_outils/fix_r.js <qcm> <graine>
    python3 build_qcm.py --tous            (assemble et répartit tous les QCM)
    python3 build_qcm.py --verifier [module …]   (rejoue dans un dossier temporaire, compare à l'octet, n'écrit rien)

Le gabarit doit suivre ce que les outils du site posent sur les pages publiées (contraste, licence, loupe…) : le
18/11/2026, il en avait cinq de retard, et une régénération les aurait effacés. `--verifier` le dit avant qu'on
régénère : sortie 0, chaque QCM sort identique ; 1, un QCM diffère (le gabarit ou la banque est en retard sur la
page) ; 2, aucun QCM vérifié (n°299). `banc_ateliers.py` le lance.
"""
import sys as _sys_ic
_sys_ic.path.insert(0, next(str(d / "_outils") for d in __import__("pathlib").Path(__file__).resolve().parents if (d / "_outils" / "intituler_codes.py").is_file()))
import intituler_codes  # noqa: E402
import importlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import build  # noqa: E402
import moteur  # noqa: E402
_sys_qa = __import__("sys")
_sys_qa.path.insert(0, next(str(d / "_outils" / "qcm_aides") for d in __import__("pathlib").Path(__file__).resolve().parents if (d / "_outils" / "qcm_aides" / "poser.py").is_file()))
from poser import poser_si_donnees as _poser_aides  # noqa: E402  aides et pièges du lot (n°339)

ORDRE = ("expl", "ex", "err")
GABARIT = ICI / "gabarit_qcm.tpl"


def bloc_question(o):
    p = ["c:" + json.dumps(o["c"], ensure_ascii=False),
         "n:" + json.dumps(o["n"], ensure_ascii=False),
         "q:" + json.dumps(o["q"], ensure_ascii=False)]
    if "img" in o:
        p.append("img:{src:%s,alt:%s}" % (json.dumps(o["img"]["src"], ensure_ascii=False),
                                          json.dumps(o["img"]["alt"], ensure_ascii=False)))
    p.append("o:[%s]" % ",".join(json.dumps(x, ensure_ascii=False) for x in o["o"]))
    p.append("r:0")
    for k in ORDRE:
        p.append("%s:%s" % (k, json.dumps(o[k], ensure_ascii=False)))
    p.append("d:[%s]" % ",".join(json.dumps(x, ensure_ascii=False) for x in o["d"]))
    p.append("ret:" + json.dumps(o["ret"], ensure_ascii=False))
    return "{" + ",\n ".join(p) + "}"


OUVERTURE_NIVEAU = r"""
/* ══════ Ouvrir sur les questions du niveau de l'élève ══════
   L'atelier de chaque niveau appelle ce QCM avec ?codes=<codes du niveau>.
   On ouvre alors sur ces questions-là ; le parcours complet reste à un clic. */
(function ouvrirSurMonNiveau(){
  const m = /codes=([^&#]+)/.exec((location.search || "") + (location.hash || ""));
  if (!m) return;
  const codes = decodeURIComponent(m[1]).split(",").filter(Boolean);
  const liste = [...Array(N).keys()].filter(i => codes.includes(QUESTIONS[i].c));
  if (!liste.length) return;
  const sel = $("selComp");
  if (codes.length === 1) { sel.value = codes[0]; setMode("cible"); }
  else { setMode("cible"); etat.sousListe = liste; etat.courante = liste[0]; save(); rendreTout(); }
  signale("🎯 Le QCM s'ouvre sur les " + liste.length + " questions de ton niveau. Pour toutes les questions, choisis « Parcours complet ».");
})();
"""


def construire(module, verifier=False):
    at = importlib.import_module("donnees_" + module)
    banque = importlib.import_module("q_" + module)
    Q = banque.Q
    s = GABARIT.read_text(encoding="utf-8")
    s = intituler_codes.sans_bulles(s)   # les étiquettes du gabarit, sans leurs bulles (17/11/2026)
    sortie = build.qcm(at)
    d = sortie.parent
    codes = []
    for x in Q:
        if x["c"] not in codes:
            codes.append(x["c"])
    niveaux = []
    for c in codes:
        n = c.split("_")[0]
        if n not in niveaux:
            niveaux.append(n)

    lignes = ["const QUESTIONS = ["]
    prec = None
    for i, o in enumerate(Q):
        if o["c"] != prec:
            lignes.append("/* ═══ %s — %s ═══ */" % (o["c"], moteur.formulation(o["c"])))
            prec = o["c"]
        lignes.append(bloc_question(o) + ("," if i < len(Q) - 1 else ""))
    lignes.append("];")
    ancien = re.search(r"const QUESTIONS = \[.*?\n\];", s, re.S)
    if not ancien:
        raise SystemExit("Bloc QUESTIONS introuvable dans le gabarit.")
    s = s[:ancien.start()] + "\n".join(lignes) + s[ancien.end():]

    nb_img = sum(1 for x in Q if "img" in x)
    repartition = " · ".join("%s : %d" % (c, sum(1 for x in Q if x["c"] == c)) for c in codes)
    comp = ",\n  ".join('"%s":%s' % (c, json.dumps("%s — %s" % (c, moteur.formulation(c)), ensure_ascii=False)) for c in codes)
    options = "\n".join('      <option value="%s">%s — %s</option>' % (c, c, moteur.e(moteur.formulation(c))) for c in codes)
    pages = " · ".join('<a href="%s">Atelier %s</a>' % (moteur.rel(d, build.page_niveau(at, n)), n) for n in at.NIVEAUX)
    nav = ['<a href="%s">⌂ Accueil</a>' % moteur.rel(d, moteur.DEPOT / "index.html")]
    for n in at.NIVEAUX:
        nav.append('<a href="%s">← Atelier %s</a>' % (moteur.rel(d, build.page_niveau(at, n)), n))
    nav.append('<a href="%s">🧭 Toutes les représentations</a>' % moteur.rel(d, build.CARTE))

    remplacements = [
        (r"/\* Banque de questions — .*? \*/",
         "/* Banque de questions — Atelier : %s. %d questions (%s), dont %d illustrées. Source : _generation/q_%s.py */"
         % (at.TITRE_COURT, len(Q), repartition, nb_img, module)),
        # `CLE` (facultatif) dans la banque : quand ses questions changent, la clé de sauvegarde change aussi
        (r'const KEY="[^"]*";', 'const KEY="qcm_%s";' % getattr(banque, "CLE", at.SLUG)),
        (r"const COMP_LABELS=\{.*?\};", "const COMP_LABELS={\n  %s };" % comp),
        (r"<title>.*?</title>", "<title>%s</title>" % moteur.e("Thème 1 · %s — QCM : %s (%s)" % (
            "-".join(niveaux), at.TITRE_COURT, " · ".join(codes)))),
        (r"<h1>.*?</h1>", "<h1>%s QCM — %s</h1>" % (at.EMOJI, at.TITRE)),
        (r'<p class="subtitle">.*?</p>', '<p class="subtitle">%s</p>' % at.QCM_SOUS_TITRE),
        (r'<div class="badges">.*?</div>',
         '<div class="badges">\n  <span class="badge niveau">%s</span>\n%s\n  <span class="badge theme">%d questions · %d illustrées · chaque distracteur réfuté</span>\n</div>'
         % (" · ".join(niveaux), "\n".join('  <span class="badge code">%s</span>' % c for c in codes), len(Q), nb_img)),
        (r'(<select id="selComp"[^>]*>).*?(</select>)', r"\g<1>" + "\n" + options.replace("\\", "\\\\") + "\n    \\g<2>"),
        (r"<footer>\s*<p>.*?</p>",
         "<footer>\n  <p>QCM (questionnaire à choix multiples) d’entraînement %s · Thème 1 · Technologie cycle 4 (2024) · ateliers associés : %s</p>"
         % (" · ".join(codes), pages)),
        (r"#navharm\{position:sticky;top:0;z-index:1200;display:flex;gap:8px;",
         "#navharm{position:sticky;top:0;z-index:1200;display:flex;flex-wrap:wrap;gap:8px;"),
        (r'<nav id="navharm".*?</nav>', '<nav id="navharm" aria-label="Navigation du site">%s</nav>' % "".join(nav)),
        (r'⬅ Revenir à l\'atelier de ton niveau : .*?</p>', "⬅ Revenir à l'atelier de ton niveau : %s</p>" % pages),
    ]
    for motif, rempl in remplacements:
        s2, n = re.subn(motif, lambda m, r=rempl: m.expand(r) if "\\g<" in r else r, s, count=1, flags=re.S)
        if n != 1:
            raise SystemExit("Motif absent du gabarit : %r" % motif[:70])
        s = s2
    # Ouvrir sur le niveau de l'élève (#codes=…) : à la fin du script de la loupe, avant celui qui efface la
    # sauvegarde (n°322), comme sur les pages publiées
    pos = s.find("</script>\n<script>/* Règle d'or n°322")
    if pos < 0:
        raise SystemExit("Script d'effacement de la sauvegarde (n°322) absent du gabarit")
    s = s[:pos] + OUVERTURE_NIVEAU + s[pos:]
    # les aides et les pièges du QCM (n°339), avant le contrôle des restes : sans cela, régénérer les effacerait
    s = _poser_aides(s, str(sortie))
    # Rien du gabarit d'origine ne doit survivre
    for reste in ("planification", "GanttProject", "C7.1", "Brooklyn", "Shenzhen", "chemin critique"):
        if reste in s:
            raise SystemExit("Reste du gabarit d'origine non remplacé : %r" % reste)
    s = intituler_codes.poser_texte(s)   # chaque étiquette de code dit sa compétence au survol
    graine = sum(ord(c) for c in at.SLUG) % 997
    if verifier:
        # même chaîne (gabarit, banque, fix_r.js et sa graine), dans un dossier temporaire : la page n'est pas touchée
        with tempfile.TemporaryDirectory() as tmp:
            temoin = pathlib.Path(tmp) / sortie.name
            temoin.write_text(s, encoding="utf-8")
            r = subprocess.run(["node", str(moteur.DEPOT / "_outils" / "fix_r.js"), str(temoin), str(graine)],
                               capture_output=True, text=True)
            if r.returncode != 0:
                raise SystemExit("fix_r.js a échoué : %s" % r.stderr)
            pareil = temoin.read_bytes() == sortie.read_bytes()
        print("%s %s" % ("✅" if pareil else "⛔", sortie.relative_to(moteur.DEPOT))
              + ("" if pareil else " : la régénération ne la reproduit pas (gabarit ou banque en retard sur la page)"))
        return pareil
    sortie.write_text(s, encoding="utf-8")
    r = subprocess.run(["node", str(moteur.DEPOT / "_outils" / "fix_r.js"), str(sortie), str(graine)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("fix_r.js a échoué : %s" % r.stderr)
    print("QCM écrit : %s (%d questions, %d illustrées, graine %d) — %s"
          % (sortie.relative_to(moteur.DEPOT), len(Q), nb_img, graine, r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ""))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    verifier = sys.argv[1] == "--verifier"
    mods = build.MODULES if sys.argv[1] == "--tous" or sys.argv[1:] == ["--verifier"] else \
        [a for a in sys.argv[1:] if not a.startswith("--")]
    resultats = []
    for m in mods:
        try:
            importlib.import_module("q_" + m)
        except ModuleNotFoundError:
            print("  (pas encore de banque pour « %s »)" % m)
            continue
        resultats.append(construire(m, verifier=verifier))
    if verifier:
        if not resultats:
            print("✘ aucun QCM vérifié")
            raise SystemExit(2)
        print("%d QCM sur %d reproduits à l'octet" % (sum(resultats), len(resultats)))
        raise SystemExit(0 if all(resultats) else 1)
