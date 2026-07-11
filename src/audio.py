import pygame
import os


pygame.mixer.init()


def play_sound(file):

    sound = pygame.mixer.Sound(
        os.path.join(
            "assets",
            "sounds",
            file
        )
    )

    sound.play()



def play_music():

    pygame.mixer.music.load(
        "assets/sounds/music.mp3"
    )

    pygame.mixer.music.play(
        -1
    )