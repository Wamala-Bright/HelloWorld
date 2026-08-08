import pygame
import random

from settings import *


class Coin:


    def __init__(self):

        self.rect = pygame.Rect(
            300,
            200,
            25,
            25
        )



    def random_position(self):

        self.rect.x = random.randint(
            0,
            WIDTH-25
        )


        self.rect.y = random.randint(
            0,
            HEIGHT-25
        )



    def draw(self,screen):

        pygame.draw.rect(
            screen,
            YELLOW,
            self.rect
        )