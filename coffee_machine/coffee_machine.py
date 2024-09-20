import coffee_data
money = 0

def resources_check(order):
    if coffee_data.resources["water"] < coffee_data.MENU[order]["ingredients"]["water"]:
        return "water"
    if order != "espresso":
        if coffee_data.resources["milk"] < coffee_data.MENU[order]["ingredients"]["milk"]:
            return "milk"
    if coffee_data.resources["coffee"] < coffee_data.MENU[order]["ingredients"]["coffee"]:
        return "coffee"
    return ""

def request_money (order):
    print("The price is ${:.2f}".format(coffee_data.MENU[order]["cost"]))
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    change = total - coffee_data.MENU[order]["cost"]
    if change < 0:
        print("Sorry, that's not enough money. Money refunded.")
        return -1
    elif change > 0:
        print("Here is ${:.2f} in change.".format(change))
    print("Thank you for your purchase.")
    return 0
    


def handle_order (order):
    coffee_data.resources["water"] -= coffee_data.MENU[order]["ingredients"]["water"]
    if order != "espresso":
        coffee_data.resources["milk"] -= coffee_data.MENU[order]["ingredients"]["milk"]
    coffee_data.resources["coffee"] -= coffee_data.MENU[order]["ingredients"]["coffee"]
    print(f"Here is your {order}. Enjoy!")
        


while True:
    lacking_resource = ""
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        break
    if order == "report":
        print(f"Water: {coffee_data.resources['water']}ml")
        print(f"Milk: {coffee_data.resources['milk']}ml")
        print(f"Coffee: {coffee_data.resources['coffee']}g")
        print(f"Money: ${"{:.2f}".format(float(money))}")
        continue
    if order != "espresso" and order != "latte" and order != "cappuccino":
        continue
    lacking_resource = resources_check(order)
    if lacking_resource != "":
        print(f"Sorry, there is not enough {lacking_resource}.")
        continue
    if request_money(order) == -1:
        continue
    money += coffee_data.MENU[order]["cost"]
    handle_order(order)