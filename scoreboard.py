import pygame.font
from pygame.sprite import Group

from rocket import Rocket

class Scoreboard():

    def __init__(self,seti,screen,stats):
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.seti=seti
        self.stats=stats

        self.text_color=(30,30,30)
        self.font=pygame.font.Font(None,48)

        self.high_score=0

        self.prep_rockets()


    def prep_score(self): 
        #turn the score into rendered image
        score_str="Score:"+str(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.seti.bg_color)

        #display the score in the screen
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=self.screen_rect.top

    def show_score(self):
        #Draw score to the screen
        self.screen.blit(self.score_image,self.score_rect)

    def update_score(self):
        self.stats.score+=5

    def prep_high_score(self):
        #turn the high score into rendered image
        with open("highscore.txt","r")as file:
            for line in file:
                self.high_score=int(line)
        high_score_str="High Score:"+str(self.high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.seti.bg_color)

        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.screen_rect.top

    def show_high_score(self):
        self.screen.blit(self.high_score_image,self.high_score_rect)

    def prep_level(self):
        level_str="Level:"+str(self.stats.level)
        self.level_image=self.font.render(level_str,True,self.text_color,self.seti.bg_color)

        self.level_image_rect=self.level_image.get_rect()
        self.level_image_rect.right=self.score_rect.right
        self.level_image_rect.top=self.score_rect.bottom+1
        
    def show_level(self):
        self.screen.blit(self.level_image,self.level_image_rect)
        
    def prep_rockets(self):
        self.rockets=Group()
        for rocket_number in range(self.stats.rockets_left):
            rocket=Rocket(self.screen,self.seti)
            rocket.rect.x=rocket_number*rocket.rect.width
            rocket.rect.y=0
            self.rockets.add(rocket)

    def show_rockets(self):
        self.rockets.draw(self.screen)




















                                 
        
