# -*- coding: utf-8 -*-
"""Banc de `intituler_codes.py` : chaque étiquette de code du programme dit sa compétence au survol (17/11/2026).

Usage : python3 _outils/tests_intituler_codes.py      Sortie : 0 tout passe · 1 un cas échoue.
"""
import os
import shutil
import subprocess
import sys
import tempfile

OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, OUT)
import intituler_codes as I  # noqa: E402

ok = ko = 0


def cas(nom, cond, detail=""):
    global ok, ko
    if cond:
        ok += 1; print("  ✔ " + nom)
    else:
        ko += 1; print("  ✘ " + nom + (" — " + detail if detail else ""))


cas("un code", I.codes_de("3e_C4.1") == [("3", "4", "1")])
cas("le niveau se transmet : 4e_C7.1 · C7.2 · C7.3", I.codes_de("4e_C7.1 · C7.2 · C7.3") == [("4", "7", "1"), ("4", "7", "2"), ("4", "7", "3")])
cas("une plage : 5e_C9.1 → C9.3", I.codes_de("5e_C9.1 → C9.3") == [("5", "9", "1"), ("5", "9", "2"), ("5", "9", "3")])
cas("deux niveaux dans une étiquette : 3e_C7.3 · 3e_C4.2", I.codes_de("3e_C7.3 · 3e_C4.2") == [("3", "7", "3"), ("3", "4", "2")])
b = I.bulle(I.codes_de("3e_C4.1"))
cas("la bulle : « Programme 2024 — code : intitulé »", b.startswith("Programme 2024 — 3e_C4.1 : ") and "chaîne d’énergie" in b, b)
cas("le sigle OST écrit en toutes lettres (n°313)", "OST" not in b and "objet ou système technique" in b, b)
cas("« de l’OST » : de l’objet ou du système technique", "de l’objet ou du système technique" in I.intitule("3", "4", "6"))
cas("plusieurs codes : une ligne par code", I.bulle(I.codes_de("3e_C1.3 + 3e_C1.4")).count("\n") == 2)

page = ('<html><body><div class="badges"><span class="badge niveau">3e</span>'
        '<span class="badge code">3e_C4.1</span>'
        '<span class="badge code" title="Code de rangement de la séquence : paraphrase.">3e_C4.2</span>'
        '<span class="badge theme" title="Domaines du socle">Socle</span></div>'
        '<span class="badge code" title="Une note à garder">3e_C4.3</span></body></html>')
u, a, d, n, autres = I.analyser(page)
cas("pose la bulle d'une étiquette sans bulle", 'title="Programme 2024 — 3e_C4.1' in u)
cas("remplace une bulle « Code de rangement… »", 'Code de rangement' not in u and 'title="Programme 2024 — 3e_C4.2' in u)
cas("garde la bulle d'une autre étiquette (socle)", 'title="Domaines du socle"' in u)
cas("signale, sans l'écraser, une bulle d'un autre contenu", 'title="Une note à garder"' in u and len(autres) == 1, str(autres))
cas("rejouer ne change rien", I.analyser(u)[0] == u)
v = I.poser_texte(I.sans_bulles(u))
cas("sans_bulles puis poser_texte : les mêmes bulles (générateurs)",
    "Programme 2024" not in I.sans_bulles(u) and v.count("Programme 2024 —") == u.count("Programme 2024 —") and I.analyser(v)[1] == 0)

tmp = tempfile.mkdtemp()
try:
    f = os.path.join(tmp, "sequence_x.html")
    open(f, "w", encoding="utf-8").write(page)
    r = subprocess.run([sys.executable, os.path.join(OUT, "intituler_codes.py"), "--etat", "--strict", tmp], capture_output=True, text=True)
    cas("--etat --strict sort à 1 s'il reste une étiquette sans bulle", r.returncode == 1, r.stdout)
    subprocess.run([sys.executable, os.path.join(OUT, "intituler_codes.py"), "--ecrire", tmp], capture_output=True, text=True)
    r = subprocess.run([sys.executable, os.path.join(OUT, "intituler_codes.py"), "--etat", "--strict", tmp], capture_output=True, text=True)
    cas("après --ecrire, --strict sort à 0", r.returncode == 0, r.stdout)
    vide = os.path.join(tmp, "vide"); os.makedirs(vide)
    r = subprocess.run([sys.executable, os.path.join(OUT, "intituler_codes.py"), "--etat", vide], capture_output=True, text=True)
    cas("rien lu : sortie 2 (n°299)", r.returncode == 2, r.stdout)
finally:
    shutil.rmtree(tmp)

print("%d / %d" % (ok, ok + ko))
sys.exit(1 if ko else 0)
