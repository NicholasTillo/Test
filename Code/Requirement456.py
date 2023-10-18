import re 
import random

nextID = 10

class cart():
    def __init__(self) -> None:
        self.current_cart= []

    def get_total_price(self):
        total_cost = 0
        for i in self.current_cart:
            total_cost += i.cost
        print(total_cost)
        


usr_cart = cart()


def add_to_cart(item):
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

def create_delivery_status(p_cost, item_list):
    x = random.randint(1,50000)
    file = open("Code/Fulfilled _Orders.csv", 'a')
    file.write("\n"+str(x)+","+str(p_cost)+","+ str(item_list)+",No,No")
    file.close()
    return x

def check_delivery_status(order_id):
    file = open("Code/Fulfilled _Orders.csv", 'r')
    for i in file:
        split = i.split(",")
        if split[0] == str(order_id):
            print(split)
    file.close()
    pass

