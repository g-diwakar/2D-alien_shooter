import pygame
from pygame.sprite import Group
import sys

from settings import Setings
from rocket import Rocket
import game_function as gf
from bullet import Bullet
from game_stats import GameStats as gs
from button import Button
from scoreboard import Scoreboard
import sound


seti=Setings()

def run_game():
    #initialize game and create a screen object
    pygame.init()
    screen=pygame.display.set_mode((seti.screen_width,seti.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats=gs(seti)
    sb=Scoreboard(seti,screen,stats)

    rocket=Rocket(screen,seti)
    bullets=Group()
    aliens=Group()
    gf.create_fleet(seti,screen,rocket,aliens)

    play_button=Button(seti,screen,"Play")
    
    #main loop for the game
    while True:
        
        gf.check_events(seti,screen,stats,play_button,rocket,aliens,bullets)
        #sound.load_sound_effects()
        
        
        if stats.game_active:
            #sound.load_sound_effects()
            rocket.update()
            bullets.update()
            gf.update_bullets(bullets,aliens,seti,screen,rocket,sb,stats,play_button)  #remove the disappered bullets from screen
            gf.update_aliens(seti,stats,screen,rocket,aliens,bullets)
        gf.update_screen(seti,screen,rocket,aliens,bullets,play_button,stats,sb,expo=None)
        

if __name__=="__main__":
    run_game()
