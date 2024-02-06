import pickle
zoznam_krajin = {}
def pridaj_krajinu(country, capital):
    country = str(input("Pridajte krajinu"))
    capital = str(input("Pridaj capital"))
    zoznam_krajin[country] = capital
    return f"krajina {country} bola pridana s hlavnym mestom {capital}"

def vymaz_krajinu(country):
    if country in zoznam_krajin:
        del zoznam_krajin[country]
        return f"krajina {country} bola vymazana aj s hlavnym mestom {capital}"
    else:
        return f"krajina {country} sa nenachadza v zozname krajin"

def uprav_krajinu(country, new_capital, zoznam_krajin):
     if country in zoznam_krajin:
            new_capital = str(input("Napiste nove hlavne mesto: "))
            zoznam_krajin[country] = new_capital
            print(f"Hlavne mesto pre {country} bolo zmenene na {new_capital}.")
     else:
            print(f"Krajina {country} nie je v zozname.")


def najst_krajinu(country):
    if country in zoznam_krajin:
        return f"krajina sa nachadza"
    else:
        return f"krajina sa nenachadza"

def saving(country):
    saved = pickle.dumps(country)
    print(saved)

def nacitaj(country):
    nacitany = pickle.loads(country)
    print(nacitany)

def display_menu():
    print("Krajiny : hlavne mesta Operations Menu:")
    print("1. Pridaj krajinu")
    print("2. Vymaz krajinu")
    print("3. Uprav krajinu")
    print("4. Najdi krajinu")
    print("5. Nacitaj")
    print("6. Saveni")
    choice = int(input("Enter your choice: "))
    return choice

def perform_operation(choice):
    if choice == 1:
        pridaj_krajinu()
    elif choice == 2:
        vymaz_krajinu()
    elif choice == 3:
        uprav_krajinu()

    elif choice == 4:
        najst_krajinu()
    elif choice == 5:
        nacitaj()
    elif choice == 6:
        saving()
    else:
        print("Invalid choice. Please try again.")

def main():
    q = display_menu()
    while True:
       choice = display_menu()
       perform_operation(choice)

main()
