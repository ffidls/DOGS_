import pygame
import DATAS.const


def start_pos_door():
    return [(189, 349), (18, 349)]


def pos_people_house():
    return {(189, 349): 'anna_house', (18, 349): 'neighbor_house'}


def get_all_inf():
    return start_pos_door(), pos_people_house()


class LOCATION:
    def __init__(self):
        self.width, self.height = DATAS.const.WIDTH_LOCATION_1, DATAS.const.HEIGHT_LOCATION_1
        self.pos_border = DATAS.const.BORDER_NEXT

        self.entity_location = pygame.Rect((0, 0, self.width, self.height))

    def entity(self):
        return [self.entity_location]

    def checking_border(self, entity_Anna):
        next_num_location, new_pos_user = 2, DATAS.const.NEW_POC_NEXT_LOCATION
        entity_border_next = pygame.Rect((self.pos_border[0], self.pos_border[1],
                                          DATAS.const.BORDER_HEIGHT, DATAS.const.BORDER_WIDTH))
        entity_user = pygame.Rect(entity_Anna)
        if pygame.Rect.colliderect(entity_border_next, entity_user):
            return next_num_location, new_pos_user
        return None, None
