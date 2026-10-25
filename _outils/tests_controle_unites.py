# -*- coding: utf-8 -*-
"""tests_controle_unites.py — le banc de la règle d'or n°312 : une unité se lit en toutes lettres.

Rejoue le cas qui a fait naître la règle (le tableau « Les chiffres pour choisir » de Chengdu : « 1,2 W ·
0,4 W · 12 W » sans le mot « watts »), les cas qui doivent passer (le nom entre parenthèses, le nom dans
l'intitulé du tableau, une unité connue de l'école, un listing de code, un schéma intégré), la frontière
des zones (un nom écrit dans l'activité d'avant ne compte pas ; une question de QCM se lit seule), les
fausses pistes écartées (adresse MAC, « niveau 2 A »), l'option seule à porter le nom dans un choix (refusée ;
écrite en toutes lettres, elle passe), la panne d'une racine vide (règle d'or n°299) et le dépôt réel.

Usage : python3 _outils/tests_controle_unites.py
"""
import contextlib, io, os, pathlib, shutil, subprocess, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_unites as C  # noqa: E402

PAGE = '<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>t</title></head><body>%s</body></html>\n'
ok = ko = 0


def verifier(nom, cond, detail=""):
    global ok, ko
    if cond:
        ok += 1
        print("✅", nom)
    else:
        ko += 1
        print("❌", nom, detail)


def jouer(fichiers):
    """Écrit les pages dans une racine jetable (sous theme-x/), lance le contrôle, rend (code, sortie)."""
    racine = pathlib.Path(tempfile.mkdtemp())
    try:
        for rel, contenu in fichiers.items():
            p = racine / "theme-1-essai" / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(contenu, encoding="utf-8")
        ancien = C.DEPOT
        C.DEPOT = str(racine)
        s, e = io.StringIO(), io.StringIO()
        try:
            with contextlib.redirect_stdout(s), contextlib.redirect_stderr(e):
                code = C.main([str(racine)])
        finally:
            C.DEPOT = ancien
        return code, s.getvalue() + e.getvalue()
    finally:
        shutil.rmtree(racine, ignore_errors=True)


TABLEAU_CHENGDU = ('<h2>Activité 1 — Une fonction, trois principes</h2><table><tr><th>Critère</th><th>P1</th><th>P2</th></tr>'
                   '<tr><td>Prix</td><td>25 €</td><td>900 €</td></tr>'
                   '<tr><td>Consommation</td><td>1,2 W</td><td>0,4 W</td></tr></table>')

# 1. le cas d'origine : refusé
code, out = jouer({"sequence_a.html": PAGE % TABLEAU_CHENGDU})
verifier("le tableau de Chengdu sans « watts » est refusé", code == 1 and "W sans « watts »" in out, out)

# 2. le nom entre parenthèses à la première apparition : passe
code, out = jouer({"sequence_a.html": PAGE % TABLEAU_CHENGDU.replace("1,2 W</td>", "1,2 W (watts)</td>")})
verifier("« 1,2 W (watts) » dans le tableau passe", code == 0, out)

# 3. le nom dans l'intitulé de la ligne : passe
code, out = jouer({"sequence_a.html": PAGE % TABLEAU_CHENGDU.replace("<td>Consommation</td>", "<td>Consommation (en watts, W)</td>")})
verifier("le nom dans l'intitulé du tableau passe", code == 0, out)

# 4. frontière des zones : un nom écrit dans l'activité d'avant ne compte pas
deux = ('<h2>Activité 1 — Le besoin</h2><p>La station consomme 6 W (watts) en continu.</p>'
        '<h2>Activité 2 — La réserve</h2><p>Avec 6 W pendant 72 h, il faut 432 Wh (wattheures).</p>')
code, out = jouer({"sequence_a.html": PAGE % deux})
verifier("le nom de l'activité 1 ne vaut pas pour l'activité 2", code == 1 and "[Activité 2" in out and "W sans « watts »" in out, out)

# 5. watt et wattheure ne se confondent pas
code, out = jouer({"sequence_a.html": PAGE % '<h2>Activité 1</h2><p>Il faut 432 Wh, soit une puissance en watts.</p>'})
verifier("« watts » ne nomme pas « Wh »", code == 1 and "Wh sans « wattheures »" in out, out)

# 6. unités connues, code et schéma : pas exigés
code, out = jouer({"sequence_a.html": PAGE % ('<h2>Activité 1</h2><p>50 km/h, 26 °C, 17,4 kg, 3 min, 25 %.</p>'
                                               '<pre>tension = 5 V</pre><code>12 V</code>'
                                               '<svg><text>12 V</text></svg>')})
