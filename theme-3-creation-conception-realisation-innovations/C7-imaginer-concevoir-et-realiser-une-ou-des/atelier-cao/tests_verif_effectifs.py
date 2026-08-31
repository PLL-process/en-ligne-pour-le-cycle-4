# -*- coding: utf-8 -*-
"""tests_verif_effectifs.py — le contrôle doit refuser, et refuser au bon endroit.

Un contrôle qui ne refuse jamais est une décoration. Celui-ci est né d'une erreur
réelle — six occurrences de « trois TP » dans un atelier qui en comptait quatre,
dont deux seulement avaient été corrigées la veille — et ce banc vérifie qu'il la
retrouverait, ainsi que les quatre trous voisins que la même croissance avait
laissés.

Il vérifie aussi, et c'est aussi important, qu'il **ne crie pas au loup** : une
phrase datée, une phrase restreinte à un niveau, un article (« un TP mené en
classe ») et un nombre écrit dans un commentaire ne sont pas des fautes.
(Règle d'or n°248 : un contrôle qui signale du faux finit ignoré.)

Les cas se jouent sur des arborescences **fabriquées**, jamais sur le dépôt —
sauf le dernier, qui exige que l'atelier réel passe.

Usage : python3 tests_verif_effectifs.py
Sortie : 0 si tout passe, 1 sinon.
"""
import contextlib
import io
import json
import os
import pathlib
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import verif_effectifs as VE  # noqa: E402

MANIFESTE_JUSTE = {
    "eleve": ["tp_a.html", "tp_b.html"],
    "codes_servis": ["5e_C7.6"],
    "evaluation": {"5e_C7.6": "qcm.html"},
    "releves_de_captures": ["RELEVE_A.md", "RELEVE_B.md"],
    "releve_par_tp": {"tp_a.html": "RELEVE_A.md", "tp_b.html": "RELEVE_B.md"},
    "chaine_de_production": {"scenarios": ["a.json", "b.json"]},
}

SCENARIOS = {
    "a.json": {"fichier_sortie": "tp_a.html", "retour_sequence": "../x/y.html"},
    "b.json": {"fichier_sortie": "tp_b.html", "retour_sequence": "../x/z.html"},
}


def atelier(tmp, manifeste=None, scenarios=None, prose=None, fichiers=None, voisins=None):
    """Fabrique un atelier minimal et renvoie sa racine.

    `tmp` est le dossier PARENT : l'atelier vit dans `tmp/atelier-cao`, et
    `voisins` y dépose des fichiers frères — c'est là que vivait la phrase
    fautive du 31/08 (n°263). Chaque cas a son propre parent, sinon un cas
    lirait les voisins d'un autre.
    """
    r = pathlib.Path(tmp) / "atelier-cao"
    (r / "scenarios").mkdir(parents=True, exist_ok=True)
    (r / "Synthèses").mkdir(parents=True, exist_ok=True)
    m = json.loads(json.dumps(manifeste if manifeste is not None else MANIFESTE_JUSTE))
    (r / "manifest_cao.json").write_text(json.dumps(m, ensure_ascii=False), encoding="utf-8")
    for nom, contenu in (scenarios if scenarios is not None else SCENARIOS).items():
        (r / "scenarios" / nom).write_text(json.dumps(contenu, ensure_ascii=False),
                                           encoding="utf-8")
    for nom in (fichiers if fichiers is not None
                else ["tp_a.html", "tp_b.html", "qcm.html", "RELEVE_A.md", "RELEVE_B.md"]):
        (r / nom).write_text("<p>page</p>\n" if nom.endswith(".html") else "page\n",
                             encoding="utf-8")
    if prose:
        for nom, texte in prose.items():
            (r / nom).write_text(texte, encoding="utf-8")
    for nom, texte in (voisins or {}).items():
        chemin = r.parent / nom
        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_text(texte, encoding="utf-8")
    return r


def jouer(racine):
    """Lance le contrôle sur cette racine et renvoie (code de sortie, texte imprimé)."""
    sortie = io.StringIO()
    with contextlib.redirect_stdout(sortie):
        code = VE.main(racine=pathlib.Path(racine))
    return code, sortie.getvalue()


