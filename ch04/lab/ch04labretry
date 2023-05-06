import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))

def guess():
    screen.fill("orange")
    player1button = pygame.draw.rect(screen, "green", [100, 200, 80, 80])
    player2button = pygame.draw.rect(screen, "black", [100, 290, 80, 80])
    pygame.display.update()
    pygame.time.wait(5000)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_rect = pygame.draw.rect(screen, (0,0,0), [10, 10, mouse_x, mouse_y])

    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if player1button.colliderect(mouse_rect) == True: 
                guess = "Player_1"
            elif player2button.colliderect(mouse_rect) == True: 
                guess = "Player_2"

def main():
    guess()

    circle_center = (200,200)
    circle_radius = 200

    screen.fill("orange")

    circle = pygame.draw.circle(screen, "blue", circle_center, circle_radius, 0)
    border = pygame.draw.circle(screen, "black", circle_center, circle_radius, 5)
    pygame.display.flip()

    player1points = []
    player2points = []

    for i in range(10):

        ## PLAYER 1 DART ##

        dart_pos1 = (random.randint(0, 400), random.randint(0, 400))
        # distance formula to determine if the dart landed in the circle
        if (dart_pos1[0] - circle_center[0]) ** 2 + (dart_pos1[1] - circle_center[1]) ** 2 <= circle_radius ** 2:
            player1points.append(1)
            pygame.draw.circle(screen, "green", dart_pos1, 10)
            pygame.time.wait(2000)
            pygame.display.update()

        else:
            pygame.draw.circle(screen, "red", dart_pos1, 10)
            pygame.time.wait(2000)
            pygame.display.update()
        
        ## PLAYER 2 DART ##
        dart_pos2 = (random.randint(0, 400), random.randint(0, 400))
        if (dart_pos2[0] - circle_center[0]) ** 2 + (dart_pos2[1] - circle_center[1]) ** 2 <= circle_radius ** 2:
            player2points.append(1)
            pygame.draw.circle(screen, "white", dart_pos2, 10)
            pygame.time.wait(2000)
            pygame.display.update()

        else:
            pygame.draw.circle(screen, "black", dart_pos2, 10)
            pygame.time.wait(2000)
            pygame.display.update()

    players = ("PLAYER 1", "PLAYER_2") 
    for player in players:
        if len(player1points) > len(player2points):
            screen.fill("green")
            pygame.display.update()
            winner = "PLAYER 1"
            message = "RED/GREEN Player 1 Wins!"
        elif len(player1points) == len(player2points):
            screen.fill("orange")
            pygame.display.update()
            message = "TIE!" 
        else:
            screen.fill("black")
            pygame.display.update()
            winner = "PLAYER_2"
            message = "BLACK/WHITE Blue Player 2 Wins!" 
        if guess == winner: 
            font = pygame.font.Font(None, 24) 
            guess_txt = font.render("YOU GUESSED CORRECTLY", True, "purple") 
            screen.blit(guess_txt, (100,270))
            pygame.display.flip()
            pygame.time.wait (5000)
        elif guess != winner:
            font = pygame.font.Font(None, 24) 
            guess_txt = font.render("YOU GUESSED WRONG", True, "purple") 
            screen.blit(guess_txt, (100,270))
            pygame.display.flip()
            pygame.time.wait (5000)



    font = pygame.font.Font(None, 24) 
    text = font.render(message, True, "white") 
    screen.blit(text, (100, 200))
    pygame.display.flip()
    pygame.time.wait (5000)

main()