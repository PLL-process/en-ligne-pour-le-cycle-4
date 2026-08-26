/*
  STATION D'ALERTE CYCLONIQUE — 3e_C9.2 (dossier principal) & 3e_C8.3
  Carte : Arduino UNO (arduino:avr:uno) + shield Grove
  Élèves : programme réalisé en blocs ArduBlock Éducation 1.7 ;
           ce fichier est le C++ de référence, commenté ligne par ligne.

  IHM (interaction humain-machine, cœur de 3e_C9.2) :
    - Afficheur LCD RGB Grove (I2C)  : niveau d'alerte + vitesse du vent
    - Bouton Grove (D2)              : ACQUITTER l'alarme sonore
    - DEL rouge Grove (D3)           : signal visuel d'alerte
    - Buzzer Grove (D5)              : alarme sonore (acquittable)
  Capteur :
    - Potentiomètre Grove (A1)       : simule l'anémomètre (vitesse du vent)

  Sécurité : montage en très basse tension (5 V) uniquement.
*/

#include <Wire.h>              // bibliothèque du bus I2C (dialogue avec le LCD)
#include "rgb_lcd.h"           // bibliothèque Grove de l'afficheur LCD RGB

rgb_lcd ecran;                 // objet qui représente l'afficheur LCD

// ---- Brochages (constantes : elles ne changent jamais) ----
const int BROCHE_BOUTON  = 2;   // bouton d'acquittement sur D2
const int BROCHE_ORANGE  = 3;   // voyant ORANGE (ouragan) sur D3
const int BROCHE_ROUGE   = 4;   // voyant ROUGE (ouragan majeur) sur D4
const int BROCHE_BUZZER  = 5;   // buzzer d'alarme sur D5
const int BROCHE_VERT    = 6;   // voyant VERT (veille) sur D6
const int BROCHE_JAUNE   = 7;   // voyant JAUNE (tempête tropicale) sur D7
const int BROCHE_VENT    = A1;  // potentiomètre « anémomètre » sur A1

// ---- Seuils, en km/h : ce sont ceux de l'échelle de Saffir-Simpson ----
// 63 = entrée en tempête tropicale · 118 = entrée en ouragan (catégorie 1)
// 178 = ouragan majeur (catégorie 3). Ils sont écrits À UN SEUL ENDROIT :
// c'est ce qui permet de les régler sans relire tout le programme.
const int SEUIL_JAUNE  = 63;
const int SEUIL_ORANGE = 118;
const int SEUIL_ROUGE  = 178;

// ---- Variables d'état (elles changent pendant l'exécution) ----
int  vitesseVent   = 0;        // vitesse du vent calculée, en km/h
int  niveauAlerte  = 0;        // 0 = veille · 1 = tempête tropicale · 2 = ouragan · 3 = ouragan majeur
int  niveauPrecedent = -1;     // niveau au tour de boucle précédent
bool alarmeAcquittee = false;  // true si l'humain a acquitté l'alarme

// ---- La pulsation des voyants ----
// Le voyant du niveau courant s'allume et s'éteint tour à tour, pour attirer
// l'œil. Le VERT, lui, reste FIXE : une lumière qui clignote en permanence, on
// finit par ne plus la voir — la pulsation doit rester un SIGNAL.
// On ne l'obtient pas avec delay() : delay() arrêterait TOUT le programme, y
// compris la lecture du bouton. On regarde l'heure à la place.
const unsigned long DEMI_PERIODE_PULSATION = 600;  // ms → un cycle complet de 1,2 s
unsigned long dernierBasculement = 0;
bool pulsation = true;

// ---- Annonce des sous-programmes ----
// L'IDE Arduino les devine tout seul ; on les écrit quand même, parce que c'est
// la règle en C++ : on ANNONCE avant d'UTILISER. Le programme devient alors
// compilable par n'importe quel compilateur C++, et la liste ci-dessous se lit
// comme un sommaire — on voit d'un coup d'œil ce que la station sait faire.
void afficherEtat();
void allumerVoyants();

void setup() {
  pinMode(BROCHE_BOUTON, INPUT);    // le bouton Grove est une ENTRÉE numérique
  pinMode(BROCHE_VERT,   OUTPUT);   // les quatre voyants sont des SORTIES
  pinMode(BROCHE_JAUNE,  OUTPUT);
  pinMode(BROCHE_ORANGE, OUTPUT);
  pinMode(BROCHE_ROUGE,  OUTPUT);
  pinMode(BROCHE_BUZZER, OUTPUT);   // le buzzer est une SORTIE numérique
  ecran.begin(16, 2);               // démarre le LCD : 16 colonnes, 2 lignes
  Serial.begin(9600);               // ouvre le moniteur série (mise au point)
  ecran.print("Station ALERTE");    // message d'accueil, ligne 1
  ecran.setCursor(0, 1);            // curseur au début de la ligne 2
  ecran.print("Cyclone - 3e");      // message d'accueil, ligne 2
  delay(2000);                      // laisse 2 s pour lire l'accueil
}

