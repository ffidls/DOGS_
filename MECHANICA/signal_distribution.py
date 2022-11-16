import PEOPLE.ANNA
import DIALOG_BUTTONS.buttons, DIALOG_BUTTONS.mechanic_contact


class USERS_SIGNAL:
    def __init__(self):
        self.signal = None
        self.annas_pos = PEOPLE.ANNA.Anna()
        self.buttons = DIALOG_BUTTONS.buttons.BUTTONS()
        self.dialog = DIALOG_BUTTONS.mechanic_contact.SETTING_CONTACT()

    def give_signals(self, signal):
        all_sides = ['left', 'right', 'up', 'down']
        self.signal = signal

        self.sides() if signal in all_sides else self.mouse(signal)

    def sides(self):
        self.annas_pos.setting_movement(self.signal)
        self.buttons.find_contact_buttons(self.annas_pos.entity_anna())

    def mouse(self, pos):  # for button
        self.dialog.for_dialogs(pos)
