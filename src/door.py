import pygame

from settings import *


class Door:


    def __init__(self):

        self.rect = pygame.Rect(
            700,
            500,
            40,
            60
        )

        self.locked = True



    def unlock(self):

        self.locked = False



    def draw(self,screen):

        if self.locked:

            color = (150,0,0)

        else:

            color = (0,255,0)


        pygame.draw.rect(
            screen,
            color,
            self.rect
        )