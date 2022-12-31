import pygame
import FIRST_PART.DATAS.const


def start_pos_door():
    return [(53, 87), (366, 82), (23, 363), (345, 357)]


def pos_people_house():
    return {(53, 87): 'alina_house', (366, 82): 'neighbor_house',
            (23, 363): 'neighbor_house', (345, 357): 'kira_house'}


def get_all_inf():
    return start_pos_door(), pos_people_house()


def private_place():
    return [(245, 62), (143, 262), (297, 360)]


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
