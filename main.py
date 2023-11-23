import pygame
import random

# UI STATE
show_menu = True
show_highscore = False
show_game = False






pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 800))
# game name
pygame.display.set_caption("Jogo De Toupeiras")

# create cursor_weapon
image = pygame.image.load("mallet.png").convert_alpha()
weapon = image.get_rect()

# create empty list, then create X obstacle rectangles using a loop and add to list
obstacles = []
for _ in range(50):
    obstacle_rect = pygame.Rect(random.randint(
        0, 400), random.randint(0, 600), 25, 25)
    obstacles.append(obstacle_rect)

# define colours

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# hide cursor
pygame.mouse.set_visible(False)

# background

DISPLAYSURF.fill(WHITE)
menu_background = pygame.image.load("menu_background.jpg")
menu_background = pygame.transform.scale(menu_background, (600, 800))

# button class for menu
click1 = pygame.image.load("button.png").convert_alpha()
click2 = pygame.image.load("button2.png").convert_alpha()


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        DISPLAYSURF.blit(self.image, (self.rect.x, self.rect.y))


start_button = Button(100, 200, click1)
multi_button = Button(200, 200, click2)
# score_button = Button(100, 600, button)

run = True
while run:
    # update background
    DISPLAYSURF.blit(menu_background, (0, 0))

    start_button.draw()
    multi_button.draw()
    # score_button.draw()

    # check collision and change colour
    col = GREEN
    # if weapon.collidelist(obstacles) >= 0 and pygame.mouse.get_pressed(num_buttons=1)[0]:
    if weapon.collidelist(obstacles) >= 0 and pygame.mouse.get_pressed()[0]:
        # print("colide")
        col = RED
        # obstacles.pop()

    # get mouse coordinates and use them to position the rectangle
    pos = pygame.mouse.get_pos()
    weapon.center = pos

    # draw all rectangles
    # blit the image onto the DISPLAYSURF
    DISPLAYSURF.blit(image, weapon.topleft)
    for obstacle in obstacles:
        pygame.draw.rect(DISPLAYSURF, col, obstacle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

pygame.quit()
