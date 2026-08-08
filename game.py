import pygame

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
        self.level = 1

        self.game_over = False
        self.win = False

        self.last_hit = 0
        self.damage_cooldown = 500

    def update(self):

        if self.game_over or self.win:
            return

        self.player.update()
        self.enemy.update(self.player)

        # Enemy collision
        if self.player.rect.colliderect(self.enemy.rect):

            current_time = pygame.time.get_ticks()

            if current_time - self.last_hit >= self.damage_cooldown:

                self.player.health -= 10
                self.last_hit = current_time

                if self.player.health <= 0:
                    self.game_over = True

        # Coin collection
        if self.player.rect.colliderect(self.coin.rect):

            self.score += 1

            self.coin.random_position()

            # Increase difficulty every 5 coins
            if self.score % 5 == 0:

                self.level += 1

                self.enemy.speed += 1

            # Win at level 5
            if self.level >= 5:
                self.win = True

    def draw(self, screen):

        screen.fill(WHITE)

        font = pygame.font.Font(None, 36)

        if self.game_over:

            text = font.render(
                "GAME OVER - Press R",
                True,
                RED
            )

            screen.blit(text, (180, 250))
            return

        if self.win:

            text = font.render(
                "YOU WIN! - Press R",
                True,
                GREEN
            )

            screen.blit(text, (200, 250))
            return

        self.player.draw(screen)
        self.enemy.draw(screen)
        self.coin.draw(screen)

        score = font.render(
            f"Score: {self.score}",
            True,
            BLACK
        )

        health = font.render(
            f"Health: {self.player.health}",
            True,
            BLACK
        )

        level = font.render(
            f"Level: {self.level}",
            True,
            BLACK
        )

        screen.blit(score, (20, 20))
        screen.blit(health, (20, 55))
        screen.blit(level, (20, 90))