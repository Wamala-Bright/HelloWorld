import pygame
import random

from settings import *
from assets import load_image


class Enemy:


    def __init__(self, level):

        self.rect = pygame.Rect(
            random.randint(50, WIDTH-50),
            random.randint(50, HEIGHT-50),
            40,
            40
        )


        # Balanced scaling

        self.speed = 1 + (level * 0.3)


        # Sprite

        self.image = load_image(
            "enemy.png"
        )



    def move(self, player):


        # Chase player

        if self.rect.x < player.rect.x:

            self.rect.x += self.speed


        elif self.rect.x > player.rect.x:

            self.rect.x -= self.speed



        if self.rect.y < player.rect.y:

            self.rect.y += self.speed


        elif self.rect.y > player.rect.y:

            self.rect.y -= self.speed



    def avoid_spawn(self):

        self.rect.x = random.randint(
            50,
            WIDTH - 50
        )

        self.rect.y = random.randint(
            50,
            HEIGHT - 50
        )



    def draw(self, screen):

        screen.blit(
            self.image,
            self.rect
        )