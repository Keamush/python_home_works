from turtle import Turtle

from Lesson_17.cross_game.game_lib.settings.game_settings import FONT


class PauseLabel(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()

    def update_pause(self):
        self.clear()
        self.color('red')
        self.write(arg='Player set pause', align='center', font=FONT)
