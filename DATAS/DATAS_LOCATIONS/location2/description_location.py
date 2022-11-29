import pygame
import DATAS.const


def start_pos_door():
    return None


def pos_people_house():
    return None


def get_all_inf():
    return start_pos_door(), pos_people_house()


class LOCATION:  # 2 LOCATION
    def __init__(self):
        self.width, self.height = DATAS.const.WIDTH_LOCATION_2, DATAS.const.HEIGHT_LOCATION_2
        self.pos_border_next = DATAS.const.BORDER_NEXT
        self.pos_border_ago = DATAS.const.BORDER_AGO

        self.new_pos_ago, self.new_pos_next = DATAS.const.NEW_POC_AGO_LOCATION, DATAS.const.NEW_POC_NEXT_LOCATION

        self.entity_location = pygame.Rect((0, 0, self.width, self.height))

    def entity(self):
        return [self.entity_location]

    def checking_border(self, pos_user):
        if pos_user[0] >= self.pos_border_next[0] and pos_user[1] == self.pos_border_next[1]:
            next_num_location, new_pos_user = 3, (self.new_pos_next, pos_user[1])
            return next_num_location, new_pos_user
        elif pos_user[1] >= self.pos_border_ago[0] and pos_user[0] == self.pos_border_ago[1]:
            next_num_location, new_pos_user = 1, (self.new_pos_ago, pos_user[1])
            return next_num_location, new_pos_user

        return None, None
