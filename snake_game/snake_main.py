from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)

snake = Snake()
food = Food()
board = Scoreboard()

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

    # Detect if the snake has collected food
    if snake.head.distance(food) < 15:
        board.update_score()
        snake.extend()
        food.refresh()

    # Detect if the snake hits a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        board.game_over()

    # Detect if the snake collides it itself
    for seg in snake.snake_segments:
        if snake.head == seg:
            continue
        if snake.head.distance(seg) < 10:
            game_on = False
            board.game_over()


scr.exitonclick()