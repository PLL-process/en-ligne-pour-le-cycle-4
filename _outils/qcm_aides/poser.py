# -*- coding: utf-8 -*-
"""qcm_aides/poser.py — un QCM qui aide avant de corriger (règles d'or n°337 et n°339, 17/11/2026).

LE CONSTAT
----------
Audit « double regard » (élève de 5e / inspecteur) du QCM de Shenzhen, transmis par Pascal le 17/11/2026 :
  · « avant de commencer, l'élève devrait lire trois informations très simples : ce qu'il va apprendre, ce qu'il doit
    savoir faire et comment réussir » — Pascal l'étend « à toutes les séquences » (n°337) ;
  · « des aides progressives : lorsqu'un élève se trompe, il devrait pouvoir consulter un premier indice, puis une
    explication plus détaillée, sans voir immédiatement la bonne réponse » ;
  · « une révision fondée sur les difficultés : si l'élève confond régulièrement un interacteur et une exigence, le
    système devrait lui proposer plusieurs questions supplémentaires sur cette distinction ».
Le gabarit maison montrait la correction complète dès la validation, et ne savait rien des confusions.

CE QUE POSE L'OUTIL (sur un QCM du gabarit maison, `const QUESTIONS`)
-----------------------------------------------------------------
Les DONNÉES du lot, dans un fichier JSON (`qcm_aides_<lot>.json`), réécrites à chaque passage :
  · « 🎯 Avant de commencer : trois choses à lire », avant « Ma progression » : `avant_de_commencer` =
    {"revoir": [lignes], "savoir_faire": [lignes], "reussir": [lignes]} (une idée par ligne, HTML court permis) ;
  · les PIÈGES : `pieges` = {clé: {"libelle": "…", "notions": ["notion exacte d'une question", …]}} — une
    question appartient à un piège par sa notion (`n`) ; un piège a au moins trois questions ;
  · facultatif, `bilan_remarquable` : le premier message du bilan (« Remarquable ! … »), quand celui du gabarit
    parle d'autres notions que celles du QCM (n°338).
Le MOTEUR, commun, posé une fois (chaque morceau cherche sa marque avant de se poser) :
  · les aides progressives — une réponse fausse montre 💡 le pourquoi de la proposition choisie (`d[k]`), puis sur
    demande 💡💡 la règle à appliquer (`ret`), puis 📖 la correction complète ; la bonne réponse n'est ni dite ni
    marquée en vert avant ; « 🔁 Réessayer » à chaque étape. Juste ou non répondue : la correction complète, comme
    avant (n°96) ;
  · la révision par pièges — une erreur propose « Réviser ce piège : N questions » (mode `piege`, les questions pas
    encore réussies d'abord) ; le bilan liste les pièges ratés, du plus fréquent au moins fréquent ; le compte des
    erreurs par piège est sauvegardé.
Le JavaScript posé n'imbrique aucun gabarit (`${…`…`…}`) : `_outils/sans_modale.py` lit les scripts avec un
analyseur simple, qui s'y perd.

Usage :
  python3 _outils/qcm_aides/poser.py <qcm.html> <donnees.json>            pose ou met à jour
  python3 _outils/qcm_aides/poser.py <qcm.html> <donnees.json> --verifier  dit si la page est à jour (0 / 1)
  python3 _outils/qcm_aides/poser.py --etat [--strict] [racine]            mesure le dépôt (n°337 côté QCM, n°339)
Sortie : 0 à jour · 1 à poser / à corriger (--verifier, --strict) · 2 rien lu, ou données refusées.
"""
from __future__ import annotations

import json
import os
import re
import sys

DEPOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ANCRE_CARTE = '<section class="card">\n  <h2>📊 Ma progression</h2>'
CARTE_RE = re.compile(r'<section class="card trois-lignes" id="trois-lignes">.*?</section>\n\n', re.S)
PIEGES_RE = re.compile(r"/\* Les pièges : .*?function questionsDuPiege\(f\)\{[^\n]*\}\n", re.S)
BILAN_RE = re.compile(r'(const msg= note>=16\?")([^"]*)(":)')

MOTEUR = []   # (marque, ancre, texte, position)


def m(marque, ancre, texte, position):
    MOTEUR.append((marque, ancre, texte, position))


