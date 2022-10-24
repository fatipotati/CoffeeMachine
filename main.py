MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}

drinks_available = ""
for drink in MENU:
    drinks_available += drink
    drinks_available += ", "
drinks_available = drinks_available[:-2]

while True:
    answer = input(f"What would you like? ({drinks_available}): ")

    if answer == "report":
        print(f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}g
Coffee: {resources["coffee"]}ml
Money: ${resources["money"]}""")

    elif answer in MENU:
        print("Please insert coins.")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickels = int(input("How many nickels?"))
        pennies = int(input("How many pennies?"))

        money_received = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01
        money_needed = MENU[answer]["cost"]

        insufficient_supply = ""
        if resources["water"] >= MENU[answer]["ingredients"]["water"]:
            enough_water = True
        else:
            enough_water = False
            insufficient_supply += "water and "
        if resources["milk"] >= MENU[answer]["ingredients"]["milk"]:
            enough_milk = True
        else:
            enough_milk = False
            insufficient_supply += "milk and "
        if resources["coffee"] >= MENU[answer]["ingredients"]["coffee"]:
            enough_coffee = True
        else:
            enough_coffee = False
            insufficient_supply += "coffee and "
        if insufficient_supply != "":
            insufficient_supply = insufficient_supply[:-5]


        if money_received >= money_needed:
            if enough_milk and enough_coffee and enough_water:
                resources["money"] += MENU[answer]["cost"]
                resources["water"] -= MENU[answer]["ingredients"]["water"]
                resources["milk"] -= MENU[answer]["ingredients"]["milk"]
                resources["coffee"] -= MENU[answer]["ingredients"]["coffee"]

                change = money_received - money_needed
                print(f"Here is {change:.2f} in change.")
                print(f"Here is your {answer}. Enjoy!")
            else:
                print(f"Sorry, there's not enough {insufficient_supply}.")
        else:
            print("Sorry, that's not enough money. Money refunded.")



