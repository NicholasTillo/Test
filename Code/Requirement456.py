import re 
import random
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import csv






class cart():
    def __init__(self) -> None:
        self.current_cart= []

    def get_total_price(self):
        total_cost = 0
        for i in self.current_cart:
            total_cost += i.cost
        print(total_cost)
        

#Each user has 1 cart. 
usr_cart = cart()

#Create Tkinter Window
root = ThemedTk(theme ="equilux")

# File paths
users_csv_path = "Code/users.csv"
restaurants_csv_path = "Code/restaurants.csv"
menu_csv_path = "Code/menu.csv"


current_login = None


#Create and Populate GUI
def create_GUI():
    root.geometry("500x500")
    tabControl = ttk.Notebook(root,name = "qoo")
    tab1 = ttk.Frame(tabControl,name ="one")
    tab2 = ttk.Frame(tabControl,name = "two")
    tab3 = ttk.Frame(tabControl, name = "three")
    tab4 = ttk.Frame(tabControl, name = "four")

    tabControl.add(tab1, text = "Home")
    tabControl.add(tab2, text = "Cart")
    tabControl.add(tab3, text = "Orders")
    tabControl.add(tab4, text = "Resturants")
    tabControl.pack(expand="1",fill="both")
    populate_home()
    root.mainloop()


def register_insert():
    name=root.nametowidget(".qoo.one.i1").get()
    password=root.nametowidget(".qoo.one.i2").get()
    email =root.nametowidget(".qoo.one.i3").get()
    location= root.nametowidget(".qoo.one.i4").get()
    role =root.nametowidget(".qoo.one.i5").state()
    if role:
        role = "customer"
    else:
        role = "restaruant"

    print(register_user(name,password,email,location,role))


def login_insert():
    name=root.nametowidget(".qoo.one.l1").get()
    password=root.nametowidget(".qoo.one.l2").get()
    print(login_user(name,password))
    print(current_login)




def populate_home():
    RegisterTitle = ttk.Label(root.nametowidget(".qoo.one") ,text = "Register Info").grid(row = 0,column = 0)

    RegisterName = ttk.Label(root.nametowidget(".qoo.one") ,text = "Username").grid(row = 1,column = 0)
    RegisterPassword = ttk.Label(root.nametowidget(".qoo.one") ,text = "Password").grid(row = 2,column = 0)
    RegisterEmail = ttk.Label(root.nametowidget(".qoo.one") ,text = "Email Id").grid(row = 3,column = 0)
    RegisterLocation = ttk.Label(root.nametowidget(".qoo.one") ,text = "Location (Postal Code)").grid(row = 4,column = 0)

    RegisterNameEntry = ttk.Entry(root.nametowidget(".qoo.one"),name = "i1").grid(row = 1,column = 1)
    RegisterPasswordEntry = ttk.Entry(root.nametowidget(".qoo.one"), name = "i2").grid(row = 2,column = 1)
    RegisterEmailEntry = ttk.Entry(root.nametowidget(".qoo.one"), name = "i3").grid(row = 3,column = 1)
    RegisterLocationEntry = ttk.Entry(root.nametowidget(".qoo.one"), name = "i4").grid(row = 4,column = 1)
    RegisterRoleButton = ttk.Checkbutton(root.nametowidget(".qoo.one"), text='Are You A Customer?',onvalue=1, offvalue=0, name = "i5").grid(row=5,column=1)

    
    RegisterSubmit = ttk.Button(root.nametowidget(".qoo.one"), text="Submit", command=register_insert).grid(row=6,column=0)


    LoginTitle = ttk.Label(root.nametowidget(".qoo.one") ,text = "Login Info").grid(row = 7,column = 0)

    LoginName = ttk.Label(root.nametowidget(".qoo.one") ,text = "Username").grid(row = 8,column = 0)
    LoginPass = ttk.Label(root.nametowidget(".qoo.one") ,text = "Password").grid(row = 9,column = 0)
    LoginNameEntry = ttk.Entry(root.nametowidget(".qoo.one"),name = "l1").grid(row = 8,column = 1)
    LoginPassEntry = ttk.Entry(root.nametowidget(".qoo.one"), name = "l2").grid(row = 9,column = 1)
    LoginSubmit = ttk.Button(root.nametowidget(".qoo.one"), text="Submit", command=login_insert).grid(row=10,column=0)



#counter = 0

