import turtle as t

LINE_SIZE = 20

tim = t.Turtle()

tim.pen(fillcolor="black", pencolor="black", pensize=3)

for _ in range(LINE_SIZE):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5)

screen = t.Screen()
screen.exitonclick()

