# -*- coding: utf-8 -*-
"""corriger_question.py — remplacer une proposition ou un indice d'un QCM, dans le bloc de SA question seulement
(lot 3, 17/11/2026 ; skill `propositions-sans-indice`, § QCM).

Un intrus-plaisanterie ou un indice creux se réécrit dans `const QUESTIONS`, où la même chaîne (« ! », « Rien à voir. »)
revient souvent d'une question à l'autre : un remplacement global corrigerait la mauvaise. Ici, chaque remplacement
vise une question, désignée par un morceau unique de son énoncé, et une chaîne qui doit y figurer une fois. Tout est
vérifié avant d'écrire : un seul remplacement impossible, et la page reste intacte.

Les remplacements, en JSON : [["morceau unique de l'énoncé", "ancienne chaîne", "nouvelle chaîne"], …]
  — une proposition change dans `o` ; son pourquoi dans `d` (même rang) ; la bonne réponse et `r` ne bougent pas.

  python3 _outils/qcm_aides/corriger_question.py <qcm.html> <remplacements.json>
  puis : node _outils/verif_qcm_coherence.mjs <qcm> · python3 _outils/controle_longueurs.py · indices_creux.mjs

Sortie : 0 écrit · 1 un remplacement impossible (rien n'est écrit).
"""
import json
import sys


def corriger(s: str, remplacements):
    for frag, ancien, neuf in remplacements:
        if s.count(frag) != 1:
            raise ValueError("énoncé « %s » trouvé %d fois (il faut un morceau unique)" % (frag, s.count(frag)))
        i = s.find(frag)
        debut = s.rfind("{c:", 0, i)
        fin = s.find("\n{c:", i)
        fin = fin if fin > 0 else s.find("\n];", i)
        bloc = s[debut:fin]
        a, n = json.dumps(ancien, ensure_ascii=False), json.dumps(neuf, ensure_ascii=False)
        if bloc.count(a) != 1:
            raise ValueError("« %s » : %d fois dans la question « %s »" % (ancien, bloc.count(a), frag))
        s = s[:debut] + bloc.replace(a, n) + s[fin:]
    return s


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 1
    p, R = argv[0], json.load(open(argv[1], encoding="utf-8"))
    s = open(p, encoding="utf-8").read()
    try:
        u = corriger(s, R)
    except ValueError as e:
        print("✘ %s — rien n'est écrit" % e)
        return 1
    open(p, "w", encoding="utf-8").write(u)
    print("✍ %d remplacement(s) dans %s" % (len(R), p))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
