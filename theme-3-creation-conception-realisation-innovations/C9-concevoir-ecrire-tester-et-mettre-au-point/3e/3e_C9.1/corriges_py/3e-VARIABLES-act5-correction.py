def vitesse_ventilation(air, train_arrive):
    if air >= 100:
        return 3
    elif train_arrive:
        return 2
    else:
        return 1

print(vitesse_ventilation(150, False))  # T1 : attendu 3
print(vitesse_ventilation(60, True))    # T2 : attendu 2
print(vitesse_ventilation(40, False))   # T3 : attendu 1
print(vitesse_ventilation(100, False))  # T4 : le cas limite, attendu 3
