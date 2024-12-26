import turtle
from turtle import Turtle

NW = list(range(90, 180))
NE = list(range(0, 90))
SW = list(range(180, 270))
SE = list(range(270, 360))


class Bricks(Turtle):
    def __init__(self):
        super().__init__()

        self.all_bricks = []
        # Bounce against brick means the ball entering both the following ranges:
        # loc = 'brick location'
        # X --> -20+xloc <= xloc <= 20+xloc
        # and
        # Y --> -10+yloc <= yloc <= 10+yloc

        # 1st round: 10 rows between position Y=250 and Y=110.
        colors = ['gray', 'red', 'blue', 'orange', 'cyan', 'yellow', 'lightgreen']
        first_round_colors = dict(zip(range(250, 110, -20), colors))

        self.bricks_lowest_point = 110
        self.bricks_highest_point = 250

        for x_range in range(-390, 391, 60):
            for y_range in range(self.bricks_highest_point, self.bricks_lowest_point, -20):
                some_turtle = Turtle()
                some_turtle.penup()
                some_turtle.shape('square')
                some_turtle.color(first_round_colors.get(y_range))
                some_turtle.shapesize(1, 2.9, 1)
                some_turtle.goto(x_range, y_range)
                self.all_bricks.append(some_turtle)

    def check_hit_brick(self, ball_x, ball_y, ball_head_):

        def kill_turtle(brick_):
            brick.clear()
            brick.hideturtle()
            self.all_bricks.pop(self.all_bricks.index(brick_))

        if self.bricks_lowest_point - 20 < ball_y < self.bricks_highest_point + 20:
            for brick in self.all_bricks:
                if (brick.xcor() - 32 < ball_x < brick.xcor() + 32 and
                brick.ycor() - 12 < ball_y < brick.ycor() + 12):
                    kill_turtle(brick)
                    if ball_head_ in NW:
                        if ball_y > brick.ycor() - 6:
                            return True, 'my_ball.hit_west()'
                        else:
                            return True, 'my_ball.hit_north()'
                    elif ball_head_ in NE:
                        if ball_y > brick.ycor() - 6:
                            return True, 'my_ball.hit_east()'
                        else:
                            return True, 'my_ball.hit_north()'
                    elif ball_head_ in SW:
                        if ball_y < brick.ycor() + 6:
                            return True, 'my_ball.hit_west()'
                        else:
                            return True, 'my_ball.hit_south()'
                    elif ball_head_ in SE:
                        if ball_y < brick.ycor() + 6:
                            return True, 'my_ball.hit_east()'
                        else:
                            return True, 'my_ball.hit_south()'
            return False, False
        else:
            return False, False

    def check_victory(self):
        if len(self.all_bricks) == 0:
            return True

    def kill_bricks(self):
        for item in self.all_bricks:
            item.clear()
            item.hideturtle()
