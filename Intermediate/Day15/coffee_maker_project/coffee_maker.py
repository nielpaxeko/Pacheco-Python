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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Ask user to select a coffee, they may also enter off to turn off machine or report to view remaining resources
def coffeePrompt():
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if prompt == "report":
        for resource, amount in resources.items():
            print(f"{resource}: {amount}")
        return coffeePrompt()
    elif (
        prompt != "espresso"
        and prompt != "latte"
        and prompt != "cappuccino"
        and prompt != "off"
    ):
        print("Please enter a valid type of coffee!")
        return coffeePrompt()
    else:
        return prompt

# Check if remaining resources are enough to make coffee
def checkResources(coffee):
    sufficientResources = True
    ingredients = MENU[coffee]["ingredients"]
    for ingredient, amount in ingredients.items():
        if resources[ingredient] < amount:
            print(f"Not enough {ingredient} to make {coffee}")
            sufficientResources = False
    return sufficientResources

# Ask user to pay for coffee and check wether enough money has been inserted to finish transaction
def transaction():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many quarters?: "))
    nickels = int(input("How many quarters?: "))
    pennies = int(input("How many quarters?: "))
    coffeeCost = MENU[coffee]["cost"]
    insertedMoney = (
        (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    )
    print(f"The price of the coffe is {round(coffeeCost, 2)} dollars.")
    print(f"You have inserted {insertedMoney} dollars.")
    change = insertedMoney - coffeeCost
    if coffeeCost > insertedMoney:
        print("You don't have enough money! Your money has been refunded.")
        return False
    else:
        print(f"Here's your change: {round(change, 2)}")
        return True


def updateResources(coffee):
    ingredients = MENU[coffee]["ingredients"]
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount
    resources["money"] += MENU[coffee]["cost"]


machineIsOn = True
while machineIsOn:
    # TODO 1: Get coffee
    coffee = coffeePrompt()
    if coffee == "off":
        machineIsOn = False
        break
    # TODO 2: Check wether there are enough resources to make coffee
    if checkResources(coffee):
        # TODO 3: If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
        if transaction():
            # TODO 4: Update resources and give coffee to customer before serving next customer.
            updateResources(coffee)
            print(f"Here's your {coffee} ☕ Enjoy!")
