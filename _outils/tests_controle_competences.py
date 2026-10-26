# -*- coding: utf-8 -*-
"""Banc de la règle d'or n°314 : `controle_competences.py`, l'outil `nommer_competences.py`, et le contrôle du mode
essentiel `controle_mode_essentiel.py` (même lot, 26/10/2026). Des pages fabriquées pour chaque cas, puis le dépôt réel.

    python3 _outils/tests_controle_competences.py

Sortie 0 si tout passe, 1 sinon.
"""
import os
import pathlib
import subprocess
import sys
import tempfile

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import controle_competences as cc  # noqa: E402
import nommer_competences as nc  # noqa: E402

res = []


def t(nom, ok, detail=""):
    res.append(bool(ok))
    print(("✔" if ok else "✘"), nom, "" if ok else "\n     " + str(detail).strip().replace("\n", "\n     ")[:1500])


def page(corps, tete=""):
    return "<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\"><title>t</title>%s</head><body>%s</body></html>" % (tete, corps)


def g(corps, tete=""):
    return cc.griefs(page(corps, tete))


# ── le texte ─────────────────────────────────────────────────────────────────────────────────────────────────────────
t("« CRCN 1.3 » seul est refusé", g("<p>Trace CRCN 1.3 dans le tableau.</p>"))
t("« CRCN 1.3 Traiter des données » passe", not g("<p>Trace CRCN 1.3 Traiter des données dans le tableau.</p>"))
t("« CRCN 1.3 — Traiter des données · N2 » passe (tiret, niveau)", not g("<h3>CRCN 1.3 — Traiter des données · N2</h3>"))
t("une liste « CRCN : 1.2 · 1.3 » refuse chaque code sans intitulé",
  len(g("<p>CRCN : 1.2 Gérer des données · 1.3</p>")) == 1)
t("« CRCN 5.1 (niv. 3) · 2.3 » : le niveau ne cache pas le code suivant", len(g("<p>CRCN 5.1 Résoudre des problèmes techniques (niv. 3) · 2.3</p>")) == 1)
t("le cadre nommé sans code (« compétences du CRCN ») passe", not g("<p>Les compétences du CRCN se certifient en 3e.</p>"))
t("une chaîne de JavaScript qui s'affiche est lue", g("<script>const q = {q:\"Pour prouver la compétence CRCN 1.3 ?\"};</script>"))
t("un commentaire n'est pas lu", not g("<!-- CRCN 1.3 --><script>/* CRCN 3.4 */</script><style>/* CRCN 5.1 */</style>"))
t("une infobulle hors étiquette est lue", g('<p title="CRCN 3.4">programme</p>'))
t("un intitulé à l'apostrophe typographique passe", not g("<p>CRCN 4.1 Sécuriser l’environnement numérique</p>"))
t("un code de rangement (4e_C8.1) n'est pas une compétence", not g("<p>Compétence 4e_C8.1 · C8.2</p>"))
# ── les étiquettes ───────────────────────────────────────────────────────────────────────────────────────────────────
t("une étiquette « CRCN » seule est refusée", g('<div class="badges"><span class="badge">CRCN</span></div>'))
t("une étiquette CRCN sans infobulle est refusée",
  g('<div class="badges"><span class="badge">🎯 CRCN 3.4 Programmer — Niv. 2</span></div>'))
BULLE_34 = nc.titre_crcn(["3.4"], {"3.4": "niveau 2"}, {"3.4": "tu écris l'algorithme SI T > 30 ALORS alerte, puis le testes"})
BULLE_34_HTML = BULLE_34.replace("&", "&amp;").replace('"', "&quot;").replace(">", "&gt;").replace("\n", "&#10;")
t("une bulle qui ne redit que l'intitulé est refusée (« traiter des données, c'est vaste »)",
  g('<div class="badges"><span class="badge" title="Compétence numérique du CRCN : 3.4 Programmer.">🎯 CRCN 3.4 Programmer — Niv. 2</span></div>'))
