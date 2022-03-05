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
    "ingredients": {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        },
    "money": 0
}


def make_drink(drink):
    for res in resources["ingredients"]:
        resources["ingredients"][res] -= MENU[drink]["ingredients"][res]
    print("Here is your drink. Enjoy!\n\n")
    machine_start()


def charge_money(drink):
    quarters = .25 * int(input("Insert number of quarters: "))
    dimes = .1 * int(input("Insert number of dimes: "))
    nickels = .05 * int(input("Insert number of nickels: "))
    pennies = .01 * int(input("Insert number of pennies: "))
    total_coins = quarters + dimes + nickels + pennies

    if total_coins < MENU[drink]["cost"]:
        print("Sorry, that's not enough money. Money refunded.\n\n")
        machine_start()
    elif total_coins > MENU[drink]["cost"]:
        change = total_coins - MENU[drink]["cost"]
        print(f"Here is ${round(change, 2)} as your change.\n")

    print("Preparing your drink...\n")
    resources["money"] += MENU[drink]["cost"]


def check_resources(drink):
    for res in resources["ingredients"]:
        if MENU[drink]["ingredients"][res] > resources["ingredients"][res]:
            print(f"Sorry, not enough {res}.\n\n")
            return machine_start()


def machine_start():
    inp = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if inp == "off":
        exit()
    elif inp == "report":
        print(f"{resources}\n\n")
        machine_start()
    elif inp == "espresso" or "latte" or "cappuccino":
        check_resources(inp)
        charge_money(inp)
        make_drink(inp)
        print(resources)
    else:
        print("Invalid input.\n\n")
        machine_start()


machine_start()
