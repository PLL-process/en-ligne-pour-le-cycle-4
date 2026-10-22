"""Régénère les cinq schémas fonctionnels SVG et leurs sources draw.io.

Fonctions dans les blocs, composants en dessous, énergies sur les flèches.
La batterie porte une annotation de stock, distincte des flux électriques.
Aucune bibliothèque, police ou ressource distante n'est nécessaire.
"""
from pathlib import Path
from html import escape
import xml.etree.ElementTree as ET
import json
import re

ROOT = Path(__file__).resolve().parents[1]
C4 = Path('theme-2-structure-fonctionnement-comportement/C4-decrire-et-caracteriser-lorganisation')
C9 = Path('theme-3-creation-conception-realisation-innovations/C9-concevoir-ecrire-tester-et-mettre-au-point/3e/3e_C9.2')
BG, BOX, WHITE = '#050f24', '#0d2347', '#e4eaf5'
CYAN, YELLOW, VIOLET, GREEN, ORANGE, BLUE = '#61dafb', '#ffd66b', '#c68ef2', '#81fba1', '#ffb454', '#81aaff'


class Diagram:
    def __init__(self, title, desc, h=900, w=1600):
        self.w, self.h, self.title, self.desc = w, h, title, desc
        self.parts = []
        self.model = ET.Element('mxGraphModel', page='1', pageWidth=str(w), pageHeight=str(h), background=BG, adaptiveColors='auto')
        self.root = ET.SubElement(self.model, 'root')
        ET.SubElement(self.root, 'mxCell', id='0')
        ET.SubElement(self.root, 'mxCell', id='1', parent='0')
        self.n = 1
        self.text(w / 2, 44, title, BLUE, 30, True)

    def cell(self, value, style, x, y, w, h):
        self.n += 1
        c = ET.SubElement(self.root, 'mxCell', id=str(self.n), value=value, style=style, vertex='1', parent='1')
        ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h), **{'as': 'geometry'})

    def text(self, x, y, text, color=WHITE, size=20, bold=False, anchor='middle', role=None):
        # Chaque ligne est un vrai texte SVG : lisible et imprimable sans foreignObject.
        lines = text.split('\n')
        width = max(len(s) for s in lines) * size * .58 + 12
        left = x - width / 2 if anchor == 'middle' else x
        for i, line in enumerate(lines):
            ry = y + i * (size + 7)
            attrs = f' data-role="{role}"' if role else ''
            self.parts.append(f'<text x="{x}" y="{ry}" fill="{color}" font-size="{size}" font-weight="{700 if bold else 400}" text-anchor="{anchor}"{attrs}>{escape(line)}</text>')
        self.cell(text, f'text;html=0;whiteSpace=wrap;align={"center" if anchor == "middle" else "left"};verticalAlign=middle;fontFamily=Arial;fontColor={color};fontSize={size};fontStyle={1 if bold else 0};', left, y-size, width, len(lines)*(size+7))

    def block(self, x, y, function, component, color=ORANGE, w=210, stock=False, ident=None):
        h = 76
        self.parts.append(f'<g data-role="function"{f" id={chr(34)}{ident}{chr(34)}" if ident else ""}><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{BOX}" stroke="{color}" stroke-width="3"/>')
        lines = function.split('\n')
        self.text(x+w/2, y+(46 if len(lines)==1 else 31), function, color, 23, True)
        self.parts.append('</g>')
        self.cell(function, f'rounded=1;arcSize=16;html=0;whiteSpace=wrap;fillColor={BOX};strokeColor={color};strokeWidth=3;fontColor={color};fontSize=23;fontStyle=1;fontFamily=Arial;', x,y,w,h)
        self.text(x+w/2, y+111, component, WHITE, 21, role='component')
        if stock:
            self.text(x+w/2, y+111+len(component.split('\n'))*28, 'Énergie chimique\nstockée', YELLOW, 19, role='stock')

    def arrow(self, points, color=ORANGE, label=None, lx=None, ly=None, dashed=False, both=False):
        d='M '+' L '.join(f'{x} {y}' for x,y in points)
        dash=' stroke-dasharray="8 6"' if dashed else ''
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3" stroke-linejoin="round" marker-end="url(#a{color[1:]})"{f" marker-start={chr(34)}url(#a{color[1:]}){chr(34)}" if both else ""}{dash}/>')
        self.n+=1
        c=ET.SubElement(self.root,'mxCell',id=str(self.n),style=f'edgeStyle=none;html=0;strokeColor={color};strokeWidth=3;endArrow=block;endFill=1;startArrow={"block" if both else "none"};dashed={1 if dashed else 0};',edge='1',parent='1')
        g=ET.SubElement(c,'mxGeometry',relative='1',**{'as':'geometry'})
        ET.SubElement(g,'mxPoint',x=str(points[0][0]),y=str(points[0][1]),**{'as':'sourcePoint'})
        ET.SubElement(g,'mxPoint',x=str(points[-1][0]),y=str(points[-1][1]),**{'as':'targetPoint'})
        a=ET.SubElement(g,'Array',**{'as':'points'})
        for x,y in points[1:-1]: ET.SubElement(a,'mxPoint',x=str(x),y=str(y))
        if label:
            self.text(lx if lx is not None else (points[0][0]+points[-1][0])/2, ly if ly is not None else points[0][1]-30, label, color, 18, role='flow')

    def section(self,y,label,color):
        self.text(35,y,label,color,23,True,anchor='start')

    def save(self,path):
        dest=ROOT/path
        # Les cellules texte de fonction sont redondantes avec leur rectangle draw.io :
        # seul le SVG conserve les deux primitives nécessaires au rendu natif.
        for c in list(self.root):
            if c.get('style','').startswith('text;') and c.get('value') in {'ACQUÉRIR','TRAITER','COMMUNIQUER','CONVERTIR','RÉGULER','DISTRIBUER','STOCKER /\nALIMENTER','ADAPTER','TRANSMETTRE','ALIMENTER'}:
                self.root.remove(c)
        mxfile=ET.Element('mxfile',host='app.diagrams.net',type='device')
        dg=ET.SubElement(mxfile,'diagram',id='chaine',name=self.title)
        dg.append(self.model)
        native=ET.tostring(mxfile,encoding='unicode')
        source=dest.parent.parent/('_generation/chaines_energie/'+dest.stem+'.drawio')
        if 'book-train' in dest.name:
            source=dest.parent.parent/'fichiers_drawio/chaine_energie_book-train.drawio'
        source.parent.mkdir(parents=True,exist_ok=True)
        source.write_text(native+'\n',encoding='utf-8')
        markers=''.join(f'<marker id="a{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="12" markerHeight="12" orient="auto-start-reverse" markerUnits="userSpaceOnUse"><path d="M0 0L10 5L0 10Z" fill="{c}"/></marker>' for c in (CYAN,YELLOW,VIOLET,GREEN,ORANGE,BLUE))
        css='@media print{.paper{fill:white}rect[fill="'+BOX+'"]{fill:white}text[fill="'+WHITE+'"]{fill:#172a49}}'
        for c,dark in [(CYAN,'#006a86'),(YELLOW,'#805600'),(VIOLET,'#7836ad'),(GREEN,'#126c2a'),(ORANGE,'#925000'),(BLUE,'#244e9a')]:
            css+='@media print{[fill="%s"]{fill:%s}[stroke="%s"]{stroke:%s}}' % (c,dark,c,dark)
        svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" style="width:100%;height:auto" viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="t d" font-family="Segoe UI, Arial, sans-serif" content="{escape(native,quote=True)}">\n<title id="t">{escape(self.title)}</title><desc id="d">{escape(self.desc)}</desc>\n<defs>{markers}</defs><style>{css}</style><rect class="paper" width="{self.w}" height="{self.h}" fill="{BG}"/>\n'+ '\n'.join(self.parts)+'\n</svg>\n'
        dest.write_text(svg,encoding='utf-8')
        print(path)


def lampadaire():
    d=Diagram('Lampadaire solaire : information et énergie',
        'Les capteurs de luminosité et de mouvement acquièrent les informations. La carte traite et communique un ordre à l’interrupteur électronique. Le panneau convertit l’énergie lumineuse en énergie électrique. Le régulateur de charge relie panneau, batterie et alimentation des LED. La batterie stocke de l’énergie chimique ; ses échanges avec le régulateur sont électriques, dans les deux sens. L’interrupteur distribue l’énergie électrique au bloc LED qui la convertit en lumière pour éclairer la zone.',890)
    d.section(95,"CHAÎNE D’INFORMATION",CYAN)
    d.block(160,125,'ACQUÉRIR','Capteur de luminosité\nDétecteur de mouvement',CYAN)
    d.block(590,125,'TRAITER','Carte électronique\nSi nuit et passage : allumer',VIOLET,w=250)
    d.block(1060,125,'COMMUNIQUER','Sortie de commande\nde la carte',GREEN,w=240)
    d.arrow([(370,163),(580,163)],CYAN,'Mesures',475,143)
    d.arrow([(840,163),(1050,163)],CYAN,'Décision',945,143)
    d.arrow([(1180,262),(1180,315),(945,315),(945,390)],GREEN,'Ordre d’allumage',1180,294,dashed=True)
    d.section(352,"CHAÎNE D’ÉNERGIE",ORANGE)
    for args in [(155,'CONVERTIR','Panneau solaire',ORANGE),(510,'RÉGULER','Régulateur de charge',YELLOW),(840,'DISTRIBUER','Interrupteur électronique\n(ou pilote de LED)',CYAN),(1195,'CONVERTIR','Bloc LED',VIOLET)]:
        d.block(args[0],410,*args[1:])
    d.arrow([(15,448),(145,448)],ORANGE,'Énergie\nlumineuse',76,385)
    for x1,x2 in [(365,500),(720,830),(1050,1185)]: d.arrow([(x1,448),(x2,448)],ORANGE,'Énergie\nélectrique',(x1+x2)/2,385)
    d.arrow([(1405,448),(1555,448)],ORANGE,'Énergie\nlumineuse',1480,385)
    d.text(1480,500,'Éclairer\nla zone',WHITE,22,True)
    d.block(510,650,'STOCKER /\nALIMENTER','Batterie',YELLOW,stock=True)
    d.arrow([(720,470),(780,470),(780,688),(720,688)],YELLOW,'Énergie électrique\nCharge / décharge',950,605,both=True)
    d.text(800,865,'Les fonctions sont dans les blocs ; les composants en dessous ; les formes d’énergie sur les flèches.',BLUE,18)
    d.save(C4/'5e/5e_C4.1/Images/chaines_energie_information_lampadaire.svg')


def jardin():
    d=Diagram('Jardin connecté : information, énergie et eau',
        'Les capteurs d’humidité transmettent les mesures à la carte qui décide et communique les données au réseau et à l’application. Les ordres pilotent les interfaces de puissance de la pompe et des électrovannes. Le panneau fournit de l’énergie électrique au régulateur de charge. La batterie, reliée au régulateur, stocke de l’énergie chimique. La pompe convertit l’énergie électrique en énergie hydraulique. Les actionneurs des électrovannes convertissent l’énergie électrique en mouvement d’ouverture ou de fermeture. Le circuit d’eau, séparé, va du réservoir à la pompe puis aux électrovannes et aux bacs. Une vanne commune arrose simultanément ; une vanne par bac permet une commande indépendante.',1120)
    d.section(95,"CHAÎNE D’INFORMATION",CYAN)
    d.block(100,120,'ACQUÉRIR','Capteurs d’humidité\nun par bac',CYAN)
    d.block(580,120,'TRAITER','Carte programmable\nCompare aux seuils',VIOLET,w=250)
    d.block(1160,120,'COMMUNIQUER','Module Wi-Fi et application\nMesures et courbes',GREEN,w=290)
    d.arrow([(310,158),(570,158)],CYAN,'Mesures',440,138)
    d.arrow([(830,158),(1150,158)],CYAN,'Données à afficher',990,138)
    d.arrow([(705,258),(705,304),(940,304),(940,380)],GREEN,'Ordres d’arrosage',1020,292,dashed=True)
    d.section(350,"CHAÎNE D’ÉNERGIE",ORANGE)
    d.block(150,400,'CONVERTIR','Panneau solaire',ORANGE)
    d.block(495,400,'RÉGULER','Régulateur de charge',YELLOW)
    d.block(835,400,'DISTRIBUER','Relais ou transistors\nCommande des actionneurs',CYAN)
    d.block(1190,400,'CONVERTIR','Électropompe',VIOLET)
    d.arrow([(12,438),(140,438)],ORANGE,'Énergie\nlumineuse',75,375)
    for a,b in [(360,485),(705,825),(1045,1180)]: d.arrow([(a,438),(b,438)],ORANGE,'Énergie\nélectrique',(a+b)/2,375)
    d.arrow([(1400,438),(1565,438)],ORANGE,'Énergie\nhydraulique',1480,375)
    d.text(1480,497,'Mettre l’eau\nen mouvement',WHITE,20,True)
    d.block(495,650,'STOCKER /\nALIMENTER','Batterie 12 V',YELLOW,stock=True)
    d.arrow([(705,465),(760,465),(760,688),(705,688)],YELLOW,'Énergie électrique\nCharge / décharge',590,582,both=True)
    d.block(1190,650,'CONVERTIR','Actionneur(s)\nd’électrovanne(s)',VIOLET)
    d.arrow([(940,550),(940,688),(1180,688)],ORANGE,'Énergie électrique',1040,620)
    d.arrow([(1400,688),(1565,688)],ORANGE,'Énergie\nmécanique',1480,625)
    d.text(1480,746,'Ouvrir / fermer\nl’arrivée d’eau',WHITE,20,True)
    d.section(875,'CIRCUIT D’EAU — trajet de la matière, distinct des flèches d’énergie',CYAN)
    for x,txt in [(150,'Réservoir'),(550,'Pompe'),(975,'Électrovanne(s)'),(1430,'Bacs A, B, C')]: d.text(x,945,txt,WHITE,24,True)
    for a,b in [(245,445),(635,835),(1120,1300)]: d.arrow([(a,936),(b,936)],CYAN,'Eau',(a+b)/2,904)
    d.text(800,1005,'La pompe et les électrovannes sont les mêmes composants que dans la chaîne d’énergie.',BLUE,20)
    d.text(800,1050,'Vanne commune : arrosage simultané. Une vanne par bac : commande indépendante des bacs.',BLUE,20)
    d.text(800,1093,'Schéma de principe : les raccordements du régulateur et les interfaces dépendent du matériel choisi.',BLUE,18)
    d.save(C4/'4e/4e_C4.1/Images/chaines_jardin_connecte.svg')


def gabarit():
    d=Diagram('Station autonome : élaborer son alimentation électrique',
        'Gabarit à compléter : conversion solaire, régulation de charge, sélection de la source puis adaptation de tension vers les équipements de la station. La batterie est une branche de stockage reliée au régulateur, avec énergie chimique stockée et échanges électriques de charge et décharge. Une alimentation secteur isolée de 12 volts constitue une autre branche vers le sélecteur de source, utilisable quand le secteur est disponible. Cinq composants à placer : panneau (1), batterie (2), régulateur (3), convertisseur de tension (4) et basculement (5). L’ampoule et le haut-parleur sont hors du périmètre de cette alimentation ; ils seraient des récepteurs alimentés par elle.',1080)
    d.text(800,88,'À compléter : associe les composants aux fonctions, puis nomme les énergies sur les flèches.',WHITE,22)
    d.section(145,'GABARIT — fonctions fournies, composants à choisir',ORANGE)
    for x,f,c in [(155,'CONVERTIR','1. ………………………'),(500,'RÉGULER','3. ………………………'),(850,'DISTRIBUER','5. ………………………'),(1200,'ADAPTER','4. ………………………')]: d.block(x,235,f,c,YELLOW)
    for a,b in [(15,145),(365,490),(710,840),(1060,1190),(1410,1560)]: d.arrow([(a,273),(b,273)],ORANGE,'Énergie\n…………',(a+b)/2,202)
    d.text(1490,340,'Alimenter\nla station',WHITE,21,True)
    d.block(500,490,'STOCKER /\nALIMENTER','2. ………………………',YELLOW,stock=True)
    d.arrow([(710,290),(760,290),(760,528),(710,528)],YELLOW,'Énergie électrique\nCharge / décharge',970,447,both=True)
    d.text(955,390,'Sélectionner la source',BLUE,18)
    d.text(1305,390,'12 V continu → 5 V continu',BLUE,18)
    d.block(850,650,'ALIMENTER','Alimentation secteur\nisolée : sortie 12 V continu',CYAN)
    d.arrow([(955,640),(955,390)],CYAN,'Énergie électrique\nSecteur disponible',1200,525)
    d.text(315,712,'Entrée secteur',BLUE,21)
    d.arrow([(440,704),(840,704)],CYAN,'Énergie électrique',635,744)
    d.section(820,'PALETTE DES COMPOSANTS — cinq à placer, deux hors du périmètre',VIOLET)
    labels=['Panneau solaire','Régulateur de charge','Batterie 12 V — 40 Ah','Basculement des sources','Convertisseur 12 V → 5 V']
    for i,txt in enumerate(labels): d.text(175+i*310,875,txt,WHITE,19,True)
    d.text(800,935,'Hors du périmètre de l’alimentation : ampoule et haut-parleur, qui en seraient des récepteurs.',BLUE,20)
    d.text(800,987,'Justifie les branchements : le régulateur contrôle la charge ; le sélecteur choisit la source disponible.',WHITE,20)
    d.text(800,1035,'Pendant une coupure du secteur, la batterie peut alimenter la station ; l’autonomie de 72 h reste à vérifier.',BLUE,19)
    d.save(C4/'3e/3e_C4.1/Images/chaine_energie_a_elaborer.svg')


def station():
    d=Diagram('Station d’alerte : mesurer, décider et avertir',
        'La chaîne d’information acquiert une tension analogique simulant le vent sur A1, convertie par le CAN, et un signal logique du bouton sur D2. Le programme traite les mesures et l’acquittement. Le LCD, les voyants et le buzzer communiquent l’alerte à l’agent. Un ordre issu du traitement commande la distribution de l’énergie par les sorties de la carte et les interfaces des modules. L’alimentation USB fournit de l’énergie électrique ; les voyants et le buzzer la convertissent en énergies lumineuse et sonore. La présence d’un transistor intégré dépend du module. Aucune transmission mécanique séparée n’est nécessaire.',850)
    d.section(100,"CHAÎNE D’INFORMATION",CYAN)
    d.block(130,130,'ACQUÉRIR','Anémomètre simulé : A1\nBouton d’acquittement : D2',CYAN,w=300)
    d.text(280,308,'A1 : CAN 10 bits (0 à 1023)\nD2 : entrée logique (0 ou 1)',BLUE,19)
    d.block(660,130,'TRAITER','Microcontrôleur et programme\nSeuils et mémoire d’acquittement',VIOLET,w=300)
    d.block(1200,130,'COMMUNIQUER','Écran LCD, voyants, buzzer\nVers l’agent d’accueil',GREEN,w=300)
    d.arrow([(430,168),(650,168)],CYAN,'Données',540,148)
    d.arrow([(960,168),(1190,168)],CYAN,'Résultats / décisions',1070,148)
    d.arrow([(810,290),(810,365),(755,365),(755,470)],GREEN,'Ordres de commande',1015,351,dashed=True)
    d.section(420,"CHAÎNE D’ÉNERGIE — signalisation lumineuse et sonore",ORANGE)
    d.block(160,490,'ALIMENTER','USB de l’ordinateur\n5 V continu',YELLOW,w=240)
    d.block(610,490,'DISTRIBUER','Sorties de la carte et\ninterfaces des modules',CYAN,w=290)
    d.block(1120,490,'CONVERTIR','Voyants et buzzer',VIOLET,w=250)
    d.arrow([(15,528),(150,528)],ORANGE,'Énergie\nélectrique',80,465)
    d.arrow([(400,528),(600,528)],ORANGE,'Énergie\nélectrique',500,465)
    d.arrow([(900,528),(1110,528)],ORANGE,'Énergie\nélectrique',1005,465)
    d.arrow([(1370,510),(1565,510)],ORANGE,'Énergie lumineuse',1470,480)
    d.arrow([(1370,550),(1565,550)],ORANGE,'Énergie sonore',1470,589)
    d.text(1470,640,'Avertir l’agent',WHITE,22,True)
    d.text(755,663,'Shield Grove : raccordement\nInterface de commande : intégrée ou séparée selon le module',BLUE,19)
    d.text(800,748,'Un voyant ou un buzzer convertit de l’énergie et communique une information : deux points de vue sur le même composant.',BLUE,19)
    d.text(800,797,'Pas de transmission mécanique séparée nécessaire. Vérifier le câblage et les caractéristiques des modules utilisés.',BLUE,19)
    d.save(C9/'Images/chaine_info_energie_station.svg')


def book():
    d=Diagram('Book Train : chaîne d’énergie du déplacement',
        'Modèle fonctionnel simplifié du Book Train. Le réseau électrique alimente une alimentation adaptée. La commande de puissance distribue l’énergie électrique au moteur sur ordre de l’automate. Le moteur convertit l’énergie électrique en énergie mécanique de rotation. Le réducteur et les organes d’entraînement transmettent le mouvement pour déplacer le wagonnet et sa nacelle. Les capteurs fournissent des comptes rendus à la chaîne d’information. Les détails de tensions, de stockage et d’entraînement doivent être établis à partir de la documentation technique.',730)
    d.section(100,"CHAÎNE D’INFORMATION — rappel",CYAN)
    d.block(600,130,'TRAITER','Automate et programme\nDonnées issues des capteurs',VIOLET,w=300)
    d.arrow([(650,270),(650,325),(585,325),(585,430)],GREEN,'Ordres : démarrer, ralentir, arrêter',930,309,dashed=True)
    d.arrow([(1265,415),(1265,170),(910,170)],CYAN,'Comptes rendus des capteurs',1220,130,dashed=True)
    d.section(385,"CHAÎNE D’ÉNERGIE",ORANGE)
    d.block(135,450,'ALIMENTER','Alimentation électrique\nadaptée',YELLOW,w=200)
    d.block(485,450,'DISTRIBUER','Commande de puissance',CYAN,w=200)
    d.block(835,450,'CONVERTIR','Moteur électrique',VIOLET,w=200)
    d.block(1185,450,'TRANSMETTRE','Réducteur et organes\nd’entraînement',GREEN,w=220)
    d.text(80,625,'Source : réseau électrique du bâtiment',BLUE,20,anchor='start')
    d.arrow([(15,488),(125,488)],ORANGE,'Énergie\nélectrique',72,425)
    d.arrow([(335,488),(475,488)],ORANGE,'Énergie\nélectrique',405,425)
    d.arrow([(685,488),(825,488)],ORANGE,'Énergie\nélectrique',755,425)
    d.arrow([(1035,488),(1175,488)],ORANGE,'Énergie mécanique\nde rotation',1105,425)
    d.arrow([(1405,488),(1570,488)],ORANGE,'Énergie\nmécanique',1488,425)
    d.text(1490,555,'Déplacer\nle wagonnet\net sa nacelle',WHITE,20,True)
    d.text(800,675,'Modèle fonctionnel : tensions, éventuel secours et détails d’entraînement à préciser d’après la documentation technique.',BLUE,18)
    d.save(C4/'4e/4e_C4.1_book-train/Images/chaine_energie_book-train.svg')
    # Même schéma disponible depuis le dossier des fichiers modifiables.
    src=ROOT/C4/'4e/4e_C4.1_book-train/Images/chaine_energie_book-train.svg'
    (src.parent.parent/'fichiers_drawio/chaine_energie_book-train.svg').write_bytes(src.read_bytes())
    lot=src.parent.parent
    complete=(lot/'fichiers_drawio/chaine_energie_book-train.drawio').read_text(encoding='utf-8')
    template=ET.fromstring(complete)
    components={'Alimentation électrique\nadaptée','Commande de puissance','Moteur électrique','Réducteur et organes\nd’entraînement'}
    for cell in template.iter('mxCell'):
        if cell.get('value') in components:
            cell.set('value','Composant : ………………………')
        elif cell.get('value') in {'ALIMENTER','DISTRIBUER','CONVERTIR','TRANSMETTRE'}:
            cell.set('value','Fonction : ……………')
        elif cell.get('value','').startswith('Énergie'):
            cell.set('value','Énergie : ……………')
    blank=ET.tostring(template,encoding='unicode')+'\n'
    (lot/'fichiers_drawio/chaine_energie_a_completer.drawio').write_text(blank,encoding='utf-8')
    page=lot/'sequence_4e_C4.1-C4.2-C4.4_book-train.html'
    html=page.read_text(encoding='utf-8')
    inline=src.read_text(encoding='utf-8')
    ids=re.findall(r'\bid="([^"]+)"',inline)
    for ident in ids:
        inline=inline.replace(f'id="{ident}"',f'id="fig4{ident}"').replace(f'url(#{ident})',f'url(#fig4{ident})')
    inline=inline.replace('aria-labelledby="t d"','aria-labelledby="fig4t fig4d"')
    html,n=re.subn(r'<svg\b[^>]*aria-labelledby="fig4t fig4d"[^>]*>.*?</svg>',lambda _:inline,html,count=1,flags=re.S)
    if n!=1: raise RuntimeError('Figure 4 du Book Train introuvable')
    def downloads(m):
        files=json.loads(m.group(1))
        files['chaine_energie_book-train.drawio']=complete
        files['chaine_energie_a_completer.drawio']=blank
        return 'var FICHIERS = '+json.dumps(files,ensure_ascii=False)+';'
    html,n=re.subn(r'var FICHIERS = (\{[^\n]*\});',downloads,html,count=1)
    if n!=1: raise RuntimeError('Fichiers incorporés du Book Train introuvables')
    page.write_text(html,encoding='utf-8')
    quiz=lot/'qcm_book-train.html'
    q=quiz.read_text(encoding='utf-8')
    alternative='Chaîne d’énergie : ALIMENTER (alimentation électrique adaptée), DISTRIBUER (commande de puissance), CONVERTIR (moteur), TRANSMETTRE (réducteur et organes d’entraînement). Les flèches portent l’énergie électrique puis mécanique. L’ordre de l’automate pilote DISTRIBUER. Action : déplacer le wagonnet et sa nacelle.'
    q=re.sub(r'img:\{"src":"Images/chaine_energie_book-train\.svg","alt":"[^"\n]*"\}',lambda _:'img:'+json.dumps({'src':'Images/chaine_energie_book-train.svg','alt':alternative},ensure_ascii=False,separators=(',',':')),q)
    q=q.replace('"réseau continu 24 V → converti en alternatif 480 V → moteur → rail","réseau alternatif 480 V → continu 24 V → rail → moteur → wagonnet","batterie du wagonnet → moteur → rail → capteurs","moteur → convertisseur → rail → réducteur"','"moteur → alimentation → commande → wagonnet","réseau → alimentation adaptée → commande de puissance → moteur → transmission → déplacement","capteurs → moteur → réseau → rail","transmission → réseau → moteur → commande"')
    q=q.replace('Le bâtiment est alimenté en alternatif : on part du 480 V ~, on ne le fabrique pas.','Le moteur reçoit de l’énergie électrique : il ne précède pas son alimentation.')
    q=q.replace("Le wagonnet n'a pas de batterie : il est alimenté en continu par le rail.",'Les capteurs fournissent des informations ; ils ne constituent pas le départ de cette chaîne d’énergie.')
    quiz.write_text(q,encoding='utf-8')


if __name__=='__main__':
    for generate in (lampadaire,jardin,gabarit,station,book): generate()
