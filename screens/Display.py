class Display:
    def __init__(self, show_menu=True, show_singleplayer=False, show_multiplayer=False, show_highscore=False):
        self.show_menu = show_menu
        self.show_singleplayer = show_singleplayer
        self.show_multiplayer = show_multiplayer
        self.show_highscore = show_highscore

    def go_to_menu_screen(self):
        self.show_menu = True
        self.show_singleplayer = False
        self.show_multiplayer = False
        self.show_highscore = False

    def go_to_singleplayer_screen(self):
        self.show_menu = False
        self.show_singleplayer = True
        self.show_multiplayer = False
        self.show_highscore = False
