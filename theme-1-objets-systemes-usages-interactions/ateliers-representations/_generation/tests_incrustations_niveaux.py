"""Banc : une incrustation prend le niveau de titre que la séquence lui laisse (26/11/2026).

Page ouverte (règle d'or n°361), cinq séquences sautaient un niveau de titre : un h4 incrusté sous le h2 d'une activité
(3e, 4e et 5e_C3.1), ou les exercices en h5 sous les intertitres h3 du cours (5e_C1.3, 4e_C2.1, 5e_C2.1, C3.1,
5e_C4.1). Le générateur lit désormais le dernier titre écrit avant le point de pose, et corrige le niveau par
`aria-level` — la balise, donc le style, ne change pas.

    python3 tests_incrustations_niveaux.py      # sortie 0 si tout passe, 1 sinon, 2 si l'outil ne se charge pas
"""
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
try:
    import incrustations as I
    import moteur as M
    I.dernier_niveau, I.niveau_de_pose, M.niveau_aria
except Exception as e:  # noqa: BLE001
    print("⛔ EN PANNE : incrustations.dernier_niveau / niveau_de_pose ou moteur.niveau_aria introuvable (%s)" % e)
    raise SystemExit(2)

RES = []


def t(nom, ok, detail=""):
    RES.append(bool(ok))
    print(("✔ " if ok else "✘ ") + nom + ("" if ok else "\n   " + str(detail)[:300]))


# ── le dernier titre avant le point de pose ──────────────────────────────────────────────────────────────────────
t("le dernier titre écrit compte", I.dernier_niveau("<h1>a</h1><h2>b</h2><p>x</p>") == 2)
t("un aria-level corrige la balise", I.dernier_niveau('<h2>b</h2><h4 aria-level="3">c</h4>') == 3)
t("les titres d'un script, d'un style ou d'un commentaire ne comptent pas",
  I.dernier_niveau("<h2>b</h2><script>x='<h5>'</script><style>h6{}</style><!-- <h5>z</h5> -->") == 2,
  I.dernier_niveau("<h2>b</h2><script>x='<h5>'</script><style>h6{}</style><!-- <h5>z</h5> -->"))
t("un élément role=heading compte par son aria-level",
  I.dernier_niveau('<h2>b</h2><div role="heading" aria-level="3">c</div>') == 3)
t("aucun titre : None", I.dernier_niveau("<p>rien</p>") is None)
t("<header> n'est pas un titre", I.dernier_niveau("<h2>b</h2><header>x</header>") == 2)

# ── le niveau de pose ────────────────────────────────────────────────────────────────────────────────────────────
t("un h4 sous un h2 descend à 3", I.niveau_de_pose({"balise": "h4"}, "<h2>Activité 1</h2>") == 3)
t("un h4 sous un h3 garde 4", I.niveau_de_pose({"balise": "h4"}, "<h2>a</h2><h3>b</h3>") == 4)
t("un h3 sous un h5 garde 3 (remonter est permis)", I.niveau_de_pose({"balise": "h3"}, "<h5>a</h5>") == 3)
t("sans titre avant : la balise", I.niveau_de_pose({"balise": "h4"}, "<p>x</p>") == 4)

# ── ce que le moteur écrit ───────────────────────────────────────────────────────────────────────────────────────
t("niveau égal à la balise : rien n'est ajouté", M.niveau_aria("h4", 4) == "" and M.niveau_aria("h4", None) == "")
t("niveau différent : aria-level", M.niveau_aria("h5", 4) == ' aria-level="4"')


class Atelier:
    COURS = {"5e": "<h3>Le besoin</h3><p>x</p><h3>Lire</h3>"}


c = M.bloc_cours(Atelier, "5e", niveau=5)
t("les intertitres du cours prennent le niveau demandé, balise h3 gardée",
  c.count('<h3 aria-level="5">') == 2 and "<h3>" not in c, c)
t("cours sous un h2 : intertitres inchangés", M.bloc_cours(Atelier, "5e", niveau=3).count("<h3>") == 2)

# ── sur une vraie incrustation (bête à cornes, 3e_C3.1 : un h4 posé sous le h2 de l'activité) ───────────────────────
import incrustations_table as table  # noqa: E402

inc = next((x for x in table.INCRUSTATIONS if x["id"] == "bcm-3e-shenzhen-c3"), None)
if inc is None:
    t("l'incrustation bcm-3e-shenzhen-c3 existe", False, "absente de incrustations_table")
else:
    html = I.section(inc, I.niveau_de_pose(inc, "<h2>Activité 1</h2>"))
    t("titre de l'incrustation : h4 lu comme un niveau 3", '<h4 id="incruste-bcm-3e-shenzhen-c3-titre" aria-level="3">' in html,
      html[:300])
    import re
    h5 = re.findall(r'<h5 id="[^"]+"[^>]*>', html)
    t("ses exercices : chaque h5 lu comme un niveau 4", h5 and all('aria-level="4"' in x for x in h5), h5)
    html2 = I.section(inc, I.niveau_de_pose(inc, "<h2>a</h2><h3>b</h3>"))
    t("sous un h3 : ni le titre ni les exercices ne portent d'aria-level",
      re.findall(r'<h[45] id="[^"]+"[^>]*>', html2) and not any("aria-level" in x for x in re.findall(r'<h[45] id="[^"]+"[^>]*>', html2)))

n = sum(RES)
print("%d / %d" % (n, len(RES)))
raise SystemExit(0 if n == len(RES) else 1)
