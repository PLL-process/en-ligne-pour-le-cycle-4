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
const int BROCHE_BOUTON = 2;   // bouton d'acquittement sur D2
const int BROCHE_DEL    = 3;   // DEL rouge d'alerte sur D3
const int BROCHE_BUZZER = 5;   // buzzer d'alarme sur D5
const int BROCHE_VENT   = A1;  // potentiomètre « anémomètre » sur A1

// ---- Seuils d'alerte (en km/h) — à étalonner pendant la séance C8.3 ----
const int SEUIL_VIGILANCE = 100;  // au-dessus : vigilance orange
const int SEUIL_ALERTE    = 150;  // au-dessus : alerte rouge

// ---- Variables d'état (elles changent pendant l'exécution) ----
int  vitesseVent   = 0;        // vitesse du vent calculée, en km/h
int  niveauAlerte  = 0;        // 0 = veille, 1 = vigilance, 2 = alerte rouge
int  niveauPrecedent = -1;     // niveau au tour de boucle précédent
bool alarmeAcquittee = false;  // true si l'humain a acquitté l'alarme

void setup() {
  pinMode(BROCHE_BOUTON, INPUT);    // le bouton Grove est une ENTRÉE numérique
  pinMode(BROCHE_DEL, OUTPUT);      // la DEL est une SORTIE numérique
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
  if (vitesseVent >= SEUIL_ALERTE) {
    niveauAlerte = 2;                                 // alerte rouge
  } else if (vitesseVent >= SEUIL_VIGILANCE) {
    niveauAlerte = 1;                                 // vigilance orange
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
  afficherEtat();                                     // sous-programme d'affichage
  digitalWrite(BROCHE_DEL, (niveauAlerte >= 1) ? HIGH : LOW);  // DEL dès la vigilance
  bool alarmeSonore = (niveauAlerte == 2) && !alarmeAcquittee; // buzzer si alerte non acquittée
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
  if (niveauAlerte == 2) {
    ecran.setRGB(255, 0, 0);                    // fond ROUGE
    ecran.print("ALERTE ROUGE !  ");
  } else if (niveauAlerte == 1) {
    ecran.setRGB(255, 120, 0);                  // fond ORANGE
    ecran.print("Vigilance orange");
  } else {
    ecran.setRGB(0, 180, 60);                   // fond VERT
    ecran.print("Veille          ");
  }
  ecran.setCursor(0, 1);                        // ligne 2 : la mesure
  ecran.print("Vent: ");
  ecran.print(vitesseVent);
  ecran.print(" km/h   ");
}
