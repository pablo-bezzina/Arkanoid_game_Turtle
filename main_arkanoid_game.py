from turtle import Screen
from arkanoid_frame import Frame
from arkanoid_bricks import Bricks
from arkanoid_pad import Pad
from arkanoid_ball import Ball
from arkanoid_misc import Misc
import tkinter
from tkinter import messagebox
import time

my_screen = Screen()
my_screen.tracer(0)

my_tkinter = tkinter.Tk()
my_tkinter.withdraw()

my_frame = Frame()
my_bricks = Bricks()
my_pad = Pad()
my_ball = Ball()

my_screen.title("My Arkanoid Game")
X = 1000
Y = 1000
my_screen.setup(width=X, height=Y)
my_screen.bgcolor("black")
my_screen.listen()

go_again = True
game_on = True

my_misc = Misc()
my_screen.update()

answer = messagebox.askyesno('Welcome!', "Please press 'yes' to start game.")
if not answer:
    my_screen.bye()


while go_again:
    time.sleep(1)
    counter = 0
    while game_on:
        counter += 1
        my_screen.tracer(0)
        my_ball.go_on()

        my_screen.onkeypress(key="4", fun=my_pad.go_left)
        my_screen.onkeypress(key="6", fun=my_pad.go_right)

        my_ball.check_impact_frame()

        ballx, bally = my_ball.ball_location()
        ball_heading = int(my_ball.ball_heading())

        is_pad_hit, is_edge_hit, is_left_hit = my_pad.check_hit_pad(ballx, bally)
        if is_pad_hit:
            my_ball.toggle_edge_hit(is_edge_hit)
            my_ball.hit_south(is_left_hit)

        is_brick_hit, bounce_where = my_bricks.check_hit_brick(ballx, bally, ball_heading)
        if is_brick_hit:
            eval(bounce_where)

        if counter == 10:
            my_screen.update()
            counter = 0

        missed_ball = my_ball.check_miss()
        if missed_ball:
            my_pad.kill_pad()
            my_ball.kill_ball()
            if my_misc.one_life_less():
                my_pad = Pad()
                my_ball = Ball()
                my_screen.update()
                time.sleep(3)
                continue
            else:
                answer = messagebox.askyesno('GAME OVER', "You run out of lives. Do you want to play again?")
                if not answer:
                    go_again = False
                    game_on = False
                    break
                else:
                    my_bricks.kill_bricks()
                    my_bricks = Bricks()
                    my_pad = Pad()
                    my_ball = Ball()
                    my_misc.kill_misc()
                    my_misc = Misc()
                    break

        victory = my_bricks.check_victory()
        if victory:
            answer = messagebox.askyesno('Congratulations!', "You completed the level. Do you want to go again?.")
            if not answer:
                go_again = False
                game_on = False
                break
            else:
                my_bricks.kill_bricks()
                my_bricks = Bricks()
                my_pad = Pad()
                my_ball = Ball()
                my_misc.kill_misc()
                my_misc = Misc()
                break
