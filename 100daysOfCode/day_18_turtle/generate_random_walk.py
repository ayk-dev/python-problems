from turtle import Turtle, Screen, colormode
from random import randint, choice

LINE_SIZE = 2
START = 0
END_RANGE = randint(1, 100)
DRAW_LENGTH = randint(1, 100)

colormode(255)
directions = [0, 90, 180, 270]

tim = Turtle()
tim.pensize(LINE_SIZE)


tim.pendown()
tim.speed("fast")

for _ in range(END_RANGE):
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))

    tim.forward(randint(1, 25))
    tim.setheading(choice(directions))


screen = Screen()
screen.exitonclick()