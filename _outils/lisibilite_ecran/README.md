# Lisibilité à l'écran — un bloc commun, posé par outil

**Demande de Pascal, 26/11/2026** : « lancer directement tout sur toutes les séquences etc. », puis « si quelque chose
d'autre ne va pas, tu le corriges ». Le 26/11 au soir, l'audit des dix skills de design
(`docs/audits/AUDIT_SKILLS_DESIGN_2026-11-26.md`) propose une vague « lisibilité au téléphone » ; réponse de Pascal :
« Tu as carte blanche » (26/11, 27/11 et 28/11). Branche transversale `fable/skills-design-audit-26-11`.

## Ce que fait le bloc

Il ne touche **que l'écran** (`@media screen`) : l'impression ne change pas (captures A4 de onze pages, avant et après :
identiques au pixel). Chaque page ne reçoit que les règles qui la concernent :

| Règle | Pages qui la reçoivent | Pourquoi |
|---|---|---|
| Note de sauvegarde et problématique alignées à gauche sous 700 px | celles qui portent `.saved-note` ou `.problematique` | Un texte centré de six lignes n'a pas de bord où reprendre la ligne : coûteux pour un élève qui lit difficilement. `!important` sur la note : 27 pages la centrent par un style écrit dans la balise |
| Chapeau centré s'il tient sur une ligne, aligné à gauche s'il est long (sous 700 px) | QCM (`.subtitle`), lexiques (`p.sub.ms-entete`), ateliers (`p.mission`) | `width:fit-content` et marges automatiques : un chapeau court reste centré sous le titre. Pas sur un chapeau en `nowrap` (il déborderait) |
| Légendes des synthèses élève à 13 px au moins | synthèses élève dont une règle écrit une légende sous 13 px | Le même sélecteur que la page (sinon la règle de la page gagne), `max(13px, taille d'origine)` : jamais plus petit qu'avant |
| Barre du haut opaque, même couleur | pages dont `#navharm` est translucide **sans** flou | Le texte qui défile se lisait à travers la barre (vu en mode mission, à l'ouverture). `nav#navharm` : sur dix séquences, la règle de la barre est écrite dans le corps de la page, après ce bloc. Une barre floutée (verre dépoli voulu) n'est pas touchée |
| Marge de défilement : 64 px sous la barre du haut, 104 px au-dessus du pied « Suivant » du mode mission | pages à barre du haut, pages en mode mission | Au clavier (Tab), le navigateur amenait le champ sous la barre ou sous le pied (137 pages en vue élève). Sert aussi aux liens vers une ancre. Une page qui règle déjà sa marge garde la sienne |

## Les commandes

```bash
python3 _outils/lisibilite_ecran/poser.py --site               # pose ou met à jour le bloc sur tout le site
python3 _outils/lisibilite_ecran/poser.py --verifier --site    # 0 : à jour · 1 : une page en retard · 2 : panne
python3 _outils/lisibilite_ecran/poser.py <page.html> […]      # quelques pages
```

Le bloc est entre `<!-- lisibilite-ecran vN : début … -->` et `<!-- lisibilite-ecran : fin -->`, juste avant `</head>`
(avant `<body` dans les quatre pages de la station `3e_C9.2`, qui n'écrivent pas `</head>`). **Il ne se modifie pas dans
la page** : la source unique est `poser.py`. Une page qui n'a plus rien à recevoir rend son bloc. Après une retouche de
`poser.py` : `--site`, puis `--verifier --site`, puis les mesures ci-dessous.

## Mesurer avant et après

Les mesures se font **dans la vue de l'élève**. Un navigateur piloté (`navigator.webdriver`) reçoit la page complète ;
l'élève arrive en mode mission (décision du 14/11/2026). Mesurer sans `--eleve`, c'est mesurer une page que l'élève ne
voit pas d'abord (erreur commise le 26/11, rectifiée au rapport).

```bash
python3 docs/audits/skills-design-2026-11-26/mesures_telephone.py . --json t.json --eleve   # texte centré, barre, à 390 px
python3 docs/audits/skills-design-2026-11-26/mesures_rendu.py . --json r.json --procs 2 --eleve   # clavier, tailles, cibles
python3 docs/audits/skills-design-2026-11-26/bilan_rendu.py r.json
```

## Ce qu'il ne fait pas

`p.question` des synthèses (le titre-question, en gras) reste centré : un titre court centré se lit. Les mentions de
licence non plus. Le bouton « Mode mission » flottant n'est pas touché : il n'apparaît qu'une fois l'élève sorti du mode
mission (demande de Pascal du 16/11/2026).
