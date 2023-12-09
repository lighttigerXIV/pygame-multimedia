import random
from enum import Enum

import pygame
from pygame import SurfaceType, Surface

from Constants import WHITE
from Utils import get_image, get_sfx, get_music_path


class MultiPlayerScreen:
    def __init__(self, navigation, surface, font):
        self.first_player_score = 0
        self.second_player_score = 0
        self.first_player_hearts = 5
        self.second_player_hearts = 5
        self.diglett_hole_position = -1
        self.diglett_y_offset = 0
        self.move_diglett_up = True
        self.spawn_new_diglett = True
        self.navigation = navigation
        self.surface: Surface | SurfaceType = surface
        self.font = font
        self.diglett_type = self.DiglettType.NORMAL

    def init_screen(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.stop()
        pygame.mixer.music.load(self.Components.game_music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer_music.play(True)

    hole_positions = [(68, 258), (188, 344), (315, 238), (68, 412), (198, 458), (323, 398), (68, 542), (188, 590),
                      (323, 557)]

    class Components:
        background = get_image("game_background.png")
        background = pygame.transform.scale(background, (400, 600))

        background_mask = get_image("gamemask_background.png")
        background_mask = pygame.transform.scale(background_mask, (400, 600))

        heart = get_image("heart.png")
        heart = pygame.transform.scale(heart, (30, 30))

        blue_heart = get_image("heart_blue.png")
        blue_heart = pygame.transform.scale(blue_heart, (30, 30))

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
            self.diglett_y_offset -= 1.6

        elif not self.move_diglett_up:
            self.diglett_y_offset += 1.6

        if int(self.diglett_y_offset) <= -50:
            self.move_diglett_up = False

        elif int(self.diglett_y_offset) >= 0:
            self.move_diglett_up = True
            self.spawn_new_diglett = True

    def draw_screen(self):
        self.surface.blit(self.Components.background, (0, 0))

        x, y = self.hole_positions[self.diglett_hole_position]

        if self.diglett_type == self.DiglettType.NORMAL:
            self.surface.blit(self.Components.diglett, self.Components.diglett_rect)
            self.Components.diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.SHINY:
            self.surface.blit(self.Components.shiny_diglett, self.Components.shiny_diglett_rect)
            self.Components.shiny_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.HEALING:
            self.surface.blit(self.Components.healing_diglett, self.Components.healing_diglett_rect)
            self.Components.healing_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.BOMB:
            self.surface.blit(self.Components.bomb_diglett, self.Components.bomb_diglett_rect)
            self.Components.bomb_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.NORMAL_HIT:
            self.surface.blit(self.Components.hit_diglett, self.Components.hit_diglett_rect)
            self.Components.hit_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.SHINY_HIT:
            self.surface.blit(self.Components.hit_shiny_diglett, self.Components.hit_shiny_diglett_rect)
            self.Components.hit_shiny_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.HEALING_HIT:
            self.surface.blit(self.Components.hit_healing_diglett, self.Components.hit_healing_diglett_rect)
            self.Components.hit_healing_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.diglett_type == self.DiglettType.BOMB_HIT:
            self.surface.blit(self.Components.hit_bomb_diglett, self.Components.hit_bomb_diglett_rect)
            self.Components.hit_bomb_diglett_rect.center = (x, y + self.diglett_y_offset)

        if self.spawn_new_diglett:
            population = [self.DiglettType.NORMAL, self.DiglettType.SHINY, self.DiglettType.HEALING,
                          self.DiglettType.BOMB]

            weights = [0.79, 0.01, 0.1, 0.1]

            new_diglett = random.choices(population, weights, k=1)[0]

            self.diglett_type = new_diglett
            self.diglett_hole_position = random.randint(0, 8)
            self.spawn_new_diglett = False

        self.move_diglett()

        self.surface.blit(self.Components.background_mask, (0, 0))

        first_player_score_text = self.font.render(str(self.first_player_score), True, WHITE)
        self.surface.blit(first_player_score_text, (75, 30))

        second_player_score_text = self.font.render(str(self.second_player_score), True, WHITE)
        self.surface.blit(second_player_score_text, (285, 30))

        if self.first_player_hearts >= 1:
            self.surface.blit(self.Components.heart, (10, 0))

        if self.first_player_hearts >= 2:
            self.surface.blit(self.Components.heart, (45, 0))

        if self.first_player_hearts >= 3:
            self.surface.blit(self.Components.heart, (80, 0))

        if self.first_player_hearts >= 4:
            self.surface.blit(self.Components.heart, (115, 0))

        if self.first_player_hearts == 5:
            self.surface.blit(self.Components.heart, (150, 0))

        if self.second_player_hearts >= 1:
            self.surface.blit(self.Components.blue_heart, (220, 0))

        if self.second_player_hearts >= 2:
            self.surface.blit(self.Components.blue_heart, (255, 0))

        if self.second_player_hearts >= 3:
            self.surface.blit(self.Components.blue_heart, (290, 0))

        if self.second_player_hearts >= 4:
            self.surface.blit(self.Components.blue_heart, (325, 0))

        if self.second_player_hearts == 5:
            self.surface.blit(self.Components.blue_heart, (360, 0))

    def on_key_down(self, key):

        if self.first_player_hearts > 0:
            if key == pygame.K_q:
                self.verify_collision(1, 0)
            if key == pygame.K_w:
                self.verify_collision(1, 1)
            if key == pygame.K_e:
                self.verify_collision(1, 2)
            if key == pygame.K_a:
                self.verify_collision(1, 3)
            if key == pygame.K_s:
                self.verify_collision(1, 4)
            if key == pygame.K_d:
                self.verify_collision(1, 5)
            if key == pygame.K_z:
                self.verify_collision(1, 6)
            if key == pygame.K_x:
                self.verify_collision(1, 7)
            if key == pygame.K_c:
                self.verify_collision(1, 8)

        if self.second_player_hearts > 0:
            if key == pygame.K_KP7:
                self.verify_collision(2, 0)
            if key == pygame.K_KP8:
                self.verify_collision(2, 1)
            if key == pygame.K_KP9:
                self.verify_collision(2, 2)
            if key == pygame.K_KP4:
                self.verify_collision(2, 3)
            if key == pygame.K_KP5:
                self.verify_collision(2, 4)
            if key == pygame.K_KP6:
                self.verify_collision(2, 5)
            if key == pygame.K_KP1:
                self.verify_collision(2, 6)
            if key == pygame.K_KP2:
                self.verify_collision(2, 7)
            if key == pygame.K_KP3:
                self.verify_collision(2, 8)

    def verify_collision(self, player: int, position: int):

        if position == self.diglett_hole_position:

            if self.diglett_type == self.DiglettType.NORMAL:
                self.diglett_type = self.DiglettType.NORMAL_HIT
                self.Components.diglett_rect.center = (-1000, -1000)
                self.Components.diglett_cry.play()

                if player == 1:
                    self.first_player_score += 1
                else:
                    self.second_player_score += 1

            if self.diglett_type == self.DiglettType.SHINY:
                self.diglett_type = self.DiglettType.SHINY_HIT
                self.Components.shiny_diglett_rect.center = (-1000, -1000)
                self.Components.diglett_cry.play()

                if player == 1:
                    self.first_player_score += 100
                else:
                    self.second_player_score += 100

            if self.diglett_type == self.DiglettType.HEALING:
                self.diglett_type = self.DiglettType.HEALING_HIT
                self.Components.healing_diglett_rect.center = (-1000, -1000)
                self.Components.life_sfx.play()

                if player == 1:
                    self.first_player_score += 1
                    if self.first_player_hearts < 5:
                        self.first_player_hearts += 1
                else:
                    self.second_player_score += 1
                    if self.second_player_hearts < 5:
                        self.second_player_hearts += 1

            if self.diglett_type == self.DiglettType.BOMB:
                self.diglett_type = self.DiglettType.BOMB_HIT
                self.Components.bomb_diglett_rect.center = (-1000, -1000)
                self.Components.bomb_sfx.play()

                if player == 1:
                    if self.first_player_hearts > 0:
                        self.first_player_hearts -= 1
                else:
                    if self.second_player_hearts > 0:
                        self.second_player_hearts -= 1

        else:
            if player == 1:
                self.first_player_hearts -= 1
            else:
                self.second_player_hearts -= 1

        if self.first_player_hearts == 0 and self.second_player_hearts == 0:
            self.gameover()

    def gameover(self):
        self.navigation.go_to_multiplayer_gameover_screen(self.first_player_score, self.second_player_score)
        self.__init__(self.navigation, self.surface, self.font)
