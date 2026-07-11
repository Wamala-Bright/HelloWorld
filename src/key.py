import pygame
import random

from settings import *


class Key:


    def __init__(self):

        self.rect = pygame.Rect(
            random.randint(50,700),
            random.randint(50,500),
            25,
            25
        )


    def draw(self,screen):

        pygame.draw.rect(
            screen,
            (255,255,0),
            self.rect
        )