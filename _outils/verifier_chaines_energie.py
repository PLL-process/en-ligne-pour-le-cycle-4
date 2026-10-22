"""Vérifie les six figures et la scène 6 du vélo dans Chromium.

Usage : python _outils/verifier_chaines_energie.py [dossier de captures]
Requiert Playwright/Chromium, comme les suites pédagogiques du dépôt.
"""
from pathlib import Path
import hashlib,json,subprocess,sys,re
import xml.etree.ElementTree as ET
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from urllib.parse import quote
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
LOT=ROOT/'theme-1-objets-systemes-usages-interactions/C3-caracteriser-et-choisir-un-objet-ou-un/5e/5e_C3.1'
INFO_ET_ENERGIE={'chaines_energie_information_lampadaire.svg','chaines_jardin_connecte.svg','chaine_info_energie_station.svg','chaine_energie_book-train.svg'}
NAMES=['chaines_energie_information_lampadaire.svg','chaines_jardin_connecte.svg','chaine_energie_a_elaborer.svg','chaine_info_energie_station.svg','chaine_energie_book-train.svg','chaine_energie_velo_cargo.svg']
FILES=[next(ROOT.glob('theme-*/**/Images/'+n)) for n in NAMES]
OUT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else None
if OUT:OUT.mkdir(parents=True,exist_ok=True)
results=[]
server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(ROOT)))
Thread(target=server.serve_forever,daemon=True).start()
base='http://127.0.0.1:'+str(server.server_address[1])+'/'
def check(label,ok,detail=''):
    results.append(bool(ok));print(('OK ' if ok else 'ECHEC ')+label+(' : '+str(detail) if detail else ''))
def digest(p):return hashlib.sha256(p.read_bytes().replace(b'\r\n',b'\n')).hexdigest()   # fins de ligne ignorées : sous Windows le dépôt sort en CRLF, les générateurs écrivent en LF

