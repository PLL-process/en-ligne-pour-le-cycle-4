# -*- coding: utf-8 -*-
"""Ce que l'audit « double regard » du 17/11/2026 a ajouté au QCM de 5e_C2.1, rejouable sur le gabarit.

`build_qcm.py` applique ces apports après ses remplacements ; on peut aussi les appliquer seuls à la page déjà
construite : `python3 apports_audit.py <qcm.html>`. Chaque apport refuse de s'appliquer si son point d'ancrage
manque, et ne s'applique pas deux fois (il cherche d'abord sa marque).

1. « Avant de commencer » — trois lignes en langue élève, avant « Ma progression » (Pascal, 17/11/2026 : « avant de
   commencer, et dans toutes les séquences, l'élève devrait lire trois informations très simples : ce qu'il va
   apprendre, ce qu'il doit savoir faire et comment réussir »).
2. Des aides progressives (audit, point 3 : « un premier indice, puis une explication plus détaillée, sans voir
   immédiatement la bonne réponse ») — après une réponse fausse :
     💡 indice 1 : pourquoi CETTE réponse ne va pas (le « pourquoi » de la proposition choisie, `d[k]`) ;
     💡💡 indice 2, sur demande : la règle à appliquer (le « À retenir » de la question, `ret`) ;
     📖 la correction complète, sur demande — elle reste entière, à un clic (le bouton de correction).
   La bonne réponse n'est pas marquée en vert tant que la correction n'est pas ouverte. Juste, ou non répondue : la
   correction complète s'ouvre, comme avant.
3. Une révision fondée sur les difficultés (audit, point 4 : « si l'élève confond régulièrement un interacteur et
   une exigence, le système devrait lui proposer plusieurs questions supplémentaires sur cette distinction ») —
   chaque question appartient à un PIÈGE (une confusion fréquente, `PIEGE_DE_NOTION`, par sa notion). Une erreur
   propose « Réviser ce piège : N questions » (le mode `piege` ne garde que ses questions, les ratées d'abord) ; le
   bilan liste les pièges où l'élève s'est trompé, avec le nombre d'erreurs et le même bouton.
4. Le message du bilan parlait de « chaînes d'énergie et d'information, matériaux et réseau » (un reste du gabarit) :
   il parle des interacteurs et des choix de conception.
"""
import sys

OPS = []   # (marque, ancre, texte, position) — position : "avant", "apres" ou "remplace"


def op(marque, ancre, texte, position):
    OPS.append((marque, ancre, texte, position))


# ── 1. Avant de commencer ──
op('id="trois-lignes"', '<section class="card">\n  <h2>📊 Ma progression</h2>', '''<section class="card trois-lignes" id="trois-lignes">
  <h2>🎯 Avant de commencer&nbsp;: trois choses à lire</h2>
  <ul class="trois-lignes-liste">
    <li><b>📚 Ce que tu vas revoir</b>
    <br>Les interacteurs d'un objet&nbsp;: tout ce qui l'entoure et agit sur lui.
    <br>Et les choix de sa forme&nbsp;: ergonomie, sécurité, développement durable.</li>
    <li><b>🛠 Ce que tu dois savoir faire</b>
    <br>Reconnaître un interacteur, et le ranger dans sa famille.
    <br>Dire à quoi sert un détail de la station, et pour qui.</li>
    <li><b>✅ Comment réussir</b>
    <br>Lis la question jusqu'au bout, puis écarte d'abord les réponses fausses.
    <br>Si tu te trompes, lis l'indice et réessaie avant d'ouvrir la correction.
    <br>Commence par «&nbsp;10 questions&nbsp;» ; finis par «&nbsp;Uniquement mes erreurs&nbsp;».</li>
  </ul>
</section>

''', "avant")
op(".trois-lignes-liste{", '  .correction-bloc{margin-top:16px;border-radius:12px;padding:14px 16px;display:none}\n', '''  .trois-lignes-liste{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:10px}
  .trois-lignes-liste li{border-left:3px solid #61dafb;padding:2px 0 2px 12px;line-height:1.55}
  .indice-zone{margin:8px 0 10px;padding:10px 12px;border-radius:10px;background:rgba(255,213,79,.08);border:1px solid #6b5a2f}
  .indice-zone p{margin:6px 0}
  .indice-zone .btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
  .piege-ligne{margin-top:10px;padding-top:8px;border-top:1px dashed #6b5a2f}
  .pieges-bilan li{margin:6px 0}
''', "avant")

