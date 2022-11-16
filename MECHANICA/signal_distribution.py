import PEOPLE.ANNA
import DIALOG_BUTTONS.buttons


class USERS_SIGNAL:
    def __init__(self):
        self.signal = None
        self.annas_pos = PEOPLE.ANNA.Anna()
        self.buttons = DIALOG_BUTTONS.buttons.BUTTONS()

    def give_signals(self, signal):
        all_sides = ['left', 'right', 'up', 'down']
        self.signal = signal

        self.sides() if signal in all_sides else self.mouse()

    def sides(self):
        self.annas_pos.setting_movement(self.signal)
        self.buttons.find_contact_buttons(self.annas_pos.entity_anna())

    def mouse(self):  # for button
        pass
