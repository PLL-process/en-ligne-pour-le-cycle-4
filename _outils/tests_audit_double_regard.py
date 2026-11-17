# -*- coding: utf-8 -*-
"""Banc des outils de l'audit « double regard » (17/11/2026) : n°337, n°338, n°339 et la correction des billets.

  trois_lignes.py            la carte se pose en tête du volet #ouverture, se réécrit sans se doubler, refuse une
                             rubrique vide ou trop longue, refuse une page sans volet ; --etat la juge.
  qcm_aides/poser.py         sur une copie du QCM de Shenzhen : rejouable à l'identique, refuse une notion inconnue,
                             un piège de moins de trois questions, une notion dans deux pièges.
  controle_memes_nombres.py  N1 (annonce du QCM fausse), N2 (« au moins N » qui change), N3 (bilan recopié).
  corriger_billet.py         la correction du billet : la bonne réponse et le pourquoi de chaque leurre ; un billet
                             dont le vérificateur contredit la page est refusé.

Usage : python3 _outils/tests_audit_double_regard.py      Sortie : 0 tout passe · 1 un cas échoue.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

OUT = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.dirname(OUT)
sys.path.insert(0, OUT)
sys.path.insert(0, os.path.join(OUT, "qcm_aides"))
import trois_lignes  # noqa: E402
import poser  # noqa: E402

ok = ko = 0


def cas(nom, cond, detail=""):
    global ok, ko
    if cond:
        ok += 1; print("  ✔ " + nom)
    else:
        ko += 1; print("  ✘ " + nom + (" — " + detail if detail else ""))


def lance(*args):
    r = subprocess.run([sys.executable] + list(args), capture_output=True, text=True, cwd=DEPOT)
    return r.returncode, r.stdout + r.stderr


SEQ = '''<html><head><style>body{}</style></head><body>
<details class="rappel-ouverture" id="ouverture" open>
<summary>📖 Rappel</summary>
<div class="badges"><span>5e</span></div>
<section class="card"><h2>La situation</h2></section>
</details>
<div class="seance-tabs"></div>
<!-- mode-mission v1 : début -->
</body></html>'''
D = {"apprendre": ["Ceci."], "savoir_faire": ["Faire cela."], "reussir": ["Comparer."]}

print("trois_lignes.py")
s1 = trois_lignes.poser(SEQ, D)
cas("la carte se pose dans le volet, après les badges, avant les onglets",
    s1.find('id="trois-lignes"') > s1.find('<div class="badges">') and s1.find('id="trois-lignes"') < s1.find("seance-tabs"))
cas("le style se pose une fois", s1.count(".trois-lignes-liste{") == 1)
cas("la carte porte son propre cadre (gabarits sans style de carte)", "section.trois-lignes{max-width:960px" in s1)
ancien = s1.replace(trois_lignes.CSS, "/* avant de commencer, trois lignes : apprendre, savoir faire, réussir (règle d'or n°337) */\n"
                    ".trois-lignes-liste{list-style:none}\n.trois-lignes-liste li{padding:0}\n")
s1b = trois_lignes.poser(ancien, D)
cas("un style plus ancien est remplacé, pas doublé", s1b.count(".trois-lignes-liste{") == 1 and "section.trois-lignes{" in s1b)
s2 = trois_lignes.poser(s1, dict(D, apprendre=["Autre chose."]))
cas("reposer réécrit la carte sans la doubler", s2.count('id="trois-lignes"') == 1 and "Autre chose." in s2 and "Ceci." not in s2)
cas("jugée conforme", trois_lignes.juger(s2) == [], str(trois_lignes.juger(s2)))
for nom, d in (("une rubrique vide est refusée", dict(D, reussir=[])),
               ("une rubrique de plus de 40 mots est refusée", dict(D, apprendre=["mot " * 41]))):
    try:
        trois_lignes.poser(SEQ, d); cas(nom, False)
    except trois_lignes.Refus:
        cas(nom, True)
try:
    trois_lignes.poser("<html><body><section class=\"card\"></section></body></html>", D); cas("une page sans volet #ouverture est refusée", False)
except trois_lignes.Refus:
    cas("une page sans volet #ouverture est refusée", True)
cas("une page sans carte est jugée", trois_lignes.juger(SEQ) == ["pas de carte « Avant de commencer »"])

print("qcm_aides/poser.py")
QCM = os.path.join(DEPOT, "theme-1-objets-systemes-usages-interactions/C2-decrire-les-interactions-entre-un-objet-ou/5e/5e_C2.1/qcm_5e_C2_shenzhen_station_velos.html")
DQ = json.load(open(os.path.join(os.path.dirname(QCM), "qcm_aides_5e_C2.1.json"), encoding="utf-8"))
s = open(QCM, encoding="utf-8").read()
cas("le QCM de Shenzhen est à jour (rejouable à l'identique)", poser.appliquer(s, DQ) == s)
for nom, mod in (("une notion inconnue est refusée", lambda d: d["pieges"]["lieu"]["notions"].append("N'existe pas")),
                 ("un piège de deux questions est refusé", lambda d: d["pieges"]["lieu"].update(notions=d["pieges"]["lieu"]["notions"][:2])),
                 ("une notion dans deux pièges est refusée", lambda d: d["pieges"]["lieu"]["notions"].append("Définition"))):
    d = json.loads(json.dumps(DQ)); mod(d)
    try:
        poser.appliquer(s, d); cas(nom, False)
    except poser.Refus:
        cas(nom, True)
d = json.loads(json.dumps(DQ)); d["avant_de_commencer"]["revoir"] = ["Une autre ligne."]
u = poser.appliquer(s, d)
cas("changer les données réécrit la carte, une seule fois", u.count('id="trois-lignes"') == 1 and "Une autre ligne." in u)

print("controle_memes_nombres.py")
tmp = tempfile.mkdtemp()
try:
    lot = os.path.join(tmp, "theme-x", "lot")
    os.makedirs(lot)
    q = 'const QUESTIONS = [\n{c:"C1",n:"a",q:"x",img:{src:"i",alt:"j"},o:[],r:0},\n{c:"C1",n:"b",q:"y",o:[],r:0}\n];\nconst msg= note>=16?"Remarquable ! Copié.":'
    open(os.path.join(lot, "qcm_lot.html"), "w").write(q)
    open(os.path.join(lot, "README.md"), "w").write("QCM : 2 questions, dont 1 illustrées.")
    open(os.path.join(lot, "sequence_lot.html"), "w").write(
        "<section><h2>Activité</h2><p>Production : au moins six interacteurs.</p><p>Critère : au moins 6 interacteurs.</p></section>"
        "<p>Le QCM : <b>3 questions</b>, dont <b>1 illustrées</b></p>")
    lot2 = os.path.join(tmp, "theme-x", "lot2"); os.makedirs(lot2)
    open(os.path.join(lot2, "qcm_lot2.html"), "w").write(q)
    open(os.path.join(lot2, "sequence_l2.html"), "w").write(
        "<section><h2>Recenser</h2><p>au moins huit interacteurs</p><p>au moins 6 interacteurs</p></section>")
    code, sortie = lance(os.path.join(OUT, "controle_memes_nombres.py"), "--strict", tmp)
    cas("N1 : l'annonce fausse de la séquence est vue, celle du README juste ne l'est pas",
        "✘ N1" in sortie and "lot/sequence_lot.html" in sortie and "README.md" not in sortie, sortie)
    cas("N2 : « au moins huit » et « au moins 6 » dans le même bloc", "N2" in sortie and "6 / 8" in sortie, sortie)
    cas("N2 : six et 6 sont le même nombre", sortie.count("✘ N2") == 1, sortie)
    cas("N3 : le même bilan dans deux lots", "N3" in sortie, sortie)
    cas("--strict sort à 1", code == 1)
finally:
    shutil.rmtree(tmp)

print("corriger_billet.py")
tmp = tempfile.mkdtemp()
try:
    page = os.path.join(tmp, "sequence_b.html")
    radio = lambda i, v, p="": '<input type="radio" name="be_1" id="be_1__%d" value="%s"%s><label for="be_1__%d">%s</label>' % (
        i, v, (' data-pourquoi="%s"' % p) if p else "", i, v)
    corps = ('<section class="card"><h2>🎫 Billet d\'entrée</h2><fieldset class="qcm-groupe" id="be_1"><legend>Q ?</legend>'
             + radio(1, "juste") + radio(2, "faux", "parce que non") + radio(3, "je ne sais pas encore")
             + '</fieldset><button data-check="0">Vérifier</button>\n<p class="feedback" id="fb0" role="status"></p></section>')
    open(page, "w").write("<html><body>%s<script>const att={be_1:\"juste\"};</script></body></html>" % corps)
    code, sortie = lance(os.path.join(OUT, "corriger_billet.py"), "--ecrire", page)
    t = open(page).read()
    cas("la correction est posée sous le message", t.find("correction-billet") > t.find('id="fb0"') > 0, sortie)
    cas("la bonne réponse et le pourquoi du leurre ; « je ne sais pas encore » laissé de côté",
        "✅ <b>juste</b>" in t and "parce que non" in t and "je ne sais pas encore</label>" in t and t.count("✘ «") == 1)
    lance(os.path.join(OUT, "corriger_billet.py"), "--ecrire", page)
    cas("rejouer ne double pas la correction", open(page).read().count("correction-billet") == 1)
    open(page, "w").write("<html><body>%s<script>const att={be_1:\"faux\"};</script></body></html>" % corps)
    code, sortie = lance(os.path.join(OUT, "corriger_billet.py"), page)
    cas("un vérificateur qui contredit la page est refusé", code == 1 and "refus" in sortie, sortie)
finally:
    shutil.rmtree(tmp)

print("%d / %d" % (ok, ok + ko))
sys.exit(1 if ko else 0)
