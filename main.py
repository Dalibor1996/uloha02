import pickle
zoznam_krajin = {}
def pridaj_krajinu(country, capital):
    """Add a country and its capital to the dictionary."""
    zoznam_krajin[country] = capital
    return f"krajina {country} bola pridana s hlavnym mestom {capital}"

def vymaz_krajinu(country):
    if country in zoznam_krajin:
        del zoznam_krajin[country]
        return f"krajina {country} bola vymazana aj s hlavnym mestom {capital}"
    else:
        return f"krajina {country} sa nenachadza v zozname krajin"

def uprav_krajinu(country, capital, new_capital):
    if country in zoznam_krajin:
        new_capital = str(input("Napiste nove hlavne mesto"))
        zoznam_krajin[country] = new_capital
    return f"krajine {country} bolo zmenene hlavne mesto z {capital} na {new_capital}"

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
        print("Queue is empty." if queue.is_empty() else "Queue is not empty.")
    elif choice == 2:
        vymaz_krajinu()
        print("Queue is full." if queue.is_full() else "Queue is not full.")
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
       perform_operation(choice, q)

main()
