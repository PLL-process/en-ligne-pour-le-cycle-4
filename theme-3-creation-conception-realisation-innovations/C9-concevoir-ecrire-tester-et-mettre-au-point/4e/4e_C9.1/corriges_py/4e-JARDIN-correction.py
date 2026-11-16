# --- les réglages, écrits une seule fois, tout en haut ---
SEUIL = 40
HEURE_DEBUT = 6
HEURE_FIN = 10

# --- les entrées (en vrai : le capteur et l'horloge) ---
H = 25
heure = 8

# --- la décision : le losange de l'algorigramme ---
if H < SEUIL and heure >= HEURE_DEBUT and heure <= HEURE_FIN:
    print("POMPE ON")
else:
    print("POMPE OFF")
