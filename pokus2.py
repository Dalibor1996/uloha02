class CountryCapitalDictionary:
    def __init__(self):
        self.dictionary = {}

    def add_data(self):
        country = input("Enter the country name: ")
        capital = input("Enter the capital name: ")
        self.dictionary[country] = capital
        return "1. Data added: {} - {}".format(country, capital)

    def delete_data(self):
        country = input("Enter the country name to delete: ")
        if country in self.dictionary:
            del self.dictionary[country]
            return "2. Data deleted for country: {}".format(country)
        else:
            return "2. No data found for country: {}".format(country)

    def find_data(self):
        country = input("Enter the country name to find: ")
        capital = self.dictionary.get(country, 'Not found')
        return "3. Capital of {}: {}".format(country, capital)

    def edit_data(self):
        country = input("Enter the country name to edit: ")
        if country in self.dictionary:
            new_capital = input("Enter the new capital for {}: ".format(country))
            self.dictionary[country] = new_capital
            return "4. Data edited for {}, new capital: {}".format(country, new_capital)
        else:
            return "4. No data found for country: {}".format(country)

    def save_data(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self.dictionary, file)
        return "5. Data saved to {}".format(file_path)

    def load_data(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                self.dictionary = pickle.load(file)
            return "6. Data loaded from {}".format(file_path)
        except FileNotFoundError:
            return "6. File not found: {}".format(file_path)
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

def perform_operation(cc_dict, choice):
    if choice == 1:
        return cc_dict.add_data()
    elif choice == 2:
        return cc_dict.delete_data()
    elif choice == 3:
        return cc_dict.edit_data()

    elif choice == 4:
        return cc_dict.find_data()

    else:
        print("Invalid choice. Please try again.")
# Example usage in a local environment
cc_dict = CountryCapitalDictionary()
choice = display_menu()
result = perform_operation(cc_dict, choice)
print(result)
#cc_dict.add_data()  # User will be prompted for input
