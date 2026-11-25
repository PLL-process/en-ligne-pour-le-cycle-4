"""Banc : un bloc incrusté réécrit garde les infobulles de sigles qu'une vague y a posées (n°44, 25/11/2026).

    python3 tests_incrustations_infobulles.py      # sortie 0 si tout passe, 1 sinon, 2 si l'outil ne se charge pas
"""
import pathlib
import sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
try:
    import incrustations as I
    I.garder_infobulles
except Exception as e:  # noqa: BLE001
    print("⛔ EN PANNE : incrustations.garder_infobulles introuvable (%s)" % e)
    raise SystemExit(2)

LED = '<abbr class="sigle" title="Light-Emitting Diode, diode électroluminescente" tabindex="0">LED</abbr>'
RES = []


def t(nom, ok, detail=""):
    RES.append(bool(ok))
    print(("✔ " if ok else "✘ ") + nom + ("" if ok else "\n   " + detail[:300]))


ancien = "<!-- d -->\n<dl><dt>%s</dt><dd>une LED rouge</dd></dl>\n<!-- f -->" % LED
neuf = "<!-- d -->\n<dl><dt>LED</dt><dd>une LED rouge</dd></dl>\n<!-- f -->"
t("bloc identique au balisage près : l'infobulle reste à sa place, la deuxième apparition reste nue",
  I.garder_infobulles(ancien, neuf) == ancien, I.garder_infobulles(ancien, neuf))

neuf2 = "<!-- d -->\n<dl><dt>LED</dt><dd>une LED verte, plus économe</dd></dl>\n<!-- f -->"
r2 = I.garder_infobulles(ancien, neuf2)
t("bloc réécrit ailleurs : l'infobulle passe dans la nouvelle version", r2.count(LED) == 1
  and r2.startswith("<!-- d -->\n<dl><dt>" + LED) and "LED verte, plus économe" in r2, r2)

neuf3 = "<!-- d -->\n<dl><dd>une LED rouge</dd></dl>\n<!-- f -->"
t("autant d'apparitions ? non : rien n'est posé au hasard, infobuller s'en chargera",
  I.garder_infobulles(ancien, neuf3) == neuf3, I.garder_infobulles(ancien, neuf3))

attr = '<!-- d -->\n<p title="LED">LED</p>\n<!-- f -->'
t("un sigle dans un attribut ne compte pas", I.garder_infobulles('<!-- d -->\n<p title="LED">%s</p>\n<!-- f -->' % LED, attr)
  == '<!-- d -->\n<p title="LED">%s</p>\n<!-- f -->' % LED)

t("sans infobulle dans l'ancien bloc, le nouveau est rendu tel quel", I.garder_infobulles(neuf, neuf2) == neuf2)

print("\n%d / %d" % (sum(RES), len(RES)))
raise SystemExit(0 if all(RES) else 1)
