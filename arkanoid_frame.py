import turtle
from turtle import Turtle

WEST_WALL = -430
NORTH_WALL = 430
EAST_WALL = 430


class Frame(Turtle):
    def __init__(self):
        super().__init__()

        # sides of the frame to be drawn:
        # Bounce against frame means the ball exceeding:
            # X < -430
            # X > 430
            # Y > 430

        # 1. Left Side
        for y_range in range(-480, 431, 20):
            some_turtle = Turtle()
            some_turtle.penup()
            some_turtle.shape('square')
            some_turtle.color('white')
            some_turtle.goto(WEST_WALL, y_range)

        # 2. Top Side
        for x_range in range(-430, 431, 20):
            some_turtle = Turtle()
            some_turtle.penup()
            some_turtle.shape('square')
            some_turtle.color('white')
            some_turtle.goto(x_range, NORTH_WALL)

        # 3. Right Side
        for y_range in range(430, -481, -20):
            some_turtle = Turtle()
            some_turtle.penup()
            some_turtle.shape('square')
            some_turtle.color('white')
            some_turtle.goto(EAST_WALL, y_range)
