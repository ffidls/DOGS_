import DOG.brain


class MOVE:
    def __init__(self, side_user, type_move):
        missing_pos = self.missing_pos_zona(side_user) if type_move == 'zona' else self.missing_pos_place()

    def missing_pos_zona(self, side):
        border_pos_zona = DOG.brain.get_pos_zona(side)

    def missing_pos_place(self):
        pass
