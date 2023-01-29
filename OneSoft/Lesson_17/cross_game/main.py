from time import sleep

from cross_game.game_lib.labels.pause import PauseLabel
from cross_game.game_lib.sprites.player import Player
from cross_game.game_lib.windows.main_window import Window
from cross_game.managers.car_manager import CarManager


class Game:
    pause = False

    def __init__(self):
        self.window = Window()
        self.player = Player()
        self.car_manager = CarManager()
        self.pause_label = PauseLabel()

        self.window.canvas.onkeypress(self.player.move, 'Up')
        self.window.canvas.onkeypress(self.set_pause, 'p')

    def run(self):
        game_is_on = True

        while game_is_on:
            sleep(0.05)
            self.window.canvas.update()

            self.car_manager.make_car()
            self.car_manager.move()

            for car in self.car_manager.all_cars:
                if self.player.distance(car) < 20:
                    game_is_on = False

            if self.player.is_at_finish_line():
                self.player.go_to_start()
                self.car_manager.increase_speed()

    def set_pause(self):
        if self.pause:
            self.pause = False
            self.player.pause = False
            self.car_manager.pause = False
            self.pause_label.clear()
        else:
            self.pause = True
            self.player.pause = True
            self.car_manager.pause = True
            self.pause_label.update_pause()


if __name__ == '__main__':
    game = Game()
    game.run()
