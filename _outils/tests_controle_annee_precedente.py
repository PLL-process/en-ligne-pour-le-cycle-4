# -*- coding: utf-8 -*-
"""tests_controle_annee_precedente.py — un contrôle se prouve par ses refus, et par ce qu'il laisse passer.

Ce banc joue `controle_annee_precedente.py` (règle d'or n°304, sur toute la page) :
  · sur des phrases écrites pour lui — chacune des trois formes de défaut (A l'élève au passé, B le souvenir commun,
    C l'objet d'une autre année donné comme connu), puis leurs voisines qui doivent PASSER : la forme prudente, la
    progression du programme, un lien de rattrapage, l'histoire d'un objet, un code, la 5e Avenue, un camarade de 6e,
    l'année de la page elle-même ;
  · sur des pages fabriquées, en sous-processus, comme on le lance vraiment (n°299, second corollaire) : le défaut
    caché dans un pourquoi, dans une ligne de tableau, dans la banque d'un QCM ; un script ignoré ; une page de 5e qui
    affirme la 6e ; un dossier sans page d'élève (sortie 2, en panne et non vert).

Usage : python3 _outils/tests_controle_annee_precedente.py
Sortie : 0 si tout passe, 1 sinon.
"""
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import controle_annee_precedente as C  # noqa: E402

OUTIL = os.path.join(ICI, "controle_annee_precedente.py")


