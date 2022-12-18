import pygame, sys
from pygame.locals import *
import FIRST_PART.DRAW.all_drawing
import FIRST_PART.MECHANICA.signal_distribution
import FIRST_PART.DATAS

all_const = FIRST_PART.DATAS.const


def main():
    pygame.init()

    global all_const

    ####################
    SCREEN = pygame.display.set_mode((all_const.WIDTH, all_const.HEIGHT), 0, 32)

    draw_game = FIRST_PART.DRAW.all_drawing.DRAW_MOVING_AND_FON(SCREEN)
    accept_signals_user = FIRST_PART.MECHANICA.signal_distribution.USERS_SIGNAL()
    ###################

    while True:
        pygame.time.Clock().tick(all_const.FPS)  # Частота обновления экрана

        for event in pygame.event.get():

            if event.type == QUIT:
                # Тип проверяемого события НАЖАТ Х В ОКНЕ ИГРЫ
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                # ESC key pressed
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                accept_signals_user.give_signals(pygame.mouse.get_pos())

        #################
        # MOVING GAME
        keys = pygame.key.get_pressed()
        side = None

        if keys[pygame.K_LEFT]:
            side = 'left'
        if keys[pygame.K_RIGHT]:
            side = 'right'
        if keys[pygame.K_UP]:
            side = 'up'
        if keys[pygame.K_DOWN]:
            side = 'down'

        accept_signals_user.give_signals(side) if side is not None \
            else accept_signals_user.give_signals(side, absence=True)
        #################

        draw_game.processor()

        pygame.display.update()


if __name__ == "__main__":
    main()
