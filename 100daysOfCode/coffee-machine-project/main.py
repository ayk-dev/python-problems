def report(resrcs, money):
    result = f'Water: {resrcs["water"]}ml\n'
    result += f'Milk: {resrcs["milk"]}ml\n'
    result += f'Coffee: {resrcs["coffee"]}gr\n'
    result += f'Money: ${money}'
    return result


def are_resources_sufficient(choice, menu, resrcs):
    for k, v in resrcs.items():
        pass


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
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_input == 'report':
        print(report(resources, money))
        continue

    if user_input == 'off':
        break