def main():
    echecs, n = [], 0

    def juge(titre, attendu, phrase, niveau=4):
        nonlocal n
        n += 1
        j = C.juger(phrase, niveau)
        rendu = j[0] if j else None
        if rendu != attendu:
            echecs.append("%s : attendu %s, rendu %s — « %s »" % (titre, attendu or "rien", rendu or "rien", phrase))

    # ── les trois défauts ────────────────────────────────────────────────────
    juge("A : l'élève au passé composé", "A", "En 5e, tu as suivi le chemin d'une donnée.")
    juge("A : l'élève à l'imparfait", "A", "Souviens-toi : en 5e tu réservais le .1 à la passerelle.", niveau=3)
    juge("A : « Souviens-toi du lampadaire de 5e »", "A", "Souviens-toi du lampadaire de 5e : déjà le sel.", niveau=3)
    juge("A : « Ta passerelle de 4e »", "A", "Ta passerelle de 4e a maintenant un corps.", niveau=3)
    juge("B : « comme en 5e »", "B", "Le protocole va jusqu'à la casse, comme en 5e.")
    juge("B : « Rappel de 5e »", "B", "Rappel de 5e : avec la patère, on comparait des matériaux.")
    juge("B : « vu en 5e »", "B", "Le tableau des conversions (vu en 5e).")
    juge("B : « l'an dernier » qui parle de l'élève", "B", "L'an dernier tu recensais ce qui entoure l'objet.")
    juge("B : « votre avis de l'an dernier »", "B", "Le bureau d'études a lu votre avis de l'an dernier.", niveau=3)
    juge("C : un objet d'une autre année donné comme connu", "C", "Même logique que le lampadaire de 5e : mesure, décision, action.")
    juge("C : une séquence d'une autre année", "C", "Exactement comme les trois jardins de la séquence de 4e.", niveau=3)
    juge("C : « la serre de 4e »", "C", "Dans la serre de 4e (même réseau), c'était TTL=128.", niveau=3)
    juge("une page de 5e qui affirme la 6e", "B", "Cette séquence s'appuie sur ce que tu as fait en 6e et à l'école.", niveau=5)

    # ── ce qui doit passer ───────────────────────────────────────────────────
    juge("la forme prudente : « peut-être… sinon »", None,
         "Tu as peut-être déjà vu ce raisonnement en 4e, sur le jardin connecté ; sinon, le voici.", niveau=3)
    juge("la forme prudente : « si tu as déjà fait »", None, "Si tu as déjà fait le dé en 5e, tu reconnaîtras l'idée.")
    juge("la progression du programme, au présent", None, "En 5e on suit un planning, en 4e on l'organise, en 3e on l'élabore.", niveau=3)
    juge("« au programme de 5e »", None, "Cette notion est au programme de 5e.")
    juge("un lien de rattrapage vers un atelier d'un autre niveau", None,
         "Pour la revoir : l'atelier de 4e « Le diagramme des interacteurs ».", niveau=3)
    juge("l'histoire de l'objet, sans l'élève", None, "La station que le club a réparée l'an dernier est toujours en haut du mât.", niveau=3)
    juge("les élèves d'une autre classe", None, "Six bacs que les 4e de l'an dernier ont plantés en juin.")
    juge("un code de compétence n'est pas une année", None, "Tu la règles comme le banc d'essai (5e_C8.2).")
    juge("la 5e Avenue de New York", None, "Elle dessert les musées de la 5e Avenue, Times Square et Coney Island.", niveau=3)
    juge("un camarade de 6e", None, "Choisis un destinataire : un camarade de 6e — et montre-lui ce que tu as observé.", niveau=3)
    juge("l'année de la page elle-même", None, "En 4e, tu lis un système complet.")
    juge("une phrase sans année", None, "Tu as suivi le chemin d'une donnée jusqu'au serveur.")

    # ── en sous-processus, sur des pages fabriquées ──────────────────────────
    def lancer(*args):
        r = subprocess.run([sys.executable, OUTIL, *args], capture_output=True, text=True)
        return r.returncode, r.stdout + r.stderr

    def sortie(titre, attendue, dossier, contient=""):
        nonlocal n
        n += 1
        code, out = lancer(dossier)
        if code != attendue or contient not in out:
            echecs.append("%s : sortie %d (attendu %d)%s" % (titre, code, attendue,
                                                             "" if contient in out else " — « %s » absent" % contient))

    with tempfile.TemporaryDirectory() as tmp:
        def poser(rel, contenu):
            p = os.path.join(tmp, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w", encoding="utf-8").write(contenu)
            return os.path.dirname(p)

        d = poser("a/4e/4e_X/sequence_x.html", '<html><body><p>Une page saine. En 4e, tu conçois.</p>'
                  '<script>// « comme en 5e » dans un script ne se lit pas</script></body></html>')
        sortie("une page de 4e saine (un script n'est pas lu)", 0, d, "aucune phrase n'affirme")
        d = poser("b/4e/4e_X/sequence_x.html", '<html><body><input type="radio" value="v" '
                  'data-pourquoi="Casser, c\'était le protocole de 5e, pour comparer."></body></html>')
        sortie("un défaut caché dans un pourquoi", 1, d, "C objet donné comme connu : 1")
        d = poser("c/3e/3e_X/sequence_x.html", '<html><body><table><tr><td><b>5e</b><br>Shenzhen</td>'
                  '<td>tu <b>recensais</b> ce qui entoure l\'objet</td></tr></table></body></html>')
        sortie("une ligne de tableau se lit d'un trait", 1, d, "A au passé : 1")
        d = poser("e/3e/3e_X/qcm_3e_x.html", '<html><script>\nconst QUESTIONS = [\n{c:"C",n:"N",q:"Q ?",o:["a","b"],r:0,'
                  'ex:"Comme les trois jardins de la séquence de 4<sup>e</sup>.",d:["","b"]}\n];\n</script></html>')
        sortie("un défaut dans la banque d'un QCM, « 4<sup>e</sup> » compris", 1, d, "C objet donné comme connu : 1")
        d = poser("f/5e/5e_X/sequence_x.html", "<html><body><p>Cette séquence s'appuie sur ce que tu as programmé en 6e.</p></body></html>")
        sortie("une page de 5e qui affirme la 6e", 1, d, "A au passé : 1")
        d = poser("g/commun/sequence_sans_niveau.html", "<html><body><p>Comme en 5e.</p></body></html>")
        sortie("une page sans niveau n'est pas lue : rien lu, en panne", 2, d, "rien n'a été lu")

    print("%d / %d tests passés" % (n - len(echecs), n))
    for e in echecs:
        print("  ✘ " + e)
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
