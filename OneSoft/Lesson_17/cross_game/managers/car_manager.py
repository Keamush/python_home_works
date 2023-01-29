import random

from cross_game.game_lib.sprites.car import Car
from cross_game.game_lib.settings.game_settings import CAR_COLORS, SCREEN_HEIGHT, SCREEN_WIDTH


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.pause = False

    def make_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Car()
            new_car.color(random.choice(CAR_COLORS))
            random_y = random.randint(-SCREEN_HEIGHT // 2 + 50, SCREEN_HEIGHT // 2 - 50)
            new_car.goto(SCREEN_WIDTH // 2 + 10, random_y)

            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            if not self.pause:
                car.move()

            if car.xcor() < -SCREEN_WIDTH // 2 - 50:
                car.hideturtle()

    @staticmethod
    def increase_speed():
        Car.move_increment += 1

