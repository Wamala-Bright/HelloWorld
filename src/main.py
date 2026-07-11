import pygame
import sys
import random


from player import Player
from treasure import Treasure
from enemy import Enemy
from level import Level
from map import GameMap
from key import Key
from door import Door

from settings import *



pygame.init()



screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)


pygame.display.set_caption(
    "Treasure Runner"
)



clock = pygame.time.Clock()



font = pygame.font.SysFont(
    None,
    32
)



# -------------------------
# GAME OBJECTS
# -------------------------

player = Player(
    100,
    100
)


game_map = GameMap()


treasure = Treasure()


key = Key()


door = Door()


level = Level()



enemies = []


for i in range(level.enemy_count()):

    enemies.append(
        Enemy(level.current)
    )



# Timers

damage_timer = 0

spawn_protection = 300



game_won = False



running = True



while running:


    # -------------------------
    # EVENTS
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False



    keys = pygame.key.get_pressed()



    # -------------------------
    # PLAYER
    # -------------------------

    player.move(
        keys,
        game_map.walls
    )


    player.boundary()



    # -------------------------
    # TREASURE
    # -------------------------

    if player.rect.colliderect(
        treasure.rect
    ):


        player.score += 10


        treasure = Treasure()



    # -------------------------
    # KEY COLLECTION
    # -------------------------

    if player.rect.colliderect(
        key.rect
    ):


        player.has_key = True



    # -------------------------
    # DOOR SYSTEM
    # -------------------------

    if player.rect.colliderect(
        door.rect
    ):


        if player.has_key:


            door.unlock()


            level.increase()


            player.has_key = False


            key = Key()

            treasure = Treasure()



            # add difficulty

            if len(enemies) < 5:

                enemies.append(
                    Enemy(level.current)
                )



    # -------------------------
    # TIMERS
    # -------------------------

    if damage_timer > 0:

        damage_timer -= 1



    if spawn_protection > 0:

        spawn_protection -= 1



    # -------------------------
    # ENEMIES
    # -------------------------

    for enemy in enemies:


        enemy.move(
            player
        )



        if spawn_protection <= 0:


            if player.rect.colliderect(
                enemy.rect
            ):


                if damage_timer == 0:


                    player.health -= 1


                    damage_timer = 60



                    enemy.rect.x = random.randint(
                        50,
                        WIDTH - 50
                    )


                    enemy.rect.y = random.randint(
                        50,
                        HEIGHT - 50
                    )



    # -------------------------
    # LEVEL COMPLETE
    # -------------------------

    if level.current >= 5:

        game_won = True



    # -------------------------
    # GAME OVER
    # -------------------------

    if player.health <= 0:

        print("GAME OVER")

        running = False



    # -------------------------
    # DRAW
    # -------------------------

    screen.fill(
        BACKGROUND
    )



    game_map.draw(
        screen
    )



    treasure.draw(
        screen
    )



    key.draw(
        screen
    )


    door.draw(
        screen
    )



    player.draw(
        screen
    )



    for enemy in enemies:

        enemy.draw(
            screen
        )



    # HUD

    hud = font.render(

        f"Score: {player.score}  HP: {player.health}  Level: {level.current}  Key: {player.has_key}",

        True,

        WHITE
    )


    screen.blit(
        hud,
        (20,20)
    )



    if spawn_protection > 0:

        text = font.render(
            "READY!",
            True,
            WHITE
        )

        screen.blit(
            text,
            (350,300)
        )



    if game_won:

        win_text = font.render(
            "YOU WIN!",
            True,
            WHITE
        )

        screen.blit(
            win_text,
            (330,280)
        )



    pygame.display.update()



    clock.tick(
        FPS
    )



pygame.quit()

sys.exit()