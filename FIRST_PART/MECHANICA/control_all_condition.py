import FIRST_PART.DATAS.get_datas, FIRST_PART.DATAS.write_new_datas
import FIRST_PART.PEOPLE.KIRA
import FIRST_PART.DATAS.get_datas


def get_condition():
    return FIRST_PART.DATAS.get_datas.get_condition_anna()


class CONTROL:
    def __init__(self):
        self.write_data, self.get_data = FIRST_PART.DATAS.write_new_datas, FIRST_PART.DATAS.get_datas
        self.data_kira = FIRST_PART.PEOPLE.KIRA.CONTROL_MOVE()

    def write_new_condition(self, type_condition, signal=None):
        self.write_data.new_condition_anna(type_condition)
        if signal is not None:
            self.write_data.new_side_user(signal)

    def condition_dialogs(self):
        type_dialog = FIRST_PART.DATAS.get_datas.get_data_dialog()[0]
        self.data_kira.sorter_dialog(type_dialog)

