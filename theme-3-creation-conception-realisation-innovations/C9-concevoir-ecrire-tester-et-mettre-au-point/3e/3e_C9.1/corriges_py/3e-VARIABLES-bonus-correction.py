# Défi convertisseur : une correction possible.
def miles_vers_km(d):
    return round(d * 1.609, 2)  # 1 mile = 1.609 km

def fahrenheit_vers_celsius(t):
    return round((t - 32) / 1.8, 1)  # la formule du panneau, activité 4

print("Marathon :", miles_vers_km(26.2), "km")
print("Canicule :", fahrenheit_vers_celsius(98), "°C")

# Défi MetroCard : la carte 1 $, chaque trajet 2.90 $, gratuits au-delà de 12 par semaine.
def prix_total(nb_trajets):
    payants = min(nb_trajets, 12)
    return round(1 + 2.90 * payants, 2)

# le banc de tests, écrit avant : 0 trajet, 1, la frontière 12, juste après 13, et loin après 20
for n in [0, 1, 12, 13, 20]:
    print(n, "trajets :", prix_total(n), "$")
