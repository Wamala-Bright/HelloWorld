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

        self.random_position()

    def random_position(self):

        self.rect.x = random.randint(
            0,
            WIDTH - self.rect.width
        )

        self.rect.y = random.randint(
            0,
            HEIGHT - self.rect.height
        )

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            YELLOW,
            self.rect
        )