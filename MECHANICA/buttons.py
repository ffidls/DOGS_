import pygame
import DATAS.const
import DATAS.location.description_location_1
import DATAS.get_datas


def checking_contact(rect_user, rect_button):
    return pygame.Rect.colliderect(rect_button, rect_user)


def new_inf_for_buttons(pos):
    pass


class BUTTONS:
    def __init__(self):
        self.width, self.height = DATAS.const.WIDTH_BUTTON, DATAS.const.HEIGHT_BUTTON
        self.start_pos_lst = DATAS.location.description_location_1.start_pos_door()

    def entity_button(self, pos):
        return pos[1], pos[2], self.width, self.height

    def find_contact_buttons(self, entity_user):
        pos_contact_button = None
        for possible_pos in self.start_pos_lst:
            pos_contact_button = possible_pos if checking_contact(entity_user, possible_pos) else None

        new_inf_for_buttons(pos_contact_button)
        return pos_contact_button
