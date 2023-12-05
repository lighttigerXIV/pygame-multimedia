import pygame
import screens.Display
from pygame import Surface, SurfaceType
from Utils import get_image, get_music_path


class MenuScreen:

    def __init__(self, display, surface):
        self.display = display
        self.surface = surface

    def init_screen(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.stop()
        pygame.mixer.music.load(self.Components.menu_music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer_music.play(True)

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

        menu_music = get_music_path("menu.wav")

    def on_mouse_click(
            self,
            pointer_position
    ):
        if MenuScreen.Components.singleplayer_button_rect.collidepoint(pointer_position):
            self.display.go_to_singleplayer_screen()

    def draw_screen(self):
        self.surface.blit(MenuScreen.Components.background, (0, 0))
        self.surface.blit(MenuScreen.Components.menu_art, (75, 50))
        self.surface.blit(MenuScreen.Components.singleplayer_button, (100, 275))
        self.surface.blit(MenuScreen.Components.multiplayer_button, (100, 375))
        self.surface.blit(MenuScreen.Components.highscore_button, (100, 475))
