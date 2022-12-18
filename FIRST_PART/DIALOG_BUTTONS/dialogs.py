import pygame
import FIRST_PART.DIALOG_BUTTONS.mechanic_contact
import FIRST_PART.DIALOG_BUTTONS.buttons
import FIRST_PART.DATAS, FIRST_PART.DATAS.const, FIRST_PART.DATAS.write_new_datas, FIRST_PART.DATAS.get_datas


def pos_draw_button():
    pos_button = FIRST_PART.DATAS.get_datas.inf_for_button()[1]
    return pos_button[0], pos_button[1] - FIRST_PART.DATAS.const.POS_DOORS


class DIALOGS:
    def __init__(self):
        self.setting_button = FIRST_PART.DIALOG_BUTTONS.buttons.BUTTONS()

    def get_pos(self, mouse_pos):
        if self.checking_contact_with_button(mouse_pos):
            name_dialog = FIRST_PART.DATAS.get_datas.inf_for_button()[2]
            FIRST_PART.DATAS.write_new_datas.new_inf_dialog(name_dialog, count=1)

    def checking_contact_with_button(self, mouse_pos):
        button = self.create_entity_button()
        return pygame.Rect.collidepoint(button, mouse_pos)

    def create_entity_button(self):
        pos_entity_button = pos_draw_button()
        return self.setting_button.entity_button(pos_entity_button, for_contact=True)

    def setting(self, mouse_pos):
        datas = FIRST_PART.DATAS.get_datas.get_data_dialog()
        name_dialog, count_phrase = datas[0], int(datas[1])

        if name_dialog != 'None':
            all_phrase = int(FIRST_PART.DATAS.get_datas.get_dialog_phrase(name_dialog, 0)[0])
            new_datas = [name_dialog, count_phrase + 1] if all_phrase > count_phrase else [None, 0]
            FIRST_PART.DATAS.write_new_datas.new_inf_dialog(new_datas[0], new_datas[1])
        else:
            self.get_pos(mouse_pos)
