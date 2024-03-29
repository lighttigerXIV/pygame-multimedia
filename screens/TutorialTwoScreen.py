import pygame
from pygame import Surface, SurfaceType

from Utils import get_image
from screens import Navigation


class TutorialTwoScreen:
    def __init__(self, navigation, surface):
        self.navigation: Navigation = navigation
        self.surface: Surface | SurfaceType = surface

    class Components:
        background = get_image("tutorial2.png")
        background = pygame.transform.scale(background, (400, 600))

    def draw_screen(self):
        self.surface.blit(self.Components.background, (0, 0))

    def on_mouse_click(self):
        self.navigation.go_to_tutorial_three_screen()
