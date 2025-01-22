from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

def coffeePrompt():
    prompt = input(f"What would you like? ({menu.get_items()}): ")
    if prompt == "report":
        coffeeMaker.report()
        moneyMachine.report()
        return coffeePrompt()
    elif prompt == "off":
        return "off"
    elif not menu.find_drink(prompt):
        return coffeePrompt()
    else:
        return menu.find_drink(prompt)


machineIsOn = True
while machineIsOn:
    coffee = coffeePrompt()
    if coffee == "off":
        machineIsOn = False
        break
    # TODO 2: Check wether there are enough resources to make coffee
    if coffeeMaker.is_resource_sufficient(coffee):
        # TODO 3: If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
        if moneyMachine.make_payment(coffee.cost):
            # TODO 4: Update resources and give coffee to customer before serving next customer.
            coffeeMaker.make_coffee(coffee)