import pygame
import DATAS.get_datas, DATAS.const


def png_fon():
    num_location = DATAS.get_datas.get_count_location()
    return DATAS.get_datas.locations(num_location)


class FON:
    def __init__(self):
        self.width, self.height = DATAS.const.WIDTH, DATAS.const.HEIGHT

    def draw_fon(self, SCREEN):
        background = pygame.image.load(png_fon())
        SCREEN.blit(background, (0, 0))
