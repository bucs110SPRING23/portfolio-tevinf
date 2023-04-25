import turtle
import random

pen = turtle.Turtle() 
pen.shape("turtle")
pen.speed(0)

distance = 10 
angle = 90
is_in_screen = True

colors = ["red", "orange", "yellow", "green"]

while is_in_screen: 
    coin = random.randrange(0,2)
    if coin:
        turtle.right(angle)
    else:
        turtle.left(angle)
    turtle.forward(distance)

    turtleX = turtle.xcor()
    turtleY = turtle.ycor()

    x_range = wn.window_width() / 2
    y_range = wn.window.width() / 2

    turtle.color(random.choice(colors))
    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        is_in_screen = False 



#print(dimensions)
#center of screen = (896,560)

