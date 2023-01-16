# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 108)
#
# rgb_colors = []
# for c in colors:
#     red = c.rgb[0]
#     green = c.rgb[1]
#     blue = c.rgb[2]
#     rgb_colors.append((red, green, blue))
#
# print(rgb_colors)

import turtle
import random

STEP = 50
NUMBER_OF_DOTS = 10
DOT_SIZE = 20


def draw_a_row(colors_list):
    for _ in range(NUMBER_OF_DOTS):
        t.forward(STEP)
        color = random.choice(colors_list)
        t.dot(DOT_SIZE, color)
        t.penup()


colors_list = [(222, 152, 103), (128, 172, 199), (221, 130, 149), (221, 73, 90), (243, 208, 99), (17, 121, 157), (34, 120, 82), (230, 74, 70), (142, 86, 60), (116, 85, 102), (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75), (213, 222, 213), (1, 98, 119), (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]

t = turtle.Turtle()

turtle.colormode(255)
t.penup()
t.hideturtle()
t.speed("fastest")

x = -300.00
y = -200.00
t.setposition(x, y)

for _ in range(NUMBER_OF_DOTS):
    draw_a_row(colors_list)
    y += STEP
    t.setposition(x, y)

screen = turtle.Screen()
screen.exitonclick()