from turtle import Turtle, Screen, colormode
from random import randint


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(n):
    for _ in range(360 // n):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + n)


colormode(255)

tim = Turtle()

tim.pendown()
tim.speed("fastest")

to_angle = 5
draw_spirograph(to_angle)

screen = Screen()
screen.exitonclick()