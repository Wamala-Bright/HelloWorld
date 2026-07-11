import pygame

from settings import *


class Obstacle:


    def __init__(self,x,y):

        self.rect = pygame.Rect(
            x,
            y,
            40,
            40
        )



    def draw(self,screen):

        pygame.draw.rect(
            screen,
            OBSTACLE_COLOR,
            self.rect
        )