# ── 3. Les pièges : données, état, mode ──
op("const PIEGES=", "let etat={\n", '''/* Les pièges : les confusions fréquentes de la séquence, et les questions qui les travaillent (audit du 17/11/2026,
   « une révision fondée sur les difficultés »). Une question appartient à un piège par sa notion. */
const PIEGES={
  besoin:"La bête à cornes : à qui, sur quoi, dans quel but ?",
  dedans:"Interacteur ou pas ? Une règle (une exigence), une pièce de l'objet, sa couleur",
  familles:"Les quatre familles d'interacteurs, sans oublier l'invisible",
  lieu:"Changer de lieu, c'est changer d'interacteurs",
  domaines:"Quel domaine : ergonomie, sécurité ou développement durable ?",
  expliquer:"Expliquer un choix (pas le décrire), et ce qu'il coûte"
};
const PIEGE_DE_NOTION={
  "Les trois questions de la bête à cornes":"besoin","À qui ou sur quoi":"besoin",
  "Fonction d'usage ou fonction technique":"besoin","Les mots de référence":"besoin",
  "Définition":"dedans","Ce qui n'en est pas un":"dedans","Un interacteur non vivant":"dedans",
  "Un interacteur invisible":"dedans","Ce qui contraint":"dedans","Extérieur ou intérieur":"dedans",
  "Les quatre familles":"familles","La famille invisible":"familles","Le réflexe coûteux":"familles",
  "Ce qui alimente":"familles","Le geste de recensement":"familles","À quoi ça sert":"familles",
  "Changer de lieu":"lieu","Un interacteur martiniquais":"lieu","Le sel marin":"lieu","Transposer":"lieu",
  "Trois domaines":"domaines","L'ergonomie":"domaines","La sécurité":"domaines",
  "Un choix pour la maintenance":"domaines","Deux domaines à la fois":"domaines",
  "Le développement durable comme domaine":"domaines",
  "Lire un objet":"expliquer","La question qui ouvre":"expliquer","Retrouver l'interacteur":"expliquer",
  "Le coût d'un choix":"expliquer","Deux réponses au même problème":"expliquer","Un gain payé ailleurs":"expliquer",
  "Justifier, pas décrire":"expliquer"
};
function piege(i){ return PIEGE_DE_NOTION[QUESTIONS[i].n]||null; }
function questionsDuPiege(f){ return [...Array(N).keys()].filter(i=>piege(i)===f); }
''', "avant")
op("indice2={}", 'let timerInterval=null, choixTemp=null;',
   'let timerInterval=null, choixTemp=null;\n'
   'const corrVue={}, indice2={};   /* la correction complète, l\'indice n°2 ouverts (non sauvegardés : l\'indice revient) */',
   "remplace")
op('"piege","erreursPiege"', '["reponses","validees","marquees","courante","mode","sousListe","tempsMs","sansMinuteur","identite"].forEach(',
   '["reponses","validees","marquees","courante","mode","sousListe","tempsMs","sansMinuteur","identite","piege","erreursPiege"].forEach(',
   "remplace")
