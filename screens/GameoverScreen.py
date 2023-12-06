import pygame
from pygame import Surface, SurfaceType
from pygame.font import Font

from Utils import get_image, get_music_path


class GameOverScreen:
    def __init__(self, surface):
        self.score: int = 0
        self.surface: Surface | SurfaceType = surface
        self.gameover_font: Font = pygame.font.SysFont("arial", 40)
        self.score_font: Font = pygame.font.SysFont("arial", 60)
        self.click_to_exit_font: Font = pygame.font.SysFont("arial", 20)

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

        gameover_music = get_music_path("gameover.wav")

    def draw_screen(self):
        self.surface.blit(self.Components.background, (0, 0))

        score_text = self.gameover_font.render("Gameover", True, (0, 0, 0))
        self.surface.blit(score_text, score_text.get_rect(center=(200, 200)))

        score_text = self.score_font.render(str(self.score), True, (0, 0, 0))
        self.surface.blit(score_text, score_text.get_rect(center=(200, 300)))

        click_text = self.click_to_exit_font.render("Click anywhere to go to menu", True, (0, 0, 0))
        self.surface.blit(click_text, click_text.get_rect(center=(200, 550)))