m(".trois-lignes-liste{", '  .correction-bloc{margin-top:16px;border-radius:12px;padding:14px 16px;display:none}\n', '''  .trois-lignes-liste{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:10px}
  .trois-lignes-liste li{border-left:3px solid #61dafb;padding:2px 0 2px 12px;line-height:1.55}
  .indice-zone{margin:8px 0 10px;padding:10px 12px;border-radius:10px;background:rgba(255,213,79,.08);border:1px solid #6b5a2f}
  .indice-zone p{margin:6px 0}
  .indice-zone .btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
  .piege-ligne{margin-top:10px;padding-top:8px;border-top:1px dashed #6b5a2f}
  .pieges-bilan li{margin:6px 0}
''', "avant")
m("indice2={}", 'let timerInterval=null, choixTemp=null;',
  'let timerInterval=null, choixTemp=null;\n'
  'const corrVue={}, indice2={};   /* la correction complète, l\'indice n°2 ouverts (non sauvegardés : l\'indice revient) */',
  "remplace")
m('"piege","erreursPiege"', '["reponses","validees","marquees","courante","mode","sousListe","tempsMs","sansMinuteur","identite"].forEach(',
  '["reponses","validees","marquees","courante","mode","sousListe","tempsMs","sansMinuteur","identite","piege","erreursPiege"].forEach(',
  "remplace")
m('mode==="piege"', '  else if(mode==="marquees"){', '''  else if(mode==="piege"){ const f=etat.piege, idx=questionsDuPiege(f);
    if(!f||!idx.length) return setMode("complet");
    const juste=i=>etat.validees[i]&&etat.reponses[i]===QUESTIONS[i].r;
    etat.sousListe=idx.filter(i=>!juste(i)).concat(idx.filter(juste));
    signale("🎯 Révision du piège « "+PIEGES[f]+" » : "+idx.length+" questions, celles que tu n'as pas encore réussies d'abord."); }
''', "avant")
m("erreursPiege[f]", '  etat.validees[i]=true; choixTemp=null;\n  if(!etat.timerOn', '''  if(etat.reponses[i]!==null && etat.reponses[i]!==QUESTIONS[i].r){ const f=piege(i);
    if(f){ etat.erreursPiege=etat.erreursPiege||{}; etat.erreursPiege[f]=(etat.erreursPiege[f]||0)+1; } }
''', "avant")
m("[data-piege]", '$("selComp").addEventListener("change",()=>setMode("cible"));', '''
/* « Réviser ce piège » — sous un indice, ou dans le bilan */
document.addEventListener("click",e=>{ const b=e.target.closest("[data-piege]"); if(!b) return;
  etat.piege=b.dataset.piege; montrerEcran("q"); setMode("piege");
  const z=document.getElementById("ecranQuestion"); if(z) z.scrollIntoView({behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"}); });''',
  "apres")
m("💡💡 Un indice de plus", '''  bloc.className="correction-bloc show "+(ok?"c-ok":"c-err");
  bloc.innerHTML=`''', '''  /* Aides progressives (audit du 17/11/2026) : une réponse fausse montre pourquoi ELLE ne va pas, sans la bonne ;
     puis, sur demande, la règle à appliquer ; la correction complète reste à un clic. (Chaînes concaténées, sans
     gabarit imbriqué : les contrôles du dépôt lisent ce script avec un analyseur simple.) */
  if(choix!==null && !ok && !corrVue[i]){
    const f=piege(i), nbF=f?questionsDuPiege(f).length:0, deja=f&&etat.erreursPiege?(etat.erreursPiege[f]||0):0;
    const l2=indice2[i]?'<p><b>💡💡 La règle à appliquer&nbsp;:</b> '+Q.ret+'</p>':"";
    const b2=indice2[i]?"":'<button class="btn small ghost" id="btnIndice2">💡💡 Un indice de plus</button>';
    const lp=f?'<p class="piege-ligne">🎯 C\\'est le piège «&nbsp;'+PIEGES[f]+'&nbsp;»'+(deja>1?' — tu t\\'y es déjà trompé·e '+deja+' fois':'')+'.'
      +'<br><button class="btn small" data-piege="'+f+'">Réviser ce piège&nbsp;: '+nbF+' questions</button></p>':"";
    bloc.className="correction-bloc show c-err";
    bloc.innerHTML='<h3>'+verdict+'</h3><div class="indice-zone">'
      +'<p><b>💡 Indice&nbsp;:</b> tu as choisi '+lettres[choix]+'. '+(Q.d[choix]||"Cette réponse ne convient pas.")+'</p>'+l2
      +'<div class="btns"><button class="btn small" id="btnRetenter">🔁 Réessayer avec '+(indice2[i]?"ces indices":"cet indice")+'</button>'+b2
      +'<button class="btn small ghost" id="btnVoirCorr">📖 Voir la correction complète</button></div>'+lp+'</div>';
    $("btnRetenter").addEventListener("click",()=>{
      etat.validees[i]=false; etat.reponses[i]=null; choixTemp=null; save(); rendreTout();
    });
    if($("btnIndice2")) $("btnIndice2").addEventListener("click",()=>{ indice2[i]=true; rendreCorrection(); });
    $("btnVoirCorr").addEventListener("click",()=>{ corrVue[i]=true; rendreQuestion(); });
    return;
  }
''', "avant")
m("pendant l’indice, la bonne réponse reste cachée", '      if(k===Q.r) b.classList.add("bonne");',
  '      if(k===Q.r && (etat.reponses[i]===Q.r || etat.reponses[i]===null || corrVue[i])) b.classList.add("bonne");   /* pendant l’indice, la bonne réponse reste cachée */',
  "remplace")
