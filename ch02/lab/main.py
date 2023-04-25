import turtle
import random 
import pygame
import math 


#Part A

window = turtle.Screen() 
window.bgcolor("yellow")

timmy = turtle.Turtle()
jimmy = turtle.Turtle()
timmy.color("blue")
jimmy.color("red")
timmy.shape("turtle")
jimmy.shape("turtle") 
timmy.speed(0)
jimmy.speed(0)

# Race 1 
jimmy.up()
timmy.up()
jimmy.goto(-100,20)
timmy.goto(-100,-20)

jimdistance = random.randrange(0, 101) # 0 is 1, 100 is 101 bc they are indexed at 0 
timdistance = random.randrange(0,101)
jimmy.forward(jimdistance)
timmy.forward(timdistance)

jimmy.goto(-100,20)
timmy.goto(-100,-20)

# window.exitonclick()
# Race 2

moveamount = random.randrange(1,11) 
for i in range(10):
    jimmy.forward(moveamount)
    timmy.forward(moveamount) 

jimmy.goto(-100,20)
timmy.goto (-100,-20)
window.exitonclick()

# Part B 

pygame.init()
window = pygame.display.set_mode()

points = []
side_length = 120 
xpos = 400 
ypos = 400 
num_sides = [3, 4, 6, 20, 100, 360]

for side in num_sides: 
    window.fill("green") 
    pygame.display.flip()
    pygame.time.wait(3000)
    for i in range(side):
        angle = 360 / side
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x, y])
    pygame.display.flip()
    pygame.draw.polygon( window, "orange", points)
    pygame.display.flip()
    pygame.time.wait(2000)
    points = [] 

