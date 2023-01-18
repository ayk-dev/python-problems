from turtle import Turtle, Screen
from random import randint


scr = Screen()
scr.setup(width=500, height=400)


def create_race_turtles(list_of_colors):
    trtls = []
    for i in range(len(list_of_colors)):
        t = Turtle(shape='turtle')
        t.color(list_of_colors[i])
        t.penup()
        x_pos = -(scr.window_width() // 2 - 10)
        y_pos = -(scr.window_height() // 2 - scr.window_height() * 0.2) + i * (scr.window_height() // 8)
        t.goto(x=x_pos, y=y_pos)
        trtls.append(t)
    return trtls


colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple']

user_input = scr.textinput(title='Place your bet', prompt='Which turtle will win the race? Enter a color: ')

turtles = create_race_turtles(colors)
is_race_over = False
winner = None

while not is_race_over:
    for t in turtles:
        if t.xcor() == scr.window_width() // 2:
            winner = t.fillcolor()
            is_race_over = True
        t.forward(randint(0, 10))

if winner == user_input.lower():
    print(f'You win! Winner is {user_input}')
else:
    print(f'You lose. Winner is {winner}')

scr.exitonclick()