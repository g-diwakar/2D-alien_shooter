import pygame

class dummysound:
    def play(self):pass

def load_sound(file):
    if not pygame.mixer:
        return dummysound()
    try:
        sound=pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print("Unable to load")

    return dummysound()

def load_sound_effects():
    if pygame.mixer and pygame.mixer.music:
        music="Sounds/house_lo.mp3"
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

def load_boom_sound():
    boom_sound=load_sound("Sounds/boom.wav")
    boom_sound.play()

def load_shoot_sound():
    shoot_sound=load_sound("Sounds/car_door.wav")
    shoot_sound.play()
    
    
