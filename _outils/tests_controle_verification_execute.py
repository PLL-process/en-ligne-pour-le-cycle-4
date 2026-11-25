# -*- coding: utf-8 -*-
"""tests_controle_verification_execute.py — le contrôle n°333 d'abord éprouvé sur des cas dont on connaît la réponse
(règle n°194), puis sur la page qui l'a fait naître, telle qu'elle était avant sa correction (git, si disponible).

Sortie : 0 tout passe · 1 un échec.
Usage : python3 _outils/tests_controle_verification_execute.py
"""
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import controle_verification_execute as cve  # noqa: E402

EDITEUR = '<textarea id="clTa"></textarea>'
PY = '<textarea id="py_a4" class="editeur-py-code"></textarea>'


def page(corps, js):
    return "<html><body>%s<script>%s</script></body></html>" % (corps, js)


CAS = [
    ("motifs seuls, lecture directe", "T", page(EDITEUR, 'const CHECKS = { 4: function(){ const code=$("clTa").value; '
                                                       'return {valide: /SEUIL\\s*=\\s*60/.test(code)}; } };')),
    ("motifs seuls, par une fonction qui lit l'éditeur", "T",
     page(EDITEUR, 'function codeSans(){ return $("clTa").value.replace(/#.*/g, ""); }\n'
                   'const CHECKS = { 4: function(){ const code=codeSans(); return {valide: (code.match(/True/g)||[]).length>=2}; } };')),
    ("exécution directe", "X", page(EDITEUR, 'const CHECKS = { 4: function(){ const r=BancPython.executer($("clTa").value, {}); '
                                            'return {valide: r.ok}; } };')),
    ("exécution par une fonction de la page", "X",
     page(EDITEUR, 'function essayer(c){ return BancPython.executer(c, {}); }\n'
                   'const CHECKS = { 4: function(){ const code=$("clTa").value, r=essayer(code); return {valide: r.ok}; } };')),
    ("exécution ET motif qui peut décider", "M",
     page(EDITEUR, 'const CHECKS = { 4: function(){ const code=$("clTa").value, r=BancPython.executer(code, {}); '
                   'return {valide: r.ok && code.includes("elif")}; } };')),
    ("exécution, motif seulement dans un conseil de forme", "X",
     page(EDITEUR, 'function conseilForme(c){ return /if\\s+\\d/.test(c) ? "écris la constante" : ""; }\n'
                   'const CHECKS = { 4: function(){ const code=$("clTa").value, r=BancPython.executer(code, {}); '
                   'return {valide: r.ok, message: conseilForme(code)}; } };')),
    ("éditeur Python intégré : preuve rangée par l'écouteur editeur-py:fin", "X",
     page(PY, 'document.addEventListener("editeur-py:fin", e => { const d=e.detail; window.__exp.preuve4 = {code: d.code, ok: !d.erreur}; });\n'
              'const CHECKS = { 4(){ const p4=window.__exp.preuve4; return {valide: !!p4 && p4.ok}; } };')),
    ("éditeur, mais aucune vérification ne lit le programme", "N",
     page(EDITEUR, 'const CHECKS = { 1: function(){ return {valide: $("d1").value === "a"}; } };')),
    ("une variable « e » d'une autre vérification n'est pas le programme", "X",
     page(EDITEUR, 'function etat(){ return {code: $("clTa").value}; }\n'
                   'const CHECKS = { 4: function(){ const r=BancPython.executer($("clTa").value, {}); const e=String(r.ok); '
                   'return {valide: /true/.test(e)}; }, 5: function(){ const e=etat(); return {valide: !!e}; } };')),
    # 25/11/2026 — trois façons de juger après une exécution, et deux verrous faibles
    ("le résultat de l'exécution rangé (window.__lamp = e.detail), relu par une fonction de CHECKS", "X",
     page(PY, 'document.addEventListener("editeur-py:fin", e => { if(e.detail && e.detail.champ === "py_a4") window.__lamp = e.detail; });\n'
              'function lampJuger(r){ return {ok: !!r && !r.erreur && /allume/.test(r.sortie)}; }\n'
              'const CHECKS = { 4(){ const j = lampJuger(window.__lamp); return {valide: j.ok}; } };')),
    ("banc-eleve : l'écouteur fait rejouer le programme par une fonction qui l'exécute", "X",
     page('<div class="editeur-py" id="vs1">' + PY + '</div>',
          'const BANC_ELEVE = {vs1: {essais: []}};\n'
          'function beJuger(b, c){ return window.EditeurPython.executer(c, {}); }\n'
          'function beOk(b){ return !!window.__exp[b]; }\n'
          'document.addEventListener("editeur-py:fin", e => { const d = e.detail; beJuger(d.bloc, d.code).then(v => { window.__exp[d.bloc] = v.ok; }); });\n'
          'const CHECKS = { 4(){ return {valide: beOk("vs1")}; } };')),
    ("verrou faible : une sortie non vide suffit (clé calculée, 3e_C7.1 avant le 25/11)", "X",
     page('<div class="editeur-py" id="vs1">' + PY + '</div>',
          'document.addEventListener("editeur-py:fin", e => { const d = e.detail || {}; if(["vs1"].includes(d.bloc) && !d.erreur && (d.sortie || "").trim()){ window.__exp[d.bloc] = true; } });\n'
          'const CHECKS = { 4(){ return {valide: true, exp: !!window.__exp.vs1}; } };')),
    ("verrou faible : n'importe quelle sortie, clés sans guillemets (4e_C6.2 avant le 25/11)", "X",
     page('<div class="editeur-py" id="vs3">' + PY + '</div>',
          'document.addEventListener("editeur-py:fin", e => { const d = e.detail || {}; const preuve = {vs3: /./}[d.bloc]; if(preuve && preuve.test(d.sortie || "")){ window.__exp[d.bloc] = true; } });\n'
          'const CHECKS = { 4(){ return {valide: true, exp: !!window.__exp.vs3}; } };')),
    ("ce qu'un bloc posé contient n'est pas le code de la page", "N",
     page(EDITEUR, '') .replace('</body>', '<!-- banc-python v1 : début -->\n<script>const CHECKS = { 4: function(){ return {valide: /x/.test($("clTa").value)}; } };</script>\n<!-- banc-python v1 : fin --></body>')),
]


