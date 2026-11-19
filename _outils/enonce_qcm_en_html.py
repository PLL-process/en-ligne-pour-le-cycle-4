#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""enonce_qcm_en_html.py — rendre l'énoncé des QCM du gabarit maison en HTML (19/11/2026) : le moteur l'écrivait avec textContent, si bien que
<code>, <b>, les entités et un listing <div class="py"> s'affichaient en clair. Rejouable : ne touche qu'aux pages dont
un énoncé porte une balise ou une entité, et qui ne sont pas déjà corrigées.

Usage, depuis la racine du dépôt :  python3 _outils/enonce_qcm_en_html.py [--ecrire]
Le garde-fou est dans _outils/verif_qcm_coherence.mjs : un énoncé à balises écrit avec textContent y est refusé."""
import os, re, subprocess, sys
ECRIRE = "--ecrire" in sys.argv
ANCIEN = '  $("qTexte").textContent=Q.q;'
ANCIEN_PY = '  ecrireEnonce($("qTexte"),Q.q);'
NOUVEAU = ('  // L\'énoncé est écrit en HTML, comme les propositions : <code>, <b>, un listing <div class="py">. Un listing est\n'
           '  // coloré comme dans un IDE par le colorisateur commun (règle d\'or n°13), quand la page le charge.\n'
           '  $("qTexte").innerHTML=Q.q;\n'
           '  if(window.CodeColore) $("qTexte").querySelectorAll("div.py,pre.py").forEach(e=>{ window.CodeColore.colorer(e,"python"); window.CodeColore.legende(e,"python"); });')
CSS_ANCRE = "  .q-texte{font-size:1.05em;font-weight:600;margin:8px 0 14px}"
CSS = ("  .q-texte code,.option code,.bloc-detail code{font-family:ui-monospace,Consolas,'Courier New',monospace;font-size:.95em;"
       "background:rgba(97,218,251,.13);color:#9fe8ff;padding:0 .3em;border-radius:4px;white-space:pre-wrap}\n"
       "  .q-texte .py{display:block;white-space:pre;overflow-x:auto;font:400 .92em/1.5 ui-monospace,Consolas,'Courier New',monospace;"
       "background:#050f24;border:1px solid var(--border);border-radius:10px;padding:10px 12px;margin-top:10px}")
fichiers = subprocess.run(["git", "ls-files", "theme-*/*qcm_*.html"], capture_output=True, text=True).stdout.split()
for f in fichiers:
    s = open(f, encoding="utf-8").read()
    if "const QUESTIONS" not in s: continue
    qs = re.findall(r'\bq:"((?:[^"\\]|\\.)*)"', s)
    if not any(re.search(r"<[a-z]|&[a-z#0-9]+;", q, re.I) for q in qs): continue
    if '$("qTexte").innerHTML=Q.q;' in s:
        print("déjà corrigé ·", os.path.basename(f)); continue
    t = s
    if ANCIEN_PY in t:   # le premier correctif du 19/11 (qcm_python_variables) : on le remplace par le rendu commun
        t = t.replace(ANCIEN_PY, NOUVEAU.replace("  //", "  //", 1))
        t = re.sub(r"/\* L'énoncé peut porter du code entre <code>…</code>.*?\n}\n", "", t, count=1, flags=re.S)
        t = re.sub(r"  \.q-texte code,\.option code,\.bloc-detail code,\.bloc-aide code\{[^\n]*\}\n", "", t, count=1)
    else:
        assert t.count(ANCIEN) == 1, f
        t = t.replace(ANCIEN, NOUVEAU)
    assert t.count(CSS_ANCRE) == 1, f
    t = t.replace(CSS_ANCRE, CSS_ANCRE + "\n" + CSS)
    if any('class=\\"py' in q for q in qs) and "code-colore.js" not in t:
        rel = os.path.relpath("_ressources-communes/code-colore", os.path.dirname(f))
        t = t.replace("</head>", f'<link rel="stylesheet" href="{rel}/code-colore.css">\n<script src="{rel}/code-colore.js"></script>\n</head>', 1)
    print(("✍ " if ECRIRE else "· ") + os.path.basename(f))
    if ECRIRE: open(f, "w", encoding="utf-8").write(t)
