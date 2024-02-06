import pickle

# Define the dictionary that will hold the country names and their capitals
countries_dict = {}

# Define functions for each of the operations required

def add_data(country, capital):
    """Add a country and its capital to the dictionary."""
    countries_dict[country] = capital
    return f"{country} added with capital {capital}"

def delete_data(country):
    """Delete a country and its capital from the dictionary."""
    if country in countries_dict:
        del countries_dict[country]
        return f"{country} deleted"
    else:
        return f"{country} not found"

def find_data(country):
    """Find the capital of a country."""
    return countries_dict.get(country, f"Capital of {country} not found")

def edit_data(country, new_capital):
    """Edit the capital of an existing country."""
    if country in countries_dict:
        countries_dict[country] = new_capital
        return f"Capital of {country} changed to {new_capital}"
    else:
        return f"{country} not found to edit"

def save_data(filename="countries.pkl"):
    """Save the dictionary to a file using pickle."""
    with open(filename, 'wb') as handle:
        pickle.dump(countries_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return f"Data saved to {filename}"

def load_data(filename="countries.pkl"):
    """Load the dictionary from a file using pickle."""
    with open(filename, 'rb') as handle:
        global countries_dict
        countries_dict = pickle.load(handle)
    return f"Data loaded from {filename}"

# Demonstrate the usage of these functions:

# Add some countries and their capitals
add_msg1 = add_data("Germany", "Berlin")
add_msg2 = add_data("France", "Paris")

# Edit a capital
edit_msg = edit_data("Germany", "New Berlin")

# Find a capital
find_msg = find_data("France")

# Save the data to a file
save_msg = save_data()

# Now, let's delete a country
delete_msg = delete_data("Germany")

# Load the data back from the file
load_msg = load_data()

# Let's check the current state of the dictionary
current_state = countries_dict

(add_msg1, add_msg2, edit_msg, find_msg, save_msg, delete_msg, load_msg, current_state)

