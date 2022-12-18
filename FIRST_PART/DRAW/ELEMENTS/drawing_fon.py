import pygame
import FIRST_PART.DATAS.get_datas, FIRST_PART.DATAS.const


def png_fon():
    num_location = FIRST_PART.DATAS.get_datas.get_count_location()
    return FIRST_PART.DATAS.get_datas.locations(num_location)


class FON:
    def __init__(self):
        self.width, self.height = FIRST_PART.DATAS.const.WIDTH, FIRST_PART.DATAS.const.HEIGHT

    def draw_fon(self, SCREEN):
        background = pygame.image.load(png_fon())
        SCREEN.blit(background, (0, 0))
