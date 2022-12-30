import pygame
import FIRST_PART.DATAS.const


def start_pos_door():
    return [(55, 366), (277, 87)]


def pos_people_house():
    return {(55, 366): 'neighbor_house', (277, 87): 'neighbor_house'}


def get_all_inf():
    return start_pos_door(), pos_people_house()


def private_place():
    return [(466, 31), (27, 159), (29, 288), (460, 473)]


class LOCATION:  # 3 LOCATION
    def __init__(self):
        self.width, self.height = FIRST_PART.DATAS.const.WIDTH_LOCATION_2, FIRST_PART.DATAS.const.HEIGHT_LOCATION_2
        self.pos_border_ago = FIRST_PART.DATAS.const.BORDER_AGO
        self.pos_border_x = FIRST_PART.DATAS.const.BORDER_SIDE_X

        self.new_pos_ago = FIRST_PART.DATAS.const.NEW_POC_AGO_LOCATION
        self.new_pos_left = FIRST_PART.DATAS.const.NEW_POS_LEFT_LOCATION
        self.entity_houses = FIRST_PART.DATAS.const.ENTITY_LOCATION_3

    def entity(self):
        entity = []
        for datas in self.entity_houses:
            entity.append(pygame.Rect(datas[0], datas[1], datas[2], datas[3]))
        return entity

    def checking_border(self, pos_user):
        if pos_user[1] >= self.pos_border_ago[0] and pos_user[0] >= self.pos_border_ago[1]:
            next_num_location, new_pos_user = 2, (self.new_pos_ago, pos_user[1])
            return next_num_location, new_pos_user

        if pos_user[1] <= 15:
            next_num_location, new_pos_user = 4, (197, 456)
            return next_num_location, new_pos_user
        return None, None
