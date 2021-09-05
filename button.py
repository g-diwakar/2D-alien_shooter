import pygame
pygame.font.init()
class Button():
    def __init__(self,seti,screen,msg):
        #initialize the button attributes
        self.screen=screen
        self.screen_rect=screen.get_rect()

        #Set the dimensions and the properties of the button.
        self.width,self.height=200,50
        self.button_color=(60,60,60)
        self.text_color=(255,2555,255)
        self.font=pygame.font.Font(None,48)

        #Build the button's rect object and center it
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self,msg):
        #Turn msg into a rendered image and center text on the button
        self.msg_image=self.font.render(msg,True,(255,255,255),(60,60,60))
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        #Draw blank button and then draw messsage
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
