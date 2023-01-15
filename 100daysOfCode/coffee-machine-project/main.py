def report(resrcs, money):
    result = f'Water: {resrcs["water"]}ml\n'
    result += f'Milk: {resrcs["milk"]}ml\n'
    result += f'Coffee: {resrcs["coffee"]}gr\n'
    result += f'Money: ${money}'
    return result


def resources_insufficient(choice, menu, resrcs):
    for ingr in menu[choice]["ingredients"]:
        # print(f'ingr {ingr}')
        # print(f'menu[choice]["ingredients"] {menu[choice]["ingredients"]}')
        # print(f'menu[choice]["ingredients"][ingr] {menu[choice]["ingredients"][ingr]}')
        # print(resrcs[ingr])
        if menu[choice]["ingredients"][ingr] >= resrcs[ingr]:
            return ingr
    return False


def process_money(qs, ds, ns, ps, menu, choice):
    """If inserted money by user is enough, returns change,
    else return None if money is refunded. If successful, money is increased."""
    inserted_money = (qs * 25 + ds * 10 + ns * 5 + ps * 1) / 100
    if inserted_money >= menu[choice]["cost"]:
        return inserted_money
    return None


def update_resources(choice, menu, resrcs):
    for ingr in menu[choice]["ingredients"]:
        resrcs[ingr] -= menu[choice]["ingredients"][ingr]


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

money = 0

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == 'report':
        print(report(resources, money))
        continue

    if user_input == 'off':
        break

    if resources_insufficient(user_input, MENU, resources):
        print(f'Sorry, there is not enough {resources_insufficient(user_input, MENU, resources)}')
        continue

    print(f'Price for {user_input} is ${MENU[user_input]["cost"]}')
    print('Please insert coins.')
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickels = int(input("How many nickels?:"))
    pennies = int(input("How many pennies?:"))

    inserted_money = process_money(quarters, dimes, nickels, pennies, MENU, user_input)
    if inserted_money is None:
        print('Sorry, that\'s not enough money. Money refunded.')
        continue
    change = inserted_money - MENU[user_input]["cost"]
    print(f'Here is ${change} in change.')

    money += inserted_money - change

    update_resources(user_input, MENU, resources)
    print(f'Here is your {user_input}. Enjoy!')








