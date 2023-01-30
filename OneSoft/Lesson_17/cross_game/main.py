from time import sleep


from OneSoft.Lesson_17.cross_game.game_lib.labels.pause import PauseLabel
from OneSoft.Lesson_17.cross_game.game_lib.sprites.player import Player
from OneSoft.Lesson_17.cross_game.game_lib.windows.main_window import Window
from OneSoft.Lesson_17.cross_game.managers.car_manager import CarManager
from OneSoft.Lesson_17.cross_game.game_lib.windows.scoreboard import Scoreboard


class Game:
    pause = False

    def __init__(self):
        self.window = Window()
        self.player_1 = Player((-100, - 280))
        self.player_2 = Player((100, -280))
        self.scoreboard = Scoreboard()
        self.car_manager = CarManager()
        self.pause_label = PauseLabel()

        self.window.canvas.onkeypress(self.player_1.move, 'w')
        self.window.canvas.onkeypress(self.player_2.move, 'Up')
        self.window.canvas.onkeypress(self.set_pause, 'p')

    def run(self):
        game_is_on = True

        while game_is_on:
            sleep(0.05)
            self.window.canvas.update()

            self.car_manager.make_car()
            self.car_manager.move()

            for car in self.car_manager.all_cars:
                if self.player_1.distance(car) < 20 or self.player_2.distance(car) < 20:
                    game_is_on = False

            if self.player_1.is_at_finish_line() or self.player_2.is_at_finish_line():
                self.player_1.restart()
                self.car_manager.increase_speed()

            elif self.player_2.is_at_finish_line():
                self.player_2.restart()
                self.car_manager.increase_speed()

            elif self.player_1.ycor() > 230:
                self.scoreboard.increase_1()
                self.player_1.restart()

            elif self.player_2.ycor() > 230:
                self.scoreboard.increase_2()
                self.player_2.restart()

    def set_pause(self):
        if self.pause:
            self.pause = False
            self.player_1.pause = False
            self.player_2.pause = False
            self.car_manager.pause = False
            self.pause_label.clear()
        else:
            self.pause = True
            self.player_1.pause = True
            self.player_2.pause = True
            self.car_manager.pause = True
            self.pause_label.update_pause()


if __name__ == '__main__':
    game = Game()
    game.run()
