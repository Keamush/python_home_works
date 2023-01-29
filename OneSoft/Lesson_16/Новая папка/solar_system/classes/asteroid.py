from random import random
from math import sin, cos

from solar_system.dto.planet_data import PlanetData
from solar_system.classes.planet import Planet


class Asteroid(Planet):
    start_angle = 0.001
    increase_start_angle = 0.012421

    def __init__(self, star, radius):
        asteroid_data = PlanetData((0.1, 0.1), self.generate_color(), radius, self.increase_start_angle)
        super().__init__(asteroid_data, star)
        self.angle += self.start_angle
        Asteroid.start_angle += self.increase_start_angle

    def move(self):
        """Move asteroids"""
        self.x = self.radius * cos(self.angle) * 2
        self.y = self.radius * sin(self.angle)
        self.goto(self.star.xcor() + self.x, self.star.ycor() + self.y)
        self.angle += self.increase_angle

    @staticmethod
    def generate_color():
        return random(), random(), random()


