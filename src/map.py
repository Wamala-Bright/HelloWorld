import pygame
from obstacle import Obstacle


class GameMap:


    def __init__(self):

        self.walls = []


        self.create_level()



    def create_level(self):

        # Border walls

        for x in range(0,800,40):

            self.walls.append(
                Obstacle(x,0)
            )

            self.walls.append(
                Obstacle(x,560)
            )


        for y in range(0,600,40):

            self.walls.append(
                Obstacle(0,y)
            )

            self.walls.append(
                Obstacle(760,y)
            )


        # Inside obstacles

        positions = [

            (200,200),
            (240,200),
            (280,200),

            (500,350),
            (540,350),
            (580,350)

        ]


        for pos in positions:

            self.walls.append(
                Obstacle(
                    pos[0],
                    pos[1]
                )
            )



    def draw(self,screen):

        for wall in self.walls:

            wall.draw(screen)