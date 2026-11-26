# -*- coding: utf-8 -*-
"""tests_controle_bonus_corrige.py — le contrôle du corrigé des Bonus, et le recomptage de `replier_bonus.py`,
éprouvés sur des cas dont on connaît la réponse (règle n°194).

Sortie : 0 tout passe · 1 un échec.
Usage : python3 _outils/tests_controle_bonus_corrige.py
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import controle_bonus_corrige as c  # noqa: E402
import replier_bonus as r  # noqa: E402

TITRE = "<h2>🎁 Bonus (facultatif — hors parcours obligatoire)</h2>"
D1 = "<p>🗺 <b>Défi carte :</b> retrouve les câbles.</p>"
D2 = "<p>⏱ <b>Défi mesure :</b> compte les routeurs.</p>"
D3 = "<p>🔧 <b>Défi Filius :</b> ajoute un réseau.</p>"
CHAMP = '<p><label for="bonusRep"><b>✍ Ma réponse au Bonus</b></label></p><textarea id="bonusRep"></textarea>'
ETAYE = ('<details class="etayage"><summary>🪜 Version étayée</summary><ul><li>J\'ai choisi ____.</li>'
         "<li>J'ai trouvé ____.</li><li>Parce que ____.</li><li>Donc ____.</li></ul></details>")


def corr(titre, classe="correction"):
    return '<details class="%s"><summary>%s</summary><p>La réponse, et pourquoi.</p></details>' % (classe, titre)


def page(corps, replie=None):
    if replie:
        corps = '<details class="bonus-replie"><summary>%s</summary>%s</details>' % (replie, corps)
    return "<html><body><section class=\"card\">%s%s</section><section><h2>Bilan</h2></section></body></html>" % (TITRE, corps)


def codes(html):
    j = c.juger(html)
    return None if j is None else sorted(k for k, _ in j)


def main():
    ok = total = 0

    def cas(nom, bon):
        nonlocal ok, total
        total += 1
        ok += bool(bon)
        print("%s %s" % ("✅" if bon else "❌", nom))

    cas("une page sans Bonus n'est pas jugée", c.juger("<html><body><section><h2>Bilan</h2></section></body></html>") is None)
    cas("un Bonus sans aucun corrigé : B1", codes(page(D1 + D2 + D3 + CHAMP)) == ["B1"])
    cas("trois défis nommés, chacun suivi de son corrigé : conforme",
        codes(page(D1 + corr("✅ Corrigé du défi carte") + D2 + corr("✅ Corrigé du défi mesure") + D3
                   + corr("✅ Corrigé du défi Filius") + CHAMP)) == [])
    j = c.juger(page(D1 + corr("✅ Corrigé du défi carte") + D2 + D3 + CHAMP))
    cas("trois défis, un seul corrigé : B2, et les deux défis sans corrigé sont nommés",
        [k for k, _ in j] == ["B2"] and "Défi mesure" in j[0][1] and "Défi Filius" in j[0][1] and "carte" not in j[0][1])
    cas("un corrigé d'ensemble « Corrigé du Bonus » couvre tous les défis",
        codes(page(D1 + D2 + D3 + CHAMP + corr("📖 Corrigé du Bonus (à ouvrir APRÈS ton essai)"))) == [])
    cas("« Ce qu'une bonne réponse contient » est un corrigé d'ensemble",
        codes(page(D1 + D2 + D3 + CHAMP + corr("📖 Ce qu'une bonne réponse contient", "approfondissement"))) == [])
    cas("« Corrigé des trois défis » est un corrigé d'ensemble",
        codes(page(D1 + D2 + D3 + CHAMP + corr("✅ Corrigé des trois défis"))) == [])
    cas("des corrigés rangés à la fin, qui nomment leur défi, sont rendus à leur défi",
        codes(page(D1 + D2 + D3 + CHAMP + corr("✅ Corrigé du défi carte — les câbles") + corr("✅ Corrigé du défi mesure")
                   + corr("✅ Corrigé du défi Filius"))) == [])
    cas("le titre « Les 4 défis » pour trois défis nommés : B3",
        codes(page(D1 + D2 + D3 + corr("📖 Corrigé du Bonus"), "🎁 Les 4 défis du Bonus — ouvre-les quand tu as fini")) == ["B3"])
    cas("le titre « Le défi du Bonus — » pour trois défis nommés : B3",
        codes(page(D1 + D2 + D3 + corr("📖 Corrigé du Bonus"), "🎁 Le défi du Bonus — ouvre-le quand tu as fini")) == ["B3"])
    cas("le titre « Les 3 défis » pour trois défis nommés : conforme",
        codes(page(D1 + D2 + D3 + corr("📖 Corrigé du Bonus"), "🎁 Les 3 défis du Bonus — ouvre-les quand tu as fini")) == [])
    seul = "<p>Sur l'établi, monte la station du collège voisin.</p><p>Puis écris ce que tu observes.</p>"
    cas("un seul défi, sans libellé, titre au singulier, avec son corrigé : conforme",
        codes(page(seul + CHAMP + ETAYE + corr("✅ Corrigé du Bonus — la station du collège voisin"),
                   "🎁 Le défi du Bonus — ouvre-le quand tu as fini")) == [])
    cas("un seul défi sans libellé sous le titre « Les 3 défis » : B3 (compter à la main)",
        codes(page(seul + CHAMP + ETAYE + corr("✅ Corrigé du Bonus"), "🎁 Les 3 défis du Bonus — ouvre-les quand tu as fini")) == ["B3"])
    cas("les phrases de la version étayée ne sont pas des défis",
        len(c.lire(seul + CHAMP + ETAYE + corr("✅ Corrigé du Bonus"))[0]) == 0)
    liste = "<ol><li><b>La variable qui ment.</b> Remplace.</li><li><b>Le robot sans robot.</b> Réécris.</li><li><b>Le nom.</b> Reprends.</li></ol>"
    cas("des défis en liste numérotée : trois défis comptés ; sans corrigé : B1",
        len(c.lire(liste)[0]) == 3 and codes(page(liste)) == ["B1"])
    cas("des défis en liste, avec un corrigé d'ensemble : conforme", codes(page(liste + corr("📖 Corrigé du Bonus"))) == [])
    boite = '<p>Défi : le store.</p><div id="bonusCorrection" class="correction-box" hidden><p>La correction complète.</p></div>'
    cas("un bloc de correction que la vérification découvre (class=\"correction-box\") compte", codes(page(boite)) == [])
    prof = ('<html><body><details class="prof"><summary>🎁 Bonus (facultatif — hors parcours obligatoire) : ArduBlock</summary>'
            "<p>Pour le professeur.</p></details><section><h2>Bilan</h2></section></body></html>")
    cas("un titre de Bonus repris dans un aparté du professeur n'est pas le Bonus de l'élève", c.juger(prof) is None)
    cas("un défi d'évaluation déclaré data-sans-corrige est dispensé",
        codes(page('<div data-sans-corrige="évaluation sommative">' + D1 + D2 + "</div>")) == [])
    numerote = ("<p>Sur le banc, trouve deux publications.</p>" + corr("✅ Corrigé du défi 1 — les deux publications")
                + "<p>Laquelle accepterais-tu ?</p>" + corr("✅ Corrigé du défi 2 — celle que j'accepterais"))
    cas("des défis que seuls leurs corrigés numérotent : deux défis, conforme sous « Les 2 défis »",
        len(c.lire(numerote)[0]) == 2 and codes(page(numerote, "🎁 Les 2 défis du Bonus — ouvre-les quand tu as fini")) == [])
    cas("le libellé « Défi 1 — le cinquième organe. » est lu, et son corrigé « Corrigé du défi 1 » lui revient",
        codes(page("<p><b>Défi 1 — le cinquième organe.</b><br>La mairie ajoute.</p><p><b>Défi 2 — l'auto-test qui ment.</b><br>Écris.</p>"
                   + CHAMP + corr("✅ Corrigé du défi 1 — le cinquième organe") + corr("✅ Corrigé du défi 2 — l'auto-test qui ment"))) == [])

    # replier_bonus.py : le recomptage
    cas("replier_bonus.compter : trois défis nommés → 3 ; un défi sans libellé, version étayée à quatre phrases → 1",
        r.compter(D1 + D2 + D3 + CHAMP) == 3 and r.compter(seul + CHAMP + ETAYE) == 1)
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "p.html")
        open(f, "w", encoding="utf-8").write(page(D1 + D2 + D3 + corr("📖 Corrigé du Bonus"), "🎁 Les 5 défis du Bonus — ouvre-les quand tu as fini"))
        avant = r.retitrer(f, True)
        cas("replier_bonus --titres : « Les 5 défis » devient « Les 3 défis », puis plus rien à changer",
            avant and "Les 3 défis" in avant[1] and "Les 3 défis du Bonus" in open(f, encoding="utf-8").read() and r.retitrer(f, True) is None)
        open(f, "w", encoding="utf-8").write(page(D1 + D2 + D3 + corr("📖 Corrigé du Bonus"), "🎁 Le défi du Bonus : faire retenir le bon geste"))
        cas("replier_bonus --titres : un titre écrit à la main n'est pas touché", r.retitrer(f, True) is None)
        vide = os.path.join(d, "vide.html")
        open(vide, "w", encoding="utf-8").write("<html><body><p>rien</p></body></html>")
        cas("aucune page avec un Bonus : le contrôle sort 2 (rien vérifié), pas 0", c.main([vide]) == 2)
        open(f, "w", encoding="utf-8").write(page(D1 + D2 + CHAMP))
        cas("une page en écart : le contrôle sort 1", c.main([f]) == 1)
    cas("le site : chaque Bonus a son corrigé et son titre juste (sortie 0)", c.main([]) == 0)
    print("\n%d / %d" % (ok, total))
    return 0 if ok == total else 1


if __name__ == "__main__":
    sys.exit(main())
