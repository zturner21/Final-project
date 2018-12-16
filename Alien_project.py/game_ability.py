import sys
import pygame

def check_events():
    #when a key is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #which key deterines where the ship goes
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                ship.rect.centerx += 1
#I had trouble making the ship go up/down so it just goes left/right
        elif event.type == pygame.KEYUP:
            if event.type == pygame.K_RIGHT:
                ship.moving_right = False

def update_screen(ai.settings, screen, ship):