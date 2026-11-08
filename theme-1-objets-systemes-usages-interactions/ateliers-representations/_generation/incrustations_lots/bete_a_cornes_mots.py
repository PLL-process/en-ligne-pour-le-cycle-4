# -*- coding: utf-8 -*-
"""Thème 1 — la bête à cornes et ses mots de référence (04/11/2026).

Pascal, le 04/11/2026 : « Les mots de cette représentation devront être utilisés plusieurs fois, ce sont des
références » (utilisateur, matière d'œuvre, produit, fonction — la méthode APTE), puis « rien ne nous empêche de faire
une piqûre de rappel en 4e et 3e », « sous forme d'exercices intégrés aussi ».

Deux sortes d'entrées :
  · le dessin de référence (`html`, sans exercice ni moteur), là où la bête à cornes est présentée :
      carte des représentations      après le tableau « Analyse externe — Thème 1 »
      5e Shenzhen (5e_C2.1)          séance 1, fin de l'activité 1 a), avant b)
      5e Shanghai (5e_C3.1)          séance 1, activité 1, juste avant « D'abord le besoin »
  · la piqûre de rappel sur l'objet de la séquence (2 à 3 min), au moment où la bête à cornes revient, juste avant
    l'exercice de l'atelier « Le besoin » déjà incrusté :
      4e Tsinghua (4e_C1.1-C1.3)     séance 5, activité 5 — le système de détection des feux
      4e Hangzhou (4e_C3.1-C3.3)     séance 1, activité 1 — la flotte de vélos en libre-service
      3e Shenzhen (3e_C3.1-C3.4)     séance 1, activité 1 — le local des serveurs
Le repère de pose d'un rappel est le marqueur de début de l'incrustation qui le suit : il est unique dans la page.
"""
T1 = "theme-1-objets-systemes-usages-interactions/"
C1 = T1 + "C1-decrire-les-liens-entre-usages-et-evolutions/"
C2 = T1 + "C2-decrire-les-interactions-entre-un-objet-ou/"
C3 = T1 + "C3-caracteriser-et-choisir-un-objet-ou-un/"


def debut(ident):
    return "<!-- ateliers-representations:debut %s -->" % ident


NOTE_RAPPEL = ("Ce rappel accompagne <a href=\"%s\">l'atelier de {niv} « Le besoin »</a>, qui a le sien, sur {objet}, avec les "
               "autres exercices et le QCM.")

ENTREES = [
    dict(id="bc-ref-carte", module="besoin", html="FIG_REFERENCE_CARTE",
         sequence=T1 + "_reperes/carte_des_representations.html", avant="<h3>Analyse interne — Thème 2</h3>"),
    dict(id="bc-ref-5e-shenzhen", module="besoin", html="FIG_REFERENCE_SHENZHEN",
         sequence=C2 + "5e/5e_C2.1/sequence_5e_C2_shenzhen_station_velos.html",
         avant="  <!-- ══ b) : l'exercice du vélo-cargo"),
    dict(id="bc-ref-5e-shanghai", module="besoin", html="FIG_REFERENCE_APTE",
         sequence=C3 + "5e/5e_C3.1/sequence_5e_C3.1-C3.4_shanghai.html", avant=debut("bc-5e-shanghai-c3")),
    dict(id="bcm-4e-tsinghua-s5", module="besoin", niveau="4e", exos=["rappel-feux"], cours=False,
         sequence=C1 + "4e/4e_C1.1/sequence_4e_C1.1-C1.3_tsinghua_feux.html", avant=debut("bc-4e-tsinghua-s5"),
         balise="h3", balise_exo="h4",
         titre="🧠 Piqûre de rappel&nbsp;: les mots de la bête à cornes, sur ton système",
         # révision du 08/11/2026 (la charge de lecture de la séance 5) : le rappel ne sert qu'à qui a oublié les mots
         replie="🧠 Piqûre de rappel (2 à 3 min)&nbsp;: les quatre mots de la bête à cornes — ouvre-la si tu ne les as "
                "plus en tête",
         intro="La bête à cornes revient juste après, sur le jardin d'un collège. Avant, retrouve ses quatre <b>mots de "
               "référence</b> — utilisateur, matière d'œuvre, produit, fonction — sur le système de détection des feux des "
               "séances 1 à 4. Deux à trois minutes&nbsp;; l'exercice se vérifie tout seul et a sa correction complète.",
         note=NOTE_RAPPEL.format(niv="4e", objet="le jardin")),
    dict(id="bcm-4e-hangzhou-c3", module="besoin", niveau="4e", exos=["rappel-velos"], cours=False,
         sequence=C3 + "4e/4e_C3.1/sequence_4e_C3.1-C3.3_hangzhou.html", avant=debut("bc-4e-hangzhou-c3"),
         balise="h4", balise_exo="h5",
         titre="🧠 Piqûre de rappel&nbsp;: les mots de la bête à cornes, sur la flotte de Hangzhou",
         intro="Tu vas tirer des caractéristiques d'une bête à cornes. Avant, retrouve ses quatre <b>mots de référence</b> — "
               "utilisateur, matière d'œuvre, produit, fonction — sur <b>ton</b> objet, la flotte de vélos de Hangzhou. Deux "
               "à trois minutes&nbsp;; l'exercice se vérifie tout seul et a sa correction complète.",
         note=NOTE_RAPPEL.format(niv="4e", objet="le jardin")),
    dict(id="bcm-3e-shenzhen-c3", module="besoin", niveau="3e", exos=["rappel-local"], cours=False,
         sequence=C3 + "3e/3e_C3.1/sequence_3e_C3.1-C3.4_shenzhen.html", avant=debut("bc-3e-shenzhen-c3"),
         balise="h4", balise_exo="h5",
         titre="🧠 Piqûre de rappel&nbsp;: les mots de la bête à cornes, sur le local des serveurs",
         intro="Établir une liste commence par un besoin bien écrit, dans une bête à cornes. Avant, retrouve ses quatre "
               "<b>mots de référence</b> — utilisateur, matière d'œuvre, produit, fonction — sur <b>ton</b> problème, le "
               "local des serveurs. Deux à trois minutes&nbsp;; l'exercice se vérifie tout seul et a sa correction complète.",
         note=NOTE_RAPPEL.format(niv="3e", objet="l'alerte cyclonique")),
]
