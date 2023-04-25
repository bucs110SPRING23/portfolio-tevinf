import random 
import math 
import pygame
pygame.init()

print("Green Dot Means Hit, Red Dot Means Miss")
screen = pygame.display.set_mode()

dimensions = screen.get_size()
#print(dim)

starting_point = [dimensions[0] // 2, dimensions[1] // 2] 
pygame.draw.circle(screen, "blue", starting_point, 250)
pygame.draw.circle(screen,"purple", starting_point, 230)
pygame.display.flip()
pygame.time.wait(30000)
#pygame.display.get_init()

color = ["green", "red"]
#hitspot = [randrange(0, dimensions[0]//2), randrange(0,dimensions[1]//2)]
distance_from_center = math.hypot(x1-x2, y2-y1) 
is_in_circle = distance_from_center <= dimensions[0] // 2

for _ in range(10):
    hitspot = [random.randrange(0, dimensions[0]//2), random.randrange(0,dimensions[1]//2)]
    dart = pygame.draw.circle(screen, color, hitspot, 50)
    pygame.display.flip()
    pygame.time.wait(3000)
    if dart == hitspot:
        color = "green"
    else:
        color = "red" 

