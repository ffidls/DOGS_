import PEOPLES.ANNA


class USERS_SIGNAL:
    def __init__(self):
        self.signal = None
        self.annas_pos = PEOPLES.ANNA.Anna()

    def give_signals(self, signal):
        all_sides = ['left', 'right', 'up', 'down']
        self.signal = signal

        self.sides() if signal in all_sides else self.mouse()

    def sides(self):
        self.annas_pos.setting_movement(self.signal)

    def mouse(self):  # for button
        pass
