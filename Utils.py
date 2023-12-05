import pygame
from pygame import Surface, SurfaceType
from pygame.mixer import Sound

from Constants import IMAGES_DIRECTORY, AUDIO_DIRECTORY


def get_image(name: str) -> Surface | SurfaceType:
    return pygame.image.load(f"{IMAGES_DIRECTORY}/{name}")


def get_sfx(name: str) -> Sound:
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    return pygame.mixer.Sound(f"{AUDIO_DIRECTORY}/{name}")
