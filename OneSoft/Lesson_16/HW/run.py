from turtle import Screen, Turtle
from screeninfo import get_monitors
from typing import List, Callable
from random import choice, uniform
import math

from solar_system.classes.planet import PlanetData, Planet, Asteroid


WIDTH = get_monitors().pop().width
HEIGHT = get_monitors().pop().height - 50


def make_window():
    """Make window of Solar system"""
    screen = Screen()
    screen.bgcolor('black')
    screen.title('Solar system')
    screen.setup(WIDTH, HEIGHT)
    screen.cv._rootwindow.resizable(False, False)
    screen.onkey(screen.bye, 'Escape')
    screen.listen()
    screen.tracer(0)
    return screen


def make_base_planet():
    """Make base planet"""
    base_planet = Turtle(shape='circle')
    base_planet.color('yellow')
    base_planet.shapesize(5.0, 5.0)
    return base_planet


def make_solar_planets_data():
    """Planets data"""
    earth_data = PlanetData((1.0, 1.0), 'blue', 150, 0.001)
    moon_data = PlanetData((0.5, 0.5), 'gray', 25, 0.005)
    saturn_data = PlanetData((2.0, 2.0), 'orange', 200, 0.0005, 'saturn')
    mars_data = PlanetData((0.8, 0.8), 'red', 300, 0.0007)
    phobos_data = PlanetData((0.3, 0.3), 'lime', 40, 0.007)
    deimos_data = PlanetData((0.2, 0.2), 'white', 25, 0.008)
    planets_data = {
        'earth': earth_data,
        'moon': moon_data,
        'saturn': saturn_data,
        'mars': mars_data,
        'phobos': phobos_data,
        'deimos': deimos_data
    }
    return planets_data


def make_asteroids(central_planet: Turtle, count: int = 200):
    asteroids = []
    for _ in range(count):
        color = choice(['blue', 'red', 'yellow', 'orange'])
        size = choice([(0.1, 0.1), (0.15, 0.15), (0.2, 0.2)])
        radius = choice([1150, 1170, 1190, 1210])
        initial_angle = uniform(0, 2 * math.pi)
        asteroid_data = PlanetData(size, color, radius, 0.002)
        asteroid = Asteroid(asteroid_data, central_planet, initial_angle)
        asteroids.append(asteroid)
    return asteroids


def make_solar_planets(base_planet: Turtle):
    """Make planets of solar system"""
    sun = base_planet
    asteroids = make_asteroids(sun)
    planets_data = make_solar_planets_data()
    earth = Planet(planets_data['earth'], sun)
    moon = Planet(planets_data['moon'], earth)
    saturn = Planet(planets_data['saturn'], sun)
    mars = Planet(planets_data['mars'], sun)
    phobos = Planet(planets_data['phobos'], mars)
    deimos = Planet(planets_data['deimos'], mars)
    planets = [earth, moon, saturn, mars, phobos, deimos]
    planets += asteroids
    return planets


def make_belt_around_planet():
    """Make asteroid belt around planet"""
    belt = Turtle()
    belt.hideturtle()
    belt.up()
    belt.width(5)
    belt.color('white')
    return belt


def move_starts(stars: List[Planet], belt: Turtle):
    """Move stars"""
    for star in stars:
        if star.name != 'planet':
            belt.goto(star.xcor(), star.ycor() - 50)
            belt.circle(50)
            belt.down()
        star.move()


def mainloop(make_system_planets: Callable, make_central_planet: Callable):
    """Mainloop of solar system"""
    window = make_window()
    base_planet = make_central_planet()
    planets = make_system_planets(base_planet)
    belt = make_belt_around_planet()
    while True:
        belt.clear()
        move_starts(planets, belt)
        window.update()


if __name__ == '__main__':
    mainloop(make_solar_planets, make_base_planet)
