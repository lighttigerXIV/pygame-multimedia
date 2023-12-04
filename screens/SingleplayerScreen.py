import pygame
from pygame import SurfaceType, Surface

from Utils import get_image


class SinglePlayerScreen:
    def __init__(self, score=0):
        self.score = score

    class Components:
        background = get_image("game_background.png")
        background = pygame.transform.scale(background, (400, 600))

        first_hole = get_image("dirt.png")
        first_hole_rect = first_hole.get_rect()
        first_hole_rect.topleft = (50, 300)

    def draw_screen(
            self,
            display_surface: Surface | SurfaceType
    ):
        display_surface.blit(SinglePlayerScreen.Components.background, (0, 0))
        display_surface.blit(SinglePlayerScreen.Components.first_hole, (50, 300))
        self.score = 0
