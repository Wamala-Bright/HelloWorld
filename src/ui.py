import pygame


def draw_health(
    screen,
    health
):

    pygame.draw.rect(
        screen,
        (100,0,0),
        (20,60,200,20)
    )


    pygame.draw.rect(
        screen,
        (0,255,0),
        (20,60,health*60,20)
    )