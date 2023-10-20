import re 
import random
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import csv





#Define the framework for the users cart.  
class cart():
    #Initizliae a list for the cart.
    def __init__(self) -> None:
        self.current_cart= []

    #Method to get the combined price of all items in the cart. 
    def get_total_price(self):
        total_cost = 0
        for i in self.current_cart:
            total_cost += float(re.findall("\d*\.\d", i)[0])
        return total_cost
        

#Each user has 1 cart. 
usr_cart = cart()

#Create Tkinter Window
root = ThemedTk(theme ="equilux")

# File paths
users_csv_path = "users.csv"
restaurants_csv_path = "restaurants.csv"
menu_csv_path = "menu.csv"
fulfilled_orders_path = "Fulfilled _Orders.csv"

#Current Login
current_login = None


#Create and Populate GUI with the home screen and the tabs. 
def create_GUI():
    root.geometry("900x500")
    tabControl = ttk.Notebook(root,name = "qoo")
    tab1 = ttk.Frame(tabControl,name ="one")
    tab2 = ttk.Frame(tabControl,name = "two")
    tab3 = ttk.Frame(tabControl, name = "three")
    tab4 = ttk.Frame(tabControl, name = "four")
    tab5 = ttk.Frame(tabControl, name = "five")

    #Add tabs to the frames
    tabControl.add(tab1, text = "Home")
    tabControl.add(tab2, text = "Cart")
    tabControl.add(tab3, text = "Orders")
    tabControl.add(tab4, text = "Resturants")
    tabControl.add(tab5, text = "Owner View")

    #Pack Tabs
    tabControl.pack(expand="1",fill="both")
    populate_home()
    root.mainloop()

#Gather the information from the register forms to send to the Register_User function
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

#Gather the information from the login entries and send it to the login_user() function 
def login_insert():
    name=root.nametowidget(".qoo.one.l1").get()
    password=root.nametowidget(".qoo.one.l2").get()
    print(login_user(name,password))
    print(current_login)



#Create buttons, entries and labels for the home page, 
def populate_home():
    RegisterTitle = ttk.Label(root.nametowidget(".qoo.one") ,text = "Register Info").grid(row = 0,column = 0)

    RegisterName = ttk.Label(root.nametowidget(".qoo.one") ,text = "Username").grid(row = 1,column = 0)
    RegisterPassword = ttk.Label(root.nametowidget(".qoo.one") ,text = "Password").grid(row = 2,column = 0)
    RegisterEmail = ttk.Label(root.nametowidget(".qoo.one") ,text = "Email Id").grid(row = 3,column = 0)
    RegisterLocation = ttk.Label(root.nametowidget(".qoo.one") ,text = "Location (First 3 Characters Of Postal Code)").grid(row = 4,column = 0)

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


#Create buttons for the owners options
def populate_owner_view():
    RegisterSubmit = ttk.Button(root.nametowidget(".qoo.five"), text="Create Restaurant", command=create_restaurant).grid(row=1,column=0)
    RegisterSubmit = ttk.Button(root.nametowidget(".qoo.five"), text="Delete Restaurant", command=delete_restaurant).grid(row=2,column=0)
    RegisterSubmit = ttk.Button(root.nametowidget(".qoo.five"), text="Edit Restaurant", command=edit_restaurant).grid(row=3,column=0)
    RegisterSubmit = ttk.Button(root.nametowidget(".qoo.five"), text="Add Item", command=add_item).grid(row=4,column=0)
    RegisterSubmit = ttk.Button(root.nametowidget(".qoo.five"), text="Delete Item", command= remove_item).grid(row=5,column=0)
    RegisterSubmit = ttk.Button(root.nametowidget(".qoo.five"), text="Edit Item", command= edit_item).grid(row=6,column=0)

#Create buttons and labels for the ordering and cart tabs.
def populate_cart():
    print_cart = ttk.Button(root.nametowidget(".qoo.two"), text="Show Cart", command= lambda:check_cart(usr_cart)).grid(row=0,column=0)
    print_cart = ttk.Button(root.nametowidget(".qoo.two"), text="Remove Item From Cart", command= lambda:remove_from_cart()).grid(row=1,column=0)

    CheckOut = ttk.Button(root.nametowidget(".qoo.two"), text="Checkout", command=check_out).grid(row= 3,column=0)
    CheckOut = ttk.Button(root.nametowidget(".qoo.three"), text="Check For Orders", command=populate_fulfilled).pack()
    CheckOut = ttk.Label(root.nametowidget(".qoo.three"), text="OrderID | Cost | Item List | Payment Recieved | Order Fulfilled | User").pack()