verifier("unités connues, listing et schéma intégré ne sont pas exigés", code == 0, out)

# 7. fausses pistes : adresse MAC, « niveau 2 A », symbole collé à un mot
code, out = jouer({"sequence_a.html": PAGE % ('<h2>Activité 1</h2><p>MAC : 00:1A:2B:3C. Aide de niveau 2 A : regarde. '
                                               '12 Volts. 20 W/m² au soleil.</p>')})
verifier("adresse MAC, « niveau 2 A », « 12 Volts », « W/m² » ne déclenchent rien", code == 0, out)

# 7 bis. un Gantt : « <td>2</td><td>A</td> » (une durée, puis une tâche) n'est pas « 2 A »
code, out = jouer({"atelier_a.html": PAGE % ('<h2>Activité 1</h2><table><tr><td>Relever</td><td>2</td><td>A</td></tr></table>')})
verifier("Gantt : une durée suivie d'une lettre de tâche n'est pas une intensité", code == 0, out)

# 8. QCM : une question se lit seule
qcm = ('<script>const QUESTIONS = [\n'
       '{c:"C4.1",q:"La batterie fait 12 V. Que vaut…",o:["a","b"],r:0,expl:"La tension se mesure en volts."},\n'
       '{c:"C4.1",q:"Le moteur consomme 2 A.",o:["a","b"],r:1,expl:"Rien."}\n'
       '];</script>')
code, out = jouer({"qcm_a.html": PAGE % qcm})
verifier("QCM : la question 1 (« volts » dans l'explication) passe, la question 2 est refusée",
         code == 1 and "[question 2] A sans « ampères »" in out and "question 1" not in out, out)

# 8 bis. une option seule à porter le nom se distingue : refusée ; écrite en toutes lettres, elle passe
seule = ('<script>const QUESTIONS = [\n'
         '{c:"5e",q:"Quelle règle de sécurité ?",o:["des gants isolants","il ne manipule que du 5 V (volts)",'
         '"il coupe le disjoncteur"],r:1,expl:"Très basse tension."}\n];</script>')
code, out = jouer({"qcm_a.html": PAGE % seule})
verifier("QCM : la bonne réponse seule à porter « (volts) » est refusée",
         code == 1 and "[question 1] seule option à porter le nom" in out, out)
code, out = jouer({"qcm_a.html": PAGE % seule.replace("du 5 V (volts)", "du 5 volts")})
verifier("QCM : la même option écrite « 5 volts » passe", code == 0, out)
liste = ('<h2>Activité 1</h2><p>Quelle source ?</p><select id="q1"><option value="">— je choisis —</option>'
         '<option>le secteur</option><option value="la pile 9 V">la pile 9 V (volts)</option><option>le panneau</option></select>'
         '<p>Réglage :</p><select id="src"><option>Pile 9 V (volts)</option><option>Secteur</option></select>')
code, out = jouer({"sequence_a.html": PAGE % liste})
verifier("liste-question à une seule option nommée refusée ; liste de réglage (sans « — je choisis — ») ignorée",
         code == 1 and "[liste q1] seule option" in out and "liste src" not in out, out)

# 9. synthèse professeur : hors périmètre
code, out = jouer({"sequence_a.html": PAGE % "<h2>Activité 1</h2><p>12 V (volts)</p>",
                   "synthese_professeur_a.html": PAGE % "<p>12 V</p>"})
verifier("une synthèse professeur n'est pas lue", code == 0, out)

# 10. règle n°299 : une racine sans page élève est une panne
racine = tempfile.mkdtemp()
try:
    ancien = C.DEPOT; C.DEPOT = racine
    e = io.StringIO()
    with contextlib.redirect_stderr(e), contextlib.redirect_stdout(io.StringIO()):
        code = C.main([racine])
    C.DEPOT = ancien
    verifier("une racine vide sort en panne (2)", code == 2 and "PANNE" in e.getvalue(), e.getvalue())
finally:
    shutil.rmtree(racine, ignore_errors=True)

# 11. le dépôt réel, lancé comme on le lance vraiment
r = subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "controle_unites.py"), "--muet"],
                   capture_output=True, text=True, timeout=600)
verifier("le dépôt réel est lu (sortie 0 ou 1, jamais 2)", r.returncode in (0, 1) and "page(s) lues" in r.stdout,
         r.stdout + r.stderr)

print("\n%d / %d" % (ok, ok + ko))
sys.exit(0 if ko == 0 else 1)
