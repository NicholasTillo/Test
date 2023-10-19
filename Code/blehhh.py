import csv

user = "placeholder2"

def create_restaurant():
    '''
    Checks csv file if there is a restaurant already made by this user.
    If the user hasn't already made a restaurant, user is asked for input on restaurant details.
    Adds this information to the csv file.
    '''
    with open('restaurants.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == user:
                print("Error: A user may only have one restaurant at a time.")
                return
    file.close()

    print("Please input the following: Restaurant Name, Address, Description, and Direct Deposit Info.")
    name = str(input("Name:"))
    addr = str(input("Address:"))
    desc = str(input("Description:"))
    dd = int(input("Direct Deposit Info:"))

    with open('restaurants.csv', 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([name,addr,desc,dd,user])
    file.close()
    print("Restaurant successfully created.")

def delete_restaurant():
    '''
    Checks csv file to see if user owns a restaurant.
    If user does, their restaurant is removed from the csv file.

    '''
    newfile = []
    found = False
    with open('restaurants.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == user:
                print("Found row to be deleted")
                found = True
            else:
                newfile.append(row)
    if not found:
        print("No restaurant to delete.")
        return
    with open('restaurants.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        for line in newfile:
            writer.writerow([line[0],line[1],line[2],line[3],line[4]])
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
    with open('items.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == user:
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
    with open('restaurants.csv', 'w', newline='\n') as file:
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
    with open('restaurants.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == user:
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
    instock = str(input("Is it in stock? (Input Y or N):"))

    if instock == 'y':
        instock = 'Y'
    elif instock == 'n':
        instock = 'N'
    if instock == 'Y':
        instock = True
    else:
        instock = False
    with open('items.csv', 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([name,price,category,desc,instock,restaurant_name])
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
    with open('restaurants.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == user:
                restaurant_name = row[0]
                found = True
                break
    file.close()
    if not found:
        print("Error, cannot remove items from a menu if you do not own a restaurant.")
        return

    found = False
    newfile = []
    with open('items.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[5] == restaurant_name and row[0] == todelete:
                found = True
            else:
                newfile.append([row[0],row[1],row[2],row[3],row[4],row[5]])
    file.close()
    if found:
        print("Item successfully deleted.")
    else:
        print("Could not find item.")
    with open('items.csv', 'w', newline='\n') as file:
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
    with open('restaurants.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == user:
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
    with open('items.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[5],restaurant_name)
            print(row[0],toedit)
            if row[5] == restaurant_name and row[0] == toedit:
                found = True
                if x == 0:
                    newfile.append([y,row[1],row[2],row[3],row[4],row[5]])
                elif x == 1:
                    newfile.append([row[0],y,row[2],row[3],row[4],row[5]])
                elif x == 2:
                    newfile.append([row[0],row[1],y,row[3],row[4],row[5]])
                elif x == 3:
                    newfile.append([row[0],row[1],row[2],y,row[4],row[5]])
                else:
                    newfile.append([row[0],row[1],row[2],row[3],y,row[5]])
            else:
                newfile.append(row)
    file.close()
    if found:
        print("Item successfully edited.")
    else:
        print("Could not find item.")
        return
    with open('items.csv', 'w', newline='\n') as file:
        writer = csv.writer(file)
        for line in newfile:
            writer.writerow([line[0],line[1],line[2],line[3],line[4],line[5]])
    file.close()


print("What would you like to do?\n1. Create a restaurant\n2. Delete restaurant\n3. Edit resttaurant details\n4. Add item to your restaurant's menu\n5. Remove an item from your restaurant's menu\n6. Edit an item on you restaurant's menu")

x = None
x = int(input("Input the menu number(1-6) you would like."))

if x == 1:
    create_restaurant()
elif x == 2:
    delete_restaurant()
elif x == 3:
    edit_restaurant()
elif x == 4:
    add_item()
elif x == 5:
    remove_item()
elif x == 6:
    edit_item()