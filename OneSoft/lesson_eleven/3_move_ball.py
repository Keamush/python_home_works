from turtle import Screen, Pen


WIDTH = 800
HEIGHT = 600


def make_window():
    """Make main window"""
    screen = Screen()
    screen.title('Move ball')
    screen.bgcolor('black')
    screen.setup(WIDTH, HEIGHT)
    screen.onkey(screen.bye, 'Escape')
    screen.listen()
    return screen


def make_ball(speed: int = 1, color='red'):
    """Make ball object"""
    pen = Pen()
    pen.up()
    pen.delta_x = speed
    pen.delta_y = speed
    pen.radius = 50
    pen.shape('circle')
    pen.color(color)
    pen.shapesize(5, 5)
    return pen


def move_ball(ball: Pen):
    """Move ball"""
    x = ball.xcor()
    y = ball.ycor()
    ball.setpos(x + ball.delta_x, y + ball.delta_y)


def check_border(ball: Pen):
    """Check border and chance direction"""
    if ball.xcor() > WIDTH // 2 - ball.radius or ball.xcor() < -WIDTH // 2 + ball.radius:
        ball.delta_x *= -1

    if ball.ycor() > HEIGHT // 2 - ball.radius or ball.ycor() < -HEIGHT // 2 + ball.radius:
        ball.delta_y *= -1


window = make_window()
red_ball = make_ball(2)
blue_ball = make_ball(3, color='blue')

while True:
    check_border(red_ball)
    check_border(blue_ball)
    move_ball(red_ball)
    move_ball(blue_ball)

print('hello')