void loop() {
  // 1. ACQUÉRIR : lire le capteur (0 à 1023) et convertir en km/h (0 à 250)
  int mesureBrute = analogRead(BROCHE_VENT);          // valeur brute du CAN
  vitesseVent = map(mesureBrute, 0, 1023, 0, 250);    // conversion en km/h

  // 2. TRAITER : décider du niveau d'alerte selon les seuils
  if (vitesseVent >= SEUIL_ROUGE) {
    niveauAlerte = 3;                                 // ouragan majeur
  } else if (vitesseVent >= SEUIL_ORANGE) {
    niveauAlerte = 2;                                 // ouragan
  } else if (vitesseVent >= SEUIL_JAUNE) {
    niveauAlerte = 1;                                 // tempête tropicale
  } else {
    niveauAlerte = 0;                                 // simple veille
  }

  // 3. INTERACTION HUMAIN → MACHINE : le bouton acquitte l'alarme sonore
  if (digitalRead(BROCHE_BOUTON) == HIGH) {           // bouton Grove appuyé
    alarmeAcquittee = true;                           // l'humain a répondu
  }
  if (niveauAlerte != niveauPrecedent) {              // le niveau vient de changer
    alarmeAcquittee = false;                          // nouvel événement : l'alarme repart
  }

  // 4. COMMANDER : machine → humain (LCD, DEL, buzzer)
  if (millis() - dernierBasculement >= DEMI_PERIODE_PULSATION) {
    dernierBasculement = millis();                    // on note l'heure du basculement
    pulsation = !pulsation;                           // et on inverse l'état
  }
  afficherEtat();                                     // sous-programme d'affichage
  allumerVoyants();                                   // sous-programme des voyants
  bool alarmeSonore = (niveauAlerte == 3) && !alarmeAcquittee; // buzzer en ouragan majeur seulement
  digitalWrite(BROCHE_BUZZER, alarmeSonore ? HIGH : LOW);

  // 5. TRACER : envoyer la mesure au moniteur série (mise au point, C8.3)
  Serial.print("vent(km/h)=");
  Serial.print(vitesseVent);
  Serial.print(" niveau=");
  Serial.println(niveauAlerte);

  niveauPrecedent = niveauAlerte;   // mémorise le niveau pour le tour suivant
  delay(200);                       // 5 mesures par seconde environ
}

// Sous-programme (fonction) : affiche le niveau et la vitesse sur le LCD
// — la structuration en sous-programmes est exigée par 3e_C9.1/C9.2.
void afficherEtat() {
  ecran.setCursor(0, 0);                        // ligne 1 : le niveau
  if (niveauAlerte == 3) {
    ecran.setRGB(255, 0, 0);                    // fond ROUGE
    ecran.print("OURAGAN MAJEUR  ");
  } else if (niveauAlerte == 2) {
    ecran.setRGB(255, 120, 0);                  // fond ORANGE
    ecran.print("OURAGAN         ");
  } else if (niveauAlerte == 1) {
    ecran.setRGB(230, 210, 60);                 // fond JAUNE
    ecran.print("TEMPETE TROP.   ");
  } else {
    ecran.setRGB(0, 180, 60);                   // fond VERT
    ecran.print("VEILLE          ");
  }
  ecran.setCursor(0, 1);                        // ligne 2 : la mesure
  ecran.print("Vent: ");
  ecran.print(vitesseVent);
  ecran.print(" km/h   ");
}

// Sous-programme : un SEUL voyant allumé, celui du niveau courant.
// Écrire les quatre états à chaque fois — et non « allumer celui-ci » —
// évite qu'un voyant du niveau précédent reste allumé par inadvertance.
// À partir du jaune, le voyant PULSE ; le vert reste fixe.
void allumerVoyants() {
  digitalWrite(BROCHE_VERT,   (niveauAlerte == 0) ? HIGH : LOW);              // FIXE
  digitalWrite(BROCHE_JAUNE,  (niveauAlerte == 1 && pulsation) ? HIGH : LOW); // pulse
  digitalWrite(BROCHE_ORANGE, (niveauAlerte == 2 && pulsation) ? HIGH : LOW); // pulse
  digitalWrite(BROCHE_ROUGE,  (niveauAlerte == 3 && pulsation) ? HIGH : LOW); // pulse
}
