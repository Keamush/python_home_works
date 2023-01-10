import turtle
from turtle import Screen, Pen
from random import randint, random, choice
from typing import List, Union

WIDTH = 800
HEIGHT = 400


def move_player(direction: str):
    """Move player with arrows"""
    if direction == 'up' and player.ycor() <= HEIGHT // 2 - player.radius - player.speed:
        player.setheading(90)
        player.forward(player.speed)
    elif direction == 'down' and player.ycor() >= -HEIGHT // 2 + player.radius + player.speed:
        player.setheading(270)
        player.forward(player.speed)
    elif direction == 'left' and player.xcor() >= -WIDTH // 2 + player.radius + player.speed:
        player.setheading(180)
        player.forward(player.speed)
    elif direction == 'right' and player.xcor() <= WIDTH // 2 - player.radius - player.speed:
        player.setheading(0)
        player.forward(player.speed)


def make_window():
    """Make main window"""
    screen = Screen()
    screen.title('Move ball')
    screen.bgcolor('black')
    screen.setup(WIDTH, HEIGHT)
    screen.onkey(screen.bye, 'Escape')
    screen.onkeypress(lambda: move_player('up'), 'Up')
    screen.onkeypress(lambda: move_player('down'), 'Down')
    screen.onkeypress(lambda: move_player('left'), 'Left')
    screen.onkeypress(lambda: move_player('right'), 'Right')
    screen.listen()
    screen.tracer(0)
    return screen


def random_color():
    """Generate random color RGB"""
    return random(), random(), random()


def make_ball(speed: Union[float, int] = 0.05, shapesize: Union[float, int] = 0.5):
    """Make ball object"""
    directions = -1, 1
    pen = Pen()
    pen.hideturtle()
    pen.up()
    pen.delta_x = speed * choice(directions)
    pen.delta_y = speed * choice(directions)
    pen.radius = 20 * shapesize // 2
    pen.shape('circle')
    pen.color(random_color())
    pen.shapesize(shapesize, shapesize)
    pen.setx(randint(-WIDTH // 2 + pen.radius, WIDTH // 2 - pen.radius))
    pen.sety(randint(-HEIGHT // 2 + pen.radius, HEIGHT // 2 - pen.radius))
    pen.showturtle()
    return pen


def make_player(shapesize: Union[float, int] = 2.0):
    """Make player object"""
    pen = Pen()
    pen.up()
    pen.speed = 2
    pen.radius = 20 * shapesize // 2
    pen.shape('square')
    pen.color('white')
    pen.shapesize(shapesize, shapesize)
    pen.showturtle()
    return pen


def make_pen(size: int = 5):
    """Make pen object"""
    pen = Pen()
    pen.width(size)
    pen.up()
    return pen


def make_barrier(shapesize: Union[float, int] = 5.0):
    barrier = Pen()
    barrier.penup()
    barrier.hideturtle()
    barrier.speed(0)
    barrier.shape('square')
    barrier.color('red')
    barrier.shapesize(shapesize, shapesize)
    barrier.goto(50, 0)
    barrier.showturtle()
    barrier.forward(150)
    barrier.penup()
    print(barrier.pos())
    return barrier

def move_ball(ball: Pen):
    """Move ball"""
    x = ball.xcor()
    y = ball.ycor()
    ball.setpos(x + ball.delta_x, y + ball.delta_y)


def check_border(ball: Pen):
    """Check border and change direction"""
    if ball.xcor() > WIDTH // 2 - ball.radius or ball.xcor() < -WIDTH // 2 + ball.radius:
        ball.delta_x *= -1

    if ball.ycor() > HEIGHT // 2 - ball.radius or ball.ycor() < -HEIGHT // 2 + ball.radius:
        ball.delta_y *= -1


def check_barrier(ball: Pen):
    """Check barrier diapason and change direction"""
    if ball.xcor() >= 50 - ball.radius and ball.xcor() <= 200 + ball.radius:
        ball.delta_x *= -1

    if ball.ycor() >= 0 - ball.radius or ball.ycor() <= 150 + ball.radius:
        ball.delta_y *= -1


def balls_collisions(balls: List[Pen]):
    """Check if balls collision"""
    for i in range(len(balls)):
        # if balls[i].distance(inner_border) < balls[i].radius + inner_border.radius:
        #     balls[i].delta_x *= -1
        #     balls[i].delta_y *= -1
        for j in range(i + 1, len(balls)):
            if balls[i].distance(balls[j]) < balls[i].radius + balls[j].radius:
                balls[i].delta_x, balls[j].delta_x = balls[j].delta_x, balls[i].delta_x
                balls[i].delta_y, balls[j].delta_y = balls[j].delta_y, balls[i].delta_y



window = make_window()
ball_sizes = [0.5, 0.7, 1.0, 1.2]
balls = [make_ball(shapesize=choice(ball_sizes)) for _ in range(25)]
player = make_player()
barrier_one = make_barrier()



while True:
    for ball in balls:
        check_border(ball)
        check_barrier(ball)
        move_ball(ball)
    balls_collisions(balls)
    window.update()

