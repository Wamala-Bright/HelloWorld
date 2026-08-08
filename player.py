import pygame

from settings import *


class Player:


    def __init__(self):

        self.rect = pygame.Rect(
            100,
            100,
            50,
            50
        )


        self.speed = PLAYER_SPEED

        self.health = PLAYER_HEALTH



    def update(self):

        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:

            self.rect.x -= self.speed


        if keys[pygame.K_RIGHT]:

            self.rect.x += self.speed


        if keys[pygame.K_UP]:

            self.rect.y -= self.speed


        if keys[pygame.K_DOWN]:

            self.rect.y += self.speed



        # Screen boundaries

        self.rect.left = max(
            0,
            self.rect.left
        )


        self.rect.right = min(
            WIDTH,
            self.rect.right
        )


        self.rect.top = max(
            0,
            self.rect.top
        )


        self.rect.bottom = min(
            HEIGHT,
            self.rect.bottom
        )



    def draw(self,screen):

        pygame.draw.rect(
            screen,
            BLUE,
            self.rect
        )