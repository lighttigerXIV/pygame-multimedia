import pygame
import screens.Navigation as Navigation
from Utils import get_image


pygame.init()
navigation = Navigation.Navigation()

pygame.display.set_caption("Whack A Diglett")

cursor_image = get_image("hammer.png")
weapon = cursor_image.get_rect()
pygame.mouse.set_visible(False)

run = True
while run:

    if navigation.show_menu:
        navigation.menu_screen.draw_screen()

    if navigation.show_tutorial_one:
        navigation.tutorial_one_screen.draw_screen()

    if navigation.show_tutorial_two:
        navigation.tutorial_two_screen.draw_screen()

    if navigation.show_tutorial_three:
        navigation.tutorial_three_screen.draw_screen()

    if navigation.show_singleplayer:
        navigation.singleplayer_screen.draw_screen()

    if navigation.show_multiplayer:
        navigation.multiplayer_screen.draw_screen()

    if navigation.show_gameover:
        navigation.gameover_screen.draw_screen()

    if navigation.show_multiplayer_gameover:
        navigation.multiplayer_gameover_screen.draw_screen()

    if navigation.show_highscores:
        navigation.highscore_screen.draw_screen()

    weapon.center = pygame.mouse.get_pos()

    if not navigation.show_multiplayer:
        navigation.surface.blit(cursor_image, weapon.topleft)

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:

                if navigation.show_singleplayer:
                    navigation.singleplayer_screen.gameover()

                navigation.go_to_menu_screen()

            if navigation.show_gameover:
                navigation.gameover_screen.on_key_press(event.key, event.unicode)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pointer_position = pygame.mouse.get_pos()

            if navigation.show_menu:
                navigation.menu_screen.on_mouse_click(pointer_position)

            elif navigation.show_tutorial_one:
                navigation.tutorial_one_screen.on_mouse_click()

            elif navigation.show_tutorial_two:
                navigation.tutorial_two_screen.on_mouse_click()

            elif navigation.show_tutorial_three:
                navigation.tutorial_three_screen.on_mouse_click()

            elif navigation.show_singleplayer:
                navigation.singleplayer_screen.on_mouse_click(pointer_position)

            elif navigation.show_gameover:
                navigation.gameover_screen.on_mouse_click(pointer_position)

            elif navigation.show_multiplayer_gameover:
                navigation.go_to_menu_screen()

            elif navigation.show_highscores:
                navigation.highscore_screen.on_mouse_click()

        if navigation.show_multiplayer:
            if event.type == pygame.KEYDOWN:
                navigation.multiplayer_screen.on_key_down(event.key)

    pygame.display.update()
    navigation.fps.tick(60)

pygame.quit()
