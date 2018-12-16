import sys 
import pygame 
from settings import Settings
from ship import Ship
import game_ability 

#thanks to...
#shout out MR.COZORT for the ideas and code
#kids can code
#pythonroom
#stackoverflow  especially the people who helped me on the questions board
#the spaceship playlist on youtube with many creators contributing!!!!!!


'''
Notes-

problems->  Only runs well sometimes(????). Every library that I made had a problem where it wouldnt import the function to the code saying
it was not a member. This problem was fixed my me restarting my computer but I had to do it everytime I ran the game in order for it to work. 
Also the ship cannot move up and down, only left and right.

Future-> I didnt have enought time to make the enemies which is what I would like to do as my next step. I think I took on too big
of a task and so I spent too much time focusing on the ship and its movement instead of the rest of the game. Also I would work on the aesthetic 
parts of the game because right now it looks ugly becuase my main focus was the code.

Positive-> I learned a lot and I now feel comfortable coding. I feel that with a bit more time I could have finished this project.
Compared to my knowledge at the beginning of the semester, I have learned so much and am eager to finish my project.

Starting-> If I could do it again, I would have done a project that was much more manageable in the time I had to complete it.
I also would have found ways to write less code while still doing the same thing.
'''


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Sad Boi Alien Game") 
    #creating the object
    ship = Ship(screen)
  
    #background color
    bg_color = ( 200, 200, 200)
    screen.fill(bg_color)
   
#this is my first attempt at making a spaceship (failed)
    # class spaceship:
    #     def __init__(self):
    #         self.image = pygame.Surface((30, 40))
    #         self.image.fill(WHITE)
    #         self.rect = self.image.get_rect()
    #         self.rect.center = (WIDTH / 12, HEIGHT /12)
    #         self.vx = 0
    #         self.vy = 0
    #         self.falling = False

    #game loop
    while True: 
        game_ability.check_events(ship)
        ship.update()
        game_ability.check_events()
        game_ability.update_screen(ai_settings, screen, ship)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #keys being pressed and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

    
run_game()