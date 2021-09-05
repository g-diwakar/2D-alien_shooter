import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,seti,screen,rocket):
        super(Bullet,self).__init__()
        self.screen=screen

        self.rect=pygame.Rect(0,0,seti.bullet_width,seti.bullet_height)
        self.rect.centerx=rocket.rect.centerx
        self.rect.top=rocket.rect.top

        self.y=float(self.rect.y)

        self.color=seti.bullet_color
        self.speed_factor=seti.bullet_speed

    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect,4)
        
