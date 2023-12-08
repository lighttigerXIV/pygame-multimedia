import pygame
from pygame import Surface, SurfaceType
from pygame.font import Font

from Utils import get_image, get_music_path, write_highscore, get_last_used_name
from Constants import BLACK, GREY, SELECTED_GREY
from screens import Navigation


class GameOverScreen:
    def __init__(self, surface, navigation):
        self.score: int = 0
        self.surface: Surface | SurfaceType = surface
        self.navigation: Navigation = navigation
        self.gameover_font: Font = pygame.font.SysFont("arial", 40)
        self.score_font: Font = pygame.font.SysFont("arial", 60)
        self.small_font: Font = pygame.font.SysFont("arial", 20)
        self.name = get_last_used_name()
        self.name_textbox_focused = False

    def init_screen(self, score):
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.stop()
        pygame.mixer.music.load(self.Components.gameover_music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer_music.play(True)

        self.score = score

    class Components:
        background = pygame.transform.scale(get_image("gameover.png"), (400, 600))
        background_rect = background.get_rect()

        text_box = pygame.Rect(20, 325, 360, 40)
        text_box.center = (200, 345)

        gameover_music = get_music_path("gameover.wav")

    def draw_screen(self):
        self.surface.blit(self.Components.background, (0, 0))

        gameover_label = self.gameover_font.render("Gameover", True, BLACK)
        self.surface.blit(gameover_label, gameover_label.get_rect(center=(200, 220)))

        score_label = self.score_font.render(str(self.score), True, BLACK)
        self.surface.blit(score_label, score_label.get_rect(center=(200, 270)))

        player_name_label = self.small_font.render("Player Name", True, BLACK)
        self.surface.blit(player_name_label, player_name_label.get_rect(center=(100, 310)))

        pygame.draw.rect(self.surface, SELECTED_GREY if self.name_textbox_focused else GREY, self.Components.text_box,
                         border_radius=48)

        player_name_text = self.small_font.render(self.name, True, BLACK)
        self.surface.blit(player_name_text, player_name_text.get_rect(topleft=(35, 335)))

        click_label = self.small_font.render("Click anywhere to go to menu", True, BLACK)
        self.surface.blit(click_label, click_label.get_rect(center=(200, 580)))

    def on_mouse_click(self, pointer_position):

        if self.Components.text_box.collidepoint(pointer_position):
            self.name_textbox_focused = True
        else:
            write_highscore(self.name if len(self.name) > 0 else "Player 1", self.score)
            self.navigation.go_to_menu_screen()

    def on_key_press(self, key, unicode):

        if self.name_textbox_focused:
            if key == pygame.K_BACKSPACE:
                if len(self.name) > 0:
                    self.name = self.name[:-1]
            elif key == pygame.K_RETURN:
                write_highscore(self.name if len(self.name) > 0 else "Player 1", self.score)
                self.navigation.go_to_menu_screen()
            else:
                self.name = self.name + unicode