def populate_resturant():
    counter = 0
    global current_login

    restaurants = {}

    # Open restaurants.csv
    with open(restaurants_csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if row:
                restaurant_name = row[0] 
                restaurant_location = row[-2]

                if restaurant_location == current_login[2]:
                    restaurants[restaurant_name] = restaurant_location

    if not restaurants:
        return f"No restaurants found in {current_login[2]}."


    for i in restaurants.keys():
        create_restaurant_button(restaurants,i,counter)
        counter += 1


def create_restaurant_button(essd,i,val):
    ttk.Button(root.nametowidget(".qoo.four"), text = i,command = lambda: select_restaurant_and_view_menu(current_login[2],val+1)).pack()
    ttk.Label(root.nametowidget(".qoo.four"), text = i).pack()
    ttk.Label(root.nametowidget(".qoo.four"), text = essd[i]).pack()


def populate_smn():
    pass




def add_to_cart(item):
    print(item)
    usr_cart.current_cart.append(item)


def remove_from_cart(item):
    usr_cart.current_cart.pop(item)


def check_out():
    check_cart(usr_cart)
    x = payment(usr_cart)
    while not x:
        x = payment(usr_cart)
    create_delivery_status(usr_cart.get_total_price(), usr_cart.current_cart)



def payment(cart):
    input = getCardInfo()
    if chargeCard(cart.getTotalPrice(), input):
        return True
    else:
        return False
    

def getCardInfo():
    while True:
        x = input("Enter Credit Card Number (16 Digit Code)")
        y = input("Enter Credit Card Expiration Date: (dd/mm)")
        z = input("Enter Credit Card Card Verification Value: (cvv)")
        retval = [x,y,z]
        if checkValidCard(retval):
            x = input("this shit bad redo, x to cancel space to redo ")
            if x == "x":
                return
            else:
                continue       
        return retval

def checkValidCard(credit_card):
    x = re.search("\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}", str(credit_card[0]))
    y = re.search("\d{2}[ /]?\d{2}",credit_card[1])
    z = re.search("\d{3}",credit_card[2])

    return (x == None or y == None or z == None)



def chargeCard(p_card, p_price):
    try:
        pass
    except:
        return False
    pass


def check_cart(p_cart):
    for i in p_cart:
        display_item(i)


def display_item(p_item):
    print(p_item)

#
def create_delivery_status(p_cost, item_list):
    x = random.randint(1,50000)
    file = open("Code/Fulfilled _Orders.csv", 'a')
    file.write("\n"+str(x)+","+str(p_cost)+","+ str(item_list)+",No,No")
    file.close()
    return x

#Check a given order_id for its current status and print it out. 
def check_delivery_status(order_id):
    file = open("Code/Fulfilled _Orders.csv", 'r')
    for i in file:
        split = i.split(",")
        if split[0] == str(order_id):
            print(split)
    file.close()
    pass




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





# Log in a user
def login_user(username, password):
    
    global current_login
    user_found = False
    # Open the users.csv file in read mode to verify the user
    with open(users_csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if row[0] == username:
                user_found = True

                if row[1] == password:
                    current_login = (username,password,row[3])
                    populate_resturant()
                    return "Login success!"
                else:
                    return "Password is invalid."
    if user_found == False:
        return "User does not exist. Please double check credentials or register as a new user"



def select_restaurant_and_view_menu(user_location,selection = 0):
    print(selection)
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
    #selection = input(
    #    "Enter the number of the selected restaurant (i.e. for the first restaurant on the list type in '1'): ")

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

        print(f"You selected: {selected_name}. Menu: {', '.join(menu)}")
        display_menu(selected_name,menu)

    except (ValueError, IndexError):
        print("Invalid selection. Please select a valid number from the list.")


def display_menu(store, menu):
    print(menu)
    root2 = ThemedTk(theme ="equilux")
    root2.title(store)
    root2.geometry("325x325")
    for i in menu:
        print(i)
        create_menu_button(root2, i)

    root2.mainloop()


def create_menu_button(root2,i):
    ttk.Button(root2, text = i,command = lambda: add_to_cart(i)).pack()

    





test_user2 = login_user("Christyl", "321")
print(test_user2)


# Test the restaurant selection and menu viewing function
#user_location = "K7K"  # Assuming the user is in Toronto
#restaurant_menu = select_restaurant_and_view_menu(user_location)
#print(restaurant_menu)





create_GUI()