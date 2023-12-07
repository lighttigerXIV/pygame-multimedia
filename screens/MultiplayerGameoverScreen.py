import pygame
from pygame import Surface, SurfaceType
from pygame.font import Font

from Utils import get_image, get_music_path
from Constants import BLACK


class MultiPlayerGameOverScreen:
    def __init__(self, surface):
        self.first_player_score: int = 0
        self.second_player_score: int = 0
        self.surface: Surface | SurfaceType = surface
        self.gameover_font: Font = pygame.font.SysFont("arial", 40)
        self.score_font: Font = pygame.font.SysFont("arial", 60)
        self.small_font: Font = pygame.font.SysFont("arial", 20)

    def init_screen(self, first_player_score, second_player_score):
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.stop()
        pygame.mixer.music.load(self.Components.gameover_music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer_music.play(True)

        self.first_player_score = first_player_score
        self.second_player_score = second_player_score

    class Components:
        background = pygame.transform.scale(get_image("gameover.png"), (400, 600))
        background_rect = background.get_rect()

        gameover_music = get_music_path("gameover.wav")

    def draw_screen(self):
        self.surface.blit(self.Components.background, (0, 0))

        gameover_text = self.gameover_font.render("Gameover", True, BLACK)
        self.surface.blit(gameover_text, gameover_text.get_rect(center=(200, 200)))

        first_player_text = self.small_font.render("Player 1", True, BLACK)
        self.surface.blit(first_player_text, first_player_text.get_rect(center=(100, 250)))

        second_player_text = self.small_font.render("Player 2", True, BLACK)
        self.surface.blit(second_player_text, second_player_text.get_rect(center=(300, 250)))

        first_player_score_text = self.score_font.render(str(self.first_player_score), True, BLACK)
        self.surface.blit(first_player_score_text, first_player_score_text.get_rect(center=(100, 300)))

        second_player_score_text = self.score_font.render(str(self.second_player_score), True, BLACK)
        self.surface.blit(second_player_score_text, second_player_score_text.get_rect(center=(300, 300)))

        click_text = self.small_font.render("Click anywhere to go to menu", True, BLACK)
        self.surface.blit(click_text, click_text.get_rect(center=(200, 550)))
