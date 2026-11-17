# -*- coding: utf-8 -*-
"""Banc de `controle_validations.py` et de `controle_propositions_indices.py` (17/11/2026, audit de `3e_C4.1`)."""
import os
import subprocess
import sys
import tempfile

OUT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, OUT)
import controle_propositions_indices as I  # noqa: E402
import controle_validations as V  # noqa: E402

ok = ko = 0


def verifie(nom, cond):
    global ok, ko
    ok, ko = (ok + 1, ko) if cond else (ok, ko + 1)
    print(("  ✔ " if cond else "  ✘ ") + nom)


def page(seuil="ok===6", critere="6 / 6 réponses", revoque=True, relu=True, simplifie=True):
    return """<html><body>
<div class="activite" id="act1"><p>Consigne</p>
<label for="d1">Énergie : … Wh</label><input id="d1">
<label for="d2">Capacité : 432 Wh ÷ 12 V = … Ah</label><input id="d2">
<fieldset class="qcm-groupe" id="q1"><legend>Le procédé ?</legend>
<div class="qcm-option"><input type="radio" name="q1" id="q1__1" value="moulage par injection (la série rentabilise le moule)"><label for="q1__1">x</label></div>
<div class="qcm-option"><input type="radio" name="q1" id="q1__2" value="sculpture à la main"><label for="q1__2">x</label></div>
<div class="qcm-option"><input type="radio" name="q1" id="q1__3" value="impression 3D"><label for="q1__3">x</label></div>
</fieldset>
<input type="range" id="sim">%s
<button data-check="1">Vérifier</button>
<div class="critere"><b>🎯 Critère de réussite :</b> %s.</div></div>
<fieldset class="qcm-groupe positionnement" id="auto1"><legend>Où en suis-je ?</legend>
<div class="qcm-option"><input type="radio" name="auto1" id="auto1__1" value="🔴 fragile"><label for="auto1__1">🔴 fragile</label></div>
<div class="qcm-option"><input type="radio" name="auto1" id="auto1__3" value="🟢 solide"><label for="auto1__3">🟢 solide</label></div>
<div class="qcm-option"><input type="radio" name="auto1" id="auto1__2" value="🟡 en cours"><label for="auto1__2">🟡 en cours</label></div>
</fieldset>
<script>
const CHECKS = {
  1: function(){
    let ok=0; const att={q1:"moulage par injection (la série rentabilise le moule)"};
    if(num("d1")===432) ok++;
    const j=txt("j4"); const jOk=j.length>=30;
    return {score:ok,total:6,extra:"%s",valide:%s&&jOk};
  },
};
%s
</script></body></html>""" % (
        "<p>⚠️ Modèle simplifié : sans aucune perte.</p>" if simplifie else "",
        critere,
        "Ta justification sera relue par ton professeur." if relu else "",
        seuil,
        "zone.addEventListener('input', e=>{ window.__valid[n] = false; });" if revoque else "",
    )


def codes(res, g=None):
    return sorted(c for gg, c, _ in res if g is None or gg == g)


r = V.analyser(page())
verifie("V1. seuil codé = seuil annoncé : rien à signaler", "V1" not in codes(r))
r = V.analyser(page(seuil="ok>=5"))
verifie("V1 ✘. « 6 / 6 » annoncé, `ok>=5` codé : refus", codes(r, "✘") == ["V1"])
r = V.analyser(page(seuil="ok>=5", critere="toutes les réponses"))
verifie("V1 ⚠. tolérance non annoncée : signalée, pas refusée", "V1" in codes(r, "⚠") and not codes(r, "✘"))
r = V.analyser(page(seuil="ok>=5", critere="5 réponses justes sur 6"))
verifie("V1. tolérance annoncée (« 5 réponses justes sur 6 ») : rien à signaler", "V1" not in codes(r))
r = V.analyser(page(revoque=False, relu=False, simplifie=False))
verifie("V3, V4, V5. pas de retrait, réponse écrite non relue, simulateur sans hypothèses : signalés",
        {"V3", "V4", "V5"} <= set(codes(r, "⚠")))
r = V.analyser(page())
verifie("V3, V4, V5. retrait, « relue par ton professeur », « modèle simplifié » : rien à signaler",
        not ({"V3", "V4", "V5"} & set(codes(r))))

r = I.analyser(page())
verifie("I1. la bonne réponse seule à porter sa justification : signalée", "I1" in codes(r))
verifie("I3. le résultat attendu (432) dans l'étiquette suivante : signalé", "I3" in codes(r))
verifie("I4 ✘. l'échelle dans le désordre : refus ; ses niveaux sans description : signalés",
        codes(r, "✘") == ["I4"] and "I4" in codes(r, "⚠"))
propre = page().replace("432 Wh ÷", "ton énergie ÷").replace("(la série rentabilise le moule)", "") \
    .replace('id="auto1__3" value="🟢 solide"><label for="auto1__3">🟢 solide', 'id="auto1__2" value="🟡 en cours"><label for="auto1__2">🟡 en cours — avec l\'aide') \
    .replace('id="auto1__2" value="🟡 en cours"><label for="auto1__2">🟡 en cours</label>', 'id="auto1__3" value="🟢 solide"><label for="auto1__3">🟢 solide — seul·e</label>')
r = I.analyser(propre)
verifie("I1, I3, I4. la page corrigée : rien à signaler", not codes(r))
toutes = page().replace('value="sculpture à la main"', 'value="sculpture à la main (chaque pièce serait différente)"') \
    .replace('value="impression 3D"', 'value="impression 3D (bien pour une pièce unique)"')
verifie("I1. toutes les propositions portent la leur : le choix porte sur l'argument, rien à signaler",
        "I1" not in codes(I.analyser(toutes)))

with tempfile.TemporaryDirectory() as d:
    vide = subprocess.run([sys.executable, os.path.join(OUT, "controle_validations.py"), d], capture_output=True, text=True)
    verifie("n°299. aucune page lue : sortie 2", vide.returncode == 2)

print("══ controle_validations · controle_propositions_indices : %d / %d ══" % (ok, ok + ko))
sys.exit(1 if ko else 0)
