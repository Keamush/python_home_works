import turtle, random
count = 10
s = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
balls = ['bal'+ str(i) for i in range(count)]

window = turtle.Screen()
class Border:
    border = turtle.Turtle()
    border.up()
    border.speed(0)
    border.hideturtle()
    border.pensize(5)
    border.color('red')
    border.goto(250, 250)
    border.down()
    border.goto(250, -250)
    border.goto(-250, -250)
    border.goto(-250, 250)
    border.goto(250, 250)

def randomColors():
    red = random.random()
    green = random.random()
    blue = random.random()
    return red, green, blue
print(randomColors())
class Ball:
    def __init__(self, name, dx, dy, color):
        self.name = name
        self.dx = dx
        self.dy = dy
        self.color = color
        self.name = turtle.Turtle()
        self.name.hideturtle()
        self.name.shape('circle')
        self.name.penup()
        self.randx = random.randint(-240, 240)
        self.randy = random.randint(-240, 240)
        self.name.goto(self.randx, self.randy)
        self.name.showturtle()
        self.name.color(*self.color)

    def moveBall(self):
        x, y = self.name.position()
        if x + self.dx >= 250 - 10 or x + self.dx <= -250 + 10:
            self.dx = -self.dx
        if y + self.dy >= 250 - 10 or y + self.dy <= -250 + 10:
            self.dy = -self.dy
        self.name.goto(x + self.dx, y + self.dy)

Border

for i in range(count):
    balls[i] = Ball(balls[i], random.choice(s), random.choice(s), randomColors())
while True:
    for i in range(count):
        balls[i].moveBall()

window.mainloop()