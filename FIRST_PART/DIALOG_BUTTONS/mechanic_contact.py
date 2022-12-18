import FIRST_PART.DIALOG_BUTTONS.buttons, FIRST_PART.DIALOG_BUTTONS.dialogs
import FIRST_PART.DATAS.get_datas, FIRST_PART.DATAS.const


class SETTING_CONTACT:
    def __init__(self):
        self.dialogs = FIRST_PART.DIALOG_BUTTONS.dialogs.DIALOGS()
        self.pos_draw = FIRST_PART.DATAS.const.POS_DOORS

    def distribution_mouse(self):  # for mouse
        pass

    def setting_for_draw_button(self):
        pos_button = FIRST_PART.DATAS.get_datas.inf_for_button()[1]
        return pos_button[0], pos_button[1] - self.pos_draw

    def for_dialogs(self, pos):
        check_contact_button = FIRST_PART.DATAS.get_datas.inf_for_button()[0]
        self.dialogs.setting(pos) if check_contact_button else None

    def datas_from_draw_dialog(self):
        name_dialog, count_phrase = FIRST_PART.DATAS.get_datas.get_data_dialog()
        if name_dialog != 'None':
            return FIRST_PART.DATAS.get_datas.get_dialog_phrase(name_dialog, count_phrase)
        return None