#Create labels represending the fulfilled orders onto the correct tab. 
def populate_fulfilled():
    with open(fulfilled_orders_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                user_name = row[5]
                if user_name == current_login[0]:
                    ttk.Label(root.nametowidget(".qoo.three"), text= row).pack()

#Gather all the restaurants within the location and display them on the corresponding tab. 
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

#Create and pack the putton for each restaurant, 
def create_restaurant_button(essd,i,val):
    ttk.Button(root.nametowidget(".qoo.four"), text = i,command = lambda: select_restaurant_and_view_menu(current_login[2],val+1)).pack()
    ttk.Label(root.nametowidget(".qoo.four"), text = i).pack()
    ttk.Label(root.nametowidget(".qoo.four"), text = essd[i]).pack()


#Add the clicked item to cart. 
def add_to_cart(item):
    print(item)
    usr_cart.current_cart.append(item)

#Promt the user to chose a cart item and remove it. 
def remove_from_cart():
    check_cart(usr_cart)
    x = input("Which Item Would You Like To Remove?")
    usr_cart.current_cart.pop(int(x))

#Process and checkout all items in the users cart. 
def check_out():
    #Print Cart
    check_cart(usr_cart)
    #Gather payment 
    x = payment(usr_cart)
    while not x:
        x = payment(usr_cart)
    create_delivery_status(usr_cart.get_total_price(), usr_cart.current_cart)


#Gather payment information and charge card
def payment(cart):
    input = get_card_info()
    x = cart.get_total_price()
    print("Cost: " + str(x))
    if charge_card(x, input):
        return True
    else:
        return False
    
#Gather card infomration form the user. 
def get_card_info():
    while True:
        x = input("Enter Credit Card Number (16 Digit Code)")
        y = input("Enter Credit Card Expiration Date: (dd/mm)")
        z = input("Enter Credit Card Card Verification Value: (cvv)")
        retval = [x,y,z]
        if check_valid_card(retval):
            x = input("Invalid Card Information, Type x to cancel, Press ENTER to redo ")
            if x == "x":
                return
            else:
                continue      
        return retval

#Verify that the card information is valid. 
def check_valid_card(credit_card):
    x = re.search("\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}", str(credit_card[0]))
    y = re.search("\d{2}[ /]?\d{2}",credit_card[1])
    z = re.search("\d{3}",credit_card[2])

    return (x == None or y == None or z == None)


#Take funds from the card and transfer it to the buissness
def charge_card(p_card, p_price):
    try:
        return True
    except:
        return False
    pass

#Print out all items in the current cart including price
def check_cart(p_cart):
    print("Current Cart:")
    for i in p_cart.current_cart:
        display_item(i)
    print("Total Cost: " + float(p_cart.get_total_price()))

#Display one individual item.
def display_item(p_item):
    print(p_item)

#Put information into the fulfilled orders csv. 
def create_delivery_status(p_cost, item_list):
    x = random.randint(1,50000)
    file = open(fulfilled_orders_path, 'a')
    file.write("\n"+str(x)+","+str(p_cost)+","+ str(item_list).replace(",",".")+",No,No," + str(current_login[0]))
    file.close()
    return x

#Check a given order_id for its current status and print it out. 
def check_delivery_status(order_id):
    file = open(fulfilled_orders_path, 'r')
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
                    populate_cart()
                    if row[4] == "restaruant":
                        populate_owner_view()
                    return "Login success!"
                else:
                    return "Password is invalid."
    if user_found == False:
        return "User does not exist. Please double check credentials or register as a new user"


#display all resturants on the screen and select one to show its menu. 
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

#Create a secondary window to display the menu. 
def display_menu(store, menu):
    root2 = ThemedTk(theme ="equilux")
    root2.title(store)
    root2.geometry("325x325")
    for i in menu:
        create_menu_button(root2, i)

    root2.mainloop()

#Create a button for each item to "Add to cart"
def create_menu_button(root2,i):
    ttk.Button(root2, text = i,command = lambda: add_to_cart(i)).pack()





def create_restaurant():
    '''
    Checks csv file if there is a restaurant already made by this user.
    If the user hasn't already made a restaurant, user is asked for input on restaurant details.
    Adds this information to the csv file.
    '''
    with open(restaurants_csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            if row[5] == current_login[0]:
                print("Error: A user may only have one restaurant at a time.")
                return
    file.close()

    print("Please input the following: Restaurant Name, Address, Description, and Direct Deposit Info.")
    name = str(input("Name:"))
    addr = str(input("Address:"))
    desc = str(input("Description:"))
    dd = int(input("Direct Deposit Info:"))
    postal = str(input("Postal Code (First 3 Characters):"))


    with open(restaurants_csv_path, 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([name,addr,desc,dd,postal,current_login[0]])
    file.close()
    print("Restaurant successfully created.")

def delete_restaurant():
    '''
    Checks csv file to see if user owns a restaurant.
    If user does, their restaurant is removed from the csv file.

    '''
    newfile = []
    found = False
    with open(restaurants_csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[5] == current_login[0]:
                print("Found row to be deleted")
                found = True
            else:
                newfile.append(row)
    if not found:
        print("No restaurant to delete.")
        return
    with open(restaurants_csv_path, 'w', newline='\n') as file:
        writer = csv.writer(file)
        for line in newfile:
            writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5]])
    file.close()
    print("Restaurant successfully deleted.")

def edit_restaurant():
    '''
    Checks csv file to see if user owns a restaurant.
    If user does, they are prompted on which attribute they want to change,
    and what they want to change it to.
    '''
    print("Which attribute would you like to change?\n1. Name\n2. Address\n3. Description\n4. Direct Deposit")
    x = int(input("Input the menu number(1-4) you would like."))
    y = input("What would you like to replace it with?")
    if x == 4:
        y = int(y)
    x -= 1
    newfile = []
    found = False
    with open(menu_csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[5] == current_login[0]:
                found = True
                if x == 0:
                    newfile.append([y,row[1],row[2],row[3],row[4]])
                elif x == 1:
                    newfile.append([row[0],y,row[2],row[3],row[4]])
                elif x == 2:
                    newfile.append([row[0],row[1],y,row[3],row[4]])
                else:
                    newfile.append([row[0],row[1],row[2],y,row[4]])
            else:
                newfile.append(row)
    if not found:
        print("Restaurant not found")
        return
    with open(restaurants_csv_path, 'w', newline='\n') as file:
        writer = csv.writer(file)
        for line in newfile:
            writer.writerow([line[0],line[1],line[2],line[3],line[4]])
    file.close()
    print("Restaurant successfully edited.")
    

def add_item():
    '''
    Checks csv file to see if user owns a restaurant.
    If user does, they are prompted on the attributes of the item they wish to add.
    The new item is then created, and added to the csv file.
    '''
    found = False
    with open(restaurants_csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[5] == current_login[0]:
                restaurant_name = row[0]
                found = True
                break
    file.close()
    if not found:
        print("Error, cannot add items to a menu if you do not own a restaurant.")
        return

    print("Please input the following: Item Name, Price in Dollars, Category, Description, and whether it is in stock or not.")
    name = str(input("Name:"))
    price = float(input("Price:"))
    category = str(input("Category:"))
    desc = str(input("Description:"))
    instock = int(input("How Many Do You Have In Stock:"))

    
    with open(menu_csv_path, 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([restaurant_name,name,price,category,desc,instock,])
    file.close()
    print("Item successfully created.")
 
def remove_item():
    '''
    Checks csv file to see if user owns a restaurant.
    Asks user what item they want to delete.
    Checks csv file to see if the item exists, if it does it is removed.
    '''
    todelete = str(input("Enter the name of the item you wish to delete:"))
    found = False
    with open(restaurants_csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[5] == current_login[0]:
                restaurant_name = row[0]
                found = True
                break
    file.close()
    if not found:
        print("Error, cannot remove items from a menu if you do not own a restaurant.")
        return

    found = False
    newfile = []
    with open(menu_csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == restaurant_name and row[1] == todelete:
                found = True
            else:
                newfile.append([row[0],row[1],row[2],row[3],row[4],row[5]])
    file.close()
    if found:
        print("Item successfully deleted.")
    else:
        print("Could not find item.")
    with open(menu_csv_path, 'w', newline='\n') as file:
        writer = csv.writer(file)
        for line in newfile:
            writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5]])
    file.close()
    
def edit_item():
    '''
    Checks csv file to see if user owns a restaurant.
    If user does, they are prompted on the attribute of the item they wish to change.
    Checks csv file to see if the item they wish to edit exists. If it does, the selected attribute is changed.
    '''
    toedit = str(input("Enter the name of the item you wish to edit:"))
    found = False
    with open(restaurants_csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[5] == current_login[0]:
                restaurant_name = row[0]
                found = True
                break
    file.close()
    if not found:
        print("Error, cannot edit items from a menu if you do not own a restaurant.")
        return

    print("Which attribute would you like to change?\n1. Name\n2. Price\n3. Category\n4. Description\n5. Quantity")
    x = int(input("Input the menu number(1-5) you would like."))
    if x == 5:
        y = input("What would you like to replace it with?")
        if y == 'y':
            y = 'Y'
        if y == 'n':
            y = 'N'
        if y == 'Y':
            y = True
        else:
            y = False
    elif x == 2:
        y = float(input("Price:"))
    else:
        y = input("What would you like to replace it with?") 
    
    x -= 1
    found = False
    newfile = []
    with open(menu_csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0],restaurant_name)
            print(row[1],toedit)
            if row[0] == restaurant_name and row[1] == toedit:
                found = True
                if x == 0:
                    newfile.append([row[0],y,row[2],row[3],row[4],row[5]])
                elif x == 1:
                    newfile.append([row[0],row[1],y,row[3],row[4],row[5]])
                elif x == 2:
                    newfile.append([row[0],row[1],row[2],y,row[4],row[5]])
                elif x == 3:
                    newfile.append([row[0],row[1],row[2],row[3],y,row[5]])
                else:
                    newfile.append([row[0],row[1],row[2],row[3],row[4],y])
            else:
                newfile.append(row)
    file.close()
    if found:
        print("Item successfully edited.")
    else:
        print("Could not find item.")
        return
    with open(menu_csv_path, 'w', newline='\n') as file:
        writer = csv.writer(file)
        for line in newfile:
            writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5]])
    file.close()

create_GUI()