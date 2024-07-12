# logo = '''
#
#  ▄████▄   ▒█████    █████▒ █████▒▓█████ ▓█████     ███▄ ▄███▓ ▄▄▄       ██ ▄█▀▓█████  ██▀███
# ▒██▀ ▀█  ▒██▒  ██▒▓██   ▒▓██   ▒ ▓█   ▀ ▓█   ▀    ▓██▒▀█▀ ██▒▒████▄     ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
# ▒▓█    ▄ ▒██░  ██▒▒████ ░▒████ ░ ▒███   ▒███      ▓██    ▓██░▒██  ▀█▄  ▓███▄░ ▒███   ▓██ ░▄█ ▒
# ▒▓▓▄ ▄██▒▒██   ██░░▓█▒  ░░▓█▒  ░ ▒▓█  ▄ ▒▓█  ▄    ▒██    ▒██ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄
# ▒ ▓███▀ ░░ ████▓▒░░▒█░   ░▒█░    ░▒████▒░▒████▒   ▒██▒   ░██▒ ▓█   ▓██▒▒██▒ █▄░▒████▒░██▓ ▒██▒
# ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒ ░    ▒ ░    ░░ ▒░ ░░░ ▒░ ░   ░ ▒░   ░  ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
#   ░  ▒     ░ ▒ ▒░  ░      ░       ░ ░  ░ ░ ░  ░   ░  ░      ░  ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
# ░        ░ ░ ░ ▒   ░ ░    ░ ░       ░      ░      ░      ░     ░   ▒   ░ ░░ ░    ░     ░░   ░
# ░ ░          ░ ░                    ░  ░   ░  ░          ░         ░  ░░  ░      ░  ░   ░
# ░
#
# '''

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


# TODO 1: Checking the resources for the coffee machine ☕

def price():
    print("Please insert coins.")
    quarters = int(input("how many quarters?:")) * 0.25
    dimes = int(input("how many dimes?:")) * 0.1
    nickles = int(input("how many nickles?:")) * 0.05
    pennies = int(input("how many pennies?:")) * 0.01
    total = (quarters + dimes + nickles + pennies)
    return total


def is_transaction_successful(money_received, total_cost):
    if money_received >= total_cost:
        change = round(money_received - total_cost, 2)
        print(f"Here is your ${change} in change.")
        global profit
        profit += total_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def is_ingredients_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is no {item}")
            return False
    return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy")


is_on = True

while is_on:
    # print(logo)
    order = input("What would you like? (expresso/latte/cappuccino):")

    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffee = {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[order]
        if is_ingredients_sufficient(drink["ingredients"]):
            payment = price()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])
