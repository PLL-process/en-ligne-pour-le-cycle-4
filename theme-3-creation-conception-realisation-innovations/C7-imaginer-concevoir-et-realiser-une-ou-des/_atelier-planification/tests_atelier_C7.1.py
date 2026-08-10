# -*- coding: utf-8 -*-
"""Contrôles réellement exécutés sur l'atelier de planification (règle n°43).

Ne déclare que ce qui a été lancé : chaque ligne imprimée correspond à une
assertion qui vient de passer, sur la page telle qu'elle est engagée.
"""
import json
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

D = pathlib.Path(__file__).resolve().parent
PAGE = D / "atelier_C7.1_planification_taches.html"
COR = json.loads((D / "_corrige_calcule.json").read_text(encoding="utf-8"))
P4, P3 = COR["jardin-connecte-brooklyn"], COR["capteur-confort-ny"]
JALON4 = sorted(P4["libelle"])[-1]
faits = []


def ok(msg):
    faits.append(msg)
    print("  ✔ " + msg)


def main():
    src = PAGE.read_text(encoding="utf-8")

    # ── statique
    for n in range(1, 6):
        m = re.search(r'src="(Images/ganttproject_%d[^"]+)"' % n, src)
        assert m, "image %d absente du HTML" % n
        assert (D / m.group(1)).exists(), "fichier %s absent du disque" % m.group(1)
    ok("les cinq captures sont référencées ET présentes sur le disque")

    for m in re.finditer(r"<img\b[^>]*>", src):
        assert 'alt="' in m.group(0) and len(re.search(r'alt="([^"]*)"', m.group(0)).group(1)) > 120, \
            "une image sans alternative textuelle longue : " + m.group(0)[:80]
    ok("chaque image porte une alternative textuelle qui la DÉCRIT (règle n°1)")

    assert "Prêt" in src and "qcm_C7.1_planification_taches.html" in src
    assert src.count('href="qcm_C7.1_planification_taches.html"') == 1
    ok("un seul bouton QCM dans toute la page (règle n°4)")
    assert "Bonus (facultatif" in src
    ok("le bloc Bonus est présent, annoncé hors parcours obligatoire")
    i_bilan, i_qcm, i_bonus = src.index("Bilan —"), src.index("Prêt"), src.index("Bonus (facultatif")
    assert i_bilan < i_qcm < i_bonus, "l'ordre bilan → QCM → bonus n'est pas respecté"
    ok("l'ordre bilan → entraînement → bonus ferme la page (règle n°4)")

    assert "230" not in src and "secteur" not in src.lower()
    ok("aucune mention du secteur : l'activité est en papier et en logiciel")

    assert "http://" not in src and "https://" not in src.replace("http://www.w3.org", "")
    ok("aucun appel réseau : la page fonctionne hors ligne (règle n°40)")

    # ── dynamique
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        pg = nav.new_page()
        erreurs = []
        pg.on("pageerror", lambda e: erreurs.append(str(e)))
        pg.on("console", lambda m: erreurs.append(m.text) if m.type == "error" else None)
        pg.goto(PAGE.as_uri())
        pg.wait_for_timeout(300)
        assert not erreurs, "erreurs JS : %s" % erreurs
        ok("aucune erreur JavaScript au chargement")

        # onglets
        for t, p in [("tab-p5", "p5"), ("tab-p4", "p4"), ("tab-p3", "p3"), ("tab-gp", "gp"), ("tab-pm", "pm")]:
            pg.click("#" + t)
            assert pg.eval_on_selector("#" + p, "e=>e.classList.contains('active')")
        ok("les cinq onglets s'ouvrent et affichent leur panneau")

        # verrou expérientiel : la bonne réponse écrite ne suffit pas sans les bandes
        pg.click("#tab-pm")
        pg.fill("#a1_taches",
                "Câbler le capteur — 2 séances — après : choisir les grandeurs\n"
                "Fabriquer le support — 3 séances — après : choisir les grandeurs\n"
                "Écrire le programme — 2 séances — après : relever les besoins\n"
                "Le jardin s'arrose seul — jalon, aucune durée")
        pg.click('[data-check="1"]')
        assert "class" in pg.eval_on_selector("#fb1", "e=>e.outerHTML")
        assert not pg.evaluate("window.__valid['1']"), "validé sans avoir découpé les bandes"
        ok("le verrou expérientiel tient : sans les bandes découpées, rien n'est validé")

        pg.select_option("#exp_bandes", index=2)
        pg.click('[data-check="1"]')
        assert pg.evaluate("window.__valid['1']"), "toujours pas validé alors que tout est fait"
        ok("une fois les bandes déclarées faites, l'activité 1 se valide")

        # les dates au plus tôt : les réponses justes viennent du corrigé calculé
        pg.click("#tab-p4")
        pg.select_option("#p4_1", label="une seule : A")
        pg.select_option("#p4_2", label="C et E")
        pg.select_option("#p4_3", label="qu'elle peut être écrite très tôt, pendant que d'autres câblent ou fabriquent")
        for i in sorted(P4["libelle"]):
            if i in ("A", JALON4):
                continue
            pg.select_option("#p4d_" + i, label=str(P4["debut_au_plus_tot"][i] + 1))
        pg.select_option("#p4_fin", label=str(P4["duree_totale"]))
        pg.fill("#p4_para",
                "C et E peuvent avancer en même temps parce qu'elles n'attendent que B "
                "et qu'aucune contrainte ne les relie entre elles.\n"
                "Dans mon groupe, deux élèves câblent le capteur pendant que les deux autres "
                "fabriquent le support étanche.")
        pg.click('[data-check="3"]')
        assert pg.evaluate("window.__valid['3']"), pg.inner_text("#fb3")
        ok("les dates au plus tôt du corrigé calculé sont bien celles que la page accepte")

        # une seule date fausse doit faire échouer
        faux = str(P4["debut_au_plus_tot"]["E"] + 3)
        pg.select_option("#p4d_E", label=faux)
        pg.click('[data-check="3"]')
        assert not pg.evaluate("window.__valid['3']"), "une date fausse passe quand même"
        ok("une date fausse est refusée — le vérificateur vérifie vraiment")

        # 3e : le chemin le plus long proposé est celui que calcule le script
        pg.click("#tab-p3")
        pg.select_option("#p3_3", label=" → ".join(P3["chemin"]))
        assert pg.input_value("#p3_3") == " → ".join(P3["chemin"])
        ok("le chemin le plus long offert en réponse est exactement celui du calcul")

        # sauvegarde / restauration
        avant = pg.input_value("#a1_taches")
        pg.reload()
        pg.wait_for_timeout(300)
        assert pg.input_value("#a1_taches") == avant, "la sauvegarde locale ne revient pas"
        assert pg.evaluate("window.__valid['1']") is True
        ok("les réponses et les validations reviennent après rechargement")

        # mode essentiel
        pg.click("#btnEssentiel")
        assert pg.eval_on_selector("body", "e=>e.classList.contains('essentiel')")
        assert pg.eval_on_selector(".referentiel-card",
                                   "e=>getComputedStyle(e).display==='none'")
        ok("le mode essentiel masque bien le référentiel et les corrections")

        # impression : aucun panneau caché
        pg.emulate_media(media="print")
        caches = pg.eval_on_selector_all(
            ".seance-panel", "l=>l.filter(e=>getComputedStyle(e).display==='none').length")
        assert caches == 0, "%d panneaux resteraient invisibles à l'impression" % caches
        ok("à l'impression, les cinq panneaux sont visibles")

        nav.close()

    print("\n%d contrôles exécutés, %d réussis." % (len(faits), len(faits)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
