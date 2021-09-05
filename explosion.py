import pygame

class Explosion():
    def __init__(self,screen,alien):
        self.screen=screen
        self.alien=alien
        
        #self.alien_rect=self.alien.get_rect()

        self.image=pygame.image.load("Images/explosion.bmp")
        self.rect=self.image.get_rect()

        self.rect.x=self.alien.rect.x
        self.rect.y=self.alien.rect.y
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)

        