t("une bulle à trois étages (intitulé et niveau, cadre, « Ici : ») passe",
  not g('<div class="badges"><span class="badge" title="%s">🎯 CRCN 3.4 Programmer — Niv. 2</span></div>' % BULLE_34_HTML),
  g('<div class="badges"><span class="badge" title="%s">🎯 CRCN 3.4 Programmer — Niv. 2</span></div>' % BULLE_34_HTML))
t("une bulle sans « Ici : » est refusée, et le grief dit ce qui manque",
  [x[1] for x in g('<span class="badge" title="%s">CRCN 3.4 Programmer</span>' % nc.titre_crcn(["3.4"]))]
  == ["étiquette CRCN : la bulle de 3.4 (Programmer) ne donne pas « Ici : » ce que l'élève fait"])
t("le cadre doit être celui de la compétence : le cadre de 1.3 sous 3.4 est refusé",
  g('<span class="badge" title="CRCN 3.4 Programmer.&#10;Le cadre : « Appliquer des traitements à des données pour les '
    'analyser et les interpréter. »&#10;Ici : tu programmes l\'alerte de la station.">CRCN 3.4 Programmer</span>'))
deux = nc.titre_crcn(["1.3", "5.1"], {}, {"1.3": "tu ranges tes mesures dans un tableau et en tires une décision"})
t("deux compétences : chacune a son « Ici : » (celui de 1.3 ne vaut pas pour 5.1)",
  len(g('<span class="badge" title="%s">CRCN 1.3 Traiter des données · 5.1 Résoudre des problèmes techniques</span>'
        % deux.replace("\n", "&#10;"))) == 1)
t("une étiquette du socle sans infobulle est refusée", g('<div class="badges"><span class="badge socle">Socle : D2 · D4</span></div>'))
t("une infobulle du socle abrégée (« D4 systèmes techniques ») est refusée",
  g('<span class="badge" title="D2 méthodes et outils pour apprendre, D4 systèmes techniques">D2 · D4</span>'))
t("une étiquette du socle avec ses domaines en toutes lettres passe",
  not g('<span class="badge" title="%s">D2 · D4</span>' % nc._titre_socle(["D2", "D4"])))
# ── l'outil ──────────────────────────────────────────────────────────────────────────────────────────────────────────
src = page('<div class="badges"><span class="badge theme" title="Compétence numérique travaillée : '
           'les données — l\'élève exploite un tableau de mesures.">🖥 CRCN 1.3 · niveau 2</span>'
           '<span class="badge" title="Compétences numériques du CRCN : traiter des données.">CRCN 1.3 Traiter des données</span>'
           '<span class="badge theme">D1.3 · D2 · D4 · CRCN 1.3 niv. 2</span><span class="badge socle">Socle : D2 · D4 (+ D1)</span>'
           '<span class="badge" title="%s">🎯 CRCN 3.4 Programmer — Niv. 2</span>'
           '<span class="badge">CRCN : 5.1 Résoudre des problèmes techniques (niv. 2→3) · 3.4 Programmer (Niv. 1-2)</span></div>'
           '<h2>Activité 3 (CRCN 3.4)</h2><p><strong>CRCN 3.4 Programmer</strong> — lire un algorigramme.</p>'
           "<script>const L = 'CRCN 4.1 sécurité'; /* CRCN 1.2 */</script><!-- CRCN 5.2 -->" % BULLE_34_HTML)
apres, ajouts, changees = nc.nommer(src)
reste = cc.griefs(apres)
t("après l'outil, le contrôle ne réclame plus que les « Ici : », qui s'écrivent à la main",
  reste and all(x[1].endswith("ne donne pas « Ici : » ce que l'élève fait") for x in reste), reste)
t("l'outil est idempotent", nc.nommer(apres)[0] == apres)
t("l'outil écrit l'intitulé après le code, dans un titre", "Activité 3 (CRCN 3.4 Programmer)" in apres)
t("l'outil ne double pas un intitulé déjà écrit après une balise",
  apres.count("<strong>CRCN 3.4 Programmer</strong> — lire") == 1 and "Programmer Programmer" not in apres, apres)
