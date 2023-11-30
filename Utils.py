import pygame
from pygame import Surface, SurfaceType

from Constants import IMAGES_DIRECTORY


def get_image(name: str) -> Surface | SurfaceType:
    return pygame.image.load(f"{IMAGES_DIRECTORY}/{name}")
