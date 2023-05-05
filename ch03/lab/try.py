import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))


circle_center = (200,200)
circle_radius = 200

screen.fill("orange")

circle = pygame.draw.circle(screen, "blue", circle_center, circle_radius, 0)
border = pygame.draw.circle(screen, "black", circle_center, circle_radius, 5)
pygame.display.flip()

for i in range(10):
    dart_pos = (random.randint(0, 400), random.randint(0, 400))
    # distance formula to determine if the dart landed in the circle
    if (dart_pos[0] - circle_center[0]) ** 2 + (dart_pos[1] - circle_center[1]) ** 2 <= circle_radius ** 2:
        pygame.draw.circle(screen, "green", dart_pos, 10)
        pygame.time.wait(2000)
        pygame.display.update()
    else:
        pygame.draw.circle(screen, "red", dart_pos, 10)
        pygame.time.wait(2000)
        pygame.display.update()
    
run = True 
while run: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()