t("l'outil écrit l'apostrophe typographique dans une chaîne JavaScript", "'CRCN 4.1 Sécuriser l’environnement numérique sécurité'" in apres, apres)
t("l'outil ne touche pas aux commentaires", "/* CRCN 1.2 */" in apres and "<!-- CRCN 5.2 -->" in apres)
t("l'outil écrit le niveau et le cadre officiel dans la bulle",
  "CRCN 1.3 Traiter des données — niveau 2.&#10;Le cadre : « Appliquer des traitements à des données pour les analyser et"
  " les interpréter. »" in apres, apres)
t("l'outil lit « niv. 2→3 » et « Niv. 1-2 »", "— niveau 2, vers le 3." in apres and "— niveaux 1 à 2." in apres, apres)
t("l'outil garde ce que l'ancienne infobulle ajoutait, comme « Ici : »", "Ici : L'élève exploite un tableau de mesures." in apres, apres)
t("l'outil n'invente pas de « Ici : »", apres.count("Ici : ") == 2, apres)
t("l'outil ne touche pas une bulle qui a ses trois étages", 'title="%s"' % BULLE_34_HTML in apres, apres)
t("l'outil écrit « > » en &gt; dans une bulle, et relit une balise dont la bulle contient « > »",
  "SI T &gt; 30" in apres and "SI T > 30" not in apres, apres)
t("l'outil sépare une étiquette mixte en deux (socle, puis CRCN)",
  apres.count('class="badge theme"') == 3 and ">D1.3 · D2 · D4</span> <span" in apres, apres)
t("l'outil lit « (+ D1) » comme un domaine", "D1 Les langages pour penser et communiquer" in apres)
# ── le dépôt réel ────────────────────────────────────────────────────────────────────────────────────────────────────
r = subprocess.run([sys.executable, str(ICI / "controle_competences.py")], capture_output=True, text=True, encoding="utf-8")
t("le dépôt réel : chaque compétence se lit en toutes lettres", r.returncode == 0, r.stdout[-1500:])
with tempfile.TemporaryDirectory() as d:
    r = subprocess.run([sys.executable, str(ICI / "controle_competences.py"), d], capture_output=True, text=True, encoding="utf-8")
    t("aucune page lue : sortie 2 (n°299)", r.returncode == 2, r.stdout + r.stderr)
# ── le mode essentiel ────────────────────────────────────────────────────────────────────────────────────────────────
ESS = ('<style>body.essentiel .crcn{display:none}</style><button id="btnEssentiel" onclick="document.body.classList.toggle(\'essentiel\')">'
       'mode</button>%s')
env = dict(os.environ, PLAYWRIGHT_BROWSERS_PATH=os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))


def essentiel(corps):
    with tempfile.TemporaryDirectory() as d:
        pathlib.Path(d, "sequence_a.html").write_text(page(ESS % corps), encoding="utf-8")
        r = subprocess.run([sys.executable, str(ICI / "controle_mode_essentiel.py"), d], capture_output=True, text=True,
                           encoding="utf-8", env=env)
        return r.returncode, r.stdout + r.stderr


code, out = essentiel('<section class="card"><h2>🎯 CRCN mobilisés</h2><div class="crcn">CRCN 1.3 Traiter des données</div></section>')
t("mode essentiel : une carte réduite à son titre est refusée (le cas du jardin)", code == 1 and "CRCN mobilisés" in out, out)
code, out = essentiel('<section class="card"><h2>Hypothèse</h2><p>Écris ton hypothèse.</p><div class="crcn">x</div></section>')
t("mode essentiel : une carte qui garde du contenu passe", code == 0, out)
code, out = essentiel('<section class="card crcn"><h2>Référentiel</h2><p>codes</p></section>')
t("mode essentiel : une carte masquée en entier, titre compris, passe", code == 0, out)
with tempfile.TemporaryDirectory() as d:
    r = subprocess.run([sys.executable, str(ICI / "controle_mode_essentiel.py"), d], capture_output=True, text=True, encoding="utf-8", env=env)
    t("mode essentiel : aucune séquence lue, sortie 2 (n°299)", r.returncode == 2, r.stdout + r.stderr)

print("\n%d / %d" % (sum(res), len(res)))
sys.exit(0 if all(res) else 1)
