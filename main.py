import pygame
import random

# UI STATE
show_menu = True
show_game = False
show_multiplayer_game = False
show_highscore = False






pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 600))
# game name
pygame.display.set_caption("Jogo De Toupeiras")

# create cursor_weapon
image = pygame.image.load("hammer.png").convert_alpha()
#image = pygame. transform. scale(image,1, 2)
weapon = image.get_rect()

# create empty list, then create X obstacle rectangles using a loop and add to list
obstacles = []
for _ in range(5):
    dig = pygame.image.load("obstacle.png").convert_alpha()
    obstacle_rect = dig
    obstacle_rect = dig.get_rect()
    obstacle_rect.topleft = (random.randint(100, 300), random.randint(100, 500))
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

    #shows menu
    if show_menu == True:
        # update background
        DISPLAYSURF.blit(menu_background, (0, 0))

        big_button.draw()
        if start_button.draw():
            print('start')
            show_menu = False
            show_game = True
        if multi_button.draw():
            show_menu = False
            show_game = True
            show_multiplayer_game = True
            print('multi')
        if score_button.draw():
            print('score')

    # check collision and change colour
    #col = GREEN
    if show_game == True:

        DISPLAYSURF.blit(menu_background, (0, 0))

        for obstacle_rect in obstacles:
            DISPLAYSURF.blit(dig, obstacle_rect.topleft)
            #pygame.draw.rect(DISPLAYSURF, obstacle)


        # if weapon.collidelist(obstacles) >= 0 and pygame.mouse.get_pressed(num_buttons=1)[0]:
        if weapon.collidelist(obstacles) >= 0:
            if pygame.mouse.get_pressed()[2]:
                # print("colide")
                #col = RED
                obstacles.pop()

        

    # get mouse coordinates and use them to position the rectangle
    pos = pygame.mouse.get_pos()
    weapon.center = pos

    # draw all rectangles
    # blit the image onto the DISPLAYSURF
    if not show_multiplayer_game:
       DISPLAYSURF.blit(image, weapon.topleft)
   

    events = pygame.event.get()
    
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                show_game = False
                show_multiplayer_game = False
                show_highscore = False
                show_menu = True

        if show_multiplayer_game:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("Tecla 1")
                if event.key == pygame.K_2:
                    print("Tecla 2")
                if event.key == pygame.K_3:
                    print("Tecla 3")
                if event.key == pygame.K_4:
                    print("Tecla 4")
                if event.key == pygame.K_5:
                    print("Tecla 5")
                if event.key == pygame.K_6:
                    print("Tecla 6")
                if event.key == pygame.K_7:
                    print("Tecla 7")
                if event.key == pygame.K_8:
                    print("Tecla 8")
                if event.key == pygame.K_9:
                    print("Tecla 9")
                if event.key == pygame.K_KP1:
                    print("Tecla Numpad 1")
                if event.key == pygame.K_KP2:
                    print("Tecla Numpad 2")
                if event.key == pygame.K_KP3:
                    print("Tecla Numpad 3")
                if event.key == pygame.K_KP4:
                    print("Tecla Numpad 4")
                if event.key == pygame.K_KP5:
                    print("Tecla Numpad 5")
                if event.key == pygame.K_KP6:
                    print("Tecla Numpad 6")
                if event.key == pygame.K_KP7:
                    print("Tecla Numpad 7")
                if event.key == pygame.K_KP8:
                    print("Tecla Numpad 8")
                if event.key == pygame.K_KP9:
                    print("Tecla Numpad 9")
        

    # update display
    pygame.display.update()

pygame.quit()
