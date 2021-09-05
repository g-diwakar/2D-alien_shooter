import pygame
from pygame.sprite import Sprite



pygame.init()
class Rocket(Sprite):

    def __init__(self,screen,seti):
        #Initialize the Rocket and its starting position
        super(Rocket,self).__init__()
        self.screen=screen
        self.seti=seti
        

        #Loading the Rocket image
        self.image=pygame.image.load("Images/Rocket.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #start each new Rocket at the bottom of screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #Movement Flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        #Update the Rocket's position
        if self.moving_right:
            if self.rect.centerx==self.seti.screen_width:
                self.rect.centerx=self.seti.screen_width
            else:
                self.rect.centerx+=self.seti.rocket_speed_factor

        if self.moving_left:
            if self.rect.centerx==0:
                self.rect.centerx=0
            else:
                self.rect.centerx-=self.seti.rocket_speed_factor

    def blitme(self):
        #Drawing the sheep at the current location
        self.screen.blit(self.image,self.rect)


    def center_rocket(self):
        self.center=self.screen_rect.centerx
