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


class LOCATION:  # 4 LOCATION
    def __init__(self):
        # self.width, self.height = FIRST_PART.DATAS.const.WIDTH_LOCATION_2, FIRST_PART.DATAS.const.HEIGHT_LOCATION_2
        self.pos_side_x = FIRST_PART.DATAS.const.BORDER_SIDE_X
        self.pos_side_y = FIRST_PART.DATAS.const.BORDER_SIDE_Y

        self.new_pos_ago = FIRST_PART.DATAS.const.NEW_POC_AGO_LOCATION
        self.entity_houses = FIRST_PART.DATAS.const.ENTITY_LOCATION_4

    def entity(self):
        entity = []
        for datas in self.entity_houses:
            entity.append(pygame.Rect(datas[0], datas[1], datas[2], datas[3]))
        return entity

    def checking_border(self, pos_user):
        if pos_user[1] >= 457 and pos_user[0] >= 80:
            next_num_location, new_pos_user = 3, (260, 55)
            return next_num_location, new_pos_user

        return None, None
