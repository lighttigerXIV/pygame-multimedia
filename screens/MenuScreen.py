import pygame
import screens.Display
from pygame import Surface, SurfaceType
from Utils import get_image


class MenuScreen:

    def __init__(self, display, surface):
        self.display = display
        self.surface = surface

    class Components:
        background = get_image("menu_background.jpg")
        background = pygame.transform.scale(background, (400, 600))

        menu_art = get_image("menu_art.png")

        singleplayer_button = get_image("button_single.png")
        singleplayer_button_rect = singleplayer_button.get_rect()
        singleplayer_button_rect.topleft = (100, 275)

        multiplayer_button = get_image("button_multiplayer.png")
        multiplayer_button_rect = multiplayer_button.get_rect()
        multiplayer_button_rect.topleft = (100, 375)

        highscore_button = get_image("button_highscore.png")
        highscore_button_rect = highscore_button.get_rect()
        highscore_button_rect.topleft = (100, 475)

    def on_mouse_click(
            self,
            pointer_position
    ):
        if MenuScreen.Components.singleplayer_button_rect.collidepoint(pointer_position):
            self.display.go_to_singleplayer_screen()

    def draw_screen(self):
        self.surface.blit(MenuScreen.Components.background, (0, 0))
        self.surface.blit(MenuScreen.Components.menu_art, (75, 75))
        self.surface.blit(MenuScreen.Components.singleplayer_button, (100, 275))
        self.surface.blit(MenuScreen.Components.multiplayer_button, (100, 375))
        self.surface.blit(MenuScreen.Components.highscore_button, (100, 475))
