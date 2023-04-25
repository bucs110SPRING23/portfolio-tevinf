import pygame
import random 
import math 

pygame.init()

# Dart Board
screen = pygame.display.set_mode()
dimensions = screen.get_size() 
center = (dimensions [0] // 2, dimensions [1] // 2)

pygame.draw.circle(screen, "pink", center, 300)
pygame.display.flip()


for i in range(10):

    xcor1 = random.randrange(dimensions[0]//2 - 300, dimensions[0]//2 + 300)
    ycor1 = random.randrange(dimensions [1]//2 - 300, dimensions [1]//2 + 300)
    xcor2 = random.randrange(dimensions[0]//2 - 300, dimensions[0]//2 + 300)
    ycor2 = random.randrange(dimensions [1]//2 - 300, dimensions [1]//2 + 300)
    player1 = pygame.draw.circle(screen, "red", (xcor1, ycor1), 10)
    player2 = pygame.draw.circle(screen, "blue", (xcor2, ycor2), 10)
    darts = (player1, player2)
    p1points = [0]
    p2points = [0]
    for player1 in darts:
        pygame.draw.circle(screen, "red", (xcor1, ycor1), 10)
        pygame.display.flip()
        pygame.time.wait(500)
        if 496 < xcor1 < 996 and 200 < ycor1 < 780: #from screen size
            p1points.append(1)
            print("player 1 good shot")
        else:
            print("player 1 missed")
    for player2 in darts: 
        pygame.draw.circle(screen, "blue", (xcor2, ycor2), 10)
        pygame.display.flip()
        pygame.time.wait(500)
        if 496 < xcor2 < 996 and 200 < ycor2 < 780:
            p2points.append(1)
            print("player 2 good shot")
        else: 
            print("player 2 missed")
if len(p1points) > len(p2points):
    message = "Red Player 1 Wins!"
elif len(p1points) == len(p2points):
    message = "TIE!" 
else:
    message = "Blue Player 2 Wins!"

import pygame
pygame.init()
font = pygame.font.Font(None, 48) 
text = font.render(message, True, "white") 
screen.blit(text, (300,300))
pygame.display.flip()
pygame.time.wait (5000)


while True:
    pygame.draw.rect(screen,"red",[100,200,100,200])
    pygame.draw.rect(screen, "blue", [200, 300, 100, 200])
    redbutton = pygame.draw.rect(screen,"red",[100,200,100,200])
    bluebutton = pygame.draw.rect(screen, "blue", [200, 300, 100, 200])
    if pygame.MOUSEBUTTONDOWN(redbutton) and len(p1points) > len(p2points):
        print("you won the bet")
    else:
        print("you lost") 
