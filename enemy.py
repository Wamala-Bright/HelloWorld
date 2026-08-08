import pygame

from settings import *


class Enemy:

    def __init__(self):

        self.rect = pygame.Rect(
            500,
            300,
            50,
            50
        )

        self.speed = ENEMY_SPEED

    def update(self, player):

        if self.rect.x < player.rect.x:
            self.rect.x += self.speed

        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed

        if self.rect.y < player.rect.y:
            self.rect.y += self.speed

        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            RED,
            self.rect
        )