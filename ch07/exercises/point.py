import random 
import pygame 


class LED: 
    """docstring for Point"""

    def __init__(self, x = 0, y = 0, color = "red"):
        # self ties the data to the objects scope rather than function scope
        # functions are called methods when they are in a class 
        # the first parameter to any method is self 
        #self.xcoor = x
        #self.ycoor = y
        self.on = True 
        self.rect = pygame.Rect(abs(x), abs(y), 5, 5)
        self.radius = 4
        self.color = color 

    # no return 
    #####

    def random_color(self):
        
        colors = ["green", "red", "yellow", "blue"]
        self.color = random.choice(colors)
        