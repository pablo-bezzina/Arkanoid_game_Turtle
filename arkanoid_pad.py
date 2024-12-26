import turtle
from turtle import Turtle
from arkanoid_frame import WEST_WALL, NORTH_WALL, EAST_WALL

MOVE_RANGE = 20
PAD_Y_LOCATION = -380


class Pad(Turtle):
    def __init__(self):
        super().__init__()

        self.pad_units = []

        # Moving pad:
        # Bounce against pad means the ball exceeding:
        # X > pad_units[0].xloc - 5
        # and
        # X < pad_units[len(pad_units)-1].xloc + 5
        # and
        # Y < -370

        for x_range in range(-50, 51, 10):
            some_turtle = Turtle()
            some_turtle.shapesize(1, 0.5, 1)
            some_turtle.penup()
            some_turtle.shape('square')
            some_turtle.color('blue')
            some_turtle.goto(x_range, PAD_Y_LOCATION)
            some_turtle.is_edge = False
            some_turtle.is_left = False
            self.pad_units.append(some_turtle)

        # Giving the pad round shape on the edges, and set attribute "is_left" as True for the left half of the pad.
        for i in range(len(self.pad_units)):
            if i == 0 or i == len(self.pad_units) - 1:
                self.pad_units[i].shape('circle')
                self.pad_units[i].shapesize(1, 1, 1)
                self.pad_units[i].is_edge = True
                if i == 0:
                    self.pad_units[i].is_left = True
            elif i in range(1, 5):
                self.pad_units[i].is_left = True

    def go_left(self):
        if self.pad_units[0].xcor() - 5 - MOVE_RANGE > WEST_WALL + 10:
            for unit in self.pad_units:
                unit.setx(unit.xcor() - MOVE_RANGE)

    def go_right(self):
        if self.pad_units[len(self.pad_units)-1].xcor() + 5 + MOVE_RANGE < EAST_WALL - 10:
            for unit in self.pad_units:
                unit.setx(unit.xcor() + MOVE_RANGE)

    def check_hit_pad(self, ball_x, ball_y):
        if ball_y < -350:
            for piece_of_pad in self.pad_units:
                if (piece_of_pad.xcor() - 5 < ball_x < piece_of_pad.xcor() + 5 and
                piece_of_pad.ycor() - 7 < ball_y < piece_of_pad.ycor() + 10):
                    return True, piece_of_pad.is_edge, piece_of_pad.is_left
            return False, False, False
        else:
            return False, False, False

    def kill_pad(self):
        for item in self.pad_units:
            item.clear()
            item.hideturtle()
