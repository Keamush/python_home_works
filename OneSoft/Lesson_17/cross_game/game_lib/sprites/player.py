from OneSoft.Lesson_17.cross_game.game_lib.sprites.base_sprite import Sprite
from OneSoft.Lesson_17.cross_game.game_lib.settings.game_settings import (
    PLAYER_START_POSITION,
    PLAYER_MOVE_DISTANCE,
    FINISH_LINE
)


class Player(Sprite):
    def __init__(self, position):
        super().__init__(shape_name='turtle')
        self.pause = False
        self.setheading(90)
        self.color('salmon')
        self.player_position = position
        self.goto(self.player_position)
        self.showturtle()

    # def go_to_start(self):
    #     self.goto(PLAYER_START_POSITION)

    def move(self):
        if not self.pause:
            self.forward(PLAYER_MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        return False

    def restart(self):
        self.goto(self.player_position)
