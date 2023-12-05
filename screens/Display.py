import pygame

from screens.MenuScreen import MenuScreen
from screens.SingleplayerScreen import SinglePlayerScreen


class Display:
    def __init__(self):

        font = pygame.font.SysFont("arial", 60)

        self.show_menu = True
        self.show_singleplayer = False
        self.show_multiplayer = False
        self.show_highscore = False
        self.surface = pygame.display.set_mode((400, 600))
        self.fps = pygame.time.Clock()
        self.menu_screen = MenuScreen(self, self.surface)
        self.singleplayer_screen = SinglePlayerScreen(self, self.surface, font)

        self.menu_screen.init_screen()

    def init_menu_screen(self):
        self.menu_screen.init_screen()

    def go_to_menu_screen(self):
        self.show_menu = True
        self.show_singleplayer = False
        self.show_multiplayer = False
        self.show_highscore = False

        self.menu_screen.init_screen()

    def go_to_singleplayer_screen(self):
        self.show_menu = False
        self.show_singleplayer = True
        self.show_multiplayer = False
        self.show_highscore = False

        self.singleplayer_screen.init_screen()
