def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }


def calculate(op, n1, n2):
    return operations[op](n1, n2)


def calculator():
    n1 = float(input("What's the first number?: "))
    for oper in operations:
        print(oper)
    should_continue = True

    while should_continue:
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))

        if operation == '/' and n2 == 0:
            print("Cannot divide by zero")
            continue

        result = calculate(operation, n1, n2)
        print(f'{n1} {operation} {n2} = {result}')

        question = input(f'Would you like to continue calculating with {result}? Type y or n: ')
        if question == 'n':
            should_continue = False
            calculator()
        else:
            n1 = result


calculator()





