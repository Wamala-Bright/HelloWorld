import pygame

from settings import *
from assets import load_image


class Player:

    def __init__(self, x, y):

        self.rect = pygame.Rect(
            x,
            y,
            40,
            40
        )

        self.speed = PLAYER_SPEED

        self.health = 3

        self.score = 0

        # Inventory
        self.has_key = False

        # Sprite
        self.image = load_image(
            "player.png"
        )



    def move(self, keys, walls):

        old_position = self.rect.copy()


        # Movement

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed


        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed


        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed


        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed



        # Wall collision

        for wall in walls:

            if self.rect.colliderect(
                wall.rect
            ):

                self.rect = old_position



    def boundary(self):

        self.rect.clamp_ip(
            pygame.Rect(
                0,
                0,
                WIDTH,
                HEIGHT
            )
        )



    def draw(self, screen):

        screen.blit(
            self.image,
            self.rect
        )