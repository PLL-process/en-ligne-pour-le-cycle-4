# Le programme du lampadaire (activité 6) : une version parmi d'autres.
SEUIL_BAS = 20    # il fait vraiment sombre
SEUIL_HAUT = 60   # il fait vraiment jour

while True:
    L = lire_luminosite()
    if L < SEUIL_BAS:
        allumer_lampadaire()
    elif L > SEUIL_HAUT:
        eteindre_lampadaire()
    # entre 20 et 60 : on ne change rien
