import pygame
import random
from settings import *


class Treasure:


    def __init__(self):

        self.rect = pygame.Rect(
            random.randint(20,760),
            random.randint(20,560),
            25,
            25
        )


    def draw(self,screen):

        pygame.draw.rect(
            screen,
            TREASURE_COLOR,
            self.rect
        )