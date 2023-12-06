import pygame

from screens.MenuScreen import MenuScreen
from screens.SingleplayerScreen import SinglePlayerScreen
from screens.GameoverScreen import GameOverScreen
from screens.TutorialOneScreen import TutorialOneScreen


class Display:
    def __init__(self):
        font = pygame.font.SysFont("arial", 60)

        self.show_menu = True
        self.show_tutorial_one = False
        self.show_singleplayer = False
        self.show_gameover = False
        self.show_multiplayer = False
        self.show_highscore = False
        self.surface = pygame.display.set_mode((400, 600))
        self.fps = pygame.time.Clock()
        self.menu_screen = MenuScreen(self, self.surface)
        self.tutorial_one_screen = TutorialOneScreen(self, self.surface)
        self.singleplayer_screen = SinglePlayerScreen(self, self.surface, font)
        self.gameover_screen = GameOverScreen(self.surface)

        self.menu_screen.init_screen()

    def init_menu_screen(self):
        self.menu_screen.init_screen()

    def enable_screen(
            self,
            show_menu=False,
            show_tutorial_one=False,
            show_singleplayer=False,
            show_gameover=False,
            show_multiplayer=False,
            show_highscore=False
    ):
        self.show_menu = show_menu
        self.show_tutorial_one = show_tutorial_one
        self.show_singleplayer = show_singleplayer
        self.show_gameover = show_gameover
        self.show_multiplayer = show_multiplayer
        self.show_highscore = show_highscore

    def go_to_menu_screen(self):
        self.enable_screen(show_menu=True)
        self.menu_screen.init_screen()

    def go_to_tutorial_one_screen(self):
        self.enable_screen(show_tutorial_one=True)

    def go_to_singleplayer_screen(self):
        self.enable_screen(show_singleplayer=True)
        self.singleplayer_screen.init_screen()

    def go_to_gameover_screen(self, score):
        self.enable_screen(show_gameover=True)
        self.gameover_screen.init_screen(score)