with sync_playwright() as p:
    b=p.chromium.launch()
    for f in FILES:
        pg=b.new_page(viewport={'width':1600,'height':1200})
        pg.goto(f.as_uri())
        r=pg.evaluate('''() => {
          const s=document.querySelector('svg'),v=s.viewBox.baseVal;
          const ts=[...s.querySelectorAll('text')].map(e=>({s:e.textContent,b:e.getBBox()}));
          const pairs=[];
          for(let i=0;i<ts.length;i++)for(let j=i+1;j<ts.length;j++){
            const a=ts[i].b,b=ts[j].b;
            if(Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x)>2 && Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y)>2)pairs.push([ts[i].s,ts[j].s]);
          }
          const blocks=[...s.querySelectorAll('[data-role="function"] rect,.vpp-chaine rect')].map(e=>e.getBBox());
          const energy=[...s.querySelectorAll('[data-role="flow"],[data-role="stock"],.vpp-energy,.vpp-stock')];
          const inside=energy.filter(e=>{const t=e.getBBox();return blocks.some(r=>t.x<r.x+r.width && t.x+t.width>r.x && t.y<r.y+r.height && t.y+t.height>r.y)}).map(e=>e.textContent);
          return {outside:ts.filter(t=>t.b.x < -1 || t.b.x+t.b.width>v.width+1 || t.b.y<0 || t.b.y+t.b.height>v.height+1).map(t=>t.s),pairs,inside,
            accessible:!!s.querySelector('title')&&!!s.querySelector('desc'),remote:[...s.querySelectorAll('[href],[src]')].some(e=>/^https?:/.test(e.getAttribute('href')||e.getAttribute('src')))};
        }''')
        check(f.name+' : textes dans le cadre, sans chevauchement',not r['outside'] and not r['pairs'],r['outside']+r['pairs'])
        check(f.name+' : énergies hors des blocs, alternative présente, autonome',not r['inside'] and r['accessible'] and not r['remote'],r['inside'])
        if f.name in INFO_ET_ENERGIE:
            # Convention conservée (règle d'or du schéma) : la chaîne d'information est AU-DESSUS de la chaîne d'énergie, l'ordre descend.
            src=f.read_text(encoding='utf-8')
            y_info=[float(y) for y in re.findall(r'<text x="[^"]*" y="([^"]*)"[^>]*>CHAÎNE D’INFORMATION',src)]
            y_ener=[float(y) for y in re.findall(r'<text x="[^"]*" y="([^"]*)"[^>]*>CHAÎNE D’ÉNERGIE',src)]
            check(f.name+' : convention « information en haut, énergie en bas, l’ordre descend » — dite et dessinée',
                  bool(y_info) and bool(y_ener) and y_info[0]<y_ener[0] and all(k in src.lower() for k in ('en haut','en bas','descend')),(y_info,y_ener))
        if OUT:pg.locator('svg').screenshot(path=str(OUT/(f.stem+'.png')))
        if f.name!='chaine_energie_velo_cargo.svg':
            pg.emulate_media(media='print')
            check(f.name+' : fond blanc à l’impression',pg.locator('.paper').evaluate("e=>getComputedStyle(e).fill")=='rgb(255, 255, 255)')
        pg.close()
    pg=b.new_page(viewport={'width':1280,'height':1000})
    errors=[];pg.on('pageerror',lambda e:errors.append(str(e)))
    pg.add_init_script("const original=HTMLMediaElement.prototype.play;HTMLMediaElement.prototype.play=function(){window.__lastAudio=this;return original.apply(this,arguments)};")
    pg.goto((LOT/'sequence_5e_C3.1-C3.4_shanghai.html').as_uri()+'#velo-cargo-pas-a-pas')
    pg.wait_for_selector('#vppPanneau:not([hidden])')
    pg.wait_for_function("getComputedStyle(document.querySelector('.vpp-dessin .vpp-chaine')).opacity==='0'")
    check('Scène 1 : bandeau final masqué',pg.locator('.vpp-dessin .vpp-chaine').evaluate("e=>getComputedStyle(e).opacity")=='0')
    for _ in range(5):pg.click('#vppSuiv')
    pg.wait_for_function("document.getElementById('velo-cargo-pas-a-pas').getAttribute('data-scene')==='6'")
    pg.wait_for_function("getComputedStyle(document.querySelector('.vpp-dessin .vpp-chaine')).opacity==='1'")
    narration=json.loads((LOT/'_generation/voix_velo_cargo/phrases.json').read_text(encoding='utf-8'))['phrases'][5]['dit']
    check('Scène 6 : narration affichée identique au texte de synthèse',narration in pg.locator('#vppPanneau').inner_text())
    check('Scène 6 : contrôleur présent dans le dessin',pg.locator('.vpp-dessin .pv-controller').count()==1)
    pg.click('#vppEcouter')
    pg.wait_for_function("window.__lastAudio && window.__lastAudio.currentTime>0.1 && window.__lastAudio.currentSrc.includes('velo-cargo_scene6.')",timeout=10000)
    media=pg.evaluate("[{src:window.__lastAudio.currentSrc,duration:window.__lastAudio.duration,error:!!window.__lastAudio.error}]")
    check('Scène 6 : le nouvel audio se charge et se lit',bool(media) and media[0]['duration']>5 and not media[0]['error'],media)
    pg.evaluate('window.__lastAudio.pause()')
    if OUT:
        pg.wait_for_timeout(2200)
        pg.locator('#vppPanneau').screenshot(path=str(OUT/'scene6-dans-sequence.png'))
    check('Scène 6 : aucune erreur JavaScript',not errors,errors)
    book=FILES[4].parent.parent
    html=(book/'sequence_4e_C4.1-C4.2-C4.4_book-train.html').read_text(encoding='utf-8')
    embedded=json.loads(re.search(r'var FICHIERS = (\{[^\n]*\});',html).group(1))
    for name in ['chaine_energie_book-train.drawio','chaine_energie_a_completer.drawio']:
        check('Book Train : téléchargement incorporé synchronisé ('+name+')',embedded[name]==(book/'fichiers_drawio'/name).read_text(encoding='utf-8'))
    values=[c.get('value','') for c in ET.fromstring(embedded['chaine_energie_a_completer.drawio']).iter('mxCell')]
    check('Book Train : copie élève conserve fonctions et énergies à compléter',values.count('Fonction : ……………')==4 and values.count('Énergie : ……………')==5 and not any(v in {'ALIMENTER','DISTRIBUER','CONVERTIR','TRANSMETTRE'} for v in values))
    pg.goto((book/'sequence_4e_C4.1-C4.2-C4.4_book-train.html').as_uri())
    check('Book Train : figure 4 incorporée corrigée',pg.locator('svg[aria-labelledby="fig4t fig4d"]').count()==1 and 'Commande de puissance' in pg.locator('svg[aria-labelledby="fig4t fig4d"]').text_content())
    # Vérifier les SVG dans leur vrai objet d'intégration, pas seulement seuls.
    c4=ROOT/'theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation'
    for f,page in [(FILES[0],c4/'5e/5e_C4.1/sequence_5e_C4.1-C4.8_lampadaire_intelligent.html'),(FILES[1],c4/'4e/4e_C4.1/sequence_4e_C4.1-C4.9_jardin_connecte.html'),(FILES[2],c4/'3e/3e_C4.1/sequence_3e_C4.1-C4.2_energie_station.html')]:
        pg.goto(base+quote(page.relative_to(ROOT).as_posix()))
        obj=pg.locator('object[data="Images/'+f.name+'"]')
        panel=obj.evaluate("e=>e.closest('.seance-panel')?.id")
        if panel:pg.locator('.seance-tab[data-panel="'+panel+'"]').click()
        pg.wait_for_function("name=>{let e=document.querySelector('object[data=\"Images/'+name+'\"]');return e&&e.contentDocument&&e.contentDocument.querySelector('svg')}",arg=f.name,timeout=10000)
        r=obj.evaluate("e=>({largeur:e.getBoundingClientRect().width,svg:e.contentDocument.querySelector('svg').getBoundingClientRect().width})")
        check(f.name+' : tient dans son objet HTML',r['svg']<=r['largeur']+1,r)
    b.close()
server.shutdown()
server.server_close()

for n in range(1,6):
    for ext in ['mp3','ogg']:
        f=LOT/'Audio'/f'velo-cargo_scene{n}.{ext}'
        original=subprocess.check_output(['git','show','HEAD:'+f.relative_to(ROOT).as_posix()],cwd=ROOT)
        check(f.name+' : prise validée conservée',f.read_bytes()==original)

check('Les phrases de la page et de synthèse sont synchronisées',subprocess.run([sys.executable,str(LOT/'_generation/voix_velo_cargo/generer.py'),'--verifier'],cwd=ROOT).returncode==0)
# Les deux générations doivent conserver les SVG et la page à l’octet près.
watched=FILES+[LOT/'sequence_5e_C3.1-C3.4_shanghai.html']
before={str(f):digest(f) for f in watched}
subprocess.run([sys.executable,str(ROOT/'_outils/regenerer_chaines_energie.py')],cwd=ROOT,check=True)
subprocess.run(['node',str(LOT/'_generation/figure_iso_velo_cargo/build.mjs')],cwd=ROOT,check=True)
check('Les générateurs reproduisent les corrections sans les écraser',all(digest(Path(f))==h for f,h in before.items()))
print(f'\n{sum(results)} / {len(results)} vérifications réussies')
sys.exit(0 if all(results) else 1)
