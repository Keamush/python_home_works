from turtle import Turtle
from math import sin, cos

from Lesson_16.solar_system.classes.sprite import Sprite
from Lesson_16.solar_system.dto.planet_data import PlanetData


class Planet(Sprite):
    """Planet class"""
    def __init__(self, planet_data: PlanetData, star: Turtle):
        super().__init__()
        self.name = planet_data.name
        self.shapesize(*planet_data.planet_size)
        self.x = 0
        self.y = 0
        self.color(planet_data.planet_color)
        self.up()
        self.angle = 0
        self.increase_angle = planet_data.increase_angle
        self.radius = planet_data.radius
        self.star = star

    def move(self):
        """Move planet"""
        self.x = self.radius * cos(self.angle)
        self.y = self.radius * sin(self.angle)
        self.goto(self.star.xcor() + self.x, self.star.ycor() + self.y)
        self.angle += self.increase_angle


