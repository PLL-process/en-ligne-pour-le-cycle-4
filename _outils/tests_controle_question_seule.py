# -*- coding: utf-8 -*-
"""tests_controle_question_seule.py — un contrôle se prouve par ses refus, et par ce qu'il laisse passer.

Ce banc joue `controle_question_seule.py` (règles d'or n°343, n°344, n°345 ; n°304 et n°330 mesurées) :
  · sur des questions écrites pour lui, une par mesure — S1 code sans nom, S2 renvoi sans document, S3 autre année,
    S4 notion qui souffle, E1 liste tronquée — et sur leurs voisines qui ne doivent PAS être refusées (un code nommé
    à côté, une classe de flexibilité F2, un document sous la question, une liste entière, « trois fois ») ;
  · en sous-processus, comme on le lance vraiment (n°299, second corollaire), sur des dossiers fabriqués : un QCM
    fautif sort à 1 avec `--strict` et à 0 sans ; un QCM sain sort à 0 ; un dossier vide sort à 2 (en panne, pas vert) ;
    un QCM de séquence sous six questions sur document et une séquence sans billet de sortie sont des chantiers
    (D1, P1) : comptés, jamais refusés.

Usage : python3 _outils/tests_controle_question_seule.py
Sortie : 0 si tout passe, 1 sinon.
"""
import os
import pathlib
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

import controle_question_seule as CQ  # noqa: E402

OUTIL = os.path.join(ICI, "controle_question_seule.py")


def qcm(*questions):
    """Une page de QCM réduite à sa banque, à la forme du gabarit maison."""
    blocs = []
    for q in questions:
        img = ('\n img:{src:"Images/doc_x.svg",alt:"Un document."},' if q.get("doc") else "")
        blocs.append('{c:"C3.1",n:"%s",q:"%s",%s\n o:[%s], r:%d,\n expl:"e",ex:"x",err:"r",d:["","b","c","d"],ret:"t"}'
                     % (q.get("n", "Notion"), q["q"], img, ", ".join('"%s"' % o for o in q["o"]), q.get("r", 0)))
    return "<html><script>\nconst QUESTIONS = [\n" + ",\n".join(blocs) + "\n];\n</script></html>\n"


SAINE = {"q": "Un matériau, c'est…", "o": ["la matière dont l'objet est fait", "sa forme", "son énergie", "son prix"]}


