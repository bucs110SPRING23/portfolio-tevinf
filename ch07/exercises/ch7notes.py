# a class is a blueprint for an object 
# values of data change and not part of an algorithm, it's the type of the data that's important 
# def function(), class X(TitleCase) ex. class ColorPoint:
# classes are the same as type 
#classes go into their own file with files named according to the class 

#class Point: 
    #"""docstring for Point"""

    #def __init__(self):
        #self.xcoor = 0 
        #self.ycoor = 0 
        #self.color = "red"

## new python file ##

# 1. looks in current folder in file / module 
# 2. looks in python installed modules (pip) 
# 3. looks in python library 

## CASES ##

#snake_case = underscores for spaces, all lowercase 
#camelCase = capital for spaces, starts lowercase 
#TitleCase = capital for spaces, starts capital 

import point 
import random 
import turtle 
import pygame 

pygame.init()
display = pygame.display.set_mode()

points = []
x = random.randint(0,250)
y = random.randint(0,250)
p = point.LED (x, y)
p1 = point.LED(x = 100, y = 100) 
pygame.draw.circle(display, p1.color, (p1.rect.x, p1.rect.y), p1.radius)
while True:
    pygame.display.flip()

#print(p1.xcoor, p1.ycoor, p1.color, type(p1), id(p1))
#p2 = point.Point(3, 4, "yellow")
#print(p2.xcoor, p2.ycoor, p2.color, type(p2), id(p2))

#points = []
#for p in range(10): 
    #x = random.randint(0, 255) 
    #y = random.randint(0,255)
    #points.append(point.Point(x,y))

#t = turtle.Turtle()
#for p in points: 
    #p.random_color()
    #t.color(p.color)
    #t.goto(p.xcoor, p.ycoor)

#turtle.Screen().exitonclick()

### MVC- Model View Controller ### 
# for GUI programs 
# like accumulator pattern 
# design patterns - language independent 

# view: displays things on screen (typically libraries, but they can be written too)
#       - pygame 
#       - turtle 
# controller: controls things on screen 
#       -keyboard 
# model: a class and contains data for the program 
#       - model is about how the class is used 