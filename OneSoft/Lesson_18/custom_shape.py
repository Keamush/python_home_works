import turtle

# turtle object
dimond_turtle = turtle.Turtle()

# the coordinates
# of each corner
shape =((0, 0), (10, 10), (20, 0), (10, -10))

# registering the new shape
turtle.register_shape('diamond', shape)

# changing the shape to 'diamond'
dimond_turtle.shape('diamond')
turtle.mainloop()
