from tijdreizen import reis_naar_1886, reis_naar_1969, reis_naar_2026



print("=== CHRONOLAB ===")
print("Welkom in het Tijdreis Laboratorium!")

naam = input("Wat is je naam? ")

print(f"Welkom {naam}!")
print("Jouw missie: red de toekomst door tijd te reizen.")

score = 0

while True:
    print("\n=== TIJDREIS MENU ===")
    print("1. Reis naar 1886")
    print("2. Reis naar 1969")
    print("3. Reis naar 2026")
    print("4. Stoppen")

    keuze = input("Maak je keuze: ")

    if keuze == "1":
        reis_naar_1886()
    
    elif keuze == "2":
        reis_naar_1969()

    elif keuze == "3":
        reis_naar_2026()

    elif keuze == "4":
        print("\nJe sluit de tijdmachine. Tot ziens!")
        break

    else:
        print("\nOngeldige keuze, probeer opnieuw.")