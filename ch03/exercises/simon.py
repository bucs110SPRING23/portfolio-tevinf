import pygame
import random
pygame.init()
screen = pygame.display.set_mode()
colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)

for color in colors:
    screen.fill(color)
    pygame.display.flip()
    pygame.time.wait(1000)

    screen.fill("black")
    pygame.display.flip()
    pygame.time.wait(300)
messages = """"""
    Simon says:
    UP:RED 
    DOWN:BLUE
    LEFT:GREEN
    RIGHT:YELLOW

    click on the window, enter a sequence, then press enter 
""""""

response = input(message)

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN: 
        if event.key == pygame.K_UP:
            print("up")
        elif event.key == pygame.K_DOWN:
            print("down")
        elif event.key == pygame.K_LEFT:
            print("left")
        elif event.key == pygame.K_RIGHT:
            print("right")
usersequence=[]
for