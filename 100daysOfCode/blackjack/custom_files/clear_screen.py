import os
from time import sleep


# This is not working as expected
def clear():
    sleep(1)
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
