from tkinter import messagebox
from turtle import Screen, Pen
from random import randint, random, choice
from typing import List, Union

WIDTH = 1000
HEIGHT = 800
WIDTH_HALF = WIDTH // 2
HEIGHT_HALF = HEIGHT // 2


def move_player(direction: str):
    """Move player with arrows"""
    if direction == 'up' and player.ycor() <= HEIGHT_HALF - player.radius - player.speed:
        player.setheading(90)
        player.forward(player.speed)
    elif direction == 'down' and player.ycor() >= -HEIGHT_HALF + player.radius + player.speed:
        player.setheading(270)
        player.forward(player.speed)
    elif direction == 'left' and player.xcor() >= -WIDTH_HALF + player.radius + player.speed:
        player.setheading(180)
        player.forward(player.speed)
    elif direction == 'right' and player.xcor() <= WIDTH_HALF - player.radius - player.speed:
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
    pen.setx(randint(-WIDTH_HALF + pen.radius, WIDTH_HALF - pen.radius))
    pen.sety(randint(-HEIGHT_HALF + pen.radius, HEIGHT_HALF - pen.radius))
    pen.showturtle()
    return pen


def make_player(shapesize: Union[float, int] = 2.0):
    """Make player object"""
    pen = Pen()
    pen.up()
    pen.speed = 5
    pen.radius = 20 * shapesize // 2
    pen.shape('square')
    pen.color('white')
    pen.shapesize(shapesize, shapesize)
    pen.showturtle()
    return pen


def make_score():
    """Make pen to draw score"""
    pen = Pen()
    pen.hideturtle()
    pen.speed(0)
    pen.up()
    pen.color('white')
    pen.setpos((-WIDTH_HALF + 60, HEIGHT_HALF - 40))
    return pen


def draw_score(score: Pen, balls_qty: int):
    """Draw balls left to win"""
    score.clear()
    score.write(f'Balls: {balls_qty}', align='center', font=('Arial', 16, 'bold'))


def check_win(balls_qty: int):
    """Check if player win"""
    if balls_qty <= 0:
        messagebox.showinfo("Winner", "You win in this hard game!")
        window.bye()


def move_ball(ball: Pen):
    """Move ball"""
    x = ball.xcor()
    y = ball.ycor()
    ball.setpos(x + ball.delta_x, y + ball.delta_y)


def check_border(ball: Pen):
    """Check border and chance direction"""
    if ball.xcor() > WIDTH_HALF - ball.radius or ball.xcor() < -WIDTH_HALF + ball.radius:
        ball.delta_x *= -1

    if ball.ycor() > HEIGHT_HALF - ball.radius or ball.ycor() < -HEIGHT_HALF + ball.radius:
        ball.delta_y *= -1


def balls_collisions(balls: List[Pen]):
    """Check if balls collision"""
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if balls[i].distance(balls[j]) < balls[i].radius + balls[j].radius:
                balls[i].delta_x, balls[j].delta_x = balls[j].delta_x, balls[i].delta_x
                balls[i].delta_y, balls[j].delta_y = balls[j].delta_y, balls[i].delta_y


def collect_balls(balls: List[Pen]):
    """Check player and ball collision"""
    for ball in balls:
        if player.distance(ball) < ball.radius + player.radius:
            ball.hideturtle()
            draw_score(score, len(balls) - 1)
    balls = [ball for ball in balls if ball.isvisible()]
    return balls


window = make_window()
ball_sizes = [0.5, 0.7, 1.0, 1.2]
balls = [make_ball(shapesize=choice(ball_sizes)) for _ in range(10)]
player = make_player()

score = make_score()
score.write(f'Balls: {len(balls)}', align='center', font=('Arial', 16, 'bold'))

while True:
    for ball in balls:
        check_border(ball)
        move_ball(ball)
    balls_collisions(balls)
    balls = collect_balls(balls)
    window.update()
    check_win(len(balls))