def lancer(*args):
    r = subprocess.run([sys.executable, OUTIL, *args], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def main():
    echecs, controles = [], 0

    def juge(titre, attendus, notion, enonce, props, r=0, doc=False, niveau=None):
        """`attendus` : les codes que `juger` doit rendre, ni plus ni moins."""
        nonlocal controles
        controles += 1
        rendus = sorted(c for c, _ in CQ.juger(notion, enonce, props, r, doc, niveau))
        if rendus != sorted(attendus):
            echecs.append("%s : attendu %s, rendu %s" % (titre, sorted(attendus) or "rien", rendus or "rien"))

    def sortie(titre, attendue, args, contient=""):
        nonlocal controles
        controles += 1
        code, texte = lancer(*args)
        if code != attendue:
            echecs.append("%s : sortie %d, attendue %d\n     %s" % (titre, code, attendue, texte.strip()[-300:]))
        elif contient and contient not in texte:
            echecs.append("%s : message sans « %s »\n     %s" % (titre, contient, texte.strip()[-300:]))

    quatre = ["oui", "non", "parfois", "jamais"]

    # ── S1 : un code sans son nom ────────────────────────────────────────────
    juge("S1 : « S2 » seul dans l'énoncé", ["S1"], "Notion", "S2 consomme 165 Wh par km. Pourquoi ?", quatre)
    juge("S1 : le code nommé à côté, « le vélo-cargo (S1) »", [], "Notion", "Le vélo-cargo (S1) consomme peu. Pourquoi ?", quatre)
    juge("S1 : une classe de flexibilité, « F2 », est du vocabulaire enseigné", [], "Notion", "Une exigence de flexibilité F2 est…", quatre)
    juge("S1 : un document sous la question nomme les codes", [], "Notion", "S2 consomme-t-il plus que S1 ?", quatre, doc=True)
    juge("S1 : un code de compétence n'est pas un code d'objet", [], "Notion", "La compétence C3.1 demande de…", quatre)
    # (25/11/2026) un code se nomme aussi par le mot qui le précède, ce qui le suit, une parenthèse ; un nom composé n'en est pas un
    juge("S1 : « le port A0 » est nommé", [], "Notion", "Le capteur est branché sur le port A0. Que lit le programme ?", quatre)
    juge("S1 : « les tests T1 et T2, mais rate T3 » : la famille est nommée", [], "Notion", "Le programme réussit les tests T1 et T2, mais rate T3.", quatre)
    juge("S1 : « T1 à la batterie, T2 après le fusible »", [], "Notion", "Points de mesure : T1 à la batterie, T2 après le fusible. T2 = 0 V : où chercher ?", quatre)
    juge("S1 : « entrée analogique (A0 à A3) »", [], "Notion", "Quelle différence entre une entrée analogique (A0 à A3) et une entrée numérique (D2 à D8) ?", quatre)
    juge("S1 : « TECHNO-C4 », un nom de réseau, n'est pas un code", [], "Notion", "Le smartphone connecté au réseau TECHNO-C4 est…", quatre)
    juge("S1 : « Base Shield V2 », une version de produit", [], "Notion", "Le Base Shield V2 ne mesure rien. À quoi sert-il ?", quatre)
    juge("S1 : « sur D6 », toujours sans nom", ["S1"], "Notion", "Pourquoi le bandeau doit-il être branché sur D6 ?", quatre)

    # ── S2 : un renvoi sans document ─────────────────────────────────────────
    juge("S2 : « du tableau », sans tableau", ["S2"], "Notion", "La solution la plus performante du tableau est aussi…", quatre)
    juge("S2 : « dans notre travail »", ["S2"], "Notion", "Dans notre travail, la borne servait à…", quatre)
    juge("S2 : le même renvoi, le document sous la question", [], "Notion", "La solution la plus performante du tableau est aussi…", quatre, doc=True)

    # ── S3 : une autre année (n°304) ─────────────────────────────────────────
    juge("S3 : « En 4e à Hangzhou »", ["S3"], "Notion", "En 4e à Hangzhou, la borne refusait une carte. Ici…", quatre)
    juge("S3 : « par rapport à la 5e », même sous un document", ["S3"], "Notion", "Par rapport à la 5e, ce qui change…", quatre, doc=True)
    juge("S3 : « Dans une autre étude » ne suppose aucune année", [], "Notion", "Dans une autre étude, la borne refusait une carte. Ici…", quatre)
    # (25/11/2026) le passé de l'élève, pas la progression d'une compétence ni l'année du QCM lui-même
    juge("S3 : « En 4e tu écrivais… »", ["S3"], "Notion", "En 4e tu écrivais 192.168.20.1 dans la case. Qu'est devenue cette passerelle ?", quatre, niveau="3")
    juge("S3 : la progression dite (« En 5e on SUIT, en 4e on ORGANISE ») dans un QCM de 3e", [], "Notion",
         "En 5e on SUIT un processus, en 4e on l'ORGANISE. Qu'attend-on de toi en 3e ?", quatre, niveau="3")
    juge("S3 : « En 5e » dans un QCM de 5e", [], "Notion", "En 5e, que fais-tu du diagramme de planification ?", quatre, niveau="5")
    juge("S3 : « en cinquième année » n'est pas une classe", [], "Notion", "Qui remontera l'échelle en cinquième année ?", quatre)
    juge("S3 : un leurre qui parle du passé de l'histoire (« le banc de l'an dernier »)", [], "Notion", "Pourquoi la simulation calcule-t-elle la rupture ?",
         ["pour vérifier le banc", "pour montrer que le banc de l'an dernier se trompait", "pour remplir", "par habitude"], r=0)

    # ── S4 : la notion affichée souffle la réponse ───────────────────────────
    crcn = ["CRCN 1.2 — Gérer des données", "CRCN 1.3 — Traiter des données", "CRCN 2.1 — Interagir", "CRCN 4.1 — Sécuriser"]
    juge("S4 : « La compétence CRCN 1.2 » au-dessus de « CRCN 1.2 — … »", ["S4"], "La compétence CRCN 1.2", "Ranger un fichier relève de…", crcn)
    juge("S4 : la notion renommée ne porte plus le nombre", [], "Ranger : quelle compétence ?", "Ranger un fichier relève de…", crcn)
    juge("S4 : un nombre que l'énoncé dit lui-même ne souffle rien", [], "« Entre 6 et 10 »", "Comment s'écrit « l'heure est entre 6 et 10 » ?",
         ["6 < heure < 10", "heure = 6 OU heure = 10", "heure ≥ 6 ET heure ≤ 10", "heure ENTRE 6 ET 10"], r=2)
    juge("S2 : « ci-dessous », le programme écrit dans l'énoncé", [], "Notion",
         "Dans le programme ci-dessous, quelle ligne correspond au losange ? SEUIL = 40 H = 25 heure = 8 if H < SEUIL and heure >= 6: print(1)", quatre)
    juge("S4 : un nombre que toutes les propositions reprennent ne désigne rien", [], "Les 5 volts",
         "Sur la carte, le 5 volts…", ["alimente en 5 volts", "coupe le 5 volts", "mesure le 5 volts", "double le 5 volts"])

    # ── E1 : une liste annoncée et tronquée (n°344) ──────────────────────────
    cinq = ["extraction, fabrication, distribution, utilisation, fin de vie", "achat, usage, panne, poubelle, oubli",
            "conception, vente, publicité, service, retour", "fabrication, extraction, usage, vente, fin de vie"]
    juge("E1 : « Les cinq étapes », quatre citées", ["E1"], "Les cinq étapes", "Dans l'ordre, les étapes du cycle de vie sont…",
         ["extraction, fabrication, utilisation, fin de vie"] + cinq[1:])
    juge("E1 : les cinq étapes citées toutes les cinq", [], "Les cinq étapes", "Dans l'ordre, les cinq étapes du cycle de vie sont…", cinq)
    juge("E1 : « trois fois » n'annonce pas une liste", [], "Notion", "On mesure trois fois, parce que…",
         ["une mesure peut être ratée", "le premier essai ne compte pas", "cela use les freins", "chacun en fait un"])

    with tempfile.TemporaryDirectory() as tmp:
        b = pathlib.Path(tmp)

        def poser(dossier, nom, contenu):
            p = b / dossier / nom
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(contenu, encoding="utf-8")
            return str(b / dossier)

        # ── en sous-processus : les trois sorties ────────────────────────────
        fautif = poser("fautif", "qcm_fautif.html", qcm(SAINE, {"q": "S2 consomme 165 Wh par km. Pourquoi ?", "o": quatre}))
        sortie("un QCM fautif, sans --strict : mesuré, pas refusé", 0, [fautif], "S1 code sans nom : 1")
        sortie("le même, avec --strict : refusé", 1, ["--strict", fautif], "✘ S1")
        sain = poser("sain", "qcm_sain.html", qcm(SAINE, SAINE))
        sortie("un QCM sain, avec --strict", 0, ["--strict", sain], "✅ aucune question ne renvoie ailleurs")
        vide = b / "vide"
        vide.mkdir()
        sortie("un dossier sans QCM ni séquence : en panne, pas vert (n°299)", 2, ["--strict", str(vide)], "rien n'a été lu")
        sans_banque = poser("sans_banque", "qcm_autre_gabarit.html", "<html><body>un autre gabarit</body></html>")
        sortie("une page qcm_ sans banque lisible : rien lu, en panne", 2, ["--strict", sans_banque])

        # ── les chantiers : comptés, jamais refusés ──────────────────────────
        lot = poser("lot", "qcm_lot.html", qcm(SAINE, dict(SAINE, doc=True)))
        poser("lot", "sequence_lot.html", "<html><!-- mode-mission v1 : début --><body>une séquence</body></html>")
        sortie("D1 et P1 : un QCM de séquence à une question sur document, une séquence sans billet", 0,
               ["--strict", "--chantiers", lot], "D1 moins de six questions sur document : 1 · P1 séquence sans billet de sortie : 1")
        poser("lot", "sequence_lot.html",
              '<html><!-- mode-mission v1 : début --><body><section class="card" id="billetSortie">…</section></body></html>')
        sortie("P1 : la même séquence, son billet de sortie posé", 0, ["--strict", lot], "P1 séquence sans billet de sortie : 0")

        # (26/11/2026) une séquence découpée en pages engendrées porte son billet sur la page de la dernière séance
        meta = '<meta name="sequence-sans-onglets" content="engendrée">'
        decoupe = poser("decoupe", "sequence_x_1_debut.html", "<html>%s<!-- mode-mission v1 : début --><body>p1</body></html>" % meta)
        poser("decoupe", "sequence_x_2_fin.html", "<html>%s<!-- mode-mission v1 : début --><body>p2</body></html>" % meta)
        sortie("P1 : deux pages découpées, aucune n'a de billet : les deux sont comptées", 0,
               ["--strict", decoupe], "P1 séquence sans billet de sortie : 2")
        poser("decoupe", "sequence_x_2_fin.html",
              '<html>%s<!-- mode-mission v1 : début --><body><section class="card" id="billetSortie">…</section></body></html>' % meta)
        sortie("P1 : le billet sur la dernière page découpée vaut pour ses pages sœurs", 0,
               ["--strict", decoupe], "P1 séquence sans billet de sortie : 0")
        isolee = poser("isolee", "sequence_y.html", "<html><!-- mode-mission v1 : début --><body>p</body></html>")
        poser("isolee", "sequence_z.html",
              '<html><!-- mode-mission v1 : début --><body><section class="card" id="billetSortie">…</section></body></html>')
        sortie("P1 : sans la déclaration de découpe, le billet d'une autre séquence du dossier ne compte pas", 0,
               ["--strict", isolee], "P1 séquence sans billet de sortie : 1")

    print("%d / %d tests passés" % (controles - len(echecs), controles))
    for e in echecs:
        print("  ✘ " + e)
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
