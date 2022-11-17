import pygame
import DATAS.const


def start_pos_door():
    return [(189, 349), (18, 349)]


def pos_people_house():
    return {(189, 349): 'anna_house', (18, 349): 'neighbor_house'}


class LOCATION_1:
    def __init__(self):
        self.width, self.height = DATAS.const.WIDTH_LOCATION_1, DATAS.const.HEIGHT_LOCATION_1

        self.entity_location = pygame.Rect((0, 0, self.width, self.height))

    def entity(self):
        return self.entity_location
