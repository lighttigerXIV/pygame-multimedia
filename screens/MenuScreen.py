import pygame
import screens.Display
from pygame import Surface, SurfaceType
from Utils import get_image


class MenuScreen:
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
        pointer_position,
        display_state: screens.Display.State
):
    if MenuScreen.Components.singleplayer_button_rect.collidepoint(pointer_position):
        print("Entrou aqui")
        display_state.go_to_singleplayer_screen()


def draw_screen(
        display_surface: Surface | SurfaceType
):
    display_surface.blit(MenuScreen.Components.background, (0, 0))
    display_surface.blit(MenuScreen.Components.menu_art, (75, 75))
    display_surface.blit(MenuScreen.Components.singleplayer_button, (100, 275))
    display_surface.blit(MenuScreen.Components.multiplayer_button, (100, 375))
    display_surface.blit(MenuScreen.Components.highscore_button, (100, 475))