op('mode==="piege"', '  else if(mode==="marquees"){', '''  else if(mode==="piege"){ const f=etat.piege, idx=questionsDuPiege(f);
    if(!f||!idx.length) return setMode("complet");
    const juste=i=>etat.validees[i]&&etat.reponses[i]===QUESTIONS[i].r;
    etat.sousListe=idx.filter(i=>!juste(i)).concat(idx.filter(juste));
    signale("🎯 Révision du piège « "+PIEGES[f]+" » : "+idx.length+" questions, celles que tu n'as pas encore réussies d'abord."); }
''', "avant")
op("erreursPiege[f]", '  etat.validees[i]=true; choixTemp=null;\n  if(!etat.timerOn', '''  if(etat.reponses[i]!==null && etat.reponses[i]!==QUESTIONS[i].r){ const f=piege(i);
    if(f){ etat.erreursPiege=etat.erreursPiege||{}; etat.erreursPiege[f]=(etat.erreursPiege[f]||0)+1; } }
''', "avant")
op("[data-piege]", '$("selComp").addEventListener("change",()=>setMode("cible"));', '''
/* « Réviser ce piège » — sous un indice, ou dans le bilan */
document.addEventListener("click",e=>{ const b=e.target.closest("[data-piege]"); if(!b) return;
  etat.piege=b.dataset.piege; montrerEcran("q"); setMode("piege");
  const z=document.getElementById("ecranQuestion"); if(z) z.scrollIntoView({behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"}); });''',
   "apres")

# ── 2. Les aides progressives ──
op("💡💡 Un indice de plus", '''  bloc.className="correction-bloc show "+(ok?"c-ok":"c-err");
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
op("pendant l’indice, la bonne réponse reste cachée", '      if(k===Q.r) b.classList.add("bonne");',
   '      if(k===Q.r && (etat.reponses[i]===Q.r || etat.reponses[i]===null || corrVue[i])) b.classList.add("bonne");   /* pendant l’indice, la bonne réponse reste cachée */',
   "remplace")

# ── 3 (suite). Le bilan dit les pièges ──
op("Tes pièges", '  $("rNotions").innerHTML=html||"<p>Réponds aux questions pour construire ton bilan de notions.</p>";', '''  /* les pièges où l'élève s'est trompé, et la révision qui les travaille (audit du 17/11/2026) */
  const rates={}; [...Array(N).keys()].forEach(i=>{ const f=piege(i); if(f&&etat.validees[i]&&etat.reponses[i]!==QUESTIONS[i].r) rates[f]=(rates[f]||0)+1; });
  const fs=Object.keys(rates).sort((a,b)=>rates[b]-rates[a]);
  if(fs.length) html+='<p><b>🎯 Tes pièges, du plus fréquent au moins fréquent&nbsp;:</b></p><ul class="pieges-bilan">'
    +fs.map(f=>'<li>«&nbsp;'+PIEGES[f]+'&nbsp;» — '+rates[f]+' erreur'+(rates[f]>1?"s":"")+' <button class="btn small" data-piege="'+f+'">Réviser ce piège&nbsp;: '+questionsDuPiege(f).length+' questions</button></li>').join("")+'</ul>';
''', "avant")

# ── 4. Le message du bilan ──
op("Les interacteurs et les choix de conception n’ont plus de secret",
   "Remarquable ! Fonctions, chaînes d’énergie et d’information, matériaux et réseau n’ont plus de secret pour toi",
   "Remarquable ! Les interacteurs et les choix de conception n’ont plus de secret pour toi",
   "remplace")


def appliquer(s: str) -> str:
    for marque, ancre, texte, position in OPS:
        if marque in s:
            continue
        if s.count(ancre) != 1:
            raise SystemExit("apports_audit : point d'ancrage absent ou ambigu (%d) : %r" % (s.count(ancre), ancre[:70]))
        s = s.replace(ancre, {"avant": texte + ancre, "apres": ancre + texte, "remplace": texte}[position])
    return s


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    f = sys.argv[1]
    t = open(f, encoding="utf-8").read()
    u = appliquer(t)
    if u != t:
        open(f, "w", encoding="utf-8").write(u)
        print("apports de l'audit appliqués :", f)
    else:
        print("déjà appliqués :", f)
