import pygame
import os
import pandas as pd
import time
from pygame import Surface, SurfaceType
from pygame.mixer import Sound

from Constants import IMAGES_DIRECTORY, SFX_DIRECTORY, MUSIC_DIRECTORY


def get_image(name: str) -> Surface | SurfaceType:
    return pygame.image.load(f"{IMAGES_DIRECTORY}/{name}")


def get_sfx(name: str) -> Sound:
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    return pygame.mixer.Sound(f"{SFX_DIRECTORY}/{name}")


def get_music_path(name: str) -> str:
    return f"{MUSIC_DIRECTORY}/{name}"


def write_highscore(player_name: str, score: int):
    if not os.path.exists("highscores.csv"):
        scores_df = pd.DataFrame(columns=["name", "score", "last_modified"])
        scores_df.to_csv("highscores.csv", index=False)

    scores_df = pd.read_csv("highscores.csv")
    player_index = -1

    for index, row in scores_df.iterrows():
        if row["name"] == player_name:
            player_index = index

    if player_index == -1:
        scores_df.loc[len(scores_df.index)] = [player_name, score, time.time()]
        scores_df.to_csv("highscores.csv", index=False)
    else:
        if score > scores_df.loc[player_index]["score"]:
            scores_df.loc[player_index, ["score"]] = [score]

        scores_df.loc[player_index, ["last_modified"]] = [time.time()]
        scores_df.to_csv("highscores.csv", index=False)


def get_last_used_name() -> str:
    if not os.path.exists("highscores.csv"):
        return "Player 1"

    scores_df = pd.read_csv("highscores.csv")

    if len(scores_df.index) == 0:
        return "Player 1"

    last_modified = 0
    last_index = -1

    for index, row in scores_df.iterrows():
        if row["last_modified"] > last_modified:
            last_modified = row["last_modified"]
            last_index = index

    if last_modified == -1:
        return "Player 1"

    return scores_df.loc[last_index]["name"]
