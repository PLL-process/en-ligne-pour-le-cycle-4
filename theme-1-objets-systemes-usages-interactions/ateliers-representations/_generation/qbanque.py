# -*- coding: utf-8 -*-
"""La forme commune des banques de questions des ateliers.

Chaque question : 4 propositions, la bonne en position 0 (la répartition sur
A/B/C/D est faite ensuite par `_outils/fix_r.js`), une explication, un exemple,
une erreur fréquente, une réfutation pour CHAQUE distracteur et un « à retenir ».
"""


class Banque:
    def __init__(self):
        self.Q = []

    def q(self, c, n, question, options, expl, ex, err, refs, ret, img=None):
        assert len(options) == 4 and len(refs) == 4, n
        assert refs[0] == "", n
        assert len(set(options)) == 4, (n, "propositions en double")
        for r in refs[1:]:
            assert len(r) > 20, (n, r)
        o = {"c": c, "n": n, "q": question, "o": options, "r": 0,
             "expl": expl, "ex": ex, "err": err, "d": refs, "ret": ret}
        if img:
            o["img"] = img
        self.Q.append(o)

    def longueurs(self):
        """Les questions dont la bonne réponse se devine à sa longueur (même mesure que
        _outils/controle_longueurs.py : écart visible de plus de 8 caractères)."""
        detachees, plus_longues = [], []
        for x in self.Q:
            L = [len(o) for o in x["o"]]
            bonne, autres = L[0], L[1:]
            if bonne > max(autres) + 8 or bonne < min(autres) - 8:
                detachees.append((x["n"], bonne, autres))
            if bonne == max(L):
                plus_longues.append(x["n"])
        return detachees, plus_longues

    def fin(self, total, par_code):
        det, pl = self.longueurs()
        assert len(det) <= 2, "bonnes réponses détachées par leur longueur : %s" % det
        assert len(pl) <= int(0.4 * total), "bonne réponse la plus longue dans %d questions : %s" % (len(pl), pl)
        assert len(self.Q) == total, (len(self.Q), total)
        for code, nb in par_code.items():
            vu = sum(1 for x in self.Q if x["c"] == code)
            assert vu == nb, (code, vu, nb)
        assert sum(1 for x in self.Q if "img" in x) >= 3, "au moins trois questions illustrées"
        return self.Q
