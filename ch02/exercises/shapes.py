import pygame
pygame.init()
screen = pygame.display.set_mode()

pygame.draw.circle(screen , "green", [500, 100] , 20)
pygame.display.flip()
pygame.time.wait(3000)
pygame.draw.circle(screen, "red", [500, 150], 40)
pygame.display.flip()
pygame.time.wait(3000)
pygame.draw.circle(screen, "orange", [500, 200], 60)
pygame.display.flip()
pygame.time.wait(3000)