m("Tes pièges", '  $("rNotions").innerHTML=html||"<p>Réponds aux questions pour construire ton bilan de notions.</p>";', '''  /* les pièges où l'élève s'est trompé, et la révision qui les travaille (audit du 17/11/2026) */
  const rates={}; [...Array(N).keys()].forEach(i=>{ const f=piege(i); if(f&&etat.validees[i]&&etat.reponses[i]!==QUESTIONS[i].r) rates[f]=(rates[f]||0)+1; });
  const fs=Object.keys(rates).sort((a,b)=>rates[b]-rates[a]);
  if(fs.length) html+='<p><b>🎯 Tes pièges, du plus fréquent au moins fréquent&nbsp;:</b></p><ul class="pieges-bilan">'
    +fs.map(f=>'<li>«&nbsp;'+PIEGES[f]+'&nbsp;» — '+rates[f]+' erreur'+(rates[f]>1?"s":"")+' <button class="btn small" data-piege="'+f+'">Réviser ce piège&nbsp;: '+questionsDuPiege(f).length+' questions</button></li>').join("")+'</ul>';
''', "avant")


class Refus(Exception):
    pass


def carte(d: dict) -> str:
    a = d.get("avant_de_commencer") or {}
    for k in ("revoir", "savoir_faire", "reussir"):
        if not a.get(k):
            raise Refus("avant_de_commencer.%s manque (n°337 : trois rubriques, une idée par ligne)" % k)
    def li(titre, lignes):
        return "    <li><b>%s</b>\n    <br>%s</li>" % (titre, "\n    <br>".join(lignes))
    return ('<section class="card trois-lignes" id="trois-lignes">\n'
            '  <h2>🎯 Avant de commencer&nbsp;: trois choses à lire</h2>\n'
            '  <ul class="trois-lignes-liste">\n%s\n%s\n%s\n  </ul>\n</section>\n\n'
            % (li("📚 Ce que tu vas revoir", a["revoir"]), li("🛠 Ce que tu dois savoir faire", a["savoir_faire"]),
               li("✅ Comment réussir", a["reussir"])))


def bloc_pieges(d: dict, notions: list) -> str:
    p = d.get("pieges") or {}
    if not p:
        raise Refus("pieges manque (n°339 : au moins un piège)")
    vues = {}
    for cle, v in p.items():
        if not re.fullmatch(r"[a-z][a-z0-9_]*", cle):
            raise Refus("clé de piège invalide : %r (minuscules, chiffres, _)" % cle)
        for n in v.get("notions", []):
            if n not in notions:
                raise Refus("piège %s : la notion %r n'est celle d'aucune question" % (cle, n))
            if n in vues:
                raise Refus("la notion %r est dans deux pièges (%s, %s)" % (n, vues[n], cle))
            vues[n] = cle
        if len(v.get("notions", [])) < 3:
            raise Refus("piège %s : %d question(s) ; il en faut au moins trois pour réviser" % (cle, len(v.get("notions", []))))
    lignes = ["/* Les pièges : les confusions fréquentes de la séquence, et les questions qui les travaillent (règle d'or n°339).",
              "   Une question appartient à un piège par sa notion. Données : qcm_aides_<lot>.json — on modifie le JSON, pas ce bloc. */",
              "const PIEGES={"]
    lignes.append(",\n".join("  %s:%s" % (k, json.dumps(v["libelle"], ensure_ascii=False)) for k, v in p.items()))
    lignes.append("};")
    lignes.append("const PIEGE_DE_NOTION={")
    lignes.append(",\n".join("  %s:%s" % (json.dumps(n, ensure_ascii=False), json.dumps(k)) for n, k in vues.items()))
    lignes.append("};")
    lignes.append("function piege(i){ return PIEGE_DE_NOTION[QUESTIONS[i].n]||null; }")
    lignes.append("function questionsDuPiege(f){ return [...Array(N).keys()].filter(i=>piege(i)===f); }")
    return "\n".join(lignes) + "\n"


def notions_du_qcm(s: str) -> list:
    bloc = re.search(r"const QUESTIONS = \[(.*?)\n\];", s, re.S)
    if not bloc:
        raise Refus("bloc const QUESTIONS introuvable : ce n'est pas un QCM du gabarit maison")
    return [json.loads(x) for x in re.findall(r'\bn:("(?:[^"\\]|\\.)*")', bloc.group(1))]


