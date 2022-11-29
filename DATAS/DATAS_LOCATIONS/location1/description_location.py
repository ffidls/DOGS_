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
        self.pos_border_next = DATAS.const.BORDER_NEXT

        self.entity_location = pygame.Rect((0, 0, self.width, self.height))

    def entity(self):
        return [self.entity_location]

    def checking_border(self, pos_user):
        next_num_location, new_pos_user = 2, DATAS.const.NEW_POC_NEXT_LOCATION

        if pos_user[1] >= self.pos_border_next[0] and pos_user[0] <= self.pos_border_next[1]:
            return next_num_location, (new_pos_user, pos_user[1])
        return None, None
