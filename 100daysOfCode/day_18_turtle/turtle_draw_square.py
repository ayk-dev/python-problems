from turtle import Turtle, Screen

bobi = Turtle()

bobi.color("green")

bobi.pen(fillcolor="black", pencolor="red", pensize=5)

bobi.pendown()
for _ in range(4):
    bobi.forward(100)
    bobi.right(90)
bobi.penup()

screen = Screen()
screen.exitonclick()