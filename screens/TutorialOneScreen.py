import pygame
from pygame import Surface, SurfaceType
from pygame.font import Font

from Utils import get_image
from screens import Display
from Constants import BLACK


class TutorialOneScreen:
    def __init__(self, display, surface):
        self.display: Display = display
        self.surface: Surface | SurfaceType = surface
        self.font: Font = pygame.font.SysFont("arial", 20)

    class Components:
        background = get_image("tutorial1.png")
        background = pygame.transform.scale(background, (400, 600))

    def draw_screen(self):
        self.surface.blit(self.Components.background, (0, 0))

        text = self.font.render("+1 point", True, BLACK)
        self.surface.blit(text, text.get_rect(center=(215, 175)))

        text = self.font.render("+100 points", True, BLACK)
        self.surface.blit(text, text.get_rect(center=(235, 265)))

        text = self.font.render("-1 life", True, BLACK)
        self.surface.blit(text, text.get_rect(center=(200, 355)))

        text = self.font.render("+1 life", True, BLACK)
        self.surface.blit(text, text.get_rect(center=(200, 445)))

        text = self.font.render("Click anywhere to play", True, BLACK)
        self.surface.blit(text, text.get_rect(center=(200, 550)))

    def on_mouse_click(self):
        self.display.go_to_singleplayer_screen()
