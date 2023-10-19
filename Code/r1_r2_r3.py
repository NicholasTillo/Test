import csv

# File paths
users_csv_path = "Code/users.csv"
restaurants_csv_path = "Code/restaurants.csv"
menu_csv_path = "Code/menu.csv"


# Register user with a password
def register_user(username, password, email, location, role):
    # Open the users.csv file in read mode to check if the username already exists then close it
    with open(users_csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        # Checking username which is first column of the row
        for row in reader:
            if row[0] == username:
                return "This username already exists!"

    # Username does not exist so register the new user
    # Open the user csv and add a new row
    with open(users_csv_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Write in the user details
        writer.writerow([username, password, email, location, role])

    return print("Success! Proceed to log in.")


test_user1 = register_user(
    "Dan", "DanDan12", "dandan@email.com", "SF", "customer")
print(test_user1)


# Log in a user
def login_user(username, password):
    user_found = False
    # Open the users.csv file in read mode to verify the user
    with open(users_csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if row[0] == username:
                user_found = True

                if row[1] == password:
                    return "Login success!"
                else:
                    return "Password is invalid."
    if user_found == False:
        return "User does not exist. Please double check credentials or register as a new user"


test_user2 = login_user("Christyl", "321")
print(test_user2)


def select_restaurant_and_view_menu(user_location):
    restaurants = {}

    # Open restaurants.csv
    with open(restaurants_csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if row:
                restaurant_name = row[0] 
                restaurant_location = row[-2]

                if restaurant_location == user_location:
                    restaurants[restaurant_name] = restaurant_location

    if not restaurants:
        return f"No restaurants found in {user_location}."

    # Display the list of restaurants near the user's location
    for index, name in enumerate(restaurants.keys(), start=1):
        print(f"{index}. {name}")

    # Ask the user to select a restaurant
    selection = input(
        "Enter the number of the selected restaurant (i.e. for the first restaurant on the list type in '1'): ")

    try:
        # Convert the selection to an integer
        selected_index = int(selection) - 1  # Adjusting for 0-based index
        selected_name = list(restaurants.keys())[selected_index]

        # Read and isplay the menu for the selected restaurant
        menu = []
        with open(menu_csv_path, 'r') as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                restaurant_name, item_name, price, category, description, quantity = row
                if restaurant_name == selected_name:
                    menu_item = f"{item_name} - Price: {price}, Category: {category}, Description: {description}"
                    menu.append(menu_item)

        return f"You selected: {selected_name}. Menu: {', '.join(menu)}"

    except (ValueError, IndexError):
        return "Invalid selection. Please select a valid number from the list."


# Test the restaurant selection and menu viewing function
user_location = "K7K"  # Assuming the user is in Toronto
restaurant_menu = select_restaurant_and_view_menu(user_location)
print(restaurant_menu)
