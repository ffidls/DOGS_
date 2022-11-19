import pygame
import DATAS.const


class LOCATION_2:
    def __init__(self):
        self.width, self.height = DATAS.const.WIDTH_LOCATION_2, DATAS.const.HEIGHT_LOCATION_2

        self.entity_location = pygame.Rect((0, 0, self.width, self.height))

    def entity(self):
        return self.entity_location
