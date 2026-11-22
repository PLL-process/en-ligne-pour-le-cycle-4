# -*- coding: utf-8 -*-
"""tests_expliquer_sigles.py — l'outil qui explique les sigles (n°44, complément et décision de Pascal du 22/11/2026).

    python3 _outils/tests_expliquer_sigles.py

Sur des pages fabriquées, sans navigateur :
  1. en clair : « QCM (questionnaire à choix multiples) » à la première apparition du texte, au pluriel après « des »,
     jamais dans le titre, la navigation ou un lien ;
  2. l'infobulle : à la première apparition de la page, puis à la première de chaque séance ; le texte courant passe avant
     un lien ; dans un lien, pas de tabindex ; jamais dans la navigation, un listing, une option de liste ;
  3. le style commun posé une seule fois, et rien d'autre ne change dans le texte ;
  4. relancé, l'outil ne pose rien (n°149) ; le contrôle compte l'infobulle pour une explication ;
  5. `infobuller` (pour les générateurs) : QCM en clair d'abord, les autres sigles en infobulle, et idempotent ;
  6. la barre de navigation en dernier recours : un sigle qui n'apparaît d'abord que là y reçoit l'infobulle, sans
     tabindex ; jamais quand le texte de la page peut la porter.

Sortie : 0 tout passe · 1 un échec (n°299 : ce banc lit toujours ses pages fabriquées, il ne peut pas sortir à 2).
"""
import pathlib
import re
import sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import controle_sigles_expliques as cse  # noqa: E402
import expliquer_sigles as es  # noqa: E402

RES = []


def t(quoi, ok, detail=""):
    RES.append(bool(ok))
    print(("✔" if ok else "✘"), quoi, "" if ok else f"— {detail}")


