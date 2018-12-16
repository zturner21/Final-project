import pygame
#this is my spaceship library to set the position of the ship and when to draw to ship 
"""I learned a lot of this from the stackoverflow questions page so thanks to the people in the chat for this"""
class Ship():
    
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('_images/spaceship_image.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom 
        self.moving_right = False

#the ship moves 
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
       
       
       
       
def blitme(self):
    self.screen.blit(self.image, self.rect)

