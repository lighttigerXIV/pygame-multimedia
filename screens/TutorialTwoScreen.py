import pygame
from pygame import Surface, SurfaceType
from pygame.font import Font

from Utils import get_image
from screens import Navigation
from Constants import BLACK


class TutorialTwoScreen:
    def __init__(self, display, surface):
        self.display: Display = display
        self.surface: Surface | SurfaceType = surface

    class Components:
        background = get_image("tutorial2.png")
        background = pygame.transform.scale(background, (400, 600))

    def draw_screen(self):
        self.surface.blit(self.Components.background, (0, 0))

    def on_mouse_click(self):
        self.display.go_to_multiplayer_screen()
