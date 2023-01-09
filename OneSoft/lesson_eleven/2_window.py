from turtle import Screen, Pen
from random import random


def print_hi():
    print('Hi, turtle!')


WIDTH = 800
HEIGHT = 600


def make_window():
    """Make main window"""
    screen = Screen()
    screen.title('Window application')
    screen.setup(WIDTH, HEIGHT)
    screen.onkey(screen.bye, 'Escape')
    screen.onkey(print_hi, 'p')
    screen.listen()
    return screen


def make_pen(size: int = 5):
    """Make pen object"""
    pen = Pen()
    pen.width(size)
    pen.up()
    return pen


def random_color():
    """Generate random RGB color"""
    return random(), random(), random()


def draw_square(turtle, size: int):
    """Draw square"""
    turtle.down()
    for _ in range(4):
        print(turtle.pos())
        color = random_color()
        turtle.color(color)
        turtle.forward(size)
        turtle.left(90)
    turtle.up()


def draw_triangle(turtle: Pen, size: int):
    """Draw triangle"""
    turtle.down()
    for _ in range(3):
        color = random_color()
        turtle.color(color)
        turtle.forward(size)
        turtle.left(120)
    turtle.up()


window = make_window()
turtle_steve = make_pen()
turtle_bob = make_pen()

turtle_steve.forward(50)

turtle_bob.left(180)
turtle_bob.forward(200)

draw_square(turtle_steve, 150)
draw_triangle(turtle_steve, 100)

draw_square(turtle_bob, 250)

window.mainloop()
