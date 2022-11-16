import DIALOG_BUTTONS.buttons, DIALOG_BUTTONS.dialogs
import DATAS.get_datas, DATAS.const


class SETTING_CONTACT:
    def __init__(self):
        self.setting_buttons = DIALOG_BUTTONS.buttons.BUTTONS()
        self.dialogs = DIALOG_BUTTONS.dialogs.DIALOGS()

        self.pos_draw = DATAS.const.POS_DOORS

    def distribution_mouse(self):  # for mouse
        pass

    def setting_for_draw_button(self):
        pos_button = DATAS.get_datas.inf_for_button()[1]
        return pos_button[0], pos_button[1] - self.pos_draw

    def for_dialogs(self, pos):
        check_contact_button = DATAS.get_datas.inf_for_button()[0]
        self.dialogs.get_pos(pos) if check_contact_button else None
