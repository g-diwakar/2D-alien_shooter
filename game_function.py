import pygame
import sys
from time import sleep

from bullet import Bullet
from alien import Alien
from explosion import Explosion
import sound

def check_events(seti,screen,stats,play_button,rocket,aliens,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit(0)

        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(seti,screen,stats,play_button,rocket,aliens,bullets,mouse_x,mouse_y)

        elif event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_RIGHT:
                rocket.moving_right=True
                
            if event.key==pygame.K_LEFT:
                rocket.moving_left=True

            if event.key==pygame.K_p and not stats.game_active:
                '''We are going to start the game using keyboard pressing 'p'.Since we already
                   have a function to deactivate the play button what we have done is set the
                   mouse position to the center of the screen where play button is'''
                
                mouse_x,mouse_y=seti.screen_width/2,seti.screen_height/2
                check_play_button(seti,screen,stats,play_button,rocket,aliens,bullets,mouse_x,mouse_y)
                
                
            if event.key==pygame.K_SPACE or event.key==pygame.K_UP:
                if len(bullets)<seti.bullets_allowed:
                    new_bullet=Bullet(seti,screen,rocket)
                    bullets.add(new_bullet)
                    sound.load_shoot_sound()
                

        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                rocket.moving_right=False

            if event.key==pygame.K_LEFT:
                rocket.moving_left=False

def update_screen(seti,screen,rocket,aliens,bullets,play_button,stats,sb,expo):
    screen.fill(seti.bg_color)
    rocket.blitme()
    aliens.draw(screen)
    #Redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    sb.prep_score()    
    sb.show_score()
    sb.prep_high_score()
    sb.show_high_score()
    sb.prep_level()
    sb.show_level()
    sb.prep_rockets()
    sb.show_rockets()
    #Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    if expo:
        expo.blitme()
        pygame.display.flip()
        sleep(0.05)
        
    #for making things visible in the screen
    if not expo:
        pygame.display.flip()

def update_bullets(bullets,aliens,seti,screen,rocket,sb,stats,play_button):
    #remove the bullets that have disspared
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    '''collision=pygame.sprite.groupcollide(bullets,aliens,False,True)
    if collision:
        sound.load_boom_sound()
        sb.update_score()
        check_high_score(stats,sb)
        bullets.remove(bullet)'''
    for alien in aliens.sprites():
        if pygame.sprite.spritecollideany(alien,bullets):
            sound.load_boom_sound()
            sb.update_score()
            check_high_score(stats,sb)
            bullets.remove(bullet)
            aliens.remove(alien)
            expo=Explosion(screen,alien)
            update_screen(seti,screen,rocket,aliens,bullets,play_button,stats,sb,expo)
        
    if len(aliens)==0:
        #Destroy existing bullets,speed up game,and create a new fleet.
        bullets.empty()
        seti.increase_speed()
        create_fleet(seti,screen,rocket,aliens)
        #increase level
        stats.level+=1
    
def create_fleet(seti,screen,rocket,aliens):
    #Create full fleet of aliens
    alien=Alien(seti,screen)
    number_aliens_x=get_number_aliens_x(seti,alien.rect.width)
    number_rows=get_number_rows(seti,rocket.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(seti,screen,aliens,alien_number,row_number)
        
def get_number_aliens_x(seti,alien_width):
    #determine the number of aliens that fit in a row
    available_space_x=seti.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(seti,rocket_height,alien_height):
    #determine the number of rows that fits the screen
    available_space_y=(seti.screen_height-3*alien_height-rocket_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(seti,screen,aliens,alien_number,row_number):
    #Create an alien and place it in row
     alien=Alien(seti,screen)
     alien_width=alien.rect.width
     alien.x=alien_width+2*alien_width*alien_number
     alien.rect.x=alien.x
     alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
     aliens.add(alien)

def update_aliens(seti,stats,screen,rocket,aliens,bullets):
    check_fleet_edges(seti,aliens)
    aliens.update()
    check_aliens_bottom(seti,stats,screen,rocket,aliens,bullets)

    #check for alien rocket collisions
    if pygame.sprite.spritecollideany(rocket,aliens):
        rocket_hit(seti,stats,screen,rocket,aliens,bullets)

def check_fleet_edges(seti,aliens):
    #Respond if any aliens have reached an edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(seti,aliens)
            break

def change_fleet_direction(seti,aliens):
    #Drop the entire fleet and change the fleet direction
    for alien in aliens.sprites():
        alien.rect.y+=seti.fleet_drop_speed
    seti.fleet_direction*=-1

def rocket_hit(seti,stats,screen,rocket,aliens,bullets):
    if stats.rockets_left>0:
        stats.rockets_left-=1

        aliens.empty()
        bullets.empty()

        create_fleet(seti,screen,rocket,aliens)
        rocket.center_rocket()

        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(seti,stats,screen,rocket,aliens,bullets):
    #Check if any aliens have reached the bottom
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            rocket_hit(seti,stats,screen,rocket,aliens,bullets)
            break
    

def check_play_button(seti,screen,stats,play_button,rocket,aliens,bullets,mouse_x,mouse_y):
    #Stats new game when the player clicks play
    if play_button.rect.collidepoint(mouse_x,mouse_y)  and not stats.game_active:
        #Reset the game settings
        seti.initialize_dynamic_settings()
        #hide the mouse cursor
        pygame.mouse.set_visible(False)
        #reset the game stats

        stats.reset_stats()
        stats.game_active=True

        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the rocket
        create_fleet(seti,screen,rocket,aliens)
        rocket.center_rocket()

def check_high_score(stats,sb):
    if stats.score>sb.high_score:
        sb.high_score=stats.score

        #writes high scores to file
        with open("highscore.txt","w")as file_object:
            file_object.write(str(sb.high_score))

        sb.prep_high_score()






























        
