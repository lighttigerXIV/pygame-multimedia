import pygame
import random
from enum import Enum

from Utils import get_image, get_sfx, get_music_path


class SinglePlayerScreen:
    def __init__(self, display, surface, font):
        self.score = 0
        self.hearts = 5
        self.combo = 0
        self.diglett_hole_position = -1
        self.diglett_y_offset = 0
        self.move_diglett_up = True
        self.spawn_new_diglett = True
        self.display = display
        self.surface = surface
        self.font = font
        self.current_diglett = self.DiglettType.NORMAL

    def init_screen(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.stop()
        pygame.mixer.music.load(self.Components.game_music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer_music.play(True)

    hole_positions = [(68, 254), (188, 344), (315, 240), (68, 410), (198, 456), (323, 398), (68, 540), (188, 588),
                      (323, 556)]  # x, y

    class Components:
        background = get_image("game_background.png")
        background = pygame.transform.scale(background, (400, 600))

        background_mask = get_image("gamemask_background.png")
        background_mask = pygame.transform.scale(background_mask, (400, 600))

        heart = get_image("heart.png")
        heart = pygame.transform.scale(heart, (30, 30))

        diglett = get_image("diglett.png")
        diglett_rect = diglett.get_rect()

        black_diglett = get_image("black_diglett.png")
        black_diglett_rect = black_diglett.get_rect()

        diglett_cry = get_sfx("diglett_cry.wav")
        diglett_cry.set_volume(0.3)

        woosh_sfx = get_sfx("woosh.wav")
        woosh_sfx.set_volume(0.2)

        game_music = get_music_path("game.wav")

    class DiglettType(Enum):
        NORMAL = 0
        NORMAL_HIT = 1
        SHINY = 2
        SHINY_HIT = 3
        HEAL = 4
        HEAL_HIT = 5
        BOMB = 6
        BOMB_HIT = 7


    def move_diglett(self):

        if self.move_diglett_up:
            self.diglett_y_offset -= 2

        elif not self.move_diglett_up:
            self.diglett_y_offset += 2

        if self.diglett_y_offset == -50:
            self.move_diglett_up = False

        elif self.diglett_y_offset == 0:
            self.move_diglett_up = True
            self.spawn_new_diglett = True

    def draw_screen(self):
        self.surface.blit(self.Components.background, (0, 0))

        x, y = self.hole_positions[self.diglett_hole_position]

        self.surface.blit(self.Components.diglett, self.Components.diglett_rect)
        self.Components.diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.spawn_new_diglett:
            self.diglett_hole_position = random.randint(0, 8)
            self.spawn_new_diglett = False

        self.move_diglett()

        self.surface.blit(self.Components.background_mask, (0, 0))

        highscore_text = self.font.render(str(self.score), True, (255, 255, 255))
        self.surface.blit(highscore_text, (20, 20))

        if self.hearts >= 1:
            self.surface.blit(self.Components.heart, (10, 0))

        if self.hearts >= 2:
            self.surface.blit(self.Components.heart, (45, 0))

        if self.hearts >= 3:
            self.surface.blit(self.Components.heart, (80, 0))

        if self.hearts >= 4:
            self.surface.blit(self.Components.heart, (115, 0))

        if self.hearts == 5:
            self.surface.blit(self.Components.heart, (150, 0))

    def on_mouse_click(
            self,
            pointer_position
    ):

        self.Components.woosh_sfx.play()

        if self.Components.diglett_rect.collidepoint(pointer_position):
            self.combo += 1
            self.score += self.combo
            self.Components.diglett_cry.play()
        else:
            self.hearts -= 1
            self.combo = 0

            if self.hearts == 0:
                self.gameover()

    def gameover(self):
        self.display.go_to_menu_screen()
        self.__init__(self.display, self.surface, self.font)
