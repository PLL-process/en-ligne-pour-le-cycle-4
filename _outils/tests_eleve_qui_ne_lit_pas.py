# -*- coding: utf-8 -*-
"""Banc de `eleve_qui_ne_lit_pas.py` (règle d'or n°360), sur trois pages dont on connaît la réponse (n°194).

    python3 _outils/tests_eleve_qui_ne_lit_pas.py

- une page où la bonne réponse est toujours la plus longue : l'outil doit la refuser (sortie 1) ;
- une page aux bonnes réponses réparties et de longueurs égales : l'outil doit l'accepter (sortie 0) ;
- une page sans `CHECKS` : l'outil doit dire qu'il n'a rien lu (sortie 2) ;
- deux pages du kit des ateliers (`#donnees-page`, un bouton « Vérifier » par exercice `[data-exo]`, depuis le
  26/11/2026) : la bonne réponse toujours la première est refusée ; réparties, elles sont acceptées.
Sortie du banc : 0 tout passe · 1 un échec · 2 Playwright absent.
"""
import pathlib
import subprocess
import sys
import tempfile

try:
    import playwright  # noqa: F401
except ImportError:
    print("✘ Playwright absent : rien n'a été vérifié")
    sys.exit(2)

OUTIL = pathlib.Path(__file__).resolve().parent / "eleve_qui_ne_lit_pas.py"


def page(questions, seuil):
    """questions : liste de (propositions, indice de la bonne)."""
    blocs, bonnes = [], []
    for i, (props, k) in enumerate(questions, 1):
        radios = "".join(f'<input type="radio" name="q{i}" id="q{i}_{j}" value="{p}"><label for="q{i}_{j}">{p}</label>'
                         for j, p in enumerate(props))
        blocs.append(f"<fieldset><legend>Question {i}</legend>{radios}</fieldset>")
        bonnes.append(props[k])
    js_bonnes = ",".join(f'"{b}"' for b in bonnes)
    return f"""<!doctype html><meta charset="utf-8"><title>banc</title>
{''.join(blocs)}<button data-check="1">Vérifier</button>
<script>
const B=[{js_bonnes}];
const CHECKS={{1:function(){{let s=0;B.forEach((b,i)=>{{const r=document.querySelector('input[name="q'+(i+1)+'"]:checked');
  if(r&&r.value===b)s++;}});return {{score:s,total:B.length,valide:s>={seuil}}};}}}};
</script>"""


def page_kit(bonnes):
    """Le gabarit du kit, réduit : un exercice de trois questions ; « Vérifier » écrit le retour, classe `ok` si tout
    est juste (comme kit.js) ; les réponses attendues dans le script JSON d'identifiant donnees-page."""
    props = ["Alpha", "Bravo", "Charl", "Delta"]
    qs = "".join('<fieldset><legend>Question %d</legend>%s</fieldset>' % (i, "".join(
        '<label><input type="radio" name="e1_q%d" value="%s"> %s</label>' % (i, v, v) for v in props))
        for i in range(1, len(bonnes) + 1))
    attendu = ",".join('"e1_q%d":"%s"' % (i, props[k]) for i, k in enumerate(bonnes, 1))
    return f"""<!doctype html><meta charset="utf-8"><title>banc kit</title>
<script type="application/json" id="donnees-page">{{"e1":{{{attendu}}}}}</script>
<section data-exo="e1">{qs}<p><button class="btn verifier" type="button">Vérifier</button></p>
<p class="retour" data-retour="e1"></p></section>
<script>
document.querySelector("button.verifier").addEventListener("click", () => {{
  const att = JSON.parse(document.getElementById("donnees-page").textContent).e1;
  const juste = Object.keys(att).every(n => {{ const r = document.querySelector('input[name="' + n + '"]:checked');
    return r && r.value === att[n]; }});
  const z = document.querySelector(".retour[data-retour]"); z.className = "retour " + (juste ? "ok" : "ko");
  z.textContent = juste ? "Juste." : "Pas encore.";
}});
</script>"""


LONGUE = [(["Oui", "Non", "Le capteur envoie la mesure au programme qui décide", "Rien"], 2)] * 4
REPARTIE_PROPS = ["Alpha", "Bravo", "Charl", "Delta"]
REPARTIE = [(REPARTIE_PROPS, k) for k in (0, 1, 2, 3, 1, 0, 3, 2)]

res = []
with tempfile.TemporaryDirectory() as d:
    d = pathlib.Path(d)
    (d / "longue.html").write_text(page(LONGUE, 3), encoding="utf-8")
    (d / "repartie.html").write_text(page(REPARTIE, 6), encoding="utf-8")
    billet = page(REPARTIE, 6).replace("valide:s>=6", "valide:true")
    (d / "billet.html").write_text(billet, encoding="utf-8")
    enfermee = page(LONGUE, 3).replace("<script>", "<div id=\"fb1\" class=\"feedback\"></div><script>(function(){") \
        .replace("</script>", "document.querySelector('[data-check]').addEventListener('click',()=>{const r=CHECKS[1]();"
                              "document.getElementById('fb1').className='feedback show '+(r.valide?'ok':'ko');});})();</script>")
    (d / "enfermee.html").write_text(enfermee, encoding="utf-8")
    (d / "kit_premiere.html").write_text(page_kit([0, 0, 0]), encoding="utf-8")
    (d / "kit_repartie.html").write_text(page_kit([2, 1, 3]), encoding="utf-8")
    (d / "sans_checks.html").write_text("<!doctype html><meta charset='utf-8'><title>x</title><fieldset>"
                                        "<input type=radio name=a value=1></fieldset>", encoding="utf-8")
    for nom, attendu, quoi in [("longue.html", 1, "la bonne réponse toujours la plus longue est refusée"),
                               ("repartie.html", 0, "des bonnes réponses réparties, de même longueur, sont acceptées"),
                               ("enfermee.html", 1, "CHECKS enfermé dans une fonction : lu par le bouton, et refusé"),
                               ("billet.html", 0, "un billet validé quelle que soit la réponse n'est pas une faute"),
                               ("sans_checks.html", 2, "une page sans CHECKS : « rien lu », jamais vert"),
                               ("kit_premiere.html", 1, "kit : la bonne réponse toujours la première est refusée "
                                                        "(la bête à cornes de 5e, exercice 1, avant le 26/11/2026)"),
                               ("kit_repartie.html", 0, "kit : des bonnes réponses réparties sont acceptées")]:
        r = subprocess.run([sys.executable, str(OUTIL), str(d / nom)], capture_output=True, text=True, timeout=120)
        ok = r.returncode == attendu
        res.append(ok)
        print(("✔" if ok else "✘"), quoi, "" if ok else f"— sortie {r.returncode}, attendue {attendu}\n{r.stdout}{r.stderr}")
    r = subprocess.run([sys.executable, str(OUTIL), str(d / "longue.html")], capture_output=True, text=True, timeout=120)
    ok = "« la plus longue »" in r.stdout
    res.append(ok)
    print(("✔" if ok else "✘"), "le message nomme la stratégie qui valide", "" if ok else r.stdout)

    r = subprocess.run([sys.executable, str(OUTIL), str(d / "billet.html")], capture_output=True, text=True, timeout=120)
    ok = "quelle que soit la réponse" in r.stdout
    res.append(ok)
    print(("✔" if ok else "✘"), "le billet est listé à part, pour vérifier que la page le dit", "" if ok else r.stdout)

print(f"\n{sum(res)} / {len(res)} tests passés")
sys.exit(0 if all(res) else 1)
