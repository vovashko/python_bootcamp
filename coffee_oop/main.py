from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
espresso = MenuItem("espresso", 20, 30,30, 2)

maker_of_coffee = CoffeeMaker()
bankroll = MoneyMachine()



while True:
    choice=input(f"Please choose a drink. Options are {coffee_menu.get_items()} ")
    if choice == "off":
        break
    elif choice == "report":
        maker_of_coffee.report()
        bankroll.report()
        continue
    drink = coffee_menu.find_drink(choice)
    if not drink:
        continue
    if maker_of_coffee.is_resource_sufficient(drink) == True:
        if bankroll.make_payment(drink.cost) == True:
            maker_of_coffee.make_coffee(drink)
        
   