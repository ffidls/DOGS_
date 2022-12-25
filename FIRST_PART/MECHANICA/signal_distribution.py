import FIRST_PART.PEOPLE.ANNA
import FIRST_PART.DIALOG_BUTTONS.buttons, FIRST_PART.DIALOG_BUTTONS.mechanic_contact
import FIRST_PART.DOG.brain, FIRST_PART.DOG.independent_move
import FIRST_PART.MECHANICA.control_all_condition


class USERS_SIGNAL:
    def __init__(self):
        self.annas_pos = FIRST_PART.PEOPLE.ANNA.Anna()
        self.buttons = FIRST_PART.DIALOG_BUTTONS.buttons.BUTTONS()
        self.dialog = FIRST_PART.DIALOG_BUTTONS.mechanic_contact.SETTING_CONTACT()
        self.work_condition = FIRST_PART.MECHANICA.control_all_condition.CONTROL()

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
        self.work_condition.write_new_condition(type_condition='run', signal=signal)

    def mouse(self, pos):  # for button
        self.dialog.for_dialogs(pos)
        self.work_condition.write_new_condition(type_condition='move')

    def free_parts(self):
        FIRST_PART.DOG.independent_move.INDEPENDENCE_MOVE()
        self.work_condition.write_new_condition(type_condition='move')
