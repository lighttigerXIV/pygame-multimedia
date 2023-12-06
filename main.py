import pygame
import screens.Display as Display
from Utils import get_image


pygame.init()
display = Display.Display()

pygame.display.set_caption("Whack A Diglett")

cursor_image = get_image("hammer.png")
weapon = cursor_image.get_rect()
pygame.mouse.set_visible(False)

run = True
while run:

    if display.show_menu:
        display.menu_screen.draw_screen()

    if display.show_tutorial_one:
        display.tutorial_one_screen.draw_screen()

    if display.show_singleplayer:
        display.singleplayer_screen.draw_screen()

    if display.show_gameover:
        display.gameover_screen.draw_screen()

    weapon.center = pygame.mouse.get_pos()

    if not display.show_multiplayer:
        display.surface.blit(cursor_image, weapon.topleft)

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:

                if display.show_singleplayer:
                    display.singleplayer_screen.gameover()

                display.go_to_menu_screen()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pointer_position = pygame.mouse.get_pos()

            if display.show_menu:
                display.menu_screen.on_mouse_click(pointer_position)

            elif display.show_tutorial_one:
                display.tutorial_one_screen.on_mouse_click()

            elif display.show_singleplayer:
                display.singleplayer_screen.on_mouse_click(pointer_position)

            elif display.show_gameover:
                display.go_to_menu_screen()

        if display.show_multiplayer:
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

    pygame.display.update()
    display.fps.tick(60)

pygame.quit()