def appliquer(s: str, d: dict) -> str:
    notions = notions_du_qcm(s)
    # données : la carte, les pièges, le message du bilan — réécrits à chaque passage
    c = carte(d)
    if CARTE_RE.search(s):
        s = CARTE_RE.sub(lambda _: c, s, count=1)
    else:
        if s.count(ANCRE_CARTE) != 1:
            raise Refus("ancre de la carte absente ou ambiguë : %r" % ANCRE_CARTE[:50])
        s = s.replace(ANCRE_CARTE, c + ANCRE_CARTE)
    pj = bloc_pieges(d, notions)
    if PIEGES_RE.search(s):
        s = PIEGES_RE.sub(lambda _: pj, s, count=1)
    else:
        if s.count("let etat={\n") != 1:
            raise Refus("ancre des pièges absente ou ambiguë : 'let etat={'")
        s = s.replace("let etat={\n", pj + "let etat={\n")
    if d.get("bilan_remarquable"):
        if not BILAN_RE.search(s):
            raise Refus("message du bilan introuvable (const msg= note>=16?\"…\")")
        s = BILAN_RE.sub(lambda mm: mm.group(1) + d["bilan_remarquable"].replace('"', '\\"') + mm.group(3), s, count=1)
    # moteur
    for marque, ancre, texte, position in MOTEUR:
        if marque in s:
            continue
        if s.count(ancre) != 1:
            raise Refus("point d'ancrage du moteur absent ou ambigu (%d) : %r" % (s.count(ancre), ancre[:70]))
        s = s.replace(ancre, {"avant": texte + ancre, "apres": ancre + texte, "remplace": texte}[position])
    return s


def poser_si_donnees(s: str, sortie: str) -> str:
    """Pour un générateur de QCM (`_generation/build_qcm.py`), juste avant d'écrire sa page : si le dossier du lot porte
    un `qcm_aides_*.json` dont « qcm » est le nom de cette page, pose les aides et les pièges ; sinon rend `s` tel quel.
    Sans cet appel, une régénération effacerait les aides (n°339)."""
    dossier, nom = os.path.dirname(os.path.abspath(sortie)), os.path.basename(sortie)
    for f in sorted(os.listdir(dossier)):
        if f.startswith("qcm_aides_") and f.endswith(".json"):
            d = json.load(open(os.path.join(dossier, f), encoding="utf-8"))
            if d.get("qcm") == nom:
                return appliquer(s, d)
    return s


def etat(racine: str, strict: bool) -> int:
    lus = 0
    manques = []
    for d, _, fs in os.walk(racine):
        if "_archive" in d or "/." in d.replace(os.sep, "/") or "node_modules" in d or "_exports" in d:
            continue
        for f in fs:
            if not (f.startswith("qcm") and f.endswith(".html")):
                continue
            p = os.path.join(d, f)
            s = open(p, encoding="utf-8").read()
            if "const QUESTIONS" not in s:
                continue
            lus += 1
            ok_carte = 'id="trois-lignes"' in s
            ok_aides = all(mq in s for mq, *_ in MOTEUR)
            ok_pieges = "const PIEGE_DE_NOTION" in s
            if not (ok_carte and ok_aides and ok_pieges):
                manques.append((os.path.relpath(p, racine), ok_carte, ok_aides, ok_pieges))
    if not lus:
        print("✘ aucun QCM du gabarit maison lu : rien n'a été vérifié")
        return 2
    for rel, a, b, c in manques:
        print("  %s %s — %s" % ("✘" if strict else "⚠", rel,
                                 ", ".join(x for x, v in (("avant de commencer", a), ("aides progressives", b), ("pièges", c)) if not v)))
    print("%d QCM lus · %d avec les trois (avant de commencer, aides progressives, pièges) · %d à poser"
          % (lus, lus - len(manques), len(manques)))
    return 1 if (strict and manques) else 0


def main(argv) -> int:
    if "--etat" in argv:
        autres = [a for a in argv if not a.startswith("--")]
        return etat(autres[0] if autres else DEPOT, "--strict" in argv)
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 2:
        print(__doc__)
        return 2
    page, donnees = args
    try:
        s = open(page, encoding="utf-8").read()
        d = json.load(open(donnees, encoding="utf-8"))
        u = appliquer(s, d)
    except (Refus, OSError, json.JSONDecodeError) as e:
        print("✘ %s" % e)
        return 2
    if "--verifier" in argv:
        print(("✅ à jour : " if u == s else "✘ à reposer : ") + page)
        return 0 if u == s else 1
    if u != s:
        open(page, "w", encoding="utf-8").write(u)
        print("✍ posé : %s" % page)
    else:
        print("✅ déjà à jour : %s" % page)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
