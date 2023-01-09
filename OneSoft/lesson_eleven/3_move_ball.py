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


def make_red_ball(speed: int = 1):
    """Make ball object"""
    pen = Pen()
    pen.hideturtle()
    pen.up()
    pen.delta_x = speed
    pen.delta_y = speed
    pen.radius = 50
    pen.shape('circle')
    pen.color('red')
    pen.shapesize(5, 5)
    pen.goto(-150, 50)
    pen.showturtle()
    return pen

def make_blue_ball(speed: int = 1):
    """Make ball object"""
    pen = Pen()
    pen.hideturtle()
    pen.up()
    pen.delta_x = speed
    pen.delta_y = speed
    pen.radius = 50
    pen.shape('circle')
    pen.color('blue')
    pen.shapesize(5, 5)
    pen.goto(100, 25)
    pen.showturtle()
    return pen

def make_green_ball(speed: int = 1):
    """Make ball object"""
    pen = Pen()
    pen.hideturtle()
    pen.up()
    pen.delta_x = speed
    pen.delta_y = speed
    pen.radius = 50
    pen.shape('circle')
    pen.color('green')
    pen.shapesize(5, 5)
    pen.goto(-100, -100)
    pen.showturtle()
    return pen

def make_yellow_ball(speed: int = 1):
    """Make ball object"""
    pen = Pen()
    pen.hideturtle()
    pen.up()
    pen.delta_x = speed
    pen.delta_y = speed
    pen.radius = 50
    pen.shape('circle')
    pen.color('yellow')
    pen.shapesize(5, 5)
    pen.goto(200, -50)
    pen.showturtle()
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
red_ball = make_red_ball(7)
blue_ball = make_blue_ball(10)
green_ball = make_green_ball(5)
yellow_ball = make_yellow_ball(4)



while True:
    check_border(red_ball)
    check_border(blue_ball)
    check_border(green_ball)
    check_border(yellow_ball)
    move_ball(red_ball)
    move_ball(blue_ball)
    move_ball(green_ball)
    move_ball(yellow_ball)
