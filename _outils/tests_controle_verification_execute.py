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
    print("\n%d / %d" % (ok, total))
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