def texte(src):
    sans_style = re.sub(r'<style id="sigles-css">.*?</style>\n?', "", src, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", sans_style))


PAGE = """<!doctype html><html><head><title>Le QCM et l'IP</title></head><body>
<nav id="navharm"><a href="qcm.html">🧠 QCM</a> · IP</nav>
<h1>Réseau du collège</h1>
<p>Ouvre le <a href="qcm.html">QCM</a> quand tu as fini.</p>
<p>Je sais paramétrer une adresse IP fixe et lire un QCM.</p>
<pre>ping IP</pre>
<select><option>4e_C4.5 — données issues d'un OST.</option></select>
<div class="seance-panel" id="s1"><p>Chaque machine a une IP.</p><p>Une autre IP.</p></div>
<div class="seance-panel" id="s2"><p><button>Voir l'IP</button></p><p>Le routeur garde son IP.</p></div>
<div class="seance-panel" id="s3"><p><a href="#">IP du serveur</a></p></div>
</body></html>"""

# 1. En clair
neuf, ctx = es.poser(PAGE, "QCM")
t("en clair : QCM s'explique à sa première apparition dans le texte, pas dans le titre, la navigation ni le lien",
  neuf and "lire un QCM (questionnaire à choix multiples)." in neuf and "<title>Le QCM et" in neuf
  and '🧠 QCM</a>' in neuf and '>QCM</a> quand' in neuf, ctx)
plur, _ = es.poser("<p>Les élèves font des QCM chaque semaine.</p>", "QCM")
t("en clair : au pluriel après « des »", plur and "des QCM (questionnaires à choix multiples)" in plur, plur)

# 2. L'infobulle
b, info = es.poser_infobulle(PAGE, "IP")
abbrs = re.findall(r'<abbr class="sigle" title="([^"]+)"( tabindex="0")?>IP</abbr>', b or "")
t("infobulle : la page, puis les séances 1, 2 et 3 (quatre infobulles)", len(abbrs) == 4, info)
t("infobulle : le texte courant avant le lien (« adresse IP fixe »), et l'explication du contrôle dans le title",
  b and 'adresse <abbr class="sigle" title="Internet Protocol' in b and abbrs[0][0] == cse.SIGLES["IP"][0]
  .replace("'", "&#x27;"), abbrs[:1])
t("infobulle : en séance 2, le texte passe avant le bouton", b and "<button>Voir l'IP</button>" in b
  and 'garde son <abbr class="sigle"' in b)
t("infobulle : en séance 3, seul un lien porte le sigle — infobulle posée, sans tabindex",
  b and re.search(r'<a href="#"><abbr class="sigle" title="[^"]+">IP</abbr> du serveur</a>', b))
t("infobulle : jamais dans la navigation, le titre, un listing", b and "· IP</nav>" in b and "<pre>ping IP</pre>" in b
  and "<title>Le QCM et l'IP</title>" in b)
o, info_o = es.poser_infobulle(PAGE, "OST")
t("infobulle : jamais dans une option de liste (l'outil le dit)", o is None and "absent" in info_o, info_o)

# 3. Le style, et rien d'autre
t("le style commun posé une fois, dans <head>", b and b.count('id="sigles-css"') == 1
  and b.index('id="sigles-css"') < b.index("</head>"))
t("le texte de la page ne change pas (hors infobulles et style)", b and texte(b) == texte(PAGE))
t("le style affiche l'explication au focus et à l'impression", ":focus::after" in es.CSS_SIGLES
  and "@media print" in es.CSS_SIGLES and 'attr(title)' in es.CSS_SIGLES)

# 4. Idempotence et contrôle
t("relancé, l'outil ne pose rien (n°149)", es.poser_infobulle(b, "IP") == (None, "déjà posé"))
t("le contrôle : sans infobulle, IP jamais expliqué (E) ; avec, expliqué",
  cse.mesurer_source(PAGE).get("IP") == "E" and cse.mesurer_source(b).get("IP") == "ok",
  (cse.mesurer_source(PAGE).get("IP"), cse.mesurer_source(b).get("IP")))

# 5. infobuller, pour un générateur
g = es.infobuller(PAGE)
m = cse.mesurer_source(g)
t("infobuller : QCM écrit en clair, IP en infobulle", "lire un QCM (questionnaire à choix multiples)" in g
  and '<abbr class="sigle"' in g and m.get("QCM") == "ok" and m.get("IP") == "ok", m)
t("infobuller : relancé, la page ne change pas d'un octet", es.infobuller(g) == g)

# 6. Une apparition déjà expliquée en clair ne reçoit pas d'infobulle (vu le 22/11/2026 : « QCM (questionnaire à choix
#    multiples) » s'écrivait deux fois au focus et sur papier)
DOUBLE = """<!doctype html><html><head></head><body>
<p>Ouvre le <a href="qcm.html">QCM</a>.</p>
<div class="seance-panel" id="s1"><p>Le QCM (questionnaire à choix multiples) de l'atelier.</p></div>
<div class="seance-panel" id="s2"><p>Refais le QCM.</p></div>
</body></html>"""
d = es.infobuller(DOUBLE)
t("déjà en clair : pas d'infobulle collée à « QCM (questionnaire à choix multiples) »",
  "QCM</abbr> (questionnaire" not in d and "Le QCM (questionnaire à choix multiples) de" in d, d)
e, _ = es.poser_infobulle(DOUBLE, "QCM")
t("déjà en clair plus bas : le lien qui le précède porte l'infobulle, sans tabindex ; la séance 2 a la sienne ; "
  "l'apparition en clair reste nue",
  e and re.search(r'<a href="qcm.html"><abbr class="sigle" title="[^"]+">QCM</abbr></a>', e)
  and re.search(r'Refais le <abbr class="sigle" title="[^"]+" tabindex="0">QCM</abbr>', e)
  and "Le QCM (questionnaire à choix multiples) de" in e, e)
t("déjà en clair : relancé, rien ne change", es.infobuller(d) == d)

# 7. Une page assemblée de morceaux qui portent déjà des infobulles reçoit le style commun
MORCEAUX = """<!doctype html><html><head><title>Station</title></head><body>
<p>Ouvre le QCM (questionnaire à choix multiples).</p><p>Une adresse <abbr class="sigle" title="Internet Protocol" tabindex="0">IP</abbr>.</p>
</body></html>"""
m7 = es.infobuller(MORCEAUX)
t("infobulles sans style : infobuller pose le style commun, une fois", m7.count('id="sigles-css"') == 1
  and m7.index('id="sigles-css"') < m7.index("</head>") and es.infobuller(m7) == m7, m7)
SANS_HEAD = MORCEAUX.replace("<head><title>Station</title></head>", '<meta charset="utf-8"><title>Station</title><style>p{}</style>')
m8 = es.infobuller(SANS_HEAD)
t("infobulles sans style, page sans </head> : le style se pose avant la première feuille de style",
  m8.count('id="sigles-css"') == 1 and m8.index('id="sigles-css"') < m8.index("<style>p{}") and es.infobuller(m8) == m8, m8)

# 8. La barre de navigation en dernier recours (22/11/2026) : « 🧠 QCM » d'une synthèse, et rien d'autre
SYNTHESE = """<!doctype html><html><head><title>Synthèse</title></head><body>
<nav id="navharm"><a href="../index.html">⌂ Accueil</a><a href="../qcm_x.html">🧠 QCM</a></nav>
<h1>Ce qu'il faut retenir</h1><p>Une adresse IP identifie une machine.</p>
</body></html>"""
g8 = es.infobuller(SYNTHESE)
m8b = cse.mesurer_source(g8)
t("barre : « QCM » seulement dans la barre reçoit l'infobulle, sans tabindex, et la page est expliquée",
  '<a href="../qcm_x.html">🧠 <abbr class="sigle" title="questionnaire à choix multiples">QCM</abbr></a>' in g8
  and m8b.get("QCM") == "ok" and m8b.get("IP") == "ok" and g8.count('id="sigles-css"') == 1, (m8b, g8[:400]))
t("barre : relancé, rien ne change ; le texte de la page ne bouge pas", es.infobuller(g8) == g8
  and texte(g8) == texte(SYNTHESE))
PLUS_BAS = SYNTHESE.replace("<p>Une adresse IP", "<p>" + "Un réseau relie des machines entre elles. " * 6
                            + "</p><p>Le QCM (questionnaire à choix multiples) te prépare.</p><p>Une adresse IP")
g9 = es.infobuller(PLUS_BAS)
t("barre : expliqué en clair plus bas (P), la barre reçoit l'infobulle, l'explication en clair reste",
  cse.mesurer_source(PLUS_BAS).get("QCM") == "P" and
  'class="sigle" title="questionnaire à choix multiples">QCM</abbr></a>' in g9
  and "Le QCM (questionnaire à choix multiples) te prépare" in g9 and cse.mesurer_source(g9).get("QCM") == "ok", g9)
AILLEURS = SYNTHESE.replace("<p>Une adresse IP", "<p>Refais le QCM demain.</p><p>Une adresse IP")
g10 = es.infobuller(AILLEURS)
t("barre : le sigle a aussi sa place dans le texte, la barre n'est pas touchée",
  '>🧠 QCM</a></nav>' in g10 and cse.mesurer_source(g10).get("QCM") == "ok", g10)

print(f"\n{sum(RES)} / {len(RES)}")
sys.exit(0 if all(RES) else 1)
