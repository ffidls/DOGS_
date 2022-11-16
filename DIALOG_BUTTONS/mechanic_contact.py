import DIALOG_BUTTONS.buttons
import DATAS.get_datas, DATAS.const


class SETTING_CONTACT:
    def __init__(self):
        self.setting_buttons = DIALOG_BUTTONS.buttons.BUTTONS()

        self.pos_draw = DATAS.const.POS_DOORS

    def distribution_mouse(self):  # for mouse
        pass

    def setting_for_draw_button(self):
        pos_button = DATAS.get_datas.inf_for_button()[1]
        return pos_button[0], pos_button[1] - self.pos_draw
