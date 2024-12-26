import turtle
from turtle import Turtle


class Misc:

    def __init__(self):

        self.lives = 3

        self.my_text = Turtle()
        self.my_text.goto(0, 435)
        self.my_text.hideturtle()
        self.my_text.penup()
        self.my_text.color('white')
        self.my_text.write(arg=f'Lives left: {self.lives}',
                   align='center',
                   font=('Fixedsys', 42, 'normal'))

    def one_life_less(self):
        if self.lives == 1:
            return False
        else:
            self.lives -= 1
            self.my_text.clear()
            self.my_text.write(arg=f'Lives left: {self.lives}',
                               align='center',
                               font=('Fixedsys', 42, 'normal'))
            return True

    def kill_misc(self):
        self.my_text.clear()
        self.my_text.hideturtle()
