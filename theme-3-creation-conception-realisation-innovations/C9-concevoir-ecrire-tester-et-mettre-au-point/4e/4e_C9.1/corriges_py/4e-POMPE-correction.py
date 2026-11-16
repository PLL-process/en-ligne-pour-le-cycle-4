# La pompe à deux seuils (activité 5) : le Python que l'atelier écrit avec les bons blocs.
# lire_humidite() et commander_relais() sont fournies par l'atelier de la page (ou par la carte).
SEUIL_BAS = 35
SEUIL_HAUT = 45
# la mémoire : la pompe est-elle allumée ?
pompe_allumee = False
while True:
    H = lire_humidite()
    if H < SEUIL_BAS:
        pompe_allumee = True
    elif H > SEUIL_HAUT:
        pompe_allumee = False
    else:
        pass   # rien : la pompe garde son état
    commander_relais(pompe_allumee)
