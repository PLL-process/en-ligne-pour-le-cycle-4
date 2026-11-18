#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Banc de `controle_consignes_a_la_ligne.py` (règle d'or n°342) : des lignes connues, puis l'outil lancé comme on le
lance vraiment, en sous-processus (n°299, second corollaire), sur des pages écrites pour l'occasion."""
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import controle_consignes_a_la_ligne as C  # noqa: E402

OUTIL = os.path.join(ICI, "controle_consignes_a_la_ligne.py")
ok = ko = 0


def verifier(nom, obtenu, attendu):
    global ok, ko
    if obtenu == attendu:
        ok += 1
        print("✅ " + nom)
    else:
        ko += 1
        print("✘ %s : obtenu %r, attendu %r" % (nom, obtenu, attendu))


def codes(html):
    corps = "<body>" + html + "</body>"
    return sorted(c for frag in C.consignes(corps) for l in C.lignes(frag) for c, _ in C.ecarts_ligne(l))


# ── les lignes ──
verifier("deux étapes numérotées sur une ligne → N1",
         codes('<div class="consigne">① Lis le programme. ② Classe chaque donnée.</div>'), ["N1"])
verifier("deux étapes numérotées, chacune sur sa ligne → rien",
         codes('<div class="consigne"><b>Consigne :</b><br>① Lis le programme.<br>② Classe chaque donnée.</div>'), [])
verifier("deux actions cousues par « ; » → N2",
         codes('<div class="consigne">Lis le programme ; classe chaque donnée.</div>'), ["N2"])
verifier("un circonstant, puis deux actions cousues par « , puis » → N2",
         codes('<p class="consigne-tableau">Pour chaque essai, compare ce que tu observes au résultat attendu, '
               'puis choisis : conforme ou non conforme.</p>'), ["N2"])
verifier("deux phrases à l'impératif sur une ligne → N2",
         codes('<p><b>Consigne :</b> la bouée embarque ce programme. Lis-le. Réponds aux questions.</p>'), ["N2"])
verifier("« lis-le, puis réponds » (pronom accroché au verbe) → N2",
         codes('<p><b>Consigne :</b> lis-le, puis réponds.</p>'), ["N2"])
verifier("trois actions en liste, séparées par des virgules → N2",
         codes('<div class="consigne">① Exécute les 3 tests du banc, compare « attendu » et « obtenu ».</div>'), ["N2"])
verifier("un circonstant suivi d'une virgule n'est pas une deuxième action → rien",
         codes('<div class="consigne"><b>Consigne :</b> pour chaque fonction, choisis le bon élément.</div>'), [])
verifier("deux actions jointes par « et » → N3 (à juger)",
         codes('<div class="consigne">Lis le programme et réponds aux questions.</div>'), ["N3"])
verifier("« le programme », « la classe », « la note » ne sont pas des actions → rien",
         codes('<div class="consigne">Le programme de la classe compte trois lignes ; la note finale est sur 20.</div>'),
         [])
verifier("une phrase de contexte, puis une action à la ligne → rien",
         codes('<div class="consigne"><b>Consigne :</b> Météo-France recalibre ses niveaux : le seuil passe à '
               '60 km/h.<br>① Modifie la ligne 2.<br>② Réponds aux questions.</div>'), [])
verifier("a) … ; b) … sur une ligne → N1",
         codes('<div class="consigne"><b>Consigne :</b> a) calcule la sortie ; b) analyse ensuite le bug.</div>'),
         ["N1"])
verifier("le code à recopier n'est pas lu (son « ; » n'enchaîne rien) → rien",
         codes('<div class="consigne">① Ajoute la ligne <code>a = 1; b = 2; print(a)</code> à la fin.</div>'), [])
verifier("un listing <pre> n'est pas lu → rien",
         codes('<div class="consigne">① Recopie ce bloc :<pre>lis(a); classe(b)</pre></div>'), [])
verifier("une consigne imbriquée dans une autre se lit une fois",
         len(C.consignes('<body><div class="consigne"><p class="consigne-grille">Donne le rôle.</p></div></body>')), 1)
verifier("une classe qui nomme la consigne (« verif-consigne », « bac-consigne-ms ») est lue",
         len(C.consignes('<body><p class="verif-consigne">Coche.</p><div class="ms-seul bac-consigne-ms">Va.</div>'
                         '</body>')), 2)
verifier("« consignes » au pluriel dans une autre classe n'est pas une consigne",
         len(C.consignes('<body><div class="resume-consignes-x">Rien.</div></body>')), 0)

# ── l'outil, lancé comme on le lance ──
with tempfile.TemporaryDirectory() as d:
    bonne = os.path.join(d, "bonne.html")
    mauvaise = os.path.join(d, "mauvaise.html")
    vide = os.path.join(d, "vide.html")
    open(bonne, "w", encoding="utf-8").write(
        '<html><body><div class="consigne"><b>Consigne :</b><br>① Lis.<br>② Réponds.</div></body></html>')
    open(mauvaise, "w", encoding="utf-8").write(
        '<html><body><div class="consigne">Lis le programme ; classe chaque donnée, puis relève les lignes.</div>'
        '</body></html>')
    open(vide, "w", encoding="utf-8").write("<html><body><p>Rien à faire.</p></body></html>")

    def lancer(*args):
        r = subprocess.run([sys.executable, OUTIL] + list(args), capture_output=True, text=True)
        return r.returncode, r.stdout

    code, sortie = lancer("--strict", bonne)
    verifier("--strict sur une page aux consignes à la ligne → sortie 0", code, 0)
    verifier("… et elle annonce ce qu'elle a lu", "1 page(s) lues · 1 consigne(s)" in sortie, True)
    code, sortie = lancer("--strict", mauvaise)
    verifier("--strict sur une page qui enchaîne → sortie 1", code, 1)
    verifier("… et l'écart est cité", "N2 3 actions enchaînées" in sortie, True)
    code, _ = lancer(mauvaise)
    verifier("sans --strict, c'est une mesure → sortie 0", code, 0)
    code, sortie = lancer("--strict", vide)
    verifier("une page sans consigne → sortie 0, « 0 consigne(s) » dit", (code, "0 consigne(s)" in sortie), (0, True))
    code, _ = lancer(os.path.join(d, "absente.html"))
    verifier("aucune page lue → sortie 2 (n°299)", code, 2)
    j = os.path.join(d, "releve.json")
    code, _ = lancer("--json", j, mauvaise)
    verifier("--json écrit le relevé", (code, os.path.exists(j)), (0, True))

print("%d / %d" % (ok, ok + ko))
sys.exit(1 if ko else 0)
