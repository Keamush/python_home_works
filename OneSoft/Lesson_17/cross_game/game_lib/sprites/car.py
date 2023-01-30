from OneSoft.Lesson_17.cross_game.game_lib.sprites.base_sprite import Sprite
from OneSoft.Lesson_17.cross_game.game_lib.settings.game_settings import STARTING_MOVE_DISTANCE


class Car(Sprite):
    move_increment = 0

    def __init__(self):
        super().__init__(shape_name='square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.showturtle()

    def move(self):
        self.backward(STARTING_MOVE_DISTANCE + self.move_increment)
