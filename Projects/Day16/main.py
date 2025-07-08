from menu import Menu
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        is_on = False
        
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()   
    else:
        drink = menu.find_drink(choice)
        resources = coffee_maker.is_resource_sufficient(drink)
        if resources == True and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            
        elif resources == False:
            print("Insufficient Resources please come again later")
        