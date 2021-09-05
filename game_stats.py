class GameStats():
    #Tract stats for alien invasion

    def __init__(self,seti):
        self.seti=seti
        self.reset_stats()

        self.game_active=False

    def reset_stats(self):
        #Initialize stats that can change during the game
        self.rockets_left=self.seti.rocket_limit
        self.score=0
        self.level=1
        
