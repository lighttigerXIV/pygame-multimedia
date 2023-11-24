import pygame
import random

# UI STATE
show_menu = True
show_highscore = False
show_game = False






pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 600))
# game name
pygame.display.set_caption("Jogo De Toupeiras")

# create cursor_weapon
image = pygame.image.load("mallet.png").convert_alpha()
weapon = image.get_rect()

# create empty list, then create X obstacle rectangles using a loop and add to list
obstacles = []
for _ in range(0):
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
click1 = pygame.image.load("button_single.png").convert_alpha()
click2 = pygame.image.load("button_multiplayer.png").convert_alpha()
click3 = pygame.image.load("button_highscore.png").convert_alpha()
click4 = pygame.image.load("red.png").convert_alpha()
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        state = False
        posa = pygame.mouse.get_pos()

        if self.rect.collidepoint(posa):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                state = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked= False

        DISPLAYSURF.blit(self.image, (self.rect.x, self.rect.y))
        return state


big_button = Button (75, 25, click4)
start_button = Button(100, 275, click1)
multi_button = Button(100, 375, click2)
score_button = Button(100, 475, click3)

run = True
while run:
    # update background
    DISPLAYSURF.blit(menu_background, (0, 0))

    big_button.draw()
    if start_button.draw():
        print('start')
    if multi_button.draw():
        print('multi')
    if score_button.draw():
        print('score')

    # check collision and change colour
    col = GREEN
    
    # if weapon.collidelist(obstacles) >= 0 and pygame.mouse.get_pressed(num_buttons=1)[0]:
    if weapon.collidelist(obstacles) >= 0:
        if pygame.mouse.get_pressed()[0]:
            # print("colide")
            col = RED
            
            #obstacles.pop()

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
