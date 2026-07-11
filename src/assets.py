import pygame
import os


IMAGE_PATH = os.path.join(
    "assets",
    "images"
)



def load_image(filename):

    path = os.path.join(
        IMAGE_PATH,
        filename
    )


    try:

        image = pygame.image.load(
            path
        )


        image = pygame.transform.scale(
            image,
            (40,40)
        )


        return image


    except:

        print(
            f"Missing image: {filename}"
        )


        # fallback square

        image = pygame.Surface(
            (40,40)
        )


        image.fill(
            (255,255,255)
        )


        return image