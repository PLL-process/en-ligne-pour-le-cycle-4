# -*- coding: utf-8 -*-
"""Banc de controle_mouvement.py : python3 _outils/tests_controle_mouvement.py"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import controle_mouvement as C  # noqa: E402

KF = "@keyframes avance{from{opacity:0}to{opacity:1}}"
CAS = [
    ("une animation sans repli est relevée (M1)",
     "<style>%s .a{animation:avance 1s}</style>" % KF, 1, False),
    ("« * { animation: none } » sous moins de mouvement couvre tout",
     "<style>%s .a{animation:avance 1s}@media (prefers-reduced-motion: reduce){*{animation:none!important}}</style>" % KF, 0, False),
    ("la classe animée cachée sous moins de mouvement est couverte",
     "<style>%s .flux{animation:avance 1.6s linear infinite}@media (prefers-reduced-motion:reduce){.flux{display:none}}</style>"
     "<button>⏸ Pause</button>" % KF, 0, False),
    ("un repli qui vise une autre classe ne couvre pas",
     "<style>%s .a{animation:avance 1s}@media (prefers-reduced-motion:reduce){.b{animation:none}}</style>" % KF, 1, False),
    ("un repli qui ne fait qu'allonger la durée ne couvre pas",
     "<style>%s .a{animation:avance 1s}@media (prefers-reduced-motion:reduce){.a{animation-duration:3s}}</style>" % KF, 1, False),
    ("une boucle sans fin sans bouton pause est relevée (M2)",
     "<style>%s .a{animation:avance 1s infinite}@media (prefers-reduced-motion:reduce){.a{animation:none}}</style>" % KF, 0, True),
    ("une boucle sans fin avec un bouton « Arrêter l'animation » ne l'est pas",
     "<style>%s .a{animation:avance 1s infinite}@media (prefers-reduced-motion:reduce){.a{animation:none}}</style>"
     "<button type=button>Arrêter l'animation</button>" % KF, 0, False),
    ("une animation dans un attribut style n'est couverte que par « * »",
     "<style>%s @media (prefers-reduced-motion:reduce){.a{animation:none}}</style><div style=\"animation:avance 2s\"></div>" % KF, 1, False),
    ("une animation posée sous « no-preference » est son propre repli",
     "<style>@media (prefers-reduced-motion:no-preference){ .loupe img{animation:avance .16s ease-out} %s }</style>" % KF, 0, False),
    ("un bloc qui pose son bouton pause (data-pause-animations) compte",
     "<style>%s .a{animation:avance 1s infinite}@media (prefers-reduced-motion:reduce){.a{animation:none}}</style>"
     "<script>b.setAttribute('data-pause-animations','')</script>" % KF, 0, False),
    ("« .zone * » sous moins de mouvement compte pour ce qui est dessous",
     "<style>%s .zone .case{animation:avance .4s}@media (prefers-reduced-motion:reduce){.zone *{animation:none}}</style>" % KF, 0, False),
    ("une @keyframes que rien n'utilise ne compte pas",
     "<style>%s .a{color:red}</style>" % KF, 0, False),
    ("deux animations sur une règle : chacune est lue",
     "<style>@keyframes x{to{opacity:1}}@keyframes y{to{opacity:0}} .t{animation:x 4s steps(60) forwards,y .9s step-end infinite}</style>", 2, True),
]


def jouer():
    ok = 0
    for nom, html, m1, m2 in CAS:
        anims, couvertes, pause = C.lire(html)
        uniques = set((a, s) for a, s, _ in anims)
        n1 = len([x for x in uniques if x not in couvertes])
        b2 = any(inf for _, _, inf in anims) and not pause
        bon = (n1 == m1 and b2 == m2)
        ok += bon
        print(("✅ " if bon else "❌ ") + nom + ("" if bon else "  — M1 %d (attendu %d), M2 %s (attendu %s)" % (n1, m1, b2, m2)))
    print("%d/%d cas passent — controle_mouvement.py" % (ok, len(CAS)))
    return 0 if ok == len(CAS) else 1


if __name__ == "__main__":
    sys.exit(jouer())
