import FIRST_PART.PEOPLE.ANNA
import FIRST_PART.DIALOG_BUTTONS.buttons, FIRST_PART.DIALOG_BUTTONS.mechanic_contact
import FIRST_PART.DOG.brain, FIRST_PART.DOG.independent_move


class USERS_SIGNAL:
    def __init__(self):
        self.annas_pos = FIRST_PART.PEOPLE.ANNA.Anna()
        self.buttons = FIRST_PART.DIALOG_BUTTONS.buttons.BUTTONS()
        self.dialog = FIRST_PART.DIALOG_BUTTONS.mechanic_contact.SETTING_CONTACT()

    def give_signals(self, signal, absence=False):
        all_sides = ['left', 'right', 'up', 'down']

        if not absence:
            self.sides(signal) if signal in all_sides else self.mouse(signal)
        else:
            self.free_parts()

    def sides(self, signal):
        self.annas_pos.setting_movement(signal)
        self.buttons.find_contact_buttons(self.annas_pos.entity_anna())
        FIRST_PART.DOG.brain.MOVE(signal)

    def mouse(self, pos):  # for button
        self.dialog.for_dialogs(pos)

    def free_parts(self):
        FIRST_PART.DOG.independent_move.INDEPENDENCE_MOVE()
