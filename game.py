import pygame
import random

from player import Player
from enemy import Enemy
from coin import Coin

from settings import *


class Game:


    def __init__(self):

        self.restart()



    def restart(self):

        self.player = Player()

        self.enemy = Enemy()

        self.coin = Coin()


        self.score = 0

        self.game_over = False



    def update(self):

        if self.game_over:
            return


        self.player.update()


        self.enemy.update(
            self.player
        )


        # Player touches enemy

        if self.player.rect.colliderect(
            self.enemy.rect
        ):

            self.player.health -= 1


            if self.player.health <= 0:

                self.game_over = True



        # Player collects coin

        if self.player.rect.colliderect(
            self.coin.rect
        ):

            self.score += 1

            self.coin.random_position()



    def draw(self, screen):

        screen.fill(WHITE)


        if self.game_over:


            font = pygame.font.Font(
                None,
                60
            )


            text = font.render(
                "GAME OVER - Press R",
                True,
                RED
            )


            screen.blit(
                text,
                (150,250)
            )


            return



        self.player.draw(screen)


        self.enemy.draw(screen)


        self.coin.draw(screen)



        font = pygame.font.Font(
            None,
            30
        )


        score_text = font.render(
            f"Score: {self.score}",
            True,
            BLACK
        )


        health_text = font.render(
            f"Health: {self.player.health}",
            True,
            BLACK
        )


        screen.blit(
            score_text,
            (20,20)
        )


        screen.blit(
            health_text,
            (20,50)
        )