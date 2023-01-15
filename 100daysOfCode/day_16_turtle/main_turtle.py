# from turtle import Turtle, Screen
#
# bob = Turtle()
# print(bob)
#
# bob.shape("turtle")
# bob.color("green")
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
#
# print(bob.position())
# bob.forward(100)
# print(bob.position())
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirl", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)