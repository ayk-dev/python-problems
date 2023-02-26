from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for p in START_POSITIONS:
            snk = Turtle()
            snk.shape("square")
            snk.color("white")
            snk.width(20)
            snk.penup()
            snk.goto(p[0], p[1])
            self.snake_segments.append(snk)

    def move(self):
        for idx in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[idx - 1].xcor()
            new_y = self.snake_segments[idx - 1].ycor()
            self.snake_segments[idx].goto(new_x, new_y)
        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

