class Setings():
    #Store all settings for the game
    def __init__(self):
        
        #for rocket
        self.rocket_limit=3
        
        #for screen
        self.screen_width=1350
        self.screen_height=700
        self.bg_color=(230,230,230)
        
        #settings for Bullet
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3
        
        #settings for alien
        self.fleet_drop_speed=10
       
        #leveling up the game
        self.speedup_scale=1.3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #Initialize the settings that change throught the game
        self.rocket_speed_factor=1.5
        self.bullet_speed=3
        self.alien_speed_factor=1
         #fleet_direction of 1 represents right;-1 represents left
        self.fleet_direction=1

    def increase_speed(self):
        #Increase speed settings
        self.rocket_speed_factor*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        
        
        
