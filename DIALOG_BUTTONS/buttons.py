import pygame
import DATAS.const
import MECHANICA.Change_locations
import DATAS.write_new_datas
import DATAS.get_datas


def checking_contact(rect_user, rect_button):
    return pygame.Rect.colliderect(rect_button, rect_user)


class BUTTONS:
    def __init__(self):
        self.width, self.height = DATAS.const.WIDTH_BUTTON, DATAS.const.HEIGHT_BUTTON
        self.safe_new_inf = DATAS.write_new_datas
        self.action_for_locations = MECHANICA.Change_locations.LOCATIONS()

    def entity_button(self, pos, for_contact=False):
        if for_contact:
            self.width, self.height = DATAS.const.AREA_WIDTH, DATAS.const.AREA_HEIGHT
        return pygame.Rect(pos[0], pos[1], self.width, self.height)

    def find_contact_buttons(self, entity_user):
        start_pos_lst, name_houses = self.action_for_locations.inf_location(type_inf='people')
        self.action_checking(entity_user, start_pos_lst, name_houses) if name_houses is not None else None

    def action_checking(self, entity_user, start_pos_lst, name_houses):
        pos_contact_button = None
        for possible_pos in start_pos_lst:
            rect_button = self.entity_button(possible_pos)
            if checking_contact(entity_user, rect_button):
                pos_contact_button = possible_pos
                break

        name_house = name_houses[pos_contact_button] if pos_contact_button is not None else None
        self.safe_new_inf.new_inf_for_button(pos_contact_button, name_house)
