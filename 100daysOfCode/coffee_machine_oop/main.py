from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def print_report(cm: CoffeeMaker, mm: MoneyMachine):
    cm.report()
    mm.report()


machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ").lower()

    if user_input == 'report':
        print_report(machine, money_machine)
        continue

    if user_input == 'off':
        break

    drink = menu.find_drink(user_input)
    if drink:
        if machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            machine.make_coffee(drink)




