import pygame
import DIALOG_BUTTONS.mechanic_contact
import DIALOG_BUTTONS.buttons
import DATAS, DATAS.const, DATAS.write_new_datas


def pos_draw_button():
    pos_button = DATAS.get_datas.inf_for_button()[1]
    return pos_button[0], pos_button[1] - DATAS.const.POS_DOORS


class DIALOGS:
    def __init__(self):
        self.setting_button = DIALOG_BUTTONS.buttons.BUTTONS()

    def get_pos(self, mouse_pos):
        if self.checking_contact_with_button(mouse_pos):
            name_dialog = DATAS.get_datas.inf_for_button()[2]
            DATAS.write_new_datas.new_inf_dialog(name_dialog, count=0)

    def checking_contact_with_button(self, mouse_pos):
        button = self.create_entity_button()
        return pygame.Rect.collidepoint(button, mouse_pos)

    def create_entity_button(self):
        pos_entity_button = pos_draw_button()
        return self.setting_button.entity_button(pos_entity_button, for_contact=True)

    def setting(self):
        pass
