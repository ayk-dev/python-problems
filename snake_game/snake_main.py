from turtle import Screen, Turtle
import time
from snake import Snake

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)

snake = Snake()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")

game_on = True
while game_on:
    scr.update()
    time.sleep(0.1)
    snake.move()


scr.exitonclick()