def main():
    echecs, controles = [], 0

    def cas(titre, racine, doit_refuser, attendu_dans=""):
        nonlocal controles
        controles += 1
        code, texte = jouer(racine)
        if doit_refuser and code == 0:
            echecs.append("%s : le contrôle a accepté, il devait refuser" % titre)
        elif not doit_refuser and code != 0:
            echecs.append("%s : le contrôle a refusé\n     %s"
                          % (titre, texte.strip().replace("\n", "\n     ")))
        elif attendu_dans and attendu_dans not in texte:
            echecs.append("%s : refus correct mais le message ne dit pas « %s »\n     %s"
                          % (titre, attendu_dans, texte.strip().replace("\n", "\n     ")))

    with tempfile.TemporaryDirectory() as tmp:
        base = pathlib.Path(tmp)

        # ── 1. un atelier qui dit vrai passe ────────────────────────────────
        cas("un atelier qui se compte juste",
            atelier(base / "c1", prose={"fiche.md": "Les deux TP de l'atelier.\n"}),
            False)

        # ── 2. l'erreur réelle : la prose est en retard d'un TP ─────────────
        m = json.loads(json.dumps(MANIFESTE_JUSTE))
        m["eleve"] = ["tp_a.html", "tp_b.html", "tp_c.html"]
        m["releves_de_captures"] = ["RELEVE_A.md", "RELEVE_B.md", "RELEVE_C.md"]
        m["releve_par_tp"]["tp_c.html"] = "RELEVE_C.md"
        m["chaine_de_production"]["scenarios"] = ["a.json", "b.json", "c.json"]
        sc = dict(SCENARIOS,
                  **{"c.json": {"fichier_sortie": "tp_c.html", "retour_sequence": "../x/c.html"}})
        f = ["tp_a.html", "tp_b.html", "tp_c.html", "qcm.html",
             "RELEVE_A.md", "RELEVE_B.md", "RELEVE_C.md"]
        cas("« les deux TP » dans un atelier qui en compte trois",
            atelier(base / "c2", m, sc, {"fiche.md": "Les deux TP le disent en tête.\n"}, f),
            True, "deux TP")

        # ── 3. toutes les occurrences sont dites, pas seulement la première ──
        controles += 1
        _code, texte = jouer(atelier(
            base / "c3", m, sc,
            {"fiche.md": "Les deux TP le disent en tête.\n",
             "autre.md": "Les images des deux TP manquent.\n",
             "Synthèses/s.html": "<p>Les deux TP ne sont pas prêts.</p>\n"}, f))
        if texte.count("deux TP") < 3:
            echecs.append("le contrôle ne nomme pas les TROIS endroits fautifs — "
                          "c'est précisément l'erreur qu'il existe pour empêcher")

        # ── 4. la prose du manifeste lui-même est lue ───────────────────────
        m4 = json.loads(json.dumps(m))
        m4["limites_declarees"] = ["La règle n°77 refuse les deux TP."]
        cas("une phrase fausse dans le manifeste",
            atelier(base / "c4", m4, sc, None, f), True, "manifest_cao.json")

        # ── 5. les chiffres comptent comme les lettres ──────────────────────
        cas("« les 2 TP » écrit en chiffres",
            atelier(base / "c5", m, sc, {"fiche.md": "Les 2 TP sont prêts.\n"}, f),
            True, "2 TP")

        # ── 6. un TP sans relevé de captures ────────────────────────────────
        m6 = json.loads(json.dumps(MANIFESTE_JUSTE))
        del m6["releve_par_tp"]["tp_b.html"]
        m6["releves_de_captures"] = ["RELEVE_A.md"]
        cas("un TP dont personne ne réclame les images",
            atelier(base / "c6", m6), True, "pas de relevé de captures déclaré")

        # ── 7. un relevé déclaré qui n'existe pas ───────────────────────────
        m7 = json.loads(json.dumps(MANIFESTE_JUSTE))
        m7["releve_par_tp"]["tp_b.html"] = "RELEVE_FANTOME.md"
        cas("un relevé déclaré et absent du disque",
            atelier(base / "c7", m7), True, "RELEVE_FANTOME.md")

        # ── 8. un relevé rattaché à aucun TP ────────────────────────────────
        m8 = json.loads(json.dumps(MANIFESTE_JUSTE))
        m8["releves_de_captures"].append("RELEVE_ORPHELIN.md")
        cas("un relevé orphelin", atelier(base / "c8", m8), True,
            "n'est rattaché à aucun TP")

        # ── 9. un scénario qui produit une page non déclarée ────────────────
        sc9 = dict(SCENARIOS,
                   **{"c.json": {"fichier_sortie": "tp_surprise.html",
                                 "retour_sequence": "../x/c.html"}})
        m9 = json.loads(json.dumps(MANIFESTE_JUSTE))
        m9["chaine_de_production"]["scenarios"] = ["a.json", "b.json", "c.json"]
        cas("un scénario dont la page n'est pas déclarée",
            atelier(base / "c9", m9, sc9), True, "tp_surprise.html")

        # ── 10. un code servi sans adresse d'évaluation (règle n°250) ───────
        m10 = json.loads(json.dumps(MANIFESTE_JUSTE))
        m10["codes_servis"].append("4e_C7.2")
        cas("un code déclaré servi et évalué nulle part",
            atelier(base / "c10", m10), True, "4e_C7.2")

        # ── 11. une adresse d'évaluation qui n'existe pas ───────────────────
        m11 = json.loads(json.dumps(MANIFESTE_JUSTE))
        m11["evaluation"]["5e_C7.6"] = "qcm_qui_nexiste_pas.html"
        cas("une adresse d'évaluation morte",
            atelier(base / "c11", m11), True, "qcm_qui_nexiste_pas.html")

        # ── 12. le scénario de modèle est écarté, pas refusé ────────────────
        sc12 = dict(SCENARIOS,
                    **{"_MODELE.json": {"fichier_sortie": "tp_modele.html",
                                        "retour_sequence": "../<niveau>/<code>/x.html"}})
        m12 = json.loads(json.dumps(MANIFESTE_JUSTE))
        m12["chaine_de_production"]["scenarios"] = ["_MODELE.json", "a.json", "b.json"]
        cas("un scénario de gabarit ne s'engendre pas et ne compte pas",
            atelier(base / "c12", m12, sc12), False)

        # ── 13 à 16. ce qui NE DOIT PAS être signalé ────────────────────────
        cas("une phrase datée décrit le passé",
            atelier(base / "c13", m, sc,
                    {"src.md": "Les seize rendus des trois TP (11 août 2026).\n"}, f),
            False)
        cas("une phrase restreinte à un niveau",
            atelier(base / "c14", m, sc,
                    {"fiche.md": "Les deux TP de 5e ouvrent la progression.\n"}, f),
            False)
        cas("« un TP » est un article, pas un compte",
            atelier(base / "c15", m, sc,
                    {"fiche.md": "La phrase de référence, d'un TP mené en classe.\n"}, f),
            False)
        cas("un nombre dans un commentaire n'est pas lu",
            atelier(base / "c16", m, sc,
                    {"p.html": "<!-- jadis les deux TP -->\n<p>rien</p>\n"}, f),
            False)
        cas("un nombre dans un bloc de code n'est pas lu",
            atelier(base / "c17", m, sc,
                    {"doc.md": "```\nles deux TP\n```\n"}, f),
            False)

        # ── 18. une phrase qui va à la ligne reste une phrase (n°262) ───────
        # Le cas réel du 31/08 : « écrite en tête des trois\n  TP ». Il avait
        # traversé la première version de ce contrôle ET deux recherches grep.
        cas("un compte coupé par un retour à la ligne",
            atelier(base / "c18", m, sc,
                    {"s.html": "<p>exception assumée, écrite en tête des deux\n  TP.</p>\n"},
                    f),
            True, "deux TP")

        # ── 19. un voisin qui parle de l'atelier en hérite les comptes (n°263)
        cas("un fichier voisin qui parle d'Onshape et compte faux",
            atelier(base / "c19", m, sc, None, f,
                    voisins={"5e/5e_C7.6/Synthèses/s.html":
                             "<p>Onshape exige le réseau : écrit en tête des deux TP.</p>\n"}),
            True, "deux TP")

        # ── 20. un voisin étranger à l'atelier reste hors périmètre ─────────
        # Le périmètre est DÉCLARÉ — un fichier qui nomme Onshape ou l'atelier
        # CAO —, pas deviné. Un lot réseaux qui compte ses propres TP n'a rien
        # à voir avec celui-ci.
        cas("un fichier voisin étranger à l'atelier n'est pas jugé",
            atelier(base / "c20", m, sc, None, f,
                    voisins={"4e/4e_C4.7/README.md":
                             "Le lot réseaux comprend deux TP débranchés.\n"}),
            False)

    # ── 21. l'atelier réel doit passer, sans rien avoir à réécrire ──────────
    controles += 1
    code, texte = jouer(VE.A)
    if code != 0:
        echecs.append("l'atelier réel ne passe pas :\n     "
                      + texte.strip().replace("\n", "\n     "))

    if echecs:
        for e in echecs:
            print("❌ " + e)
        print("\n%d / %d" % (controles - len(echecs), controles))
        return 1
    print("✅ %d contrôles — le contrôle refuse ce qui est faux, et se tait sur ce qui "
          "ne l'est pas" % controles)
    print("\n%d / %d" % (controles, controles))
    return 0


if __name__ == "__main__":
    sys.exit(main())
