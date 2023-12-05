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
        self.diglett_type = self.DiglettType.NORMAL

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

        hit_diglett = get_image("hit_diglett.png")
        hit_diglett_rect = hit_diglett.get_rect()

        shiny_diglett = get_image("shiny_diglett.png")
        shiny_diglett_rect = shiny_diglett.get_rect()

        hit_shiny_diglett = get_image("hit_shiny_diglett.png")
        hit_shiny_diglett_rect = hit_shiny_diglett.get_rect()

        bomb_diglett = get_image("bomb_diglett.png")
        bomb_diglett_rect = bomb_diglett.get_rect()

        hit_bomb_diglett = get_image("hit_bomb_diglett.png")
        hit_bomb_diglett_rect = hit_bomb_diglett.get_rect()

        healing_diglett = get_image("healing_diglett.png")
        healing_diglett_rect = healing_diglett.get_rect()

        hit_healing_diglett = get_image("hit_healing_diglett.png")
        hit_healing_diglett_rect = hit_healing_diglett.get_rect()

        diglett_cry = get_sfx("diglett_cry.wav")
        diglett_cry.set_volume(0.2)

        woosh_sfx = get_sfx("woosh.wav")
        woosh_sfx.set_volume(0.2)

        bomb_sfx = get_sfx("bomb.wav")
        bomb_sfx.set_volume(0.8)

        life_sfx = get_sfx("life.wav")
        life_sfx.set_volume(0.2)

        game_music = get_music_path("game.wav")

    class DiglettType(Enum):
        NORMAL = 0
        NORMAL_HIT = 1
        SHINY = 2
        SHINY_HIT = 3
        HEALING = 4
        HEALING_HIT = 5
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

        if self.diglett_type == self.DiglettType.NORMAL:
            self.surface.blit(self.Components.diglett, self.Components.diglett_rect)
            self.Components.diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.NORMAL_HIT:
            self.surface.blit(self.Components.hit_diglett, self.Components.hit_diglett_rect)
            self.Components.hit_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.SHINY:
            self.surface.blit(self.Components.shiny_diglett, self.Components.shiny_diglett_rect)
            self.Components.shiny_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.SHINY_HIT:
            self.surface.blit(self.Components.hit_shiny_diglett, self.Components.hit_shiny_diglett_rect)
            self.Components.hit_shiny_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.HEALING:
            self.surface.blit(self.Components.healing_diglett, self.Components.healing_diglett_rect)
            self.Components.healing_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.HEALING_HIT:
            self.surface.blit(self.Components.hit_healing_diglett, self.Components.hit_healing_diglett_rect)
            self.Components.hit_healing_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.BOMB:
            self.surface.blit(self.Components.bomb_diglett, self.Components.bomb_diglett_rect)
            self.Components.bomb_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.BOMB_HIT:
            self.surface.blit(self.Components.hit_bomb_diglett, self.Components.hit_bomb_diglett_rect)
            self.Components.hit_bomb_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.spawn_new_diglett:

            random_diglett = random.randint(1, 100)

            if random_diglett in range(1, 79):
                self.diglett_type = self.DiglettType.NORMAL

            if random_diglett == 80:
                self.diglett_type = self.DiglettType.SHINY

            if random_diglett in range(81, 90):
                if self.hearts < 5:
                    self.diglett_type = self.DiglettType.HEALING
                else:
                    self.diglett_type = self.DiglettType.NORMAL

            if random_diglett in range(91, 100):
                self.diglett_type = self.DiglettType.BOMB

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

            self.Components.diglett_rect.center = (-100, -100)

            self.Components.diglett_cry.play()
            self.diglett_type = self.DiglettType.NORMAL_HIT

        elif self.Components.shiny_diglett_rect.collidepoint(pointer_position):
            self.combo += 1
            self.score += self.combo + 100

            self.Components.shiny_diglett_rect.center = (-100, -100)

            self.Components.diglett_cry.play()
            self.diglett_type = self.DiglettType.SHINY_HIT

        elif self.Components.bomb_diglett_rect.collidepoint(pointer_position):
            self.hearts -= 1

            self.Components.bomb_diglett_rect.center = (-100, -100)

            self.Components.bomb_sfx.play()
            self.diglett_type = self.DiglettType.BOMB_HIT

        elif self.Components.healing_diglett_rect.collidepoint(pointer_position):
            self.hearts += 1
            self.combo += 1
            self.score += self.combo

            self.Components.healing_diglett_rect.center = (-100, -100)

            self.Components.life_sfx.play()
            self.diglett_type = self.DiglettType.HEALING_HIT

        else:
            self.hearts -= 1
            self.combo = 0

            if self.hearts == 0:
                self.gameover()

    def gameover(self):
        self.display.go_to_menu_screen()
        self.__init__(self.display, self.surface, self.font)
