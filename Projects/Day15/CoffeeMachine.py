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

def is_resource_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item} ")
            return False
    return True

def process_coins():
    """Returns the total Calculated from coins inserted"""
    print("Please insert Coins")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.01
    return total


def Is_transaction_successfull(money_received, cost_of_drink):
    """Returns True when payment is successfull and False if money is insufficient"""
    if money_received >= cost_of_drink:
        change =  round(money_received - cost_of_drink, 2)
        print(f"Here is your change {change}")
        global profit
        profit += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money is refunded")
        return False
    
def make_Coffee(drink_name, order_ingredients):
    """Deducts the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

is_on = True

while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            user_payment = process_coins()
            if Is_transaction_successfull(user_payment, drink["cost"]):
                make_Coffee(user_choice, drink["ingredients"])






