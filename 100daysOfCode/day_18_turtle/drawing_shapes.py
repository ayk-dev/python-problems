import turtle as t
from random import randint

LINE_SIZE = 20
START = 3
END_RANGE = 11
DRAW_LENGTH = 75

tim = t.Turtle()
t.pensize(LINE_SIZE)
t.colormode(255)
t.pendown()

for i in range(START, END_RANGE):
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(i):
        t.forward(DRAW_LENGTH)
        t.right(360 // i)

screen = t.Screen()
screen.exitonclick()