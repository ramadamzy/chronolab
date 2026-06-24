print("=== CHRONOLAB ===")
print("Welkom in het Tijdreis Laboratorium!")

naam = input("Wat is je naam? ")

print(f"Welkom {naam}!")
print("Jouw missie: red de toekomst door tijd te reizen.")

while True:
    print("\n=== TIJDREIS MENU ===")
    print("1. Reis naar 1886")
    print("2. Reis naar 1969")
    print("3. Reis naar 2026")
    print("4. Stoppen")

    keuze = input("Maak je keuze: ")

    if keuze == "1":
        print("\n🕰️ Je reist naar 1886...")
        print("Je komt aan in een oud, verlaten laboratorium.")

        antwoord = input ("Puzzel: Wat is 12 + 8?")
        if antwoord == "20":
            print("Correct! Je hebt de puzzel opgelost en een aanwijzing gevonden.") 
        else:
            print("Helaas, dat is niet correct. Probeer het opnieuw.")        
    
    elif keuze == "2":
        print("\n🚀 Je reist naar 1969...")
        print("Je staat in een geheime NASA faciliteit.")

    elif keuze == "3":
        print("\n💻 Je reist naar 2026...")
        print("De toekomst is chaotisch en instabiel.")

    elif keuze == "4":
        print("\nJe sluit de tijdmachine. Tot ziens!")
        break

    else:
        print("\nOngeldige keuze, probeer opnieuw.")