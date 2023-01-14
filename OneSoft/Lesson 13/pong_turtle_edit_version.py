from turtle import Pen, Screen
from time import sleep
from random import choice

WIDTH = 1000
HEIGHT = 800
WIDTH_HALF = WIDTH // 2
HEIGHT_HALF = HEIGHT // 2


def make_window():
    """Make main window"""
    screen = Screen()
    screen.title('Ping pong')
    screen.bgcolor('black')
    screen.setup(WIDTH, HEIGHT)
    screen.onkey(screen.bye, 'Escape')
    screen.onkeypress(lambda: move_paddle(paddle_user, 'up'), 'w')
    screen.onkeypress(lambda: move_paddle(paddle_user, 'down'), 's')
    screen.onkeypress(lambda: move_paddle(paddle_computer, 'up'), 'Up')
    screen.onkeypress(lambda: move_paddle(paddle_computer, 'down'), 'Down')
    screen.listen()
    screen.tracer(0)
    return screen


def make_paddle(start_x: int):
    """Make paddle settings"""
    paddle = Pen()
    paddle.shape('square')
    paddle.shapesize(5.0, 1.0)
    paddle.color('white')
    paddle.up()
    paddle.setpos((start_x, 0))
    paddle.width = 100
    paddle.height = 20
    return paddle


def move_paddle(paddle: Pen, direction: str, speed: int = 10):
    """Move paddle"""
    y = paddle.ycor()
    if direction == 'up' and y < HEIGHT_HALF - paddle.width // 2:
        paddle.sety(y + speed)
    elif direction == 'down' and y > -HEIGHT_HALF + paddle.width // 2:
        paddle.sety(y - speed)


def make_ball():
    """Make ball"""
    pen = Pen()
    pen.shape('circle')
    pen.up()
    pen.color('white')
    pen.size = 20
    pen.delta_x = 0.1
    pen.delta_y = 0.1
    pen.delta_x *= choice(directions)
    pen.delta_y *= choice(directions)
    return pen


def move_ball():
    x = ball.xcor()
    y = ball.ycor()
    ball.setpos(x + ball.delta_x, y + ball.delta_y)


def reset_ball():
    """Reset ball position and sleep for one second"""
    ball.hideturtle()
    ball.setpos((0, 0))
    ball.showturtle()
    window.update()
    sleep(1)
    ball.delta_x *= choice(directions)
    ball.delta_y *= choice(directions)


def check_border():
    global score_user, score_computer
    x = ball.xcor()
    y = ball.ycor()
    if y > HEIGHT_HALF - ball.size // 2 or y < -HEIGHT_HALF + ball.size // 2:
        ball.delta_y *= -1

    if x > WIDTH_HALF + ball.size or x < -WIDTH_HALF - ball.size:
        if x < 0:
            score_computer += 1
            print(f'Computer win, computer_score: {score_computer}')
        else:
            score_user += 1
            print(f'Player win, player_score: {score_user}')
        reset_ball()


def check_ball_paddle_collision():
    """Check for ball and paddles collision"""
    if (WIDTH_HALF - 50 - paddle_computer.height < ball.xcor() < WIDTH_HALF - 40 - paddle_computer.height) and \
            (paddle_computer.ycor() + paddle_computer.width // 2 > ball.ycor() > paddle_computer.ycor() - paddle_computer.width // 2):
        ball.setx(WIDTH_HALF - 50 - paddle_computer.height)
        ball.delta_x *= -1
    elif (-WIDTH_HALF + 50 + paddle_user.height > ball.xcor() > -WIDTH_HALF + 40 + paddle_user.height) and \
            (paddle_user.ycor() + paddle_user.width // 2 > ball.ycor() >paddle_user.ycor() - paddle_user.width // 2):
        ball.setx(-WIDTH_HALF + 50 + paddle_user.height)
        ball.delta_x *= -1


window = make_window()

paddle_user = make_paddle(-WIDTH_HALF + 50)
paddle_computer = make_paddle(WIDTH_HALF - 50)

score_user = 0
score_computer = 0
directions = [-1, 1]
ball = make_ball()

while True:
    move_ball()
    check_border()
    check_ball_paddle_collision()
    window.update()