def main():
    ok = 0
    for nom, attendu, html in CAS:
        j = cve.juger(html)
        obtenu = j["classe"] if j else None
        bon = obtenu == attendu
        ok += bon
        print("%s %s — attendu %s, obtenu %s%s" % ("✅" if bon else "❌", nom, attendu, obtenu,
                                                 "" if bon or not j else " " + str(j["motifs"])))
    total = len(CAS)
    # les verrous faibles se signalent ; un juge qui compare ne se signale pas
    attendus_faibles = {"verrou faible : une sortie non vide suffit (clé calculée, 3e_C7.1 avant le 25/11)": True,
                        "verrou faible : n'importe quelle sortie, clés sans guillemets (4e_C6.2 avant le 25/11)": True,
                        "banc-eleve : l'écouteur fait rejouer le programme par une fonction qui l'exécute": False,
                        "le résultat de l'exécution rangé (window.__lamp = e.detail), relu par une fonction de CHECKS": False}
    for nom, html in [(n, h) for n, _, h in CAS if n in attendus_faibles]:
        bon = bool(cve.juger(html)["faibles"]) == attendus_faibles[nom]
        ok += bon
        total += 1
        print("%s %s — verrou faible %s" % ("✅" if bon else "❌", nom[:60], "signalé" if attendus_faibles[nom] else "non signalé"))
    # un éditeur d'activité que rien ne nomme est listé ; un éditeur de Bonus sans banc est compté à part
    html = page('<div class="editeur-py" id="edpy-a3">' + PY + '</div><section id="bonus"><div class="editeur-py" id="vs9" data-fichier="X-bonus-TON NOM">'
                '<textarea id="py_bonus" class="editeur-py-code"></textarea></div></section>',
                'document.addEventListener("editeur-py:fin", e => { if(e.detail.champ === "reinv") window.__lamp = e.detail; });\n'
                'const CHECKS = { 6(){ return {valide: !!window.__lamp}; } };')
    j = cve.juger(html)
    bon = j["sans_jugement"] == ["edpy-a3 (py_a4)"] and j["bonus_libres"] == ["vs9 (py_bonus)"]
    ok += bon
    total += 1
    print("%s un éditeur d'activité que rien ne juge est listé, un Bonus sans banc compté à part — obtenu %s · %s"
          % ("✅" if bon else "❌", j["sans_jugement"], j["bonus_libres"]))
    # sans éditeur : la page n'est pas comptée ; aucune page à éditeur → EN PANNE (n°299)
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "sans.html")
        open(f, "w", encoding="utf-8").write(page("<p>rien</p>", "const CHECKS = {};"))
        r = cve.main([f])
        bon = cve.juger(open(f, encoding="utf-8").read()) is None and r == 2
        ok += bon
        total += 1
        print("%s une page sans éditeur n'est pas comptée, et aucune page à éditeur = EN PANNE (2)" % ("✅" if bon else "❌"))
    # la page qui a fait naître le contrôle, telle qu'elle était le 21/11/2026 (main à f745eca) : ✘ T
    chemin = "theme-2-structure-fonctionnement-comportement/C6-comprendre-et-modifier-un-programme-associe/3e/3e_C6.1/sequence_3e_C6.1-C6.3_programmer_alerte.html"
    try:
        ancien = subprocess.run(["git", "-C", os.path.dirname(ICI), "show", "f745eca:" + chemin], capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        ancien = ""
    if ancien:
        j = cve.juger(ancien)
        bon = bool(j) and j["classe"] == "T" and len(j["motifs"]) >= 7
        ok += bon
        total += 1
        print("%s « Programmer l'alerte » avant l'audit (f745eca) : ✘ T, au moins 7 motifs — obtenu %s, %d motifs"
              % ("✅" if bon else "❌", j["classe"] if j else None, len(j["motifs"]) if j else 0))
    else:
        print("○ la version du 21/11/2026 n'est pas dans cet historique git (clone partiel) : cas non joué")
    # les pages d'avant le 25/11/2026 (main à 3f24c49d) : les verrous faibles et l'éditeur de 4e_C9.1 que rien ne jugeait
    avant = [("theme-3-creation-conception-realisation-innovations/C7-imaginer-concevoir-et-realiser-une-ou-des/3e/3e_C7.1/sequence_3e_C7_capteur-confort-ny.html",
              lambda j: bool(j["faibles"]), "3e_C7.1 : verrou faible signalé"),
             ("theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/4e/4e_C9.1/sequence_4e_C9_jardin-programme.html",
              lambda j: j["sans_jugement"] == ["edpy-a3 (py_a3)"], "4e_C9.1 : l'éditeur de l'activité 3 que rien ne jugeait")]
    for chemin2, verif, libelle in avant:
        try:
            v = subprocess.run(["git", "-C", os.path.dirname(ICI), "show", "3f24c49d:" + chemin2], capture_output=True, text=True, check=True).stdout
        except (OSError, subprocess.CalledProcessError):
            v = ""
        if not v:
            print("○ %s : version du 25/11/2026 absente de cet historique git, cas non joué" % libelle)
            continue
        bon = verif(cve.juger(v))
        ok += bon
        total += 1
        print("%s avant le 25/11 (3f24c49d) — %s" % ("✅" if bon else "❌", libelle))
    print("\n%d / %d" % (ok, total))
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
