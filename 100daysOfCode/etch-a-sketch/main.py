from turtle import Turtle, Screen


t = Turtle()
scr = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.back(10)


def counter_clockwise():
    t.left(5)
    t.forward(5)


def clockwise():
    t.right(5)
    t.forward(5)


def clear():
    scr.resetscreen()


scr.listen()

scr.onkey(key="w", fun=move_forward)
scr.onkey(key="s", fun=move_backward)
scr.onkey(key="a", fun=counter_clockwise)
scr.onkey(key="d", fun=clockwise)
scr.onkey(key="c", fun=clear)


scr.exitonclick()