import os.path
import pandas as pd
import pygame

from pandas import DataFrame
from pygame import SurfaceType, Surface
from pygame.font import Font

from Constants import WHITE
from Utils import get_image, get_music_path
from screens import Navigation


def get_highscores() -> DataFrame:
    if not os.path.exists("highscores.csv"):
        return DataFrame(columns=["name", "score", "last_modified"])

    scores_df = pd.read_csv("highscores.csv")

    if len(scores_df.index) == 0:
        return DataFrame(columns=["name", "score", "last_modified"])

    return scores_df.sort_values(by="score", ascending=False)


class HighscoresScreen:
    def __init__(self, navigation, surface):
        self.highscores_df: DataFrame = get_highscores()
        self.navigation: Navigation = navigation
        self.surface: Surface | SurfaceType = surface
        self.font: Font = pygame.font.SysFont("Arial", 20)

    def init_screen(self):
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.stop()
        pygame.mixer.music.load(self.Components.highscores_music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer_music.play(True)

        self.highscores_df = get_highscores()

    class Components:
        background = get_image("score_background.png")
        highscores_music = get_music_path("highscore.wav")

    def draw_screen(self):
        self.surface.blit(self.Components.background, (0, 0))

        score_y_position = 160

        for index, row in self.highscores_df[0:8].iterrows():
            name_text = self.font.render(row["name"], True, WHITE)
            self.surface.blit(name_text, name_text.get_rect(topleft=(70, score_y_position)))

            score_text = self.font.render(str(row["score"]), True, WHITE)
            self.surface.blit(score_text, score_text.get_rect(topright=(330, score_y_position)))
            score_y_position += 30

    def on_mouse_click(self):
        self.navigation.go_to_menu_screen()
