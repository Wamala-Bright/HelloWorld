import pygame


class Menu:


    def __init__(self):

        self.font = pygame.font.SysFont(
            None,
            60
        )



    def draw(self,screen):

        screen.fill(
            (20,20,20)
        )


        title=self.font.render(
            "TREASURE RUNNER",
            True,
            (255,255,255)
        )


        start=self.font.render(
            "PRESS ENTER",
            True,
            (255,255,255)
        )


        screen.blit(
            title,
            (180,200)
        )


        screen.blit(
            start,
            (250,320)
        )



    def start(self):

        keys=pygame.key.get_pressed()

        return keys[pygame.K_RETURN]