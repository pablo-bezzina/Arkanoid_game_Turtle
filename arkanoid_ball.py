import turtle
from turtle import Turtle
from arkanoid_pad import PAD_Y_LOCATION
from arkanoid_frame import WEST_WALL, NORTH_WALL, EAST_WALL
import random

BALL_STEP = 2
NORTH = list(range(0, 180))
SOUTH = list(range(181, 360))
EAST = list(range(0, 90)) + list(range(270, 360))
WEST = list(range(90, 270))


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        self.ball_turtle = Turtle()
        self.ball_turtle.penup()
        self.ball_turtle.shape('circle')
        self.ball_turtle.color('purple')
        self.ball_turtle.shapesize(0.75, 0.75, 1)
        self.ball_turtle.setheading(random.choice([45, 135]))
        self.ball_turtle.speed(0)
        self.ball_turtle.straight_angle = True
        self.ball_turtle.goto(0, PAD_Y_LOCATION + 15)

        self.delta1 = 90
        self.delta2 = 270
        self.delta3 = None

        self.shift_to_edge_shot = {45: 30, 135: 150, 225: 210, 315: 330}
        self.shift_to_middle_shot = {30: 45, 150: 135, 210: 225, 330: 315}
    
    def go_on(self):
        self.ball_turtle.forward(BALL_STEP)

    def toggle_edge_hit(self, is_edge: bool):
        if self.ball_turtle.straight_angle:
            if is_edge:
                self.ball_turtle.straight_angle = False
                direction = int(self.ball_turtle.heading())
                self.ball_turtle.setheading(self.shift_to_edge_shot.get(direction))
                self.delta1 = 120
                self.delta2 = 300
                self.delta3 = 60
        elif not self.ball_turtle.straight_angle:
            if not is_edge:
                self.ball_turtle.straight_angle = True
                direction = int(self.ball_turtle.heading())
                self.ball_turtle.setheading(self.shift_to_middle_shot.get(direction))
                self.delta1 = 90
                self.delta2 = 270
                self.delta3 = None

    def ball_location(self):
        return self.ball_turtle.xcor(), self.ball_turtle.ycor()

    def ball_heading(self):
        return self.ball_turtle.heading()

    def check_impact_frame(self):
        if (self.ball_turtle.xcor() < WEST_WALL + 60 or self.ball_turtle.xcor() > WEST_WALL - 60 or
                self.ball_turtle.ycor() > NORTH_WALL - 60):
            if self.ball_turtle.xcor() - 10 < WEST_WALL + 10:
                self.hit_west()
            elif self.ball_turtle.xcor() + 10 > EAST_WALL - 10:
                self.hit_east()
            elif self.ball_turtle.ycor() + 10 > NORTH_WALL - 10:
                self.hit_north()

    # "hit_west" meaning the ball is hitting an obstacle west of the ball, hence bouncing off towards the east
    def hit_west(self):
        direction = self.ball_turtle.heading()
        if direction in NORTH:
            self.ball_turtle.setheading(direction - self.delta1)
        else:
            self.ball_turtle.setheading(direction + self.delta1)

    def hit_east(self):
        direction = self.ball_turtle.heading()
        if direction in NORTH:
            self.ball_turtle.setheading(direction + self.delta1)
        else:
            self.ball_turtle.setheading(direction - self.delta1)

    def hit_north(self):
        direction = self.ball_turtle.heading()
        if direction in EAST:
            self.ball_turtle.setheading(direction + self.delta2)
        else:
            if not self.delta3:
                self.ball_turtle.setheading(direction + self.delta1)
            else:
                self.ball_turtle.setheading(direction + self.delta3)

    def hit_south(self, on_the_left=False):
        direction = self.ball_turtle.heading()
        if direction in EAST:
            if on_the_left:
                self.ball_turtle.left(180)
            else:
                self.ball_turtle.setheading(direction - self.delta2)
        else:
            if not on_the_left:
                self.ball_turtle.left(180)
            else:
                if not self.delta3:
                    self.ball_turtle.setheading(direction - self.delta1)
                else:
                    self.ball_turtle.setheading(direction - self.delta3)

    def check_miss(self):
        if self.ball_turtle.ycor() < -500:
            return True
        else:
            return None

    def kill_ball(self):
        self.ball_turtle.clear()
        self.ball_turtle.hideturtle()
