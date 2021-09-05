import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,seti,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.seti=seti
        
        #load alien image and treat it as rectangular object
        self.image=pygame.image.load("Images/alien.bmp")
        self.rect=self.image.get_rect()

        #start each new alien at the top left of the screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height+20

        self.x=float(self.rect.x)
        self.y=float(self.rect.y)

    def blitme(self):
        #draw the alien in the screen
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        self.x+=(self.seti.alien_speed_factor*self.seti.fleet_direction)
        self.rect.x=self.x

    def check_edges(self):
        #Return True if alien is at the edge of screen
        self.screen_rect=self.screen.get_rect()
        if self.rect.right>=self.screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True


        
        
