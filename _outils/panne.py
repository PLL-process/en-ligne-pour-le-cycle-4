# -*- coding: utf-8 -*-
"""panne.py — « un contrôle qui n'a rien vérifié n'est pas vert, il est en panne ».

LE CONSTAT QUI A DONNÉ CE MODULE
--------------------------------
Le 19/09/2026, `controle_impression.mjs` s'est révélé muet depuis le 02/09 : sa
garde de lancement ne passait pas sous Windows, `main()` ne partait pas, et le
script **sortait à 0 sans avoir lu une seule page**. Dix-sept jours. Le défaut
n'était pas la garde — une garde se répare en trois lignes — mais le fait que
rien, dans ce script, ne distinguait « j'ai tout vérifié, tout va bien » de
« je n'ai rien vérifié du tout ».

Le balayage qui a suivi a mesuré l'étendue : recopiés dans une racine vide, les
**dix-sept** contrôles du dépôt sortaient **tous à 0**. La plupart écrivaient
honnêtement « 0 page(s) lues » — mais un code de sortie 0 est ce que lit une
batterie, un `&&`, un rapport de tests. Et `controle_cadres.py` écrivait, sur un
dépôt entièrement vide, « ✅ aucun cadre <iframe> vers fr.vittascience.com ».

CE QUE CE MODULE DONNE
----------------------
Une seule façon de le dire, pour que la règle d'or n°299 ait la même forme d'un
outil à l'autre : un message sur la **sortie d'erreur** — donc visible même sous
`--muet`, qui n'éteint que `stdout` — et un **code de sortie 2**.

    0  le contrôle a tourné et n'a rien à refuser
    1  le contrôle a tourné et refuse quelque chose
    2  le contrôle n'a RIEN PU VÉRIFIER

Usage, à la fin du travail de comptage et avant tout verdict :

    import panne
    if not pages_lues:
        return panne.rien_vu("aucune page .html sous %s" % DEPOT)

`rien_vu` REND 2 au lieu de sortir lui-même : les bancs appellent `main()` et
doivent pouvoir lire ce 2 comme une valeur, pas le subir comme un `SystemExit`.
"""
import sys

CODE = 2

#: Ce qu'on écrit sous le motif, toujours, pour qu'un 2 ne soit jamais muet.
RAPPEL = ("     Ce contrôle n'a RIEN vérifié ; ne le lisez pas comme un succès "
          "(règle d'or n°299).")


def rien_vu(motif, rappel=RAPPEL):
    """Annonce la panne sur stderr et rend le code de sortie 2.

    `motif` dit ce qui manquait, en clair et avec le chemin regardé : « aucune
    page .html sous C:\\… », « racine introuvable », « aucun lot à médias ».
    Un motif sans chemin oblige celui qui lit à deviner où l'outil a cherché.
    """
    print("⛔ EN PANNE — %s" % motif, file=sys.stderr)
    if rappel:
        print(rappel, file=sys.stderr)
    return CODE
