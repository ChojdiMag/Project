from art import logo
MENU = {
    "virgin": {
        "ingredients" : {
            "sparkling_water" : 100,
            "juice_mint": 50,
            "ice": 10,
        },
        "cost": 2,
    },
    "normal":{
        "ingredients":{
            "sparkling_water" : 75,
            "juice_mint": 25,
            "ice": 10,
            "rum" : 50,
        },
        "cost":3,
    },
    "strong":{
        "ingredients":{
            "sparkling_water": 10,
            "juice_mint": 5,
            "ice":10,
            "rum":100,
        },
        "cost":5,
    }
}
profit = 0
resource = {
    "sparkling_water" : 500,
    "juice_mint" : 200,
    "ice": 1000,
    "rum": 1500,
}


def fine_resource(order_ingredients):
    """" Return true when order can be made"""
    for item in order_ingredients:
        if order_ingredients[item] > resource[item]:
            print(f"Sorry you can't drink, ther is not enough {item}.")
            return False
    return True

def payment():
    """Returns total results from the coins inserted"""
    print("Insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def successful_payment (money_received, drink_cost):
    """Return True when payment is accepted"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print ("Sorry that's not enough money")
        return False

def make_mojito(drink_name, order_ingredients):
    for item in order_ingredients:
        resource[item]-= order_ingredients[item]
    print(f"Here is you {drink_name}. Taste it good. Enjoy!")
    print(logo)

is_on = True

while is_on:
    choice = input("What would you like? (wirgin/normal/strong)?")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"sparkling_water: {resource['sparkling_water']} oz")
        print(f"juice_mint : {resource['juice_mint']} oz")
        print(f"ice:{resource['ice']} oz")
        print (f"rum:{resource['rum']}oz")
        print (f"Money:${profit}")
    else:
        drink = MENU[choice]
        if fine_resource(drink["ingredients"]):
            payment = payment()
        if successful_payment(payment, drink["cost"]):
            make_mojito(choice, drink["ingredients"])

