# -*- coding: utf-8 -*-
"""La piqûre de rappel du cahier des charges, dans chaque séquence de 4e et de 3e qui s'en sert (demande du professeur
du 04/11/2026). Les rappels sont décrits dans `donnees_rappel_cdc.py` (une entrée par séquence, avec son objet et ses
lignes) ; ce lot ne fait que les poser, juste avant l'activité qui se sert du cahier des charges.

Posés (13 séquences) : 4e_C2.1 Hangzhou, 4e_C6.2, 4e_C7.1, 4e_C7.3, 4e_C7.5, 4e_C8.1 ; 3e_C3.1 Shenzhen, 3e_C7.3, 3e_C7.5,
3e_C7.7, 3e_C8.1, 3e_C8.2, 3e_C9.2 (la page tout-en-un : `generer_les_quatre_pages.py` engendre ensuite les quatre pages).
Les deux ateliers « Le diagramme des exigences » (4e, 3e) reçoivent le leur par `moteur.page_atelier`.

Non posés, et pourquoi :
  · 4e_C4.1 (jardin connecté) : l'exercice incrusté à l'activité 5 EST la leçon (atelier pieuvre 4e, exercice 6) ; un
    rappel juste avant ferait faire deux fois la même chose. Le rappel s'y fond dans l'exercice existant.
  · 4e_C7.7, 4e_C9.1, 3e_C1.1 : le cahier des charges n'y est que cité, dans une correction ou une aide.
  · 3e_C7.1 (capteur de confort) : la page part d'un besoin d'une ligne et de critères de choix ; le mot n'y apparaît
    que dans l'exercice FAST incrusté.
  · 4e_C8.3 : pas de séquence, un panneau qui renvoie à l'atelier des exigences de 4e, qui a son rappel.
"""
import importlib.util as _iu
import pathlib as _pl

_spec = _iu.spec_from_file_location("donnees_rappel_cdc", _pl.Path(__file__).resolve().parent.parent / "donnees_rappel_cdc.py")
_rc = _iu.module_from_spec(_spec)
_spec.loader.exec_module(_rc)

ENTREES = [dict(id="%s-%s" % (_rc.COURT, r["id"]), rappel=r["id"], module="rappel_cdc", niveau=r["niveau"], exos=[],
                sequence=r["sequence"], avant=r["avant"], balise=r["balise"], balise_exo=r["balise_exo"])
           for r in _rc.RAPPELS if r.get("sequence")]
