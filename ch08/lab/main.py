import pygame
import random

pygame.init()

## SCREEN DIMENSIONS ##

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))

## DARTBOARD SETUP ##

center = (screen_width // 2, screen_height // 2)
radius = 200
screen.fill("blue")
pygame.draw.circle(screen, "orange", center, radius)

## DART ACTIONS ##

dart_x = (random.randint(0, 400))
dart_y = (random.randint(0, 400))
dart_pos = (dart_x, dart_y)
is_inside_circle = (dart_pos[0] - center[0]) ** 2 + (dart_pos[0] - center[1]) ** 2 <= radius ** 2
# this applies the distance formula between the x and y coordinates of the dartboard and the dart
# if the distance <= the radius ^ 2, then the dart point is inside the circle by the distance formula 

## DART THROWING LOOP ##

def dartthrow(): 

    for i in range(10):
        if is_inside_circle == True:
            pygame.draw.circle(screen,"green", dart_pos, 10)
        else:
            pygame.draw.circle(screen,"red", dart_pos, 10)
        pygame.time.wait(2000)
        pygame.display.flip()
    
dartthrow()

